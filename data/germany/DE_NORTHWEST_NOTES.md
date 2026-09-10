# DE_NORTHWEST — Schleswig-Holstein, Hamburg, Bremen, Niedersachsen, Nordrhein-Westfalen

Research pass for airplane.museum, September 2026. Output directory
`/home/claude/de/northwest/`. Museums file `de_museums.csv`, one
`<slug>_aircraft.csv` per site.

Assigned exclusions honoured: **Luftfahrtmuseum Laatzen-Hannover** and
**Hubschraubermuseum Bückeburg** are not recorded here (another agent has
them). Also outside the five Länder and therefore not recorded:
Militärhistorisches Museum Flugplatz Berlin-Gatow, Internationales
Luftfahrtmuseum Schwenningen, Flugausstellung Hermeskeil, Hangar 10
Heringsdorf, Segelflugmuseum Wasserkuppe, Otto-Lilienthal-Museum Anklam,
Fliegerhorst Büchel (Rheinland-Pfalz, not Nordrhein-Westfalen as the
assignment brief grouped it).

---

## Sources and how much weight each carried

1. **Museums' own websites** — used first wherever one existed and said
   anything concrete: `aeronauticum.de` (the Arado Ar 196 provenance and
   restoration status), `ju52-halle.de` (exhibit list, opening hours, the
   fact the museum sits in the western, non-secure part of Fliegerhorst
   Wunstorf), `luftbrueckenmuseum.de`, `bremen-airport.com` (Bremenhalle),
   `laarbruch-museum.net`, `quax-flieger.de` (full club fleet with
   registrations and Werknummern), `fliegerhorst-oldenburg.de`,
   `westfalengeschwader.com`, `damme.de` (Transall viewing arrangements),
   `edxq.de` (Rotenburg Transall). These win on "what is here now" and on
   opening arrangements.
2. **SpotterMania (`spottermania.com`)** — the single most productive
   source for this region. Its per-airfield and per-museum pages carry an
   explicit *PRESERVED* / *WITHDRAWN FROM USE* split with Bundeswehr code,
   construction number, operator, and flags for gate guardians, ground
   instructional airframes, fuselage-/cabin-only survivors and false
   markings. The site's sitemap is dated August 2026, so it is current.
   **Almost every base gate-guard record here comes from it.** Its museum
   pages also gave the street addresses used in `de_museums.csv`.
   Weakness: it duplicates a small number of airframes across two pages
   (see *Conflicts* below), so it should not be trusted blind on location.
3. **International F-104 Society (`i-f-s.nl`), "Preserved in Germany"** —
   the authoritative Starfighter survivor list; it supplied every
   plinth/monument Starfighter recorded here that no other source
   mentions. It is undated, so those five monument records are marked in
   `description` as not re-confirmed by a dated photograph.
4. **`aviationmuseum.eu`** — used as a cross-check on Gütersloh, Oldenburg,
   Varel and Bad Oeynhausen. Its Germany index is useful for *finding*
   sites but its aircraft lists lag: the Gütersloh list differs from
   SpotterMania's, and its Bad Oeynhausen entry still describes a museum
   that closed in 2007.
5. **German and English Wikipedia** — treated as leads. German Wikipedia
   was good on the Bremenhalle contents, Flugplatz Damme, Flugplatz
   Uetersen/Heist, the Bremen (Junkers W 33) and the fate of the
   Luftwaffenmuseum Uetersen. Its `Liste von Luftfahrtmuseen` renders as an
   empty table and was useless. The English `List of surviving Lockheed
   F-104 Starfighters` is thin and partly wrong for Germany (it places
   24+63 both at PS Aero Baarlo and at the Curioseum in Usseln); the F-104
   Society list was preferred. The English F-86 survivor list produced one
   find nothing else had: the Sabre still standing at Uetersen.
6. **`flugzeuginfo.net` museum index** (last updated 16 Dec 2024) — used to
   confirm site existence and rough collection sizes only.

Sources that did **not** work: `mil-airfields.de` (domain returns a parked
page), `vdlgt.de` and `flugplatzmuseum-guetersloh.de` (both down/TLS-broken
at time of research), `airhistory.net` (403 to automated fetches), the
old `aviationmuseum.eu` `/World/Europe/` tree (bot-challenge page).

---

## Corrections and judgment calls

- **Ju 52 D-AQUI and the Lockheed L-1649A Super Star D-ALAN are NOT in this
  region.** Both are now in Lufthansa's Hangar One at **Frankfurt**
  (Hessen), which opens to the public in summer 2026. The Super Star was
  rolled out at Lufthansa Technik **Hamburg** in January 2025, shown at
  **Münster/Osnabrück** in mid-2025, then dismantled and moved to Frankfurt
  later that month. Recording either in Hamburg would have been wrong by
  about a year. Passed to the Hessen agent as a lead.
- **Breguet Atlantic 61+06** is recorded once, as the gate guardian of the
  naval air station at Nordholz, and was removed from the Aeronauticum file
  where SpotterMania's museum page also listed it. The Aeronauticum keeps
  61+14 (the one with the African motif on the fin, which the museum's own
  material describes).
- **Alouette II 75+95** is listed by SpotterMania at both Heeresflugplatz
  Celle and Fliegerhorst Wahn. Recorded once, at Celle (an Army school
  site, where an Army Alouette is the more plausible fit) and flagged in
  the row's `description`. **This needs a human to settle.**
- **F-104G 22+59 (DF+101)** at Rheine-Bentlage: SpotterMania calls it a
  gate guardian back on display April 2022; the F-104 Society reports it
  inside the same shelter as 25+86. Both identities are the same airframe
  (c/n 7140), so it is recorded once, under the Westfalengeschwader
  collection, with the discrepancy stated in `description`.
- **Rheine-Bentlage restructured.** The two Starfighters and the F-4F
  cockpit there belong to the *Private Militärgeschichtliche Sammlung
  Traditionsgemeinschaft Westfalengeschwader e.V.* inside the
  Theodor-Blank-Kaserne, not to a roadside gate. The ZMSBw collection
  register states the collection **is currently being reworked and is not
  accessible** — recorded as `access_type = restricted` with the closure
  said plainly in the rows.
- **C-47 "Faßberg Flyer" identity conflict.** `nasa-wings.info` gives
  c/n 13880 / USAAF 43-30729, ex-Turkish Air Force, delivered 5 Oct 1943
  and flown to Faßberg inside a Beluga on 19 June 1998. SpotterMania gives
  the same c/n 13880 but the marking "H-068 (43-15208)" and flags it as a
  false registration. `43-30729` is used in `tail_number`; the airframe is
  in any case painted to represent the *original* Faßberg Flyer
  (C-47A-80-DL 43-19674), which is a different aeroplane. Said so in the
  row.
- **Nordholz museum vs. base.** The Aeronauticum and the Marineflieger­
  stützpunkt are adjacent but separate sites with separate records; F-104G
  22+98 is the museum's, 22+92 the base's.
- **Wunstorf museum vs. base.** Same split: the Ju52-Halle exhibits
  (51+07, 58+95, GR+248, 70+68, DB+RD, the Mi-8 and the gliders) are one
  site; the ground instructional airframes inside the Fliegerhorst
  (50+60, 50+70, 58+90, 90+56, 90+65, 70+38, 72+01, 73+24, 87+34) are a
  second, `restricted`.
- **"WITHDRAWN FROM USE" lists were deliberately not recorded.** At Faßberg
  in particular SpotterMania lists ~30 further Tiger, NH90, CH-53 and Bo
  105 airframes in that state — dumped or in the hands of the fire section,
  not preserved and not visible. Only the *PRESERVED* blocks were taken.
  Faßberg's genuinely preserved set is 5 airframes plus the museum C-47.
- **Cockpit / nose / fuselage sections** are recorded as their own rows with
  the section status stated in `description`: Canberra T.4 WT480 (Gütersloh,
  cockpit), Harrier GR.3 ZD670 (Gütersloh, cockpit), Canberra T.4 WH849 and
  Buccaneer S.2C XV337 (Weeze, noses), Sea Lynx Mk 88 83+01 and 83+07
  (Nordholz, cabin sections), CH-53G 84+04 (Geilenkirchen, fuselage),
  A321 F-WTDG (Finkenwerder, fuselage), F-4F cockpit (Rheine-Bentlage).
- **Airworthy aircraft (Quax-Verein, Paderborn).** The Quax-Hangar is a
  genuine public exhibition with published opening days, but its aircraft
  fly. Recorded the ten types the hangar page lists, with registrations
  only where a source ties that airframe to Paderborn; the rotation caveat
  is in every row. Registrations left blank for the Fi 156 Storch, the
  Klemm Kl 107, the J-3 Cub and the PA-18 rather than guessing between the
  several club and member machines.
- **Bundeswehr codes** are written with the plus sign as displayed;
  Werknummern, false markings and pre-1968 letter codes (JB+110, GR+248,
  DB+RD, EB+250, DE+121, UA+113, RB+363) go in `tail_number` where that is
  what the aircraft wears, otherwise in `aliases`.
- **Drones.** The Deutsches Panzermuseum Munster holds no manned aircraft
  but does exhibit four German Army UAV airframes (KZO, LUNA, Aladin,
  MIKADO). Recorded, `role_type = drone`, tails blank.
- **Spacelab** at the Bremenhalle is recorded as `spacecraft` /
  `role_type = space`.
- **`latitude`/`longitude` are blank for 27 of the 33 sites.** German PLZ
  is precise enough to geocode and a guessed pin would be worse. Only
  coordinates that were actually published (Aeronauticum, Bremen Airport,
  Paderborn, Finkenwerder, Quax) were entered.

---

## Excluded, and why — named

| Site | Reason |
|---|---|
| **Luftwaffenmuseum Uetersen** | Closed. The whole collection — 3,030 t in 553 truckloads, 58 aircraft flown out by helicopter — moved to Berlin-Gatow in 1995. Only Sabre JB+110 stayed behind, and that is recorded as its own site. |
| **Luftfahrtmuseum Köln-Butzweilerhof** | Operated 1986–1996 and is gone. The only monument at Butzweilerhof today is a commemorative stele erected 1995 — no airframe. |
| **Motor Technica Museum, Bad Oeynhausen** | Closed 2007; the ~16 aircraft (MiG-21s, MiG-23UB, Mi-2, Mi-8PS, P-47D, TF-104G, Sycamore, Do 27, An-2, L-39, Alouette II) were dispersed, all remaining vehicles removed by end 2016 and the inventory dissolved by end 2017. **Where those airframes went is the single biggest open question in this region.** |
| **Private aircraft collection, Winterberg-Niedersfeld (NRW)** | Formerly an open-air display of a Mil Mi-1, two MiG-21 and a MiG-23 visible from the street; by 2013 partly scrapped and the rest moved into a locked hall. No confirmed public access, so not recorded. F-104 23+76 is attributed to a private German collector without a confirmed address. |
| **Deutsches Museum Bonn** | Holds no aircraft, helicopters or rockets; the site is now given over to the "Mission KI" artificial-intelligence exhibition. |
| **Automuseum Melle** | Aircraft *models* at 1:30 only, in a temporary exhibition. No airframes. |
| **Robert von Zeppelin- und Fliegermuseum, Wittmund** | Models of the airfield, of Zeppelins and of aircraft, plus printing presses and uniforms. No airframes. |
| **phaeno Wolfsburg / Autostadt / Stadtmuseum Wolfsburg** | No aircraft found in any of them. |
| **Miniatur Wunderland, Hamburg** | Models. Excluded by the brief and correctly so. |
| **Flughafen-Modellschau Hamburg** | Models. |
| **Boeing 707-430 D-ABOD, Hamburg Airport** | Lufthansa 1960–75, Lufthansa Technik trainer 1975–99, airport museum aircraft 1999–2021; scrapped from spring 2021 after Sinsheim/Speyer declined it, individual cockpit and cabin parts auctioned. Whether any section survives intact is unresolved. |
| **F-104G 21+25, Flensburg** | At the Nord Schrott scrapyard. No public access. |
| **F-104G 24+43, Hamburg** | Private owner, no address, no known access. |
| **F-104G 20+86, Wittmund** | Reported by the F-104 Society as marked for scrapping in August 2024. Not recorded; needs confirmation either way. |
| **Fliegerhorst Eggebek / Fliegerhorst Leck** | Both closed; Eggebek is now a solar park and industrial estate. No preserved airframe found at either. |
| **Flugplatz Bonn-Hangelar** | No museum, monument or preserved airframe found, despite the field's 1909 pioneering history and the Bundespolizei flying group next door. |
| **Segelflugzentrum Oerlinghausen** | A gliding centre with historic types flying, but no fixed public collection identified. Worth a second look. |
| **Tornado tail fin, Rahrdum roundabout, Fliegerhorst Upjever** | A vertical stabiliser on a roundabout, restored at a Rostock yard and reinstalled. A component, not an airframe or cockpit section — deliberately excluded. |

---

## Blank fields left deliberately

- `latitude`/`longitude` — see above.
- `year_built` — filled for only 7 rows (Junkers W 33 1927, Ju 52 1939,
  Bf 108 1940, C-47 1943, Do 27 D-EQXG 1959, F-104G 25+86 1964, Transall
  50+37 1970 and 50+66 1971). Everywhere else no sourced build or delivery
  date was found; Werknummern were *not* converted into years.
- `tail_number` blank on 16 rows: the Fw 44 at Bremen, the Mi-8T and
  Sycamore at Wunstorf, the DFS 230 and SG 38 at Wunstorf, the Arado Ar 196
  under restoration at Nordholz, four Quax types, the four Munster drones,
  and the F-4F cockpit at Rheine. Each says why in `description`.
- `website` blank for the gate-guard and monument sites, which have none.

---

## File and row counts

| file | rows | with tail |
|---|---|---|
| `aeronauticum_nordholz_aircraft.csv` | 21 | 20 |
| `airbus_museumsinsel_hamburg_aircraft.csv` | 8 | 8 |
| `bremenhalle_aircraft.csv` | 3 | 1 |
| `deutsches_marinemuseum_wilhelmshaven_aircraft.csv` | 1 | 1 |
| `deutsches_panzermuseum_munster_aircraft.csv` | 4 | 0 |
| `f104_denkmal_auenhausen_aircraft.csv` | 1 | 1 |
| `f104_denkmal_kropp_aircraft.csv` | 1 | 1 |
| `fliegerhorst_diepholz_aircraft.csv` | 3 | 3 |
| `fliegerhorst_hohn_aircraft.csv` | 2 | 2 |
| `fliegerhorst_jever_aircraft.csv` | 1 | 1 |
| `fliegerhorst_noervenich_aircraft.csv` | 4 | 4 |
| `fliegerhorst_schleswig_jagel_aircraft.csv` | 4 | 4 |
| `fliegerhorst_wittmundhafen_aircraft.csv` | 5 | 5 |
| `fliegerhorst_wunstorf_lehrsammlung_aircraft.csv` | 9 | 9 |
| `flugplatz_uetersen_sabre_aircraft.csv` | 1 | 1 |
| `flugplatzmuseum_guetersloh_aircraft.csv` | 9 | 9 |
| `heeresflugplatz_celle_aircraft.csv` | 3 | 3 |
| `heeresflugplatz_fassberg_aircraft.csv` | 5 | 5 |
| `ju52_halle_wunstorf_aircraft.csv` | 10 | 6 |
| `koeln_bonn_flugbereitschaft_aircraft.csv` | 7 | 7 |
| `luftbrueckenmuseum_fassberg_aircraft.csv` | 1 | 1 |
| `marinefliegerstuetzpunkt_nordholz_aircraft.csv` | 7 | 7 |
| `marseille_kaserne_appen_aircraft.csv` | 1 | 1 |
| `mgs_westfalengeschwader_rheine_aircraft.csv` | 3 | 2 |
| `movie_park_germany_starfighter_aircraft.csv` | 1 | 1 |
| `nato_air_base_geilenkirchen_aircraft.csv` | 2 | 2 |
| `quax_hangar_paderborn_aircraft.csv` | 10 | 6 |
| `raf_museum_laarbruch_weeze_aircraft.csv` | 5 | 5 |
| `traditionsgemeinschaft_jabog41_husum_aircraft.csv` | 2 | 2 |
| `traditionsgemeinschaft_jabog43_oldenburg_aircraft.csv` | 4 | 4 |
| `transall_damme_aircraft.csv` | 1 | 1 |
| `transall_rotenburg_aircraft.csv` | 1 | 1 |
| `von_seydlitz_kaserne_kalkar_aircraft.csv` | 1 | 1 |
| **total** | **141** | **125** (88%) |
**33 sites, 141 airframes, 125 with a tail number (88%).** Serial coverage
is high because German practice is to paint the Bundeswehr code on the
aircraft. The 12% without one are gliders, drones, restoration projects and
airworthy club aircraft whose individual identity rotates.

By Land: Niedersachsen 15 sites, Nordrhein-Westfalen 9, Schleswig-Holstein 6,
Hamburg 1, Bremen 1 (plus one Niedersachsen site, Deutsches Marinemuseum
Wilhelmshaven, that is a naval museum with a single gate-guard aircraft).

---

## Needs a human on site — ranked

1. **Alouette II 75+95 — Celle or Köln-Wahn?** One airframe, two claimed
   locations in the same source. Somebody has to look at both gates.
2. **Where did the Motor Technica Museum (Bad Oeynhausen) aircraft go?**
   Sixteen airframes including a P-47D Thunderbolt, a TF-104G, a Bristol
   Sycamore, MiG-21s and a MiG-23UB left that site between 2007 and 2017.
   Some are probably now recorded elsewhere in Germany under other museums;
   some may be in private hands in NRW. This is the largest unresolved
   population in the region.
3. **Is F-104G 20+86 still at Wittmund?** Reported for scrapping in
   August 2024. If it survives it is a missing record; if not, that should
   be stated.
4. **Gütersloh's exact holdings.** SpotterMania and aviationmuseum.eu give
   overlapping but different lists; a 2022 forum thread supports the union
   of nine airframes recorded here, but the museum's own site
   (`vdlgt.de` / `flugplatzmuseum-guetersloh.de`) was offline throughout
   this pass. The Su-22M4 25+06 (ex-NVA 370) and the Hungarian MiG-21MF
   9510 are the two least-confirmed. Visits are by arrangement only.
5. **The five monument Starfighters taken solely from the F-104 Society
   list** — 22+77 (pole, Kropp), 29+08 (pole, Auenhausen), 27+28 (Movie
   Park Germany, Bottrop-Kirchhellen), 29+05 (Von-Seydlitz-Kaserne, Kalkar)
   and 22+06 (Marseille-Kaserne, Appen). None was confirmed by a dated
   photograph. A single geotagged photo each would settle them, and would
   also let the coordinate columns be filled.
6. Secondary: the serial of the Mi-8T and of the Sycamore at the Ju52-Halle
   Wunstorf; the registration of the Fw 44 Stieglitz in the Bremenhalle;
   the serial of the F-4F cockpit at Rheine-Bentlage; and whether the
   Junkers W 33 "Bremen" loan from the Henry Ford Museum (taken over by
   Bremen Airport on 1 January 2009 with a ten-year return clause) has in
   fact been extended — it was still on display as of the airport's current
   Bremenhalle page, but the clause deserves a check.

---

## Leads for other agents

- **Hessen.** Lufthansa's **Hangar One at Frankfurt Airport** now holds both
  the Ju 52/3m **D-AQUI** (also registered D-CDLH; Lufthansa service
  1986–2018, ~250,000 passengers, ~11,500 hours) and the Lockheed
  **L-1649A Super Star D-ALAN** (c/n 1018, ex-N7316C), restored at
  Lufthansa Technik Hamburg, repainted into 1950s livery, permanently
  grounded after the 2018 cancellation of the return-to-flight programme.
  Public opening summer 2026. That is a two-airframe site nobody should
  miss.
- **Mecklenburg-Vorpommern.** The **Interessenverein Luftfahrt
  Neuenkirchen** (Am Gutshaus, 17039 Neuenkirchen) is a substantial ex-NVA
  collection — 24 airframes including MiG-17F ×2, MiG-21M/MF/PFM, MiG-23ML
  20+10, Su-7U, Su-22M-4 362, Mi-8TB 93+86, two Kamov Ka-26 (DDR-SPQ,
  DDR-SPW), L-39ZO, An-2TD, Fiat G.91 31+62, F-4F 37+58, Tornado 43+73,
  Letov KT-04, Z-37 Cmelak. Some listings put "Neuenkirchen" in
  Niedersachsen; it is not.
- **Rheinland-Pfalz.** Fiat G.91 R/3 **30+74** is mounted on concrete
  plinths at the Reservistenkameradschaft Ramstein-Landstuhl, Talstraße,
  Ramstein — a monument site that is easy to miss.
- **Whoever sweeps NRW again**: F-104G **24+63** is placed by English
  Wikipedia at PS Aero, Baarlo (Netherlands) painted as D-8212 and by the
  F-104 Society at the "Curioseum" in **Usseln** (Willingen, Hessen). One
  of the two is stale.
- **Berlin.** Several airframes recorded elsewhere in Germany trace back to
  the 1995 Uetersen→Gatow move; anyone reconciling Gatow's provenance
  fields will find the Uetersen history useful.
