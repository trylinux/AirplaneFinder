"""scripts/build_from_research.py — realigning malformed research output.

Research passes are told to emit 13 pipe-separated fields and mostly do, but a
few lines per batch come back short or long. Counting pipes cannot tell you
*which* field went missing, so the builder locates the three controlled-
vocabulary columns by value and rebuilds the row around them.

That realignment is the riskiest code in the pipeline: get it wrong and every
value shifts one column, `monoplane` lands in military_civilian, and the
atomic importer throws away the whole file. Hence these tests.
"""

import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import build_from_research as B  # noqa: E402

GOOD = ("North American|F-100|D|55-2888|Super Sabre||fixed_wing|monoplane|"
        "military|fighter|1955|Thunderbirds|on_display")


def one(line, museum="Test Museum"):
    row, problem = B.realign(line.split("|"))
    if problem:
        return None, problem
    row, problems = B.sanitise(row, museum)
    return row, ("; ".join(problems) if problems else None)


class TestWellFormedLines:

    def test_all_thirteen_fields_map_correctly(self):
        row, problem = one(GOOD)
        assert problem is None
        assert row["manufacturer"] == "North American"
        assert row["model"] == "F-100"
        assert row["variant"] == "D"
        assert row["tail_number"] == "55-2888"
        assert row["model_name"] == "Super Sabre"
        assert row["aircraft_name"] == ""
        assert row["aircraft_type"] == "fixed_wing"
        assert row["wing_type"] == "monoplane"
        assert row["military_civilian"] == "military"
        assert row["role_type"] == "fighter"
        assert row["year_built"] == "1955"
        assert row["aliases"] == "Thunderbirds"
        assert row["display_status"] == "on_display"
        assert row["museum_name"] == "Test Museum"


class TestRealignment:
    """The whole point of the module."""

    def test_short_line_does_not_shift_the_enum_columns(self):
        """A dropped field must not push monoplane into military_civilian."""
        short = ("Messerschmitt|Bf 109|G-10|||fixed_wing|monoplane|military|"
                 "fighter|||on_display")            # 12 fields, not 13
        row, problem = one(short)
        assert problem is None
        assert row["manufacturer"] == "Messerschmitt"
        assert row["model"] == "Bf 109"
        assert row["variant"] == "G-10"
        assert row["wing_type"] == "monoplane"
        assert row["military_civilian"] == "military"
        assert row["role_type"] == "fighter"

    def test_long_line_keeps_manufacturer_and_model(self):
        """An extra pipe inside a note must not corrupt the first two fields,
        which are the two that must be right."""
        long = ("Vultee|L-1|A|41-19039|Vigilant|Extra|Name|fixed_wing|"
                "monoplane|military|utility|||O-49|on_display")
        row, problem = one(long)
        assert problem is None
        assert row["manufacturer"] == "Vultee"
        assert row["model"] == "L-1"
        assert row["variant"] == "A"
        assert row["tail_number"] == "41-19039"

    def test_missing_display_status_defaults_to_on_display(self):
        line = ("Ryan|PT-22|||Recruit||fixed_wing|monoplane|military|trainer||")
        row, problem = one(line)
        assert problem is None
        assert row["display_status"] == "on_display"

    def test_status_is_read_when_present(self):
        line = ("Sukhoi|Su-22|M4||Fitter-K||fixed_wing|monoplane|military|"
                "ground_attack|||in_storage")
        row, _ = one(line)
        assert row["display_status"] == "in_storage"

    def test_line_without_an_aircraft_type_is_rejected_not_guessed(self):
        row, problem = one("Boeing|B-17|G|44-1|Fortress||||military|bomber|||")
        assert row is None
        assert "aircraft_type" in problem

    def test_line_without_military_civilian_is_rejected(self):
        row, problem = one("Boeing|B-17|G|44-1|Fortress||fixed_wing|monoplane|"
                           "|bomber|||on_display")
        assert row is None
        assert "military_civilian" in problem


class TestSchemaRules:

    def test_wing_type_is_stripped_from_helicopters(self):
        line = ("Sikorsky|HH-3|E|67-14709|Jolly Green Giant||rotary_wing|"
                "monoplane|military|search_rescue|||on_display")
        row, _ = one(line)
        assert row["wing_type"] == "", \
            "a helicopter with a wing type is a data error the schema will store"

    def test_wing_type_is_stripped_from_missiles(self):
        line = ("Martin|TM-61|A||Matador||missile_rocket|monoplane|military|"
                "cruise|||on_display")
        row, _ = one(line)
        assert row["wing_type"] == ""

    def test_fixed_wing_gets_a_default_wing_type(self):
        line = ("Seversky|P-35|||||fixed_wing||military|fighter|||on_display")
        row, _ = one(line)
        assert row["wing_type"] == "monoplane"

    def test_unknown_role_becomes_other_rather_than_failing_the_import(self):
        line = ("Boeing|B-17|G|44-1|Fortress||fixed_wing|monoplane|military|"
                "heavy_bombardment|||on_display")
        row, _ = one(line)
        assert row["role_type"] == "other"


class TestTailNumberHygiene:

    @pytest.mark.parametrize("raw,expected", [
        ("BuNo 140048", "140048"),
        ("S/N 43-3374", "43-3374"),
        ("SN 43-3374", "43-3374"),
        ("Serial: 62-0001", "62-0001"),
        ("44-83624", "44-83624"),
    ])
    def test_serial_prefixes_are_stripped(self, raw, expected):
        line = (f"North American|T-28|B|{raw}|Trojan||fixed_wing|monoplane|"
                f"military|trainer|||on_display")
        row, _ = one(line)
        assert row["tail_number"] == expected


class TestNeverInvent:
    """METHODOLOGY.md: an empty field is always better than a guess."""

    def test_blank_tail_stays_blank(self):
        line = ("Martin|B-10|||||fixed_wing|monoplane|military|bomber|||on_display")
        row, _ = one(line)
        assert row["tail_number"] == ""

    def test_a_serial_in_year_built_is_rejected_not_stored(self):
        """The single most common research error."""
        line = ("Republic|P-47|D|42-23278|Thunderbolt||fixed_wing|monoplane|"
                "military|fighter|42-23278||on_display")
        row, problem = one(line)
        # realign only accepts a 4-digit year there; anything else is prose
        # and lands in aliases, never in year_built.
        assert row is None or row["year_built"] == ""

    def test_prose_in_the_year_column_goes_to_aliases(self):
        line = ("Northrop|B-2|||Spirit||fixed_wing|monoplane|military|bomber|"
                "structural test airframe||on_display")
        row, _ = one(line)
        assert row["year_built"] == ""
        assert "structural test airframe" in row["aliases"]


class TestEndToEnd:

    def test_writes_a_csv_the_importer_header_expects(self, tmp_path):
        src = tmp_path / "raw.txt"
        src.write_text(GOOD + "\n---NOTES---\nsome commentary\n", encoding="utf-8")
        out = tmp_path / "out.csv"
        sys.argv = ["prog", "--in", str(src), "--museum", "M", "--out", str(out)]
        assert B.main() == 0
        rows = list(csv.DictReader(out.open(encoding="utf-8")))
        assert len(rows) == 1, "the ---NOTES--- block must not become a row"
        assert list(rows[0].keys()) == B.HEADER
