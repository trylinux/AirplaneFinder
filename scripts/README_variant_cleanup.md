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
| `E` | variant is `[mark] + name` and `model_name` is **empty** | `31-55` + `A Senior Skyrocket` → variant `A`, model_name `Senior Skyrocket` | yes |
| `A` | the name would overwrite a different `model_name` | `47` + `J-2 Ranger`, model_name `Sioux` | **no — review** |

Against the live catalog: **250 rows in the plan, 154 to review.**

Class `E` is the one that actually moves a name out of the variant column. `A+`
and `D` only work when `model_name` already holds the name, so on their own they
never populate it — `E` is what fixes `CT-133` + `Silver Star 3` into variant
`3`, model_name `Silver Star`. Marks are taken from **both ends** of the string,
which is how the trailing `3` there ends up in the right place.

Class `A` is what is left, and it is not automatable. A **Spitfire Mk IX** and a
**Canberra Mk 20** are correctly written as they are, and where a name really is
in the wrong column the existing `model_name` is often equally right: a Bell 47
is a **Sioux** in military service and a **Ranger** as the civil J-2; a Stinson
108-1 is a **Voyager** and a 108-2 a **Flying Station Wagon**. The review file
prints `candidate_mark` and `candidate_name` next to the existing `model_name`,
so the decision is between two named options rather than an abstraction.

Some of those 154 are plain errors worth fixing: `95` + `B55 Baron` with
`model_name` `Travel Air` is a Beech 95-B55 Baron, and the Travel Air is a
different aeroplane.

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

**Upper-case tokens are variant CODES, not names.** `AJSF` on a Saab 37, `GCBC`
on a Citabria 7, `A-II`, `SIGINT` on an Atlantic — an earlier version of this
script read those as type names and sent 61 correct rows to review. Names in
this catalog are Title Case, so requiring upper case costs nothing and rescues
all of them.

## Known limitation

A designation sitting in the variant column with no word-like token in it is
invisible to every rule here: `Alouette II` + `SE 3130` reads as two marks.
Widening the name test to catch it would start eating correct variants like
`F.6` and `M4`, so those rows stay until someone reviews them by eye.
`tests/test_variant_cleanup.py` pins this rather than hiding it.
