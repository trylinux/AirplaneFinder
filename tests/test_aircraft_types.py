"""Shared aircraft type information — the inherited "what IS this aeroplane" text.

The problem this feature exists to solve: 372 T-33As, 328 UH-1Hs and 199
F-104Gs in the collection each wanted the same paragraph, and the only place
to put it was Aircraft.description — one copy per airframe, none of them
editable in one place.

The contract these tests hold:
  - matching is normalization-insensitive: "MiG-21", "MIG 21" and "Mig21"
    are one type;
  - matching is NOT manufacturer-scoped, because a Fuji-built UH-1H and a
    Kawasaki-built T-33A are the same aircraft as the Bell and the Lockheed.
    791 of 4,877 designations in the real data carry more than one
    manufacturer spelling, so a manufacturer-scoped key would fragment
    exactly what this table exists to share;
  - a variant record beats a base record, and the base catches everything
    without one;
  - the type text never overwrites, hides or replaces the per-airframe
    description — both appear, and the airframe's own note wins the SEO slot;
  - a draft (unpublished) type reaches nobody anonymous;
  - writes are permission-gated the same way the rest of the admin API is.
"""

import pytest

from models import AircraftType, type_match_key


# ─────────────────────────────────────────────────────────────────────
# The join key
# ─────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("model,variant,expected", [
    ("T-33", "A", "T33A"),
    ("t-33", "a", "T33A"),
    ("MiG-21", None, "MIG21"),
    ("MIG 21", "", "MIG21"),
    ("Mig21", None, "MIG21"),
    ("F-4", "C", "F4C"),
    # The importer has recorded this designation both ways. They must land
    # on the same type, because they are the same aeroplane.
    ("F-4C", None, "F4C"),
    ("UH-1", "H", "UH1H"),
    ("Mi-8", "T", "MI8T"),
])
def test_match_key_normalizes(model, variant, expected):
    assert type_match_key(model, variant) == expected


def test_match_key_is_none_for_empty_model():
    """None means "no match possible" — callers must not build a key from
    punctuation alone and collide every such record together."""
    assert type_match_key("", None) is None
    assert type_match_key(None, None) is None
    assert type_match_key("-", " ") is None


# ─────────────────────────────────────────────────────────────────────
# Resolution
# ─────────────────────────────────────────────────────────────────────

@pytest.fixture
def make_type(db_session):
    import models

    def _factory(**kwargs):
        defaults = dict(
            model="T-33",
            variant=None,
            display_name="Lockheed T-33 Shooting Star",
            description="A two-seat jet trainer developed from the P-80.",
            manufacturer="Lockheed",
            aircraft_type="fixed_wing",
            military_civilian="military",
            is_published=True,
        )
        defaults.update(kwargs)
        slug_bits = [defaults["model"], defaults.get("variant") or ""]
        defaults.setdefault("slug", "-".join(b for b in slug_bits if b).lower().replace(" ", "-"))
        t = models.AircraftType(**defaults)
        t.sync_key()
        db_session.add(t)
        db_session.commit()
        return t
    return _factory


def test_base_type_serves_every_variant(make_type):
    base = make_type(model="T-33", variant=None)
    for variant in ("A", "B", "SF", None):
        assert AircraftType.resolve_for("T-33", variant) is base


def test_variant_type_beats_base_type(make_type):
    base = make_type(model="T-33", variant=None, slug="t-33")
    exact = make_type(model="T-33", variant="A", slug="t-33a",
                      display_name="Lockheed T-33A Shooting Star",
                      description="The USAF production trainer variant.")
    assert AircraftType.resolve_for("T-33", "A") is exact
    # Everything else still falls through to the base.
    assert AircraftType.resolve_for("T-33", "B") is base
    assert AircraftType.resolve_for("T-33", None) is base


def test_resolution_ignores_punctuation_and_case(make_type):
    t = make_type(model="MiG-21", variant=None, slug="mig-21",
                  display_name="Mikoyan-Gurevich MiG-21")
    for spelling in ("MiG-21", "MIG 21", "mig21", "Mig-21"):
        assert AircraftType.resolve_for(spelling, None) is t


def test_resolution_is_not_manufacturer_scoped(make_type, make_aircraft, client):
    """A licence-built airframe inherits the original designer's write-up.

    This is the single most consequential design decision in the feature:
    Fuji built 89 of the UH-1s in the real collection, Kawasaki 36 of the
    T-33s, HAL 38 of the MiG-21s. Scoping the key by manufacturer would
    leave every one of those airframes with no type information at all.
    """
    make_type(model="UH-1", variant=None, slug="uh-1",
              manufacturer="Bell", display_name="Bell UH-1 Iroquois",
              also_built_by="Fuji, Dornier",
              description="The Huey. The first turbine-powered helicopter in US service.")

    fuji = make_aircraft(manufacturer="Fuji", model="UH-1", variant="H",
                         aircraft_type="rotary_wing")
    r = client.get(f"/aircraft/{fuji.id}")
    body = r.get_data(as_text=True)
    assert r.status_code == 200
    assert "The first turbine-powered helicopter in US service." in body
    # ...while the airframe still shows its actual builder.
    assert "Fuji" in body


def test_unrelated_designation_resolves_to_nothing(make_type):
    make_type(model="T-33", variant=None)
    assert AircraftType.resolve_for("F-104", "G") is None


def test_unpublished_type_does_not_resolve(make_type):
    make_type(model="T-33", variant=None, is_published=False)
    assert AircraftType.resolve_for("T-33", "A") is None
    # ...but admin-side lookups can still find it.
    assert AircraftType.resolve_for("T-33", "A", published_only=False) is not None


def test_draft_variant_does_not_mask_published_base(make_type):
    """A half-written variant record must not blank out the page. If the
    exact match is a draft, the airframe falls back to the live base type
    rather than showing nothing."""
    base = make_type(model="T-33", variant=None, slug="t-33")
    make_type(model="T-33", variant="A", slug="t-33a", is_published=False,
              description="draft, not ready")
    assert AircraftType.resolve_for("T-33", "A") is base


# ─────────────────────────────────────────────────────────────────────
# Rendering
# ─────────────────────────────────────────────────────────────────────

def test_type_card_and_airframe_description_both_render(make_type, make_aircraft, client):
    """Type info is additive. The per-airframe research prose is a different
    thing and keeps its own card."""
    make_type(model="T-33", variant=None, slug="t-33",
              description="A two-seat jet trainer developed from the P-80 Shooting Star.")
    a = make_aircraft(manufacturer="Lockheed", model="T-33", variant="A",
                      description="Delivered to the ANG in 1957; wears 58th FIS markings.")
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert "A two-seat jet trainer developed from the P-80 Shooting Star." in body
    assert "Delivered to the ANG in 1957" in body
    # The heading names the TYPE, not the airframe: a base record is titled
    # "About the T-33" even on a T-33A page, because that is the scope of
    # the text underneath it.
    assert "About the T-33" in body


def test_variant_type_titles_itself_with_the_variant(make_type, make_aircraft, client):
    make_type(model="T-33", variant="A", slug="t-33a",
              description="The USAF production trainer variant.")
    a = make_aircraft(model="T-33", variant="A")
    assert "About the T-33A" in client.get(f"/aircraft/{a.id}").get_data(as_text=True)


def test_page_renders_without_a_type(make_aircraft, client):
    """The common case until the library fills out: no type, no card, no error."""
    a = make_aircraft(model="Bede", variant="BD-5")
    r = client.get(f"/aircraft/{a.id}")
    assert r.status_code == 200
    assert "About the" not in r.get_data(as_text=True)


def test_airframe_description_wins_the_meta_slot(make_type, make_aircraft, client):
    """Search engines should see what makes THIS airframe distinct, not the
    same type paragraph repeated across hundreds of pages."""
    make_type(model="T-33", variant=None, slug="t-33",
              description="Generic type text about the T-33.")
    a = make_aircraft(model="T-33", variant="A",
                      description="Flown by the Thunderbirds in 1956.")
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert 'name="description" content="Flown by the Thunderbirds in 1956.' in body


def test_type_text_fills_the_meta_slot_when_airframe_has_none(make_type, make_aircraft, client):
    make_type(model="T-33", variant=None, slug="t-33",
              description="Generic type text about the T-33.")
    a = make_aircraft(model="T-33", variant="A", description=None)
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert 'name="description" content="Generic type text about the T-33.' in body


def test_specs_render_only_when_present(make_type, make_aircraft, client):
    make_type(model="T-33", variant=None, slug="t-33",
              first_flight_year=1948, number_built=6557, crew="2")
    a = make_aircraft(model="T-33", variant="A")
    body = client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    assert "First flight" in body and "1948" in body
    assert "6,557" in body                 # thousands separator
    assert "Wingspan" not in body          # not set, so not shown


# ─────────────────────────────────────────────────────────────────────
# API
# ─────────────────────────────────────────────────────────────────────

def test_detail_api_exposes_type_as_a_sibling_key(make_type, make_aircraft, client):
    """Not merged into `aircraft` — a client must be able to tell which
    fields describe the airframe and which describe the type."""
    make_type(model="T-33", variant=None, slug="t-33")
    a = make_aircraft(model="T-33", variant="A")
    data = client.get(f"/api/v1/aircraft/{a.id}").get_json()
    assert data["type"]["model"] == "T-33"
    assert data["type"]["designation"] == "T-33"
    assert "description" in data["aircraft"]


def test_detail_api_type_is_null_when_unmatched(make_aircraft, client):
    a = make_aircraft(model="Nothing-Like-This")
    assert client.get(f"/api/v1/aircraft/{a.id}").get_json()["type"] is None


def test_resolve_endpoint_reports_what_matched(make_type, client):
    make_type(model="T-33", variant=None, slug="t-33")
    make_type(model="T-33", variant="A", slug="t-33a")
    assert client.get("/api/v1/aircraft-types/resolve?model=T-33&variant=A").get_json()["matched_on"] == "variant"
    assert client.get("/api/v1/aircraft-types/resolve?model=T-33&variant=B").get_json()["matched_on"] == "base"
    assert client.get("/api/v1/aircraft-types/resolve?model=F-104").get_json()["resolved"] is None
    assert client.get("/api/v1/aircraft-types/resolve").status_code == 400


def test_anonymous_list_hides_drafts(make_type, client):
    make_type(model="T-33", variant=None, slug="t-33", is_published=True)
    make_type(model="F-104", variant=None, slug="f-104", is_published=False)
    models_seen = {t["model"] for t in client.get("/api/v1/aircraft-types").get_json()}
    assert models_seen == {"T-33"}


def test_authenticated_list_shows_drafts(make_type, manager_client):
    make_type(model="F-104", variant=None, slug="f-104", is_published=False)
    models_seen = {t["model"] for t in manager_client.get("/api/v1/aircraft-types").get_json()}
    assert "F-104" in models_seen


def test_anonymous_cannot_create(client):
    r = client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "x"})
    assert r.status_code in (401, 403)


def test_manager_can_create_and_key_is_derived(manager_client):
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "MiG-21", "variant": "bis",
        "display_name": "Mikoyan-Gurevich MiG-21bis",
        "description": "The final major Soviet production variant.",
    })
    assert r.status_code == 201, r.get_data(as_text=True)
    body = r.get_json()
    assert body["match_key"] == "MIG21BIS"
    assert body["slug"] == "mig-21bis"
    assert body["designation"] == "MiG-21bis"


def test_duplicate_designation_is_refused_with_the_existing_id(manager_client):
    """The unique key is what stops two half-finished F-104 write-ups from
    both existing and the page picking arbitrarily. The 409 has to say which
    record already holds it, or the editor cannot act on the refusal."""
    first = manager_client.post("/api/v1/aircraft-types", json={
        "model": "F-104", "display_name": "Lockheed F-104 Starfighter",
        "description": "Interceptor.",
    }).get_json()
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "f 104", "display_name": "duplicate by another spelling",
        "description": "Interceptor, again.",
    })
    assert r.status_code == 409
    assert r.get_json()["existing_id"] == first["id"]


def test_create_requires_model_display_name_and_description(manager_client):
    r = manager_client.post("/api/v1/aircraft-types", json={"model": "T-33"})
    assert r.status_code == 400
    assert "display_name" in r.get_json()["error"]


def test_numeric_fields_are_validated(manager_client):
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "x",
        "first_flight_year": "not-a-year",
    })
    assert r.status_code == 400


def test_redesignating_moves_the_inheriting_airframes(manager_client, make_aircraft, client):
    """Fixing a typo in the designation has to move the write-up with it —
    otherwise the type silently applies to nothing."""
    t = manager_client.post("/api/v1/aircraft-types", json={
        "model": "F-140", "display_name": "typo", "description": "Interceptor.",
    }).get_json()
    starfighter = make_aircraft(model="F-104", variant="G")
    assert client.get(f"/api/v1/aircraft/{starfighter.id}").get_json()["type"] is None

    manager_client.put(f"/api/v1/aircraft-types/{t['id']}", json={"model": "F-104"})
    resolved = client.get(f"/api/v1/aircraft/{starfighter.id}").get_json()["type"]
    assert resolved["id"] == t["id"]
    assert resolved["match_key"] == "F104"
    assert resolved["slug"] == "f-104"


def test_redesignating_onto_an_existing_key_is_refused(manager_client):
    manager_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "x"})
    other = manager_client.post("/api/v1/aircraft-types", json={
        "model": "F-104", "display_name": "F-104", "description": "y"}).get_json()
    r = manager_client.put(f"/api/v1/aircraft-types/{other['id']}", json={"model": "T 33"})
    assert r.status_code == 409


def test_unpublishing_hides_the_card_without_deleting_anything(manager_client, make_aircraft, client):
    t = manager_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "Trainer prose."}).get_json()
    a = make_aircraft(model="T-33", variant="A")
    assert "Trainer prose." in client.get(f"/aircraft/{a.id}").get_data(as_text=True)

    manager_client.put(f"/api/v1/aircraft-types/{t['id']}", json={"is_published": False})
    assert "Trainer prose." not in client.get(f"/aircraft/{a.id}").get_data(as_text=True)
    # The record is still there, which is the point of a draft state.
    assert AircraftType.query.get(t["id"]) is not None


def test_manager_cannot_delete(manager_client):
    t = manager_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "x"}).get_json()
    assert manager_client.delete(f"/api/v1/aircraft-types/{t['id']}").status_code in (401, 403)
    assert AircraftType.query.get(t["id"]) is not None


def test_admin_can_delete(admin_client):
    t = admin_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "x"}).get_json()
    assert admin_client.delete(f"/api/v1/aircraft-types/{t['id']}").status_code == 200
    assert AircraftType.query.get(t["id"]) is None


def test_deleting_a_type_leaves_the_aircraft_row_intact(admin_client, make_aircraft, client):
    """Airframes inherit by lookup, not by foreign key. Deleting the type
    must not touch a single aircraft record."""
    t = admin_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "x"}).get_json()
    a = make_aircraft(model="T-33", variant="A", description="This airframe has its own story.")
    admin_client.delete(f"/api/v1/aircraft-types/{t['id']}")

    r = client.get(f"/aircraft/{a.id}")
    assert r.status_code == 200
    assert "This airframe has its own story." in r.get_data(as_text=True)


def test_inherits_count_credits_the_winning_type(manager_client, make_aircraft):
    """A base type must not claim airframes that a variant type has taken —
    otherwise the "shown on N pages" warning in admin is a lie."""
    base = manager_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "display_name": "T-33", "description": "base"}).get_json()
    exact = manager_client.post("/api/v1/aircraft-types", json={
        "model": "T-33", "variant": "A", "display_name": "T-33A", "description": "variant"}).get_json()
    for _ in range(3):
        make_aircraft(model="T-33", variant="A")
    make_aircraft(model="T-33", variant="B")
    make_aircraft(model="T-33", variant=None)

    assert manager_client.get(f"/api/v1/aircraft-types/{exact['id']}").get_json()["inherits_count"] == 3
    assert manager_client.get(f"/api/v1/aircraft-types/{base['id']}").get_json()["inherits_count"] == 2


def test_admin_page_renders(manager_client):
    r = manager_client.get("/admin/aircraft-types")
    assert r.status_code == 200
    assert "Aircraft Types" in r.get_data(as_text=True)


# ─────────────────────────────────────────────────────────────────────
# The seeded library
# ─────────────────────────────────────────────────────────────────────

def test_seed_file_imports_cleanly_and_covers_its_designations(admin_client, make_aircraft):
    """The shipped seed file must survive the real API's validation, and each
    record must actually attach to airframes spelled the way the importer
    writes them — including licence builders, which is the whole point."""
    import json
    from pathlib import Path

    seed_path = Path(__file__).resolve().parent.parent / "data" / "aircraft_types" / "seed_top25.json"
    records = json.loads(seed_path.read_text(encoding="utf-8"))
    assert len(records) >= 25

    keys = [type_match_key(r["model"], r.get("variant")) for r in records]
    assert len(set(keys)) == len(keys), "seed file has two records for one designation"

    for rec in records:
        r = admin_client.post("/api/v1/aircraft-types", json=rec)
        assert r.status_code == 201, f"{rec['model']}: {r.get_data(as_text=True)}"

    # Spot-check the licence-built cases against the manufacturer spellings
    # that actually occur in the collection.
    for manufacturer, model, variant in [
        ("Fuji", "UH-1", "H"),
        ("Kawasaki", "T-33", "A"),
        ("HAL", "MiG-21", "FL"),
        ("Aeritalia", "F-104", "S"),
        ("Mikojan-Guriewicz", "MiG-17", None),
        ("WSK PZL-Mielec", "An-2", None),
    ]:
        a = make_aircraft(manufacturer=manufacturer, model=model, variant=variant)
        assert AircraftType.resolve_for(a.model, a.variant) is not None, \
            f"{manufacturer} {model} {variant or ''} inherited nothing"


def test_seed_records_declare_which_variant_their_figures_describe(admin_client):
    """A base type covers every variant; its numbers cannot. Any seeded
    record carrying performance figures has to name the variant they are
    for, or the spec block is quietly wrong on most of the pages showing it."""
    import json
    from pathlib import Path

    seed_path = Path(__file__).resolve().parent.parent / "data" / "aircraft_types" / "seed_top25.json"
    for rec in json.loads(seed_path.read_text(encoding="utf-8")):
        has_figures = any(rec.get(f) for f in
                          ("max_speed_kmh", "range_km", "ceiling_m", "length_m", "engines"))
        if has_figures:
            assert (rec.get("spec_basis") or "").strip(), \
                f"{rec['model']} publishes figures with no spec_basis"
            assert len(rec["spec_basis"]) <= 100, f"{rec['model']} spec_basis too long for the column"
