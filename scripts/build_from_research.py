#!/usr/bin/env python3
"""Turn pipe-delimited research output into an importable aircraft CSV.

METHODOLOGY.md step 2: "Clean locally, never trust the agent output raw."

THE FIELD-COUNT PROBLEM
-----------------------
Research passes are told to emit exactly 14 pipe-separated fields. In practice
a few lines per batch come back with 11, 12 or 14 — a field dropped, or an
extra pipe inside a note. Importing those blind shifts every value one column
left and writes `monoplane` into military_civilian, which the validator
rejects for the whole file (the importer is atomic).

Counting pipes cannot fix it, because you cannot tell *which* field went
missing. But three of the columns draw from small controlled vocabularies —
aircraft_type, military_civilian, display_status — so their positions can be
found by value rather than by index, and the rest realigned around them. A
line whose anchors cannot be located is reported, never guessed at.

DESCRIPTION VS ALIASES
----------------------
The contract's last two data fields are description then aliases. Before the
14-field contract everything after year_built was treated as aliases, which is
how research prose ended up in the search-indexed aliases table and had to be
migrated back out in September 2026. _split_desc_aliases keeps them apart.

WHAT IT WILL NOT DO
-------------------
Invent a tail number or a year. Rows arrive with those blank on purpose.

Usage:
    python3 scripts/build_from_research.py --in raw.txt \\
        --museum "National Museum of the United States Air Force" \\
        --out data/ohio/nmusaf_topup_m_to_z_aircraft.csv
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

HEADER = ["manufacturer", "model", "variant", "tail_number", "model_name",
          "aircraft_name", "aircraft_type", "wing_type", "military_civilian",
          "role_type", "year_built", "description", "aliases",
          "museum_name", "display_status"]

AIRCRAFT_TYPES = {"fixed_wing", "rotary_wing", "lighter_than_air",
                  "spacecraft", "missile_rocket"}
WING_TYPES = {"monoplane", "biplane", "triplane"}
MIL_CIV = {"military", "civilian"}
STATUSES = {"on_display", "in_storage", "under_restoration"}
ROLES = {
    "fighter", "bomber", "transport", "trainer", "recon", "ground_attack",
    "utility", "experimental", "test", "tanker", "drone", "electronic_warfare",
    "search_rescue", "commercial_transport", "private", "freighter", "space",
    "air_to_air", "air_to_surface", "ballistic", "cruise", "sounding", "other",
}

# Left of aircraft_type the contract has six fields.
LEFT = ["manufacturer", "model", "variant", "tail_number", "model_name",
        "aircraft_name"]


_DIGITS = "0123456789"


def join_designation(model, variant):
    """Join model and variant the way the DB's generated column does."""
    model = (model or "").strip()
    variant = (variant or "").strip()
    if not variant:
        return model
    if variant[0] in _DIGITS:
        return f"{model}-{variant}"
    if model and model[-1] in _DIGITS:
        return f"{model}{variant}"
    return f"{model} {variant}"


_DESIG = re.compile(r"^([A-Za-z]{1,4})-(\d{1,3}[A-Za-z]{0,3})$")


def dashless(s):
    """PT-22 -> PT22. Returns None if the string is not a designation."""
    m = _DESIG.match((s or "").strip())
    if not m:
        return None
    v = m.group(1) + m.group(2)
    return v if v != s.strip() else None


def _split_desc_aliases(tail):
    """Map the fields after year_built onto (description, aliases).

    A well-formed 14-field line leaves exactly two: description then aliases.
    One field means the research dropped one — an aliases list is short and
    semicolon-separated, a description is prose, so length decides. More than
    two means an unescaped pipe inside the description, so everything but the
    last field folds back into it.
    """
    tail = [t.strip() for t in tail]
    if not tail:
        return "", ""
    if len(tail) == 1:
        one = tail[0]
        if ";" in one or len(one.split()) <= 6:
            return "", one
        return one, ""
    return " ".join(t for t in tail[:-1] if t), tail[-1]


def realign(parts):
    """Map a split line onto the 13-field contract. Returns (row, problem)."""
    idx = next((i for i, p in enumerate(parts)
                if p.strip().lower() in AIRCRAFT_TYPES), None)
    if idx is None:
        return None, "no aircraft_type value found"

    left = [p.strip() for p in parts[:idx]]
    if len(left) < len(LEFT):
        # Fields were dropped somewhere on the left and we cannot tell which.
        # Manufacturer and model are the two that must be right, and they are
        # always first, so pad on the RIGHT — the trailing name fields are
        # optional and blank is honest.
        left = left + [""] * (len(LEFT) - len(left))
    elif len(left) > len(LEFT):
        # An extra pipe inside a name. Fold the surplus into aircraft_name.
        left = left[:len(LEFT) - 1] + [" ".join(left[len(LEFT) - 1:])]
    row = dict(zip(LEFT, left))
    row["aircraft_type"] = parts[idx].strip().lower()

    rest = [p.strip() for p in parts[idx + 1:]]
    if not rest:
        return None, "nothing after aircraft_type"

    # display_status is the last field, but may be missing entirely.
    if rest and rest[-1].lower() in STATUSES:
        row["display_status"] = rest[-1].lower()
        rest = rest[:-1]
    else:
        row["display_status"] = "on_display"

    mi = next((i for i, p in enumerate(rest) if p.lower() in MIL_CIV), None)
    if mi is None:
        return None, "no military_civilian value found"
    wing = [p for p in rest[:mi] if p.lower() in WING_TYPES]
    row["wing_type"] = wing[0].lower() if wing else ""
    row["military_civilian"] = rest[mi].lower()

    tail = rest[mi + 1:]
    row["role_type"] = (tail[0].lower()
                        if tail and tail[0].lower() in ROLES else "")
    if row["role_type"]:
        tail = tail[1:]
    # The year_built slot is always consumed, whatever is sitting in it, so
    # that a blank year cannot shift the description/aliases split that
    # follows. A real year is kept; anything else there is prose, which is
    # moved to the front of the description rather than dropped or aliased.
    row["year_built"] = ""
    stray_year_prose = ""
    if tail:
        head, tail = tail[0], tail[1:]
        if re.fullmatch(r"(1[89]|20)\d{2}", head):
            row["year_built"] = head
        elif head:
            stray_year_prose = head
    # The contract's last two data fields are description then aliases.
    # Before the 14-field contract everything here was aliases, which is how
    # prose ended up in the search-indexed aliases table (see the September
    # 2026 alias migration). Split them.
    row["description"], alias_src = _split_desc_aliases(tail)
    if stray_year_prose:
        row["description"] = (stray_year_prose + " " + row["description"]).strip()
    row["aliases"] = ";".join(
        a.strip() for a in alias_src.split(";") if a.strip())
    return row, None


def sanitise(row, museum):
    """Enforce the schema's rules regardless of what the research said."""
    problems = []
    row.setdefault("description", "")
    row["museum_name"] = museum

    # Folding surplus fields with " ".join produces a lone space when the
    # surplus fields were all empty, which then imports as a one-character
    # aircraft_name. Strip everything once, here, rather than per-field.
    for k, v in list(row.items()):
        if isinstance(v, str):
            row[k] = v.strip()

    # Tail numbers arrive with prefixes: "BuNo 140048", "S/N 43-3374".
    t = row.get("tail_number", "").strip()
    t = re.sub(r"^(BuNo|Bu\.?No\.?|S/?N|Serial|Ser\.?)\s*[:.]?\s*", "", t, flags=re.I)
    row["tail_number"] = t.strip()

    if row["aircraft_type"] != "fixed_wing":
        # A helicopter with wing_type set is a data error, and the schema will
        # happily store it — so it has to be caught here.
        row["wing_type"] = ""
    elif not row["wing_type"]:
        row["wing_type"] = "monoplane"

    if row["military_civilian"] not in MIL_CIV:
        row["military_civilian"] = "military"
    if row["role_type"] not in ROLES:
        row["role_type"] = "other"
    if row["display_status"] not in STATUSES:
        row["display_status"] = "on_display"

    # Dashless designation variants as aliases: a visitor searching "PT22"
    # must find the PT-22. Established September 2026; every imported state
    # from Ohio onward carries these.
    al = [a.strip() for a in row.get("aliases", "").split(";") if a.strip()]
    low = {a.lower() for a in al}
    for src in [row.get("model", ""),
                join_designation(row.get("model"), row.get("variant"))] + list(al):
        d = dashless(src)
        if d and d.lower() not in low:
            al.append(d)
            low.add(d.lower())
    row["aliases"] = "; ".join(al)

    # A comma anywhere in these two would need CSV quoting the importer's
    # splitter does not expect; the research contract forbids them.
    for f in ("description", "aliases"):
        if "," in row.get(f, ""):
            problems.append(f"comma in {f} — the contract forbids it")

    if not row.get("manufacturer") or not row.get("model"):
        problems.append("missing manufacturer or model")
    # A serial filed as a year is the single most common research error.
    if row["year_built"] and not re.fullmatch(r"\d{4}", row["year_built"]):
        problems.append(f"year_built not a year: {row['year_built']!r}")
        row["year_built"] = ""
    return row, problems


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="src", required=True)
    p.add_argument("--museum", help="museum name for every row")
    p.add_argument("--out", help="output CSV (single-museum mode)")
    p.add_argument("--museum-in-last-field", action="store_true",
                   help="each line carries its museum as a 14th, final field; "
                        "write one <slug>_aircraft.csv per museum into --out-dir")
    p.add_argument("--out-dir", help="directory for per-museum files")
    args = p.parse_args()
    if args.museum_in_last_field:
        if not args.out_dir:
            p.error("--museum-in-last-field needs --out-dir")
    elif not (args.museum and args.out):
        p.error("need --museum and --out, or --museum-in-last-field --out-dir")

    rows, rejected, deduped = [], [], []
    seen_tail = {}
    for lineno, line in enumerate(Path(args.src).read_text(encoding="utf-8")
                                  .splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("---") or "|" not in line:
            continue
        # A pasted-in header row is not data.
        if line.lower().startswith("manufacturer|model|"):
            continue
        parts = line.split("|")
        # A region sweep with several small museums is easier to research as
        # one file. In that mode the museum rides along as a trailing field
        # and is peeled off here, so realign() sees the usual 14.
        museum = args.museum
        if args.museum_in_last_field:
            museum = parts.pop().strip()
            if not museum:
                rejected.append((lineno, "no museum in last field", line[:90]))
                continue
        row, problem = realign(parts)
        if problem:
            rejected.append((lineno, problem, line[:90]))
            continue
        row, problems = sanitise(row, museum)
        if problems:
            rejected.append((lineno, "; ".join(problems), line[:90]))
            continue

        # Cross-slice duplicates. Research is split by manufacturer initial,
        # which assumes every airframe has one canonical manufacturer — and
        # compound credits break that. A Vought/Chance Vought RF-8G lands in
        # both the A-L and M-Z passes; so do Lancair/Neibauer, Howard/Poberezny
        # and Boeing/Stearman. The tail number is the airframe's identity, so
        # it is what catches them.
        #
        # Keyed on (model, tail), which is the database's own unique index —
        # NOT on tail alone. A bare-tail key was fine while every tail was a
        # globally unique USAF serial, and then Monino arrived with painted
        # bort numbers ("01" on a MiG-9, a MiG-17, a Tu-4 and an An-14) and
        # Le Bourget with four different Dassault prototypes all numbered
        # "01". Keying on tail alone threw away 39 real aircraft.
        tail = row["tail_number"].strip().lower()
        if tail:
            key = (row["model"].strip().lower(), tail)
            if key in seen_tail:
                deduped.append((row, seen_tail[key]))
                continue
            seen_tail[key] = f"{row['manufacturer']} {row['model']}"
        rows.append({k: row.get(k, "") for k in HEADER})

    def write(path, subset):
        with open(path, "w", newline="", encoding="utf-8") as f:
            # lineterminator="\n": csv defaults to "\r\n", which would make every
            # generated file CRLF while every existing data/ file is LF - see
            # METHODOLOGY.md "If you rewrite existing CSVs programmatically".
            w = csv.DictWriter(f, fieldnames=HEADER, lineterminator="\n")
            w.writeheader()
            w.writerows(subset)
        tails = sum(1 for r in subset if r["tail_number"])
        print(f"wrote {path}: {len(subset)} rows, {tails} with a tail number "
              f"({tails * 100 // max(len(subset), 1)}%)", file=sys.stderr)

    if args.museum_in_last_field:
        # One file per museum, as everywhere else: the importer is atomic per
        # request, so a bad row can only ever take down its own museum.
        import unicodedata
        outdir = Path(args.out_dir); outdir.mkdir(parents=True, exist_ok=True)
        by_museum = {}
        for r in rows:
            by_museum.setdefault(r["museum_name"], []).append(r)
        for name, subset in by_museum.items():
            slug = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
            slug = re.sub(r"[^a-z0-9]+", "_", slug.lower()).strip("_")[:40]
            write(outdir / f"{slug}_aircraft.csv", subset)
    else:
        write(args.out, rows)
    if deduped:
        print(f"  dropped {len(deduped)} duplicate airframe(s) already seen "
              f"under another manufacturer credit:", file=sys.stderr)
        for row, first in deduped:
            print(f"      {row['manufacturer']} {row['model']} "
                  f"{row['tail_number']} — already had it as {first}",
                  file=sys.stderr)
    if rejected:
        print(f"REJECTED {len(rejected)} lines — fix by hand, do not guess:",
              file=sys.stderr)
        for ln, why, txt in rejected:
            print(f"   line {ln}: {why}\n      {txt}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
