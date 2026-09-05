"""scripts/filter_new_museums.py — subtracting already-imported museums.

The bulk importer is atomic, so a single already-present museum makes it
reject the whole file. That is correct for a first import but blocks
re-running a museums file after adding a row. This script subtracts what's
already there; these tests pin the matching rule (case-insensitive
name+city+country, mirroring the importer's own duplicate check).
"""

import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

HEADER = ["name", "city", "state_province", "country", "postal_code",
          "region", "address", "website", "latitude", "longitude"]


@pytest.fixture
def mod():
    import filter_new_museums
    return filter_new_museums


def write_csv(path, museums):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        for name, city in museums:
            w.writerow({"name": name, "city": city, "state_province": "California",
                        "country": "United States", "postal_code": "",
                        "region": "North America", "address": "", "website": "",
                        "latitude": "", "longitude": ""})


class FakeClient:
    base_url = "http://test"
    api_key = None

    def __init__(self, existing):
        self._existing = existing

    def iter_museums(self):
        return iter([{"name": n, "city": c, "country": "United States"}
                     for n, c in self._existing])


class TestKeyMatching:

    def test_key_is_case_and_space_insensitive(self, mod):
        assert mod.key("Yanks Air Museum", "Chino", "United States") == \
               mod.key("  yanks AIR museum ", " CHINO ", "united states")

    def test_country_defaults_when_missing(self, mod):
        assert mod.key("X", "Y", None) == mod.key("X", "Y", "United States")
        assert mod.key("X", "Y", "") == mod.key("X", "Y", "United States")

    def test_same_name_different_city_is_distinct(self, mod):
        """Hiller Aviation (San Carlos) vs Hillier Air (Modesto) is the real
        case this protects — but even identical names in different cities
        must not collapse."""
        assert mod.key("Air Museum", "Chino", "United States") != \
               mod.key("Air Museum", "Tucson", "United States")


class TestFiltering:

    def _run(self, mod, monkeypatch, tmp_path, in_museums, existing):
        src = tmp_path / "in.csv"
        out = tmp_path / "out.csv"
        write_csv(src, in_museums)
        monkeypatch.setattr(mod, "AirplaneClient", lambda: FakeClient(existing))
        monkeypatch.setattr(sys, "argv",
                            ["prog", str(src), "--out", str(out)])
        code = mod.main()
        rows = (list(csv.DictReader(out.open(encoding="utf-8")))
                if out.exists() else [])
        return code, rows

    def test_all_new_writes_everything(self, mod, monkeypatch, tmp_path):
        code, rows = self._run(mod, monkeypatch, tmp_path,
                               [("Yanks Air Museum", "Chino"),
                                ("Lyon Air Museum", "Santa Ana")], [])
        assert code == 0
        assert len(rows) == 2

    def test_all_existing_returns_3_and_writes_nothing(self, mod, monkeypatch, tmp_path):
        """Exit 3 is what tells the shell script to skip the import."""
        code, rows = self._run(mod, monkeypatch, tmp_path,
                               [("Yanks Air Museum", "Chino")],
                               [("Yanks Air Museum", "Chino")])
        assert code == 3
        assert rows == []

    def test_partial_writes_only_the_new_ones(self, mod, monkeypatch, tmp_path):
        """The case that actually bit: 43 museums in the file, 43 already
        imported, one new one added later."""
        code, rows = self._run(
            mod, monkeypatch, tmp_path,
            [("Yanks Air Museum", "Chino"), ("Lyon Air Museum", "Santa Ana"),
             ("USS Midway Museum", "San Diego")],
            [("Yanks Air Museum", "Chino"), ("Lyon Air Museum", "Santa Ana")])
        assert code == 0
        assert [r["name"] for r in rows] == ["USS Midway Museum"]

    def test_match_ignores_case_differences(self, mod, monkeypatch, tmp_path):
        code, rows = self._run(mod, monkeypatch, tmp_path,
                               [("Yanks Air Museum", "Chino")],
                               [("YANKS AIR MUSEUM", "chino")])
        assert code == 3

    def test_transport_failure_returns_2(self, mod, monkeypatch, tmp_path):
        """A TLS/DNS failure must exit 2 so the shell falls back to the
        unfiltered file rather than dying on a traceback."""
        class Boom:
            base_url = "https://unreachable"
            def iter_museums(self):
                raise OSError("certificate verify failed")
        src = tmp_path / "in.csv"
        write_csv(src, [("Yanks Air Museum", "Chino")])
        monkeypatch.setattr(mod, "AirplaneClient", lambda: Boom())
        monkeypatch.setattr(sys, "argv", ["prog", str(src)])
        assert mod.main() == 2

    def test_missing_file_returns_2(self, mod, monkeypatch, tmp_path):
        monkeypatch.setattr(sys, "argv", ["prog", str(tmp_path / "nope.csv")])
        assert mod.main() == 2
