#!/usr/bin/env python3
"""Plan the aircraft-type alias pass. Writes nothing.

Reads the curated map in type_alias_map.py and the live catalogue, and
answers the only questions that matter before applying it:

  * does the target type exist, identified the way uq_type_match
    identifies it — (designation, manufacturer_scope)?
  * would the alias collide with a real type or with another type's alias?
  * how many airframes does it actually reach, counted the way the site
    resolves them (normalized key, exact before base, manufacturer scope
    honoured on both the alias and the type it points at)?
  * how many of those already had a write-up, and so are not a gain?

An alias that reaches zero airframes is not an error -- the designation may
simply not be in the collection yet -- but it is reported, because a long
tail of zeros usually means a spelling in the map that the catalogue does
not use.

Usage
-----
    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/plan_type_aliases.py
    python3 scripts/plan_type_aliases.py --out scripts/type_alias_plan.json
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
from type_alias_map import CONFIRMED, JUDGEMENT  # noqa: E402

# Must agree with type_match_key() / manufacturer_matches() in models.py.
_NOISE = re.compile(r"[^A-Z0-9]+")


def match_key(model, variant=None):
    joined = f"{(model or '').strip()}{(variant or '').strip()}".upper()
    return _NOISE.sub("", joined) or None


def scope_matches(scope, manufacturer):
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
    ap.add_argument("--out", default="scripts/type_alias_plan.json")
    ap.add_argument("--base-url", default=None)
    args = ap.parse_args()

    client = AirplaneClient(base_url=args.base_url)
    try:
        types = client.get("/api/v1/aircraft-types")
        aircraft = list(client.iter_aircraft())
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)

    # (match_key, scope) -> type. The same pair uq_type_match uses.
    by_pair = {(t["match_key"], t.get("manufacturer_scope") or ""): t for t in types}
    by_key = defaultdict(list)
    for t in types:
        by_key[t["match_key"]].append(t)
    existing_aliases = {}
    for t in types:
        for a in t.get("aliases") or []:
            existing_aliases[(a["match_key"], a.get("manufacturer_scope") or "")] = t["id"]

    # Which airframes already have a write-up, by the site's own rule.
    covered = set()
    for a in aircraft:
        for key in (match_key(a.get("model"), a.get("variant")), match_key(a.get("model"))):
            if not key:
                continue
            for t in by_key.get(key, []):
                if scope_matches(t.get("manufacturer_scope"), a.get("manufacturer")):
                    covered.add(a["id"])
                    break
            if a["id"] in covered:
                break

    rows, problems = [], []
    claimed = {}            # (key, scope) -> alias designation, within this run
    total_gain = set()

    for designation, scope, target_designation, target_scope, why in CONFIRMED:
        key = match_key(designation)
        target = by_pair.get((match_key(target_designation), target_scope))
        if target is None:
            problems.append(f"{designation}: no type for '{target_designation}'"
                            + (f" scoped to {target_scope}" if target_scope else "")
                            + " — write it first, or fix the map")
            continue
        if key.isdigit() and not scope:
            problems.append(f"{designation}: bare number with no scope — would match "
                            f"unrelated aircraft")
            continue
        clash = by_pair.get((key, scope))
        if clash and clash["id"] != target["id"]:
            problems.append(f"{designation}: already a type of its own "
                            f"(id {clash['id']}, {clash['display_name']})")
            continue
        owner = existing_aliases.get((key, scope))
        if owner is not None and owner != target["id"]:
            problems.append(f"{designation}: already an alias of type {owner}")
            continue
        if (key, scope) in claimed:
            problems.append(f"{designation}: duplicates '{claimed[(key, scope)]}' in the map")
            continue
        claimed[(key, scope)] = designation

        # Who it reaches. An alias must satisfy its own scope AND the scope
        # of the type it points at -- it is a second door, not a bypass.
        reached, gained = [], []
        for a in aircraft:
            if key not in (match_key(a.get("model"), a.get("variant")),
                           match_key(a.get("model"))):
                continue
            mfr = a.get("manufacturer")
            if not scope_matches(scope, mfr):
                continue
            if not scope_matches(target.get("manufacturer_scope"), mfr):
                continue
            reached.append(a["id"])
            if a["id"] not in covered:
                gained.append(a["id"])
        total_gain.update(gained)

        rows.append({
            "designation": designation,
            "manufacturer_scope": scope,
            "target_id": target["id"],
            "target": target["designation"],
            "target_display_name": target["display_name"],
            "why": why,
            "reaches": len(reached),
            "gains": len(gained),
            # What the catalogue actually spells these, so a zero-gain row
            # can be diagnosed without another query.
            "spellings": Counter(
                (a.get("manufacturer") or "?") for a in aircraft
                if key in (match_key(a.get("model"), a.get("variant")),
                           match_key(a.get("model")))
            ).most_common(4),
        })

    rows.sort(key=lambda r: -r["gains"])
    total = len(aircraft)
    before = len(covered) / total * 100
    after = (len(covered) + len(total_gain)) / total * 100

    print(f"{len(rows)} alias(es) planned across {len({r['target_id'] for r in rows})} types")
    print(f"coverage {len(covered):,}/{total:,} ({before:.1f}%) "
          f"-> {len(covered) + len(total_gain):,} ({after:.1f}%), "
          f"+{len(total_gain):,} airframes\n")
    for r in rows:
        note = "" if r["gains"] else "   [reaches nothing — check the spelling]"
        scope = f" ({r['manufacturer_scope']} only)" if r["manufacturer_scope"] else ""
        print(f"  {r['designation'] + scope:<22} -> {r['target']:<10} "
              f"+{r['gains']:>4} airframes{note}")

    if problems:
        print(f"\n{len(problems)} refused:")
        for p in problems:
            print(f"  ! {p}")

    print(f"\n{len(JUDGEMENT)} related designations deliberately NOT aliased "
          f"(see type_alias_map.JUDGEMENT):")
    for designation, target, why in JUDGEMENT:
        print(f"  - {designation:<14} vs {target:<12} {why}")

    out = Path(args.out)
    out.write_text(json.dumps({
        "coverage_before": round(before, 2),
        "coverage_after": round(after, 2),
        "airframes_gained": len(total_gain),
        "aliases": rows,
        "problems": problems,
    }, indent=2), encoding="utf-8")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
