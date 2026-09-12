# Aircraft name normalisation

`data/_research/aircraft_name_table.tsv` is a curated table of 1,228 aircraft
families: for each one, the popular name that belongs in `model_name` and every
other name the family is known by, which belong in `aliases`.

It exists because search (`_build_aircraft_filter` in app.py) is a plain
`LIKE %q%` across manufacturer, model, variant, full_designation, model_name,
aircraft_name and aliases. That means a family is only findable by a name if
**every** member of it carries that name somewhere. Before this pass, 43% of
aircraft had no `model_name` at all, some B-29s carried `Enola Gay` where
`Superfortress` belonged, and `super fortress` matched nothing because the
stored form was solid.

## The table

| column | meaning |
|---|---|
| `family` | base designation with the mission-modifier prefix stripped (`WB-50` → `B-50`), or the type name where the model is not a designation |
| `mfr_key` | normalised manufacturer, so Republic F-84 and Avro CF-105 never merge |
| `canonical` | the name to write into `model_name` when a record has none; `NONE` where the type genuinely has no popular name |
| `also_known_as` | every other legitimate name for any member of the family — sibling names, export and licence-built names, NATO reporting names, foreign-service names, RAF/Commonwealth names, and the name of a closely related family of the same lineage (a B-50 is a modernised B-29, so both carry Superfortress) |
| `variant_rules` | `MODEL=Name` pairs where members of one family carry genuinely different primary names |
| `confidence` | `high` or `low`; 1,170 of 1,228 are high |
| `note` | anything that needed saying — a merged designation, a misfiled name, a spelling to watch |

## Running it

    python3 scripts/snapshot.py            # pull the live database to a local cache
    python3 scripts/plan_names.py          # diff the cache against the table
    AIRPLANE_KEY=amt_... python3 scripts/apply_names.py

`plan_names.py` writes `name_plan.json` and changes nothing. `apply_names.py`
PATCHes only what the plan lists, logs every id it lands to `applied_ids.txt`,
and is resumable — re-run it until it reports zero errors. It never removes an
existing alias: the alias list it sends is the old list plus additions, because
`PATCH /api/v1/aircraft/<id>` **replaces** aliases wholesale.

`overrides.py` holds the hand-adjudicated records: `MOVE` for genuine individual
airframe names that belong in `aircraft_name` (Enola Gay, Bockscar, Shoo Shoo
Baby, Mei-Ling), `REPLACE` for model_name values that were really a designation
or a description.

Re-run the whole thing after any large import; it is idempotent.

## Things to know

- The API returns HTTP 500 on a minority of concurrent alias writes. They are
  transient — the applier retries, and a second run clears the rest. Two worker
  threads is about the useful limit.
- `variants()` in `plan_names.py` generates the spelling forms a substring search
  would otherwise miss: accent-stripped (`Delfín` → `Delfin`), camel-split
  (`SeaCobra` → `Sea Cobra`), solid (`Sea Cobra` → `SeaCobra`), and a hand list
  for solid compounds that are not camel-cased (`Superfortress` →
  `Super Fortress`). It deliberately does not de-space names with digits or
  three words, which only produced unreadable noise.
