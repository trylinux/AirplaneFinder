# -*- coding: utf-8 -*-
"""Plan merges of duplicate SITE records.

Two museum records are candidates when they are within 300 m of each other, OR
when they share an identified airframe and distance cannot be used. A pair is
PROVEN when both hold the same identified airframe - same full_designation and
the same tail number or construction number. Nothing here deletes anything; it
writes a reviewable plan.

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/plan_merge.py

Why the second candidate rule exists: proximity silently skips any museum with
no coordinates, and 270 of 6,222 records (4.3%) have none. 25 airframes were
hiding behind that -- including the TS-11 1227 pair at Modlin, where a
coordinate-less Wikipedia stub duplicated a site-verified monument record.

Candidates are labelled by how they were found, because the three do NOT mean
the same thing:

  proximity       both sited, under 300 m apart -- a site duplicate. Includes
                  pairs the distance loop missed: it buckets on round(lat,2)
                  and compares only within a bucket, so records straddling a
                  bucket boundary never met until the identity pass found them
  no_coordinates  share an airframe, at least one has no coordinates -- very
                  likely a site duplicate, but nothing measured it
  distant         share an airframe, both sited, far apart -- NOT a merge.
                  One of the two sites is wrong, or the identity was applied to
                  the wrong airframe. These go to their own file for
                  adjudication; merging them would invent a move that never
                  happened.

Known blind spot: the identity key is (full_designation, tail-or-c/n), so two
records for one airframe whose DESIGNATIONS still disagree do not match. The
TS-11 1227 pair at Modlin is the example -- one reads "TS-11Iskra" because a
name is still stuck in its variant, the other "TS-11". Cleaning the variant is
what would make them match, but that clean is itself blocked by the uq_airframe
collision the duplicate causes. Pairs caught in that knot have to be broken by
hand; scripts/plan_variants.py surfaces them as 409s.
"""
import argparse,json,collections,math,os,re,unicodedata,sys,urllib.request

_HERE=os.path.dirname(os.path.abspath(__file__))
_ap=argparse.ArgumentParser(description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
_ap.add_argument("--exhibits",default=os.path.join(_HERE,"cache","exhibits.json"),
                 help="cached /api/v1/exhibits payload; fetched if absent")
_ap.add_argument("--out-dir",default=os.path.join(_HERE,"..","data","_research"))
_ap.add_argument("--base-url",default=os.environ.get("AIRPLANE_BASE_URL",
                                                     "https://airplane.museum"))
_args=_ap.parse_args()

def _load_exhibits(path,base):
    if os.path.exists(path):
        return json.load(open(path,encoding="utf-8"))["results"]
    print(f"no cache at {path}; fetching {base}/api/v1/exhibits ...")
    with urllib.request.urlopen(f"{base}/api/v1/exhibits",timeout=180) as r:
        payload=json.load(r)
    rows=payload if isinstance(payload,list) else payload.get("results",payload)
    os.makedirs(os.path.dirname(path),exist_ok=True)
    json.dump({"results":rows},open(path,"w",encoding="utf-8"))
    return rows

ex=_load_exhibits(_args.exhibits,_args.base_url)
mus={}; bymus=collections.defaultdict(list)
for l in ex:
    m=l["museum"]; mus[m["id"]]=m
    bymus[m["id"]].append(l)

def dist(a,b):
    return math.hypot((a["latitude"]-b["latitude"])*111000,
                      (a["longitude"]-b["longitude"])*111000*math.cos(math.radians(a["latitude"])))

def ident(ac):
    t=(ac.get("tail_number") or "").strip().upper() or None
    c=(ac.get("construction_number") or "").strip().upper() or None
    return ac.get("full_designation"), t, c

def same_airframe(x,y):
    dx,tx,cx=ident(x); dy,ty,cy=ident(y)
    if dx!=dy: return False
    if cx and cy: return cx==cy
    if tx and ty: return tx==ty
    if not tx and not ty:
        return (x.get("manufacturer")==y.get("manufacturer") and x.get("variant")==y.get("variant"))
    return False

def sited(m):
    return m.get("latitude") is not None and m.get("longitude") is not None

pts=[m for m in mus.values() if sited(m)]
buck=collections.defaultdict(list)
for m in pts: buck[(round(m["latitude"],2),round(m["longitude"],2))].append(m)
pairs=[]; seen=set()
for v in buck.values():
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            x,y=v[i],v[j]
            if x.get("country")!=y.get("country"): continue
            d=dist(x,y)
            if d>=300: continue
            k=tuple(sorted((x["id"],y["id"])))
            if k in seen: continue
            seen.add(k); pairs.append((d,x,y,"proximity"))

# ── identity pass: pairs proximity cannot reach ──────────────────────
# Index every IDENTIFIED airframe by (designation, tail-or-c/n). Two museums
# holding the same key are the same airframe recorded twice, whatever the
# coordinates say -- which is the point, since a museum with no coordinates is
# invisible to the loop above.
ident_index=collections.defaultdict(set)
for l in ex:
    a=l["aircraft"]; desig,t,c=ident(a)
    key=(desig,c or t)
    if desig and (c or t):
        ident_index[key].add(l["museum"]["id"])
for key,mids in ident_index.items():
    if len(mids)<2: continue
    mids=sorted(mids)
    for i in range(len(mids)):
        for j in range(i+1,len(mids)):
            x,y=mus[mids[i]],mus[mids[j]]
            if x.get("country")!=y.get("country"): continue
            k=tuple(sorted((x["id"],y["id"])))
            if k in seen: continue
            seen.add(k)
            if sited(x) and sited(y):
                d=dist(x,y)
                # Under 300 m this is an ordinary site duplicate that the
                # proximity loop MISSED: that loop buckets on round(lat,2),
                # a ~1.1 km grid, and compares only within a bucket -- so two
                # records 60 m apart straddling a bucket boundary never meet.
                # The identity pass has no such blind spot, so it recovers
                # them; they are proximity pairs, not distant ones.
                basis="proximity" if d<300 else "distant"
                # Both sited and genuinely far apart: the same airframe cannot
                # be in two places, so one record is wrong. Never a merge.
                pairs.append((d,x,y,basis))
            else:
                pairs.append((None,x,y,"no_coordinates"))

plan=[]
for d,x,y,basis in pairs:
    lx,ly=bymus[x["id"]],bymus[y["id"]]
    shared=[]
    for a in lx:
        for b in ly:
            if same_airframe(a["aircraft"],b["aircraft"]):
                idd=ident(a["aircraft"])
                shared.append((a,b,bool(idd[1] or idd[2])))
    proven=any(s[2] for s in shared)              # identity match: tail or c/n
    type_only=bool(shared) and not proven          # same type, both tails blank
    # Survivor: most airframes first (fewest rows to move), then the more
    # completely filled record, then the more specific name. A bare
    # "Aeroport de Kinshasa-N'Dolo" should lose to "Kinshasa N'Dolo Dakota".
    def score(m, links):
        fields=sum(1 for f in ("address","website","postal_code","city","access_type")
                   if (m.get(f) or "").strip())
        return (len(links), fields, len(m["name"] or ""))
    keep,drop = (x,y) if score(x,lx) >= score(y,ly) else (y,x)
    why = ("more airframes" if len(bymus[keep["id"]])!=len(bymus[drop["id"]])
           else "more complete record")
    kl,dl=bymus[keep["id"]],bymus[drop["id"]]
    dupe_ids=set(); matched=[]
    for a,b,_ in shared:
        loser  = a if a["museum"]["id"]==drop["id"] else b
        winner = b if a["museum"]["id"]==drop["id"] else a
        dupe_ids.add(loser["aircraft_id"])
        matched.append({"keep_aircraft":winner["aircraft_id"],
                        "drop_aircraft":loser["aircraft_id"]})
    move=[l for l in dl if l["aircraft_id"] not in dupe_ids]
    plan.append({
        "match_basis": basis,
        "distance_m": (round(d) if d is not None else None),
        "keep_reason": why,
        "proven": proven,
        "type_only": type_only,
        "shared_count": len(shared),
        "keep": {"id":keep["id"],"name":keep["name"],"city":keep.get("city"),
                 "country":keep.get("country"),"aircraft":len(kl)},
        "drop": {"id":drop["id"],"name":drop["name"],"city":drop.get("city"),
                 "aircraft":len(dl)},
        "delete_aircraft": sorted(dupe_ids),
        "matched": matched,
        "relink_links": [{"aircraft_id":l["aircraft_id"],"link_id":l["id"],
                          "display_status":l.get("display_status")} for l in move],
        "relink_aircraft": sorted(l["aircraft_id"] for l in move),
        "shared_examples": [f'{a["aircraft"].get("full_designation")} {a["aircraft"].get("tail_number") or a["aircraft"].get("construction_number") or ""}'.strip()
                            for a,b,ok in shared if ok][:4],
    })
plan.sort(key=lambda p:(not p["proven"], p["distance_m"] is None, p["distance_m"] or 0))

# A distant pair is NOT a merge: the same airframe cannot be in two places, so
# one of the two records is wrong and a person has to say which. Keeping them
# out of merge_plan.json is what stops apply_merge from inventing a move that
# never happened.
distant=[p for p in plan if p["match_basis"]=="distant"]
mergeable=[p for p in plan if p["match_basis"]!="distant"]

os.makedirs(_args.out_dir,exist_ok=True)
json.dump(mergeable,open(os.path.join(_args.out_dir,"merge_plan.json"),"w"),indent=1)
json.dump(distant,open(os.path.join(_args.out_dir,"distant_conflicts.json"),"w"),indent=1)

def _tally(rows):
    return (sum(1 for p in rows if p["proven"]),
            sum(1 for p in rows if p.get("type_only")),
            sum(1 for p in rows if not p["proven"] and not p.get("type_only")))

pv=[p for p in mergeable if p["proven"]]
by_basis=collections.Counter(p["match_basis"] for p in mergeable)
print(f"candidate pairs: {len(plan)}  ({len(mergeable)} mergeable, {len(distant)} distant)")
for basis in ("proximity","no_coordinates"):
    rows=[p for p in mergeable if p["match_basis"]==basis]
    proven,type_only,none_=_tally(rows)
    print(f"  {basis:15s} {len(rows):4d} pairs   proven {proven:3d}   type-only {type_only:3d}   no shared airframe {none_:3d}")
print(f"\nthe proven set would: delete {sum(len(p['delete_aircraft']) for p in pv)} duplicate aircraft rows,")
print(f"  relink {sum(len(p['relink_aircraft']) for p in pv)} aircraft to the surviving site, remove {len(pv)} museum records")
if distant:
    print(f"\n{len(distant)} DISTANT pairs -> distant_conflicts.json. Not merges: the same")
    print("  airframe is recorded at two places that are far apart, so one record is")
    print("  wrong. Adjudicate as in data/_research/resolved_batch*.md.")
    for p in distant[:6]:
        print(f"    {p['distance_m']:>7,} m  {p['keep']['name'][:34]:34} <-> {p['drop']['name'][:34]:34} {p['shared_examples'][:1]}")
