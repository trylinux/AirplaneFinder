"""scripts/airplane_api.py — base-URL normalization.

`AIRPLANE_BASE_URL=airplane.museum` (no scheme) used to fail deep inside
requests' prepare_url with a MissingSchema traceback that pointed at the
HTTP layer rather than at the one-token typo that caused it. The client
now fills the scheme in.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))


@pytest.fixture
def Client():
    from airplane_api import AirplaneClient
    return AirplaneClient


class TestNormalizeBaseUrl:

    @pytest.mark.parametrize("raw,expected", [
        ("airplane.museum",          "https://airplane.museum"),
        ("airplane.museum/",         "https://airplane.museum"),
        ("  airplane.museum  ",      "https://airplane.museum"),
        ("airplane.museum:8443",     "https://airplane.museum:8443"),
        ("example.com/api",          "https://example.com/api"),
    ])
    def test_schemeless_public_host_gets_https(self, Client, raw, expected):
        assert Client.normalize_base_url(raw) == expected

    @pytest.mark.parametrize("raw,expected", [
        ("localhost:5000",   "http://localhost:5000"),
        ("127.0.0.1:5000",   "http://127.0.0.1:5000"),
        ("localhost",        "http://localhost"),
        ("0.0.0.0:8000",     "http://0.0.0.0:8000"),
    ])
    def test_schemeless_local_host_gets_http(self, Client, raw, expected):
        """Local dev servers rarely have a TLS certificate; defaulting them
        to https would break every localhost run."""
        assert Client.normalize_base_url(raw) == expected

    @pytest.mark.parametrize("raw", [
        "https://airplane.museum",
        "http://127.0.0.1:5000",
        "http://airplane.museum",
    ])
    def test_explicit_scheme_is_left_alone(self, Client, raw):
        assert Client.normalize_base_url(raw) == raw.rstrip("/")

    def test_trailing_slash_stripped(self, Client):
        assert Client.normalize_base_url("https://airplane.museum/") == \
            "https://airplane.museum"

    @pytest.mark.parametrize("raw", ["", "   ", None])
    def test_empty_falls_back_to_default(self, Client, raw):
        assert Client.normalize_base_url(raw) == Client.DEFAULT_BASE_URL


class TestClientUsesNormalizedUrl:

    def test_constructor_normalizes(self, Client):
        assert Client(base_url="airplane.museum").base_url == \
            "https://airplane.museum"

    def test_env_var_normalized(self, Client, monkeypatch):
        monkeypatch.setenv("AIRPLANE_BASE_URL", "airplane.museum")
        assert Client().base_url == "https://airplane.museum"

    def test_request_builds_a_valid_absolute_url(self, Client, monkeypatch):
        """The original failure: a schemeless base produced
        'airplane.museum/api/v1/aircraft/search', which requests rejects."""
        captured = {}

        class FakeResp:
            ok = True
            status_code = 200
            content = b"{}"
            def json(self): return {}

        c = Client(base_url="airplane.museum")

        def fake_request(method, url, **kw):
            captured["url"] = url
            return FakeResp()

        monkeypatch.setattr(c._session, "request", fake_request)
        c.get("/api/v1/aircraft/search")
        assert captured["url"] == "https://airplane.museum/api/v1/aircraft/search"
        assert "://" in captured["url"]
