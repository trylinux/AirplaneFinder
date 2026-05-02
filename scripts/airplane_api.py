"""Tiny Python client for the Aircraft Finder REST API.

Used by the other scripts in this directory; also fine to ``import`` from
your own one-off tools. Everything is just thin wrappers around the public
``/api/v1/*`` endpoints — no Flask app imports, no DB access — so scripts
work against a remote deployment as well as localhost.

Usage
-----

    from airplane_api import AirplaneClient

    client = AirplaneClient()                          # uses env vars
    print(client.stats())

    for aircraft in client.iter_aircraft():            # auto-paginated
        print(aircraft["full_designation"])

    # Auth needed for write operations:
    client = AirplaneClient(api_key="amt_...")
    report = client.bulk_import_aircraft(
        data=open("scripts/sample_aircraft.csv").read(),
        fmt="csv",
        dry_run=True,
    )

Environment variables (used as defaults)
----------------------------------------
    AIRPLANE_BASE_URL    Base URL of the API. Default: http://127.0.0.1:5000
    AIRPLANE_API_KEY     Bearer API key for write/admin operations.
"""

from __future__ import annotations

import os
from typing import Iterator, Optional

import requests


class ApiError(RuntimeError):
    """Raised on any non-2xx response from the API. ``status`` carries the
    HTTP status code and ``payload`` the parsed JSON body (or the raw text
    if the body wasn't valid JSON)."""

    def __init__(self, status: int, payload, url: str):
        self.status = status
        self.payload = payload
        self.url = url
        msg = payload.get("error") if isinstance(payload, dict) else str(payload)
        super().__init__(f"{status} from {url}: {msg}")


class AirplaneClient:
    """Thin requests wrapper. One instance is fine to share across many
    calls — it reuses the underlying urllib3 connection pool."""

    DEFAULT_BASE_URL = "http://127.0.0.1:5000"

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self.base_url = (base_url or os.environ.get("AIRPLANE_BASE_URL")
                         or self.DEFAULT_BASE_URL).rstrip("/")
        self.api_key = api_key or os.environ.get("AIRPLANE_API_KEY")
        self.timeout = timeout
        self._session = requests.Session()
        if self.api_key:
            self._session.headers["Authorization"] = f"Bearer {self.api_key}"

    # ── Low-level helpers ──────────────────────────────────────────

    def _request(self, method: str, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        # Long timeouts are usually a deployment smell, not a feature — we
        # surface them rather than hang. Override per-call if you really
        # need to (e.g. on a 5000-row bulk import over a slow link).
        kwargs.setdefault("timeout", self.timeout)
        resp = self._session.request(method, url, **kwargs)
        if not resp.ok:
            try:
                payload = resp.json()
            except ValueError:
                payload = resp.text
            raise ApiError(resp.status_code, payload, url)
        if resp.status_code == 204 or not resp.content:
            return None
        return resp.json()

    def get(self, path, **params):
        return self._request("GET", path, params=params)

    def post(self, path, json=None, **kwargs):
        return self._request("POST", path, json=json, **kwargs)

    def put(self, path, json=None, **kwargs):
        return self._request("PUT", path, json=json, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)

    # ── Read endpoints (no auth needed) ────────────────────────────

    def stats(self):
        """Dashboard counts: aircraft / museums / exhibits / countries."""
        return self.get("/api/v1/stats")

    def search_aircraft(self, q="", page=1, per_page=20, sort_by=None, sort_dir="asc"):
        params = {"q": q, "page": page, "per_page": per_page}
        if sort_by:
            params["sort_by"] = sort_by
            params["sort_dir"] = sort_dir
        return self.get("/api/v1/aircraft/search", **params)

    def iter_aircraft(self, q="", per_page=100, **sort):
        """Yield every aircraft page-by-page. ``per_page`` capped at 100
        server-side. Useful for full exports."""
        return self._iter_paginated("/api/v1/aircraft/search",
                                    q=q, per_page=per_page, **sort)

    def get_aircraft(self, aircraft_id: int):
        """Aircraft + the museums where it's on display (each carrying link_id)."""
        return self.get(f"/api/v1/aircraft/{aircraft_id}")

    def search_museums(self, q="", region="", page=1, per_page=20,
                       sort_by=None, sort_dir="asc"):
        params = {"q": q, "region": region, "page": page, "per_page": per_page}
        if sort_by:
            params["sort_by"] = sort_by
            params["sort_dir"] = sort_dir
        return self.get("/api/v1/museums/search", **params)

    def iter_museums(self, q="", region="", per_page=100, **sort):
        return self._iter_paginated("/api/v1/museums/search",
                                    q=q, region=region, per_page=per_page, **sort)

    def get_museum(self, museum_id: int):
        return self.get(f"/api/v1/museums/{museum_id}")

    def find_nearest(self, aircraft: str, location: str, museum: str = "",
                     limit: int = 5):
        params = {"aircraft": aircraft, "location": location, "limit": limit}
        if museum:
            params["museum"] = museum
        return self.get("/api/v1/nearest", **params)

    # ── Bulk import (write — needs Bearer key) ─────────────────────

    def bulk_import_aircraft(self, *, data: str, fmt: str = "auto",
                             dry_run: bool = False):
        """POST raw CSV/JSON text to the aircraft bulk-import endpoint.

        ``fmt`` is "csv", "json", or "auto" (the server detects from the
        first character). Returns the per-row report dict."""
        return self.post("/api/v1/aircraft/bulk_import",
                         json={"format": fmt, "data": data, "dry_run": dry_run})

    def bulk_import_museums(self, *, data: str, fmt: str = "auto",
                            dry_run: bool = False):
        return self.post("/api/v1/museums/bulk_import",
                         json={"format": fmt, "data": data, "dry_run": dry_run})

    # ── Internal pagination iterator ───────────────────────────────

    def _iter_paginated(self, path: str, **base_params) -> Iterator[dict]:
        """Walk every page of a /search endpoint and yield items. Stops
        when the server reports no more pages, so an exhaustive loop
        terminates cleanly even if the dataset is empty."""
        page = 1
        while True:
            data = self.get(path, page=page, **base_params)
            for item in data.get("results", []):
                yield item
            total_pages = data.get("pages") or 1
            if page >= total_pages:
                break
            page += 1
