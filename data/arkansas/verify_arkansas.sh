#!/bin/bash
# Verify the Arkansas import against the live API: every site present, and each
# site's live aircraft count equal to its CSV row count.
set -uo pipefail
cd "$(dirname "$0")/../.."
HOST="${AIRPLANE_HOST:-https://airplane.museum}"

python3 - "$HOST" <<'PY'
import csv,glob,json,os,sys,urllib.parse,urllib.request
host=sys.argv[1]
def get(u):
    return json.load(urllib.request.urlopen(host+u,timeout=60))

live={}
p=1
while True:
    j=get(f"/api/v1/museums/search?per_page=100&page={p}")
    for m in j["results"]:
        if m.get("state_province")=="Arkansas": live[m["name"]]=m["id"]
    if p>=j["pages"]: break
    p+=1

want={}
for r in csv.DictReader(open("data/arkansas/ar_museums.csv")):
    want[r["name"]]=0
for f in sorted(glob.glob("data/arkansas/*_aircraft.csv")):
    rows=list(csv.DictReader(open(f)))
    name=rows[0]["museum_name"]
    want[name]=want.get(name,0)+len(rows)

bad=0
print(f"live Arkansas sites: {len(live)}   expected: {len(want)}\n")
for name,n in sorted(want.items()):
    mid=live.get(name)
    if not mid:
        print(f"  MISSING SITE                       {name}"); bad=1; continue
    a=get(f"/api/v1/museums/{mid}").get("aircraft") or []
    flag="ok " if len(a)==n else "MISMATCH"
    if len(a)!=n: bad=1
    print(f"  {flag} csv={n:3d} live={len(a):3d}  {name}")

extra=set(live)-set(want)
if extra: print("\n  unexpected Arkansas sites:", ", ".join(sorted(extra))); bad=1
print("\ntotal airframes expected:", sum(want.values()))
s=get("/api/v1/stats"); print("db totals:", s)
sys.exit(bad)
PY
