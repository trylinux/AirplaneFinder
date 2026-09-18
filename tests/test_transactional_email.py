"""Registration verification, password reset, and Brevo delivery tests."""

from __future__ import annotations

import json

import pytest


@pytest.fixture
def configured_email(monkeypatch):
    from config import Config

    monkeypatch.setattr(Config, "BREVO_API_KEY", "test-brevo-key")
    monkeypatch.setattr(Config, "EMAIL_SENDER", "no-reply@airplane.test")
    monkeypatch.setattr(Config, "EMAIL_SENDER_NAME", "Aircraft Finder")
    monkeypatch.setattr(Config, "PUBLIC_BASE_URL", "https://airplane.test")
    monkeypatch.setattr(Config, "EMAIL_TIMEOUT", 2.0)
    monkeypatch.setattr(Config, "EMAIL_VERIFY_MAX_AGE", 86400)
    monkeypatch.setattr(Config, "PASSWORD_RESET_MAX_AGE", 3600)


@pytest.fixture
def captured_email(monkeypatch, configured_email):
    import app as appmod

    messages = []

    def fake_send(**message):
        messages.append(message)
        return f"message-{len(messages)}"

    monkeypatch.setattr(appmod, "send_transactional_email", fake_send)
    return messages


def _register(client, email="Pilot@Example.com"):
    return client.post(
        "/register",
        data={
            "username": "new_pilot",
            "email": email,
            "password": "Strong-pass-123",
            "password2": "Strong-pass-123",
        },
        follow_redirects=False,
    )


class TestRegistrationVerification:
    def test_configured_registration_requires_email(self, client, captured_email):
        response = _register(client, email="")
        assert response.status_code == 200
        assert b"Email is required" in response.data
        assert captured_email == []

    def test_registration_normalizes_and_sends_without_login(
        self, client, db_session, captured_email
    ):
        import models

        response = _register(client)
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/login")
        user = models.User.query.filter_by(username="new_pilot").one()
        assert user.email == "pilot@example.com"
        assert user.email_verification_required is True
        assert user.email_verified_at is None
        assert len(captured_email) == 1
        assert captured_email[0]["tag"] == "email-verification"
        assert "https://airplane.test/verify-email?token=" in captured_email[0]["html_content"]
        with client.session_transaction() as flask_session:
            assert "_user_id" not in flask_session

    def test_duplicate_email_is_rejected_case_insensitively(
        self, client, db_session, captured_email
    ):
        import models

        user = models.User(username="existing", email="pilot@example.com", role="viewer")
        user.set_password("Strong-pass-123")
        db_session.add(user)
        db_session.commit()
        response = _register(client, email="PILOT@example.com")
        assert response.status_code == 200
        assert b"account with that email already exists" in response.data
        assert captured_email == []

    def test_unverified_user_cannot_login(self, client, db_session):
        import models

        user = models.User(
            username="waiting",
            email="waiting@example.com",
            email_verification_required=True,
            role="viewer",
        )
        user.set_password("Strong-pass-123")
        db_session.add(user)
        db_session.commit()
        response = client.post(
            "/login", data={"username": "waiting", "password": "Strong-pass-123"}
        )
        assert response.status_code == 200
        assert b"verify your email" in response.data

    def test_verification_requires_post_and_activates_login(
        self, client, db_session
    ):
        import app as appmod
        import models

        user = models.User(
            username="waiting",
            email="waiting@example.com",
            email_verification_required=True,
            role="viewer",
        )
        user.set_password("Strong-pass-123")
        db_session.add(user)
        db_session.commit()
        token = appmod._make_email_token(user, "verify")

        get_response = client.get("/verify-email", query_string={"token": token})
        assert get_response.status_code == 200
        db_session.refresh(user)
        assert user.email_verification_required is True

        post_response = client.post("/verify-email", data={"token": token})
        assert post_response.status_code == 302
        db_session.refresh(user)
        assert user.email_verification_required is False
        assert user.email_verified_at is not None

    def test_tampered_verification_token_is_rejected(self, client):
        response = client.get("/verify-email", query_string={"token": "invalid"})
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/resend-verification")

    def test_expired_verification_token_is_rejected(
        self, client, viewer_user, monkeypatch, configured_email
    ):
        import app as appmod
        from config import Config

        token = appmod._make_email_token(viewer_user, "verify")
        monkeypatch.setattr(Config, "EMAIL_VERIFY_MAX_AGE", -1)
        response = client.get("/verify-email", query_string={"token": token})
        assert response.status_code == 302


class TestPasswordReset:
    def test_request_is_generic_for_known_and_unknown_users(
        self, client, viewer_user, captured_email
    ):
        known = client.post(
            "/forgot-password", data={"email": viewer_user.email}, follow_redirects=True
        )
        unknown = client.post(
            "/forgot-password", data={"email": "missing@example.com"}, follow_redirects=True
        )
        expected = b"If an active account uses that address"
        assert expected in known.data
        assert expected in unknown.data
        assert len(captured_email) == 1
        assert captured_email[0]["tag"] == "password-reset"

    def test_reset_changes_password_invalidates_token_and_existing_session(
        self, app, admin_client, admin_user, db_session, configured_email
    ):
        import app as appmod

        token = appmod._make_email_token(admin_user, "reset")
        reset_client = app.test_client()
        response = reset_client.post(
            "/reset-password",
            data={
                "token": token,
                "password": "New-password-456",
                "password2": "New-password-456",
            },
        )
        assert response.status_code == 302
        db_session.refresh(admin_user)
        assert admin_user.check_password("New-password-456")
        assert admin_user.auth_version == 1

        reused = reset_client.get("/reset-password", query_string={"token": token})
        assert reused.status_code == 302
        assert reused.headers["Location"].endswith("/forgot-password")
        old_session = admin_client.get("/account")
        assert old_session.status_code == 302

    def test_mismatched_passwords_do_not_consume_token(
        self, client, viewer_user, configured_email
    ):
        import app as appmod

        token = appmod._make_email_token(viewer_user, "reset")
        response = client.post(
            "/reset-password",
            data={
                "token": token,
                "password": "New-password-456",
                "password2": "Different-789",
            },
        )
        assert response.status_code == 200
        assert b"Passwords do not match" in response.data
        assert viewer_user.check_password("Tester-1234")

    def test_expired_reset_token_is_rejected(
        self, client, viewer_user, monkeypatch, configured_email
    ):
        import app as appmod
        from config import Config

        token = appmod._make_email_token(viewer_user, "reset")
        monkeypatch.setattr(Config, "PASSWORD_RESET_MAX_AGE", -1)
        response = client.get("/reset-password", query_string={"token": token})
        assert response.status_code == 302
        assert response.headers["Location"].endswith("/forgot-password")

    def test_sensitive_pages_are_not_cached_and_mobile_template_renders(
        self, client, configured_email
    ):
        response = client.get(
            "/forgot-password",
            headers={"User-Agent": "Mozilla/5.0 (iPhone; Mobile Safari)"},
        )
        assert response.status_code == 200
        assert response.headers["Cache-Control"] == "no-store"
        assert response.headers["Referrer-Policy"] == "no-referrer"
        assert b'class="m-card"' in response.data


class TestBrevoClient:
    def test_posts_expected_payload_and_returns_message_id(
        self, monkeypatch, configured_email
    ):
        import email_service

        captured = {}

        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self):
                return b'{"messageId":"brevo-message-id"}'

        def fake_urlopen(request, timeout):
            captured["request"] = request
            captured["timeout"] = timeout
            return FakeResponse()

        monkeypatch.setattr(email_service, "urlopen", fake_urlopen)
        message_id = email_service.send_transactional_email(
            to_email="pilot@example.com",
            to_name="Pilot",
            subject="Test",
            html_content="<p>Test</p>",
            text_content="Test",
            tag="test-message",
        )
        assert message_id == "brevo-message-id"
        assert captured["timeout"] == 2.0
        payload = json.loads(captured["request"].data)
        assert payload["to"] == [{"email": "pilot@example.com", "name": "Pilot"}]
        assert payload["tags"] == ["test-message"]
        assert dict(captured["request"].header_items())["Api-key"] == "test-brevo-key"
