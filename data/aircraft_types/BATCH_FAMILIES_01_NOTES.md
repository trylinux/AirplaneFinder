# Batch: families 01 — Sept 2026

Six type records, seventeen aliases. **Coverage 36.6% → 40.6%** (12,663 of
31,186 airframes), +1,235 including the aliases this batch enabled.

This was the first batch run under the `generate-aircraft-types` skill, and it
was chosen to test the skill's central claim: that the unit of work is an
aircraft, not a designation.

## Families collapsed

Six write-ups covering 622 airframes. Written one designation at a time, the
same six aeroplanes would have taken seventeen.

| type written | aliases | airframes |
|---|---|---|
| `H-19` Sikorsky Chickasaw / S-55 | Whirlwind (54), S-55↦Sikorsky (20), UH-19 (14), HO4S (6), WS-55 (4), HRS (1) | 124 |
| `C-45` Beech Expeditor | AT-11 (35), Expeditor (12), SNB (9), Model 18↦Beech (5) | 116 |
| `PT-17` Stearman Kaydet | N2S (24), PT-13 (21) | 103 |
| `DHC-1` Chipmunk | Chipmunk (46) | 101 |
| `OH-58` Kiowa / 206 JetRanger | 206↦Bell (32), 206↦Agusta-Bell (3) | 95 |
| `Sea King` | SH-3 (19), S-61 (9) | 83 |

Two of these were adjacent entries in the raw worklist and would have been
researched as separate aircraft: **DHC-1 (55) and Chipmunk (46)**, and
**OH-58 (60) and 206 (42)**.

Where the licence-built airframes outnumber the originals — 54 Westland
Whirlwinds to 25 H-19s, 55 Westland Sea Kings to 19 SH-3s — the description
says so explicitly, including the Gnome re-engining. The majority of readers
are standing in front of the British aircraft.

## Scope decisions

- **`206` needs two alias rows, not one.** Uniqueness is
  `(match_key, manufacturer_scope)`, so `206`↦Bell and `206`↦Agusta-Bell
  coexist. Necessary because "Agusta-Bell" does not prefix-match "Bell", and
  unscoped `206` would take in 5 Cessna 206s and 2 Beagle 206s.
- **`Model 18` scoped to Beech.** There are 6 Lockheed Model 18 Lodestars in
  the collection to 5 Beeches. "Beech" prefix-matches both "Beechcraft" and
  "Beech Aircraft", so the scope costs nothing.
- **`S-55` scoped to Sikorsky**, excluding a Soko and a Savoia-Marchetti S.55
  — the latter is a 1920s twin-hull flying boat.
- **Nothing else scoped.** `PT-17`, `N2S` and `PT-13` are Boeing (30),
  Boeing-Stearman (21) and Stearman (7) — three spellings of one Kaydet, and a
  scope would strip the write-up from most of them. Same for `Whirlwind`
  (Westland only) and `Chipmunk` (de Havilland Canada only).

## Figures rejected

Three of the six research agents returned a defect worth recording, all of the
same shape: **a Wikipedia specification block trusted without checking its own
heading.**

- **H-19.** The agent labelled the block `H-19D`. The heading is
  `Specifications (UH-19C)`, and the article text states an H-19D had the
  700 hp Wright R-1300-3 while the block lists the 600 hp P&W R-1340-57. The
  block is a UH-19C set. Relabelled `spec_basis: UH-19C` and the R-1340-57
  kept, so the figures and the engine describe one real aircraft. Had this
  gone in as written, 124 pages would have carried the wrong engine under a
  variant label the source never claimed.
- **DHC-1.** The agent labelled it `Chipmunk T.10`. The heading is the generic
  `Specifications (DHC-1 Chipmunk)` and the engine is a Gipsy Major 1C, not
  the T.10's Major 8. `spec_basis` now matches the source exactly.
- **PT-17.** The agent gave `retired_year: 1948`. Wikipedia's `retired` field
  is empty and the same article records Argentine N2S service into the early
  1960s. Dropped to null.

Separately, **four of six agents returned `engines` as an integer** (`2`)
rather than the powerplant designation. That column reads
"1 x Allison J33-A-35 turbojet"; stored as written it would have printed "2"
on ~400 pages. Every powerplant here was re-sourced individually.

`Sea King` keeps `max_speed_kmh` and `ceiling_m` null — the HAS.5 block does
not carry them, and no second source was mixed in.

## Blank on purpose

- **`retired_year` null on all six.** Every one of these types still flies
  somewhere, civil or military. The H-19 is the arguable case: the US Navy
  retired the CH-19E in 1969 and the RAF its Whirlwinds around 1981, but no
  single sourced date covers all operators of a family this widely exported,
  so it stays blank rather than asserting one.
- **`PT-17` `range_km`** — not in the PT-17 block, and not worth importing
  from a different variant.
- **`C-45` `also_built_by`** — the Model 18 was not licence-built.

## Data defects found

Research turned these up; they are data passes, not write-ups.

- **`Aircraft` (130) and `Light aircraft` (72)** remain the top two worklist
  entries and are not designations. Every row is manufacturer `Unidentified`.
  With `Unidentified` (308) that is 510 airframes whose model field records
  only that nobody knew.
- **`Hawk` (58) cannot be covered safely as it stands.** British Aerospace
  (41), BAE Systems (8) and BAe (4) are one jet trainer under three spellings
  that do not prefix-match each other, so no single `manufacturer_scope`
  covers them; and Pilcher (2), Curtiss (1), Cox (1) and CGS Aviation (1) are
  a hang glider, a biplane fighter and a microlight. Normalising the three
  BAE spellings first would make this writable.
- **`Hurricane` (57)** has one Sindlinger Hurricane — a homebuilt replica —
  filed under the same string as 55 Hawkers.
- **`Model 75` (4)** was left un-aliased: too generic a string to be worth
  four pages.
- **Westland Whirlwind is also a 1938 twin-engined fighter.** All 54 in the
  collection today are the helicopter (HAR/HAS marks), so the unscoped alias
  is safe *now*. If a Whirlwind fighter is ever imported it will silently
  inherit a helicopter write-up, and scoping cannot fix it — both are
  Westland. It would need a variant-level type record.

## Open question for a human

On an aliased page the card heading names the **type**, not the designation on
the page: a Westland Whirlwind HAR.10 now reads "About the H-19". That is
correct behaviour and may still read oddly to a visitor. 1,239 airframes now
reach a write-up through an alias, so this is worth a deliberate decision:
leave it, use the alias designation in the heading, or add a line naming the
relationship.
