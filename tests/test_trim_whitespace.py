"""scripts/trim_whitespace.py — the field-detection logic.

The script talks to a live API, so the network layer isn't what's worth
testing. What matters is `find_dirty`: which fields it flags, what it
leaves alone, and that an all-whitespace value becomes None rather than
an empty string (the API normalizes "" to NULL for tail_number, and an
empty manufacturer would fail validation).
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))


@pytest.fixture
def mod():
    import trim_whitespace
    return trim_whitespace


class FakeClient:
    """Stands in for AirplaneClient — only iter_aircraft is used."""
    base_url = "http://test"
    api_key = "amt_test"

    def __init__(self, records):
        self._records = records

    def iter_aircraft(self):
        return iter(self._records)


class TestFindDirty:

    def test_clean_records_are_ignored(self, mod):
        c = FakeClient([
            {"id": 1, "manufacturer": "Boeing", "model": "B-52", "variant": "D",
             "tail_number": "56-0612"},
        ])
        assert mod.find_dirty(c, mod.DEFAULT_FIELDS) == []

    def test_leading_space_in_model_flagged(self, mod):
        c = FakeClient([
            {"id": 7, "manufacturer": "Fairchild", "model": " C-7", "variant": "A",
             "tail_number": "63-9757"},
        ])
        dirty = mod.find_dirty(c, mod.DEFAULT_FIELDS)
        assert len(dirty) == 1
        ac, changes = dirty[0]
        assert ac["id"] == 7
        assert changes["model"] == (" C-7", "C-7")

    def test_trailing_space_in_tail_flagged(self, mod):
        c = FakeClient([
            {"id": 9, "manufacturer": "Boeing", "model": "KC-135",
             "tail_number": "55-3130 "},
        ])
        _, changes = mod.find_dirty(c, mod.DEFAULT_FIELDS)[0]
        assert changes["tail_number"] == ("55-3130 ", "55-3130")

    def test_multiple_fields_on_one_record(self, mod):
        c = FakeClient([
            {"id": 3, "manufacturer": "Lockheed ", "model": "F-117 ",
             "variant": "A", "tail_number": " 85-0833"},
        ])
        _, changes = mod.find_dirty(c, mod.DEFAULT_FIELDS)[0]
        assert set(changes) == {"manufacturer", "model", "tail_number"}

    def test_whitespace_only_becomes_none(self, mod):
        """'   ' should clear to NULL, not to an empty string."""
        c = FakeClient([
            {"id": 4, "manufacturer": "Boeing", "model": "B-52",
             "aircraft_name": "   "},
        ])
        _, changes = mod.find_dirty(c, mod.DEFAULT_FIELDS)[0]
        assert changes["aircraft_name"] == ("   ", None)

    def test_internal_whitespace_untouched(self, mod):
        """'Flying  Fortress' has a doubled inner space — not this script's
        job, and collapsing it could change a real name."""
        c = FakeClient([
            {"id": 5, "manufacturer": "Boeing", "model": "B-17",
             "model_name": "Flying  Fortress"},
        ])
        assert mod.find_dirty(c, mod.DEFAULT_FIELDS) == []

    def test_non_string_and_missing_fields_skipped(self, mod):
        c = FakeClient([
            {"id": 6, "manufacturer": "Boeing", "model": "B-29",
             "year_built": 1944, "variant": None},
        ])
        assert mod.find_dirty(c, mod.DEFAULT_FIELDS) == []

    def test_description_not_touched_by_default(self, mod):
        c = FakeClient([
            {"id": 8, "manufacturer": "Boeing", "model": "B-29",
             "description": " leading space in prose "},
        ])
        assert mod.find_dirty(c, mod.DEFAULT_FIELDS) == []
        # ...but can be opted into explicitly.
        dirty = mod.find_dirty(c, ("description",))
        assert dirty and dirty[0][1]["description"][1] == "leading space in prose"

    def test_limit_stops_early(self, mod):
        c = FakeClient([
            {"id": i, "manufacturer": "X ", "model": "M"} for i in range(10)
        ])
        assert len(mod.find_dirty(c, mod.DEFAULT_FIELDS, limit=3)) == 3
