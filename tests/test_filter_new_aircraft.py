"""scripts/filter_new_aircraft.py — row-level idempotency for top-up files.

The importer is atomic, so one already-present row rejects a whole file.
The museum-level guard can't help top-ups: "does this museum have
aircraft?" is true for every top-up by definition, so they bypass it and
then collide instead. This filters at the row level so a top-up can be
re-run safely as a collection grows.
"""

import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

HEADER = ["manufacturer", "model", "variant", "tail_number", "model_name",
          "aircraft_name", "aircraft_type", "wing_type", "military_civilian",
          "role_type", "year_built", "description", "aliases",
          "museum_name", "display_status"]


@pytest.fixture
def mod():
    import filter_new_aircraft
    return filter_new_aircraft


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            base = {k: "" for k in HEADER}
            base.update({"aircraft_type": "fixed_wing",
                         "military_civilian": "military",
                         "museum_name": "Test Museum",
                         "display_status": "on_display"})
            base.update(r)
            w.writerow(base)


class FakeClient:
    base_url = "http://test"
    api_key = "amt_test"

    def __init__(self, exhibits=None, aircraft=None):
        self._exhibits = exhibits or []
        self._aircraft = aircraft or []

    def get(self, path, **params):
        if path == "/api/v1/exhibits":
            return {"results": self._exhibits}
        raise AssertionError(path)

    def iter_aircraft(self):
        return iter(self._aircraft)


def exhibit(museum, manufacturer, model, variant="", tail=None):
    return {"aircraft": {"manufacturer": manufacturer, "model": model,
                         "variant": variant, "tail_number": tail},
            "museum": {"name": museum}}


def run(mod, monkeypatch, tmp_path, rows, client, extra_argv=()):
    src, out = tmp_path / "in.csv", tmp_path / "out.csv"
    write_csv(src, rows)
    monkeypatch.setattr(mod, "AirplaneClient", lambda: client)
    monkeypatch.setattr(sys, "argv",
                        ["prog", str(src), "--out", str(out), *extra_argv])
    code = mod.main()
    written = (list(csv.DictReader(out.open(encoding="utf-8")))
               if out.exists() else [])
    return code, written


class TestTailMatching:

    def test_drops_rows_already_present_by_tail(self, mod, monkeypatch, tmp_path):
        client = FakeClient(exhibits=[
            exhibit("Test Museum", "Lockheed", "SR-71", "A", "61-7960")])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Lockheed", "model": "SR-71", "variant": "A",
             "tail_number": "61-7960"},
            {"manufacturer": "Boeing", "model": "B-52", "variant": "D",
             "tail_number": "56-0612"},
        ], client)
        assert code == 0
        assert [r["model"] for r in out] == ["B-52"]

    def test_tail_match_is_case_insensitive(self, mod, monkeypatch, tmp_path):
        client = FakeClient(exhibits=[
            exhibit("Test Museum", "Grumman", "F-14", "A", "160694")])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "grumman", "model": "f-14", "tail_number": "160694"},
        ], client)
        assert code == 3          # nothing new

    def test_unlinked_aircraft_still_block_a_tail(self, mod, monkeypatch, tmp_path):
        """An aircraft with no museum link still occupies its (model, tail),
        so importing the same serial would fail the unique index."""
        client = FakeClient(exhibits=[],
                            aircraft=[{"model": "C-130", "tail_number": "62-1787"}])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Lockheed", "model": "C-130", "tail_number": "62-1787"},
        ], client)
        assert code == 3


class TestUntailedRows:

    def test_untailed_duplicate_at_same_museum_dropped(self, mod, monkeypatch, tmp_path):
        """A blank tail is NULL and never collides, so the importer would
        happily create a second copy. Match on type at that museum instead."""
        client = FakeClient(exhibits=[
            exhibit("Test Museum", "Mitsubishi", "A6M", "5")])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Mitsubishi", "model": "A6M", "variant": "5"},
        ], client)
        assert code == 3

    def test_untailed_same_type_at_a_different_museum_is_kept(
            self, mod, monkeypatch, tmp_path):
        """Two museums each owning a Zero is normal and must not be filtered."""
        client = FakeClient(exhibits=[
            exhibit("Some Other Museum", "Mitsubishi", "A6M", "5")])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Mitsubishi", "model": "A6M", "variant": "5"},
        ], client)
        assert code == 0 and len(out) == 1

    def test_keep_untailed_flag_overrides(self, mod, monkeypatch, tmp_path):
        client = FakeClient(exhibits=[
            exhibit("Test Museum", "Mitsubishi", "A6M", "5")])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Mitsubishi", "model": "A6M", "variant": "5"},
        ], client, extra_argv=("--keep-untailed",))
        assert code == 0 and len(out) == 1


class TestOutcomes:

    def test_all_new_keeps_everything(self, mod, monkeypatch, tmp_path):
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Boeing", "model": "B-17", "tail_number": "44-1"},
            {"manufacturer": "Boeing", "model": "B-29", "tail_number": "44-2"},
        ], FakeClient())
        assert code == 0 and len(out) == 2

    def test_all_present_returns_3(self, mod, monkeypatch, tmp_path):
        """Exit 3 tells the shell script to skip this file entirely."""
        client = FakeClient(exhibits=[
            exhibit("Test Museum", "Boeing", "B-17", "G", "44-1")])
        code, out = run(mod, monkeypatch, tmp_path, [
            {"manufacturer": "Boeing", "model": "B-17", "variant": "G",
             "tail_number": "44-1"},
        ], client)
        assert code == 3 and out == []

    def test_transport_failure_returns_2(self, mod, monkeypatch, tmp_path):
        class Boom:
            base_url = "https://unreachable"
            def get(self, *a, **k): raise OSError("connection refused")
            def iter_aircraft(self): return iter([])
        src = tmp_path / "in.csv"
        write_csv(src, [{"manufacturer": "Boeing", "model": "B-17"}])
        monkeypatch.setattr(mod, "AirplaneClient", lambda: Boom())
        monkeypatch.setattr(sys, "argv", ["prog", str(src)])
        assert mod.main() == 2

    def test_missing_file_returns_2(self, mod, monkeypatch, tmp_path):
        monkeypatch.setattr(sys, "argv", ["prog", str(tmp_path / "nope.csv")])
        assert mod.main() == 2
