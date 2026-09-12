#!/usr/bin/env python3
"""Reconcile one region's research passes, validate, and import.

  python3 run_region.py <regiondir> <StateName>[,<StateName>...] [--apply]

Reads <regiondir>/pass*_raw.md, writes <regiondir>/raw/*.txt + *_museums.csv,
dry-runs everything against the live API, and applies only if every dry run is
clean. Never overwrites an existing record: a (model,tail) already in the
database is imported with a BLANK tail and the serial preserved in aliases."""
import csv, glob, io, json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pipe import *
import json as _json
_CA="/home/claude/pipeline/cache_aircraft.json"; _CM="/home/claude/pipeline/cache_museums.json"
def live_tailmap():
    ac=_json.load(open(_CA)); m=collections.defaultdict(list)
    for a in ac:
        if a.get("tail_number"): m[(a["model"], a["tail_number"].strip().upper())].append(a)
    return m, ac
def live_state(state):
    return [x for x in _json.load(open(_CM)) if (x.get("state_province") or "")==state]

def main():
    d = sys.argv[1].rstrip("/")
    states = sys.argv[2].split(",")
    apply_ = "--apply" in sys.argv
    OUT = os.path.join(d, "raw"); os.makedirs(OUT, exist_ok=True)
    paths = sorted(glob.glob(os.path.join(d, "pass*_raw.md")))
    if not paths: print("NO PASS FILES in", d); return 2
    sites, rows = harvest(paths)
    print(f"harvested {len(sites)} site lines, {sum(len(v) for v in rows.values())} aircraft lines from {len(paths)} files")

    # ---- collapse duplicate sites by name-stem, then by coordinate proximity
    def stem(n): return re.sub(r'[^a-z0-9]','', n.lower().split("--")[0])[:38]
    canon = {}
    for p in sites:
        k = stem(p[0])
        if k not in canon: canon[k] = p
        else:                                   # prefer the one with coordinates
            if not canon[k][9] and p[9]: canon[k] = p
    bycoord = {}
    aliasof = {}          # popped stem -> surviving stem, so its rows are kept
    for k, p in list(canon.items()):
        if p[9] and p[10]:
            ck = (round(float(p[9]), 3), round(float(p[10]), 3))
            if ck in bycoord and bycoord[ck] != k:
                aliasof[k] = bycoord[ck]
                print("  same-coordinate site merged: %r -> %r" % (p[0], canon[bycoord[ck]][0]))
                canon.pop(k, None); continue
            bycoord[ck] = k

    # ---- attach rows to sites
    built, used = [], set()
    for k, p in canon.items():
        name = p[0]
        got = []
        for h, rs in rows.items():
            if not h: continue
            hs = stem(h)
            if hs == k or aliasof.get(hs) == k or h.strip() == name or name.split(" -- ")[0].lower() in h.lower():
                got += rs; used.add(h)
        got = normalise(merge(got))
        if got: built.append((p, got))
    orphan = sum(len(v) for h, v in rows.items() if h not in used)
    print(f"reconciled to {len(built)} sites; {orphan} aircraft lines had no matching site heading")

    # ---- in-batch duplicate tails
    seen = {}
    for p, got in built:
        keep = []
        for r in got:
            k = akey(r)
            if k[1] and k in seen:
                q = r.split("|"); q[11] = (q[11].rstrip(". ")+
                  "; tail_number blank - this serial is also claimed by "+seen[k]+" in this batch and the conflict is unresolved")
                q[12] = (q[12]+"; "+k[1]).strip("; "); q[3] = ""
                r = "|".join(q)
            elif k[1]: seen[k] = p[0]
            keep.append(r)
        got[:] = keep

    # ---- collisions with the live database
    tm, _ = live_tailmap()
    nblank = 0
    for p, got in built:
        keep = []
        for r in got:
            k = akey(r)
            if k[1] and k in tm:
                where = tm[k][0]
                q = r.split("|"); q[11] = (q[11].rstrip(". ")+
                  "; tail_number blank - this serial is already recorded in the database (aircraft id %d) and the conflict is unresolved" % where["id"])
                q[12] = (q[12]+"; "+k[1]).strip("; "); q[3] = ""
                r = "|".join(q); nblank += 1
            keep.append(r)
        got[:] = keep
    print(f"{nblank} rows blanked on live-database serial collisions")

    # ---- existing museums in these states become TOP-UPS
    # match existing museums by name across the whole database, not just these
    # states - a live record's state_province may be spelled differently ("DC")
    existing = {}
    for m in _json.load(open(_CM)):
        if m.get("name"): existing[m["name"].strip().lower()] = m
    newsites = [(p,g) for p,g in built if p[0].strip().lower() not in existing]
    topups   = [(p,g) for p,g in built if p[0].strip().lower() in existing]
    if topups: print("TOP-UPS onto existing museums:", [p[0] for p,_ in topups])
    # a top-up must not re-add what the museum already holds: drop rows matching
    # an existing aircraft there by (model,tail) or, untailed, by mfr+model+variant
    for pp, got in topups:
        m = existing[pp[0].strip().lower()]
        if not m.get("id"): continue
        try: cur = get("/museums/%d" % m["id"]).get("aircraft") or []
        except Exception as e: print("  could not read existing", pp[0], e); continue
        have_t = {(a.get("model"), (a.get("tail_number") or "").strip().upper()) for a in cur if a.get("tail_number")}
        have_n = {(a.get("manufacturer"), a.get("model"), a.get("variant") or "") for a in cur}
        keep = []
        for r in got:
            q = r.split("|"); k = akey(r)
            if k[1] and k in have_t: continue
            if not k[1] and (q[0], q[1], q[2]) in have_n: continue
            keep.append(r)
        if len(keep) != len(got):
            print("  %s: dropped %d row(s) already present" % (pp[0], len(got)-len(keep)))
        got[:] = keep

    # ---- manual adjudications: <regiondir>/drops.txt, one "<site-slug>|<substring>"
    # per line, drops the matching row(s). Lives outside the generated files so a
    # rebuild cannot silently revert an adjudication.
    dp = os.path.join(d, "drops.txt")
    if os.path.exists(dp):
        rules = [l.strip().split("|", 1) for l in open(dp) if l.strip() and not l.startswith("#")]
        for pp, got in built:
            sl = slugify(pp[0]); keep = []
            for r in got:
                if any(sl == a and b in r for a, b in rules): continue
                keep.append(r)
            if len(keep) != len(got): print("  drops.txt: %s -%d" % (sl, len(got)-len(keep)))
            got[:] = keep

    # ---- emit
    with open(os.path.join(OUT, "museums.csv"), "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(HDR_M)
        for p,_ in newsites: w.writerow(p)
    files = []
    for p, got in built:
        slug = slugify(p[0])
        body = io.StringIO(); w = csv.writer(body, lineterminator="\n")
        w.writerow(HDR_A)
        for r in got:
            q = r.split("|"); w.writerow(q[:13] + [p[0]] + [q[13]])
        files.append((slug, p[0], body.getvalue(), len(got)))
        with open(os.path.join(OUT, slug + ".txt"), "w") as fh: fh.write("\n".join(got)+"\n")
    total = sum(n for _,_,_,n in files)
    print(f"\n{len(newsites)} new sites, {len(topups)} top-ups, {total} airframes")

    # ---- dry run: museums, then one concatenated aircraft batch per ~40 sites
    mcsv = open(os.path.join(OUT, "museums.csv")).read()
    r = bulk("museums", mcsv, True)
    print("museums dry-run:", {k:r.get(k) for k in ("created","skipped")}, (r.get("errors") or [])[:2])
    if r.get("errors"): print("STOP: museums file rejected"); return 1
    if not apply_:
        print("\n(dry-run only; aircraft cannot be dry-run until museums exist)"); return 0

    r = bulk("museums", mcsv, False)
    print("museums applied:", {k:r.get(k) for k in ("created","skipped")}, (r.get("errors") or [])[:2])
    if r.get("errors"): print("STOP: museum apply failed"); return 1

    batches, cur, n = [], [HDR_A], 0
    for slug, name, text, cnt in files:
        rdr = list(csv.reader(io.StringIO(text)))[1:]
        cur += rdr; n += 1
        if n >= 40: batches.append(cur); cur=[HDR_A]; n=0
    if len(cur) > 1: batches.append(cur)
    ok = True
    for i, b in enumerate(batches, 1):
        buf = io.StringIO(); csv.writer(buf, lineterminator="\n").writerows(b)
        r = bulk("aircraft", buf.getvalue(), True)
        errs = r.get("errors") or []
        print(f"  batch {i}/{len(batches)} dry-run: created={r.get('created')} errors={json.dumps(errs)[:400]}")
        if errs: ok = False
    if not ok: print("STOP: aircraft dry runs failed; nothing applied"); return 1
    for i, b in enumerate(batches, 1):
        buf = io.StringIO(); csv.writer(buf, lineterminator="\n").writerows(b)
        r = bulk("aircraft", buf.getvalue(), False)
        print(f"  batch {i}/{len(batches)} APPLIED: created={r.get('created')} errors={json.dumps(r.get('errors') or [])[:300]}")
    # keep the local snapshot in step with what we just created, so the next
    # region sees this region's serials as live collisions
    try:
        ca = _json.load(open(_CA)); cm = _json.load(open(_CM))
        for pp, _g in newsites: cm.append({"name": pp[0], "state_province": pp[2]})
        for _s, _n, text, _c in files:
            for q in list(csv.reader(io.StringIO(text)))[1:]:
                if q[3]: ca.append({"id": -1, "model": q[1], "tail_number": q[3]})
        _json.dump(ca, open(_CA,"w")); _json.dump(cm, open(_CM,"w"))
    except Exception as e: print("cache update failed:", e)
    print("\nDONE")
    return 0

if __name__ == "__main__": sys.exit(main())
