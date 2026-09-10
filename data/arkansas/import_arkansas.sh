#!/bin/bash
# Arkansas import: museums first, then one aircraft file per museum.
#
#   AIRPLANE_KEY=amt_... bash data/arkansas/import_arkansas.sh [--apply]
#
# Without --apply it dry-runs everything and changes nothing. With --apply it
# re-dry-runs each file and applies it only if that dry run is clean, so a bad
# file can never reach the database. Import is atomic per file.
set -uo pipefail
cd "$(dirname "$0")/../.."

HOST="${AIRPLANE_HOST:-https://airplane.museum}"
KEY="${AIRPLANE_KEY:-${AIRPLANE_API_KEY:-}}"
APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1

if [ -z "$KEY" ]; then echo "AIRPLANE_KEY is not set" >&2; exit 2; fi

post() {  # post <endpoint> <csv-file> <dry_run true|false>
  python3 - "$HOST" "$KEY" "$1" "$2" "$3" <<'PY'
import json,sys,urllib.request
host,key,ep,path,dry=sys.argv[1:6]
body=json.dumps({"data":open(path,encoding="utf-8").read(),"format":"csv",
                 "dry_run":dry=="true"}).encode()
req=urllib.request.Request(f"{host}/api/v1/{ep}/bulk_import",data=body,
      headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
try:
    r=json.load(urllib.request.urlopen(req,timeout=120))
except urllib.error.HTTPError as e:
    print("HTTP %s %s"%(e.code,e.read().decode()[:400])); sys.exit(1)
errs=r.get("errors") or []
print("created=%s updated=%s skipped=%s errors=%s"%(
    r.get("created"),r.get("updated"),r.get("skipped"),json.dumps(errs)[:400]))
sys.exit(1 if errs else 0)
PY
}

run() {  # run <endpoint> <file>
  local ep=$1 f=$2 n; n=$(basename "$f")
  printf '  %-58s ' "$n"
  local out; out=$(post "$ep" "$f" true)
  if [ $? -ne 0 ]; then echo "DRY-RUN FAILED: $out"; return 1; fi
  if [ "$APPLY" = "1" ]; then
    out=$(post "$ep" "$f" false)
    if [ $? -ne 0 ]; then echo "APPLY FAILED: $out"; return 1; fi
    echo "applied  $out"
  else
    echo "dry-run  $out"
  fi
}

fail=0
echo "== museums =="
run museums data/arkansas/ar_museums.csv || fail=1
if [ "$fail" != "0" ]; then echo "museums failed - stopping (aircraft link by name)"; exit 1; fi

echo "== aircraft =="
for f in data/arkansas/*_aircraft.csv; do run aircraft "$f" || fail=1; done

echo
if [ "$fail" != "0" ]; then echo "FAILURES ABOVE - resolve before applying"; exit 1; fi
[ "$APPLY" = "1" ] && echo "ALL APPLIED" || echo "ALL DRY RUNS CLEAN - re-run with --apply"
