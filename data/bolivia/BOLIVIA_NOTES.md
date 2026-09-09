# Bolivia — aviation preservation research notes (all three passes)

Output: `/home/claude/sa/bolivia/` — `bo_museums.csv` (13 sites) + 13 `*_aircraft.csv` files (36 rows, 33 with tail numbers). Built by `build_bo.py` (python `csv`, UTF-8, `lineterminator="\n"`).

## File / row-count table

| slug | site | rows | tails |
|---|---|---|---|
| museo-aeroespacial-fab-el-alto | Museo Aeroespacial de la Fuerza Aérea Boliviana, El Alto | 23 | 22 |
| i-brigada-aerea-el-alto-gate-t33 | I Brigada Aérea El Alto Gate Guard T-33 | 1 | 1 |
| plaza-walter-arze-rojas-b25-cochabamba | B-25 Mitchell roundabout, Cochabamba | 1 | 1 |
| biblioavion-convair-t29-cochabamba | Biblioavión Convair T-29B library, Cochabamba | 1 | 1 |
| biblioavion-boeing-737-cliza | Biblioavión Boeing 737 library, Cliza | 1 | 1 |
| rotonda-fuerza-aerea-pc7-cochabamba | PC-7 on pole, Rotonda Fuerza Aérea, Cochabamba | 1 | 1 |
| gabs-51-lama-monument-cochabamba | SA 315B Lama on pole, GABS 51, Cochabamba | 1 | 0 |
| politecnico-militar-aeronautica-t33-cochabamba | T-33 at Politécnico Militar de Aeronáutica roundabout | 1 | 1 |
| plaza-de-aeronaves-colmilav-santa-cruz | Plaza de Aeronaves COLMILAV / III Brigada Aérea, Santa Cruz | 2 | 2 |
| avion-pirata-constellation-santa-cruz | Avión Pirata (L-049), Santa Cruz | 1 | 1 |
| plazuela-el-aviador-c47-trinidad | Plazuela El Aviador C-47, Trinidad (Beni) | 1 | 0 |
| oruro-t33-monument | Oruro T-33 monument | 1 | 1 |
| avenida-las-americas-at6-tarija | AT-6D monument, Tarija | 1 | 1 |
| **total** | 13 sites | **36** | **33** |

Serial coverage 92%. The three blank tails are deliberate (see "Blank fields").

## Sources and their weight

- **airhistory.net** (dated photos, incl. a photographer's October 2025 Bolivia trip: Electra TAM-69 at the museum 20 Oct 2025, T-33 FAB-634 at the I Brigada gate 20 Oct 2025, T-33 FAB-601 at Oruro 18 Oct 2025, B-25 Cochabamba 23 Oct 2015; C-130A TAM-65 caption "on display with the museum by 2018"; first FAB-634 at the Politécnico Militar Cochabamba 1997). Highest weight for currency. Site is behind Cloudflare and answered only about half of fetches — the operator page 2+, the Santa Cruz-El Trompillo location page and several registration pages could not be read. **A rerun with browser access should read `airhistory.net/basic-operator/2433/Bolivia-Air-Force` pages 2-4 and `location/893/Santa-Cruz-El-Trompillo`.**
- **JetPhotos** (dated photos): T-33 FAB-627 "standing at plaza de la aviación at El Trompillo" 5 Jul & 15 Aug 2026; F-27 TAM-95 "displayed in new Bolivian Aeronautical Museum" 31 Oct 2015; CV-580 FAB-72 and Electra TAM-69 La Paz May 2025; AT-6D FAB-336 Tarija Feb 2009.
- **Roll Out – Aerospotter blog (aerospotter.blogspot.com)** — Argentine/Bolivian spotter blog with per-type fleet lists (T-33 list Aug 2017 with c/n, ex-identities and fates; C-47/TAM list; Arava; F-27; Convair; B-25; C-54) and monument posts ("La plazuela El Aviador" Oct 2023, "El biblioavión de Cliza" Jan 2023, "La biblioteca del avión" 2006, "El Pirata que resiste al tiempo" Jul 2026, "Douglas C-84 TAM-01" Jun 2026, "El traslado de un Boeing 727 en Cochabamba" Apr 2026). Weight: high for identities; the fleet lists are 2017-2020 so fates were cross-checked against dated photos.
- **aviationmuseum.eu** collection list for the El Alto museum (c.2016) — the only serial-by-serial list found for the museum. Its HTML table renders as two separate columns and a first read mis-aligned them; the raw HTML was re-parsed to confirm the pairing (FAB-636 = T-33, FAB-503 = T-25, FAB-362 = T-6D, FAB-411 = T-28A, FAB-452 = PC-7, FAB-028 = Turbo Commander, FAB-016 = Stearman, FAB-161 = T-23). Two of its entries were overridden by better sources: F-27 "FAB-90" → TAM-95 (JetPhotos photo on display 2015 + Aerospotter fleet list: FAB-90 still flying 2020); Electra "TAM-01" → now re-marked TAM-69 (airhistory 2025).
- **es/en Wikipedia** museum article: type list only, no serials; coordinates -16.5016/-68.1751 (article level). **OpenStreetMap** (Overpass `historic=aircraft` query + Nominatim): gave museum position -16.5030/-68.1740 on Av. Juan Pablo II and revealed the Cochabamba, Tarija, Sucre, Puerto Suárez and El Alto leads below. OSM nodes are used as *leads* and, for three Cochabamba monuments, as the only source (flagged in each description).
- **Revista Fuentes (SciELO, Dec 2015)** — article by the museum's curator Ramiro Molina Alanes: 23 aircraft at opening, Plaza de Aeronaves beside hangar No. 1, and the statement that the Curtiss Wasp, Vickers Scout and Cóndor no longer exist (so the Wasp/Vickers/Potez in the museum are replicas). Also names the B-25 (Cochabamba) and L-049 (Santa Cruz) as the two historic aircraft "left outdoors".
- **El Alto Digital** museum tour (2017, updated Feb 2024), **Los Tiempos** 19 Feb 2023 (B-25), **eju.tv** 22 Oct 2023 (C-47 TAM-38 and the nine-aircraft Plaza de Aeronaves), **CRE** 11 Dec 2023 (lighting for "Museo de Aeronaves del COLMILAV" at Av. Santos Dumont y 2do anillo), **Opinión** 30 Jul 2019 (Biblioavión), **infodefensa** (T-33 retirement 31 Jul 2017; GAC 67 reactivated at Sucre May 2024), helis.com FAB fleet (c/n for FAB-740, FAB-747).
- Wikipedia survivor lists for F-86, T-33, B-25, C-46: **no Bolivia entries** (the B-25 and Oruro/El Alto T-33s are absent from them — worth adding upstream).
- Web-search quota ran out near the end; Wikimedia API calls were rate-limited through the shared proxy (HTML pages worked with pauses). Facebook posts (COLMILAV, GDF) are robots-blocked.

## Corrections / identity resolutions

- **Museum C-47 "TAM-01"** → true identity **TAM-16** (c/n 26666/15221). Aerospotter, June 2026: the original TAM-01 was a Douglas C-84 (42-57512) destroyed 14 Apr 1972; the museum C-47 inherited the marking. Tail = TAM-16, TAM-01 in aliases.
- **Museum Electra**: c/n 1125, ex N6134A/CP-853; served as TAM-69 then TAM-01; re-marked **TAM-69** for display (airhistory 2025). Tail = TAM-69.
- **Museum F-27**: TAM-95 (c/n 10601), not FAB-90.
- **FAB-634** was issued twice. The gate guard at I Brigada Aérea (2025 photo) is the second airframe (Aerospotter: c/n T33-400); the first (ex French 21400) was an instructional airframe at the Politécnico Militar, Cochabamba, and was scrapped c.1997. Note Aerospotter's ex-French ferry marks (F-ZVLx) repeat across airframes — they were reused ferry registrations, so they are **not** put in aliases.
- **B-25 FAB-542**: marked FAB-542; Los Tiempos says ex-Venezuela 1973, aeroflight says Bolivia's B-25s arrived 1948 with 546/547 ex-FAV; airhistory: "still defies identification". Tail recorded as the painted FAB-542 with the doubt in the description.
- **TAM-38 C-47** at Santa Cruz: Aerospotter TAM list = Basler BT-67, c/n 20507, deactivated Sep 1997; eju.tv = crashed Chimoré 1995, rebuilt 2023. Recorded as model C-47 with Basler BT-67 in aliases.
- **Museo de Aeronaves del COLMILAV** (CRE) and the **"Plaza de Aeronaves" of III Brigada Aérea** (eju.tv) and JetPhotos' **"plaza de la aviación at El Trompillo"** are the same place at Av. Santos Dumont / 2do anillo — one site record.

## Judgment calls

- **Replicas excluded**: the museum's Curtiss Wasp triplane, Vickers Type 143 "Bolivian Scout" (Rafael Pabón's aircraft) and Potez 25 shown in the Chaco War hall are reproductions (the curator's 2015 article states the originals were lost). Also excluded: satellite/rocket scale models (Túpac Katari, Long March 3B), the 1932 Ford truck.
- **Library aircraft** (Biblioavión T-29B Cochabamba; Biblioavión 737 Cliza) and the **Avión Pirata** (bank branch/library/advertising hoarding) are recorded — real airframes, publicly accessible, clearly landmarks.
- **T-33 FAB-607** at the museum is included on Aerospotter's 2017 word only (no later photo) — flagged for on-site confirmation. **FAB-600 and FAB-602** ("preserved at Base Aérea El Alto", Aerospotter 2017) are **not** given rows: no location on the base and no sighting since; see needs-a-human list.
- **Three Cochabamba monuments (PC-7 FAB-479 on pole, SA 315B Lama on pole at GABS 51, T-33 FAB-617 at the Politécnico roundabout)** rest on OpenStreetMap tagging only (detailed tags: refs, pole support, Lama install date 12 Sep 2016). Included because the tagging is specific and consistent with FAB fleet records (FAB-617 = spares airframe; PC-7s are FAB-45x/47x), but each description says "confirm on site".
- **Access**: everything is `public`. The COLMILAV plaza faces the avenue and receives school visits; the I Brigada gate guard is visible from Av. Juan Pablo II. The Museo Aeroespacial is inside the air base but is a ticketed public museum (Mon-Fri 09:00-12:30 / 14:30-18:30, weekends by request).
- **Coordinates**: OSM node positions for the airframes/plazas (B-25, both Biblioaviones, Avión Pirata, Tarija AT-6, COLMILAV plaza node, Cochabamba monuments); Aerospotter's own GPS for Trinidad; OSM museum node for El Alto (museum-level, not per airframe). Oruro blank.
- **military_civilian**: Biblioavión T-29B = civilian (last identity CP-1356, Frigoríficos Reyes); Trinidad C-47 = civilian (last operator TA San Jorge); Cliza 737 = military (FAB-116).

## Blank fields, deliberately

- `tail_number` blank: museum **Arava** (no serial in any list; candidates TAM-78/TAM-80); **Lama on pole at GABS 51** (OSM gives none); **Trinidad C-47** (Aerospotter: "CP-1960 (o CP-1990)" — ambiguous; true USAAF identity 42-100530 and c/n 18993 are in aliases).
- `year_built` blank throughout except none — dates in descriptions only (first-flight dates known for the Electra 22 Feb 1960 and Cliza 737 4 Feb 1981 are in descriptions; left out of `year_built` to stay conservative — importer may promote them).
- Oruro `latitude/longitude` blank: no source gives the plaza.
- `website` blank except the museum's Wix site (fab.bo is unreachable through the proxy).

## Excluded and why (do not re-research without new evidence)

- **F-86F Sabres**: none preserved in Bolivia. The last three went to Dixie Air Parts (USA) in 1995; FAB-658 is at NASM Udvar-Hazy (USA), FAB-651 became N860AG (Comanche Fighters). Wikipedia F-86 survivor list has no Bolivia entry.
- **P-47B/D, Curtiss CW-19, Grumman JRF-6, F-51 Mustangs** — all exported to US collectors 1958-1994 (SciELO 2015).
- **Derelict/stored airliners at El Alto** (C-46s CP-987, CP-1655 "El Payaso", CP-973-type, DC-6s, Convair 340, Queen Air) and **Cochabamba** (AeroSur/LAB 727s CP-2422/2423/2447/2464/2515, 737s CP-2486/2561/2595, DC-10 CP-2489, Canedo C-46 CP-973, CASA 212 FAB-85 instructional hulk, MA60s) — stored/derelict on airport property, not displays.
- **Boeing 727-2S7 N685CA** (ex Champion Air/LAB) towed out of Cochabamba airport to private land in La Chimba on 17 Apr 2026 for a planned restaurant/event venue — intent only; not open. Re-check in 2027.
- **C-54 TAM-51** — derelict at Pucallpa, Peru (lead for Peru agent, but it is a wreck, not a display).
- **Arava remains at V Brigada Aérea, Trinidad** — stripped hulk used for drills (2015), not a display.
- **T-33 FAB-624** — spares hulk at El Trompillo (2006), no later trace.
- **FAB-461 PC-7 and FAB-501 T-25** photographed at El Trompillo on 5 Jul 2026 by the same photographer as the plaza T-33 — could be plaza exhibits (the plaza has nine aircraft) but both types are still in FAB service, so not recorded.
- **Museo Corralito / Museo Histórico Militar Héroes del Chaco (Villamontes)** — Chaco War museums; no aircraft found in their descriptions.
- **Guyana/other**: n/a here.

## Needs a human on site (ranked)

1. **Museo Aeroespacial El Alto — current serial list.** Only a c.2016 list exists; 2024 press says "24 aircraft and 3 helicopters". Confirm FAB-607 and FAB-636 (two T-33s), the BAe 146 FAB-103, the Arava's serial, the Stearman sub-type/serial, and whether the C-130A TAM-65 and anything added since 2018 (e.g. K-8, Lear Jet) is on show.
2. **COLMILAV Plaza de Aeronaves, Santa Cruz** — identify the other seven of the nine aircraft (C-47 TAM-38 and T-33 FAB-627 confirmed). Candidates: PC-7, T-25, Cessna, UH-1H, K-8 hulk.
3. **Oruro T-33 FAB-601** — exact plaza (airhistory only says "Off-Airport"), coordinates.
4. **OSM-only monuments in Cochabamba** — PC-7 FAB-479 (Rotonda Fuerza Aérea), Lama at GABS 51 (serial), T-33 FAB-617 at the Politécnico; OSM also maps a helicopter on a pedestal (-17.4486, -66.1408) and two more aircraft (-17.4514/-17.4521, -66.1404) on Av. Politécnico inside the PMA campus — types unknown.
5. **Unidentified OSM `historic=aircraft` nodes** (types unknown, no photos found): Sucre, Grupo Aéreo de Caza 67 at the old Juana Azurduy airport (-19.0145, -65.2920); Puerto Suárez, Base Aérea Cap. Salvador Ogaya (-18.9799, -57.8166); Tarija, 4ª Brigada Aérea at the airport (-21.5522, -64.7115); Tolata/Angostura, Escuela de Perfeccionamiento Técnico Aeronáutico (-17.5474, -66.0600); El Alto SAR "Illimani" station, Av. de los Héroes (-16.5064, -68.1703, military type); and a cluster of ~10 military airframes inside I Brigada Aérea El Alto at -16.5015 to -16.5039, -68.181 to -68.184 (could be the FAB storage "graveyard" where C-130A TAM-64 was photographed in 2009, or a second display line; FAB-600/FAB-602 T-33s "preserved at Base Aérea El Alto" may be among them).
6. Biblioavión Cochabamba/Cliza opening hours in 2026; Avión Pirata condition after the 2023 repaint.

## Leads for other agents

- **Brazil (Roraima)**: OSM maps an "Avião Xavante" monument (2.84897, -60.70516, access=yes) and an "Avião Super Tucano" (2.84741, -60.6993) in Boa Vista — presumably at the Base Aérea de Boa Vista / city; not in my scope.
- **Peru**: ex-TAM C-54 TAM-51 (45-0551, c/n 36004) derelict on the grass at Pucallpa since 2009 — a wreck, probably not a record.
- **USA**: F-86F FAB-658 (Udvar-Hazy), FAB-651 N860AG; ex-FAB P-47 at Champlin/… — out of scope.
- **Argentina**: Aerospotter documents ex-Bolivian aircraft in Argentina (LAB 727 CP-2463/CP-2498 stored at Morón 2006) — stored, not displays.
