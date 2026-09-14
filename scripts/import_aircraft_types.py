#!/usr/bin/env python3
"""Load or refresh the shared aircraft-type library from a JSON file.

A type is one write-up per designation, inherited at render time by every
airframe whose normalized model+variant matches. Editing one record here
changes hundreds of aircraft pages at once, so this script is deliberately
idempotent and dry-run-first: it matches existing records by designation
and reports exactly what it would change before anything is written.

Usage
-----
    # see what would happen (no writes, no auth needed for the read)
    python3 scripts/import_aircraft_types.py --file data/aircraft_types/seed_top25.json --dry-run

    # write, against a local server
    AIRPLANE_API_KEY=amt_... \
        python3 scripts/import_aircraft_types.py --file data/aircraft_types/seed_top25.json

    # write, against production
    AIRPLANE_BASE_URL=https://airplane.museum AIRPLANE_API_KEY=amt_... \
        python3 scripts/import_aircraft_types.py --file data/aircraft_types/seed_top25.json

    # publish drafts as they are written
    ... --publish

Input format
------------
A JSON array of objects. `model` is required; `variant` is optional and
omitting it makes a BASE type that serves every variant of that
designation. `display_name` and `description` are required. Every other
field in _FIELDS below is optional.

Exit codes
    0  — nothing to do, or all changes applied
    1  — one or more records failed
    2  — request failed (network, auth, bad file)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

# Mirrors _AIRCRAFT_TYPE_FIELDS in app.py plus model/variant. Kept explicit
# so a stray key in a hand-edited JSON file is reported rather than posted.
_FIELDS = {
    "model", "variant", "display_name", "manufacturer", "manufacturer_scope", "model_name",
    "also_built_by", "origin_country", "description", "aircraft_type",
    "role_type", "wing_type", "military_civilian", "first_flight_year",
    "introduced_year", "retired_year", "number_built", "spec_basis", "crew",
    "engines", "length_m", "wingspan_m", "height_m", "max_speed_kmh",
    "range_km", "ceiling_m", "source_name", "source_url", "wikipedia_url",
    "is_published",
}
_REQUIRED = ("model", "display_name", "description")

# Same rule as type_match_key() in models.py. Duplicated rather than
# imported because scripts/ talks to the API over HTTP and never imports
# the Flask app -- so this file must stay in agreement with that one.
_NOISE = re.compile(r"[^A-Z0-9]+")


def match_key(model, variant=None):
    joined = f"{(model or '').strip()}{(variant or '').strip()}".upper()
    return _NOISE.sub("", joined) or None


def _load(path: Path):
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)
    if not isinstance(records, list):
        print("error: top level must be a JSON array of type objects", file=sys.stderr)
        raise SystemExit(2)
    return records


def _validate(records):
    """Return a list of (index, message). Empty means the file is usable."""
    problems, seen = [], {}
    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            problems.append((i, "not a JSON object"))
            continue
        for field in _REQUIRED:
            if not str(rec.get(field) or "").strip():
                problems.append((i, f"missing required field '{field}'"))
        # Keys beginning with "_" are notes to a human editor -- TEMPLATE.json
        # ships with one -- and are dropped rather than posted.
        unknown = {k for k in rec if k not in _FIELDS and not k.startswith("_")}
        if unknown:
            problems.append((i, f"unknown field(s): {', '.join(sorted(unknown))}"))
        key = match_key(rec.get("model"), rec.get("variant"))
        if not key:
            problems.append((i, "model has no letters or digits"))
            continue
        # Uniqueness is (designation, manufacturer_scope): a Grumman S-2 and a
        # Pitts S-2 are two legitimate records, two unscoped S-2s are not.
        scoped_key = (key, (rec.get("manufacturer_scope") or "").strip())
        if scoped_key in seen:
            problems.append((i, f"duplicate designation and scope, already at index {seen[scoped_key]}"))
        else:
            seen[scoped_key] = i
    return problems


def _diff(existing: dict, incoming: dict):
    """Fields whose value would actually change. Skips keys not supplied."""
    changed = {}
    for field, new in incoming.items():
        if field in ("model", "variant"):
            continue                       # handled by the designation match
        old = existing.get(field)
        if isinstance(new, float) or isinstance(old, float):
            same = old is not None and new is not None and abs(float(old) - float(new)) < 1e-9
        else:
            same = (old or None) == (new or None)
        if not same:
            changed[field] = (old, new)
    return changed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", required=True, type=Path, help="JSON file of type records")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would change and write nothing")
    ap.add_argument("--publish", action="store_true",
                    help="force is_published=true on every record written")
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--api-key", default=None)
    args = ap.parse_args()

    records = _load(args.file)
    problems = _validate(records)
    if problems:
        for i, msg in problems:
            print(f"  record {i}: {msg}", file=sys.stderr)
        print(f"error: {len(problems)} problem(s) in {args.file}; nothing written",
              file=sys.stderr)
        raise SystemExit(1)

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)

    try:
        # One read of the whole library; it is a few hundred rows at most.
        existing = {(t["match_key"], t.get("manufacturer_scope") or ""): t
                    for t in client.get("/api/v1/aircraft-types")}
    except ApiError as exc:
        print(f"error: could not list existing types: {exc}", file=sys.stderr)
        raise SystemExit(2)

    created = updated = unchanged = failed = 0
    for rec in records:
        payload = {k: v for k, v in rec.items() if k in _FIELDS and not k.startswith("_")}
        if args.publish:
            payload["is_published"] = True
        scope = (rec.get("manufacturer_scope") or "").strip()
        key = (match_key(rec.get("model"), rec.get("variant")), scope)
        designation = rec.get("model") + (f" {rec['variant']}" if rec.get("variant") else "")
        if scope:
            designation += f" [{scope} only]"
        current = existing.get(key)

        try:
            if current is None:
                if args.dry_run:
                    print(f"  CREATE  {designation}")
                else:
                    client.post("/api/v1/aircraft-types", json=payload)
                    print(f"  created {designation}")
                created += 1
                continue

            changes = _diff(current, payload)
            if not changes:
                unchanged += 1
                continue
            if args.dry_run:
                print(f"  UPDATE  {designation} (id {current['id']}): "
                      f"{', '.join(sorted(changes))}")
            else:
                client.put(f"/api/v1/aircraft-types/{current['id']}", json=payload)
                print(f"  updated {designation} (id {current['id']}): "
                      f"{', '.join(sorted(changes))}")
            updated += 1
        except ApiError as exc:
            print(f"  FAILED  {designation}: {exc}", file=sys.stderr)
            failed += 1

    verb = "would be" if args.dry_run else ""
    print(f"\n{len(records)} record(s): {created} {verb} created, {updated} {verb} updated, "
          f"{unchanged} unchanged, {failed} failed")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
