#!/usr/bin/env python3
"""Reconcile a built region against the live database, per museum.

WHY THIS EXISTS
A blank tail number cannot collide: NULL != NULL in MySQL, so the importer's
duplicate check cannot see a re-run and every blank-tail row inserts again.
USS Midway went in four times this way; the Russian plinth pass, which is 46%
blank-tail, duplicated on its second and third apply.

A dry run cannot help either -- it reports collisions, and these do not
collide. The only reliable check is to compare, per museum, the multiset of
(full_designation, tail_number) the files say should be there against what
the live database actually holds, and then fix the difference in both
directions: delete the surplus, import the shortfall.

    python3 scripts/reconcile_import.py <data-dir> [--apply]

Without --apply it only reports.
"""
import collections, csv, glob, json, os, sys, urllib.request, time

BASE = "https://airplane.museum"
KEY = os.environ.get("AIRPLANE_API_KEY") or os.environ.get("K")


def api(path, method="GET", payload=None):
    body = json.dumps(payload).encode() if payload is not None else None
    h = {"Authorization": "Bearer " + KEY}
    if body:
        h["Content-Type"] = "application/json"
    r = urllib.request.Request(BASE + path, body, h, method=method)
    for a in range(3):
        try:
            return json.load(urllib.request.urlopen(r, timeout=120))
        except urllib.error.HTTPError as e:
            if e.code == 429 and a < 2:
                time.sleep(45); continue
            return {"HTTP": e.code, "body": e.read().decode()[:300]}
        except Exception as e:                                  # noqa: BLE001
            if a < 2:
                time.sleep(10); continue
            return {"EXC": str(e)[:200]}


def desig(model, variant):
    model, variant = (model or "").strip(), (variant or "").strip()
    if not variant:
        return model
    if variant[0].isdigit():
        return f"{model}-{variant}"
    if model and model[-1].isdigit():
        return f"{model}{variant}"
    return f"{model} {variant}"


def main():
    d = sys.argv[1]
    apply = "--apply" in sys.argv
    want = collections.defaultdict(list)
    hdr = None
    for f in sorted(glob.glob(os.path.join(d, "*_aircraft.csv"))):
        lines = open(f, encoding="utf-8").read().splitlines()
        hdr = lines[0]
        for row, raw in zip(csv.DictReader(open(f, encoding="utf-8")), lines[1:]):
            want[row["museum_name"]].append(
                ((desig(row["model"], row["variant"]),
                  (row["tail_number"] or "").strip()), raw))

    globe = {m["name"]: m for m in api("/api/v1/museums/globe")}
    surplus, shortfall = [], []
    for name, entries in want.items():
        live_stub = globe.get(name)
        if not live_stub:
            shortfall.extend(r for _, r in entries)
            continue
        if live_stub.get("aircraft_count") == len(entries):
            continue                       # count matches: assume in step
        det = api(f"/api/v1/museums/{live_stub['id']}")
        live = det.get("aircraft") or []
        have = collections.defaultdict(list)
        for a in live:
            have[((a.get("full_designation") or "").strip(),
                  (a.get("tail_number") or "").strip())].append(a["id"])
        need = collections.Counter(k for k, _ in entries)
        for k, ids in have.items():
            extra = len(ids) - need.get(k, 0)
            for i in ids[len(ids) - extra:] if extra > 0 else []:
                surplus.append((i, name, k))
        seen = collections.Counter()
        for k, raw in entries:
            seen[k] += 1
            if seen[k] > len(have.get(k, [])):
                shortfall.append(raw)

    # DANGEROUS BY DEFAULT, so it is now opt-in. A "surplus" is only a
    # duplicate when the file is the COMPLETE inventory for that museum. For a
    # top-up file -- which lists only the airframes being added -- every row
    # already at the site looks like surplus, and deleting them destroys the
    # earlier pass's work. That happened on 10 September 2026: 89 pre-existing
    # African rows were deleted before the mistake was caught.
    if "--delete-surplus" not in sys.argv:
        surplus = []
    print(f"surplus rows in the database (duplicates): {len(surplus)}")
    print(f"shortfall rows still to import:            {len(shortfall)}")
    for s in surplus[:10]:
        print("   surplus", s)
    if not apply:
        print("\n(dry -- pass --apply to fix)")
        return
    for aid, name, k in surplus:
        r = api(f"/api/v1/aircraft/{aid}", method="DELETE")
        if isinstance(r, dict) and (r.get("HTTP") or r.get("EXC")):
            print("delete failed", aid, r)
    print(f"deleted {len(surplus)}")
    # The shortfall is computed from full_designation strings the API
    # renders, which do not always round-trip a variant exactly, so a few
    # rows in it are already present. Strip those and retry rather than
    # losing the whole atomic batch to them.
    # A tailed row can only be short once; if the shortfall names it twice the
    # second copy collides with the first at apply time and takes the batch
    # with it. Blank-tail rows are exempt -- two Mi-8s at one site are two
    # aircraft and both belong.
    seen_row = set()
    dedup = []
    for raw in shortfall:
        f = next(csv.reader([raw]))
        # Key on the JOINED designation, not on (model, variant): the parser can
        # emit "Mi-8"+"T" for a Cyrillic string and "Mi-8T"+"" for a Latin one,
        # and the database compares the joined form, so those two look distinct
        # here and identical to MySQL.
        k = (desig(f[1], f[2]), f[3], f[5])
        if f[3] and k in seen_row:
            continue
        if f[3]:
            seen_row.add(k)
        dedup.append(raw)
    if len(dedup) != len(shortfall):
        print(f"shortfall deduped {len(shortfall)} -> {len(dedup)}")
    shortfall = dedup

    placed = 0
    stuck = []
    for i in range(0, len(shortfall), 40):
        ch = shortfall[i:i + 40]
        for _ in range(4):
            r = api("/api/v1/aircraft/bulk_import", "POST",
                    {"data": "\n".join([hdr] + ch), "format": "csv",
                     "dry_run": True})
            errs = r.get("errors") or []
            if not errs:
                break
            gone = {e["row"] for e in errs if "already exists" in e.get("message", "")}
            if not gone:
                print("blocking", json.dumps(errs)[:300]); ch = []; break
            ch = [x for j, x in enumerate(ch) if j not in gone]
            if not ch:
                break
        if not ch:
            continue
        r = api("/api/v1/aircraft/bulk_import", "POST",
                {"data": "\n".join([hdr] + ch), "format": "csv",
                 "dry_run": False})
        if not r.get("errors"):
            placed += r.get("created") or 0
            continue
        # The batch is atomic, so one row the dry run could not predict --
        # the server also dedupes on construction_number, which no dry run
        # of ours models -- takes the other 39 with it. Fall back to one at
        # a time so a bad row costs only itself, and name the survivors.
        for one in ch:
            r1 = api("/api/v1/aircraft/bulk_import", "POST",
                     {"data": "\n".join([hdr, one]), "format": "csv",
                      "dry_run": False})
            if r1.get("errors"):
                f1 = next(csv.reader([one]))
                stuck.append((f1[15], f1[1], f1[2], f1[3],
                              json.dumps(r1["errors"])[:150]))
            else:
                placed += r1.get("created") or 0
    print(f"imported {placed}")
    if stuck:
        print(f"could not place {len(stuck)} row(s):")
        for x in stuck:
            print("   ", x[1], x[2], repr(x[3]), "@", x[0][:45], "--", x[4])


if __name__ == "__main__":
    main()
