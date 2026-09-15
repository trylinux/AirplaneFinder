"""Candidate-finding in the site merge planner.

The planner decides which museum records are the same place. Its original rule
was proximity alone, which has two blind spots this test file pins:

  - a museum with NO coordinates is invisible to a distance check, and 270 of
    6,222 records (4.3%) have none;
  - the distance loop buckets on round(lat, 2) — a ~1.1 km grid — and compares
    only within a bucket, so two records 60 m apart either side of a boundary
    never meet.

An identity pass (same designation, same tail or c/n) closes both. What it must
NOT do is turn a distant conflict into a merge: the same airframe recorded at
two places far apart means one record is wrong, and merging would invent a move
that never happened.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "plan_merge.py"


def _museum(mid, name, lat=None, lon=None, country="Testland"):
    return {"id": mid, "name": name, "city": "Town", "country": country,
            "latitude": lat, "longitude": lon, "address": "", "website": "",
            "postal_code": "", "access_type": "public"}


def _link(lid, museum, aircraft_id, designation, tail=None, cn=None):
    return {"id": lid, "aircraft_id": aircraft_id, "display_status": "on_display",
            "museum": museum,
            "aircraft": {"id": aircraft_id, "full_designation": designation,
                         "tail_number": tail, "construction_number": cn,
                         "manufacturer": "Acme", "variant": None}}


def _run(tmp_path, links):
    exhibits = tmp_path / "exhibits.json"
    exhibits.write_text(json.dumps({"results": links}), encoding="utf-8")
    out = tmp_path / "out"
    r = subprocess.run([sys.executable, str(_SCRIPT), "--exhibits", str(exhibits),
                        "--out-dir", str(out)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return (json.loads((out / "merge_plan.json").read_text()),
            json.loads((out / "distant_conflicts.json").read_text()))


def test_museum_without_coordinates_is_found_by_shared_airframe(tmp_path):
    """The Modlin shape: a coordinate-less stub duplicating a sited record.
    Proximity can never see it; the identity pass must."""
    sited = _museum(1, "Fortress Aircraft Monuments", 52.44176, 20.67954)
    stub = _museum(2, "Fortress Museum")           # no coordinates
    plan, distant = _run(tmp_path, [
        _link(10, sited, 100, "TS-11", tail="1227"),
        _link(11, stub, 200, "TS-11", tail="1227"),
    ])
    assert distant == []
    assert len(plan) == 1
    assert plan[0]["match_basis"] == "no_coordinates"
    assert plan[0]["proven"] is True
    assert plan[0]["distance_m"] is None


def test_bucket_edge_pair_is_recovered_and_called_proximity(tmp_path):
    """60 m apart but either side of a round(lat, 2) boundary. The identity
    pass finds it, and it is an ordinary site duplicate — not a distant one."""
    a = _museum(1, "Museum A", 10.004999, 20.0)
    b = _museum(2, "Museum B", 10.005001, 20.0)   # different 0.01 bucket
    plan, distant = _run(tmp_path, [
        _link(10, a, 100, "A-37B", tail="0475"),
        _link(11, b, 200, "A-37B", tail="0475"),
    ])
    assert distant == []
    assert plan[0]["match_basis"] == "proximity"
    assert plan[0]["distance_m"] < 300


def test_distant_pair_is_never_a_merge(tmp_path):
    """Dęblin vs Stalowa Wola, 150 km. One record is wrong; merging would
    fabricate a relocation."""
    a = _museum(1, "Museum A", 51.5, 21.9)
    b = _museum(2, "Monument B", 50.58, 22.05)
    plan, distant = _run(tmp_path, [
        _link(10, a, 100, "TS-11bis B", tail="721"),
        _link(11, b, 200, "TS-11bis B", tail="721"),
    ])
    assert plan == [], "a distant conflict must not reach the merge plan"
    assert len(distant) == 1
    assert distant[0]["match_basis"] == "distant"
    assert distant[0]["distance_m"] > 100_000


def test_same_tail_in_different_countries_is_not_paired(tmp_path):
    """Serial numbers are national — a Polish 1227 and a Czech 1227 are two
    aircraft. The country guard applies to the identity pass too."""
    a = _museum(1, "Museum A", 52.0, 20.0, country="Poland")
    b = _museum(2, "Museum B", 50.0, 14.0, country="Czechia")
    plan, distant = _run(tmp_path, [
        _link(10, a, 100, "TS-11", tail="1227"),
        _link(11, b, 200, "TS-11", tail="1227"),
    ])
    assert plan == [] and distant == []


def test_unidentified_airframes_do_not_pair_across_distance(tmp_path):
    """With no tail and no c/n there is no identity to match on, so two sited
    records far apart stay unrelated."""
    a = _museum(1, "Museum A", 52.0, 20.0)
    b = _museum(2, "Museum B", 40.0, 10.0)
    plan, distant = _run(tmp_path, [
        _link(10, a, 100, "MiG-21"),
        _link(11, b, 200, "MiG-21"),
    ])
    assert plan == [] and distant == []


def test_construction_number_alone_is_enough_to_pair(tmp_path):
    a = _museum(1, "Museum A", 52.0, 20.0)
    b = _museum(2, "Stub B")
    plan, _ = _run(tmp_path, [
        _link(10, a, 100, "C-47A", cn="19347"),
        _link(11, b, 200, "C-47A", cn="19347"),
    ])
    assert len(plan) == 1 and plan[0]["proven"] is True
