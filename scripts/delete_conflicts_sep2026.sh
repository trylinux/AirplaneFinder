#!/bin/bash
# Delete the 24 aircraft records that adjudication showed are not at the site
# they are recorded at. Read data/CONFLICTS_RESOLVED_SEP2026.md first.
#
#   AIRPLANE_KEY=amt_... bash scripts/delete_conflicts_sep2026.sh
#
# Afterwards run scripts/retry_patch.py: five identity moves are blocked until
# their counterpart is gone, because the unique key will not let two rows hold
# one serial.
#
# Every id below has a one-line reason. Nothing here is a duplicate of a record
# at the SAME site - those are the separate site-merge plan.
set -uo pipefail
KEY="${AIRPLANE_KEY:-}"; [ -z "$KEY" ] && { echo "AIRPLANE_KEY is not set" >&2; exit 2; }
HOST="${AIRPLANE_HOST:-https://airplane.museum}"

del() {  # del <id> <reason>
  # No Content-Type on a bodyless DELETE: Werkzeug 400s a request that declares
  # JSON and carries nothing to parse.
  code=$(curl -s -o /dev/null -w '%{http_code}' -X DELETE \
    -H "Authorization: Bearer $KEY" "$HOST/api/v1/aircraft/$1")
  printf '  %-6s %s  %s\n' "$1" "$code" "$2"
}

echo "== the airframe is at another site =="
del 26718 "TA-4J 158479 is at Gladstone MI (26801); Oglesby holds only a UH-1H"
del 26698 "TA-4J 158479 is at Gladstone MI (26801); Dixon holds an F-105D and an AH-1G"
del 26716 "A-6E 152603 moved to Richmond IN (26769) on 10 Apr 2022"
del 26696 "A-6E 152603 is at Richmond IN (26769)"
del 25622 "AH-1F 66-15307 is at Weirton WV (25670)"
del 25621 "A-7D 69-6241 is at Weirton WV (25669)"
del 27318 "C-47A 43-15200 c/n 19666 is at the site kept as 24868"
del 27174 "GF-4C 63-7417 c/n 0349 is at the site kept as 27167"
del 26251 "RF-4C 67-0438 is at the site kept as 26280"
del 10656 "T-33A 52-9171 is at the site kept as 27102"
del 25678 "UH-1H 66-16109 c/n 5803 is at the site kept as 25671"
del 27163 "T-33A 53-6100 is at Chamberlain SD (27187)"
del 27161 "UH-1H 65-9667 c/n 4711 is at Sleepy Eye MN (27132)"
del 27110 "UH-1B 63-8701 is at Long Prairie MN (27125)"
del 26815 "AH-1F 67-15805 c/n 20469 is at the site kept as 26795"
del 26713 "F-105D 60-0455 c/n D143 is at the site kept as 26694"
del 26794 "UH-1H 67-17562 c/n 9760 is at the site kept as 26768"

echo
echo "== Veterans Memorial Park -- D'Iberville MS holds no aircraft at all =="
echo "   (zero historic=aircraft nodes within 1500 m; every row was pasted from"
echo "    a Tennessee park, and two of them from two DIFFERENT Tennessee parks)"
del 26244 "AH-1F 67-15642 is at Collegedale"
del 26249 "UH-1H 68-16450 is at Jeffersontown"
del 26248 "A-4M 158430 is at Sequatchie County"
del 26247 "T-33A 53-6132 is at Dunlap"
del 26245 "TA-4J 159795 is at Collegedale"

echo
echo "== not a preserved airframe =="
del 6947 "C-47B 43-49942 burned out on takeoff at Burnet 21 Jul 2018 - a write-off"

echo
echo "== LOW CONFIDENCE - read the note before running this one =="
echo "   Mount Clemens American Legion Post 4 displays F-101B 57-0430, not a Huey,"
echo "   so the record is wrong. But the Orland Post 423 placement of 67-17562"
echo "   could not be confirmed, so this deletes a row whose airframe is unplaced."
read -r -p "   delete 26814? [y/N] " a
[ "$a" = "y" ] && del 26814 "UH-1H 67-17562, Mount Clemens - unconfirmed"

echo
echo "Now run:  AIRPLANE_KEY=\$AIRPLANE_KEY python3 scripts/retry_patch.py"
