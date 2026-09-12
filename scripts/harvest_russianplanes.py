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
    # The source writes "?" (and a few variants) where the bort is unknown.
    # Passing that through makes every unknown-bort airframe of a type
    # collide with every other one -- 20 rows were silently deduped this way
    # before it was caught.
    if g in ("?", "??", "-", "--", "н/д", "неизвестно"):
        return ""
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
    if site_cc == "RU" and re.search(r"красн|син|бел|ж[её]лт|голуб|ч[её]рн|зел[её]н", g):
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


# ── Build ─────────────────────────────────────────────────────────────────
# Written 10 September 2026. `build` was documented in this file's usage
# block from the start but never implemented, so the Russian plinth pass sat
# "ready" for a day without being buildable.
#
# Classification is by model family. The source gives a type string and
# nothing else -- no role, no configuration -- so these tables are the one
# place in this pipeline where the script asserts something the source did
# not say. They assert only what the designation itself determines: a Mi- is
# a helicopter, an An-2 is a biplane, a MiG is a fighter. Anything a
# designation does not determine falls to `other`, which is a legal enum
# value and an honest one.

ROTARY = ("Mi-", "Ka-", "Z-5")
BIPLANE = {"An-2", "Y-5", "Po-2", "U-2", "I-15", "I-152", "I-153", "Sh-2"}

ROLE_BY_MODEL = {
    # fighters
    "MiG-1": "fighter", "MiG-3": "fighter", "MiG-9": "fighter",
    "MiG-15": "fighter", "MiG-17": "fighter", "MiG-19": "fighter",
    "MiG-21": "fighter", "MiG-23": "fighter", "MiG-25": "fighter",
    "MiG-27": "ground_attack", "MiG-29": "fighter", "MiG-31": "fighter",
    "La-5": "fighter", "La-7": "fighter", "La-9": "fighter",
    "La-11": "fighter", "La-15": "fighter", "LaGG-3": "fighter",
    "I-15": "fighter", "I-16": "fighter", "I-153": "fighter",
    "Yak-1": "fighter", "Yak-3": "fighter", "Yak-7": "fighter",
    "Yak-9": "fighter", "Yak-25": "fighter", "Yak-28": "fighter",
    "Yak-38": "fighter", "Su-9": "fighter", "Su-11": "fighter",
    "Su-15": "fighter", "Su-27": "fighter", "Su-30": "fighter",
    "Su-33": "fighter", "Su-35": "fighter", "J-5": "fighter",
    "J-6": "fighter", "J-7": "fighter", "F-6": "fighter",
    "Lim-2": "fighter", "Lim-5": "fighter", "SBLim-2": "trainer",
    # attack
    "Su-7": "ground_attack", "Su-17": "ground_attack",
    "Su-20": "ground_attack", "Su-22": "ground_attack",
    "Su-24": "ground_attack", "Su-25": "ground_attack",
    "Il-2": "ground_attack", "Il-10": "ground_attack", "Q-5": "ground_attack",
    # bombers
    "Tu-2": "bomber", "Tu-4": "bomber", "Tu-16": "bomber",
    "Tu-22": "bomber", "Tu-95": "bomber", "Tu-160": "bomber",
    "Il-28": "bomber", "H-5": "bomber", "Pe-2": "bomber", "Pe-8": "bomber",
    "Yer-2": "bomber", "M-4": "bomber", "DB-3": "bomber",
    # transports
    "An-8": "transport", "An-10": "commercial_transport", "An-12": "transport",
    "An-14": "utility", "An-22": "transport", "An-24": "commercial_transport",
    "An-26": "transport", "An-28": "utility", "An-30": "recon",
    "An-32": "transport", "An-72": "transport", "An-124": "transport",
    "An-2": "utility", "Y-5": "utility",
    "Il-12": "transport", "Il-14": "transport", "Il-18": "commercial_transport",
    "Il-62": "commercial_transport", "Il-76": "transport",
    "Il-86": "commercial_transport", "Il-96": "commercial_transport",
    "Li-2": "transport", "L-410": "commercial_transport",
    "Tu-104": "commercial_transport", "Tu-114": "commercial_transport",
    "Tu-124": "commercial_transport", "Tu-134": "commercial_transport",
    "Tu-144": "commercial_transport", "Tu-154": "commercial_transport",
    "Tu-204": "commercial_transport",
    "Yak-40": "commercial_transport", "Yak-42": "commercial_transport",
    # trainers
    "L-29": "trainer", "L-39": "trainer", "L-59": "trainer",
    "TS-11": "trainer", "TS-8": "trainer", "UT-2": "trainer",
    "Yak-11": "trainer", "Yak-18": "trainer", "Yak-50": "trainer",
    "Yak-52": "trainer", "Yak-55": "trainer", "Yak-130": "trainer",
    "Z-42": "trainer", "Z-43": "trainer", "Z-142": "trainer",
    "Po-2": "trainer", "U-2": "trainer",
    # maritime / special
    "Be-6": "search_rescue", "Be-12": "search_rescue", "Be-103": "utility",
    "Tu-142": "recon", "Il-38": "recon", "MiG-25R": "recon",
    "Z-37": "utility", "L-200": "private", "L-13": "trainer",
    # rotary
    "Mi-1": "utility", "Mi-2": "utility", "Mi-4": "utility",
    "Mi-6": "transport", "Mi-8": "utility", "Mi-10": "transport",
    "Mi-14": "search_rescue", "Mi-17": "utility", "Mi-24": "ground_attack",
    "Mi-26": "transport", "Mi-28": "ground_attack",
    "Ka-15": "utility", "Ka-18": "utility", "Ka-25": "search_rescue",
    "Ka-26": "utility", "Ka-27": "search_rescue", "Ka-50": "ground_attack",
    "Z-5": "utility",
}
MISSILE_ROLE = {"S-75": "surface_to_air", "S-125": "surface_to_air",
                "S-200": "surface_to_air", "KS-1": "air_to_surface",
                "P-15": "anti_ship", "Kh-22": "air_to_surface",
                "Kh-55": "cruise", "Kh-20": "air_to_surface",
                "Kh-28": "air_to_surface", "KSR-2": "air_to_surface",
                "KSR-11": "air_to_surface", "KSR-5": "air_to_surface"}


def classify(model):
    if model in MISSILE_ROLE:
        return "missile_rocket", "", MISSILE_ROLE[model]
    if model in ("Buran", "Soyuz", "Vostok"):
        return "spacecraft", "", "space"
    if model.startswith(ROTARY):
        return "rotary_wing", "", ROLE_BY_MODEL.get(model, "utility")
    wing = "biplane" if model in BIPLANE else "monoplane"
    return "fixed_wing", wing, ROLE_BY_MODEL.get(model, "other")


def _clean(s):
    """Commas are forbidden in description and aliases -- the builder rejects
    the line -- and a pipe would shift every field to its left."""
    return (s or "").replace("|", "/").replace(",", ";").replace("\n", " ").strip()


def stage_build():
    import csv as _csv
    sites = json.load(open(_cache("sites.json")))
    live = json.load(open(_cache("live_museums.json")))   # written by stage_live

    def near_live(la, lo):
        for m in live:
            if m.get("latitude") is None:
                continue
            if haversine(la, lo, m["latitude"], m["longitude"]) <= 500:
                return m["name"]
        return None

    rows, museums, skipped_existing, no_site = [], [], [], 0
    used_names = {}
    for key, pts in sorted(clusters().items(), key=lambda kv: -len(kv[1])):
        kk = f"{key[0]}_{key[1]}"
        site = sites.get(kk)
        if not site or site.get("cc") != "RU":
            continue                       # this pass is Russia only
        la = sum(p["la"] for p in pts) / len(pts)
        lo = sum(p["lo"] for p in pts) / len(pts)
        existing = near_live(la, lo)
        if existing:
            skipped_existing.append((existing, len(pts)))
            continue
        city = site.get("city") or site.get("name") or ""
        if not city:
            no_site += 1
            continue
        parsed = []
        for p in pts:
            r = parse_type(p["t"])
            if not r or not r[0] or not r[1]:
                continue
            parsed.append((p, r))
        if not parsed:
            continue
        if len(parsed) == 1:
            mdl = parsed[0][1][1]
            base = f"{mdl} Monument -- {city}"
        else:
            base = f"{city} Aircraft Monuments"
        name = base
        n = 2
        while name in used_names:
            name = f"{base} ({n})"
            n += 1
        used_names[name] = True
        museums.append({
            "name": name, "city": city, "state_province": site.get("state", ""),
            "country": "Russia", "postal_code": "", "region": "Europe",
            "address": "", "website": "", "access_type": "public",
            "latitude": f"{la:.6f}", "longitude": f"{lo:.6f}",
        })
        for p, (mfr, model, variant, mname) in parsed:
            atype, wing, role = classify(model)
            tail = normalise_tail(p.get("g"))
            oc = operator_country(p.get("g"), "RU")
            cn = _clean(p.get("s") or "")
            desc = [f"russianplanes.net monument point {p.get('id','')}"]
            if p.get("re"):
                # The contributor note is carried verbatim and never
                # machine-translated into an assertion -- these notes hold
                # relocations and identity doubts, exactly the class of claim
                # that must not be laundered into a description.
                desc.append(f"contributor note (ru): {_clean(p['re'])}")
            if p.get("g") and tail != (p.get("g") or "").strip():
                desc.append(f"source records the bort as {_clean(p['g'])}")
            aliases = []
            if mname:
                aliases.append(mname)
            rows.append("|".join([
                mfr, model, variant or "", tail, mname or "", "",
                atype, wing, "military", role, "",
                _clean("; ".join(desc)), _clean("; ".join(aliases)),
                "on_display", cn, oc, name,
            ]))

    # Same registration, same site, twice: russianplanes maps some airframes
    # from two points (a re-survey, or a photo of each side), and a civil
    # registration is unique, so this is one aircraft entered twice. Merge on
    # (model, tail) within the site -- which is the key the test suite checks,
    # deliberately ignoring variant, because the two points sometimes disagree
    # on the sub-variant of the very same airframe.
    merged, keep = 0, []
    seen_site = set()
    for r in rows:
        f = r.split("|")
        k = (f[16], f[1], f[3].lower())
        if f[3] and k in seen_site:
            merged += 1
            continue
        if f[3]:
            seen_site.add(k)
        keep.append(r)
    rows = keep
    print(f"same registration mapped twice at one site -- merged: {merged}")

    # A two-digit bort is not unique in Russia and never was: "01 Red" recurs
    # town after town. Where the same (designation, tail, operator_country)
    # turns up at more than one SITE these are different airframes, so the
    # bort cannot serve as the identity -- blank it and keep the number in the
    # description, where the construction number (51% coverage) does the
    # identifying work instead. Silently deduping them, which is what the
    # builder does downstream, would throw away real aircraft.
    seen_key = collections.defaultdict(set)
    for r in rows:
        f = r.split("|")
        if f[3]:
            seen_key[(f[1], f[2], f[3], f[15])].add(f[16])
    collided = 0
    for i, r in enumerate(rows):
        f = r.split("|")
        if f[3] and len(seen_key[(f[1], f[2], f[3], f[15])]) > 1:
            f[11] = _clean(f[11] + f"; wears bort {f[3]}"
                           " -- that number recurs at other Russian sites so it"
                           " is recorded here as a marking rather than as an"
                           " identity")
            f[3] = ""
            rows[i] = "|".join(f)
            collided += 1
    print(f"borts blanked as non-unique across sites: {collided}")

    out = os.path.join(os.path.dirname(CACHE), "..", "data", "russia_monuments")
    out = os.path.normpath(out)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "russia_monuments_museums.csv"), "w",
              newline="", encoding="utf-8") as fh:
        w = _csv.DictWriter(fh, fieldnames=list(museums[0].keys()),
                            lineterminator="\n")
        w.writeheader()
        w.writerows(museums)
    with open(os.path.join(out, "russia_monuments_raw.txt"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(rows) + "\n")
    print(f"sites {len(museums)}  airframes {len(rows)}")
    print(f"skipped as already-in-database (within 500 m): "
          f"{len(skipped_existing)} sites, "
          f"{sum(n for _, n in skipped_existing)} airframes")
    print(f"skipped for having no city: {no_site}")


def stage_live():
    """Cache the live database's Russian museums so build can tell a new
    plinth from a top-up onto a site that is already recorded."""
    req = urllib.request.Request("https://airplane.museum/api/v1/museums/globe",
                                 headers={"User-Agent": "airplane.museum/1.0"})
    d = json.load(urllib.request.urlopen(req, timeout=60))
    ru = [m for m in d if m.get("country") == "Russia"]
    json.dump(ru, open(_cache("live_museums.json"), "w"))
    print(f"cached {len(ru)} live Russian museums")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    if cmd == "fetch":
        stage_fetch()
    elif cmd == "geocode":
        stage_geocode(int(sys.argv[2]) if len(sys.argv) > 2 else 300)
    elif cmd == "report":
        stage_report()
    elif cmd == "live":
        stage_live()
    elif cmd == "build":
        stage_build()
    else:
        sys.exit(__doc__)
