#!/usr/bin/env python3
"""Inspect candidate designations before writing a type for them.

The coverage worklist ranks *designation strings*, and that is not the same
as ranking aircraft. Several of its top entries are one aeroplane recorded
under several names: DHC-1 (55) and Chipmunk (46) are the same trainer;
C-45, AT-11, Expeditor and SNB are 111 Beech Model 18s; Whirlwind, H-19,
S-55 and WS-55 are 105 Sikorsky S-55s. Working down the list top-first
writes the same description two and three times.

So this answers the two questions to ask before researching anything:

  * how many airframes does each candidate really have, and is it already
    covered (directly or through an alias)?
  * what does the catalogue say built them -- which is how you spot a
    designation string that needs a manufacturer_scope, or one whose
    spellings vary too much to scope at all?

Both are just readings of the live data. Nothing is written.

Usage
-----
    AIRPLANE_BASE_URL=https://airplane.museum \\
        python3 scripts/type_family.py DHC-1 Chipmunk

    # a whole family, with the total if one record covered all of them
    python3 scripts/type_family.py --family C-45 AT-11 Expeditor SNB

    # the worklist, with placeholder models dropped
    python3 scripts/type_family.py --worklist 40
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

_NOISE = re.compile(r"[^A-Z0-9]+")

# Not designations. These are rows whose model field records that nobody
# knew what the aircraft was, and they sit at the top of the worklist by
# sheer count. Writing a type for "Aircraft" is not a content task; fixing
# 1,132 rows is a data task.
PLACEHOLDERS = {"AIRCRAFT", "LIGHTAIRCRAFT", "UNIDENTIFIED", "UNKNOWN",
                "GLIDER", "HELICOPTER", "JET", "BIPLANE", "MONOPLANE"}


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


def build_index(types):
    """key -> [(scope, label, is_alias)] for everything already covered."""
    index = {}
    for t in types:
        index.setdefault(t["match_key"], []).append(
            (t.get("manufacturer_scope") or "", t["designation"], False))
        for al in t.get("aliases") or []:
            scopes = [al.get("manufacturer_scope") or "",
                      t.get("manufacturer_scope") or ""]
            index.setdefault(al["match_key"], []).append(
                (max(scopes, key=len), t["designation"], True))
    return index


def report(designation, aircraft, index):
    key = match_key(designation)
    rows = [a for a in aircraft
            if key in (match_key(a.get("model"), a.get("variant")),
                       match_key(a.get("model")))]
    builders = Counter((a.get("manufacturer") or "?") for a in rows)

    covered_by = None
    for scope, label, is_alias in index.get(key, ()):
        if any(scope_matches(scope, a.get("manufacturer")) for a in rows):
            covered_by = f"{label}{' (via alias)' if is_alias else ''}"
            break

    print(f"\n{designation}  —  {len(rows)} airframe(s)")
    if key in PLACEHOLDERS:
        print("  ** PLACEHOLDER, not a designation. This is a data-quality")
        print("     row, not a type to write. Skip it.")
    if covered_by:
        print(f"  ** already covered by {covered_by} — do not research this")
    for builder, n in builders.most_common(8):
        print(f"     {n:>4}  {builder}")
    if len(builders) > 8:
        print(f"     ... and {len(builders) - 8} more")

    # Whether to scope turns on one question, and it is NOT how many
    # spellings there are: it is whether the minority builders are the same
    # company written differently or a different company altogether.
    # "Boeing / Boeing-Stearman / Stearman" is one Kaydet. "British
    # Aerospace / Pilcher / Curtiss" is a jet trainer, an 1896 hang glider
    # and a 1920s biplane fighter that happen to share the word Hawk.
    #
    # So cluster the builders by whether they would satisfy each other AS A
    # SCOPE -- the same prefix rule the site uses -- and report the clusters.
    # One cluster means one aircraft and no scope needed. More than one
    # means look, because at least one of them is probably not this type.
    clusters = []
    for builder, n in builders.most_common():
        for c in clusters:
            if any(scope_matches(other, builder) or scope_matches(builder, other)
                   for other in c["builders"]):
                c["builders"].append(builder)
                c["n"] += n
                break
        else:
            clusters.append({"builders": [builder], "n": n})

    if len(clusters) > 1:
        print(f"  ! {len(clusters)} unrelated builder group(s) share this string:")
        for c in clusters:
            print(f"       {c['n']:>4}  {' / '.join(c['builders'])}")

        # Does ONE scope string cover the whole main group? The shortest
        # spelling is the only candidate, since the rule is prefix matching.
        main = clusters[0]
        candidate = min(main["builders"], key=lambda b: len(_NOISE.sub("", b.upper())))
        works = all(scope_matches(candidate, b) for b in main["builders"])
        minority = sum(c["n"] for c in clusters[1:])

        print(f"    Decide which groups are THIS aircraft. If the small ones are")
        print(f"    a different aeroplane sharing the name, scope the type; if")
        print(f"    they are licence builders, leave it unscoped.")
        if works:
            print(f"    manufacturer_scope \"{candidate}\" would keep all "
                  f"{main['n']} and exclude the other {minority}.")
        else:
            print(f"    No single scope string covers "
                  f"{' / '.join(main['builders'])}: they do not prefix-match each")
            print(f"    other, so any scope also drops some of the {main['n']} you")
            print(f"    want. Normalising those spellings, or fixing the "
                  f"{minority} stray")
            print(f"    row(s), is the better pass — see "
                  f"scripts/README_manufacturer_spelling.md.")
    elif len(builders) > 1:
        print(f"  = one builder under {len(builders)} spellings — do NOT scope;")
        print(f"    a scope here would strip the write-up from most of them.")

    return len(rows), covered_by is not None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("designations", nargs="*")
    ap.add_argument("--family", action="store_true",
                    help="also print the combined total, i.e. what ONE type "
                         "record plus aliases for the rest would cover")
    ap.add_argument("--worklist", type=int, default=0,
                    help="pull the top N uncovered designations instead")
    ap.add_argument("--base-url", default=None)
    args = ap.parse_args()

    client = AirplaneClient(base_url=args.base_url)
    try:
        types = client.get("/api/v1/aircraft-types")
        aircraft = list(client.iter_aircraft())
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)

    index = build_index(types)

    names = list(args.designations)
    if args.worklist:
        uncovered, labels = Counter(), {}
        for a in aircraft:
            base = match_key(a.get("model"))
            if not base or base in PLACEHOLDERS:
                continue
            hit = False
            for key in (match_key(a.get("model"), a.get("variant")), base):
                for scope, _l, _al in index.get(key, ()):
                    if scope_matches(scope, a.get("manufacturer")):
                        hit = True
                        break
                if hit:
                    break
            if not hit:
                uncovered[base] += 1
                labels.setdefault(base, Counter())[(a.get("model") or "").strip()] += 1
        names = [labels[k].most_common(1)[0][0]
                 for k, _n in uncovered.most_common(args.worklist)]

    if not names:
        print("nothing to inspect", file=sys.stderr)
        raise SystemExit(2)

    total, covered = 0, 0
    for designation in names:
        n, is_covered = report(designation, aircraft, index)
        total += n
        covered += is_covered

    if args.family:
        print(f"\n{'=' * 60}")
        print(f"one type record + {len(names) - 1} alias(es) would cover "
              f"{total} airframes")
    elif covered:
        print(f"\n{covered} of {len(names)} are already covered.")


if __name__ == "__main__":
    main()
