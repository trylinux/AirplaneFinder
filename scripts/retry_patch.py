# -*- coding: utf-8 -*-
"""Re-apply the conflict PATCH set, skipping anything already correct.

Eight identity moves are blocked until their counterpart record is deleted -
the unique key will not let two rows hold one serial. Run this again after
scripts/delete_conflicts_sep2026.sh and they go through.
"""
import json, os, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from conflict_ops import PATCH

KEY = os.environ["AIRPLANE_KEY"]


def call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Authorization": f"Bearer {KEY}"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    r = urllib.request.Request("https://airplane.museum/api/v1" + path,
                               data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(r, timeout=60) as f:
            return f.status, json.loads(f.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:200]}
    except Exception as e:
        return 0, {"error": str(e)}


done = blocked = skipped = 0
still = []
for i, body in PATCH.items():
    s, r = call("GET", f"/aircraft/{i}")
    if s != 200:
        print(f"  {i}: not found ({s})")
        continue
    cur = r["aircraft"]
    if all(str(cur.get(k) or "") == str(v) for k, v in body.items()):
        skipped += 1
        continue
    s, r = call("PATCH", f"/aircraft/{i}", body)
    if s == 200:
        done += 1
        print(f"  {i} patched: {', '.join(f'{k}={v!r}' for k, v in body.items())[:90]}")
    else:
        blocked += 1
        still.append(i)
        who = ""
        try:
            who = f" (waits on id {json.loads(r['error']).get('existing_id')})"
        except Exception:
            pass
        print(f"  {i} blocked {s}{who}")

print(f"\npatched {done}, already correct {skipped}, blocked {blocked}")
if still:
    print("blocked ids:", still)
    print("re-run this after the deletes")
