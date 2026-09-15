#!/usr/bin/env python3
"""How much of the collection currently inherits a type write-up.

Answers two questions the type library needs answered continuously:

  1. What fraction of airframes currently show an "About the type" card?
  2. Which designations, ordered by airframe count, would buy the most
     coverage if written next?

Coverage is measured the way the site resolves it -- normalized
model+variant, exact variant beating base model, manufacturer_scope
honoured, and aliases counted -- so the number here is the number of
aircraft pages that actually show a write-up, not an estimate.

Aliases matter to the worklist as much as to the number. Without them
AT-6 (59 airframes) and CF-104 (56) sit at the top of "write this next"
forever, and both are already covered: they are a T-6 and an F-104 under
a second designation. Sending a research batch at those is the exact
waste the alias feature exists to prevent.

Usage
-----
    python3 scripts/type_coverage.py                      # against localhost
    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/type_coverage.py
    python3 scripts/type_coverage.py --worklist 50        # next 50 to write
    python3 scripts/type_coverage.py --worklist 50 --json > next.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

# Must agree with type_match_key() in models.py. See the note in
# import_aircraft_types.py about why this is duplicated rather than imported.
_NOISE = re.compile(r"[^A-Z0-9]+")


def match_key(model, variant=None):
    joined = f"{(model or '').strip()}{(variant or '').strip()}".upper()
    return _NOISE.sub("", joined) or None


def scope_matches(scope, manufacturer):
    """Must agree with manufacturer_matches() in models.py."""
    scope_key = _NOISE.sub("", (scope or "").upper())
    if not scope_key:
        return True
    mfr_key = _NOISE.sub("", (manufacturer or "").upper())
    if not mfr_key:
        return False
    return mfr_key.startswith(scope_key) or scope_key.startswith(mfr_key)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--worklist", type=int, default=25,
                    help="how many uncovered designations to list (default 25)")
    ap.add_argument("--json", action="store_true",
                    help="emit the worklist as JSON, ready to seed a research run")
    ap.add_argument("--base-url", default=None)
    args = ap.parse_args()

    client = AirplaneClient(base_url=args.base_url)
    try:
        types = client.get("/api/v1/aircraft-types")
        aircraft = list(client.iter_aircraft())
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)

    # key -> list of (scope, is_alias). A designation can be answered by a
    # real record, by an alias, or by several of each at different scopes,
    # and only a scope that matches the airframe's builder counts.
    have = defaultdict(list)
    for t in types:
        have[t["match_key"]].append((t.get("manufacturer_scope") or "", False))
        for al in t.get("aliases") or []:
            # An alias must satisfy its own scope AND the type's, so the
            # effective scope is the more restrictive of the two. They are
            # never both set in practice; taking the longer is enough.
            scopes = [al.get("manufacturer_scope") or "",
                      t.get("manufacturer_scope") or ""]
            have[al["match_key"]].append((max(scopes, key=len), True))

    def answered(key, manufacturer):
        for scope, is_alias in have.get(key, ()):
            if scope_matches(scope, manufacturer):
                return True, is_alias
        return False, False

    covered = 0
    by_variant = 0
    by_alias = 0
    uncovered = Counter()
    labels = {}                       # match_key -> Counter of raw spellings
    for a in aircraft:
        exact = match_key(a.get("model"), a.get("variant"))
        base = match_key(a.get("model"))
        mfr = a.get("manufacturer")
        hit_exact, alias_exact = answered(exact, mfr) if exact else (False, False)
        hit_base, alias_base = answered(base, mfr) if base else (False, False)
        if hit_exact:
            covered += 1
            by_variant += 1
            by_alias += alias_exact
        elif hit_base:
            covered += 1
            by_alias += alias_base
        elif base:
            uncovered[base] += 1
            # Keep the most common raw spelling as the human-readable label:
            # the key is normalized, and "MIG 21" is not what anyone wants
            # to read in a worklist.
            labels.setdefault(base, Counter())[(a.get("model") or "").strip()] += 1

    total = len(aircraft)
    pct = (covered / total * 100) if total else 0.0
    print(f"{len(types)} type record(s) in the library")
    print(f"{covered:,} of {total:,} airframes inherit a write-up ({pct:.1f}%)")
    print(f"  {by_variant:,} matched a variant record, {covered - by_variant:,} the base model")
    if by_alias:
        print(f"  {by_alias:,} of those arrived through an alias "
              f"(see scripts/README_type_aliases.md)")
    print(f"  {total - covered:,} airframes across {len(uncovered):,} uncovered designations\n")

    rows = uncovered.most_common(args.worklist)
    if args.json:
        json.dump([
            {"model": labels[k].most_common(1)[0][0], "airframes": n}
            for k, n in rows
        ], sys.stdout, indent=2)
        print()
        return

    if not rows:
        print("Nothing uncovered.")
        return

    print(f"Next {len(rows)} designations by airframe count:")
    running = covered
    for i, (key, n) in enumerate(rows, 1):
        running += n
        label = labels[key].most_common(1)[0][0]
        print(f"{i:3d}. {label:20s} {n:5,d} airframes   "
              f"-> {running / total * 100:.1f}% cumulative coverage")


if __name__ == "__main__":
    main()
