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
| `uss_midway_aircraft.csv` | 35 | **0 (0%)** | validated, 0 errors |
| `western_museum_of_flight_aircraft.csv` | 16 | 7 (44%) | validated, 0 errors |
| `joe_davies_heritage_airpark_aircraft.csv` | 20 | 20 (100%) | validated, 0 errors |
| `chico_air_museum_aircraft.csv` | 18 | 7 (39%) | validated, 0 errors |
| `caf_socal_aircraft.csv` | 14 | 8 (57%) | validated, 0 errors |
| `uss_hornet_aircraft.csv` | 12 | 7 (58%) | validated, 0 errors |
| `moffett_field_museum_aircraft.csv` | 9 | 8 (89%) | validated, 0 errors |
| `mojave_legacy_park_aircraft.csv` | 2 | 1 (50%) | validated, 0 errors |
| `san_diego_air_and_space_aircraft.csv` | 61 | 8 (13%) | validated, 0 errors |
| `sdasm_gillespie_annex_aircraft.csv` | 25 | 2 (8%) | validated, 0 errors |
| `california_science_center_aircraft.csv` | 14 | 8 (57%) | validated, 0 errors |
| `warbirds_west_aircraft.csv` | 6 | 6 (100%) | validated — museum may be closed |
| `allen_airways_aircraft.csv` | 4 | 4 (100%) | validated, 0 errors |
| `wings_of_history_aircraft.csv` | 27 | 2 (7%) | validated, 0 errors |
| `museum_of_flying_aircraft.csv` | 17 | 4 (24%) | validated, 0 errors |
| `lyon_air_museum_aircraft.csv` | 9 | 6 (67%) | validated, 0 errors |
| **Total** | **829** | **366 (44%)** | **25 museums** |

### Batch 6

| File | Rows | Tails |
|---|---|---|
| `wings_of_history_aircraft.csv` | 27 | 2 |
| `museum_of_flying_aircraft.csv` | 17 | 4 |
| `lyon_air_museum_aircraft.csv` | 9 | 6 |

**Two museums in `ca_museums.csv` turn out to hold no aircraft at all:**

- **Alameda Naval Air Museum** — its "aircraft gallery" pages are *archival
  photographs* of aircraft that passed through NAS Alameda, not airframes it
  owns. Visitor reports confirm the collection is models, artifacts and
  memorabilia; the only thing outdoors is a drop tank. **No aircraft file.**
- **Aviation Museum of Santa Paula** — a "chain of hangars" where private
  owners display their own aircraft. Nothing is named anywhere on the site,
  and the contents change with the owners. **No aircraft file.**

Both museum records are harmless to keep (they are real places worth
visiting) but they will always show zero aircraft. Consider whether an
aviation-*finder* should list them at all.

Notable flags:
- **Museum of Flying**: its Lockheed Vega and Wright Flyer are **movie
  props** — the Vega from 20th Century Fox, the Flyer built for *Night at
  the Museum*. The T-33 is a cockpit section. Its Douglas World Cruiser
  "New Orleans" is `in_storage`. A-4M and F-86H are on loan from Pensacola.
- **Wings of History**: three airframes marked `under_restoration` (1930
  Alexander primary glider, Peel Z-1 glider boat, Security Airster). Its
  Stahltaube is a flyable ¾-scale reproduction and its Wright Flyer a
  non-flying reproduction built for a restaurant. Their VJ-23 page describes
  the Channel-crossing record aircraft but also says that airframe is in
  Manchester, England — so the one on display probably isn't it.
- **Lyon Air Museum**: largely airworthy privately-owned warbirds, so
  "on display" is truer on average than on any given day.

## Still outstanding

Museums with a collection but no file yet: Lyon Air Museum, Museum of
Flying (Santa Monica), Wings of History, Hillier Air Museum (Modesto),
Minter Field, Aviation Museum of Santa Paula, Alameda Naval Air Museum,
Stockton Field, Boron Aerospace, Prop and Jet, Wings & Rotors, China Lake,
Golden Age Flight Museum, Tomorrow's Aeronautical, Battleship USS Iowa,
Flight Path Learning Center, The Proud Bird, The American Military Museum,
American Veterans Memorial, NTC & 11th ACR, West Gate Century Circle.

Remaining top-ups: **Hiller Aviation** (4 of ~40) and **Palm Springs**
(43 of ~75) — both need a diff against live data first, like San Diego did.

Note: the six Century Circle aircraft are currently recorded under the Air
Force Flight Test Museum, which operates them. If you want West Gate
Century Circle to show its own collection, they need moving.

### Batch 5 — El Cajon cluster + California Science Center

| File | Rows | Tails |
|---|---|---|
| `sdasm_gillespie_annex_aircraft.csv` | 25 | 2 |
| `california_science_center_aircraft.csv` | 14 | 8 |
| `warbirds_west_aircraft.csv` | 6 | 6 |
| `allen_airways_aircraft.csv` | 4 | 4 |

**California Science Center is the first file to use `display_status`
properly: 12 of 14 are `in_storage`, only 2 `on_display`.** Endeavour, the
Apollo-Soyuz CM, Gemini 11, Mercury-Redstone 2, the Monocoupe and the Wright
Glider reproduction are all in storage pending the Samuel Oschin Air and
Space Center opening on **13 November 2026**. Four more (F11F Tiger, F-106A,
Pitts S-1C, Harrier T.4) are physically installed in the new Korean Air
gallery but it isn't open yet. Only the A-12 Blackbird and the F/A-18A are
actually viewable today. Sending a visitor there expecting to see Endeavour
would be wrong until November.

Also at CSC: **Cassini-Huygens and the Viking Lander are full-scale
engineering models**, never-flown, and were excluded as non-aircraft. Their
Apollo, Gemini and Mercury capsules, by contrast, are all genuine flown
hardware on loan from the Smithsonian.

⚠️ **Warbirds West may be permanently closed.** AviationMuseum.eu lists it
"Permanently closed", the Warbirds Resource Group archive agrees, and
wwam.org now resolves to a parked placeholder — but a Yelp listing shows
hours updated May 2026. The 6 aircraft are real and well documented (all 6
have registrations), so the file is included, but **verify before you show
it to visitors** and delete the file if the museum is gone.

Gillespie Annex excluded a Boeing 377 and 727 cockpit section, a winged
Citroën 2CV novelty, and an F-14A that a Nov 2025 announcement says moved
to Balboa Park.

### San Diego Air & Space — a TOP-UP, read this before importing

This is the first top-up file rather than a fresh museum, and it has two
traps:

1. **The museum is already in your database as "San Diego Air and Space
   Museum" (id 39) — spelled with "and", not "&".** The file uses that exact
   string. Changing it to an ampersand would leave all 61 rows
   unresolvable and roll the batch back. Note this is a *different* record
   from "San Diego Air & Space Museum Gillespie Field Annex" (id 71), which
   `ca_museums.csv` added and which is still empty.
2. **Five researched aircraft were removed because they are already
   there**: Apollo 9 Command Module, A-12 60-6933, YF2Y-1 135763, Curtiss
   A-1, and the MQ-1 Predator. Four of the five have **no tail number in
   the database**, so they would not have collided — they would have
   silently duplicated. 67 researched, 61 written.

**24 of the 61 are replicas or mock-ups**, now marked in `description` and
tagged `replica` in `aliases`. This museum lost much of its original
collection in a 1978 fire and rebuilt with reproductions, so this is
expected rather than sloppy — but presenting a reproduction as an original
is exactly the sort of thing a visitor notices. Genuine originals worth
knowing: the **Apollo 9 Command Module "Gumdrop" is flown hardware**
(already in your database), while the Mercury, Gemini and Apollo CSM items
are mock-ups that never flew. The **Montgomery Evergreen glider (1911)** is
a real pioneer-era original.

Their "MiG-17" is, per Wikipedia, actually a Chinese-built Shenyang J-5
(licensed copy). Kept under the museum's own labelling, with `Shenyang J-5`
in aliases.

Excluded: a Ryan PT-22 and a Bell UH-1V that the museum's own pages place
at the Gillespie Field Annex, not Balboa Park.

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
### Batch 4 caveats

- **Joe Davies is the second file at 100% serial coverage** — the City of
  Palmdale publishes an aircraft-by-aircraft brochure. Note its F-16
  (78-0105) is a *composite* radar-target airframe: forward fuselage from
  84-1228, aft from 78-0105. One record, two donor airframes.
- **Excluded from Joe Davies**: four F-117s, a U-2R, an F-104N and an L-1011
  that sit at the Lockheed Martin plant entrance elsewhere on Plant 42, not
  in the airpark. The city's own brochure draws that line.
- **Mojave yielded only 2 rows.** It's a working spaceport, not a museum,
  and has no versioned collection list. The Roton ATV (N990RR) is a genuine
  vehicle that made three hover flights in 1999; the SpaceShipOne is a
  full-size **replica** (the real one is in the Smithsonian). Excluded a
  small-scale Voyager model, plus a Draken and an F-4D documented as being
  elsewhere on airport property.
- **CAF SoCal aircraft mostly fly.** 11 of 14 are airworthy warbirds that
  travel to airshows, so "on display" is truer on average than on any given
  day. Their Bearcat is in restoration.
- **USS Hornet's three spacecraft rows need care.** Apollo CM-011 is a real
  uncrewed Block I flight-test article (on loan from the Smithsonian), not a
  flown lunar capsule. Both Gemini items are explicitly **boilerplate** —
  non-functional training mock-ups.
- **Three of Moffett's nine are cockpit sections only** (AV-8A Harrier,
  TP-3A Orion, F-8A Crusader), flagged in `aliases`. Their serials came from
  Wikipedia citing Aerial Visuals, since the museum publishes none. Their
  site mentions a P-2 Neptune that no source could pin to a serial, so it
  is not included.
- **Chico**: the SPAD S.XIII is a flying **replica**, and the BT-13 is on
  loan rather than owned. One entry on their list ("EAA Biplane") had no
  identifiable manufacturer and was dropped.

### Batch 3 caveats

- **USS Midway has ZERO published serials** — 0 of 35. Their aircraft gallery
  pages give generic type specifications and never name the airframe on deck.
  This is the first file in the set where *nothing* has a tail number, which
  matters: blank tails never collide, so re-importing this file would create
  35 duplicates with no error raised. The idempotency guard in
  `import_california.sh` is the only thing standing between you and that.
  Their O-1 Bird Dog is an explicit **replica** — the original Buang-Ly
  aircraft is at Pensacola — flagged in `aliases`.
- **Western Museum of Flight** is Northrop-heavy and full of one-offs. The
  **YF-23A "Black Widow II" (PAV-2, 87-801)** is on long-term loan from NASA,
  and the **YO-3A Quiet Star** is in storage rather than on display. The
  Montgomery Glider is a 1985 replica of an 1883 design. Excluded the
  Northrop RP-99: the museum's own page says no flight article was ever
  built, so it is a wind-tunnel mock-up, not an airframe.
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
