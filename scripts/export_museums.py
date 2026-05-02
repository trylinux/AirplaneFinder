#!/usr/bin/env python3
"""Export every museum to CSV or JSON in the bulk_import-accepted shape.

Usage
-----
    python3 scripts/export_museums.py
    python3 scripts/export_museums.py --format json --out museums_backup.json
    python3 scripts/export_museums.py --region "Europe"
    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/export_museums.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402


MUSEUM_COLUMNS = [
    "name", "city", "state_province", "country", "postal_code", "region",
    "address", "website", "latitude", "longitude",
]


def _row(museum: dict) -> dict:
    """Flat dict suitable for csv.DictWriter or JSON serialization. Empty
    string for missing fields in CSV; preserved as None in JSON."""
    return {col: (museum.get(col) if museum.get(col) is not None else "")
            for col in MUSEUM_COLUMNS}


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--format", choices=("csv", "json"), default="csv")
    p.add_argument("--out", "-o", default="-")
    p.add_argument("--query", "-q", default="",
                   help="Filter by free-text search")
    p.add_argument("--region", default="",
                   help="Restrict to a specific region (e.g. 'Europe')")
    p.add_argument("--base-url")
    p.add_argument("--api-key")
    args = p.parse_args()

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)

    try:
        rows = list(client.iter_museums(q=args.query, region=args.region))
    except ApiError as e:
        print(f"export failed: {e}", file=sys.stderr)
        sys.exit(2)

    out_stream = sys.stdout if args.out == "-" else open(args.out, "w", newline="")
    try:
        if args.format == "json":
            # JSON keeps None instead of "" for null fields — round-trip
            # cleaner.
            payload = [{c: m.get(c) for c in MUSEUM_COLUMNS} for m in rows]
            json.dump(payload, out_stream, indent=2)
            out_stream.write("\n")
        else:
            writer = csv.DictWriter(out_stream, fieldnames=MUSEUM_COLUMNS,
                                    extrasaction="ignore")
            writer.writeheader()
            for m in rows:
                writer.writerow(_row(m))
    finally:
        if args.out != "-":
            out_stream.close()

    if args.out != "-":
        print(f"wrote {len(rows)} museums to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
