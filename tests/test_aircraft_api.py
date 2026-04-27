"""High-bug-rate paths on the aircraft API.

Pinned regressions:
  - link_id needed to be added to /api/v1/aircraft/<id>'s museums dicts
    (the spread-then-overwrite ordering quietly dropped it).
  - (model, tail_number) uniqueness with whitespace handling.
  - sort_by must accept whitelisted columns and silently fall back on
    anything else (covered fully in test_helpers.py — here we hit the
    HTTP surface).
"""

import pytest


# ─────────────────────────────────────────────────────────────────────
# /api/v1/aircraft/<id>  — link_id must be present on each museum dict
# ─────────────────────────────────────────────────────────────────────

class TestAircraftDetailLinkId:
    """The admin UI's unlink button calls
    DELETE /api/v1/exhibits/<link_id>. If link_id is missing from the
    detail response, no unlink is possible."""

    def test_link_id_present_on_each_museum(
        self, client, make_aircraft, make_museum, make_link
    ):
        a = make_aircraft(model="C-130", tail_number="55-0014")
        m1 = make_museum(name="AFM")
        m2 = make_museum(name="Smithsonian")
        l1 = make_link(a, m1)
        l2 = make_link(a, m2, display_status="in_storage")

        r = client.get(f"/api/v1/aircraft/{a.id}")
        assert r.status_code == 200
        data = r.get_json()
        link_ids = sorted(m["link_id"] for m in data["museums"])
        assert link_ids == sorted([l1.id, l2.id])

    def test_museum_id_also_still_present(
        self, client, make_aircraft, make_museum, make_link
    ):
        """The spread-then-overwrite ordering matters: museum.id must
        survive even though we add a link_id field too."""
        a = make_aircraft(model="C-130", tail_number="55-0014")
        m = make_museum(name="AFM")
        make_link(a, m)
        r = client.get(f"/api/v1/aircraft/{a.id}")
        museum = r.get_json()["museums"][0]
        assert museum["id"] == m.id
        assert "link_id" in museum


# ─────────────────────────────────────────────────────────────────────
# (model, tail_number) uniqueness check on create / update
# ─────────────────────────────────────────────────────────────────────

class TestAircraftUniqueness:
    """Pinned regression: a duplicate aircraft creation used to succeed.
    We now reject 409 at the API and keep a UNIQUE INDEX as a backstop."""

    def test_creating_duplicate_returns_409(self, admin_client, make_aircraft):
        make_aircraft(model="C-130", tail_number="55-0014")
        r = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Lockheed", "model": "C-130", "tail_number": "55-0014",
            "aircraft_type": "fixed_wing", "military_civilian": "military",
        })
        assert r.status_code == 409
        body = r.get_json()
        assert "55-0014" in body["error"]
        assert body["existing_id"] is not None

    def test_whitespace_padded_tail_is_normalized(self, admin_client, make_aircraft):
        """A leading/trailing space shouldn't sneak a duplicate past the check."""
        make_aircraft(model="C-130", tail_number="55-0014")
        r = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Lockheed", "model": "C-130", "tail_number": "  55-0014  ",
            "aircraft_type": "fixed_wing", "military_civilian": "military",
        })
        assert r.status_code == 409, "whitespace-padded duplicate slipped past!"

    def test_null_tail_does_not_collide_with_other_null_tails(self, admin_client):
        """Multiple aircraft without tail numbers (display models, replicas,
        etc.) must coexist."""
        for _ in range(2):
            r = admin_client.post("/api/v1/aircraft", json={
                "manufacturer": "Lockheed", "model": "C-130",
                "aircraft_type": "fixed_wing", "military_civilian": "military",
            })
            assert r.status_code == 201

    def test_empty_tail_treated_as_null(self, admin_client):
        """Submitting tail_number='' should coexist with another '' just
        like NULL would. _normalize_tail_number folds them together."""
        r1 = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Lockheed", "model": "C-130", "tail_number": "",
            "aircraft_type": "fixed_wing", "military_civilian": "military",
        })
        r2 = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Lockheed", "model": "C-130", "tail_number": "   ",
            "aircraft_type": "fixed_wing", "military_civilian": "military",
        })
        assert r1.status_code == 201 and r2.status_code == 201

    def test_different_model_with_same_tail_is_ok(self, admin_client, make_aircraft):
        """Tail uniqueness is per-model. Real-world tail numbers do
        get reused across different aircraft types."""
        make_aircraft(model="C-130", tail_number="55-0014")
        r = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Boeing", "model": "B-52", "tail_number": "55-0014",
            "aircraft_type": "fixed_wing", "military_civilian": "military",
        })
        assert r.status_code == 201

    def test_update_to_existing_pair_rejected(
        self, admin_client, make_aircraft
    ):
        """Editing an aircraft to take another's tail number should be
        blocked, otherwise the unique index would catch it later but with
        a worse error."""
        make_aircraft(model="C-130", tail_number="55-0014")
        b = make_aircraft(model="C-130", tail_number="55-0099")
        r = admin_client.put(f"/api/v1/aircraft/{b.id}", json={
            "tail_number": "55-0014",
        })
        assert r.status_code == 409


# ─────────────────────────────────────────────────────────────────────
# Sort param via HTTP
# ─────────────────────────────────────────────────────────────────────

class TestAircraftSearchSort:

    def test_sort_by_manufacturer_desc(self, admin_client, make_aircraft):
        make_aircraft(model="C-130", manufacturer="Lockheed")
        make_aircraft(model="B-29",  manufacturer="Boeing")
        make_aircraft(model="A-10",  manufacturer="Fairchild")
        r = admin_client.get("/api/v1/aircraft/search?sort_by=manufacturer&sort_dir=desc")
        manufacturers = [a["manufacturer"] for a in r.get_json()["results"]]
        assert manufacturers == sorted(manufacturers, reverse=True)

    def test_unknown_sort_field_does_not_error(self, admin_client, make_aircraft):
        """Probe with a non-whitelisted name. Endpoint should respond 200
        with the default ordering, not 500."""
        make_aircraft(model="C-130")
        r = admin_client.get("/api/v1/aircraft/search?sort_by=password_hash")
        assert r.status_code == 200

    def test_sql_injection_shaped_sort_does_not_error(
        self, admin_client, make_aircraft
    ):
        make_aircraft(model="C-130")
        r = admin_client.get(
            "/api/v1/aircraft/search?sort_by=1%3B+DROP+TABLE+users--"
        )
        assert r.status_code == 200, (
            "injection-shaped sort_by should fall back silently, not error"
        )
