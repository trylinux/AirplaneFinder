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
]

# Descriptions with trailing whitespace or a stray CRLF. Trivial, but the
# hygiene test flags them on every run.
TRIM_DESCRIPTIONS = True

SUSPECT = """
Suspected wrong, NOT changed — needs a primary source first:

  * USS Midway Museum: "Douglas TBD-1 Devastator" (untailed). No Devastator is
    on display anywhere in the world; the only recovered airframes are wrecks.
    Midway has an SBD Dauntless. Likely a wrong designation, but which?
  * EAA Aviation Museum AND Smithsonian NASM (Mall) each hold an identical
    untailed "Curtiss JN-4D" + "Wright Flyer" pair. Two museums with the same
    two placeholder-looking rows is more likely a bad early import than a
    coincidence. The real 1903 Flyer is at NASM; EAA's is a replica.
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
        print(f"\n  {verb} /api/v1/aircraft/{aid}  {payload or ''}\n      {why}")
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
        path = f"/api/v1/aircraft/{aid}"
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
