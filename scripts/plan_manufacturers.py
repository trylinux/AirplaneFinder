#!/usr/bin/env python3
"""Plan a normalisation of the `manufacturer` column. Writes nothing.

Manufacturer is a facet visitors filter on, so one company spelled two ways
splits its own results. Three classes of split exist in this catalog:

  T  transliteration   German/Polish renderings of Russian bureau names
                       "Mikojan-Guriewicz" -> "Mikoyan-Gurevich"     121 rows
  D  accents only      "Aerospatiale" -> "Aérospatiale"              ~215 rows
  C  case only         "LET" vs "Let", "SOCATA" vs "Socata"           ~79 rows

T and D go to the plan. C goes to review, because it is an acronym question
a script cannot answer: ERCO really is an acronym (Engineering and Research
Corporation) and should stay capitalised even though "Erco" is the majority
spelling here, while "de Havilland" is a name and "De Havilland" is wrong.
Majority-wins would get two of the nine backwards.

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/plan_manufacturers.py

Outputs: manufacturer_plan.json, manufacturer_review.tsv, manufacturer_summary.txt
"""

from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

# ── T: transliteration ───────────────────────────────────────────────
# Only bureau names actually present in the catalog, each verified against
# the canonical spelling already dominant in the same column. Deliberately
# NOT a general -ow/-ew rule: Bölkow, Schleicher, Lommatzsch and Barkley-Grow
# are real names with those shapes and must not be touched.
TRANSLITERATION = {
    "Mikojan-Guriewicz": "Mikoyan-Gurevich",
    "Suchoj": "Sukhoi",
    "Jakowlew": "Yakovlev",
    "Antonow": "Antonov",
    "Tupolew": "Tupolev",
    "Polikarpow": "Polikarpov",
    "Lisunow": "Lisunov",
    "Petlakow": "Petlyakov",
}

# ── D: accents ───────────────────────────────────────────────────────
# The default is to prefer the accented form: it is the company's own
# spelling and the unaccented one is nearly always a transcription loss.
#
# Breguet is the exception that proves the rule. Louis Charles Breguet's
# surname carries an accent, but the AIRCRAFT COMPANY wrote itself Breguet
# — Breguet 19, Breguet Atlantic — and every aviation reference follows it.
# An exception list is the honest way to hold that; a rule cannot infer it.
ACCENT_EXCEPTIONS = {
    "breguet": "Breguet",
}


def strip_accents(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def accent_count(s: str) -> int:
    """How many characters carry a diacritic (or are otherwise non-ASCII).

    Counted per character rather than by zipping against the stripped form,
    because stripping changes the length -- "Ø" vanishes entirely -- and a
    zip would then compare misaligned positions.
    """
    return sum(1 for ch in s if ord(ch) > 127)


def choose_accented(forms):
    """Canonical spelling among forms differing only by accents/case.

    Returns (canonical, reason) or (None, why-it-needs-review).
    """
    key = strip_accents(forms[0]).lower()
    if key in ACCENT_EXCEPTIONS:
        return ACCENT_EXCEPTIONS[key], "company's own unaccented spelling"
    ranked = sorted(forms, key=lambda f: (-accent_count(f), f))
    best = ranked[0]
    if accent_count(best) == 0:
        return None, "no accented form to prefer"
    if len(ranked) > 1 and accent_count(ranked[1]) == accent_count(best):
        return None, "two forms accented differently"
    return best, "accented form is the company's own spelling"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--base-url", default=None)
    args = ap.parse_args()

    client = AirplaneClient(base_url=args.base_url)
    try:
        aircraft = list(client.iter_aircraft())
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)

    counts = Counter((a.get("manufacturer") or "").strip() for a in aircraft)
    counts.pop("", None)

    # Group spellings that differ only by case and/or accents.
    groups = defaultdict(Counter)
    for value, n in counts.items():
        groups[strip_accents(value).lower()][value] = n

    canonical = {}          # wrong spelling -> (right spelling, class, reason)
    review = []
    for key, forms in groups.items():
        if len(forms) < 2:
            continue
        form_list = list(forms)
        if len({f.lower() for f in form_list}) == 1:
            # C -- case only. Never automatic.
            majority = forms.most_common(1)[0][0]
            review.append((key, dict(forms), majority,
                           "case only: acronym or name? majority shown as a suggestion"))
            continue
        winner, reason = choose_accented(form_list)
        if winner is None:
            review.append((key, dict(forms), "", reason))
            continue
        for f in form_list:
            if f != winner:
                canonical[f] = (winner, "D", reason)

    for wrong, right in TRANSLITERATION.items():
        if counts.get(wrong):
            canonical[wrong] = (right, "T", "German/Polish rendering of a Russian bureau name")

    plan = []
    for a in aircraft:
        m = (a.get("manufacturer") or "").strip()
        if m in canonical:
            right, cls, reason = canonical[m]
            plan.append({"_id": a["id"], "_class": cls, "_before": m,
                         "_note": f"{m!r} -> {right!r} ({reason})",
                         "manufacturer": right})

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "manufacturer_plan.json").write_text(
        json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")
    with (args.out_dir / "manufacturer_review.tsv").open("w", encoding="utf-8") as f:
        f.write("folded\tspellings\tsuggestion\treason\n")
        for key, forms, suggestion, reason in sorted(review):
            spelled = "; ".join(f"{v} x{n}" for v, n in
                                sorted(forms.items(), key=lambda x: -x[1]))
            f.write(f"{key}\t{spelled}\t{suggestion}\t{reason}\n")

    by_class = Counter(p["_class"] for p in plan)
    summary = "\n".join([
        f"{len(aircraft):,} airframes examined",
        f"{len([g for g in groups.values() if len(g) > 1]):,} manufacturer names spelled more than one way",
        "",
        f"  T  {by_class['T']:4,}  transliteration of a Russian bureau name",
        f"  D  {by_class['D']:4,}  accents restored",
        f"     {len(plan):4,}  rows in the plan",
        f"  C  {len(review):4,}  names needing a decision -> manufacturer_review.tsv",
    ])
    (args.out_dir / "manufacturer_summary.txt").write_text(summary + "\n", encoding="utf-8")
    print(summary)
    print(f"\nwrote {args.out_dir/'manufacturer_plan.json'} and "
          f"{args.out_dir/'manufacturer_review.tsv'}")


if __name__ == "__main__":
    main()
