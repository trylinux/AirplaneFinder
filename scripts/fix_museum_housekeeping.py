#!/usr/bin/env python3
"""Three data-integrity fixes that need judgment, not bulk import.

1. MERGE THE DUPLICATE UDVAR-HAZY RECORDS
   The database holds the same museum twice:
     id 22  "Steven F. Udvar-Hazy Center"                    3 aircraft, has coords + website
     id 50  "Smithsonian Institution Steven F. Udvar-Hazy Center"  1 aircraft, no coords
   Keeps 22 (it is complete and on the map), moves 50's aircraft across,
   then deletes 50. Doing this BEFORE building Udvar-Hazy's ~170 aircraft
   avoids splitting the collection over two records.

2. SPLIT SHARED TYPE RECORDS
   Five aircraft records are each linked to 2-3 museums — one airframe in
   several places at once, which is impossible. They are type-level records
   from the seed (a "Wright Flyer", a "Zero") rather than specific
   airframes, and each museum involved genuinely does hold an example.

   So the fix is to SPLIT, not to unlink: the first museum keeps the
   original record, and every other museum gets its own copy. Deleting the
   extra links instead would wrongly say those museums hold nothing.

3. DELETE THE HILLIER AIR MUSEUM RECORD
   Permanently closed, zero aircraft, collection whereabouts unknown.

Usage:
    export AIRPLANE_BASE_URL=http://127.0.0.1:5000
    export AIRPLANE_API_KEY=amt_your_admin_key
    python3 scripts/fix_museum_housekeeping.py            # dry run
    python3 scripts/fix_museum_housekeeping.py --apply

Exit codes: 0 ok, 1 changes pending (dry run), 2 error.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from airplane_api import AirplaneClient, ApiError  # noqa: E402

KEEP_MUSEUM = 22          # Steven F. Udvar-Hazy Center
DROP_MUSEUM = 50          # Smithsonian Institution Steven F. Udvar-Hazy Center
HILLIER = 80              # Hillier Air Museum, Modesto — permanently closed

# Fields copied when cloning a shared type record. Deliberately excludes
# tail_number: these records have none, and inventing one would be worse
# than leaving it blank.
CLONE_FIELDS = ("manufacturer", "model", "variant", "model_name", "aircraft_name",
                "aircraft_type", "wing_type", "military_civilian", "role_type",
                "year_built", "description")


def log(dry, msg):
    print(("  [dry] " if dry else "  ") + msg)


def merge_udvar_hazy(c, dry):
    """Move DROP_MUSEUM's aircraft onto KEEP_MUSEUM, then delete the record."""
    print("\n── 1. Merge the duplicate Udvar-Hazy records ──")
    try:
        drop = c.get_museum(DROP_MUSEUM)
    except ApiError as e:
        if e.status == 404:
            print("  museum 50 already gone — nothing to merge"); return 0
        raise
    keep = c.get_museum(KEEP_MUSEUM)
    print(f"  keep: [{KEEP_MUSEUM}] {keep['museum']['name']} "
          f"({len(keep.get('aircraft', []))} aircraft)")
    print(f"  drop: [{DROP_MUSEUM}] {drop['museum']['name']} "
          f"({len(drop.get('aircraft', []))} aircraft)")

    moved = 0
    for ac in drop.get("aircraft", []):
        label = f"{ac.get('full_designation')} {ac.get('tail_number') or ''}".strip()
        log(dry, f"move {label} -> museum {KEEP_MUSEUM}")
        if not dry:
            # Create the new link first; only then drop the old one, so a
            # failure halfway leaves the aircraft attached somewhere rather
            # than orphaned.
            c.post("/api/v1/exhibits", json={
                "aircraft_id": ac["id"], "museum_id": KEEP_MUSEUM,
                "display_status": ac.get("display_status", "on_display"),
            })
            c.delete(f"/api/v1/exhibits/{ac['link_id']}")
        moved += 1

    log(dry, f"delete museum {DROP_MUSEUM}")
    if not dry:
        c.delete(f"/api/v1/museums/{DROP_MUSEUM}")
    return moved + 1


def split_shared_records(c, dry):
    """One record linked to N museums becomes N records, one per museum."""
    print("\n── 2. Split aircraft records shared across museums ──")
    exhibits = c.get("/api/v1/exhibits")["results"]
    by_aircraft = {}
    for row in exhibits:
        by_aircraft.setdefault(row["aircraft"]["id"], []).append(row)
    shared = {k: v for k, v in by_aircraft.items() if len(v) > 1}
    if not shared:
        print("  none found"); return 0

    changes = 0
    for ac_id, rows in sorted(shared.items()):
        ac = rows[0]["aircraft"]
        label = ac.get("full_designation") or ac.get("model")
        museums = ", ".join(r["museum"]["name"] for r in rows)
        print(f"  {label} (id {ac_id}) is at {len(rows)} museums: {museums}")
        # First row keeps the original record; the rest get their own copy.
        for row in rows[1:]:
            log(dry, f"    clone for {row['museum']['name']}")
            if not dry:
                payload = {f: ac.get(f) for f in CLONE_FIELDS if ac.get(f) is not None}
                payload["aliases"] = ac.get("aliases", [])
                payload["museum_id"] = row["museum"]["id"]
                payload["display_status"] = row.get("display_status", "on_display")
                c.post("/api/v1/aircraft", json=payload)
                c.delete(f"/api/v1/exhibits/{row['id']}")
            changes += 1
    return changes


def delete_hillier(c, dry):
    print("\n── 3. Delete the closed Hillier Air Museum record ──")
    try:
        m = c.get_museum(HILLIER)
    except ApiError as e:
        if e.status == 404:
            print("  already gone"); return 0
        raise
    n = len(m.get("aircraft", []))
    if n:
        print(f"  REFUSING: museum {HILLIER} now has {n} aircraft — "
              f"someone added data. Review by hand.")
        return 0
    log(dry, f"delete museum {HILLIER} ({m['museum']['name']}, {m['museum']['city']})")
    if not dry:
        c.delete(f"/api/v1/museums/{HILLIER}")
    return 1


def main():
    p = argparse.ArgumentParser(description="Museum data housekeeping.")
    p.add_argument("--apply", action="store_true", help="actually make the changes")
    args = p.parse_args()
    dry = not args.apply

    c = AirplaneClient()
    if args.apply and not c.api_key:
        print("error: --apply needs an admin API key. Set AIRPLANE_API_KEY "
              "(or AIRPLANE_KEY).", file=sys.stderr)
        return 2

    print("=" * 66)
    print(f"  Museum housekeeping{'  (DRY RUN)' if dry else ''}")
    print(f"  {c.base_url}")
    print("=" * 66)

    total = 0
    try:
        total += merge_udvar_hazy(c, dry)
        total += split_shared_records(c, dry)
        total += delete_hillier(c, dry)
    except ApiError as e:
        print(f"\nerror: {e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"\nerror: {type(e).__name__}: {e}", file=sys.stderr)
        return 2

    print("\n" + "=" * 66)
    if dry:
        print(f"  Dry run — {total} change(s) pending. Re-run with --apply.")
        return 1
    print(f"  Done — {total} change(s) applied.")
    print("  Verify:  python3 scripts/dedupe_aircraft.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
