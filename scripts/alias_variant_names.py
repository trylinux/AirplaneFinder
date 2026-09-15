#!/usr/bin/env python3
"""Record a second type name from the variant column as an alias.

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/alias_variant_names.py --dry-run
    AIRPLANE_API_KEY=amt_... python3 scripts/alias_variant_names.py

What is left in variant_review.tsv after every mechanical class has run is not
a data error. It is a missing concept: the aircraft genuinely has TWO names and
model_name holds one of them.

    C-47   variant "Dakota C.4"      model_name "Skytrain"
    T-50   variant "Crane Mk I"      model_name "Bobcat"
    AT-6   variant "A Harvard"       model_name "Texan"
    P-40   variant "Kittyhawk I"     model_name "Warhawk"
    S-75   variant "Dvina"           model_name "SA-2 Guideline"

Both names are right. Which is primary depends on who operated the airframe --
Dakota is the Commonwealth name for the Skytrain, Crane the RCAF name for the
Bobcat -- and picking one would throw the other away.

So this script throws nothing away. It copies the name out of the variant into
aircraft_aliases, which the schema already describes as "alternate names /
search terms", and leaves variant and model_name exactly as they are. A visitor
searching "Dakota" now finds the Skytrain; the variant keeps the distinction it
was drawing.

Doing that also retires the row: plan_variants.py treats a name already present
in the aliases as accounted for, so these stop appearing in the review file
without an allowlist to maintain.

NOTE the API replaces the whole alias set on PATCH, so each write sends the
union of the existing aliases and the new name.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402
from plan_variants import classify, fold_name, split_mark_and_name  # noqa: E402


# The split is mechanical and gets a handful wrong, so those are stated here
# rather than regexed at. Each line is a designation judgement, in the shape of
# scripts/conflict_ops.py.

# Rows where the variant holds a CODE, not a name. Nothing to alias.
SKIP = {
    12315: "Ka-25 BShZ is a variant code",
    28908: "Ki-43 II Otsu -- Otsu is the Japanese sub-variant marker, not a name",
    5827:  "Ki-45 KAIc is a variant code",
    31380: "Lim-2 Rbis is a variant code",
    17595: "MiG-21 bis-SAU is a variant code",
    22008: "TS-11 bis-B is a variant code",
}

# Rows where the mechanical split truncated the name. "Pou" and "du" are both
# three characters or fewer, so the splitter reads them as marks and leaves
# only "Ciel".
NAME_OVERRIDES = {
    17882: "Pou du Ciel",
    17893: "Pou du Ciel",
    20665: "Pou du Ciel",
    8481:  "Arrow II",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--done", type=Path,
                    default=Path(__file__).resolve().parent / "aliased_variant_ids.txt")
    args = ap.parse_args()

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)
    try:
        aircraft = list(client.iter_aircraft())
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)

    done = set()
    if args.done.exists():
        done = {int(x) for x in args.done.read_text().split() if x.strip()}

    todo = []
    for a in aircraft:
        if a["id"] in done:
            continue
        cls, _, _ = classify(a.get("model"), a.get("variant"),
                             a.get("model_name"), a.get("aliases"))
        if cls != "A":
            continue
        if a["id"] in SKIP:
            continue
        name = NAME_OVERRIDES.get(a["id"])
        if not name:
            _, name = split_mark_and_name((a.get("variant") or "").strip())
        if not name:
            continue
        existing = [x for x in (a.get("aliases") or [])]
        if fold_name(name) in {fold_name(x) for x in existing}:
            continue
        todo.append((a, name, existing))

    print(f"{len(todo)} airframes with a second name to record\n")
    applied = failed = 0
    fh = None if args.dry_run else args.done.open("a", encoding="utf-8")
    for a, name, existing in todo:
        line = (f"  {a['id']:<6} {(a.get('manufacturer') or '')[:16]:16} "
                f"{a.get('full_designation',''):14} +alias {name!r:24} "
                f"(model_name {a.get('model_name')!r})")
        if args.dry_run:
            print(line)
            applied += 1
            continue
        try:
            client.patch(f"/api/v1/aircraft/{a['id']}",
                         json={"aliases": existing + [name]})
        except ApiError as exc:
            print(f"  FAILED {a['id']}: {exc}", file=sys.stderr)
            failed += 1
            continue
        fh.write(f"{a['id']}\n")
        applied += 1
        if applied % 25 == 0:
            fh.flush()
            print(f"  {applied}/{len(todo)}")
    if fh:
        fh.close()

    verb = "would gain an alias" if args.dry_run else "aliased"
    print(f"\n{applied} {verb}, {failed} failed")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
