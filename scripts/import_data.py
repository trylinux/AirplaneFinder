#!/usr/bin/env python3
"""POST a CSV/JSON file to the bulk_import endpoint and print the report.

Format is auto-detected from the file extension. Use --dry-run first to
validate without writing — the server will return per-row errors so you
can fix them before committing.

Usage
-----
    # validate first
    python3 scripts/import_data.py --entity aircraft --file my.csv --dry-run

    # actually import (needs an admin or aircraft_admin API key)
    AIRPLANE_API_KEY=amt_... \
        python3 scripts/import_data.py --entity aircraft --file my.csv

    # against a remote deployment
    AIRPLANE_BASE_URL=https://airplane.museum AIRPLANE_API_KEY=amt_... \
        python3 scripts/import_data.py --entity museums --file world.json

Exit codes
    0  — clean import (or dry-run with no errors)
    1  — validation failed; some rows had errors
    2  — request failed (network, auth, etc.)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402


def _detect_format(path: Path, override: str = "auto") -> str:
    if override and override != "auto":
        return override
    return "json" if path.suffix.lower() == ".json" else "csv"


def _print_report(report: dict, dry_run: bool) -> int:
    """Pretty-print the per-row report. Returns the intended exit code."""
    errors = report.get("errors") or []
    created = report.get("created", 0)
    skipped = report.get("skipped", 0)

    if dry_run:
        if errors:
            print(f"DRY RUN: {len(errors)} error(s); nothing would be inserted.",
                  file=sys.stderr)
        else:
            print(f"DRY RUN: would create {created} row(s).", file=sys.stderr)
    else:
        if errors:
            print(f"FAILED: {len(errors)} error(s); rolled back. "
                  f"created={created} skipped={skipped}", file=sys.stderr)
        else:
            print(f"OK: created {created}, skipped {skipped}.", file=sys.stderr)

    if errors:
        # Per-row table — row index in the report is 0-based; +1 to match
        # CSV / spreadsheet conventions.
        print("", file=sys.stderr)
        print(f"  {'row':>5}  {'field':<30}  message", file=sys.stderr)
        print(f"  {'-'*5}  {'-'*30}  {'-'*40}", file=sys.stderr)
        for e in errors:
            row = (e.get("row", -1) + 1) if e.get("row", -1) >= 0 else "—"
            print(f"  {row:>5}  {str(e.get('field') or ''):<30}  "
                  f"{e.get('message') or ''}", file=sys.stderr)

    return 1 if errors else 0


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--entity", required=True, choices=("aircraft", "museums"),
                   help="Which collection to import into")
    p.add_argument("--file", "-f", required=True,
                   help="Path to CSV or JSON file to upload")
    p.add_argument("--format", choices=("auto", "csv", "json"), default="auto",
                   help="Force a format (default: detect from extension)")
    p.add_argument("--dry-run", action="store_true",
                   help="Validate without inserting")
    p.add_argument("--base-url")
    p.add_argument("--api-key",
                   help="Bearer API key (or set AIRPLANE_API_KEY). "
                        "Real imports require admin / aircraft_admin level.")
    args = p.parse_args()

    path = Path(args.file)
    if not path.is_file():
        print(f"file not found: {path}", file=sys.stderr)
        sys.exit(2)

    fmt = _detect_format(path, args.format)
    text = path.read_text(encoding="utf-8")

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)
    if not args.dry_run and not client.api_key:
        print("Refusing to import without an API key. Pass --api-key or set "
              "AIRPLANE_API_KEY (admin / aircraft_admin level required).",
              file=sys.stderr)
        sys.exit(2)

    method = (client.bulk_import_aircraft if args.entity == "aircraft"
              else client.bulk_import_museums)

    try:
        report = method(data=text, fmt=fmt, dry_run=args.dry_run)
    except ApiError as e:
        print(f"request failed: {e}", file=sys.stderr)
        sys.exit(2)

    sys.exit(_print_report(report, args.dry_run))


if __name__ == "__main__":
    main()
