# Cleaning the `variant` column

`variant` is meant to hold a mark or suffix — `A`, `F.6`, `Mk 20`, `bis` — and
it is half of the generated `full_designation` column, which in turn is part of
the `uq_airframe` key. Research passes have also used it for the **type name**,
which belongs in `model_name`, so the catalog renders headings like
`CT-133 Silver Star 3` and `SE 210 Caravelle`.

This pass separates the mechanical fixes from the judgement calls. It does not
fill blank variants — 31% of airframes have none, and deriving them from tails
and descriptions is a different, far more error-prone job.

## Running it

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/plan_variants.py
    # read scripts/variant_summary.txt, then:
    python3 scripts/apply_variants.py --dry-run
    AIRPLANE_API_KEY=amt_... python3 scripts/apply_variants.py

`plan_variants.py` writes nothing to the database. It produces
`variant_plan.json` (mechanical), `variant_review.tsv` (for a person) and
`variant_summary.txt` (counts).

`apply_variants.py` is resumable: applied ids are appended to
`applied_variant_ids.txt` as they land, so an interrupted run is safe to repeat
and never rewrites a row. `--only D` restricts a run to one class.

## The four classes

| class | rule | example | auto |
|---|---|---|---|
| `C` | stray whitespace | `" A "` → `A` | yes |
| `B` | variant restates the model | `A-4` + `A-4KU` → `KU` | yes |
| `D` | variant duplicates `model_name` | `SE 210` + `Caravelle`, name `Caravelle` → blank | yes |
| `A+` | variant carries a name **already in** `model_name` | `CL-13` + `Sabre Mk.6`, name `Sabre` → `Mk.6` | yes |
| `A` | variant carries some other word | `CW-1` + `Junior` | **no — review** |

Roughly 560 rows fall in the automatic classes and 1,020 in `A`.

Class `A` is not automatable and the script does not try. The distinction it
would have to make is one a regex cannot: a **Spitfire Mk IX** and a **Canberra
Mk 20** are correctly written that way, while a **CM.170 Magister** is a name in
the wrong column. Only `model_name` vouching for the word makes it safe, which
is exactly what separates `A+` from `A`.

## Two things to keep in mind

**A 409 is a FINDING, not a failure.** Changing `variant` changes
`full_designation`, which is part of `uq_airframe (full_designation,
tail_number, operator_country)`. A 409 therefore means the corrected
designation now collides with another row — the same airframe is in the
database twice, and the cleanup has just proved it. Those are collected in
`variant_conflicts.tsv` rather than retried. This is the same shape as the c/n
recovery's 89 collisions in `data/CN_DUPLICATES.md`; adjudicate them the same
way, deciding which site actually holds the airframe.

**Generic designator words are never stripped.** `Ki-11` + `Type 91` with
`model_name` `Type 91 Fighter` looks exactly like the `A+` case — the word
`Type` really is in `model_name` — but stripping it leaves the bare number
`91`, which is worse than doing nothing. `type`, `model`, `series`, `mark`,
`variant`, `version`, `class` and `number` disqualify a row from `A+` and send
it to review.

## Known limitation

A designation sitting in the variant column with no word-like token in it is
invisible to every rule here: `Alouette II` + `SE 3130` reads as two marks.
Widening the name test to catch it would start eating correct variants like
`F.6` and `M4`, so those rows stay until someone reviews them by eye.
`tests/test_variant_cleanup.py` pins this rather than hiding it.
