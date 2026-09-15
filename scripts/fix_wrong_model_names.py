#!/usr/bin/env python3
"""Correct model_name where the variant was right and model_name was wrong.

    AIRPLANE_BASE_URL=https://airplane.museum AIRPLANE_API_KEY=amt_... \
        python3 scripts/fix_wrong_model_names.py --dry-run
    ... python3 scripts/fix_wrong_model_names.py

These came out of variant_review.tsv. In each row the variant carried both a
mark and a name, and the name in the variant was the CORRECT one for that
variant while model_name held the name of a different member of the family.
Every entry is a two-field PATCH: the mark stays on the variant, the right
name moves to model_name.

Hand-curated with a reason per line, in the shape of scripts/conflict_ops.py.
Nothing here is guessed from the data -- each is a designation fact.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

# id -> (variant, model_name, reason)
FIXES = {
    # An F-84F is a THUNDERSTREAK. Thunderjet is the straight-wing F-84B/D/E/G;
    # the F is the swept-wing aircraft with the Wright J65 and a different
    # airframe. Eight rows are publicly mislabelled.
    17032: ("F", "Thunderstreak", "F-84F is the swept-wing Thunderstreak, not the Thunderjet"),
    17653: ("F", "Thunderstreak", "as 17032"),
    17701: ("F", "Thunderstreak", "as 17032"),
    17708: ("F", "Thunderstreak", "as 17032"),
    18032: ("F", "Thunderstreak", "as 17032"),
    18037: ("F", "Thunderstreak", "as 17032"),
    18040: ("F", "Thunderstreak", "as 17032"),
    30001: ("F", "Thunderstreak", "as 17032"),

    # The F-5E is the Tiger II. Freedom Fighter is the earlier F-5A/B.
    29979: ("E", "Tiger II", "F-5E is the Tiger II; Freedom Fighter is the A/B"),

    # Beech 95-B55 is a Baron. The Travel Air is the earlier Model 95.
    21402: ("B55", "Baron", "Beech 95-B55 is a Baron; Travel Air is the Model 95"),

    # Stinson 108-2 is the Flying Station Wagon; the 108-1 is the Voyager.
    21267: ("2", "Flying Station Wagon", "Stinson 108-2 is the Flying Station Wagon; 108-1 is the Voyager"),

    # Civil Bell 47J-2 / 47J-3B1 are Rangers. Sioux is the US Army H-13 name.
    21324: ("J-2", "Ranger", "civil Bell 47J-2 is a Ranger; Sioux is the military H-13"),
    20680: ("J-3B1", "Ranger", "civil Bell 47J-3B1 is a Ranger; Sioux is the military H-13"),

    # The Aeronca 7AC is the Champion. "Champ" is the nickname, not the name.
    21443: (None, "Champion", "Aeronca 7AC is the Champion; Champ is the nickname"),
    21473: (None, "Champion", "Aeronca 7AC is the Champion; Champ is the nickname"),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--api-key", default=None)
    args = ap.parse_args()

    client = AirplaneClient(base_url=args.base_url, api_key=args.api_key)
    ok = failed = skipped = 0
    for aid, (variant, model_name, reason) in FIXES.items():
        try:
            before = client.get(f"/api/v1/aircraft/{aid}")["aircraft"]
        except ApiError as exc:
            print(f"  MISSING {aid}: {exc}", file=sys.stderr); failed += 1; continue

        if (before.get("model_name") or "") == model_name:
            skipped += 1
            continue
        line = (f"  {aid:<6} {before.get('model'):8} "
                f"variant {before.get('variant')!r} -> {variant!r}   "
                f"model_name {before.get('model_name')!r} -> {model_name!r}")
        if args.dry_run:
            print(line + f"\n         {reason}")
            ok += 1
            continue
        try:
            client.patch(f"/api/v1/aircraft/{aid}",
                         json={"variant": variant, "model_name": model_name})
        except ApiError as exc:
            print(f"  FAILED {aid}: {exc}", file=sys.stderr); failed += 1; continue
        print(line)
        ok += 1

    verb = "would change" if args.dry_run else "changed"
    print(f"\n{ok} {verb}, {skipped} already correct, {failed} failed")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
