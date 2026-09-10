# Central America — Guatemala, Belize, El Salvador, Honduras, Nicaragua, Costa Rica, Panama

Sweep run 10 September 2026. **Prior database state: zero sites and zero airframes in
all seven countries.** Region field is recorded as `North America`, matching the
existing Caribbean records (Museo Girón, Cuba) — the schema has no `Central America`
value and one was not added for this pass.

## What went in

**25 sites · 84 airframes · 6 of 7 countries.**

| Country | Sites | Airframes |
|---|---|---|
| El Salvador | 11 | 39 |
| Guatemala | 6 | 10 |
| Costa Rica | 4 | 6 |
| Nicaragua | 2 | 2 |
| Belize | 1 | 1 |
| Honduras | 1 | 26 |
| **Panama** | **0** | **0** — a researched negative, not an unfinished search |

Files: `central_america_museums.csv`, 25 `*_aircraft.csv` (one per site),
`central_america_raw.txt` (the pipe-delimited research input), and the four
full per-country research dossiers `research_*.md`, which carry the evidence
behind every line below.

Serial coverage is 62/84 (74%) — high for a region with this little published
airframe-level material, and almost entirely down to one source (see below).

## Sources, and how they performed

**`flotilla-aerea.com` carried El Salvador single-handed and belongs in
`METHODOLOGY.md`'s hierarchy.** "Aeronaves de El Salvador en exposición"
(28 Sep 2018, revised through 2025) is airframe-level national research with c/n,
USAAF serial or BuNo, delivery date, withdrawal cause and display location for every
preserved FAS airframe. It also documents its own uncertainties — FAS tail booms were
swapped in maintenance so fuselage and tail serials disagree, ID plates were removed on
pre-1980 deliveries, and some airframes were renumbered to commemorate events with no
record of the change. That is rung 3 material, not rung 8.

**The Salvadoran Air Force's own museum page is stale and must not be used as an
inventory.** `fas.gob.sv/museo` is written in the future tense and lists an Ouragan
"FAS 714" and a C-47 "FAS 106" that match no preserved airframe; the displayed Ouragan
is FAS 713 and the three preserved Dakotas are FAS 109, 114 and 115. The page appears to
predate a 2017 move. Its contact/hours page is current and was used.

**`aviationmuseum.eu` failed again, in two new ways.** It claims 37 aircraft at the
Museo del Aire de Honduras *including an F-5E* — the enabling Congress decree (144-2003)
and the museum's own list both say 25, plus C-130 FAH-558 added later, and the FAH still
operates F-5s. No F-5 record was created. Its Museo Militar (Guatemala) coordinate is
~11 km west of the actual site, the same failure mode measured in Mali; its coordinates
were discarded wholesale. Its Costa Rica and Nicaragua pages are **empty**, and its
Panama page is a stub soliciting information.

**OSM Overpass found what search could not.** Run from the local bridge after the
container's proxy blocked it, `historic=aircraft` over the whole isthmus returned three
Guatemalan airframe-level nodes; two became records (Parque Natural Altamira, Antigua;
Piper PA-23-250 YN-CAZ at Lemon Tree Hostel, Antigua) with airframe-level coordinates.
**Overpass should lead, not follow, in any region where English coverage is thin.**

Wikipedia's survivor lists — P-51, T-33, C-47 — have **no Central American entries at
all**, despite a Mustang standing in public view in Guatemala City for ~47 years. Those
are gaps in Wikipedia, not evidence of absence, and they are why the negative results
below are reported as searched rather than as confirmed.

## Corrections made

1. **The Football War premise is wrong for El Salvador.** There is no Mustang and no
   Corsair left in the country; every ex-FAS piston fighter left decades ago. FG-1D
   ex-FAS 207 (wearing a false "FAS 220") and ex-FAS 217 went to US collectors; F-51D
   ex-FAS 404 stood in Ilopango's central park 1971–74 and was destroyed at Galveston in
   2013. **The only Football War piston fighter still in Central America is Honduras's
   F4U-5N FAH-609, BuNo 124715** (Warbird Registry; photographed at Toncontín 2 Mar 2011
   with three kill marks, under cover since a 2012 restoration).
2. **The Guatemala Mustang's "336" is paint, not identity.** AirHistory says it was
   displayed in camouflage as "360" and repainted silver as "336" in the mid-1980s; the
   Warbird Registry says the reverse. `tail_number` is blank and both numbers are
   aliases. Importing "336" would be importing paint.
3. **El Avión's C-123 at Quepos is NOT the Hasenfus aircraft.** That was Corporate Air
   Services HPF821 (ex-N4410F, c/n 20128, ex-USAF 54-679), destroyed in Nicaragua. The
   Quepos airframe is the sister ship and its own identity is unestablished; a "54-663"
   read off a 2019 photograph is recorded as a marking only.
4. **Curtiss Robin TI-BGZ moved in May 2025** from the Juan Santamaría domestic terminal
   to the Museo Aeronáutico de Costa Rica at IFA Heredia, where it is disassembled under
   restoration. Every list still placing it at the airport — including oldjets.net as of
   Feb 2024 — is stale.
5. **"Museo del Ejército de Guatemala" and "Museo Militar y Ex Fuerte de San José" are
   one institution** (SIC carries it a third way, as "Museo Servicio de Historia
   Militar"). Recorded once.
6. **A-37B A-416's "69-6404" is an order serial**, not a build year. No `year_built` in
   this region was taken from any serial; the five populated years all come from stated
   build or delivery dates.

## Judgment calls

- **Hotel and restaurant conversions are site records.** Costa Rica's preserved-aircraft
  landscape is *mostly* this: Hotel Costa Verde (three airframes), El Avión, Suites
  Charter Boutique. Deliberate retention plus public presentation is the test and they
  pass it. The two hotels are `appointment` because the airframes are gated behind a
  booking; El Avión is a walk-in restaurant, so `public`.
- **Costa Verde and El Avión recorded as two sites** despite likely common ownership —
  El Avión has its own name, address, website and access model. Flag for merge if
  ownership is confirmed.
- **Ilopango is six sites, not one.** Flotilla Aérea consistently distinguishes the
  Museo Nacional de Aviación (7 airframes, indoors) from the Plaza de la Aviación (8, on
  the apron); the base unit displays (10), the paratrooper C-47 monument, the AAC/ICCAE
  compound and the Comalapa 2nd Air Brigade are all separately located. Merge the museum
  and the Plaza only if a curator says they are one exhibit.
- **Three airframes are `Unidentified`.** The Cobán roundabout monument, the Altamira
  trail aircraft and the Condega hilltop FAN twin all have real, sourced site records and
  no sourceable type. `manufacturer` and `model` are required fields, so they follow the
  existing house precedent (`Unidentified` + a descriptive model, as used for the two
  autogyros already in the database) rather than being dropped or guessed. Every other
  identity field on those three rows is blank.
- **The Condega airframe is a shoot-down, not a crash site.** Hit by FSLN fire on
  7 April 1979, forced down near the town slaughterhouse largely intact, then dragged
  onto the hill by a civic committee and made the centrepiece of a public mirador.
  Deliberate retention — it is a record. The Perquín Museo de la Revolución wreckage was
  judged the same way.
- **Generic site names carry a `-- <City>` suffix** (Plaza Bicentenario -- San Salvador,
  Restaurante El Avión -- Manuel Antonio, Museo Nacional de Aviación -- Ilopango, and
  eleven more). "Museo Nacional de Aviación" and "Parque Mirador El Avión" are exactly
  the class of name that collides across a continent.

## Excluded, with reasons

- **Panama, entirely.** ~20 Spanish and English query sets plus every reference list
  returned nothing enterable. Wikipedia's T-33 and C-47 survivor lists both omit Panama,
  aviationmuseum.eu's page is an empty stub, silverhawkauthor has no Panama page, and the
  Autoridad de Aeronáutica Civil's own national aviation history page mentions no
  preserved aircraft, museum or monument anywhere in the country. The strongest
  candidate — a **Fokker 100 placed on Naos Island in 2021** as a restaurant billed as
  including a *museo aeronáutico* — was ordered removed by the AAC, classified as scrap
  and hauled away (La Prensa, 21 May 2026). No captured Panamanian Defense Forces
  airframe could be confirmed in any US museum either; Just Cause sources describe FAP
  aircraft destroyed on the ground rather than taken as trophies.
- **Northrop F-5E at the Museo del Aire de Honduras** — aviationmuseum.eu only, against
  the museum's own list and the enabling decree. Not recorded.
- **T-41A at the Ilopango museum** — appears on the FAS museum page and nowhere in
  Flotilla Aérea's inventory. Not recorded.
- **Museo de Historia Militar, Tegucigalpa** — its "aircraft collection" is scale models.
- **Monumento "El Aviador", Totonicapán** — a helicopter propeller on a plinth, not an
  airframe (SIC's own description).
- **OSM node 13135133403, Playa Grande Ixcán** — `historic=aircraft` and nothing else;
  3.2 km from the airport and 4.5 km from the parque central, in the one municipality in
  Guatemala where "a plane in a field" is most likely to be an abandoned narco airframe.
  Kept as a lead, not made a record.
- **Museo Nacional de Costa Rica** — holds no aircraft. **"Museo Aéreo Fénix"** — is in
  Panama City, **Florida**; a recurring false positive worth remembering.
- **Operational fleets**: SENAN's UH-1Hs and UH-1STs, the FAN ramp at Sandino, Nicaragua's
  annual Exposición Estática, COOPESA storage at SJO. **Departed airframes**: the
  "Panchito" DC-3 (scrapped), the UH-19B that left La Aurora in 2015, ex-FAS/FAH Corsairs
  and Mustangs now in the USA.

## Deliberately blank

- **Coordinates on 16 of 25 sites.** Only Ilopango's museum, the two Antigua OSM nodes
  and a handful of Nominatim feature-level matches gave a defensible fix. The rest would
  have been town or air-base centroids, and a centroid dressed up as a fix is worse than
  nothing.
- **`year_built` on 79 of 84 rows.** No sourced construction date existed.
- **`tail_number` on 22 rows**, including all four Guatemala City monuments except the
  A-37B — no Guatemalan source publishes serials.
- **The Beechcraft Twin Bonanza's `military_civilian`** was blank in research (the museum's
  own inventory gives no registration and no provenance). It is recorded `military` /
  `utility` because the validator requires a value and the site is the Honduran Air Force
  museum; the description says so explicitly. This is the one field in the region set by
  default rather than by source.

## Needs a human — ranked

1. **Fundación Museo del Aire de Honduras — museo_del_aire@live.com, +504 9992 4543.**
   One call resolves the Kingcobra serial (FAH-402 vs FAH-403), the F-5E claim, the
   Twin Bonanza's provenance, and probably several coordinates.
2. **Honduras outside Tegucigalpa is a hole.** Twelve Spanish searches across San Pedro
   Sula, La Ceiba, Comayagua/Palmerola, Catacamas and Juticalpa returned zero monuments
   or gate guards. That is implausible for a country with a 90-year air force. Nothing
   was recorded rather than guessed — this is the region's largest known gap.
3. **Belize's Harrier GR.3 ZD669** is the weakest record in the region: two independent
   sources agree it survives at Ladyville, neither gives an address, owner or dated
   photograph, and OSM has no node. `restricted` was chosen because the only credible
   location is inside Price Barracks; if it stands outside the wire this should become
   `public`. BATSUB or the Belize Defence Force would settle it.
4. **Guatemala City zona 13 serials.** Four plinthed airframes on a public street and
   three of the four have no published serial. One visitor with a camera closes it.
5. **The Cobán monument (Sep 2020) and the four-airframe zona 13 row (Nov 2019/2020)**
   both rest on 5–6 year old evidence with no confirmation they are still standing.
6. **Panama: an Overpass + satellite imagery sweep of Albrook, Panamá Pacífico, Río Hato
   and David**, plus calls to UTP's aviation school and SENAN. The region-wide Overpass
   run for this pass returned nothing in Panama, which strengthens the negative but does
   not close it — imagery was never checked.
7. **Managua 737-200 TG-REX vs N103HA** rests on one source (oldjets); the airframe now
   wears political slogans and no photograph shows the registration legibly.

## A note for the schema backlog

Every airframe in this region was imported with `operator_country` blank, because the
house research contract does not carry the field. The region is full of two- and
three-digit national serials of exactly the kind that broke Russia and the Middle East
(FAS 500, FAS 601, FAH-105, A-416). Nothing collided this time, but populating
`operator_country` from the research contract — now that `uq_airframe` includes it —
would make that safe rather than lucky.
