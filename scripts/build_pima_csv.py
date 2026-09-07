#!/usr/bin/env python3
"""Turn parse_pima_feed.py output into an importable aircraft CSV.

METHODOLOGY.md step 2: "Clean locally, never trust the source raw." The feed
is authoritative about *which airframes are there* and *what their serials
are*; it says nothing about the enum fields our schema requires, and its
manufacturer strings are inconsistently cased ("Sikorsky", "SIKORSKY",
"SIKORKSY").

WHICH FIELD BECOMES tail_number
-------------------------------
Pima's "Serial Number" column means two different things depending on the
airframe. On a military type it is the military serial — 61-0086, 149289,
XZ396 — which is the canonical identity of that airframe and what is painted
on it. On a civil type it is the manufacturer's construction number — DC1,
442, 1G211-41 — which is stamped on a plate, not displayed, and is not what
anyone would look up.

So: a serial that *looks* military wins; otherwise the registration wins; a
construction number is only used when there is nothing else, and then it goes
in aliases too so it stays searchable. Everything not chosen goes to aliases
rather than being discarded.

WHAT THIS SCRIPT WILL NOT DO
----------------------------
It never invents a year_built. Pima does not publish build years, and a year
derived from "this mark entered service in 1943" is a guess about a specific
airframe. METHODOLOGY.md: an empty field is always better than a guess.

Usage:
    python3 scripts/build_pima_csv.py --in /tmp/pima_nz.jsonl \\
        --out data/arizona/pima_topup_n_to_z_aircraft.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

MUSEUM = "Pima Air & Space Museum"

HEADER = ["manufacturer", "model", "variant", "tail_number", "model_name",
          "aircraft_name", "aircraft_type", "wing_type", "military_civilian",
          "role_type", "year_built", "description", "aliases",
          "museum_name", "display_status"]

# The museum's own strings, normalised. Keys are lowercased source values.
# Includes two misspellings on their side (SIKORKSY, Schemmp-Hirth, Rhurstahl).
MANUFACTURER = {
    "sikorksy": "Sikorsky", "sikorsky": "Sikorsky",
    "shorts": "Short Brothers", "short": "Short Brothers",
    "schemmp-hirth": "Schempp-Hirth", "schempp-hirth": "Schempp-Hirth",
    "rhurstahl": "Ruhrstahl",
    "sopwith": "Sopwith", "starr": "Starr", "steen": "Steen",
    "taylorcraft": "Taylorcraft", "taylorcraft bc-12d": "Taylorcraft",
    "teledyne": "Teledyne Ryan", "vought": "Vought", "waco": "Waco",
    "pitts": "Pitts", "saab": "Saab", "scheibe": "Scheibe",
    "naval aircraft factory": "Naval Aircraft Factory",
    "radioplane/northrop": "Radioplane", "ryan/temco": "Ryan",
    "pzl mielec": "PZL Mielec", "tl-ultralight": "TL-Ultralight",
    "u.s. navy": "United States Navy", "wright brothers": "Wright Brothers",
    "sud aviation": "Sud Aviation", "rotary air force": "Rotary Air Force",
    "pacific airwave": "Pacific Airwave", "north american": "North American",
    "yokosuka": "Yokosuka", "nakajima": "Nakajima", "vickers": "Vickers",
    "supermarine": "Supermarine", "westland": "Westland", "vultee": "Vultee",
    "stinson": "Stinson", "snow": "Snow", "shenyang": "Shenyang",
    "schweizer": "Schweizer", "sepecat": "SEPECAT", "rutan": "Rutan",
    "republic": "Republic", "ryan": "Ryan", "piper": "Piper",
    "piasecki": "Piasecki", "pereira": "Pereira", "pentecost": "Pentecost",
    "panavia": "Panavia", "northrop": "Northrop", "thiokol": "Thiokol",
    "trautmann": "Trautmann", "radioplane": "Radioplane",
}

# Designation prefix -> role. US tri-service designators are systematic, so a
# table beats guessing per airframe. Longest prefix wins.
ROLE_BY_PREFIX = [
    ("AGM", "air_to_surface"), ("ASM", "air_to_surface"), ("BGM", "cruise"),
    ("AQM", "drone"), ("MQM", "drone"), ("OQ", "drone"), ("PGM", "ballistic"),
    ("RF-", "recon"), ("RA-", "recon"), ("DF-", "utility"),
    ("VH-", "transport"), ("VC-", "transport"), ("KC-", "tanker"),
    ("CT-", "transport"), ("HH-", "search_rescue"), ("MH-", "utility"),
    ("SH-", "utility"), ("UH-", "utility"), ("CH-", "transport"),
    ("HO", "utility"), ("HUP", "utility"), ("TG-", "trainer"),
    ("YC-", "transport"), ("OV-", "recon"),
    ("A-", "ground_attack"), ("B-", "bomber"), ("C-", "transport"),
    ("F-", "fighter"), ("FJ", "fighter"), ("T-", "trainer"),
    ("U-", "utility"), ("L-", "utility"), ("P-", "fighter"),
    ("X-", "experimental"), ("BT", "trainer"), ("PT", "trainer"),
    ("N3N", "trainer"), ("SE-", "commercial_transport"),
]


# Rotary-wing designators and names.
ROTARY_HINT = re.compile(
    r"^(CH-|UH-|HH-|MH-|SH-|VH-|OH-|AH-|TH-|H-\d|HO|HUP|S-5[0-9]|RAF 2000)",
    re.I)
ROTARY_WORDS = re.compile(
    r"helicopter|autogiro|autogyro|gyroplane|hoppicopter|rotor", re.I)

GLIDER = re.compile(r"^(TG-|SHK|IIIB|SGS|Schweizer TG)", re.I)

# Types we know are biplanes. Keyed on (manufacturer, MODEL) — i.e. after the
# variant has been split off — because "S-1C" never matches once the row says
# model="S-1", variant="C". Two entries were dead for exactly that reason and
# shipped the most recognisable aerobatic biplane in the world as a monoplane.
BIPLANE = {
    ("Naval Aircraft Factory", "N3N"), ("Pitts", "S-1"),
    ("Waco", "RNF"), ("Waco", "UPF-7"), ("Waco", "ZKS-6"),
    ("Steen", "Skybolt"), ("Sopwith", "Camel"), ("Wright Brothers", "Flyer"),
    ("Stearman", "PT-17"),
    # The An-2 is a biplane, and a very large one — the type's defining feature.
    ("PZL Mielec", "AN-2"),
}

# Serial shapes that mean "this is a military airframe serial", not a
# manufacturer's construction number.
MIL_SERIAL = re.compile(r"""
      ^\d{2}-\d{3,5}$          # USAF 61-0086, 48-636
    | ^\d{5,6}$                # USN BuNo 149289, 97142
    | ^[A-Z]{2}\d{3,4}$        # RAF XZ396, MT847, ZF513
    | ^\d{2}-\d{5}$
""", re.X)

CIVIL_REG = re.compile(r"^(N[0-9]|NC[0-9]|CF-|C-[FG]|G-|D-|CCCP-|HR-|XB-)", re.I)


def norm_manufacturer(m: str) -> str:
    key = m.strip().lower()
    if key in MANUFACTURER:
        return MANUFACTURER[key]
    # Title-case an all-caps or all-lower source value, keep mixed case as-is.
    if m.isupper() or m.islower():
        return " ".join(w.capitalize() for w in m.split())
    return m.strip()


# Records the automatic split gets wrong, or cannot reach. Keyed on the
# museum's own designation string, lowercased. Each entry is a judgment call
# and is listed in data/arizona/ARIZONA_NOTES.md.
#
# Three kinds of problem live here:
#   * type names the museum puts in the designation field ("Jaguar GR3A" is
#     recorded as designation "GR3A", so the type name is lost entirely)
#   * source typos ("P51D" for P-51D, "SIKORKSY", "Schemmp-Hirth")
#   * families where the model is the name, not the mark — a Westland "AH.1"
#     is a Lynx AH.1, and filing it under model "AH.1" would put three Lynxes
#     under three different models.
FIX = {
    "ki-43-iib":    dict(model="Ki-43", variant="IIb", model_name="Hayabusa",
                         role_type="fighter"),
    "tornado ids":  dict(model="Tornado", variant="IDS",
                         role_type="ground_attack"),
    "spitfire":     dict(model="Spitfire", variant="", role_type="fighter"),
    "iiib":         dict(model="Bergfalke", variant="IIIB",
                         military_civilian="civilian", role_type="other"),
    # The museum's Registration field for this airframe contains the string
    # "BC-12D" — its own model, not a registration. Using it would create a
    # tail number that identifies nothing. The construction number is real, so
    # it goes to aliases and the tail stays blank.
    "bc-12d":       dict(model="BC-12", variant="D", tail_number="",
                         military_civilian="civilian", role_type="private"),
    "n3n-3":        dict(model="N3N", variant="3", wing_type="biplane",
                         military_civilian="military", role_type="trainer"),
    "p51d":         dict(model="P-51", variant="D", role_type="fighter"),
    "na64":         dict(model="NA-64", variant="", model_name="Yale",
                         role_type="trainer", military_civilian="military"),
    "model 89":     dict(model="Model 89", variant="", role_type="private",
                         military_civilian="civilian"),
    "sd 1400 x":    dict(model="SD 1400", variant="X",
                         aircraft_type="missile_rocket",
                         role_type="air_to_surface"),
    "raf 2000 gtx": dict(model="RAF 2000", variant="GTX",
                         aircraft_type="rotary_wing", role_type="private",
                         military_civilian="civilian"),
    "model 32 variviggen sp": dict(model="Model 32", variant="SP",
                                   model_name="VariViggen",
                                   military_civilian="civilian",
                                   role_type="experimental"),
    "model 61":     dict(model="Model 61", variant="", model_name="Long-EZ",
                         military_civilian="civilian",
                         role_type="experimental"),
    "quickie":      dict(model="Quickie", variant="",
                         military_civilian="civilian",
                         role_type="experimental"),
    "rf-35xd":      dict(model="RF-35", variant="XD", model_name="Draken",
                         military_civilian="military", role_type="recon"),
    "gr3a":         dict(model="Jaguar", variant="GR3A",
                         role_type="ground_attack"),
    "t4":           dict(model="Jaguar", variant="T4", role_type="trainer"),
    "j-6a":         dict(model="J-6", variant="A", role_type="fighter"),
    "t1 tucano":    dict(model="Tucano", variant="T1", role_type="trainer"),
    "c-23b+ sherpa": dict(model="C-23", variant="B+", model_name="Sherpa",
                          role_type="transport"),
    "ho3s-1g":      dict(model="HO3S", variant="1G",
                         aircraft_type="rotary_wing", role_type="utility",
                         military_civilian="military"),
    "camel f.1":    dict(model="Camel", variant="F.1", wing_type="biplane",
                         role_type="fighter"),
    "bumble bee":   dict(model="Bumble Bee", variant="",
                         military_civilian="civilian",
                         role_type="experimental"),
    "skybolt":      dict(model="Skybolt", variant="", wing_type="biplane",
                         military_civilian="civilian", role_type="private"),
    "f4u-4":        dict(model="F4U", variant="4", model_name="Corsair",
                         role_type="fighter"),
    "aqm-34l firebee": dict(model="AQM-34", variant="L", model_name="Firebee",
                            role_type="drone"),
    "l-2m grasshopper": dict(model="L-2", variant="M",
                             model_name="Grasshopper", role_type="utility"),
    "an-2r colt":   dict(model="AN-2", variant="R", model_name="Colt",
                         military_civilian="civilian", role_type="utility",
                         wing_type="biplane"),
    # The F-105G is the Wild Weasel SAM-suppression conversion, not a fighter.
    # NMUSAF's F-105G is filed as electronic_warfare; these should agree.
    "f-105g":       dict(model="F-105", variant="G",
                         role_type="electronic_warfare"),
    # The PA-48 Enforcer was a turboprop COIN demonstrator built for USAF
    # evaluation. It carries a civil registration but was never a private
    # aircraft, and the ROLE_BY_PREFIX table has no way to know that.
    "pa-48":        dict(model="PA-48", variant="", model_name="Enforcer",
                         military_civilian="civilian", role_type="experimental"),
    # The F-84F served in both roles; NMUSAF's is ground_attack, so match it.
    "f-84f":        dict(model="F-84", variant="F", model_name="Thunderstreak",
                         role_type="ground_attack"),
    "744":          dict(model="Viscount", variant="744",
                         military_civilian="civilian",
                         role_type="commercial_transport"),
    "se-210":       dict(model="SE-210", variant="", model_name="Caravelle",
                         military_civilian="civilian",
                         role_type="commercial_transport"),
    "lysander mk.iii": dict(model="Lysander", variant="Mk.III",
                            role_type="utility"),
    "mxy7 ohka":    dict(model="MXY7", variant="", model_name="Ohka",
                         aircraft_type="missile_rocket",
                         role_type="air_to_surface"),
    "ki-115":       dict(model="Ki-115", variant="", model_name="Tsurugi",
                         role_type="ground_attack"),
    "osprey 2":     dict(model="Osprey", variant="2",
                         military_civilian="civilian",
                         role_type="experimental"),
    "e-iii":        dict(model="E-III", variant="", model_name="Hoppicopter",
                         aircraft_type="rotary_wing",
                         military_civilian="civilian",
                         role_type="experimental"),
    "d-16a":        dict(model="D-16", variant="A", model_name="Twin Navion",
                         military_civilian="civilian", role_type="private"),
    "shk-1":        dict(model="SHK", variant="1", military_civilian="civilian",
                         role_type="other"),
    "tg-3a":        dict(model="TG-3", variant="A", role_type="trainer"),
    "s-2a":         dict(model="S-2", variant="A", model_name="Thrush",
                         military_civilian="civilian", role_type="utility"),
    "roadair":      dict(model="RoadAir", variant="",
                         military_civilian="civilian",
                         role_type="experimental"),
    "asm-n-2":      dict(model="ASM-N-2", variant="", model_name="Bat",
                         aircraft_type="missile_rocket",
                         role_type="air_to_surface"),
    "s-43":         dict(model="S-43", variant="", model_name="Baby Clipper",
                         military_civilian="civilian",
                         role_type="commercial_transport"),
    "hup-3":        dict(model="HUP", variant="3", aircraft_type="rotary_wing",
                         model_name="Retriever", role_type="utility"),
    "h-5g":         dict(model="H-5", variant="G", aircraft_type="rotary_wing",
                         role_type="search_rescue"),
    # The three Westland Lynxes. Filing them under models AH.1 / AH.7 / HMA.8
    # would scatter one type across three models.
    "ah.1":         dict(model="Lynx", variant="AH.1",
                         aircraft_type="rotary_wing", role_type="utility"),
    "ah.7":         dict(model="Lynx", variant="AH.7",
                         aircraft_type="rotary_wing", role_type="utility"),
    "hma.8":        dict(model="Lynx", variant="HMA.8",
                         aircraft_type="rotary_wing", role_type="utility"),
}

# Three records publish no Designation field at all, so they are keyed on the
# museum's title instead. Anything else with a blank designation is reported
# rather than guessed at.
TITLE_FIX = {
    "thiokol space shuttle solid rocket booster": dict(
        model="Space Shuttle SRB", variant="", aircraft_type="missile_rocket",
        military_civilian="civilian", role_type="space", wing_type=""),
    "tl-ultralight stream": dict(
        model="Stream", variant="", aircraft_type="fixed_wing",
        military_civilian="civilian", role_type="private"),
    "wright 1903 flyer": dict(
        model="Flyer", variant="", model_name="Wright Flyer",
        aircraft_type="fixed_wing", wing_type="biplane",
        military_civilian="civilian", role_type="experimental"),
}

# Modern tri-service: LETTERS-NUMBER + optional variant. F-105G, UH-60MU,
# X-15A-2, OQ-19D.
MODERN = re.compile(r"^([A-Za-z]{1,4}-\d+)([A-Za-z][A-Za-z0-9+.\-]*)?$")
# US Navy pre-1962: F4U-4, N3N-3, HO3S-1G, HUP-3 — the number is the variant.
NAVY = re.compile(r"^([A-Za-z]{1,2}\d?[A-Za-z]{0,2})-(\d+[A-Za-z]*)$")
# Japanese/other: Ki-43-IIb
DASHED = re.compile(r"^([A-Za-z]{1,3}-\d+)-([A-Za-z0-9]+)$")


def split_model_variant(designation: str):
    """'F-105G' -> ('F-105', 'G'); 'F4U-4' -> ('F4U', '4').

    The generated full_designation column is built from model + variant and
    the unique index is (model, tail_number), so putting a whole designation
    in `model` silently defeats both — and filing every mark of one type under
    a different model scatters the type across the site.
    """
    d = " ".join(designation.split())
    if not d:
        return "", ""
    for rx in (DASHED, MODERN):
        m = rx.match(d)
        if m:
            return m.group(1), (m.group(2) or "")
    m = NAVY.match(d)
    if m:
        return m.group(1), m.group(2)
    return d, ""


def classify_type(man, model, designation, title):
    blob = f"{designation} {title}"
    if ROTARY_HINT.match(designation) or ROTARY_WORDS.search(blob):
        return "rotary_wing"
    if re.match(r"^(AGM|ASM|BGM|PGM|SD |MXY|XM\d)", designation, re.I):
        return "missile_rocket"
    return "fixed_wing"


def classify_role(designation):
    d = designation.upper()
    for pre, role in ROLE_BY_PREFIX:
        if d.startswith(pre.upper()):
            return role
    return ""


def pick_tail(rec, civilian=False):
    """Return (tail_number, aliases[]). Never discards a candidate.

    ``civilian`` flips the preference. A civil homebuilt's "Serial Number" is
    the builder's number, and some of those look exactly like a Navy BuNo —
    the Steen Skybolt's is 134310 — so on a civil airframe the registration
    wins outright and the serial becomes an alias.
    """
    serial = (rec.get("serial") or "").strip()
    reg = (rec.get("registration") or "").strip()
    extras = list(rec.get("other_registrations") or [])

    # "147595 (51-16608)" — the museum giving both service serials.
    paren = re.match(r"^(\S+)\s*\((.+)\)$", serial)
    if paren:
        serial, alt = paren.group(1), paren.group(2).strip()
        extras.append(alt)

    # "CF-TGI / N22SN"
    if "/" in reg:
        bits = [b.strip() for b in reg.split("/") if b.strip()]
        reg, extras = bits[0], extras + bits[1:]

    # Two serials means the record covers two airframes, or the museum is
    # unsure which one this is. Refuse to pick — leave the tail blank and put
    # both in aliases so a human can resolve it.
    if re.search(r"\b(AND|OR)\b", serial, re.I):
        return "", extras + [s for s in re.split(r"\s+(?:AND|OR)\s+", serial,
                                                 flags=re.I) if s]

    if civilian and reg:
        return reg, ([serial] if serial else []) + extras
    if serial and MIL_SERIAL.match(serial):
        return serial, ([reg] if reg else []) + extras
    if reg:
        return reg, ([serial] if serial else []) + extras
    return serial, extras


def build(rec):
    man = norm_manufacturer(rec["manufacturer"])
    designation = rec["designation"].strip()
    fix = dict(FIX.get(designation.lower(), {}))

    if not designation:
        fix = dict(TITLE_FIX.get(rec["title"].strip().lower(), {}))
        if not fix:
            return None, (f"{rec['title']}: no designation and no TITLE_FIX "
                          f"entry — add one rather than guessing")

    model = fix.get("model") or split_model_variant(designation)[0]
    variant = fix.get("variant", split_model_variant(designation)[1])
    if not model:
        return None, f"{rec['title']}: could not determine a model"

    mil_civ = fix.get("military_civilian")
    ac_type = fix.get("aircraft_type") or classify_type(
        man, model, designation, rec["title"])
    role = fix.get("role_type") or classify_role(designation)

    # Decide military/civilian before choosing the tail, because the choice
    # of tail depends on it (see pick_tail).
    if not mil_civ:
        reg = (rec.get("registration") or "")
        ser = (rec.get("serial") or "")
        mil_civ = ("civilian" if CIVIL_REG.match(reg) and
                   not MIL_SERIAL.match(ser) else "military")
    tail, aliases = pick_tail(rec, civilian=(mil_civ == "civilian"))

    # A quoted serial is a painted marking on a replica, not an identity.
    # Keep it visible in aliases, but never as the tail number.
    if rec.get("serial_is_marking") and tail:
        aliases = [f"marked {tail}"] + aliases
        tail = ""

    if "tail_number" in fix:                      # an explicit override wins
        forced = fix["tail_number"]
        if tail and tail != forced:
            aliases = aliases + [tail]
        tail = forced

    if not role and mil_civ == "civilian":
        role = "private"

    wing = fix.get("wing_type")
    if wing is None:
        wing = "biplane" if (man, model) in BIPLANE else "monoplane"
    if ac_type != "fixed_wing":
        wing = ""

    return {
        "manufacturer": man, "model": model, "variant": variant,
        "tail_number": tail, "model_name": fix.get("model_name", ""),
        "aircraft_name": rec.get("nickname", ""),
        "aircraft_type": ac_type, "wing_type": wing,
        "military_civilian": mil_civ, "role_type": role or "other",
        "year_built": "",
        # Worth stating plainly: a visitor deciding whether to drive to Tucson
        # to see an X-15 should know Pima's is a mockup.
        "description": "Replica or full-scale mockup, not an original airframe."
                       if rec.get("is_replica") else "",
        "aliases": ";".join(dict.fromkeys(a for a in aliases if a)),
        "museum_name": MUSEUM,
        # The museum states this itself; see STATUS_SENTENCE in the parser.
        "display_status": rec.get("display_status") or "on_display",
    }, None


def _assert_no_duplicate_keys(path: str) -> None:
    """Fail loudly if FIX or TITLE_FIX defines a key twice.

    A dict literal accepts duplicate keys silently and the last one wins, so a
    correction added at the top of the table can be quietly overridden by a
    stale entry further down — which is what turned the Scheibe's variant back
    from IIIB to III after it had been fixed. The tables are long enough that
    this needs to be an error, not a code-review hope.
    """
    src = Path(path).read_text(encoding="utf-8")
    for table in ("FIX", "TITLE_FIX"):
        m = re.search(rf"^{table} = \{{$(.*?)^\}}$", src, re.S | re.M)
        if not m:
            continue
        keys = re.findall(r'^\s{4}"([^"]*)":', m.group(1), re.M)
        dupes = {k for k in keys if keys.count(k) > 1}
        if dupes:
            raise SystemExit(
                f"error: {table} defines these keys more than once: "
                f"{sorted(dupes)} — the later entry silently wins, so merge them.")


def main():
    _assert_no_duplicate_keys(__file__)
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="src", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()

    rows, skipped = [], []
    for line in open(args.src, encoding="utf-8"):
        rec = json.loads(line)
        row, err = build(rec)
        (rows.append(row) if row else skipped.append(err))

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {args.out}: {len(rows)} rows", file=sys.stderr)
    tails = sum(1 for r in rows if r["tail_number"])
    print(f"  {tails}/{len(rows)} with a tail number "
          f"({tails * 100 // max(len(rows), 1)}%)", file=sys.stderr)
    if skipped:
        print(f"  {len(skipped)} skipped:", file=sys.stderr)
        for s in skipped:
            print(f"      {s}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
