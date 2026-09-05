#!/usr/bin/env bash
# Fix the 7 verified misattributed aircraft documented in
# data/verified_misattributions.md.
#
# Every change below is backed by an external airframe registry, not a
# guess. Read that file before running this — it explains each verdict and
# links the evidence.
#
# What this does NOT do: touch the five type-level records without serials
# (Wright Flyer, JN-4D, A6M Zero, Bf 109G, Mosquito). Those need a serial
# per airframe before they can be split correctly.
#
# Usage:
#   export AIRPLANE_HOST=http://127.0.0.1:5000     # localhost avoids the TLS issue
#   export AIRPLANE_KEY=amt_your_admin_key
#   bash scripts/fix_verified_misattributions.sh --dry-run   # print, change nothing
#   bash scripts/fix_verified_misattributions.sh             # apply
#
# DELETE /api/v1/exhibits/<id> removes only the LINK. The aircraft and
# museum records survive, so an unlink is easy to undo by re-POSTing.
# The one genuine deletion (Spitfire MK356) is called out separately and
# is NOT performed automatically — see the end of this script.

set -uo pipefail

HOST="${AIRPLANE_HOST:-http://127.0.0.1:5000}"
KEY="${AIRPLANE_KEY:-}"
DRY=0
[[ "${1:-}" == "--dry-run" ]] && DRY=1

[[ -z "$KEY" ]] && { echo "ERROR: set AIRPLANE_KEY" >&2; exit 2; }

unlink() {  # unlink <link_id> <why>
    if [[ $DRY -eq 1 ]]; then
        printf "  [dry] DELETE /api/v1/exhibits/%-4s  %s\n" "$1" "$2"
    else
        printf "  DELETE link %-4s  %s ... " "$1" "$2"
        curl -sS -o /dev/null -w "%{http_code}\n" -X DELETE \
             -H "Authorization: Bearer $KEY" "$HOST/api/v1/exhibits/$1"
    fi
}

relink() {  # relink <aircraft_id> <museum_id> <why>
    if [[ $DRY -eq 1 ]]; then
        printf "  [dry] POST   aircraft=%-4s museum=%-4s  %s\n" "$1" "$2" "$3"
    else
        printf "  LINK aircraft %-4s -> museum %-4s  %s ... " "$1" "$2" "$3"
        curl -sS -o /dev/null -w "%{http_code}\n" -X POST \
             -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
             -d "{\"aircraft_id\":$1,\"museum_id\":$2,\"display_status\":\"on_display\"}" \
             "$HOST/api/v1/exhibits"
    fi
}

echo "═══════════════════════════════════════════════════════════════"
echo "  Fixing verified misattributions  $([[ $DRY -eq 1 ]] && echo '(DRY RUN)')"
echo "  Host: $HOST"
echo "═══════════════════════════════════════════════════════════════"

echo
echo "── 1. P-51D 44-74936 (id 46) — NMUSAF claim is CORRECT, drop the rest ──"
unlink 112 "CAF Airbase Arizona (wrong)"
unlink 116 "EAA Aviation Museum (wrong)"
unlink 127 "IWM Duxford (wrong)"
echo "     keeping link 71 (National Museum of the USAF) — verified correct"

echo
echo "── 2. F-15A 76-0008 (id 49) — actually at March Field, on NMUSAF loan ──"
unlink 109 "Hill Aerospace (its F-15 is 77-0090)"
unlink 72  "NMUSAF (owner, but aircraft is displayed at March Field)"
relink 49 27 "March Field Air Museum — verified"

echo
echo "── 3. C-130H 74-1686 (id 38) — at Empire State Aerosciences, NY ──"
echo "     That museum is not in the database. Unlinking all three false claims;"
echo "     add the museum later if you want to keep the aircraft."
unlink 110 "Hill Aerospace (wrong)"
unlink 106 "March Field (wrong)"
unlink 70  "NMUSAF (wrong)"

echo
echo "── 4. F/A-18A 161749 (id 52) — at Flying Leatherneck, Irvine CA ──"
echo "     Flying Leatherneck is deliberately not in the database (closed to"
echo "     the public until 2027-28). Unlinking all three false claims."
unlink 97  "Museum of Flight (wrong)"
unlink 103 "National Naval Aviation Museum (wrong)"
unlink 92  "Pima (its F/A-18A is 163093)"

echo
echo "── 5. C-47A 43-15073 'SNAFU Special' (id 58) — Normandy, France ──"
unlink 114 "CAF Arizona (its C-47 is 42-23518)"
unlink 76  "NMUSAF (wrong)"
unlink 118 "Pacific Aviation Museum Pearl Harbor (wrong)"

echo
echo "── 6. UH-1H 66-16579 (id 61) — The Helicopter Museum, UK ──"
unlink 111 "Hill Aerospace (its Huey is HH-1H 70-02470)"
unlink 80  "NMUSAF (wrong)"
unlink 104 "National Naval Aviation Museum (wrong)"
unlink 119 "Pacific Aviation Museum Pearl Harbor (wrong)"

echo
echo "── 7. Spitfire Mk.IX MK356 (id 66) — DESTROYED 25 May 2024 ──"
unlink 126 "IWM Duxford (wrong)"
unlink 132 "Musee de l'Air (wrong)"
unlink 123 "RAF Museum London (wrong)"
cat <<'EOF'

     This airframe no longer exists — it crashed on 25 May 2024, killing
     Sqn Ldr Mark Long. It flew with the RAF Battle of Britain Memorial
     Flight and was never in a museum. The aircraft RECORD should probably
     be deleted outright, but that is destructive and irreversible, so it
     is left to you:

         curl -X DELETE -H "Authorization: Bearer $AIRPLANE_KEY" \
              $AIRPLANE_HOST/api/v1/aircraft/66

EOF

echo "═══════════════════════════════════════════════════════════════"
if [[ $DRY -eq 1 ]]; then
    echo "  Dry run — nothing changed. Re-run without --dry-run to apply."
else
    echo "  Done. 20 links removed, 1 created."
    echo "  Aircraft 38, 52, 58, 61 now have NO museum — they exist but are"
    echo "  unlinked, so no museum over-reports its collection. Delete them"
    echo "  or add their real museums when you're ready."
    echo
    echo "  Verify:  python3 scripts/dedupe_aircraft.py"
fi
echo "═══════════════════════════════════════════════════════════════"
