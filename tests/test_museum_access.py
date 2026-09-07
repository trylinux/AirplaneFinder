"""Museum-level visitor access (``museums.access_type``).

Pinned design decisions (see migrate_museum_access.sql):
  - ``access_type`` is the museum-level counterpart to ``display_status``:
    display_status answers "can I see this aircraft?", access_type answers
    "can I get through the door at all?"
  - Values: ``public`` (walk in), ``appointment`` (call ahead / open house
    only), ``restricted`` (military base, escort or DoD ID).
  - Visitor-facing proximity endpoints hide ``restricted`` by default and
    take ``?include_restricted=1`` to opt back in. Restricted museums are
    still fully searchable and still serve their detail pages — they just
    don't win "where can I go and see one" queries.
  - Anything written before the column existed is ``public``. A CSV with no
    access_type column must import unchanged.

Why this exists: NAS Fallon's air park holds ~25 aircraft and Nellis AFB's
Freedom Park eight, both behind a gate a member of the public cannot pass.
Recording them without this distinction would send visitors to a fence.
"""

import io
import pytest


VALID = ("public", "appointment", "restricted")


# ─────────────────────────────────────────────────────────────────────
# Defaulting
# ─────────────────────────────────────────────────────────────────────

class TestDefaults:
    def test_new_museum_defaults_to_public(self, make_museum):
        m = make_museum(name="Defaults To Public")
        assert m.to_dict()["access_type"] == "public"

    def test_api_create_without_access_type_is_public(self, admin_client):
        r = admin_client.post("/api/v1/museums", json={
            "name": "No Access Field", "city": "Boise",
            "country": "United States", "region": "North America",
        })
        assert r.status_code in (200, 201), r.get_data(as_text=True)
        assert r.get_json()["access_type"] == "public"

    def test_bulk_import_csv_without_the_column_still_works(self, admin_client):
        """A museums CSV written before this column existed must import
        unchanged. This is the regression that would break every existing
        data/<state>/*_museums.csv file."""
        csv = (
            "name,city,state_province,country,postal_code,region,address,website,latitude,longitude\n"
            "Legacy Shape Museum,Reno,Nevada,United States,89502,North America,1 A St,https://x.test,39.5,-119.8\n"
        )
        r = admin_client.post(
            "/api/v1/museums/bulk_import",
            data={"file": (io.BytesIO(csv.encode()), "m.csv")},
            content_type="multipart/form-data",
        )
        assert r.status_code == 200, r.get_data(as_text=True)
        body = r.get_json()
        assert body.get("errors") == [] or len(body.get("errors", [])) == 0
        assert body.get("created") == 1


# ─────────────────────────────────────────────────────────────────────
# Validation
# ─────────────────────────────────────────────────────────────────────

class TestValidation:
    @pytest.mark.parametrize("value", VALID)
    def test_each_valid_value_accepted(self, admin_client, value):
        r = admin_client.post("/api/v1/museums", json={
            "name": f"Valid {value}", "city": "Fallon",
            "country": "United States", "region": "North America",
            "access_type": value,
        })
        assert r.status_code in (200, 201), r.get_data(as_text=True)
        assert r.get_json()["access_type"] == value

    @pytest.mark.parametrize("bad", ["", " ", "on_display", "private", "open", "PUBLIC!"])
    def test_garbage_rejected_or_defaulted(self, admin_client, bad):
        r = admin_client.post("/api/v1/museums", json={
            "name": f"Bad {bad!r}", "city": "Fallon",
            "country": "United States", "region": "North America",
            "access_type": bad,
        })
        if bad.strip() == "":
            # blank means "not specified" -> public
            assert r.status_code in (200, 201)
            assert r.get_json()["access_type"] == "public"
        else:
            assert r.status_code == 400, r.get_data(as_text=True)

    def test_value_is_case_insensitive(self, admin_client):
        r = admin_client.post("/api/v1/museums", json={
            "name": "Shouty", "city": "Fallon",
            "country": "United States", "region": "North America",
            "access_type": "RESTRICTED",
        })
        assert r.status_code in (200, 201), r.get_data(as_text=True)
        assert r.get_json()["access_type"] == "restricted"


# ─────────────────────────────────────────────────────────────────────
# Proximity filtering — the behaviour that actually matters
# ─────────────────────────────────────────────────────────────────────

@pytest.fixture
def near_reno(make_museum, make_aircraft, make_link):
    """Two museums a few miles apart holding the same type. The nearer one
    is on a base; the farther one is public."""
    base = make_museum(name="Base Air Park", city="Fallon",
                       state_province="Nevada", region="North America",
                       latitude=39.50, longitude=-119.80,
                       access_type="restricted")
    public = make_museum(name="Town Museum", city="Reno",
                         state_province="Nevada", region="North America",
                         latitude=39.60, longitude=-119.80,
                         access_type="public")
    a1 = make_aircraft(model="F-4", variant="C", tail_number="64-0806")
    a2 = make_aircraft(model="F-4", variant="E", tail_number="66-0329")
    make_link(a1, base)
    make_link(a2, public)
    return {"base": base, "public": public}


class TestMuseumsNearest:
    def test_restricted_hidden_by_default(self, client, near_reno):
        r = client.get("/api/v1/museums/nearest?lat=39.5&lon=-119.8")
        assert r.status_code == 200, r.get_data(as_text=True)
        names = [x["museum"]["name"] if "museum" in x else x["name"]
                 for x in r.get_json()["results"]]
        assert "Base Air Park" not in names
        assert "Town Museum" in names

    def test_include_restricted_opts_back_in(self, client, near_reno):
        r = client.get(
            "/api/v1/museums/nearest?lat=39.5&lon=-119.8&include_restricted=1")
        assert r.status_code == 200
        names = [x["museum"]["name"] if "museum" in x else x["name"]
                 for x in r.get_json()["results"]]
        assert "Base Air Park" in names


class TestNearestAircraft:
    def test_restricted_museum_does_not_win_the_query(self, client, near_reno):
        """The base is nearer, but it must not be the answer to
        'where can I go and see an F-4'."""
        r = client.get("/api/v1/nearest?aircraft=F-4&location=89502")
        if r.status_code == 404:
            pytest.skip("geocoder unavailable in this environment")
        assert r.status_code == 200, r.get_data(as_text=True)
        names = [x["museum"]["name"] for x in r.get_json().get("results", [])]
        assert "Base Air Park" not in names

    def test_include_restricted_shows_it(self, client, near_reno):
        r = client.get(
            "/api/v1/nearest?aircraft=F-4&location=89502&include_restricted=1")
        if r.status_code == 404:
            pytest.skip("geocoder unavailable in this environment")
        assert r.status_code == 200
        names = [x["museum"]["name"] for x in r.get_json().get("results", [])]
        assert "Base Air Park" in names


class TestStillDiscoverable:
    """Hiding from proximity must not mean hiding from the database."""

    def test_restricted_museum_still_searchable(self, client, near_reno):
        r = client.get("/api/v1/museums/search?q=Base Air Park")
        assert r.status_code == 200
        assert any(m["name"] == "Base Air Park" for m in r.get_json()["results"])

    def test_restricted_museum_detail_still_served(self, client, near_reno):
        r = client.get(f"/api/v1/museums/{near_reno['base'].id}")
        assert r.status_code == 200
        assert r.get_json()["museum"]["access_type"] == "restricted"
