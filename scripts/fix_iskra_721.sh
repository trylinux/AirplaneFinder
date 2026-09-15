#!/bin/bash
# TS-11 Iskra bis B, side number 721 — one airframe recorded twice.
#
#   AIRPLANE_KEY=amt_... bash scripts/fix_iskra_721.sh
#
# 30205 sat at Muzeum Sił Powietrznych, Dęblin (museum 4612) with full
# provenance. 30291 sat at the Stalowa Wola monument record (museum 4577) with
# almost none. Neither record was wrong: Dęblin OWNS the aircraft and lent it
# to the Muzeum Centralnego Okręgu Przemysłowego at Stalowa Wola, where it is
# displayed outside on Hutnicza. 30205's own text already said as much --
# "Museum still publishes an exhibit page for this airframe but pl.wikipedia
# states it has moved to Muzeum COP Stalowa Wola".
#
# The catalog answers "where can I see this aircraft", so location wins over
# ownership: 30205 is relinked to Stalowa Wola and 30291 is deleted. 30205
# survives because its provenance would otherwise be lost; the useful warning
# from 30291 is folded into its description first.
#
# There is no display_status for a loan — `on_loan` was dropped from the enum
# as ambiguous (whose perspective?), see migrate_display_status_drop_on_loan.sql
# — so the loan is recorded in the exhibit link's notes.
#
# Order matters: fold the text in, attach the new link, drop the old link, and
# only then delete the duplicate. Every step is checked; the script stops on
# the first failure so a half-applied state is visible rather than silent.
set -uo pipefail
KEY="${AIRPLANE_KEY:-}"; [ -z "$KEY" ] && { echo "AIRPLANE_KEY is not set" >&2; exit 2; }
HOST="${AIRPLANE_HOST:-https://airplane.museum}"

KEEP=30205          # the record that survives (rich provenance)
DROP=30291          # the duplicate
OLD_LINK=30217      # KEEP's link to Dęblin (museum 4612)
NEW_MUSEUM=4577     # TS-11 Iskra bis B 721 Monument -- Stalowa Wola

DESC="Built 1960; served with 61 LPSB Biała Podlaska, previously with 42 BLSz Radom, and from 7 March 1996 with CSIL Oleśnica. Owned by the Muzeum Sił Powietrznych at Dęblin and displayed on loan outside the Muzeum Centralnego Okręgu Przemysłowego at Stalowa Wola; the Dęblin museum still publishes an exhibit page for it. Note that a separate MiG-21M (961813) removed from Nowa Ruda in March 2021 also went to a collector in Stalowa Wola; these are different airframes and should not be conflated."
NOTES="On loan from Muzeum Sił Powietrznych, Dęblin."

req() {  # req <method> <path> [json]
  local method="$1" path="$2" body="${3:-}" code
  if [ -n "$body" ]; then
    code=$(curl -s -o /tmp/iskra_resp -w '%{http_code}' -X "$method" \
      -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
      -d "$body" "$HOST/api/v1$path")
  else
    # No Content-Type on a bodyless request: Werkzeug 400s a request that
    # declares JSON and carries nothing to parse.
    code=$(curl -s -o /tmp/iskra_resp -w '%{http_code}' -X "$method" \
      -H "Authorization: Bearer $KEY" "$HOST/api/v1$path")
  fi
  echo "  $method $path -> $code"
  case "$code" in 2*) return 0;; *) echo "     $(head -c 300 /tmp/iskra_resp)" >&2; return 1;; esac
}

echo "1. fold 30291's warning and the loan into 30205's description"
python3 - "$DESC" > /tmp/iskra_body <<'PY'
import json,sys; print(json.dumps({"description": sys.argv[1]}))
PY
req PATCH "/aircraft/$KEEP" "$(cat /tmp/iskra_body)" || exit 1

echo "2. link 30205 to Stalowa Wola, with the loan in the notes"
python3 - "$KEEP" "$NEW_MUSEUM" "$NOTES" > /tmp/iskra_link <<'PY'
import json,sys
print(json.dumps({"aircraft_id": int(sys.argv[1]), "museum_id": int(sys.argv[2]),
                  "display_status": "on_display", "notes": sys.argv[3]}))
PY
req POST "/exhibits" "$(cat /tmp/iskra_link)" || exit 1

echo "3. drop the old Dęblin link"
req DELETE "/exhibits/$OLD_LINK" || exit 1

echo "4. delete the duplicate record 30291"
req DELETE "/aircraft/$DROP" || exit 1

rm -f /tmp/iskra_resp /tmp/iskra_body /tmp/iskra_link
echo
echo "Done. Re-run scripts/plan_variants.py: the variant fix on 30205 was blocked"
echo "by the uq_airframe collision with 30291 and should now apply, settling the"
echo "designation to 'TS-11 bis B'."
