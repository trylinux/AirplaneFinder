#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harvest the russianplanes.net monument database into build-ready CSVs.

WHY THIS IS A SCRIPT AND NOT A RESEARCH PASS
────────────────────────────────────────────
Every other region in this project was built by researching sites one at a
time, because no source covered them. Russia is the opposite problem: one
endpoint returns 9,657 preserved airframes with model, bort number,
construction number and coordinates already attached. Doing that by hand
would be worse, not better — it would introduce transcription error into
data that arrives clean.

What still needs judgement, and is therefore NOT automated here:
  · whether a given airframe is still there (the source's own `ex` category
    handles departures, which is more than most sources give us)
  · the operator country, which is asserted only where the registration
    itself carries it — see operator_country() below
  · anything in the long tail the type parser cannot resolve, which is
    dropped rather than guessed

    https://russianplanes.net/monument?action=mapGetPoints&mode=json

THE SOURCE'S FIELDS
    id  monument point id        t   type, in Cyrillic ("МиГ-21ПФМ")
    g   registration or bort     s   construction number
    la/lo  coordinates           p/f photo id and thumbnail path
    c   category                 re  the contributor's own note, in Russian

`c` is the important one. It is the source's answer to the project's
display-vs-derelict test, and it is why this dataset is usable at all:

    monument  6,773   plinthed or displayed          → import
    stored    1,181   held, not presented            → skip
    ex          763   departed this location         → skip, and useful:
                                                       it is a currency signal
                                                       no other region had
    parts       281   sections, not airframes        → skip
    (none)      659   uncategorised                  → skip

Only `monument` is taken. The others are recorded in the report so a later
pass can revisit `stored` and `parts` deliberately rather than by accident.

USAGE
    python3 harvest_russianplanes.py fetch      # download + cache the JSON
    python3 harvest_russianplanes.py geocode    # reverse-geocode site centroids
    python3 harvest_russianplanes.py build      # emit CSVs
    python3 harvest_russianplanes.py report     # print the scoping numbers

Each stage caches to disk and is safe to re-run; geocode resumes where it
left off. Nominatim is called at 1 request/second per its usage policy, with
a contact address in the User-Agent as that policy requires.
"""
import collections
import csv
import json
import math
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
SOURCE = "https://russianplanes.net/monument?action=mapGetPoints&mode=json"
UA_CONTACT = os.environ.get("NOMINATIM_CONTACT", "")
CLUSTER_M = 250          # two airframes closer than this are one site
KNOWN_SITE_M = 400       # closer than this to an existing museum = a top-up

# ── Cyrillic type strings ─────────────────────────────────────────────────
# "МиГ-21ПФМ" has to become Mikoyan-Gurevich / MiG-21 / PFM, and the
# transliteration has to be the aviation one rather than a generic GOST
# table: Х-22 is Kh-22 and never X-22, Ан-2Р is An-2R and never An-2P.
FAMILIES = {
    "Ми": ("Mil", "Mi"), "МиГ": ("Mikoyan-Gurevich", "MiG"),
    "Миг": ("Mikoyan-Gurevich", "MiG"), "Су": ("Sukhoi", "Su"),
    "Ту": ("Tupolev", "Tu"), "Ан": ("Antonov", "An"),
    "Ил": ("Ilyushin", "Il"), "Як": ("Yakovlev", "Yak"),
    "Ка": ("Kamov", "Ka"), "Бе": ("Beriev", "Be"),
    "По": ("Polikarpov", "Po"), "И": ("Polikarpov", "I"),
    "Ла": ("Lavochkin", "La"), "ЛаГГ": ("Lavochkin-Gorbunov-Gudkov", "LaGG"),
    "Пе": ("Petlyakov", "Pe"), "Ер": ("Yermolayev", "Yer"),
    "Ли": ("Lisunov", "Li"), "Ш": ("Shavrov", "Sh"),
    "М": ("Myasishchev", "M"), "Че": ("Chetverikov", "Che"),
    "Г": ("Gribovsky", "G"), "УТ": ("Yakovlev", "UT"),
}
CYR2LAT = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ж": "Zh",
    "З": "Z", "И": "I", "Й": "Y", "К": "K", "Л": "L", "М": "M", "Н": "N",
    "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F",
    "Х": "Kh", "Ц": "Ts", "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ы": "Y",
    "Э": "E", "Ю": "Yu", "Я": "Ya", "Ь": "", "Ъ": "",
}
CYR2LAT.update({k.lower(): v.lower() for k, v in CYR2LAT.items() if v})

# Types whose Latin name is not a transliteration of the Cyrillic one.
LITERAL = {
    "Л-29": ("Aero", "L-29", None, "Delfin"),
    "Л-39": ("Aero", "L-39", None, "Albatros"),
    "Л-410": ("LET", "L-410", None, "Turbolet"),
    "Л-410УВП": ("LET", "L-410", "UVP", "Turbolet"),
    "L-29": ("Aero", "L-29", None, "Delfin"),
    "L-39": ("Aero", "L-39", None, "Albatros"),
    "L-39C": ("Aero", "L-39", "C", "Albatros"),
    "L-39ZA": ("Aero", "L-39", "ZA", "Albatros"),
    "L-410": ("LET", "L-410", None, "Turbolet"),
    "Ан-2": ("Antonov", "An-2", None, "Colt"),
    "УТИ МиГ-15": ("Mikoyan-Gurevich", "MiG-15", "UTI", None),
    "J-6": ("Shenyang", "J-6", None, None),
    "J-5": ("Shenyang", "J-5", None, None),
    "Z-5": ("Harbin", "Z-5", None, None),
}
# Latin-script families whose manufacturer the string doesn't carry. The
# schema requires a manufacturer, so a type that resolves to no manufacturer
# is dropped, not imported with a blank.
LATIN_MFR = {
    "L-29": "Aero", "L-39": "Aero", "L-59": "Aero", "L-410": "LET",
    "L-200": "Morava", "L-13": "LET", "Z-37": "Zlin", "Z-42": "Zlin",
    "Z-43": "Zlin", "Z-142": "Zlin", "Z-5": "Harbin", "J-5": "Shenyang",
    "J-6": "Shenyang", "J-7": "Chengdu", "TS-11": "PZL Mielec",
    "TS-8": "PZL", "Lim-2": "PZL", "Lim-5": "PZL", "SBLim-2": "PZL",
    "An-2": "Antonov", "Su-7": "Sukhoi", "H-5": "Harbin", "Y-5": "Nanchang",
    "Q-5": "Nanchang", "F-6": "Shenyang",
}
MISSILES = {
    "С-75": ("Almaz", "S-75", None, "Dvina"),
    "С-125": ("Almaz", "S-125", None, "Neva"),
    "С-200": ("Almaz", "S-200", None, "Angara"),
    "КС-1": ("Mikoyan-Gurevich", "KS-1", None, "Kometa"),
    "П-15": ("Raduga", "P-15", None, "Termit"),
    "Х-22": ("Raduga", "Kh-22", None, "Burya"),
    "Х-55": ("Raduga", "Kh-55", None, None),
    "Х-20": ("Raduga", "Kh-20", None, None),
    "Х-28": ("Raduga", "Kh-28", None, None),
    "КСР-2": ("Raduga", "KSR-2", None, None),
    "КСР-11": ("Raduga", "KSR-11", None, None),
    "КСР-5": ("Raduga", "KSR-5", None, None),
}
SPACECRAFT = {
    "Буран": ("NPO Molniya", "Buran", None, None),
    "Союз": ("RKK Energiya", "Soyuz", None, None),
    "Восток": ("OKB-1", "Vostok", None, None),
}
JUNK = {"другие типы ВС", "?", "", "! другие ракеты-носители и МБР !",
        "другие ракеты", "неизвестно"}


def translit(s):
    return "".join(CYR2LAT.get(c, c) for c in s)


def parse_type(t):
    """(manufacturer, model, variant, model_name), or None.

    None means the string does not pin down an airframe. The caller drops
    the row. The project's rule that a blank is the correct answer applies
    to a model as much as to a serial — and here the blank is the whole row,
    because manufacturer and model are both required.
    """
    t = (t or "").strip()
    if not t or t in JUNK:
        return None
    for table in (LITERAL, MISSILES, SPACECRAFT):
        if t in table:
            return table[t]
    # A factory article number -- MiG-29 (9.13) -- is provenance, not a
    # variant, and belongs in the description.
    t = re.sub(r"\s*\([0-9][0-9.\-]*\)\s*$", "", t).strip()
    if t in LITERAL:
        return LITERAL[t]
    if re.match(r"^[A-Za-z0-9][A-Za-z0-9\-./ ]*$", t):
        m = re.match(r"^([A-Za-z]+-\d+)([A-Za-z0-9\-]*)$", t)
        if m:
            return (LATIN_MFR.get(m.group(1)), m.group(1), m.group(2) or None, None)
        return (LATIN_MFR.get(t), t, None, None)
    m = re.match(r"^([А-Яа-яЁё]+)-?(\d+[А-Яа-яЁё]*)(.*)$", t)
    if not m:
        return None
    family, num, rest = m.group(1), m.group(2), m.group(3)
    if family not in FAMILIES:
        return None
    mfr, latin = FAMILIES[family]
    digits = re.match(r"^(\d+)(.*)$", num)
    model = f"{latin}-{digits.group(1)}"
    variant = (translit(digits.group(2)) + translit(rest)).strip("- ")
    variant = re.sub(r"^-+", "", variant)
    # "bis" is lowercase in every source that matters, and the alias tests
    # compare exact strings.
    variant = re.sub(r"(?i)\bBIS\b", "bis", variant)
    return (mfr, model, variant or None, None)


# ── Bort numbers ──────────────────────────────────────────────────────────
COLOURS = {"красный": "Red", "синий": "Blue", "белый": "White",
           "жёлтый": "Yellow", "желтый": "Yellow", "голубой": "Light Blue",
           "чёрный": "Black", "черный": "Black", "зелёный": "Green",
           "зеленый": "Green"}
REG_COUNTRY = {"CCCP": "RU", "СССР": "RU", "RA": "RU", "RF": "RU",
               "UR": "UA", "EW": "BY", "UP": "KZ", "LZ": "BG", "SP": "PL",
               "HA": "HU", "OM": "SK", "OK": "CZ", "YU": "RS", "OH": "FI"}


def normalise_tail(g):
    """"46-красный" -> "46 Red".

    The colour is part of the identity, not decoration: 46 Red and 46 Blue
    are two aircraft. Dropping it — which is what happens if you keep only
    the digits — is how two airframes become one row. Under the old
    (model, tail_number) key it also made half of these collide, which is
    why 347 of 1,190 Russian rows currently sit in the database with no tail
    number at all.
    """
    g = (g or "").strip()
    if not g:
        return ""
    m = re.match(r"^(\d+)[\s\-]*([А-Яа-яЁё]+)$", g)
    if m and m.group(2).lower() in COLOURS:
        return f"{m.group(1)} {COLOURS[m.group(2).lower()]}"
    return g


def operator_country(g, site_cc):
    """Asserted only from the registration itself, or from the Soviet bort
    colour convention at a site inside Russia.

    Everything else stays blank. An airframe standing in Bulgaria was very
    probably Bulgarian-operated, and "very probably" is not a source — under
    the new key a wrong country is worse than no country, because it splits
    one airframe into two records instead of merging two into one.
    """
    g = (g or "").strip()
    if not g:
        return ""
    m = re.match(r"^([A-Za-zА-Я]{2,4})-", g)
    if m and m.group(1).upper() in REG_COUNTRY:
        return REG_COUNTRY[m.group(1).upper()]
    if site_cc == "RU" and re.search(r"красн|син|бел|желт|голуб|черн|зелен", g):
        return "RU"     # colour-suffixed bort is a Soviet/Russian convention
    return ""


# ── Geometry ──────────────────────────────────────────────────────────────
def haversine(a, b, c, d):
    R = 6371000.0
    p1, p2 = math.radians(a), math.radians(c)
    dp, dl = p2 - p1, math.radians(d - b)
    x = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(x))


def cluster_key(p):
    return (round(p["la"] / 0.0025), round(p["lo"] / 0.0045))


# ── Stages ────────────────────────────────────────────────────────────────
def _cache(name):
    os.makedirs(CACHE, exist_ok=True)
    return os.path.join(CACHE, name)


def stage_fetch():
    req = urllib.request.Request(SOURCE, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=60).read()
    with open(_cache("monuments.json"), "wb") as fh:
        fh.write(raw)
    d = json.loads(raw)
    print(f"fetched {d['count']} points -> {_cache('monuments.json')}")


def load_points():
    d = json.load(open(_cache("monuments.json")))
    return d["photos"]


def monuments():
    return [p for p in load_points()
            if p.get("c") == "monument" and p.get("la") and p.get("lo")
            and abs(p["la"]) <= 90 and abs(p["lo"]) <= 180]


def clusters():
    g = collections.defaultdict(list)
    for p in monuments():
        r = parse_type(p["t"])
        if not r or not r[0] or not r[1]:
            continue            # unresolvable type — dropped, never guessed
        g[cluster_key(p)].append(p)
    return g


def stage_geocode(limit=300):
    """Reverse-geocode cluster centroids. Resumable; 1 req/sec per policy."""
    if not UA_CONTACT:
        sys.exit("Set NOMINATIM_CONTACT to a contact address — Nominatim's "
                 "usage policy requires one in the User-Agent.")
    path = _cache("sites.json")
    out = json.load(open(path)) if os.path.exists(path) else {}
    ua = f"airplane.museum aviation-catalogue/1.0 ({UA_CONTACT})"
    todo = []
    for k, v in clusters().items():
        kk = f"{k[0]}_{k[1]}"
        if kk in out:
            continue
        todo.append((kk, sum(p["la"] for p in v) / len(v),
                     sum(p["lo"] for p in v) / len(v), len(v)))
    todo.sort(key=lambda x: -x[3])
    for i, (kk, la, lo, n) in enumerate(todo[:limit]):
        q = urllib.parse.urlencode({"lat": round(la, 6), "lon": round(lo, 6),
                                    "format": "jsonv2", "zoom": "14",
                                    "addressdetails": "1", "accept-language": "en"})
        try:
            req = urllib.request.Request(
                "https://nominatim.openstreetmap.org/reverse?" + q,
                headers={"User-Agent": ua})
            d = json.load(urllib.request.urlopen(req, timeout=25))
            a = d.get("address", {})
            out[kk] = {"la": round(la, 6), "lo": round(lo, 6), "n": n,
                       "city": a.get("city") or a.get("town") or a.get("village")
                               or a.get("municipality") or "",
                       "state": a.get("state") or a.get("region") or "",
                       "country": a.get("country") or "",
                       "cc": (a.get("country_code") or "").upper()}
        except Exception as exc:                       # noqa: BLE001
            out[kk] = {"la": round(la, 6), "lo": round(lo, 6), "n": n,
                       "err": str(exc)[:80]}
        if i % 25 == 0:
            json.dump(out, open(path, "w"))
        time.sleep(1.05)
    json.dump(out, open(path, "w"))
    print(f"geocoded {len(out)} of {len(out) + max(0, len(todo) - limit)} sites")


def stage_report():
    pts = load_points()
    cats = collections.Counter(p.get("c") for p in pts)
    print("source categories:", dict(cats))
    g = clusters()
    print(f"monuments with a resolvable type: {sum(len(v) for v in g.values())}")
    print(f"sites (clustered at {CLUSTER_M} m): {len(g)}")
    path = _cache("sites.json")
    if os.path.exists(path):
        sites = json.load(open(path))
        by_cc = collections.Counter(v.get("cc", "?") for v in sites.values())
        print("sites by country:", by_cc.most_common(15))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    if cmd == "fetch":
        stage_fetch()
    elif cmd == "geocode":
        stage_geocode(int(sys.argv[2]) if len(sys.argv) > 2 else 300)
    elif cmd == "report":
        stage_report()
    else:
        sys.exit(__doc__)
