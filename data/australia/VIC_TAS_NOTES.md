# Victoria and Tasmania — research notes

Area: Victoria (VIC) and Tasmania (TAS). Compiled September 2026 against the
`SPEC_ANZ.md` rules. 25 sites, 250 aircraft rows.

---

## 1. Sources used, and how each behaved

| Source | Use | Staleness found |
|---|---|---|
| **adf-serials.com.au** | Primary identity + current-holder check for every ADF airframe. Both the new Joomla tree (`/raaf2/…`, `/raaf3/…`, `/ran/…`) and the surviving legacy pages (`/2a79.htm`, `/2a84a.htm`, `/2a85.htm`, `/2a68a.htm`, `/2a77.htm`, `/2a52.htm`) were scraped and parsed. | Mostly current, but several "currently…" lines are 10-20 years old (see corrections below). Note that the site migration has **lost** several type pages: A20 Wirraway, A17 Tiger Moth and A94 Sabre exist only on the new tree; A79 Vampire, A84 Canberra, A77 Meteor, A85 Winjeel, A68 Mustang, A52 Mosquito, A58 Spitfire, A65 Dakota exist only as legacy `.htm`. Neither tree is complete on its own. |
| **Museum collection pages** | `aarg.com.au/ourcollection.html` (ANAM) is the single best current list in the area — it gives location *and* restoration status per airframe, including aircraft on loan out. `nhillaviationheritagecentre.com.au`, `benallaaviationmuseum.org.au`, `ballarataviationmuseum.com.au`, `b24australia.org.au`, `flyingboat.org.au`, `ansettmuseum.com.au`, `scottsdalemilitarymuseum.org.au`, `tahs.org.au`, `rslmuseummildura.com.au`. | Benalla, Ballarat, Mildura and Gippsland publish **no serial-level list at all** — their own sites are prose only. |
| **airforce.gov.au** | RAAF Museum visiting terms; No 100 Squadron heritage fleet page. | The old per-aircraft museum exhibit pages (`/raafmuseum/exhibitions/…`) are dead; only web.archive copies survive, which is what Wikipedia cites. The site blocks plain `curl` (HTTP/2 INTERNAL_ERROR) and `robots.txt` blocks some paths. |
| **aviationmuseum.eu** | Leads and roster cross-checks only, per spec. | Its Australia index was last updated **2 Nov 2016** and shows it. Several of its per-museum rosters are demonstrably wrong (below). |
| **Wikipedia survivor lists** | Leads: `List of preserved Bell UH-1 Iroquois`, `List of surviving de Havilland Vampires`, `List of displayed McDonnell Douglas F-4 Phantom IIs`, `CAC Wirraway`. | Good for finding sites; serials cross-checked against adf-serials before use. |
| **thisisflight.net / psnews.com.au** | The January 2026 No 100 Squadron divestment announcement. | Current. |
| **Nominatim / OpenStreetMap** | Mapped coordinates. | Several sites are not in OSM; coordinates left blank rather than guessed. |
| **Grokipedia** | **Not used** (appeared in one search result list for the Derelict Aircraft Museum and was discarded per spec). |

---

## 2. The two questions the brief asked directly

### 2a. Has any of the Temora Aviation Museum collection moved to Point Cook?
**No.** The Temora collection was gifted to the Commonwealth in 2019 and is flown
by No 100 Squadron (Air Force Heritage Squadron), which operates from **two**
locations — RAAF Base Point Cook and Temora. On **15 January 2026** Air Force
announced the retirement of eight aircraft from the heritage fleet
(Vampire T.35, Meteor F.8, A-37B Dragonfly, Ryan STM-S2, Canberra TT.18,
CA-27 Sabre Mk 31, CT/4A Airtrainer, and the R.E.8 replica). Five of those stay
at **Temora** on permanent static display and three were to be "considered for
static display at approved institutions". The still-flying fleet after that
announcement is:

* **Point Cook-based:** Tiger Moth, CA-25 Winjeel, CA-18 Mustang Mk 23, Sopwith Pup.
* **Temora-based:** Hudson Mk III, Spitfire Mk VIII, Spitfire Mk XVI, CA-13
  Boomerang, CA-3 Wirraway, Tiger Moth.

So nothing crossed the border into Victoria. The Temora airframes belong in the
NSW file. **Open item:** the three aircraft "considered for approved
institutions" had not been publicly allocated at the time of writing — if any of
them land in Victoria (Point Cook, Moorabbin or Benalla are the plausible
recipients) this file will need revising.

### 2b. Which Point Cook aircraft are airworthy vs static?
Recorded as museum records with the airworthy status in `description`, per spec:

* **A68-170** CA-18 Mustang Mk 23 (VH-SVU) — airworthy, heritage flight.
* **A85-439** CA-25 Winjeel (VH-FTS) — airworthy, heritage flight.
* **Sopwith Pup** replica (marked D4170) — airworthy, heritage flight.
* A **Tiger Moth** is airworthy in the Point Cook heritage flight; the museum
  holds A17-692 and A17-711 and the sources do not say which of the two flies,
  so neither row asserts it. A17-692 is the more likely (acquired 2005).
* **A79-636** Vampire T.35 was the RAAF Historic Flight aircraft and is recorded
  `in_storage` — adf-serials states it is grounded with the wings out of fatigue
  life.

Everything else at Point Cook is static, stored or under restoration.

---

## 3. Corrections made, with evidence

1. **Sabre at Moorabbin is A94-910, not A94-989.** aviationmuseum.eu and older
   adf-serials text put A94-989 on display at ANAM. adf-serials A94-910 now
   records: Point Cook store → RAAF Wagga 16 Oct 2014 → "05/2018 a change of plan
   has seen it gifted to ANAM Moorabbin", and ANAM's own 2023 collection list
   shows **CAC CA-27 Sabre A94-910, Moorabbin, On Display**. The A94-989 forward
   fuselage left Moorabbin and is now part of the composite **A94-906** displayed
   at Mildura (adf-serials, restoration finished 25 May 2025).
2. **Gippsland Armed Forces Museum no longer has its Tracker.** aviationmuseum.eu
   still lists S-2G N12-153566. adf-serials: sold to United Aeronautical
   Corporation Feb 2016, dismantled for export Sept 2016. Excluded.
3. **Bandiana no longer has Vampire A79-804.** aviationmuseum.eu lists it;
   adf-serials ends "Currently at RAAF Heritage Centre, Townsville". Excluded.
4. **Mirage A3-51 is not at Point Cook.** Older text said RAAF Museum;
   adf-serials now records it "transported by road to RAAF Wagga arriving
   19/09/2018". Excluded from the Point Cook file (belongs to NSW).
5. **Point Cook's Wirraway is A20-687, not A20-561.** Both adf-serials and the
   Wikipedia Wirraway survivors list state the airframe is A20-687 painted as
   A20-561; the real A20-561 was converted to components in 1946. Recorded with
   `tail_number` A20-687 and the false marking in aliases + description.
6. **Ballarat's Wirraway is A20-511 painted as A20-502** (adf-serials, both the
   A20-502 and A20-511 entries). The real A20-502 was destroyed at Piva in 1946.
7. **RAAF Museum F-4E is 67-0237, not 69-7208.** aviationmuseum.eu gives
   69-7208; Wikipedia's F-4 display list and JetPhotos both give 67-0237 for the
   Point Cook aircraft. Used 67-0237.
8. **Vampire A79-840 is no longer in the Derelict Aircraft Museum collection**
   (adf-serials: "Sold 05/2016 Currently owned by Steven Demanuele"). Removed
   from that site, which several web lists still show.
9. **Nhill's aviationmuseum.eu roster is column-scrambled.** It renders as
   "Avro Anson I – W2364, A20-722 / CAC CA-1 Wirraway – VH-RIN/A17-588 /
   Tiger Moth – VH-UPR / Desoutter II". Cross-checked against the Wikipedia
   Wirraway list (A20-722 static at Nhill) and ANAM's own list (Desoutter
   **VH-UPR** on loan to Nhill), the correct mapping is Anson **W2364**,
   Wirraway **A20-722**, Tiger Moth **A17-588 / VH-RIN**, Desoutter **VH-UPR**.
10. **ANAM's list writes the Benalla Jindivik as "A94-492".** A94 is the Sabre
    series; adf-serials has it under A92 as **A92-492** ("Owned by Moorabbin Air
    Museum. Was on display at Wangaratta"). Recorded as A92-492 with the ANAM
    typo explained in `description`.
11. **The Canberra at the National Vietnam Veterans Museum is A84-307**, an
    English Electric-built B.2 and the world's oldest surviving Canberra, not one
    of the GAF Mk 20s. It is under restoration inside the new display hangar.

---

## 4. Judgment calls

* **Replicas.** Flagged in `description`, never in aliases: RAAF Museum's Bristol
  Boxkite, Deperdussin 1910, B.E.2, Sopwith Pup, and — on adf-serials' explicit
  statement that Mustang A68-199 was traded in 1998 "for two World War One
  replicas (Avro 504K and SE5a) that are currently displayed at Point Cook" —
  the Avro 504K E3747 and S.E.5a A2-31. The Maurice Farman Shorthorn CFS-20 is
  *not* flagged: no source I found states whether it is original or a
  reproduction, so the row says the status is not established rather than
  guessing. Also flagged: AGM's Taylor Glider and WWS Salamandra, and the
  Lilienthal reproduction.
* **Airworthy museum aircraft recorded.** Point Cook's heritage flight aircraft
  (above), Benalla's Winjeel VH-CZE and Moth Minor VH-CZB (privately owned by
  Mark Carr but operated in conjunction with, and based at, the museum), Nhill's
  Tiger Moth VH-RIN (privately owned, on display at the centre), and Cressy's
  Tiger Moth "Millie". All `on_display` with the airworthy note in prose.
* **Access types.** RAAF Museum = `public` per spec, even though bookings are now
  essential and photo ID is required for over-16s. RAAF Base East Sale =
  `restricted`: two of its four airframes (the A7-081 Macchi and A85-405 Winjeel
  gate guards) sit at the main gate and the A23-036 PC-9 beside them, but
  A23-030 is on the parade ground inside the wire and the base is not open
  access. Avalon Airport and DSTG Fishermans Bend = `restricted` (airside /
  Defence site). Derelict Aircraft Museum and Cressy = `appointment`. Army Museum
  Bandiana = `public`: it sits inside Gaza Ridge Barracks but its own site
  advertises Wed-Sun 0900-1500 walk-in hours; one secondary source says 24-hour
  booking is required, so this may deserve `appointment`.
* **Link Trainers and simulators excluded** — ANAM's Ansett Link Trainer and
  A13-89, the DC-9 simulator, and Nhill's two Link Trainers are ground trainers,
  not airframes.
* **Section-only relics excluded** as not being airframes, but listed here so the
  next pass does not chase them: F-111C fin and rudder A8-114 at Simpson
  Barracks Watsonia (VIC), A8-146 at Cranbourne RSL (VIC), **A8-140 at South Arm
  RSL (TAS)**; Iroquois A2-382's port fuselage section in the Point Cook Vietnam
  display; Macchi forward fuselages A7-070 and A7-097 at Point Cook; Sabre
  A94-989's rear fuselage and A94-950's wreckage at Gippsland Armed Forces
  Museum; Canberra A84-222's stripped cockpit. Exceptions made where the section
  *is* the exhibit: F-111C crew module A8-131 (ANAM), Canberra A84-234 nose
  (Point Cook), Beaufort cockpit A9-164 (Gippsland), Heron VH-CLZ forward
  fuselage (QVMAG), Iskra cockpit (Ballarat).

---

## 5. Sites examined and excluded, with reasons

* **Drage's Airworld, Wangaratta** — closed c. 2002-03 and the collection was
  dispersed (Mirage A3-42, Vampire A85-402, Wirraway A20-653, Sioux A1-402,
  Hudsons A16-105/A16-112, Jindivik A92-492 all have post-Airworld dispositions
  in adf-serials). There is **no aviation museum at Wangaratta today**.
* **Latrobe Flying Museum, Traralgon** — Wikipedia: "As of 2017 this museum is
  closed and non-functional." Jeff Trappett's airframes at Latrobe Valley
  (Sabre A94-352 airworthy, Sabre A94-907, Vampire A79-659 under restoration,
  Dakota A65-72/VH-AGU) are a private collection, excluded per the spec's
  "privately owned warbird merely hangared at the field" rule.
* **The Old Aeroplane Company, Tyabb** — Judy Pay's private warbird collection
  and maintenance business (P-40, P-51, T-28, Harvard, two Vampires incl. ex-SAAF
  R1835, Storch, Cub). Open essentially only on Tyabb airshow days. Excluded on
  the same rule; **this is the most arguable exclusion in the file** — if the
  database wants private-collection sites, Tyabb is the biggest one in Victoria.
  Boomerang A46-249 is also being restored to airworthy there.
* **Airways Museum / Civil Aviation Historical Society, Essendon Fields** — a
  first-rate civil-aviation collection but its own About page says flatly
  "there are no aircraft!". Excluded; no airframe.
* **Shrine of Remembrance, Melbourne** — no aircraft in the collection.
* **Scienceworks / Melbourne Museum (Museums Victoria)** — Museums Victoria owns
  the original 1910 **Duigan pusher biplane**, a 1995 Duigan replica, and
  **Wirraway A20-651**, but its own collection records state each is
  "Currently in storage" and not exhibited at any Museums Victoria venue. No
  site record created; revisit if the Duigan returns to display.
* **RAAF Williams – Laverton** — no confirmed surviving display airframe.
  Sabre A94-941 (ex-DSTO gate guard) was last reported in a back lot at Fowles
  Auctions, Laverton North — a wrecking/auction yard, not a display. Vampire
  A79-165 outside the Fleetwings service station at Laverton is a 1970s report.
* **RAAF Williams – Point Cook (outside the museum)** — the pole-mounted Vampire
  A79-175 that once stood outside the base was swapped away by the museum in the
  1990s and is now dismantled at Parkes, NSW.
* **Mitiamo Air Museum** — adf-serials places only the *fuselage* of Macchi
  A7-024 there and the entry is undated; could not confirm the museum still
  exists. Not recorded.
* **Puckapunyal (Army Tank Museum)**, Fort Queenscliff, HMAS Castlemaine, HMAS
  Cerberus museum, Running Rabbits (Upwey), Light Horse Museum (Nar Nar Goon),
  Red Cliffs Military Museum, Soldiers Memorial Institute (Bendigo),
  Mallacoota Bunker, Chanter Estate (Moama, NSW side) — military museums with no
  aircraft.
* **"Australian Aviation Heritage Centre"** (in the seed list) is in **Winnellie,
  Darwin, NT** — not this area. There is no Victorian site of that name; the
  Caboolture organisation of a similar name is in Queensland.
* **Clyde North Aeronautical Preservation Group** has relocated to Albury, NSW.
* **Hallam, VIC** — ANAM lists Jindivik **N11-743** and a Lycoming ALF-502 on
  loan at "Hallam". No public site identified; airframe not assigned to any
  record. Open question below.
* **Tasmania**: no aviation museum exists in the state (confirmed by the
  Country Airstrips Australia national museum directory, which lists none for
  TAS). Airframes are scattered: Launceston Airport terminal, Scottsdale RSL,
  QVMAG storage, plus a DH.114 Heron fuselage **VH-CLT on private property at
  Woodbury** (private, excluded) and the South Arm RSL F-111 fin.

---

## 6. Fields deliberately left blank

* **`year_built` is blank on every row.** No construction, roll-out, first-flight
  or delivery date was sourced to the standard the spec requires. adf-serials
  gives delivery dates for many airframes but they are stated as service
  receipt dates, and conflating those with build year would be a guess.
* **`tail_number` blank** where identity is genuinely unresolved: the Bandiana
  Caribou (A4-134 per adf-serials vs A4-264 per aviationmuseum.eu — see
  `description`), the RAAF Museum Cessna O-1 (wears "0-14591", true identity not
  established), NVVM's AH-1 Cobra, both Bloodhound missiles, ANAM's mock-ups and
  several homebuilts, Ballarat's Dove/gyroplane/Flying Flea, the B-24 group's
  Oxford and Anson, and Cressy's Tiger Moth.
* **`latitude`/`longitude` blank** for Cranbourne RSL, the Derelict Aircraft
  Museum (Kamarooka — only a locality centroid was available, which is not the
  site), and DSTG Fishermans Bend. Everything else is a Nominatim/OSM mapped
  position or a published Wikipedia coordinate.
* **`address`/`website` blank** where nothing authoritative was found
  (Cranbourne RSL, Kamarooka, Braybrook, Seymour, DSTG).

---

## 7. Confidence, weakest first

1. **Australian Gliding Museum (61 rows)** — the museum's own site publishes no
   roster; the registrations come from the aviationmuseum.eu museum listing and
   have **not** been individually re-verified, which every row's `description`
   says. The museum's own site says "over thirty gliders" while that roster has
   ~61 entries, so some may be stored off-site or since disposed. This is the
   single largest block of second-tier data in the file and the first thing to
   re-do from Victorian Collections or a site visit.
2. **Derelict Aircraft Museum, Kamarooka (3 rows)** — Dick Winterburn's private
   collection moved Heathcote → Launching Place → Yalca → (per its own Facebook
   page) Kamarooka. adf-serials' per-airframe entries stop at Yalca. Presence of
   A7-023, A7-031 and N7-212 at Kamarooka is inferred, and said so in prose.
   The Wikipedia article on the museum describes it as closed and dismantled
   prior to 2017 at Launching Place, which conflicts with the active Facebook
   page — unresolved.
3. **Ballarat Aviation Museum (7 rows)** — only the Wirraway has a serial. The
   rest are typed from the museum's own prose description with blank identities.
4. **Sir Reginald Ansett Transport Museum (1 row)** — the museum says "a Fokker
   Universal aircraft, **similar to** the one used on the first Ansett flight",
   which reads like a replica, but it does not say so; aviationmuseum.eu records
   the registration VH-UTO. Recorded with the ambiguity stated. The same museum's
   blog mentions "an Ansett DC3" — not recorded, could not confirm it is an
   airframe on site.
5. **Benalla Vampires** — A79-819 and A79-835 are both at Benalla and, per
   adf-serials, the composite is displayed *as* A79-819 while A79-835 is *also*
   marked A79-819. Two rows recorded with the entanglement explained.
   aviationmuseum.eu's "A79-815" appears to be a typo for A79-819.
6. **RAAF Museum store list** — the storage rows (Avro 707A, Meteors, Neptune,
   Ventura, Harvard, S-51, Mosquito, Dakota, F-111C A8-125, Sabres A94-960 and
   A94-982, Mirage A3-72, Chinook A15-106, Auster A11-17) rest on adf-serials
   plus the archived Wikipedia list; the museum publishes no store inventory and
   these are by definition not visible to a visitor.

---

## 8. Open questions, ranked

1. **Where did the three divested No 100 Squadron aircraft go?** The January 2026
   announcement said the CA-27 Sabre Mk 31, CT/4A and R.E.8 replica would be
   "considered for static display at approved institutions" while the Meteor,
   Vampire, Ryan STM-S2, A-37B and Canberra TT.18 stay at Temora. If any of the
   three came to Victoria, this dataset is missing them.
2. **Mirage A3-44** was "allocated to Benalla Aviation Museum 02/2019" but
   adf-serials adds "As of 31/10/2019 it is still sitting in the open at
   Bankstown". Not recorded at Benalla. Did the move ever happen?
3. **The Dandenong RSL Macchis.** adf-serials records A7-002, A7-075, A7-087 and
   parts of A7-011/A7-041/A7-048/A7-059/A7-066/A7-083/A7-089 as acquired by
   Dandenong RSL for a planned formation-on-poles display, stored at the
   Dandenong Army depot, with A7-075 and the rear fuselages of A7-069 and A7-080
   "arrived Moorabbin Air Museum 06/2022?" (adf-serials' own question mark).
   ANAM's 2023 list does not show A7-075. Only the Iroquois A2-767 is recorded at
   Dandenong RSL. What is actually standing there in 2026, and did A7-075 reach
   Moorabbin?
4. **The Bandiana Caribou identity** — A4-134 or A4-264? Neither source is
   conclusive and adf-serials' A4-134 entry admits it has "not been sighted for
   quite a while".
5. **Which Point Cook Tiger Moth flies**, A17-692 or A17-711?
6. **Is the RAAF Museum's Avro 504K / S.E.5a replica claim right?** adf-serials
   states it in the A68-199 Mustang entry; the museum has always presented these
   as exhibits without qualification. Worth confirming from the museum.
7. **Jindivik N11-743 at "Hallam"** (ANAM loan) — what site is that, and is it
   publicly visible?
8. **RMIT Bundoora** — adf-serials' A19-036 entry says the CT/4 at RMIT Bundoora
   was "Replaced at Bundoora by Pilatus PC-9A A23-056", but the A23-056 entry
   itself shows no Bundoora disposition. If a PC-9 is on that campus it is a
   site record. Not created for want of confirmation.
9. **Mildura's Vampire** — three truckloads of Vampire T.35A parts were donated
   by the RAAF to the Mildura RSL in October 2025 and are being assembled by the
   **Dareton Men's Shed in NSW**, to be displayed with Sabre A94-906 at Mildura
   once the hangar is extended. Not yet a Victorian airframe; recheck in a year.
10. **Regional towns swept with no result.** Shepparton, Echuca, Warrnambool,
    Bairnsdale, Mangalore, Horsham, Swan Hill, Portland, Colac, Yarrawonga and
    Cobram produced no confirmed preserved airframe in adf-serials or in any
    museum/heritage listing. Absence of evidence only — a targeted RSL-by-RSL
    sweep with dated photography would be the way to close this out, and the
    Victorian RSL plinth population found here (Dandenong, Cranbourne,
    Braybrook, Seymour) suggests there are more.
11. **Tasmania is thin and probably under-counted.** Four airframes plus one
    F-111 fin for the whole state. Hobart in particular returned nothing —
    Cambridge Aerodrome and the Tasmanian Transport Museum were not able to be
    checked in detail before the search budget ran out.
