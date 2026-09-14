#!/usr/bin/env python3
"""Plan a cleanup of the `variant` column. Writes nothing to the database.

`variant` is meant to hold a mark or suffix -- "A", "F.6", "Mk 20", "bis" --
and it is half of the generated `full_designation` column. Research passes
have also used it for the TYPE NAME, which belongs in `model_name`, so the
catalog renders headings like "CT-133 Silver Star 3" and "SE 210 Caravelle".

This script sorts every non-empty variant into one of four classes and
writes only the mechanical ones to a plan. The judgement calls go to a TSV
for a person, because the distinction is not one a regex can make: a
Spitfire Mk IX and a Canberra Mk 20 are correctly written that way, while a
CM.170 Magister is a name in the wrong column.

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/plan_variants.py

Outputs (next to the script, or --out-dir):
    variant_plan.json     mechanical fixes, ready for apply_variants.py
    variant_review.tsv    everything needing a human decision
    variant_summary.txt   counts per class

Classes
-------
B  variant repeats the model      "A-4" + "A-4KU"        -> variant "KU"
D  variant duplicates model_name  "SE 210" + "Caravelle" -> variant blank
A+ variant carries a name ALREADY in model_name
                                  "CL-13" + "Sabre Mk.6", model_name "Sabre"
                                                         -> variant "Mk.6"
A  variant carries some other word                       -> REVIEW, never auto

B, D and A+ are the plan. A is the review file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402

_MARK_WORD = re.compile(r"^(?:mk|mark|srs|series|ser)\.?$", re.I)
_ROMAN = re.compile(r"^[IVXLC]+$")
_NAMEY = re.compile(r"^[A-Za-z][A-Za-z\-]{3,}$")
_SUFFIX_WORDS = {"bis", "ter", "uti", "utl", "kai"}

# Generic designator words. These look like names and often DO appear in
# model_name, which makes the A+ rule fire and strip them -- turning
# "Ki-11" + "Type 91" into variant "91", which is worse than leaving it
# alone. Any of these in the variant sends the row to review instead.
_GENERIC = {"type", "model", "series", "mark", "variant", "version", "class", "number"}


def is_mark_token(tok: str) -> bool:
    """Is this token a mark/suffix rather than a name?

    Deliberately generous: anything that could be a designation suffix counts,
    so only clearly word-like tokens fall through to the name classes. Being
    wrong in this direction leaves a row alone; being wrong the other way
    edits a correct record.

    The all-caps clause is what keeps real variant CODES out of the name
    classes -- AJSF on a Saab 37, GCBC on a Citabria 7, SIGINT on an
    Atlantic. Aircraft names in this catalog are written Title Case
    (Magister, Caravelle, Musketeer), so requiring upper case costs nothing
    and rescues 61 rows that an earlier version wrongly called names.
    """
    core = tok.strip(".-")
    if not core:
        return True
    if _MARK_WORD.match(core) or _ROMAN.match(core):
        return True
    if core.lower() in _SUFFIX_WORDS:
        return True
    if any(ch.isdigit() for ch in core):        # C8E, B55, J-3B1, F.6, 108-2
        return True
    if core.isupper() and len(core) <= 6:       # AJSF, GCBC, TF, KC, SIGINT
        return True
    return len(core) <= 3                       # A, EJ, bis-length suffixes


def split_mark_and_name(variant):
    """Split "A Senior Skyrocket" into ("A", "Senior Skyrocket").

    Marks are taken from BOTH ends: "Silver Star 3" is the Silver Star,
    mark 3 -- the trailing number is a mark that happens to sit last. The
    middle is the name, and it must contain at least one word-like token or
    there is no name here at all.
    """
    toks = variant.split()
    i = 0
    while i < len(toks) and is_mark_token(toks[i]):
        i += 1
    j = len(toks)
    while j > i and is_mark_token(toks[j - 1]):
        j -= 1
    name_toks = toks[i:j]
    if not any(_NAMEY.match(t) and not is_mark_token(t) for t in name_toks):
        return "", ""
    mark = " ".join(toks[:i] + toks[j:])
    return mark, " ".join(name_toks)


def classify(model, variant, model_name):
    """Return (class, patch, note). patch is None for review-only rows."""
    model = (model or "").strip()
    model_name = (model_name or "").strip()
    raw = variant or ""
    variant = raw.strip()
    if not variant:
        return None, None, ""

    # C -- stray whitespace. Compared against the RAW value, because every
    # rule below works on the stripped form and would otherwise mask this.
    tidy = re.sub(r"\s+", " ", variant)
    if tidy != raw:
        return "C", {"variant": tidy}, f"whitespace: {raw!r} -> {tidy!r}"
    variant = tidy

    # D -- the variant IS the type name, and model_name already holds it.
    if model_name and variant.lower() == model_name.lower():
        return "D", {"variant": None}, f"variant duplicates model_name {model_name!r}"

    # B -- the variant restates the model. "A-4" + "A-4KU" -> "KU".
    if variant.upper().startswith(model.upper()) and len(variant) > len(model):
        rest = variant[len(model):].lstrip(" -")
        if rest:
            return "B", {"variant": rest}, f"variant repeated the model: {variant!r} -> {rest!r}"

    toks = variant.split()
    namey = [t for t in toks if _NAMEY.match(t) and not is_mark_token(t)]
    if not namey:
        return None, None, ""            # a plain mark -- leave it alone

    # A+ -- every word-like token is already in model_name, so dropping them
    # loses nothing and the remaining mark is the real variant. A generic
    # designator word disqualifies the row: "Type 91" is a whole designation,
    # not a name plus a mark.
    if (model_name
            and not any(t.lower() in _GENERIC for t in namey)
            and all(t.lower() in model_name.lower() for t in namey)):
        rest = " ".join(t for t in toks if t not in namey).strip()
        return "A+", {"variant": rest or None}, (
            f"name {' '.join(namey)!r} already in model_name {model_name!r}"
            f" -> variant {rest or '(blank)'!r}")

    # E -- the variant is a mark plus a NAME, and model_name is empty, so the
    # split is lossless: the mark stays on the variant and the name moves to
    # the column it belongs in. "31-55" + "A Senior Skyrocket" becomes
    # variant "A", model_name "Senior Skyrocket".
    mark, name = split_mark_and_name(variant)
    # A generic designator disqualifies the split for the same reason it
    # disqualifies A+: "Model A" on a Pusher is a whole designation, and
    # moving "Model" into model_name would be nonsense.
    if name and any(t.lower() in _GENERIC for t in name.split()):
        return "A", None, f"generic designator in variant {variant!r}"
    if name and not model_name:
        return "E", {"variant": mark or None, "model_name": name}, (
            f"name {name!r} moved to model_name; variant {mark or '(blank)'!r}")

    # A -- a name we cannot account for, or one that would overwrite an
    # existing model_name. Never automatic: a Bell 47 is a Sioux in military
    # service and a Ranger as the civil J-2, and both spellings are right.
    if name and model_name:
        return "A", None, (f"variant holds the name {name!r} but model_name "
                           f"already says {model_name!r}")
    return "A", None, f"word-like token(s) {' '.join(namey)!r} in variant"


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

    plan, review, counts = [], [], Counter()
    for a in aircraft:
        cls, patch, note = classify(a.get("model"), a.get("variant"), a.get("model_name"))
        if cls is None:
            counts["leave alone"] += 1
            continue
        counts[cls] += 1
        row = {
            "_id": a["id"],
            "model": a.get("model"),
            "variant": a.get("variant"),
            "model_name": a.get("model_name"),
            "manufacturer": a.get("manufacturer"),
            "tail_number": a.get("tail_number"),
            "class": cls,
            "note": note,
        }
        if patch is None:
            review.append(row)
        else:
            plan.append({"_id": a["id"], "_class": cls, "_note": note,
                         "_before": a.get("variant"), **patch})

    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / "variant_plan.json").write_text(
        json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")

    with (args.out_dir / "variant_review.tsv").open("w", encoding="utf-8") as f:
        f.write("id\tmanufacturer\tmodel\tvariant\tmodel_name\t"
                "candidate_mark\tcandidate_name\ttail_number\tnote\n")
        for r in sorted(review, key=lambda r: ((r["model"] or ""), (r["variant"] or ""))):
            # Show the split this row WOULD get, so the decision is between
            # two named candidates rather than a judgement in the abstract.
            mark, name = split_mark_and_name((r["variant"] or "").strip())
            f.write("\t".join(str(r.get(k) or "") for k in
                    ("_id", "manufacturer", "model", "variant", "model_name"))
                    + f"\t{mark}\t{name}\t"
                    + "\t".join(str(r.get(k) or "") for k in ("tail_number", "note"))
                    + "\n")

    lines = [f"{len(aircraft):,} airframes examined", ""]
    for cls, label in (("C", "whitespace"),
                       ("B", "variant repeated the model"),
                       ("D", "variant duplicated model_name"),
                       ("A+", "name already in model_name"),
                       ("E", "name moved out to model_name")):
        lines.append(f"  {cls:3s} {counts[cls]:6,}  {label}")
    lines += ["", f"  plan   {len(plan):6,}  mechanical, ready to apply",
              f"  A      {len(review):6,}  needs a person -> variant_review.tsv",
              f"  ok     {counts['leave alone']:6,}  left alone"]
    summary = "\n".join(lines)
    (args.out_dir / "variant_summary.txt").write_text(summary + "\n", encoding="utf-8")
    print(summary)
    print(f"\nwrote {args.out_dir/'variant_plan.json'} and {args.out_dir/'variant_review.tsv'}")


if __name__ == "__main__":
    main()
