#!/usr/bin/env bash
# Load everything: every data/<region>/ directory, in dependency order.
#
# Each region directory is imported by scripts/import_data_dir.sh, which
# handles museums-before-aircraft ordering, skips files already imported,
# lets *topup* files through, and backs off on rate limits.
#
# Usage:
#   export AIRPLANE_HOST=http://127.0.0.1:5000   # localhost avoids the TLS issue
#   export AIRPLANE_KEY=amt_your_admin_key
#
#   bash scripts/import_all.sh --dry-run   # validate everything, write nothing
#   bash scripts/import_all.sh             # load it all
#
# Safe to re-run: already-imported files are skipped rather than duplicated.

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

HOST="${AIRPLANE_HOST:-http://127.0.0.1:5000}"
KEY="${AIRPLANE_KEY:-}"
DRY="${1:-}"

[[ -z "$KEY" ]] && { echo "ERROR: set AIRPLANE_KEY to an admin API key." >&2; exit 2; }

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  Loading every region                                         ║"
echo "║  Host: $(printf '%-54s' "$HOST")║"
echo "╚═══════════════════════════════════════════════════════════════╝"

failed=0

# ── Region directories ───────────────────────────────────────────────
# data/ itself holds the original Castle files; the rest are per-region.
for dir in data/*/; do
    dir="${dir%/}"
    ls "$dir"/*_aircraft.csv >/dev/null 2>&1 || continue
    echo
    echo "###############################################################"
    echo "#  $dir"
    echo "###############################################################"
    AIRPLANE_HOST="$HOST" AIRPLANE_KEY="$KEY" AIRPLANE_DATA_DIR="$dir" \
        bash scripts/import_data_dir.sh $DRY || failed=1
done

# ── Castle lives at the top level, predating the per-region layout ───
if [[ -f data/castle_air_museum_aircraft.csv ]]; then
    echo
    echo "###############################################################"
    echo "#  data/ (Castle Air Museum)"
    echo "###############################################################"
    AIRPLANE_HOST="$HOST" AIRPLANE_KEY="$KEY" AIRPLANE_DATA_DIR="data" \
        bash scripts/import_data_dir.sh $DRY || failed=1
fi

echo
echo "╔═══════════════════════════════════════════════════════════════╗"
if [[ $failed -eq 0 ]]; then
    echo "║  All regions reported zero errors.                            ║"
else
    echo "║  At least one region reported errors — see above.             ║"
fi
echo "╚═══════════════════════════════════════════════════════════════╝"

if [[ "$DRY" != "--dry-run" ]]; then
cat <<'EOF'

  Still to run by hand — these change existing records rather than adding,
  so they are deliberately NOT part of the bulk load:

    bash scripts/geocode_ca_museums.sh          # 11 museums onto the map
    bash scripts/fix_verified_misattributions.sh # 7 verified wrong locations
    bash scripts/fix_duplicate_imports.sh        # 127 duplicate records

  Then check the result:

    python3 scripts/dedupe_aircraft.py           # surface duplicates
    python3 scripts/trim_whitespace.py           # field hygiene
EOF
fi
exit $failed
