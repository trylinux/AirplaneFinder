# Queensland and Northern Territory — research notes

Scope: Queensland and the Northern Territory, all three phases (public museums,
base and service collections, single-airframe monuments). 26 sites, 236 aircraft.

## Sources used, and how each performed

**ADF-Serials (adf-serials.com.au)** — the backbone of this sweep. Every ADF
airframe in the CSVs was checked against its type page. The site is reachable
over plain HTTP at `adf-serials.com.au` (the HTTPS certificate does not match
`www.adf-serials.com.au`, which blocks robots-respecting fetchers). Type pages
used: A1 Sioux, A2 Iroquois, A3 Mirage, A4 Caribou, A7 Macchi, A8 F-111,
A9 Orion, A11 Auster, A14 Porter, A15 Chinook, A17 Kiowa, A18 Nomad, A19,
A20 707, A21 Hornet, A23 PC-9, A25 Black Hawk, A46 Boomerang, A79 Vampire,
A84 Canberra, A85 Winjeel, A89 Neptune, A92 Jindivik, A94 Sabre, A97, A98
Cessna 180, plus the Auster AOP.9 page. It is also the best *discovery* tool in
the region: grepping the type pages for Queensland and NT place names turned up
six sites no museum directory lists (Meandarra, Willowbank, Brymaroo, Bribie
Island, Caloundra RSL, Calvert Field).

**Museum collection pages** — excellent in this region and used in preference to
everything else for "what is here now":
- Queensland Air Museum publishes a live 99-entry collection list at
  `qldairmuseum.au/qam-content/aircraft/collection-list.htm` with per-airframe
  display/storage/restoration/loan status. This is the single best museum source
  found anywhere in the sweep.
- Central Australian Aviation Museum has a page per exhibit with full provenance.
- Qantas Founders Museum, AAHC Qld, FNQ Aviation Museum, Darwin Aviation Museum.

**Department of Defence / Air Force** — the 20 August 2025 Defence news item on
the reopening of the Townsville heritage centre is the authoritative current list
for that site. airforce.gov.au heritage-centre pages gave addresses, hours and
access conditions for Amberley and Townsville.

**Wikipedia and aviationmuseum.eu** — leads only, and both proved stale in
specific ways (below).

## Sources that proved stale, and how

- **Wikipedia, Queensland Air Museum** (collection "as of January 2024") is
  missing at least eleven airframes the museum now lists (Macchi A7-072,
  Cessna 310R VH-JOS, DC-6 VH-BPG, Fokker Dr.I VH-ALU, Maurice Farman Shorthorn,
  Pellarini Airjeep, Dehn Ring Wing, Birdman TL-1A, Spitfire representation
  K9787, Seeker VH-EQN, UH-1B cabin 64-13925), and still lists Sea Venom WZ910,
  Beech E18S N3781B and SA315B Lama PK-ZHB, which the museum no longer carries.
  It also gives the Orion as **A89-760**; RAAF Orions carry **A9-** serials and
  both the museum and ADF-Serials say **A9-760**. Corrected.
- **Wikipedia, RAAF Townsville Aviation Heritage Centre** lists a Vampire
  **A79-656** and Iroquois **A2-382** on display. ADF-Serials records A79-656 as
  "reported in store at Amberley but they say they don't have it — current
  location unknown", places two other Vampires (A79-804, A79-666) at Townsville,
  and records A2-382's starboard section as relocated to the 2 RAR Historical
  Collection in November 2019. The Defence reopening announcement of August 2025
  names five aircraft and neither of these. Corrected.
- **Warbirds Online's 2016 Amberley collection list** is stale in two ways:
  Canberra **A84-203** was tendered in 2015 and gifted in February 2016 to Evans
  Head, NSW; Mirage **A3-55** has since moved to RAAF Townsville. Removed both.
- **aviationspottersonline's Oakey article** places Boomerang **A46-206** at the
  Army Flying Museum. ADF-Serials records it as donated to that museum in May
  2007 but moved to RAAF Amberley on 28 August 2018 for static display. Recorded
  at Amberley.
- **aviationmuseum.eu's Oakey table** is internally mis-aligned — the serial and
  type columns are offset by one row, producing impossible pairings such as
  "A85-406 Cessna O-1A Bird Dog" and "A98-045 Bleriot XI". Not used for
  identities; Oakey's list was rebuilt from ADF-Serials.
- **aviationmuseum.eu's Australia index** still lists Caboolture Warplane Museum
  and the Beck Museum as live sites. Both are gone (below).
- **aviationmuseum.eu's Mareeba/Warbird Adventures list** gives the Beech Queen
  Air as **VH-FDS**. That registration belongs to the RFDS Drover at the
  Queensland Air Museum. The Queen Air's tail number is left blank.
- **Warbird Adventures' own website** still carries a 2014 copyright and cannot
  be treated as current for status; the collection there is corroborated by the
  February 2026 Express article, which describes the operator's airworthy Winjeel
  flights as current.

## Corrections made, with evidence

| Airframe | Was reported | Recorded as | Evidence |
|---|---|---|---|
| Orion A9-760 | A89-760 (Wikipedia) | A9-760, Queensland Air Museum | museum list + ADF-Serials A9 page |
| Canberra at QAM | A84-224 | A84-225 | ADF-Serials: A84-224 was scrapped at Morwell, Vic in 1989; the QAM sentence belongs to the A84-225 block |
| Mirage A3-55 | RAAF Amberley | RAAF Townsville, 76 Sqn markings | ADF-Serials A3 page; Defence, 20 Aug 2025 |
| Neptune gate guard, Townsville | A89-272 | A89-280 | ADF-Serials: A89-272 was cyclone-damaged in 2011, removed from the gate, used for parts and donated to HARS in 2016; A89-280 replaced it in Oct 2012 |
| Townsville gate guardian Caribou | attributed to Chinook A15-102 by a naive text split | Caribou **A4-199** | A15-102 was destroyed in Afghanistan, 30 May 2011; the "gate guardian" sentence belongs to A4-199, which A15-102 airlifted to Townsville in 2009 |
| Darwin Mirage | A3-7 (Wikipedia lists A3-36; some sources say A3-7 went to Darwin) | A3-36 on display; A3-105 crash remains outside | ADF-Serials: A3-7's stripped fuselage went to Darwin but was exported to Pakistan in 1990 |
| Chinook A15-004 "at Darwin/Oakey" | a Chinook display | not a display at all | A15-004 went to the USA in 1993 and returned as A15-104; the Darwin sentence describes a Mirage wreck it recovered, and the Oakey one belongs to A15-105 |
| Iroquois A2-769 at Oakey | on display at Oakey | departed Oakey June 2012 for the National Vietnam Veterans Museum, Phillip Island, Vic | ADF-Serials A2 page |
| Oakey's Iroquois | unclear | **A2-649**, repainted overall red in the Operation Bel Isi scheme March 2014 | ADF-Serials A2 page |
| Sabre A94-914, Darwin | single airframe | composite: A94-914 with the rear fuselage of A94-921 | ADF-Serials, quoting Bob Ogden's museums guide |
| Kiowa A17-005 | Australian Aviation Heritage Centre, Caboolture | pole-mounted at Bribie Island Vietnam Veterans Memorial Park since Aug 2019 | ADF-Serials A17 page |
| Kiowas A17-020, A17-031, A17-050 | Oakey museum | all sold away (Evans Head 2017, private sale 2019, HARS 2017) | ADF-Serials A17 page |
| Sioux A1-406, A1-407 | Oakey museum | Phillip Island, Vic and Bandiana, Vic | ADF-Serials A1 page |
| Winjeel A85-406 | Oakey museum | restored and on display at RAAF Amberley | ADF-Serials A85 page |

## Sites closed or dispersed — excluded, with reasons

- **Caboolture Warplane and Flight Heritage Museum** — **closed in 2025** after
  30 years. Its own site now carries only a post-closure message signed
  "Volunteers @ the Caboolture Warplane Museum (2025)", stating the collection is
  going to "carefully selected museum partners and historical organisations".
  Excluded as a site. Two of its airframes are recorded in ADF-Serials as being
  there — the F-111C **A8-130** crew module and Iroquois **A2-484** — and their
  new homes were not established. See open questions.
- **The Beck Museum / Sid Beck Collection, Mareeba** — the collection has
  dispersed. The P-39D "Erminie" went to Fagen Fighters in the USA; the Neptune
  A89-277 was sold to the Queensland Air Museum in 2015; and the Canberra
  A84-210, Vampire A79-89 and C-47 A65-73/VH-CIP now appear as FNQ Aviation
  Museum holdings, also at Mareeba. Recorded under FNQ Aviation Museum, not Beck.
- **Gold Coast War Museum, Mudgeeraba / Coolangatta** and **Chewing Gum Field
  Museum, Tallebudgera** — both long defunct; their aircraft dispersed to QAM,
  HARS and elsewhere in the 1980s-90s.
- **Toowoomba Aero Museum** — defunct; its Sabre A94-914 was auctioned in 1989.

## Sites and airframes checked and excluded

- **Army Museum South Queensland, Victoria Barracks Brisbane** — an Army museum
  with no aircraft in its collection.
- **Charleville** — the WWII "Secret Base" tour and the Cosmos Centre interpret a
  1943 USAAF B-17 base; no airframe is displayed.
- **Winton, Cloncurry, Barcaldine** — Qantas-heritage interpretation only; the
  physical aircraft are all at Longreach.
- **Mount Isa** — Winjeel **A85-48**'s fuselage was moved there by private owners
  for a restoration to airworthy. Private restoration project, not a display.
- **Archerfield Airport** — Geoff Moesker's Sabre **A94-922** was hangared there;
  it was sold to Jerry Yagen and is being restored at AVSpecs, Ardmore, NZ.
  Neptune A89-281 passed through Archerfield in 1990 and is now at HARS Albion
  Park. Nothing currently preserved on public display.
- **Toowoomba Airport** — the Sabre displayed there in the USAF "Honest John"
  scheme was exported to New Zealand. Nothing remains.
- **Chinook A15-001** — "currently derelict at Oakey" per ADF-Serials. A derelict
  hulk with no display intent; excluded, but worth re-checking.
- **Chinook A15-151** — installed at Robertson Barracks, Darwin in late 2016 as a
  training aid for 1 Brigade and 1 CER. Equipment in use, not a display;
  excluded. The Iroquois A2-376 at the same barracks *is* a display and is
  recorded.
- **Link Trainer at the Queensland Air Museum** — a ground flight-trainer
  cabinet, not an airframe. Excluded. The Bristol Bloodhound at the same museum
  *is* recorded, as `missile_rocket` + `surface_to_air`.
- **Royal Flying Doctor Museum, Alice Springs** — no airframe was confirmed on
  display there; excluded pending a check.

## Judgment calls

- **Access types.** RAAF Amberley is `restricted`: the heritage centre is inside
  the wire, open Tuesdays and Thursdays only, and every visitor over 16 must
  present photo ID. RAAF Townsville is `public`: it sits in a fenced compound at
  the base's original 1940 entry point with its own street address (487 Ingham
  Road), and Air Force states "entry is free and no bookings are required". Base
  gate guards, barracks displays and the Tindal Hornet are `restricted`.
  The FNQ Aviation Museum is `appointment` — its own site says the museum is
  closed to the public for building renovations and will reopen later in 2026,
  with volunteers on site Thursday and Saturday mornings.
- **Airworthy collections.** Warbird Adventures Aviation Museum at Mareeba flies
  its Winjeels, Harvard and Nanchang for adventure flights and opens as a museum
  Thursday and Sunday. Following the spec's rule for airworthy museum
  collections, the aircraft are recorded as `on_display` with the airworthy
  status in `description`. The Queensland Air Museum's Wirraway A20-652 is
  maintained in taxiable condition and is likewise `on_display`.
- **Replicas** are flagged in `description` only, never in `aliases`: the Bristol
  Scout D, CA-18 Mustang, Fokker Dr.I, Wicko Cabin Sports and Spitfire Mk I
  representation at Caloundra; the Boxkite, Deperdussin, Bleriot XI, Bristol
  F.2B, Sopwith Camel and Fokker Dr.I at Oakey; the Avro 504K, DH.50 and DH.61
  at Longreach; the Avian and Ibis at Bundaberg; the Spitfire Mk VIII at Darwin.
  The Qantas Founders Museum's Super Constellation is **not** a replica — it is a
  genuine ex-US Navy C-121J, Bu.No. 131623 / N4247K, repainted as *Southern
  Spray*. The RFDS Longreach King Air is a purpose-built full-size cutaway
  representation and is described as such.
- **Sections and cockpits are recorded as airframes**, with the extent stated in
  `description`: Caribou A4-285 (cockpit, Townsville), A4-159 (forward fuselage,
  QAM), Sea Vixen XJ607 (nose), Viscount VH-TVJ (nose), Ceres VH-CEU (cockpit),
  Porter A14-705 (nose), R44 VH-RMN (cabin), UH-1B 64-13925 (cabin), Iroquois
  A2-382 (starboard cross-section), and the four F-111 crew escape modules at
  Amberley (A8-136, A8-137, A8-141 and, formerly, A8-130 at Caboolture).
- **A single airframe on a plinth is a site.** Caloundra RSL, Bribie Island,
  Brymaroo, Meandarra, Willowbank, Calvert Field, Enoggera, Tindal and Robertson
  Barracks are each recorded as sites in their own right.

## Fields deliberately left blank

- **`year_built`** is blank on all but 15 of the 236 rows. It is filled only
  where ADF-Serials gives an explicit first-flight date (Canberras A84-204,
  A84-210, A84-225, A84-238, A84-242; Macchis A7-064, A7-072) or where the museum
  states the build year (the Central Australian Aviation Museum's DC-3, Dove,
  Drover, Beech 18, Kookaburra, Kookaburra glider, Auster and Proctor). No RAAF
  A-serial was ever read as a year.
- **`tail_number`** is blank where no identity is published: the QAM Maurice
  Farman Shorthorn, Dehn Ring Wing, Pellarini Airjeep, Winton Grasshopper, Sky
  Pup, Bensen B-8M, Birdman TL-1A, International Model Aircraft towed glider and
  SB Lim-2; the Darwin Dove, MU-2, Shrike Commander, Long-EZ, Auster J/5P, Hovey
  Delta Bird and Spitfire replica; the Oakey replicas; the Longreach Catalina,
  Constellation and three de Havilland replicas; the Caboolture Wessex,
  Boomerang and Tiger Moth; the FNQ Yale and B-17 relic; the Mareeba Queen Air.
  Construction numbers reported by a source but not confirmed as registrations
  are carried in `aliases` as `c/n <number>`, never in `tail_number`.
- **`latitude`/`longitude`** are blank for six sites where no mapped position was
  found (Kingsford Smith Memorial, Willowbank, Brymaroo, Caloundra RSL, Calvert
  Field, Lavarack Barracks). Where a site sits on a named aerodrome or base, the
  aerodrome/base reference point is used and is therefore accurate to the
  facility rather than to the building: Oakey, RAAF Amberley, RAAF Townsville,
  RAAF Tindal, Mareeba, Caboolture, Enoggera, Robertson Barracks.
- **`aircraft_name`** is used only for airframes with a genuine individual name
  (B-52G *Darwin's Pride*, the Constellation *Southern Spray*, the Fokker
  *Southern Cross*, the DH.61 replica *Apollo*, the B-17 relic *Hoomalimali*).

## Open questions, ranked

1. **Where did the Caboolture Warplane Museum's collection go?** The 2025 closure
   notice names no recipients. At minimum the F-111C **A8-130** crew module and
   Iroquois **A2-484** need to be relocated; the museum also held a Boomerang,
   Anson, Wirraway, Winjeel, T-28 and MiG-15 at various times. This is the single
   biggest gap in Queensland and should be resolved before any of those airframes
   is filed against another site.
2. **The Vampires at RAAF Townsville.** ADF-Serials places both **A79-804** and
   **A79-666** at the heritage centre, Wikipedia says **A79-656**, and the August
   2025 Defence reopening announcement names no Vampire at all. Both A79-804 and
   A79-666 are recorded here as `under_restoration`; a site visit or a photo
   dated 2025-26 would settle which airframe (or airframes) is actually present.
3. **Orion A9-757 at Darwin.** ADF-Serials records it as retired to the Darwin
   Aviation Museum in June 2018, but the museum's own "what's on display" pages
   do not mention it and give a total of 19 aircraft. Recorded as `in_storage`;
   needs confirmation.
4. **Mirage A3-100.** ADF-Serials: "Withdrawn, to Memorial at Darwin, NT
   29/09/88." No current location for this memorial was found — it is not the
   Darwin Aviation Museum's aircraft (that is A3-36). Likely on RAAF Base Darwin
   or in a Darwin park. Not recorded, because the site could not be identified.
5. **The Australian Aviation Heritage Centre's flying Boomerang and Tiger Moth.**
   Named in the March 2026 Moreton Daily report but with no serials, and it is
   not clear whether they are owned by the centre or merely based in its hangar.
   Recorded with blank tail numbers and a caveat; worth resolving, since a
   privately owned warbird merely hangared there would not be a record.
6. **Kiowas A17-033, A17-034, A17-035** were bought by the Caboolture heritage
   centre in August 2017 and none has a later ADF-Serials entry. Recorded as
   `in_storage` there; they may have been pole-mounted or on-sold like A17-005.
7. **Canberra A84-238 and A84-248 at Willowbank.** ADF-Serials notes weather
   damage, nesting birds and vandalism, with no date. Currency of the pylon
   display should be checked from dated photography before the record is trusted.
8. **Macchi A7-064 at Calvert Field.** The only evidence is a 2020 ADF-Serials
   note. A model aeroplane club is an unusual custodian and the airframe may have
   moved with A79-440, which the RAAF reclaimed from the same field.
9. **The Queensland Air Museum's three Seabird airframes** (VH-SBI, VH-SBU,
   VH-EQN) are listed by the museum as "on external loan". They are recorded
   against the museum as `in_storage`; where they physically sit is unknown, and
   under the one-airframe-one-place rule they may belong to other sites.
10. **The Beck Museum's remaining holdings.** The C-47 A65-73, Canberra A84-210
    and Vampire A79-89 have been assigned to the FNQ Aviation Museum on the
    strength of a February 2026 local-press report of "recently acquired"
    aircraft plus FNQAM's own C-47 page. If the Beck site still exists as a
    separate display, those three rows move.
11. **Vampire A79-476.** The Queensland Air Museum lists it and publishes its
    history; ADF-Serials carries a line placing it at the RAAF Museum, Point
    Cook. The museum is treated as authoritative for its own collection here, but
    the conflict is noted on the row.
12. **Kiowa "44" at Oakey.** ADF-Serials itself doubts that the "Kiowa Garden
    Display" airframe marked 44 is A17-044. Recorded with that doubt stated.
13. **Northern Territory outside Darwin, Tindal and Alice Springs.** Batchelor,
    Adelaide River, Pine Creek, Katherine, Tennant Creek, Nhulunbuy/Gove and
    Jabiru were all swept against ADF-Serials and museum directories and produced
    nothing. The WWII airfield memorials along the Stuart Highway are markers and
    interpretive panels, not airframes. Worth one pass with dated satellite
    imagery, since NT roadside displays are poorly documented online.
