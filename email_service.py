"""Transactional email delivery through Brevo's HTTPS API."""

from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from config import Config

BREVO_SEND_URL = "https://api.brevo.com/v3/smtp/email"


class EmailDeliveryError(RuntimeError):
    """Raised when a transactional message could not be accepted by Brevo."""


def email_is_configured() -> bool:
    """Return whether every setting needed to send safe absolute links exists."""
    configured = all(
        (
            getattr(Config, "BREVO_API_KEY", ""),
            getattr(Config, "EMAIL_SENDER", ""),
            getattr(Config, "PUBLIC_BASE_URL", ""),
        )
    )
    if not configured:
        return False
    public_url = urlparse(Config.PUBLIC_BASE_URL)
    return (
        public_url.scheme == "https"
        and bool(public_url.netloc)
        and not public_url.username
        and not public_url.password
    )


def send_transactional_email(
    *,
    to_email: str,
    to_name: str,
    subject: str,
    html_content: str,
    text_content: str,
    tag: str,
) -> str:
    """Send one message and return Brevo's provider message ID."""
    if not email_is_configured():
        raise EmailDeliveryError("Transactional email is not fully configured.")

    payload = {
        "sender": {"email": Config.EMAIL_SENDER, "name": Config.EMAIL_SENDER_NAME},
        "to": [{"email": to_email, "name": to_name}],
        "subject": subject,
        "htmlContent": html_content,
        "textContent": text_content,
        "tags": [tag],
    }
    request = Request(
        BREVO_SEND_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "accept": "application/json",
            "api-key": Config.BREVO_API_KEY,
            "content-type": "application/json",
        },
        method="POST",
    )

    try:
        # The URL is a constant HTTPS Brevo endpoint, not caller-controlled.
        with urlopen(request, timeout=Config.EMAIL_TIMEOUT) as response:  # nosec B310
            result = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read(512).decode("utf-8", errors="replace")
        raise EmailDeliveryError(
            f"Brevo rejected the message with HTTP {exc.code}: {detail}"
        ) from exc
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        raise EmailDeliveryError(f"Brevo request failed: {type(exc).__name__}") from exc

    message_id = result.get("messageId") if isinstance(result, dict) else None
    if not message_id:
        raise EmailDeliveryError("Brevo accepted the request without a message ID.")
    return str(message_id)
