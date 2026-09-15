#!/bin/bash
# TS-11 Iskra, tactical number 1227, Twierdza Modlin — one airframe recorded twice.
#
#   AIRPLANE_KEY=amt_... bash scripts/fix_modlin_1227.sh
#
# 29899 sat at museum 4624 "Muzeum Kampanii Wrześniowej i Twierdzy Modlin" with
# no coordinates, one aircraft, and the description "pl.wikipedia TS-11
# preserved list". 30298 sat at museum 4571 "Twierdza Modlin Aircraft
# Monuments" with coordinates, three aircraft, and a record someone physically
# checked: "Tactical number 1227; re-checked on site 5 July 2025".
#
# Same fortress, same airframe. The SITE_MERGE_PLAN rule — airframe count
# first, then completeness — picks 4571 on both counts. Note that this INVERTS
# the instinct that the museum-sounding name is the better record: here the
# museum-named row is the Wikipedia stub and the monument-sweep row is the
# verified one.
#
# Nothing to fold in: 29899's aliases (TS11, Iskra) are a subset of 30298's
# (TS11, Iskra, 1227), model_name matches, neither has a c/n or year built, and
# 30298's description is strictly the better of the two.
#
# Neither plan_merge nor apply_merge can do this pair. plan_merge keys identity
# on (full_designation, tail), and 29899 still reads "TS-11Iskra" because a name
# is stuck in its variant — the clean that would fix that is itself blocked by
# the uq_airframe collision this duplicate causes. Hence a hand cut.
set -uo pipefail
KEY="${AIRPLANE_KEY:-}"; [ -z "$KEY" ] && { echo "AIRPLANE_KEY is not set" >&2; exit 2; }
HOST="${AIRPLANE_HOST:-https://airplane.museum}"

DROP_AIRCRAFT=29899
DROP_MUSEUM=4624      # empty once the aircraft above is gone

req() {  # req <method> <path>
  local code
  # No Content-Type on a bodyless DELETE: Werkzeug 400s a request that declares
  # JSON and carries nothing to parse.
  code=$(curl -s -o /tmp/modlin_resp -w '%{http_code}' -X "$1" \
    -H "Authorization: Bearer $KEY" "$HOST/api/v1$2")
  echo "  $1 $2 -> $code"
  case "$code" in 2*) return 0;; *) echo "     $(head -c 300 /tmp/modlin_resp)" >&2; return 1;; esac
}

echo "1. delete the duplicate airframe 29899 (30298 at museum 4571 survives)"
req DELETE "/aircraft/$DROP_AIRCRAFT" || exit 1

echo "2. delete museum 4624, now holding nothing"
req DELETE "/museums/$DROP_MUSEUM" || exit 1

rm -f /tmp/modlin_resp
echo
echo "Done. Museum 4571 keeps the MiG-15 311, TS-11 1227 and Mi-2."
echo "Open question left deliberately untouched: 4571 is named from the monument"
echo "sweep. If those three airframes are the museum's outdoor exhibits rather"
echo "than standalone monuments, the record should be renamed to Muzeum Kampanii"
echo "Wrześniowej i Twierdzy Modlin. That needs someone who knows the site."
