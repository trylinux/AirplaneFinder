# Normalising manufacturer spellings

`manufacturer` is a facet visitors filter on, so one company spelled two ways
splits its own results — and `_find_aircraft_duplicate` scopes its construction
number match by manufacturer, so a split spelling also hides duplicate airframes
from the dedupe sweep.

30 manufacturer names in the catalog are spelled more than one way. They fall
into three classes that do **not** get the same treatment.

## Running it

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/plan_manufacturers.py
    # read manufacturer_summary.txt and manufacturer_review.tsv, then:
    python3 scripts/apply_manufacturers.py --dry-run
    AIRPLANE_API_KEY=amt_... python3 scripts/apply_manufacturers.py

`plan_manufacturers.py` writes nothing to the database. `apply_manufacturers.py`
is resumable — ids land in `applied_manufacturer_ids.txt` as they go — and
`--only T` or `--only D` restricts a run to one class.

## The three classes

**T — transliteration (121 rows).** German and Polish renderings of Russian
bureau names, against the canonical spelling already dominant in the same
column:

| | rows | | rows |
|---|---|---|---|
| Mikojan-Guriewicz | 60 | → Mikoyan-Gurevich | 1,686 |
| Suchoj | 37 | → Sukhoi | 486 |
| Jakowlew | 15 | → Yakovlev | 361 |
| Antonow, Tupolew, Lisunow, Polikarpow, Petlakow | 9 | | |

This is a **curated map, not a rule**, and it has to stay that way. Bölkow,
Schleicher, Lommatzsch, Messerschmitt, Barkley-Grow, Snow, Arrow and Harlow all
carry the `-ow` / `-sch` shapes a general rule would match, and all are correct.

`Mikoyan` on its own is **not** in the map: post-Gurevich aircraft (MiG-29,
MiG-31) are correctly filed that way. It is a different company name, not a
short spelling.

**D — accents (248 rows).** `Aerospatiale` → `Aérospatiale`, `Zlin` → `Zlín`,
`Blériot`, `Bücker`, `PZL-Świdnik`, `Hispano Aviación`, `ICA Braşov`,
`PZL-Okęcie`, `Orličan`, `Peenemünde`, `Malmö Flygindustri`, `Donnet-Lévêque`.

The rule is **prefer the accented form regardless of how common it is**.
Frequency is not evidence here: `Zlin` outnumbers `Zlín` 39 to 28 and is still
the transcription loss, and `Aerospatiale` vs `Aérospatiale` is a 100/101 coin
flip.

**Breguet is the exception the exception list exists for.** Louis Charles
Breguet's surname takes an accent, but the aircraft company wrote itself
*Breguet* — Breguet 19, Breguet Atlantic — and the references follow it. The
plan therefore moves 7 rows from `Bréguet` **to** `Breguet`, against the rule.
No rule can infer that; `ACCENT_EXCEPTIONS` in `plan_manufacturers.py` is where
the next one goes.

**C — case only (9 names, review).** Never automatic, because it is an acronym
question:

    de Havilland 582 / De Havilland 22      Saab 315 / SAAB 2
    Soko 82 / SOKO 1                        Let 60 / LET 21
    Erco 18 / ERCO 9                        Socata 16 / SOCATA 10
    RotorWay 12 / Rotorway 6                Sagem 3 / SAGEM 2

`manufacturer_review.tsv` shows the majority spelling as a *suggestion*, and for
at least two of these the majority is wrong: **ERCO** is Engineering and
Research Corporation and **SOCATA** is Société de Construction d'Avions de
Tourisme et d'Affaires — both genuine acronyms that should stay capitalised even
though the lower-case form is more common in the data. Decide each one, then
either add it to the transliteration-style map or fix it in admin.

## What to expect afterwards

Manufacturer is not part of `uq_airframe (full_designation, tail_number,
operator_country)`, so unlike the variant pass these writes cannot collide and a
409 here would be a surprise.

The second-order effect is the useful one. `_find_aircraft_duplicate` matches a
construction number **scoped by manufacturer**, so two records for the same
airframe filed under `Suchoj` and `Sukhoi` could not previously be recognised as
duplicates. Normalising the spelling makes them visible — so expect the next
duplicate sweep to surface new pairs, and treat that as the pass working rather
than as new damage.
