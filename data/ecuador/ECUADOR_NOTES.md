# Ecuador — research notes (all three passes)

Output directory: `/home/claude/sa/ecuador/`. Built by `build_ec.py` (edit the script and re-run; do not hand-edit CSVs).

## Files and counts

| file | site | rows | with tail |
|---|---|---|---|
| ec_museums.csv | 20 sites | — | — |
| museo-aeronautico-y-del-espacio-de-la-fuerza-aerea-ecuatoria_aircraft.csv | Museo Aeronáutico y del Espacio FAE, Quito (incl. base static park) | 23 | 22 |
| escuela-superior-militar-de-aviacion-cosme-rennella-museum-s_aircraft.csv | ESMA museum, Salinas | 9 | 9 |
| base-aerea-simon-bolivar-displays-guayaquil_aircraft.csv | Base Aérea Simón Bolívar, Guayaquil | 6 | 6 |
| ala-de-combate-no-21-taura-museum-and-gate-guards_aircraft.csv | Taura | 5 | 4 |
| fuerte-patria-bfe-9-instructional-airframes-latacunga_aircraft.csv | Fuerte Patria, Latacunga | 4 | 3 |
| base-aerea-cotopaxi-displays-latacunga_aircraft.csv | Base Aérea Cotopaxi | 2 | 2 |
| escuela-tecnica-de-la-fuerza-aerea-displays-latacunga_aircraft.csv | ETFA Latacunga | 2 | 2 |
| base-aerea-eloy-alfaro-gate-guards-manta_aircraft.csv | Manta | 2 | 2 |
| parque-infantil-a-37-and-t-33-pillaro_aircraft.csv | Píllaro | 2 | 1 |
| 11 single-airframe sites (La Carolina DC-6, Otón de Vélez, Cayambe, Ibarra, Otavalo Caravelle, San Rafael club, Ambato, Guaranda, San José de Chimbo, Bahía de Caráquez, Tulcán) | | 11 | 11 |
| **total** | **20** | **66** | **62 (94%)** |

## Sources and weight

1. **fae.mil.ec (WordPress REST API, `wp-json/wp/v2/posts?search=museo`)** — the FAE's own news: museum open by reservation (Mon-Sun 09:00-12:00 / 12:30-16:00, tel. 099 290 4619), school visits to "el Museo Aeronáutico y del Espacio y el Parque Estático de la Base Aérea Mariscal Sucre" (January–July 2025), Canberra FAE-509 plaque (November 2022), T-34C plaque (August 2022), Taura "Museo Histórico de la Aviación Supersónica" inaugurated June 2021. Highest weight for status/access.
2. **jetphotos.com** (fetched page-by-page; the Ecuador AF airline listing pp.1-10, the Salinas/Manta/Latacunga airport listings, and Diogo da Conceição's, Juan Andrés Saavedra's, Antonio Espinel's, Eric Graf's and Miguel Astudillo's 2019-2025 photos). Dated photos with photographer remarks are the currency evidence for almost every row; remarks are quoted in `description`. One photographer notes "almost 30 T-33s preserved all around Ecuador" — I found 14 of them.
3. **aerialvisuals.ca Location Dossier 4163 "Quito Air Force Museum"** (12 airframes, GPS -0.13363,-78.49218) — serials/c-ns for the museum's transports; the B-25 dossier 125297 for the smuggling history.
4. **Wikipedia (en)**: Meteor survivors list (Ecuador section, sourced to Ogden's 2008 book — stale), B-25 survivors, C-47 survivors (44-77164), Catalina survivors (53602), B-23 (39-031), HS 748 (c/n 1738 wrongly placed at the Quito museum — it is at Fuerte Patria). Treated as leads.
5. **Wikimedia Commons** — thin for Ecuador; only the Peruvian MoD photo of the AT-33 destroyed in the April 2016 earthquake and a few 2007-2009 museum photos.
6. **Web search quota ran out mid-run**, so no Spanish-press sweep of Cuenca, Loja, Machala, Esmeraldas, Portoviejo, Riobamba, Lago Agrio, Shell-Mera or the Guayaquil naval base was possible; these are listed as gaps.

## Corrections and judgment calls

- **Museum + "Parque Estático"** treated as one site: both are inside Base Aérea Mariscal Sucre (old airport) and FAE news describes them as one visit. Rows photographed "on the base ramp" for the 2020 centenary (Jaguar FAE339, Mirage F1JA FAE813, Kfir FAE909, Strikemaster FAE246, T-33 FAE633/622, T-34C FAE024, Meteor FF-122) are recorded at the museum with that caveat; the 2022 photographer confirms "most of them were the same ones as past times" and the FAE calls the area a static park in 2025. Access `appointment` per FAE ("previa reserva").
- **Mirage F1JA at Quito**: aerialvisuals says FAE806; jetphotos (May 2019) reads FAE807 with Maj. Banderas' name — both flew the 10 Feb 1995 engagement. Recorded FAE807 with FAE806 alias; flag. A second F1JA, FAE813, is on the ramp.
- **Meteor at Quito**: three identities in the sources (FF-122 painted 2022; FF-123 ex VW366 Wikipedia; F-113 aerialvisuals). tail = FF-122 (what it wears), others in aliases.
- **Meteor FF-114 at Cotopaxi**: photographer thinks it is ex FAE-704 mis-marked with its c/n; Wikipedia says ex WB136. Wikipedia's second Cotopaxi Meteor (FF-112 ex WH547) NOT recorded — no photo.
- **T-33 FAE622**: photographed at Guayaquil (April 2021 remark says it was moved to Quito) and at Quito (October 2021). Recorded once, at Quito.
- **T-33 FAE639 at Cotopaxi** wears the false serial FAE369; true 639 recorded, 369 in aliases. **Kfir FAE912 at Salinas** wears a false registration "for historical reasons" (the airframe it commemorates is in Quito) — recorded as FAE912, c/n 168.
- **B-25 44-86866**: never given an FAE serial; tail blank, USAAF/N-number in aliases; displayed as "Apache Princess".
- **HS 748 FAE738 / DHC-5 FAE063 / two DC-3s** are at the Army's Fuerte Patria (BFE 9) paratroop base, not the Cotopaxi air base — one photographer files them under "Latacunga Cotopaxi Int" (2015), another explicitly "Fuerte Patria" (2022/2024). Instructional airframes inside a barracks → `restricted`. Second DC-3: painted 4340, read as 4338/4341 by others; tail blank.
- **Taura**: Kfir CE FAE905 + Mirage F1 at the gate (January 2022) are firm. Jaguar ES FAE-309, Strikemaster FAE265 and Kfir TC.2 FAE930 were photographed as ceremony décor (February 2023) — recorded with "permanence not confirmed". Cheetah C FAE-1377 (same ceremony, special scheme) NOT recorded: Cheetahs were then still nominally operational.
- **Guayaquil Base Aérea Simón Bolívar**: the T-33 FAE623 stands at a sentry post on Av. Pedro Menéndez Gilbert and is photographable from the street (coordinates given for it); everything else is inside → site `restricted`.
- **Hacienda Pastaví Caravelle** — private farm/café; owner controls photography → `appointment`.
- **Cayambe AT-33 FAE630** — serial later reused by Boeing 737 FAE-630; rows are distinct airframes.
- **Tulcán AT-33 FAE637** — only a 2012 photo; recorded but flagged.
- **Coordinates** given only where a source states them: Quito museum (aerialvisuals), San José de Chimbo (jetphotos geotag), Guayaquil T-33 (jetphotos geotag). All others blank.

## Excluded (and why)

- **AT-33A destroyed in the 16 April 2016 earthquake** (Commons/Peruvian MoD photo; Manabí coast monument) — destroyed.
- **Cuenca Fairchild FH-227B HC-BXC** (ex Austro Aéreo) — derelict in a car park beside Mariscal Lamar airport since 2003; not a display.
- **Latacunga airport "corrosion corner"**: Boeing 727-134 FAE691, 727-230 FAE620, 727-17 HC-BLV, Sabreliner 40 FAE047, L-100 FAE893 — derelict/stored, not displays (727 FAE691 appears in a 2009 Commons photo captioned "Boeing FAE" at the old Quito airport — it was then operational).
- **Quito old airport**: C-130B FAE895 scrapped (2018); C-130B FAE896 derelict (2016); Sabreliner 40 FAE-043 "stored" (2009); T-33A FAE945 (2010 photo only, probably later repainted) — not recorded.
- **Salinas Sabreliner 60 FAE049** ("resting at SESA", 2021) and **T-34C FAE032** (2021, possibly still a trainer) — status ambiguous; not recorded.
- **Guayaquil Bell TH-57A FAE-410/-401 and Bell 206B FAE415** — stored at Ala 22 (2022), not displays.
- **Boeing 707 / Electra TAME displays, Bicentennial Park Quito aircraft, Museo Naval Guayaquil, Museo Templo de la Patria, Cuenca/Loja/Ambato-city/Riobamba/Machala/Esmeraldas/Portoviejo monuments, Army aviation Shell-Mera** — no evidence found in the sources reachable; not recorded (see gaps).
- **Mirage 50EV 3373/0155 ex-Venezuela** — operational transfers, not displays.

## Blank fields, deliberately

- `year_built` blank throughout.
- `tail_number` blank: Quito B-25, Píllaro T-33, Taura gate Mirage F1, second Fuerte Patria DC-3.
- `postal_code` blank everywhere.

## Needs a human on site (ranked)

1. **Quito museum / static park**: reconcile the Meteor identity (FF-122/FF-123/F-113), confirm which Mirage F1JA(s) (806/807/813) are present, whether HS 748 HC-AUK/FAE-001 and the Alouette FAE367 are exhibits or dumped, and list anything added since 2022.
2. **Taura**: are Jaguar FAE-309, Strikemaster FAE265, Kfir TC.2 FAE930 (and Cheetah FAE-1377) permanent museum pieces? What does the "Museo Histórico de la Aviación Supersónica" hold?
3. **T-33 monument sweep**: ~15 more T-33s are said to exist (Píllaro serial; Tulcán 2012; Machala, Loja, Riobamba, Esmeraldas, Lago Agrio, Santo Domingo, Quevedo untested).
4. **Base Aérea Cotopaxi**: identify the DC-3 and Mirage F1 displayed with T-33 FAE639, and confirm/deny the second Meteor FF-112.
5. **Guayaquil**: Meteor FF-116 vs Wikipedia's "091 ex WH540"; whether Mirage F1JA FAE803, C-47B FAE49785 and Alouette FAE-396 survive (last photos 2013-2017).
6. **Parque La Carolina DC-6** — exact coordinates and condition.

## Leads for other agents / coordinator

- **Peru**: none. **Colombia/Venezuela**: Mirage 50EV 3373 and 0155 (ex-FAV) came to Ecuador in 2010 as operational aircraft — if any were later preserved in Ecuador they were not found.
- **Otavalo Caravelle HC-BDS** and **Cuenca FH-227 HC-BXC** are civil-heritage airframes that a Latin-American airliner-preservation list might already carry.
