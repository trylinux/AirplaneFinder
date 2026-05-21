"""GET /api/v1/exhibits flat-list endpoint + /admin/exhibits page route.

The exhibits overview page was removed when exhibit-link management moved
into the aircraft/museum edit modals, then rebuilt against a real backing
endpoint instead of the old stitch-it-together-from-N-detail-calls approach.

These tests pin the endpoint's response shape, its search and sort params,
and the page route's login gate.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────
# Endpoint shape
# ─────────────────────────────────────────────────────────────────────

class TestExhibitsEndpointShape:

    def test_empty_returns_empty_list(self, client):
        r = client.get("/api/v1/exhibits")
        assert r.status_code == 200
        assert r.get_json() == {"results": [], "total": 0}

    def test_one_row_per_link(self, client, make_aircraft, make_museum, make_link):
        """One Aircraft at two museums → two exhibit rows."""
        a = make_aircraft(manufacturer="Lockheed", model="C-130", variant="A")
        make_link(a, make_museum(name="Air Zoo"))
        make_link(a, make_museum(name="Pima"))
        data = client.get("/api/v1/exhibits").get_json()
        assert data["total"] == 2
        assert len(data["results"]) == 2

    def test_row_carries_aircraft_and_museum(
        self, client, make_aircraft, make_museum, make_link
    ):
        a = make_aircraft(manufacturer="Grumman", model="F-14", variant="A",
                          tail_number="160694")
        m = make_museum(name="Intrepid")
        link = make_link(a, m, display_status="in_storage", notes="hangar 3")

        row = client.get("/api/v1/exhibits").get_json()["results"][0]
        # `id` is the AircraftMuseum (link) primary key — what the UI
        # passes to PUT/DELETE /api/v1/exhibits/<id>.
        assert row["id"] == link.id
        assert row["display_status"] == "in_storage"
        assert row["notes"] == "hangar 3"
        assert row["aircraft"]["full_designation"] == "F-14-A"
        assert row["aircraft"]["tail_number"] == "160694"
        assert row["museum"]["name"] == "Intrepid"

    def test_row_includes_aircraft_aliases(
        self, client, db_session, make_aircraft, make_museum, make_link
    ):
        """to_dict() reads aircraft.aliases — the endpoint eager-loads them,
        so this exercises the contains_eager + joinedload path."""
        import models
        a = make_aircraft(manufacturer="Boeing", model="B-29",
                          tail_number="44-27297")
        db_session.add(models.AircraftAlias(aircraft_id=a.id, alias="Superfortress"))
        db_session.commit()
        make_link(a, make_museum(name="Boeing Museum"))

        row = client.get("/api/v1/exhibits").get_json()["results"][0]
        assert "Superfortress" in row["aircraft"]["aliases"]

    def test_endpoint_is_public(self, client, make_aircraft, make_museum, make_link):
        """No auth needed — consistent with the other GET read endpoints."""
        make_link(make_aircraft(model="C-130"), make_museum(name="Air Zoo"))
        assert client.get("/api/v1/exhibits").status_code == 200


# ─────────────────────────────────────────────────────────────────────
# Search (?q=)
# ─────────────────────────────────────────────────────────────────────

class TestExhibitsSearch:

    def test_search_by_museum_name(
        self, client, make_aircraft, make_museum, make_link
    ):
        a = make_aircraft(model="C-130")
        make_link(a, make_museum(name="Air Zoo"))
        make_link(a, make_museum(name="Pima Air Museum"))
        data = client.get("/api/v1/exhibits?q=pima").get_json()
        assert data["total"] == 1
        assert data["results"][0]["museum"]["name"] == "Pima Air Museum"

    def test_search_by_aircraft_designation(
        self, client, make_aircraft, make_museum, make_link
    ):
        m = make_museum(name="Shared")
        make_link(make_aircraft(model="C-130", variant="A", tail_number="1"), m)
        make_link(make_aircraft(model="B-52", variant="D", tail_number="2",
                                manufacturer="Boeing"), m)
        data = client.get("/api/v1/exhibits?q=B-52").get_json()
        assert data["total"] == 1
        assert data["results"][0]["aircraft"]["model"] == "B-52"

    def test_search_by_manufacturer(
        self, client, make_aircraft, make_museum, make_link
    ):
        m = make_museum(name="Shared")
        make_link(make_aircraft(model="C-130", manufacturer="Lockheed",
                                tail_number="1"), m)
        make_link(make_aircraft(model="B-52", manufacturer="Boeing",
                                tail_number="2"), m)
        assert client.get("/api/v1/exhibits?q=boeing").get_json()["total"] == 1

    def test_search_no_match_returns_empty(
        self, client, make_aircraft, make_museum, make_link
    ):
        make_link(make_aircraft(model="C-130"), make_museum(name="Air Zoo"))
        assert client.get("/api/v1/exhibits?q=zzzzz").get_json()["total"] == 0


# ─────────────────────────────────────────────────────────────────────
# Sort (?sort_by= / ?sort_dir=)
# ─────────────────────────────────────────────────────────────────────

class TestExhibitsSort:

    def _seed_three_museums(self, make_aircraft, make_museum, make_link):
        """One link each at Charlie / Alpha / Bravo — names chosen so the
        default order and an explicit desc sort are both observable."""
        for name in ["Charlie Museum", "Alpha Museum", "Bravo Museum"]:
            a = make_aircraft(model="C-130", tail_number=name)
            make_link(a, make_museum(name=name))

    def test_default_order_is_museum_name(
        self, client, make_aircraft, make_museum, make_link
    ):
        self._seed_three_museums(make_aircraft, make_museum, make_link)
        names = [row["museum"]["name"]
                 for row in client.get("/api/v1/exhibits").get_json()["results"]]
        assert names == ["Alpha Museum", "Bravo Museum", "Charlie Museum"]

    def test_sort_museum_desc(
        self, client, make_aircraft, make_museum, make_link
    ):
        self._seed_three_museums(make_aircraft, make_museum, make_link)
        r = client.get("/api/v1/exhibits?sort_by=museum&sort_dir=desc")
        names = [row["museum"]["name"] for row in r.get_json()["results"]]
        assert names == ["Charlie Museum", "Bravo Museum", "Alpha Museum"]

    def test_sort_by_status(
        self, client, make_aircraft, make_museum, make_link
    ):
        m = make_museum(name="Shared")
        make_link(make_aircraft(model="C-130", tail_number="a"), m,
                  display_status="under_restoration")
        make_link(make_aircraft(model="C-130", tail_number="b"), m,
                  display_status="in_storage")
        make_link(make_aircraft(model="C-130", tail_number="c"), m,
                  display_status="on_display")
        r = client.get("/api/v1/exhibits?sort_by=status&sort_dir=asc")
        statuses = [row["display_status"] for row in r.get_json()["results"]]
        assert statuses == ["in_storage", "on_display", "under_restoration"]

    def test_unwhitelisted_sort_by_falls_back(
        self, client, make_aircraft, make_museum, make_link
    ):
        """A column not in _EXHIBIT_SORT_COLUMNS is ignored, not an error —
        the endpoint falls back to its default ordering."""
        self._seed_three_museums(make_aircraft, make_museum, make_link)
        r = client.get("/api/v1/exhibits?sort_by=notes")
        assert r.status_code == 200
        names = [row["museum"]["name"] for row in r.get_json()["results"]]
        assert names == ["Alpha Museum", "Bravo Museum", "Charlie Museum"]


# ─────────────────────────────────────────────────────────────────────
# /admin/exhibits page route
# ─────────────────────────────────────────────────────────────────────

class TestExhibitsPageRoute:

    def test_anonymous_redirected_to_login(self, client):
        r = client.get("/admin/exhibits")
        assert r.status_code in (301, 302)
        assert "/login" in r.headers.get("Location", "")

    def test_logged_in_user_sees_page(self, admin_client):
        r = admin_client.get("/admin/exhibits")
        assert r.status_code == 200
        body = r.get_data(as_text=True)
        assert "All Exhibit Links" in body
        # The page's JS fetches the new endpoint.
        assert "/api/v1/exhibits" in body
