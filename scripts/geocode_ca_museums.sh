#!/usr/bin/env bash
# Add coordinates (plus missing address / postal / website) to the 11
# California museums that have none.
#
# WHY IT MATTERS
#   api_museums_globe skips museums without coordinates entirely, and
#   api_nearest_museum can't rank them. Between them these 11 hold 89
#   aircraft that are currently invisible to the globe and to "find the
#   nearest museum displaying X" — the app's core feature.
#
# ACCURACY
#   Every coordinate points at the museum building or its aircraft display
#   area, verified against the museum's own site, mapped place data, or (for
#   the Beale SR-71) a surveyed historical-marker GPS point. None is a city
#   or ZIP centroid — a centroid would put the pin in the wrong place and
#   quietly corrupt proximity results, which is worse than having no pin.
#   Checked before writing: all inside the California bounding box, no two
#   sharing a pin, and Blackbird Airpark lands 0.12 km from the adjacent
#   Joe Davies Heritage Airpark as expected.
#
# Usage:
#   export AIRPLANE_HOST=http://127.0.0.1:5000
#   export AIRPLANE_KEY=amt_your_admin_key
#   bash scripts/geocode_ca_museums.sh --dry-run
#   bash scripts/geocode_ca_museums.sh

set -uo pipefail
HOST="${AIRPLANE_HOST:-http://127.0.0.1:5000}"
KEY="${AIRPLANE_KEY:-}"
DRY=0
[[ "${1:-}" == "--dry-run" ]] && DRY=1
[[ -z "$KEY" ]] && { echo "ERROR: set AIRPLANE_KEY" >&2; exit 2; }

# id|name|lat|lon|postal|address|website
ROWS=(
"69|Air Group One CAF Museum|32.82017|-116.97581|92020|1915 N Marshall Ave, Hangar 13|https://ag1caf.org"
"57|Alameda Naval Air Museum|37.78142|-122.29917|94501|2151 Ferry Point, Building 77|https://alamedanavalairmuseum.org"
"52|Armstrong Flight Research Center|34.95131|-117.88811|93523|4800 Lilly Ave|https://www.nasa.gov/armstrong/"
"45|Beale AFB Heritage Park|39.11368|-121.39014|95903|Heritage Park, Robert Nicoletti Way|https://www.beale.af.mil"
"51|Blackbird Airpark|34.60272|-118.08585|93550|2503 E Avenue P|https://flighttestmuseum.org/blackbird-airpark/"
"59|Golden Age Flight Museum|35.13599|-118.44492|93561|101H Commercial Way|https://goldenageflightmuseum.org"
"73|NTC & 11th ACR Museum|35.26240|-116.68823|92310|222 1st Street|https://www.history.army.mil/museums/fieldMuseums/fortIrwin/index.html"
"55|Palm Springs Air Museum|33.83268|-116.50478|92262|745 N Gene Autry Trail|https://palmspringsairmuseum.org"
"54|Ronald Reagan Presidential Library|34.25983|-118.81999|93065|40 Presidential Drive|https://www.reaganlibrary.gov"
"66|Tomorrow's Aeronautical Museum|33.88874|-118.24063|90220|961 W Alondra Blvd|https://www.tamuseum.org"
"68|West Gate Century Circle|34.87113|-117.99083|93523|Rosamond Blvd at Edwards AFB West Gate|https://flighttestmuseum.org"
)

echo "═══════════════════════════════════════════════════════════════"
echo "  Geocoding ${#ROWS[@]} California museums  $([[ $DRY -eq 1 ]] && echo '(DRY RUN)')"
echo "  Host: $HOST"
echo "═══════════════════════════════════════════════════════════════"

ok=0; fail=0
for row in "${ROWS[@]}"; do
    IFS='|' read -r id name lat lon zip addr web <<<"$row"
    body=$(python3 -c "
import json,sys
print(json.dumps({'latitude':float(sys.argv[1]),'longitude':float(sys.argv[2]),
                  'postal_code':sys.argv[3],'address':sys.argv[4],'website':sys.argv[5]}))
" "$lat" "$lon" "$zip" "$addr" "$web")
    printf "  %-40s %10s, %-11s " "$name" "$lat" "$lon"
    if [[ $DRY -eq 1 ]]; then echo "[dry]"; ok=$((ok+1)); continue; fi
    code=$(curl -sS -o /dev/null -w '%{http_code}' -X PATCH \
                -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
                -d "$body" "$HOST/api/v1/museums/$id")
    if [[ "$code" == "200" ]]; then echo "ok"; ok=$((ok+1))
    else echo "HTTP $code"; fail=$((fail+1)); fi
done

echo "═══════════════════════════════════════════════════════════════"
if [[ $DRY -eq 1 ]]; then
    echo "  Dry run — nothing written."
else
    echo "  Updated $ok, failed $fail."
    echo "  89 aircraft should now be reachable via the globe and /api/v1/nearest."
    echo
    echo "  Verify:  curl -s \$AIRPLANE_HOST/api/v1/museums/globe | head -c 300"
fi
echo "═══════════════════════════════════════════════════════════════"

# Three of these sit on active military installations (Armstrong, Beale,
# Fort Irwin) and need a pass or escort. The coordinates are right, but
# "nearest museum" will now suggest places a visitor cannot walk into.
cat <<'EOF'

  ACCESS NOTE — worth surfacing in the UI:
    Armstrong Flight Research Center  — visitor pass required
    Beale AFB Heritage Park           — base access required
    NTC & 11th ACR Museum, Fort Irwin — escort/pass arranged in advance
  West Gate Century Circle and Blackbird Airpark ARE publicly accessible.
EOF
[[ $fail -eq 0 ]]
