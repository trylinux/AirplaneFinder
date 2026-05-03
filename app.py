"""Flask application – Aircraft Finder.

Features:
  - Flask-Login session auth for the web admin panel
  - Bearer-token (API key) auth for the JSON REST API
  - Role-based access: admin, manager, viewer
  - Scoped CRUD: users see only their assigned museums/countries
  - Full CRUD on aircraft, museums, and exhibit links
  - Public read-only search + proximity endpoints
  - International museum support (optional coordinates)
  - Structured logging: auth, changes, access
"""

import csv
import io
import json
import re
import secrets
from datetime import datetime, timedelta, timezone
from functools import wraps
from urllib.parse import urlparse, urljoin

from flask import (
    Flask, render_template, request, jsonify,
    redirect, url_for, flash, abort, g, session,
)
from flask_login import (
    LoginManager, login_user, logout_user,
    login_required, current_user,
)
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from sqlalchemy import or_, func
from sqlalchemy.orm import joinedload, selectinload

from models import (
    db, User, ApiKey,
    Museum, Aircraft, AircraftAlias, AircraftMuseum, ZipCode, haversine,
    UserMuseumAssignment, UserCountryAssignment,
    AircraftTemplate, AircraftTemplateAlias,
)
from geocoder import resolve_location
from config import Config
from logger import auth_log, change_log, access_log


# ══════════════════════════════════════════════
# App factory
# ══════════════════════════════════════════════

class _BearerAwareCSRF(CSRFProtect):
    """CSRF protection that skips validation for requests authenticated via
    Authorization: Bearer header.

    Bearer-token auth is not vulnerable to CSRF because browsers do not attach
    the header automatically — possession of the token IS the authorization.
    Session (cookie) requests still go through the full CSRF flow; session AJAX
    from the admin UI includes the X-CSRFToken header set in base.html.

    The previous implementation mutated the view function's ``__dict__`` to mark
    it exempt after the first Bearer request, which leaked that exemption to
    every subsequent caller — including unauthenticated ones.
    """

    def protect(self):
        if request.headers.get("Authorization", "").startswith("Bearer "):
            return
        return super().protect()


csrf = _BearerAwareCSRF()
limiter = Limiter(key_func=get_remote_address, default_limits=[])


_DEFAULT_SECRET_KEY = "change-me-in-production"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Refuse to boot in production with the placeholder SECRET_KEY. Sessions
    # are signed with this key — a known value means anyone can forge a
    # session cookie and impersonate any user.
    if Config.SECRET_KEY == _DEFAULT_SECRET_KEY:
        if not Config.SERVER_DEBUG:
            raise RuntimeError(
                "SECRET_KEY is the default placeholder. Set the SECRET_KEY env var "
                "(or [app] secret_key in web.config) before running outside debug mode."
            )
        # Dev mode: still loud about it.
        import logging as _logging
        _logging.warning("SECRET_KEY is the default placeholder. OK in debug, never in prod.")

    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    @app.errorhandler(CSRFError)
    def _handle_csrf_error(e):
        return jsonify({"error": "CSRF validation failed. Reload the page and try again."}), 400

    login_manager = LoginManager()
    login_manager.login_view = "login_page"
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


app = create_app()


# ══════════════════════════════════════════════
# Request logging middleware
# ══════════════════════════════════════════════

@app.before_request
def _log_request():
    """Stash request start time; identify user for logging."""
    g.request_start = datetime.now(timezone.utc)
    g.log_user = "anonymous"
    if current_user.is_authenticated:
        g.log_user = current_user.username


@app.after_request
def _log_response(response):
    """Log every request to the appropriate log file."""
    user = getattr(g, "log_user", "anonymous")
    method = request.method
    path = request.path
    status = response.status_code
    ip = request.remote_addr

    line = f"{ip} {user} {method} {path} → {status}"

    if method == "GET":
        access_log.info(line)
    elif method in ("POST", "PUT", "PATCH", "DELETE"):
        change_log.info(line)

    return response


# ══════════════════════════════════════════════
# Session timeout
# ══════════════════════════════════════════════

# Endpoints that must keep working even when an idle session has just been
# timed out — otherwise we can't render the login page or process the logout.
_TIMEOUT_EXEMPT_ENDPOINTS = {
    "login_page", "logout", "register_page", "static",
    "desktop_only_page",
}


def _idle_timeout_for(user):
    """Idle-timeout in seconds for ``user``'s role."""
    if user.is_admin:
        return Config.SESSION_IDLE_TIMEOUT_ADMIN
    if user.is_manager:
        return Config.SESSION_IDLE_TIMEOUT_MANAGER
    return Config.SESSION_IDLE_TIMEOUT_VIEWER


def _full_logout():
    """Tear the session down completely AND make sure the remember-me cookie
    actually gets cleared on the response.

    Naive version is broken: ``logout_user(); session.clear()`` wipes the
    ``_remember = 'clear'`` flag that Flask-Login sets to signal cookie
    deletion, so the long-lived remember cookie survives and on the very
    next request Flask-Login auto-re-authenticates the user. (We hit this
    on the explicit /logout route AND on the timeout middleware — both
    routes need the same dance.)

    We capture _remember and _remember_seconds before the clear and put
    them back, so Flask-Login's response handler can still issue the
    expiring Set-Cookie header.
    """
    logout_user()
    remember_signal  = session.get("_remember")
    remember_seconds = session.get("_remember_seconds")
    session.clear()
    if remember_signal is not None:
        session["_remember"] = remember_signal
    if remember_seconds is not None:
        session["_remember_seconds"] = remember_seconds


@app.before_request
def _enforce_session_timeout():
    """Log out an authenticated user whose session is idle or too old.

    Called on every request. Two conditions can trigger logout:
      - Idle:     more than ``role idle timeout`` since the last activity.
      - Absolute: more than SESSION_ABSOLUTE_TIMEOUT since login_time.
    Either condition flashes a message and redirects to /login. We update
    last_activity at the END of this hook so each request resets the idle
    timer (even unauthenticated ones — harmless).
    """
    # Skip for endpoints that need to work even when the session just expired
    # (login page, logout endpoint, static files, the desktop-only page).
    if request.endpoint in _TIMEOUT_EXEMPT_ENDPOINTS:
        return None

    if not current_user.is_authenticated:
        # Anonymous: just refresh last_activity so any subsequent login starts
        # with a clean clock; nothing to enforce.
        session["last_activity"] = datetime.now(timezone.utc).isoformat()
        return None

    now = datetime.now(timezone.utc)
    login_time_iso = session.get("login_time")
    last_activity_iso = session.get("last_activity")

    # Defensive: if either value is missing (e.g. the user is on a session
    # cookie issued before this code shipped), seed both and continue.
    if not login_time_iso or not last_activity_iso:
        session["login_time"] = now.isoformat()
        session["last_activity"] = now.isoformat()
        return None

    login_time = datetime.fromisoformat(login_time_iso)
    last_activity = datetime.fromisoformat(last_activity_iso)

    # Absolute timeout: from login, regardless of activity.
    if (now - login_time).total_seconds() > Config.SESSION_ABSOLUTE_TIMEOUT:
        username = current_user.username
        _full_logout()
        auth_log.info(f"SESSION_TIMEOUT_ABSOLUTE user={username} ip={request.remote_addr}")
        flash("Your session has expired. Please sign in again.", "warning")
        return redirect(url_for("login_page"))

    # Idle timeout: per-role.
    idle_limit = _idle_timeout_for(current_user)
    if (now - last_activity).total_seconds() > idle_limit:
        username = current_user.username
        _full_logout()
        auth_log.info(f"SESSION_TIMEOUT_IDLE user={username} ip={request.remote_addr}")
        flash("You have been signed out due to inactivity.", "warning")
        return redirect(url_for("login_page"))

    # Activity recorded — bump the idle clock.
    session["last_activity"] = now.isoformat()
    return None


# ══════════════════════════════════════════════
# Password policy
# ══════════════════════════════════════════════

def _validate_password_strength(password):
    """Validate ``password`` against the configured policy.

    Returns ``None`` if valid; otherwise returns a human-readable error
    string suitable for showing to the user.
    """
    if password is None:
        return "Password is required."
    if len(password) < Config.PASSWORD_MIN_LENGTH:
        return f"Password must be at least {Config.PASSWORD_MIN_LENGTH} characters."
    if Config.PASSWORD_REQUIRE_MIXED:
        has_letter = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)
        if not (has_letter and has_digit):
            return "Password must contain at least one letter and one digit."
    return None


# ══════════════════════════════════════════════
# Security headers + safe-redirect helper
# ══════════════════════════════════════════════

# Per-request CSP nonce. Generated in _generate_csp_nonce (before_request)
# and exposed to templates via the _csp_nonce context processor. Inline
# <script nonce="{{ csp_nonce }}"> tags execute; anything injected via XSS
# will not have the nonce and will be blocked by the browser.


def _build_csp(nonce):
    """Construct the Content-Security-Policy header value for THIS request.

    Built per-request because the script-src directive embeds a fresh nonce
    each time. The other directives are static.

    Notes on the rules:
      default-src 'self'              only load resources from our origin
                                      unless explicitly allowed below
      script-src                      our origin + cdnjs (jQuery, Three.js,
                                      Font Awesome) + a per-request nonce
                                      that legitimate inline <script> tags
                                      carry. NO 'unsafe-inline' — that's the
                                      whole point of the nonce.
      style-src                       still has 'unsafe-inline' because the
                                      templates have many inline `style=`
                                      attributes and inline <style> blocks.
                                      Lower XSS risk than script.
      font-src                        Google Fonts and Font Awesome.
      img-src 'self' data: https:     museum/site images from any HTTPS origin.
      connect-src                     'self' + jsDelivr (world-borders GeoJSON).
                                      Tight allowlist — not 'https:' — so an
                                      XSS payload can't exfiltrate to any host.
      frame-ancestors 'none'          no one can iframe us (clickjacking).
      base-uri 'self'                 block <base href="evil"> tricks.
      form-action 'self'              POSTs only go to us.
      object-src 'none'               <object>/<embed> are blocked entirely.
    """
    return (
        f"default-src 'self'; "
        f"script-src 'nonce-{nonce}' 'self' https://cdnjs.cloudflare.com; "
        f"style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://fonts.googleapis.com; "
        f"font-src 'self' https://cdnjs.cloudflare.com https://fonts.gstatic.com data:; "
        f"img-src 'self' data: https:; "
        f"connect-src 'self' https://cdn.jsdelivr.net; "
        f"frame-ancestors 'none'; "
        f"base-uri 'self'; "
        f"form-action 'self'; "
        f"object-src 'none'"
    )


@app.before_request
def _generate_csp_nonce():
    """Mint a fresh nonce per request. Stored on flask.g so the after_request
    handler and the template context processor see the same value within
    one request lifecycle. 16 bytes = 128 bits of entropy, base64 url-safe.
    """
    g.csp_nonce = secrets.token_urlsafe(16)


@app.context_processor
def _csp_nonce():
    """Expose ``csp_nonce`` to every Jinja template — used as
    ``<script nonce="{{ csp_nonce }}">`` on every legitimate inline script."""
    return {"csp_nonce": getattr(g, "csp_nonce", "")}


@app.after_request
def _add_security_headers(response):
    """Apply standard security response headers.

    All gated by SECURITY_HEADERS_ENABLED so local HTTP dev isn't disrupted
    (HSTS over HTTP is wasted; some browsers also bicker about it).
    """
    if not Config.SECURITY_HEADERS_ENABLED:
        return response

    # Don't ever let the page be framed (clickjacking + UI-redress attacks).
    response.headers.setdefault("X-Frame-Options", "DENY")
    # Defense against MIME-type sniffing.
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    # Don't leak full URLs as Referer to third-party origins.
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    # Block APIs we don't use; tightens the surface against compromised JS.
    response.headers.setdefault(
        "Permissions-Policy",
        "geolocation=(), camera=(), microphone=(), payment=(), usb=()",
    )
    # CSP is per-request — the script-src directive embeds the nonce so
    # legitimate inline <script> blocks can execute while injected ones can't.
    response.headers.setdefault(
        "Content-Security-Policy",
        _build_csp(getattr(g, "csp_nonce", "")),
    )

    # HSTS only makes sense on a secure connection. Set max-age 6 months,
    # preload-eligible. Trust X-Forwarded-Proto if a reverse proxy is
    # terminating TLS in front of us.
    is_secure = request.is_secure or (
        request.headers.get("X-Forwarded-Proto", "").lower() == "https"
    )
    if is_secure:
        response.headers.setdefault(
            "Strict-Transport-Security",
            "max-age=15552000; includeSubDomains",
        )
    return response


def _safe_next_url(target):
    """Return ``target`` if it's a same-origin URL, else None.

    Mitigates open-redirect via ``?next=https://evil.com``. Allows relative
    paths (most common case) and absolute URLs whose netloc matches this
    request's host. Anything else gets dropped — caller falls back to a
    safe default.
    """
    if not target:
        return None
    # urljoin resolves a relative target against the current URL; absolute
    # targets pass through unchanged. urlparse then lets us inspect them.
    test_url = urlparse(urljoin(request.host_url, target))
    ref_url = urlparse(request.host_url)
    same_scheme = test_url.scheme in ("http", "https")
    same_host = test_url.netloc == ref_url.netloc
    if same_scheme and same_host:
        # Return the original (so a caller-supplied relative URL stays
        # relative when redirected — preserves clean URLs).
        return target
    return None


# ══════════════════════════════════════════════
# Mobile dispatch
# ══════════════════════════════════════════════

# A small regex covering the User-Agent strings of phones and small tablets.
# Intentionally conservative — better to render desktop for an ambiguous UA
# (an unknown bot, e.g.) than to ship a half-broken mobile layout. Users on a
# desktop browser in mobile-emulation mode trip this regex too, which is fine
# for testing.
_MOBILE_UA_RE = re.compile(
    r"(iPhone|iPod|Android.*Mobile|BlackBerry|IEMobile|Opera Mini|"
    r"Mobile Safari|Windows Phone|webOS)",
    re.IGNORECASE,
)


def _is_mobile_request():
    """True if the current request looks like it's from a phone.

    Honors a per-session override: visiting any URL with ``?desktop=1`` flips
    a session flag that forces the desktop layout for the rest of the session.
    Visiting ``?desktop=0`` clears the override. The override exists so users
    can request the full site from a phone (and so devs can verify mobile
    routing without spoofing UA).
    """
    if request.args.get("desktop") == "1":
        session["force_desktop"] = True
    elif request.args.get("desktop") == "0":
        session.pop("force_desktop", None)
    if session.get("force_desktop"):
        return False
    ua = request.headers.get("User-Agent", "")
    return bool(_MOBILE_UA_RE.search(ua))


@app.before_request
def _detect_mobile():
    """Stash is_mobile on flask.g so route handlers and templates can branch."""
    g.is_mobile = _is_mobile_request()


@app.context_processor
def _inject_mobile_flag():
    """Make ``is_mobile`` available inside every Jinja template."""
    return {"is_mobile": getattr(g, "is_mobile", False)}


def mobile_render(name, **context):
    """Render ``mobile/<name>`` for phone clients, else the desktop ``<name>``.

    Used by every public-facing web route. Admin routes use ``@no_mobile``
    instead, which redirects to /desktop-only — admin is desktop-only by
    product decision.
    """
    if getattr(g, "is_mobile", False):
        return render_template(f"mobile/{name}", **context)
    return render_template(name, **context)


def no_mobile(fn):
    """Decorator: redirect mobile callers to /desktop-only.

    Apply to every admin route. Mobile users get a friendly page explaining
    that admin tools require a larger screen, with a one-click link to
    request the desktop layout for the rest of their session.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if getattr(g, "is_mobile", False):
            return redirect(url_for("desktop_only_page"))
        return fn(*args, **kwargs)
    return wrapper


@app.route("/desktop-only")
def desktop_only_page():
    """Mobile-only landing page shown when a phone hits an admin route."""
    return render_template("mobile/desktop_only.html")


# ══════════════════════════════════════════════
# API-key authentication decorator
# ══════════════════════════════════════════════

_LAST_USED_THROTTLE_SECONDS = 60


def _get_api_user():
    """Return (User, ApiKey) from the Authorization header, or (None, None)."""
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        raw_key = auth[7:].strip()
        api_key = ApiKey.lookup(raw_key)
        if api_key:
            # Throttle last_used writes: only update if the previous value is
            # missing or stale. This keeps the auth-check path read-only on hot
            # traffic instead of committing a row on every request.
            now = datetime.now(timezone.utc)
            prev = api_key.last_used
            if prev is not None and prev.tzinfo is None:
                prev = prev.replace(tzinfo=timezone.utc)
            if prev is None or (now - prev).total_seconds() > _LAST_USED_THROTTLE_SECONDS:
                api_key.last_used = now
                db.session.commit()
            return api_key.user, api_key
    return None, None


def api_auth_required(min_permission="read"):
    """Decorator: require a valid API key with at least *min_permission*.

    Permission levels: read < readwrite < admin
    Also accepts a logged-in web session as a fallback.
    """
    levels = {"read": 0, "readwrite": 1, "admin": 2}

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user, api_key = _get_api_user()

            # Fallback: logged-in web session
            if user is None and current_user.is_authenticated:
                user = current_user
                # Map web session role to permission level. The 'admin'
                # permission level here means "can perform admin-level data
                # operations" — both 'admin' and 'aircraft_admin' qualify.
                # User-management endpoints use the separate @admin_required
                # decorator, which strictly checks is_admin (role == 'admin').
                if user.is_data_admin:
                    perm_level = 2
                elif user.is_manager:
                    perm_level = 1
                else:
                    perm_level = 0
            elif api_key:
                perm_level = levels.get(api_key.permissions, 0)
            else:
                return jsonify({"error": "Authentication required. Supply 'Authorization: Bearer <api_key>' header."}), 401

            if perm_level < levels.get(min_permission, 0):
                return jsonify({"error": f"Insufficient permissions. Requires '{min_permission}'."}), 403

            # Store the resolved user on g for scope checks
            g.api_user = user
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def admin_required(fn):
    """Decorator: require admin role (web session only)."""
    @wraps(fn)
    @login_required
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return fn(*args, **kwargs)
    return wrapper


def _get_effective_user():
    """Return the authenticated user from either API key or web session."""
    return getattr(g, "api_user", current_user if current_user.is_authenticated else None)


def _increment_contribution():
    """Bump the contribution counter for the effective user."""
    user = _get_effective_user()
    if user:
        user.contribution_count = (user.contribution_count or 0) + 1


def _user_can_write_museum(museum_id):
    """Check if the current user has write access to a museum (by ID)."""
    user = _get_effective_user()
    if not user:
        return False
    if user.is_admin:
        return True
    museum = Museum.query.get(museum_id)
    if not museum:
        return False
    return user.can_access_museum(museum)


# ══════════════════════════════════════════════
# Web page routes (public)
# ══════════════════════════════════════════════

@app.route("/")
def index():
    return mobile_render("index.html")


@app.route("/aircraft")
def aircraft_page():
    return mobile_render("aircraft.html")


@app.route("/museums")
def museums_page():
    return mobile_render("museums.html")


@app.route("/aircraft/<int:aircraft_id>")
def aircraft_detail_page(aircraft_id):
    """Aircraft detail page.

    Mobile: renders a dedicated detail template.
    Desktop: the list page handles detail in-place — redirect there with a
    ``focus`` query param so the existing JS can highlight/scroll to the row.
    """
    if getattr(g, "is_mobile", False):
        return render_template("mobile/aircraft_detail.html", aircraft_id=aircraft_id)
    return redirect(url_for("aircraft_page") + f"?focus={aircraft_id}")


@app.route("/museums/<int:museum_id>")
def museum_detail_page(museum_id):
    """Museum detail page — same dispatch pattern as aircraft_detail_page."""
    if getattr(g, "is_mobile", False):
        return render_template("mobile/museum_detail.html", museum_id=museum_id)
    return redirect(url_for("museums_page") + f"?focus={museum_id}")


# ══════════════════════════════════════════════
# Auth: login / logout / register
# ══════════════════════════════════════════════

# Rate-limit login by username AND by IP. The username key blocks an
# attacker spreading attempts across a botnet against one account, while
# the IP key blocks a single client trying many usernames.
def _login_username_key():
    return (request.form.get("username") or "").strip().lower() or get_remote_address()


@app.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute", methods=["POST"])
@limiter.limit("10 per hour", key_func=_login_username_key, methods=["POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("admin_page"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()

        # Lockout check runs before the password check so a locked attacker
        # learns nothing about whether their password is correct, AND so a
        # legitimate user with a forgotten password sees the lockout
        # message instead of repeatedly hitting "wrong password" and
        # extending their own lockout.
        if user and user.is_locked:
            remaining = user.lockout_seconds_remaining()
            mins = max(1, remaining // 60)
            auth_log.warning(
                f"LOGIN_BLOCKED_LOCKED user={username} ip={request.remote_addr} "
                f"remaining={remaining}s"
            )
            flash(f"Account temporarily locked. Try again in {mins} minute(s).", "error")
            return mobile_render("login.html")

        if user and user.check_password(password) and user.is_active:
            user.last_login = datetime.now(timezone.utc)
            user.last_login_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
            user.reset_failed_logins()
            db.session.commit()

            # Session-fixation defense: clear any pre-existing session before
            # we mark the user as authenticated, so an attacker who planted
            # a session ID via an XSS or shared-link vector can't elevate it
            # by waiting for the victim to log in. Flask's signed-session
            # implementation derives the cookie from session content, so a
            # cleared-then-rebuilt session effectively rotates the cookie.
            session.clear()

            login_user(user, remember=True)
            # Stamp absolute and idle clocks for the timeout middleware.
            now_iso = datetime.now(timezone.utc).isoformat()
            session["login_time"] = now_iso
            session["last_activity"] = now_iso
            auth_log.info(f"LOGIN_SUCCESS user={username} ip={user.last_login_ip}")

            # Open-redirect defense: only redirect to ?next= if it's a URL
            # on this host. Anything else (full external URL, missing host)
            # falls back to /admin.
            next_url = _safe_next_url(request.args.get("next")) or url_for("admin_page")
            return redirect(next_url)

        # Failed authentication: bump the counter and possibly lock.
        if user:
            locked_now = user.register_failed_login(
                Config.LOGIN_LOCKOUT_MAX_ATTEMPTS,
                Config.LOGIN_LOCKOUT_DURATION,
            )
            db.session.commit()
            if locked_now:
                auth_log.warning(
                    f"LOGIN_LOCKOUT user={username} ip={request.remote_addr} "
                    f"after {user.failed_login_count} failed attempts"
                )

        auth_log.warning(f"LOGIN_FAILED user={username} ip={request.remote_addr}")
        flash("Invalid username or password.", "error")

    return mobile_render("login.html")


@app.route("/logout")
@login_required
def logout():
    # Capture identity BEFORE we tear the session down — current_user
    # becomes anonymous as soon as logout_user() runs.
    username = current_user.username
    user_id = current_user.id

    # Stamp last_logout on the database row.
    user = User.query.get(user_id)
    if user:
        user.last_logout = datetime.now(timezone.utc)
        db.session.commit()

    auth_log.info(f"LOGOUT user={username} ip={request.remote_addr}")

    # See _full_logout for the why-is-this-so-fiddly comment. Same dance
    # is used by the session-timeout middleware so the two paths can't
    # silently drift apart.
    _full_logout()

    # flash() must come AFTER session.clear() (flash messages live in the
    # session). Redirect to /login (not /) so the user gets unambiguous
    # feedback that they're signed out — the topbar on the index page
    # only updates after the next render, which can confuse on cache.
    flash("You have been signed out.", "info")
    return redirect(url_for("login_page"))


@app.route("/register", methods=["GET", "POST"])
@limiter.limit("3 per minute", methods=["POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("admin_page"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip() or None
        password = request.form.get("password", "")
        password2 = request.form.get("password2", "")

        password_error = _validate_password_strength(password) if password else None
        if not username or not password:
            flash("Username and password are required.", "error")
        elif password != password2:
            flash("Passwords do not match.", "error")
        elif password_error:
            flash(password_error, "error")
        elif User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
        else:
            # First user is automatically admin
            is_first = User.query.count() == 0
            role = "admin" if is_first else "viewer"
            user = User(username=username, email=email, role=role)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            auth_log.info(f"REGISTER user={username} role={role} ip={request.remote_addr}")
            flash("Account created!" + (" You are the first user, so you have admin rights." if is_first else ""), "success")
            return redirect(url_for("admin_page"))

    return mobile_render("register.html")


# ══════════════════════════════════════════════
# User account page (session-protected)
# ══════════════════════════════════════════════

@app.route("/account")
@login_required
def account_page():
    return mobile_render("account.html")


# ══════════════════════════════════════════════
# Admin panel (session-protected)
# ══════════════════════════════════════════════

@app.route("/admin")
@no_mobile
@login_required
def admin_page():
    return render_template("admin.html")


@app.route("/admin/aircraft")
@no_mobile
@login_required
def admin_aircraft_page():
    return render_template("admin_aircraft.html")


@app.route("/admin/aircraft/new")
@no_mobile
@login_required
def admin_aircraft_new_page():
    return render_template("admin_aircraft_new.html")


@app.route("/admin/museums")
@no_mobile
@login_required
def admin_museums_page():
    return render_template("admin_museums.html")


@app.route("/admin/museums/new")
@no_mobile
@login_required
def admin_museums_new_page():
    return render_template("admin_museums_new.html")


# /admin/exhibits and /admin/exhibits/new were removed when exhibit-link
# management was folded into the aircraft and museum edit modals. The API
# endpoints (POST/PUT/DELETE /api/v1/exhibits/...) stay; only the page
# routes and their templates were deleted.


@app.route("/admin/templates")
@no_mobile
@login_required
def admin_templates_page():
    return render_template("admin_templates.html")


@app.route("/admin/import")
@no_mobile
@login_required
def admin_import_page():
    """Bulk-import landing page. Auth handled by the login_required decorator;
    the API endpoints behind the form enforce the admin-data role gate."""
    return render_template("admin_import.html")


@app.route("/admin/users")
@no_mobile
@admin_required
def admin_users_page():
    return render_template("users.html")


@app.route("/admin/api-keys")
@no_mobile
@login_required
def api_keys_page():
    return render_template("api_keys.html")


# ══════════════════════════════════════════════
# Public: contributions leaderboard
# ══════════════════════════════════════════════

@app.route("/contributors")
def contributors_page():
    return mobile_render("contributors.html")


@app.route("/api/v1/contributors")
def api_contributors():
    """Public endpoint: list users with contribution counts, sorted by most contributions."""
    # Column-only query: avoids loading full User rows (and their relationships)
    # just to serialize three fields.
    rows = (
        db.session.query(User.username, User.role, User.contribution_count)
        .filter(User.contribution_count > 0)
        .order_by(User.contribution_count.desc())
        .all()
    )
    return jsonify([
        {"username": username, "role": role, "contributions": count}
        for username, role, count in rows
    ])


# ══════════════════════════════════════════════
# API: Public read-only (no auth needed)
# ══════════════════════════════════════════════

# Sortable-column whitelists. Only columns listed here can be sorted via
# ?sort_by=...; anything else is silently ignored and the endpoint falls back
# to its default ORDER BY. This stops "?sort_by=password_hash" style probes
# in case someone tries to sort by a column we never meant to expose.
_AIRCRAFT_SORT_COLUMNS = {
    "id":                lambda: Aircraft.id,
    "model":             lambda: Aircraft.model,
    "variant":           lambda: Aircraft.variant,
    "model_name":        lambda: Aircraft.model_name,
    "aircraft_name":     lambda: Aircraft.aircraft_name,
    "tail_number":       lambda: Aircraft.tail_number,
    "manufacturer":      lambda: Aircraft.manufacturer,
    "aircraft_type":     lambda: Aircraft.aircraft_type,
    "military_civilian": lambda: Aircraft.military_civilian,
    "role_type":         lambda: Aircraft.role_type,
    "year_built":        lambda: Aircraft.year_built,
    "full_designation":  lambda: Aircraft.full_designation,
}

_MUSEUM_SORT_COLUMNS = {
    "id":             lambda: Museum.id,
    "name":           lambda: Museum.name,
    "city":           lambda: Museum.city,
    "state_province": lambda: Museum.state_province,
    "country":        lambda: Museum.country,
    "region":         lambda: Museum.region,
}


def _apply_sort(query, column_map, default_order):
    """Apply ?sort_by=…&sort_dir=… to ``query`` if the requested column is
    in the ``column_map`` whitelist; otherwise fall back to ``default_order``.

    column_map values are zero-arg callables returning the column expression
    so we evaluate them only when used (avoids touching the model at module
    import time before the app is configured).
    """
    sort_by = (request.args.get("sort_by") or "").strip()
    sort_dir = (request.args.get("sort_dir") or "asc").strip().lower()
    column_factory = column_map.get(sort_by)
    if column_factory is None:
        return query.order_by(*default_order)
    column = column_factory()
    return query.order_by(column.desc() if sort_dir == "desc" else column.asc())


def _build_aircraft_filter(q):
    """Build an OR filter that matches aircraft by model, name, tail, manufacturer, or alias."""
    like = f"%{q}%"
    # Subquery: aircraft IDs that match via aliases. Use scalar_subquery() so
    # SQLAlchemy 2.x doesn't emit a coercion warning when this is fed into
    # in_(); the older .subquery() form is deprecated for that use case.
    alias_ids = db.session.query(AircraftAlias.aircraft_id).filter(
        AircraftAlias.alias.ilike(like)
    ).scalar_subquery()
    return or_(
        Aircraft.tail_number.ilike(like),
        Aircraft.model_name.ilike(like),
        Aircraft.aircraft_name.ilike(like),
        Aircraft.model.ilike(like),
        Aircraft.variant.ilike(like),
        # Use the STORED generated column (indexed as idx_full_desig) instead
        # of computing CONCAT(model, '-', variant) per row, which would defeat
        # the index and force a full table scan.
        Aircraft.full_designation.ilike(like),
        Aircraft.manufacturer.ilike(like),
        Aircraft.id.in_(alias_ids),
    )


@app.route("/api/v1/aircraft/search")
def api_aircraft_search():
    """Search aircraft by tail number, model, variant, name, manufacturer, or alias."""
    q = request.args.get("q", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)

    query = Aircraft.query
    if q:
        query = query.filter(_build_aircraft_filter(q))
    # Honor ?sort_by=field&sort_dir=asc|desc; default ordering otherwise.
    query = _apply_sort(
        query, _AIRCRAFT_SORT_COLUMNS,
        default_order=(Aircraft.model, Aircraft.variant, Aircraft.model_name),
    )
    p = query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({"results": [a.to_dict() for a in p.items], "total": p.total, "page": p.page, "pages": p.pages})


@app.route("/api/v1/aircraft/<int:aircraft_id>")
def api_aircraft_detail(aircraft_id):
    """Get a single aircraft with its museum locations."""
    aircraft = Aircraft.query.get_or_404(aircraft_id)
    links = (
        AircraftMuseum.query
        .options(joinedload(AircraftMuseum.museum))
        .filter_by(aircraft_id=aircraft_id)
        .all()
    )
    # NOTE on key ordering: spread museum.to_dict() FIRST, then add the link
    # fields after — otherwise the museum's `id` would clobber a link `id`.
    # We expose the AircraftMuseum primary key as `link_id` so the UI can call
    # DELETE /api/v1/exhibits/<link_id> to unlink without ambiguity.
    museums = [
        {
            **lnk.museum.to_dict(),
            "display_status": lnk.display_status,
            "notes": lnk.notes,
            "link_id": lnk.id,
        }
        for lnk in links
    ]
    return jsonify({"aircraft": aircraft.to_dict(), "museums": museums})


@app.route("/api/v1/museums/search")
def api_museum_search():
    """Search museums by name, city, state/province, country, or region."""
    q = request.args.get("q", "").strip()
    region = request.args.get("region", "").strip()
    country = request.args.get("country", "").strip()
    state = request.args.get("state", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)

    query = Museum.query
    if q:
        like = f"%{q}%"
        query = query.filter(or_(
            Museum.name.ilike(like),
            Museum.city.ilike(like),
            Museum.state_province.ilike(like),
            Museum.country.ilike(like),
        ))
    if region:
        query = query.filter(Museum.region == region)
    if country:
        query = query.filter(Museum.country.ilike(country))
    if state:
        query = query.filter(Museum.state_province.ilike(state))
    query = _apply_sort(
        query, _MUSEUM_SORT_COLUMNS,
        default_order=(Museum.name,),
    )
    p = query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({"results": [m.to_dict() for m in p.items], "total": p.total, "page": p.page, "pages": p.pages})


@app.route("/api/v1/museums/<int:museum_id>")
def api_museum_detail(museum_id):
    """Get a single museum with its aircraft collection."""
    museum = Museum.query.get_or_404(museum_id)
    links = (
        AircraftMuseum.query
        .options(joinedload(AircraftMuseum.aircraft))
        .filter_by(museum_id=museum_id)
        .all()
    )
    # See note on api_aircraft_detail — link_id is the AircraftMuseum primary
    # key, exposed for the UI's unlink action.
    aircraft_list = [
        {
            **lnk.aircraft.to_dict(),
            "display_status": lnk.display_status,
            "notes": lnk.notes,
            "link_id": lnk.id,
        }
        for lnk in links
    ]
    return jsonify({"museum": museum.to_dict(), "aircraft": aircraft_list})


@app.route("/api/v1/museums/regions")
def api_museum_regions():
    """List all regions with museum counts."""
    rows = db.session.query(Museum.region, func.count(Museum.id)).group_by(Museum.region).all()
    return jsonify([{"region": r, "count": c} for r, c in rows])


@app.route("/api/v1/museums/globe")
def api_museums_globe():
    """Lightweight endpoint for the 3D globe view.

    Returns only the fields needed to plot each museum as a pin plus the
    total number of aircraft linked to it. Museums without coordinates are
    skipped.
    """
    rows = (
        db.session.query(
            Museum.id, Museum.name, Museum.city, Museum.country,
            Museum.latitude, Museum.longitude,
            func.count(AircraftMuseum.id),
        )
        .outerjoin(AircraftMuseum, AircraftMuseum.museum_id == Museum.id)
        .filter(Museum.latitude.isnot(None), Museum.longitude.isnot(None))
        # Group by every selected non-aggregate column so this stays valid
        # under MySQL's ONLY_FULL_GROUP_BY sql_mode (the default in 5.7+).
        .group_by(
            Museum.id, Museum.name, Museum.city, Museum.country,
            Museum.latitude, Museum.longitude,
        )
        .all()
    )
    return jsonify([
        {
            "id": mid,
            "name": name,
            "city": city,
            "country": country,
            "latitude": float(lat),
            "longitude": float(lon),
            "aircraft_count": int(count),
        }
        for (mid, name, city, country, lat, lon, count) in rows
    ])


@app.route("/api/v1/museums/countries")
def api_museum_countries():
    """List all countries with museum counts."""
    rows = db.session.query(Museum.country, func.count(Museum.id)).group_by(Museum.country).all()
    return jsonify([{"country": c, "count": n} for c, n in rows])


@app.route("/api/v1/nearest")
def api_nearest_museum():
    """Find nearest museum(s) with a specific aircraft to a location.

    The 'aircraft' param can match model, name, tail, manufacturer, or alias.
    Optionally filter by 'museum' name as well.
    Only museums with known coordinates are included in distance results.
    Museums without coordinates are listed separately.
    """
    aircraft_query = request.args.get("aircraft", "").strip()
    museum_query = request.args.get("museum", "").strip()
    location = request.args.get("location", "").strip()
    limit = min(request.args.get("limit", 5, type=int), 25)

    if not aircraft_query or not location:
        return jsonify({"error": "Both 'aircraft' and 'location' parameters are required."}), 400

    lat, lon = _resolve_location(location)
    if lat is None:
        return jsonify({"error": f"Could not resolve location: {location}"}), 404

    matching = Aircraft.query.filter(_build_aircraft_filter(aircraft_query)).all()
    if not matching:
        return jsonify({"error": f"No aircraft matching '{aircraft_query}' found."}), 404

    links_query = (
        AircraftMuseum.query
        .options(
            joinedload(AircraftMuseum.museum),
            joinedload(AircraftMuseum.aircraft),
        )
        .filter(AircraftMuseum.aircraft_id.in_([a.id for a in matching]))
    )

    # Optional museum name filter — single subquery instead of two round-trips.
    # scalar_subquery() so SQLAlchemy 2.x doesn't warn about coercion in IN().
    if museum_query:
        museum_like = f"%{museum_query}%"
        matching_museum_ids = db.session.query(Museum.id).filter(Museum.name.ilike(museum_like)).scalar_subquery()
        links_query = links_query.filter(AircraftMuseum.museum_id.in_(matching_museum_ids))

    links = links_query.all()
    if not links:
        return jsonify({"error": f"No museums found displaying aircraft matching '{aircraft_query}'."}), 404

    results = []
    no_coords = []
    for lnk in links:
        museum = lnk.museum
        if museum.has_coordinates:
            dist = haversine(lat, lon, float(museum.latitude), float(museum.longitude))
            results.append({
                "distance_miles": round(dist, 1),
                "museum": museum.to_dict(),
                "aircraft": lnk.aircraft.to_dict(),
                "display_status": lnk.display_status,
            })
        else:
            no_coords.append({
                "museum": museum.to_dict(),
                "aircraft": lnk.aircraft.to_dict(),
                "display_status": lnk.display_status,
                "note": "Distance unavailable — museum coordinates not on file.",
            })

    results.sort(key=lambda x: x["distance_miles"])
    response = {
        "origin": {"location": location, "latitude": lat, "longitude": lon},
        "results": results[:limit],
    }
    if no_coords:
        response["no_coordinates"] = no_coords
    return jsonify(response)


@app.route("/api/v1/museums/nearby")
def api_nearby_museums():
    """Find museums nearest to a given location.

    Parameters:
        location (required) — zip/postal code or city name.
        region   (optional) — filter by museum region.
        limit    (optional) — max results (default 10, max 50).
    """
    location = request.args.get("location", "").strip()
    region = request.args.get("region", "").strip()
    limit = min(request.args.get("limit", 10, type=int), 50)

    if not location:
        return jsonify({"error": "The 'location' parameter is required."}), 400

    lat, lon = _resolve_location(location)
    if lat is None:
        return jsonify({"error": f"Could not resolve location: {location}"}), 404

    # Split the query so coord-less rows are fetched only when they need to be
    # reported, instead of loading every museum into Python just to filter.
    base = Museum.query
    if region:
        base = base.filter(Museum.region == region)

    with_coords = base.filter(
        Museum.latitude.isnot(None), Museum.longitude.isnot(None)
    ).all()
    without_coords = base.filter(
        or_(Museum.latitude.is_(None), Museum.longitude.is_(None))
    ).all()

    results = [
        {
            "distance_miles": round(
                haversine(lat, lon, float(m.latitude), float(m.longitude)), 1
            ),
            "museum": m.to_dict(),
        }
        for m in with_coords
    ]
    no_coords = [
        {"museum": m.to_dict(), "note": "Distance unavailable — coordinates not on file."}
        for m in without_coords
    ]

    results.sort(key=lambda x: x["distance_miles"])
    response = {
        "origin": {"location": location, "latitude": lat, "longitude": lon},
        "results": results[:limit],
    }
    if no_coords:
        response["no_coordinates"] = no_coords
    return jsonify(response)


@app.route("/api/v1/stats")
def api_stats():
    """Dashboard statistics."""
    return jsonify({
        "aircraft_count": Aircraft.query.count(),
        "museum_count": Museum.query.count(),
        "link_count": AircraftMuseum.query.count(),
        "country_count": db.session.query(func.count(func.distinct(Museum.country))).scalar(),
    })


# ── Backward-compat aliases (old /api/ routes) ──

@app.route("/api/aircraft/search")
def aircraft_search_compat():
    return api_aircraft_search()

@app.route("/api/aircraft/<int:aircraft_id>")
def aircraft_detail_compat(aircraft_id):
    return api_aircraft_detail(aircraft_id)

@app.route("/api/museums/search")
def museum_search_compat():
    return api_museum_search()

@app.route("/api/museums/<int:museum_id>")
def museum_detail_compat(museum_id):
    return api_museum_detail(museum_id)

@app.route("/api/museums/regions")
def museum_regions_compat():
    return api_museum_regions()

@app.route("/api/nearest")
def nearest_compat():
    return api_nearest_museum()

@app.route("/api/museums/nearby")
def nearby_museums_compat():
    return api_nearby_museums()

@app.route("/api/stats")
def stats_compat():
    return api_stats()


# ══════════════════════════════════════════════
# API: Authenticated CRUD (requires API key or session)
# ══════════════════════════════════════════════

# ══════════════════════════════════════════════
# Bulk import (aircraft + museums, CSV + JSON)
# ══════════════════════════════════════════════

# Hard cap on rows per request. Keeps any single import bounded so a 100k-row
# upload can't tie up a worker for minutes; users with bigger batches should
# split them.
_BULK_MAX_ROWS = 5000

# Enum allowlists used by the validators below. Must match the schema ENUMs.
_AIRCRAFT_TYPE_VALUES = {
    "fixed_wing", "rotary_wing", "lighter_than_air", "spacecraft",
    # Missiles, rockets, and unmanned expendable flight vehicles. See
    # migrate_missile_rocket.sql for the schema-side enum change.
    "missile_rocket",
}
_WING_TYPE_VALUES = {"monoplane", "biplane", "triplane"}
_MILITARY_CIVILIAN_VALUES = {"military", "civilian"}
_REGION_VALUES = {
    "North America", "Europe", "Asia", "Asia-Pacific", "South America",
    "Oceania", "Africa", "Middle East",
}


def _parse_bulk_payload(raw, fmt):
    """Parse ``raw`` (a string) as ``fmt`` ('csv' or 'json') and return a list
    of dicts. Raises ValueError on malformed input.

    'auto' format detection picks JSON if the text starts with [ or {,
    otherwise CSV. This matches both pasted-text and uploaded-file flows.
    """
    fmt = (fmt or "auto").lower()
    text = raw.strip() if isinstance(raw, str) else raw.decode("utf-8").strip()

    if fmt == "auto":
        fmt = "json" if text[:1] in ("[", "{") else "csv"

    if fmt == "json":
        try:
            data = json.loads(text)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON parse error: {e.msg} at line {e.lineno}, col {e.colno}")
        if not isinstance(data, list):
            raise ValueError("JSON payload must be a list of objects.")
        if not all(isinstance(row, dict) for row in data):
            raise ValueError("Every entry in the JSON list must be an object.")
        return data

    if fmt == "csv":
        # csv.DictReader handles quoted fields with embedded commas, etc.
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        if not rows:
            raise ValueError("CSV is empty or missing a header row.")
        return rows

    raise ValueError(f"Unsupported format: {fmt!r}. Use 'csv', 'json', or 'auto'.")


def _split_aliases(value):
    """Aliases are JSON arrays in JSON payloads, semicolon-separated strings
    in CSV. Normalize both into a clean list of unique non-empty strings."""
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [a.strip() for a in value if isinstance(a, str) and a.strip()]
    if isinstance(value, str):
        # Both ; and , can show up in user CSVs. Default to ; (since aircraft
        # designations contain commas inside aliases like "B-29, Superfortress").
        parts = [p.strip() for p in value.split(";")]
        return [p for p in parts if p]
    return []


def _coerce_int(value, field_name, errors):
    """Try to parse ``value`` as int; record an error and return None if not."""
    if value is None or value == "":
        return None
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        errors.append({"field": field_name, "message": f"must be an integer (got {value!r})"})
        return None


def _coerce_float(value, field_name, errors):
    if value is None or value == "":
        return None
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        errors.append({"field": field_name, "message": f"must be a number (got {value!r})"})
        return None


def _validate_aircraft_row(row):
    """Return (clean_dict, errors). clean_dict is None if errors is non-empty."""
    errors = []
    # Trim every string field for safety.
    g = lambda k: (row.get(k) or "").strip() if isinstance(row.get(k), str) else row.get(k)

    manufacturer = g("manufacturer")
    model = g("model")
    if not manufacturer:
        errors.append({"field": "manufacturer", "message": "required"})
    if not model:
        errors.append({"field": "model", "message": "required"})

    aircraft_type = g("aircraft_type") or "fixed_wing"
    if aircraft_type not in _AIRCRAFT_TYPE_VALUES:
        errors.append({"field": "aircraft_type",
                       "message": f"must be one of {sorted(_AIRCRAFT_TYPE_VALUES)}"})

    wing_type = g("wing_type") or None
    if wing_type and wing_type not in _WING_TYPE_VALUES:
        errors.append({"field": "wing_type",
                       "message": f"must be one of {sorted(_WING_TYPE_VALUES)} or empty"})

    mil_civ = g("military_civilian") or "military"
    if mil_civ not in _MILITARY_CIVILIAN_VALUES:
        errors.append({"field": "military_civilian",
                       "message": f"must be one of {sorted(_MILITARY_CIVILIAN_VALUES)}"})

    year_built = _coerce_int(row.get("year_built"), "year_built", errors)

    if errors:
        return None, errors

    return {
        "manufacturer": manufacturer,
        "model": model,
        "variant": g("variant") or None,
        "tail_number": _normalize_tail_number(g("tail_number")),
        "model_name": g("model_name") or None,
        "aircraft_name": g("aircraft_name") or None,
        "aircraft_type": aircraft_type,
        "wing_type": wing_type,
        "military_civilian": mil_civ,
        "role_type": g("role_type") or None,
        "year_built": year_built,
        "description": g("description") or None,
        "aliases": _split_aliases(row.get("aliases")),
    }, []


def _validate_museum_row(row):
    """Return (clean_dict, errors). clean_dict is None if errors is non-empty."""
    errors = []
    g = lambda k: (row.get(k) or "").strip() if isinstance(row.get(k), str) else row.get(k)

    name = g("name")
    city = g("city")
    country = g("country") or "United States"
    region = g("region")

    if not name:    errors.append({"field": "name", "message": "required"})
    if not city:    errors.append({"field": "city", "message": "required"})
    if not region:  errors.append({"field": "region", "message": "required"})

    if region and region not in _REGION_VALUES:
        errors.append({"field": "region",
                       "message": f"must be one of {sorted(_REGION_VALUES)}"})

    latitude = _coerce_float(row.get("latitude"), "latitude", errors)
    longitude = _coerce_float(row.get("longitude"), "longitude", errors)
    # Either both coordinates or neither.
    if (latitude is None) != (longitude is None):
        errors.append({"field": "latitude/longitude",
                       "message": "set both latitude AND longitude, or neither"})

    if errors:
        return None, errors

    return {
        "name": name,
        "city": city,
        "state_province": g("state_province") or None,
        "country": country,
        "postal_code": g("postal_code") or None,
        "region": region,
        "address": g("address") or None,
        "website": g("website") or None,
        "latitude": latitude,
        "longitude": longitude,
    }, []


def _bulk_import_aircraft(rows, dry_run):
    """Validate + (optionally) insert aircraft rows. Atomic: any error
    triggers rollback so an import never half-applies."""
    report = {"created": 0, "skipped": 0, "errors": [], "dry_run": dry_run}

    # First pass: validate every row, collect errors with row indices.
    cleaned = []
    seen_pairs = set()  # (model, tail) duplicates within the batch
    for i, raw in enumerate(rows):
        clean, errs = _validate_aircraft_row(raw)
        if errs:
            for e in errs:
                report["errors"].append({"row": i, **e})
            continue
        # Within-batch duplicate detection (DB unique index would catch it too,
        # but we want a clean error report instead of an opaque IntegrityError).
        if clean["tail_number"]:
            pair = (clean["model"], clean["tail_number"])
            if pair in seen_pairs:
                report["errors"].append({
                    "row": i, "field": "(model, tail_number)",
                    "message": f"duplicate of an earlier row in this batch: {pair}",
                })
                continue
            seen_pairs.add(pair)
        cleaned.append((i, clean))

    # If validation failed anywhere, bail without writing.
    if report["errors"]:
        return report

    if dry_run:
        report["created"] = len(cleaned)
        return report

    # Second pass: insert. Existing-DB duplicate check uses our helper.
    try:
        for i, clean in cleaned:
            existing = _find_aircraft_duplicate(clean["model"], clean["tail_number"])
            if existing is not None:
                report["skipped"] += 1
                report["errors"].append({
                    "row": i, "field": "(model, tail_number)",
                    "message": f"already exists in DB (id={existing.id}); skipped",
                })
                continue
            aliases = clean.pop("aliases")
            ac = Aircraft(**clean)
            db.session.add(ac)
            db.session.flush()
            for alias in aliases:
                db.session.add(AircraftAlias(aircraft_id=ac.id, alias=alias))
            report["created"] += 1
        # Roll back if ANY row triggered a "skipped because duplicate" error —
        # the alternative is partial success which is hard to recover from.
        # Comment out the rollback here if you want skip-and-continue semantics.
        if report["errors"]:
            db.session.rollback()
            report["created"] = 0   # report rolls back too
        else:
            db.session.commit()
    except Exception as exc:
        db.session.rollback()
        report["errors"].append({"row": -1, "field": "_db", "message": str(exc)})
        report["created"] = 0
    return report


def _bulk_import_museums(rows, dry_run):
    """Validate + (optionally) insert museum rows. Same atomic semantics."""
    report = {"created": 0, "skipped": 0, "errors": [], "dry_run": dry_run}

    cleaned = []
    seen_names = set()
    for i, raw in enumerate(rows):
        clean, errs = _validate_museum_row(raw)
        if errs:
            for e in errs:
                report["errors"].append({"row": i, **e})
            continue
        # Within-batch dup: same name + city + country = same museum.
        key = (clean["name"].lower(), clean["city"].lower(), clean["country"].lower())
        if key in seen_names:
            report["errors"].append({
                "row": i, "field": "name+city+country",
                "message": f"duplicate of an earlier row in this batch",
            })
            continue
        seen_names.add(key)
        cleaned.append((i, clean))

    if report["errors"]:
        return report
    if dry_run:
        report["created"] = len(cleaned)
        return report

    try:
        for i, clean in cleaned:
            # Existing-DB dedupe: same name+city+country already in DB?
            existing = Museum.query.filter(
                func.lower(Museum.name) == clean["name"].lower(),
                func.lower(Museum.city) == clean["city"].lower(),
                func.lower(Museum.country) == clean["country"].lower(),
            ).first()
            if existing is not None:
                report["skipped"] += 1
                report["errors"].append({
                    "row": i, "field": "name+city+country",
                    "message": f"already exists in DB (id={existing.id}); skipped",
                })
                continue
            db.session.add(Museum(**clean))
            report["created"] += 1
        if report["errors"]:
            db.session.rollback()
            report["created"] = 0
        else:
            db.session.commit()
    except Exception as exc:
        db.session.rollback()
        report["errors"].append({"row": -1, "field": "_db", "message": str(exc)})
        report["created"] = 0
    return report


def _bulk_import_request_payload():
    """Pull the import payload from EITHER a multipart file upload OR a JSON
    body. Returns (raw_text, fmt, dry_run). Raises ValueError on malformed
    input or oversize payload."""
    dry_run = False
    fmt = "auto"
    raw = None

    # 1. Multipart upload (the admin web UI uses this path).
    if "file" in request.files and request.files["file"].filename:
        f = request.files["file"]
        # Detect format from filename extension if format wasn't specified.
        if request.form.get("format"):
            fmt = request.form["format"]
        elif f.filename.lower().endswith(".json"):
            fmt = "json"
        else:
            fmt = "csv"
        dry_run = request.form.get("dry_run", "").lower() in ("1", "true", "yes", "on")
        raw = f.read().decode("utf-8")
    else:
        # 2. JSON body: {"format": "csv"|"json", "data": "...", "dry_run": bool}
        body = request.get_json(silent=True) or {}
        fmt = body.get("format", "auto")
        dry_run = bool(body.get("dry_run", False))
        raw = body.get("data")
        if not raw:
            raise ValueError(
                "Provide either a 'file' upload (multipart) or a JSON body "
                "with a 'data' field containing the CSV/JSON text."
            )

    if len(raw) > Config.MAX_CONTENT_LENGTH:
        raise ValueError(f"Payload exceeds {Config.MAX_CONTENT_LENGTH:,}-byte limit.")
    return raw, fmt, dry_run


@app.route("/api/v1/aircraft/bulk_import", methods=["POST"])
@api_auth_required("admin")
@limiter.limit("10 per hour")
def api_bulk_import_aircraft():
    """Bulk-create aircraft from a CSV or JSON payload. aircraft_admin+."""
    try:
        raw, fmt, dry_run = _bulk_import_request_payload()
        rows = _parse_bulk_payload(raw, fmt)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    if len(rows) > _BULK_MAX_ROWS:
        return jsonify({"error": f"At most {_BULK_MAX_ROWS} rows per import."}), 400
    report = _bulk_import_aircraft(rows, dry_run=dry_run)
    user = _get_effective_user()
    change_log.info(
        f"BULK_IMPORT_AIRCRAFT created={report['created']} skipped={report['skipped']} "
        f"errors={len(report['errors'])} dry_run={dry_run} by={user.username}"
    )
    return jsonify(report)


@app.route("/api/v1/museums/bulk_import", methods=["POST"])
@api_auth_required("admin")
@limiter.limit("10 per hour")
def api_bulk_import_museums():
    """Bulk-create museums from a CSV or JSON payload. aircraft_admin+."""
    try:
        raw, fmt, dry_run = _bulk_import_request_payload()
        rows = _parse_bulk_payload(raw, fmt)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    if len(rows) > _BULK_MAX_ROWS:
        return jsonify({"error": f"At most {_BULK_MAX_ROWS} rows per import."}), 400
    report = _bulk_import_museums(rows, dry_run=dry_run)
    user = _get_effective_user()
    change_log.info(
        f"BULK_IMPORT_MUSEUMS created={report['created']} skipped={report['skipped']} "
        f"errors={len(report['errors'])} dry_run={dry_run} by={user.username}"
    )
    return jsonify(report)


# ── Aircraft CRUD ──

def _normalize_tail_number(raw):
    """Normalize a tail-number value: empty/whitespace becomes None.

    Tail numbers are optional. Treating "" the same as NULL keeps duplicate
    detection sane — multiple unmarked airframes shouldn't collide with each
    other, only real tail-number reuses should.
    """
    if raw is None:
        return None
    s = str(raw).strip()
    return s or None


def _find_aircraft_duplicate(model, tail_number, exclude_id=None):
    """Return the existing Aircraft that would conflict with (model, tail_number),
    or None. tail_number must already be normalized — passing None means "no
    tail number, no conflict possible" (NULL doesn't collide with NULL).
    """
    if not tail_number:
        return None
    q = Aircraft.query.filter(
        Aircraft.model == model,
        Aircraft.tail_number == tail_number,
    )
    if exclude_id is not None:
        q = q.filter(Aircraft.id != exclude_id)
    return q.first()


@app.route("/api/v1/aircraft", methods=["POST"])
@api_auth_required("readwrite")
def api_create_aircraft():
    """Create a new aircraft record.

    Optional: pass ``museum_id`` and ``display_status`` to automatically
    link the aircraft to a museum on creation.
    Scoped users can only link to museums they have access to.
    """
    data = request.get_json() or {}
    required = ["manufacturer", "model"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    # Scope check: if linking to museum, user must have access
    museum_id = data.get("museum_id")
    if museum_id and not _user_can_write_museum(int(museum_id)):
        return jsonify({"error": "You do not have access to that museum."}), 403

    # Sanity check: refuse to create a duplicate (same model + tail number).
    # Empty/missing tail numbers are treated as "unknown" and never collide.
    tail = _normalize_tail_number(data.get("tail_number"))
    dup = _find_aircraft_duplicate(data["model"], tail)
    if dup:
        return jsonify({
            "error": (
                f"An aircraft with model '{data['model']}' and tail number "
                f"'{tail}' already exists (id={dup.id})."
            ),
            "existing_id": dup.id,
        }), 409

    aircraft = Aircraft(
        tail_number=tail,
        model_name=data.get("model_name"),
        aircraft_name=data.get("aircraft_name"),
        manufacturer=data["manufacturer"],
        model=data["model"],
        variant=data.get("variant"),
        aircraft_type=data.get("aircraft_type", "fixed_wing"),
        wing_type=data.get("wing_type") or None,
        military_civilian=data.get("military_civilian", "military"),
        role_type=data.get("role_type") or None,
        year_built=data.get("year_built"),
        description=data.get("description"),
    )
    db.session.add(aircraft)
    db.session.flush()

    # Add aliases if provided
    for alias_str in data.get("aliases", []):
        alias_str = alias_str.strip()
        if alias_str:
            db.session.add(AircraftAlias(aircraft_id=aircraft.id, alias=alias_str))

    # Optionally link to a museum right away
    if museum_id:
        museum = Museum.query.get(museum_id)
        if museum:
            link = AircraftMuseum(
                aircraft_id=aircraft.id,
                museum_id=museum.id,
                display_status=data.get("display_status", "on_display"),
            )
            db.session.add(link)

    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"AIRCRAFT_CREATE id={aircraft.id} model={aircraft.model} by={user.username}")
    return jsonify(aircraft.to_dict()), 201


@app.route("/api/v1/aircraft/<int:aircraft_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_aircraft(aircraft_id):
    """Update an existing aircraft record. Include 'aliases' array to replace all aliases."""
    aircraft = Aircraft.query.get_or_404(aircraft_id)
    data = request.get_json() or {}

    # Pre-flight uniqueness check: figure out what the (model, tail_number)
    # would be after this update and reject if it would clash with another row.
    new_model = data["model"] if "model" in data and data["model"] else aircraft.model
    new_tail = (
        _normalize_tail_number(data["tail_number"])
        if "tail_number" in data
        else aircraft.tail_number
    )
    dup = _find_aircraft_duplicate(new_model, new_tail, exclude_id=aircraft.id)
    if dup:
        return jsonify({
            "error": (
                f"Another aircraft (id={dup.id}) already has model '{new_model}' "
                f"and tail number '{new_tail}'."
            ),
            "existing_id": dup.id,
        }), 409

    for field in ["tail_number", "model_name", "aircraft_name",
                   "manufacturer", "model", "variant",
                   "aircraft_type", "wing_type", "military_civilian", "role_type",
                   "year_built", "description"]:
        if field in data:
            if field == "tail_number":
                val = _normalize_tail_number(data[field])
            else:
                val = data[field] if data[field] else None  # treat empty string as None
            setattr(aircraft, field, val)
    # Replace aliases if provided
    if "aliases" in data:
        AircraftAlias.query.filter_by(aircraft_id=aircraft_id).delete()
        for alias_str in data["aliases"]:
            alias_str = alias_str.strip()
            if alias_str:
                db.session.add(AircraftAlias(aircraft_id=aircraft_id, alias=alias_str))
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"AIRCRAFT_UPDATE id={aircraft_id} by={user.username}")
    return jsonify(aircraft.to_dict())


@app.route("/api/v1/aircraft/<int:aircraft_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_aircraft(aircraft_id):
    """Delete an aircraft record (admin only)."""
    aircraft = Aircraft.query.get_or_404(aircraft_id)
    db.session.delete(aircraft)
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"AIRCRAFT_DELETE id={aircraft_id} by={user.username}")
    return jsonify({"deleted": True, "id": aircraft_id})


# ── Museum CRUD ──

@app.route("/api/v1/museums", methods=["POST"])
@api_auth_required("readwrite")
def api_create_museum():
    """Create a new museum record.

    Required: name, city, country, region.
    Optional: state_province, postal_code, address, website, latitude, longitude.
    """
    data = request.get_json() or {}
    required = ["name", "city", "country", "region"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    museum = Museum(
        name=data["name"],
        city=data["city"],
        state_province=data.get("state_province"),
        country=data["country"],
        postal_code=data.get("postal_code"),
        region=data["region"],
        address=data.get("address"),
        website=data.get("website"),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
    )
    db.session.add(museum)
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"MUSEUM_CREATE id={museum.id} name={museum.name} by={user.username}")
    return jsonify(museum.to_dict()), 201


@app.route("/api/v1/museums/<int:museum_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_museum(museum_id):
    """Update an existing museum record. Scoped users can only edit assigned museums."""
    museum = Museum.query.get_or_404(museum_id)

    # Scope check
    user = _get_effective_user()
    if not user.is_admin and not user.can_access_museum(museum):
        return jsonify({"error": "You do not have access to this museum."}), 403

    data = request.get_json() or {}
    for field in ["name", "city", "state_province", "country", "postal_code", "region",
                   "address", "website", "latitude", "longitude"]:
        if field in data:
            setattr(museum, field, data[field])
    _increment_contribution()
    db.session.commit()
    change_log.info(f"MUSEUM_UPDATE id={museum_id} by={user.username}")
    return jsonify(museum.to_dict())


@app.route("/api/v1/museums/<int:museum_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_museum(museum_id):
    """Delete a museum record (admin only)."""
    museum = Museum.query.get_or_404(museum_id)
    db.session.delete(museum)
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"MUSEUM_DELETE id={museum_id} by={user.username}")
    return jsonify({"deleted": True, "id": museum_id})


# ── Exhibit links ──

@app.route("/api/v1/exhibits", methods=["POST"])
@api_auth_required("readwrite")
def api_create_exhibit():
    """Link an aircraft to a museum. Scoped users can only link to assigned museums."""
    data = request.get_json() or {}
    if not data.get("aircraft_id") or not data.get("museum_id"):
        return jsonify({"error": "Both 'aircraft_id' and 'museum_id' are required."}), 400

    # Scope check
    if not _user_can_write_museum(int(data["museum_id"])):
        return jsonify({"error": "You do not have access to that museum."}), 403

    Aircraft.query.get_or_404(data["aircraft_id"])
    Museum.query.get_or_404(data["museum_id"])

    link = AircraftMuseum(
        aircraft_id=data["aircraft_id"],
        museum_id=data["museum_id"],
        display_status=data.get("display_status", "on_display"),
        notes=data.get("notes"),
    )
    db.session.add(link)
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"EXHIBIT_CREATE aircraft={data['aircraft_id']} museum={data['museum_id']} by={user.username}")
    return jsonify(link.to_dict()), 201


@app.route("/api/v1/exhibits/<int:link_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_exhibit(link_id):
    """Update an exhibit link (status, notes)."""
    link = AircraftMuseum.query.get_or_404(link_id)

    # Scope check
    if not _user_can_write_museum(link.museum_id):
        return jsonify({"error": "You do not have access to this museum."}), 403

    data = request.get_json() or {}
    for field in ["display_status", "notes"]:
        if field in data:
            setattr(link, field, data[field])
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"EXHIBIT_UPDATE id={link_id} by={user.username}")
    return jsonify(link.to_dict())


@app.route("/api/v1/exhibits/<int:link_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_exhibit(link_id):
    """Remove an exhibit link (admin only)."""
    link = AircraftMuseum.query.get_or_404(link_id)
    db.session.delete(link)
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"EXHIBIT_DELETE id={link_id} by={user.username}")
    return jsonify({"deleted": True, "id": link_id})


# ── Aircraft templates ──

# Fields that a template can set on a fresh aircraft when used to prefill the
# admin create form. Kept as a module-level tuple so the client and server
# agree on the shape and we don't scatter the list of names across files.
_TEMPLATE_FIELDS = (
    "name", "manufacturer", "model", "variant", "model_name",
    "aircraft_type", "wing_type", "military_civilian", "role_type", "description",
)


@app.route("/api/v1/templates")
def api_template_list():
    """Public: list all aircraft templates, alphabetized by name. Supports
    an optional ``q`` query that fuzzy-matches name / manufacturer / model."""
    q = request.args.get("q", "").strip()
    query = AircraftTemplate.query
    if q:
        like = f"%{q}%"
        query = query.filter(or_(
            AircraftTemplate.name.ilike(like),
            AircraftTemplate.manufacturer.ilike(like),
            AircraftTemplate.model.ilike(like),
            AircraftTemplate.model_name.ilike(like),
        ))
    templates = query.order_by(AircraftTemplate.name).all()
    return jsonify([t.to_dict() for t in templates])


@app.route("/api/v1/templates/<int:template_id>")
def api_template_detail(template_id):
    """Public: single template with its aliases."""
    t = AircraftTemplate.query.get_or_404(template_id)
    return jsonify(t.to_dict())


@app.route("/api/v1/templates", methods=["POST"])
@api_auth_required("readwrite")
def api_create_template():
    """Create a new aircraft template.

    Required: name, manufacturer, model.
    Optional: variant, model_name, aircraft_type, wing_type,
              military_civilian, role_type, description, aliases[].
    """
    data = request.get_json() or {}
    missing = [f for f in ("name", "manufacturer", "model") if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    if AircraftTemplate.query.filter_by(name=data["name"]).first():
        return jsonify({"error": f"A template named '{data['name']}' already exists."}), 409

    t = AircraftTemplate(
        name=data["name"],
        manufacturer=data["manufacturer"],
        model=data["model"],
        variant=data.get("variant") or None,
        model_name=data.get("model_name") or None,
        aircraft_type=data.get("aircraft_type", "fixed_wing"),
        wing_type=data.get("wing_type") or None,
        military_civilian=data.get("military_civilian", "military"),
        role_type=data.get("role_type") or None,
        description=data.get("description") or None,
    )
    db.session.add(t)
    db.session.flush()

    for alias_str in data.get("aliases", []):
        alias_str = (alias_str or "").strip()
        if alias_str:
            db.session.add(AircraftTemplateAlias(template_id=t.id, alias=alias_str))

    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"TEMPLATE_CREATE id={t.id} name={t.name} by={user.username}")
    return jsonify(t.to_dict()), 201


@app.route("/api/v1/templates/<int:template_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_template(template_id):
    """Update a template. Include 'aliases' to replace the full alias set."""
    t = AircraftTemplate.query.get_or_404(template_id)
    data = request.get_json() or {}

    # Unique-name check only fires when the caller actually changes the name.
    if "name" in data and data["name"] and data["name"] != t.name:
        if AircraftTemplate.query.filter_by(name=data["name"]).first():
            return jsonify({"error": f"A template named '{data['name']}' already exists."}), 409

    for field in _TEMPLATE_FIELDS:
        if field in data:
            val = data[field] if data[field] not in ("", None) else None
            # name is NOT NULL; refuse to blank it
            if field == "name" and not val:
                return jsonify({"error": "Template name cannot be empty."}), 400
            setattr(t, field, val)

    if "aliases" in data:
        AircraftTemplateAlias.query.filter_by(template_id=template_id).delete()
        for alias_str in data["aliases"]:
            alias_str = (alias_str or "").strip()
            if alias_str:
                db.session.add(AircraftTemplateAlias(template_id=template_id, alias=alias_str))

    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"TEMPLATE_UPDATE id={template_id} by={user.username}")
    return jsonify(t.to_dict())


@app.route("/api/v1/templates/<int:template_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_template(template_id):
    """Delete a template (admin only). Does not touch aircraft that were
    originally created from this template — once an Aircraft exists it has
    its own copy of the type fields."""
    t = AircraftTemplate.query.get_or_404(template_id)
    name = t.name
    db.session.delete(t)
    _increment_contribution()
    db.session.commit()
    user = _get_effective_user()
    change_log.info(f"TEMPLATE_DELETE id={template_id} name={name} by={user.username}")
    return jsonify({"deleted": True, "id": template_id})


# ── Backward-compat write aliases ──

@app.route("/api/aircraft", methods=["POST"])
@api_auth_required("readwrite")
def create_aircraft_compat():
    return api_create_aircraft()

@app.route("/api/aircraft/<int:aid>", methods=["PUT"])
@api_auth_required("readwrite")
def update_aircraft_compat(aid):
    return api_update_aircraft(aid)

@app.route("/api/aircraft/<int:aid>", methods=["DELETE"])
@api_auth_required("admin")
def delete_aircraft_compat(aid):
    return api_delete_aircraft(aid)

@app.route("/api/museums", methods=["POST"])
@api_auth_required("readwrite")
def create_museum_compat():
    return api_create_museum()

@app.route("/api/museums/<int:mid>", methods=["PUT"])
@api_auth_required("readwrite")
def update_museum_compat(mid):
    return api_update_museum(mid)

@app.route("/api/museums/<int:mid>", methods=["DELETE"])
@api_auth_required("admin")
def delete_museum_compat(mid):
    return api_delete_museum(mid)

@app.route("/api/aircraft_museum", methods=["POST"])
@api_auth_required("readwrite")
def link_compat():
    return api_create_exhibit()

@app.route("/api/aircraft_museum/<int:lid>", methods=["DELETE"])
@api_auth_required("admin")
def unlink_compat(lid):
    return api_delete_exhibit(lid)


# ══════════════════════════════════════════════
# API: Key management (session-auth only)
# ══════════════════════════════════════════════

@app.route("/api/v1/keys", methods=["GET"])
@login_required
def api_list_keys():
    """List current user's API keys."""
    keys = ApiKey.query.filter_by(user_id=current_user.id).all()
    return jsonify([k.to_dict() for k in keys])


@app.route("/api/v1/keys", methods=["POST"])
@login_required
@limiter.limit("10 per hour")
def api_create_key():
    """Generate a new API key for the current user.

    Optional ``expires_in_days``: set to a positive integer to auto-expire the
    key after that many days.  Omit or pass ``null`` for a key that never expires.
    """
    data = request.get_json() or {}
    label = data.get("label", "default")
    permissions = data.get("permissions", "read")
    if permissions not in ("read", "readwrite", "admin"):
        return jsonify({"error": "permissions must be 'read', 'readwrite', or 'admin'."}), 400
    if permissions == "admin" and not current_user.is_admin:
        return jsonify({"error": "Only admins can create admin-level keys."}), 403

    expires_at = None
    expires_in = data.get("expires_in_days")
    if expires_in is not None:
        try:
            days = int(expires_in)
            if days < 1:
                return jsonify({"error": "expires_in_days must be a positive integer."}), 400
            expires_at = datetime.now(timezone.utc) + timedelta(days=days)
        except (ValueError, TypeError):
            return jsonify({"error": "expires_in_days must be a positive integer."}), 400

    api_key, raw_key = ApiKey.generate(current_user.id, label=label, permissions=permissions, expires_at=expires_at)
    db.session.add(api_key)
    db.session.commit()
    auth_log.info(f"API_KEY_CREATE user={current_user.username} label={label} perms={permissions}")
    return jsonify({"key": raw_key, "id": api_key.id, "label": label, "permissions": permissions}), 201


@app.route("/api/v1/keys/<int:key_id>", methods=["DELETE"])
@login_required
def api_revoke_key(key_id):
    """Revoke (deactivate) an API key."""
    api_key = ApiKey.query.get_or_404(key_id)
    if api_key.user_id != current_user.id and not current_user.is_admin:
        abort(403)
    api_key.is_active = False
    db.session.commit()
    auth_log.info(f"API_KEY_REVOKE key_id={key_id} by={current_user.username}")
    return jsonify({"revoked": True, "id": key_id})


# ── Admin: manage keys for any user ──

@app.route("/api/v1/users/<int:user_id>/keys", methods=["GET"])
@login_required
def api_list_user_keys(user_id):
    """List API keys for a user. Admins can view any user; users can view their own."""
    if not current_user.is_admin and current_user.id != user_id:
        abort(403)
    User.query.get_or_404(user_id)
    keys = ApiKey.query.filter_by(user_id=user_id).all()
    return jsonify([k.to_dict() for k in keys])


@app.route("/api/v1/users/<int:user_id>/keys", methods=["POST"])
@login_required
def api_create_user_key(user_id):
    """Create an API key for a user. Admins can create for anyone; users can create for themselves.

    The key inherits the user's scope (museum/country assignments).
    Optional: label, permissions (read/readwrite/admin, default based on user role).
    """
    if not current_user.is_admin and current_user.id != user_id:
        abort(403)
    target_user = User.query.get_or_404(user_id)
    data = request.get_json() or {}
    label = data.get("label", "default")

    # Default permissions based on user role
    # aircraft_admin gets admin-level keys (full data CRUD); only the strict
    # 'admin' role gets user-management endpoints, which API keys can't reach
    # anyway since those use the @admin_required (session) decorator.
    role_perm_map = {"admin": "admin", "aircraft_admin": "admin",
                     "manager": "readwrite", "viewer": "read"}
    permissions = data.get("permissions", role_perm_map.get(target_user.role, "read"))

    if permissions not in ("read", "readwrite", "admin"):
        return jsonify({"error": "permissions must be 'read', 'readwrite', or 'admin'."}), 400

    # Don't allow creating admin-level keys for users whose role doesn't
    # already imply admin-level data access. Both 'admin' and 'aircraft_admin'
    # qualify (they're the two data-admin roles).
    if permissions == "admin" and target_user.role not in ("admin", "aircraft_admin"):
        return jsonify({"error": "Cannot create admin-level keys for users without an admin-level role."}), 400

    # Don't allow readwrite keys for viewers
    if permissions == "readwrite" and target_user.role == "viewer":
        return jsonify({"error": "Cannot create readwrite keys for viewer users."}), 400

    api_key, raw_key = ApiKey.generate(user_id, label=label, permissions=permissions)
    db.session.add(api_key)
    db.session.commit()
    auth_log.info(f"API_KEY_CREATE for_user={target_user.username} label={label} perms={permissions} by={current_user.username}")
    return jsonify({
        "key": raw_key,
        "id": api_key.id,
        "user_id": user_id,
        "label": label,
        "permissions": permissions,
        "note": f"Key inherits {target_user.username}'s scope ({target_user.role} role).",
    }), 201


# ══════════════════════════════════════════════
# API: User management (admin only)
# ══════════════════════════════════════════════

@app.route("/api/v1/users", methods=["GET"])
@login_required
def api_list_users():
    """List all users. Admins see all; others see only themselves."""
    if current_user.is_admin:
        # Eager-load assignments + api_keys because to_dict() needs them for
        # every row. Without this we'd fire 3 queries per user.
        users = (
            User.query
            .options(
                selectinload(User.museum_assignments),
                selectinload(User.country_assignments),
                selectinload(User.api_keys),
            )
            .order_by(User.username)
            .all()
        )
    else:
        users = [current_user]
    return jsonify([u.to_dict() for u in users])


@app.route("/api/v1/users", methods=["POST"])
@admin_required
def api_create_user():
    """Create a new user (admin only).

    Required: username, password.
    Optional: email, role (admin/manager/viewer).
    """
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    password = data.get("password", "")
    email = (data.get("email") or "").strip() or None
    role = data.get("role", "viewer")

    if not username or not password:
        return jsonify({"error": "username and password are required."}), 400
    if role not in ("admin", "aircraft_admin", "manager", "viewer"):
        return jsonify({"error": "role must be 'admin', 'aircraft_admin', 'manager', or 'viewer'."}), 400
    pw_error = _validate_password_strength(password)
    if pw_error:
        return jsonify({"error": pw_error}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken."}), 409

    user = User(username=username, email=email, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.flush()

    # Assign museums
    for mid in data.get("assigned_museums", []):
        museum = Museum.query.get(mid)
        if museum:
            db.session.add(UserMuseumAssignment(user_id=user.id, museum_id=mid))

    # Assign countries
    for country in data.get("assigned_countries", []):
        if country.strip():
            db.session.add(UserCountryAssignment(user_id=user.id, country=country.strip()))

    # Auto-generate an API key based on user role
    perm_map = {"admin": "admin", "aircraft_admin": "admin",
                "manager": "readwrite", "viewer": "read"}
    auto_perms = perm_map.get(role, "read")
    api_key_obj, raw_key = ApiKey.generate(user_id=user.id, label="auto", permissions=auto_perms)
    db.session.add(api_key_obj)

    db.session.commit()
    auth_log.info(f"USER_CREATE user={username} role={role} by={current_user.username}")
    change_log.info(f"USER_CREATE id={user.id} user={username} role={role} by={current_user.username}")
    resp = user.to_dict()
    resp["generated_api_key"] = raw_key
    return jsonify(resp), 201


@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
@login_required
def api_user_detail(user_id):
    """Get user details. Admins can view any user; others can only view themselves."""
    if not current_user.is_admin and current_user.id != user_id:
        abort(403)
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())


@app.route("/api/v1/users/<int:user_id>", methods=["PUT", "PATCH"])
@admin_required
def api_update_user(user_id):
    """Update a user (admin only). Can change role, email, active status, and assignments."""
    user = User.query.get_or_404(user_id)
    data = request.get_json() or {}

    if "email" in data:
        user.email = data["email"] or None
    if "role" in data and data["role"] in ("admin", "aircraft_admin", "manager", "viewer"):
        user.role = data["role"]
    if "is_active" in data:
        user.is_active_user = bool(data["is_active"])
    if "password" in data and data["password"]:
        pw_error = _validate_password_strength(data["password"])
        if pw_error:
            return jsonify({"error": pw_error}), 400
        user.set_password(data["password"])
        # New password = clean slate, drop any pending lockout.
        user.reset_failed_logins()

    # Replace museum assignments
    if "assigned_museums" in data:
        UserMuseumAssignment.query.filter_by(user_id=user_id).delete()
        for mid in data["assigned_museums"]:
            museum = Museum.query.get(mid)
            if museum:
                db.session.add(UserMuseumAssignment(user_id=user_id, museum_id=mid))

    # Replace country assignments
    if "assigned_countries" in data:
        UserCountryAssignment.query.filter_by(user_id=user_id).delete()
        for country in data["assigned_countries"]:
            if country.strip():
                db.session.add(UserCountryAssignment(user_id=user_id, country=country.strip()))

    db.session.commit()
    change_log.info(f"USER_UPDATE id={user_id} by={current_user.username}")
    return jsonify(user.to_dict())


@app.route("/api/v1/users/<int:user_id>", methods=["DELETE"])
@admin_required
def api_delete_user(user_id):
    """Delete a user (admin only). Cannot delete yourself."""
    if current_user.id == user_id:
        return jsonify({"error": "Cannot delete your own account."}), 400
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    change_log.info(f"USER_DELETE id={user_id} username={user.username} by={current_user.username}")
    return jsonify({"deleted": True, "id": user_id})


# ══════════════════════════════════════════════
# API documentation page
# ══════════════════════════════════════════════

@app.route("/api/v1/docs")
def api_docs():
    return render_template("api_docs.html")


# ══════════════════════════════════════════════
# Helper
# ══════════════════════════════════════════════

def _resolve_location(location_str):
    """Return (lat, lon) for a zip/postal code or city name.

    Delegates to the geocoder module which tries, in order:
      1. Database cache (zip_codes table)
      2. pgeocode — offline postal-code data for 80+ countries
      3. geopy/Nominatim — online fallback for city names & addresses

    Successful external lookups are cached in the DB automatically.
    """
    return resolve_location(location_str, db=db, ZipCode=ZipCode)


if __name__ == "__main__":
    app.run(
        host=Config.SERVER_HOST,
        port=Config.SERVER_PORT,
        debug=Config.SERVER_DEBUG,
    )
