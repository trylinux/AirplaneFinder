# California aviation museums — build notes

Working from AeroCorner's ["65 Aviation Museums in California"](https://aerocorner.com/blog/aviation-museums-in-california/)
as the starting list, then verifying each against its own site.

## Phase 1 (this file): museum records

`ca_museums.csv` — **43 museums** to add, ready for
`POST /api/v1/museums/bulk_import`. Import this before any aircraft file,
since aircraft rows resolve their museum by name.

- 37 of 43 have verified coordinates. Six do not, and **will not appear on
  the globe or in proximity search** until they get them: Alameda Naval Air
  Museum, Golden Age Flight Museum, Tomorrow's Aeronautical Museum, West
  Gate Century Circle, Air Group One CAF, NTC & 11th ACR Museum. Coordinates
  were left blank rather than guessed from a city centroid, which would put
  a pin in the wrong place and quietly corrupt "nearest museum" results.
- 23 publish a collection page — those are the ones that can be inventoried
  accurately. See `ca_museums_collection_sources.csv`.
- Known counts alone imply **~838 aircraft**, and that excludes the seven
  museums that publish no count.

## Excluded, and why

Of the 65 on the source list, **14 were dropped**. Each is a real finding,
not an omission:

**Permanently closed**

| Museum | Detail |
|---|---|
| Milestones of Flight (Lancaster) | Closed since ~2015 |
| Central California Historical Military Museum (Firebaugh) | Fixed site closed; successor is a travelling collection with no public address |
| California Flight Museum (San Diego) | Closed at Brown Field, no successor found |
| California Army National Guard Museum (San Luis Obispo) | Defunct; three aircraft transferred to Estrella Warbirds in Feb 2025 |
| Museum of the Forgotten Warriors (Marysville) | Closed to the public since June 2023, land-title dispute |

**No aircraft at all** — Exploratorium, Whittier Museum, Oakland Museum of
California, Kern County Museum, Louis A. Turpen Aviation Museum (SFO — an
aviation library and artifact museum, no airframes).

**Other**

- **Richard Nixon Presidential Library** — its only aircraft, the VH-3A Sea
  King, was removed 28–29 June 2026 for multi-year restoration **at March
  Field Air Museum**, not due back until ~2028. Zero aircraft today. Worth
  noting because that helicopter is currently *at* a museum already in your
  database.
- **P-38 Museum (March ARB)** — the only P-38 on site is a fibreglass
  replica. The association's real P-38 was sold and is now at Fagen Fighters
  in Minnesota.
- **Flying Leatherneck Aviation Museum** — closed at MCAS Miramar in April
  2021; its 31 aircraft moved to Hangar 297 at Orange County Great Park,
  Irvine (move completed Dec 2024). New building broke ground Oct 2025,
  public opening expected **Fall 2027 / Spring 2028**. The aircraft exist and
  are in California, but no visitor can see them, so it is held back rather
  than listed as somewhere to go. Add it when it opens.
- **NASA Ames Exploration Center** — genuinely ambiguous. NASA's own page
  says Ames hosts no public tours and redirects visitors to Chabot in
  Oakland; third-party listings still show it operating. Needs a phone call.

## Renames and moves worth knowing

- **Saxon Aerospace Museum → Boron Aerospace Museum** (renamed 2017).
- **Golden Age Flight Museum** left Bakersfield for **Tehachapi** in 2022.
- **Hillier Air Museum (Modesto)** is a different institution from **Hiller
  Aviation Museum (San Carlos)**. Similar names, one letter apart, both in
  California. Do not merge them — Hiller (San Carlos) is already in the
  database as id 56.
- **Moffett Field Historical Society Museum** now brands as **Moffett Field
  Museum**.
- **American Society of Military History** now trades as **The American
  Military Museum** ("Tankland"). The General Patton Memorial Museum is a
  separate institution ~140 miles away in Chiriaco Summit.

## Low-confidence records to sanity-check

- **Stockton Field Aviation Museum** — site content looks stale (2011-era);
  Yelp says closed as of April 2026. Included, but verify.
- **Tomorrow's Aeronautical Museum** — official site last updated ~2014.
- **The Proud Bird** — a restaurant with aircraft, some of them replicas.
- **American Veterans Memorial (Tulare)** — a roadside AMVETS memorial, not
  a staffed museum. Its B-17G "Preston's Pride" is on loan from the National
  Museum of the USAF.
- **Museum of Flying (Santa Monica)** — official site shows current hours,
  Yelp says closed. Conflicting.

## Phase 2 progress

| File | Rows | With tail no. | Import status |
|---|---|---|---|
| `yanks_air_museum_aircraft.csv` | 138 | 31 (22%) | validated, 0 errors |
| `planes_of_fame_aircraft.csv` | 145 | 44 (30%) | validated, 0 errors |
| `flight_test_museum_aircraft.csv` | 81 | 71 (88%) | validated, 0 errors |
| `estrella_warbirds_aircraft.csv` | 39 | 37 (95%) | validated, 0 errors |
| `pacific_coast_air_museum_aircraft.csv` | 34 | 2 (6%) | validated, 0 errors |
| `classic_rotors_aircraft.csv` | 34 | 16 (47%) | validated, 0 errors |
| `travis_afb_aircraft.csv` | 33 | 33 (100%) | validated, 0 errors |
| `oakland_aviation_museum_aircraft.csv` | 20 | 19 (95%) | validated, 0 errors |
| `aerospace_museum_of_california_aircraft.csv` | 16 | 15 (94%) | validated, 0 errors |
| **Total** | **540** | **267 (49%)** | |

Run it all with `bash scripts/import_california.sh --dry-run` first.

### Per-museum caveats (batch 2)

- **Aerospace Museum of California — only 16, not the ~40 advertised.** Their
  live collection page lists 16; Wikipedia lists 40+ types (F-14D, MiG-17,
  FB-111A, EC-121D…) from 2016-era archived pages with dead citations. Not
  included, since the current primary source doesn't confirm them. Worth a
  phone call — this may be the single biggest gap in the whole set.
  Two of their aircraft wear *other* airframes' serials: F-102A 56-1140 is
  painted as 55-431, and F-100D 56-3288 as 55-3777. Real serials used.
  Their page titled "F-80B Shooting Star" actually describes a T-33A
  (53-5205) in its own specifications — recorded as the T-33A.
- **Classic Rotors is the weakest data in the set.** Their per-aircraft pages
  contain *no text at all*, only photo galleries — the researcher recovered
  identities from image filenames. Three entries had no identifiable
  manufacturer and were dropped. Two tail numbers (UH-1N 158256, HH-46E
  157688) came from photo captions rather than placards. Treat this file as
  a starting point to verify on site, not as authoritative.
- **Pacific Coast Air Museum publishes no serials whatsoever** — 2 of 34, and
  both of those came from third-party airframe dossiers, not the museum.
  Almost every detail page on their site is an empty template.
- **Travis is the cleanest file in the set: 33 aircraft, 100% with serials.**
  One F-4C (63-7567) excluded — the museum's own page says it sits at the
  David Grant Medical Center gate, a separate location on base. Several
  included aircraft are dispersed around the base rather than in the airpark
  (C-54D at the Base Exchange, C-141B on Burgan Blvd) but remain museum
  inventory. Their "F-100" page is headed "F-101A Super Sabre" — an internal
  labelling error on their side; recorded as F-100.
- **Estrella** includes three aircraft transferred from the closed California
  Army National Guard Museum (OH-23C, O-1A, U-6A) — the transfer this file
  set predicted. Several listed aircraft are privately owned and flyable
  (notably C-47B "Betsy's Biscuit Bomber") so may not always be on site.
  Its UH-34D and UH-19D are composite airframes, so their serials describe
  the aircraft as displayed rather than one clean identity.
- **Oakland** includes two nose-section-only airframes (DC-6BF N444SQ,
  S-2A 136624), kept as rows and flagged in `aliases`. Excluded a 1/50-scale
  dirigible model and two aircraft the registry marks "Removed".

`wing_type` is now populated on all three by `scripts/fix_wing_type.py`:
307 monoplane, 37 biplane, 1 triplane (the Fokker Dr.1), 19 correctly blank
for helicopters, missiles and the one spacecraft. The classifier keys on
(manufacturer, model) rather than model alone, because a Pitts S-2 is a
biplane while a Grumman S-2 Tracker is a monoplane.

### Air Force Flight Test Museum — aircraft deliberately excluded

Its published inventory includes airframes that are **not at Edwards**.
Listing them under the Flight Test Museum would repeat the B-52D error:

| Aircraft | Actually at |
|---|---|
| Lockheed A-12 60-6924 | Blackbird Airpark, Palmdale (museum id 51) |
| Lockheed D-21B | Blackbird Airpark |
| Lockheed SR-71A 61-7973 | Blackbird Airpark |
| Lockheed U-2D 56-6721 | Blackbird Airpark |
| Grumman X-29 82-0049 | NASA Armstrong (museum id 52) |
| McDonnell F-4C 64-0741 | Mojave Airport (not a museum) |

The first five belong in the Blackbird Airpark / Armstrong **top-ups**, not
here. Also dropped: a duplicated C-141A 61-2779 row, and seven other
repeats caused by broken links on the museum's own inventory page.

**Probable duplicate against live data:** your database already holds
`NB-52 | 52-008`. The Flight Test Museum file lists the same airframe —
"Balls 8", the X-15 mother ship — as `B-52 | 52-0008`. Different model
prefix and a different zero-padding, so the importer's exact-match check
will **not** catch it and you will end up with two records for one
aircraft. Reconcile these by hand before or after import.

Both were checked against the live database's existing `(model, tail_number)`
pairs, so neither can trigger the rollback-on-collision problem.

### Known limits of these two files

- **Tail numbers are sparse** — 75 of 283 rows have one. Both museums
  organise their sites by aircraft *type* and publish serials only on some
  detail pages. Blank was recorded rather than guessed; blank tails never
  collide in the duplicate check, so they import safely, but those airframes
  can't be uniquely identified later.
- **`wing_type` is blank throughout.** Both collections are full of biplanes
  and at least one triplane (Fokker Dr.1), so the blanket "monoplane" used
  in the Castle file would have been wrong dozens of times.
- **`description` is blank throughout.** Neither site publishes a consistent
  per-airframe description worth transcribing.
- **Yanks is under-documented at source.** Wikipedia says the collection
  "exceeds 190 aircraft"; the museum's own site itemises ~125. The gap is
  aircraft in storage and the restoration hangar that nobody lists publicly.
  138 rows is the best available *public* documentation, not a full physical
  count.
- **Planes of Fame has a second site in Valle, Arizona.** Their listing does
  not distinguish it. Five airframes whose photos carried "valle" filenames
  were **left out** rather than risk attributing an Arizona aircraft to
  Chino — the same error class as the B-52D. Also excluded: a Bristol F.2b
  pair, an F11F Tiger, a Vampire F.3, a second Stearman PT-17, a Goodyear
  blimp gondola (a component, not an airframe), and a "Douglas B-17G" entry
  that looks like a source error.
- Planes of Fame lists ~53 aircraft as "Storage" at Chino. Those **are**
  included — the storage hangars are on the Chino field — but they're not on
  the public display floor, so `under_restoration` may fit some better than
  `on_display`.

## Phase 2: remaining aircraft inventories

Per-museum CSV files, same shape as the Castle file, one museum each so a
bad row can never take down another museum's import. Priority order by
collection size:

1. Yanks Air Museum (~190)
2. Planes of Fame (~100)
3. Air Force Flight Test Museum (~85)
4. Classic Rotors (~45)
5. Aerospace Museum of California (~40)
6. Estrella Warbirds, Pacific Coast, Travis AFB (~35 each)
7. Oakland Aviation, USS Midway (~30 each)
8. …then the long tail

**Top-ups for museums already in your database** (fetch full collection,
diff against what's live, emit only what's missing):
San Diego Air & Space (5 of ~120), Hiller Aviation (4 of ~40),
Palm Springs (43 of ~75), Armstrong (6), Blackbird Airpark (1 of ~4),
Beale AFB (1), Reagan Library (1).
