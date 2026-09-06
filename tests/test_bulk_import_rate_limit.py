"""The bulk-import rate limit is configurable, not hard-coded.

It was "10 per hour", which silently caps a real data load: importing one
file per museum is dozens of requests in a few minutes, and the 11th comes
back as a 429 HTML error page rather than a JSON report — which looks like
the import failed rather than being throttled.

The limit isn't what protects a worker from a huge import (_BULK_MAX_ROWS
and MAX_CONTENT_LENGTH do that), so it can be generous. These tests pin
that it reads from Config so it can be tuned per deployment.
"""

import json

import pytest


class TestRateLimitIsConfigurable:

    def test_config_exposes_the_limit(self):
        from config import Config
        assert hasattr(Config, "BULK_IMPORT_RATE_LIMIT")
        assert isinstance(Config.BULK_IMPORT_RATE_LIMIT, str)
        assert "per" in Config.BULK_IMPORT_RATE_LIMIT

    def test_default_allows_a_real_multi_file_import(self):
        """41 museum files plus a dry run is ~84 requests. The default has
        to clear that or the documented workflow can't run."""
        from config import Config
        n = int(Config.BULK_IMPORT_RATE_LIMIT.split()[0])
        assert n >= 100, (
            f"default limit {Config.BULK_IMPORT_RATE_LIMIT!r} is too low to "
            f"import the California data set in one pass"
        )

    def test_endpoints_are_not_hard_coded(self):
        """Guard against someone re-hard-coding the old value."""
        import re
        from pathlib import Path
        src = (Path(__file__).resolve().parent.parent / "app.py").read_text()
        for m in re.finditer(r'@limiter\.limit\("(\d+) per hour"\)\n'
                             r'def api_bulk_import', src):
            pytest.fail(f"bulk import limit hard-coded to {m.group(1)}/hour")


class TestImportStillWorksUnderTheLimit:

    def test_many_sequential_imports_succeed(self, admin_client, db_session,
                                             make_museum):
        """Twelve imports in a row — comfortably past the old 10/hour cap.

        The limiter is disabled in the test fixture, so this asserts the
        endpoint itself stays healthy across repeated calls rather than
        exercising the limiter.
        """
        import models
        make_museum(name="Castle Air Museum", city="Atwater")
        for i in range(12):
            payload = {"format": "json", "data": json.dumps([
                {"manufacturer": "Lockheed", "model": f"T-{i}",
                 "tail_number": f"60-{1000+i}",
                 "museum_name": "Castle Air Museum"},
            ])}
            r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
            assert r.status_code == 200, f"import {i} returned {r.status_code}"
            assert r.get_json()["errors"] == []
        assert models.Aircraft.query.count() == 12
        assert models.AircraftMuseum.query.count() == 12
