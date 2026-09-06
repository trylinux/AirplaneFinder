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
| batch 7 (7 files, see below) | 75 | 32 | validated, 0 errors |
| batch 8 (9 files, see below) | 84 | 28 | validated, 0 errors |
| **Total** | **988** | **426 (43%)** | **41 files** |

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

### Batch 7 — the small museums

| File | Rows | Tails |
|---|---|---|
| `china_lake_museum_aircraft.csv` | 22 | 0 |
| `golden_age_flight_museum_aircraft.csv` | 18 | 2 |
| `minter_field_aircraft.csv` | 11 | 10 |
| `prop_and_jet_aircraft.csv` | 10 | 6 |
| `wings_and_rotors_aircraft.csv` | 6 | 6 |
| `boron_aerospace_aircraft.csv` | 5 | 5 |
| `stockton_field_aircraft.csv` | 3 | 3 |

**China Lake is 4 aircraft and 18 missiles** — the largest use of
`missile_rocket` in the dataset (Sidewinder, Phoenix, Tomahawk, HARM,
Walleye, Maverick and more, all developed there). Plain unguided ordnance
(Mk 80-series bombs, Rockeye, Paveway kits) was excluded — they're munitions,
not flight vehicles, and there is no honest `aircraft_type` for them. Note
the museum has **moved off the Navy base** to 130 E Las Flores Ave in
Ridgecrest, so it no longer needs base access — the address in
`ca_museums.csv` is correct.

⚠️ **Hillier Air Museum (Modesto) has no file — it is permanently closed.**
AviationMuseum.eu lists it closed and its own domain returns nothing. Nine
aircraft were documented but the collection's current whereabouts are
unknown, so attributing them to a closed museum would be inventing a place
to visit. **Its museum record should probably be removed from
`ca_museums.csv`.**

⚠️ **Wings & Rotors (Murrieta) status unconfirmed** — its domain is a parked
placeholder and a 2019 thread says it closed, but directories still list
hours. Included with all 6 registrations, same treatment as Warbirds West.
Verify both before showing them to visitors.

Also excluded: aircraft that Aerial Visuals lists as having *moved off-site*
from Minter Field (7 airframes), Stockton's PV-2D Harpoon and RC-45J (both
sold in late 2025), and several Prop and Jet aircraft the registry marks
only as "may be in the collection".

### Batch 8 — final round

| File | Rows | Tails |
|---|---|---|
| `hiller_aviation_topup_aircraft.csv` | 56 | 5 |
| `tomorrows_aeronautical_aircraft.csv` | 15 | 15 |
| `proud_bird_aircraft.csv` | 3 | 0 |
| `blackbird_airpark_topup_aircraft.csv` | 3 | 3 |
| `american_veterans_memorial_aircraft.csv` | 2 | 2 |
| `flight_path_aircraft.csv` | 2 | 2 |
| `armstrong_topup_aircraft.csv` | 1 | 1 |
| `uss_iowa_aircraft.csv` | 1 | 0 |
| `american_military_museum_aircraft.csv` | 1 | 0 |

**Three of these are TOP-UPS** and exclude what's already live:

- **Hiller Aviation** (4 → 60). Excludes the Aero Commander 500-U, L-39C
  533526, Airbus Vahana and AR-5 already recorded. Strong on Hiller company
  prototypes and early rotorcraft, plus a genuinely modern eVTOL group
  (Kitty Hawk Flyer, Opener BlackFly, Wisk Cora). Two entries are
  **fuselage/cockpit sections**: a Boeing 747-100 forward fuselage
  (G-AWNG) and a 737-200 cockpit. Many pioneer-era items are replicas,
  flagged in `aliases`. Its Marriott Avitor is the **only
  `lighter_than_air` record in the whole dataset**.
- **Blackbird Airpark** (1 → 4): the A-12 60-6924, D-21B and U-2D 56-6721
  that the Air Force Flight Test Museum lists but that physically sit at
  Palmdale. This closes the loop on that misattribution.
- **Armstrong** (6 → 7): the Grumman X-29 82-0049, same story.

**The Proud Bird**: a restaurant, and most of its "warbirds" are fibreglass
replicas. A 2025 historical-marker source identifies only **three genuine
airframes** — a DC-3, a Twin Beech C-45 and an A-4 Skyhawk. The other ~10
(Spitfire, P-51, P-38, Bf 109 and so on) were excluded as mock-ups.

**Battleship USS Iowa** holds exactly one aircraft, a HUP-2 Retriever. Its
Kingfisher catapults survive but the aircraft does not — no row invented.

Tomorrow's Aeronautical (Compton) came from a third-party directory rather
than the museum's own site, which publishes no list. All 15 have tail
numbers, but it deserves a spot-check.

## Status: California complete

**41 files, 988 aircraft, 43 museums with collections.** Every file
validates through the real importer with zero errors.

| | |
|---|---|
| fixed_wing | 834 |
| rotary_wing | 116 |
| missile_rocket | 24 |
| spacecraft | 13 |
| lighter_than_air | 1 |
| **on_display / in_storage / under_restoration** | **965 / 13 / 10** |
| monoplane / biplane / triplane | 740 / 90 / 4 |

### Deliberately not built

| Site | Why |
|---|---|
| Hillier Air Museum (Modesto) | Permanently closed; collection whereabouts unknown |
| Alameda Naval Air Museum | Holds no airframes — photo galleries and models only |
| Aviation Museum of Santa Paula | Private hangars, no published or stable list |
| Milestones of Flight, California Flight Museum, CA Army National Guard Museum, Central California Historical Military Museum, Museum of the Forgotten Warriors | Permanently closed |
| Exploratorium, Whittier Museum, Oakland Museum of CA, Kern County Museum, SFO Turpen Museum | No aircraft |
| Nixon Library | Its VH-3A is away at March Field until ~2028 |
| P-38 Museum | Its P-38 is fibreglass |
| Flying Leatherneck | 31 real aircraft, but closed to the public until 2027-28 |
| NASA Ames Exploration Center | Public access genuinely ambiguous |

### Verify before trusting

- **Warbirds West** and **Wings & Rotors** — both may be permanently closed.
- **Tomorrow's Aeronautical** — sourced from a directory, not the museum.
- **Aerospace Museum of California** — 16 published vs ~40 claimed elsewhere.
- **Classic Rotors** — identities recovered from photo filenames.
- The **NB-52 52-008 / B-52 52-0008** duplicate (see
  `../verified_misattributions.md`) is still unresolved.

### Remaining top-up

**Palm Springs Air Museum** holds 43 records against a real collection of
about 75. It is the only substantial gap left in the state.
