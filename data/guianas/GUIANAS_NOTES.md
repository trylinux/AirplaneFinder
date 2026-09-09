# Guyana, Suriname, French Guiana — aviation preservation research notes (all three passes)

Output: `/home/claude/sa/guianas/` — `gy_museums.csv` (one file for all three countries; `country` field per row) + `guyaspace-experience-kourou_aircraft.csv`. Built by `build_gy.py`.

## File / row-count table

| slug | site | country | rows | tails |
|---|---|---|---|---|
| guyaspace-experience-kourou | Guyaspace Expérience (Centre Spatial Guyanais), Kourou | French Guiana | 1 (Ariane 5 full-scale mock-up) | 0 (n/a for a rocket model) |
| — | Guyana | Guyana | 0 | — |
| — | Suriname | Suriname | 0 | — |

Result: **one site, one record**. Guyana and Suriname searched empty (details below). These are genuinely small aviation-heritage countries; the empty results are findings, not gaps in effort.

## French Guiana

### Recorded
**Guyaspace Expérience (ex-Musée de l'Espace), Centre Spatial Guyanais, Route de l'Espace, 97310 Kourou.** Opened 1996, closed Sept 2022 for a €7.5 M rebuild (CNES with Semeccel/Cité de l'Espace), reopened 26 July 2024 under the new name. Mon-Sat 09:00-18:00 plus first Sunday of the month; €10 adult / €6 child; 33,000 visitors in the first year (Semeccel). Sources: fr.wikipedia "Guyaspace Expérience" (raw wikitext fetched), Guyaweb 2024, franceguyane, Semeccel, CNES visitor site, Petit Futé, guyane-amazonie.fr.

- **Ariane 5 full-scale mock-up** — outdoors at the CSG reception/entrance with an Earth globe. Recorded as `missile_rocket` / `launch_vehicle`, description flags it as a *display model, not flight hardware*. Currency: Sagaphoto Oct 2018 ("fusée Ariane 5 à l'échelle 1 à l'entrée du CNES"); Wikimedia Commons "Maquette Ariane 5 à l'accueil du centre spatial guyanais" 5 Sept 2022 (camera position 5.168644, -52.683498 — used as the site coordinates); instinct-voyageur travel report 2023/24 photo; Petit Futé visitor comments after the 2024 reopening about "full-scale rocket models outside". Manufacturer given as ArianeGroup (design authority), tail blank.
- Inside (not recorded — components, not vehicles): Vulcain engine (Commons photo), HM7 combustion chamber, Viking injector, Ariane 4 booster cut-away, payload fairing, ERS-1 / XMM-Newton / Meteosat satellite models, Soviet SK-1 and US Mark IV suits (buran-energia.com visit report, pre-2022 layout — the new layout is "maquettes de lanceurs et de satellites" per CNES; whether every pre-2022 item returned is unknown).

### Searched empty / excluded
- **Ariane 1, Diamant, Véronique full-scale models at Kourou** — none found. The full-scale Ariane 1 is at Le Bourget (Musée de l'Air et de l'Espace); Diamant and Véronique are represented at Kourou only by the historic launch sites (ELM-Diamant, visited on the CSG bus tour) and scale models. No "rond-point" rocket in Kourou town found.
- **BA 367 "Capitaine François Massé", Cayenne-Rochambeau** — no gate guard or heritage aircraft in the 50th-anniversary coverage (Oct 2024) or the Puma farewell (Aug 2026, five Pumas withdrawn, replaced by H225M Caracal — disposal not stated; **re-check in 2027 whether a Puma became a monument**).
- **Gendarmerie SAG Cayenne, 3e REI Kourou, 9e RIMa** — no displayed aircraft found (French, English searches).
- **Cayenne-Félix Eboué airport, Air Guyane heritage** — nothing.
- **Musée départemental Alexandre-Franconie / Musée des cultures guyanaises** — no aircraft.

## Guyana

### Searched empty
- **Guyana Defence Force Air Corps (Air Station London, Timehri / Camp Ayanganna)**: Shorts Skyvan 3M **8R-GGK** (c/n SH.1980, ex G-BLLI, Barbados govt 1984, Guyana Airways 1987-2001, GDF 2001-22) made its last flight 5 Oct 2022; the Chief of Staff said it "will be mounted in a prominent place at Air Station London" (Stabroek News 6 Oct 2022). **No evidence found of the mounting having happened (2023-26)** — searched news, JetPhotos (last photo Boa Vista Aug 2022), airhistory. Intent only → not recorded. **Top re-check item for Guyana.**
- Camp Ayanganna military museum (National Trust listing: museum, veterans monument, three cannons) — no aircraft.
- Guyana National Museum, Museum of African Heritage — no aircraft.
- Ogle/Eugene F. Correia airport, Linden, New Amsterdam, Bartica, Lethem — no monuments found. JetPhotos Guyana page shows only active aircraft.
- Historic GDF losses (Skyvans 8R-GFF 1981, 8R-GMC 2003; Rotorway 8R-GLA 2005) — crashed, not preserved. Bell 206s 8R-GEX/GEY — in service per aeroflight.

## Suriname

### Searched empty
- **Surinaamse Luchtmacht (Zorg en Hoop / Zanderij)**: fleet history from aeroflight and Wikipedia (Islanders 001-004, PC-7s 111-113, Alouette IIIs 300/400, Bell 205 300, Cessnas, CASA 212s 212/214 sold to the USA 2012, Chetaks SAF811-813) — no preserved/monument airframes recorded anywhere; the Dutch Wikipedia lists "Lijst van gedenktekens in Suriname" and "…in Paramaribo" (raw wikitext grepped) contain no aircraft, only the SLM 1989 crash memorial sculpture and a 2026 Matapica crash memorial column.
- Fort Zeelandia / Surinaams Museum, Nationaal Militair Museum — no aircraft.
- SLM DC-3/C-47 heritage — none preserved in Suriname found (Dutch and English searches).
- airhistory.net Suriname Air Force and Zorg en Hoop location pages returned 403 (Cloudflare) — **a rerun with browser access should read `airhistory.net/basic-operator/15442/Suriname-Air-Force` and `location/8379/Paramaribo-Zorg-en-Hoop`** to be certain no stored/derelict Islander or Alouette is on display.

## Judgment calls
- The Ariane 5 mock-up is recorded because the brief explicitly asks for CSG full-scale models as `missile_rocket`/`launch_vehicle` with mock-up status flagged. No other mock-up at Kourou could be evidenced.
- Coordinates: camera position of the 2022 Commons photo of the mock-up (within tens of metres of the object). Mappy/TomTom place the museum POI at 5.1691, -52.6836 — consistent.
- `country` for the Kourou row is "French Guiana" (per brief); `state_province` also "French Guiana"; postal code 97310 from the official address.

## Needs a human on site (ranked)
1. Guyana: has Skyvan 8R-GGK been mounted at Air Station London (Cheddi Jagan airport)? If yes it is a `restricted`/gate-visible record with c/n SH.1980, ex G-BLLI.
2. Kourou: confirm the outdoor Ariane 5 mock-up survived the 2022-24 rebuild in place (visitor reports say yes) and whether any other full-scale launcher (Vega, Ariane 6 element) was added outside.
3. Cayenne BA 367: disposition of the five withdrawn Pumas (2026).
4. Suriname: walk Zorg en Hoop for any Islander/Alouette III hulk on display at the Luchtmacht compound.

## Leads for other agents
- None in scope; ex-GDF Skyvan photos are all of the aircraft in Brazil (Boa Vista) while operational.
