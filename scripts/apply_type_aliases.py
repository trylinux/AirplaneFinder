#!/usr/bin/env python3
"""Apply the alias plan to the live catalogue. Resumable.

Reads scripts/type_alias_plan.json and PATCHes each target type's alias
list. The API replaces the list it is sent, so this reads each type's
current aliases first and sends the union -- an alias someone added by hand
in admin is never silently dropped by a later run of this script.

One PATCH per TYPE, not per alias, for the same reason: sending them one at
a time would have each request clobber the one before it.

Resumable through scripts/applied_type_alias_ids.txt, the same convention
the country and c/n passes use. Re-running is safe and cheap: a type whose
aliases already match is skipped without a write.

Usage
-----
    AIRPLANE_BASE_URL=https://airplane.museum AIRPLANE_API_KEY=... \\
        python3 scripts/apply_type_aliases.py --dry-run
    ... python3 scripts/apply_type_aliases.py
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

DONE_FILE = Path(__file__).with_name("applied_type_alias_ids.txt")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", default="scripts/type_alias_plan.json")
    ap.add_argument("--done", default=str(DONE_FILE))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--base-url", default=None)
    args = ap.parse_args()

    plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
    rows = plan["aliases"]
    if not rows:
        print("nothing to apply")
        return

    done_path = Path(args.done)
    done = set()
    if done_path.exists():
        done = {int(line) for line in done_path.read_text().split() if line.strip()}

    by_type = defaultdict(list)
    for r in rows:
        by_type[r["target_id"]].append(r)

    client = AirplaneClient(base_url=args.base_url)
    applied = skipped = failed = 0

    for type_id, entries in sorted(by_type.items()):
        if type_id in done:
            skipped += 1
            continue
        try:
            current = client.get(f"/api/v1/aircraft-types/{type_id}")
        except ApiError as exc:
            print(f"  ! type {type_id}: {exc}")
            failed += 1
            continue

        # Union with whatever is already there, keyed the way the database
        # keys it, so a hand-added alias survives this pass.
        merged = {}
        for a in current.get("aliases") or []:
            merged[(a["match_key"], a.get("manufacturer_scope") or "")] = {
                "designation": a["designation"],
                "manufacturer_scope": a.get("manufacturer_scope") or "",
            }
        added = []
        for r in entries:
            key = (r["designation"].upper().replace("-", "").replace(" ", "").replace(".", ""),
                   r["manufacturer_scope"])
            payload = {"designation": r["designation"],
                       "manufacturer_scope": r["manufacturer_scope"]}
            if not any(v["designation"].lower() == r["designation"].lower()
                       and v["manufacturer_scope"] == r["manufacturer_scope"]
                       for v in merged.values()):
                merged[key] = payload
                added.append(r["designation"])

        label = f"{current['designation']} (id {type_id})"
        if not added:
            print(f"  = {label}: already has all {len(entries)} alias(es)")
            done.add(type_id)
            skipped += 1
            continue

        gain = sum(r["gains"] for r in entries)
        print(f"  {'[dry] ' if args.dry_run else ''}{label}: +{len(added)} "
              f"({', '.join(added)})  ~{gain} airframes")
        if args.dry_run:
            continue
        try:
            client.patch(f"/api/v1/aircraft-types/{type_id}",
                         json={"aliases": list(merged.values())})
        except ApiError as exc:
            print(f"  ! {label}: {exc}")
            failed += 1
            continue
        applied += 1
        done.add(type_id)
        done_path.write_text("\n".join(str(i) for i in sorted(done)) + "\n")

    print(f"\n{applied} type(s) updated, {skipped} already done, {failed} failed")
    if not args.dry_run and not failed:
        print(f"expected coverage: {plan['coverage_before']}% -> {plan['coverage_after']}% "
              f"(+{plan['airframes_gained']:,} airframes)")
        print("verify with: python3 scripts/type_coverage.py")


if __name__ == "__main__":
    main()
