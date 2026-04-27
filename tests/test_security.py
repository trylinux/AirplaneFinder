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
