#!/usr/bin/env python3
"""Turn the India / Gulf research packages into data/<country>/ CSVs.

Reads the pipe-delimited SITE / AC lines the research agents wrote,
normalises them (alias hygiene, dashless designations, placeholders,
wing types), reports cross-package collisions, and writes one museums
CSV per country plus one aircraft CSV per site.
"""
import csv, os, re, sys, json, unicodedata
from collections import defaultdict, Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import models  # for join_designation

RESEARCH = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), "..", "data")

PKG = {
    "india_museums.txt": "india", "india_north.txt": "india", "india_west.txt": "india",
    "india_south.txt": "india", "india_east.txt": "india",
    "uae.txt": "uae", "saudi.txt": "saudi_arabia", "oman_kuwait.txt": None,  # split by country
}
COUNTRY_DIR = {"India": "india", "United Arab Emirates": "uae", "Saudi Arabia": "saudi_arabia",
               "Oman": "oman", "Kuwait": "kuwait"}
PREFIX = {"india": "in", "uae": "ae", "saudi_arabia": "sa", "oman": "om", "kuwait": "kw"}

PROSE = re.compile(
    r"\b(is|are|was|were|has|have|had|been|delivered|served|flew|flown|"
    r"displayed|restored|arrived|painted|moved|sold|stood|stands|confirmed|"
    r"reported|acquired|donated|transferred|retired|wears|carries|represents|"
    r"honou?rs|dedicated|remains|includes|assigned|operated|listed|recorded|"
    r"appears|shown|placed|installed|loaned|owned|used|until|since|according)\b", re.I)
NOT_A_NAME = {"replica", "reproduction", "airworthy", "inert", "outdoors", "indoors",
              "flying", "flyable", "static", "prototype", "mockup", "mock-up", "full scale",
              "full-scale", "pylon-mounted", "pole-mounted", "museum-owned", "privately owned",
              "on loan", "unverified"}
DESIG = re.compile(r"^([A-Za-z]{1,4})-(\d{1,3}[A-Za-z]{0,3})$")
JUNK = {"unknown", "none", "n/a", "na", "tbd", "unk", "-", "null", ""}
AC_TYPES = {"fixed_wing", "rotary_wing", "lighter_than_air", "spacecraft", "missile_rocket"}
ROLES = set("fighter trainer private experimental utility ground_attack recon transport bomber test commercial_transport drone search_rescue other space electronic_warfare air_to_surface cruise ballistic tanker surface_to_air sounding air_to_air freighter launch_vehicle artillery_rocket anti_tank anti_ship".split())
BIPLANE_HINT = re.compile(r"tiger moth|dh\.?9|wapiti|dh\.?82|dh\.?60|moth\b|stampe|bristol f\.?2|avro 504|hawker hart|audax|wapiti|jenny|ce-?32|bücker|pt-17|stearman|n3n|po-2|an-2|swordfish|gladiator|fury", re.I)

AC_FIELDS = ["manufacturer", "model", "variant", "tail_number", "model_name", "aircraft_name",
             "aircraft_type", "wing_type", "military_civilian", "role_type", "year_built",
             "description", "aliases", "museum_name", "display_status"]
SITE_FIELDS = ["name", "city", "state_province", "country", "postal_code", "region", "address",
               "website", "access_type", "latitude", "longitude"]

problems = []
def warn(*a): problems.append(" ".join(str(x) for x in a))

def clean(v):
    v = unicodedata.normalize("NFC", (v or "")).replace(" ", " ").strip()
    return "" if v.lower() in JUNK else v

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:60]

def fix_aliases(row, pkg):
    raw = [a.strip() for a in row["aliases"].replace(",", ";").split(";")]
    out, seen = [], set()
    def add(a):
        a = a.strip().strip('"').strip()
        if not a or a.lower() in seen: return
        seen.add(a.lower()); out.append(a)
    for a in raw:
        if not a: continue
        a = re.sub(r"^(painted|marked|as|coded|c/n|cn|msn)\s+", "", a, flags=re.I).strip()
        if a.lower() in NOT_A_NAME:
            continue
        if PROSE.search(a) or len(a.split()) > 4 or len(a) > 34:
            warn(pkg, row["museum_name"], row["model"], "alias moved to description:", repr(a))
            row["description"] = (row["description"] + " " + a.rstrip(".") + ".").strip()
            continue
        add(a)
    model, variant = row["model"], row["variant"]
    for src in [model, models.join_designation(model, variant)] + list(out):
        m = DESIG.match(src)
        if m:
            add(m.group(1) + m.group(2))
    row["aliases"] = "; ".join(out)

def load():
    sites, aircraft = {}, []
    for fn, pkgdir in PKG.items():
        path = os.path.join(RESEARCH, fn)
        for ln in open(path, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if ln.startswith("SITE|"):
                f = [clean(x) for x in ln.split("|")[1:]]
                if len(f) != 11: warn(fn, "bad SITE field count", len(f), ln[:80]); continue
                s = dict(zip(SITE_FIELDS, f)); s["_pkg"] = fn
                s["country"] = {"UAE": "United Arab Emirates"}.get(s["country"], s["country"])
                if s["country"] not in COUNTRY_DIR: warn(fn, "bad country", s["country"], s["name"]); continue
                s["_dir"] = COUNTRY_DIR[s["country"]]
                key = s["name"].lower()
                if key in sites: warn(fn, "duplicate site name", s["name"], "(also in", sites[key]["_pkg"] + ")")
                else: sites[key] = s
            elif ln.startswith("AC|"):
                f = [clean(x) for x in ln.split("|")[1:]]
                if len(f) == 16 and f[6] == "" and f[7] in AC_TYPES:
                    del f[6]  # uae.txt wrote an extra empty column after aircraft_name
                if len(f) != 15: warn(fn, "bad AC field count", len(f), ln[:80]); continue
                r = dict(zip(AC_FIELDS, f)); r["_pkg"] = fn
                r["museum_name"] = SITE_ALIAS.get(r["museum_name"], r["museum_name"])
                aircraft.append(r)
    return sites, aircraft

# Regional packages that recorded a site the museums package also holds, under
# another name. Left side is dropped as a site; its aircraft merge into the right.
SITE_ALIAS = {
    "Heritage Transport Museum, Taoru": "Heritage Transport Museum Taoru",
    "Junagarh Fort Karan Mahal Bikaner DH.9": "Junagarh Fort Museum Bikaner",
    "Air Force Heritage Museum Jodhpur (Officers Mess complex)": "IAF Heritage Museum Jodhpur",
    "Lucknow Zoo (Nawab Wajid Ali Shah Zoological Garden) Tu-124": "Nawab Wajid Ali Shah Zoological Garden Lucknow",
    "Tu-142M Aircraft Museum Visakhapatnam": "TU 142 Aircraft Museum Visakhapatnam",
    "Victory at Sea Memorial Visakhapatnam": "Victory at Sea War Memorial Visakhapatnam",
    "Rashtrapati Bhavan Museum Complex MiG-21": "Rashtrapati Bhavan Museum",
    "Garhwal Rifles Regimental Museum Lansdowne Sea Harrier": "Garhwal Rifles Regimental Museum Lansdowne",
    "Pushpa Gujral Science City Kapurthala": "Pushpa Gujral Science City",
    "Biju Patnaik International Airport Dakota Display": "Biju Patnaik Dakota Display Bhubaneswar Airport",
    "Biju Patnaik Aeronautical Museum HAL Sunabeda": "Biju Patnaik Aeronautical Museum Sunabeda",
    "General Thimayya Museum Madikeri": "General Thimayya Memorial Museum Madikeri",
    "Eastern Air Command Air Force Museum Upper Shillong": "Air Force Museum Upper Shillong",
}
MUSEUM_PKG = "india_museums.txt"

# One airframe, one place: (tail, site) -> action for the losing claim.
TAIL_FIXES = {
    ("W1758", "Sainik School Rewa"): ("", "W1758",
        "Serial W1758 is retained by the aerialvisuals/Commons-photographed Iskra at IAF Museum Palam; the Rewa claim rests on Bharat Rakshak alone, so tail left blank here."),
    ("E261", "Kerala State Science and Technology Museum"): ("", "E261",
        "The marking E261 is also worn by the Gnat at HQ Maintenance Command Nagpur, which has the documented ex-2 Sqn provenance; tail left blank here and the painted serial kept as an alias."),
    ("D1220", "HQ South Western Air Command Gandhinagar"): ("", "D1220",
        "D1220 is also recorded by warbirds.in and Bharat Rakshak at the IAF Heritage Museum Jodhpur; one of the two Maruts wears a spurious serial, and the Jodhpur claim is the better documented, so tail left blank here."),
    ("U455", "C V Raman Park Nagercoil"): ("", "U455",
        "A second MiG-21U painted U-455 stands at AFS Bagdogra (photographed 2017); tail left blank here and the painted serial kept as an alias."),
    ("DS362", "Air Force Station Kalaikunda"): ("DS361", "DS362",
        "warbirds.in (2022) states the Bharat Rakshak locations for DS361/DS362 are swapped and places DS362 at AFA Dundigal; this Kalaikunda airframe is therefore recorded as DS361, with DS362 kept as an alias pending a photo of the data plate."),
    ("709", "King Abdulaziz Air Base Main Gate Displays"): ("52-4537", "709",
        "Recorded under its USAF identity because the Riyadh museum's F-86H also wears 709."),
    ("IE1205", "Gandhi Bagh Nagpur Gnat"): ("", "IE1205",
        "warbirds.in considers the Vayu Bhavan Delhi Gnat the genuine IE-1205; tail left blank here and the painted serial kept as an alias."),
}

def normalise(r, sites):
    pkg = r["_pkg"]
    if r["museum_name"].lower() not in sites:
        warn(pkg, "AC names unknown site", r["museum_name"]); return False
    if r["aircraft_type"] not in AC_TYPES: warn(pkg, r["museum_name"], "bad aircraft_type", r["aircraft_type"]); return False
    if r["military_civilian"] not in ("military", "civilian"): warn(pkg, r["museum_name"], "bad mil/civ", r["military_civilian"]); return False
    if r["display_status"] not in ("on_display", "in_storage", "under_restoration"):
        warn(pkg, r["museum_name"], "display_status defaulted from", repr(r["display_status"])); r["display_status"] = "on_display"
    if r["role_type"] not in ROLES: warn(pkg, r["museum_name"], r["model"], "role_type ->other from", repr(r["role_type"])); r["role_type"] = "other"
    if r["aircraft_type"] != "fixed_wing":
        r["wing_type"] = ""
    elif r["wing_type"] not in ("monoplane", "biplane", "triplane"):
        guess = "biplane" if BIPLANE_HINT.search(r["manufacturer"] + " " + r["model"] + " " + r["model_name"]) else "monoplane"
        warn(pkg, r["museum_name"], r["manufacturer"], r["model"], "wing_type filled:", guess, "(was", repr(r["wing_type"]) + ")")
        r["wing_type"] = guess
    y = r["year_built"]
    if y and not (y.isdigit() and 1850 <= int(y) <= 2030):
        warn(pkg, r["museum_name"], r["model"], "year_built dropped:", y); r["year_built"] = ""
    if not r["variant"] and re.fullmatch(r"[A-Z]{1,3}-\d+[A-Z]", r["model"]):
        r["variant"] = r["model"][-1]; r["model"] = r["model"][:-1]
        warn(pkg, r["museum_name"], "split variant:", r["model"], r["variant"])
    if r["model_name"].replace(" ", "").lower() == models.join_designation(r["model"], r["variant"]).replace(" ", "").lower():
        r["model_name"] = ""
    r["description"] = r["description"].replace("|", "/")
    fix_aliases(r, pkg)
    return True

def norm_tail(t): return re.sub(r"[\s-]", "", t or "").upper()

def merge_duplicates(aircraft):
    """Where two packages inventoried the same site, keep the museums package's
    rows and add only regional rows that bring a new tail (or a new untailed type)."""
    by_site = defaultdict(list)
    for r in aircraft: by_site[r["museum_name"].lower()].append(r)
    out = []
    for site, rows in by_site.items():
        pkgs = {r["_pkg"] for r in rows}
        if len(pkgs) == 1:
            out.extend(rows); continue
        base_pkg = MUSEUM_PKG if MUSEUM_PKG in pkgs else sorted(pkgs)[0]
        base = [r for r in rows if r["_pkg"] == base_pkg]
        tails = {norm_tail(r["tail_number"]) for r in base if r["tail_number"]}
        types = {(r["model"].lower()) for r in base}
        out.extend(base)
        for r in rows:
            if r["_pkg"] == base_pkg: continue
            t = norm_tail(r["tail_number"])
            if t and t in tails: continue
            if not t and r["model"].lower() in types:
                warn("merge dropped untailed", r["model"], "at", r["museum_name"], "from", r["_pkg"]); continue
            warn("merge added", r["model"], r["tail_number"], "at", r["museum_name"], "from", r["_pkg"])
            out.append(r); tails.add(t); types.add(r["model"].lower())
    return out

def apply_tail_fixes(aircraft):
    for r in aircraft:
        key = (norm_tail(r["tail_number"]), r["museum_name"])
        if key in TAIL_FIXES:
            new, alias, note = TAIL_FIXES[key]
            r["tail_number"] = new
            r["aliases"] = (r["aliases"] + "; " + alias).strip("; ")
            r["description"] = (r["description"] + " " + note).strip()
            warn("tail fix", key, "->", repr(new))

def main():
    sites, aircraft = load()
    for k in list(sites):
        if sites[k]["name"] in SITE_ALIAS:
            del sites[k]
    aircraft = [r for r in aircraft if normalise(r, sites)]
    aircraft = merge_duplicates(aircraft)
    apply_tail_fixes(aircraft)
    for r in aircraft: fix_aliases(r, r["_pkg"])  # re-run for merged/fixed aliases

    # ---- cross-package duplicate detection ----
    # near-duplicate sites by coordinates
    coords = [(s, float(s["latitude"]), float(s["longitude"])) for s in sites.values()
              if s["latitude"] and s["longitude"]]
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            a, la, lo = coords[i]; b, lb, lob = coords[j]
            if abs(la - lb) < 0.003 and abs(lo - lob) < 0.003:
                print(f"NEAR: {a['name']} [{a['_pkg']}]  ~  {b['name']} [{b['_pkg']}]")
    # same tail in two rows
    bytail = defaultdict(list)
    for r in aircraft:
        t = re.sub(r"[\s-]", "", r["tail_number"]).upper()
        if t: bytail[t].append(r)
    for t, rows in bytail.items():
        if len(rows) > 1:
            print(f"TAIL {t}: " + " || ".join(f"{r['model']} @ {r['museum_name']} [{r['_pkg']}]" for r in rows))
    # untailed indistinguishable rows within a site
    seen = Counter()
    for r in aircraft:
        if not r["tail_number"]:
            k = tuple(r[x].lower() for x in ("museum_name", "manufacturer", "model", "variant", "aircraft_name", "aliases", "description", "year_built"))
            seen[k] += 1
    for k, n in seen.items():
        if n > 1: print("INDISTINCT untailed:", k[:4], n)

    for p in problems: print("WARN", p)

    if "--write" not in sys.argv:
        print(f"\n{len(sites)} sites, {len(aircraft)} aircraft (dry parse)"); return

    # ---- write ----
    per_site = defaultdict(list)
    for r in aircraft: per_site[r["museum_name"].lower()].append(r)
    for s in sites.values():
        if s["name"].lower() not in per_site: warn("site has no aircraft — dropped:", s["name"])
    by_dir = defaultdict(list)
    for s in sites.values():
        if s["name"].lower() in per_site: by_dir[s["_dir"]].append(s)
    for d, ss in by_dir.items():
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
        with open(os.path.join(OUT, d, f"{PREFIX[d]}_museums.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, lineterminator="\n"); w.writerow(SITE_FIELDS)
            for s in sorted(ss, key=lambda x: x["name"]):
                w.writerow([s[k] for k in SITE_FIELDS])
        used = set()
        for s in ss:
            fn = slug(s["name"]);
            while fn in used: fn += "_2"
            used.add(fn)
            with open(os.path.join(OUT, d, f"{fn}_aircraft.csv"), "w", newline="", encoding="utf-8") as fh:
                w = csv.writer(fh, lineterminator="\n"); w.writerow(AC_FIELDS)
                for r in per_site[s["name"].lower()]:
                    w.writerow([r[k] for k in AC_FIELDS])
        print(d, len(ss), "sites", sum(len(per_site[s['name'].lower()]) for s in ss), "aircraft")
    for p in problems[len(problems):]: pass
    with open(os.path.join(RESEARCH, "build_warnings.txt"), "w") as fh: fh.write("\n".join(problems))

main()
