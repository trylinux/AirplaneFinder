# Arkansas — research and import notes

Researched 9 September 2026. The state was greenfield: no Arkansas museum or
aircraft existed in the database before this work (the nearest records were
American Legion Post 339 in Roland, Oklahoma and Caruthersville, Missouri).

**19 sites · 69 airframes.** Three research passes (public museums + discovery
sweep; military base collections; monuments and single displays), cross-package
dedupe, a Google satellite / Street View currency pass on the weak-currency
sites, Nominatim reverse-geocoding of every postal code, and a collision check of
every tail against the 10,764 live airframes and every name against the 1,765
live museums (zero collisions either way).

## Files

| File | Site | Rows |
|---|---|---|
| `ar_museums.csv` | all 19 sites | — |
| `arkansas_air_and_military_museum_aircraft.csv` | Arkansas Air & Military Museum, Fayetteville | 22 |
| `little_rock_afb_heritage_park_aircraft.csv` | Little Rock AFB Heritage Park | 10 |
| `arkansas_national_guard_museum_camp_robinson_aircraft.csv` | Arkansas National Guard Museum -- Camp Robinson | 7 |
| `aviation_cadet_museum_aircraft.csv` | Aviation Cadet Museum -- Silver Wings Field, Eureka Springs | 7 |
| `188th_wing_static_display_collection_aircraft.csv` | 188th Wing Static Display Collection -- Fort Smith Regional Airport | 6 |
| `jacksonville_museum_of_military_history_aircraft.csv` | Jacksonville Museum of Military History | 2 |
| `wings_of_honor_museum_aircraft.csv` | Wings of Honor Museum, Walnut Ridge | 2 |
| `vietnam_veterans_memorial_rogers_aircraft.csv` | Vietnam Veterans Memorial -- Rogers Executive Airport | 2 |
| eleven single-airframe files | LRAFB main gate; LRAFB Joint Education Center; 189th AW Base Ops; Chaffee Crossing; VFW 5225 West Memphis; Wynne courthouse; Holiday Island; Legion Post 41 Helena; Kindley Park Gravette; VFW 1341 Bull Shoals; VFW 9095 Little Rock | 1 each |

Raw research packages are kept beside the CSVs for audit:
`arkansas_phase1_museums_research_raw.md`, `arkansas_phase2_bases_research_raw.md`,
`arkansas_phase3_monuments_research_raw.md`, `arkansas_imagery_checks.md`.

Serial coverage: 62 of 69 rows carry a tail number. The seven blanks are
deliberate (see below).

## Sources and their weight

1. **Vintage Aviation News, "Adam's Profile Reports: Arkansas Air and Military
   Museum", 24 Oct 2025** — a dated walk-through that is the backbone of the
   Fayetteville list. The museum's own collection pages list types but carry no
   serials at all.
2. **FAA registry** (queried 9 Sep 2026) — N23BY, N39668, N12143, N58577,
   N88769, N2278H, N18207, N614K, N3263G, N20830, N5682, N47365, N220JK. The
   deregistration trail settled several departures (below).
3. **Aerial Visuals** — airframe dossiers for every military serial, and a
   photo batch dated **August 2026** for Little Rock AFB Heritage Park and Camp
   Robinson (UH-1V 71-20332), plus the F-4C 63-7463 photo of 4 Aug 2024. That
   batch is what makes the LRAFB rows current rather than assumed. The Locator
   search form is broken by GET but works by POST (`Locator.php`,
   `Region=Arkansas`, `Scope=3`); location dossiers were throwing PHP errors on
   9 Sep 2026 so per-airframe coordinates came from OSM instead.
4. **OpenStreetMap `historic=aircraft` nodes** (Overpass; the main API is
   proxy-blocked, `overpass.private.coffee` works) — every Heritage Park
   airframe is mapped with its serial, plus the gate C-130A, the JEC C-130, the
   Base Ops RF-84F, six unlabeled nodes at the pre-move 188th Wing row, and the
   VFW 9095 Huey. Nothing for Camp Robinson.
5. **Joe Baugher** via the crouze.com mirror and Wayback (`web.archive.org/web/2023id_/`)
   copies of the broken-year pages; the archived 1951 page is missing
   51-607 to 51-2849, so F-84F 51-1817 could not be block-checked.
6. **NMUSAF "Aircraft on Loan by Location" PDF, April 2016** (WebFetch only;
   curl is 403'd). Arkansas rows: LRAFB 19 MXS ×10, 189 AW ×2, 188 MXS ×6, ARNG
   Museum ×4, Jacksonville MMH F-105F, Fayetteville T-33A, Newport T-37B,
   Gravette T-33A, Rogers GF-101B, West Helena T-33A.
7. **Google satellite + Street View** (9 Sep 2026): Holiday Island (SV Mar 2024),
   Wynne (SV Jul 2024), West Memphis (SV Feb 2026), Helena (SV Nov 2024, jet
   behind a tree; visible in satellite), Bull Shoals (SV Sep 2025), Chaffee
   Crossing (photosphere Apr 2021), LRAFB gate (SV Jun 2019), JEC C-130
   (photosphere Oct 2020), Base Ops RF-84F (satellite). Fort Smith satellite is
   **pre-July-2025** — it still shows six airframes on Thunderflash Drive and
   nothing on the Signature ramp.
8. Dated press: Talk Business & Politics Aug 2025 (Ebbing move) and 31 Mar 2025
   (Walnut Ridge); Arkansas Democrat-Gazette Oct/Nov 2022 (VFW 9095); Arkansas
   Living Nov 2023 (Rogers); 5NEWS 21 Jul 2023 (Gravette); Atlas Obscura
   10 Mar 2026 (Gravette); Air & Space Forces Magazine 31 Oct 2018 (RF-101C
   dedication); littlerock.af.mil articles 2010-2016.
9. Lead lists only: aviationmuseum.eu (its AAMM and Aviation Cadet tables are
   **column-shifted** — every serial sits one row off its aircraft; each was
   re-anchored elsewhere or dropped), silverhawkauthor (Marden ancestry),
   tinfeathers (DNS-dead mid-session), Wikipedia survivor lists.

## Corrections made

- **Jacksonville Museum of Military History's jet is F-105F 63-8261**, not an
  F-4. Baugher and NMUSAF agree; it is marked "6-3261". Wikipedia and Aerial
  Visuals say "Little Rock AFB" — it is at the civilian museum outside the gate.
- **LRAFB gate C-130A is 56-0518.** Baugher repeats the gate-display claim under
  57-0518 (c/n 3225, which went to Mexico as XA-RYZ). OSM, NMUSAF and the
  evacuation history all belong to 56-0518.
- **Fayetteville H-21 "55-4154"** is Aerial Visuals' 53-4354 (FY53 H-21B block)
  wearing a painted 55-4154. Recorded under the true serial; painted number in
  aliases. aviationmuseum.eu's "T-6G 55-4154" is that painted serial mis-rowed;
  there is no T-6G at the museum.
- **Aviation Cadet Museum**: aviationmuseum.eu pairs the F-5E with 62-4422, the
  T-33A with 56-3904 and the QF-100F with 741528 — all one row off. Re-anchored:
  F-105 nose 62-4422 (Wikipedia + AV), QF-100F 56-3904 (AV, dated roll-out
  11 Dec 1957), F-5E 74-1528 / BuNo 741528 (AV). tinfeathers "63-306" is 63-8306.
- **Ebbing's F-16 is an F-16A Block 15 (82-0970)** and its **A-10 is an A-10A/OA-10A
  (77-0216)**; the Aug 2025 press calls them F-16C and A-10C.
- **Camp Robinson T-37 is a T-37A** (c/n 40098 is in the A run; Baugher and AV
  agree); NMUSAF lists it as a T-37B.
- **C-119 53-8084 is Fairchild-built**; Baugher's block header says Kaiser-Frazer
  but the Kaiser Boxcars were 51-8098/8168. OSM's C-119 node carries the B-47's
  serial by copy-paste.
- **West Memphis F-4 is BuNo 152263** (F-4B-22-MC, later F-4N); it is painted
  151463.
- **Camp Robinson UH-1 66-15212** is a UH-1M conversion (Baugher); AV says UH-1C.
- **Rogers Huey serial resolved** to 67-17416 (phase 1 had it blank; phase 3 found
  it in Baugher and the AV Goldbook-derived history).

## Judgment calls

- **Little Rock AFB is four records**, split by how a visitor reaches each:
  Heritage Park (restricted), Main Gate C-130A (public — outside the gate beside
  the visitor centre), Joint Education Center C-130E (public — outside the
  fence), and the 189th AW Base Operations RF-84F (restricted; 1.4 km from the
  park, different unit).
- **Camp Robinson is `restricted`** even though the museum says any visitor can
  get a day pass at the gate with licence, registration and insurance; the
  description says so. The site coordinate is the museum building (Lloyd England
  Hall) because the aircraft pads could not be located: the AV per-airframe
  fixes supplied by the base pass were checked in satellite imagery and are lawn.
  The F-4C (AV photo Aug 2024) and UH-1V (AV photo Aug 2026) are certainly on
  the camp; where exactly is open item 1.
- **The 188th Wing collection is one record at its interim location** — the
  Signature Aviation ramp at Fort Smith Regional, where all six were towed on
  11 Jul 2025 for about three years while the FMS training centre and a new
  entry control point are built. The plan is to line the new entry road inside
  the fence c.2028; re-site the record then. Access `restricted` (viewable
  through the FBO fence, not walk-up).
- **Chaffee Crossing Cobra** is recorded at the Vietnam Veterans Museum, where
  the public finds it, not as "VVA Chapter 467 -- Fort Smith" which owns it.
- **Learjet 23 N23BY stays `on_display`**: live FAA registration to the Younkin
  family, but the Oct 2025 profile describes a static exhibit inside the
  museum. If it flies again it becomes a based private aircraft and leaves.
- **Piper J-3 recorded under its historic N20830** (the number is today on a
  2020 Cessna 172S); the description says so. **Travel Air Mystery Ship** is a
  1979 Younkin replica, recorded with a blank tail because FAA N614K belongs to
  the other Younkin replica at Tullahoma; painted NR614K in aliases.
- **F-105G 63-8306 and the 62-4422 nose section** are `electronic_warfare` per
  the suite's Wild Weasel rule; the nose section is recorded because the museum
  presents it as an exhibit (cf. the T-29 forward fuselage there).
- **Camp Robinson rows resting on 2007 photographs** (UH-1M 66-15212, F-84F
  51-1817, T-37A 56-3526) are kept: NMUSAF custody in 2016, no recorded
  transfer, and Aerial Visuals tracks departures from this site (it recorded
  the RF-101C leaving). The Baugher Oct 2018 sightings of AH-1S 71-21023 and
  UH-1V 73-21718 at the "All Flags Heritage Park" are kept as separate rows;
  AV's AH-1S 68-15129 (last seen stored 2004) is not, though it is possible
  68-15129 and 71-21023 are one airframe under two readings.
- **Bull Shoals Cobra identity**: Baugher says 66-15343 was shot down 19 Apr 1972
  and the display (marked 66-15434 — outside the AH-1G block) must be another
  airframe; AV's Goldbook-derived chain has a Jul 1972 recovery, ARADMAC
  rebuild, AH-1F conversion and transfer to Post 1341 in Aug 2003. The dated
  chain wins; painted number in aliases; needs a data plate.
- `year_built` is populated on 15 rows only, each from a sourced acceptance,
  first-flight, roll-out, delivery or FAA YEAR-MFR date. The F-101B's AV
  "constructed 1958" was dropped as too weak.

## Excluded, and why (do not re-research)

Sites:
- **Aerospace Education Center / Arkansas Aviation Historical Society, Little
  Rock** — ceased 1 Jan 2011, demolished 2014, assets liquidated; the Sopwith
  Camel and Apollo CSM replicas are untraced.
- **Fort Smith Air Museum** (airport terminal) — 64 display cases; its only
  airframe, a loaned Piper J-3 Cub, is in storage off-view. Re-check if re-hung.
- **Blytheville / Arkansas Aeroplex** — the BAFB Exhibition (Bldg 202) is
  memorabilia; the National Cold War Center is projected 2027+ and holds no
  airframe yet (Dec 2025 fundraising press). Re-check 2027.
- **Titan II** — four launch complexes are NRHP-listed (373-5 Center Hill,
  374-5 Springhill, 374-7 Damascus, 373-9 Vilonia "Titan Ranch"); structures
  only. The 308th SMW memorial at LRAFB is a demilitarised Mk 6 re-entry vehicle
  on a time capsule (17 Aug 1987) — a component, not recorded. Jacksonville MMH
  holds a launch console. No Titan II missile is preserved anywhere in Arkansas.
- **Mountain Home High School A-7E 160614** — placed Dec 2004 per AV; the only
  citation is the school's NJROTC page retrieved July 2015. The whole campus
  was scanned in satellite at three scales and Street View on Bomber Blvd
  (Sep 2025) shows no jet. Not recorded; open item 3.
- **Southern Arkansas University Tech, East Camden** — T-33A 58-0651 has a live
  FAA registration (N88769) to the college since 1973, but AV flags it as a
  probable instructional airframe with OH-23B 51-16258 and TC-45J 29626, and
  satellite shows only a ~30 m T-tail airliner (the 727-100 trainer) on the
  ramp. Not a public display on present evidence.
- **Newport T-37B 68-8077** — NMUSAF 2016 loan to the City of Newport; no
  location, photo, or news found; absent from the Wikipedia T-37 list.
- **Wilson F-86L 53-1047** — Baugher only ("on display outside at Wilson");
  AV has a placeholder; absent from the Wikipedia F-86 list; nothing local.
- Pocahontas: A-7A 153150 to Cecil Field FL Aug 2019; HH-52A 1398 to Elizabeth
  City NC 2009-10. Harrison F-84F 51-1662 to Mayville ND 1993. Jonesboro T-33A
  53-5933 to Iowa. Magnolia T-33A 51-6678 and North Little Rock T-33A 53-5342
  ("on display 1973") untraced since.
- **Texarkana Spring Lake Park T-33A** — on the Texas side (OSM node at
  33.4626, -94.0571); belongs to the Texas file.
- Instructional / stored / private, not displays: Pulaski Tech AMT Center
  (T-34B, U-8D, Hughes 269, Learjet 24, TH-55A); Walnut Ridge ramp (737-2H4
  N86SW, 777-236 N703BA, T-42A, BT-15); Mena DC-3/C-47TP hulks; Springdale
  CH-21C N106MH / AT-7C; Texarkana Jet Provost XS219 / Lodestar; Furlow Beech
  18s; Pine Bluff EAA 1388 hangar; LRAFB loadmaster trainers (63-7784, 63-9815,
  68-10949, 63-7764, 64-0524, 63-7820, 68-10948, 63-7852); Fort Chaffee
  Razorback Range targets (A-4, A-7, AH-1, MiG-29); the 188th's MQ-9 "static
  display" (a display model).
- CAF Razorback Wing, North Little Rock — airworthy fleet, not a museum display.
- Walmart Museum, Bentonville — "Flying With Sam" exhibit; no source says the
  Ercoupe hangs there.
- LRAFB former displays, all gone: F-4C 64-0748 (Langley), F-100D 56-3434
  (Titusville 2015), F-86D/L 52-3653 (Pueblo), F-104A 56-0753 (Hill), F-102A
  56-1432 (Palm Springs 2015), T-33A 51-9080 (Skiatook OK), HH-1H 70-2470 (Hill
  2021), C-130E 61-2358 (Edwards 2012), EC-130H 62-1862 (Scott 2009), C-130E
  63-7819 (moved on); C-130E 62-1830 and C-130A 56-0539 scrapped.
- **KC-135E 56-3630** — AV says "to be joining" LRAFB; Baugher last has it at
  AMARC in 2017 and no arrival was found. Pre-shipment press is not arrival.
- **Camp Robinson RF-101C 56-0057** — AV closes its display span "by May 2018"
  and marks the pad vacated; the 2016 loan list and Wikipedia still place it
  there; warbirdsresourcegroup says "was preserved at Camp Robinson, currently
  preserved at Little Rock" without saying where. Not recorded; open item 1.
- Departed from Fayetteville: Howard DGA-11 N18207 (FAA now Mid America Flight
  Museum, TX); Aero Adventure Aventura N220JK (N-number reassigned); Ercoupe
  N2278H — see open item 2.

Airframes not recorded because only the 2016-era aviationmuseum.eu tables list
them and they are absent from the museum's 2026 collection page and the Oct 2025
profile: at Fayetteville — Luscombe 8E, Globe Swift, Taylorcraft BC-12D, Travel
Air D4000, Howard DGA-6 replica, S.E.5a replica, Bensen gyrocopter, Revolution
Mini-500, DC-3 cockpit, Falcon 20; at Walnut Ridge — Beech SNB-5, Bell AH-1F
(and a TracesOfWar "Fw 190" with no corroboration anywhere).

## Deliberately blank

- **Tail numbers (7):** Aviation Cadet T-33A (marking read as 57-0688 vs
  57-0668 in a shifted table — needs the data block), T-34B (no valid BuNo in
  any source), T-29 forward fuselage; Fayetteville Mystery Ship replica,
  Curtiss-Wright Junior, PA-22, Pietenpol (registrations not published; the
  aviationmuseum.eu N86483 sits in a misaligned table).
- **year_built** on 54 rows — FY prefixes never used.
- Painted markings on the Heritage Park airframes beyond those a source stated.
- Camp Robinson per-airframe coordinates (see judgment calls).

## Needs a human on site (ranked)

1. **Camp Robinson roster and pad locations** — is RF-101C 56-0057 still on the
   camp; which Cobra (68-15129 vs 71-21023); where the F-4C/UH-1V pad, the
   "All Flags Heritage Park", the F-84F and the T-37A actually sit. One call:
   Arkansas National Guard Museum (501) 435-2400, dotm.museum@arkansas.gov.
2. **Sam Walton's Ercoupe 415-C N2278H** — displayed at Fayetteville from 2007;
   FAA registrant is now Echo Matrix LLC, Bentonville; absent from the Oct 2025
   profile; not confirmed at the reopened Walmart Museum. AAMM (479) 521-4947
   also closes: whether the Luscombe, Swift, Taylorcraft, D4000, DGA-6 and
   S.E.5a replicas and Falcon 20 are stored (in_storage is still a record), the
   Pietenpol and Tri-Pacer registrations, and data-plate photos of both H-21s.
3. **Mountain Home High School A-7E 160614** — where did it go? School office
   (870) 425-1215 / NJROTC.
4. **Aviation Cadet Museum** (479) 253-5008 — T-33A data block, T-34B BuNo, T-29
   nose serial, and the ninth aircraft the museum says it holds.
5. **188th Wing** — confirm all six are on the Signature ramp today and what is
   painted on the F-100A (54-629 vs FW-629); 188th Wing PA via the wing site.
6. **Wings of Honor** (800) 584-5575 — SNB-5 / AH-1F ever displayed or stored;
   BT-13A 42-1574 from the data plate.
7. **Jacksonville MMH** (501) 241-1943 — Huey serial/variant 64-14150 UH-1C.
8. **Chaffee Crossing** (479) 478-0110 — Cobra variant as displayed.
9. Newport City Hall / Wilson city office — the T-37B and F-86L leads.
10. HMdb and Waymarking Arkansas listings could not be enumerated (Cloudflare);
    a browser session on hmdb.org (Arkansas, Air & Space) may surface Huey or
    T-33 memorials in towns the sweep did not reach.
