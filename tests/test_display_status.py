"""Visitor-perspective filtering on display_status.

Pinned design decisions (see migrate_display_status_drop_on_loan.sql):
  - `display_status` is the visitor's answer to "can I see this aircraft
    at this museum right now?"
  - `on_loan` is no longer a valid value. The API rejects writes that use
    it; existing rows have been folded to `on_display` by migration.
  - Visitor-facing endpoints either filter to `on_display` always
    (proximity, globe pin counts, dashboard stats) or accept
    `?visible_only=true` (detail endpoints, which serve admin too).

These tests are the tripwire that catches a curator-perspective value
leaking back into the vocabulary.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────
# Write-path: API rejects on_loan
# ─────────────────────────────────────────────────────────────────────

class TestRejectOnLoan:
    """A POST or PUT carrying display_status='on_loan' must 400. This is
    the only barrier preventing the old vocab from creeping back in via
    a stale client."""

    def test_create_exhibit_with_on_loan_rejected(
        self, admin_client, make_aircraft, make_museum
    ):
        a = make_aircraft(model="C-130", tail_number="55-0014")
        m = make_museum(name="AFM")
        r = admin_client.post("/api/v1/exhibits", json={
            "aircraft_id": a.id, "museum_id": m.id,
            "display_status": "on_loan",
        })
        assert r.status_code == 400, r.get_data(as_text=True)
        body = r.get_json()
        assert "display_status" in body["error"].lower()
        # Helpful error: list the valid values so the client can recover.
        assert "on_display" in body["message"]

    def test_create_aircraft_with_inline_on_loan_link_rejected(
        self, admin_client, make_museum
    ):
        m = make_museum(name="AFM")
        r = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Lockheed", "model": "C-130",
            "aircraft_type": "fixed_wing", "military_civilian": "military",
            "museum_id": m.id,
            "display_status": "on_loan",
        })
        assert r.status_code == 400

    def test_update_exhibit_to_on_loan_rejected(
        self, admin_client, make_aircraft, make_museum, make_link
    ):
        a = make_aircraft(model="C-130")
        m = make_museum(name="AFM")
        lnk = make_link(a, m)
        r = admin_client.put(f"/api/v1/exhibits/{lnk.id}", json={
            "display_status": "on_loan",
        })
        assert r.status_code == 400

    def test_arbitrary_garbage_status_rejected(
        self, admin_client, make_aircraft, make_museum
    ):
        """Same gate also rejects typos and made-up values — the
        allowlist is the only thing standing between curator imagination
        and a polluted column."""
        a = make_aircraft(model="C-130")
        m = make_museum(name="AFM")
        r = admin_client.post("/api/v1/exhibits", json={
            "aircraft_id": a.id, "museum_id": m.id,
            "display_status": "borrowed_kinda_sorta",
        })
        assert r.status_code == 400

    def test_valid_values_still_accepted(
        self, admin_client, make_aircraft, make_museum
    ):
        a = make_aircraft(model="C-130", tail_number="55-0014")
        m = make_museum(name="AFM")
        for status in ("on_display", "in_storage", "under_restoration"):
            # Fresh link each time — we delete after to avoid the
            # (aircraft_id, museum_id) uniqueness constraint.
            r = admin_client.post("/api/v1/exhibits", json={
                "aircraft_id": a.id, "museum_id": m.id,
                "display_status": status,
            })
            assert r.status_code == 201, (status, r.get_data(as_text=True))
            link_id = r.get_json()["id"]
            admin_client.delete(f"/api/v1/exhibits/{link_id}")


# ─────────────────────────────────────────────────────────────────────
# Read-path: visible_only filter on detail endpoints
# ─────────────────────────────────────────────────────────────────────

class TestAircraftDetailVisibleOnly:
    """The aircraft detail endpoint serves both the admin edit modal
    (which needs every link) and the public detail page (which must not
    advertise museums where the aircraft isn't actually viewable). The
    ?visible_only=true param threads that needle."""

    def test_without_filter_returns_all_links(
        self, client, make_aircraft, make_museum, make_link
    ):
        a = make_aircraft(model="C-130", tail_number="55-0014")
        m1, m2, m3 = (make_museum(name=n) for n in ("A", "B", "C"))
        make_link(a, m1, display_status="on_display")
        make_link(a, m2, display_status="in_storage")
        make_link(a, m3, display_status="under_restoration")

        r = client.get(f"/api/v1/aircraft/{a.id}")
        assert r.status_code == 200
        # Default behavior: admin gets the full picture.
        assert len(r.get_json()["museums"]) == 3

    def test_with_filter_returns_only_on_display(
        self, client, make_aircraft, make_museum, make_link
    ):
        a = make_aircraft(model="C-130", tail_number="55-0014")
        m1, m2, m3 = (make_museum(name=n) for n in ("A", "B", "C"))
        make_link(a, m1, display_status="on_display")
        make_link(a, m2, display_status="in_storage")
        make_link(a, m3, display_status="under_restoration")

        r = client.get(f"/api/v1/aircraft/{a.id}?visible_only=true")
        assert r.status_code == 200
        museums = r.get_json()["museums"]
        assert len(museums) == 1
        assert museums[0]["display_status"] == "on_display"


class TestMuseumDetailVisibleOnly:

    def test_with_filter_returns_only_on_display(
        self, client, make_aircraft, make_museum, make_link
    ):
        m = make_museum(name="AFM")
        a1 = make_aircraft(model="C-130", tail_number="55-0014")
        a2 = make_aircraft(model="B-29",  tail_number="44-0001")
        make_link(a1, m, display_status="on_display")
        make_link(a2, m, display_status="under_restoration")

        r = client.get(f"/api/v1/museums/{m.id}?visible_only=true")
        assert r.status_code == 200
        aircraft = r.get_json()["aircraft"]
        assert len(aircraft) == 1
        assert aircraft[0]["display_status"] == "on_display"


# ─────────────────────────────────────────────────────────────────────
# Endpoints that filter unconditionally (pure visitor-facing)
# ─────────────────────────────────────────────────────────────────────

class TestUnconditionalFilters:

    def test_nearest_excludes_non_on_display(
        self, client, make_aircraft, make_museum, make_link, monkeypatch
    ):
        """Proximity search must not tell a visitor to drive to a museum
        where the aircraft is actually in storage. This is the original
        UX bug the field rework was meant to fix."""
        a = make_aircraft(model="C-130", tail_number="55-0014")
        viewable = make_museum(
            name="AFM", city="Dayton", country="USA",
            latitude=39.78, longitude=-84.10,
        )
        hidden = make_museum(
            name="Storage Annex", city="Dayton", country="USA",
            latitude=39.78, longitude=-84.10,
        )
        make_link(a, viewable, display_status="on_display")
        make_link(a, hidden,   display_status="in_storage")

        # Stub the geocoder so the test doesn't need real ZIP lookups.
        import app as appmod
        monkeypatch.setattr(appmod, "_resolve_location", lambda loc: (39.78, -84.10))

        r = client.get("/api/v1/nearest?aircraft=C-130&location=45433")
        assert r.status_code == 200
        results = r.get_json()["results"]
        names = [hit["museum"]["name"] for hit in results]
        assert "AFM" in names
        assert "Storage Annex" not in names, (
            "in_storage link leaked into public proximity search!"
        )

    def test_stats_link_count_excludes_non_on_display(
        self, client, make_aircraft, make_museum, make_link
    ):
        """Dashboard 'aircraft on display' count must match what the
        proximity search would actually surface."""
        a1 = make_aircraft(model="C-130", tail_number="55-0014")
        a2 = make_aircraft(model="B-29",  tail_number="44-0001")
        m = make_museum(name="AFM")
        make_link(a1, m, display_status="on_display")
        make_link(a2, m, display_status="in_storage")

        r = client.get("/api/v1/stats")
        assert r.status_code == 200
        # Two links exist in the DB; only one is viewable.
        assert r.get_json()["link_count"] == 1

    def test_globe_pin_count_excludes_non_on_display(
        self, client, make_aircraft, make_museum, make_link
    ):
        """Globe shows aircraft_count per museum pin. Must match what a
        visitor would actually see if they showed up at the museum."""
        m = make_museum(
            name="AFM", country="USA",
            latitude=39.78, longitude=-84.10,
        )
        for tail in ("55-0001", "55-0002", "55-0003"):
            a = make_aircraft(model="C-130", tail_number=tail)
            make_link(a, m, display_status="on_display")
        a_hidden = make_aircraft(model="C-130", tail_number="55-9999")
        make_link(a_hidden, m, display_status="under_restoration")

        r = client.get("/api/v1/museums/globe")
        assert r.status_code == 200
        afm = next(pin for pin in r.get_json() if pin["name"] == "AFM")
        assert afm["aircraft_count"] == 3, (
            f"globe count includes non-on_display links: got {afm['aircraft_count']}, expected 3"
        )

    def test_globe_includes_museums_with_zero_viewable_aircraft(
        self, client, make_aircraft, make_museum, make_link
    ):
        """Edge case: a museum whose only links are in_storage should
        still appear as a pin (with count 0), not vanish from the map.
        This is why the filter lives on the outerjoin, not in WHERE."""
        m = make_museum(
            name="Restoration Hangar", country="USA",
            latitude=39.78, longitude=-84.10,
        )
        a = make_aircraft(model="C-130", tail_number="55-0001")
        make_link(a, m, display_status="under_restoration")

        r = client.get("/api/v1/museums/globe")
        pin = next((p for p in r.get_json() if p["name"] == "Restoration Hangar"), None)
        assert pin is not None, "museum dropped from globe because it has no viewable links"
        assert pin["aircraft_count"] == 0


# ─────────────────────────────────────────────────────────────────────
# Vocabulary pin — make sure code + docs stay in sync
# ─────────────────────────────────────────────────────────────────────

class TestVocabularyInSync:
    """Stops the slow drift of one surface adding `on_loan` back while
    another forgets to."""

    def test_server_allowlist_is_canonical(self):
        from app import _DISPLAY_STATUS_VALUES
        assert _DISPLAY_STATUS_VALUES == {
            "on_display", "in_storage", "under_restoration",
        }
        assert "on_loan" not in _DISPLAY_STATUS_VALUES

    @pytest.mark.parametrize("path", [
        "templates/admin_aircraft.html",
        "templates/admin_aircraft_new.html",
        "templates/admin_museums.html",
        "templates/api_docs.html",
    ])
    def test_on_loan_removed_from_admin_surfaces(self, path):
        """Admin dropdowns + API docs must not list on_loan as a value."""
        import os, re
        full = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), path)
        text = open(full).read()
        # `on_loan` as a quoted value or label entry. Lenient regex —
        # catches `'on_loan'`, `"on_loan"`, and the bare token used as a
        # CSS class would still appear in the role-badge stylings, which
        # we intentionally leave alone (they're not display_status).
        # So we look only for the quoted-value form.
        assert not re.search(r"['\"]on_loan['\"]", text), (
            f"{path} still references 'on_loan' as a display_status value"
        )
