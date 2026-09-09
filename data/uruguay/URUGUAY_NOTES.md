# Uruguay — research notes (all three passes)

Researched 9 September 2026. Output: `uy_museums.csv` + 8 per-site aircraft files.

## Tooling caveat (read first)

Mid-run the shared WebSearch budget was exhausted by parallel agents, and every
search engine reachable by curl (Bing, DDG, Brave, Qwant, Mojeek, Marginalia)
served captchas or bot-blocks. The FAU's own sites (`museo.fau.mil.uy`,
`fau.mil.uy`, `ema.fau.mil.uy`, `eta.fau.mil.uy`) present a certificate the proxy
does not trust, so they were read only through the Wayback Machine. Wikimedia's
API rate-limited the shared IP; raw wikitext and category HTML still worked.
No browser was connected, so Google Maps/Street View could not be used.
Consequently the department-by-department Spanish sweep was done through
Wikipedia/Commons categories, Aerial Visuals' Locator, FAU news archives and
photo sites rather than open web search. Coverage of small-town plazas is
therefore weaker than intended — see "Needs a human on site".

## Sources and their weight

1. **Museum's own site (museo.fau.mil.uy, `aeronaves.html`)** — Wayback capture
   of January 2026. Gives the hangar list (34 items) but the per-aircraft
   `FICHAS/` pages were never archived and the live site was redesigned in
   2026 (old URLs now 404), so serials come from elsewhere. Weight: current
   holdings, high.
2. **FAU news (fau.mil.uy, via Wayback)** — authoritative and dated for the June
   2025 AT-6D/A-37B exchange between Durazno and the ETA, the October 2021
   Durazno T-33 allocation, the 2022 Tiger Moth handover, the 2020 Pucará
   monument. High.
3. **Aerial Visuals Locator + airframe dossiers** — the only country-wide
   location list reachable; gave coordinates for Carrasco, Durazno, ETA,
   Laguna del Sauce, Atlántida, and c/ns/ex-serials. It is partly stale: it
   still places Wessex 071 at the museum (it is in Cardona since 2012) and
   Viscount CX-BJA on the airport's west side (moved to the museum 2017).
   Treated as leads plus identity data, not as currency.
4. **Wikimedia Commons** — dated photographs (2011, 2013, 2016, 2017) of museum
   and base aircraft; the "Monuments featuring aircraft in Uruguay" and
   "exteriors of Base Aérea Cesáreo Berisso" categories. Good currency to 2016-17.
5. **JetPhotos** (S-2G 856, June 2019), **helicopterosarg blog** (Wessex 070,
   November 2015), **helis.com** Wessex production list (fates of all eleven FAU
   Wessex), **Aviation Press "Aviación Naval Uruguaya"** (August 2023, naval
   base preserved list), **s2ftracker/grummantracker.com** (Tracker BuNos),
   **aeronavescx.blogspot** (museum visit January 2018), **aerospotter.blogspot**
   (museum survey 2009, old Cilindro site), **Gaceta Aeronáutica** (EMA open
   day October 2016), **Avialatina** (Durazno Pucará monument, August 2020),
   **elacontecer.com.uy** (Durazno open day October 2024; Durazno memorial
   August 2026), **pluna.uy** (Viscount and DC-3 history).
6. **Wikipedia es/en** — museum article (edited January 2026), survivor lists
   (F-80, T-33, C-47, Wessex, A-37). Leads only; the en article's collection list
   still contains aircraft lost in the 1997 fire (Potez 25, Fw 44, DH.60, 14-bis).
7. **aviationmuseum.eu** — lead list only; its museum table mixes eras (lists
   Cessna 170A "736", Queen Air "546", U-206 "744", two PT-26s, a second
   Chipmunk "608") that no dated photo or the museum's own list supports.

## Corrections made

- **Carrasco C-47 "T-510"**: the airframe on the Ruta 101 frontage is ex-USAF
  43-48275 (the former US Air Mission aircraft) painted as FAU T-510; the
  original 510 (42-100558/CX-BJG) was scrapped c.1970 (Aerial Visuals dossier
  65061). Recorded with tail `T-510` and the false serial in aliases.
- **Durazno Pucará "FAU 221"**: the monument airframe is ex-Colombian FAC 2201
  (ex-Argentine A-580), received 2008 as a spares source; the real 221 was
  cannibalised (Avialatina, 18 Aug 2020). Tail recorded as `FAC 2201`, `FAU 221`
  and `A-580` in aliases.
- **Wessex 071 vs 076**: Aerial Visuals and older lists put 071 (ex-XR522) at the
  museum. It left the museum in early 2012 for Cardona (agesor.com 2012; Commons
  photo February 2016). The museum's hangar Wessex is 076 (c/n WA122; Commons
  photo July 2016). Recorded accordingly.
- **AT-6D FAU 350**: moved from the ETA (there since the 1990s) to the Brigada
  Aérea II main access in June 2025; the ETA received A-37B FAU 286 on 12 June
  2025 (FAU news 13 June 2025). Both recorded at their 2025 locations.
- **Viscount CX-BJA**: not at the airport terminal any more — on the museum site
  since 2017, interior restored 2021, opened to visitors on scheduled days.
- **Tracker 856**: no longer stored at Laguna del Sauce (2006-2010 lists); at the
  museum since 2018 (JetPhotos June 2019).
- **B-25J FAU 156**: two USAAF identities circulate (44-30743 via c/n 108-34017;
  43-27847 via c/n 108-34860). Neither put in tail; both in description.
- **T-33 203/205**: the 2009 survey calls 203 the AT-33A (c/n 9889, ex 55-4443)
  and 205 the T-33A; Aerial Visuals calls 203 the T-33A (c/n 580-9887, ex 55-4443)
  and 205 the AT-33A (ex 53-5860). Both rows carry `AT-33A` as alias and the
  ex-serial attributed by the majority of sources.

## Judgment calls

- **Replicas recorded and flagged**: Blériot XI, Castaibert VI and Farman
  "El Palomar" are reproductions built for the museum; each description says
  "Replica, not an original airframe". The full-scale F-51D Mustang "maqueta"
  (a 2020s model, museum news 1021) was **excluded**.
- **Airworthy aircraft**: T-6D FAU 366 (CX-NAT) is the FAU/museum heritage
  flyer (solo flights Dec 2023, Jul 2025). Recorded under the museum as
  `on_display` because it is presented at museum open days; it lives with the
  flying unit, so a weekday visitor may not see it.
- **Nose section**: C-47 "T-521" is a cockpit section only, flagged in aliases
  and description.
- **Lodestar N69415**: unrestored outdoors; recorded `on_display` (visible) with
  condition in description rather than `under_restoration` (no work under way
  per es.wikipedia "a la espera").
- **Access types**: museum `public` (Sundays 13:00-18:00, weekday guided visits
  by arrangement). Brigada Aérea I displays sit inside the base but line
  Ruta 101 and are photographed from the road — recorded `restricted` with that
  note. ETA displays are on the Ruta 102 frontage — `restricted`. Durazno, EMA
  and the naval base — `restricted` (open days once a year). Cardona and
  Atlántida — `public`.
- **Naval Aviation SNJ-4**: tail recorded as `256` (true identity) with the
  painted `A-258` in aliases (Aviation Press 2023; Linea ALA 2010).
- **Chipmunks**: two rows (CX-AVA and G-ANOW) on the strength of separate 2016
  photographs; if the museum has only one, G-ANOW is the one to keep.
- **Coordinates**: museum = Wikipedia/Aerial Visuals hangar position; Carrasco,
  Durazno, ETA, Laguna del Sauce, Atlántida = Aerial Visuals airframe positions;
  EMA = airport reference point (Scramble); Cardona = town centroid (Nominatim).
  Postal code only for Cardona (75200, Nominatim).

## Excluded, and why

- **Durazno city "Plaza de la Aviación" T-33 memorial** — allocated October 2021,
  still unbuilt in August 2026 (elacontecer, 16 Aug 2026). Intent, not arrival.
- **Museo Andes 1972 (Montevideo)** — holds fragments of FH-227D FAU 571 only,
  no airframe.
- **"Museo Berisso" on the 2nd floor of Carrasco airport** — 2010 loan of a
  Castaibert replica and SG-38 glider CX-ALU; no evidence it still exists, and the
  Castaibert is back in the museum hangar. SG-38 CX-ALU whereabouts unknown.
- **HS-125-400 CX-BVD at Ángel Adami airport** — a based/derelict bizjet
  (ex-Argentine Navy 0653), not a display.
- **Wessex 073, 074, 075, 077 (Nueva Helvecia aero club), 079** — scrapped or
  reduced to parachute-training hulks per helis.com; none displayed.
- **Trackers 853, 854, 855 at Laguna del Sauce** — 853/855 dumped behind the
  hangar, 854 held as a hangar reserve airframe (2023): not displays. Jetstream
  T2 875/876 dumped; Bo 105 065 and HB355 071 withdrawn — not displays.
- **F-80C FAU 221** — at the National Museum of the USAF (Dayton) since 1979;
  **F-80C FAU 218** — at the USAF Armament Museum, Eglin (as FT-713). Not in
  Uruguay.
- **Cilindro Municipal site (Montevideo)** — the museum's 1965-2014 home,
  demolished for the Antel Arena. Aerial Visuals still lists it.
- **aviationmuseum.eu extras** (Cessna 170A 736, Beech Queen Air 546, U-206
  744, PT-26A 634 / 42-15361, Chipmunk 608, Piper J-3C S-503 as a second Cub,
  Curtiss CW-22B G2-205 as a second Falcon) — unsupported by any dated photo or
  the museum's own 2026 list; the S-503/CX-AEU Cub and E-205/G2-205 Falcon are
  single aircraft.
- **Curtiss-Wright P-3A "Dehmel" and Thompson Bros P505 Mk V** on the museum's
  list — a ground flight trainer and an item I could not identify as an
  airframe; not recorded.
- **"Ultraliviano motorizado"** on the museum list — type unknown; not recorded.
- **1997 fire losses** (Potez 25 A.2, Fw 44J, DH.60 Gipsy Moth, DH.90 Dragonfly
  "Churrinche", Santos-Dumont 14-bis replica) — still listed by en.wikipedia;
  destroyed 4 December 1997.

## Blank fields, deliberately

- `tail_number` blank for: museum Bo 105 P1, Tiger Moth, three replicas, ETA
  T-33 (serial unread), Neybar is civil CX-AGI.
- `year_built` only for Viscount CX-BJA (first flight 6 Dec 1958, pluna.uy).
- `postal_code` blank except Cardona.
- Museum website given as `https://museo.fau.mil.uy/` (redesigned 2026).

## Needs a human on site (ranked)

1. **FH-227D FAU 572 at Brigada Aérea I** — is the Andes-crash sister ship still
   on the base, and in what state? Only Aerial Visuals and an undated
   pilotoviejo.com photo place it there.
2. **Museum T-33s** — are both 203 and 205 present (museum list shows one
   T-33A)? Read the serials and note which is the AT-33A.
3. **ETA static display** — read the T-33 serial; confirm Wessex 080 at the gate
   and whether 078 is viewable.
4. **EMA Pando** — confirm T-6D 340, T-41D 604 and Blaník 690 still in place
   (last dated evidence October 2016).
5. **Atlántida F-27 CX-BHV** — confirm it still stands on the Interbalnearia and
   what it is used for.
6. **Brigada Aérea I C-47B T-514 and Wessex 072** — confirm presence (helis.com
   and Aerial Visuals only).
7. **Mercedes (Soriano) 2013 memorial** — elacontecer says Mercedes got an
   aircraft memorial in 2013 (after Cardona 2012); type and location unknown.
   Possibly connected to the Tte. Luis Tuya homage. Not recorded.
8. **A-37B fleet retired May 2026 (FAU 270-277 batch plus 28x)** — disposition
   unknown; expect new plaza/base displays in 2026-27.
9. **Museum Bo 105 and Tiger Moth serials**; the Chipmunk count.
10. **Naval base** — is the Bell 47G 055 / T-28S 403 area viewable on open days;
    Tracker 851 on its pylon is visible from the airport road?

Phone: Museo Aeronáutico (+598) 2604 0210 al 14 int. 5003; cel (+598) 98 274 774.

## File / row-count table

| file | site | rows | with tail |
|---|---|---|---|
| uy_museums.csv | 8 sites | 8 | – |
| museo-aeronautico-meregalli_aircraft.csv | Museo Aeronáutico Cnel. (Av.) Jaime Meregalli | 37 | 32 |
| brigada-aerea-i-carrasco_aircraft.csv | Brigada Aérea I, Carrasco | 5 | 5 |
| brigada-aerea-ii-durazno_aircraft.csv | Brigada Aérea II, Durazno | 4 | 4 |
| escuela-tecnica-aeronautica-toledo_aircraft.csv | ETA, Toledo | 4 | 3 |
| escuela-militar-aeronautica-pando_aircraft.csv | EMA, Pando | 3 | 3 |
| base-aeronaval-curbelo-laguna-del-sauce_aircraft.csv | Base Aeronaval Nº 2 | 5 | 5 |
| wessex-cardona_aircraft.csv | Cardona | 1 | 1 |
| f27-atlantida_aircraft.csv | Atlántida | 1 | 1 |
| **total** | | **60** | **54 (90%)** |

## Leads for other agents

- **USA**: F-80C FAU 221 (NMUSAF Dayton, painted 8th FBG) and F-80C FAU 218
  (Eglin Armament Museum, painted FT-713) are ex-Uruguayan airframes — add
  `FAU 221` / `FAU 218` aliases if those records exist.
- **Colombia**: Pucará FAC 2202/2203 (the other ex-FAC airframes sent to
  Uruguay 2008) — not seen in Uruguay; may be parts only.
- **Argentina**: T-34A FAU 636 went to the Bolivian AF in 2000 (Commons caption)
  — Bolivia agent.
- **Paraguay**: CX-BIM (FH-227B, PLUNA) photographed at Asunción 1975 — not
  preserved; ignore if it surfaces.
