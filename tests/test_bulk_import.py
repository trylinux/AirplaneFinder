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

    def test_missile_rocket_aircraft_type_accepted(self, admin_client, db_session):
        """The bulk-import validator's enum allowlist must include the new
        missile_rocket value, mirroring the schema-side ENUM."""
        import models
        payload = {
            "format": "json",
            "data": json.dumps([
                {"manufacturer": "Raytheon", "model": "AIM-9", "tail_number": "M-1",
                 "aircraft_type": "missile_rocket", "role_type": "air_to_air"},
                {"manufacturer": "NASA",     "model": "Saturn V", "tail_number": "M-2",
                 "aircraft_type": "missile_rocket", "military_civilian": "civilian",
                 "role_type": "launch_vehicle"},
            ]),
        }
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.status_code == 200
        report = r.get_json()
        assert report["created"] == 2, f"expected 2, got {report}"
        # Confirm both landed with the right type.
        types = sorted(a.aircraft_type for a in models.Aircraft.query.all())
        assert types == ["missile_rocket", "missile_rocket"]

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


class TestAircraftBulkImportMuseumLink:
    """Optional museum_id / museum_name / display_status columns.

    These let one file create the aircraft AND the exhibit link. The
    museum has to already exist; an unresolvable reference is a validation
    error, which (per the atomic rule) rolls back the whole batch rather
    than quietly importing unlinked aircraft.
    """

    def test_museum_id_creates_link(self, admin_client, db_session, make_museum):
        import models
        m = make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "SR-71", "variant": "A",
             "tail_number": "61-7960", "museum_id": m.id},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.status_code == 200
        report = r.get_json()
        assert report["created"] == 1
        assert report["linked"] == 1
        link = models.AircraftMuseum.query.one()
        assert link.museum_id == m.id
        assert link.display_status == "on_display"   # default

    def test_museum_name_resolves(self, admin_client, db_session, make_museum):
        import models
        m = make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Boeing", "model": "B-52", "variant": "D",
             "tail_number": "56-0612", "museum_name": "Castle Air Museum"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.get_json()["linked"] == 1
        assert models.AircraftMuseum.query.one().museum_id == m.id

    def test_museum_name_match_is_case_insensitive(
        self, admin_client, db_session, make_museum
    ):
        make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Boeing", "model": "B-52", "museum_name": "castle AIR museum"},
        ])}
        assert admin_client.post(
            "/api/v1/aircraft/bulk_import", json=payload
        ).get_json()["linked"] == 1

    def test_explicit_display_status_honored(
        self, admin_client, db_session, make_museum
    ):
        import models
        make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Douglas", "model": "B-18", "tail_number": "37-0029",
             "museum_name": "Castle Air Museum", "display_status": "under_restoration"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert r.get_json()["linked"] == 1
        assert models.AircraftMuseum.query.one().display_status == "under_restoration"

    def test_invalid_display_status_rejected(
        self, admin_client, db_session, make_museum
    ):
        import models
        make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Douglas", "model": "B-18",
             "museum_name": "Castle Air Museum", "display_status": "on_loan"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 0
        assert any(e["field"] == "display_status" for e in report["errors"])
        assert models.Aircraft.query.count() == 0

    def test_unknown_museum_name_fails_whole_batch(self, admin_client, db_session):
        """The aircraft is otherwise valid — but importing it unlinked would
        silently lose the curator's intent, so the batch fails."""
        import models
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "SR-71",
             "museum_name": "Museum That Does Not Exist"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 0
        assert any(e["field"] == "museum_name" for e in report["errors"])
        assert models.Aircraft.query.count() == 0

    def test_unknown_museum_id_fails(self, admin_client, db_session):
        import models
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "SR-71", "museum_id": 99999},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert any(e["field"] == "museum_id" for e in r.get_json()["errors"])
        assert models.Aircraft.query.count() == 0

    def test_ambiguous_museum_name_reports_ids(
        self, admin_client, db_session, make_museum
    ):
        """Two museums with the same name in different cities — the importer
        refuses to guess and hands back the ids to disambiguate with."""
        m1 = make_museum(name="Air Museum", city="Atwater")
        m2 = make_museum(name="Air Museum", city="Tucson")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "SR-71", "museum_name": "Air Museum"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        errs = r.get_json()["errors"]
        assert any(e["field"] == "museum_name" for e in errs)
        msg = " ".join(e["message"] for e in errs)
        assert str(m1.id) in msg and str(m2.id) in msg

    def test_both_museum_id_and_name_rejected(
        self, admin_client, db_session, make_museum
    ):
        m = make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "SR-71",
             "museum_id": m.id, "museum_name": "Castle Air Museum"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        assert any(e["field"] == "museum_id/museum_name"
                   for e in r.get_json()["errors"])

    def test_rows_without_museum_still_work(self, admin_client, db_session):
        """Link columns are optional — omitting them imports plain aircraft."""
        import models
        payload = {"format": "json", "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        report = r.get_json()
        assert report["created"] == 1
        assert report["linked"] == 0
        assert models.AircraftMuseum.query.count() == 0

    def test_csv_link_columns(self, admin_client, db_session, make_museum):
        import models
        make_museum(name="Castle Air Museum", city="Atwater")
        csv_text = (
            "manufacturer,model,variant,tail_number,museum_name,display_status\n"
            "Lockheed,SR-71,A,61-7960,Castle Air Museum,on_display\n"
            "Convair,B-58,A,55-0666,Castle Air Museum,on_display\n"
        )
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": csv_text})
        report = r.get_json()
        assert report["created"] == 2
        assert report["linked"] == 2
        assert models.AircraftMuseum.query.count() == 2

    def test_dry_run_counts_links_without_writing(
        self, admin_client, db_session, make_museum
    ):
        import models
        make_museum(name="Castle Air Museum", city="Atwater")
        payload = {"format": "json", "dry_run": True, "data": json.dumps([
            {"manufacturer": "Lockheed", "model": "SR-71",
             "museum_name": "Castle Air Museum"},
        ])}
        r = admin_client.post("/api/v1/aircraft/bulk_import", json=payload)
        report = r.get_json()
        assert report["dry_run"] is True
        assert report["linked"] == 1
        assert models.Aircraft.query.count() == 0
        assert models.AircraftMuseum.query.count() == 0


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
