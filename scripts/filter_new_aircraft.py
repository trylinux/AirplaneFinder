#!/usr/bin/env python3
"""Filter an aircraft CSV down to rows not already in the database.

WHY THIS EXISTS
---------------
The importer is atomic: one row that already exists makes it reject the
whole file. That's right for a first import, but it makes top-up files
un-rerunnable — and top-ups are exactly the files you want to re-run as a
museum's collection grows.

The museum-level guard in import_data_dir.sh can't help here. It asks
"does this museum already have aircraft?", which is true for every top-up
by definition. So top-ups bypass it, and then collide instead.

This filters at the row level: drop rows whose (model, tail_number) is
already present, keep everything else. That makes any aircraft file safely
idempotent.

ROWS WITHOUT A TAIL NUMBER
--------------------------
A blank tail is NULL, and NULL never collides — so these rows can't be
matched against the database and would duplicate silently on a re-run.
They are dropped only when the museum already holds a record with the same
(manufacturer, model, variant), which is the best available signal. Use
--keep-untailed to override, but understand you may create duplicates.

Usage
-----
    python3 scripts/filter_new_aircraft.py data/arizona/pima_topup_g_to_m_aircraft.csv
    python3 scripts/filter_new_aircraft.py IN.csv --out /tmp/new.csv

Exit codes:
    0  wrote a file containing at least one new row
    3  nothing new — every row is already in the database
    2  error
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from airplane_api import AirplaneClient  # noqa: E402


def norm(s):
    return (s or "").strip().lower()


def build_indexes(client):
    """(model, tail) pairs, and (museum, manufacturer, model, variant) keys."""
    by_tail, by_type_at_museum = set(), set()
    for row in client.get("/api/v1/exhibits")["results"]:
        ac, mus = row["aircraft"], row["museum"]
        if ac.get("tail_number"):
            by_tail.add((norm(ac["model"]), norm(ac["tail_number"])))
        by_type_at_museum.add((norm(mus["name"]), norm(ac.get("manufacturer")),
                               norm(ac["model"]), norm(ac.get("variant"))))
    # aircraft with no museum link at all still occupy a (model, tail)
    for ac in client.iter_aircraft():
        if ac.get("tail_number"):
            by_tail.add((norm(ac["model"]), norm(ac["tail_number"])))
    return by_tail, by_type_at_museum


def main():
    p = argparse.ArgumentParser(description="Drop aircraft rows already in the DB.")
    p.add_argument("csv_path")
    p.add_argument("--out", default=None)
    p.add_argument("--keep-untailed", action="store_true",
                   help="keep rows without a tail number even if the museum "
                        "already holds that type (risks duplicates)")
    args = p.parse_args()

    src = Path(args.csv_path)
    if not src.is_file():
        print(f"error: {src} not found", file=sys.stderr)
        return 2
    out = Path(args.out) if args.out else src.with_suffix(".new.csv")

    client = AirplaneClient()
    try:
        by_tail, by_type = build_indexes(client)
    except Exception as e:
        print(f"error: could not read the database from {client.base_url}: "
              f"{type(e).__name__}: {e}", file=sys.stderr)
        return 2

    rows = list(csv.DictReader(src.open(encoding="utf-8")))
    if not rows:
        print(f"error: {src} has no rows", file=sys.stderr)
        return 2

    new, dropped_tail, dropped_type = [], 0, 0
    for r in rows:
        tail = (r.get("tail_number") or "").strip()
        if tail:
            if (norm(r["model"]), norm(tail)) in by_tail:
                dropped_tail += 1
                continue
        elif not args.keep_untailed:
            key = (norm(r.get("museum_name")), norm(r.get("manufacturer")),
                   norm(r["model"]), norm(r.get("variant")))
            if key in by_type:
                dropped_type += 1
                continue
        new.append(r)

    print(f"  {src.name}: {len(rows)} rows, {dropped_tail} already present "
          f"by tail, {dropped_type} untailed duplicates, {len(new)} new",
          file=sys.stderr)

    if not new:
        print("  nothing to import", file=sys.stderr)
        return 3

    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(new)
    print(f"  wrote {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
