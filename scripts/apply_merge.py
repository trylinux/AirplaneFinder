# -*- coding: utf-8 -*-
"""Execute the PROVEN site merges in merge_plan.json.

Per pair, in this order:
  1. fold any field the surviving airframe lacks in from its duplicate
  2. delete the duplicate airframe row
  3. relink the losing site's unique aircraft to the survivor, then drop the
     old link
  4. delete the losing museum record
Every step is logged so it can be replayed against rollback_site_merge.json.
"""
import json, os, sys, time, urllib.request, urllib.error

KEY = os.environ["AIRPLANE_KEY"]
H = "https://airplane.museum/api/v1"
HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.join(HERE, "..", "data", "_research", "merge_plan.json")
LOG = open(os.path.join(HERE, "..", "merge_actions.log"), "a")
DONE = os.path.join(HERE, "..", "merged_pairs.txt")
done = set()
if os.path.exists(DONE):
    done = {l.strip() for l in open(DONE) if l.strip()}


def call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(H + path, data=data, method=method,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    for a in range(5):
        try:
            with urllib.request.urlopen(r, timeout=90) as f:
                return f.status, json.loads(f.read() or b"{}")
        except urllib.error.HTTPError as e:
            b = e.read().decode()[:200]
            if e.code in (429, 500, 502, 503, 504) and a < 4:
                time.sleep(3 * (a + 1)); continue
            return e.code, {"error": b}
        except Exception as e:
            if a < 4:
                time.sleep(3); continue
            return 0, {"error": str(e)}


def get_ac(i):
    s, d = call("GET", f"/aircraft/{i}")
    return d.get("aircraft") if s == 200 else None


FOLD = ["tail_number", "construction_number", "operator_country", "year_built",
        "aircraft_name", "model_name", "variant"]


def merge_fields(keep_id, drop_id):
    """Anything the survivor is missing and the duplicate has, move across."""
    k, d = get_ac(keep_id), get_ac(drop_id)
    if not k or not d:
        return
    body = {}
    for f in FOLD:
        if not str(k.get(f) or "").strip() and str(d.get(f) or "").strip():
            body[f] = d[f]
    al = list(k.get("aliases") or [])
    have = {s.lower() for s in al}
    for s in (d.get("aliases") or []):
        if s.lower() not in have:
            al.append(s); have.add(s.lower())
    if len(al) != len(k.get("aliases") or []):
        body["aliases"] = al
    dd = (d.get("description") or "").strip()
    kd = (k.get("description") or "").strip()
    if dd and len(dd) > len(kd) + 40:
        body["description"] = dd
    if not body:
        return
    s, r = call("PATCH", f"/aircraft/{keep_id}", body)
    if s != 200 and "tail_number" in body:      # a collision on the tail alone
        body.pop("tail_number")
        s, r = call("PATCH", f"/aircraft/{keep_id}", body) if body else (200, {})
    LOG.write(f"FOLD {drop_id}->{keep_id} {s} {json.dumps(body)[:200]}\n")


plan = [p for p in json.load(open(PLAN)) if p["proven"]]
picked = [a for a in sys.argv[1:] if a != "--all"]
sel = [p for p in plan if str(p["drop"]["id"]) in picked] if picked else plan
print(f"pairs to merge: {len(sel)}", flush=True)

ok = fail = 0
for p in sel:
    tag = f"{p['keep']['id']}<-{p['drop']['id']}"
    if tag in done:
        continue
    for m in p["matched"]:
        merge_fields(m["keep_aircraft"], m["drop_aircraft"])
    bad = False
    for i in p["delete_aircraft"]:
        s, r = call("DELETE", f"/aircraft/{i}")
        LOG.write(f"DEL_AC {i} {s}\n")
        if s not in (200, 204, 404):
            bad = True
            print("  delete aircraft failed", i, s, r, flush=True)
    for rl in p["relink_links"]:
        s, r = call("POST", "/exhibits", {"aircraft_id": rl["aircraft_id"],
                                          "museum_id": p["keep"]["id"],
                                          "display_status": rl.get("display_status") or "on_display"})
        LOG.write(f"RELINK {rl['aircraft_id']}->{p['keep']['id']} {s}\n")
        if s in (200, 201):
            s2, _ = call("DELETE", f"/exhibits/{rl['link_id']}")
            LOG.write(f"DEL_LINK {rl['link_id']} {s2}\n")
        else:
            bad = True
            print("  relink failed", rl, s, r, flush=True)
    if bad:
        fail += 1
        continue
    s, r = call("DELETE", f"/museums/{p['drop']['id']}")
    LOG.write(f"DEL_MUS {p['drop']['id']} {s}\n")
    if s in (200, 204, 404):
        ok += 1
        with open(DONE, "a") as f:
            f.write(tag + "\n")
        print(f"  merged {p['drop']['name'][:34]} -> {p['keep']['name'][:34]}", flush=True)
    else:
        fail += 1
        print("  museum delete failed", p["drop"]["id"], s, r, flush=True)

LOG.flush()
print(f"\nDONE merged {ok}  failed {fail}")
