# -*- coding: utf-8 -*-
"""Undo a site merge from rollback_site_merge.json.

Recreates any museum, aircraft and link that apply_merge.py removed, using the
state captured immediately before the merge ran. New ids are assigned by the
server, so this restores the DATA, not the original row ids; the mapping is
printed and written to restore_map.json.

    AIRPLANE_KEY=amt_... python3 scripts/restore_merge.py            # everything
    AIRPLANE_KEY=amt_... python3 scripts/restore_merge.py 6107       # one museum
"""
import json, os, sys, time, urllib.request, urllib.error

KEY = os.environ["AIRPLANE_KEY"]
H = "https://airplane.museum/api/v1"
SNAP = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","data","_research","rollback_site_merge.json")))


def call(method, path, body=None):
    # Content-Type only when there is a body - Werkzeug 400s a bodyless request
    # that declares application/json, which would break every exists() check.
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Authorization": f"Bearer {KEY}"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    r = urllib.request.Request(H + path, data=data, method=method, headers=headers)
    for a in range(4):
        try:
            with urllib.request.urlopen(r, timeout=90) as f:
                return f.status, json.loads(f.read() or b"{}")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and a < 3:
                time.sleep(3 * (a + 1)); continue
            return e.code, {"error": e.read().decode()[:200]}
        except Exception as e:
            if a < 3:
                time.sleep(3); continue
            return 0, {"error": str(e)}


def exists(kind, i):
    s, _ = call("GET", f"/{kind}/{i}")
    return s == 200


picked = set(sys.argv[1:])
newmus, newac = {}, {}

for mid, m in SNAP["museums"].items():
    if picked and mid not in picked:
        continue
    if m is None or exists("museums", int(mid)):
        continue
    body = {k: m[k] for k in ("name", "city", "state_province", "country", "postal_code",
                              "region", "address", "website", "access_type",
                              "latitude", "longitude") if m.get(k) is not None}
    s, r = call("POST", "/museums", body)
    if s in (200, 201):
        newmus[mid] = (r.get("museum") or r).get("id")
        print(f"museum {mid} -> {newmus[mid]}  {m['name']}")
    else:
        print(f"museum {mid} FAILED {s} {r}")

for aid, a in SNAP["aircraft"].items():
    if exists("aircraft", int(aid)):
        continue
    links = [l for l in SNAP["links"] if str(l["aircraft_id"]) == aid]
    if picked and not any(str(l["museum_id"]) in picked for l in links):
        continue
    body = {k: a[k] for k in ("manufacturer", "model", "variant", "tail_number",
                              "model_name", "aircraft_name", "aircraft_type", "wing_type",
                              "military_civilian", "role_type", "year_built", "description",
                              "operator_country", "construction_number") if a.get(k)}
    body["aliases"] = a.get("aliases") or []
    s, r = call("POST", "/aircraft", body)
    if s in (200, 201):
        newac[aid] = (r.get("aircraft") or r).get("id")
        print(f"aircraft {aid} -> {newac[aid]}  {a.get('manufacturer')} {a.get('full_designation')}")
    else:
        print(f"aircraft {aid} FAILED {s} {r}")

for l in SNAP["links"]:
    aid, mid = str(l["aircraft_id"]), str(l["museum_id"])
    if picked and mid not in picked:
        continue
    a = newac.get(aid, l["aircraft_id"])
    m = newmus.get(mid, l["museum_id"])
    if not exists("aircraft", a) or not exists("museums", m):
        continue
    s, r = call("POST", "/exhibits", {"aircraft_id": a, "museum_id": m,
                                      "display_status": l.get("display_status") or "on_display",
                                      "notes": l.get("notes")})
    if s not in (200, 201) and "already" not in json.dumps(r):
        print(f"link {a}@{m} {s} {r}")

json.dump({"museums": newmus, "aircraft": newac},
          open("restore_map.json", "w"), indent=1)
print(f"\nrestored {len(newmus)} museums and {len(newac)} aircraft")
