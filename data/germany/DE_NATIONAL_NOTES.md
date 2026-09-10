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
