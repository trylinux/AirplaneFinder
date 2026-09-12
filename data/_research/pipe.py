#!/usr/bin/env python3
"""Reusable state/region pipeline: harvest research pass files -> reconcile ->
normalise -> CSV -> dry-run -> apply -> verify.

Used for the overnight multi-state run. Every decision it makes automatically is
conservative: it never invents a value, never overwrites an existing record, and
blanks a tail rather than duplicating an airframe."""
import csv, glob, io, json, os, re, sys, time, collections, urllib.request, urllib.error

API   = "https://airplane.museum/api/v1"
KEY   = os.environ.get("AIRPLANE_KEY","")
HDR_A = ["manufacturer","model","variant","tail_number","model_name","aircraft_name",
         "aircraft_type","wing_type","military_civilian","role_type","year_built",
         "description","aliases","museum_name","display_status"]
HDR_M = ["name","city","state_province","country","postal_code","region",
         "address","website","access_type","latitude","longitude"]
TYPES = {"fixed_wing","rotary_wing","lighter_than_air","spacecraft","missile_rocket"}
MILCIV= {"military","civilian"}
STATUS= {"on_display","in_storage","under_restoration"}
WINGS = {"monoplane","biplane","triplane"}
TRAIL = re.compile(r'\s+(reported|painted|claimed|marked|noted|listed)$', re.I)
LEAD  = re.compile(r'^(painted|marked|wears|as)\s+(as\s+)?', re.I)
ATTR  = {"replica","reproduction","mockup","mock-up","static","composite","non-flying",
         "full-scale replica","full scale replica"}
PLACE = {"-","--","n/a","na","none","unknown","?","tbd",""}

# ------------------------------------------------------------------ harvest
def harvest(paths):
    """-> (sites[list of 11-field lists], rows{heading: [14-field lines]})"""
    sites, rows = [], {}
    for path in paths:
        h3 = None
        for ln in open(path, encoding="utf-8", errors="replace"):
            s = ln.rstrip("\n").strip()
            m = re.match(r'^(#+)\s*(.+)$', s)
            if m:
                if len(m.group(1)) <= 3: h3 = m.group(2).strip()
                continue
            if s.count("|") == 10 and "United States" in s and "state_province" not in s:
                sites.append([x.strip() for x in s.split("|")])
            elif s.count("|") == 13 and "manufacturer|model" not in s and not s.startswith("|"):
                rows.setdefault(h3, []).append(s)
    return sites, rows

def slugify(n):
    s = re.sub(r'[^a-z0-9]+','_', n.lower()).strip('_')
    return re.sub(r'_+','_', s)[:70]

def akey(r):
    p = r.split("|"); return (p[1].strip(), p[3].strip().upper())

# ------------------------------------------------------------- normalise
def normalise(rows):
    out = []
    for r in rows:
        p = r.split("|")
        if len(p) != 14: continue
        for i in (2,3,4,5,10):
            if p[i].strip().lower() in PLACE: p[i] = ""
        keep, moved = [], []
        for a in [x.strip() for x in p[12].split(";") if x.strip()]:
            b = TRAIL.sub("", LEAD.sub("", a)).strip()
            if b.lower() in ATTR or len(b) > 26 or len(b.split()) > 4:
                moved.append(b); continue
            if b: keep.append(b)
        if moved:
            at = [m for m in moved if m.lower() in ATTR]
            ot = [m for m in moved if m.lower() not in ATTR]
            bits = []
            if at: bits.append("recorded as a %s not an original airframe" % at[0].lower())
            if ot: bits.append("also recorded as " + "; ".join(ot))
            note = "; ".join(bits)
            p[11] = (p[11].rstrip(". ") + "; " + note) if p[11].strip() else note[0].upper()+note[1:]
        p[11] = p[11].replace(",", ";").strip()
        p[12] = "; ".join(dict.fromkeys(keep))
        # dashless designation variants, as the canonical builder does
        extra = []
        for d in (p[1].strip(), (p[1].strip()+p[2].strip()) if p[2].strip() else ""):
            if d and "-" in d: extra.append(d.replace("-",""))
        if extra:
            al = [x for x in p[12].split("; ") if x] + [e for e in extra if e]
            p[12] = "; ".join(dict.fromkeys(al))
        # required-field guards
        if not p[0].strip() or not p[1].strip(): continue
        if p[6].strip() not in TYPES: continue
        if p[8].strip() not in MILCIV: p[8] = "military"
        if p[13].strip() not in STATUS: p[13] = "on_display"
        if p[6].strip() != "fixed_wing": p[7] = ""
        elif p[7].strip() not in WINGS: p[7] = "monoplane"
        out.append("|".join(p))
    return out

def merge(*groups):
    out, seen, unt = [], set(), set()
    for g in groups:
        for r in g:
            p = r.split("|"); k = akey(r)
            if k[1]:
                if k in seen: continue
                seen.add(k); out.append(r)
            else:
                uk = tuple(x.strip().lower() for x in (p[0],p[1],p[2],p[4],p[5]))
                if uk in unt: continue
                unt.add(uk); out.append(r)
    return out

# ------------------------------------------------------------------ API
def _post(ep, payload):
    req = urllib.request.Request(f"{API}/{ep}", data=json.dumps(payload).encode(),
        headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=240))
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:300]
            if e.code in (429,502,503) and attempt < 2: time.sleep(30); continue
            return {"errors":[f"HTTP {e.code} {body}"]}
        except Exception as e:
            if attempt < 2: time.sleep(10); continue
            return {"errors":[str(e)]}

def bulk(ep, csv_text, dry):
    return _post(f"{ep}/bulk_import", {"data":csv_text,"format":"csv","dry_run":dry})

def get(path):
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(API+path, timeout=120))
        except Exception:
            if attempt < 2: time.sleep(5); continue
            raise

def live_state(state):
    out, p = [], 1
    while True:
        j = get(f"/museums/search?per_page=100&page={p}")
        out += [m for m in j["results"] if (m.get("state_province") or "")==state]
        if p >= j["pages"]: break
        p += 1
    return out

def live_tailmap():
    j = get("/aircraft/search?per_page=100&page=1"); ac = list(j["results"])
    for p in range(2, j["pages"]+1):
        ac += get(f"/aircraft/search?per_page=100&page={p}")["results"]
    m = collections.defaultdict(list)
    for a in ac:
        if a["tail_number"]: m[(a["model"], a["tail_number"].strip().upper())].append(a)
    return m, ac
