#!/bin/bash
# Deletes the rows listed in REVIEW_DUPLICATES_SEP2026.md. Nothing here runs
# unless you run it: read that file first, then
#
#   AIRPLANE_KEY=amt_... bash data/delete_reviewed_sep2026.sh
#
# Section 1 (erroneous) and section 2 (duplicates). The site-level duplicate in
# section 3 is NOT handled here - it needs a decision, not a delete.
set -uo pipefail
KEY="${AIRPLANE_KEY:-}"; [ -z "$KEY" ] && { echo "AIRPLANE_KEY is not set" >&2; exit 2; }
HOST="${AIRPLANE_HOST:-https://airplane.museum}"
ERRONEOUS="25228 25892"
DUPLICATES="26490 26491 26492 26493 26494 26486 26595 26473 31095 31094 31090 31091 31092 31093"
DUP_MUSEUMS="4723 4724 4725"
for id in $ERRONEOUS $DUPLICATES; do
  code=$(curl -s -o /dev/null -w '%{http_code}' -X DELETE \
    -H "Authorization: Bearer $KEY" "$HOST/api/v1/aircraft/$id")
  printf '  %-6s %s\n' "$id" "$code"
done
echo
echo "If 25892 (the Seymour Johnson P-51D) is gone, attach its serial to the"
echo "real airframe at the National WWII Museum:"
echo "  curl -X PATCH -H \"Authorization: Bearer \$AIRPLANE_KEY\" -H 'Content-Type: application/json' \\"
echo "    -d '{\"tail_number\":\"44-63615\"}' $HOST/api/v1/aircraft/26009"
