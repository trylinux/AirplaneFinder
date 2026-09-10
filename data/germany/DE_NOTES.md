# Germany — coordinator summary

Imported live 10 September 2026. Four research passes: the national and
largest collections; the ex-NVA east (Brandenburg, Berlin outside the two big
museums, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt, Thüringen); the
north-west (Schleswig-Holstein, Hamburg, Bremen, Niedersachsen,
Nordrhein-Westfalen); and the south (Bayern, Baden-Württemberg, Hessen,
Rheinland-Pfalz, Saarland). The per-pass research notes follow this summary
unchanged; where they disagree with this section, this section is what was
imported.

**Files:** `de_museums.csv` (151 new sites) and 152 `*_aircraft.csv` files,
one per site, including `schleissheim_topup_aircraft.csv` — 93 rows added to
the single Bf 109 G that was all Germany had in the database before this pass.

**Rows:** 1598 aircraft · 1274 with tail numbers (79%) ·
1505 on_display / 84 in_storage / 9 under_restoration.

**Sites by Land:** Bayern 31, Niedersachsen 17, Baden-Württemberg 16, Mecklenburg-Vorpommern 15, Brandenburg 11, Sachsen 10, Nordrhein-Westfalen 10, Rheinland-Pfalz 9, Sachsen-Anhalt 8, Hessen 8, Schleswig-Holstein 6, Berlin 4, Thüringen 4, Bremen 1, Hamburg 1.
**Access:** 103 public · 22 appointment · 26 restricted.

**Largest collections:** Militärhistorisches Museum der Bundeswehr – Flugplatz Berlin-Gatow 147, Flugausstellung Hermeskeil 123, Deutsches Museum Flugwerft Schleissheim 93, Technik Museum Speyer 75, Deutsches Segelflugmuseum mit Modellflug 62, Hubschraubermuseum Bückeburg 61, Luftfahrtmuseum Wernigerode 61, Technik Museum Sinsheim 59, Flugplatzmuseum Cottbus 53, Internationales Luftfahrtmuseum Manfred Pflumm 51.

**Coordinates:** every site has one. 15 were fixed by the researchers;
the rest were geocoded by the coordinator and the level is recorded per site in
`de_geocode_log.csv` — 77 from the street address, 58 from the PLZ
(five-digit German postcodes are tight, typically a few streets), 1 city-level.

## Sources that carried the pass

- **`aviationmuseum.eu`** supplied the museum inventories, including a dated
  2022 walk-round survey of Gatow split into on-display and stored aircraft.
  Its tables are two side-by-side HTML cells, so a naive text extraction
  **scrambles the type/serial pairing** — the agents parsed raw HTML cell by
  cell. The Speyer table is genuinely mis-aligned in its first seven rows and
  was realigned by hand.
- **`mig-21.de`** carries a complete per-airframe disposal register for every
  NVA MiG-21, and `biancahoegel.de` the equivalent for the Su-22M4/UM3K.
  Together they produced most of the eastern plinth population and
  independently confirmed several museum inventories.
- **`916-starfighter.de`** and the International F-104 Society fate lists, with
  2024-25 sightings, for the Starfighter monuments — the classic West German
  plinth aircraft. **`i-f-s.nl`** "Preserved in Germany" likewise.
- **SpotterMania's per-airfield "PRESERVED" tables** (current to August 2026)
  supplied nearly every north-western gate-guard record. Its "WITHDRAWN FROM
  USE" lists were deliberately not recorded — dumped, not preserved.

German Wikipedia was treated as a lead list and repeatedly proved stale; the
Gatow table still carries a 2018 date stamp.

## Cross-pass adjudications (one airframe, one place)

Nine airframes came back at two sites. Eight resolve the same way: **Gatow's
stored/reserve list is stale, and the aircraft are on loan elsewhere.**
Recorded where a visitor would find them, per the methodology's rule that we
record where an aircraft *is*, not who owns it:

- L-29 **313** and Fiat G.91 R/3 **99+01** → Luftfahrttechnisches Museum
  Rothenburg (both documented on the museum's own 2026 site as loans from the
  Militärhistorisches Museum Dresden).
- Sabre **JB+110** → Flugplatz Uetersen-Heist, where it stayed behind when the
  Luftwaffenmuseum moved to Berlin-Gatow in 1995.
- Sabre **D-9539** and Fiat G.91 T/3 **99+41** → Flugwelt Altenburg-Nobitz.
- F-104F **29+14** → Traditionsverein Immelmann, Eschbach, which the F-104
  Society's 2025 list records as a Gatow loan.
- Bü 131 **D-EAZO** → Fliegendes Museum Großenhain over an undated
  aviationmuseum.eu inventory line at Luftraum Süd.
- F-104G **21+55** → the Starfighter-Denkmal at Haßfurt (F-104 Society, 2025)
  rather than "on the airfield" at Großenhain.
- He 162 **Wnr 120076**: the original is in the Deutsches Technikmuseum Berlin.
  Rechlin's is a rebuild with roughly 40 percent original parts, so its tail was
  blanked and the Werknummer kept as an alias.

**False markings blanked rather than imported:** Technik Museum Sinsheim's
Spanish-built CASA 352L wears **D-AQUI** in Lufthansa colours; the real D-AQUI
(Werknummer 130714) is the Lufthansa Traditionsflug aircraft now permanently in
Hangar One at Frankfurt. Speyer's sister airframe was already flagged the same
way by its researcher.

**Three two-digit Soviet bort numbers** — An-2 "03" at Sinsheim, Su-7 "07" at
Neuenkirchen, MiG-17 "07" at Rechlin — collided with Russian records already in
the database. Bort numbers are not unique identifiers, and the
`(model, tail_number)` key cannot hold both, so the German tails were blanked
with the bort kept as an alias. Same workaround as SAAF Mirage F1CZ 207.

## Coordinator corrections applied before import

- 146 dashless designation aliases added (`MiG21`, `F104G`, `Su22` …).
- `Ju 52/3m` normalised to model `Ju 52` + variant `3m` country-wide, with the
  old spelling kept as an alias; `UH-1D` split to `UH-1` + `D`.
- `Unknown` manufacturer placeholders replaced with `Unidentified`.
- `_fix_adjudications.py` in this directory reproduces every one of these
  decisions against the raw research output.

**Validation:** every row passed `_validate_aircraft_row` and the alias suite;
zero museum-name collisions against the 2,083 museums then live; a combined dry
run of all 1598 rows returned `created: 1598, linked: 1598, errors: []`;
after import all 152 per-site live counts equal the file counts.

## What is still open

- **The closed museums' collections are untraced.** Luftfahrt- und
  Technikmuseum Merseburg was ordered shut in November 2020 and roughly 20
  airframes including an Il-62 and a Tu-134 went somewhere. The Red Stars
  Museum at Bensheim dispersed ten ex-Warsaw Pact aircraft. Motor Technica Bad
  Oeynhausen dispersed sixteen. Each is a findable set of airframes that is
  currently in the database nowhere.
- **Gatow's ~70 stored airframes** need a currency check after the Hangar 4
  conversion.
- **Airpark Zehdenick's newest evidence is September 2020** — the largest site
  in the country resting on five-year-old sightings.
- Fürstenfeldbruck's seven plinth aircraft have no published serials and the
  site may clear before 2030.
- Peenemünde has been emptied of aircraft; its MiG-23 went to Rechlin, the An-2
  and Su-22 to Neuenkirchen, three MiG-21s appear as a set at Pütnitz.

---

# Research pass: the national and largest collections

# DE_NATIONAL_NOTES.md — Germany's largest aviation collections

Research pass covering the twelve biggest published aviation collections in
Germany plus a top-up for the one German site already in the database.
Output directory: `/home/claude/de/national/`.

---

## 1. Files written

| file | rows | with serial | on_display | in_storage | under_restoration |
|---|---|---|---|---|---|
| `de_museums.csv` | 12 sites | — | — | — | — |
| `schleissheim_topup_aircraft.csv` | 93 | 59 (63%) | 92 | 0 | 1 |
| `gatow_aircraft.csv` | 153 | 134 (88%) | 83 | 70 | 0 |
| `hermeskeil_aircraft.csv` | 123 | 111 (90%) | 123 | 0 | 0 |
| `speyer_aircraft.csv` | 75 | 60 (80%) | 75 | 0 | 0 |
| `wernigerode_aircraft.csv` | 61 | 55 (90%) | 61 | 0 | 0 |
| `bueckeburg_aircraft.csv` | 61 | 39 (64%) | 61 | 0 | 0 |
| `sinsheim_aircraft.csv` | 59 | 49 (83%) | 59 | 0 | 0 |
| `deutsches_museum_aircraft.csv` | 48 | 29 (60%) | 33 | 15 | 0 |
| `dtm_berlin_aircraft.csv` | 44 | 33 (75%) | 43 | 0 | 1 |
| `laatzen_aircraft.csv` | 39 | 18 (46%) | 39 | 0 | 0 |
| `dornier_aircraft.csv` | 24 | 20 (83%) | 24 | 0 | 0 |
| `mhm_dresden_aircraft.csv` | 5 | 0 (0%) | 5 | 0 | 0 |
| `zeppelin_friedrichshafen_aircraft.csv` | 2 | 1 (50%) | 2 | 0 | 0 |
| **total aircraft rows** | **787** | **608 (77%)** | | | |

Validation run over the finished files: every `role_type` is in the permitted
vocabulary; every `aircraft_type`, `military_civilian` and `display_status` is
a valid enum; `wing_type` is set for every fixed-wing row and blank for every
other row; every alias is ≤34 characters, ≤4 words and comma-free with the
dashless form present; **no `tail_number` is duplicated within a file, and none
is duplicated across the thirteen files**. No `year_built` holds a serial.

The Schleissheim top-up uses `museum_name` = `Deutsches Museum Flugwerft
Schleissheim` exactly and Schleissheim is deliberately **absent** from
`de_museums.csv`.

---

## 2. Sources and how much weight each carried

**Rung 1 — a structured feed from the museum.** None of these twelve museums
publishes one. The Technik Museum Sinsheim/Speyer "Exponate" catalogue
(`technik-museum.de/de/entdecken/exponate/`) is a curated highlights list of
174 objects across both sites, not an inventory, and the per-exhibition
listings (`.../ausstellungen/flugzeuge-speyer/`) load their object grids from
JavaScript that returns only four items to a plain fetch. Probed and rejected.

**Rung 2 — the museum's own collection pages.** Used as the spine wherever one
exists:

- **Deutsches Museum**: `deutsches-museum.de/flugwerft-schleissheim/ausstellung/exponate`
  is a complete, museum-authored exhibit index for the Flugwerft (marked
  "Änderungen vorbehalten"). The Museumsinsel pages `.../historische-luftfahrt`
  and `.../moderne-luftfahrt` give the hall composition ("ca. 690 Objekte,
  davon 16 vollständige Flugzeuge"; "10 Flugzeuge und 6 Hubschrauber") and
  named highlights. These decided every Munich attribution where sources
  conflicted.
- **Luftfahrtmuseum Laatzen-Hannover**: `luftfahrtmuseum-hannover.de` →
  *Unsere Flugzeuge* is a full museum-written roster, hall by hall. It is the
  only source that distinguishes airframes from the museum's many **Großmodelle**
  (large scale models) — see the exclusions below. It won outright over
  third-party lists here.
- **Luftfahrtmuseum Wernigerode**, **Hubschraubermuseum Bückeburg**,
  **Flugausstellung Hermeskeil**, **Zeppelin Museum**: their sites confirm
  address, opening status and headline counts but publish no per-airframe list.
- **MHM Gatow** (`gatow.mhmbw.de`): the site has *no* collection listing at all
  despite the brief's expectation. Verified by crawling the whole navigation.

**Rung 3 — airframe listings.** `aviationmuseum.eu` (Z.A.P.P. / Rob Vogelaar)
carried this pass. It publishes a two-column type/serial table per museum, and
for Gatow it is explicitly dated "Visit 2022" and split into a display list
(69 airframes) and a stored list (72). That table is the backbone of the Gatow,
Speyer, Sinsheim, Hermeskeil, Wernigerode, Bückeburg, DTM Berlin and Dornier
files. **Important caveat on how it is encoded:** the serial column and the type
column are two separate table cells, each a run of paragraphs, so a row is only
correct if both runs have the same length. I parsed the raw HTML cell-by-cell
rather than trusting rendered text, and checked alignment against known anchors
(D-ABYM = the Speyer 747; XE656 = the Speyer Hunter; F-BVFB = the Sinsheim
Concorde; CCCP-77112 = the Tu-144; 74-0109 = the F-15A). **The Speyer table is
mis-aligned in its first seven entries** (two identifiers share one paragraph);
that block was realigned by hand and is flagged per row below. A generic
summarising fetch of the same page returns badly scrambled pairs — do not use
one.

**Rung 4 — German Wikipedia.** `Militärhistorisches Museum Flugplatz
Berlin-Gatow` carries a large sourced table but is dated "Stand April 2018" and
proved partly stale: it shows nine airframes as *verliehen nach Rechlin*
(Bücker Bü 181, DFS 230, Fokker D.VII/Dr.I/E.III, Junkers J 9, Etrich-Rumpler
Taube, Bf 109 G-2, Siemens-Schuckert D.III), the Ju 52 as a permanent loan to
Wunstorf, the An-14 to Cottbus, the MiG-21bis 24+53 to Neuhardenberg and the
Do 29 to Friedrichshafen. The 2022 survey lists **none** of the Rechlin group,
which corroborates the loans; but it *does* list the An-14 (995) at Gatow, so
that one Wikipedia claim is treated as superseded. `Flugwerft Schleißheim`
lists types without a single serial and includes several aircraft the museum's
own index does not (An-2, Yak-50, MiG-23BN, Ka-26, Fi 156, VFW 614, Saab
Draken, HA-300, HF-24 Marut); the ones with independent serial evidence were
kept, the rest are open questions (§6). `Technik-Museum Speyer` and
`Technik-Museum Sinsheim` have no aircraft list worth the name; the English
articles are worse.

**What I did not use.** `web.archive.org` is blocked by this environment's
egress policy, so no snapshot-versus-live currency diffing was possible. That
is the single biggest weakness of this pass: presence is asserted from lists
dated 2018–2026, not from dated photographs.

---

## 3. Corrections and conflicts resolved

**One aircraft, one place.** Four serials appeared in two museums' lists and
were resolved rather than duplicated:

| serial | claimed by | resolution |
|---|---|---|
| `798` (Su-22M-4) | Gatow, Sinsheim | Kept at **Gatow** — German Wikipedia independently gives Su-22M-4 25+44 *ex 798* on the Gatow Freigelände. The Sinsheim aircraft is recorded as **25+20** with the 798 claim explained in its `description`. |
| `40+26` (Alpha Jet) | Gatow reserve, Speyer | Neither has independent corroboration. Kept at **Gatow**; the Speyer Alpha Jet is recorded with a **blank** serial and the clash written into its description. |
| `21+53` (F-104) | Deutsches Museum, Flugwerft Schleissheim | Kept at **Schleissheim**, whose own exhibit index lists "Lockheed F-104G Starfighter, 1963". The Museumsinsel Starfighter is recorded with a **blank** serial, because the museum describes its exhibit as "eine in den USA gebaute Ausbildungsmaschine" — a US-built *trainer*, which points to an F-104F, not a licence-built G. Unresolved; see §6. |
| `106` | DTM Berlin (Noralpha c/n), Wernigerode (Lim-2) | DTM's is a construction number, not a displayed serial; blanked there, kept at **Wernigerode**. |
| `29+03` | Gatow MiG-29G, Gatow stored F-104F | Both codes genuinely exist in the Bundeswehr system. Kept on the **MiG-29G** (corroborated by Wikipedia: ex-NVA 615 → 29+03); the stored F-104F is recorded serial-blank. |
| `D-EBCQ` (LF 1 Zaunkönig) | Schleissheim, Sinsheim | Kept at **Schleissheim**, where the Deutsches Museum's own page lists a Zaunkönig among its research aircraft. The Sinsheim Zaunkönig is serial-blank. |
| `D-AQUI` (CASA 352L) | Speyer, Sinsheim | Kept at **Sinsheim**, whose entry is internally consistent (CASA C-352L in Lufthansa colours). Speyer's Ju 52 (CASA 352L) is serial-blank. |
| `83+17` / `PT+TP` / `DE623` / `D-EBUC` / `D-9506` / `393` / `OK-02` / `D-ENTE` | within one museum's own list | Each is a source repeat — the same airframe listed twice under two names (H-21C = "Vertol H-21C"; Ikarus Kurir = "Fieseler Fi 156 Storch (Kurir L)"; Merckle SM-67 twice), or a serial copied onto the wrong neighbour. Merged or blanked, with the reason in `description`. |

**Aircraft that have moved between these museums** (the brief asked for these
explicitly):

- **Dornier Do 29 V1** `YA+101` / `VA+101` — Gatow → **Dornier Museum
  Friedrichshafen**, permanent loan, moved 2018. Recorded at Friedrichshafen.
- **Douglas C-47B `A65-69`** (ex-RAAF) — owned by the **Deutsches Technikmuseum
  Berlin**, displayed **at Gatow** in front of the tower. Recorded at Gatow.
  The DTM's own Berlin Airlift C-47B `45-0951`, mounted on the museum roof, is a
  different airframe and is recorded at DTM.
- **Halberstadt CL.IV `D-IBAO`** — DTM Berlin property, recorded **at Gatow**
  (Hangar 3) per Wikipedia. The DTM keeps a second Halberstadt, the **CLS.1**
  (Wnr 3441, `TV+UB`), which is recorded at DTM. If a visitor finds only one
  Halberstadt in Berlin, this is the row to re-check.
- **CASA 2.111** `G1-AD` at Gatow was on loan to Museum Rotterdam until
  25 October 2015 and was rebuilt to He 111 configuration on return.
- **Sojus 29 descent capsule** — MHM Dresden → Deutsches Museum München on
  multi-year loan → **back at Dresden**. Recorded at Dresden.
- **Fieseler Fi 156 Storch `A-96`** — recorded at the **Museumsinsel**
  (Historische Luftfahrt describes a Fi 156 in the hall); German Wikipedia still
  lists a Fi 156 C at the Flugwerft. Treated as a move into the 2022 hall.
- **Nine Gatow airframes are on loan to the Luftfahrttechnisches Museum
  Rechlin**, one to the Ju-52-Museum of LTG 62 Wunstorf, one to Neuhardenberg
  (MiG-21bis 24+53). All excluded from `gatow_aircraft.csv`; see §7.
- **Dornier Do 31**: prototype **E1** (`D-9530`) is at the Dornier Museum,
  prototype **E3** (`D-9531`) at Schleissheim. Two aircraft, not one.
- **Musculair 1** (Deutsches Museum store) and **Musculair 2** (Schleissheim,
  on display) are likewise two aircraft.

**Deutsches Museum, Museumsinsel — what actually reopened.** The aviation hall
reopened on **8 July 2022** with two exhibitions stacked in it: *Moderne
Luftfahrt* on level 0 (aviation since 1945; ten aircraft and six helicopters
among ~500 objects) and *Historische Luftfahrt* on level 1 and the mezzanine
(1918–1945; 16 complete aircraft among ~690 objects), with *Raumfahrt* on
level 2. The museum's **pre-1918 collection is not exhibited**: a third hall,
*Historische Luftfahrt bis 1918*, is planned for **2028**, and the museum says
the original Lilienthal Normal-Segelapparat — currently being restored in a
dedicated studio at the Flugwerft, where visitors can watch — will be moved to
the Museumsinsel for it. Fifteen Museumsinsel rows are therefore marked
`in_storage` (Wright Model A, two Lilienthal gliders, Blériot XI, Grade,
Etrich-Rumpler Taube, Rumpler C.IV, Parseval PL.2 gondola, Fokker Dr.I, and
six others that could not be tied to either open exhibition). Marking them
`in_storage` is a deliberate visitor-truth call: they are real holdings that
cannot currently be seen.

**Replicas and reproductions** are flagged in plain English in `description`
("This exhibit is a replica/reproduction, not an original airframe") and their
worn markings are moved out of `tail_number` into `aliases`, so that two
replicas wearing the same First World War marking (e.g. Fokker Dr.I `152/17` at
both Speyer and Hermeskeil, `425/17` at Laatzen and the Deutsches Museum) can
never collide on import. Replica rows in this pass: Farman III and Junkers D.I
(Gatow), Avro 504K (Gatow), Wright Model A and two Fokker Dr.I and a Pfalz D.III
and an Me 262 mock-up (Speyer), Avro 504K, Fw 190 A-3, Fokker E.III, Nieuport 11
and a BK 117 mock-up (Sinsheim), Concorde nose, Blériot XI, Fokker Dr.I and
Landmann La.11 (Hermeskeil), Fw A 16 and a Lilienthal flapping-wing machine
(DTM Berlin), Dornier Merkur and Do J Wal (Dornier Museum), Udet U 12, Lilienthal
Normalsegelapparat, Chanute glider, Grade monoplane, Otto biplane and the
Pelzner hang glider (Schleissheim), and eleven of the Laatzen airframes.

**Cockpit, nose and section rows** are recorded as their own rows with the fact
stated in `description`: 12 cockpit sections at Wernigerode and Gatow, the
Hermeskeil Harrier GR.3, Lightning F.53, MiG-21SPS-K and S-64 Skycrane cockpits,
the Sinsheim Nimrod R.1 and RF-84F front fuselages, the DTM Lancaster wing,
Go 242 frame, Fw 200 fuselage sections and Il-2 nose, the Laatzen Halberstadt
CL.IV rear fuselage and Ju 52 fuselage segment, and the Bf 110D wings at Speyer.

---

## 4. Judgment calls

- **The Zeppelin Museum Friedrichshafen holds no complete aircraft.** Its
  centrepiece is a 33 m **reconstruction** of the LZ 129 Hindenburg passenger
  section, walk-through, in Bauhaus fit-out. I recorded it as one
  `lighter_than_air` row with the reconstruction status stated flatly, plus a
  second row for the largest surviving **original** Hindenburg wreck part, the
  rudder bearing arm, displayed inside it. A visitor going there for airframes
  should know this before travelling; two honest rows say so better than an
  empty file or an inflated one.
- **MHM Dresden holds no complete aircraft either.** Its aviation-adjacent
  large exhibits are the A4 (V-2) rocket — largely original components with
  reproduction parts, notably the air rudders, impaled through Libeskind's
  glass wedge — a separate original A4 combustion chamber from the Mittelwerk
  tunnels, the Sojus 29 descent capsule, an MGR-1 Honest John, an AS.30 and a
  Propagandagranate 41. Five rows, no serials: none of these carry a displayed
  identity. A P-51 Mustang wing section is also exhibited; a bare wing is below
  the threshold for a row and is recorded here instead. The Bundeswehr's
  aircraft collection is at Gatow, which is an outstation of Dresden.
- **Hang gliders and ultralights are in.** Schleissheim's Pelzner, Huber
  Alpengleiter, Super Gryphon, Laser 12.8 and Exxtacy, and Laatzen's Windspiel,
  Dallach and FFB Flamingo, are exhibited airframes in a sport-aviation display
  and are recorded as `fixed_wing` / `private`.
- **Rockets and missiles are in**, per the brief. Gatow contributes 14 such rows
  (Nike Hercules, Hawk, Patriot, S-75, S-125M, S-200, Roland 2, Matador,
  Pershing 1A, Fritz X, Hs 293, CL-89, TUCAN-95, Q2), Schleissheim the complete
  three-stage **Europa** launch vehicle — the only intact example anywhere.
  **Radar sets, flak guns and ground support vehicles are out**: FuMG 65
  Würzburg-Riese, AN/TPS-43, Tamara, Ramona, ASR-B, PAR-C, the 8.8 cm Flak, the
  ZU-23/2, the Bofors and the Hawk XM501 loader are all at Gatow and are all
  omitted as not airframes. Named here so the omission is a finding.
- **Spacecraft**: Buran OK-GLI, Soyuz TM-19 and BOR-5 at Speyer; Sojus 29 at
  Dresden. `aircraft_type` = `spacecraft`, `role_type` = `space`.
- **Access type** is `public` for all twelve. Hermeskeil is **seasonal**
  (1 April – 1 November, Tue–Sun from 2026); that belongs in a visit note rather
  than in `access_type`, which has no seasonal value.
- **Serial plausibility filter.** Where the source's type/serial pairing is
  impossible for the type or the operator — a German glider registration against
  an Indian HF-24, a Danish civil registration against a Soviet Su-22, `75+00`
  (an Alouette II block) against a Fiat G.91, `D-EDSF` against an Mi-24 — the
  serial was **dropped**, not guessed at, and the reason written into
  `description`. Fifteen rows lost a serial this way. That is the main reason
  coverage is 77% and not 90%.

---

## 5. Excluded, and why

- **Deliberately not added to `de_museums.csv`: Deutsches Museum Flugwerft
  Schleissheim** — already in the database; delivered as a top-up file.
- **Luftfahrttechnisches Museum Rechlin, Flugplatzmuseum Cottbus,
  Ju-52-Museum Wunstorf, Museum Neuhardenberg** — real sites holding real
  airframes, but out of this assignment's scope. Listed as leads (§7).
- **Laatzen "Großmodelle"** — the museum's own list marks a dozen exhibits as
  large scale models, and third-party listings quietly treat several of them as
  airframes. Excluded by name: the Montgolfier balloon model, the 1:48 Zeppelin
  L 1927, Akaflieg Hannover Vampyr (Großmodell), Schempp-Hirth Minimoa,
  Blériot XI, Klemm Kl 26, a second Fokker Dr.I, DHC-1 Chipmunk, the 1:1.8
  Messerschmitt **Me 209 V1**, the Eurocopter Tiger, and the roughly twenty
  further Großmodelle (Fw 187, Do 335, Me 163, He 111, Hs 129, Ju 88, Ju 87,
  Fw 190 A-3/D, Bf 109 E, P-51 D, F-86, PA-18). `aviationmuseum.eu` lists the
  Me 209 V1 as a "1:4 replica" and a "Levasseur Antoinette" that the museum
  does not mention at all — both excluded.
- **The MiG-21 on a pylon at Karlsruher Straße / Ulmer Straße, Laatzen** — it
  belongs to the Luftfahrtmuseum and serves as a signpost to it, but it stands
  off the museum site on a public street and is a plinth monument. Excluded from
  the museum file per the brief; passed on as a lead (§7).
- **Albatros D.III `253.24`** and **Wagner DOWA 81 `I.B.4/13`** at Schleissheim
  — listed by `aviationmuseum.eu` under the Flugwerft but on neither the
  Deutsches Museum's exhibit index nor German Wikipedia. The DOWA 81 is recorded
  once, at the Museumsinsel and `in_storage`, with the conflict stated; the
  Albatros is left out entirely rather than invented into a hall.
- **Four orphan glider registrations** at the end of the Schleissheim source
  table (`BWLV 98`, `D-1065`, `D-1085`, `D-8287`) have no type against them and
  are excluded.
- **Engines, propellers and simulators** everywhere. The Deutsches Museum's
  40-odd piston, jet and turboprop engines, the Laatzen Motorensammlung, the
  Gatow engine hall, the DA 42 simulator and the Wernigerode Bf 109/UH-1D
  cockpit simulators are all out of scope.
- **Aircraft parts below the section threshold**: the MHM Dresden P-51 wing, the
  Deutsches Museum's Ariane 5 booster segment and A4 rocket motor, the Airbus
  A350 XWB fuselage section and the Boeing 707 / A320 cockpits in Moderne
  Luftfahrt. The A300B fuselage section **is** recorded, because it is the first
  A300 and is presented as an aircraft; the two airliner cockpits are presented
  as flight-deck demonstrators and are not.

---

## 6. Needs a human on site, ranked

1. **Which Starfighter is where in Munich?** Does the Flugwerft Schleissheim
   hold F-104G `21+53` and the Museumsinsel an F-104F (`29+03`?), or the other
   way round? The Museumsinsel row currently carries no serial. One photograph
   of each placard settles it.
2. **Gatow: is the 2022 stored list still stored, and still there?** Seventy
   rows are marked `in_storage` on the strength of one survey. Hangar 4 was
   being converted to permanent exhibition space from 2018 and the museum has a
   published *Neukonzeption*; some of those 70 may now be on view and some may
   have gone out on loan. Also: does the Halberstadt CL.IV `D-IBAO` stand at
   Gatow or back at the Deutsches Technikmuseum?
3. **Speyer's first seven entries.** The source table merges identifiers there.
   Specifically: is the Beech E50 Twin Bonanza `D-ITMS`, and is the Bell Sioux
   AH.1 `XT120` ex-`D-HAFC` or the other way round? And is the L-39ZO really
   coded `08+28`?
4. **Does the Flugwerft Schleissheim still hold the Wikipedia-only aircraft?**
   An-2, Yak-50 `DDR-WQV`, Ka-26 `D-HOAZ`, MiG-23BN `20+47`, Bo 209 Monsun,
   Let Z-37 — all present here on third-party evidence but absent from the
   museum's own 2026 exhibit index. Conversely Wikipedia lists a Saab J 35
   Draken, a Hispano HA-300, an HF-24 Marut, an F-4E Phantom and a VFW 614 at
   Schleissheim that no other source supports; those are **not** in the file.
5. **Is the Speyer Ju 52 one aircraft or two?** The source shows both a CASA
   352L and a Ju 52/3m g4e (`6821`, code `CA-JY`) at Speyer while Sinsheim has
   three CASA 352Ls. Four Ju 52-family airframes across two sister museums is
   plausible but unverified.

---

## 7. Leads for other agents

Sites encountered while resolving loans and conflicts, all out of this
assignment's scope:

- **Luftfahrttechnisches Museum Rechlin** (Mecklenburg-Vorpommern) — holds nine
  Gatow loans: Bücker Bü 181, DFS 230 (repro), Fokker D.VII / Dr.I / E.III
  (repros), Junkers J 9 / D.I (repro), Etrich-Rumpler Taube (repro),
  Messerschmitt Bf 109 G-2 (rebuilt from a Spanish HA-1109 K-1-L with a
  Hispano-Suiza engine), Siemens-Schuckert D.III (repro).
- **Ju-52-Museum / Museum des LTG 62, Wunstorf** (Niedersachsen) — holds the
  Gatow **Junkers Ju 52/3m g4e** on permanent loan. Likely `restricted`, inside
  a Luftwaffe base.
- **Flugplatzmuseum Cottbus** (Brandenburg) — Wikipedia places the Gatow
  **An-14 `996`** there; the 2022 Gatow survey lists an An-14 `995` at Gatow.
  Two aircraft or one? Worth a look either way; Cottbus is a substantial ex-NVA
  collection in its own right.
- **Museum Neuhardenberg** (Brandenburg) — Gatow's **MiG-21bis `24+53`, ex NVA
  990**.
- **MiG-21 monument, Karlsruher Straße / Ulmer Straße, Laatzen** — on a pylon
  as a signpost to the Luftfahrtmuseum. A plinth site for the monuments agent.
- **Luftwaffenmuseum Uetersen / Fliegerhorst Uetersen-Heist**
  (Schleswig-Holstein) — the collection Gatow grew out of; check what remained.
- **Verkehrsmuseum Dresden**, **Technikmuseum Hugo Junkers Dessau**
  (Sachsen-Anhalt), **Zeppelin Museum Zeppelinheim** (Hessen), **Zeppelin
  Museum Meersburg** and **Albert-Sammt-Zeppelin-Museum** (Baden-Württemberg),
  **Schwäbisches Bauern- und Technikmuseum Seifertshofen** — all carry aircraft
  and all sit outside this assignment.
- **Lufthansa Super Constellation**: `D-ALIN` is recorded at Hermeskeil in this
  pass; Lufthansa's own airworthy-restoration Connie is a separate airframe and
  a separate site question.
- **Flugwerft Schleissheim's glass workshop** restores objects for the whole
  Deutsches Museum aviation collection, including the original Lilienthal
  Normal-Segelapparat, which will move to Munich in 2028. Whoever revisits
  Munich after 2028 should expect several rows to change site.


---

# Research pass: the ex-NVA east

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


---

# Research pass: the north-west

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


---

# Research pass: the south

# DE-SOUTH — Bayern, Baden-Württemberg, Hessen, Rheinland-Pfalz, Saarland

Output directory: `/home/claude/de/south/`
Files: `de_museums.csv` (58 sites) + 58 `<slug>_aircraft.csv` files (323 airframes,
266 with a tail number / tactical code — 82 % serial coverage).

---

## Sources and how much weight each carried

**Rung 1 — the site's own publication.** Used where it exists: the Bundeswehr
`zms.bundeswehr.de` Museums- und Sammlungsverbund pages (Kaufbeuren TAZLw,
Fürstenfeldbruck TG Fursty, Laupheim HSG 64, and Wunstorf LTG 62 which turned out
to be in Niedersachsen and is not mine); `jabog34allgaeu.de`; `munich-airport.de`;
the Lufthansa Group newsroom for Hangar One; `mgs-lechfeld.de`; `f-104.de`.
These win on "what is here now" and I preferred them over lists.

**Rung 2 — two specialist F-104 registers, both current.**
- `i-f-s.nl` "Preserved in Germany" (International F-104 Society). Entry-by-entry,
  with 2024 and 2025 sightings noted in the text (e.g. Memmingen 24+17 "repainted
  late April 2024", Köln-Wahn 23+98 "since June 2025"). This is the single best
  currency source I found for Germany.
- `916-starfighter.de/F-104_GAF_fate_quicklist.pdf`, the German F-104 fate list,
  with "NEW" flags on 2024–25 changes (23+92 moved to Bad Wildungen; 24+85 to
  Wittmund; 28+22 sold August 2025).
Between them these two carry most of the 39 Starfighter rows in this set and are
the reason serial coverage is as high as it is. **They disagree with German
Wikipedia repeatedly, and where they do I followed them** (see corrections below).

**Rung 3 — `aviationmuseum.eu`.** Per-museum inventories with registration/type
pairs from photo surveys. It is by far the widest net for the small German
museums and supplied the bulk of the non-Starfighter rows. It is *not* reliable
on individual identities — see "Known bad data" — and it carries no visit dates,
so every collection sourced only from it says so in `description`.

**Rung 4 — German Wikipedia** `Liste von Luftfahrtmuseen` was used only to
enumerate candidate sites, never as an aircraft-level fact. It proved stale in
both directions: it lists the Albatros-Flugmuseum Stuttgart (closed), the Albert
Sammt Zeppelin Museum (closed) and Red Stars Bensheim (closed) as if current, and
it omits Luftraum Süd's real inventory, the Lufthansa Hangar One, and every
Bundeswehr traditions collection in the five Länder.

The English Wikipedia `List of surviving Lockheed F-104 Starfighters` is badly
incomplete for Germany (23 entries against ~90 real ones) and
`List of displayed McDonnell Douglas F-4 Phantom IIs` lists five German Phantoms
where there are certainly more. Neither was used as a source of record.

---

## Corrections made, with the evidence

- **F-104G 22+58.** German Wikipedia puts it with the Traditionsgemeinschaft
  JaboG 34 at Memmingen. Both F-104 registers put it indoors at Motorworld
  Böblingen, privately owned by Robert Dietz, wearing the tail of 23+26, and
  note that the venue was renamed from "Meilenwerk" in January 2014 — detail a
  copied list would not carry. Recorded at Böblingen. The Memmingen Starfighter
  is recorded as **20+98 in the false code 20+05**, which is what both registers
  say. The JaboG 34 website does still link a page about 22+58, so this is the
  one conflict I could not close; both rows say so.
- **F-104G 21+53** (Deutsches Museum, Munich) and **F-104F 29+03**. The registers
  record that 21+53 moved to Oberschleißheim in April 2016 and will not go back,
  and that 29+03 went to the Munich Luftfahrthalle in June 2022. Both sites are
  excluded from my assignment; noted here as a lead so the Munich agent gets the
  swap the right way round.
- **F-104G 25+99** was at the Zollernalb-Kaserne in Meßstetten until September
  2014; it has been at the Stetten am kalten Markt collection since end 2016. It
  is recorded at Stetten, not Meßstetten.
- **RF-104G 23+92** left PS Aero at Baarlo (NL) in **August 2024** for the Krausz
  yard at Bad Wildungen-Wega. Recorded in Hessen, not the Netherlands.
- **Grenzmuseum Schifflersgrund** is listed under Hessen by German Wikipedia. Its
  address is Platz der Wiedervereinigung 1, **37318 Asbach-Sickenberg**, which is
  in **Thüringen**. Not recorded here — handed to the eastern agent (see Leads).
- **Munich Besucherpark.** aviationmuseum.eu lists four aircraft including
  Bo 105S D-HILF. The airport's own 2025 page names three historic aircraft
  (Super Constellation, C-53, CASA 352L). I recorded the three the airport names
  and left the Bo 105 out.

## Known bad data in aviationmuseum.eu, and what I did about it

- **Museum Kiemele, Seifertshofen** — the listing gives "McDonnell F-101D Voodoo
  85-0701/SP". There is no F-101D, and 85-0701 is an F-4 serial block; the /SP
  tailcode is Spangdahlem. The row is kept as an F-101 with **no serial** and a
  description saying the identification is not credible.
- The same listing gives MiG-15 "1973" and MiG-21F-13 "1981". Those read as years.
  **1981 is also the serial the same site gives the MiG-21F-13 at the Pflumm
  museum.** I kept 1981 on the Pflumm row (where it is quoted with Hungarian Air
  Force attribution, which fits) and left both Seifertshofen rows blank.
- **Pflumm, Schwenningen** — two SG 38s are both given D-7033, and D-7033 is the
  registration of the Reiher III at the Wasserkuppe. Neither Schwenningen row
  carries a registration.
- **Pflumm** — photo captions on the same page name a Do 27 D-EMKA and a Do 27B1
  D-EJJJ and an "F-86K BB-141" while the inventory table gives Do 27B-2 D-EFFA,
  Do 27B-3 D-ELTT and "Canadair CL-13 Sabre 5 BB+141". I followed the table. BB+1xx
  is the Luftwaffe Canadair Sabre Mk 5 block, not the F-86K block (JD+), so
  Canadair is right and the caption is wrong; the F-86K claim is noted in the row.
- **AMF Fichtelberg** — "Schneider Sch-2 Fledermaus D-HBAT". A D-H registration is
  a helicopter; the type name is not one I can confirm. Kept with the registration
  and an explicit "identification unverified" note.
- **Pflumm** — "Mifka Mi-1 D-HMIA" is not a Mil Mi-1; recorded as listed with a
  description saying so, so it cannot be mistaken for the Soviet type.

## Judgment calls

- **Cockpit and nose sections** are recorded as their own rows and every one says
  "cockpit section only" in `description`: F-104G 24+11 and Fiat G.91T 34+13 at
  Söllingen; F-104G 21+83 at Neuburg; RF-104G 24+49 at Niederalteich; RF-104G
  25+07 at Roth; F-104G 26+25 at Kaufbeuren; TF-104G 27+26 at Memmingen; Convair
  240 N87982 and DC-8 fuselage 5A-DGK at Griesheim; MiG-21MF 23+38 fuselage at
  Bad Wörishofen.
- **Replicas and mock-ups** are recorded (they are what a visitor sees) with the
  replica status in `description`, never in `aliases`: the Do 335 at Schwenningen,
  the Bf 109 G-2 and Me 163/Me 262 at Manching, the Weißkopf No. 21 at
  Leutershausen, the Lilienthal gliders and the Vampyr at the Wasserkuppe, the
  Euler Nr. 33, Fokker Dr.I and "Spirit of St. Louis" at Griesheim, and the
  **MBB Lampyridae** at Niederalteich, which is a full-size manned mock-up that
  never flew.
- **Airworthy aircraft** are recorded where they live: the Messerschmitt Stiftung
  Bf 109 G-4 / G-10 at Manching, the Luftraum Süd warbirds at Elchingen. The
  Lufthansa Ju 52 D-AQUI is recorded at Hangar One because it is retired from
  flying and is now the permanent exhibit there.
- **`access_type`.** 33 `public`, 11 `appointment`, 14 `restricted`. Gate
  guardians visible from a public road are `public` (Büchel Torwächter, Haldenwang,
  Aich, Haßfurt, Ummendorf, Lahr, Söllingen, Speyer Pfalz-Flugzeugwerke, Stuttgart
  roof, Allgäu Airport). Airframes inside a Bundeswehr or USAFE perimeter are
  `restricted` (Fliegerhorst Lechfeld, Manching, Roth, Büchel, Neuburg,
  Fürstenfeldbruck, Erding/WIWeB, Germersheim, Brauheck, Neubiberg, Memmingen
  barracks, Ramstein). Bad Wildungen-Wega is `public` because the aircraft are
  explicitly described as visible from the main road although the yard is not open.
- **Büchel is split into two site records** — `Fliegerhorst Büchel Torwächter`
  (public, 21+67) and `Fliegerhorst Büchel` (restricted, the instructional 26+26)
  — because a visitor can reach one and not the other.
- **Fürstenfeldbruck** is recorded as one site covering both the plinth aircraft
  spread across the former airfield and the TG Fursty collection in the Captain
  Richard Higgins building, since they are the same visit.

## Blank fields left deliberately

- `latitude`/`longitude` are blank everywhere except the Wasserkuppe. Every record
  carries a five-digit PLZ, which the brief says geocodes precisely; I did not
  invent pins.
- `year_built` is filled only four times (Munich Constellation 1957, C-53 1941,
  CASA 352L 1949, Frankfurt C-54 1945, Penzing Noratlas 1956) where a build or
  roll-out date was published.
- 57 rows have no `tail_number`. The largest blocks are the seven
  Fürstenfeldbruck plinth aircraft, five of the six Laupheim helicopters, the
  three JaboG 34 types and 12 unregistered gliders/replicas at the Wasserkuppe.
  In every case the description says the serial is not published.

---

## Excluded, and why — named

**Out of scope by assignment** (another agent has them): Deutsches Museum München,
Deutsches Museum Flugwerft Schleißheim, Technik Museum Speyer, Auto- und
Technikmuseum Sinsheim, Flugausstellung Hermeskeil, Dornier Museum Friedrichshafen,
Zeppelin Museum Friedrichshafen.

**Deutsches Museum Verkehrszentrum, München** (Bo 105C D-HDDX). A third Deutsches
Museum site in Munich. Left out as part of the Deutsches Museum exclusion; flagged
as a lead so it is not lost.

**No airframe held** — checked, nothing to record:
- Zeppelin-Museum Zeppelinheim, Neu-Isenburg — permanent exhibition of airship
  history, models and artefacts, no airframe.
- Zeppelinmuseum Meersburg — same.
- Ballonmuseum Gersthofen — ballooning history; no gas or hot-air envelope
  recorded as a preserved airframe on its own pages.

**Closed**:
- Albatros-Flugmuseum, Flughafen Stuttgart — German Wikipedia's own note is
  "geschlossen".
- Albert Sammt Zeppelin Museum, Niederstetten — closed; held photographs and
  models only.
- Red Stars Museum, Schillerstraße 76, Bensheim (Hessen) — closed. Its former
  collection was substantial and ex-Warsaw Pact (L-39ZO 122, L-410MA 0402, MiG-17F,
  MiG-21UM 23+81, MiG-23UB 20+61, Mi-8T 94+23, Mi-24, TS-11 Iskra 324, Su-20
  6137/20, Mi-2 SP-SAI). Where those airframes went is the single biggest open
  question in this region — see below.
- Sammler & Hobbywelt Collection, Kiesacker 5, 35418 Buseck (Hessen) — "closed, no
  aircraft". Its former collection included Mirage IIIE 499, Mystère IVA 191,
  Fiat G.91R/1 32+58, Fouga CM.170 MT48, three T-33s, F-104F 29+14, MiG-21bis
  24+25, MiG-21MF 91+05, Mi-8T ZS-RUB and Whirlwind XG576. **29+14 is now at
  Eschbach** and is recorded there; the rest are unlocated.

**No public access** — deliberately not recorded as sites:
- F-104G 22+67 (fuselage and tail), privately stored at Rednitzhembach, Bayern.
- F-104G 26+20 cockpit, privately owned at Augsburg.
- F-104G 26+17 cockpit, private collector in Kaiserslautern.
- F-104G 23+27 "KG-101" and F-104G 23+76 "22+90", both sold to unnamed private
  owners in the Stuttgart area / elsewhere in Germany; location unknown.
- F-104G 25+87, "inside a private collection at unknown location".

**Checked and nothing found** (recorded here so the gap is a finding, not an
omission): Heeresflugplatz Fritzlar (Hessen); Heeresflugplatz Niederstetten
(Baden-Württemberg); Flugplatz Aschaffenburg-Großostheim; a "Flugplatzmuseum
Bayreuth" — no such museum is traceable; Spangdahlem, Bitburg, Hahn, Zweibrücken,
Sembach and Pferdsfeld (Rheinland-Pfalz) — no preserved airframe confirmed at any
of them; and **the whole Saarland**, where I could not confirm a single preserved
airframe on public display. The Saarland result should be treated as unproven
rather than proven negative.

**Uncertain, left out**: Museum Flugsicherheit und Rettung, Baden Airpark,
77836 Rheinmünster (a MiG-21 cockpit). aviationmuseum.eu's own note is "We don't
know if the museum is still open". Not recorded rather than recorded wrongly.

---

## Ranked "needs a human on site"

1. **Where did the Red Stars Bensheim collection go?** Ten ex-Warsaw Pact
   airframes, including a Mi-24 and an Su-20, vanished from the record when the
   museum on the Sanner works site closed. Nothing in this region matters more.
2. **Fürstenfeldbruck plinth serials.** Seven airframes recorded with blank tails.
   They are also politically live: the Bund offered them to the town in 2023 and
   the Bundeswehr returns to the site in October 2026 as a training location, so
   they may move. Somebody should read the codes before they do.
3. **Memmingen: is the shelter Starfighter 20+98 or 22+58?** Both registers say
   20+98/"20+05" at Memmingen and 22+58 at Böblingen; the association's own site
   references 22+58. One reading of the nose settles it.
4. **Laupheim HSG 64 serials.** Six helicopters and a Do 27, only the CH-53G
   84+06 identified. Registration in advance is required anyway, so the same visit
   could capture all seven.
5. **Is the 24+11 cockpit at Söllingen or at Brauheck?** The museum lists one;
   the 916-starfighter list puts 24+11's cockpit with TaktLwG 33 at Cochem and its
   tail on 24+38 at Lahr. Recorded once, at Söllingen, with the conflict flagged.
6. Pflumm Schwenningen rotates its display — roughly 40 of ~90 airframes are out
   at a time. The 51 rows here are the published inventory, not a confirmed
   simultaneous sighting.
7. Bad Wildungen-Wega: the Fokker F27 (André Rieu's first aircraft) has no
   published registration, and two further aircraft plus a helicopter are
   mentioned without types.

---

## File and row counts

| file | rows | with tail |
|---|---:|---:|
| `august_euler_flugplatz_museum_aircraft.csv` | 10 | 6 |
| `besucherpark_flughafen_muenchen_aircraft.csv` | 3 | 3 |
| `cf104_denkmal_lahr_aircraft.csv` | 1 | 1 |
| `cf104_denkmal_soellingen_aircraft.csv` | 1 | 1 |
| `curioseum_willingen_aircraft.csv` | 5 | 4 |
| `dd_museum_moedlareuth_aircraft.csv` | 1 | 1 |
| `dt_fahrzeugmuseum_fichtelberg_aircraft.csv` | 10 | 10 |
| `dt_kanadisches_luftwaffenmuseum_aircraft.csv` | 7 | 7 |
| `dt_segelflugmuseum_wasserkuppe_aircraft.csv` | 62 | 50 |
| `f104_denkmal_ummendorf_aircraft.csv` | 1 | 1 |
| `fahrzeugmuseum_marxzell_aircraft.csv` | 3 | 3 |
| `fliegerhorst_buechel_aircraft.csv` | 1 | 1 |
| `fliegerhorst_buechel_torwaechter_aircraft.csv` | 1 | 1 |
| `fliegerhorst_lechfeld_aircraft.csv` | 3 | 3 |
| `fliegerhorst_manching_aircraft.csv` | 5 | 5 |
| `fliegerhorst_roth_aircraft.csv` | 2 | 2 |
| `fliegerhorstmuseum_jg74_neuburg_aircraft.csv` | 7 | 7 |
| `fliegerhorstmuseum_leipheim_aircraft.csv` | 11 | 10 |
| `fliegermuseum_bad_woerishofen_aircraft.csv` | 3 | 1 |
| `flugmuseum_messerschmitt_aircraft.csv` | 10 | 8 |
| `flugpioniermuseum_gustav_weisskopf_aircraft.csv` | 1 | 0 |
| `franks_fahrendes_militaermuseum_aircraft.csv` | 3 | 3 |
| `gerhard_neumann_museum_aircraft.csv` | 11 | 10 |
| `ilm_manfred_pflumm_aircraft.csv` | 51 | 42 |
| `lehrsammlung_tazlw_kaufbeuren_aircraft.csv` | 3 | 2 |
| `luftbrueckendenkmal_frankfurt_aircraft.csv` | 2 | 2 |
| `luftfahrzeugsammlung_bad_wildungen_aircraft.csv` | 2 | 1 |
| `lufthansa_group_hangar_one_aircraft.csv` | 2 | 2 |
| `luftraum_sued_aircraft.csv` | 20 | 20 |
| `memmingen_kaserne_tf104_cockpit_aircraft.csv` | 1 | 1 |
| `mgs_hsg64_laupheim_aircraft.csv` | 6 | 1 |
| `mgs_lechfeld_aircraft.csv` | 4 | 4 |
| `mgs_manching_aircraft.csv` | 1 | 1 |
| `mgs_stetten_am_kalten_markt_aircraft.csv` | 1 | 1 |
| `motorworld_boeblingen_aircraft.csv` | 1 | 1 |
| `muna_museum_marktbergel_aircraft.csv` | 2 | 2 |
| `museum_kiemele_seifertshofen_aircraft.csv` | 19 | 13 |
| `museum_stammheim_aircraft.csv` | 3 | 3 |
| `museum_zivil_wehrtechnik_uffenheim_aircraft.csv` | 1 | 1 |
| `pfalz_flugzeugwerke_speyer_aircraft.csv` | 1 | 1 |
| `point_alpha_rasdorf_aircraft.csv` | 2 | 2 |
| `ramstein_air_base_phantom_aircraft.csv` | 1 | 1 |
| `rolls_royce_museum_oberursel_aircraft.csv` | 2 | 2 |
| `starfighter_denkmal_aich_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_allgaeu_airport_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_brauheck_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_germersheim_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_haldenwang_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_hassfurt_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_neuburg_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_stuttgart_zuffenhausen_aircraft.csv` | 1 | 1 |
| `tg_fursty_fuerstenfeldbruck_aircraft.csv` | 7 | 0 |
| `tg_jabog34_allgaeu_aircraft.csv` | 3 | 1 |
| `tg_ltg61_penzing_aircraft.csv` | 1 | 1 |
| `traditionsverein_immelmann_eschbach_aircraft.csv` | 1 | 1 |
| `unibw_neubiberg_aircraft.csv` | 1 | 1 |
| `wehrtechnische_studiensammlung_koblenz_aircraft.csv` | 14 | 12 |
| `wiweb_erding_starfighter_aircraft.csv` | 1 | 1 |

**Total: 58 sites, 323 airframes, 266 with a tail number or tactical code (82 %).**
By Land: Bayern 30 sites, Baden-Württemberg 13, Hessen 8, Rheinland-Pfalz 7,
Saarland 0.

---

## Leads for other agents

- **Munich agent (Deutsches Museum / Flugwerft Schleißheim).** F-104G 21+53 moved
  from the Munich Luftfahrthalle to Oberschleißheim in April 2016 and is *not*
  going back; F-104F **29+03** has been in the Munich Luftfahrthalle since June
  2022. F-104G **20+90**'s cockpit is in store at Oberschleißheim. Also: the
  **Deutsches Museum Verkehrszentrum** in Munich holds Bo 105C **D-HDDX** and is
  not covered by anyone in my set.
- **Speyer agent.** The Technik Museum Speyer holds F-104G 22+01 (as "26+63", in
  Vikings colours), F-104G 25+66 (skin partly removed) and TF-104G 28+27 outside
  on stilts. Note that **F-104G 20+46 at the Pfalz-Flugzeugwerke on Speyer
  airfield is a different site** and is in my set, not theirs.
- **Sinsheim agent.** F-104G 22+49, last noted 14 October 2021.
- **Hermeskeil agent.** F-104G 20+43 (last noted 31 July 2021), RF-104G 24+91
  (bare metal, on a wall, very hard to photograph, at 49°41'6.7"N 6°57'37.4"E),
  F-104G 26+61 (lizard camouflage, no markings, in store) and Belgian FX60 with
  the tail of FX65.
- **Eastern agent.** `Grenzmuseum Schifflersgrund`, Platz der Wiedervereinigung 1,
  37318 Asbach-Sickenberg, **Thüringen** — UH-1D D-HAQI, Bo 105M 87+82, Mi-2
  D-HZPH/307, Mi-2RM 386, Mi-8TB 752, **Mi-24V 01**, Alouette II D-HBJA. German
  Wikipedia files it under Hessen; the address is Thuringian. Also F-104G 20+07
  in a private collection near Freiberg, Sachsen.
- **Northern agent.** `Militärgeschichtliche Sammlung Lufttransportgeschwader 62`
  is at Fliegerhorst Wunstorf, Zur Luftbrücke 1, 31515 Wunstorf: Ju 52/3m g4e and
  Do 28 indoors, Noratlas, Piaggio P.149, ex-NVA Mi-8, UH-1D and a walk-through
  Transall C-160D outdoors.
- **Whoever does the national/type sweeps.** `916-starfighter.de`'s German fate
  quicklist (PDF) and `i-f-s.nl`'s "Preserved in Germany" together give a
  near-complete, 2025-current census of every German Starfighter with location and
  false codes. Nothing else I found in this project comes close for a single type.
