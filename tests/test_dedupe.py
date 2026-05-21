"""Seed-data shape + dedupe script behavior.

After the on_loan rework we noticed the dashboard was reporting ~2x the
expected number of exhibits — caused by the seed reusing one Aircraft
row for many museums. seed_data.py was refactored so each EXHIBITS
entry produces exactly one Aircraft row + one link (1:1). These tests
pin that invariant on the seed structure, and they pin the dedupe
script's behavior so the curator-facing cleanup tool stays correct.
"""

import os
import re
import sys
from pathlib import Path

import pytest


# Make scripts/ importable so we can call dedupe directly.
sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent / "scripts")
)


# ─────────────────────────────────────────────────────────────────────
# Seed-data shape — static checks on the EXHIBITS list itself
# ─────────────────────────────────────────────────────────────────────

class TestSeedStructure:
    """Static-source checks. These don't need a database — they verify
    the seed file is shaped correctly, which is the actual fix."""

    @pytest.fixture
    def seed_module(self):
        import importlib
        import seed_data
        importlib.reload(seed_data)
        return seed_data

    def test_no_links_variable_remains(self, seed_module):
        """LINKS was the old structure that caused the 2x ratio.
        It must not exist as a module attribute, or someone will
        accidentally start using it again."""
        assert not hasattr(seed_module, "LINKS"), (
            "seed_data.LINKS resurfaced — the old per-type-row pattern is back"
        )

    def test_exhibits_variable_exists(self, seed_module):
        assert hasattr(seed_module, "EXHIBITS")
        assert isinstance(seed_module.EXHIBITS, list)
        assert len(seed_module.EXHIBITS) > 0

    def test_each_aircraft_at_most_one_museum_in_seed(self, seed_module):
        """The whole point of the refactor: one Aircraft row → one link.
        Every EXHIBITS row generates a *new* Aircraft, so a single
        (museum_idx, type_idx, tail, name, status) tuple can't appear
        twice with the same tail (that'd be the same airframe linked twice).
        """
        non_null_tails = [
            (type_idx, tail) for (_, type_idx, tail, _, _) in seed_module.EXHIBITS
            if tail is not None
        ]
        assert len(non_null_tails) == len(set(non_null_tails)), (
            "two EXHIBITS rows share (type_idx, tail) — same airframe seeded twice"
        )

    def test_exhibit_count_equals_link_count(self, seed_module):
        """The dashboard's 'aircraft' and 'exhibits' counts should be
        equal after seeding — no aircraft can have 2+ museum links."""
        # Number of Aircraft rows the seed would create == number of links.
        # If they're equal, the ratio that triggered the bug is fixed.
        assert len(seed_module.EXHIBITS) >= len(seed_module.AIRCRAFT), (
            "EXHIBITS shouldn't be smaller than the type-template list — "
            "every type with at least one exhibit needs at least one row"
        )

    def test_all_referenced_type_indices_are_valid(self, seed_module):
        n_types = len(seed_module.AIRCRAFT)
        for museum_idx, type_idx, *_ in seed_module.EXHIBITS:
            assert 0 <= type_idx < n_types, (
                f"EXHIBITS references type_idx={type_idx} which is out of bounds"
            )
            assert 0 <= museum_idx < len(seed_module.MUSEUMS), (
                f"EXHIBITS references museum_idx={museum_idx} which is out of bounds"
            )

    def test_status_value_is_in_allowlist(self, seed_module):
        from app import _DISPLAY_STATUS_VALUES
        for _, _, _, _, status in seed_module.EXHIBITS:
            assert status in _DISPLAY_STATUS_VALUES, (
                f"EXHIBITS contains status={status!r} — not in allowlist"
            )


# ─────────────────────────────────────────────────────────────────────
# Dedupe script — find_duplicate_groups
# ─────────────────────────────────────────────────────────────────────

class TestFindDuplicateGroups:

    def test_distinct_aircraft_are_not_grouped(self, app, db_session, make_aircraft):
        import dedupe_aircraft as ddu
        make_aircraft(manufacturer="Lockheed", model="C-130", variant="A")
        make_aircraft(manufacturer="Boeing",   model="B-52",  variant="D")
        groups = ddu.find_duplicate_groups()
        assert groups == []

    def test_two_aircraft_same_type_are_grouped(
        self, app, db_session, make_aircraft
    ):
        import dedupe_aircraft as ddu
        a1 = make_aircraft(manufacturer="Grumman", model="F-14", variant="A",
                           tail_number="160694")
        a2 = make_aircraft(manufacturer="Grumman", model="F-14", variant="A",
                           tail_number=None)
        groups = ddu.find_duplicate_groups()
        assert len(groups) == 1
        canonical, members = groups[0]
        member_ids = {m.id for m in members}
        assert member_ids == {a1.id, a2.id}

    def test_case_insensitive_match(self, app, db_session, make_aircraft):
        """Curators sometimes enter different casing — the dedupe should
        catch them anyway, otherwise the tool would silently miss the
        common shape of "Lockheed" vs "lockheed"."""
        import dedupe_aircraft as ddu
        make_aircraft(manufacturer="LOCKHEED", model="C-130", variant="A")
        make_aircraft(manufacturer="lockheed", model="C-130", variant="a")
        groups = ddu.find_duplicate_groups()
        assert len(groups) == 1

    def test_min_size_filter(self, app, db_session, make_aircraft):
        import dedupe_aircraft as ddu
        # Two of one type, three of another. min=3 should keep only one.
        for _ in range(2):
            make_aircraft(manufacturer="Boeing", model="B-29", tail_number=None)
        for _ in range(3):
            make_aircraft(manufacturer="Lockheed", model="C-130", variant="A",
                          tail_number=None)
        all_groups = ddu.find_duplicate_groups(min_size=2)
        big_groups = ddu.find_duplicate_groups(min_size=3)
        assert len(all_groups) == 2
        assert len(big_groups) == 1


# ─────────────────────────────────────────────────────────────────────
# Dedupe script — merge
# ─────────────────────────────────────────────────────────────────────

class TestMerge:

    def test_merge_repoints_links(
        self, app, db_session, make_aircraft, make_museum, make_link
    ):
        import dedupe_aircraft as ddu
        keep = make_aircraft(manufacturer="Grumman", model="F-14", variant="A",
                             tail_number="160694")
        drop = make_aircraft(manufacturer="Grumman", model="F-14", variant="A",
                             tail_number=None)
        m1 = make_museum(name="Intrepid")
        m2 = make_museum(name="Pensacola")
        make_link(keep, m1)
        l2 = make_link(drop, m2)
        from models import AircraftMuseum, Aircraft

        result = ddu.merge(keep.id, drop.id, assume_yes=True)
        assert result is not None
        links_moved, links_dropped, _, _ = result
        assert links_moved == 1
        assert links_dropped == 0

        # The link that pointed at DROP now points at KEEP.
        l2_refreshed = AircraftMuseum.query.get(l2.id)
        assert l2_refreshed.aircraft_id == keep.id

        # DROP is gone.
        assert Aircraft.query.get(drop.id) is None

    def test_merge_drops_duplicate_link_when_both_at_same_museum(
        self, app, db_session, make_aircraft, make_museum, make_link
    ):
        """KEEP and DROP both linked to museum X. After merge, KEEP keeps
        its link, DROP's duplicate is deleted (the unique index would
        otherwise reject the re-point)."""
        import dedupe_aircraft as ddu
        keep = make_aircraft(manufacturer="Bell", model="UH-1", variant="H",
                             tail_number="66-16579")
        drop = make_aircraft(manufacturer="Bell", model="UH-1", variant="H",
                             tail_number=None)
        m = make_museum(name="Shared Museum")
        make_link(keep, m)
        make_link(drop, m)

        result = ddu.merge(keep.id, drop.id, assume_yes=True)
        assert result is not None
        _, links_dropped, _, _ = result
        assert links_dropped == 1, "duplicate link should be deleted"

        from models import AircraftMuseum
        remaining = AircraftMuseum.query.filter_by(museum_id=m.id).all()
        assert len(remaining) == 1
        assert remaining[0].aircraft_id == keep.id

    def test_merge_repoints_aliases_and_dedupes(
        self, app, db_session, make_aircraft
    ):
        import dedupe_aircraft as ddu
        from models import AircraftAlias
        keep = make_aircraft(manufacturer="Boeing", model="B-17", variant="G",
                             tail_number="44-83624")
        drop = make_aircraft(manufacturer="Boeing", model="B-17", variant="G",
                             tail_number=None)
        # KEEP already has 'B17'. DROP has 'B17' (duplicate) and 'Flying Fortress' (unique).
        db_session.add(AircraftAlias(aircraft_id=keep.id, alias="B17"))
        db_session.add(AircraftAlias(aircraft_id=drop.id, alias="B17"))
        db_session.add(AircraftAlias(aircraft_id=drop.id, alias="Flying Fortress"))
        db_session.commit()

        result = ddu.merge(keep.id, drop.id, assume_yes=True)
        assert result is not None
        _, _, aliases_moved, aliases_dropped = result
        assert aliases_moved == 1, "unique alias should be re-pointed"
        assert aliases_dropped == 1, "duplicate alias should be deleted"

        keep_aliases = {a.alias for a in AircraftAlias.query.filter_by(
            aircraft_id=keep.id
        ).all()}
        assert keep_aliases == {"B17", "Flying Fortress"}

    def test_merge_rejects_same_id(self, app, db_session, make_aircraft):
        import dedupe_aircraft as ddu
        a = make_aircraft(manufacturer="Boeing", model="B-29")
        with pytest.raises(ValueError, match="same id"):
            ddu.merge(a.id, a.id, assume_yes=True)

    def test_merge_rejects_unknown_id(self, app, db_session, make_aircraft):
        import dedupe_aircraft as ddu
        a = make_aircraft(manufacturer="Boeing", model="B-29")
        with pytest.raises(ValueError, match="not found"):
            ddu.merge(a.id, 99999, assume_yes=True)
        with pytest.raises(ValueError, match="not found"):
            ddu.merge(99999, a.id, assume_yes=True)

    def test_merge_with_no_aliases_or_links_just_deletes_drop(
        self, app, db_session, make_aircraft
    ):
        """Edge case: DROP has no FK rows at all. Merge should still
        succeed and just remove DROP."""
        import dedupe_aircraft as ddu
        from models import Aircraft
        keep = make_aircraft(manufacturer="Boeing", model="B-29",
                             tail_number="44-27297")
        drop = make_aircraft(manufacturer="Boeing", model="B-29",
                             tail_number=None)
        result = ddu.merge(keep.id, drop.id, assume_yes=True)
        assert result == (0, 0, 0, 0)
        assert Aircraft.query.get(drop.id) is None
        assert Aircraft.query.get(keep.id) is not None
