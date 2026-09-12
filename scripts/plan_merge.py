# -*- coding: utf-8 -*-
"""Plan merges of duplicate SITE records.

Two museum records within 300 m of each other are candidates. A pair is PROVEN
when both hold the same identified airframe - same full_designation and the same
tail number or construction number. Nothing here deletes anything; it writes a
reviewable plan.
"""
import json,collections,math,re,unicodedata,sys

ex=json.load(open("/home/claude/pipeline/exhibits.json"))["results"]
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

pts=[m for m in mus.values() if m.get("latitude") and m.get("longitude")]
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
            seen.add(k); pairs.append((d,x,y))

plan=[]
for d,x,y in pairs:
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
        "distance_m": round(d),
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
plan.sort(key=lambda p:(not p["proven"], p["distance_m"]))
json.dump(plan,open("/home/claude/pipeline/merge_plan.json","w"),indent=1)
pv=[p for p in plan if p["proven"]]
to=[p for p in plan if p.get("type_only")]
none=[p for p in plan if not p["proven"] and not p.get("type_only")]
print(f"candidate pairs: {len(plan)}")
print(f"  PROVEN (share an airframe identified by tail or c/n): {len(pv)}")
print(f"  type-only (share a type, both tails blank):           {len(to)}")
print(f"  no shared airframe at all:                            {len(none)}")
print(f"\nthe proven set would: delete {sum(len(p['delete_aircraft']) for p in pv)} duplicate aircraft rows,")
print(f"  relink {sum(len(p['relink_aircraft']) for p in pv)} aircraft to the surviving site, remove {len(pv)} museum records")
