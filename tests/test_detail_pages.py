"""Dedicated aircraft and museum pages at /aircraft/<id> and /museums/<id>.

These replaced a desktop redirect to ``/aircraft?focus=<id>`` that popped a
modal. The modal had no room for the description, the aliases or the airframe
history, so 2,200 aircraft carried research prose nobody could read.

The contract these tests hold:
  - both routes render 200 for desktop AND mobile (one server-rendered
    template picks its layout from ``is_mobile``);
  - the description is on the page;
  - every alias is on the page, as a link into the directory search — that
    is what aliases are *for*, and a plain-text alias is a regression;
  - museum links that the public cannot see are not advertised.
"""

import pytest

IPHONE_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
)
DESKTOP_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
BOTH_UAS = [pytest.param(DESKTOP_UA, id="desktop"), pytest.param(IPHONE_UA, id="mobile")]


@pytest.fixture
def blackbird(make_aircraft, make_museum, make_link, db_session):
    """An SR-71 with a description, aliases and one visible museum link."""
    import models

    a = make_aircraft(
        manufacturer="Lockheed", model="SR-71", variant="A",
        tail_number="61-7976", model_name="Blackbird",
        role_type="recon", wing_type="monoplane", year_built=1967,
        description="Delivered to Beale in 1967; retired 1990.",
    )
    for alias in ("SR71", "Blackbird", "Habu", "A-12"):
        db_session.add(models.AircraftAlias(aircraft_id=a.id, alias=alias))
    db_session.commit()
    m = make_museum(name="Test Air Museum", city="Dayton", state_province="Ohio")
    make_link(a, m)
    return a, m


# ── the pages render at all ──────────────────────────────────────────

@pytest.mark.parametrize("ua", BOTH_UAS)
def test_aircraft_page_renders_200(client, blackbird, ua):
    a, _ = blackbird
    r = client.get(f"/aircraft/{a.id}", headers={"User-Agent": ua})
    assert r.status_code == 200


@pytest.mark.parametrize("ua", BOTH_UAS)
def test_museum_page_renders_200(client, blackbird, ua):
    _, m = blackbird
    r = client.get(f"/museums/{m.id}", headers={"User-Agent": ua})
    assert r.status_code == 200


def test_aircraft_page_no_longer_redirects_desktop(client, blackbird):
    """The old behaviour was a 302 to /aircraft?focus=<id>."""
    a, _ = blackbird
    r = client.get(f"/aircraft/{a.id}", headers={"User-Agent": DESKTOP_UA})
    assert r.status_code == 200, "desktop must render the page, not redirect to a modal"


def test_museum_page_no_longer_redirects_desktop(client, blackbird):
    _, m = blackbird
    r = client.get(f"/museums/{m.id}", headers={"User-Agent": DESKTOP_UA})
    assert r.status_code == 200


@pytest.mark.parametrize("path", ["/aircraft/999999", "/museums/999999"])
def test_missing_record_is_404(client, path):
    assert client.get(path).status_code == 404


# ── the content the pages exist for ──────────────────────────────────

@pytest.mark.parametrize("ua", BOTH_UAS)
def test_description_is_on_the_page(client, blackbird, ua):
    a, _ = blackbird
    body = client.get(f"/aircraft/{a.id}", headers={"User-Agent": ua}).get_data(as_text=True)
    assert "Delivered to Beale in 1967" in body


@pytest.mark.parametrize("ua", BOTH_UAS)
def test_every_alias_is_rendered(client, blackbird, ua):
    a, _ = blackbird
    body = client.get(f"/aircraft/{a.id}", headers={"User-Agent": ua}).get_data(as_text=True)
    for alias in ("SR71", "Blackbird", "Habu", "A-12"):
        assert alias in body, f"alias {alias!r} missing from the aircraft page"


def test_aliases_link_into_the_directory_search(client, blackbird):
    """An alias is a search term. Rendering it as inert text wastes it."""
    a, _ = blackbird
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert "/aircraft?q=SR71" in body
    assert "/aircraft?q=Habu" in body


@pytest.mark.parametrize("ua", BOTH_UAS)
def test_full_spec_is_rendered(client, blackbird, ua):
    a, _ = blackbird
    body = client.get(f"/aircraft/{a.id}", headers={"User-Agent": ua}).get_data(as_text=True)
    for expected in ("Lockheed", "61-7976", "Blackbird", "1967", "Recon", "Monoplane"):
        assert expected in body, f"{expected!r} missing from the airframe details"


def test_aircraft_page_links_to_its_museum(client, blackbird):
    a, m = blackbird
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert f"/museums/{m.id}" in body
    assert "Test Air Museum" in body


def test_museum_page_links_to_its_aircraft(client, blackbird):
    a, m = blackbird
    body = client.get(f"/museums/{m.id}").get_data(as_text=True)
    assert f"/aircraft/{a.id}" in body
    assert "SR-71-A" in body or "SR-71" in body


def test_history_container_is_present_for_the_timeline(client, blackbird):
    """airframe-history.js renders into #history-events; without the
    container the timeline silently never appears."""
    a, _ = blackbird
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert 'id="history-app"' in body
    assert 'id="history-events"' in body
    assert f'data-aircraft-id="{a.id}"' in body


def test_attached_facts_surface_on_the_page(client, blackbird, db_session):
    import models
    a, _ = blackbird
    db_session.add(models.AircraftFact(
        fact="It leaked fuel on the ground until friction heat sealed the tanks.",
        aircraft_id=a.id, is_active=True,
    ))
    db_session.commit()
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert "friction heat sealed the tanks" in body


def test_hidden_facts_do_not_surface(client, blackbird, db_session):
    import models
    a, _ = blackbird
    db_session.add(models.AircraftFact(
        fact="Disputed claim held back from publication.",
        aircraft_id=a.id, is_active=False,
    ))
    db_session.commit()
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert "Disputed claim" not in body


# ── what the pages must NOT advertise ────────────────────────────────

def test_non_viewable_museum_link_is_not_advertised(
    client, make_aircraft, make_museum, make_link
):
    a = make_aircraft(model="B-52", tail_number="55-0677")
    m = make_museum(name="Back Lot Storage")
    make_link(a, m, display_status="in_storage")
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert "Back Lot Storage" not in body
    assert "Not currently on display" in body


def test_museum_page_omits_non_viewable_aircraft(
    client, make_aircraft, make_museum, make_link
):
    m = make_museum(name="Half Open Museum")
    shown = make_aircraft(model="F-4", variant="C", tail_number="63-7407")
    hidden = make_aircraft(model="F-105", variant="G", tail_number="63-8320")
    make_link(shown, m)
    make_link(hidden, m, display_status="under_restoration")
    body = client.get(f"/museums/{m.id}").get_data(as_text=True)
    assert "63-7407" in body
    assert "63-8320" not in body


def test_aircraft_with_no_aliases_renders_cleanly(client, make_aircraft):
    a = make_aircraft(model="Piper", variant="J-3", tail_number="N12345")
    r = client.get(f"/aircraft/{a.id}")
    assert r.status_code == 200
    assert "Also known as" not in r.get_data(as_text=True)
