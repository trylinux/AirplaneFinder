"""Museum proximity search + aviation facts.

Two features:

- ``GET /api/v1/museums/nearest`` answers "what's near me?", where the
  existing ``/api/v1/nearest`` answers "where can I see a B-17?". Mobile
  passes lat/lon from the browser; the web form passes a typed location.
- ``AircraftFact`` and its endpoints back the /facts page and /admin/facts.
  ``aircraft_id`` is deliberately nullable — most trivia has no single
  airframe — and ON DELETE SET NULL so removing an aircraft doesn't destroy
  the writing about it.
"""

import json

import pytest


# ─────────────────────────────────────────────────────────────────────
# Museums near a point
# ─────────────────────────────────────────────────────────────────────

class TestMuseumsNearest:

    @pytest.fixture
    def three_museums(self, make_museum, make_aircraft, make_link):
        """Los Angeles, San Diego, and one with no coordinates."""
        la = make_museum(name="LA Museum", city="Los Angeles",
                         latitude=34.0522, longitude=-118.2437)
        sd = make_museum(name="SD Museum", city="San Diego",
                         latitude=32.7157, longitude=-117.1611)
        nowhere = make_museum(name="No Coords Museum", city="Mystery")
        a1 = make_aircraft(model="B-17", variant="G", tail_number="44-1")
        a2 = make_aircraft(model="P-51", variant="D", tail_number="44-2")
        make_link(a1, la)
        make_link(a2, la, display_status="in_storage")   # must NOT be counted
        make_link(a1, sd) if False else None
        return la, sd, nowhere

    def test_requires_location_or_coords(self, client):
        r = client.get("/api/v1/museums/nearest")
        assert r.status_code == 400
        assert "lat" in r.get_json()["error"]

    def test_lat_lon_returns_sorted_by_distance(self, client, three_museums):
        # Origin: downtown Los Angeles — LA Museum must come first.
        r = client.get("/api/v1/museums/nearest?lat=34.05&lon=-118.24")
        assert r.status_code == 200
        d = r.get_json()
        names = [x["museum"]["name"] for x in d["results"]]
        assert names[0] == "LA Museum"
        assert "SD Museum" in names
        assert d["results"][0]["distance_miles"] < d["results"][1]["distance_miles"]

    def test_museum_without_coordinates_is_omitted(self, client, three_museums):
        """A museum with no pin can't be ranked by distance, so it is left
        out rather than shown with a fake or zero distance."""
        r = client.get("/api/v1/museums/nearest?lat=34.05&lon=-118.24")
        names = [x["museum"]["name"] for x in r.get_json()["results"]]
        assert "No Coords Museum" not in names

    def test_aircraft_count_excludes_non_display(self, client, three_museums):
        """LA has two links but one is in_storage — the count a visitor sees
        must reflect only what they can actually go and look at."""
        r = client.get("/api/v1/museums/nearest?lat=34.05&lon=-118.24")
        la = next(x for x in r.get_json()["results"] if x["museum"]["name"] == "LA Museum")
        assert la["aircraft_count"] == 1

    def test_radius_filters(self, client, three_museums):
        r = client.get("/api/v1/museums/nearest?lat=34.05&lon=-118.24&radius=25")
        names = [x["museum"]["name"] for x in r.get_json()["results"]]
        assert names == ["LA Museum"]          # San Diego is ~110 miles away

    def test_limit_caps_results_but_total_reports_all(self, client, three_museums):
        r = client.get("/api/v1/museums/nearest?lat=34.05&lon=-118.24&limit=1")
        d = r.get_json()
        assert d["count"] == 1
        assert d["total_in_range"] == 2

    def test_rejects_out_of_range_coordinates(self, client, three_museums):
        assert client.get("/api/v1/museums/nearest?lat=99&lon=0").status_code == 400
        assert client.get("/api/v1/museums/nearest?lat=0&lon=999").status_code == 400

    def test_zero_aircraft_museum_still_listed(self, client, make_museum):
        """Somewhere with nothing on display is still somewhere you can go —
        it should appear with a count of 0, not vanish."""
        make_museum(name="Empty Museum", city="Nowhere",
                    latitude=34.05, longitude=-118.24)
        r = client.get("/api/v1/museums/nearest?lat=34.05&lon=-118.24")
        res = r.get_json()["results"]
        assert res and res[0]["museum"]["name"] == "Empty Museum"
        assert res[0]["aircraft_count"] == 0

    def test_endpoint_is_public(self, client, three_museums):
        assert client.get("/api/v1/museums/nearest?lat=34&lon=-118").status_code == 200


# ─────────────────────────────────────────────────────────────────────
# Facts
# ─────────────────────────────────────────────────────────────────────

class TestFactsRead:

    @pytest.fixture
    def facts(self, db_session, make_aircraft):
        import models
        ac = make_aircraft(model="SR-71", variant="A", tail_number="61-7960")
        rows = [
            models.AircraftFact(fact="Visible general fact."),
            models.AircraftFact(fact="Fact about the Blackbird.", aircraft_id=ac.id),
            models.AircraftFact(fact="Hidden fact.", is_active=False),
        ]
        db_session.add_all(rows)
        db_session.commit()
        return ac

    def test_list_excludes_inactive_by_default(self, client, facts):
        d = client.get("/api/v1/facts").get_json()
        texts = [f["fact"] for f in d["results"]]
        assert "Hidden fact." not in texts
        assert d["total"] == 2

    def test_include_inactive_shows_hidden(self, client, facts):
        d = client.get("/api/v1/facts?include_inactive=true").get_json()
        assert d["total"] == 3

    def test_filter_by_aircraft(self, client, facts):
        d = client.get(f"/api/v1/facts?aircraft_id={facts.id}").get_json()
        assert d["total"] == 1
        assert d["results"][0]["aircraft"]["full_designation"] == "SR-71A"

    def test_random_returns_an_active_fact(self, client, facts):
        r = client.get("/api/v1/facts/random")
        assert r.status_code == 200
        assert r.get_json()["fact"] != "Hidden fact."

    def test_random_404s_when_empty(self, client, db_session):
        assert client.get("/api/v1/facts/random").status_code == 404

    def test_random_varies(self, client, db_session):
        """Not a strict randomness test — just that with many facts we don't
        always get the same one back, which would mean the ordering isn't
        random at all."""
        import models
        for i in range(25):
            db_session.add(models.AircraftFact(fact=f"Fact number {i}."))
        db_session.commit()
        seen = {client.get("/api/v1/facts/random").get_json()["fact"] for _ in range(15)}
        assert len(seen) > 1


class TestFactsWrite:

    def test_create_requires_auth(self, client, db_session):
        r = client.post("/api/v1/facts", json={"fact": "x"})
        assert r.status_code == 401

    def test_viewer_cannot_create(self, viewer_client, db_session):
        r = viewer_client.post("/api/v1/facts", json={"fact": "x"})
        assert r.status_code == 403

    def test_manager_can_create(self, manager_client, db_session):
        r = manager_client.post("/api/v1/facts", json={"fact": "A new fact."})
        assert r.status_code == 201
        assert r.get_json()["fact"] == "A new fact."

    def test_empty_fact_rejected(self, admin_client, db_session):
        assert admin_client.post("/api/v1/facts", json={"fact": "   "}).status_code == 400

    def test_overlong_fact_rejected(self, admin_client, db_session):
        r = admin_client.post("/api/v1/facts", json={"fact": "x" * 5001})
        assert r.status_code == 400

    def test_unknown_aircraft_id_rejected(self, admin_client, db_session):
        r = admin_client.post("/api/v1/facts",
                              json={"fact": "x", "aircraft_id": 99999})
        assert r.status_code == 404

    def test_non_integer_aircraft_id_rejected(self, admin_client, db_session):
        r = admin_client.post("/api/v1/facts",
                              json={"fact": "x", "aircraft_id": "not-a-number"})
        assert r.status_code == 400

    def test_create_with_aircraft_link(self, admin_client, db_session, make_aircraft):
        ac = make_aircraft(model="B-17", variant="G", tail_number="44-83624")
        r = admin_client.post("/api/v1/facts",
                              json={"fact": "About the Fort.", "aircraft_id": ac.id})
        assert r.status_code == 201
        assert r.get_json()["aircraft"]["full_designation"] == "B-17G"

    def test_hide_via_patch(self, admin_client, db_session):
        import models
        fid = admin_client.post("/api/v1/facts", json={"fact": "temp"}).get_json()["id"]
        r = admin_client.patch(f"/api/v1/facts/{fid}", json={"is_active": False})
        assert r.status_code == 200
        assert r.get_json()["is_active"] is False
        # hidden, but not destroyed
        assert models.AircraftFact.query.get(fid) is not None

    # NOTE: admin_client and manager_client are built on the SAME underlying
    # test client (see conftest), so requesting both in one test leaves you
    # logged in as whichever authenticated last. These are split so each
    # test exercises exactly one role.

    def test_manager_cannot_delete(self, manager_client, db_session):
        import models
        f = models.AircraftFact(fact="temp")
        db_session.add(f); db_session.commit()
        assert manager_client.delete(f"/api/v1/facts/{f.id}").status_code == 403

    def test_admin_can_delete(self, admin_client, db_session):
        import models
        f = models.AircraftFact(fact="temp")
        db_session.add(f); db_session.commit()
        assert admin_client.delete(f"/api/v1/facts/{f.id}").status_code == 200
        assert models.AircraftFact.query.get(f.id) is None

    def test_deleting_aircraft_keeps_the_fact(self, admin_client, db_session, make_aircraft):
        """ON DELETE SET NULL, not CASCADE. Removing an aircraft record
        shouldn't silently destroy the writing about it — the fact survives
        and becomes a general one."""
        import models
        ac = make_aircraft(model="P-38", variant="L", tail_number="44-53236")
        fid = admin_client.post("/api/v1/facts",
                                json={"fact": "About the Lightning.",
                                      "aircraft_id": ac.id}).get_json()["id"]
        admin_client.delete(f"/api/v1/aircraft/{ac.id}")
        db_session.expire_all()
        fact = models.AircraftFact.query.get(fid)
        assert fact is not None, "fact was destroyed with its aircraft"
        assert fact.aircraft_id is None


class TestFactPages:

    def test_facts_page_public(self, client):
        r = client.get("/facts")
        assert r.status_code == 200
        assert "Aviation Facts" in r.get_data(as_text=True)

    def test_near_me_page_public(self, client):
        r = client.get("/near-me")
        assert r.status_code == 200
        body = r.get_data(as_text=True)
        assert "Museums Near Me" in body
        assert "/api/v1/museums/nearest" in body

    def test_admin_facts_requires_login(self, client):
        r = client.get("/admin/facts")
        assert r.status_code in (301, 302)
        assert "/login" in r.headers.get("Location", "")

    def test_admin_facts_renders(self, admin_client):
        r = admin_client.get("/admin/facts")
        assert r.status_code == 200
        assert "Add a Fact" in r.get_data(as_text=True)

    def test_directions_link_builder_present(self, client):
        """The maps handoff has to pick Apple vs Google per platform —
        assert both branches ship rather than silently regressing to one."""
        body = client.get("/near-me").get_data(as_text=True)
        assert "maps.apple.com" in body
        assert "google.com/maps/dir" in body
