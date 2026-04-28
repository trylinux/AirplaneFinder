"""Security hardening — headers, redirect protection, secret-key guard.

These tests defend the configurations that turn a working app into a safe
one. Most of them flip ``SECURITY_HEADERS_ENABLED`` to True for the test —
the conftest disables it by default so every other test doesn't have to
think about it.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────
# Response headers
# ─────────────────────────────────────────────────────────────────────

class TestSecurityHeaders:
    """Each header has a specific reason. Document the reason in the test
    name so a future reader gets a free explanation of why we set it."""

    @pytest.fixture
    def hdrs(self, app, db_session):
        # _add_security_headers reads Config.SECURITY_HEADERS_ENABLED
        # at request time, NOT app.config[...]. Flip the class attr.
        import config
        config.Config.SECURITY_HEADERS_ENABLED = True
        client = app.test_client()
        r = client.get("/")
        return {k.lower(): v for k, v in r.headers.items()}

    def test_x_frame_options_blocks_clickjacking(self, hdrs):
        # DENY (not SAMEORIGIN) — we don't iframe ourselves.
        assert hdrs["x-frame-options"] == "DENY"

    def test_x_content_type_options_blocks_mime_sniffing(self, hdrs):
        assert hdrs["x-content-type-options"] == "nosniff"

    def test_referrer_policy_avoids_leaking_full_urls(self, hdrs):
        assert hdrs["referrer-policy"] == "strict-origin-when-cross-origin"

    def test_permissions_policy_disables_unused_apis(self, hdrs):
        # Tightens the surface against compromised JS that tries to grab
        # geolocation/camera/etc. We don't use any of these, so deny all.
        pp = hdrs["permissions-policy"]
        for feature in ("geolocation=()", "camera=()", "microphone=()"):
            assert feature in pp, f"missing {feature} in {pp}"

    def test_csp_present_with_frame_ancestors_none(self, hdrs):
        csp = hdrs["content-security-policy"]
        assert "default-src 'self'" in csp
        assert "frame-ancestors 'none'" in csp
        assert "object-src 'none'" in csp
        assert "form-action 'self'" in csp

    def test_csp_allows_jsdelivr_for_globe_geojson(self, hdrs):
        # The desktop and mobile globe both fetch country borders from
        # cdn.jsdelivr.net — connect-src must allow it or those views break.
        csp = hdrs["content-security-policy"]
        assert "https://cdn.jsdelivr.net" in csp

    def test_script_src_no_unsafe_inline(self, hdrs):
        """The whole point of the nonce: 'unsafe-inline' is gone from
        script-src. An XSS-injected <script> can't execute because it
        won't have a nonce, and 'unsafe-inline' isn't there to bail it out."""
        csp = hdrs["content-security-policy"]
        # Find just the script-src directive (not other directives that
        # legitimately keep 'unsafe-inline').
        script_src = next(
            (d.strip() for d in csp.split(";") if d.strip().startswith("script-src")),
            "",
        )
        assert script_src, f"script-src directive missing from CSP: {csp}"
        assert "'unsafe-inline'" not in script_src, (
            f"script-src still has 'unsafe-inline' — XSS would execute "
            f"freely. Directive was: {script_src}"
        )

    def test_script_src_uses_a_nonce(self, hdrs):
        csp = hdrs["content-security-policy"]
        script_src = next(d for d in csp.split(";") if d.strip().startswith("script-src"))
        assert "'nonce-" in script_src, (
            f"script-src missing nonce — inline scripts won't execute. "
            f"Directive was: {script_src}"
        )

    def test_hsts_only_on_https(self, hdrs):
        # The test client is plain HTTP — HSTS would be wasted and some
        # browsers complain about it on bare HTTP responses.
        assert "strict-transport-security" not in hdrs

    def test_hsts_emitted_on_https(self, app, db_session):
        """Set X-Forwarded-Proto: https (typical reverse-proxy header) and
        verify HSTS now ships."""
        import config
        config.Config.SECURITY_HEADERS_ENABLED = True
        client = app.test_client()
        r = client.get("/", headers={"X-Forwarded-Proto": "https"})
        hsts = r.headers.get("Strict-Transport-Security")
        assert hsts is not None and "max-age=" in hsts


# ─────────────────────────────────────────────────────────────────────
# Open-redirect protection on ?next=
# ─────────────────────────────────────────────────────────────────────

class TestOpenRedirectProtection:
    """Login does ``redirect(_safe_next_url(request.args.get('next')) or
    fallback)``. Anything cross-origin must be dropped."""

    def test_external_next_is_silently_ignored(self, app, admin_user):
        """``?next=https://evil.com/phish`` must NOT redirect to evil.com."""
        client = app.test_client()
        r = client.post(
            "/login?next=https://evil.com/phish",
            data={"username": admin_user.username, "password": "Tester-1234"},
            follow_redirects=False,
        )
        assert r.status_code in (301, 302)
        assert "evil.com" not in r.headers["Location"]

    def test_relative_next_is_honored(self, app, admin_user):
        client = app.test_client()
        r = client.post(
            "/login?next=/account",
            data={"username": admin_user.username, "password": "Tester-1234"},
            follow_redirects=False,
        )
        assert r.status_code in (301, 302)
        assert "/account" in r.headers["Location"]

    def test_javascript_scheme_in_next_is_dropped(self, app, admin_user):
        """A successful redirect to ``javascript:alert(1)`` would execute JS
        in our origin's context — XSS via redirect."""
        client = app.test_client()
        r = client.post(
            "/login?next=javascript:alert(1)",
            data={"username": admin_user.username, "password": "Tester-1234"},
            follow_redirects=False,
        )
        assert r.status_code in (301, 302)
        loc = r.headers["Location"]
        assert "javascript:" not in loc.lower()


# ─────────────────────────────────────────────────────────────────────
# CSP nonce — emitted in header AND embedded in rendered HTML
# ─────────────────────────────────────────────────────────────────────

import re


class TestCspNonce:
    """For nonce-based CSP to actually work, two invariants must hold:
       1. Every legitimate inline <script> in the rendered HTML must carry
          the nonce that was emitted in the response's CSP header.
       2. The nonce must change per request (otherwise a cached nonce is
          a forgeable nonce — defeats the whole point).
    """

    @pytest.fixture
    def headered_client(self, app, db_session):
        """Test client that runs through the security-headers hook."""
        import config
        config.Config.SECURITY_HEADERS_ENABLED = True
        return app.test_client()

    def _extract_nonce_from_csp(self, response):
        """Pull the nonce-XXX value out of a CSP header. Returns the raw
        nonce string ('XXX'), or None if no nonce in script-src."""
        csp = response.headers.get("Content-Security-Policy", "")
        m = re.search(r"'nonce-([^']+)'", csp)
        return m.group(1) if m else None

    def test_response_includes_nonce_in_script_src(self, headered_client):
        r = headered_client.get("/")
        nonce = self._extract_nonce_from_csp(r)
        assert nonce, "no nonce in script-src directive of CSP header"
        # Should be a non-trivial random value (token_urlsafe(16) → 22 chars).
        assert len(nonce) >= 16

    def test_inline_script_in_html_carries_matching_nonce(self, headered_client):
        """The rendered page should have at least one <script nonce="…">
        tag where the nonce matches what's in the CSP header. If they
        don't match, the inline script will be blocked by the browser."""
        r = headered_client.get("/")
        nonce = self._extract_nonce_from_csp(r)
        body = r.get_data(as_text=True)
        # At least one inline <script nonce="<the-nonce-from-csp>">
        # Hoist the regex into a variable: f-strings can't contain backslashes
        # inside the {} placeholder on Python 3.10.
        actual_nonces = re.findall(r'<script[^>]+nonce="([^"]+)"', body)[:3]
        assert f'nonce="{nonce}"' in body, (
            f"rendered HTML doesn't carry the CSP nonce on any inline script. "
            f"CSP nonce was {nonce!r}; nonce attributes in body: {actual_nonces}"
        )

    def test_nonce_rotates_per_request(self, headered_client):
        """Same client, two requests, two different nonces."""
        n1 = self._extract_nonce_from_csp(headered_client.get("/"))
        n2 = self._extract_nonce_from_csp(headered_client.get("/"))
        assert n1 and n2 and n1 != n2, (
            f"nonce did NOT rotate across requests: {n1!r} == {n2!r}. "
            "A static nonce is no better than 'unsafe-inline'."
        )

    def test_no_inline_script_lacks_nonce(self):
        """Static check across every template: every inline <script> tag
        (no src=) must carry nonce="{{ csp_nonce }}". If a new template
        ever adds a bare <script> tag, this fails the build."""
        import os, glob
        # Crude but effective: open each template, find <script> tags, and
        # for any without src=, require nonce="{{ csp_nonce }}".
        offenders = []
        templates_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "templates"
        )
        for path in glob.glob(os.path.join(templates_dir, "**", "*.html"),
                              recursive=True):
            with open(path) as f:
                contents = f.read()
            # Match <script ...> opening tags. Skip closing </script>.
            for m in re.finditer(r"<script\b([^>]*)>", contents):
                attrs = m.group(1)
                if "src=" in attrs:
                    continue   # external script — uses URL allowlist instead
                if 'nonce="{{ csp_nonce }}"' not in attrs:
                    offenders.append((path, m.group(0)))
        assert not offenders, (
            "inline <script> tag(s) missing nonce attribute:\n  " +
            "\n  ".join(f"{p}: {tag}" for p, tag in offenders)
        )


# ─────────────────────────────────────────────────────────────────────
# Default SECRET_KEY refuses to boot in production
# ─────────────────────────────────────────────────────────────────────

class TestSecretKeyGuard:
    """If someone forgets to set SECRET_KEY in production, sessions are
    forgeable and any user can be impersonated. create_app() should
    refuse to start in that case."""

    def test_default_secret_key_raises_outside_debug(self):
        import config
        import app as appmod
        original_key = config.Config.SECRET_KEY
        original_debug = config.Config.SERVER_DEBUG
        try:
            config.Config.SECRET_KEY = appmod._DEFAULT_SECRET_KEY
            config.Config.SERVER_DEBUG = False
            with pytest.raises(RuntimeError, match="SECRET_KEY"):
                appmod.create_app()
        finally:
            config.Config.SECRET_KEY = original_key
            config.Config.SERVER_DEBUG = original_debug

    def test_default_secret_key_warns_but_allows_debug(self):
        """In debug mode we just warn — devs shouldn't have to set a
        secret to spin up locally."""
        import config
        import app as appmod
        original_key = config.Config.SECRET_KEY
        original_debug = config.Config.SERVER_DEBUG
        try:
            config.Config.SECRET_KEY = appmod._DEFAULT_SECRET_KEY
            config.Config.SERVER_DEBUG = True
            # Should not raise.
            new_app = appmod.create_app()
            assert new_app is not None
        finally:
            config.Config.SECRET_KEY = original_key
            config.Config.SERVER_DEBUG = original_debug
