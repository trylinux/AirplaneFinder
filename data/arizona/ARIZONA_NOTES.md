# Arizona — build notes

Strategy shift from California: rather than sweeping a whole state, this
phase tops up the **big museums already in the database that are showing
almost nothing**. Arizona first, because Pima is the largest single gap
anywhere in the dataset.

## Pima Air & Space Museum (id 23) — 5 recorded, ~366 real

Pima publishes a WordPress REST feed at
`pimaair.org/wp-json/wp/v2/museum_aircraft`, which is far better than
scraping the HTML: it exposes per-airframe Manufacturer / Markings /
Designation / Registration / Serial Number fields. **366 aircraft records
site-wide.** That also corrects the widely-quoted "~425" figure.

Split by manufacturer initial so each slice is a manageable research pass.

| File | Slice | Rows | Tails |
|---|---|---|---|
| `pima_topup_a_to_f_aircraft.csv` | manufacturers A–F | 142 | 140 (**98%**) |
| _(pending)_ | G–M | ~110 | |
| _(pending)_ | N–Z | ~110 | |

**98% serial coverage is the best in the whole project** — better than
Travis or Joe Davies, and far better than the 44% California average.
Pima publishes a serial for nearly every airframe.

Already recorded, excluded from the top-up: Boeing VC-137B 58-6971 (A–F),
plus Lockheed C-130E 62-1787, P-38L 44-53236, F-16C 84-1301 and
SR-71A 61-7951, which fall in the L slice.

### A–F caveats

- **8 aircraft are `in_storage`** and 2 `under_restoration`, taken from
  Pima's own "not currently on public display" wording rather than assumed.
- **Four are on loan or displayed off Pima's own grounds** but remain in
  their catalogue, so they are kept: the Curtiss F6C-4 Hawk (National
  Museum of the Marine Corps), the AIR-2 Genie (NMUSAF), the Bell UH-1F
  (physically at the adjacent **Titan Missile Museum**), and the B-17G
  (at the **390th Memorial Museum** on the same campus). If you ever add
  those two as separate museums, these three should move.
- **Three are missiles**, in Pima's own aircraft catalogue: AIR-2 Genie,
  SM-75 Thor, Fi 103 (V-1). Typed `missile_rocket`.
- **One `lighter_than_air`** — the Avian Falcon II balloon.
- A source bug: Pima's own Manufacturer field reads "Brewster" for the
  Bowers Fly Baby, an obvious copy/paste error. Corrected to Bowers.
- The Bolingbroke is recorded under **Fairchild Aircraft Ltd** (the Canadian
  licensee), which is what Pima's page says, rather than Bristol.
- No AMARG/boneyard aircraft appeared in this slice — the adjacent boneyard
  is not part of the museum and is excluded by policy.

## Other Arizona museums in the database

**Commemorative Air Force Airbase Arizona** (id 29, Mesa) — 0 aircraft.
Not yet researched.

Worth adding later: Titan Missile Museum (Sahuarita), Planes of Fame Valle
— note the Valle site is the one whose aircraft were deliberately excluded
from the Chino file, so it has a ready-made starting list in
`../california/CALIFORNIA_NOTES.md`.
