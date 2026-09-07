#!/usr/bin/env python3
"""Apply verified corrections to live records that no import file can fix.

Each entry is a record that was checked against a primary source and found
wrong. This is NOT a place for guesses: anything only *suspected* wrong is
listed in the SUSPECT block at the bottom and printed, never changed.

Dry run by default. Records are matched by content at run time — never by a
hard-coded id — so a record that has already been fixed, or that differs
from what this script expects, is reported and skipped rather than clobbered.

    export AIRPLANE_BASE_URL=https://airplane.museum
    export AIRPLANE_API_KEY=amt_admin_key
    python3 scripts/apply_live_corrections.py            # dry run
    python3 scripts/apply_live_corrections.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient  # noqa: E402


def n(s):
    return (s or "").strip().lower()


# (description, matcher over an exhibit row, action, payload)
#   action "patch_aircraft" -> PATCH /api/v1/aircraft/<id>
#   action "delete_aircraft" -> DELETE /api/v1/aircraft/<id>  (admin; cascades the link)
CORRECTIONS = [
    ("Udvar-Hazy does not hold a B-2. The Smithsonian has only archival B-2 "
     "material; the sole B-2 on public display is the structural-test airframe "
     "at NMUSAF. Record 82-1066 is wrong outright.",
     lambda e: n(e["museum"]["name"]) == "steven f. udvar-hazy center"
               and n(e["aircraft"]["model"]) == "b-2",
     "delete_aircraft", None),

    ("Pima's Hawker Hurricane is a replica; the museum writes its serial in "
     "quotation marks to mark it as painted-on. BG974 must not be its tail.",
     lambda e: n(e["museum"]["name"]).startswith("pima")
               and n(e["aircraft"].get("tail_number")) == "bg974",
     "patch_aircraft", {"tail_number": None, "aliases": ["marked BG974", "replica"]}),

    ("Pensacola's Beechcraft GB-2 has its tail stored with the prefix: "
     "'USN BuNo 23688'. The BuNo is 23688.",
     lambda e: n(e["aircraft"].get("tail_number")) == "usn buno 23688",
     "patch_aircraft", {"tail_number": "23688"}),

    # The three rows first flagged as suspect, now resolved against the
    # museums' own pages. Each turned out to be a different failure mode than
    # assumed, and only one is a deletion.
    ("USS Midway's TBD Devastator is real, but it is a full-scale film-prop "
     "replica built by Lionsgate for the 2019 film Midway (steel tube and "
     "foam), assembled by museum volunteers and displayed since October "
     "2019. No BuNo exists. Correct, don't delete. "
     "midway.org/visit/aircraft-gallery/tbd-devastator",
     lambda e: n(e["museum"]["name"]) == "uss midway museum"
               and n(e["aircraft"]["model"]) == "tbd",
     "patch_aircraft",
     {"description": "Full-scale replica built as a prop for the 2019 film "
                     "Midway; not an original airframe. Assembled by museum "
                     "volunteers, on display since October 2019.",
      "aliases": ["Devastator", "replica", "film prop"]}),

    ("EAA's Wright Flyer is a replica built jointly by EAA and Blackhawk "
     "Technical Institute, completed 1978 for the 75th anniversary, from "
     "plans taken off the Smithsonian's original. "
     "eaa.org/.../1903-wright-flyer-replica",
     lambda e: n(e["museum"]["name"]) == "eaa aviation museum"
               and "wright flyer" in n(e["aircraft"]["model"]),
     "patch_aircraft",
     {"description": "Replica of the 1903 Flyer, built by EAA and Blackhawk "
                     "Technical Institute, completed 1978.",
      "year_built": 1978, "aliases": ["replica"]}),

    ("NASM holds exactly one JN-4D — Air Service serial 4983, inventory "
     "A19190006000 — and its own object page places it at the Udvar-Hazy "
     "Center's Business Aviation gallery. The untailed Mall row is the stale "
     "location from before the Mall renovation. Udvar-Hazy's row (4983) is "
     "the real one. airandspace.si.edu/collection-objects/curtiss-jn-4d-jenny",
     lambda e: n(e["museum"]["name"]).startswith("smithsonian national air")
               and n(e["aircraft"]["model"]) == "jn-4"
               and not e["aircraft"].get("tail_number"),
     "delete_aircraft", None),
]

# Museums with no coordinates are invisible to the globe and to nearest-
# museum search. Every pin below is a mapped building or the museum's own
# place record — never a city or ZIP centroid, which would silently put the
# museum in the wrong place. Matched by name at run time.
MUSEUM_FIXES = {
    "Air Force Armament Museum -- Eglin Air Force Base": dict(
        address="100 Museum Drive", postal_code="32542",
        website="https://afarmamentmuseum.com/", latitude=30.4666, longitude=-86.5612),
    "Air Zoo": dict(
        address="6151 Portage Road", city="Portage", postal_code="49002",
        website="https://www.airzoo.org/", latitude=42.2275, longitude=-85.5572),
    "Barksdale Air Force Base": dict(
        name="Barksdale Global Power Museum", address="88 Shreveport Road",
        postal_code="71110", website="https://www.barksdaleglobalpowermuseum.com/",
        latitude=32.5134, longitude=-93.6832),
    "Cosmosphere": dict(
        address="1100 N Plum Street", postal_code="67501",
        website="https://cosmo.org/", latitude=38.0656, longitude=-97.9214),
    "Evergreen Aviation Museum": dict(
        address="500 NE Captain Michael King Smith Way", postal_code="97128",
        website="https://noramaerospace.org/", latitude=45.2043, longitude=-123.1454),
    "Lackland Air Force Base": dict(
        name="USAF Airman Heritage Museum", address="2051 George Ave, Building 5206",
        postal_code="78236", website="https://www.airmenheritage.com/enlisted-museum",
        latitude=29.3841, longitude=-98.6216),
    "Museum of Aviation -- Robins Air Force Base": dict(
        address="1942 Heritage Blvd", postal_code="31098",
        website="https://museumofaviation.org/", latitude=32.5919, longitude=-83.5869),
    "Science Museum of Virginia": dict(
        address="2500 W Broad Street", postal_code="23220",
        website="https://smv.org/", latitude=37.5611, longitude=-77.4658),
    "Strategic Air Command & Aerospace Museum": dict(
        address="28210 W Park Highway", postal_code="68003",
        website="https://www.sacmuseum.org/", latitude=41.0169, longitude=-96.3198),
}

# Descriptions with trailing whitespace or a stray CRLF. Trivial, but the
# hygiene test flags them on every run.
TRIM_DESCRIPTIONS = True

SUSPECT = """
Not changed, for a decision:

  * Evergreen Aviation & Space Museum has rebranded as the North American
    Aerospace Museum (NORAM); evergreenmuseum.org now redirects to
    noramaerospace.org. The record keeps the old name for now because the
    pending data/oregon/evergreen_aircraft.csv resolves its museum by that
    name. Rename after that file has imported, and update the CSV to match.
"""

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    client = AirplaneClient()
    try:
        exhibits = client.get("/api/v1/exhibits")["results"]
    except Exception as e:
        print(f"error: could not read {client.base_url}: {e}", file=sys.stderr)
        return 2

    planned = []
    for why, match, action, payload in CORRECTIONS:
        hits = [e for e in exhibits if match(e)]
        if len(hits) == 0:
            print(f"  already fixed / not present: {why[:70]}...")
            continue
        if len(hits) > 1:
            print(f"  AMBIGUOUS ({len(hits)} matches), skipped: {why[:70]}...")
            continue
        e = hits[0]
        planned.append((action, e["aircraft_id"], payload, why))

    try:
        museums = client.get("/api/v1/museums/search", q="", per_page=500)["results"]
    except Exception as e:
        print(f"error: could not list museums: {e}", file=sys.stderr)
        return 2
    for name, patch in MUSEUM_FIXES.items():
        hits = [m for m in museums if n(m["name"]) == n(name)]
        if len(hits) != 1:
            print(f"  museum not matched exactly once, skipped: {name}")
            continue
        m = hits[0]
        if m.get("latitude") is not None and "name" not in patch:
            print(f"  already has coordinates: {name}")
            continue
        planned.append(("patch_museum", m["id"], patch, f"geocode {name}"))

    if TRIM_DESCRIPTIONS:
        for e in exhibits:
            d = e["aircraft"].get("description")
            if isinstance(d, str) and d != d.strip():
                planned.append(("patch_aircraft", e["aircraft_id"],
                                {"description": d.strip()},
                                f"trim description on {e['aircraft']['manufacturer']} "
                                f"{e['aircraft']['model']}"))

    for action, aid, payload, why in planned:
        verb = "DELETE" if action == "delete_aircraft" else "PATCH "
        res = "museums" if action == "patch_museum" else "aircraft"
        print(f"\n  {verb} /api/v1/{res}/{aid}  {payload or ''}\n      {why[:110]}")
    print(f"\n{len(planned)} change(s) planned.")
    print(SUSPECT)

    if not args.apply:
        print("Dry run — nothing written. Re-run with --apply.")
        return 0
    if not client.api_key:
        print("error: --apply needs AIRPLANE_API_KEY (admin)", file=sys.stderr)
        return 2

    failed = 0
    for action, aid, payload, _ in planned:
        path = f"/api/v1/{'museums' if action == 'patch_museum' else 'aircraft'}/{aid}"
        try:
            if action == "delete_aircraft":
                client.delete(path)
            else:
                client.patch(path, payload)
            print(f"  ok   {action} {path}")
        except Exception as e:
            failed += 1
            print(f"  FAIL {path}: {e}", file=sys.stderr)
    print(f"\napplied {len(planned) - failed}/{len(planned)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
