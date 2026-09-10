# Pennsylvania — research and import notes

Researched and imported 10 September 2026. The state was greenfield: zero
Pennsylvania records existed, and nothing at all inside the state's bounding
box, before this work.

**50 sites · 369 airframes.** Six research passes (public museums plus a
discovery sweep; military base collections; monuments and single displays; a
county gap-fill; an identity-resolution pass; an HMdb town sweep), then a
satellite / Street View currency pass, cross-package reconciliation, a collision
check against the 19,409 then-existing tail-numbered airframes and 2,831
museum names (zero collisions after adjudication), and per-site verification
against the live API after import.

Serial coverage 269 of 369 rows. The 100 blanks are overwhelmingly civil
antiques and one-off prototypes for which no identity is published anywhere;
they are enumerated per site in the raw research files.

## Sources and their weight

1. **The FAA registry's owner-name search** — `registry.faa.gov/AircraftInquiry/
   Search/NameResult?Nametxt=<museum>` — was the single most productive tool in
   this state, independently anchoring roughly 100 airframes across five
   museums. It is the only hard evidence available for the Golden Age Air
   Museum's collection. **Punctuation matters**: "MID-ATLANTIC" returns nothing,
   "MID ATLANTIC" returns 50+. Add it to METHODOLOGY.md; it deserves to sit
   beside the per-N-number lookup, and it should be standard for every
   remaining US state.
2. **Aerial Visuals' *Location* dossier** (`LocationDossier.php?Serial=<id>`),
   not the seed search, is what cracked the American Helicopter Museum: 26
   identities where the museum publishes none and the FAA knows only one
   aircraft. The Locator search form is broken by GET but works by POST
   (`Locator.php`, `Region=Pennsylvania`, `Scope=3`), returning ~120 PA
   locations. Its vintage is roughly 2008-2015, so it is an identity source and
   never a currency source.
3. **OpenStreetMap `historic=aircraft` nodes** via the `overpass.private.coffee`
   mirror (the main API is proxy-blocked). The PA extract carries a
   **2026-07-28** timestamp, which makes it the only genuinely current
   machine-readable source in the set, and it supplied metre-level fixes for the
   whole Horsham cluster plus Whitehall, East Berlin, DuBois and Carlisle. Plain
   tag queries work; regex queries time out.
4. **HMdb** — `results.asp?Search=Place&Town=<town>&State=Pennsylvania` gives an
   exact coordinate, a photo, a dated catalogue/revision stamp and often the
   serial in the inscription. County listings paginate at 100 and a page-1
   summary silently hides markers (proven by Monroe County omitting the known
   Tobyhanna aircraft). The Air & Space topic browse cannot be state-filtered.
5. **NMUSAF "Aircraft on Loan by Location"** (April 2016) — the live PDF is 403
   to curl *and* the WebFetch summariser truncates before the Pennsylvania rows.
   All 15 PA rows were retrieved via `web.archive.org/web/2023id_/` plus
   `pdftotext`. Authoritative on custody, worthless on currency.
6. Dated site reports: Photorecon 22 May 2025 and Vintage Aviation News
   30 Oct 2025 (both Horsham); Williamsport Sun-Gazette June 2024; a
   RoadsideAmerica visitor report dated 14 Apr 2026 (Erie).
7. Google Street View and Bing aerial for the currency pass (see below).
8. Lead lists only: aviationmuseum.eu, silverhawkauthor.

## The Willow Grove question, answered

This was the state's biggest expected stale-data trap and the answer is the
opposite of what was feared. NAS JRB Willow Grove closed in 2011, but **its air
park never dispersed.** All 22 airframes remain on the Horsham site as the
Harold F. Pitcairn Wings of Freedom Aviation Museum, run by the Delaware Valley
Historical Aircraft Association — and it is now a **public walk-up museum
outside the guard fence**, not a restricted base air park. Directories have the
access type wrong, not the aircraft list. Two independent dated site reports
(May and October 2025) confirm presence.

Wings of Freedom and DVHAA are **one organisation, not two**: DVHAA, founded
1972 as the Willow Grove Historical Aircraft Association, owns and operates the
museum at 1155 Easton Road.

The famous Willow Grove captured-Axis aircraft went to Pensacola and NASM
piecemeal *decades* before the 2011 closure and are not Pennsylvania records.
F-14A 157984 has been at Pensacola since 1989.

## Corrections made

- **Tobyhanna Army Depot has a signed six-aircraft outdoor display park**, which
  the base pass had excluded as "nothing found". HMdb carries depot-erected
  markers for the AH-1S, F-14, OH-58D, OH-6A, OV-1 and RC-12H, and Aerial
  Visuals adds UH-1C 66-15193 and C-130A 54-1622. Eight rows recorded. This also
  resolved a separate Forty Fort claim: C-130A 54-1622 is at Tobyhanna.
- **The October 2025 "Marine One" H-34 at Horsham is the museum's existing
  UH-34J BuNo 145694 repainted**, not a second helicopter. Directories will
  double-count it.
- **TV-1 33824 is not a T-33.** The TV-1 is the Navy single-seat P-80C, not the
  two-seat trainer; one pass filed it as `T-33` variant `TV-1`, which is wrong
  twice. Recorded as `TV-1`.
- **F8U-1 143806 recorded as `F-8` + `A`** (the database holds 31 F-8 rows
  against 3 F8U), with F8U-1 in aliases. **H-13G 52-7833** kept as `H-13` + `G`
  (FY52, pre-1962) with OH-13G in aliases.
- **Wings of Freedom T-34B: tail left blank.** Directories give it N4028A, but
  the FAA shows N4028A **cancelled and held as a reservation by an unrelated
  party since 18 October 2025** (checked 10 September 2026). Using it would be
  wrong and would eventually collide. Registration preserved in aliases.
- **The Franklin Institute's Franklin Air Show gallery closed permanently on
  5 January 2026** and the current exhibit index lists no aviation exhibit. The
  Wright Model B stays in the building at an unannounced location; the T-33's
  fate is unreported, so it is recorded `in_storage`. The museum's own "1948
  ex-Navy TO-2" copy is an error — TO-2s carry BuNos, and 53-6038 block-checks
  as a T-33A-1-LO. **The Budd BB-1 Pioneer is confirmed still outdoors** at the
  20th Street entrance and is now the only Franklin Institute aircraft the
  public can reliably see.
- **AH-1G 67-15663 is at Carlisle, not Phillipsburg** (the 2026 OSM extract
  decides it). The Chambersburg Cobra is a different airframe, 67-15653.
- Aerial Visuals' "A-1E 122811" is impossible — it is an AD-3. AV also files New
  Jersey's Alexandria Field under Pennsylvania, and the Army list's 68-15074 is
  Monroe **Michigan** while 68-15086 is Bath **New York**.
- HMdb markers 12540 and 12542 are **one** EC-130E, not two; the Fort Indiantown
  Gap "F-102" is a two-seat TF-102A.
- "AK-503" on the Williamsport A-6E is a tail code; the true BuNo is 161676.
- Two decoys worth naming: the "Montrose Huey" is Montrose **Colorado**, and
  T-33A 51-6656 reads as Pennsylvania ANG but is displayed in Henderson, Texas.

## The imagery currency pass

Run with the built-in browser (the Chrome extension was offline). Google Maps
satellite would not render in that pane, so aerial work fell back to Bing, which
carries **no on-screen capture date** — only three checks are dated, and they
are the valuable ones.

**Confirmed present:** VFW Post 8168 Midland (Street View **July 2025**),
Carlisle Airport (Street View **October 2023**), VFW Post 8106 New Galilee
(Street View **June 2024**), plus undated aerial confirmations at Whitehall,
East Berlin, DuBois, Imperial, North Huntingdon, New Kensington Memorial Park,
Carrolltown, Lycoming County, Erie County, Butler County, Tobyhanna and Indiana
County.

The Carlisle result matters: SA-16A Albatross 49-0082 rested on a 2014 sighting
and was the single most doubtful record in the state. October 2023 Street View
resolves it.

**Fourteen sites did not show an airframe in aerial imagery** — New Kensington
VFW 92, White Haven, Towanda, Beaverdale, Pleasant Hills, West Brownsville,
Stoystown, Jersey Shore, Milford, New Berlin, Port Carbon, Fort Washington,
901 Pub and Bradford Regional. **These were NOT excluded.** All fourteen rest on
undated Bing aerials with no dated Street View pass, and a small pole-mounted
helicopter is easy to miss from directly overhead. Removal needs positive
evidence, not an unclear photograph. They are recorded with their single-source
provenance stated in each description, and they are the priority list for the
next imagery pass.

## Excluded, and why (do not re-research)

- **Allegheny Arms & Armor Museum, Smethport** — A-6A 147867 and CH-34A
  57-1698/N94485 are satellite-mapped there and an AH-1F has already departed,
  but the newest dated evidence is 2010 photographs describing them as "very
  poor shape" plus a 2017 comment. Fails the 2025-26 test.
- **Beaver County Airport F-86H 53-1338** — the 2016 NMUSAF list assigns it to
  "BEAVER COUNTY BEAVER FALLS PA" and Wikipedia places it at the airport, but no
  separate gate guard is visible anywhere on the field in current imagery, and
  it is not in Air Heritage's own collection. The site record was dropped rather
  than shipped with a coordinate that points at the museum ramp. One call to Air
  Heritage settles whether it is indoors, moved, or gone.
- **Three coordinates were blanked** because they resolved to unrelated land —
  VVA Chapter 210 Doylestown (downtown retail core), The Collegeville Pit Stop
  (farmland) and Willow Grove Veterans Memorial Park (a supermarket block). A
  blank beats a wrong fix; the addresses are recorded.
- Flight 93 National Memorial (no aircraft); Pennsylvania Military Museum
  Boalsburg (armour only); the PAFA "Grumman Greenhouse" S-2 at Lenfest Plaza
  (removed August 2022 — and Aerial Visuals' two dossiers for it were one object
  under two conflicting BuNos); CAF Keystone Wing West Mifflin (closed); the
  Penndel Constellation; Isett Heritage Museum's "KC-135" (a cargo load-planning
  trainer, not an airframe); Dutch Springs (submerged); Colonial Flying Corps
  Museum (no 2023-26 evidence); Mercer (private storage, and F-86F 52-5303 fails
  its block check); Scotrun BK-117 (unidentified).
- **Every Pennsylvania Nike memorial is plaque-only** — no missile at any of
  them, Herminie included. Re-verified twice.
- **Biddle ANGB (111th Attack Wing) has no gate guard or heritage display** — an
  MQ-9 unit with nothing on station. Recorded here as a confirmed absence so it
  is not re-researched.
- 911th AW Pittsburgh, 193rd SOW Harrisburg (its heritage EC-130E is at Fort
  Indiantown Gap), Boeing Ridley Park, Philadelphia Naval Shipyard, Letterkenny,
  New Cumberland, all ROTC and campus displays, and all former airfields:
  searched, nothing found.
- Instructional airframes at four college A&P programmes, and ~15 based or
  operational airfield fleets that Aerial Visuals lists as though they were
  displays.

## Deliberately blank

- 100 tail numbers, chiefly 27 American Helicopter Museum exhibits for which no
  source anywhere publishes an identity (named individually in the phase 5 file
  so nobody re-researches them), plus civil antiques at Golden Age and Eagles
  Mere.
- `year_built` except where an FAA `YEAR-MFR`, acceptance or roll-out date
  exists. Fiscal-year prefixes were never used.
- Coordinates at the three sites named above.

## Test-suite fixes applied before import

The build failed four checks on first pass and was corrected at source, in the
raw pipe files, so the fixes survive a rebuild: `PA-41P` split to model `PA-41`
+ variant `P`; the attribute aliases "reproduction" and "replica" moved from
`aliases` into `description` at Mid-Atlantic and Wings of Freedom; and
`painted 61071` reduced to the bare identifier `61071` at Carlisle. Full suite
green at 42,152 tests before anything was applied.

## Needs a human (ranked)

1. **American Helicopter Museum, (610) 436-9600.** 27 of its 42 exhibits have no
   published identity anywhere. One call closes more blank tails than any other
   action available in this state, and would also confirm the CH-21C, VZ-8P
   Airgeep and V-22 FSD identities that currently rest on a single source.
2. **The Midland Cobra's serial.** An AH-1 is physically confirmed at VFW Post
   8168 by July 2025 Street View, but imagery cannot read a serial, and the
   serial Aerial Visuals attaches to it — **71-21031** — is already held in this
   database at the **Mid-America Air Museum, Liberal, Kansas**, marked
   `in_storage`. Aerial Visuals' own dossier for 71-21031 gives its current
   location as the Midland post and shows no Kansas history at all, so the
   Kansas record looks like the wrong one and its description misquotes what AV
   actually says. The Midland row was therefore imported with a **blank
   tail_number** and the serial in aliases: it duplicates nothing and overwrites
   nothing, and either placement is recoverable. Resolving it needs a data-plate
   photograph at Midland or a call to Mid-America (620-624-5263). **This is also
   a pre-existing data-quality bug in the Kansas records, not just a PA issue.**
3. **A dated Street View pass over the fourteen sites that did not show in
   aerial imagery** (listed above). This is the cheapest large quality win left.
4. **Beaver County F-86H 53-1338** — Air Heritage, (724) 843-2820.
5. **Franklin Institute**, (215) 448-1200 — where the Wright Model B now sits
   and what happened to the T-33 after the gallery closed.
6. **29 counties were never queried on HMdb** and 14 were read at page 1 only,
   which given pagination hides markers. Fort Indiantown Gap's public heritage
   trail may also hold more than the seven aircraft recorded.
7. Chambersburg/Guilford Township AH-1G **67-15653** has a serial but no
   location or sighting — not recorded, worth one local check.
