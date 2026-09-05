#!/usr/bin/env python3
"""Fill wing_type on generated aircraft CSVs.

wing_type only describes fixed-wing aircraft; helicopters, missiles and
spacecraft must leave it empty. Almost everything built after ~1935 is a
monoplane, so the honest approach is: enumerate the biplanes and triplanes
explicitly, default the rest of the fixed-wing rows to monoplane, and blank
everything else.

Keyed on (manufacturer, model) rather than model alone, because model
designations collide across manufacturers — a Pitts S-2 is a biplane while
a Grumman S-2 Tracker is a monoplane, and getting that backwards would be
a silent data error.

Usage:
    python3 scripts/fix_wing_type.py data/california/*.csv
    python3 scripts/fix_wing_type.py --dry-run data/california/foo.csv
"""
import csv, sys, os

# (manufacturer_substring, model) — manufacturer matched loosely so
# "Curtiss" also catches "Curtiss-Wright".
BIPLANE = {
    ("curtiss","jn-4"), ("curtiss","jns"), ("curtiss","model d"), ("curtiss","r3c"),
    ("dayton-wright","j-1"), ("thomas-morse","s-4"),
    ("wright","flyer"), ("american eagle","a-1"), ("beech","uc-43"), ("beech","d17"),
    ("brunner-winkle","bird"), ("command-aire","3-c-3"), ("fleet","7"), ("fleet","2"),
    ("great lakes","2t-1"), ("oldfield","baby great lakes"), ("kreider-reisner","kr-31"),
    ("de havilland","dh-60"), ("naval aircraft factory","n3n"), ("stearman","4"),
    ("stearman","pt-9"), ("stearman","pt-17"), ("swallow","tp"), ("travel air","2000"),
    ("waco","uec"), ("waco","gxe"), ("waco","yks-7"), ("lincoln-page","lp-3"),
    ("thomas-pigeon","flying boat"), ("boeing","fb"), ("boeing","p-12"),
    ("sopwith","pup"), ("nieuport","17"), ("hanriot","hd.1"), ("pitts","s-2"),
    ("pitts","s-1"), ("wright","ex"), ("wright","model d"),
    ("grumman","g-32"), ("bristol","f.2b"),
}
TRIPLANE = {("fokker","dr.1")}

def classify(mfr, model, actype, current):
    if actype != "fixed_wing":
        return ""                      # helicopters/missiles have no wing_type
    m, mo = mfr.strip().lower(), model.strip().lower()
    # Never downgrade a value the source explicitly supplied. A researcher
    # who wrote "biplane" looked at the aircraft; this table is a fallback,
    # not an authority, and it once turned a Wright EX into a monoplane.
    if current in ("biplane", "triplane"):
        return current
    for (bm, bmo) in TRIPLANE:
        if bm in m and mo == bmo:
            return "triplane"
    for (bm, bmo) in BIPLANE:
        if bm in m and mo == bmo:
            return "biplane"
    return "monoplane"

def process(path, dry=False):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    if not rows or "wing_type" not in rows[0]:
        print(f"  {path}: no wing_type column, skipped"); return
    changes = {"biplane":0, "triplane":0, "monoplane":0, "cleared":0}
    for r in rows:
        new = classify(r["manufacturer"], r["model"], r["aircraft_type"], r["wing_type"])
        if new != r["wing_type"]:
            changes["cleared" if new == "" else new] += 1
            r["wing_type"] = new
    if not dry:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    tally = ", ".join(f"{k}={v}" for k, v in changes.items() if v)
    print(f"  {os.path.basename(path):<46} {len(rows):>4} rows  {tally or 'no change'}")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    print("DRY RUN" if dry else "Applying wing_type:")
    for p in args:
        process(p, dry)
