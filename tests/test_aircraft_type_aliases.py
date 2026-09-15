"""Alternate designations that reach one type write-up.

The problem. Type resolution joins on a normalized designation string,
which sees through punctuation and case but not through the fact that
aviation gives one aeroplane several names. The catalogue records whichever
one is painted on the airframe, so a T-6 write-up misses every AT-6 and
SNJ, an F-104 write-up misses every CF-104, and a MiG-15 write-up misses
every Lim-2 — about 850 airframes in the real collection, none of which are
different aircraft, all of which would otherwise need their own duplicate
paragraph.

The contract these tests hold:
  - an alias is a second match key into an existing type: no aircraft row
    changes, no text is duplicated, and deleting the type takes its aliases
    with it;
  - a real record always beats an alias of the same specificity, so writing
    an actual type for an aliased designation quietly supersedes the alias
    rather than colliding with it;
  - a more specific designation still wins: an exact variant record beats
    an alias, and an alias beats a less specific base record;
  - an alias carries its own manufacturer scope, and must ALSO satisfy the
    scope of the type it points at — it is a second door into a type, never
    a way around its scope;
  - a bare-number alias without a scope is refused, because unscoped "204"
    would attach the UH-1 write-up to anything spelled 204 and the failure
    would be invisible on every page that suffered it;
  - an alias may not shadow a real type or another type's alias.
"""

import pytest

from models import AircraftType, AircraftTypeAlias, type_match_key


@pytest.fixture
def make_type(db_session):
    import models

    def _factory(**kwargs):
        defaults = dict(
            model="T-6",
            variant=None,
            display_name="North American T-6 Texan",
            description="The advanced trainer that taught most of the Allied air forces to fly.",
            manufacturer="North American",
            aircraft_type="fixed_wing",
            military_civilian="military",
            manufacturer_scope="",
            is_published=True,
        )
        defaults.update(kwargs)
        slug_bits = [defaults["model"], defaults.get("variant") or "",
                     defaults.get("manufacturer_scope") or ""]
        defaults.setdefault("slug", "-".join(b for b in slug_bits if b).lower().replace(" ", "-"))
        t = models.AircraftType(**defaults)
        t.sync_key()
        db_session.add(t)
        db_session.commit()
        return t
    return _factory


@pytest.fixture
def add_alias(db_session):
    def _factory(t, designation, scope=""):
        a = AircraftTypeAlias(type_id=t.id, designation=designation,
                              manufacturer_scope=scope)
        a.sync_key()
        db_session.add(a)
        db_session.commit()
        return a
    return _factory


# ─────────────────────────────────────────────────────────────────────
# The join
# ─────────────────────────────────────────────────────────────────────

def test_alias_reaches_the_type(make_type, add_alias):
    t = make_type(model="T-6")
    add_alias(t, "AT-6")
    assert AircraftType.resolve_for("AT-6", "D") is t
    assert AircraftType.resolve_for("AT-6") is t


def test_alias_matching_ignores_punctuation_like_the_real_key(make_type, add_alias):
    """"SNJ-5" in the catalogue and "SNJ 5" in a source are one aeroplane.
    The alias produces a match_key by the same rule an aircraft row does, so
    it cannot drift from it."""
    t = make_type(model="T-6")
    add_alias(t, "SNJ")
    assert AircraftType.resolve_for("SNJ", "5") is t
    assert AircraftType.resolve_for("snj", "5") is t
    assert AircraftType.resolve_for("S.N.J.", "5") is t
    # The limitation aliases inherit rather than fix: a model recorded whole
    # as "SNJ5" has no base key to fall back to, exactly as a real T-6 type
    # would not catch a model recorded as "T6G". That is the variant column's
    # job, and the variant cleanup pass is what keeps it done.
    assert AircraftType.resolve_for("SNJ5") is None


def test_alias_changes_no_aircraft_row(make_type, add_alias, make_aircraft, client):
    """The whole point: the airframe keeps saying AT-6 and still inherits."""
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "AT-6")
    a = make_aircraft(manufacturer="North American", model="AT-6", variant="D")
    r = client.get(f"/aircraft/{a.id}")
    body = r.get_data(as_text=True)
    assert r.status_code == 200
    assert "taught most of the Allied air forces to fly" in body
    assert a.model == "AT-6"


def test_unaliased_designation_still_resolves_to_nothing(make_type, add_alias):
    t = make_type(model="T-6")
    add_alias(t, "AT-6")
    assert AircraftType.resolve_for("BT-13") is None


def test_unpublished_type_does_not_resolve_through_its_alias(make_type, add_alias):
    """A draft is a draft by whichever door you knock on."""
    t = make_type(model="T-6", is_published=False)
    add_alias(t, "AT-6")
    assert AircraftType.resolve_for("AT-6", "D") is None
    assert AircraftType.resolve_for("AT-6", "D", published_only=False) is t


def test_deleting_the_type_takes_its_aliases(make_type, add_alias, db_session):
    t = make_type(model="T-6")
    add_alias(t, "AT-6")
    db_session.delete(t)
    db_session.commit()
    assert AircraftTypeAlias.query.filter_by(match_key="AT6").first() is None


# ─────────────────────────────────────────────────────────────────────
# Precedence
# ─────────────────────────────────────────────────────────────────────

def test_a_real_type_beats_an_alias_for_the_same_designation(make_type, add_alias):
    """This is what makes aliases safe to add in bulk. Pointing Su-17 at the
    Su-22 write-up today does not block writing a real Su-17 record later:
    the moment one exists it wins, and nobody has to remember to go and
    delete the alias first."""
    su22 = make_type(model="Su-22", display_name="Sukhoi Su-22 Fitter",
                     description="The export swing-wing Fitter.")
    add_alias(su22, "Su-17")
    assert AircraftType.resolve_for("Su-17", "M4") is su22

    su17 = make_type(model="Su-17", display_name="Sukhoi Su-17 Fitter",
                     description="The Soviet-service swing-wing Fitter.")
    assert AircraftType.resolve_for("Su-17", "M4") is su17
    # ...and the alias is untouched, still there if the real record is dropped.
    assert AircraftTypeAlias.query.filter_by(match_key="SU17").count() == 1


def test_an_exact_variant_record_beats_an_alias(make_type, add_alias):
    """More specific still wins. A CF-104D write-up is a better answer for a
    CF-104D than the F-104 one it would otherwise reach by alias."""
    f104 = make_type(model="F-104", display_name="Lockheed F-104 Starfighter",
                     description="The missile with a man in it.")
    add_alias(f104, "CF-104")
    exact = make_type(model="CF-104", variant="D",
                      display_name="Canadair CF-104D",
                      description="The two-seat Canadian trainer Starfighter.")
    assert AircraftType.resolve_for("CF-104", "D") is exact
    # The single-seaters still reach the F-104 write-up through the alias.
    assert AircraftType.resolve_for("CF-104", "A") is f104


def test_an_alias_beats_a_less_specific_base_record(make_type, add_alias):
    """Rank is (specificity, then real-before-alias). An exact-key alias
    outranks a base-key record, because matching the whole designation is
    the stronger signal."""
    generic = make_type(model="F", display_name="F", description="Nothing useful.")
    f104 = make_type(model="F-104", display_name="Lockheed F-104 Starfighter",
                     description="The missile with a man in it.")
    add_alias(f104, "F-104G")
    assert AircraftType.resolve_for("F-104G") is f104
    assert generic is not None  # present, and correctly not the answer


# ─────────────────────────────────────────────────────────────────────
# Scope
# ─────────────────────────────────────────────────────────────────────

def test_a_scoped_alias_only_answers_for_its_manufacturer(make_type, add_alias):
    """"204" is Bell's commercial number for the UH-1, and also a string that
    hundreds of unrelated aircraft could be spelled with."""
    uh1 = make_type(model="UH-1", display_name="Bell UH-1 Iroquois",
                    manufacturer="Bell", description="The Huey.",
                    aircraft_type="rotary_wing")
    add_alias(uh1, "204", scope="Bell")
    assert AircraftType.resolve_for("204", None, "Bell") is uh1
    assert AircraftType.resolve_for("204", None, "Bell Helicopter") is uh1
    assert AircraftType.resolve_for("204", None, "Nord") is None
    # No manufacturer given at all is not a match either: a scoped record
    # that cannot verify its scope must not fire.
    assert AircraftType.resolve_for("204", None, None) is None


def test_an_alias_cannot_escape_the_scope_of_the_type_it_points_at(make_type, add_alias):
    """An alias is a second door into a type, not a way around its scope.
    Without this the Pitts exclusion could be defeated by aliasing."""
    grumman = make_type(model="S-2", manufacturer_scope="Grumman",
                        manufacturer="Grumman", display_name="Grumman S-2 Tracker",
                        description="Carrier-based anti-submarine aircraft.")
    add_alias(grumman, "S2F")
    assert AircraftType.resolve_for("S2F", "1", "Grumman") is grumman
    assert AircraftType.resolve_for("S2F", "1", "Pitts") is None


def test_an_unscoped_alias_serves_licence_builders(make_type, add_alias):
    """The default stays permissive, for the same reason the type key is:
    a Polish-built MiG-15 is still a MiG-15."""
    mig15 = make_type(model="MiG-15", manufacturer="Mikoyan-Gurevich",
                      display_name="Mikoyan-Gurevich MiG-15",
                      description="The swept-wing fighter that shocked the West over Korea.")
    add_alias(mig15, "Lim-2")
    assert AircraftType.resolve_for("Lim-2", None, "PZL Mielec") is mig15
    assert AircraftType.resolve_for("Lim-2", None, None) is mig15


# ─────────────────────────────────────────────────────────────────────
# resolve_detail_for / the API
# ─────────────────────────────────────────────────────────────────────

def test_resolve_detail_names_the_alias_it_came_in_by(make_type, add_alias):
    t = make_type(model="T-6")
    add_alias(t, "AT-6")
    found, alias = AircraftType.resolve_detail_for("AT-6", "D")
    assert found is t
    assert alias is not None and alias.designation == "AT-6"
    # A direct hit reports no alias.
    found, alias = AircraftType.resolve_detail_for("T-6", "G")
    assert found is t and alias is None


def test_resolve_endpoint_reports_the_alias(make_type, add_alias, client):
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "AT-6")
    r = client.get("/api/v1/aircraft-types/resolve?model=AT-6&variant=D")
    data = r.get_json()
    assert data["resolved"]["id"] == t.id
    assert data["matched_via_alias"]["designation"] == "AT-6"

    r = client.get("/api/v1/aircraft-types/resolve?model=T-6&variant=G")
    assert r.get_json()["matched_via_alias"] is None


def test_type_payload_lists_its_aliases(make_type, add_alias, client):
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "SNJ")
    add_alias(t, "AT-6")
    r = client.get(f"/api/v1/aircraft-types/{t.id}")
    aliases = r.get_json()["aliases"]
    # Sorted, so the admin list and the API agree on an order.
    assert [a["designation"] for a in aliases] == ["AT-6", "SNJ"]
    assert aliases[0]["match_key"] == "AT6"


def test_create_accepts_aliases_as_strings_or_objects(manager_client):
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "UH-1", "display_name": "Bell UH-1 Iroquois",
        "description": "The Huey.", "manufacturer": "Bell",
        "aliases": ["HU-1", {"designation": "204", "manufacturer_scope": "Bell"}],
    })
    assert r.status_code == 201, r.get_json()
    aliases = {a["designation"]: a["manufacturer_scope"] for a in r.get_json()["aliases"]}
    assert aliases == {"204": "Bell", "HU-1": None}
    assert AircraftType.resolve_for("HU-1", "A") is not None
    assert AircraftType.resolve_for("204", None, "Bell") is not None


def test_a_bare_number_alias_needs_a_scope(manager_client):
    """The failure this refusal prevents is silent: an unscoped "204" would
    attach the UH-1 write-up to every airframe spelled 204, and nothing on
    those pages would say anything was wrong."""
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "UH-1", "display_name": "Bell UH-1 Iroquois",
        "description": "The Huey.", "aliases": ["204"],
    })
    assert r.status_code == 400
    assert "manufacturer_scope" in r.get_json()["error"]
    # ...and nothing was created by the attempt.
    assert AircraftType.query.filter_by(match_key="UH1").first() is None


def test_an_alias_may_not_shadow_a_real_type(make_type, manager_client):
    make_type(model="Su-17", display_name="Sukhoi Su-17 Fitter",
              description="The Soviet-service Fitter.")
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "Su-22", "display_name": "Sukhoi Su-22 Fitter",
        "description": "The export Fitter.", "aliases": ["Su-17"],
    })
    assert r.status_code == 400
    assert "already a type of its own" in r.get_json()["error"]


def test_an_alias_may_not_be_stolen_from_another_type(make_type, add_alias, manager_client):
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "SNJ")
    r = manager_client.post("/api/v1/aircraft-types", json={
        "model": "BT-13", "display_name": "Vultee BT-13 Valiant",
        "description": "The basic trainer between primary and the T-6.",
        "aliases": ["SNJ"],
    })
    assert r.status_code == 400
    assert "already points at type" in r.get_json()["error"]


def test_patching_aliases_replaces_the_list(make_type, add_alias, manager_client):
    """Replace, not merge — the same contract aircraft aliases already have,
    so removing one is a PATCH without it rather than a second endpoint."""
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "SNJ")
    add_alias(t, "AT-6")
    r = manager_client.patch(f"/api/v1/aircraft-types/{t.id}", json={"aliases": ["AT-6"]})
    assert r.status_code == 200
    assert [a["designation"] for a in r.get_json()["aliases"]] == ["AT-6"]
    assert AircraftType.resolve_for("SNJ", "5") is None
    assert AircraftType.resolve_for("AT-6", "D") is t


def test_patching_without_aliases_leaves_them_alone(make_type, add_alias, manager_client):
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "AT-6")
    r = manager_client.patch(f"/api/v1/aircraft-types/{t.id}",
                             json={"description": "Revised."})
    assert r.status_code == 200
    assert [a["designation"] for a in r.get_json()["aliases"]] == ["AT-6"]


def test_clearing_aliases_with_an_empty_list(make_type, add_alias, manager_client):
    t = make_type(model="T-6", slug="t-6")
    add_alias(t, "AT-6")
    r = manager_client.patch(f"/api/v1/aircraft-types/{t.id}", json={"aliases": []})
    assert r.status_code == 200
    assert r.get_json()["aliases"] == []
    assert AircraftType.resolve_for("AT-6", "D") is None


def test_anonymous_cannot_add_an_alias(make_type, client):
    t = make_type(model="T-6", slug="t-6")
    r = client.patch(f"/api/v1/aircraft-types/{t.id}", json={"aliases": ["AT-6"]})
    assert r.status_code in (401, 403)


def test_alias_key_matches_the_aircraft_key_rule(make_type, add_alias):
    """One rule, one implementation. If these ever diverge the join silently
    stops finding airframes, so pin them together."""
    t = make_type(model="T-6")
    a = add_alias(t, "AT-6")
    assert a.match_key == type_match_key("AT-6")
    assert a.match_key == type_match_key("AT", "6")
