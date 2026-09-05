"""The shipped Castle Air Museum import files must actually import.

`data/castle_air_museum_*.csv` were compiled from the museum's own
collection listing. A data file that fails validation is worse than no
file at all — you find out mid-import, after the museum row is already in.
So these tests run the real files through the real endpoints.
"""

import csv
import io
from pathlib import Path

import pytest


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
MUSEUM_CSV = DATA_DIR / "castle_air_museum_museum.csv"
AIRCRAFT_CSV = DATA_DIR / "castle_air_museum_aircraft.csv"


@pytest.fixture
def museum_text():
    return MUSEUM_CSV.read_text(encoding="utf-8")


@pytest.fixture
def aircraft_text():
    return AIRCRAFT_CSV.read_text(encoding="utf-8")


class TestFilesExist:

    def test_both_files_present(self):
        assert MUSEUM_CSV.is_file()
        assert AIRCRAFT_CSV.is_file()


class TestCastleImport:

    def test_museum_imports(self, admin_client, db_session, museum_text):
        import models
        r = admin_client.post("/api/v1/museums/bulk_import",
                              json={"format": "csv", "data": museum_text})
        assert r.status_code == 200
        report = r.get_json()
        assert report["errors"] == []
        assert report["created"] == 1
        m = models.Museum.query.one()
        assert m.name == "Castle Air Museum"
        assert m.city == "Atwater"
        assert m.has_coordinates

    def test_aircraft_import_after_museum(
        self, admin_client, db_session, museum_text, aircraft_text
    ):
        """The real end-to-end run: museums first, then aircraft, which
        resolve `museum_name` and link themselves to Castle."""
        import models
        admin_client.post("/api/v1/museums/bulk_import",
                          json={"format": "csv", "data": museum_text})

        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": aircraft_text})
        assert r.status_code == 200
        report = r.get_json()
        assert report["errors"] == [], report["errors"][:5]
        assert report["created"] > 80
        # Every row carries museum_name, so every row should link.
        assert report["linked"] == report["created"]

        museum = models.Museum.query.one()
        links = models.AircraftMuseum.query.filter_by(museum_id=museum.id).all()
        assert len(links) == report["created"]

    def test_aircraft_alone_fails_without_museum(self, admin_client, db_session,
                                                 aircraft_text):
        """Guard rail: importing the aircraft file first must fail loudly
        rather than creating 90+ unlinked aircraft."""
        import models
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "data": aircraft_text})
        report = r.get_json()
        assert report["created"] == 0
        assert any(e["field"] == "museum_name" for e in report["errors"])
        assert models.Aircraft.query.count() == 0

    def test_dry_run_is_clean(self, admin_client, db_session, museum_text,
                              aircraft_text):
        admin_client.post("/api/v1/museums/bulk_import",
                          json={"format": "csv", "data": museum_text})
        r = admin_client.post("/api/v1/aircraft/bulk_import",
                              json={"format": "csv", "dry_run": True,
                                    "data": aircraft_text})
        report = r.get_json()
        assert report["errors"] == []
        assert report["dry_run"] is True


class TestCastleDataQuality:
    """Checks on the data itself, independent of the import machinery."""

    @pytest.fixture
    def rows(self, aircraft_text):
        return list(csv.DictReader(io.StringIO(aircraft_text)))

    def test_every_row_targets_castle(self, rows):
        assert rows
        assert all(r["museum_name"] == "Castle Air Museum" for r in rows)

    def test_no_duplicate_model_tail_pairs(self, rows):
        """A repeat (model, tail_number) would trip the DB unique index and
        roll the whole batch back."""
        pairs = [(r["model"], r["tail_number"]) for r in rows if r["tail_number"]]
        dupes = {p for p in pairs if pairs.count(p) > 1}
        assert not dupes, f"duplicate (model, tail): {dupes}"

    def test_enums_are_valid(self, rows):
        from app import (_AIRCRAFT_TYPE_VALUES, _WING_TYPE_VALUES,
                         _MILITARY_CIVILIAN_VALUES, _DISPLAY_STATUS_VALUES)
        for r in rows:
            assert r["aircraft_type"] in _AIRCRAFT_TYPE_VALUES, r
            assert r["military_civilian"] in _MILITARY_CIVILIAN_VALUES, r
            assert r["display_status"] in _DISPLAY_STATUS_VALUES, r
            if r["wing_type"]:
                assert r["wing_type"] in _WING_TYPE_VALUES, r

    def test_rotary_and_missiles_have_no_wing_type(self, rows):
        """wing_type describes a fixed wing; a helicopter or missile with
        'monoplane' set would be a data error."""
        for r in rows:
            if r["aircraft_type"] in ("rotary_wing", "missile_rocket"):
                assert r["wing_type"] == "", r

    def test_required_fields_present(self, rows):
        for r in rows:
            assert r["manufacturer"].strip(), r
            assert r["model"].strip(), r

    def test_year_built_is_plausible(self, rows):
        for r in rows:
            if r["year_built"]:
                assert 1930 <= int(r["year_built"]) <= 2026, r

    def test_role_types_match_ui_vocabulary(self, rows):
        """role_type isn't server-validated, but a value outside the admin
        dropdown's list would render as an unselectable option in the edit
        modal — so pin it here instead."""
        military = {"bomber", "transport", "recon", "electronic_warfare", "fighter",
                    "tanker", "search_rescue", "ground_attack", "utility",
                    "trainer", "test", "drone"}
        civilian = {"commercial_transport", "freighter", "private", "experimental",
                    "utility", "space", "other"}
        missile = {"air_to_air", "surface_to_air", "air_to_surface", "anti_ship",
                   "ballistic", "cruise", "sounding", "launch_vehicle"}
        for r in rows:
            role = r["role_type"]
            if not role:
                continue
            if r["aircraft_type"] == "missile_rocket":
                allowed = missile
            elif r["military_civilian"] == "civilian":
                allowed = civilian
            else:
                allowed = military
            assert role in allowed, f"{role!r} not valid for {r['model']}"
