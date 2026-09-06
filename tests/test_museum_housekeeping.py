"""scripts/fix_museum_housekeeping.py — the three judgment-call fixes.

The interesting one is the SPLIT. Five seed records are each linked to
several museums, which says one airframe is in several places. They're
type-level records ("a Wright Flyer") and every museum involved genuinely
holds an example — so the fix is to give each museum its own record, NOT
to delete the extra links, which would wrongly say those museums hold
nothing.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))


@pytest.fixture
def mod():
    import fix_museum_housekeeping
    return fix_museum_housekeeping


class FakeClient:
    """Records calls instead of making them."""
    base_url = "http://test"
    api_key = "amt_test"

    def __init__(self, museums=None, exhibits=None):
        self._museums = museums or {}
        self._exhibits = exhibits or []
        self.posts, self.deletes = [], []

    def get_museum(self, mid):
        from airplane_api import ApiError
        if mid not in self._museums:
            raise ApiError(404, {"error": "not found"}, f"/api/v1/museums/{mid}")
        return self._museums[mid]

    def get(self, path, **params):
        if path == "/api/v1/exhibits":
            return {"results": self._exhibits}
        raise AssertionError(path)

    def post(self, path, json=None, **kw):
        self.posts.append((path, json)); return {"id": 999}

    def delete(self, path, **kw):
        self.deletes.append(path); return {"deleted": True}


def museum(mid, name, aircraft=()):
    return {"museum": {"id": mid, "name": name, "city": "Chantilly"},
            "aircraft": list(aircraft)}


class TestUdvarHazyMerge:

    def test_moves_aircraft_then_deletes_the_duplicate(self, mod):
        c = FakeClient(museums={
            22: museum(22, "Steven F. Udvar-Hazy Center", [{"id": 1}]),
            50: museum(50, "Smithsonian Institution Steven F. Udvar-Hazy Center",
                       [{"id": 7, "link_id": 179, "full_designation": "SR-71-A",
                         "tail_number": "61-7972", "display_status": "on_display"}]),
        })
        mod.merge_udvar_hazy(c, dry=False)
        # new link created on the surviving museum
        assert ("/api/v1/exhibits", {"aircraft_id": 7, "museum_id": 22,
                                     "display_status": "on_display"}) in c.posts
        # old link removed, then the duplicate museum
        assert "/api/v1/exhibits/179" in c.deletes
        assert "/api/v1/museums/50" in c.deletes

    def test_link_is_created_before_the_old_one_is_removed(self, mod):
        """Ordering matters: if the delete ran first and the create failed,
        the aircraft would be orphaned."""
        c = FakeClient(museums={
            22: museum(22, "keep"),
            50: museum(50, "drop", [{"id": 7, "link_id": 179,
                                     "full_designation": "X", "tail_number": None}]),
        })
        order = []
        c.post = lambda p, json=None, **k: order.append("post") or {"id": 1}
        c.delete = lambda p, **k: order.append("delete") or {}
        mod.merge_udvar_hazy(c, dry=False)
        assert order[0] == "post"

    def test_dry_run_changes_nothing(self, mod):
        c = FakeClient(museums={
            22: museum(22, "keep"),
            50: museum(50, "drop", [{"id": 7, "link_id": 179,
                                     "full_designation": "X", "tail_number": None}]),
        })
        mod.merge_udvar_hazy(c, dry=True)
        assert c.posts == [] and c.deletes == []

    def test_already_merged_is_a_no_op(self, mod):
        c = FakeClient(museums={22: museum(22, "keep")})
        assert mod.merge_udvar_hazy(c, dry=False) == 0
        assert c.deletes == []


class TestSplitSharedRecords:

    def _exhibits(self):
        ac = {"id": 67, "full_designation": "A6M-Zero", "manufacturer": "Mitsubishi",
              "model": "A6M", "aircraft_type": "fixed_wing", "military_civilian": "military",
              "aliases": ["Zero", "Zeke"]}
        return [
            {"id": 120, "aircraft": ac, "museum": {"id": 1, "name": "Pearl Harbor"},
             "display_status": "on_display"},
            {"id": 133, "aircraft": ac, "museum": {"id": 2, "name": "Hamamatsu"},
             "display_status": "on_display"},
            {"id": 134, "aircraft": ac, "museum": {"id": 3, "name": "Australian War Memorial"},
             "display_status": "on_display"},
        ]

    def test_first_museum_keeps_the_original(self, mod):
        c = FakeClient(exhibits=self._exhibits())
        mod.split_shared_records(c, dry=False)
        # only the 2nd and 3rd links are replaced
        assert "/api/v1/exhibits/120" not in c.deletes
        assert "/api/v1/exhibits/133" in c.deletes
        assert "/api/v1/exhibits/134" in c.deletes

    def test_each_extra_museum_gets_its_own_record(self, mod):
        c = FakeClient(exhibits=self._exhibits())
        n = mod.split_shared_records(c, dry=False)
        assert n == 2
        created = [p for p in c.posts if p[0] == "/api/v1/aircraft"]
        assert len(created) == 2
        assert {p[1]["museum_id"] for p in created} == {2, 3}

    def test_clone_copies_identity_but_not_a_tail_number(self, mod):
        """These records have no serial. Copying one would be inventing an
        identity; leaving it blank is honest and never collides."""
        c = FakeClient(exhibits=self._exhibits())
        mod.split_shared_records(c, dry=False)
        payload = [p[1] for p in c.posts if p[0] == "/api/v1/aircraft"][0]
        assert payload["manufacturer"] == "Mitsubishi"
        assert payload["model"] == "A6M"
        assert payload["aliases"] == ["Zero", "Zeke"]
        assert "tail_number" not in payload

    def test_singly_linked_aircraft_untouched(self, mod):
        c = FakeClient(exhibits=[
            {"id": 1, "aircraft": {"id": 5, "full_designation": "B-17-G", "model": "B-17"},
             "museum": {"id": 1, "name": "Only One"}, "display_status": "on_display"},
        ])
        assert mod.split_shared_records(c, dry=False) == 0
        assert c.posts == [] and c.deletes == []

    def test_dry_run_changes_nothing(self, mod):
        c = FakeClient(exhibits=self._exhibits())
        assert mod.split_shared_records(c, dry=True) == 2
        assert c.posts == [] and c.deletes == []


class TestHillierDeletion:

    def test_deletes_when_empty(self, mod):
        c = FakeClient(museums={80: museum(80, "Hillier Air Museum")})
        assert mod.delete_hillier(c, dry=False) == 1
        assert "/api/v1/museums/80" in c.deletes

    def test_refuses_if_aircraft_appeared(self, mod):
        """Someone may have added data since. Don't delete a museum that is
        no longer empty just because a script said so."""
        c = FakeClient(museums={80: museum(80, "Hillier", [{"id": 1}])})
        assert mod.delete_hillier(c, dry=False) == 0
        assert c.deletes == []

    def test_already_deleted_is_a_no_op(self, mod):
        c = FakeClient(museums={})
        assert mod.delete_hillier(c, dry=False) == 0
