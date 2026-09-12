# Recovering construction numbers from `aliases`

A construction number is the only genuinely unique airframe identifier there is.
It has its own indexed column (`idx_mfr_cn`, scoped by manufacturer because c/n
1044 is a Puma and also, somewhere, a Cessna), and `_find_aircraft_duplicate`
treats a manufacturer + c/n match as the same airframe **even across a change of
registration** — exactly when a tail-based check misses a duplicate.

Research passes have long written it into `aliases` instead, where nothing can
use it and where it breaks the house rule that aliases are alternative *names*.

## Running it

    python3 scripts/snapshot.py          # live database -> local cache
    python3 scripts/plan_cn.py           # writes cn_plan.json + cn_skipped.tsv
    AIRPLANE_KEY=amt_... python3 scripts/apply_cn.py

`plan_cn.py` changes nothing. It parses aliases of the form `c/n X`, `cn X`,
`msn X`, `s/n X`, `w.nr X` and `Werknummer X`, writes the value to
`construction_number` and drops the alias. A row carrying two different candidate
values is skipped into `cn_skipped.tsv` for a person to settle.

`apply_cn.py` is resumable — it logs each id it lands and can be re-run until it
reports no errors other than 409s.

## Two things to keep in mind

**The separator is required.** `^(?:c/n|cn|msn|s/n|…)[\s:.]+` — with `*` instead
of `+`, the bare `cn` form swallows the de-spaced registration aliases the name
pass generates, reading `CNCCG` as construction number `CCG` on a Moroccan 727.

**A 409 is a finding, not a failure.** It means the c/n index recognised an
airframe already in the database. Collect them: they are duplicate pairs, and
because a c/n match holds across different tail numbers they catch duplicates
that no serial comparison would. The September run produced 89, most of them
cross-site serial conflicts from the US state sweep that the c/n settles as one
airframe rather than two.

Re-run after any large import; research files still put c/n in aliases by habit.
