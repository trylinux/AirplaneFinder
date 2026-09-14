"""Apply manufacturer_plan.json to the live catalog. Resumable.

    AIRPLANE_BASE_URL=https://airplane.museum AIRPLANE_API_KEY=amt_... \
        python3 scripts/apply_manufacturers.py --dry-run
    ... python3 scripts/apply_manufacturers.py

Each entry is a PATCH of `manufacturer` on one aircraft. Applied ids are
appended to applied_manufacturer_ids.txt as they land, so a re-run picks up
where an interrupted one stopped and never repeats a write.

`--only T` restricts a run to the transliteration class, `--only D` to the
accent class.

Unlike the variant pass, manufacturer is NOT part of uq_airframe
(full_designation, tail_number, operator_country), so these writes do not
collide and a 409 here would be a surprise. One second-order effect is worth
knowing about: _find_aircraft_duplicate matches a construction number
scoped by MANUFACTURER, so two records for the same airframe filed under
"Suchoj" and "Sukhoi" could not previously be seen as duplicates. Normalising
the spelling makes them visible to the next duplicate sweep -- which is a
gain, but expect that sweep to surface new pairs afterwards.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

_HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plan", type=Path, default=_HERE / "manufacturer_plan.json")
    ap.add_argument("--done", type=Path, default=_HERE / "applied_manufacturer_ids.txt")
    ap.add_argument("--conflicts", type=Path, default=_HERE / "manufacturer_conflicts.tsv")
    ap.add_argument("--dry-run", action="store_true",
                    help="print what would change and write nothing")
    ap.add_argument("--only", metavar="CLASS", action="append",
                    help="apply only these classes (B, C, D, A+); repeatable")
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--api-key", default=None)
    args = ap.parse_args()

    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"error: {exc}. Run plan_manufacturers.py first.", file=sys.stderr)
        raise SystemExit(2)

    if args.only:
        wanted = set(args.only)
        plan = [p for p in plan if p.get("_class") in wanted]

    done = set()
    if args.done.exists():
        done = {int(line) for line in args.done.read_text().split() if line.strip()}
    todo = [p for p in plan if p["_id"] not in done]
    print(f"{len(todo):,} to apply, {len(done):,} already applied")
    if not todo:
        return

    if args.dry_run:
        for p in todo[:40]:
            print(f"  [{p['_class']:2s}] id={p['_id']:<7} {p['_note']}")
        if len(todo) > 40:
            print(f"  ... and {len(todo)-40:,} more")
        print("\ndry run -- nothing written")
        return

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)
    conflicts, errors, applied = [], 0, 0
    with args.done.open("a", encoding="utf-8") as fh:
        for p in todo:
            body = {k: v for k, v in p.items() if not k.startswith("_")}
            try:
                client.patch(f"/api/v1/aircraft/{p['_id']}", json=body)
            except ApiError as exc:
                if exc.status == 409:
                    conflicts.append((p, exc))
                    print(f"  409 id={p['_id']} {p['_note']}  <- unexpected here; "
                          f"manufacturer is not part of uq_airframe", flush=True)
                else:
                    errors += 1
                    print(f"  ERR id={p['_id']} {exc}", file=sys.stderr, flush=True)
                continue
            fh.write(f"{p['_id']}\n")
            applied += 1
            if applied % 100 == 0:
                fh.flush()
                print(f"  {applied:,}/{len(todo):,}", flush=True)

    if conflicts:
        with args.conflicts.open("w", encoding="utf-8") as f:
            f.write("id\tclass\tbefore\tnote\terror\n")
            for p, exc in conflicts:
                f.write(f"{p['_id']}\t{p['_class']}\t{p.get('_before') or ''}\t"
                        f"{p['_note']}\t{exc}\n")

    print(f"\napplied {applied:,}  conflicts {len(conflicts):,}  errors {errors:,}")
    if conflicts:
        print(f"{len(conflicts):,} unexpected 409s in {args.conflicts}. Manufacturer is not "
              f"part of any unique key, so investigate before re-running.")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
