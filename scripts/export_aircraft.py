#!/usr/bin/env python3
"""Export every aircraft to CSV or JSON.

The output is in the same shape ``/api/v1/aircraft/bulk_import`` accepts,
so you can export → edit in a spreadsheet → re-import without touching
the format. (Aliases get joined into ``Herc;Hercules`` for CSV; JSON keeps
them as a list.)

Usage
-----
    # CSV to stdout
    python3 scripts/export_aircraft.py

    # JSON to a file
    python3 scripts/export_aircraft.py --format json --out backup.json

    # Filter while exporting
    python3 scripts/export_aircraft.py --query "C-130"

    # Against a remote deployment (env var or --base-url)
    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/export_aircraft.py
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

# Allow running the script directly without installing the package: add
# this script's directory to sys.path so ``import airplane_api`` works.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402


# Column order that round-trips through bulk_import. Must match what the
# server's _validate_aircraft_row accepts.
AIRCRAFT_COLUMNS = [
    "manufacturer", "model", "variant", "tail_number",
    "model_name", "aircraft_name",
    "aircraft_type", "wing_type", "military_civilian", "role_type",
    "year_built", "description", "aliases",
]


def _row_for_csv(aircraft: dict) -> dict:
    """Project an API aircraft dict into a flat CSV row."""
    return {
        col: ";".join(aircraft.get("aliases") or [])
        if col == "aliases"
        else (aircraft.get(col) if aircraft.get(col) is not None else "")
        for col in AIRCRAFT_COLUMNS
    }


def _row_for_json(aircraft: dict) -> dict:
    """Project for JSON. Same fields as CSV, but aliases stays a list."""
    out = {col: aircraft.get(col) for col in AIRCRAFT_COLUMNS}
    out["aliases"] = list(aircraft.get("aliases") or [])
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--format", choices=("csv", "json"), default="csv",
                   help="Output format (default: csv)")
    p.add_argument("--out", "-o", default="-",
                   help="Output file path (default: stdout)")
    p.add_argument("--query", "-q", default="",
                   help="Filter by free-text search across aircraft fields")
    p.add_argument("--base-url",
                   help="API base URL (overrides $AIRPLANE_BASE_URL)")
    p.add_argument("--api-key",
                   help="Bearer API key (overrides $AIRPLANE_API_KEY). "
                        "Not required for export — search endpoints are public.")
    args = p.parse_args()

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)

    try:
        rows = list(client.iter_aircraft(q=args.query))
    except ApiError as e:
        print(f"export failed: {e}", file=sys.stderr)
        sys.exit(2)

    out_stream = sys.stdout if args.out == "-" else open(args.out, "w", newline="")
    try:
        if args.format == "json":
            json.dump([_row_for_json(a) for a in rows], out_stream, indent=2)
            out_stream.write("\n")
        else:
            writer = csv.DictWriter(out_stream, fieldnames=AIRCRAFT_COLUMNS,
                                    extrasaction="ignore")
            writer.writeheader()
            for a in rows:
                writer.writerow(_row_for_csv(a))
    finally:
        if args.out != "-":
            out_stream.close()

    if args.out != "-":
        print(f"wrote {len(rows)} aircraft to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
