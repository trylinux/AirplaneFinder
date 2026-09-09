# Virginia — statewide sweep (September 2026)

Adds 12 sites and 101 airframes to the two Virginia records the database
already held (Steven F. Udvar-Hazy Center id 22, Science Museum of Virginia
id 48). Virginia was effectively a stub state before this pass.

## Files

| File | Rows | Tails |
|---|---|---|
| `accomack_county_airport_aircraft.csv` | 1 | 1 (100%) |
| `air_power_park_aircraft.csv` | 14 | 9 (64%) |
| `aviation_historical_park_nas_oceana_aircraft.csv` | 12 | 12 (100%) |
| `front_royal_warren_county_airport_aircraft.csv` | 1 | 1 (100%) |
| `langley_afb_memorial_park_aircraft.csv` | 8 | 8 (100%) |
| `nasa_wallops_visitor_center_aircraft.csv` | 1 | 0 (0%) |
| `national_museum_marine_corps_aircraft.csv` | 20 | 20 (100%) |
| `shannon_air_museum_aircraft.csv` | 5 | 1 (20%) |
| `us_army_transportation_museum_aircraft.csv` | 20 | 19 (95%) |
| `virginia_air_space_science_center_aircraft.csv` | 19 | 15 (79%) |
| **total** | **101** | **86** |

`va_museums.csv` creates all 12 sites. The Military Aviation Museum at
Virginia Beach is created as a **site record with no airframes** — see the
refusal below.

## Currency evidence

- **FAA registry name search on TSI Holdco Inc** (the Yagen family holding
  entity behind the Military Aviation Museum) returned **82 live
  registrations**; N943HH spot-checked as a Hawker Siddeley Hurricane MkIIB,
  s/n 56022, certificate valid to 2031. 2026-current.
- **Rod Bearden's 2017 on-site photo log** and **militaryaircrafthistorian**
  independently agree on eight Air Power Park serials — two genuinely separate
  readings off the airframes.
- **HMdb interpretive markers** installed for Hampton's May 2024 park
  refurbishment carry USAF delivery dates: F-105D 61-0073 delivered
  29 January 1962, RF-4C 69-0372 delivered 19 August 1970. Those are the only
  two `year_built` values in the Air Power Park block, and both come from a
  delivery date, never from an FY prefix.
- **Aerial Visuals** dossier for F-14D 164604 carries a 16 September 2022
  photograph in place at Oceana.
- **Joint Base Langley-Eustis official article** is a primary source on both
  the identity and the location of F-4C 64-0748.

## The Military Aviation Museum returns zero airframes, deliberately

`aviationmuseum.eu`'s MAM table is corrupted and was refused. FAA cross-checks,
five spot-checks, four to five verifiable errors:

| Table says | FAA says |
|---|---|
| N108ZZ = Lockheed PV-2 Harpoon | **Nord 1002** |
| N22518 = Piper J-3 Super Cub | **North American SNJ-4** |
| N1639P = Sopwith 1½ Strutter | **Polikarpov I-16 Type 24** |
| N183FW = Flug Werk FW-190 | **Focke Wulf FW44J** |
| N23827 = "Douglas A-4D Skyraider" | **Douglas AD-4** |

Its serial column also mixes construction numbers with painted markings
(a P-51D listed as "49-3087" is not a P-51D serial). MAM has 70+ airframes and
is the largest single gap left in the state. The FAA name search above is the
right way to rebuild it and is the recommended next step.

## Other stale sources caught

- **silverhawkauthor failed at Langley.** It places an F-4N BuNo 151510 and an
  F-105D 61-0217 there; the official JBLE article gives **F-4C 64-0748** and
  Aerial Visuals gives **F-105D 61-0188**. It also credits Shannon Air Museum
  with "50+ aircraft including an F-14D and an A-4C" when the museum's own
  exhibits page lists five civil antiques. Used only for lead generation, and
  for Fort Eustis with every row flagged single-source in its description.
- **Wikipedia's Aviation Historical Park list is stale.** It still carries a
  Douglas XAD-1 that left for the Intrepid Sea Air and Space Museum on
  14 May 2014, and omits the A-7E the newer list carries.
- **HMdb "permanently removed" flags at Air Power Park are about signage,
  not aircraft.** Nine single-aircraft markers show removed and eight paired
  markers show present — that is the 2024 refurbishment replacing old signs,
  not a collection dispersal. The park relaunched in May 2024 with restored
  aircraft (WTKR, 25 May 2024).

## Corrections made

- Air Power Park Kestrel **64-18268 → 64-18266**. The XV-6A block is
  64-18262/18267; militaryaircrafthistorian's number is impossible. Identity
  agreed by Wikipedia, AirHistory.net and dated Flickr logs (XS692, NASA 520).
- VASC Starfighter **F-104G → F-104C**, 57-0916 (block 57-0910/0930, buzz
  number FG-916, 2017 photo log).
- VASC: the source directory's serial column is **offset by one row** around
  the Piper/Pitts/Republic/Rutan entries. 51-1786 reassigned from the Pitts
  Special to the **F-84F** on the strength of the FS-786 buzz number. The Pitts
  and VariEze registrations are left blank rather than guessed (the directory's
  "07481" is not a valid US registration).
- NMMC **"Boeing CH-46D Chinook" → Boeing Vertol CH-46D Sea Knight**
  (rear fuselage only). The CH-46 is the Sea Knight; the Chinook is the CH-47.
- Fort Eustis **"Boeing CH-46A" 59-4984 → Vertol YHC-1A**, the Army
  designation matching an FY59 Army serial.
- **F-14D 164604 is at Oceana**, not the Cradle of Aviation — that is 164603,
  the last in Navy *service*. 164604 is the last *built*. Routinely confused.

## Production-block failures, flagged in-row rather than dropped

- Oceana F4D-1 **141414** and F2H-4 **127369** could not be matched to any
  published block for those variants.
- Oceana "F-4A 152295" cannot be an F-4A — 152295 sits inside the F-4B block
  152207/152331. `variant` left blank.
- Oceana "F-8E 145802" falls in the earlier F8U-1/F8U-2 range. `variant` blank.

## Dropped

- **Fort Eustis "UH-1B 56-6723"** — 56-6723 is one of the three XH-40
  prototypes and the survivor is at Fort Rucker. Almost certainly a
  transcription of a different airframe.
- **Fort Eustis YCH-54A 64-14202** — the same source that places it here also
  records it lost in Vietnam in August 1966.
- **Fort Eustis Doak VZ-4DA 56-9642** — collided with existing record id 9783,
  which states the airframe transferred to the US Army Aviation Museum at Fort
  Rucker in August 2024 (Wikipedia-confirmed). The Alabama record wins; this is
  exactly the departure the Fort Eustis source failed to catch.
- **Fort Eustis UH-1H 64-13644** — collided with existing record id 8399 at the
  Museum of Missouri Military History. One attribution is wrong and the
  Virginia one is the single-source side. Unresolved; not imported.

## Read before trusting the Fort Eustis block

Every Fort Eustis serial is **single-source**, from a source that verifiably
failed a currency test elsewhere in this state, for a museum that is
**closing/consolidating** and from which at least one airframe (the Avrocar's
stablemate VZ-4DA) demonstrably left in August 2024. Types are corroborated by
an independent 2008 on-site log; identities are not. Treat the 20 imported rows
as presence-plausible and identity-unverified. The Avrocar VZ-9AV 59-4975 is
imported as `under_restoration` per its source and is
Smithsonian-owned.

## Coordinate provenance

Air Power Park, Front Royal and DSCR are HMdb marker fixes (near-airframe).
Oceana, NMMC, VASC and Fort Eustis are Wikipedia site coordinates. **Shannon
and Melfa are airport reference points, not airframe fixes. Langley Memorial
Park is the Langley AFB airfield reference point** — no airframe fix or imagery
for Nealy Avenue could be obtained; treat as approximate.

## Open items

1. **Military Aviation Museum, 70+ airframes.** Rebuild from the FAA name
   search on TSI Holdco Inc, not from any compilation.
2. **Fort Eustis is closing.** Re-verify the 20 rows against the museum
   directly before anyone relies on them, and find out where the collection
   is going.
3. **Defense Supply Center Richmond Air Park** has a site record and no
   airframes — it was created from an HMdb marker fix with no sourced roster.
4. NASA Wallops holds **no aircraft**; its one row is a Little Joe booster.
   The Nike-Cajun sounding rocket and the four-stage reentry vehicle there are
   deliberately omitted as not airframes.

Full research output preserved at `virginia_sweep_research_raw.md`.
