#!/usr/bin/env python3
"""Apply the Pima A–M corrections found by re-parsing the museum's feed.

WHY THESE EXIST
---------------
The A–F and G–M slices were imported before the feed parser learned two things
the museum states plainly on its own pages:

1. A sentence under the title — "This aircraft is not currently on public
   display" / "currently undergoing restoration" — which is exactly our
   visitor-perspective display_status. Those rows went in as `on_display`.
2. A serial written in quotation marks, which is how Pima marks a serial as
   painted-on rather than the airframe's identity. All three site-wide are
   replicas. One of them, the Hawker Hurricane "BG974", is already live with
   BG974 as its tail number.

These are edits to existing records, not an import, so they cannot ride along
with a CSV. This script resolves ids at run time from /api/v1/exhibits rather
than hard-coding them, because ids differ between environments.

SAFETY
------
Dry run by default: it prints what it would change and touches nothing.
Pass --apply to write. Every change is matched on (model, tail_number) at
Pima specifically, and anything that doesn't match exactly one live record is
reported and skipped rather than guessed at.

Usage:
    export AIRPLANE_BASE_URL=https://airplane.museum
    export AIRPLANE_API_KEY=amt_your_admin_key
    python3 scripts/apply_pima_corrections.py            # dry run
    python3 scripts/apply_pima_corrections.py --apply
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from airplane_api import AirplaneClient  # noqa: E402

MUSEUM = "Pima Air & Space Museum"
CORRECTIONS = (Path(__file__).resolve().parent.parent
               / "data" / "arizona" / "pima_a_to_m_corrections.csv")


def norm(s):
    return (s or "").strip().lower()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true",
                   help="actually write; omit for a dry run")
    p.add_argument("--csv", default=str(CORRECTIONS))
    args = p.parse_args()

    src = Path(args.csv)
    if not src.is_file():
        print(f"error: {src} not found", file=sys.stderr)
        return 2

    client = AirplaneClient()
    try:
        exhibits = client.get("/api/v1/exhibits")["results"]
    except Exception as e:
        print(f"error: could not read {client.base_url}: "
              f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2

    at_pima = [e for e in exhibits if norm(e["museum"]["name"]) == norm(MUSEUM)]
    print(f"{len(at_pima)} aircraft recorded at {MUSEUM}\n")

    planned, unmatched, already = [], [], 0
    for row in csv.DictReader(src.open(encoding="utf-8")):
        # Match on whichever identifier we actually stored. The builder picks
        # the military serial for a military airframe and the registration for
        # a civil one, so a civil aircraft is live under N7004U while the feed
        # calls its "Serial Number" 18296 (a construction number). Matching on
        # the serial alone reported three already-correct records as missing.
        candidates = {norm(row.get("serial")), norm(row.get("registration"))}
        candidates.discard("")
        hits = [e for e in at_pima
                if norm(e["aircraft"].get("tail_number")) in candidates]
        if len(hits) != 1:
            unmatched.append((row, len(hits)))
            continue
        e = hits[0]
        want_status = row["display_status"]
        is_marking = row["serial_is_marking"].strip().lower() == "true"

        if want_status == e["display_status"] and not is_marking:
            already += 1
        if want_status != e["display_status"]:
            planned.append(("exhibit", e["id"], {"display_status": want_status},
                            f"{row['manufacturer']} {row['designation']} "
                            f"{e['display_status']} -> {want_status}"))
        if is_marking:
            planned.append(
                ("aircraft", e["aircraft_id"], {"tail_number": None},
                 f"{row['manufacturer']} {row['designation']} clear painted "
                 f"serial {row['serial']} (replica)"))

    for kind, oid, payload, why in planned:
        print(f"  PATCH /api/v1/{'exhibits' if kind == 'exhibit' else 'aircraft'}"
              f"/{oid}  {payload}\n        {why}")
    print(f"\n{len(planned)} change(s) planned "
          f"({already} record(s) already correct).")

    if unmatched:
        print(f"\n{len(unmatched)} correction(s) could not be matched to "
              f"exactly one live record — skipped, resolve by hand:")
        for row, n in unmatched:
            print(f"   {row['manufacturer']} {row['designation']} "
                  f"serial={row['serial']!r} reg={row.get('registration')!r}: "
                  f"{n} matches")

    if not args.apply:
        print("\nDry run — nothing written. Re-run with --apply to make these "
              "changes.")
        return 0

    if not client.api_key:
        print("error: --apply needs AIRPLANE_API_KEY (admin)", file=sys.stderr)
        return 2

    failed = 0
    for kind, oid, payload, why in planned:
        path = f"/api/v1/{'exhibits' if kind == 'exhibit' else 'aircraft'}/{oid}"
        try:
            client.patch(path, payload)
            print(f"  ok   {path}")
        except Exception as e:
            failed += 1
            print(f"  FAIL {path}: {type(e).__name__}: {e}", file=sys.stderr)
    print(f"\napplied {len(planned) - failed}/{len(planned)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
