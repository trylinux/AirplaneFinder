#!/usr/bin/env bash
# Import the California museum + aircraft data set.
#
# Order matters: museums first. Every aircraft row carries
# museum_name=<its museum>, which the importer resolves against museums that
# already exist. Run the aircraft files against an empty museum table and all
# of them fail validation and roll back — deliberately, so you never end up
# with hundreds of unlinked aircraft.
#
# Each museum is a separate file so one bad row can only ever take down that
# museum's import, never the whole state.
#
# Usage:
#   export AIRPLANE_HOST=https://airplane.museum
#   export AIRPLANE_KEY=amt_your_admin_key
#   bash scripts/import_california.sh --dry-run     # validate everything, write nothing
#   bash scripts/import_california.sh               # do it for real
#
# Exit codes: 0 all good, 1 at least one file reported errors.

set -uo pipefail

HOST="${AIRPLANE_HOST:-https://airplane.museum}"
KEY="${AIRPLANE_KEY:-}"
DRY=""
[[ "${1:-}" == "--dry-run" ]] && DRY="-F dry_run=1"

cd "$(dirname "${BASH_SOURCE[0]}")/.."
DATA=data/california

if [[ -z "$KEY" ]]; then
    echo "ERROR: set AIRPLANE_KEY to an admin API key." >&2
    exit 2
fi
if ! command -v jq >/dev/null 2>&1; then
    echo "note: jq not found — responses will print raw." >&2
fi

failed=0

# Re-running an aircraft file that is already imported is NOT harmless.
# Only rows WITH a tail number collide; rows with a blank tail_number are
# NULL, and NULL never collides — so on a second run those rows would be
# created a second time as duplicates. Today the atomic rollback hides that
# (one collision discards the batch), but a file whose rows all lack tail
# numbers would silently double. So: check first, skip if already loaded.
# Returns 0 ("already loaded") if that museum already has aircraft.
#
# This MUST fail closed. An earlier version began with
#   command -v jq >/dev/null 2>&1 || return 1
# so on a box without jq the guard reported "not loaded" and the import
# went ahead — which is how USS Midway ended up imported four times and
# China Lake twice. Files with no tail numbers duplicate silently, because
# a NULL tail never collides. It now uses python3 only (already required
# for the museum filter) and returns "already loaded" if it cannot tell.
already_loaded() {  # already_loaded <csv>
    local file="$1" result
    if ! command -v python3 >/dev/null 2>&1; then
        echo "      (python3 missing — cannot verify; skipping to be safe)" >&2
        return 0                       # fail CLOSED: skip rather than duplicate
    fi
    result=$(AIRPLANE_BASE_URL="$HOST" python3 - "$file" <<'PY' 2>/dev/null
import csv, json, sys, os, urllib.parse, urllib.request
path = sys.argv[1]
base = os.environ.get("AIRPLANE_BASE_URL", "").rstrip("/")
try:
    row = next(csv.DictReader(open(path, encoding="utf-8")), None)
    name = (row or {}).get("museum_name", "").strip()
    if not name:
        print("UNKNOWN"); sys.exit()
    q = base + "/api/v1/museums/search?q=" + urllib.parse.quote(name)
    res = json.load(urllib.request.urlopen(q, timeout=20))
    m = next((x for x in res.get("results", []) if x["name"] == name), None)
    if not m:
        print("NEW"); sys.exit()        # museum absent -> nothing imported yet
    d = json.load(urllib.request.urlopen(f"{base}/api/v1/museums/{m['id']}", timeout=20))
    print("LOADED" if d.get("aircraft") else "NEW")
except Exception:
    print("UNKNOWN")
PY
)
    case "$result" in
        NEW)    return 1 ;;            # safe to import
        LOADED) return 0 ;;            # skip, already there
        *)      echo "      (could not verify $(basename "$file") — skipping to be safe)" >&2
                return 0 ;;            # fail CLOSED
    esac
}

post() {  # post <endpoint> <file>
    local endpoint="$1" file="$2"
    if [[ ! -f "$file" ]]; then
        echo "  SKIP (missing): $file"; return
    fi
    if [[ "$endpoint" == *aircraft* && -z "$DRY" ]] && already_loaded "$file"; then
        printf "  %-46s already imported — skipped\n" "$(basename "$file")"
        return
    fi
    local rows; rows=$(($(wc -l < "$file") - 1))
    printf "  %-46s %4d rows  " "$(basename "$file")" "$rows"
    local resp code attempt=1
    # The bulk endpoints are rate limited. Importing one file per museum is
    # dozens of requests in a couple of minutes, so a 429 is expected rather
    # than exceptional — back off and retry instead of reporting a phantom
    # failure. A 429 body is an HTML error page, not JSON, so it has to be
    # caught by status code before we try to parse it.
    while :; do
        resp=$(curl -sS -w '\n%{http_code}' -H "Authorization: Bearer $KEY" \
                    -F "file=@${file}" $DRY "${HOST}${endpoint}")
        code=$(tail -n1 <<<"$resp")
        resp=$(sed '$d' <<<"$resp")
        [[ "$code" != "429" ]] && break
        if (( attempt > 5 )); then
            echo "rate limited (429) — gave up after $((attempt-1)) retries"
            echo "        raise BULK_IMPORT_RATE_LIMIT in config.py, or wait an hour."
            failed=1
            return
        fi
        local wait=$(( attempt * 60 ))
        printf "\n      429 rate limited — waiting %ds (attempt %d/5) " "$wait" "$attempt"
        sleep "$wait"
        attempt=$((attempt+1))
    done
    if [[ "$code" != "200" ]]; then
        echo "HTTP $code"
        failed=1
        return
    fi
    if command -v jq >/dev/null 2>&1; then
        local created linked errs
        created=$(jq -r '.created // 0' <<<"$resp")
        linked=$(jq -r '.linked // 0' <<<"$resp")
        errs=$(jq -r '(.errors // []) | length' <<<"$resp")
        printf "created=%-4s linked=%-4s errors=%s\n" "$created" "$linked" "$errs"
        if [[ "$errs" != "0" ]]; then
            failed=1
            jq -r '.errors[:5][] | "        row \(.row) \(.field): \(.message)"' <<<"$resp"
        fi
    else
        echo "$resp"
    fi
}

echo "═══════════════════════════════════════════════════════════════"
echo "  California import ${DRY:+(DRY RUN — nothing will be written)}"
echo "  Host: $HOST"
echo "═══════════════════════════════════════════════════════════════"

echo
echo "── Step 1: museums (must run first) ──"
# Subtract museums that already exist. Without this, one already-imported
# museum makes the atomic importer reject all 43 rows — which is what
# happens the moment you add a museum and re-run.
MUSEUM_FILE="$DATA/ca_museums.csv"
if command -v python3 >/dev/null 2>&1; then
    FILTERED=$(mktemp /tmp/ca_museums_new.XXXXXX.csv)
    AIRPLANE_BASE_URL="$HOST" AIRPLANE_API_KEY="$KEY" \
        python3 scripts/filter_new_museums.py "$MUSEUM_FILE" --out "$FILTERED"
    case $? in
        0) MUSEUM_FILE="$FILTERED" ;;
        3) echo "  all museums already present — skipped"; MUSEUM_FILE="" ;;
        *) echo "  (filter failed; falling back to the full file)" ;;
    esac
fi
[[ -n "$MUSEUM_FILE" ]] && post /api/v1/museums/bulk_import "$MUSEUM_FILE"
[[ -n "${FILTERED:-}" ]] && rm -f "$FILTERED"

echo
echo "── Step 2: aircraft, one file per museum ──"
for f in "$DATA"/*_aircraft.csv; do
    post /api/v1/aircraft/bulk_import "$f"
done

echo
echo "═══════════════════════════════════════════════════════════════"
if [[ $failed -eq 0 ]]; then
    echo "  All files reported zero errors."
    if [[ -n "$DRY" ]]; then
        echo "  Dry run — nothing written. Re-run without --dry-run to apply."
    else
        echo
        echo "  Next:"
        echo "    python3 scripts/dedupe_aircraft.py      # surface duplicates"
        echo "    python3 scripts/trim_whitespace.py      # check field hygiene"
    fi
else
    echo "  One or more files reported errors — see above."
    echo "  The importer is atomic, so any file with errors wrote NOTHING."
    echo "  Fix those rows and re-run; files that succeeded are already in."
fi
echo "═══════════════════════════════════════════════════════════════"
exit $failed
