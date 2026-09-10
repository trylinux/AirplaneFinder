# Canada — coordinator summary

Imported live 10 September 2026. Five research passes: major museums east and
west; Canadian Armed Forces base displays; and monument sweeps of western and
eastern Canada. The per-pass research notes follow this summary unchanged;
where they disagree with this section, this section is what was imported.

Canada previously held **one site with two aircraft** — the Canada Aviation and
Space Museum with a Lancaster and a Mosquito, against a real collection of
about 130. It received a **138-row top-up**; everything else is new.

**Files:** `ca_museums.csv` (159 new sites) and 160 `*_aircraft.csv` files, one
per site.

**Rows:** 1230 aircraft · 955 with tail numbers (77%) ·
1029 on_display / 144 in_storage / 57 under_restoration.

**Sites by province:** Ontario 64, Alberta 22, Quebec 17, Manitoba 13, British Columbia 12, Nova Scotia 7, Newfoundland and Labrador 7, Saskatchewan 6, New Brunswick 6, Northwest Territories 3, Yukon 1, Prince Edward Island 1.
**Access:** 126 public · 13 appointment · 20 restricted.

**Largest collections:** Reynolds-Alberta Museum 145, Canada Aviation and Space Museum 138, Canadian Warplane Heritage Museum 45, Canadian Museum of Flight 43, National Air Force Museum of Canada 42, Alberta Aviation Museum 40, British Columbia Aviation Museum 40, Royal Aviation Museum of Western Canada 39, The Hangar Flight Museum 31, Bomber Command Museum of Canada 28.

**Coordinates:** every site has one. 113 were fixed by the researchers —
mostly from Aerial Visuals Location Dossiers, which carry mapped display
positions — and the rest were geocoded by the coordinator, level recorded per
site in `ca_geocode_log.csv`: 18 from the street address, 16 from the
postal code, 12 city-level.

## The brief's designated spine is dead

`rwrwalker.ca` — the Canadian Military Aircraft Serial Numbers site, and the
best per-serial disposition register Canada had — **no longer exists**. The
domain now serves an online-casino affiliate site under the name "Walker
Military Insights"; its WordPress API exposes about sixty surviving aviation
pages, and the CF-100, CF-104, CT-133, CT-114 and Sabre pages are not among
them. All five agents hit this independently. The full original is in the
Wayback Machine (333 pages, best capture `20211025221528`), but web.archive.org
was unreachable from this environment. **Someone should mirror it before it
ages out.**

What the agents substituted, in order of usefulness:

- **`caspir.warplane.com`** — the Canadian Warplane Heritage Museum's serial
  database, built on Griffin's registries and RCAF record cards, organised by
  type and serial with dated dispositions and last-update stamps in August
  2026. This is the most likely permanent replacement for rwrwalker and should
  be the spine for any future Canadian work.
- **`aerialvisuals.ca` Location Dossiers**, reached via
  `Airframes.php?Seeds=` → `AirframeDossier.php` → `LocationDossier.php`, or
  the Locator with `ShowMap=1`, whose embedded map markers pair each site's
  coordinates with its dossier link. This is where most of the coordinates in
  this package come from. It rate-limits hard — roughly one request per minute,
  then an extended block — and returns an empty body to curl while fetching
  fine through a browser fetch.
- **`silverhawkauthor.com`** (Harold Skaarup, *Canadian Warplanes*) — per
  province, per town and per type, far richer than Wikipedia for Canada. Its
  trap: photo captions and display entries are interleaved, which produced most
  of the location conflicts below, and it carries airframes at museums they
  left years ago.

Two environment facts worth passing on: `en.wikipedia.org` article pages return
"domain is cache-only" here, but `curl .../Special:Export/<Title>` works; and
airhistory.net is blocked outright.

## Cross-pass adjudications (one airframe, one place)

Sixteen sites came back recorded twice under different names and were merged
rather than imported — Comox, Greenwood, Base Borden, Summerside, the Canadian
Harvard Aircraft Association, the Saskatchewan Aviation Museum, The Military
Museums Calgary, RMC Kingston, KF Centre, the RCMP Heritage Centre, Val-d'Or
and others. `_fix_adjudications.py` reproduces every decision.

Twenty-four airframes were claimed by two different sites. The rule applied,
and stated here because it will recur: **a dated first-party museum listing
beats a third-party survey, and a public display beats a restricted
instructional airframe** — the database answers "where can I go and see this".
So CT-114 114021 and 114063 went to the Western Development Museum and the
Memorial Military Museum rather than to CFSATE Borden's training hall; CC-144
144614 to the Musée de l'aviation de Montréal, which put it on outdoor display
on 28 July 2026; CT-134 134222 to Canadian Warplane Heritage on its own
September 2026 collection page. Where a monument had the fuller provenance it
won instead: CT-114 114115 stands on a pylon outside the Comox Valley Visitor
Centre, 114187 at Creston Millennium Park with its full taken-on-strength
chain, CT-133 133648 as the Princeton Airport weathervane.

**Wikipedia's Canada Aviation and Space Museum table is materially wrong.**
Three airframes it credits to Ottawa are at Hamilton — CF-100 100785 (moved
1 August 1996), Spitfire TE214 (on loan since about 1997) and Sabre 23651
(Ingenium's own page says its Sabre is 23455). All three were removed from the
top-up before import.

**The existing Ottawa database row is probably misattributed.** It records
`Lancaster B.X KB726`; KB726 is the memorial marking worn by the Canadian
Warplane Heritage Museum's airworthy FM213. Ottawa's Lancaster is **KB944**.
That live row should be corrected.

## Live-database corrections made during this pass

- **Junkers F 13 CF-ALX left Berlin.** It was loaned to the Deutsches
  Technikmuseum in 2005 and **returned to the Royal Aviation Museum of Western
  Canada in September 2024** (Vintage Aviation News). The Berlin record's tail
  was blanked with the history written into it, and the row was removed from
  `data/germany/dtm_berlin_aircraft.csv` so a re-import cannot reintroduce it.
- **Bolingbroke 9041** was recorded as a nose section at the Manx Aviation and
  Military Museum. The complete restored Bolingbroke Mk IV 9041 is at the
  Bomber Command Museum of Canada; nose-section serial attributions from the
  Canadian prairie recoveries are frequently approximate. The Manx record's
  tail was blanked, with the reasoning written into it.

## Coordinator corrections applied before import

- 314 dashless designation aliases added (`CF100`, `CF104`, `CT133` …).
- `HS-2L` split to `HS-2` + `L`; the Sperwer UAV's `aircraft_type` corrected
  from `drone` to `fixed_wing` (Q-designated UAVs are aircraft); an
  amateur-built "Edelweiss" whose name sat in the manufacturer column moved
  into `model`, which the importer requires.
- Buchón **C.4K-114** blanked at Nanton: Ottawa and Nanton record the same
  Spanish serial on Buchóns of different construction numbers, so one is wrong.

**Validation:** every row passed `_validate_aircraft_row` and the alias suite;
zero museum-name collisions against the 2,672 museums then live; a combined dry
run of all 1230 rows returned `created: 1230, linked: 1230, errors: []`;
after import all 160 per-site live counts equal the file counts and every
Canadian site carries coordinates.

## What is still open

- **Both Bomarc sites are empty.** North Bay's missile was on loan from the
  NMUSAF and was removed on 15 September 2009; La Macaza's squadron stood down
  in 1972 and only bunkers remain. Canada's two preserved Bomarcs are at Ottawa
  and Edmonton.
- **Shearwater's 17 airframes and the Atlantic Canada Aviation Museum's 25 have
  no published serials**, and the third-party surveys contradict each other.
  Two phone calls would close fifty rows.
- **Warner, Alberta** — up to three CT-133s are placed there by two sources
  with no owner, address or access evidence. Excluded; the biggest unresolved
  cluster in the country.
- **CF-101 101037 at Slemon Park** is reported scrapped in 2025 while the
  park's own page still lists it.
- **Two ex-German Sabre 6s, at Winnipeg and Bagotville, are both quoted as
  serial 23605.** Neither row carries a serial.
- **New Brunswick Aviation Museum closed on 1 June 2026** and its collection
  dispersed; the destinations are unknown.
- Reynolds-Alberta's 146 rows are a soft `on_display` — the museum says not all
  of its collection is exhibited, and the display-versus-warehouse split is not
  published.

---

# Research pass: major museums, Ontario eastward, and the Ottawa top-up

# Eastern Canada aviation museums — research notes

Scope: major aviation museums in Ontario, Quebec and Atlantic Canada, plus a
top-up file for the Canada Aviation and Space Museum in Ottawa.
Research done 10 September 2026. Output directory `/home/claude/ca/museums_east/`.

---

## 1. The brief's spine source is gone

**`rwrwalker.ca` no longer exists as an aviation site.** The domain now serves a
Canadian online-casino affiliate page under the name "Walker Military Insights";
every old path (`/CF100_detailed_1.html` etc.) 302-redirects to unrelated
content. There is no serial data there at all. Every other Canada agent should
be told this before they burn calls on it.

**The replacement I used is `caspir.warplane.com`** — CASPIR, the Canadian
Aircraft Serial Presentation and Information Retrieval database run by the
Canadian Warplane Heritage Museum. It is built on J. A. Griffin's registries and
the RCAF aircraft record cards, is organised by type and serial, gives a dated
disposition history per airframe, and is actively maintained (records I read
carried "last update: 2026-August-19"). One type page is one large HTML document
(the Canuck page is 2.6 MB), so fetch it with curl and grep it rather than
running it through a summariser. It resolved the CF-100 conflict below outright.

## 2. Source weighting, and what proved stale

| Source | Weight | Verdict |
|---|---|---|
| `airforcemuseum.ca/wp-json/wp/v2/aircraft` | 1 — structured museum feed | Best source in this whole sweep. 43 airframes, serials on nearly all. Two internal errors (below). |
| `warplane.com/aircraft/collection/details.aspx?aircraftId=N` | 1 — structured museum pages | Excellent: serial, c/n, civil registration, current markings, build year, and an explicit status/airworthiness field per airframe. |
| `ingenium.ca/aviation/en/activity/reserve-hangar/` | 2 — museum's own | Authoritative and current for what is in CASM's Reserve Hangar; 68 aircraft named. Contains airframes Wikipedia's CASM list omits entirely. |
| Museums' own collection pages (ACAM, Shearwater, GMAM, NAAM, MAM, JAM) | 2 | Reliable for *what is here*, but none of these six publishes serial numbers. |
| `caspir.warplane.com` | 3 — registry | Reliable, dated, sourced to record cards. |
| `aerialvisuals.ca` airframe dossiers | 3 — registry | Good per-serial history with display dates. The Locator search needs its own form parameters; a hand-built query string is rejected ("Unable to handle request string"), so I only used direct `AirframeDossier.php?Serial=` hits found via search. |
| `aviationmuseum.eu` | 3 — enthusiast survey | Per-site tables with registration *and* serial. Undated, so currency is unknown, but internally consistent. Used for Base Borden, Bagotville and part of the Jet Aircraft Museum, always flagged in `description`. |
| Wikipedia museum lists | 4 — lead only | The CASM article's aircraft table is **materially wrong** (below). Bushplane and CHAA articles held up better. |
| `silverhawkauthor.com` | 4 — lead only, **contaminated** | Its per-museum pages mix in airframes that are somewhere else and repeat serials. See below. |

### silverhawkauthor.com is not safe to copy from
Its Canadian Warplane Heritage page lists Spitfire TE214, Sabre 23651, CF-100
100785 *and* CT-133 21275 alongside a Vampire also numbered 21275 — two
airframes with one serial. Its Edenvale page gives the Conservancy CT-134 134222
and Tutor CF-LTW-X, both of which the owning museums' own pages place elsewhere
(Hamilton and Trenton respectively). Its Shearwater page lists a Supermarine
Stranraer, which is at the RAF Museum. I used it only where nothing better
existed, and said so in every affected `description`.

---

## 3. Corrections and conflicts resolved

**CF-100 100785 — CASM vs Hamilton. Resolved for Hamilton.** Wikipedia credits
CASM with two CF-100s, 100757 and 100785. CASPIR's record for RCAF 18785
(= CAF 100785) reads: painted black for the type's retirement, made the last
operational Canuck flight on 3 December 1981, delivered to the museum at
Rockcliffe on 10 February 1982, "On display at the Canadian Warplane Heritage
Museum in Hamilton from 1 August 1996, still there in 2022." CWHM's own page
confirms it. **100785 removed from the CASM top-up.** CASM's 100757 (RCAF 18757,
"Preserved in National Aeronautical Collection by 1982") stands.

**Spitfire LF Mk XVI TE214 — recorded at Hamilton, not Ottawa.** The aerialvisuals
dossier for TE214 puts it in the CASM inventory from 1966 and on loan to CWHM
from about 1997, photographed there in 1997 and 2004; CWHM's own page carries it
with c/n CBAF.IX.4424 and registration C-GVXI. The methodology says record where
a visitor finds it, so it is in the CWHM file with the ownership stated in the
description. **Removed from the CASM top-up.**

**Sabre Mk 6 23651 — Hamilton.** Ingenium's own Sabre collection-highlight page
says CASM's Sabre is 23455 and nothing else; CWHM's page carries 23651 with
c/n 1441. Wikipedia gave CASM both. **23651 removed from the CASM top-up.**

**Lancaster: the existing Ottawa database row looks wrong.** The database
currently records `Lancaster B.X KB726` at the Canada Aviation and Space Museum.
KB726 is not an Ottawa airframe — it is the memorial marking worn by CWHM's
airworthy FM213 (c/n 3414, C-GVRA), honouring Andrew Mynarski VC. CASM's own
complete Lancaster is Mk X **KB944**. **Before importing the CWHM file, the
existing Ottawa row should be corrected from KB726 to KB944**, or the two will
collide on the serial. I left both the complete Lancaster and the Mosquito out
of the top-up because they correspond to the two rows already in the database;
I did include CASM's Lancaster **nose section KB848**, which is a genuinely
separate airframe.

**CASM's Mosquito.** The database row says "Mosquito B.35"; the museum's own
Reserve Hangar list says "de Havilland D.H.98 Mosquito B XX" and Wikipedia gives
KB336. Same aircraft, differing variant call. Not re-recorded; flagged here.

**Trenton feed errors.** The museum's own JSON gives serial 118101 for *both* its
CH-136 Kiowa and its CH-118 Iroquois. 118101 is an Iroquois number, so the Kiowa
row carries a blank serial. The Boeing 720 entry says "C-EFTB" in the header
field but "C-FETB" in the body text; I used C-FETB.

**H-5/HO3S 9601 — unresolved.** Trenton's own listing gives its Sikorsky H-5
Dragonfly as 9601; Wikipedia gives CASM an HO3S-1 Dragonfly as RCN 9601. Both
cannot be right. I kept 9601 on the Trenton row (museum's own source) and
**blanked nothing on the CASM row** — the CASM row still carries 9601 with the
conflict stated in its description. One of the two needs a human.

**Auster VF582 — unresolved.** Trenton's own listing gives its Auster AOP.6 as
RCAF 16651 / ex-RAF VF582. Wikipedia gives CASM's Auster AOP.6 as VF582. CASM's
Reserve Hangar list confirms it *has* an Auster but gives no serial, so the CASM
row's serial was left blank and Trenton keeps 16651.

**CC-115 Buffalo 115452 — Ottawa, not Borden.** Ingenium's press release and the
aircraft's own collection page confirm 115452 (last operational CC-115 flight,
15 January 2022) arrived at CASM in October 2023 and lives in the Reserve
Hangar. The aviationmuseum.eu Base Borden table still lists 115452 at Borden;
that entry is stale and Borden's Buffalo is not recorded here.

**Avro 504K G-CYCK — Ottawa.** Same source lists G-CYCK at Base Borden; CASM has
G-CYCK on display. Borden's Avro 504K is recorded with a blank serial.

**CWHM Buffalo is not 115461.** CWHM's own page identifies it as ex-Sudanese Air
Force 811, c/n 85, *painted* as CAF 115461. Recorded with a blank tail number
and the false marking in `aliases`, per the brief.

**Base31 is a separate site, not a Trenton row.** Lancaster KB882 is not at
Trenton. NAFMC's restorations page says it is on temporary public display in
Hangar 1 at Base31 in Picton, exterior restoration finished June 2024, returning
to Trenton in 2029. It has its own site record and its own one-row file.

---

## 4. Judgment calls

- **CASM Reserve Hangar = `in_storage`.** The museum calls it "8,200 square
  metres of storage space" and it is only reachable on a paid guided tour at
  11:30 and 13:30, 15 people at a time. I marked those 68 airframes
  `in_storage` and said in every one of their descriptions that the public *can*
  see them on the daily tour, so a reader is not misled either way.
- **Museums on military bases: `public`, not `restricted`.** The brief defines
  `restricted` as "inside a base gate". Greenwood's museum is explicitly "just
  outside the main gate at 1 Ward Road"; Bagotville's is off-base at 6513 chemin
  des Aviateurs on Route 170; Shearwater's has a civic street address and normal
  opening hours; Base Borden's has published hours and free admission. All four
  are recorded `public`. Only Borden is genuinely inside a base perimeter, and I
  judged published-hours-free-admission to outweigh the literal reading.
- **Replicas kept, and labelled.** The Great War Flying Museum's entire fleet is
  modern flying replicas; so are the Conservancy's two Arrows, the several
  Silver Darts, Trenton's Spitfire and Hurricane, and Shearwater's Hurricane.
  Every one says "replica" in `description` and none carries "replica" in
  `aliases`.
- **Cockpit and nose sections in scope, stated plainly**: CASM's Lancaster KB848
  nose, Jetliner nose, Comet nose and Arrow nose; the Montreal Bolingbroke 9066
  nose; the Conservancy's Nimrod XV239 tail section; Gander's DC-3 cockpit; the
  Jet Aircraft Museum's CT-133 133648 cockpit trailer.
- **Airworthy aircraft recorded `on_display`** where the museum shows them
  between flights (CWHM's Lancaster, Mitchell, Canso, Dakota etc.), with the
  airworthiness in `description`.
- **Serial left blank rather than guessed** in 107 of 410 rows. That is entirely
  deliberate and concentrated in three museums (Shearwater, ACAM, Gander) that
  publish no serials and where the available third-party surveys contradict each
  other.

---

## 5. Excluded, and why

| Site | Reason |
|---|---|
| **Billy Bishop Home and Museum**, Owen Sound | No airframe of any kind. Uniforms, medals, photographs and scale models only. Out of scope. |
| **Secrets of Radar Museum**, London ON | Radar equipment and personal histories; no aircraft, missile or rocket airframe. Out of scope. |
| **Diefenbunker**, Carp ON | Cold War bunker museum. No aircraft and, despite the Bomarc connection in the story it tells, no missile airframe found in its own material. Out of scope on present evidence — worth a human check. |
| **Canada Science and Technology Museum**, Ottawa (Ingenium) | Nothing in Ingenium's own listings shows an aircraft, missile or rocket airframe there; its aviation collection is at CASM. Excluded for want of evidence, not asserted empty. |
| **New Brunswick Aviation Museum**, Miramichi | **Closed as of 1 June 2026**, aircraft and artefacts dispersed. Its Vampire and its 1947 Navion C-GYIY went to a British Columbia museum, the Taylor JT-1 C-FWVG went back to its owner, artefacts to the New Brunswick Military History Museum in Oromocto. May reopen under new leadership. |
| **Niagara Aerospace Museum** | In New York State. Out of scope, as the assignment said. |
| **Canadian Museum of Rail Travel** | Skipped as instructed. |
| **CWHM North American Yale RCAF 3350** (C-FCWZ) | The museum's own page says "On loan to the South Carolina Historic Aviation Foundation". Not in Hamilton, so not recorded there. |
| **CWHM Canso A RCAF 11024** (C-FUAW) | The museum's own page gives its status as "To be on display in British Columbia". Not recorded at Hamilton. Lead for the BC agent. |
| **Conservancy Lancaster FM104** | Transferred to the British Columbia Aviation Museum. Lead for the BC agent. |
| **Gander International Airport heritage displays** | Could not establish that any airframe stands at the airport separately from the North Atlantic Aviation Museum on the Trans-Canada Highway. Not recorded; see open questions. |
| **"Musée québécois de l'aéroplane"** | No such institution found under that exact name. The Quebec institutions that do hold airframes and are recorded here are the Musée de l'aviation de Montréal and the Musée de l'aérospatiale du Québec at Saint-Hubert. |

---

## 6. Currency flags a reader should know about

- **Musée de l'aviation de Montréal is closed.** Major renovation since February
  2026; a 23 July 2026 notice says the hoped-for September reopening slipped to
  late October 2026. Recorded as a site because it reopens, and the aircraft
  descriptions say so.
- **Shearwater Aviation Museum** was showing a "Temporarily Closed" notice in one
  third-party survey while it reinstalls exhibits after building maintenance.
  Its own collection page is live and was used as the source.
- **Canadian Air and Space Conservancy** is open Wednesday to Saturday by online
  booking only, at Edenvale Aerodrome, 5195 Highway 26 East, Stayner — recorded
  `appointment`. Its old `casmuseum.org` domain has lapsed and now redirects to a
  hotel-affiliate page; the live site is `avroarrow203.com`.
- **Jet Aircraft Museum**'s public site is a Next.js app served through an iframe
  from `jetaircraftmuseum.netlify.app`; the aircraft data is inside a JavaScript
  chunk, not in the HTML. Its own "Our Aircraft" and "Our Restorations" panels
  name only seven airframes; the rest of that file comes from the
  aviationmuseum.eu survey and is flagged row by row.

---

## 7. File and row counts

| File | Rows | With tail number |
|---|---|---|
| `ca_museums.csv` | 16 sites | — |
| `ottawa_casm_topup_aircraft.csv` | 138 | 118 (86%) |
| `canadian_warplane_heritage_aircraft.csv` | 45 | 36 (80%) |
| `national_air_force_museum_canada_aircraft.csv` | 42 | 38 (90%) |
| `canadian_bushplane_heritage_centre_aircraft.csv` | 28 | 22 |
| `atlantic_canada_aviation_museum_aircraft.csv` | 25 | 0 |
| `canadian_air_and_space_conservancy_aircraft.csv` | 23 | 11 |
| `base_borden_military_museum_aircraft.csv` | 18 | 17 |
| `jet_aircraft_museum_aircraft.csv` | 17 | 13 |
| `shearwater_aviation_museum_aircraft.csv` | 17 | 0 |
| `canadian_harvard_aircraft_association_aircraft.csv` | 10 | 10 |
| `greenwood_military_aviation_museum_aircraft.csv` | 10 | 9 |
| `musee_defense_aerienne_bagotville_aircraft.csv` | 10 | 10 |
| `musee_aviation_montreal_aircraft.csv` | 9 | 8 |
| `great_war_flying_museum_aircraft.csv` | 8 | 7 |
| `north_atlantic_aviation_museum_aircraft.csv` | 6 | 0 |
| `musee_aerospatiale_quebec_aircraft.csv` | 4 | 3 |
| `base31_lancaster_kb882_picton_aircraft.csv` | 1 | 1 |
| **Total** | **411** | **303 (74%)** |

All files validated against the brief's rules: enum values, `wing_type` only on
fixed-wing, no commas or verbs in `aliases`, dashless form present for every
dashed designation, no serial in `year_built`, no duplicate serial within a file.

### Blank fields left deliberately
- `latitude`/`longitude` blank on 13 of 16 sites — a correct postal code beats a
  guessed pin. Coordinates given only where the source published them (ACAM's
  own pages, the Jet Aircraft Museum's and the Montreal museum's Wikipedia
  infoboxes).
- `postal_code` blank for the Bushplane Centre, Great War Flying Museum, Base
  Borden, Base31, Montreal and Saint-Hubert — none of those sites published one
  where I could read it.
- 107 blank tail numbers, as set out in section 4.

---

## 8. Needs a human on site — ranked

1. **Shearwater Aviation Museum serials (17 airframes, zero recorded).** The
   museum publishes types only, and the two third-party surveys of it disagree
   badly — one of them lists a Supermarine Stranraer that is in London. Someone
   should walk the floor with the placards. Highest value per hour anywhere in
   this batch.
2. **Atlantic Canada Aviation Museum serials (25 airframes, zero recorded).**
   The museum writes good provenance prose but never a serial. Its CF-100, Sabre
   Mk 5, CF-104, CF-101, CT-133 and CP-121 are all types where a serial is
   readable off the airframe.
3. **The 9601 conflict.** Is the Sikorsky at Trenton and the one in Ottawa's
   Reserve Hangar really the same number? One of the two records is wrong.
4. **Base Borden and Bagotville serials.** Eighteen and ten airframes taken from
   an undated enthusiast survey. Borden's list already contains two airframes
   known to be elsewhere, so the rest deserves suspicion.
5. **Jet Aircraft Museum's actual current inventory.** Does it still hold the
   L-29, Jet Provost, MiG-15UTI and Hunter T.7? Does it have the MiG-29UB and
   Ohka replica Wikipedia claims? Its own site names only seven aircraft.
6. Lesser: Gander airport heritage displays; whether the Diefenbunker or the
   Canada Science and Technology Museum hold any airframe or missile; the
   Conservancy's Dash 8 (whole aircraft or section?); the CASM Reserve Hangar
   items with no published serial (SE5a, CC-130E Hercules, CH-136 Kiowa, CV-580).

---

## 9. Leads for other agents

**British Columbia agent**
- **Canadian Warplane Heritage's Canso A RCAF 11024 / C-FUAW** — CWHM's own page
  gives its status as "To be on display in British Columbia". Find where.
- **Canadian Air and Space Conservancy's Lancaster Mk X FM104** — transferred to
  the **British Columbia Aviation Museum**, Sidney.
- **New Brunswick Aviation Museum's de Havilland Vampire and its 1947 North
  American Navion C-GYIY** — both went to a British Columbia aviation museum
  when Miramichi closed in June 2026.

**New Brunswick agent**
- **New Brunswick Aviation Museum, Miramichi, closed 1 June 2026.** Do not record
  it as open. Its **CF-101B Voodoo 101053** has no recorded destination — worth
  chasing; it may now be a monument somewhere.
- Its artefacts went to the **New Brunswick Military History Museum, Oromocto**
  (CFB Gagetown) — worth checking whether that museum holds any airframe.
- **CFB Chatham** closed and dispersed its aircraft; ACAM's Golden-Hawks-painted
  Sabre Mk 5 came from the Chatham gate. Other Chatham airframes are probably
  now plinth aircraft in Miramichi.

**Bases and gate guardians agent**
- **Musée de la Défense aérienne de Bagotville is off-base** (6513 chemin des
  Aviateurs, La Baie, on Route 170 near the 3 Wing gate) and is recorded here as
  a museum with ten airframes. Do not double-record its CF-18 188720, CF-101
  101027, CF-100 100472, Sabre 19454, CF-116 116733, CT-114 114014, CT-133
  133333, MiG-23ML 4857, CH-118 118106 or H-21 9642. The 3 Wing **gate
  guardians** proper are a separate matter and are not in my files.
- **14 Wing Greenwood**: the museum's Air Park sits just outside the main gate
  and I have its ten aircraft. Anything inside the wire is yours.
- **8 Wing Trenton**: the RCAF Memorial Airpark is part of the National Air Force
  Museum of Canada and its ~30 aircraft are in my Trenton file. Trenton's gate
  guardian, if separate, is yours.
- **CFB Borden**: the Base Borden Military Museum's 18 aircraft are in my file.
  Borden has additional airframes used for technical training that I did not
  touch.
- **12 Wing Shearwater**: museum aircraft are mine; the CH-124 Sea King gate
  guardian and the base memorial airframes are yours.

**Monuments agent**
- The **CF-100 Mk 5 100493** and **CF-100 Mk 4A 18194** at Base Borden, the Avro
  504K there, and Borden's five CT-133s are museum holdings, not plinths — but
  Borden also has plinthed aircraft around the base that I did not survey.
- **Base31, Picton** (former RCAF Station Picton) is a large redeveloped wartime
  air station with an exhibition hall; besides Lancaster KB882 it may have other
  aviation heritage on site.
- **CFB Chatham NB** and **CFB Summerside PEI** closures scattered airframes
  across the Maritimes; ACAM's Sabre is one traceable example.

**Whoever writes the import**
- Correct the existing Ottawa Lancaster row from **KB726 to KB944** before
  importing `canadian_warplane_heritage_aircraft.csv`, which carries FM213 with
  KB726 as a marking alias.
- The CASM top-up deliberately omits the complete Lancaster and the Mosquito,
  which are the two rows already in the database.


---

# Research pass: major museums, Manitoba westward

# CA_MUSEUMS_WEST_NOTES.md

Research notes for **western Canada and the territories** — British Columbia,
Alberta, Saskatchewan, Manitoba, Yukon, Northwest Territories, Nunavut.
Output directory: `/home/claude/ca/museums_west/`.
Compiled September 2026.

---

## 1. The most important finding: rwrwalker.ca is gone

**`rwrwalker.ca` — the brief's designated spine — no longer exists as an
aviation resource.** The domain has been taken over and now serves online
casino affiliate content ("I Analyzed Best Canadian Online Casino (2026 Top
10)"). Every deep link, e.g. `rwrwalker.ca/CF100_1_detailed.html`, returns the
new site's 404 page. The Wayback Machine holds the old serial-range pages
(`RCAF_xxxxx_xxxxx_detailed.html`, `CF_104700_104771_detailed.html`, etc.) but
the CDX index was rate-limiting hard from this environment and could not be
paged reliably, so I did not use it systematically. **Whoever runs the next
Canadian pass should budget time to mirror rwrwalker from the Wayback Machine
before it becomes harder to reach.**

### The substitute spine I used instead

**`silverhawkauthor.com` — Harold A. Skaarup's *Canadian Warplanes* (2024 /
"Canadian Warplanes II") online edition.** It is organised the way this project
needs: one page per province, plus a dedicated page per major museum, listing
airframes with RCAF/CAF serials, construction numbers, civil registrations,
false markings and provenance. It is more current than Wikipedia (the BC
Aviation Museum page already records a CT-114 Tutor "just delivered from CFB
Trenton, March 2026") and vastly more complete. Pages used:

- `canadian-warplanes-1-british-columbia` (+ BCAM Sidney, CMF Langley, CFB Comox)
- `canadian-warplanes-2-alberta` (+ AAM Edmonton, Hangar Flight Museum, Nanton, Reynolds, CFB Cold Lake)
- `canadian-warplanes-3-saskatchewan` (+ WDM Moose Jaw, CFB Moose Jaw)
- `canadian-warplanes-4-manitoba` (+ CATP Brandon, RAM Winnipeg, CFB Winnipeg)
- `canadian-warplanes-11-northwest-territories-12-nunavut-13-yukon-territory`

Its weaknesses: it mixes archival photo captions with live survivor entries, so
a serial in a "(Library and Archives Canada Photo)" line is usually a historical
aircraft, not a preserved one; it occasionally lists the same airframe at two
sites (see §4); and it is a personal compilation with no per-entry sighting
dates.

### Source weighting actually applied

1. **Museum's own structured feed.** Only one existed: the Royal Aviation Museum
   of Western Canada publishes a WordPress custom post type at
   `royalaviationmuseum.com/wp-json/wp/v2/aircraft` (28 records, full prose
   provenance). The Alberta Aviation Museum has an `aircraft` post type in its
   sitemap but the REST route is closed; its 26 aircraft pages were scraped
   individually and turned out to carry almost no serials.
2. **Museum's own collection pages** — used as the row set wherever one exists
   (Reynolds, CMF Langley, BCAM, Saskatchewan Aviation Museum, CATP Brandon,
   Hangar Flight Museum, Bomber Command Museum). These win on "what is here now".
3. **`aerialvisuals.ca`** — works, and its **Location Dossier** pages are the
   single best structured artefact I found: per-site airframe lists with serials,
   c/ns *and decimal display coordinates*, split by sub-site (outdoor pylon /
   main hall / storage). Query path: `Airframes.php?Seeds=<serial or reg>` →
   `AirframeDossier.php?Serial=<internal id>` → `LocationDossier.php?Serial=<id>`.
   It rate-limits at roughly one request per 5-10 s (HTTP 429), so it needs a
   cached, throttled fetcher. Its *location* data is stale in places (it still
   places Lancaster FM104 in Toronto and Electra CF-TCC with Air Canada).
4. **Wikipedia** — leads only; its museum tables mix construction numbers and
   serials in one column, which produced several of the conflicts in §4.

`pinetreeline.org` was not needed (no radar-station or Bomarc sites fell in the
museum scope of this assignment). `airhistory.net` was avoided per the brief.

---

## 2. Files written

Museums file: **`ca_museums.csv`** — 16 sites.

| File | Rows | With serial | on_display | in_storage | under_restoration |
|---|---:|---:|---:|---:|---:|
| `alberta_aviation_museum_aircraft.csv` | 40 | 32 (80%) | 35 | 4 | 1 |
| `bc_aviation_museum_aircraft.csv` | 40 | 31 (77%) | 36 | 2 | 2 |
| `bomber_command_museum_canada_aircraft.csv` | 28 | 21 (75%) | 19 | 4 | 5 |
| `canadian_museum_of_flight_aircraft.csv` | 43 | 35 (81%) | 29 | 6 | 8 |
| `commonwealth_air_training_plan_museum_aircraft.csv` | 26 | 11 (42%) | 14 | 5 | 7 |
| `comox_air_force_museum_aircraft.csv` | 14 | 13 (92%) | 13 | 1 | 0 |
| `hangar_flight_museum_aircraft.csv` | 31 | 25 (80%) | 27 | 2 | 2 |
| `kf_centre_for_excellence_aircraft.csv` | 9 | 3 (33%) | 8 | 0 | 1 |
| `prince_of_wales_northern_heritage_centre_aircraft.csv` | 1 | 0 (0%) | 1 | 0 | 0 |
| `rcmp_heritage_centre_regina_aircraft.csv` | 2 | 2 (100%) | 2 | 0 | 0 |
| `reynolds_alberta_museum_aircraft.csv` | 146 | 111 (76%) | 140 | 3 | 3 |
| `royal_aviation_museum_western_canada_aircraft.csv` | 39 | 35 (89%) | 29 | 9 | 1 |
| `saskatchewan_aviation_museum_aircraft.csv` | 25 | 20 (80%) | 21 | 0 | 4 |
| `the_military_museums_calgary_aircraft.csv` | 9 | 8 (88%) | 6 | 3 | 0 |
| `wdm_moose_jaw_aircraft.csv` | 29 | 23 (79%) | 28 | 0 | 1 |
| `yukon_transportation_museum_aircraft.csv` | 4 | 4 (100%) | 4 | 0 | 0 |
| **Total** | **486** | **374 (76%)** | | | |

Rebuild scripts (`build_*.py`, `_lib.py`) are kept alongside the CSVs so every
row can be traced and re-generated.

**Serial coverage: 374 of 486 rows (76%).** The uncovered 24% is dominated by
replicas and homebuilts that genuinely have no serial (Reynolds' ultralight and
glider holdings, the CATP Museum's airworthy fleet, scale replicas), plus the
KF Centre, whose own site publishes years but not registrations.

---

## 3. The Royal Aviation Museum of Western Canada: display vs storage

The brief asked specifically what is on display in the 2022 building versus what
went to storage. Answer, as far as the sources allow:

- The new 86,000 sq ft building at **2088 Wellington Avenue** opened **21 May
  2022**. The Canadian Aviation Historical Society's account of the opening
  states **"Twenty-four aircraft are displayed in the museum, of which six are
  suspended from the ceiling in flight."**
- The museum's own site publishes **28 aircraft records**, and these are the
  ones I have marked `on_display`. They map closely onto the 24-plus-outdoor
  count: the Bristol Freighter CF-WAE is explicitly described by the museum as
  "on display outdoors in Aviation Plaza".
- **The rest of the collection — the museum says "over 90 aircraft" — is off
  site**, split between a storage building at **St. Andrews Airport north of
  Winnipeg** and a **Restoration Facility in Winnipeg**. Aerial Visuals'
  location dossier separates a group it labels "thought to be stored here":
  Expeditor 3N 1477, Vampire 3 17020, Tiger Moth 1122 and the CASA 352L.
- Airframes I have recorded as `in_storage` at RAM because they appear in Aerial
  Visuals or Wikipedia but **not** on the museum's public collection pages:
  Anson I FP805, CP-107 Argus 10715, Bolingbroke IVT 10184, Norseman IVW 2456,
  Cornell II FV705, Fairchild F-11 Husky c/n 2, Expeditor 3N 1477, Vampire 3
  17020, and the second Electra (ex-RCAF 1528 / CF-HED).
- Three airframes sit outdoors at the new building on Aerial Visuals' mapped
  coordinates and are marked `on_display`: **Sabre 6 c/n 1815** (49.895603,
  -97.221533), **Silver Star 3 21075** (49.895542, -97.220681) and **CF-100 Mk 5
  18764** (49.895564, -97.220497).
- Two recent gallery arrivals are worth flagging as evidence the museum's list is
  live: **Junkers F 13 CF-ALX** returned from a two-decade restoration at the
  Deutsches Technikmuseum in Berlin in **September 2024** (traded for the
  museum's Junkers W 34 CF-AQV), and the composite **Fox Moth CF-BNP** was
  installed in the gallery in **June 2025**.
- **The Buffalo has left.** Aerial Visuals records CC-115 Buffalo 115462 under
  "airframes once displayed here but have moved on". Destination unknown.

---

## 4. Corrections and conflicts resolved, with evidence

**Mosquito PR.35 RS700 / CF-HMS — Calgary or Nanton?** silverhawkauthor lists it
on both the Hangar Flight Museum page and the Bomber Command Museum page. It is
**at Nanton**: the museum's own Nanton page states the Mosquito arrived in the
North Hangar on 11 August 2012 for restoration by the Calgary Mosquito Society
on behalf of the City of Calgary, and Legion Magazine's feature is titled
"Resurrecting a WW II legend **in Nanton, Alta.**". Removed from the Hangar
Flight Museum file. The Hurricane XII 5389 stays at Calgary (Wikipedia records
its restoration completed there in 2019; only its Merlin was run up at Nanton).

**NA-64 Yale 3390 — Nanton or Brandon?** Listed at both by silverhawkauthor.
The Bomber Command Museum's own aircraft page states plainly that it has **one**
Yale, **3404 / ex-USAAC 64-2157**, currently in storage. 3390 therefore sits in
the **Commonwealth Air Training Plan Museum** file. I also corrected 3404's
USAAC serial from silverhawkauthor's 64-2158 to the museum's 64-2157, and moved
it from `under_restoration` to `in_storage` on the museum's own wording.

**CF-116 Freedom Fighter 116707 — Nanton or Calgary?** Listed at both.
aviationmuseum.eu's inventory of the Bomber Command Museum contains no CF-5 of
any kind; The Military Museums in Calgary is separately documented with 116707
"mounted on twin pylons". Placed at **The Military Museums** and removed from
Nanton.

**Barkley-Grow T8P-1 CF-BLV (c/n 3, "Yukon Queen").** silverhawkauthor lists it
under the Hangar Flight Museum but adds "on loan to the Alberta Aviation
Museum". Recorded **at Edmonton**, where a visitor will find it, per the
methodology rule. Calgary keeps its own Barkley-Grow, CF-BQM (c/n 8).

**Vickers Viking IV replica G-CAEB.** Listed by silverhawkauthor under both
Nanton and the Alberta Aviation Museum, with the Nanton entry noting "on
permanent loan to the AAM, Edmonton". Recorded at **Edmonton** only.

**CF-104 104731.** silverhawkauthor's Comox page says it was on display there
"until it was moved to the BC Aviation Museum in July 2023"; the BCAM page
confirms the transfer. Recorded at **BCAM**, painted as 12763. The airframe that
genuinely carries 12763 (= 104763) is at **Reynolds-Alberta**.

**Two Lockheed Electras at RAM Winnipeg, not one.** Wikipedia and Aerial Visuals
give "Electra 1528 / c/n 1064 / CF-HED"; the museum's own page describes CF-TCC,
"one of the first six aircraft purchased by the newly-formed Trans-Canada
Airlines in 1937". Aerial Visuals' CF-TCC dossier gives c/n **1116**, ex-N3749,
restored to flight by Air Canada in 1986 — a different airframe from c/n 1064.
Both are recorded; CF-TCC on display (it entered the collection in 2022),
CF-HED in storage.

**Sabre Mk 6 c/n 1815 at RAM.** The museum says it was the last Sabre ever
built (9 October 1958), delivered to the Luftwaffe as JB+372, last flown by the
**Pakistan Air Force** and donated by them in 1996; it wears RCAF 441 Squadron
markings. Aerial Visuals records the identity as "1815 PakAF". Both facts are in
the description; `tail_number` is the c/n 1815, which is all any source offers.

**RAM's CF-104 "12703".** The museum presents it as CF-104 12703 on loan from
Ren Pajot's former Canadian Starfighter Museum; Aerial Visuals records the
underlying airframe as ex-Royal Danish Air Force **R-704, c/n 683A-1003**.
Unresolved — recorded under 12703 with the conflict stated in the description.

**AAM Edmonton's CF-104.** The museum's own text is unambiguous and settles the
Wikipedia/AV disagreement: "a Lockheed TF-104G bought from a museum in the
Netherlands [ex-KLu D-5805] and is finished as CF-104D #104651 of 417 Squadron."

**AAM's Ju 52 / CASA 352L.** RAM's "Ju 52/1m, CF-ARM (RETROFIT)" is a Spanish
CASA 352L (T.2B-148, ex-N99234) being converted to represent Canadian Airways'
single-engined Ju 52 CF-ARM; the museum itself calls it "the replica of CF-ARM".
Recorded `under_restoration` as a CASA 352 with the Ju 52 identity in aliases.

**CT-114 Tutor 114115.** silverhawkauthor records it *both* as the Comox Air
Force Museum's Snowbird 3 and as Snowbird 5 on a pylon at the Comox Valley
Information Centre. One is a duplicate; flagged in the row description. Left at
the museum.

**Fox Moth at the Prince of Wales Northern Heritage Centre.** silverhawkauthor
gives CF-BNI; Aerial Visuals places CF-BNI at **Sault Ste Marie, Ontario**. The
PWNHC's own exhibit text describes a composite rebuilt from **three NWT crash
sites** starting in 1977 and gives no registration. `tail_number` left blank
rather than assert a marking that may belong to another airframe.

**Serials left deliberately unresolved and stated in the description:** the
Alberta Aviation Museum's Anson (11567 per Wikipedia vs 886 per
silverhawkauthor), its Mosquito (VP189 vs VA114), its Tiger Moth (241 / 2114 /
FE192-C-FCOH), its second Voodoo (101060 / 100060 / AV's unreadable "837B"), its
Boeing 737 registration (C-GIPW vs C-GPIW); BCAM's Anson (Mk I 6518/K8786 vs Mk
II FP846); the WDM Moose Jaw Silver Star (133275 vs 21401); the Saskatchewan
Aviation Museum's Cornell registration (C-FZRO per the museum vs C-GTOI per
silverhawkauthor) and its two Chipmunk serials (rendered by silverhawkauthor as
six digits, 182220 and 198236, which are not valid RCAF Chipmunk serials —
recorded as 18220 and 18236).

---

## 5. Judgment calls

**Reynolds-Alberta Museum display status — the biggest soft spot in this file.**
The museum's own aviation page carries the warning "Although the aircraft listed
here are in the Reynolds-Alberta Museum collection, **not all are on public
display**", and its collection management references warehouse locations
("NE Warehouse 1", "NE Warehouse 2", "Jet Line 1"). It runs "Summer Warehouse
Tours" for exactly this reason. No public source maps aircraft to locations. I
have therefore set `on_display` as the default and appended the museum's own
caveat verbatim to **every** Reynolds description, reserving `in_storage` /
`under_restoration` for the few airframes silverhawkauthor explicitly describes
that way (Lysander 2445 in storage; Bolingbrokes 9990 and 10120 unrestored;
Bolingbroke 9904, Waco YKS-7 and the Swordfish under restoration). **This is the
number one question for a human on site.**

**Reynolds row set.** I used the museum's own ~135-entry list as the spine and
added the airframes silverhawkauthor documents with a distinct serial or
registration that the museum's summary list does not itemise (a second CF-104, a
second CT-133, a second Musketeer, a second Lodestar, a second Expeditor, the
CC-129 Dakota, the Anson Mk II, the Piasecki H-44). Each of those rows says so
in its description.

**Canada's Aviation Hall of Fame** is housed *inside* the Reynolds-Alberta
Museum (it moved there when the museum opened in 1992) and holds **no separate
airframes**. It is therefore not a site record; the Reynolds record covers it.

**Ground trainers.** Link Trainers (Hangar Flight Museum, Nanton, AAM, CMF
Langley, BCAM, CATP Brandon) and the two Jacobs Jaycopter helicopter simulators
at Reynolds are recorded, each with "a ground trainer rather than an airframe"
in the description, so a later filter can drop them cleanly.

**Mock-ups and replicas** are recorded where they are the object a visitor sees,
always labelled in the description: Nanton's full-size Bf 109 mock-up (built by
Lech Lebiedowski around parts from a crash site), its 5/8-scale Spitfire and
2/3-scale Lysander; Reynolds' Arrow replica (the mock-up built for the 1997 CBC
miniseries *The Arrow*), Silver Dart, Curtiss Pusher and Sperry Messenger; BCAM's
Gibson Twin Plane, Hoffar H-1, Chanute glider and da Vinci ornithopter.

**Parts-only holdings excluded** (documented here rather than recorded as
airframes): the Hangar Flight Museum's Airspeed Oxford parts, Auster AOP.6
parts and Fairey Swordfish Mk V parts; CMF Langley's Fairey Battle parts are
recorded but flagged as parts because the museum's own restoration pages treat
them as a project. Engine collections (CMF Langley's ~30 engines, BCAM's ~15,
the Hangar Flight Museum's 58) are out of scope.

**Cockpit / nose sections recorded as such**: the RCMP Heritage Centre's
DHC-3 Otter CF-MPW (cockpit only, indoors), CMF Langley's Bolingbroke IVT 9896
(forward fuselage on display, rest in storage), Reynolds' Canadair North Star
(nose section), WDM Moose Jaw's Airspeed Oxford cockpit section, and RAM's
CP-107 Argus 10715 (reported as a forward fuselage — needs confirming).

**Airworthy aircraft** are recorded at their home museum with the fact stated in
`description`, never in `aliases`: the Comox Spitfire is the exception — see
exclusions.

**Access type.** All 16 sites are `public`. The Comox Air Force Museum sits on
19 Wing but is open to the public, and the **Heritage Air Park is 600 m from the
museum on Military Row / Little River Road, outside the wire, with its own
parking** — genuinely public.

---

## 6. Excluded, and why — named

- **Comox's Supermarine Spitfire HF Mk IXe TE294.** Restored *at* Vintage Wings
  of Canada, first flown 7 June 2017 and **airworthy with Vintage Wings**, not
  at Comox. Painted as MK304 / Y2-K for Flt Lt Arnold Roseland of 442 Sqn. Not
  recorded here; it belongs to whoever covers Gatineau, Quebec.
- **CF-101B Voodoo 101063.** silverhawkauthor says it "is being transferred to
  the Canadian Museum of Flight, Langley, from the Shearwater Aviation Museum".
  No confirmation of arrival was found. Excluded from the Langley file; see §8.
- **Aerospace & Technology Museum of British Columbia, Fort St John.** Its
  Sabre Mk 6 23692 / N3844E is, per silverhawkauthor, "currently in storage in
  Seattle, Washington" with a *plan* to move it to Fort St John. Nothing
  visitable established. Excluded; see §8. (The brief also asked about the
  **Fort St John North Peace Museum** — no aircraft found in any source.)
- **Quesnel Heritage Aircraft Museum, BC.** silverhawkauthor documents a real
  collection (two Luscombe Silvaires, two Republic Seabees incl. C-FDOQ, **three
  Scottish Aviation Pioneers** — c/n 508 C-GSTX, 516 CF-STX, 582 C-GNIS — and
  two Stinson Reliants). I could not establish that it is open to the public or
  find a website, so I did not create a site record I cannot stand behind.
  **This is the highest-value unrecorded site in my area.**
- **The Whereatt collection, Assiniboia SK** (estate of Harry Edwin Whereatt):
  Hurricane XIIa 5447 (since sold to Vintage Wings, now C-GGAJ, Gatineau),
  Hurricane XIIa 5455, Harvard 4 20334 / CF-VIR, Lysander IIIA 2365 / CF-VZZ,
  plus a Tiger Moth, a Moth, two Anson IIs, two Anson Vs, two Bolingbrokes, two
  Cranes, two Cornells and two Fleet Forts in parts. Private farm collection,
  no public access. Excluded.
- **Zalesky family, White Rock BC**: Bf 109 c/n 3535, Hurricane parts, Lysander
  IIIA hulks 2341 and 2344. Private, excluded.
- Other private owners excluded as not visitable: Milton Hughes (Nipawin SK,
  Auster AOP.6 C-FLOE), Frank Thompson (Readlyn SK, Bolingbroke 10122 and
  Harvard 20402), Donald McTaggart (Kindersley SK), Mac-Ann Farms (Tisdale SK),
  Bob Jens' Spitfire FR XIVe TZ138 / C-GVZB stored at Vancouver International.
- **BCIT Aviation, Vancouver** and the **Saskatchewan Indian Institute of
  Technologies AME school, Saskatoon**: instructional airframes at closed
  training campuses. Excluded. (BCIT's fleet includes WestJet 737-200 C-GWJT,
  a CC-117 Falcon 20C and several Aerostars.)
- **Aircraft in service** excluded throughout: Buffalo Airways' Yellowknife
  fleet (C-54G C-FIQM, P-3A N922AU, DC-3 C-FDTD, Norseman CF-SAN), Air Nunavut's
  King Air and Falcon 10s, Environment Canada's Dash 7 C-GCFR, the Province of
  Saskatchewan's La Ronge Tracker tanker fleet (1538, 1552, 1554, 1593, 1599),
  Conair's Abbotsford Firecats (1520, 1525, 1535), Royal Canadian Air Cadet
  Cessna 182s at Comox.
- **Nunavut: no preserved airframe found anywhere in the territory.** Every
  Nunavut entry in every source consulted is either an in-service commercial
  aircraft or an uncontrolled crash site. Recorded here as a negative finding.
- **"Prairie Aviation Museum"** — the only museum of that name is in Bloomington,
  **Illinois**. No Canadian institution by that name was found; the brief's query
  is answered in the negative.
- **Fraser Blues** — a civilian Navion formation display team based in the Lower
  Mainland, flying privately-owned airworthy aircraft. Not a preservation site;
  no static collection. Excluded.
- **Boundary Bay** — no airshow heritage collection found; the only preserved
  airframe silverhawkauthor lists there is Harvard 4 20354 / C-FSPC, privately
  owned. Excluded.
- **Prince George, Castlegar, Estevan** — nothing found in any source. See §8.
- **Western Development Museum's other three branches** (North Battleford,
  Saskatoon, Yorkton) hold **no aircraft**; Moose Jaw is the transportation
  branch and holds the entire WDM aviation collection.

---

## 7. The Martin Mars — answered

**The Hawaii Mars is visitable, at the British Columbia Aviation Museum in
Sidney, and it is recorded in `bc_aviation_museum_aircraft.csv`.**

- Martin **JRM-3 Mars**, US Navy bureau number **76823**, registered
  **C-FLYL** (the museum's own history page renders it CF-LYL), delivered to the
  US Navy at Alameda between February and June 1946.
- Flown as a water bomber by Forest Industries Flying Tankers and then Coulson
  Aviation; **last fire season 2015**, then stored at Sproat Lake near Port
  Alberni.
- The BC government announced a $250,000 grant toward the "Hawaii Mars rescue"
  at a press conference on **28 March 2024**; the aircraft made its **final
  flight from Sproat Lake to Patricia Bay on 11 August 2024** and is now the
  museum's centrepiece. The museum runs **Hawaii Mars flight deck tours** and
  has a whole site section for it.
- **It is no longer at Port Alberni.** The BCAM also holds a time-expired Wright
  R-3350 from a Martin Mars donated by Forest Industries Flying Tankers, and a
  Martin Mars model in FIFT colours — do not mistake either for the aircraft.
- The **Philippine Mars** (C-FLYK) is *not* in this area's records; it was
  destined for the Pima Air & Space Museum in Arizona. Worth a check by whoever
  maintains Pima.

## 7b. The Yukon DC-3 weathervane — recorded

Douglas **DC-3 CF-CPY**, c/n 4665, ex-Canadian Pacific Air Lines, is mounted on
a rotating pylon outside the **Yukon Transportation Museum** at the entrance to
Whitehorse airport, where it turns into the wind — locally billed as the world's
largest weathervane and the single best-known aviation landmark in the
territory. Aerial Visuals maps the museum's airframes at
**60.71233, -135.07900** (the site coordinates are in `ca_museums.csv`).
The museum also holds Fairchild 71C CF-BXF, the "Queen of the Yukon" Ryan B-1
Brougham replica G-CAHR, and Smith DSA-1 Miniplane CF-RKN.

---

## 8. Ranked "needs a human on site"

1. **Reynolds-Alberta Museum, Wetaskiwin — which of the 135+ aircraft are
   actually in the public hall?** This is 146 of my 486 rows and every one of
   them is currently a soft `on_display`. Curator Justin Cuffe, Transportation
   Collections, is named on the museum's aviation page (780-312-2079).
2. **Quesnel Heritage Aircraft Museum, BC — is it open, and what is its
   address?** Three Scottish Aviation Pioneers in one collection would be
   nationally significant. Nothing was recorded for it.
3. **CF-101B Voodoo 101063 — did it arrive at Langley?** If it did, the
   Canadian Museum of Flight gains a Voodoo and the Shearwater Aviation Museum
   (another agent's area) loses one.
4. **Comox: has the Vampire Pavilion opened?** DH.100 Vampire F.3 17031 has
   been hangared out of public sight since 2000 because of its plywood
   structure; the pavilion fund stood at 87% of $1 million with a target of
   summer 2025. Currently recorded `in_storage`. Also confirm whether the
   Heritage Air Park now holds a **CP-140 Aurora** (the museum's own page says
   "From the Dakota to the Aurora"; no serial found) and get the **CH-124 Sea
   King** serial. The museum's own PDF, *Guide to the Aircraft of the CAFM
   Heritage Air Park*, is linked from its Heritage Park page but 404s.
5. **CATP Museum Brandon — how many Bolingbrokes are on site and which is
   which?** The museum says two complete airframes exist, one of them at the
   Comfort Inn on Highway 1; silverhawkauthor names four serials (9059, 9883,
   9944, 10107) plus a fuselage the museum calls "Bolly 9869". I placed 9059
   on display and 9883/10107 in storage on inference alone.

Also worth a look: the true identity of RAM's CF-104 (12703 or ex-Danish R-704);
whether RAM's CP-107 Argus 10715 is a complete airframe or a nose section;
and the KF Centre for Excellence registrations, which its website omits.

---

## 9. Leads for other agents

**Gate guardians, plinth aircraft and roadside monuments in my provinces**
(deliberately *not* recorded here, per the brief):

*Alberta* — CF-104 104702 on a pylon in downtown **Cold Lake**; the CFB Cold
Lake Air Force Museum (63117 69 Avenue, Cold Lake) has its own silverhawkauthor
page and is a full museum, not just an air park; a Harvard Mk 4 on a pylon at
**Claresholm** commemorating 15 SFTS; Noorduyn Norseman V c/n N29-26 / CF-MAM on
skis in the lobby of the **Suncor Energy Centre, Calgary**; the **408 Squadron
Museum at CFB Edmonton**; the **A.V. Roe Canada Heritage Museum, Calgary**;
Harvard Historical Aviation Society and Air Spray at **Red Deer**; P-51D
44-74429 / RCAF 9598 in storage with the **Lynn Garrison estate, Calgary**.

*British Columbia* — CF-101B 101035 (c/n 541) at **Abbotsford Airport**; CF-116
116740 on a pylon outside the **Kamloops** airport terminal; CT-114 114187
between Millennium Park and the College of the Rockies at **Creston**; CT-114
114115 on a pylon at the **Comox Valley Information Centre** (see §4 — probable
duplicate); CT-133 133648 as a wind vane at **Princeton Airport** and CT-133
133423 at Princeton; Sabre Mk 6 23060 on a pylon at ANAF Veterans Club No. 302,
9831 4th Street, **Sidney**; a Spitfire replica marked 788 / RN-P on pylons at
ANAF Vets Unit No. 5, 2500 46th Ave, **Vernon**; Sopwith Triplane replica at
Collishaw Air Terminal, **Nanaimo Airport**; **CFB Esquimalt Naval and Military
Museum**; the **Hawker Typhoon JP843** rebuild at VMAerospace, Black Creek —
a Typhoon Legacy Co. project aiming for flight, currently not visitable.

*Saskatchewan* — CT-133 133630 / 21630 in **Red Knight** colours at Saskatoon;
CT-133 133072 in parts at Assiniboia; the separate **CFB Moose Jaw** page on
silverhawkauthor (2 CFFTS, Snowbirds home base).

*Manitoba* — **Bolingbroke Mk IV 9944 standing at the Comfort Inn, Highway 1,
Brandon** (an unusually good "aircraft at a motel" record); **Westland Lysander
IIIA 2375** with the Agnew family at the Brandon Flying Club; the **Air Force
Heritage Museum and Air Park, CFB Winnipeg**, which has its own silverhawkauthor
page and is a substantial air park.

*Northwest Territories* — **Bristol 170 Freighter/Wayfarer Mk 31 CF-TFX**
(ex-G-AMRV) mounted on a pylon at **Yellowknife** in Wardair's blue and red;
Hay River holds a large group of Canso As and Curtiss C-46 Commandos whose
status (in service, stored, derelict) needs sorting out — C-FUAW, C-FPQM,
C-FNJE, C-FOFI, C-GFFC, C-FAVO, C-GIBX.

*Cross-border / other regions* — Hurricane XIIa 5447 (C-GGAJ) and Spitfire
TE294, both ex-western Canada, are now with **Vintage Wings of Canada,
Gatineau, Quebec**; Sikorsky S-58 / H-34A RCAF 9630 is listed by
silverhawkauthor at both **Port Clements BC** and **Reynolds-Alberta** — one of
those is wrong.

**A method note for the rest of Canada:** Aerial Visuals' `LocationDossier.php`
pages, reached through any one known serial at a site, are the fastest way to
get a per-site airframe list *with display coordinates* — including the split
between outdoor plinths, main hall and storage. Throttle to one request every
6-10 seconds and cache; it returns HTTP 429 aggressively.


---

# Research pass: Canadian Armed Forces base displays

# CA_BASES — Canadian Armed Forces aviation displays nationwide

Output directory: `/home/claude/ca/bases/`
Files: `ca_museums.csv` (29 sites) + 29 `<slug>_aircraft.csv` files (186 aircraft rows,
179 with a serial in `tail_number` = 96% serial coverage).
Research date: 10 September 2026.

---

## 1. Sources and the weight given to each

| Source | Weight | What it gave, and how it failed |
|---|---|---|
| **silverhawkauthor.com** ("Canadian Warplanes", Harold A. Skaarup) | **Primary spine.** | Per-location *and* per-type survivor pages covering every RCAF wing. Has dedicated pages for CFB Borden, CFB Bagotville, CFB Moose Jaw, CFB Kingston/RMC, CFB Comox, CFB Shearwater, CFB Greenwood, CFB Winnipeg, CFB Cold Lake. It is the only source that names *technical-training* airframes (the 18 CFSATE Tutors, the Kiowa and Iroquois hulks). **Its weakness is that photo captions and display entries are interleaved**, so an aircraft merely *photographed* at a base reads like an aircraft *displayed* at that base. Several conflicts below come from this. |
| **aerialvisuals.ca Location Dossiers** | Strong for coordinates and for "is it still there". | `LocationDossier.php?Serial=<n>` returns per-site coordinates to six decimals plus an explicit "accessible to the public / not likely accessible" flag. Gave exact pins for 15 Wing Moose Jaw, CFB Suffield, 5 CDSB Gagetown, Shearwater. **The site rate-limits hard (HTTP 429 after a few hundred requests) and then blocks for an extended period**, so only a partial crawl was possible; most of my sites have no aerialvisuals pin. |
| **Wikipedia** (`Air Force Heritage Museum and Air Park`, `Cold Lake Air Force Museum`, `CFB North Bay`) | Lead only. | Useful for the Winnipeg and Cold Lake inventories. `CFB North Bay` is silent on the two pylon aircraft that Canadian Warplanes documents, which is an omission rather than a contradiction. |
| **Museum / park own pages** (museebagotville.ca, coldlakemuseums.org, airforceparkpei.ca, aerospacedefence.ca) | Wins on "what is here now". | coldlakemuseums.org settled that the Cold Lake Air Force Museum is now *in the city*, not on 4 Wing, with four aircraft at ground level. airforceparkpei.ca gave the Slemon Park holdings. aerospacedefence.ca (22 Wing) is a bare landing page with a phone number and no inventory. |
| **Veterans Affairs Canada national inventory of memorials** | Decisive for one exclusion. | Recorded that the North Bay Bomarc was removed in 2009. |
| **exploringwinnipegparks.ca** | Currency check. | Independent, recent listing confirming the Winnipeg air park line-up and that it sits on Air Force Way outside the wire. |
| **aviationmuseum.eu** | Currency check. | Gave the Slemon Park serials including the Buffalo the park's own page omits. |

`rwrwalker.ca` was named in the brief as the spine. In practice
silverhawkauthor.com carried the same per-serial disposition detail *organised by
location*, which is what a site-based database needs, and it was reachable
throughout. Where a serial below is called doubtful, rwrwalker is the first place
a human should check it.

---

## 2. Scope decision — base museums are recorded here

The brief assigns me "wing and base gate guardians, heritage air parks, memorial
airframes and technical-training airframes", and names 3 Wing Bagotville's Musée
de la Défense aérienne, 4 Wing Cold Lake's Air Force Museum air park, 16 Wing
Borden and CFSATE explicitly. On Canadian bases the gate guardian, the air park
and the base museum are one institution — the Bagotville Voodoo on its pylon *is*
a museum exhibit, and splitting them would put two records at one address.

**So the on-base RCAF heritage collections are recorded here, once each**, under
their proper names:

- Musée de la Défense aérienne de Bagotville (3 Wing)
- Cold Lake Air Force Museum + 4 Wing Cold Lake Air Park (recorded as two sites — see §4)
- Air Force Heritage Museum and Air Park (17 Wing)
- Comox Air Force Museum and Airpark (19 Wing)
- Shearwater Aviation Museum (12 Wing)
- Greenwood Military Aviation Museum (14 Wing)
- Base Borden Military Museum + CFSATE (16 Wing)
- 15 Wing Military Aviation Museum (Moose Jaw)
- Canadian Forces Museum of Aerospace Defence (22 Wing North Bay)
- Labrador Military Museum (5 Wing Goose Bay)
- New Brunswick Military History Museum (5 CDSB Gagetown)
- Garrison Petawawa Military Museums, Royal Canadian Artillery Museum (Shilo),
  Musée du Corps royal canadien des munitions (Longue-Pointe)

**The museums agent must not also enter these.** The one on-base museum I have
deliberately left alone is the **National Air Force Museum of Canada / RCAF
Memorial Air Park at 8 Wing Trenton**, which the brief assigns to the museums
agent. I have recorded only the two 8 Wing airframes that are *outside* that
museum: the CF-116 gate guardian on the Highway 401 pylon at Glen Miller Drive,
and CT-133 133190 at the North Gate.

---

## 3. Access-type judgments

`public` was given only where the airframe stands outside the wire and can be
seen from a public road or public ground:

| Site | access_type | Why |
|---|---|---|
| Air Force Heritage Museum and Air Park, 17 Wing Winnipeg | `public` | The air park runs along Air Force Way north of Silver Avenue, outside the 17 Wing perimeter; the CF-5 is on the corner of Ness Avenue and Conway Street. Confirmed independently by exploringwinnipegparks.ca. The B-25, Dakota, Expeditor and Bolingbroke are held *inside* the base — this is said in each row's `description`. |
| Comox Air Force Museum and Airpark, 19 Wing | `public` | Museum and airpark are on the public side of 19 Wing off Ryan Road. |
| Shearwater Aviation Museum, 12 Wing | `public` | Aerial Visuals states plainly "This museum is accessible to the public." |
| Greenwood Military Aviation Museum, 14 Wing | `public` | Public-facing museum with its own entrance. |
| Cold Lake Air Force Museum | `public` | Now in the City of Cold Lake at the decommissioned 42 Radar Site behind the Tri-City Mall, not on 4 Wing. |
| 8 Wing Trenton gate guardians | `public` | CF-116 116739 is on a pylon beside Highway 401. |
| Air Force Heritage Park, Slemon Park | `public` | Former CFB Summerside; the base closed in 1990 and the park is at the business-park entrance. |
| Former CFB Chatham Voodoo, Miramichi | `public` | Base closed 1996; the pylon stands on open former-base ground. |
| Royal Military College of Canada, Kingston | `public` | RMC's Point Frederick campus grounds are walkable by the public. |
| Val-d'Or CT-133 | `public` | On a pylon in the town; exact street not established. |
| **Everything else** | `restricted` | Inside a controlled base perimeter: Bagotville, 4 Wing Cold Lake, Borden, CFSATE, 15 Wing, 22 Wing, 5 Wing Goose Bay, CFB Kingston, CFB Saint-Jean, Valcartier, Saint-Hubert, Longue-Pointe, Petawawa, Gagetown, Edmonton, Suffield, Shilo, Connaught Range, 3 CFFTS Southport. |

The Musée de la Défense aérienne de Bagotville is marked `restricted` even though
it is a public-admission museum, because reaching it means passing the 3 Wing
gate. A visitor with ID can get in; someone who cannot show ID cannot. That is a
judgment call a human on site should confirm and possibly downgrade to `public`.

Base Borden Military Museum is likewise a public-admission museum inside a base
whose gates now check identification; marked `restricted` for the same reason.

---

## 4. Corrections and conflicts

**Resolved:**

1. **CT-134 Musketeer 134228 was claimed at two sites.** Canadian Warplanes lists
   it both at the Base Borden Military Museum and, mounted on a pylon, in the
   Winnipeg air park. Winnipeg has photographic evidence dated 8 July 2006 and an
   earlier run-up photo "in Winnipeg ca 1992". **134228 recorded at 17 Wing
   Winnipeg; the second Borden Musketeer is recorded with a blank serial**
   alongside its confirmed sibling 134222.
2. **CF-116D 116832 was claimed at Cold Lake and at Shearwater.** The Shearwater
   entry carries a complete disposition — first flight 14 February 1974, Cold Lake,
   AETE, 419 Squadron, Trenton, Mountain View, then to 406 Squadron at Shearwater
   as a training aid in June 2002, stored in museum hangar 2. **Recorded at
   Shearwater.** The Cold Lake listing is stale by more than twenty years.
3. **CF-101B 101050 was claimed at Bagotville and at Borden.** Bagotville has the
   fuller provenance (instructional airframe 842B, ex-433 Squadron, transferred
   from 425 and 433 Squadrons to the museum's holdings in April 2000, document
   number N 1510-21-804-5152). **Recorded at Bagotville**; the Borden appearance
   is a photograph, not a holding.
4. **CH-113 Labrador 11310 / 113310.** Borden was credited with 11310 and Comox
   with 113310 "(from CFB Borden)". Same airframe, moved. **Recorded at Comox
   only.**
5. **CT-133 133079** appears on the Borden page twice, once with the Base Borden
   Military Museum on a pylon and once under CFSATE. Recorded once, with the
   museum.
6. **Supermarine Stranraer 915 (CF-BYJ)** appears on the Shearwater page.
   It is at the Canada Aviation and Space Museum in Ottawa. **Dropped** from the
   Shearwater file.
7. **Cold Lake was one entry covering two places.** Canadian Warplanes treats
   "CFB Cold Lake, Air Force Museum" as a single list. The museum itself now sits
   in the City of Cold Lake with four aircraft at ground level (CF-5 116704,
   CT-133 133413, CT-114 114114, CT-134 134241); the pylon-mounted Canuck,
   Voodoo, Starfighters, Hornet, Dakota and the stored T-33s are on 4 Wing.
   **Split into two sites** with different access types. The split of individual
   airframes between the two is the least certain thing in this delivery.
8. **North Bay Bomarc.** Not recorded — see exclusions.
9. **False markings recorded as markings, not identities.** North Bay's CF-101B
   is 101054 painted as the black EF-101B 101067 (the real 101067 was a leased
   USAF aircraft returned in 1987 and is in Minnesota). Bagotville's CF-100 is
   18472 wearing 18437 to port and 18741 to starboard. Saint-Jean's CT-133 133133
   wears 133333, which is Bagotville's aircraft. Winnipeg's Harvard 20463 wears
   20301. Borden's Kiowa 136247 wears 136228. All are in `aliases` with the true
   serial in `tail_number`.

**Left unresolved, flagged in the rows:**

10. **CF-104 104704 — Bagotville or Suffield?** Canadian Warplanes traces it to
    Suffield as a range target, then to Bagotville "in derelict condition,
    February 2002". Aerial Visuals still lists it at Suffield at 50.21916 N
    111.16010 W. Recorded at Bagotville, `in_storage`, with the conflict stated.
11. **CF-104 104774 — Valcartier or Bagotville?** Listed on the Valcartier page
    as "on display at 5 Area Support Group", and on the Bagotville page as one of
    two hulks to be recovered from Suffield for restoration. **Recorded at
    Valcartier** because that entry describes a display and the Bagotville one
    describes an intention.
12. **CT-133 133413 — Cold Lake or Calgary?** Claimed by the Cold Lake Air Force
    Museum (backed by Wikipedia, "former AETE, grey with red X") and by
    The Military Museums in Calgary ("outside the Cold War Hangar, modified from
    CX-133 back to CT-133 Mk 3"). Recorded at Cold Lake; whoever holds Calgary
    should check this before entering a 133413 there.
13. **CT-114 114004 — 17 Wing or the Royal Aviation Museum of Western Canada?**
    Wikipedia lists 114004 as "on loan to" RAMWC; Canadian Warplanes puts it at
    1 Canadian Air Division HQ, 17 Wing. Recorded at 17 Wing with the loan noted.
14. **Winnipeg and Bagotville both display an ex-German Sabre 6 quoted as 23605.**
    Winnipeg's returned from Baden-Soellingen in July 1981 (c/n 1605); Bagotville's
    came from the Lahr main gate in 1994 and is painted as 19454 of 414 Squadron.
    They cannot both be 23605. **Neither row carries a serial**; both carry 23605
    in `aliases` as a worn marking. This is the single most useful thing a human
    could resolve.
15. **CT-133 "13345" at Greenwood** is one digit short in the source. Recorded as
    133345 with the reconstruction stated in the description.
16. **CC-144 614 at CFSATE and Sea King 408 at CFSATE** are quoted by the source
    as three-digit tail codes. Written out as 144614 and 12408 per the Canadian
    full-serial convention, which is the brief's instruction, but they are
    reconstructions and are described as such.

---

## 5. Excluded, and why

| Excluded | Reason |
|---|---|
| **CIM-10 Bomarc at North Bay** | The missile in Veterans Park on Kate Macé Way was on loan from the National Museum of the USAF from 1979 and **was removed by the NMUSAF on 15 September 2009** because deterioration made it unmaintainable. Nothing is there. The former launch site five nautical miles north on Highway 11N kept its 28 launcher "coffins", which are now storage sheds on Canadore College property, but **no missile**. |
| **CIM-10 Bomarc at La Macaza** | No. 447 SAM Squadron stood down in 1972. The bunkers and ancillary buildings remain; **no missile survives on site**. The only Bomarcs preserved in Canada are 60945 at the Canada Aviation and Space Museum, Ottawa, and 60447 at the Alberta Aviation Museum, Edmonton — both other agents' sites. |
| **CF-101B 101037, Slemon Park** | Canadian Warplanes states flatly "It was scrapped in 2025." The park's own display page still lists a Voodoo, which is probably an un-updated page. Excluded per the rule against recording scrapped aircraft — but see open question 1. |
| **National Air Force Museum of Canada / RCAF Memorial Air Park, 8 Wing Trenton** | Assigned to the museums agent by the brief. Its outdoor Air Park is part of that museum, not a separate wing display. |
| **9 Wing Gander** | No gate guardian or memorial airframe found on the wing. Gander's preserved aircraft, including CF-101B 101065, are at the **North Atlantic Aviation Museum** in the town — a civilian museum, another agent's. |
| **CFS Alert** | No preserved airframe. The station has the Alert Memorial Cairn commemorating the nine killed in the crash of Lancaster KB965 on 31 July 1950; a cairn is not an airframe. |
| **CFB Esquimalt** | The CFB Esquimalt Naval and Military Museum's exhibits are naval; no aircraft found. |
| **CFB Halifax** | No preserved airframe found; 12 Wing Shearwater across the harbour holds the region's naval-aviation collection. |
| **CFB Wainwright** | No preserved airframe found. |
| **CFB Mountain View (ATESS)** | Holds roughly 60 stored CT-114 Tutors, a CF-100 and a CT-133 in open storage as a disposal pool. No public access and the holdings churn; not a visitable site. Listed here so the omission is on the record. |
| **Former stations with no surviving on-site gate guard** | **Penhold, Gimli, Rivers, Downsview, Uplands, Mont-Apica, Sept-Îles, Senneterre, Lac St-Denis, Moisie, Beausejour, Yorkton, Dana** — no airframe found still standing at the station site. Gimli's CT-133 133239 and Portage la Prairie's CT-133 133277 are in town parks, not at the station, and belong to the monuments agent (see leads). Uplands' CF-101B 101045 was dedicated on a pylon on 1 April 1986 and has since gone to the Canadian Warplane Heritage Museum. |
| **CF-101B of unknown serial "at CFB Suffield"** | Canadian Warplanes carries a caption for a Voodoo at Suffield with no serial and no display context, and Aerial Visuals' Suffield dossier does not list one. Not recorded. |
| **CF-101B 101042, CFB Gagetown** | Derelict on the artillery range as a target. Not a display and not accessible. |
| **CF-100 18104, Saint-Jean-sur-Richelieu Airport** | On a pedestal beside the *civil* airport (CYJN), not inside the base. Left to the monuments agent — see leads. |
| **USAF T-33A 53-5413, Happy Valley** | On a pylon in the town of Happy Valley-Goose Bay in USAF markings, not on 5 Wing. Left to the monuments agent. |

---

## 6. Blank fields left deliberately

- **`latitude`/`longitude` blank at 24 of 29 sites.** Pins were written only where
  Aerial Visuals or Wikipedia gave real coordinates (15 Wing Moose Jaw, CFB
  Suffield, 5 CDSB Gagetown, Shearwater, Shilo, 17 Wing Winnipeg, Cold Lake Air
  Force Museum). Every other site has a postal code instead. No coordinate in
  this delivery was inferred from a base's general location.
- **`year_built` blank on every row.** No sourced build or delivery date was
  found for any airframe, only service dates. A serial was never converted into a
  year.
- **`tail_number` blank on 7 rows**: the two ex-German Sabres (see conflict 14),
  the second Borden Musketeer, the Greenwood grey CT-133 painted as 21393, the
  17 Wing Bolingbroke, and the Shilo Auster and L-19.
- **`website` blank at most base sites** — most wings have no dedicated heritage
  page; the CFMWS pages are generic base portals.

---

## 7. Needs a human on site — ranked

1. **Slemon Park, Summerside: is CF-101B 101037 still there?** Canadian Warplanes
   says scrapped in 2025; the park's own page still lists a Voodoo. One
   photograph dated 2025 or 2026 settles it. If it survives, add a row.
2. **The two ex-German Sabre 6s at Winnipeg and Bagotville.** Two airframes, one
   quoted serial (23605). Read the plates and, better, the data plate. Until then
   neither row can carry a serial.
3. **The Cold Lake split.** Which airframes stand in the museum's ground-level
   airpark in the city and which stand on pylons on 4 Wing? My split follows
   Wikipedia for the museum's four and gives 4 Wing the rest, but the boundary is
   soft — in particular CT-133 133181 and 133094, CT-114 114083, and the stored
   T-33s 21231, 21146 and 133353.
4. **CF-104 104704 and 104774 — Suffield, Bagotville or Valcartier?** Three sites,
   two airframes, contradictory sources.
5. **CFB Suffield.** Aerial Visuals gives one pin and asks its own readers where
   exactly the CF-100 and CF-104 stand. Is CF-100 18175 still displayed at
   Ralston, and can it be seen from public ground? If the answer is yes, the
   access type should change to `public`.
6. **22 Wing North Bay.** Are CF-100 100500 and CF-101 101054 still on their
   pylons? The wing has had no flying unit since 1992 and the airfield facilities
   were demolished or sold; Wikipedia's article on the base mentions no displays.
7. **Bagotville and Borden access.** Both run public-admission museums inside base
   gates. If a visitor without a DND pass can simply drive in, both should be
   `public`.
8. **CFSATE's Tutor inventory.** Eighteen airframes plus a cockpit are listed. Are
   they all still there, and does the school ever show them? The rows are marked
   `in_storage` on the assumption a visitor cannot see them.
9. **Shilo's Auster and L-19 serials.** Neither source gives one.
10. **Val-d'Or CT-133 133167** — exact street location, and whether it stands at
    the airport (former base) or in a town park. That decides whether the record
    belongs to me or the monuments agent.

---

## 8. File and row count table

| File | Rows | Rows with serial |
|---|---:|---:|
| 16_wing_borden_base_borden_military_museum_aircraft.csv | 25 | 24 |
| cfsate_borden_aircraft.csv | 28 | 28 |
| 17_wing_winnipeg_air_park_aircraft.csv | 17 | 15 |
| 12_wing_shearwater_aviation_museum_aircraft.csv | 16 | 16 |
| 4_wing_cold_lake_air_park_aircraft.csv | 15 | 15 |
| 14_wing_greenwood_military_aviation_museum_aircraft.csv | 14 | 13 |
| bagotville_musee_defense_aerienne_aircraft.csv | 13 | 12 |
| 19_wing_comox_air_force_museum_aircraft.csv | 12 | 12 |
| 15_wing_moose_jaw_aircraft.csv | 5 | 5 |
| cdsb_gagetown_aircraft.csv | 4 | 4 |
| cfb_saint_jean_aircraft.csv | 4 | 4 |
| cold_lake_air_force_museum_aircraft.csv | 4 | 4 |
| air_force_heritage_park_summerside_aircraft.csv | 3 | 3 |
| cdsb_valcartier_aircraft.csv | 3 | 3 |
| 22_wing_north_bay_aircraft.csv | 2 | 2 |
| 8_wing_trenton_gate_guardians_aircraft.csv | 2 | 2 |
| cdsb_petawawa_aircraft.csv | 2 | 2 |
| cfb_edmonton_displays_aircraft.csv | 2 | 2 |
| cfb_kingston_1_wing_aircraft.csv | 2 | 2 |
| cfb_shilo_rca_museum_aircraft.csv | 2 | 0 |
| connaught_range_ottawa_aircraft.csv | 2 | 2 |
| rmc_kingston_aircraft_displays_aircraft.csv | 2 | 2 |
| 3_cffts_southport_portage_aircraft.csv | 1 | 1 |
| 5_wing_goose_bay_labrador_military_museum_aircraft.csv | 1 | 1 |
| cfb_suffield_displays_aircraft.csv | 1 | 1 |
| former_cfb_chatham_voodoo_aircraft.csv | 1 | 1 |
| garrison_saint_hubert_aircraft.csv | 1 | 1 |
| longue_pointe_garrison_montreal_aircraft.csv | 1 | 1 |
| val_dor_ct133_aircraft.csv | 1 | 1 |
| **Total** | **186** | **179 (96%)** |

Type spread: CT-114 Tutor 33, CT-133 Silver Star 26, CF-101 Voodoo 14,
CF-116/CF-5 Freedom Fighter 12, CF-100 Canuck 12, CH-136 Kiowa 11,
CF-104 Starfighter 7, F-86 Sabre 6, CT-134 Musketeer 6, CC-129 Dakota 5,
CH-124 Sea King 4, CP-107 Argus 4, Tracker (CS2F + CP-121) 6, Harvard 3,
CC-144 Challenger 3, plus 30 singleton types.

---

## 9. Leads for other agents

**Monument / plinth agent — aircraft found while working the base sources that
are NOT on a base:**

- **CF-100 Canuck 18488**, pylon, Centennial Park on Highway 2, west end of Moncton NB
- **CF-100 Canuck 18602** (CAF A683), pylon, Head Lake Park near Haliburton Highlands Secondary School, Haliburton ON
- **CF-100 Canuck 18619** (CAF A682), pylon, Paul Coffey Park, Malton ON
- **CF-100 Canuck 18626**, pylon, Lee Park, North Bay ON — painted as 101028
- **CF-100 Canuck 18104** (A611), pedestal beside Saint-Jean-sur-Richelieu Airport CYJN, QC — first CF-100 accepted by the RCAF
- **CF-101B Voodoo 101015**, pylon, Parc Commémoratif des Vétérans, Lévis QC
- **CF-101B Voodoo 101028**, Hillsborough NB
- **CF-101B Voodoo 101051**, pylon, Thetford Mines airport QC
- **CF-104 Starfighter 104702**, pylon, Joe Hoffner Memorial Park, Grand Centre, Cold Lake AB
- **CT-133 133239**, pylon, Gimli MB (former RCAF Station Gimli, now in town)
- **CT-133 133277**, pylon, Island Park, Portage la Prairie MB
- **CT-133 133232**, pylon at 500 Wing RCAFA, Portage Avenue, Winnipeg MB — Golden Centenaires, recently repainted Red Knight
- **CT-133 133347**, pylon, RCAFA 424 Wing HQ, Cornwall ON; **CT-133 133423**, pylon, Nav Canada Training Centre, Cornwall ON
- **CT-133 133199** RCL Branch 63 Collingwood ON; **133103** RCL Branch 197 Acton ON; **133110** Hamilton AFAC Wing, Dundas ON; **133578** RCL General Stewart Branch 4 / 702 Wing, Lethbridge AB; **133271** Millennium Park near the Legion, Rocky Mountain House AB
- **CT-133 133011** pylon Edmonton AB; **133097** pylon Edson AB; **133518** pylon Leduc AB; **133130** pylon Brandon Municipal Airport MB; **133373** Sugar Bowl Park, Fort Erie ON; **133591** pedestal, Grand Bend ON; **21422** pylon near London Airport terminal ON (painted 21491); **133648** wind vane on a pylon, Princeton Airport BC; **21630** near Diefenbaker International Airport, Saskatoon SK; **133389** Pictou NS (off its pylon, awaiting preservation); **133411** dismantled in a park at Yarmouth NS
- **CT-114 Tutor 114187**, between Millennium Park and College of the Rockies, Creston BC
- **F-86 Sabre 23245**, pylon, 428 Wing RCAFA, Ontario
- **Harvard Mk II AJ693**, pylon, Kingston Municipal Airport, RCAFA 416 Wing ON
- **Harvard Mk 4 20451** (CF-ROA) Ottawa; **Harvard C-FPTP** and **CT-133 133379** (C-FSKH) at the NRC Flight Research Laboratory, Building U-61, Montréal Road, Ottawa
- **CIM-10B Bomarc 60945** Canada Aviation and Space Museum; **60447** Alberta Aviation Museum

**Museums agent:**

- **North Atlantic Aviation Museum, Gander NL** — holds CF-101B 101065, Canso 9837, Hudson, Expeditor CA110, Link Trainer
- **Québec Aerospace Museum / Musée de l'aérospatiale du Québec, Saint-Hubert QC** — CF-100 18760, the last CF-100 to fly (28 June 1982), dismounted from its St-Hubert pylon
- **Atlantic Canada Aviation Museum, Goffs NS** — CF-100 18747, CF-101B 101043 "Lynx One Canada", Sabre 23355 ex-CFB Chatham, CF-104 104783, CT-133 133365 cockpit
- **Jet Aircraft Museum, London ON** — CF-101F 101006, the last Voodoo to fly in Canada, ex-CFB Cornwallis Museum
- **Canadian Air Land Sea Museum, Markham ON** — CF-100 Mk 2 prototype 18103, CF-100 18506, CF-104D 104644, CT-133 133357/133398/133421
- **Memorial Military Museum, Campbellford ON** — CF-100 Mk 2T 18106 (B615), stored outdoors since 2009 and reported deteriorating; several museums have enquired about acquiring it
- **Canadian Museum of Flight, Langley BC** — CF-100 18138, CF-104D 104645, CT-133 21487, and CF-101B 101063 being transferred in from Shearwater
- **Alberta Aviation Museum, Edmonton** — CF-100 18476, CF-101B 101060 on a pylon out front, CT-133 133506 and 133533, Bomarc 60447
- **The Military Museums / Air Force Museum Society of Alberta, Calgary** — took delivery of a CF-101 Voodoo on loan from the Alberta Aviation Museum on 8 September 2023; also claims CT-133 133413 (see conflict 12)
- **Frontiers Military Aviation Museum, Saint-Jean-Chrysostome QC**; **Musée du Corps royal canadien des munitions** is recorded here as a base site
- **Summerside Heritage Aircraft Society / Aviation Heritage Society (PEI)** runs the Slemon Park display recorded here; its own site was returning HTTP 409 during this pass

**Whoever handles the USA:** CF-100 18241 and 18504, CF-101B 101044 and 101022,
CF-101B 101041 (as USAF 57-0377 "MAINEiacs" at Bangor ANGB) and EF-101B 101067
(Minnesota ANG Museum) are all ex-RCAF airframes now in the United States.


---

# Research pass: western monuments and Legion displays

# CA_WEST — monuments, Legion displays, air parks and oddities
## British Columbia, Alberta, Saskatchewan, Manitoba, Yukon, Northwest Territories, Nunavut

Output directory: `/home/claude/ca/west/`
Files: `ca_museums.csv` (37 sites) + 37 `<slug>_aircraft.csv` files (81 rows) + `build.py`
(the generator; re-running it reproduces every CSV exactly).

Excluded by assignment: the major museums of these provinces (Royal Aviation Museum of
Western Canada, Reynolds-Alberta, Alberta Aviation Museum, Hangar Flight Museum Calgary,
Bomber Command Museum Nanton, Canadian Museum of Flight Langley, BC Aviation Museum Sidney,
Comox Air Force Museum, Commonwealth Air Training Plan Museum Brandon, Western Development
Museum Moose Jaw, Yukon Transportation Museum) and every CAF base display.

---

## 1. Sources and how much weight each carried

| Source | Weight | What it actually gave me |
|---|---|---|
| **rwrwalker.ca** | **unusable** | The domain no longer serves the Canadian Military Aircraft Serial Numbers site. `https://www.rwrwalker.ca/` now returns a "Walker Military Insights" WordPress shell whose top-ranked content is an online-casino review page (`best-online-casino-canada.rwrwalker.ca`). Deep URLs such as `/canadian-forces-cf-104d/` and `/canadian-armed-forces/` still resolve but the per-serial disposition tables the brief describes are gone. **The assignment's designated spine does not exist any more.** See "Leads for other agents". |
| **silverhawkauthor.com** (Harold A. Skaarup, *Canadian Warplanes*) | **primary** | Became the spine in rwrwalker's place. It is organised exactly the way the brief wanted the spine to be: one page per province, alphabetical by town, plus per-type "preserved in Canada" pages. Pages used: `/aviation/canadian-warplanes-1-british-columbia/`, `/canada/alberta/canadian-warplanes-2-alberta/`, `/aviation/canadian-warplanes-3-saskatchewan/`, `/canada/manitoba/canadian-warplanes-4-manitoba/`, `/aviation/canadian-warplanes-11-northwest-territories-12-nunavut-13-yukon-territory/`, plus the CT-133 and CF-104 survivor pages. Its `post-sitemap*.xml` (60,822 URLs) is the reliable way to find its page URLs — guessing slugs 404s. |
| **aerialvisuals.ca Locator** | **primary for coordinates and serials** | The region listing is a POST form (`Continent`/`Country`/`Region`/`Scope`/`ShowMap`) but the results are also reachable as `Locator.php?Region=<X>`. With `ShowMap=1` the page embeds a Google Maps marker per site whose `position: {lat,lng}` and `LocationDossier.php?Serial=NNNN` link can be scraped together — that is where every coordinate in `ca_museums.csv` came from. Per-site dossiers give serials and c/ns. **Note: `LocationDossier.php` returns an empty body to plain curl but fetches fine through WebFetch, and the site rate-limits at roughly one request per 60s (HTTP 429).** |
| **Wikipedia** survivor/display lists | secondary, lead-grade | `List of surviving McDonnell F-101 Voodoos`, `Canadair CT-114 Tutor`, `Canadair CT-133 Silver Star`, `Avro Canada CF-100 Canuck`, `Canadair CF-5`. Useful for cross-checking serials. **`en.wikipedia.org` article pages are blocked from this environment ("domain is cache-only"), but `curl https://en.wikipedia.org/wiki/Special:Export/<Title>` works and returns raw wikitext** — that is how these were read. |
| Site-owner pages | decisive where they exist | Tourism Moose Jaw (Tutor at 450 Diefenbaker Dr), experiencecomoxvalley.ca (Tutor 114115), kfcentre.ca, canadianstarfightermuseum.ca, spectacularnwt.com (Bristol monument), mhs.mb.ca Historic Sites of Manitoba (Miss Piggy, Garland Viscount), centralalbertaonline.com (Sylvan Lake Sea Harrier). |
| airhistory.net | not used | Blocked per brief. |

**Which list proved stale, and how I know.** Skaarup's Manitoba page and Wikipedia's CF-104
list both still place CF-104 **12703** at the Canadian Starfighter Museum, St. Andrews
Airport. The museum's own news page says it lost its St. Andrews hangar in June 2021, agreed
with the Royal Aviation Museum of Western Canada to display 12703 there, and moved the
aircraft in October 2021. **St. Andrews is therefore not a site**, and 12703 belongs to
whoever is writing RAMWC. Skaarup compounds this by listing 12703 at *both* places on the
same CF-104 page.

---

## 2. Corrections made, with evidence

- **CF-104 12703 / Canadian Starfighter Museum, St. Andrews MB — dropped.** Moved to RAMWC
  October 2021 (museum's own `museum-news.php`). Two of my three sources are stale here.
- **CT-133 133413 — placed at The Military Museums, Calgary, not Cold Lake.** Skaarup's
  CT-133 page lists 133413 under CFB Cold Lake *and* under The Military Museums. The Calgary
  Herald (7 Sept 2022) and The Military Museums' own blog record its arrival in Calgary and
  its conversion back from CX-133 ejection-seat-testbed standard, so Calgary wins.
- **F-104 at Innisfail is an F-104F, not an F-104DJ.** AerialVisuals types it "F-104DJ"
  (a Japanese variant). Serial 29+17 with c/n 5070 is in the West German F-104F block;
  Skaarup calls it an F-104F. Recorded as `F-104` + variant `F`, wearing CF-104 paint.
- **Sabre 23060, Sidney — mark unresolved.** AerialVisuals: Sabre 5, c/n 0850. Skaarup:
  Sabre Mk VI. Recorded as Mk 5 with the conflict stated in `description`. The serial is not
  in dispute.
- **CT-134 at Fort la Reine — 134328 vs 134238.** AerialVisuals dossier says 134328; Skaarup
  says 134238 and also lists 134238 elsewhere in Portage la Prairie. Went with 134328 and
  flagged it for a placard reading.
- **CT-133 21437 is double-counted in the wild.** Rocky Mountain House holds the real 21437
  (on loan from Nanton); Nanton's own 21082 is *painted as* 21437. Photo captions saying
  "21437" can mean either airframe. Said so in the Rocky Mountain House row.
- **RCAFA 602 Wing Saskatoon CT-133 — identity soft.** AerialVisuals itself records
  "21630 or 21633 as 21630". Recorded as 133630 with the doubt in `description`.
- **Joe Heffner / Joe Hoffner Memorial Park.** Skaarup spells it Hoffner, AerialVisuals
  Heffner. Used Heffner; both spellings noted in the aircraft description so a search finds it.

---

## 3. Judgment calls

- **Replicas.** Three full-scale replicas are recorded as sites because they *are* the object
  a visitor travels to see and each stands where a Legion/veterans' club or airport put it:
  the ANAF Unit 5 Spitfire at Vernon, the Sopwith Triplane at Nanaimo's Collishaw Air
  Terminal, and the Nieuport 11 inside the Saskatchewan Aviation Museum. Every one says
  "replica" and "not an original airframe" in `description`. If the house rule is to drop all
  replicas, the Vernon and Nanaimo *sites* disappear entirely; the Nieuport is just one row.
- **The Military Museums, Calgary, is one site, not three.** The Air Force Museum of Alberta
  and the Naval Museum of Alberta share one campus at 4520 Crowchild Trail SW. Splitting them
  would put a Sea Fury and a Sabre a hundred metres apart in different records.
- **Miss Piggy (Churchill) is included even though it is a crash site.** It is not "an
  airframe in a dismantler with no public access": it is intact, signposted, has a picnic
  area, and visitors walk into it and sit in the seats. Access `public`.
- **Garland Viscount is `public`.** It is a private summer cottage, but it sits on Garland's
  main street in plain view; the aircraft is seen from the road, not entered.
- **Cockpit section flagged:** RCMP Otter CF-MPW at the RCMP Heritage Centre is a cockpit
  section only, and says so.
- **Springbrook is `appointment`** (Harvard Historical Aviation Society is a working society
  on the former CFB Penhold field). Everything else is `public`; nothing in this file sits
  inside a base gate, by design.
- **`year_built` is blank on all 81 rows.** No source I used gave a sourced build or delivery
  date I was willing to assert. Construction numbers and service dates went into
  `description` instead.
- **`latitude`/`longitude` blank on 11 of 37 sites.** Only AerialVisuals-mapped positions were
  used. I did not fill in the rest from a town centroid.
- **`tail_number` blank on 14 of 81 rows** — the Claresholm Harvard (AerialVisuals shows only
  the fragment "261", not enough to assert a serial), the Vernon and Nanaimo replicas, the
  Sperwer UAV, and nine KF Centre / Saskatchewan Aviation Museum airframes whose owners do
  not publish a registration.

---

## 4. Excluded, and why — named

| Excluded | Province | Reason |
|---|---|---|
| Canadian Starfighter Museum, St. Andrews | MB | Lost its hangar June 2021; its CF-104 12703 moved to RAMWC Oct 2021. No longer a visitable site. |
| CT-133 133419 (+ reported 133089/133351), Warner | AB | Skaarup and Wikipedia both place a CT-133 "in Warner, Alberta". AerialVisuals has no Warner entry, no owner, no address and no evidence of public access. Cannot stand behind it. Best single lead left in Alberta. |
| CT-133 133011 / L3Harris (ex-Spar Aerospace), Edmonton | AB | AerialVisuals maps two CT-133s at 53.31938,-113.57214 (an industrial site near Edmonton International). Skaarup lists "Edmonton, CT-133 133011, mounted on a pylon" with no address. Almost certainly the same aircraft, but the site is a contractor's yard and public visibility is unverified. |
| Chipman DC-3 fuselage | AB | Fuselage only on private land, no owner or access information. |
| Okotoks / "Northwest Aviation and Heritage Museum, Okotoks Air Park" | AB | AerialVisuals carries a Beech Expeditor 2334 and a DHC-1 at Okotoks with an explicit "a map reference is needed… are either kept in view from a public vantage point?" flag. Museum's current existence unverified. |
| Ralston F-101; Suffield CF-100 and CF-104; Gazelles at Suffield Airport | AB | CFB Suffield / DRDC Suffield — CAF base displays, another agent's. |
| Steele Barracks CH-136 Kiowa, Edmonton | AB | 3 CDSB Edmonton — base display. |
| CFB Cold Lake CF-104 104872 and the 4 Wing park; Cold Lake Air Force Museum | AB | Base displays / excluded museum. Only the *town* park (Joe Heffner) is recorded. |
| Air Force Heritage Museum and Air Park, 17 Wing Winnipeg; CFB Winnipeg Navigation School | MB | Base displays. |
| The RCA Museum, CFB Shilo | MB | Sits inside CFB Shilo; treated as a base site. It holds an Auster AOP.5 TJ398 and Cessna L-19 Bird Dogs and is worth a record if the bases agent is not covering museums-on-base. |
| Selkirk Airport (An-2, DC-3, DC-3 fuselage) | MB | AerialVisuals asks whether these are active or static; no display evidence. |
| Gimli Airport C-46s / Expeditor; Gimli Argus 20715 wreckage | MB | The Argus forward fuselage lies in a private field beside a house among derelict cars — no public access. C-46s are commercial airframes. |
| Winnipeg Assiniboine Park Zoo Bell 206 | MB | Set-dressing in a zoo exhibit, not a preserved airframe record I could verify. |
| Points North Landing DC-3 fuselage; Malcolm Island / Reindeer Lake DC-3s | SK | Remote mining and float airstrips, fuselage hulks, no public access. |
| Saskatoon HS-748 | SK | AerialVisuals: "This is a private residence and is not accessible to the public." |
| Assiniboia (Whereatt estate: Hurricanes, Lysander, Bolingbrokes, Ansons, Cranes) | SK | A dispersed private estate collection in parts; AerialVisuals flags it "NEED HELP… can you confirm?" No public access. A significant airframe cache, but not a site. |
| 15 Wing Military Aviation Museum, CFB Moose Jaw | SK | Base display. |
| Quesnel "Heritage Aircraft Museum" | BC | Appears only in Skaarup. Not in the AerialVisuals Locator, no website, no current evidence it exists. Presumed defunct/private. |
| Aerospace & Technology Museum of British Columbia, Fort St John (Sabre 23692) | BC | Skaarup describes the Sabre as *in storage in Seattle* and "to be moved to Fort St John". A plan, not a display. |
| Military Education Centre Museum, Chilliwack (Tracker 1573 / C-FKVG) | BC | Tracker moved to the BC Aviation Museum in January 2021. Site gone. |
| Royal Roads Military University Sabre, Colwood | BC | AerialVisuals: "Apparently there was a Canadair Sabre displayed on the grounds… Is it still there?" Unresolved; likely long gone. |
| Esquimalt CF-101 + CP-121 | BC | Same "may be displayed, can you confirm?" flag, and Esquimalt is a base. |
| Chemainus B737s (Artificial Reef Society) | BC | Deliberately sunk as a dive reef. Not visitable in the sense this database means. |
| Delta Heritage Air Park; BCIT Aerospace, Vancouver; Abbotsford Skydiving Centre | BC | Working airparks and a training school. BCIT's airframes (Harvard, Spitfire, SM.1019, 737, Falcon 20) are instructional and not on public display; AerialVisuals flags access as unknown. |
| Coal Harbour, Tofino, Sechelt, Pemberton, Fort Langley, Raven Field, Flin Flon, Nanaimo Harbour (Beavers/Otters) | BC/MB | Working floatplane bases. Aircraft in service. |
| Buffalo Airways, Yellowknife and Hay River (DC-3s, DC-4, C-46s, Canso, P-3) | NT | An operating airline. Aircraft in service or in a company storage yard. The Hay River storage row is a dismantler-equivalent. |
| Inuvik Airport "DC-3" | NT | It is Basler BT-67 C-FMKB (c/n 19560, ex USN 315094) — a converted, working aircraft, not a display. |
| Beaverlodge Lake Bristol Freighter wreck | NT | Wreck on a lakeshore 150 nm NW of Yellowknife. Not reachable. |
| Sitidgi Lake PBY | NT | Reportedly sold, position unconfirmed. |
| Arviat Lancaster; Resolute Bay F-27 and Lancaster | NU | Crash/wreck sites; the Arviat Lancaster is reported submerged in a lake. **Nunavut yields no recordable site.** |
| Whitehorse DC-3 weathervane CF-CPY; Yukon Transportation Museum; "Queen of the Yukon" Ryan Brougham replica | YT | Excluded by the assignment (the DC-3) or inside the excluded museum. **Yukon yields no recordable site outside the exclusions.** |

---

## 5. Needs a human on site — ranked

1. **Claresholm Harvard memorial (AB)** — read the plaque. Skaarup says serial TBC;
   AerialVisuals shows only "261". This is a BCATP memorial to No. 15 SFTS and deserves a
   real serial.
2. **Warner, Alberta (AB)** — is 133419 there, is it one aircraft or three, who owns it, and
   can the public see it? This is the largest unresolved cluster in the region.
3. **The Military Museums, Calgary (AB)** — confirm CF-104 **12846**, CF-5 **116704** and the
   Sperwer. 12846 appears in Skaarup only and in neither Wikipedia's CF-104 survivor list nor
   the AerialVisuals site dossier. Also confirm whether CF-188 188719 is still there.
4. **Fort la Reine, Portage la Prairie (MB)** — CT-134 **134328** or **134238**?
5. **RCAFA 602 Wing, Saskatoon (SK)** — is the CT-133 **21630** or **21633** repainted as
   21630?
6. **Joe Heffner Memorial Park, Cold Lake (AB)** — confirm the town Tutor is **114083**.
   AerialVisuals records the airframe without a serial; the pairing is inferred from
   Wikipedia's "CT-114083 – Cold Lake, Alberta".
7. **The Driftwood, Sylvan Lake (AB)** — Sea Harrier ZD615 was reported for sale in 2025. Is
   it still on the patio?
8. **Wetaskiwin Legion CT-134 134232 (AB)** — Skaarup only; not in the AerialVisuals Locator.
   Needs a dated photograph.
9. **Kamloops Airport (BC)** — Skaarup lists CF-116 **116703** as well as 116740. Only 116740
   is recorded here. Is there a second Freedom Fighter at Kamloops?
10. **Springbrook / Harvard Historical Aviation Society (AB)** — Skaarup lists CT-133 **21506**
    there, but 21506 (133506) is also the Alberta Aviation Museum's aircraft. Only the Harvard
    20370 is recorded. Which CT-133, if any, is at Springbrook?

---

## 6. File and row counts

| Province/Territory | Sites | Aircraft rows | With tail number | Serial coverage |
|---|---|---|---|---|
| Alberta | 14 | 25 | 23 | 92% |
| British Columbia | 9 | 17 | 9 | 52% |
| Saskatchewan | 4 | 27 | 23 | 85% |
| Manitoba | 8 | 10 | 10 | 100% |
| Northwest Territories | 2 | 2 | 2 | 100% |
| Yukon | 0 | 0 | 0 | — |
| Nunavut | 0 | 0 | 0 | — |
| **Total** | **37** | **81** | **67** | **83%** |

British Columbia's low serial coverage is almost entirely the KF Centre for Excellence, whose
own aircraft page publishes types and build years but no registrations, plus the two replicas.

Type coverage of the classic Canadian plinth population in the west, outside the excluded
museums and bases: **CT-133 × 10** (Edson, Leduc, Lethbridge, St. Albert, Rocky Mountain
House, Brandon, Gimli, Portage/Island Park, Winnipeg/Woodhaven, Saskatoon/602 Wing, plus
Calgary's 133413 and Saskatoon's CE-133 21526), **CT-114 × 5** (Cumberland, Creston, Cold
Lake, Moose Jaw, Southport), **CF-104/F-104 × 3** (Cold Lake, Innisfail, Kelowna),
**CF-101 × 2** (Abbotsford, Calgary), **CF-5 × 3** (Kamloops, Calgary ×2), **Sabre × 2**
(Sidney, Calgary), **CT-134 × 3** (Wetaskiwin, Southport, Fort la Reine), **Harvard × 2**
(Claresholm, Springbrook), **Tracker × 1** (Saskatoon). No CF-100, no CP-107 Argus, no
Dakota and **no CIM-10 Bomarc** exists in western Canada outside the excluded museums —
Canada's Bomarc squadrons were at North Bay, Ontario and La Macaza, Quebec only.

---

## 7. Leads for other agents

- **rwrwalker.ca is gone.** Every agent given it as a spine needs to know. Substitute
  `silverhawkauthor.com` (province pages + per-type survivor pages, found through
  `post-sitemap*.xml`) and the `aerialvisuals.ca` Locator scraped with `ShowMap=1` for
  coordinates. `caspir.warplane.com` (Canadian Warplane Heritage's serial registry) is
  searchable by type and serial but not browsable by province.
- **Wikipedia is fetchable only via `Special:Export`** in this environment. Ordinary article
  URLs return "domain is cache-only".
- **AerialVisuals `LocationDossier.php` needs WebFetch, not curl**, and rate-limits at about
  one request/minute.
- **For the RAMWC agent (Manitoba):** CF-104 **12703** moved there from the Canadian
  Starfighter Museum in October 2021 — it is on RAMWC's own aircraft page. Also CF-101
  **101034**, CT-114 **114004**, and Canadair Sabre No. 1815 (the last Sabre built, ex-Pakistan
  Air Force).
- **For the bases agent:** CFB Cold Lake CF-104 **104872** is a composite wrongly marked
  **104880**; the four serials tangled up in it are 12803, 12816, 12872 and 12880, and the
  real 12880 was scrapped in Germany. Also: 17 Wing Winnipeg Air Force Heritage Park holds
  CF-101 **101008**, CF-100 **18784** and CF-104 **104753**; CFB Suffield holds a CF-100 and a
  CF-104 (104704 later went to Bagotville in derelict condition); Ralston has a CF-101.
- **For the Ontario/Quebec agents:** the Nanton CT-133 **21082 is painted as 21437** while
  the real 21437 is at Rocky Mountain House — the same trap may exist elsewhere.
- **Unclaimed western sites I deliberately excluded but which someone with better access could
  resolve:** Warner AB; the Edmonton L3Harris CT-133s; the Harry Whereatt estate at
  Assiniboia SK (Hurricanes 5447/5455, Lysander 2365, Bolingbrokes, Ansons, Cranes, Cornells,
  Fleet Forts); the RCA Museum at CFB Shilo.


---

# Research pass: eastern monuments and Legion displays

# CA_EAST — monuments, Legion displays, air parks and oddities, Eastern Canada

Ontario, Quebec, New Brunswick, Nova Scotia, Prince Edward Island,
Newfoundland and Labrador. Output directory `/home/claude/ca/east/`.

Excluded by assignment (another agent has them): Canada Aviation and Space
Museum Ottawa, Canadian Warplane Heritage Hamilton, National Air Force Museum
Trenton, Canadian Bushplane Heritage Centre, Jet Aircraft Museum London,
Montreal Aviation Museum, Shearwater Aviation Museum, Atlantic Canada Aviation
Museum, Greenwood Military Aviation Museum, North Atlantic Aviation Museum
Gander, and every CAF base display.

---

## Sources and their weight

**1. `aerialvisuals.ca` Locator — the spine actually used.** The brief named
`rwrwalker.ca` as the spine, but **rwrwalker.ca no longer exists as an aviation
site**: the domain has been taken over and rebuilt as a WordPress casino
affiliate site. Its WordPress REST API returns only 189 posts, of which roughly
sixty are surviving aviation pages (CF-101, Dakotas, CF-5, CF-104D, Trackers,
some RCAF serial blocks) and the rest are casino and generic-military filler.
The CF-100, CF-104, CT-133, CT-114, Sabre and most RCAF serial-block pages
**did not survive the migration**. The original site is complete in the Wayback
Machine (333 distinct `.html` pages, last good capture 2021-10-25), but
web.archive.org was intermittently resetting connections from this environment,
so it was used only for spot checks. The surviving live rwrwalker Voodoo page
was used in full and proved decisive (see "Corrections" below).

Instead the spine is the **Aerial Visuals Locator**, queried per province with
`Scope=1` ("aircraft accessible to the public or in view"). That returned 85
Ontario, 26 Quebec, 7 New Brunswick, 6 Nova Scotia, 2 PEI and 12 Newfoundland
and Labrador locations; each location's `LocationDossier.php` page was fetched
and parsed for per-site coordinates and per-airframe serials. Nearly every
coordinate in `ca_museums.csv` comes from this source, at site (not town)
precision. The service rate-limits hard (HTTP 429 after ~15 rapid requests);
fetches were spaced out and retried.

**2. `silverhawkauthor.com` (Harold A. Skaarup, *Canadian Warplanes*).** Not in
the brief, but it is organised exactly the way this assignment is — per-province
survivor pages plus per-type survivor pages — and it is the single richest
source for Canadian plinth aircraft. Used for: serials Aerial Visuals leaves
blank (Sarnia Sabre 23164, Smiths Falls Harvard 20443, Grand Bend CT-133
133591), markings worn, and currency warnings. It is a compiled secondary
source and it does carry typos (it gives the Acton Silver Star both as 133103
and "23103", the latter impossible — 23xxx is a Sabre block).

**3. `rwrwalker.ca` surviving CF-101 page.** Authoritative per-serial
disposition histories. Decisive for the Voodoos (below).

**4. Wikipedia** — `List of surviving McDonnell F-101 Voodoos` was genuinely
useful and agreed with rwrwalker on every Eastern Canadian airframe. The
type-article "Aircraft on display" sections for CF-100, CF-104, CT-114, CT-133,
Sabre and CF-5 are thin (132 bullets worldwide) and added almost nothing beyond
what Aerial Visuals already had.

**5. Veterans Affairs Canada National Inventory of Canadian Military
Memorials** — used to settle the North Bay Bomarc.

**6. `airhistory.net`** was blocked, as the brief warned; one incidental search
snippet from it (Sabre 23053 typed as a Mk 6) is noted below but was not relied
on.

---

## Corrections made, with evidence

**Aerial Visuals records several Voodoos under their instructional-airframe
number, not their serial.** Its dossiers give "s/n 815B", "s/n 831B", "s/n
833B", "s/n 874B". These are Canadian Forces Instructional Airframe numbers.
The surviving rwrwalker CF-101 page names both the serial and the IA number for
each aircraft, which resolves all four, and Wikipedia's surviving-Voodoo list
agrees independently:

| Site | Aerial Visuals | true serial | evidence |
|---|---|---|---|
| Thetford Mines Airport | 815B (c/n 576) | **101051** | rwrwalker: 101051, c/n 576, "Became Instructional Airframe 815 B on 4 May 1983" |
| Hillsborough NB | 831B (c/n 524) | **101028** | rwrwalker: 101028, c/n 524; Wikipedia and Skaarup agree |
| Summerside PEI | 833B (c/n 544) | **101037** | rwrwalker: 101037, c/n 544, IA 833B, "On display at Slemon Park, Summerside, PEI by 1998" |
| Canadian War Museum | 874B (c/n 285) | **101002** | rwrwalker: 101002, c/n 285, IA 874B; Wikipedia agrees |

The IA numbers are carried in `aliases` so a search on them still finds the
airframe.

**Belleville and Trenton Sabres.** Skaarup's province page appeared to swap
them (Belleville 23053, Trenton 23641). His dedicated Sabre-survivors page
resolves it and agrees with Aerial Visuals: **Belleville Zwick's Island is
23641 painted as 23053**, and **Trenton is 23457 painted as 23641**, both in
Golden Hawks colours. The false markings are recorded in `aliases`.

**Fort Erie CT-133.** Aerial Visuals gives 21273 with c/n T33-273 and former
registration N233RK; Skaarup gives 21373. The construction number and the
civil registration both point to 273, so 21273 is recorded.

**CIM-10 Bomarc, North Bay** — the assignment asked whether it is publicly
displayed off base. **It is not.** The Bomarc stood in Lee Park (Veterans Park,
Kate Pace Way) for about three decades and was **removed by the National Museum
of the United States Air Force on 15 September 2009** because it had
deteriorated beyond maintenance; the site is now the Canadore College heliport
(Veterans Affairs Canada NICMM record 5711; Skaarup agrees). Recorded as a fact
in the description of the CF-100 that still stands in Lee Park. No Bomarc row
was written.

**Ontario Science Centre Sopwith Pup replica** — the Ontario Science Centre
closed to the public in June 2024 and the Don Mills building has not reopened.
The replica is not currently visitable. Excluded.

**New Brunswick Aviation Museum, Miramichi** — closed 1 June 2026; aircraft and
artifacts dispersed (its Vampire and Navion to British Columbia, the Nieuport
replica to Moncton, artifacts to the New Brunswick Military History Museum at
Oromocto). Excluded as a museum. The **CF-101B 101053** on Pollard Boulevard at
the former CFB Chatham is a separate outdoor monument and is recorded, with the
closure noted in its description.

**Voodoo 101006** moved from the Cornwallis Military Museum, Nova Scotia, to
the Jet Aircraft Museum, London, Ontario — so it is not in this file set (JAM
is another agent's). Recorded here only as context in the Cornwallis notes.

---

## Judgment calls

- **Replicas are included and labelled.** The brief's `description` field
  explicitly provides for "replica status", so full-scale replicas that *are*
  the monument were kept: the pole-mounted Avro Arrow at Zurakowski Park
  (Barry's Bay), the Spitfire and Hurricane in Jackson Park (Windsor), the
  Spitfire in Spitfire Park (Essex), the AEA Silver Dart at Baddeck, and the
  flying WWI replicas of the Great War Flying Museum. Every one says "replica"
  in `description` and none says it in `aliases`.
- **Excluded replicas:** the fibreglass Space Shuttle at Stanley Bridge, PEI
  (Aerial Visuals loc 4233) — it is a themed tourist prop, not an airframe or a
  real spacecraft.
- **Access types.** A gate guardian or plinth visible from a public road is
  `public`, including the CF-5 116746 at Denison Armoury (Toronto) and the
  CT-133/CT-134 on Keith Alder's front lawn at Picton (Aerial Visuals states
  they are visible from the road). `restricted` is used for the CF-104D inside
  the Canadian Forces College grounds, the Collège militaire royal de
  Saint-Jean CF-100, and the Norwood Tutor collection whose access Aerial
  Visuals itself flags as unknown. `appointment` for operating collections
  (Waterloo Warbirds, CHAA Tillsonburg, Tiger Boys, Edenvale, CALSM Markham,
  Canadian Aviation Museum Windsor, Vintage Wings, Musée de l'aérospatiale du
  Québec, Gananoque hangar).
- **Airworthy aircraft are recorded where they live** — CHAA Tillsonburg,
  Waterloo Warbirds, Vintage Wings, Great War Flying Museum — per the
  methodology rule that the database answers "where can I go and see it".
- **Military colleges.** RMC Kingston and Collège militaire royal de Saint-Jean
  are recorded here because Aerial Visuals treats them as locations distinct
  from CFB Kingston and CFB Saint-Jean. If the bases agent also captures them,
  these two are the likely collisions. CFB Saint-Jean itself (CF-100 18104,
  CT-133 133678 and 133133, CF-104D 104784), CFB North Bay (CF-101 101054
  marked 101067, CF-100 18500), CFB Borden, CFB Trenton, CFB Kingston, CFB
  Petawawa, CFB Bagotville, CFB Valcartier, CFB Montréal Longue-Pointe, CFB
  Gagetown and 5 Wing Goose Bay were left to the bases agent.
- **Blank fields left deliberately.** `year_built` is blank throughout — no
  build or delivery date was sourced for any airframe. `postal_code` is blank
  except where an address was published (Air Force Heritage Park C0B 2A0,
  Canadian War Museum, Canadian Museum of History). Coordinates are blank only
  for Spitfire Park, Essex, where no source gives a position. Several
  `tail_number` fields are blank rather than guessed: the Brantford Aztec, the
  Campbellford Beech 18 and Anson, the Markham Beech 18 and DC-4 cockpit, the
  Knowlton Fokker D.VII, the Saint John TBM, the Gatineau Bell 47, the second
  Cornwallis CT-133, the Goose Bay DC-3, and every replica.

---

## Excluded, and why

| Site | Reason |
|---|---|
| Ontario Science Centre, Toronto (Sopwith Pup replica) | museum closed to the public June 2024, not reopened |
| Stanley Bridge, PEI Space Shuttle replica | themed prop, not an airframe |
| Centennial College, Scarborough (Beech 18 1569) | Aerial Visuals states airframes stored indoors and out of public view during renovations |
| Barn Full of Parts / Kenneth Gamble, Dundas (10+ CT-133) | private dismantler's yard, no public access |
| Vince O'Connor collection, Uxbridge (Bolingbroke, Canso, Vampires, CT-133 fuselage, Battle, V-1) | private collection, no published public access; a strong lead if that changes |
| Huntingdon QC Lodestar | in the back yard of a private residence |
| Trois-Rivières Airport HS-748 C-GJVN; Peterborough Airport Beech 99s and DC-3; Ottawa International Airport Boeing 727s | stored or working civil airframes, not preserved displays; the Ottawa 727 at site A is a live fire-training hulk |
| Diamond Aircraft Katana, London; Kitchener–Waterloo airport Katana | mounted factory/airport signage aircraft with no serial recorded |
| International Test Pilots School, London (60+ aircraft) | working flight-test fleet, not a display collection |
| Northern Lights, Québec City (Hunters) | working fleet; Aerial Visuals flags that public visibility is unknown |
| Jackson Lake PBY, Saglek B-26, Goose Bay B-36 51-5729 and RB-45C, Kuujjuaq Avro York, Gander Sabena DC-4 crash site | remote wreck sites, not preserved displays; Aerial Visuals marks the Goose Bay ones as not accessible |
| Mount Hope Village Gateway CT-134 134222; Toronto CT-114 (loc 5804); Inglewood Gnat; Collingwood and Grand Valley Tiger Moths; Cochenour DC-3s; Gander Expeditor; Westmount/St-Hyacinthe Spitfire SL542 (reported sold to England); Bagotville-area Sabre XB816; London Soaring Society Swordfish HS517; Québec City Fairey Battle 1317 | all carry Aerial Visuals "NEED HELP" flags — existence, location or public visibility unconfirmed. Leads, not records |
| Goderich CT-133; Frankford CT-134 134206; Reece's Corners Harvard 2684 and Piper Apache C-FORM; Parry Sound Canso 11022; St. Anthony NL Canso C-FIZU; Brantford Canadian Military Heritage Museum (WWI replicas) | named by Skaarup with no coordinates and no second source; see Leads |
| Yarmouth NS park CT-133 133411 | Skaarup says the Cornwallis Silver Star was moved to a park in Yarmouth and is lying disassembled; no coordinates, no confirmation, and it would double-count the Cornwallis record |
| Project North Star Association, Rockcliffe | works on the North Star inside the Canada Aviation and Space Museum — belongs to that museum's record |

---

## Unresolved source conflicts (a human on site would settle these)

Ranked by how much damage the wrong answer does.

1. **RCAFA 441 Wing, Barrie (CT-133).** Aerial Visuals has 21100 on the plinth;
   Skaarup says the aircraft displayed beside the RCAFA building near Barrie was
   133669 wearing 21100 and **has moved to the Base Borden Military Museum**. If
   Skaarup is right this site is empty and the airframe belongs to the bases
   agent. Recorded here with the conflict in the description.
2. **Air Force Heritage Park, Summerside (CF-101 101037).** Aerial Visuals and
   rwrwalker both place it there; Skaarup's PEI page says "This aircraft has
   been scrapped". Recorded as present, with the conflict stated.
3. **Hamilton Air Force Association Club, Dundas (CT-133).** Aerial Visuals
   21123; Skaarup 133110 with IA number A661. These are different airframes.
   Recorded as 21123, conflict stated. Someone needs to read the data plate.
4. **CF-100 100760.** Aerial Visuals and Wikipedia put it in storage at the
   Canadian War Museum (previously CFB Saint-Hubert); Skaarup lists it with the
   Musée de l'aérospatiale du Québec at Saint-Hubert. Recorded at the War
   Museum as `in_storage`.
5. **CF-100 18619, Malton.** Wikipedia and Aerial Visuals both have it in Paul
   Coffey Park (formerly Wildwood Park) beside RCAFA 528 Wing; Skaarup says it
   is now at the Canadian Air Land and Sea Museum. Recorded at Malton.
6. **CT-133 133581.** Aerial Visuals: Barrie Paintball at Angus. Skaarup: the
   Canadian Air and Space Conservancy at Edenvale. Recorded at Angus.
7. **CT-134 134206.** Aerial Visuals: Campbellford Memorial Military Museum
   site B. Skaarup: Frankford. Recorded at Campbellford.
8. **CT-133 133411, Cornwallis.** Skaarup says moved to Yarmouth and
   disassembled; Aerial Visuals still shows it pole-mounted at Clementsport.
   Recorded at Cornwallis with the doubt stated.
9. **CT-133 133389, Pictou.** Skaarup says taken down from its pylon and
   awaiting preservation. Recorded `on_display` because it is still in the
   Veterans Memorial Park, but a visitor may find it on the ground.
10. **Yale 3416.** Aerial Visuals attaches the same airframe both to the 6 SFTS
    Society at Dunnville and to the Tiger Boys at Guelph Airpark; Skaarup lists
    it at both too. Recorded at Dunnville, noted at Guelph.
11. **Fleet 80 Canuck C-FDPV** is listed by Aerial Visuals at both Edenvale and
    Vintage Wings. Recorded at Edenvale, noted.
12. **Sabre 23314 (Hawk One)** — Skaarup says the Vintage Wings aircraft has
    been sold. Recorded at Gatineau with the doubt stated.

---

## Leads for other agents

- **The Wayback Machine holds the complete original `rwrwalker.ca`** — 333
  `.html` pages, best capture `20211025221528`, fetched as
  `https://web.archive.org/web/20211025221528id_/http://www.rwrwalker.ca/<page>`.
  Key pages for plinth work: `caf_canucks.html`, `RCAF_Voodoos.html`,
  `CF_104700_104771_detailed.html` / `CF_104772_104832` / `CF_104833_104900`,
  `RCAF_CF104D_detailed.html`, `RCAF_18101_18150` … `RCAF_18751_18792` (CF-100),
  `RCAF_19101_19400` and the 23xxx blocks (Sabre), `list_by_type.html`.
  web.archive.org resets connections often from this environment; retry.
- **`caspir.warplane.com`** (Canadian Warplane Heritage's CASPIR database) is
  where rwrwalker's serial data appears to have migrated. It has a per-serial
  search (`/aircraft/serial-search/aircraft-no/<id>`) and was not exploited
  here. It is the most promising replacement spine for the whole Canada effort.
- **`silverhawkauthor.com` has a per-province and per-type page for every
  province and every Canadian type.** Sitemap at `/post-sitemap{,2,3}.xml`,
  2,449 posts. Western-provinces and bases agents should use
  `canadian-warplanes-N-<province>` and the museum-specific pages
  (`…-cfb-borden-base-borden-military-museum`,
  `…-cfb-trenton-national-air-force-museum-of-canada`,
  `…-markham-canadian-air-land-sea-museum-calsm`, etc.). Content is far richer
  than Wikipedia for Canada.
- **Aerial Visuals Locator is queryable by POST**:
  `Continent=North America&Country=Canada&Region=<province>&Scope=1&ShowMap=0`
  to `Locator.php`, then `LocationDossier.php?Serial=<id>` per site for
  coordinates and airframe serials. Rate-limit to about one request every five
  seconds.
- **For the bases agent, from Aerial Visuals and Skaarup:** CFB North Bay holds
  CF-101 101054 marked 101067 (black), CF-100 18500, and a CT-133; CFB
  Mountain View / ATESS holds CF-100 18434, CT-133 133656 and CF-101 101047 in
  storage; CFB Saint-Jean holds CF-100 18104 (IA A611), CT-133 133678 and
  133133 (marked 133333) and CF-104D 104784; Valcartier holds Sabre Mk 2 19118
  marked 19430, CF-104 104774 and CH-136 136205; Gagetown holds CF-100 18773,
  CF-101 101046, CH-136 136216 and the wreck of Sabre 23292; Connaught
  Range/Shirleys Bay holds CT-133 133606, CF-5D 116834 and CH-136 136203;
  Petawawa holds CC-129 Dakota 12924 marked KG455 and CH-136 136207;
  CFB Montréal Longue-Pointe holds CF-5D 116809; St-Hubert garrison holds
  CH-136 136211.
- **Quebec leads not run down:** Frontiers Military Aviation Museum / Musée de
  l'aviation militaire des frontières at Saint-Jean-Chrysostome (Beech D18S
  C-FDWS, DC-3 CF-FST parts, a Norseman) — no coordinates found and it is not
  in the Aerial Visuals Locator at all.
- **Newfoundland transatlantic memorials:** only two include an airframe — the
  Botwood Flying Boat Museum Canso and the Spirit of Harbour Grace DC-3, both
  recorded. Lester's Field in St John's (Alcock and Brown, 1919) and the Harbour
  Grace Amelia Earhart site have monuments but no aircraft.

---

## File and row counts

| file | rows | with serial |
|---|---|---|
| `air_force_heritage_park_summerside_aircraft.csv` | 4 | 4 |
| `alexander_graham_bell_national_historic_site_baddeck_aircraft.csv` | 1 | 0 |
| `barrie_paintball_silver_star_angus_aircraft.csv` | 1 | 1 |
| `bell_textron_canada_bell_430_mirabel_aircraft.csv` | 1 | 0 |
| `botwood_flying_boat_museum_aircraft.csv` | 1 | 1 |
| `brantford_trading_post_aztec_aircraft.csv` | 1 | 0 |
| `brome_county_historical_society_museum_knowlton_aircraft.csv` | 1 | 0 |
| `canadian_air_land_and_sea_museum_markham_aircraft.csv` | 16 | 14 |
| `canadian_aviation_museum_windsor_aircraft.csv` | 9 | 8 |
| `canadian_forces_college_starfighter_toronto_aircraft.csv` | 1 | 1 |
| `canadian_harvard_aircraft_association_tillsonburg_aircraft.csv` | 13 | 13 |
| `canadian_museum_of_history_aircraft.csv` | 1 | 0 |
| `canadian_war_museum_aircraft.csv` | 6 | 4 |
| `centennial_park_canuck_moncton_aircraft.csv` | 1 | 1 |
| `central_new_brunswick_woodmen_s_museum_boiestown_aircraft.csv` | 1 | 1 |
| `college_militaire_royal_de_saint_jean_canuck_aircraft.csv` | 1 | 1 |
| `cornwallis_military_museum_clementsport_aircraft.csv` | 2 | 1 |
| `denison_armoury_freedom_fighter_toronto_aircraft.csv` | 1 | 1 |
| `desperate_dick_s_and_durty_nellie_s_seabee_sioux_lookout_aircraft.csv` | 1 | 0 |
| `duncan_mcdonald_memorial_community_gardens_sabre_trenton_aircraft.csv` | 1 | 1 |
| `dunnville_public_library_harvard_memorial_aircraft.csv` | 1 | 1 |
| `ear_falls_district_museum_aircraft.csv` | 1 | 1 |
| `edenvale_classic_aircraft_foundation_aircraft.csv` | 5 | 2 |
| `gananoque_airport_canso_aircraft.csv` | 1 | 1 |
| `germain_park_sabre_sarnia_aircraft.csv` | 1 | 1 |
| `glen_miller_drive_freedom_fighter_trenton_aircraft.csv` | 1 | 1 |
| `goose_bay_airport_vulcan_aircraft.csv` | 2 | 1 |
| `great_war_flying_museum_caledon_aircraft.csv` | 6 | 0 |
| `hamilton_air_force_association_club_silver_star_dundas_aircraft.csv` | 1 | 1 |
| `happy_valley_goose_bay_town_hall_shooting_star_aircraft.csv` | 1 | 1 |
| `ignace_expeditor_memorial_aircraft.csv` | 1 | 1 |
| `jackson_park_spitfire_and_hurricane_windsor_aircraft.csv` | 2 | 0 |
| `keith_alder_aircraft_display_picton_aircraft.csv` | 2 | 2 |
| `lee_park_canuck_north_bay_aircraft.csv` | 1 | 1 |
| `london_international_airport_silver_star_aircraft.csv` | 1 | 1 |
| `mark_s_stereo_musketeer_brockville_aircraft.csv` | 1 | 1 |
| `memorial_military_museum_campbellford_aircraft.csv` | 17 | 15 |
| `miramichi_airport_voodoo_aircraft.csv` | 1 | 1 |
| `morrison_s_quarry_beech_18_wakefield_aircraft.csv` | 1 | 0 |
| `mountain_hyundai_nessa_iv_hamilton_aircraft.csv` | 1 | 0 |
| `musee_de_l_aerospatiale_du_quebec_saint_hubert_aircraft.csv` | 4 | 3 |
| `nav_canada_training_centre_silver_star_cornwall_aircraft.csv` | 1 | 1 |
| `new_brunswick_museum_saint_john_aircraft.csv` | 1 | 0 |
| `no_6_rcaf_dunnville_museum_aircraft.csv` | 2 | 2 |
| `norseman_heritage_park_red_lake_aircraft.csv` | 1 | 1 |
| `northland_aircraft_service_norseman_ignace_aircraft.csv` | 1 | 1 |
| `norwood_tutor_collection_aircraft.csv` | 8 | 8 |
| `parc_commemoratif_des_veterans_voodoo_levis_aircraft.csv` | 1 | 1 |
| `paul_coffey_park_canuck_malton_aircraft.csv` | 1 | 1 |
| `pinery_antique_flea_market_silver_star_grand_bend_aircraft.csv` | 1 | 1 |
| `rcafa_416_wing_harvard_kingston_aircraft.csv` | 1 | 1 |
| `rcafa_420_wing_sabre_oshawa_aircraft.csv` | 1 | 1 |
| `rcafa_424_wing_silver_star_cornwall_aircraft.csv` | 1 | 1 |
| `rcafa_426_wing_sabre_brockville_aircraft.csv` | 1 | 1 |
| `rcafa_441_wing_silver_star_barrie_aircraft.csv` | 1 | 1 |
| `riverview_park_and_zoo_sabre_peterborough_aircraft.csv` | 1 | 1 |
| `royal_canadian_legion_branch_129_canuck_haliburton_aircraft.csv` | 1 | 1 |
| `royal_canadian_legion_branch_197_silver_star_acton_aircraft.csv` | 1 | 1 |
| `royal_canadian_legion_branch_397_silver_star_creemore_aircraft.csv` | 1 | 1 |
| `royal_canadian_legion_branch_63_silver_star_collingwood_aircraft.csv` | 1 | 1 |
| `royal_military_college_of_canada_kingston_aircraft.csv` | 2 | 2 |
| `rusty_myers_flying_services_fort_frances_aircraft.csv` | 2 | 1 |
| `salem_and_hillsborough_railroad_preservation_park_voodoo_aircraft.csv` | 1 | 1 |
| `spirit_of_harbour_grace_dakota_aircraft.csv` | 1 | 1 |
| `spitfire_park_essex_aircraft.csv` | 1 | 0 |
| `stephenville_airport_delta_dagger_aircraft.csv` | 1 | 1 |
| `sugar_bowl_park_silver_star_fort_erie_aircraft.csv` | 1 | 1 |
| `thetford_mines_airport_voodoo_aircraft.csv` | 1 | 1 |
| `tiger_boys_aeroplane_works_and_flying_museum_aircraft.csv` | 14 | 6 |
| `val_d_or_regional_airport_dakota_aircraft.csv` | 1 | 1 |
| `val_d_or_service_culturel_silver_star_aircraft.csv` | 1 | 1 |
| `veterans_memorial_park_silver_star_pictou_aircraft.csv` | 1 | 1 |
| `victoria_park_harvard_rcafa_442_wing_smiths_falls_aircraft.csv` | 1 | 1 |
| `vintage_wings_of_canada_aircraft.csv` | 25 | 21 |
| `waterloo_warbirds_kitchener_aircraft.csv` | 6 | 5 |
| `zurakowski_park_barry_s_bay_aircraft.csv` | 1 | 0 |
| `zwick_s_island_park_sabre_belleville_aircraft.csv` | 1 | 1 |
| **total** | **204** | **158** |

- Ontario: 52 sites
- Quebec: 11 sites
- New Brunswick: 5 sites
- Newfoundland and Labrador: 5 sites
- Nova Scotia: 3 sites
- Prince Edward Island: 1 sites

Serial coverage: 158 of 204 aircraft rows carry a tail number (77%). The uncovered rows are replicas, unidentified airframes at multi-aircraft sites, and airframes no source names.
