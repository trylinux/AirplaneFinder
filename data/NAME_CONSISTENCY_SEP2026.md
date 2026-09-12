# Aircraft name consistency pass — 10 September 2026

Search on airplane.museum is a plain `LIKE %q%` across manufacturer, model,
variant, full_designation, model_name, aircraft_name and aliases. A family is
therefore only findable by a name if **every member carries that name
somewhere**. It didn't. Three separate failures were producing the symptom:

1. **43% of aircraft had no `model_name` at all** — 12,877 of 30,444 rows.
   Every one of them was invisible to a name search.
2. **Individual airframe names were sitting in `model_name`.** The two B-29s
   that would not answer to "Superfortress" were `Enola Gay` and `Bockscar`;
   the B-17 was `Shoo Shoo Baby`. A handful of records held a serial there.
3. **Spelling forms.** `super fortress` matched nothing, because the stored
   form is solid. Same for `Delfin` vs `Delfín`, `SeaCobra` vs `Sea Cobra`.

Variants were a fourth problem in their own right: a WB-50 is a modernised
B-29, so it should answer to Superfortress, and an RF-84F should be reachable
from Thunderjet. Nothing in the data connected them.

## What was done

**A curated name table of 1,228 aircraft families**, now at
`data/_research/aircraft_name_table.tsv`. Each family carries the popular name
that belongs in `model_name`, plus every other name any member is known by:
sibling names within the family (F-84 → Thunderjet, Thunderstreak,
Thunderflash), export and licence-built names (T-33 → Silver Star, T-Bird),
NATO reporting names (MiG-21 → Fishbed, Mongol), foreign-service names (F-4 →
Kurnass), RAF and Commonwealth names (C-47 → Dakota, T-6 → Harvard), and the
name of a closely related family of the same lineage — B-29 and B-50 both carry
Superfortress, CT-133 carries Shooting Star.

1,170 of the 1,228 families are marked high confidence. 346 are marked `NONE`,
meaning the type genuinely has no popular name — most trainers, homebuilts,
gliders and many Soviet types known only by their designation. That was a
deliberate instruction: a `NONE` is always better than an invented name.

**24,083 records were updated** across two passes:

| | rows |
|---|---|
| blank `model_name` filled from the family | 6,638 |
| `model_name` was a manufacturer restatement ("North American Mitchell") | 79 |
| `model_name` was a designation or a description | 71 |
| individual airframe names moved to `aircraft_name` | 21 |
| serial numbers moved out of `model_name` | 5 |
| aliases extended only | 16,668 |

No alias was ever removed — `PATCH /api/v1/aircraft/<id>` replaces the alias
list wholesale, so every call sends the existing list plus additions. Total
aliases went from 96,871 to 190,076; `model_name` coverage from 57% to 78%.

## Result

Every one of the 60 largest families now returns at least its own membership
when searched by its canonical name — zero shortfalls. Search hits usually
exceed family size, which is the cross-family aliasing working: "Sabre" pulls
Canadair CL-13s alongside the F-86s, "Silver Star" pulls the whole T-33 family.

| query | before | after |
|---|---|---|
| `super fortress` | 0 | 30 |
| `Superfortress` | 21 | 30 |
| `Thunderflash` | 52 | 283 |
| `Fishbed` | 232 | 767 |
| `Silver Star` | 43 | 550 |
| `Harvard` | 26 | 341 |

## Judgement calls worth knowing about

- **Variant names were kept, not flattened.** An F-84F still reads
  `Thunderstreak`; it simply gained Thunderjet and Thunderflash as aliases. The
  same for Freedom Fighter / Tiger II, Skytrain / Dakota, Kiowa / Kiowa Warrior.
- **NATO reporting names are never the canonical.** A MiG-21 has no popular
  name of its own, so `model_name` stays empty and `Fishbed` lives in aliases.
- **Off-list names were kept where they might be real.** 34 records hold a
  `model_name` the table does not recognise — sub-variant names like
  `Fishbed-B`, `Kittyhawk I`, `Tomahawk IIB`, `Jet Ranger II`, and designation
  strings like `DH.82A`. They were left alone and given the family name as an
  alias, so both spellings now find them.
- **Designation collisions were caught by keying on manufacturer as well as
  designation**, so North American F-100 Super Sabre never merged with Avro
  Canada CF-100 Canuck, nor Republic F-105 Thunderchief with the CF-105 Arrow.
  The curators flagged several more in the table's `note` column.

## Things the table flagged that are worth a look

- **Bell 205A-1 with `model_name` "Cheetah"** — Cheetah is the HAL/Aérospatiale
  Lama. Likely a misfiled name.
- **Boeing 707 records** carry `Stratoliner` (that belongs to the Model 307),
  plus `Zeus`, `Cóndor` and `El Al`, which are individual aircraft or an
  operator.
- **Harbin H-5** merges two unrelated aircraft: the H-5 rows are the licence-built
  Il-28 Beagle, but the SH-5 row is the maritime flying boat.
- **Sikorsky S-62 "Sea Guardian"** should be Seaguard; **Radioplane OQ-2
  "Shelduck"** — Shelduck is the OQ-19/KD2R.
- **Lockheed "TF-33"** is an engine designation, not an aircraft; those rows are
  T-33s.

## Re-running it

`scripts/README_name_normalisation.md` documents the whole loop. It is
idempotent and resumable, and worth re-running after any large import — a second
pass over records added by concurrent work while this one ran picked up another
680. Note that the API returns a transient HTTP 500 on a minority of concurrent
alias writes; the applier retries and a repeat run clears the remainder. Two
worker threads is about the useful limit.

## Not done

The repo's `data/**/*.csv` files were not rewritten, so their `model_name` and
`aliases` columns are now behind the live database. They are import sources
rather than a mirror, and re-importing skips existing rows, so nothing breaks —
but a future import built from those files would reintroduce the old sparse
names unless the table is applied at build time. The full test suite passes
(87,431 tests).
