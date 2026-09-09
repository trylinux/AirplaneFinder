# Colombia – research notes (all three passes: museums, base collections, monuments)

Output directory: `/home/claude/sa/colombia/`. Museums file `co_museums.csv`; one `<slug>_aircraft.csv` per site;
`build.py` regenerates everything (edit the script, not the CSVs).

## Research conditions that shaped this file

The WebSearch budget for the session was exhausted (200/200, shared with the parallel agents) about a
third of the way into the Colombia sweep, and the fallback engines (Bing/Google/DDG/Startpage/Yandex via
curl) either bot-blocked or returned degraded results through the proxy. airhistory.net, abpic.co.uk
(listing pages) and Google Maps are Cloudflare/JS-blocked from this container and the Chrome extension was
not connected. The sweep therefore leans on four sources that *did* work and are individually strong:

1. **museofac.mil.co** – the Museo Aeroespacial's own per-airframe collection pages (42 pages, fetched in
   full, dated 2021-2025). Rung 2 of the hierarchy: authoritative on what is at Tocancipá.
2. **fac.mil.co Drupal site search** (`/es/search/node?keys=`) – FAC press releases 2014-2026, used as the
   primary lead source for base displays and town monuments. Dated, first-party, but written by unit press
   officers: types are reliable, serials are usually omitted.
3. **JetPhotos** (per-registration and type+operator listings via WebFetch) – dated photographs 2017-2025
   with c/ns; the best currency evidence available. Its "Other Location – Military Colombian Aerospace
   Museum" location tag was used to confirm 20+ museum airframes with 2023-2025 dates.
4. **volavi.co / aviacol.net** (Javier Franco "Topper", Colombian aviation historian) – detailed 2014-2015
   walk-rounds of EMAVI Cali and the Museo Aéreo Fénix with serials and c/ns, updated 2020.

Secondary: aviationmuseum.eu (compilation; stale in known ways – see below), oldjets.net April 2015 CATAM
photo essay (useful for the "did everything move" check), Wikipedia survivor lists (Ju 52, A-26, P-47,
C-47 – thin for Colombia), outono.net visit report 25 March 2024, El País Cali, elcolombiano/elheraldo.

Not consulted, and worth a second pass with a working search engine or browser: airhistory.net
"[Off-Airport]" Colombia photos, abpic location searches, Google Maps reviews for the town monuments,
aviacol.net forum "aeronaves preservadas" threads, Flickr.

## Site-by-site sourcing and corrections

### Museo Aeroespacial Colombiano, Tocancipá (41 rows, 37 tailed)
- Moved from CATAM (El Dorado, Bogotá) in 2015-2018; formally opened November 2017. Address per the
  museum: Km 1 vía Briceño–Zipaquirá, beside Parque Jaime Duque. Coordinates 4.9500,-73.9611 are the
  Wikipedia (en) article's figure for the museum, not an airframe fix. aviationmuseum.eu's
  4.9504,-74.1007 is 15 km west and is wrong.
- **CATAM → Tocancipá cross-check** (oldjets.net April 2015 list vs museum pages / JetPhotos 2023-25):
  everything photographed at CATAM in 2015 is now at Tocancipá **except**: T-33A **FAC 2033** (stayed at
  CATAM, "Silver Star" building – museum's own T-33 page; replaced by FAC 2008 from the Museo Militar);
  C-130B – CATAM's 2015 airframe was **FAC 1011**, the museum's is **FAC 1010** (museum page + JetPhotos
  c/n 282-3521, 2023). 1011's fate is unknown – lead. Gavilán at CATAM in 2015 wore "5067" (outside the
  5060-5063 block); the museum airframe is FAC 5062 (JetPhotos to Aug 2025). Possibly repainted; noted.
- **Howard 400 "FAC 654"**: false marking, painted as Lodestar C-60 FAC 654. aviationmuseum.eu lists both a
  "Howard 400 FAC654" and a "Lockheed C-60A Lodestar FAC654" – that is one airframe, recorded once.
  tail_number left blank (last true identities N400MC / YV-183CP; sources differ on which was last).
- **P-47D**: page title FAC 861, page text "FAC-681" – typo; 861 is painted and photographed.
  Wikipedia survivor list gives 45-49102 (in aliases; not independently verified).
- **OH-23B**: painted FAC 220 (JetPhotos c/n 40318). Museum text says the museum has FAC 221 and FAC 220
  is at CACOM-4 Melgar. Recorded as 220 with 221 in aliases and the conflict in description; Melgar row
  left untailed.
- **Mirage FAC 3035**: second Mirage, confirmed by museum page (Feb 2025: "dos en el Museo") and JetPhotos
  2022-24. Serial lies outside the museum's own quoted 3001-3034 range – flagged.
- **Kfir**: photographed at the museum in the 25 March 2024 visit report but absent from the museum's
  collection pages; untailed row, needs serial/variant read on site.
- **Caudron G.3 and Curtiss Falcon FAC 119**: probably reproductions (no original survives; FAC built a
  G.III replica for EMAVI). Recorded and flagged in description; coordinator may prefer to drop them.
- **Not recorded, despite appearing in the aviationmuseum.eu list**: second OA-37B "FAC 2771" (no serial
  in that block, no photo, not on museum pages); Gavilán 358 ARC 409 (only ever photographed at F-AIR
  2004; museum page says only FAC 5062 is there); SATENA Y-12E "FAC 1107" (no evidence); Fokker F-28
  FAC 0002 (still flying July 2022 per JetPhotos, no evidence of retirement to the museum). Kaydet PT-17
  FAC 62 is listed by the museum but its own June 2025 page says it is on show in the Taj Mahal at Parque
  Jaime Duque – recorded there. The American Coleman MB-4 tug is not an aircraft.
- Variant choices: T-37 FAC 2112 recorded as T-37C (museum) – directories say T-37B; Sabres recorded as
  Canadair CL-13 Mk.6 (Orenda-engined; museum text says "Mark IV"; volavi gives c/n 1456 for the EMAVI
  sister, a Mk.6 c/n); Bell 47 recorded as model "47" variant "G-2" with OH-13 aliases; Hughes 369HM as
  OH-6A.

### Parque Jaime Duque, Tocancipá (2 rows)
- DC-4 HK-136 (c/n 10407, ex 42-72302) – park attraction "Avión HK136"; JetPhotos August 2024.
- PT-17 FAC 62 – inside the Taj Mahal (park attraction list + museum page June 2025; JetPhotos Aug 2024).
  It was the FAC's airworthy flagship until at least 2015; recorded on_display as exhibited indoors.

### Museo Aéreo Fénix, Palmira (21 rows, 12 tailed)
- Private museum at Zona Franca Palmaseca beside Cali airport (museum site: hours, prices, address).
  Inventory assembled from aviationmuseum.eu's serial list, volavi's 2014/2020 article and the museum's
  own collection page (only the Super Cub is described there). Registrations for the Cessna 195/140, Lake,
  Aztec, PT-17, An-2, ultralights are not established; HK-27 is attached to one of the Cessnas in the
  compilation but which one is unclear – left in the Cessna 140 aliases only.
- Boeing 727-59 HK-727: donated April 2015; JetPhotos March 2024 shows it "parked next to the museum" on
  the airport side; aeroermo.com reports deterioration and restricted access. Recorded on_display – it
  is visible – but a visitor may not be able to reach it.
- C-118As HK-1703 and HK-3301: stored on the Cali apron since 2011; JetPhotos now files HK-1703 under
  "Aero Fenix" (May 2024). Whether they are inside the museum boundary needs a human check.
- The Wright Flyer is a full-size reproduction, flagged.

### EMAVI Cali (11 rows, 9 tailed) – restricted
- Serials from volavi's 2015 walk-round (with noted repaints: AT-6D 796/798, T-34 2311/2301, A-37B
  2158/2170, UH-1H 4473 once as 4216). Currency: F-86 photographed 2012; FAC visit reports 2022 and
  September 2025 still describe a "museo de aeronaves de la Base" showing the F-86, UH-1H, T-34, T-37,
  Caudron. The T-37 has no serial. Beaver FAC 5115: museum page says kept "en condición de museo";
  volavi 2015 said airworthy – recorded, flagged.
- The PT-17 FAC 1995 and T-34s kept airworthy at EMAVI are operational heritage aircraft, not displays –
  excluded.

### FAC base displays (restricted unless stated)
- CACOM-1 Palanquero: Mirage 5COAM FAC 3026 at the guardhouse/main entrance (FAC news Oct 2014; JetPhotos
  Dec 2016 "preserved at the entrance", Jan 2020). Wikipedia (es) Puerto Salgar says several aircraft
  are exhibited facing the Bogotá–Medellín highway – the Mirage is visible from the road, other types
  unknown. FAC 3030 photographed at the 2010 retirement ceremony – fate unknown. A T-33A is listed there
  by the museum (2021) – untailed.
- CACOM-2 Apiay: B-26C FAC 2504 (44-35508 per Wikipedia; museum page 2021 confirms), OV-10 monument and
  T-33A (untailed).
- CACOM-3 Malambo: T-37B FAC 2113 photographed "Malambo – Atlántico" Dec 2023 – recorded on the base;
  may in fact be in the town. The A-37 at the town entrance (April 2019) is a separate public site.
- CACOM-4 Melgar: OH-23B (serial conflict, above) and a T-6 (museum Texan page). Untailed.
- ESUFA and CAMAN, Madrid: T-33A each and a T-6 at ESUFA, all from the museum's 2021 pages; no serials,
  no photos – lowest-confidence rows in the file.
- CATAM: T-33A FAC 2033 (museum page 2021). An airhistory.net photo is titled "FAC2033 / FAC2002",
  implying the painted 2033 hides the identity 2002 – could not open the page; 2002 in aliases.
- GACAS Yopal: OV-10, A-37 and Cessna 337 described in FAC releases (March/Oct 2024) as retired
  "aeronaves emblemáticas" now part of the unit's history and shown to visitors – read as static
  displays; three untailed rows, distinguishable by type.
- GAAMA Leticia: OV-10 "avión museo" in front of the main gate (FAC 2016-2021) – recorded public.

### Town monuments (public)
- Villavicencio OV-10 FAC 2220 (FAC news 3 Dec 2021 re-inauguration; JetPhotos 2017 c/n 305A-117).
- Malambo A-37 (FAC/El Heraldo April 2019). Rionegro Las Delicias UH-1H (FAC April 2024). Flandes T-37
  (FAC 21 Dec 2023). El Cerrito T-37B FAC 2120 (FAC March 2024). Villa de Leyva T-37B FAC 2122 (JetPhotos
  Jan 2022). Manizales Bosque Popular T-37B FAC 2116 (JetPhotos Mar 2021). Cali Corredor Verde OV-10
  (FAC Nov 2018; corridor still maintained Nov 2024).
- Santa Marta "Los Trupillos" OV-10 FAC 2221 – JetPhotos Sept 2023 only; venue unidentified, access
  guessed as restricted. Weakest monument row; verify or drop.
- Colegio De La Salle Bogotá DC-3 N75T – identity fully documented (volavi 2010, JetPhotos/abpic 2008);
  presence after 2010 not re-verified (school site unreachable). Access "appointment".
- Club Casamata T-6 – from the museum's Texan page only.

## Excluded, and why
- **Hacienda Nápoles (Puerto Triunfo)**: the Piper "HK-617" on the gate was a replica; the gate was
  demolished 30 Jan 2019 and the replica re-erected inside the park painted as a zebra (El Colombiano,
  El Heraldo, Pulzo). Not an airframe record.
- **Museo Militar de Colombia, Bogotá**: its T-33A FAC 2008 moved to Tocancipá by 2018; no evidence of
  any remaining airframe.
- **Museo Histórico de la Policía Nacional, Bogotá**: site lists weapons, uniforms, vehicles; no aircraft.
- **Museo Naval del Caribe, Cartagena**: site gives no aircraft; no evidence found. Aviación Naval
  displays at Cartagena/Málaga and the Policía aviation school at Guaymaral: nothing found (searches
  cut off) – see leads.
- **Maloka, Parque Explora, Museo de Antioquia**: no aircraft (FAC only staged temporary exhibitions at
  Maloka/Planetario).
- **Museo del Transporte (Cali)** = the Museo Aéreo Fénix (renamed 2010) – one record.
- **Avianca**: no museum; the Avianca heritage airframe is the DC-4 at Parque Jaime Duque.
- Airworthy FAC heritage aircraft (PT-17 FAC 1995, T-34s, Bell 47 flagship at Melgar) – operational.
- Military Museum Park (Parque Museo Militar de las Fuerzas Militares, Tocancipá, opened 2016): no
  evidence of a real airframe (logo only).

## Blank fields, deliberately
- Coordinates: only the Museo Aeroespacial (Wikipedia figure). Nothing else could be geocoded from a
  source; nothing guessed.
- Postal codes: none.
- year_built: none – no row has a sourced build date beyond prose (1942 Stearman, 1946 DC-4, 1959 C-130B
  are in descriptions only).
- Tail numbers blank on 32 rows: Kfir, Turbo Commander, Caudron, Howard 400, ten Fénix civil aircraft,
  and every monument/base airframe where FAC press releases omit the serial.

## Needs a human on site (ranked)
1. Museo Aeroespacial: read the Kfir's serial/variant; confirm Mirage "3035"; confirm OH-23B 220 vs 221;
   check whether the Turbo Commander, Arava (added 2024-25) and any F-28 have arrived; confirm whether the
   Caudron and Falcon are reproductions.
2. Museo Aéreo Fénix: full current inventory with registrations (one afternoon with a notebook closes
   nine blank tails); status of the 727 and two C-118s outside the fence.
3. Puerto Salgar highway frontage: list every airframe on display at the CACOM-1 gate.
4. Serial and exact position of: Villavicencio-area OV-10 at Apiay, Leticia OV-10, Malambo A-37, Rionegro
   UH-1H, Flandes T-37, Cali Corredor Verde OV-10 (and whether the three further aircraft + helicopter
   promised in 2018 were installed), Melgar's town-entrance helicopter (type not even stated in the Dec
   2024 FAC release – not recorded), Santa Marta "Los Trupillos" OV-10 FAC 2221.
5. Is the DC-3 N75T still inside Colegio De La Salle, Bogotá?
6. ESUFA / CAMAN Madrid T-33s and T-6: serials and presence.

## Leads not run to ground (other agents / next pass)
- **Cali, Parque del Avión (Unidad Recreativa Parque El Avión)**: es-Wikipedia says a real aircraft sent
  by Gen. Omar Torrijos to journalist José Pardo Llada was installed in 1987 with only the shell kept and
  fitted out as a cinema; remodelled 2010. Type unknown – not recorded.
- **Acandí airport (Chocó)**: JetPhotos 2003 caption "A monument to FAC" on a Bell 205A-1 marked FAC 4102
  – 20 years old, unverified.
- **C-130B FAC 1011** (at CATAM 2015) – whereabouts.
- **La Dorada, Caldas**: the museum's Mirage page says one of four preserved Mirages is "en el municipio
  de La Dorada"; the FAC's own 2019 article says only Palanquero and the museum. Unresolved – possibly the
  same airframe as the Puerto Salgar gate guard (the towns face each other across the Magdalena).
- Universities (Los Libertadores, San Buenaventura Bogotá, UPB Medellín) and SENA aviation centres are
  reputed to hold instructional airframes – not checked.
- Tolemaida (Army aviation), Base Naval ARC Bolívar / Aviación Naval, Policía Guaymaral: nothing found;
  the JetPhotos Army/Navy/Police listings showed no preserved airframes on page 1.
- Medellín Olaya Herrera, Barranquilla, Bucaramanga, Cúcuta, Pereira, Armenia, Neiva, Popayán, Pasto,
  Cartagena, San Andrés airports/plazas: no evidence found before the search budget ran out; treat as
  unswept rather than empty.

## Row-count table

| file | site | rows | tailed |
|---|---|---|---|
| museo-aeroespacial-colombiano_aircraft.csv | Museo Aeroespacial Colombiano | 41 | 37 |
| museo-aereo-fenix_aircraft.csv | Museo Aéreo Fénix | 21 | 12 |
| emavi-cali_aircraft.csv | EMAVI Cali heritage aircraft | 11 | 9 |
| parque-jaime-duque_aircraft.csv | Parque Jaime Duque | 2 | 2 |
| cacom2-apiay_aircraft.csv | CACOM-2 Apiay | 3 | 1 |
| gacas-yopal_aircraft.csv | GACAS Yopal | 3 | 0 |
| cacom1-palanquero_aircraft.csv | CACOM-1 Palanquero | 2 | 1 |
| cacom4-melgar_aircraft.csv | CACOM-4 Melgar | 2 | 0 |
| esufa-madrid_aircraft.csv | ESUFA Madrid | 2 | 0 |
| 15 single-airframe sites | monuments, CATAM, CAMAN, De La Salle, Casamata, Santa Marta | 15 | 8 |
| **total** | **24 sites** | **102** | **70** |
