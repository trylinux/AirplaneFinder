#!/usr/bin/env bash
# Remove aircraft records created by importing the same file more than once.
#
# WHAT HAPPENED
#   USS Midway's file was imported 4 times and China Lake's twice. Neither
#   file has tail numbers, and a NULL tail never collides with another NULL,
#   so the importer's duplicate check had nothing to catch — every re-run
#   created a fresh set of records and reported success.
#
#   The idempotency guard in import_california.sh was supposed to prevent
#   this, but it began with:
#       command -v jq >/dev/null 2>&1 || return 1
#   i.e. no jq -> "not already loaded" -> import proceeds. It failed OPEN.
#   That is fixed (the guard now uses python3), but these records are
#   already in the database.
#
# WHAT THIS DELETES
#   127 aircraft: for every group of identical (designation, tail_number)
#   at the same museum, it keeps the LOWEST id and deletes the rest.
#   105 from USS Midway (35 aircraft x 3 extra copies)
#    22 from China Lake (22 aircraft x 1 extra copy)
#
#   Deliberately NOT touched — these look like duplicates but are not:
#     Planes of Fame  HA-200 x2, L-29 x2   (genuinely two airframes each)
#     Hiller          "Flyer" x2           (Wright Flyer + Kitty Hawk Flyer)
#     San Diego       "Glider" x2          (Cayley Glider + Chanute Glider)
#
# Usage:
#   export AIRPLANE_HOST=http://127.0.0.1:5000
#   export AIRPLANE_KEY=amt_your_admin_key
#   bash scripts/fix_duplicate_imports.sh --dry-run
#   bash scripts/fix_duplicate_imports.sh

set -uo pipefail
HOST="${AIRPLANE_HOST:-http://127.0.0.1:5000}"
KEY="${AIRPLANE_KEY:-}"
DRY=0
[[ "${1:-}" == "--dry-run" ]] && DRY=1
[[ -z "$KEY" ]] && { echo "ERROR: set AIRPLANE_KEY" >&2; exit 2; }

# Lowest id in each duplicate group is kept; these are the extras.
IDS=(
2552 2553 2554 2555 2556 2557 2558 2559 2560 2561 2562 2563 2564 2565 2566
2567 2568 2569 2570 2571 2572 2573 2574 2575 2576 2577 2578 2579 2580 2581
2582 2583 2584 2585 2586
3090 3091 3092 3093 3094 3095 3096 3097 3098 3099 3100 3101 3102 3103 3104
3105 3106 3107 3108 3109 3110 3111 3112 3113 3114 3115 3116 3117 3118 3119
3120 3121 3122 3123 3124
3242 3243 3244 3245 3246 3247 3248 3249 3250 3251 3252 3253 3254 3255 3256
3257 3258 3259 3260 3261 3262 3263
3618 3619 3620 3621 3622 3623 3624 3625 3626 3627 3628 3629 3630 3631 3632
3633 3634 3635 3636 3637 3638 3639 3640 3641 3642 3643 3644 3645 3646 3647
3648 3649 3650 3651 3652
)

echo "═══════════════════════════════════════════════════════════════"
echo "  Removing ${#IDS[@]} duplicate aircraft  $([[ $DRY -eq 1 ]] && echo '(DRY RUN)')"
echo "  Host: $HOST"
echo "═══════════════════════════════════════════════════════════════"

ok=0; fail=0
for id in "${IDS[@]}"; do
    if [[ $DRY -eq 1 ]]; then
        echo "  [dry] DELETE /api/v1/aircraft/$id"
        ok=$((ok+1)); continue
    fi
    code=$(curl -sS -o /dev/null -w '%{http_code}' -X DELETE \
                -H "Authorization: Bearer $KEY" "$HOST/api/v1/aircraft/$id")
    if [[ "$code" == "200" ]]; then
        ok=$((ok+1)); printf "."
    else
        fail=$((fail+1)); printf "\n  id=%s -> HTTP %s\n" "$id" "$code"
    fi
done
echo
echo "═══════════════════════════════════════════════════════════════"
if [[ $DRY -eq 1 ]]; then
    echo "  Dry run — nothing deleted. Re-run without --dry-run to apply."
else
    echo "  Deleted $ok, failed $fail."
    echo "  Expected after cleanup: USS Midway 35 aircraft, China Lake 22."
fi
echo "═══════════════════════════════════════════════════════════════"
[[ $fail -eq 0 ]]
