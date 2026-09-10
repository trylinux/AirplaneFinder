# DE_EAST — Eastern Germany preservation survey

Scope: Brandenburg, Berlin, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt,
Thüringen. Excluded by assignment: Militärhistorisches Museum Flugplatz
Berlin-Gatow, Deutsches Technikmuseum Berlin, Luftfahrtmuseum Wernigerode,
Militärhistorisches Museum Dresden.

Output: `de_museums.csv` (48 sites) plus one `<slug>_aircraft.csv` per site.

---

## Sources and how much weight each carried

**Rung 1 — the site's own publication.** Used wherever it existed and it won
every conflict about "what is here now":

- `luftfahrtmuseum-rothenburg.de` — outstanding. Every airframe has its own
  page with tactical number, Zelle-Nr/Werknummer, unit history and loan
  status, and the site *says when an aircraft has left*: the Let L-410MA
  0503, the Mi-2 94+60 (ex-NVA 383) and the blue Fiat G.91 Wnr 91-336
  (ex 30+74) are all flagged "nicht mehr im Bestand". Those three are
  therefore **not** recorded at Rothenburg. Footer copyright reads 2026, so
  the site is current.
- `luftfahrttechnisches-museum-rechlin.de` — good on replica status
  (it states plainly which exhibits are 1:1 Modellnachbauten and which are
  loans from MHM Gatow) but publishes almost no serials.
- `flugplatzmuseumcottbus.de`, `technikmuseum-puetnitz.de`,
  `technikmuseum-dessau.org`, `otto-lilienthal.de`, `ivln.de`,
  `flugwelt-altenburg-nobitz.de` — used for addresses, opening and general
  holdings; none publishes a serial list.

**Rung 2 — type-specific disposal registers.** These proved to be the single
most valuable German sources and carried more weight than any museum list:

- **`mig-21.de/deutsch/ddrverbleib.htm`** — "Verbleib der MiG-21 der LSK/LV",
  a complete fate register of every East German MiG-21 by NVA tactical
  number, version, Bundeswehr code and present location. It is the origin of
  most of the plinth and oddity records below, and it independently confirmed
  the alignment of the Finowfurt inventory (708 F-13 and 589 M both land
  exactly where the museum list puts them).
- **`biancahoegel.de/flug/typen/ru/suchoij/su-22-ddr.html`** — Su-22M4 /
  Su-22UM3K disposal table with NVA number, Bundeswehr code and location. It
  confirmed Cottbus 365 = 25+04 and 137 = 25+53, Dessau 600 = 25+09 and
  127 = 25+49, and Rechlin 119 = 25+48 against three other sources.
- English Wikipedia `List of displayed Mikoyan-Gurevich MiG-23s` — used as a
  lead only; it is the source of the Neuenkirchen 20+10 and Rostock-Laage
  20+11 records, and it disagrees with the Finowfurt inventory (below).

**Rung 3 — dated photographs.** `abpic.co.uk` location pages and
`airhistory.net` "[Off-Airport]" location pages. These decided currency at
two sites:

- Flugplatzmuseum Cottbus: a run of photographs dated **15 August 2024** and
  **9 June 2024** confirms the presence of An-2 801, MiG-21MF 653, MiG-21US
  215, MiG-23BN 696, Su-22M-4 25+04, Lim-5 537, Mi-2 380, Mi-4 785 and 792,
  Mi-9 482, UH-1D 72+77, F-104G 21+56 and 25+12, T-33A 94+69, F-84F, Sabre
  BB+237, Tu-134A CCCP-65745 and L-60 OE-BVL. Each of those descriptions
  carries the date.
- Airpark Zehdenick: photographs dated **11 September 2020** and
  **17 July 2014**, which is the only currency evidence for that private
  collection and the reason its records carry those dates.

**Rung 4 — aggregator inventories.** `aviationmuseum.eu` per-museum tables
were the backbone for sites that publish nothing themselves (Zehdenick,
Neuenkirchen, Grimmen, Altenburg-Nobitz, Borkheide, Shelter Albrecht,
Pütnitz, Hangar 10, Anklam, Großenhain, Dessau). **Caution: these tables are
two side-by-side HTML cells, and a text extractor will silently mis-align
them.** I parsed the raw HTML and matched the two columns index-for-index;
the alignment was then checked against known registration grammar (D-H… must
be a helicopter, D-E… a light single, Bundeswehr MiG-21 = 22+/23+xx,
MiG-23 = 20+xx, Su-22 = 25+xx, Mi-8 = 93+/94+xx, Mi-24 = 96+/98+xx,
Alouette II = 75+/76+xx). Anything that still failed that test is flagged in
the row's `description`.

`de.wikipedia.org/wiki/Liste_von_Luftfahrtmuseen` gave the site inventory for
all six Länder and was the reason Zehdenick, Neuenkirchen, Grimmen,
Borkheide, Shelter Albrecht, Anklam, Prora and Teistungen are in this file at
all. Its per-museum aircraft counts are roughly right; its links are current.

---

## Corrections made, with the evidence

- **Airpark Zehdenick is a mixed German/Polish collection, not an all-German
  one.** The published inventory renders the Su-22M4s as 3215/3216/3618 and
  the MiG-21s as 5304/8907/5710/9298; an earlier draft of this file wrote
  them as Bundeswehr codes (32+15 etc.). That is wrong — Bundeswehr Su-22
  codes only run 25+xx and MiG-21 codes 22+/23+xx, while 3215, 3216, 3618,
  5304, 5710, 8907 and 9298 are textbook **Polish Air Force** four-digit
  serials, and the site also holds a Polish Su-20 (6264), a PZL TS-11 Iskra
  (812), a Polish Mi-24V (0701) and a Polish Mi-2T (0815). They are recorded
  as bare four-digit serials.
- **Flugwelt Altenburg-Nobitz Su-22M4** — one inventory renders the marking
  "98+17 / 14". The Su-22 disposal register gives NVA 706 = Bundeswehr 25+31
  at Altenburg, which is the only reading consistent with Bundeswehr Su-22
  coding. Recorded as `25+31`, alias `706`, discrepancy stated in the row.
- **MiG-Museum Sömmerda-Dermsdorf Su-22M4** — the site says only "eine
  Su-22M4". JetJournal identifies it as NVA 682 / Bundeswehr 25+17.
  Recorded with that code.
- **Cottbus T-33A** — the museum inventory says `EB+399`; the 2024
  photographs read `94+69`. The photograph wins for `tail_number`, `EB+399`
  is kept as an alias and the conflict is stated in the description.
- **Cottbus F-84F** — inventory `DD+313`, 2024 photograph `DD-339`.
  Photograph wins, `DD+313` kept as an alias.
- **Cottbus Mi-4** — inventory 538 and 785; 2024 photographs read 792 and
  785. 792 recorded, 538 noted in the description.
- **Cottbus MiG-23MF** — recorded as `20+04` (Wikipedia MiG-23 list) with
  the inventory's NVA number 584 as an alias, because the inventory gives
  584 twice, once for a MiG-21MF and once for this aircraft.
- **Peenemünde has been emptied of aircraft.** The Historisch-Technisches
  Museum now shows only the V-1 and A4 replicas outdoors. Its former
  aircraft dispersed: the MiG-23MLA 332 went to Rechlin (the museum's own
  page confirms it as "ein Original des JG-9 der DDR LSK/VV 332 aus
  Peenemünde"); the An-2TD, photographed at Peenemünde in **August 2006** as
  D-FONB, is now at Neuenkirchen; the Su-22M4 362 (25+02) is likewise now at
  Neuenkirchen; and MiG-21s 677, 693 and 934, all listed at "HTIZ
  Peenemünde" in the MiG-21 register, appear as a matched set of three in
  the Technik-Museum Pütnitz inventory. They are recorded at Pütnitz. One
  MiG-21US (230) remains at the **airfield** and is recorded as its own site.
- **Rothenburg MiG-21U 244** is in the MiG-21 register at Rothenburg but has
  no page on the museum website, which covers only the U-600 296. Recorded
  as `in_storage`.
- **The Baade 152 fuselage left Rothenburg in August 1995**, per the
  museum's own history page, and is at Dresden airport. Recorded there.

## Judgment calls

- **Replicas and mock-ups are recorded, and said to be replicas in
  `description`.** Rechlin is nearly half replicas — the Do 335 there is a
  replica and the museum itself points out that the only original is at
  Udvar-Hazy; the Etrich Taube, Fokker E.III / D.VII / Dr.I, Ta 154, Fw 189
  gondola, DFS 230, Fi 103R, Me 262 and Siemens-Schuckert D.III are all
  full-scale models, several on loan from MHM Gatow. The Anklam Lilienthal
  gliders are all reproductions and are recorded as such.
- **Cockpit and nose sections recorded as their own rows**, stated plainly:
  Rechlin's Ar 234 cockpit, Ju 388 L-1 nose, Bf 109 cockpit and Fw 189
  gondola; Rothenburg's Airbus A319 nose section (from an A319 dismantled on
  the airfield by Elbe Flugzeugwerke 2020-2022 — the donor registration is
  not published, so `tail_number` is blank); Cottbus's Lim-5P 437 rear
  fuselage; Finsterwalde's MiG-21PF 836 forward fuselage.
- **`access_type`.** `public` for museums and for plinths visible from a
  public road. `appointment` for Airpark Zehdenick (the collection asks
  visitors to report to reception first), Shelter Albrecht, the Kleber
  collection at Neugersdorf, the Gellmersdorf 152 segment and the Dresden
  airport 152 (hangar, open days only). `restricted` for the two airframes
  inside Fliegerhorst Holzdorf and the Su-22 in the Laage base collection.
- **Airworthy aircraft are recorded where a visitor finds them**: Hangar 10
  at Heringsdorf and the Fliegendes Museum at Großenhain are flying
  collections; both are open to visitors and both are recorded `on_display`.
- **The Anklam hang-glider collection is deliberately not itemised.** The
  Otto-Lilienthal-Museum holds roughly **182** hang gliders (the German
  hang-gliding collection). They are aircraft, but recording 182 rows of
  unregistered fabric wings would swamp the file and none carries an
  identifier. Recorded: the nine Lilienthal reproductions and the seven
  powered aircraft/gliders. **A human should decide whether the hang-glider
  collection belongs in this database at all.**
- **`year_built` is blank on 344 of 355 rows.** It is filled only where a
  source gave a build or delivery date in words (Rothenburg's MiG-21bis 838
  and Su-22M4 757, the CASA C-127, the Fiat G.91 99+01, the Rechlin CS-102
  140, the Stölln Il-62, the Rothenburg L-29 339).

## Excluded, and why

- **Luftfahrt- und Technikmuseum Merseburg (Merseburg, Sachsen-Anhalt)** —
  **closed**. The Saalekreis building authority ordered it shut on
  13 November 2020; a 2021 sale fell through and the collection was sold off
  or returned to lenders. Its Il-62 DDR-SEC, Tu-134 DDR-SCZ, F-104G 21+56
  and 24+54, RF-84F EB+119, G.91s 31+78 and 32+11, Mi-8T 390, Alouettes
  75+28 / 75+86 / A-16, Il-14 3065 and five MiG-21s (670, 673, 725, 779,
  829) are **untraced**. This is the largest single gap in the region and
  the top item for a human.
- **Aero Park Leipzig / Flughafen Leipzig-Halle** — the park closed; of five
  aircraft (Il-18 DDR-STA, Il-62 DDR-SEF, Tu-134A DDR-SCF, Z-37A DDR-SUL,
  PZL-106 DDR-TEJ) reportedly only the Il-18 survives, and the surviving
  airliners sit inside the airport security area with no visitor access.
  Not recorded; a visitor cannot go and see them.
- **EADS / Elbe Flugzeugwerke Dresden** — holds MiG-21US 218 and, per one
  source, the best-preserved Il-14 in Germany. Industrial site, no public
  access. Not recorded.
- **Truppenübungsplatz Lehnin (Brandenburg)** — MiG-21F-13s 713, 726 and 736
  are there as range targets on a live training area. Not displayed, not
  accessible. Not recorded.
- **Militärtechnische Schule Bad Düben** — MiG-21PFs 840 and 846 are listed
  "ex", i.e. gone. Not recorded.
- **Großröhrsdorf (Sachsen)** — MiG-21PFM 758 marked "verschrottet?" in the
  register. Not recorded.
- **Berlin "Tacheles" / Waldsieversdorf** — MiG-21PFM 756 listed as "ex" at
  both. Not recorded.
- The four sites named in the assignment as another agent's are absent.

## Left deliberately blank

- Latitude/longitude on 41 of 48 sites. Coordinates are given only where
  German Wikipedia publishes them for that exact site (Finowfurt, Cottbus,
  Dessau, Verkehrsmuseum Dresden, Peenemünde, Stölln). A five-digit PLZ is
  recorded everywhere it is known and is a better pin than a guess.
- `tail_number` on 67 rows, including all of Cämmerswalde, the Da Capo
  Il-18, the Benneckenstein and Alt Schwerin airframes, the phanTECHNIKUM
  MiG-21SPS and the Rechlin replicas.
- Street addresses at Grimmen, Borkheide, Benneckenstein and several plinth
  sites, where no source published one.

## Needs a human on site, ranked

1. **Where did the Merseburg collection go?** ~20 airframes including an
   Il-62 and a Tu-134 vanished from the record after November 2020.
2. **Luftfahrtmuseum Finowfurt: how many MiG-23s, and which?** The museum
   inventory gives MiG-23S 08, MiG-23BN 20+57 and MiG-23UB 720. English
   Wikipedia gives MiG-23S 08, MiG-23BN **20+55** and MiG-23UB **20+57**.
   The 08 agrees; the other two do not. Someone needs to read the airframes.
   Related: the MiG-21 register also puts MiG-21PFMs **479** and **897** at
   Finowfurt, and neither appears in the museum's own inventory — while 479
   appears in the Technikpark Grimmen inventory as a SPS-K. One of those two
   records is stale.
3. **Cämmerswalde** (Il-14, MiG-21, Mi-2 at the Gaststätte Zum Flugzeug).
   The MiG-21 is PFM **449** per the register (ex Drewitz, ex Cottbus) but
   no source gives the Il-14 registration or the Mi-2 identity. Three easy
   reads on one visit.
4. **Cottbus MiG-21MF 584 vs MiG-23MF 584** — the same tactical number is
   published for two different aircraft at one site. One of them is wrong.
   Also confirm whether the MiG-21SPS-K is 981 or 986 (986 is separately
   recorded at Flugplatz Kamenz).
5. **Airpark Zehdenick currency.** The newest evidence is September 2020 for
   a privately owned collection at a joinery, exactly the kind of site that
   turns over. Confirm the Starfighter in particular: the inventory says
   F-104G 21+12, the 2020 photograph caption says F-104F 20+86.

Lower priority: the identity of the Da Capo Leipzig roof Il-18; whether the
Peenemünde airfield still shows the faded Soviet cruise missile reported
beside its MiG-21US; the Rechlin Junkers F 13 (original or reconstruction?)
and whether the Hispano HA-1112 listed there by one aggregator exists — the
museum itself shows only a Bf 109 cockpit and a film about assembling it.

## Leads for other agents

- **Faßberg (Niedersachsen), Technische Schule der Luftwaffe 3** — MiG-21Ms
  435, 483, 508 and 515 are held there per the MiG-21 register.
- **Museum für Technik, Natur und Verkehr, Ankum (Niedersachsen)** — a large
  ex-NVA holding: MiG-21s 217, 242, 265, 679, 717, 760 and Su-22M4s 546, 574
  and 824.
- **Flugausstellung L+P Junior, Hermeskeil (Rheinland-Pfalz)** — MiG-21s
  205 (cockpit), 238, 775, 853, 889, 979 (cockpit) and Su-22M4s 370 and 678.
- **Motor Technica Museum Bad Oeynhausen (NRW)** — MiG-21s 272, 782, 953.
- **Wehrtechnische Studiensammlung Koblenz** — MiG-21bis 846, marked "2".
- **Truppenübungsplatz Putlos (Schleswig-Holstein)** — MiG-21PFM 791.
- **Deutsches Marine Luftschiff und Marineflieger Museum Nordholz** —
  Su-22M4 366 (25+05).
- **Heidepark Soltau** — MiG-21U 295, a theme-park airframe.
- **Kartbahn Winterberg-Niedersfeld (NRW)** — MiG-21UM 266.
- **Lintel / B64, Ruppichteroth, Elsey, Eisdorf, St. Ingbert, Oyten,
  Bensheim, Lübeck, Stammheim, Memmingen, Emlichheim (Kunstpark Olmes),
  Miesitz's western equivalents** — the MiG-21 register lists a long tail of
  western-German roadside and business-forecourt MiG-21s that belong to
  other agents' areas.
- `mig-21.de/deutsch/ddrverbleib.htm` and
  `biancahoegel.de/flug/typen/ru/suchoij/su-22-ddr.html` are worth reading in
  full by whoever covers western Germany.

---

## Files and coverage

| Site | File | Aircraft | With tail number |
|---|---|---:|---:|
| Flugplatzmuseum Cottbus | `flugplatzmuseum_cottbus_aircraft.csv` | 53 | 46 |
| Airpark Zehdenick | `airpark_zehdenick_aircraft.csv` | 32 | 31 |
| Luftfahrttechnisches Museum Rechlin | `luftfahrttechnisches_museum_rechlin_aircraft.csv` | 30 | 12 |
| Luftfahrtmuseum Finowfurt | `luftfahrtmuseum_finowfurt_aircraft.csv` | 29 | 27 |
| Interessenverein Luftfahrt Neuenkirchen | `interessenverein_luftfahrt_neuenkirchen_aircraft.csv` | 25 | 24 |
| Luftfahrttechnisches Museum Rothenburg | `luftfahrttechnisches_museum_rothenburg_aircraft.csv` | 22 | 21 |
| Hangar 10 | `hangar_10_aircraft.csv` | 21 | 18 |
| Fliegendes Museum Großenhain | `fliegendes_museum_grossenhain_aircraft.csv` | 19 | 18 |
| Technikmuseum Hugo Junkers | `technikmuseum_hugo_junkers_aircraft.csv` | 18 | 15 |
| Flugwelt Altenburg-Nobitz | `flugwelt_altenburg_nobitz_aircraft.csv` | 17 | 16 |
| Otto-Lilienthal-Museum Anklam | `otto_lilienthal_museum_anklam_aircraft.csv` | 16 | 5 |
| Rechlin-Lärz Luftfahrtmuseum | `rechlin_laerz_luftfahrtmuseum_aircraft.csv` | 7 | 7 |
| Technikpark Grimmen | `technikpark_grimmen_aircraft.csv` | 6 | 6 |
| MiG-Museum Sömmerda-Dermsdorf | `mig_museum_soemmerda_dermsdorf_aircraft.csv` | 5 | 5 |
| Technik-Museum Pütnitz | `technik_museum_puetnitz_aircraft.csv` | 5 | 5 |
| phanTECHNIKUM | `phantechnikum_wismar_aircraft.csv` | 4 | 0 |
| Flughafen Berlin-Tempelhof | `flughafen_berlin_tempelhof_aircraft.csv` | 3 | 2 |
| Flugzeugmuseum Cämmerswalde | `flugzeugmuseum_caemmerswalde_aircraft.csv` | 3 | 0 |
| Hans-Grade-Museum Borkheide | `hans_grade_museum_borkheide_aircraft.csv` | 3 | 3 |
| Verkehrsmuseum Dresden | `verkehrsmuseum_dresden_aircraft.csv` | 3 | 1 |
| AGRONEUM Alt Schwerin | `agroneum_alt_schwerin_aircraft.csv` | 2 | 0 |
| Fliegerhorst Holzdorf | `fliegerhorst_holzdorf_aircraft.csv` | 2 | 2 |
| Historisch-Technisches Museum Peenemünde | `historisch_technisches_museum_peenemuende_aircraft.csv` | 2 | 0 |
| MiG-21 Denkmal, Flugplatz Neuhardenberg | `mig21_denkmal_flugplatz_neuhardenberg_aircraft.csv` | 2 | 2 |
| MiG-21 Denkmal, Flugplatz Stendal | `mig21_denkmal_flugplatz_stendal_aircraft.csv` | 2 | 2 |
| Shelter Albrecht | `shelter_albrecht_aircraft.csv` | 2 | 2 |
| AlliiertenMuseum | `alliiertenmuseum_aircraft.csv` | 1 | 1 |
| Baade 152 Flughafen Dresden | `baade_152_flughafen_dresden_aircraft.csv` | 1 | 0 |
| Da Capo Oldtimermuseum | `da_capo_oldtimermuseum_leipzig_aircraft.csv` | 1 | 0 |
| Deutsche Raumfahrtausstellung Morgenröthe-Rautenkranz | `deutsche_raumfahrtausstellung_morgenroethe_aircraft.csv` | 1 | 1 |
| Eisenbahn- und Technikmuseum Rügen | `eisenbahn_und_technikmuseum_ruegen_aircraft.csv` | 1 | 1 |
| Eisenbahnmuseum Insel Usedom | `eisenbahnmuseum_insel_usedom_aircraft.csv` | 1 | 1 |
| Flugsportinformationszentrum Gellmersdorf | `flugsportinformationszentrum_gellmersdorf_aircraft.csv` | 1 | 0 |
| Grenzlandmuseum Eichsfeld | `grenzlandmuseum_eichsfeld_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Allstedt | `mig21_denkmal_allstedt_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Autohaus Grieb Miesitz | `mig21_denkmal_autohaus_grieb_miesitz_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Finsterwalde | `mig21_denkmal_finsterwalde_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Flugplatz Kamenz | `mig21_denkmal_flugplatz_kamenz_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Flugplatz Peenemünde | `mig21_denkmal_flugplatz_peenemuende_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Flugplatz Welzow | `mig21_denkmal_flugplatz_welzow_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Grießen bei Forst | `mig21_denkmal_griessen_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, MaxCar Blankenburg | `mig21_denkmal_maxcar_blankenburg_aircraft.csv` | 1 | 1 |
| MiG-21 Denkmal, Staffelde bei Tangermünde | `mig21_denkmal_staffelde_aircraft.csv` | 1 | 1 |
| MiG-23 Denkmal, Flughafen Rostock-Laage | `mig23_denkmal_flughafen_rostock_laage_aircraft.csv` | 1 | 1 |
| Ostdeutsches Fahrzeug- und Technikmuseum Benneckenstein | `ostdeutsches_fahrzeug_und_technikmuseum_benneckenstein_aircraft.csv` | 1 | 0 |
| Otto-Lilienthal-Verein Stölln | `otto_lilienthal_verein_stoelln_aircraft.csv` | 1 | 1 |
| Sammlung Kleber Neugersdorf | `sammlung_kleber_neugersdorf_aircraft.csv` | 1 | 1 |
| Traditionssammlung Fliegerhorst Laage | `traditionssammlung_fliegerhorst_laage_aircraft.csv` | 1 | 1 |
| **Total** | 48 files | **355** | **288** |

Serial coverage: **288 of 355 rows (81 %)** carry a `tail_number`. Coverage is
near-total at the ex-NVA sites, where the tactical number or Bundeswehr
Kennzeichen is painted on and published, and lowest at Rechlin (12 of 30),
where most exhibits are unmarked full-scale replicas.
