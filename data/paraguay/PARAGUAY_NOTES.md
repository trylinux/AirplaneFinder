# Paraguay — research notes (all three passes)

Researched 9 September 2026. Output: `py_museums.csv` + 4 per-site aircraft files.
**This package is thin and should be treated as a first pass**, for the reasons
below.

## Tooling caveat (read first)

The shared WebSearch budget ran out before the Paraguay sweep started, and every
search engine reachable by curl returned captchas. `fuerzaaerea.mil.py` banned
the proxy IP outright ("You got banned permanently"), so the FAP site was read
only through Wayback captures (2016, 2021, 2024-26). No browser was connected.
Wikimedia Commons has almost nothing for Paraguayan preserved aircraft, and
es/en Wikipedia has no article on the FAP museum. The town sweep (Ciudad del
Este, Encarnación, Villarrica, Coronel Oviedo, Pedro Juan Caballero, Concepción,
Mariscal Estigarribia) therefore produced **no** verified sites — that is a gap,
not a finding. Aerial Visuals' Locator was the only country-wide list available.

## Sources and their weight

1. **FAP website (Wayback)** — 2021 museum page lists: "T-33 Silver Star, UH-1B,
   T-25, C-210, T-6 Texan, DC-3". The 2024-26 site has a "MUSEO FAP" category of
   historical type notes but no current inventory. es.wikipedia (2023) confirms
   "un museo en la base aérea de Ñu Guasú, donde se pueden observar varias
   aeronaves exhibidas así como monumentos". Weight: holdings list, medium
   (no serials, 2021).
2. **Aerial Visuals** — Locator entries for Base Aérea Ñu Guazú (T-33A 57-0627,
   SNJ-4 0129, C-47A T-67, UH-1B "PR-H-005", plus five unidentified), Silvio
   Pettirossi airport public site ("F-84?" and UH-1, a T-33 "once displayed,
   moved"), San Lorenzo (707 ZP-CCE), Guaraní airport (derelict widebodies),
   Aeroclub Yvytu San Bernardino (vintage lightplanes). Identity data good;
   currency unknown.
3. **Wikimedia Commons / es.wikipedia "Loma Grande (Paraguay)"** — photograph
   dated 7 February 2025 of the LAP Boeing 707 displayed near the Loma Grande
   access; best currency evidence in the package.
4. **aviationmuseum.eu** — "Museo de la historia de Líneas Aéreas Paraguayas /
   Hotel del Rancho, Loma Grande": 707-321B ZP-CCF/FAP-01, plus a UH-1B
   "PR-H-004" and a Fokker 100 "ZP-CFL". Lead only; only the 707 is
   corroborated.
5. **Nominatim** — Hotel del Rancho geocode (-25.2005, -57.2235 on the Loma
   Grande–Altos road).

## Corrections made

- Loma Grande 707: aviationmuseum.eu's coordinates (-25.2002, -57.5037) are
  wrong (they fall in Gran Asunción); replaced with the Nominatim position of
  the Hotel del Rancho. Airframe position not fixed.
- Aerial Visuals' "F-84?" at the Pettirossi access is not recorded as a row:
  Paraguay never operated F-84s; it is probably an AT-26 Xavante or T-33 on a
  plinth. Needs identification.

## Judgment calls

- **FAP museum access** = `restricted` (inside Base Aérea Ñu Guazú / FAP
  headquarters, Av. Gral. Elizardo Aquino 1792, Luque). If it proves to have
  walk-in hours, change to `public`.
- **UH-1B at Ñu Guazú**: Aerial Visuals' "PR-H-005" looks like a prefix plus the
  FAP helicopter serial H-005; tail left blank, both forms in aliases.
- **T-33A at Ñu Guazú**: only the ex-USAF identity (57-0627) is known; tail
  blank.
- **San Lorenzo 707 ZP-CCE** and **Pettirossi access UH-1** are recorded on
  Aerial Visuals' word alone (with coordinates) and flagged in descriptions as
  needing confirmation. Delete them if a human finds nothing there.
- **Coordinates**: Ñu Guazú = Aerial Visuals' T-33 site; Loma Grande = hotel
  geocode; San Lorenzo and Pettirossi = Aerial Visuals site positions.

## Excluded, and why

- **Guaraní International Airport (Minga Guazú/Ciudad del Este)** — DC-8-62F
  3D-FRE, 747-269B 9Q-CGI, F-27 CX-BRS are abandoned/derelict airliners, not
  displays.
- **Silvio Pettirossi airport ramp** — C-47s FAP 2030 and 2032, Convair
  CV-240 ZP-CDO, C-131D 2001: derelict/stored FAP transports (2009 photos), not
  displays; 707 ZP-CCG "displayed at the airport from February 1991" is listed
  by Aerial Visuals as having moved on (possibly the San Lorenzo airframe).
- **Aeroclub Yvytu, San Bernardino** — Cessna O-1A ZP-TZS, Fleet 2, Stearman
  ZP-TZK, Safir ZP-TAD, Cub ZP-X013: vintage aero-club aircraft, no evidence of
  static exhibition.
- **Monumento a Silvio Pettirossi (airport)** — a bust on a pylon (Commons
  photo 2025), no airframe despite its Commons categorisation.
- **Loma Grande UH-1B "PR-H-004" and Fokker 100 "ZP-CFL"** — single unverified
  directory entry; not recorded (see open questions).
- **Museo Militar / Museo de Historia Militar (Asunción)**, **Museo Naval**,
  science/transport museums — no evidence of any airframe; not researched
  beyond that.

## Blank fields, deliberately

- `tail_number` blank for the FAP museum T-33A, UH-1B, T-25 and Cessna 210 and
  for the Pettirossi UH-1.
- `year_built` blank throughout (no sourced dates).
- `postal_code` blank throughout.

## Needs a human on site (ranked)

1. **Museo FAP, Ñu Guazú** — full inventory with serials. Expect at least one
   **AT-26 Xavante** (retired 2004; the FAP's own museum category carries a
   Xavante article), possibly a Bell 47/H-13, Hiller UH-12, PT-19, Fokker T-21,
   C-212 or DHC-3 Otter; Aerial Visuals lists five unidentified airframes there.
   Ask whether the public may enter and on which days.
2. **Pettirossi airport access (Av. Aviadores del Chaco)** — identify the jet
   ("F-84?") and the UH-1 on display; the old terminal housed the Grupo
   Aerotáctico, so a Xavante monument is likely.
3. **San Lorenzo 707 ZP-CCE** — find it (Aerial Visuals -25.3228, -57.5153) and
   confirm registration; check whether it is ZP-CCG.
4. **Hotel del Rancho, Loma Grande** — confirm the UH-1B and Fokker 100 claimed
   alongside the 707, and read the 707's registration (nose shows CCF; fin
   carries a FAP-style number).
5. **Town sweep never done**: Ciudad del Este, Encarnación, Villarrica, Coronel
   Oviedo, Pedro Juan Caballero, Concepción, Mariscal Estigarribia, Base Aérea
   Concepción, Escuela de Formación de Oficiales, Naval Aviation (Base
   Aeronaval Sajonia), Army aviation — search in Spanish for "avión monumento",
   "Xavante monumento", "T-33 plaza", "Tucano exhibido" once search is available.
6. **Ex-TAM/LAP aircraft** (Electra, 737-200 ZP-CAB/CAC, BAe 146) — any
   preserved?

## File / row-count table

| file | site | rows | with tail |
|---|---|---|---|
| py_museums.csv | 4 sites | 4 | – |
| museo-fap-nu-guazu_aircraft.csv | Museo Aeronáutico FAP, Ñu Guazú | 6 | 2 |
| lap-museum-loma-grande_aircraft.csv | Hotel del Rancho, Loma Grande | 1 | 1 |
| boeing-707-san-lorenzo_aircraft.csv | San Lorenzo | 1 | 1 |
| pettirossi-airport-displays_aircraft.csv | Pettirossi airport access | 1 | 0 |
| **total** | | **9** | **4 (44%)** |

## Leads for other agents

- **Argentina**: C-47 T-67 at Ñu Guazú is ex-Fuerza Aérea Argentina T-22 (2nd
  use) / Ejército AE-7T — alias only, no action.
- **Brazil**: SNJ-4 0129 is ex-FAB 1398; C-47 FAP 2032 (derelict at Asunción) is
  ex-FAB 2090 — no action.
- **Chile**: C-47 FAP 2030 (derelict at Asunción) is ex-FACh 969 — no action.
- **Uruguay**: F-27 CX-BRS derelict at Guaraní airport is ex-Uruguayan civil —
  not a display.
