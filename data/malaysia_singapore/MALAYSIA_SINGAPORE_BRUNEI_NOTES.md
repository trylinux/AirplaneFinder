# Malaysia, Singapore and Brunei — research notes

Directory: `/home/claude/seasia/malaysia_singapore/`
Research date: September 2026. Everything below is stated as of that date.

- 22 sites: 15 Malaysia, 6 Singapore, 1 Brunei.
- 79 aircraft/weapon rows.
- Six sites carry a header-only aircraft CSV. That is deliberate — the site is real and an
  airframe is on it, but nothing published names the type, and a guessed type is worse than
  a blank file. Each is listed under "Sites recorded with no aircraft rows" below.

Local names (the museum CSVs use the English name a visitor would recognise):

| CSV name | Local name |
|---|---|
| Royal Malaysian Air Force Museum | Muzium Tentera Udara Diraja Malaysia / Muzium TUDM |
| Malaysian Army Museum | Muzium Tentera Darat |
| Royal Malaysian Navy Museum | Muzium Tentera Laut Diraja Malaysia / Muzium TLDM |
| National Museum of Malaysia | Muzium Negara |
| Royal Malaysian Police Museum | Muzium Polis Diraja Malaysia |
| Perak Museum | Muzium Perak |
| National Heroes Square Putrajaya | Dataran Pahlawan Negara |
| Kuala Kangsar Skyhawk Monument | Laman Pahlawan, Bukit Chandan |
| Royal Brunei Armed Forces Museum | Muzium Angkatan Bersenjata Diraja Brunei |

---

## 1. The two big corrections

### 1.1 The RMAF Museum is not at Sungai Besi and is not open

This is the single most important finding, and every compiled directory still gets it wrong.

- `jmm.gov.my` (Department of Museums Malaysia, the museum's own parent body) still publishes
  the museum at "D/A Pangkalan Udara K.L, Jalan Lapangan Terbang Lama, 50460 Kuala Lumpur",
  open daily 09:00–17:00, tel 03-21171133. **That page is stale by roughly nine years.**
- `aviationmuseum.eu` still gives the same Kuala Lumpur address (it does at least flag
  "currently closed").
- RMAF Kuala Lumpur (Sungai Besi) air base formally shut down in March 2018, the site handed
  over for the Bandar Malaysia redevelopment. `malaysia-traveller.com` recorded the museum as
  permanently closed from December 2017.
- The collection was moved to **RMAF Sendayan Air Base, Negeri Sembilan** in phases from
  September 2021 (the museum's own Facebook page documents "Projek Perpindahan Muzium TUDM
  Fasa 1B" dated 14 Sep 21). An RMAF news item of 12 November 2020 describes the museum as
  "temporarily housed at the former location of PDRM Air Unit quarters".
- A TripAdvisor review of November 2024 independently states the museum "was relocated at
  Sendayan Air Force Base, Bandar Sri Sendayan, Negeri Sembilan".
- Free Malaysia Today, 27 March 2025: a purpose-built RM45 million museum on a 3.52-hectare
  site at Bandar Baru Sendayan, opposite Sri Sendayan Mosque, with its own access road via
  Kampung Felda Sendayan separate from the air base. Tender was to close in May 2025 with
  construction from July 2025 and completion timed for the RMAF's 70th anniversary,
  **1 June 2028**.

Consequences applied to the data:

- `access_type` = `restricted`. Today the collection sits behind a military gate with no
  walk-up access. When the Sendayan building opens this becomes `public` and the coordinates
  should move to the new site.
- `display_status` = `in_storage` for all 37 airframes, not `on_display`. An enthusiast
  account (acesflyinghigh, 2018) describes the aircraft as having been moved to "an
  unsheltered location with no public access". They are held, not exhibited.
- Coordinates 2.6853 / 101.8440 are the Sri Sendayan Mosque node, used as the best available
  anchor for the Bandar Baru Sendayan museum site. **This is an approximate locality position,
  not a surveyed airframe position.** The air base holding the collection is adjacent and is
  not mapped in OurAirports or Wikipedia with coordinates.
- The 37-airframe inventory is the pre-move Sungai Besi list from aviationmuseum.eu. Arrival
  at Sendayan is documented for the collection as a whole, not airframe by airframe. If any
  individual aircraft was scrapped, gate-guarded elsewhere or sold during the move, this list
  would not show it.

### 1.2 The RSAF Museum closed for a year and reopened in June 2026

- Closed for refurbishment September 2025, reopened **17 June 2026**; the official launch
  speech by the Senior Minister of State for Defence is dated 16 June 2026.
- It now charges: free for Singaporeans/PRs and foreign military personnel, from S$5 for
  foreign visitors, tickets pre-booked through Defence Collective Singapore.
- Hours: 10:00–17:00, **closed Wednesdays**. Older directories give 08:30–17:00 Tue–Sun and
  free entry; both are now wrong.
- The aircraft survived the refresh. Post-reopening reporting confirms the Hunter and F-5S
  indoors, the E-2C Hawkeye and a Super Puma outdoors, and one of the two 1968 Singapore
  Flying Club Cessna 172s hanging in the new gallery.

---

## 2. Sources used, and how each behaved

**Reliable and current**
- `defencecollectivesg.com` — the RSAF Museum's own operator. Authoritative on hours,
  admission and the reopening date. Says nothing about individual airframes.
- `mindef.gov.sg` reopening speech, 16 June 2026 — confirmed the Cessna 172 by provenance.
- `airhistory.net` collection 122 (RSAF Museum) — dated photographs, 28 Feb 2019,
  27 Feb 2024 and 19 Sep 2024. The best currency evidence found for Singapore and the source
  preferred wherever it conflicts with a compiled list.
- `freemalaysiatoday.com`, 27 Mar 2025 — the new Sendayan museum project.
- `airforce.mil.my` news items — dated, official, thin on serials.
- OpenStreetMap via Overpass (`historic=aircraft`) — the single most productive discovery
  tool for this region. It found nine Malaysian and two Singaporean airframes that no
  aviation directory lists at all. It very rarely records the type.

**Useful but stale or thin**
- `aviationmuseum.eu` — the only published inventory for the RMAF Museum and the Port Dickson
  Army Museum, and a good cross-check for the RSAF Museum. Lead generation only per the spec,
  and it shows: stale address for the RMAF Museum, a duplicated FM-1054, an impossible
  Tebuan serial, "CL-14G-5" for CL-41G-5, and at least one serial that contradicts an airframe
  registry (below).
- `jmm.gov.my` — stale on the RMAF Museum; correct on the Port Dickson Army Museum.
- `aerialvisuals.ca` — good for construction numbers and for catching serial conflicts, but
  its Malaysian coverage is patchy (no record at all for FM-1902, FM-1907, FM-1051, FM-1054,
  M27-04, M42-06).
- `en.wikipedia.org` "List of displayed Douglas A-4 Skyhawks" — supplied the BuNos for every
  Singapore Skyhawk and found two Singapore sites (Discovery Centre, SAFTI). No Malaysian or
  Bruneian entries at all.
- `ms.wikipedia.org` "Muzium Tentera Udara Diraja Malaysia" — four sentences, still says
  Kuala Lumpur, gives "18 pesawat" against 37 in the survey. Not usable.
- `asisbiz.com` and `acesflyinghigh.wordpress.com` — the only sources that name FM1064 and
  the Kuala Kangsar Skyhawk. Photos from 2001 and 2018 respectively.

**Blocked or unavailable**
- `malaysiandefence.com` returns 403 to every automated fetch. Its articles on the Sendayan
  museum and on the MiG-29N gate guards were reachable only through search snippets and a
  single successful fetch of "First Fulcrum as Gate Guard". A human browser would get more
  out of this site than any other Malaysian source.
- `adf-serials.com.au` — TLS hostname mismatch and 406; its CAC Sabre survivors page would
  probably resolve the two RMAF Sabre serials and possibly the Taiping one.
- `facebook.com/tudmrasmi` and `facebook.com/RMAF-Museum` — robots-disallowed. The RMAF
  Museum's own Facebook page is where the move was documented and is the best remaining
  public record of what actually reached Sendayan.
- `pacificwrecks.com` — rate-limited (429) throughout.
- Grokipedia appeared in search results for several queries and was **not used**.

---

## 3. Corrections made, with the evidence

1. **Port Dickson Army Museum Tebuan is not M22-05.** aviationmuseum.eu lists a
   "Canadair CL-41G-5 Tutor M22-05" at Muzium Tentera Darat. Aerial Visuals airframe dossier
   16445 records CL-41G Tebuan c/n 2201, last military serial M22-05 RMaAF, last civil
   registration N401AG, "Latest Owner or Location: Embry-Riddle Aeronautical Univ, Daytona
   Beach Regional Airport, Daytona Beach, Florida". Both cannot be true. `tail_number` left
   blank; "M22-05" carried in `aliases` as the reported marking; the conflict is written into
   the description. **This is the one row most likely to be a painted-marking error rather
   than a real identity.**
2. **RMAF Museum Tebuan "FM-2201" is not a valid serial.** RMAF Tebuans were delivered as
   FM-1121 to FM-1140 and reserialled M22-01 to M22-20. FM-2201 fits neither series and looks
   like c/n 2201 transposed into a serial. `tail_number` blank, marking in `aliases`.
   The companion aircraft FM-1125 is a plausible serial and was kept.
3. **FM-1054 was listed twice** by aviationmuseum.eu, once as a de Havilland DH.114 Heron 2D
   and once as a "Riley Heron 2D/A2". One airframe cannot be in two rows, so it is recorded
   once, as a Heron, with the Riley conversion noted in the description.
4. **"Canadair CL-14G-5"** in the source is a typo for CL-41G-5; corrected silently.
5. **RSAF UH-1 258 variant.** airhistory.net photo captions (2019 and 2024) say UH-1B;
   aviationmuseum.eu says UH-1H. The dated photograph wins; UH-1B recorded.
6. **RSAF Hunters 501 and 527** are listed as "Hunter F.6" by aviationmuseum.eu and as
   "FGA74S" by airhistory.net. Recorded as FGA.74, with the F.6 origin explained in the
   description and carried in `aliases`, since the RSAF FGA.74 was a rebuild of F.6 airframes.
7. **RSAF 800** is called an "F-5S Freedom Fighter" by aviationmuseum.eu. The RSAF F-5S was an
   upgrade of the F-5E Tiger II, not a Freedom Fighter; recorded as F-5 / variant S,
   model_name Tiger II.
8. **The Royal Malaysian Navy Museum is in Melaka, not Lumut.** The seed lead placed it at
   Lumut; it moved to Melaka in 1995. Coordinates and city corrected.
9. **There is no surviving "Muzium Pengangkutan Melaka".** asisbiz and acesflyinghigh both
   place Twin Pioneer FM1064 at a Melaka Transport Museum. The Melaka Museums Corporation
   (PERZIM) current museum list contains no transport museum, and an OSM query within 250 m of
   the airframe returns only the Melaka Islamic Museum and the Dataran Pahlawan mall. The site
   is therefore recorded as an open-air monument under the name of the aircraft.

---

## 4. Judgment calls

- **Wreckage and part-airframes are recorded as sites' aircraft, flagged in the description:**
  the RSAF Museum's TA-4S 651 (forward fuselage and cockpit only), the Singapore Discovery
  Centre's Hunter 505 (nose section only), the RMAF Museum's Rakan Musa RMX-4 (fuselage only)
  and its Eurocopter AS355N 9M-PHD (held as a wreck).
- **The RMAF Museum's AS355N 9M-PHD, KR-2 9M-KPA, RotorWay Executive and RotorWay Scorpion
  9M-ARY are civilian**, not military, and are marked so. The Westland Wasp M499-04 in the
  same collection is a Royal Malaysian Navy airframe, recorded where it is rather than by
  owner, per the spec.
- **The Igla row in the RSAF Museum file is a weapon system, not an aircraft.** It is included
  because the spec's schema carries `missile_rocket`, and because it is a permanent post-2026
  exhibit. It is a Russian Igla launcher mounted on an American armoured personnel carrier;
  no serial exists to record.
- **The Flightship Airfish 3 at the Science Centre is a wing-in-ground-effect craft**, not a
  conventional aeroplane. Recorded as `fixed_wing` / `experimental` with the ambiguity spelled
  out in the description.
- **The Boeing 737-301 at ITE College Central is an instructional airframe**, not a monument.
  It is a retired, non-operational airframe on a campus, which the spec's phase 3 covers.
  `access_type` = `appointment` because a member of the public cannot simply walk onto a
  campus workshop apron.
- **No replicas or mockups were found** in any of the three countries. Everything recorded is
  believed to be a real airframe. The Sekinchan aeroplane-shaped bus terminal (Selangor), the
  "Mini Aircraft" artwork in Kedah and "Coach MY airplane" in Negeri Sembilan turned up in the
  OSM sweep and were excluded as sculpture or themed architecture, not airframes.
- **`access_type` for the RMAF Museum, RMAF Kuantan, RMAF Kuching, the Joint Force HQ MiG-29N,
  SAFTI and Tengah** is `restricted` because entry is through a controlled military gate,
  regardless of the fact that the Tengah gate guard is visible from a public road.
- **The Royal Brunei Armed Forces Museum is `restricted`**: entry is free, but the museum sits
  inside Bolkiah Garrison and reviewers report finding it closed within its stated hours.
- **`year_built` is blank on 78 of 79 rows.** No construction, roll-out or delivery date was
  found for almost anything here, and a serial is never a year. The one exception is Twin
  Pioneer FM1064, given 1961 and explicitly flagged as inferred from its 18 January 1962
  delivery date — it should be dropped if that bothers the importer.

---

## 5. Sites recorded with no aircraft rows

Each of these has a real displayed airframe on it. None of them has a published type.

| Site | Evidence | What is missing |
|---|---|---|
| RMAF Kuantan Air Base Aircraft Display | Four OSM `historic=aircraft` nodes at 3.7597–3.7598 / 103.205, Bandar Baru Jaya Gading, tagged `tourism=attraction`, mapped around 2020–2021. 400 m from the Kelab Rekreasi Angkatan Tentera and inside the base's domestic area | Four types and serials |
| RMAF Kuching Air Base Gate Guards | Two OSM nodes at 1.4796/110.3393 and 1.4846/110.3506, on the Kuching International Airport perimeter, within the RMAF Kuching Air Base footprint (1.4871/110.3419). The base historically flew Twin Pioneer, Alouette III, Caribou and Sea King | Two types and serials |
| Sri Aman Old Airport Aircraft Monument | OSM node 12945875161 with `inscription=Old Simanggang Airport Runway`, on Jalan Lapangan Terbang Lama beside the Sri Aman sports complex | Type and serial |
| Ayer Keroh Aeroplane Monument | OSM node 2.22751/102.26618 named simply "Aeroplane" on Lebuh Ayer Keroh, next to the International College of Yayasan Melaka. Distinct from the Twin Pioneer 5 km away in Bandar Hilir | Type and serial |
| Seri Kembangan Aircraft Display | OSM node 10727740805 at 3.04486/101.70876 on the Sungai Besi expressway near the Mines Selatan toll plaza and Palace of the Golden Horses | Type, serial, and confirmation it is an airframe rather than signage. **Weakest site in the set** |
| Royal Brunei Armed Forces Museum | Museum's own outdoor display, confirmed by traveller photographs showing a helicopter beside armoured vehicles; Wanderlog describes visitors being able to climb into it | Helicopter type and serial |

The Royal Malaysian Police Museum also has a header-only file: an OSM `historic=aircraft` node
sits 38 m from the museum building at 5 Jalan Perdana, but nothing published says what it is.
The Wikipedia article describes three interior galleries and no outdoor exhibits.

---

## 6. Excluded, and why — so nobody researches them again

- **RMAF Gong Kedak base museum.** A Malay-language report (rentaka.weebly.com) says a museum
  opened in the technical section of Pangkalan Udara Gong Kedak in January 2014, in a former
  military court building, showing "pesawat pemintas F-5E" and "Sukhoi Su-30MKM". The Su-30MKM
  is the base's active type, which makes the whole passage read like a display *about*
  aircraft — photographs, models, weapons — rather than airframes. One source, twelve years
  old, ambiguous. **Not a site row; the best single lead left in Malaysia.**
- **RMAF Subang and Sultan Abdul Aziz Shah Airport displays.** Searched in English and Malay;
  no evidence of any preserved airframe, and no OSM node. The RMAF Subang page on
  airforce.mil.my lists no heritage display.
- **RMAF Butterworth Sabre gate guard.** A War Thunder forum thread is titled "CA-27 Mk.32
  Sabre – RMAF Butterworth's old Gate Keeper", but the thread body identifies no airframe at
  Butterworth; the aircraft it actually discusses, A94-983/FMI983, went home to Temora Aviation
  Museum in Australia. The word "old" in the thread title suggests the gate guard is gone.
  No OSM node at Butterworth. Excluded until someone photographs the gate.
- **RMAF Labuan, Alor Setar, Ipoh.** No gate-guard evidence in any language and no OSM nodes.
- **Penang War Museum (Bukit Batu Maung).** A restored 1930s British hill fort. Tunnels, gun
  emplacements, no aircraft.
- **Sarawak and Sabah state museums, Labuan Museum, Sandakan.** No aircraft. The only Borneo
  airframes found are the two at Kuching airport and the one at Sri Aman.
- **UniKL MIAT and UPM.** UniKL MIAT's own facilities pages describe hangars, engines and
  training rigs but name no preserved airframe, and no OSM node exists at either campus.
  Malaysia's aerospace training airframes are almost certainly there, but nothing is published.
- **Preserved Malaysian airliners (MAS 737 / Fokker F27, AirAsia display airframes).** Nothing
  found. No survivor list, no OSM node, no photograph. If any exist they are inside the
  Malaysia Airlines Academy or the AirAsia academy at Sepang, behind a fence.
- **Army Museum of Singapore (ARMS), 520 Upper Jurong Road.** Eight galleries on the Singapore
  Army; no aircraft in any description. The A-4S 690 that some lists attach to "SAFTI" is at
  the SAFTI Military Institute compound, recorded separately.
- **Changi Aviation Gallery, Changi Airport Terminal 3.** Models, simulators and interactives.
  No airframe found in any account.
- **Seletar Aerospace Park.** An industrial estate. No heritage airframe found.
- **Royal Regalia Museum, Bandar Seri Begawan.** Royal chariot, gifts and regalia. No aircraft.
- **Sekinchan "Terminal Sekinchan (aeroplane)" (Selangor), "Mini Aircraft" (Kedah),
  "Coach MY airplane" (Negeri Sembilan).** OSM sweep hits; themed structures and sculpture,
  not airframes.
- **Monumen Pesawat at 0.53447 / 117.60463** appeared in the regional OSM sweep. That is in
  East Kalimantan, Indonesia — another agent's country.

---

## 7. Fields deliberately left blank

- `year_built` on all rows but one — see §4.
- `tail_number` on 11 rows: the Kuala Kangsar A-4PTM, the Taiping Sabre, the Muzium Negara
  Eagle 150B, the Tengah A-4SU, the ITE 737-301, the RMAF Museum's Rakan Musa RMX-4 and
  RotorWay Executive, the Igla, and the two Tebuans whose reported serials are contradicted or
  impossible. In each case the airframe is real and the identity is not published.
- `variant` on the Taiping Sabre: every RMAF Sabre was a CA-27 Mk.32, but that has not been
  confirmed for this specific airframe and no photograph of its markings was found. Inferring
  it would be a guess dressed as a fact.
- `website` on eight sites that have no institutional web page (monuments, gate guards, the
  Melaka navy museum, the RBAF Museum).
- `state_province` on all six Singapore rows, as instructed.
- `postal_code` on the Joint Force HQ Kuantan monument — the camp's postcode is not published.

## 8. Coordinates that are not surveyed positions

Everything else in the CSVs comes from an OSM node on the airframe itself, a Nominatim hit on
the named site, or a Wikipedia infobox.

- **Royal Malaysian Air Force Museum** — 2.6853 / 101.8440 is the Sri Sendayan Mosque, the
  anchor named in the Free Malaysia Today report. The collection is currently in the adjacent
  air base, which has no published coordinates.
- **Joint Force Headquarters Kuantan MiG-29N Monument** — 3.8930 / 103.1668 is the Sungai
  Panching locality centroid. The camp itself is not mapped by name in OSM or Nominatim.
- **Tengah Air Base** — 1.3743 / 103.7131 is the OSM node for the gate-guard Skyhawk itself,
  not the centre of the base.
- **ITE College Central** — 1.3790 / 103.8561 is the OSM `historic=aircraft` node; the campus
  centroid is about 120 m away.
- **National Heroes Square Putrajaya** — 2.9402 / 101.7057 from Nominatim for Dataran Pahlawan
  Negara, Presint 1. Note that the English Wikipedia article "National Heroes Square (Malaysia)"
  carries coordinates 41.9961 N / 21.4317 E, which is in North Macedonia — a Wikidata error.
  Do not use it.

---

## 9. Open questions, ranked

1. **What actually reached Sendayan, and in what condition?** The 37-row RMAF Museum file is a
   2010s inventory of a collection that has since been dismantled, trucked 60 km and left
   largely outdoors for five years. One visit or one email would resolve the whole file.
   *Muzium TUDM, RMAF Sendayan Air Base, Negeri Sembilan; the museum's historical contact was
   +603 2141 1133 ext 4129/4198 and fitri_muzium@yahoo.com (Sungai Besi era, may be dead).
   Current route in: Markas Tentera Udara public affairs via airforce.mil.my, or the RMAF
   Museum Facebook page, which is where the move was documented phase by phase.*
   This one contact would also settle questions 2, 3 and 8 below.
2. **The Port Dickson Tebuan's true identity.** A photograph of the data plate or a clear shot
   of the fin would settle whether the "M22-05" marking is the airframe's own or borrowed from
   the aircraft now at Embry-Riddle. *Muzium Tentera Darat, Kem Sri Rusa, Port Dickson;
   admin@armymuseumpd.gov.my, +606 640 9481/9482/9484/9488.* The same call would confirm the
   other four Port Dickson serials, none of which has a second source.
3. **The four airframes at RMAF Kuantan and the two at RMAF Kuching.** Six unidentified
   aircraft, all inside the wire, all mapped but none typed. Kuantan holds a public open day;
   Kuching's are on the airport perimeter and may be photographable from the Airport Perimeter
   Road near the Sarawak Meteorological Office.
4. **Is the MiG-29N M43-14 physically standing at Dataran Pahlawan Negara?** The handover was
   reported and the site inspection is dated 22 August 2023, but no dated photograph of the
   installed monument was found. *Perbadanan Putrajaya (Putrajaya Corporation), ppj.gov.my —
   they are the monument's client and would confirm in one call.*
5. **Did the RSAF Museum's T-33A 364, IAI Scout 513 and Searcher II 561 survive the refresh?**
   All three are in the aviationmuseum.eu list but none appears in the 2019/2024 airhistory.net
   photo sets. *hellofromsafm@defencecollectivesg.com.* The same email would confirm whether
   the Bloodhound missile that centred the old display hall is still present — it was excluded
   from the CSV for lack of any post-2010 evidence.
6. **The type of the helicopter at the Royal Brunei Armed Forces Museum.** Brunei has flown
   Bell 47/Sioux, Bell 206, Bell 212, Bell 214ST, Westland Wessex, MBB Bo105 (retired February
   2022) and now S-70i and H145M — any of which could be the exhibit, so no inference is safe.
   *RBAF Museum, Bolkiah Garrison, Jalan Pertahanan, BB3513 Bandar Seri Begawan, +673 715 5140.*
   Brunei is the thinnest country in this set by a wide margin: one site, no typed airframe.
7. **Gong Kedak: real airframes or an exhibit about aircraft?** See §6. *Pangkalan Udara Gong
   Kedak public affairs.*
8. **Whether any preserved Malaysian civil airliner exists.** MAS and AirAsia training
   airframes are the most likely candidates and nothing about them is published. *Malaysia
   Airlines Academy (Kelana Jaya) and Asian Aviation Centre of Excellence (Sepang).*
9. **What the Seri Kembangan node actually is.** Lowest-value item here; one street-level
   photograph decides whether it stays in the database at all.

## Post-research processing (import pass, 9 Sep 2026)

- Every row was validated against the real importer (`tests/test_flagship_topup_files.py`)
  and the alias-hygiene suite before import. Two mechanical corrections were applied across
  this file set: dashless search variants were added where missing (`MiG-21` → `MiG21`,
  `MiG-21PF` → `MiG21PF`), and attribute words that had been filed as aliases (`replica`)
  were moved into `description`, where the convention puts them.
- Duplicate aliases within a row were removed; the database de-duplicates them anyway, and
  leaving them in the CSV made the file and the live record disagree.
- Serials were diffed against all 3,542 tail-numbered aircraft already in the database before
  import: zero collisions. Museum names were diffed against all 424 existing sites: zero
  collisions, exact or normalised.
- Museums were imported first, then aircraft, and the result was verified per site against
  the live API — every site's aircraft count matches this directory exactly.
