# Castle Air Museum — import notes

Two import files, compiled September 2026:

| File | Rows | Import into |
|---|---|---|
| `castle_air_museum_museum.csv` | 1 | `POST /api/v1/museums/bulk_import` |
| `castle_air_museum_aircraft.csv` | 94 | `POST /api/v1/aircraft/bulk_import` |

**Import the museum file first.** Every aircraft row carries
`museum_name=Castle Air Museum`, which the importer resolves against
existing museums. If Castle isn't in the database yet, all 94 rows fail
validation and the batch rolls back — deliberately, so you never end up
with 94 unlinked aircraft.

```bash
# 1. dry run both
curl -H "Authorization: Bearer $KEY" -F file=@data/castle_air_museum_museum.csv \
     -F dry_run=1 https://your-host/api/v1/museums/bulk_import
# 2. real import, museum first
curl -H "Authorization: Bearer $KEY" -F file=@data/castle_air_museum_museum.csv \
     https://your-host/api/v1/museums/bulk_import
curl -H "Authorization: Bearer $KEY" -F file=@data/castle_air_museum_aircraft.csv \
     https://your-host/api/v1/aircraft/bulk_import
```

Or use `/admin/import` — Aircraft tab, Validate (dry run), then Import.

Expected result: `created: 94, linked: 94, skipped: 0, errors: []`.

## Source of record

The museum's own [collection listing](https://castleairmuseum.org/collection/)
is the authority for what is currently on the grounds and for the markings
each airframe wears. Where Wikipedia or Skytamer disagree, the museum's
listing wins — see conflicts below.

## What's in the file

- **91 rows `on_display`** — everything on the museum's public collection page.
- **3 rows `under_restoration`** — at the museum but in the restoration
  hangar, not yet on the display grounds:
  - **F-117A Nighthawk 85-0813 "Toxic Avenger"** — Desert Storm veteran,
    arrived from Tonopah July 2022, wings reinstalled, still being prepared.
  - **TBM Avenger** — ditched off Daytona Beach 2022, received May 2024.
  - **Hiller UH-12** — donated December 2023.

  Drop these three rows if you only want the public display grounds.

- By type: 83 fixed-wing, 7 rotary-wing, 4 missile/rocket.
- The missile/rocket rows are the AGM-28 Hound Dog, GAM-63 Rascal, ADM-20
  Quail, and the Mk.17 thermonuclear weapon shape. The Ryan BQM-34 Firebee
  and Kawasaki KAQ-1 are target drones, so they're `fixed_wing` with
  `role_type=drone` rather than `missile_rocket`.
- The Mk.17 is a free-fall bomb shape, not a missile. It has no clean home
  in the `aircraft_type` enum; it's filed under `missile_rocket` (the
  "unmanned expendable flight vehicle" bucket) with an empty `role_type`.

## Field decisions

**`tail_number` holds the markings the aircraft actually wears**, per the
museum's listing — not necessarily the airframe's construction serial.
Several aircraft are painted as other airframes:

| Aircraft | In the file | Actual airframe (per Skytamer) |
|---|---|---|
| Douglas A-26B Invader | 44-35648 | 41-39472 |
| Convair F-106A Delta Dart | 58-0793 | 58-0798, displayed as 57-2456 |
| North American F-100 Super Sabre | 53-1709 | displayed as F-100D 55-2879 |
| North American B-25J Mitchell | 44-86891 | displayed as B-25B 40-2344 |
| Lockheed F-104 Starfighter | 57-1314 (D) | 57-1330, displayed as 57-1312 |

**`year_built` is derived from the USAF fiscal-year serial prefix** where
the serial encodes one (62 of 94 rows). That prefix is the fiscal year of
the procurement contract, so delivery was often the following calendar
year — treat these as ±1. Rows with Navy BuNos, foreign serials, or no
serial have `year_built` blank rather than a guess.

**`aliases`** are semicolon-separated, and include the compact form
(`B17`), the popular name (`Flying Fortress`), and nicknames (`BUFF`,
`Thud`, `Habu`) so search finds them the way visitors ask.

## Conflicts and soft spots

Worth a curator's eye before or after import:

1. **B-17G tail** — museum says 43-38635; Skytamer says 43-8635.
2. **B-29 tail** — museum says 44-61535; Skytamer says 44-70064 and calls
   it a B-29A. File follows the museum, variant left blank.
3. **HH-43B Huskie** — museum says 62-4213; Skytamer says 62-4513.
4. **R5D-4 Skymaster** — museum says 44-9137; Skytamer says BuNo 90407.
   `year_built` left blank because the two imply different years.
5. **HC-131A Samaritan** — museum lists "#133", which looks truncated;
   Skytamer says it's a Convair 240 (N1018C) displayed as USCG CG-5785.
   **`tail_number` left blank** rather than record a partial value.
6. **EC-121 Warning Star** — the museum's "#1049A-4335" is a Lockheed
   construction number, not a tail number. Recorded as given.
7. **Stinson L-5 "76-3419"** — an L-5 should carry a 42-/44- series
   serial; recorded as the museum gives it, but it looks off.
8. **SBD-4 Dauntless "100508"** — sits suspiciously close to the CF-100's
   RCAF serial 100504 on the same page. Recorded as given.
9. **Serial formatting normalised** in two places where the museum runs
   the digits together: PT-23 `4249354` → `42-49354`, RA-3B `14-4843` →
   `144843` (BuNo). Same numbers, standard formatting.
10. **Manufacturer follows the museum's labelling.** Notably the F/A-18C
    is listed as Boeing (McDonnell Douglas designed it) and the AV-8B and
    F-4S as McDonnell Douglas.

## Duplicate check (September 2026)

Checked the museum's live collection page against this file:

- **91 entries on the site, no duplicate listings.** The category tabs
  appear to sum to more than 91 because the RB-36H Peacemaker and RA-5C
  Vigilante are each filed under *both* Bomber and Reconnaissance. Two
  categories, one airframe — not a duplicate. Both are `role_type=recon`
  here, matching their R-for-reconnaissance designations.
- **No duplicates inside this file**: no repeated `(model, tail_number)`,
  no repeated tail number, and no two rows sharing
  `(manufacturer, model, variant)` — the grouping
  `scripts/dedupe_aircraft.py` uses. Rows that share a *model* are
  genuinely different airframes (F-84C vs F-84F, F-4E vs F-4S).
- **One collision found and fixed, in the seed data.** `seed_data.py`
  listed B-52D **56-0612** as Dayton's aircraft; 56-0612 is Castle's.
  Importing this file into a seeded database would have reported that row
  as an existing duplicate and rolled back all 94 rows. The seed now uses
  Dayton's actual B-52D, **56-0665**. `tests/test_castle_import_file.py`
  fails if the two files ever share a tail number again.

## Re-generating

The files are generated data, not hand-maintained. `tests/test_castle_import_file.py`
imports both through the real endpoints on every test run, and checks the
enum values, role vocabulary, and duplicate `(model, tail_number)` pairs.
