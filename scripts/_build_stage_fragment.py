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
