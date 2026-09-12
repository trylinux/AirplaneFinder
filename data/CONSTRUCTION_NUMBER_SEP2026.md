# Construction-number recovery — 12 September 2026

**Coverage 1% → 18%.** 5,439 construction numbers moved out of `aliases` into
their own column; 0 existing values changed; 89 duplicate airframes revealed.

## Why this was the next step

`AIRFRAME_IDENTITY_KEY.md` puts the blanked-tail recovery immediately after the
`operator_country` backfill. Profiling the 8,396 rows with no tail number showed
that recovery is **not** the mechanical job the backlog assumed:

- Only **133** say the tail was deliberately blanked. Of those, **48 are
  cross-site conflicts** — two sites claiming one serial — which need
  adjudication, not restoration, and 18 say the serial was never established.
- The Russian block is thinner than recorded too. Of 641 Russia-sited blanks, the
  descriptions mostly read "no bort number or construction number recorded" —
  russianplanes has already given what it has.
- The remaining ~8,150 never had a serial to lose.

What *was* mechanically recoverable, database-wide, was the other identifier:
**5,550 rows carried a construction number inside `aliases` with the column
empty.** A c/n is the only genuinely unique airframe identifier there is, the
column is indexed (`idx_mfr_cn`), and `_find_aircraft_duplicate` uses a
manufacturer + c/n match as proof of the same airframe **even when the tails
differ** — which is precisely when a tail-based check misses a duplicate.
Leaving them in `aliases` also violates the house rule that aliases are
alternative names, never data that has a column of its own.

## What was done

Every alias of the form `c/n X`, `cn X`, `msn X`, `s/n X`, `w.nr X` or
`Werknummer X` was parsed, written to `construction_number`, and removed from the
alias list. 7 rows carrying two different candidate c/ns were skipped and listed
in `data/_research/cn_skipped.tsv` — an Erco Ercoupe with `5055` and `4055`, a
Zero with `4240` and `4241`.

One false-positive class had to be designed out. The separator is **required**:
without it the bare `cn` form swallowed the de-spaced registration aliases that
the September name pass created, reading `CNCCG` as construction number `CCG` on
a Moroccan Boeing 727.

## The 89 conflicts are the payoff

Every failed write was an HTTP 409 — the c/n index recognising an airframe
already in the database. They are listed in `data/CN_DUPLICATES.md`, and they are
a different and more useful class than the 27 the country backfill surfaced:

Most are **cross-site serial conflicts from the US state sweep that are now
settled as one airframe, not two**. When two sites claimed one serial the
importer blanked the second row's tail and left the question open. The
construction number answers it — `A-4J` c/n 14284 at Oglesby, at Delta and at
Dixon is **one aeroplane**, so two of those three sites do not have it. Examples:

| c/n | airframe | claimed by |
|---|---|---|
| 14284 | Douglas A-4J BuNo 158479 | Oglesby, Delta Township, Dixon |
| I-151 | Grumman A-6E BuNo 152603 | Oglesby, Wayne County IN, Dixon |
| A10-307 | Fairchild Republic A-10A 78-0687 | both Don F. Pratt records |
| 14252 | Douglas A-4M 158430 | D'Iberville, Sequatchie County |
| D-071 | Vought A-7D 69-6241 | Brooke County WV, Burlington Township NJ |
| 20063 | Bell AH-1F 66-15307 | Brooke County WV, Burlington Township NJ |

Brooke County and Burlington Township share two airframes, and Oglesby and Dixon
share two — a pattern that suggests one site's roster was copied onto the other
by a research pass, not two coincidences. Worth checking those four sites as
whole rosters rather than airframe by airframe.

Nothing was deleted and no tail was overwritten; both rows of every pair are
still live.

## What is left of the tail recovery

- **48 cross-site serial conflicts**, of which the pairs above are now resolved
  in principle — the c/n says they are one airframe, so the remaining question is
  only *which site has it*. That is a research task, and satellite or Street View
  imagery settles most monument cases.
- **~8,150 rows that never had a serial.** Not recoverable from the database;
  they need the same per-site research any new import does.
- **137 c/n strings still in `aliases`** — the 89 conflict rows, the 7 ambiguous
  ones, and a few written as prose rather than a bare number.

Method and re-run instructions: `scripts/README_construction_number.md`. The loop
is idempotent; re-run it after any large import, because research files still
write construction numbers into the alias field out of habit.
