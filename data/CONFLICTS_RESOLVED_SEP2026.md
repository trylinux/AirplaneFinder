# Airframe conflicts — all 46 adjudicated, 12 September 2026

Every conflict where one airframe was recorded at two sites hundreds of
kilometres apart has been researched and decided. **19 non-destructive fixes are
already applied live.** 24 deletions are staged in
`scripts/delete_conflicts_sep2026.sh`, and 5 identity moves are blocked until
those run.

| verdict | n | meaning |
|---|---|---|
| A or B | 30 | one site has it, the other's record is wrong |
| FALSE-COLLISION | 6 | never a duplicate — the detector was wrong, not the data |
| BOTH | 8 | both sites really do have an aircraft; one had the wrong identity attached |
| NEITHER | 2 | the airframe is at a **third** site |

## The detector was wrong six times, and that matters more than the data

`_find_aircraft_duplicate` treats a match on manufacturer + construction number
as proof of the same airframe. **A construction number is only unique within a
type series.** Six "duplicates" were nothing of the kind:

- Bell model 47 c/n 1090 and Bell model 204 c/n 1090 are different helicopters.
- Grumman G-63 c/n 1 and Grumman G-1159 c/n 1 are a Kitten and the first
  Gulfstream II.
- Fairchild PT-26 c/n 10846 and Fairchild C-119 c/n 10846.
- FMA IA-50 c/n 22 and FMA IA-35 c/n 22.
- Lockheed C-130E: Baugher settles it — 63-7877 is MSN 382-3948, 62-1862 is
  MSN 382-3826. One of ours carried the other's number.

Worse, **the literal string `unknown` was being used as a join key.** One record,
id 24421 at Hancock Field, collided against four different F-84F serials at once
purely because both sides read `unknown`. Those eight placeholder values have
been nulled. The underlying weakness is in the application, not just the data,
and it will recur on every import: **the c/n index should be scoped by type
series, not by manufacturer, and placeholder strings should never be stored.**

## One site holds nothing at all

**Veterans Memorial Park, D'Iberville MS** was the paste destination for five
airframes. Overpass returns zero `historic=aircraft` nodes within 1,500 m of it,
no source places any aircraft there, and — decisively — its rows were copied from
*three different Tennessee parks*, which one source record cannot be. All five
rows are staged for deletion.

Two other sites are the same shape on a smaller scale: **Veterans Memorial Park,
Dixon IL** (its own listing has an F-105D and an AH-1G, nothing else) and
**Veterans Park, Ryan IA** (which does hold an unidentified Cobra, so its
identities were blanked rather than its records deleted).

## How the errors were made

Half the conflicts had **byte-identical description text on both rows** — the
fingerprint of a research pass reading one Aerial Visuals dossier or OSM node and
pasting it onto several sites. In one case the pasted text carried the source's
own coordinate, `40.390672 -80.594217`, which is Weirton WV — sitting in a record
filed under a New Jersey park 400 km away. The record refuted itself.

This is a defect in my own overnight US state run. Worth a guard in the builder:
**two sites must never share a description string.**

## Two airframes were at a third site entirely

- **TA-4J 158479** is at Veterans Memorial Park of Delta County, Gladstone MI —
  recorded at Oglesby IL and Dixon IL, neither of which has it.
- **A-6E 152603** moved to Wayne County Veterans Memorial Park, Richmond IN on
  10 April 2022 — recorded at Oglesby and Dixon.

Two agents working different batches reached the same answer independently.

## Three type errors found in passing

- id 34192 was filed as an **Il-86**; the July 2026 OSM node names it outright as
  Ilyushin **Il-103 RA-10300**. Corrected.
- id 25705 was a **Grumman G-63**; it is the first **G-1159 Gulfstream II**.
- id 24421 was an **F-84F**; it is **F-84B 46-600**, at Lackland until 1994.

## One record is a write-off

**C-47B 43-49942 / N47HL "Bluebonnet Belle"** burned out on takeoff from Burnet
on 21 July 2018. The surviving CAF Highland Lakes Dakota is a different airframe,
44-77109 c/n 16693 "Texas Zephyr", gifted December 2019 — now recorded correctly.

## Running the rest

```bash
AIRPLANE_KEY=amt_… bash scripts/delete_conflicts_sep2026.sh   # 24 deletions, one prompts
AIRPLANE_KEY=amt_… python3 scripts/retry_patch.py             # frees the last 5 identity moves
```

Every deletion carries its reason inline. The one low-confidence call — the
Mount Clemens Huey, where the site is disproven but the airframe is unplaced —
prompts before deleting.

Per-conflict evidence with URLs and dates: `data/_research/resolved_batch{1,2,3}.md`.
