"""Bulk-import endpoints — happy path, validation, atomic rollback,
duplicate handling, dry-run, row caps, permission gates.

Atomic rollback is the highest-value invariant here: if 999 rows are valid
and one is broken, the whole batch must be rejected. Half-applied imports
are very hard to recover from, and tests pinning that behavior in are how
we keep that property as the parsing logic evolves.
"""

import io
import json
import pytest


# ─────────────────────────────────────────────────────────────────────
# Aircraft — JSON path
# ─────────────────────────────────────────────────────────────────────

class TestAircraftBulkImportJSON:

    def test_creates_rows_on_happy_path(self, admin_client, db_session):
        import models
        payload = {
            "format": "json",
            "data": json.dumps([
                {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014",
                 "aliases": ["Herc", "Hercules"]},
                {"manufacturer": "Boeing", "model": "B-29", "tail_number": "44-86292"},
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.status_code == 200
        report = r.get_json()
        assert report["created"] == 2
        assert report["errors"] == []
        # Aliases survived the round trip
        ac = models.Aircraft.query.filter_by(model="C-130").one()
        assert sorted(a.alias for a in ac.aliases) == ["Herc", "Hercules"]

    def test_dry_run_validates_without_inserting(self, admin_client, db_session):
        import models
        payload = {
            "format": "json", "dry_run": True,
            "data": json.dumps([
                {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"},
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.status_code == 200
        assert r.get_json()["dry_run"] is True
        # NOT inserted
        assert models.Aircraft.query.count() == 0

    def test_validation_error_rolls_back_entire_batch(self, admin_client, db_session):
        """Three rows: two valid, one with an invalid enum. Whole batch
        must roll back — the half-applied import is the worst outcome."""
        import models
        payload = {
            "format": "json",
            "data": json.dumps([
                {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"},
                {"manufacturer": "Boeing",   "model": "B-29",  "tail_number": "44-86292",
                 "aircraft_type": "submarine"},  # invalid enum
                {"manufacturer": "Fairchild", "model": "A-10", "tail_number": "75-0258"},
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.status_code == 200
        report = r.get_json()
        assert report["created"] == 0, "validation failure must roll back entire batch"
        assert any(e.get("field") == "aircraft_type" for e in report["errors"])
        assert models.Aircraft.query.count() == 0

    def test_within_batch_duplicate_rejected(self, admin_client, db_session):
        """Two rows with the same (model, tail_number). Without this check
        the DB unique index would catch it, but with a worse error message."""
        import models
        payload = {
            "format": "json",
            "data": json.dumps([
                {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"},
                {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"},
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.status_code == 200
        report = r.get_json()
        assert report["created"] == 0
        assert any("duplicate of an earlier row" in e["message"]
                   for e in report["errors"])

    def test_existing_db_duplicate_skipped_and_batch_rolled_back(
        self, admin_client, db_session, make_aircraft
    ):
        """Pre-existing aircraft + import that includes it: import rolls back
        because we treat 'skipped' as a non-success that warrants a clean
        retry rather than partial application."""
        import models
        make_aircraft(model="C-130", tail_number="55-0014")
        before = models.Aircraft.query.count()

        payload = {
            "format": "json",
            "data": json.dumps([
                {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"},
                {"manufacturer": "Boeing",   "model": "B-29",  "tail_number": "44-86292"},
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 0, "should roll back because of skipped duplicate"
        assert any("already exists" in e["message"] for e in report["errors"])
        # Count unchanged
        assert models.Aircraft.query.count() == before

    def test_missing_required_field_reports_error(self, admin_client, db_session):
        payload = {
            "format": "json",
            "data": json.dumps([
                {"model": "C-130", "tail_number": "55-0014"},  # no manufacturer
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 0
        assert any(e["field"] == "manufacturer" and e["message"] == "required"
                   for e in report["errors"])


# ─────────────────────────────────────────────────────────────────────
# Aircraft — CSV path
# ─────────────────────────────────────────────────────────────────────

class TestAircraftBulkImportCSV:

    def test_creates_rows_on_happy_path(self, admin_client, db_session):
        import models
        csv_text = (
            "manufacturer,model,variant,tail_number,aircraft_type,military_civilian,aliases\n"
            "Lockheed,C-130,H,55-0014,fixed_wing,military,Herc;Hercules\n"
            "Boeing,B-29,,44-86292,fixed_wing,military,\n"
        )
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": csv_text})
        report = r.get_json()
        assert report["created"] == 2, f"expected 2 created, got {report}"
        # CSV semicolon-separated aliases parsed correctly
        ac = models.Aircraft.query.filter_by(model="C-130").one()
        assert sorted(a.alias for a in ac.aliases) == ["Herc", "Hercules"]

    def test_csv_with_blank_optional_fields(self, admin_client, db_session):
        import models
        csv_text = (
            "manufacturer,model,tail_number\n"
            "Lockheed,C-130,55-0014\n"
        )
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": csv_text})
        assert r.get_json()["created"] == 1
        # aircraft_type defaults to fixed_wing when missing in CSV
        ac = models.Aircraft.query.one()
        assert ac.aircraft_type == "fixed_wing"

    def test_invalid_year_built_reported_per_row(self, admin_client, db_session):
        csv_text = (
            "manufacturer,model,tail_number,year_built\n"
            "Lockheed,C-130,55-0014,not-a-year\n"
        )
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": csv_text})
        report = r.get_json()
        assert report["created"] == 0
        assert any(e["field"] == "year_built" for e in report["errors"])

    def test_format_auto_detects_json_from_leading_bracket(self, admin_client, db_session):
        """Helpful UX: the JSON-body path doesn't need explicit format=json
        when the data starts with [ — handy when wrapping an existing JSON
        file as text in the body."""
        payload = {
            "format": "auto",
            "data": '[{"manufacturer":"Lockheed","model":"C-130","tail_number":"55-0014"}]',
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.get_json()["created"] == 1


# ─────────────────────────────────────────────────────────────────────
# Multipart file upload (the admin web UI uses this)
# ─────────────────────────────────────────────────────────────────────

class TestBulkImportFileUpload:

    def test_file_upload_csv_creates_rows(self, admin_client, db_session):
        csv_bytes = (
            "manufacturer,model,tail_number\n"
            "Lockheed,C-130,55-0014\n"
        ).encode("utf-8")
        r = admin_client.post(
            "/api/v1/aircraft/bulk_import",
            data={"file": (io.BytesIO(csv_bytes), "import.csv")},
            content_type="multipart/form-data",
        )
        assert r.status_code == 200
        assert r.get_json()["created"] == 1

    def test_file_upload_json_creates_rows(self, admin_client, db_session):
        json_bytes = json.dumps([
            {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"}
        ]).encode("utf-8")
        r = admin_client.post(
            "/api/v1/aircraft/bulk_import",
            data={"file": (io.BytesIO(json_bytes), "import.json")},
            content_type="multipart/form-data",
        )
        assert r.status_code == 200
        assert r.get_json()["created"] == 1

    def test_dry_run_via_form_field(self, admin_client, db_session):
        import models
        json_bytes = json.dumps([
            {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"}
        ]).encode("utf-8")
        r = admin_client.post(
            "/api/v1/aircraft/bulk_import",
            data={"file": (io.BytesIO(json_bytes), "import.json"), "dry_run": "1"},
            content_type="multipart/form-data",
        )
        assert r.get_json()["dry_run"] is True
        assert models.Aircraft.query.count() == 0


# ─────────────────────────────────────────────────────────────────────
# Museums
# ─────────────────────────────────────────────────────────────────────

class TestMuseumBulkImport:

    def test_creates_rows_on_happy_path(self, admin_client, db_session):
        import models
        payload = {
            "format": "json",
            "data": json.dumps([
                {"name": "AFM", "city": "Dayton", "country": "United States",
                 "region": "North America"},
                {"name": "RAF Museum", "city": "London", "country": "United Kingdom",
                 "region": "Europe"},
            ]),
        }
        r = admin_client.post("/api/v1/museums/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 2
        assert models.Museum.query.count() == 2

    def test_invalid_region_reported(self, admin_client, db_session):
        payload = {
            "format": "json",
            "data": json.dumps([
                {"name": "X", "city": "Y", "country": "Z", "region": "Atlantis"},
            ]),
        }
        r = admin_client.post("/api/v1/museums/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 0
        assert any(e["field"] == "region" for e in report["errors"])

    def test_one_coordinate_without_the_other_rejected(self, admin_client, db_session):
        payload = {
            "format": "json",
            "data": json.dumps([
                {"name": "X", "city": "Y", "country": "Z", "region": "North America",
                 "latitude": 38.8, "longitude": ""},
            ]),
        }
        r = admin_client.post("/api/v1/museums/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 0
        assert any("latitude" in e["field"] for e in report["errors"])


# ─────────────────────────────────────────────────────────────────────
# Limits + permissions
# ─────────────────────────────────────────────────────────────────────

class TestBulkImportLimits:

    def test_row_count_cap_rejected(self, admin_client, db_session):
        # One more than the cap (5000) — should refuse.
        rows = [{"manufacturer": "X", "model": f"M-{i}"} for i in range(5001)]
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "json", "data": json.dumps(rows)})
        assert r.status_code == 400
        assert "5000" in r.get_json()["error"]

    def test_malformed_json_returns_400(self, admin_client, db_session):
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "json", "data": "{not json"})
        assert r.status_code == 400

    def test_empty_csv_returns_400(self, admin_client, db_session):
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": ""})
        assert r.status_code == 400


class TestBulkImportPermissions:

    @pytest.fixture
    def small_payload(self):
        return {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"}
        ])}

    def test_aircraft_admin_can_import(self, aircraft_admin_client, db_session, small_payload):
        r = aircraft_admin_client.post("/api/v1/aircraft/bulk_import", json=small_payload)
        assert r.status_code == 200

    def test_manager_cannot_import(self, manager_client, db_session, small_payload):
        r = manager_client.post("/api/v1/aircraft/bulk_import", json=small_payload)
        assert r.status_code == 403

    def test_viewer_cannot_import(self, viewer_client, db_session, small_payload):
        r = viewer_client.post("/api/v1/aircraft/bulk_import", json=small_payload)
        assert r.status_code == 403

    def test_anonymous_cannot_import(self, client, db_session, small_payload):
        r = client.post("/api/v1/aircraft/bulk_import", json=small_payload)
        assert r.status_code == 401
