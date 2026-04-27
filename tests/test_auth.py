"""End-to-end auth flow: login, logout, lockout, session timeouts.

The bug we kept reintroducing: ``session.clear()`` after ``logout_user()``
wiped Flask-Login's ``_remember = "clear"`` signal, so the remember-me
cookie survived and the user was silently re-authenticated on the next
request. ``test_logout_actually_logs_out_with_remember_cookie`` and the
two timeout tests are specifically there to catch that.
"""

from datetime import datetime, timedelta, timezone

import pytest


# ─────────────────────────────────────────────────────────────────────
# Login / logout
# ─────────────────────────────────────────────────────────────────────

class TestLogin:

    def test_login_succeeds_with_correct_password(self, app, admin_user):
        client = app.test_client()
        r = client.post(
            "/login",
            data={"username": admin_user.username, "password": "Tester-1234"},
            follow_redirects=False,
        )
        assert r.status_code in (301, 302)

    def test_login_issues_remember_token_cookie(self, app, admin_user):
        client = app.test_client()
        client.post("/login",
                    data={"username": admin_user.username, "password": "Tester-1234"})
        # Flask-Login's remember cookie is named ``remember_token`` by default.
        assert client.get_cookie("remember_token") is not None

    def test_login_fails_with_wrong_password(self, app, admin_user):
        client = app.test_client()
        r = client.post("/login",
                        data={"username": admin_user.username, "password": "wrong-1234"},
                        follow_redirects=False)
        # Stays on /login, no redirect.
        assert r.status_code == 200

    def test_login_fails_for_unknown_user(self, app, db_session):
        client = app.test_client()
        r = client.post("/login",
                        data={"username": "nope", "password": "Tester-1234"},
                        follow_redirects=False)
        assert r.status_code == 200

    def test_authenticated_request_returns_200(self, admin_client):
        r = admin_client.get("/account", follow_redirects=False)
        assert r.status_code == 200


class TestLogout:

    def test_logout_redirects_to_login(self, admin_client):
        r = admin_client.get("/logout", follow_redirects=False)
        assert r.status_code in (301, 302)
        assert "/login" in r.headers["Location"]

    def test_logout_emits_cookie_expiring_set_cookie(self, admin_client):
        """The Set-Cookie that expires the remember token must reach the
        browser. Without this, Flask-Login auto-re-authenticates from the
        still-valid cookie on the next request."""
        r = admin_client.get("/logout", follow_redirects=False)
        set_cookies = r.headers.get_all("Set-Cookie")
        delete_remember = any(
            "remember_token=" in v
            and ("Expires=Thu, 01 Jan 1970" in v or "Max-Age=0" in v)
            for v in set_cookies
        )
        assert delete_remember, (
            "logout did not expire remember_token; Set-Cookie headers were:\n  "
            + "\n  ".join(set_cookies)
        )

    def test_logout_actually_logs_out_with_remember_cookie(self, admin_client):
        """THE regression test. Logout, then hit a @login_required endpoint
        — must redirect to /login, NOT silently return 200."""
        admin_client.get("/logout")
        r = admin_client.get("/account", follow_redirects=False)
        assert r.status_code in (301, 302), (
            f"post-logout /account expected redirect, got {r.status_code}; "
            "Flask-Login probably re-authenticated via remember cookie."
        )
        assert "/login" in r.headers["Location"]

    def test_logout_clears_session_keys(self, admin_client):
        admin_client.get("/logout")
        with admin_client.session_transaction() as s:
            assert "_user_id" not in s
            assert "login_time" not in s
            assert "last_activity" not in s


# ─────────────────────────────────────────────────────────────────────
# Failed-login lockout
# ─────────────────────────────────────────────────────────────────────

class TestLockout:

    def test_lockout_after_threshold_failed_attempts(self, app, admin_user, db_session):
        """5th failed attempt locks the account."""
        from config import Config
        threshold = Config.LOGIN_LOCKOUT_MAX_ATTEMPTS
        client = app.test_client()
        for _ in range(threshold):
            client.post("/login",
                        data={"username": admin_user.username, "password": "wrong"},
                        follow_redirects=False)
        db_session.refresh(admin_user)
        assert admin_user.is_locked, "account should be locked after threshold failures"
        assert admin_user.failed_login_count >= threshold

    def test_correct_password_during_lockout_is_rejected(self, app, admin_user, db_session):
        """Lockout check runs before password check, so even the right
        password gets a 'try again later' response while locked."""
        from config import Config
        admin_user.locked_until = datetime.now(timezone.utc) + timedelta(seconds=600)
        admin_user.failed_login_count = Config.LOGIN_LOCKOUT_MAX_ATTEMPTS
        db_session.commit()

        client = app.test_client()
        r = client.post("/login",
                        data={"username": admin_user.username, "password": "Tester-1234"},
                        follow_redirects=False)
        assert r.status_code == 200, (
            "locked account login expected 200 (re-render with flash), "
            f"got {r.status_code} — possibly an unexpected redirect"
        )

    def test_successful_login_clears_lockout(self, app, admin_user, db_session):
        """After the lock window passes, a correct password resets
        failed_login_count to 0."""
        admin_user.locked_until = datetime.now(timezone.utc) - timedelta(seconds=1)
        admin_user.failed_login_count = 5
        db_session.commit()

        client = app.test_client()
        client.post("/login",
                    data={"username": admin_user.username, "password": "Tester-1234"})
        db_session.refresh(admin_user)
        assert admin_user.failed_login_count == 0
        assert admin_user.locked_until is None


# ─────────────────────────────────────────────────────────────────────
# Session timeouts
# ─────────────────────────────────────────────────────────────────────

class TestSessionTimeout:
    """Both branches (idle + absolute) must:
       1. Redirect to /login.
       2. Emit a Set-Cookie that expires remember_token.
       3. Result in a *truly* anonymous follow-up request (the historical
          regression: redirect happened, but next request was
          re-authenticated from the surviving remember cookie).
    """

    def test_idle_timeout_evicts_user(self, admin_client):
        # Push last_activity 30 minutes back. Default admin idle is 15 min.
        with admin_client.session_transaction() as s:
            s["last_activity"] = (datetime.now(timezone.utc) - timedelta(minutes=30)).isoformat()

        r = admin_client.get("/account", follow_redirects=False)
        assert r.status_code in (301, 302)
        assert "/login" in r.headers["Location"]

        # remember_token must be expired in the response
        delete_remember = any(
            "remember_token=" in v and ("Max-Age=0" in v or "Expires=Thu, 01 Jan 1970" in v)
            for v in r.headers.get_all("Set-Cookie")
        )
        assert delete_remember, (
            "idle timeout did not expire remember_token — user will be "
            "silently re-authenticated on next request"
        )

        # Next request must be anonymous
        r = admin_client.get("/account", follow_redirects=False)
        assert r.status_code in (301, 302), (
            "post-timeout /account did not redirect — Flask-Login likely "
            "re-authenticated from the surviving remember cookie"
        )

    def test_absolute_timeout_evicts_user(self, admin_client):
        # Push login_time back further than SESSION_ABSOLUTE_TIMEOUT (default 12h).
        with admin_client.session_transaction() as s:
            s["login_time"] = (datetime.now(timezone.utc) - timedelta(hours=13)).isoformat()

        r = admin_client.get("/account", follow_redirects=False)
        assert r.status_code in (301, 302)
        assert "/login" in r.headers["Location"]

        # remember_token must be expired in the response
        assert any(
            "remember_token=" in v and ("Max-Age=0" in v or "Expires=Thu, 01 Jan 1970" in v)
            for v in r.headers.get_all("Set-Cookie")
        )
        # Next request anonymous
        r = admin_client.get("/account", follow_redirects=False)
        assert r.status_code in (301, 302)


# ─────────────────────────────────────────────────────────────────────
# Session fixation defense
# ─────────────────────────────────────────────────────────────────────

class TestSessionFixation:

    def test_login_clears_pre_existing_session_state(self, app, admin_user):
        """An attacker-planted session cookie value should NOT persist
        across login. We verify by stuffing a custom key into the session
        before login and checking it's gone after."""
        client = app.test_client()
        # Make a request first so the client has a session cookie.
        client.get("/")
        with client.session_transaction() as s:
            s["attacker_planted"] = "should-be-wiped"

        client.post("/login",
                    data={"username": admin_user.username, "password": "Tester-1234"})
        with client.session_transaction() as s:
            assert "attacker_planted" not in s, (
                "login did not clear pre-existing session — session-fixation defense failed"
            )
