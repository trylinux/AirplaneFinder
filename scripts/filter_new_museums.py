#!/usr/bin/env python3
"""Filter a museums CSV down to the rows not already in the database.

Why this exists
---------------
The bulk importer is atomic: if any row is an existing duplicate, the whole
batch is reported as errors and rolled back. That's the right behaviour for
a first import — it stops a half-applied mess — but it makes re-running a
museums file impossible once even one of its museums exists, which is
exactly what happens when you add a few museums and re-run.

Rather than making the importer non-atomic (that trade is deliberate), this
subtracts what's already there and hands back only the genuinely new rows.

Matching mirrors the importer's own duplicate rule: case-insensitive
(name, city, country).

Usage
-----
    python3 scripts/filter_new_museums.py data/california/ca_museums.csv
    python3 scripts/filter_new_museums.py IN.csv --out /tmp/new.csv

Prints a summary to stderr; writes the filtered CSV to --out (default:
alongside the input as <name>.new.csv). Exit codes:
    0  wrote a file with at least one new museum
    3  nothing new — every museum in the file already exists
    2  error
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from airplane_api import AirplaneClient, ApiError  # noqa: E402


def key(name, city, country):
    return (name.strip().lower(), city.strip().lower(),
            (country or "United States").strip().lower())


def main():
    p = argparse.ArgumentParser(description="Drop museums that already exist.")
    p.add_argument("csv_path")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    src = Path(args.csv_path)
    if not src.is_file():
        print(f"error: {src} not found", file=sys.stderr)
        return 2
    out = Path(args.out) if args.out else src.with_suffix(".new.csv")

    client = AirplaneClient()
    try:
        existing = {key(m["name"], m["city"], m.get("country"))
                    for m in client.iter_museums()}
    except Exception as e:
        # Any transport failure (TLS, DNS, refused, timeout) lands here.
        # The caller falls back to the unfiltered file, so report the cause
        # in one line rather than dumping a traceback the shell can't use.
        print(f"error: could not read museums from {client.base_url}: "
              f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2

    rows = list(csv.DictReader(src.open(encoding="utf-8")))
    new = [r for r in rows
           if key(r["name"], r["city"], r.get("country")) not in existing]
    dupes = len(rows) - len(new)

    print(f"  {src.name}: {len(rows)} rows, {dupes} already present, "
          f"{len(new)} new", file=sys.stderr)

    if not new:
        print("  nothing to import", file=sys.stderr)
        return 3

    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(new)
    print(f"  wrote {out}", file=sys.stderr)
    for r in new[:10]:
        print(f"     + {r['name']} ({r['city']})", file=sys.stderr)
    if len(new) > 10:
        print(f"     … and {len(new) - 10} more", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
