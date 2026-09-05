#!/usr/bin/env python3
"""Strip stray leading/trailing whitespace from aircraft text fields.

Why this matters
----------------
A record stored as ``model=" C-7"`` or ``tail_number="55-3130 "`` looks
fine on screen — the browser collapses the space — but it breaks every
exact match the app relies on:

  - ``_find_aircraft_duplicate`` compares ``model`` and ``tail_number``
    exactly, so " C-7" never collides with "C-7". Duplicates get created
    silently and the bulk importer's "already exists" guard misses them.
  - ``scripts/dedupe_aircraft.py`` groups on (manufacturer, model,
    variant). A leading space puts an airframe in its own group of one,
    hiding it from the very tool meant to surface duplicates.
  - ``full_designation`` is a generated column, so " C-7" renders as
    " C-7 -A" in the UI and in every API response.

This script trims the affected fields via the public API (PUT
/api/v1/aircraft/<id>), so it works against a remote deployment without
database access.

Usage
-----
Dry run first — shows every change, writes nothing:

    export AIRPLANE_BASE_URL=https://airplane.museum
    export AIRPLANE_API_KEY=amt_...
    python3 scripts/trim_whitespace.py

Apply the changes:

    python3 scripts/trim_whitespace.py --apply

Options:
    --fields a,b,c   which fields to trim (default: the text fields below)
    --json           machine-readable output
    --limit N        stop after N records (useful for a cautious first pass)

Exit codes
    0  — nothing to fix, or --apply succeeded
    1  — changes are pending (dry-run found work to do)
    2  — one or more updates failed
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from airplane_api import AirplaneClient, ApiError  # noqa: E402


# Free-text fields where a stray space is always an error. Deliberately
# excludes `description`, where internal whitespace is legitimate — we
# only strip the ends there if it's explicitly requested via --fields.
DEFAULT_FIELDS = (
    "manufacturer", "model", "variant", "tail_number",
    "model_name", "aircraft_name", "role_type",
)


def find_dirty(client, fields, limit=None):
    """Return [(aircraft, {field: (old, new)})] for records needing a trim."""
    dirty = []
    for ac in client.iter_aircraft():
        changes = {}
        for f in fields:
            val = ac.get(f)
            if not isinstance(val, str):
                continue
            trimmed = val.strip()
            if trimmed != val:
                # An all-whitespace value becomes "", which for optional
                # fields should be NULL rather than an empty string.
                changes[f] = (val, trimmed or None)
        if changes:
            dirty.append((ac, changes))
            if limit and len(dirty) >= limit:
                break
    return dirty


def describe(ac, changes):
    head = f"  id={ac['id']:>4}  {ac.get('full_designation') or ac.get('model')!r}"
    lines = [head]
    for f, (old, new) in sorted(changes.items()):
        lines.append(f"        {f}: {old!r} -> {new!r}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(
        description="Trim leading/trailing whitespace from aircraft fields.")
    p.add_argument("--apply", action="store_true",
                   help="actually write the changes (default is a dry run)")
    p.add_argument("--fields", default=",".join(DEFAULT_FIELDS),
                   help="comma-separated field list")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    p.add_argument("--limit", type=int, default=None,
                   help="only process the first N affected records")
    args = p.parse_args()

    fields = tuple(f.strip() for f in args.fields.split(",") if f.strip())

    client = AirplaneClient()
    if args.apply and not client.api_key:
        print("error: --apply needs AIRPLANE_API_KEY (readwrite or admin).",
              file=sys.stderr)
        return 2

    dirty = find_dirty(client, fields, limit=args.limit)

    if args.json:
        print(json.dumps([
            {"id": ac["id"],
             "full_designation": ac.get("full_designation"),
             "changes": {f: {"from": o, "to": n} for f, (o, n) in ch.items()}}
            for ac, ch in dirty
        ], indent=2))
    else:
        print("=" * 66)
        print(f"  Records with stray whitespace: {len(dirty)}")
        print(f"  Base URL: {client.base_url}")
        print("=" * 66)
        for ac, ch in dirty:
            print(describe(ac, ch))

    if not dirty:
        print("\n  Nothing to fix.")
        return 0

    if not args.apply:
        print(f"\n  Dry run — nothing written. Re-run with --apply to fix "
              f"{len(dirty)} record(s).")
        return 1

    failures = []
    for ac, ch in dirty:
        payload = {f: new for f, (_old, new) in ch.items()}
        try:
            client.put(f"/api/v1/aircraft/{ac['id']}", json=payload)
        except ApiError as e:
            failures.append((ac["id"], str(e)))

    fixed = len(dirty) - len(failures)
    print(f"\n  Updated {fixed} record(s).")
    if failures:
        print(f"  {len(failures)} failed:")
        for aid, msg in failures:
            print(f"    id={aid}: {msg}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
