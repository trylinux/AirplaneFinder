#!/bin/bash
# New York import.
#
#   AIRPLANE_KEY=amt_... bash data/new_york/import_new_york.sh [--apply]
#
# Phases, in this order, because aircraft resolve their museum by exact name and
# a dry run creates nothing - so aircraft cannot be dry-run until the museums
# actually exist:
#
#   1. dry-run museums                       (abort on any error)
#   2. apply museums                         (only with --apply)
#   3. dry-run EVERY aircraft file           (abort if any fails)
#   4. apply every aircraft file             (only if all of step 3 was clean)
#
# Step 3 completing before step 4 starts is the point: no aircraft file is
# applied until all 19 have passed. Import is atomic per file.
#
# Without --apply this stops after step 1, since steps 3-4 are meaningless
# until the museums exist. Re-running after a successful apply will duplicate
# blank-tail rows - do not.
set -uo pipefail
cd "$(dirname "$0")/../.."

HOST="${AIRPLANE_HOST:-https://airplane.museum}"
KEY="${AIRPLANE_KEY:-${AIRPLANE_API_KEY:-}}"
APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1
[ -z "$KEY" ] && { echo "AIRPLANE_KEY is not set" >&2; exit 2; }

post() {  # post <endpoint> <csv-file> <true|false dry_run>
  python3 - "$HOST" "$KEY" "$1" "$2" "$3" <<'PY'
import json,sys,urllib.request,urllib.error
host,key,ep,path,dry=sys.argv[1:6]
body=json.dumps({"data":open(path,encoding="utf-8").read(),"format":"csv",
                 "dry_run":dry=="true"}).encode()
req=urllib.request.Request(f"{host}/api/v1/{ep}/bulk_import",data=body,
      headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
try:
    r=json.load(urllib.request.urlopen(req,timeout=180))
except urllib.error.HTTPError as e:
    print("HTTP %s %s"%(e.code,e.read().decode()[:300])); sys.exit(1)
except Exception as e:
    print("ERR %s"%e); sys.exit(1)
errs=r.get("errors") or []
msg="created=%s skipped=%s"%(r.get("created"),r.get("skipped"))
if errs: msg+=" errors="+json.dumps(errs)[:300]
print(msg)
sys.exit(1 if errs else 0)
PY
}

step() {  # step <endpoint> <file> <true|false> <label>
  local n; n=$(basename "$2")
  printf '  %-58s %-8s ' "$n" "$4"
  local out; out=$(post "$1" "$2" "$3"); local rc=$?
  echo "$out"
  return $rc
}

echo "== 1. dry-run museums =="
step museums data/new_york/ny_museums.csv true dry-run || { echo "STOP: museums file is bad"; exit 1; }

if [ "$APPLY" != "1" ]; then
  echo
  echo "Museums dry run clean. Aircraft cannot be dry-run until the museums"
  echo "exist, so re-run with --apply to continue."
  exit 0
fi

echo "== 2. apply museums =="
step museums data/new_york/ny_museums.csv false apply || { echo "STOP: museum apply failed"; exit 1; }

echo "== 3. dry-run all aircraft =="
fail=0
for f in data/new_york/*aircraft.csv; do step aircraft "$f" true dry-run || fail=1; done
if [ "$fail" != "0" ]; then
  echo
  echo "STOP: aircraft dry runs failed. Museums ARE now imported; fix the files"
  echo "and re-run only step 4 (do not re-apply ny_museums.csv)."
  exit 1
fi

echo "== 4. apply all aircraft =="
for f in data/new_york/*aircraft.csv; do step aircraft "$f" false apply || fail=1; done

echo
[ "$fail" = "0" ] && echo "ALL APPLIED - run verify_new_york.sh" || echo "APPLY FAILURES ABOVE"
exit $fail
