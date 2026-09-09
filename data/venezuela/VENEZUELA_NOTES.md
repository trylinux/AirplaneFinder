# Venezuela — research notes (all three passes)

Output directory: `/home/claude/sa/venezuela/`. Built by `build_ve.py` (edit the script, re-run, do not hand-edit the CSVs).

## Files and counts

| file | site | rows | with tail |
|---|---|---|---|
| ve_museums.csv | 12 sites | — | — |
| museo-aeronautico-de-maracay-coronel-luis-hernan-paredes_aircraft.csv | Museo Aeronáutico de Maracay | 45 | 33 |
| museo-del-transporte-guillermo-jose-schael_aircraft.csv | Museo del Transporte, Caracas | 6 | 2 |
| academia-militar-de-la-aviacion-bolivariana-displays-maracay_aircraft.csv | EAM / Academia, Maracay | 3 | 2 |
| base-aerea-teniente-vicente-landaeta-gil-gate-guards-barquis_aircraft.csv | Barquisimeto gate guards | 5 | 5 |
| base-aerea-teniente-luis-del-valle-garcia-canberra-barcelona_aircraft.csv | Barcelona base Canberra | 1 | 1 |
| plaza-el-avion-f-86k-sabre-monument-barcelona_aircraft.csv | Plaza El Avión, Barcelona | 1 | 0 |
| avenida-el-ejercito-f-86k-sabre-monument-maturin_aircraft.csv | Maturín F-86K | 1 | 0 |
| monumento-al-avion-f-86-sabre-calabozo_aircraft.csv | Calabozo F-86 | 1 | 0 |
| t-2d-buckeye-monument-valera_aircraft.csv | Valera T-2D | 1 | 0 |
| monumento-al-aviador-ov-10-bronco-san-francisco-zulia_aircraft.csv | San Francisco (Zulia) OV-10 | 1 | 0 |
| redoma-el-avion-at-6-texan-monument-maracay_aircraft.csv | Redoma El Avión, Maracay | 1 | 0 |
| aeropuerto-tomas-de-heres-flamingo-el-rio-caroni-ciudad-boli_aircraft.csv | Ciudad Bolívar Flamingo | 1 | 1 |
| **total** | **12** | **68** | **50 (74%)** |

## Sources and weight

1. **aerialvisuals.ca Location Dossier 4170 ("Museo de la Fuerza Aerea Venezolana")** — 37 airframe dossiers, most with a David Osborn photo dated 26-27 June 2012 and per-site GPS. Best structured source for serials/c-ns; but it is a 2012 snapshot. Coordinates in `ve_museums.csv` for the museum are the AV site cluster (10.2526,-67.5951 ≈ museum ramp).
2. **Wikimedia Commons, Category:Aircraft at Museo Aeronáutico de Maracay** (Aeroprints June 2012 set + Carlos E. Pérez S.L. photos December 2013 / February 2016 + Muago September 2021) — gave the F-16A 6023, Tucano 2820, Alouette III 2112, PT-19A 0271, VF-5A and Tacarigua replica that AV lacks.
3. **Steemit visitor report dated 12 August 2025** (checked the raw JSON `created` timestamp 2025-08-13) — confirms the museum open, entry US$1, hours Mon-Fri 08:30-11:30/13:00-16:30, Sat-Sun 09:00-17:00, and shows DC-3, C-49 4AT1, C-54, C-123B, both Jet Provosts, Tucano, F-16, Stearman ×2, G.222 (walk-in "simulator"), UH-19B. Google reviews via wanderlog dated July 2024 – December 2025 corroborate ("planes dirty and covered in cobwebs", "some airplanes you can enter").
4. **jetphotos.com** (via WebFetch) — Barquisimeto gate guards (July 2009 / February 2017), Barcelona Canberra 0923 (October 2011), EAM AT-6G 2506 (July 2008), museum photos 2009-2011.
5. **airhistory.net** photo remarks for the museum's "YV-C-AKE" DC-3 (2007, 2012) — establishes the false identity.
6. **douglasdc3.com Venezuela register** — DC-3 identities at the museum and Museo del Transporte; undated compilation, treated as lead only.
7. **warbirdregistry.org** — B-25 histories (43-28096, 44-30631).
8. **Wikipedia (es/en)** — museum background, Redoma El Avión; en "List of displayed F-16s" (6023 at Maracay); "List of surviving Vampires" (3C35, 1E35).
9. **FAV-CLUB blog (favclubven.wordpress.com)** — historical photos of the Venom at the museum 1970; no current inventory.
10. **Venelogía (2010)** — OV-10 monument in San Francisco, Zulia. **Wikimedia Commons** single files — Maturín F-86K (2017), Barcelona Plaza El Avión (2023, April 2025), Calabozo F-86 (2014/2017), Valera/Trujillo T-2D (2008/2013), EAM parade-ground F-86 (2012).
11. **virtualglobetrotting.com** — "Aircraft static display, Barquisimeto" pin 2022-07 at 10.0461,-69.3663 (base gate), "Venezuelan Air Force Museum" pin at Palo Negro 10.17883,-67.55114 (2013) — see Leads.
12. The-Northrop-F-5-enthusiast-page (Venezuela) — NF-5A/CF-5 preservation notes (no serials).
13. **Grokipedia not used.** Airliners.net returned HTTP 402 to the fetcher; abpic/airhistory search pages returned 403. **Web search quota was exhausted at ~two-thirds of the run**, so the monument pass for Venezuela relied on Commons searches, Wikipedia and jetphotos rather than Google/Bing — coverage of small-town monuments is therefore incomplete (see "needs a human").

## Currency rule applied

Venezuela is a hard country for currency. Every row states its latest dated evidence. Rows resting only on pre-2019 evidence are flagged "— flagged" / "no 2022-26 confirmation" in `description`: Barquisimeto (2009/2017), Barcelona base Canberra (2011), Maturín F-86K (2017), Calabozo F-86 (2014/2017), Valera T-2D (2008/2013), San Francisco OV-10 (2010), EAM displays (2008-2012), the Flamingo (2017 article; 2022 map pin only). The Maracay museum as a whole has 2025 confirmation but individual small airframes (Rand KR-2S 2011, glider, autogiro, DC-3 nose) do not.

## Corrections and judgment calls

- **Museum name**: recorded as "Museo Aeronáutico de Maracay Coronel Luis Hernán Paredes" (its formal name; also called Museo Aeronáutico de la FAV / Fundación Museo Aeronáutico). Access `public` (walk-up, US$1 in 2025).
- **DC-3 "YV-C-AKE"**: the real YV-C-AKE (c/n 4705) crashed at Canaima 27 Aug 1972 with 34 dead (aerialvisuals dossier quotes the ASN summary). The museum aircraft is an ex-FAV extended-nose DC-3 repainted in Aeropostal colours by 1999 (airhistory.net). tail_number left blank, YV-C-AKE in aliases.
- **C-47A c/n 12386 (YV-T-RTC, painted 1840)**: douglasdc3.com puts it with the "Escuadrón Legendario" at Palo Negro; aerialvisuals (site C, GPS) and an October 2011 airliners.net photo put it at the museum. Recorded at the museum; tail = last true identity YV-T-RTC, painted 1840 in aliases.
- **C-49K c/n 4984**: displayed in FAV colours as 4AT1 (never an FAV aircraft). tail = N207U (last registration), 4AT1 in aliases.
- **B-25J 5B40**: real FAV serial 5B40 (ex 43-28096); painted 2B40 since c.1979. tail 5B40, 2B40 alias.
- **F-86K 0984 / c/n 242-31**: aerialvisuals gives ex 56-4146; recorded. **Barquisimeto F-86K 5627** c/n 242-43, jetphotos says "delivered 1956 to USAF as 4158" → 56-4158.
- **Canberra 6409**: aerialvisuals says B.2 with markings 2-A-39; Commons caption says B.82 (Venezuela's B.2s were refurbished to B.82). Variant recorded B.2, B.82 in aliases.
- **Vampire 3C35**: AV says FB.5, Wikipedia FB.52. Recorded FB.5 with FB.52 alias.
- **Caudron G.3**: aerialvisuals says replica; es.wikipedia says original restored in 1987. Recorded as one row with the doubt stated; not marked as replica in the type field.
- **HD-1ET Tacarigua**: a full-scale replica (2021) — recorded, description says replica.
- **Two Stearmans**: PT-17 41-7888/N14RL marked "1" (AV dossier) and a second A75N1 marked "7" (jetphotos 2011; both visible in the August 2025 report as two separate photos). Second row has no serial.
- **Autogiro 1XDT**: manufacturer/type unidentified; manufacturer field "Unknown". Human needed.
- **S-2 Tracker BuNo 149867**: Venezuelan Navy machine; Venezuelan serial unknown → tail blank, BuNo in aliases.
- **Harvard II E-96 (N20240)**: aerialvisuals says "based at museum" but its only photo (2008) says preserved at the Escuela de Aviación Militar; recorded at the EAM site, not the museum (one place only).
- **AT-6G 2506 / c/n 84-7448**: jetphotos "former USAF 41-1707" is not consistent with c/n 84-7448 (a 42-84xxx block); the US serial was NOT entered.
- **Barquisimeto NF-5B "27761"**: unusual marking (probably a painted serial); recorded as tail because it is what the airframe wears and no other FAV serial is known. NF-5B 1711 ex K-4018. VF-5A 3318 (wfu/stored 2009) NOT recorded — not a display.
- **Plaza El Avión, Barcelona** F-86K painted 4341 — an F-86K would not have carried a 43xx FAV serial in the old system; treated as a painted number (alias), tail blank.
- **Valera vs Trujillo**: the same Commons author captioned the T-2D "Valera – Edo. Trujillo" (2008) and "parque Fuerza Armadas Naciones en Trujillo" (2013). Recorded under Valera; city needs checking.
- **Museo del Transporte**: TSJ ruling of 20 June 2024 ordered the museum to vacate its land; a Google review dated 11 September 2025 says it is "still under renovation" with more vehicles arriving, so it is kept as `public` (Sundays 09-16). Its six aircraft are listed from the museum's own literature (IAM Venezuela 2018 / Morfema 2021) plus dated photos of the DC-3 (2014) and Skyvan (2012). The "Fairchild PT 19 (1937) biplane" of the museum text is recorded as a PT-19 (monoplane) — verify; the Aeronca model (7AC assumed) and C-45/AT-6 serials are unknown.
- **Access types**: Maracay museum, Museo del Transporte, plazas/redomas, Ciudad Bolívar airport frontage = `public`; base gate displays (Barquisimeto, Barcelona base, EAM/Academia) = `restricted` even where the gate guard is visible from the road.
- **Coordinates**: given only for the Maracay museum (AV/Commons camera positions), Museo del Transporte (IAM Venezuela article) and the Barquisimeto gate (virtualglobetrotting pin). All others blank — never guessed.

## Excluded (and why)

- **Redoma El Avión "fuerza aérea propia" (2014 plan)** to add a Tucano, OV-10, Mirage 50EV and F-16 around the Maracay roundabout — no evidence it was carried out (2018 blog still describes a single aircraft). Only the AT-6 recorded.
- **F-86K 0014** — ex-FAV, but at the Museu Aeroespacial, Rio de Janeiro (Brazil agent). **F-86K ex-FAV at Palanquero** — Colombia agent.
- **Mirage 50EV 3373 and 0155** photographed at El Libertador 2009 — transferred to Ecuador, operational, not displays.
- **T-2D Buckeye 4380, VF-5A 9456, OV-10A 0068/9004, Mirage 50 2353/7512, NF-5B 6372** at El Libertador 2009-2012 — "Open Doors" static show aircraft, not preserved displays.
- **F-16A 7268 at El Libertador and five Su-30MK2 at Barcelona (29-30 November 2025, pucara.org)** — out-of-service airframes wheeled out for the Aviation Day exposition; not permanent displays (and Su-30s are operational assets).
- **Bell 205A-1 1678 (Maracay 2007)** — withdrawn and stored for training; not a display.
- **VF-5A 3318 Barquisimeto** — stored, 2009.
- **NF-5A "in Barquisimeto town, damaged/destroyed by vandals"** (F-5 enthusiast page) — location unknown and reported destroyed; not recorded.
- **Flamingo replica built by Pedro Urbano 1974-75** for the Maracay museum — moved to El Libertador for restoration and "eventually disappeared" (aviacioncivil.com.ve).
- **Unmarked glider (2012) and "Icarus" (2013)** at the Maracay museum — unidentified types with a single old photo each; not recorded (a human should list them).
- **DC-3s YV-13C (Sufi), YV-146C (Higuerote), YV-911C (Valencia), YV-426C (Caracas wreck), YV-O-MTC-12 (Maiquetía wreck)** from douglasdc3.com — stored/wrecks, not displays.
- **Fairchild FH-227 etc.** — none found. **Aeropostal DC-9-32 "El Guarito"** (retired March 2011): es.wikipedia mentions it in the museum article context but no photo or report places it at the museum; NOT recorded — needs checking.
- **Museo Naval / Cuartel de la Montaña / Museo de Ciencias / Maiquetía / Los Roques / Mérida / Puerto Ordaz / Maturín base / Boca de Río / La Carlota / Army & Navy aviation** — no evidence of displayed airframes found within the available search budget (La Carlota base: Commons has only operational-helicopter photos).

## Blank fields, deliberately

- `year_built` blank throughout except none — no sourced build dates entered.
- `tail_number` blank for: Caudron G.3, Tacarigua replica, second Stearman, Aeropostal-painted DC-3, VF-5A at the museum, S-2 Tracker, KR-2S, Redoma AT-6, EAM F-86, all F-86 monuments (Barcelona/Maturín/Calabozo), Valera T-2D, Zulia OV-10, four Museo del Transporte airframes.
- `postal_code` blank everywhere (Maracay 2101 is in the address field only).

## Needs a human on site (ranked)

1. **Museo Aeronáutico de Maracay full inventory** — walk the ramp and hangar with the 45-row list: confirm the F-5, Mirage 50EV 4058, both Buckeyes, OV-10E, P-47D, both Sabres, Canberra, Vampires/Venom, S-2, Bell 47J, Dragonfly, Alouette III, PT-19A, MS.147 and the Caudron (original or replica?) are still present after the 2019-2024 crisis; identify the autogiro "1XDT", the glider and the "Icarus"; check whether the DC-3 nose YV-C-ANI exists; check whether the DC-9 "El Guarito" or the HS 748 ever arrived.
2. **Barquisimeto gate** — which of F-86K 5627, B-25J 4B40, NF-5B 27761/1711, VF-5A 3274 still stand (only a 2022 map pin says "something" is there).
3. **Museo del Transporte, Caracas** — did the June 2024 eviction proceed; are the six aircraft still in the hangar?
4. **Maturín, Calabozo, Valera/Trujillo, San Francisco (Zulia)** monuments — 2024-26 photos and serials.
5. **EAM / Academia Militar de la Aviación** — serials of the parade-ground F-86 and the red-and-white aircraft behind it; whether AT-6G 2506 and Harvard E-96 survive.
6. **Base Aérea Barcelona** Canberra 0923 — still at the gate?
7. **Ciudad Bolívar Flamingo** — condition; there were restoration promises.

## Leads for other agents / coordinator

- **virtualglobetrotting "Venezuelan Air Force Museum", Palo Negro, 10.17883,-67.55114 (2013)** — a display area inside Base Aérea El Libertador (possibly the "Escuadrón Legendario" collection that douglasdc3.com mentions, where DC-3 YV-T-RTC was reported). Inside the base; not visitable; not recorded. Worth a satellite look.
- **F-86K 0014 (ex-FAV)** at Museu Aeroespacial, Rio de Janeiro — Brazil file. **Ex-FAV F-86K at Palanquero** — Colombia file. **Mirage 50EV 3373/0155** went to Ecuador (operational 2010).
- **Aeroprints / Ken Meegan Flickr sets (June 2012, October 2014)** cover both Venezuelan museums thoroughly if someone can browse Flickr.
