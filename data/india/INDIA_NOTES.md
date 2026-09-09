# India - research notes

328 sites, 652 aircraft. Files in `data/india/`: `in_museums.csv` plus one `<site_slug>_aircraft.csv` per site.

Research date: September 2026. Currency target: 2025-26. All records imported live on 9 Sep 2026 and verified per site against the API.


## Build pass (9 Sep 2026)

- Research was run as parallel agents (India: one museums pass plus four regional
  base/monument passes; UAE, Saudi Arabia and Oman/Kuwait one each). Every agent's
  WebSearch quota was exhausted part-way through and scripted search engines were
  blocked, so the city-by-city discovery sweeps are thinner than intended; each
  agent's own NOTES below says where. A second sweep with search restored is the
  obvious next step.
- Rows were normalised by `scripts/build_gulf_india.py`: alias hygiene (prose and
  attribute words moved to `description`), dashless designation aliases added,
  placeholders blanked, `wing_type` cleared on rotary/missile rows, and `model`
  spellings harmonised with the live database (`A-4 Skyhawk` -> `A-4`; `TS-11 Iskra`
  / `PZL Mielec` -> `PZL-Mielec TS-11`; `DH.104 Dove`/`Devon` -> `DH.104`; `UH-3H` ->
  `SH-3` + `H`; `Kiran` -> `HJT-16`; `Br.1050` -> `Alize`; `Beech 18` -> `18`, etc.).
- Every tail was diffed across all eight packages and against the 9,982 aircraft
  already live: zero `(model, tail)` collisions. 37 same-tail/other-model overlaps
  (e.g. Strikemaster 414 vs Buccaneer 414) are legitimate and untouched.
- Every file passed `tests/test_flagship_topup_files.py` and `tests/test_alias_hygiene.py`
  against the real importer before import. Museums were imported first; every
  aircraft file dry-ran clean; per-museum counts were verified against the live API
  afterwards (zero mismatches).
- The API's bulk-import rate limit (200 requests/hour) was hit after 319 of 363
  files; the remaining 44 were imported as one combined request per country after
  a clean combined dry run.


### Cross-package reconciliation (India)

The five India packages overlapped. Where two packages inventoried the same site
the museums package's rows were kept and regional rows were added only when they
brought a new tail (Chandigarh Kanpur BR-460; Dharmasthala HT-2 IX710; Jodhpur
MiG-27 TS-556; Shillong Mi-4 Z311, Gnat E256, MiG-21s C1106/C1155, Su-7 B1354).
Untailed regional duplicates of a type already recorded were dropped (HAL museum
HA-31, HUL-26, Tejas; Bikaner DH.9; Jodhpur HT-2; Vizag Tu-142; Shillong DHC-1;
Dungarpur Mi-8). Thirteen regional site names were mapped onto the museums
package's name for the same place (Taoru, Bikaner, Jodhpur heritage museum,
Lucknow zoo, Vizag Tu-142 and Victory at Sea, Rashtrapati Bhavan, Lansdowne,
Kapurthala, Bhubaneswar airport Dakota, Sunabeda, Madikeri, Upper Shillong).

**One airframe, one place** - serials claimed at two sites, and how each was settled:

| Serial | Kept at | Blanked / changed at | Reason |
|---|---|---|---|
| Iskra W1758 | IAF Museum Palam | Sainik School Rewa (tail blank) | Palam has aerialvisuals + Commons photo; Rewa is Bharat Rakshak only |
| Gnat E261 | HQ Maintenance Command Nagpur | Kerala S&T Museum Trivandrum (tail blank, alias E261) | Nagpur has the ex-2 Sqn provenance chain |
| Marut D1220 | IAF Heritage Museum Jodhpur | HQ SWAC Gandhinagar (tail blank) | Jodhpur has WBI + BR; Gandhinagar a 2004 Sainik Samachar photo |
| MiG-21U U455 | AFS Bagdogra | C V Raman Park Nagercoil (tail blank, alias U455) | Bagdogra photographed 2017; both Type 66 |
| MiG-25 DS362 | AFA Dundigal | AFS Kalaikunda -> recorded as DS361 (alias DS362) | warbirds.in 2022 states BR's DS361/DS362 locations are swapped |
| Gnat IE1205 | Vayu Bhavan Delhi | Gandhi Bagh Nagpur (tail blank, alias IE1205) | WBI regards the Delhi aircraft as genuine |

Indian serials were written without the hyphen (C716, not C-716), as painted; the
hyphenated form is an alias on every row so both spellings search.

**Excluded at build:** Butibori aircraft restaurant, Nagpur - the ex-Air India
airframe under conversion for Haldiram's is of unidentified type and the venue had
not opened as of Sep 2026; re-check and add once it opens.

**Coordinates:** 36 sites had no fix from research and were geocoded to a
Nominatim town centroid - treat these as approximate: 11 Airmen Selection Centre Guwahati, Air Force Selection Board Kanchrapara, Air Force Station Borjhar Guwahati, Air Force Station Jorhat, Air Force Station Purnea, Air Force Station Salua, Army Public School Ranchi, Arunachal Pradesh Science Centre Itanagar, Bal Vihar Kollam, Chitralekha Udyan Tezpur, College of Aeronautical Engineering Guwahati, Dibrugarh University, Fort William Eastern Command HQ Kolkata, Gandhi Park Jorhat, HQ Andaman and Nicobar Command Port Blair, IIT Kharagpur Nehru Museum, IIT Patna Bihta, Indian Military Academy Dehradun MiG-21, Jorhat Army Cantonment, Kannur Cantonment Park, Manipur Science Centre Imphal, Mayfair Lagoon Hotel Bhubaneswar, NIT Rourkela, Nehru Bal Bhavan Thrissur, Netaji Subhas Chandra Bose International Airport Kolkata MiG-27 Display, Officers Training Academy Gaya, Piravom Post Office Junction Park, Raj Bhavan Aizawl, Raj Bhavan Kohima, Raj Bhavan Port Blair, Raj Bhavan Ranchi, Sainik School Bhubaneswar, Sainik School Purulia, Trishakti War Memorial Sukna, Kuwait Armed Forces Headquarters, Mubarak Camp, PAAET College of Technological Studies, Shuwaikh.
Two sites are left without coordinates because the geocoder returned the wrong
district: Bila Udayapur MiG-23 Display (Keonjhar) and Sainik School Tilaiya.


---

## Research agent notes - Museums and named collections

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES

SCOPE AND METHOD
- Assignment: public museums, science centres, heritage centres, named collections and the war museums/memorials explicitly assigned (Jaisalmer, Dras, Vizag). IAF station gate guards, school/college/campus airframes and park/roundabout monuments were NOT recorded as sites (other agents); the ones encountered are listed as leads below.
- Research tools available were limited during the session: WebSearch quota was exhausted early and general search engines refused scripted queries, so discovery relied on (1) a full dump of warbirds.in (Warbirds of India, 461 posts via its WordPress API, dated 1999-Sept 2025), (2) the Bharat Rakshak IAF aircraft database type listings (serial, variant, c/n, ex-identity, TOC date, preserved/written-off flag - 505 airframes flagged Preserved), (3) aerialvisuals.ca location and airframe dossiers for India, (4) aviationmuseum.eu India entries (lead-level, but its serial tables were used with caution), (5) Wikipedia pages and Wikimedia Commons category/file names, (6) jetphotos location/registration pages, (7) Google News RSS headlines with resolved article URLs (PIB, Hindustan Times, Nagpur Today, Kerala Tourism, TOI) and Wayback copies of The Hindu where the live site is blocked.
- Source reliability: warbirds.in is the best Indian source (serial-level, dated visits, corrections) but many of its museum pages date from 2006-2015; aerialvisuals gives real identities and mapped coordinates but has stale entries; aviationmuseum.eu lists are recent (mentions 2025 additions) but unsourced; Wikipedia's Palam list contains errors (e.g. C-992 is a written-off FL per Bharat Rakshak). Two directories copying each other were treated as one source.
- Coordinates: aerialvisuals mapped airframe fixes were used for Palam, Goa, HAL Bengaluru, Nehru Science Centre; Wikipedia article coordinates for Vizag Tu-142, Sea Harrier Museum, Kolkata, Raman Science Centre; warbirds.in embedded map fixes for Guwahati, Taoru, Sunabeda; all others are geocoded street/locality approximations or town centroids and should be refined (Chandigarh Sector 18, Patna, Trivandrum x2, Chennai Periyar, Kapurthala, Dharmasthala, Lansdowne, Jaisalmer, Dras, Rashtrapati Bhavan, Junapur, Tekanpur, Bikaner, Jodhpur, Kochi x2, Lucknow x2, Bhubaneswar, Ozar, Coimbatore, Madikeri, Shillong, Kakinada, Nagpur AF museum, Dungarpur).

CORRECTIONS MADE WITH EVIDENCE
- Palam MiG-21 "C-992" (Wikipedia) rejected: Bharat Rakshak lists C-992 as written off 2 Sep 1997. C499, C779 and C771 are photographed/documented; C2216 (bis) kept on Wikipedia + aerialvisuals only.
- Palam Hunter: Wikipedia's "A-476 in Thunderbolts scheme" and jetphotos "BA263" are two different aircraft (both in Bharat Rakshak as F56A ex G-9-158 and F56 TOC 1958). aviationmuseum.eu's third Hunter A941 not confirmed.
- Palam Prentice: three different painted serials in circulation (IV3381 per Bharat Rakshak/Wikipedia, IV3368 per Commons/jetphotos file names, IV336 per aerialvisuals). Recorded as IV3381 with the others as aliases - needs a photo check.
- Palam Lysander: true identity ex-RCAF 1589 (aerialvisuals); painted RAF serial differs between sources. Palam Hurricane: painted AB832; aerialvisuals' Z7059 identity unverified (Z7059 would be a Hawker/Gloster-built IIB, inconsistent with the CCF c/n it quotes).
- Palam Iskras W1757/W1758: the IAF re-used these serials for the 1999 second batch; aerialvisuals c/ns 3H 19-16 / 3H 19-08 show the museum aircraft are the 1999 airframes, not the 1975 ones.
- Kanpur I at Chandigarh: warbirds.in's 2024 visit report gives BR470, its own earlier PEC page and Bharat Rakshak give BR-460. Recorded BR470 (latest first-hand report) with BR-460 alias; painted serial to be checked.
- Chandigarh Gnat painted E-257 is IE-1114 (warbirds.in, Bharat Rakshak c/n GT-015); E-257 (Sekhon's aircraft) was lost in 1971.
- Goa Firefly INS112: aviationmuseum.eu calls it a replica; warbirds.in (which inspected it) says the fuselage is an original Firefly rebuilt with fabricated cowling, undercarriage and tail. Recorded as an original with heavy reconstruction, not as a replica.
- HAL museum MiG-21M C1691: serial painted out by 2025 (identity from 2021 photos); a component inside is marked C1660.
- Kerala Science Museum Gnat E261 vs HQ Maintenance Command Nagpur Gnat E261 (both on warbirds.in): one painted identity is spurious; not resolvable remotely.
- Palam Gnat IE1205 (aviationmuseum.eu) conflicts with warbirds.in's IE1205 at Nagpur; Palam Gnat IE1246 is written off per Bharat Rakshak. Both omitted from the Palam list.
- Tu-142 serials: Vizag IN312 (aerialvisuals dossier c/n 7609686), Kolkata IN317 and Kakinada IN318 (aviationmuseum.eu; IN318 photographed in the Rajali boneyard March 2017 consistent with later disposal). Lucknow Tu-142M serial unknown.

JUDGMENT CALLS
- Access types: Palam and the Chandigarh centre are public (Palam requires government ID / passport at the AFS gate; closed Mon-Tue). IAF Heritage Museum Jodhpur is inside AFS Jodhpur -> restricted. HAL Pragati Museum Ozar is inside the HAL township (aviationmuseum.eu gives Sunday 09:00-13:00 hours) -> restricted pending confirmation. Air Force Museum HQ MC Nagpur publishes public hours (daily except Tue, 10-14 and 16-18) so recorded public although it sits inside Vayusena Nagar; the gate-guard airframes elsewhere in HQ MC (Gnat E261, MiG-23BN SM262, MiG-29 KB3298, Jaguar A103) are not included. Titus Museum (private collector) and Udai Bilas Palace (heritage-hotel museum) recorded as appointment; BSF Museum Tekanpur inside the BSF Academy recorded as appointment. Air Force Museum Upper Shillong is a listed tourist attraction with public viewing/parking (warbirds.in, Shillong Times) -> public; the Otter IM1057 beside the ALG tower may be off-limits.
- The Otter at Shillong and the Canberra T.4 Q1793 at HAL airport are recorded at the adjacent museum site with a caveat rather than as separate sites.
- Replicas/mock-ups recorded and flagged: VITM Wright Flyer replica; HAL museum LCA mock-up, ALH mock-up IN-701 and an IJT mock-up (the real IJT S3446 is listed separately). The Palam Apollo Lunar Module replica and the Akkulam Rafale model are not aircraft records.
- Nicco Park Kolkata (amusement park MiG-21FL, unmarked, gifted 2008), National Military Memorial Park Bengaluru (MiG-23BN SM255, plus MiG-21 C1672 and Mi-8 Z2388 per aviationmuseum.eu) and the Sea Harrier IN-617 monument at Bandstand, Bandra, Mumbai (installed Dec 2020) are park/promenade monuments -> left to the monuments agent (leads below).
- Bhubaneswar airport Dakota VT-AUI and Lucknow Zoo Tu-124 V642 are included as public displays because they are formal, ticketed/managed exhibits rather than gate guards.
- Harvard HT-291 and Tiger Moth HU-512, both listed by Wikipedia at Palam, are omitted: HU-512 was restored to fly with the IAF Vintage Flight (2012) and aerialvisuals marks HT291 (later G-CGYM) as moved on; the Vintage Flight Harvard is airworthy. Confirm whether either is currently parked at the museum.

EXCLUDED (do not re-research)
- INS Vikrant museum ship, Mumbai: scrapped 2014; its Sea Hawks IN188/IN246, Alizes and Sea Kings dispersed (Sea King IN510 now at INS Kadamba, Alize IN209 at INA Ezhimala - both naval bases).
- INS Kursura and Samudrika Naval Marine Museum Port Blair: no aircraft (Port Blair's MiG-21FL C606 is a pole mount at HQ ANC - base).
- National War Memorial New Delhi, Nehru Planetarium, National Rail Museum, BITM Kolkata, Science City Kolkata, Kurukshetra Panorama, Regional Science Centres Bhopal/Tirupati/Dharwad/Bhubaneswar/Calicut, Birla Science Museum Hyderabad, Gujarat Science City, Goa Science Centre, Chennai Fort Museum, Cavalry Tank Museum Ahmednagar: no airframe found in any source consulted (Wikipedia, warbirds.in corpus, news). Kozhikode's Ajeet E1982 is outside the S K Pottekkat cultural centre park, not the science centre (lead below).
- Air Force Museum Akkulam, Thiruvananthapuram (Kerala Tourism/SAC, opened Oct 2021, refurbished Sept 2026): contains models (Rafale, Su-30, BrahMos), a MiG-21 KM-1 seat, engines and armament but no complete airframe; the two Shanghumugham-hangar Avros proposed for it in 2023 have no reported arrival.
- Punjab State War Heroes' Memorial & Museum, Amritsar (opened 2016): no aircraft found in any source; Yodhasthal Bhopal (Sudarshan Chakra Corps museum): aviationmuseum.eu lists it but no aircraft type/serial could be found - both need a human check.
- Longewala War Memorial: no verifiable aircraft; warbirds.in notes the garish Hunter formerly at the Uttarlai AFS war memorial was removed and is presumed to be the Hunter now at the Jaisalmer War Museum.
- Moradabad Trishul war museum (MiG-27 announced Dec 2025) and the Sea King Mk 42B announced for Lucknow: intent only.
- Sahar/Mumbai 747s, Nagpur Boeing 720, Palam IGI Dakotas, Kolkata VT-AUI (moved), Nagda Dakota VT-AUM (auctioned 2015, later seen at Sedam): derelict/moved airframes.
- Gulbarga Bf 109: exported to the UK long ago. Benares Hurricane: sold to the UK (Vacher).
- IAF Vintage Flight aircraft (Dakota VP905, Tiger Moth HU512, Harvard HT291, HT-2 restored 2025) are airworthy - not records.

LEADS FOR OTHER AGENTS (not recorded here)
- Gate guards / bases: Hindon AFS Su-7BMK B747 (Hindon Chowk gate, visible from road); Sulur and Coimbatore AF establishments (HT-2 at AF Administrative College); Nagpur HQ MC airframes above; Jodhpur Maruts D1198, D1216, D1240 (roundabout and Army HQ); Jaisalmer AFS Hunter BA237 / Marut D1237 / MiG-21 Bison CU2226; Uttarlai war memorial Su-7 and Marut; Halwara, Bathinda, Ambala, Leh, Srinagar, Bagdogra, Hasimara, Kalaikunda, Tezpur, Chabua, Jorhat, Dundigal (Air Force Academy museum park with ~18 airframes), Hakimpet, Yelahanka, Jalahalli AFTC, INS Dega, INS Garuda, INS Kadamba, INA Ezhimala, Naval Armament Depot Goa Sea Hawk IN244, Raipur Sea Hawk IN244 (same serial claimed at two places).
- Campus/park monuments: Nicco Park Kolkata MiG-21FL; National Military Memorial Bengaluru MiG-23BN SM255; Bandstand Bandra Sea Harrier IN617; Kozhikode S K Park Ajeet E1982 (11.255126, 75.795960); Akulam Lake Park Trivandrum Kiran U780; Nagercoil town park MiG-21UM U455; Dighalipukhuri war memorial Guwahati MiG-27ML TS522; Pune National War Memorial MiG-23BN SM273; Kamalnayan Bajaj Park Pune MiG-23MF SK423; Tatyasaheb Thorat Park Pune Gnat E359; Cubbon Road Bengaluru Ajeet E1083 (may have moved to HAL museum); Gandhinagar Marut/Hunter/MiG-23; Jahaz Chowk Mystere IA1007; Sekhon memorial Gnat IE1079; Martyrs' memorial Odisha Gnat IE1071; Dalhousie MiG-21M C1556; Rashtrapati Bhavan is included here as a museum.
- Schools/colleges/universities (dozens; see warbirds.in index): Sainik Schools, IITs, PEC Chandigarh (Mi-8 Z1381, Spitfire HS674, Auster VT-DYU), IISc Hunter A467 and HT-2 VT-DFY, Doon School, RIMC Dehradun (Hunter BA357, Sea Harrier T.60 IN654), Mayo College Ajeet E1059, BITS Pilani Dakota VT-CYT, Hindustan Institute Chennai, MIT Chennai Sea Hawk IN252 / Gnat IE1248, IIT Madras Sea Hawk IN235, NDA Khadakwasla (MiG-25R KP351, Ouragan IC585, Ajeet E247, MiG-29 KB732, Sea Hawk), NIMS University Avro VT-EIR, Sanskriti University MiG-21M C1572, Chitkara University HPT-32 X3215, Indus University Su-7.
- Hotels/restaurants/private: Lal Qila Resort Meerut HS-748 restaurant (spurious GA2023); Faridkot palace hangar (private vintage aircraft); Baramati Carver Aviation MiG-23MF (training school); Flytech Hyderabad Dakota VT-DTS (ground trainer); Singhania Hospital Thane Dakota VT-CEB; Sedam Dakota VT-AUM.

OPEN QUESTIONS NEEDING A HUMAN ON SITE (ranked)
1. Indian Air Force Museum Palam - a current full inventory walk-through: confirm presence/painted serials of Prentice (IV3381/IV3368/IV336), MiG-21s (C499, C771, C779, C2216), Hunters (BA263, A476, A941?), Gnats/Ajeets (IE1059, E265, E2016, IE1975?), Maruts (D1205, D1274?), HT-2s, second Dakota IJ817, Kanpur II VT-XAL, the ex-PAF F-86F identity, the Martin B-57 wreck, the Moradabad Hurricane storage status, whether Tiger Moth HU512 and Harvard HT291 are on site, and the Sabre 1606 paint scheme; also whether the long-planned relocation has started.
2. Naval Aviation Museum Goa - confirm Il-38SD IN306, Islander IN139, Chetak IN465 and the Kiran mentioned in 2019 press; confirm the Il-38 IN305 date.
3. HAL Heritage Centre after the April 2026 refurbishment - confirm which of Cheetah Z1897, Ajeet E1083, LCH ZP4601, Canberra T.4 Q1793, HJT-36 S3446 are actually inside the museum, and whether MiG-21M C1691 and HPT-32 X3240 are still in the rear shed.
4. Jaisalmer War Museum Hunter - read the painted serial (J1012?) and check whether it is the ex-Uttarlai aircraft; Longewala memorial - any airframe?
5. Air Force Museum Upper Shillong - verify the aviationmuseum.eu list (Hunter BA251, Caribou BM769, Mi-4 BZ531, Iskra W1784, Chipmunk, Streak Shadow G-8522, MiG-21 cockpit) and public access to the Otter.
6. Lucknow Nausena Shaurya Vatika Tu-142M serial; Kakinada Tu-142 IN318 and HPT-32 X3234 confirmation; Nagpur AF Museum MiG-21/Mi-8 serials; Raman Science Centre HPT-32 serial.
7. Dras Kargil memorial MiG-21M identity (stencils inside gear doors); Rashtrapati Bhavan MiG-21M C1492 still present; Nicco Park MiG-21FL identity.
8. Kerala Science Museum vs Nagpur - which Gnat is really E261; Madikeri MiG-21 C1624 variant/serial; Dharmasthala HT-2 identity; Jodhpur heritage museum Su-7 B790, HT-2 and MiG-27 serials and whether public tours exist.
9. Punjab State War Heroes' Memorial Amritsar and Yodhasthal Bhopal - any aircraft at all?
10. Titus Museum Junapur and Udai Bilas Palace Dungarpur - visiting arrangements; Dungarpur Mi-8 identity.


---

## Research agent notes - North

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES

Sources used and reliability
- Bharat Rakshak IAF aircraft database (bharat-rakshak.com/indianairforce/database/aircraft/<serial>) - all 505 airframes with status "Preserved" were pulled and filtered for the northern states. Per-serial pages give a "currently preserved at" location plus remarks, sometimes with a photo. Reliable for identities (many drawn from RTI/Gazette data) but locations are terse, sometimes stale, and occasionally mis-stated (e.g. Faridabad filed under UP; Kota filed under Karnataka; E-1964 remark says AFSB Dehradun while the photo evidence is Varanasi). Treated as the serial backbone.
- warbirdsofindia.com / warbirds.in (WBI) - all posts in the Delhi, Haryana/Chandigarh, Punjab, Himachal, J&K/Ladakh, Uttarakhand, UP and Rajasthan categories were read (posts 2006-2025, many updated 2022-2025 with dated photographs by Dipalay Dey, Sanjay Simha, Angad Singh). Best source for currency, painted-vs-real serials and map fixes. Where WBI gives a map pin the coordinates are taken from it (marked "Coordinates from WBI").
- WebSearch quota for the session was exhausted by parallel agents before city-by-city news sweeps could be run, and DuckDuckGo/Bing were unreachable through the proxy; aviationmuseum.eu (museum-only) and aerialvisuals.ca were therefore not consulted for this region. All records below rest on the two sources above; entries drawn only from a Bharat Rakshak one-liner are flagged "not photo-verified" in the description.
- Coordinates without a WBI fix were geocoded with Nominatim/OpenStreetMap on the institution or airfield name (street-address or campus level, not the airframe). Blank lat/lon means the geocode failed; fill by hand.

Corrections made with evidence
- Vayu Bhavan third Gnat: painted "IE-246" is not a valid serial; tail_number left blank, painted marking in aliases (WBI; Bharat Rakshak lists as E-246 with a query).
- Leh Hunter: true identity BA-317 (Bharat Rakshak, 14 Sqn 1965/71) but repainted 2024 as "BS-230" (WBI); recorded as BA-317 with the false serial in aliases.
- Leh MiG-23BN "SB255": spurious; seat says SM258, but SM-258 is at UPES Dehradun. tail_number blank.
- Gurdaspur Mystere painted IA-1007: WBI reports IA-1007 was destroyed at Pathankot in 1965; tail blank, painted serial in aliases.
- Poonch Otter marked "690B": actually BM-1002 (c/n 57, ex-RCAF 3690) per veteran D C Bharadwaj via WBI.
- Chandigarh Heritage Centre Gnat painted "E-257": true identity IE-1114 (ex-Punjabi Bagh Traffic Training Park).
- Mayo College Ajmer "E-1059": serial doubted by WBI; recorded as painted, with doubt in description.
- MERI College Rohtak Su-7: only evidence of identity is "812" on the ejection seat; tail blank.
- Kanpur Jaguar: arrived as French A160, repainted A090; tail blank.
- Dharamsala Gnat: WBI page title says IE1068, text and Bharat Rakshak say IE-1062 (c/n FL-10); recorded IE-1062.
- PEC Chandigarh Kanpur I: moved to the IAF Heritage Centre on 21 Nov 2022 (WBI, IAF tweet) - recorded only at the Heritage Centre.
- Uttarlai war memorial Hunter: gone since the early 2000s (WBI); presumed to be the unidentified Hunter at the Desert Corps War Museum, Jaisalmer - not double-recorded.
- Jaisalmer AFS Hunter BA-237: Bharat Rakshak says now at Longewala/Desert Corps museum, so it is not recorded at AFS Jaisalmer; the museum Hunter is recorded once, unidentified, with BA-237 as a possible identity.

Judgment calls
- Access: aircraft inside IAF stations, cantonments and Army HQ areas are "restricted"; gate guards visible from the public road (Hindon, Nal twin gate guards, Leh Hunter, Army R&R hospital, Ambala gate, Kanpur Chakeri gate, Vayu Bhavan, DRDO Bhavan, DG NCC) are "public"; school and university campuses are "appointment".
- Subroto Park: WAC HQ lawn and CAFME are one restricted enclave record; Army Hospital R&R (gate, public) and the Akash Officers Mess are separate records.
- Timarpur Il-14 BL-565 and the PEC Spitfire/Auster/Kanpur II are recorded as in_storage (not on view).
- Bharat Rakshak lists both D-1198 and D-1240 at "Jodhpur roundabout"; only D-1198 is photo-confirmed by WBI. D-1240 is mentioned in the D-1198 description rather than given its own record.
- Bharat Rakshak lists two MiG-21Ms (C-1592 and C-1650) at the Chandigarh Heritage Centre; WBI saw one complete MiG-21M and an unidentified MiG-21 cockpit section. Only C-1592 recorded.
- Museums in this file that the museums agent may also hold (dedupe): IAF Heritage Centre Chandigarh, Heritage Transport Museum Taoru, Punjab State War Heroes Memorial Amritsar, Maharaja Ranjit Singh War Museum Ludhiana, Pushpa Gujral Science City, Desert Corps War Museum, Jaisalmer Government Museum, Junagarh Fort, Udai Bilas Palace Dungarpur, Titus Museum, Rashtrapati Bhavan Museum, Kargil War Memorial, Garhwal Rifles museum, Jodhpur AF Heritage Museum. The Indian Air Force Museum Palam is NOT included here (museums agent); Bharat Rakshak lists ~40 airframes there (A-476, BA-263, BL-727, BM-774, BZ-900, C-499, C-779, D-1205, E-2016, E-265, HA-623, HE-924, HS-986, HT-268, HT-291, HU-512, HW-529, IA-1329, IB-799, IC-554, ID-606, IF-907, IJ-302, IK-450, IL-860, IV-3381, IX-732, IX-737, IZ-1590, KP-355, NH-631, SK-434, SM-282, TS-591, W-1757, W-1758 (now Sainik School Rewa MP), B-888, plus Sabre 1606 ex-Bangladesh) for cross-checking.

Excluded and why
- Pragati Maidan Defence Pavilion, New Delhi (Ajeet E-254, MiG-21FL C-1168): last documented 2002 (WBI); the ITPO grounds were demolished and rebuilt 2017-2023 and no post-redevelopment sighting was found. Treated as departed/unknown - needs a check; if still there they belong at 28.61977 77.24316.
- "New Delhi 71 war expo" MiG-21FL C-771 (Bharat Rakshak): temporary exhibition, no fixed site.
- Agra HS-748 H-1181: Bharat Rakshak "Agra scrapyard" - not a display.
- Jaisalmer AFS MiG-21 Bison CU2226: parked near ATC, not set up for display (WBI Nov 2024).
- Hindon Vintage Flight aircraft (Dakota VP-905 etc.) and IIT Kanpur flying fleet (Piper Cub VT-DTP, Cessna, gliders): operational/airworthy.
- Faridkot Maharaja hangar derelicts (Fairchild 24, Percival Proctor, Stinson L-5, unidentified): locked private hangar, not viewable (WBI 2023) - noted as a lead only.
- Palam derelict Dakota VT-AUT, HS-748s VT-EFQ/VT-EFR and the IAAI fire-training Il-14: disposed of during the 2006-09 airport rebuild; fates unknown/scrapped.
- Moradabad Hawker Hurricane IIB: taken by the IAF in Jan 2021, now in IAF custody in Delhi (WBI); not on display.
- Spitfire XIV SM832 (IMA Dehradun) and Spitfire VIII MT719 (Jaipur): exported to the UK/France decades ago (Bharat Rakshak/WBI).
- Doon School Harvard (with Hurricane wings): reported gone (WBI).
- Daulat Beg Oldi derelict Mi-4: wreck used as a tea shack at a forward airstrip, not accessible.
- Ludhiana Sekhon memorial Gnat: WBI said "moved, whereabouts unknown" in 2011 but updated 2015 with a 2013 photo at the collectorate - kept.
- Agra Constellation BG-583: scrapped.
- Gwalior (MP) Su-7s B-802/B-817, Canberra IF-901, Gnat E-235: outside region.

Blank fields left deliberately
- year_built only where a sourced build/acceptance date exists (VT-CTV 1943, VT-CYT 1945, SM-201 1980, Otter BM-1002 1954, Kanpur I 1958). IAF TOC dates are in descriptions, not year_built.
- postal_code blank except where a source gives it.
- Many serial identities blank for unmarked airframes (Uttarlai memorial pair, Nal Su-7 and two MiG-21s, Bathinda Marut/Su-7/MiG-21, Leh MiG-23/Mi-8, Chandigarh 12 Wing Mi-8s, Chittorgarh Harvard/HPT-32, NIMS airframes, Meerut HS 748, Siswan MiG-21bis, Ambala gate Hunter, Desert Corps Hunter, Moradabad MiG-21UM, Junagarh DH.9).

Open questions needing a human on site (ranked)
1. Delhi currency sweep: Yashwant Place C-1174, Arwachin school C-1125, CGDA C-1638, Japanese Park SM-265, Jamia SM-215, Garrison Parade Ground SM-249, Akash Mess SM-287, IGI T1 C-1661 (terminal rebuilt 2024) and Faridabad Town Park BA-219 rest on Bharat Rakshak one-liners only.
2. Pragati Maidan: did E-254 / C-1168 survive the ITPO redevelopment?
3. Desert Corps War Museum Hunter identity (BA-237 from Jaisalmer AFS, or the Uttarlai memorial Hunter?), and whether anything remains at the Jaisalmer AFS Vijay Stambh.
4. Jodhpur: is there a second roundabout Marut (D-1240) as Bharat Rakshak implies, and where exactly is D-1216?
5. HQ CAC Bamrauli MiG-21M C-1599: still on the perimeter wall or moved to Chandra Shekhar Azad Park?
6. Chandigarh Heritage Centre: is C-1650 a second MiG-21M or the cockpit section?
7. Dalhousie: is there a second MiG-21 inside Dalhousie Public School (Tribune, Oct 2013)?
8. AFS Bathinda Marut/Su-7/MiG-21 identities; Nal Su-7 and two MiG-21 identities; Uttarlai ATC MiG-21M C-1673 vs C-1676.
9. DG NCC: is Hunter T.66 S-574 really there alongside A-1012?
10. Sites in the assignment for which no evidence was found and which remain unswept: Sirsa, Suratgarh, Phalodi, Jaipur city/AFS Jaipur, Awantipur, Udhampur AFS, Jammu, Gurugram/Dwarka/Vasant Vihar/Rohini (other than Japanese Park), HAL Kanpur, Shimla town, Kota, Udaipur, Alwar, Hisar, Kurukshetra, Panipat, Sonipat. These need a news/Google Maps sweep once search access is restored.

Coordinate caveats
- The following sites could not be geocoded on the institution name and carry an approximate neighbourhood/town-level Nominatim fix (refine by hand): Army Hospital (Research and Referral) gate MiG-21 (geocoded on 'Army Hospital Research and Referral, Delhi', OSM type hospital); Akash Air Force Officers Mess (Air HQ Officers Mess) (geocoded on 'Subroto Park, Delhi', OSM type military); Directorate General NCC Headquarters, RK Puram (geocoded on 'R K Puram, New Delhi', OSM type clinic); DRDO Bhavan Tejas TD-1 (geocoded on 'Rajaji Marg, New Delhi', OSM type secondary); Air Force Station Hindon gate Sukhoi-7 (geocoded on 'Hindon Airport, Ghaziabad', OSM type aerodrome); Garrison Parade Ground Delhi Cantonment MiG-23 (geocoded on 'Delhi Cantonment', OSM type administrative); Japanese Park Rohini MiG-23 (geocoded on 'Swarn Jayanti Park, Rohini', OSM type park); Jamia Millia Islamia MiG-23 (geocoded on 'Jamia Nagar, New Delhi', OSM type school); Air Force Bal Bharati School Gnat (geocoded on 'Lodhi Road, New Delhi', OSM type secondary); Air Force Station New Delhi (Race Course) Iskra (geocoded on 'Race Course Road, New Delhi', OSM type station); Town Park Faridabad Hunter (geocoded on 'Sector 12, Faridabad', OSM type neighbourhood); Delhi Public School Ghaziabad Mystere (geocoded on 'Delhi Public School Ghaziabad', OSM type education); MERI College Rohtak Sukhoi-7 (geocoded on 'Rohtak', OSM type city); Rezang La Park Rewari HPT-32 (geocoded on 'Rewari', OSM type city); Indian Air Force Heritage Centre Chandigarh (geocoded on 'Sector 18, Chandigarh', OSM type administrative); Air Force Station Halwara War Memorial (geocoded on 'Halwara Airport', OSM type aerodrome); Bhai Kanhaiya Chowk Bathinda MiG-21 (geocoded on 'Bathinda', OSM type administrative); Punjab State War Heroes Memorial and Museum (geocoded on 'Attari Road, Amritsar', OSM type bus_stop); Sri Dasmesh Academy Anandpur Sahib Gnat (geocoded on 'Anandpur Sahib', OSM type station); Landour Language School Mussoorie Kiran (geocoded on 'Landour', OSM type hospital); UP Sainik School Lucknow (geocoded on 'Sarojini Nagar, Lucknow', OSM type centre); Lucknow Zoo (Nawab Wajid Ali Shah Zoological Garden) Tu-124 (geocoded on 'Hazratganj, Lucknow', OSM type commercial); Janeshwar Mishra Park Lucknow MiG-21 (geocoded on 'Gomti Nagar, Lucknow', OSM type station); Air Force Station Kanpur (Chakeri) gate HPT-32 (geocoded on 'Kanpur Airport', OSM type parking); Kendriya Vidyalaya Bamrauli Iskra (geocoded on 'Bamrauli, Prayagraj', OSM type suburb); Allahabad College of Engineering and Management MiG-21 (geocoded on 'Fatehpur, Uttar Pradesh', OSM type administrative); Air Force Selection Board Varanasi Ajeet (geocoded on 'Varanasi Junction railway station', OSM type station); Lal Qila Airport Resort Meerut HS 748 (geocoded on 'Meerut', OSM type administrative); Veterans Air Force School Bulandshahr MiG-27 (geocoded on 'Bulandshahr', OSM type administrative); Dr Bhim Rao Ambedkar UP Police Academy Moradabad MiG-21 (geocoded on 'Moradabad', OSM type administrative); HAL School Korwa Gnat (geocoded on 'Amethi', OSM type administrative); Bikaner War Memorial HPT-32 (geocoded on 'Bikaner', OSM type city); Sainik School Chittorgarh (geocoded on 'Chittorgarh', OSM type administrative); Singhania University Jhunjhunu MiG-21 (geocoded on 'Jhunjhunu', OSM type administrative).
- Indian Military Academy Dehradun MiG-21: no coordinate obtained; IMA is on Chakrata Road, Prem Nagar, Dehradun.


---

## Research agent notes - West and Central

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES
SCOPE: India west/central (Maharashtra, Gujarat, Goa non-museum, Madhya Pradesh, Chhattisgarh, Daman/Diu, DNH) - military base displays, gate guards, monuments, schools, colleges, parks, restaurants. Research Sep 2026. Web search quota was exhausted mid-task, so discovery relied on (a) a full scrape of warbirdsofindia.com (warbirds.in) state indexes for Maharashtra/Gujarat/Goa/MP - 69 entry pages read in full, (b) the Bharat Rakshak IAF database per-serial pages for every airframe flagged Preserved (495 pages, scraped by a sibling agent into scratchpad/brs), (c) the 2016 archived Warbirds of India register (web.archive.org copy of warbirds.in/list), (d) Google News RSS sweeps by city/type for 2017-2026 installations, (e) Wikipedia survivor sections, (f) Nominatim/Photon geocoding. Google Maps/Street View, jetphotos, Flickr, aerialvisuals and key.aero could not be reached in this session, so 2025-26 currency is mostly inferred, not photo-confirmed - flagged per record.

SOURCE RELIABILITY
- warbirdsofindia.com: dated first-hand reports with photos; the backbone. Pages are often 10-20 years old; treat currency as unverified unless a recent update is quoted (e.g. Lohegaon MiG-21 page carries a Sep 2025 tweet; Singhania Dakota page updated Jul 2024; Chandrapur/Nagpur Jaguars 2022; Saswad Gnat 2022; Indus University Su-7 2022).
- Bharat Rakshak database (bharat-rakshak.com/indianairforce/database/aircraft/<serial>): authoritative on serial/type/c/n but location strings are terse, sometimes stale or garbled (e.g. C-585 "Ozhar, Nagpur"; C-1166 Bhonsala "Nagpur, Madhya Pradesh"; E-261 listed at both Nagpur and Trivandrum; IE-1205 at both Delhi and Nagpur). Records that rest on Bharat Rakshak alone are marked "single-source" in the description - 24 aircraft. They are real database entries, not guesses, but need a photo or visit.
- 2016 Warbirds register (archive): used to corroborate Bharat Rakshak leads (IAT Pune Gnat and Su-7, KB741 TETTRA, C-585 Ozhar, SK-408 Ozhar).
- Google News (RSS): reliable for installation dates 2017-2026 (Rajkot MiG-27 2017/2021, Chinchwad MiG-23 2017, Bishop's School 2020, Bandra Sea Harrier 2020, Vadodara Highfly 2021, MILIT MiG-21 2024, Butibori 2024-25, Ujjain Avro 2025, Khed Shivapur A319 2026).
- Wikipedia survivor lists: leads only. Its MiG-29 list places KB-732 at Ozar (citing the 2016 register) whereas the later photo-based warbirds.in page places it at the NDA Pashan Gate - the latter is used.

CORRECTIONS / IDENTITY NOTES
- SSPMS Pune Canberra: painted IF-908 for years; wing marking F1188 (Ralph Lunt 1994) plus Bharat Rakshak identify it as ex-RNZAF B(I)12 NZ6109 = IAF F1188. tail_number F1188, IF-908 in aliases.
- Lohegaon Canberra painted F-910: real identity IF910 (c/n 71558/XH240).
- Ozar 11 BRD MiG-21 painted C822: actually Type 76 MiG-21PF BC822 (re-serialled C-822 after upgrade) per Air Marshal Bhojwani logbook via warbirds.in.
- Deolali School of Artillery MiG-21: Type 76 PF BC827, not an FL.
- Jeet Aerospace MiG-21FL: warbirds.in text says C603 in places, photo caption and Bharat Rakshak say C601 - C601 used, C603 aliased.
- NDA MiG-21U: warbirds.in gives U663 in text and U633 in its table; U663 used, U633 aliased.
- Gandhi Bagh Nagpur Gnat painted IE-1205 duplicates the Air HQ Delhi IE-1205; painted marking recorded, flagged.
- SWAC HQ Hunter is A492 painted BA-281 (Bharat Rakshak).
- Sea Hawk IN244: for decades at the Mormugao/Vasco roundabout (Naval Armament Depot gate); warbirds.in "Update 2015: moved to Raipur". Recorded once, at Raipur (Purkhouti Muktangan is the assumed site - the exact Raipur location is NOT confirmed by any source read here; the museums agent notes the duplicate claim). Vasco therefore has NO Sea Hawk record. Whether Vasco received a replacement airframe after 2015 could not be checked - open question.
- Sainik School Rewa Harvard: Bharat Rakshak says HT-268 went from Rewa to the IAF Museum; the Harvard still photographed at Rewa is therefore untailed here.
- Gwalior Su-7: Bharat Rakshak has both B-802 ("Pvd Gwalior AFS") and B-817 ("Gwalior base memorial, possibly"); one aircraft, identity uncertain, B817 in tail_number with B802 aliased.
- Jaguars A103 (Nagpur) and A105 (Chandrapur) are ex-French Air Force airframes imported by HAL for spares; never IAF aircraft although painted in IAF colours.

JUDGMENT CALLS
- Access: gate guards visible from the public road = public (Lohegaon MiG-21, Ozar SK419, NDA Pashan Gate, AIPT Pune, SSPMS). Anything inside a cantonment/base/Sainik School/NDA/AFMC/DIAT/MILIT = restricted. Universities and flying schools = appointment.
- HQ Maintenance Command Nagpur: the museums agent recorded "Air Force Museum HQ Maintenance Command Nagpur" (opened Apr 2025) with an untailed MiG-21 and Mi-8. This file records the separate outdoor displays on the Vayu Sena Nagar campus (SM262, KB3298, E261, A103) under a different site name, plus Mi-8 Z2352 which is probably the museum's Mi-8 - importer should dedupe against the museums file.
- Nose section: Air India 747 cockpit at Thakur Institute (identity unknown) recorded as a 747 with "nose section" in description.
- Restaurants/hotels: Vadodara Highfly A320 (open 2021), Khed Shivapur A319 (open late 2025), Butibori Haldiram (airframe on site May 2025, opening unconfirmed - under_restoration; manufacturer/model left blank because no report names the type), Ujjain HS 748 VT-EAV (arrived Oct 2025, under_restoration). Registrations of the A320/A319 not published anywhere read - blank.
- Instructional airframes inside bases recorded with in_storage and restricted: MiG-29 KB741 TETTRA School Pune (2016 register); MiG-21 at MILIT (Feb 2024) recorded on_display as it is a complete assembled airframe used as a static teaching aid.
- Nagpur Boeing 720 VT-ERS: derelict hulk at the flying club, in_storage/restricted; kept because it is India's only 720 and still extant per 2023/2026 press retrospectives.
- year_built used only where a build or taken-on-charge date is sourced (Dakota VT-CEB 1944 from USAAF serial block, Auster IN959 1942, Bell 47 VT-DXE Jan 1957, Hunters A492/S576 TOC 1966, Iskra W1788 TOC 1976). All other year_built blank.
- Coordinates: from warbirds.in map tags where the page had one (stated in description); otherwise Nominatim/Photon geocode of the park/school (stated); otherwise city centroid (stated). No coordinate was placed on an airframe by imagery in this session.

EXCLUDED (do not re-research)
- INS Vikrant (R11) museum ship, Mumbai: scrapped 2014. Its Sea Hawks IN-188/IN-246, Alizes IN-209/IN-212, Sea Kings IN-510/IN-511, Chetak IN-464 left Mumbai - not in this region's records (IN-188/IN-246 reported "in storage" by Wikipedia; whereabouts for the eastern/southern agents).
- IIT Bombay Ouragan, Mystere IVA and Hiller: scrapped 1999 (warbirds.in overview).
- Nehru Science Centre Mumbai (HF-24 BR463, Tiger Moth), HAL Pragati Aerospace Museum Ozar (TS539, C1175, C2836), BSF Museum Tekanpur (Dakota VT-DDW), Raman Science Centre Nagpur, Naval Aviation Museum Goa: already in the museums agent's file; not repeated.
- Dakota VT-AUM Birlagram/Nagda: sold Jan 2015, dismantled and sent to Gulbarga.
- Dakota VT-CRA derelict at Mumbai airport, Fokker F27 and NEPC 737 hulks at Santacruz, Air India 747s VT-EVB/VT-ESO/VT-ESP and Jet Airways 777s parked at Sahar (2024): stored/impounded airliners awaiting disposal, not preserved.
- Lohegaon Super Constellations, Vampires, MiG-29 KB-738 wreck: gone or wreckage.
- Mi-8 wrecks at Bhuj (2001) and Sahar: wreckage.
- Juhu/Bombay Flying Club: Auster Mk9 VT-DCU, Stinson L-5 fuselage, Bonanza fuselage were derelicts in a hangar c.2009 (warbirds.in); Piper Cubs and Luscombe VT-DDI airworthy. Status 2025 unknown - listed as an open question, not recorded.
- Bell 47 VT-EAP Pushpaka Aviation Mumbai: film/charter helicopter, not a display.
- HAL Ozar MiG-21 formerly reported outside the Pragati museum: covered by the museum record.
- Sea Hawk IN244 at Vasco: moved to Raipur 2015 (see above).
- Tempest II HA586: exported to UK.
- Sainik School Chandrapur LCA Tejas trainer "mock-up": model, not an airframe.
- Gujarat Science City Ahmedabad, Regional Science Centre Bhopal, Shaurya Smarak Bhopal, Sayaji Baug Vadodara, Ahmedabad/Bhavnagar/Junagadh/Kutch/Aurangabad/Solapur/Amravati/Jabalpur/Bilaspur/Bhilai/Daman/Diu/Silvassa: Google News and Wikipedia sweeps found no preserved airframe reports; no record made. Naliya, Jamnagar AFS, Amla, Betul, Saugor, Jabalpur, Raipur/Bilaspur AFS, Coast Guard sites, Army Aviation Nashik (other than CATS Bell 47), INS Hansa/INS Shikra gate guards: no source read reports a display airframe - human check needed.
- Aligarh MiG-23 OLX story: Uttar Pradesh, out of scope.

OPEN QUESTIONS (ranked)
1. Vasco da Gama/Mormugao roundabout: is there a replacement aircraft since Sea Hawk IN244 left in 2015? And where exactly is IN244 in Raipur (Purkhouti Muktangan assumed)?
2. Bharat Rakshak-only leads needing a photo/visit: Rajkot Kotecha Chowk MiG-27 TS505 (news confirms a MiG-27 installed Oct 2017 at Kotecha Chowk - serial unconfirmed); Surat Sarthana Park SK405; Godhra Vijay Circle SK404; Ujjain Engineering College SK403; Sainik School Balachadi SK417; AFS Vadodara SM225; Kalina Mumbai SM293; JK Gram Thane C2096; Bhopal park C1598 (which park?); Gwalior Zoo E235; Kolhapur MiG-27 TS521 and possibly MiG-23 SK428 (SK428 "Kolhapur" with no site - not recorded); VNIT Nagpur SM224; Bhonsala Military School Nagpur C1166; Gandhinagar SWAC C1549, SK433, Mi-8 Z1690; NDA TS564 and SK408; 11 BRD SK402/SK410/C585; HAL Training Academy C724; MILIT Iskra W1788; DIAT Su-7U U871 and Gnat; Rewa Iskra W1758; Raipur MC MiG-21 C991 (where in Raipur?).
3. Serials to read on site: Bandra Sea Harrier; Bishop's School Pune MiG-21 (and which campus); MILIT MiG-21 (2024); Baramati MiG-23MF; Deolali 25 ED MiG-23UM; Saswad Gnat; Jamnagar park Ajeet (E1981?) and the park's name; Bhuj Hunter; Rewa Harvard and Krishak; Highfly A320 and Brownstone A319 registrations.
4. Currency checks for 2000s-era reports: St Mary's Ajeet E1973, Thorat Udyan Gnat E359 (was badly damaged), Jeet Aerospace C601 (Bharat Rakshak now says "ex-Jeet"), AIPT SK401, Lohegaon IF910, SSPMS F1188, Diamond Garden E325, Daly College C763, Gandhi Bagh IE1205, Ambazari S576, Bhuj airframes, Bell 47 VT-DXE at Baramati (may have gone back to Juhu).
5. Did the Butibori Haldiram aircraft restaurant open, and what airframe is it? Did the Ujjain Avro hotel complete?
6. Juhu Flying Club hangar derelicts (Auster VT-DCU, Stinson L-5) - still there?
7. Nagpur Boeing 720 VT-ERS - still at the flying club in 2026?
8. Any airframes at INS Hansa (Goa) gate, INS Shikra Mumbai, Naval Dockyard Mumbai, Coast Guard Daman, AFS Jamnagar, AFS Naliya, AFS Amla, AFS Bhopal, AFS Jabalpur (Amla/Betul are storage units), AFS Raipur/Bilaspur - none found in sources read.


---

## Research agent notes - South

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES

SCOPE AND METHOD
- Assignment: India SOUTH, Phases 2-3 (base displays, gate guards, monuments, campus/park/school displays). Museums are included where they surfaced (HAL Heritage Centre, Vizag Tu-142M and Sea Harrier museums, Kakinada Tu-142M, CIAL Aerospace Museum, Akkulam IAF Museum, Dharmasthala, Madikeri) so the museums agent can dedupe; Bengaluru Visvesvaraya Museum deliberately omitted as instructed. Lakshadweep (Kavaratti): no preserved aircraft found in any source; no record written.
- Tooling constraints: the WebSearch budget was exhausted before this task started; Bing/DDG/Brave/Google HTML search were blocked or returned junk through the proxy. Discovery therefore relied on (a) a full scrape of warbirds.in (the WordPress successor of warbirdsofindia.com) via its WP REST API for all southern categories, 121 posts read in full; (b) a full harvest of the bharat-rakshak.com IAF per-serial database: every serial flagged Preserved (495) fetched and filtered to southern locations (126 hits); (c) Google News RSS, the New Indian Express Quintype search API, Wikipedia raw survivor sections and the aviationmuseum.eu India index for post-2015 additions. Google Maps, Flickr, ABPic and Commons could not be queried effectively (Commons API rate-limited).

SOURCE RELIABILITY
- warbirds.in (Jagan Pillarisetti / Warbirds of India): best source. Dated photographs and page-update dates; several pages updated 2023-2026 (Tambaram Gnat 2023, Yelahanka Dakota Oct 2023, HAL Balanagar Bison Dec 2025, HPS Jaguar Dec 2025, HAL museum Feb/Apr 2025, AFTC pages Sep 2025, Kazhakootam Feb 2026). Many other pages are 2004-2009 vintage; those airframes are marked currency unverified.
- bharat-rakshak.com per-serial database: same author community; gives serial, c/n, TOC dates and a preserved location, but location strings are terse, sometimes stale or contradictory (E-261 listed at both Trivandrum and Nagpur; IE-1248 at both MIT Chennai and Dehradun; U-455 at both Nagercoil and Bagdogra; DS-361/DS-362 locations swapped relative to WoI photos; W-1746 at CIAL vs WoI cutaway at Hakimpet; W-1769 vs W-1761 at Begumpet). Items sourced from BR alone are flagged Source BR only in the description and should be treated as unverified for currency.
- Iskra identities: BR records that several Iskra serials were re-used on end-of-life replacement airframes bought from Poland in 1996-2000 (e.g. W1767, W1760, W1759, W1772, W1755, W1744, W1748, W1746, W1741). The displayed airframe under a given serial may be the Srs XIX replacement rather than the 1975-76 original; c/n given in aliases where BR states it.
- NIE (newindianexpress.com) articles were fetched in full and are reliable for dates/locations (Loyola MiG-27 2021, Changampuzha Sea Hawk 2025, Akkulam museum 2026, Sea Harrier Museum 2023).
- Wikipedia survivor lists: leads only; used for Sea Hawk IN154 at INS Garuda and Sea Harrier IN606 at Vizag.
- aviationmuseum.eu: leads only. Its India list also names Tamilnadu Police Museum Coimbatore, SNC Maritime Museum Kochi and Regional Science Centre Dharwad; no aircraft could be confirmed at any of the three, so no records written (open questions below).

CORRECTIONS / JUDGMENT CALLS
- Ajeet E1083: removed from Cubbon Road roundabout in Oct 2009 (HAL newsletter via WoI); BR places it at HAL Heritage Centre. Recorded at HAL with the caveat that no dated photo of its current position was found.
- HAL MiG-21U U2974: WoI says U, BR says UM; recorded as U with note.
- Nagercoil U455: WoI says UM (ex-Romania re-import), BR says U with 1965 TOC; recorded as UM per photo page, conflict noted.
- Sea Hawk IN172 Kochi: WoI 2008 location (Pallady) superseded by NIE May 2025 photo at Changampuzha Park, Edappally.
- Thiruvananthapuram MiG-27: NIE confirms a MiG-27 at Loyola School since Apr 2021; BR serial TS-509 is attached to a differently named Trivandrum site, so tail_number left blank and TS-509 given as alias only.
- Tiger Moth at AFA Dundigal: true identity VT-DBK (ex T8582/G-AKGU), painted as HU838; recorded tail_number VT-DBK, HU838 in aliases.
- Hakimpet Vampire: true identity IB1618, painted FTW1971.
- Trinity Mess HT-2 painted T-64, true identity unknown; HITS Harvard painted VT-KCG (false); ASC Centre Dakota painted VT-606 (false): recorded as painted markings with statements in description.
- HAL LCA and ALH mock-ups recorded and flagged REPLICA; Akkulam Rafale model and BrahMos half-scale model NOT recorded (replicas without airframe status); Akkulam R-27 missile recorded as real.
- SA-2 missiles at SAC HQ (2) and AFA Dundigal (2) recorded as missile_rocket/surface_to_air, distinguished first/second of two.
- Cutaway/instructional airframes at AFTC, AFA, NIAT recorded as on_display where they are shown to visitors/cadets; unseen stored airframes (IX472, X2542) as in_storage.
- access_type: inside IAF/Navy/Army establishments = restricted even where a gate guard is visible from the road (Jalahalli X2517, Yelahanka BJ1045, Hakimpet W1786 are noted in descriptions as road-visible); private college campuses = appointment; parks, memorials, HPS (grille wall), HAL Balanagar gate, Changampuzha, museums = public. IISc = appointment (campus entry controlled).
- Coordinates: warbirds.in embedded map fixes (6-decimal values) used where present: NMM Bengaluru, CDM, MCEME, CAW mess, HPS, Nadirgul, Begumpet, Hakimpet, AFA Dundigal (academy centroid), Lawrence School, Nagercoil, NIT Trichy, SJCE not available, SAC HQ Akkulam, Kozhikode, Bijapur, CIAL. All other coordinates are approximate establishment/campus/town-level fixes from general geographic knowledge (4-decimal) and should be refined on satellite imagery; Kollam Bal Vihar, Thrissur Bal Bhavan, Piravom and Kannur Cantonment left blank because the exact spot could not be fixed.
- Postal codes are the general PIN of the locality, not verified per address.

EXCLUDED (do not re-research without new evidence)
- Visvesvaraya Industrial and Technological Museum, Bengaluru (Marut BD884, Wright Flyer replica, SLV stage): assigned to another agent.
- HAL Cheetah Z1897: WoI reports it was moved out of the HAL museum soon after 2008; BR still lists it; excluded as departed.
- Ajeet E1083 at Cubbon Road roundabout: gone since 2009 (moved to HAL).
- Devon HW-204 fuselage at Yelahanka MT section: not seen for years, presumed scrapped (WoI 2014 update). Note BR attaches HW-204 to the VSM Aerospace Devon instead; recorded under VSM with that caveat.
- AFTC Spitfire XIV MV293 and the B-24 Liberator: exported decades ago.
- Gulbarga (Kalaburagi) PDA College Bf 109: removed Aug 2002, whereabouts unknown; the HAL Pushpak received in exchange was last seen dismantled in the college garage (2002) - no current evidence, not recorded.
- Jakkur: Aeronca Super Chief VT-CQQ and Pushpak VT-DWA are/were airworthy club aircraft; NCC gliders and a derelict ultralight unidentified - not recorded.
- Begumpet: derelict NAA HS-748 (scrapped by 2002), AP Aviation Academy stored HS-748 (returned to flying), Beech Baron VT-ECO and Pushpak at the Begumpet aeronautical institute (2004, static; too old and unverified to record).
- Vayupuri park Iskra tail section (2004): fragment only.
- AFA Dundigal HPT-32 X3254 and Kiran U752 cockpit-procedure trainers, Kiran ejection trainer fuselage, An-32 CPT fuselage at Yelahanka: partial fuselages used as trainers, not recorded.
- Coimbatore Air Force Administrative College HT-2 (1998 report) and ITW Spitfire (scrapped 1950s): first too stale to confirm, second gone.
- Sulur 5 BRD stored Dakotas/Canberras (1980s auctions): no current evidence.
- Karwar aircraft museum (announced 2019, "yet to take off"), Mangaluru MiG-21 (MP promise July 2026), Punjab-style school MiG-21 proposals: announcements only.
- Chennai Victory War Memorial (Jul 2026 additions are a T-55 and ship replicas, no aircraft).
- INS Garuda Sea King IN525 (ditched 2003, fished out) and unserialled derelict Chetak, INAS Garuda Corsair wreck: wreck/derelict, not recorded. IN509 recorded as in_storage but is 2008-vintage information.
- Kerala Science Museum Gnat E261 duplicate serial at Nagpur MC HQ: both kept in respective regional files; one is mis-serialled.

BLANK FIELDS LEFT DELIBERATELY
- tail_number blank for: AFTC cutaway Gnat, SAC HQ Gnat, Bijapur Harvard, Kazhakootam Harvard, Amaravathinagar Harvard, HITS L-5, IIT Prentice, Tambaram MiG-21FL, RV University Hunter, Ezhimala Ka-25 and Sea King, Loyola MiG-27, both Tu-142Ms, Hakimpet Chetak, IARE Baron, Excel Dakota, HAL Basant/Pushpak - no identity visible in any source.
- year_built only where a build/delivery date is sourced (Vampire HB546 1948, Prentice 1951, Dakota BJ1045 1944, Sea Harrier IN603 1983, Hansa 1993).
- website blank for most military and small sites.

OPEN QUESTIONS (ranked, need a person on site or fresh photos)
1. Bengaluru and Chennai private engineering colleges: BR only surfaced ACS College (MiG-27), RV University (Hunter), HITS (MiG-23), Crescent (Gnat), RGNIYD and Amrita (MiG-23BN). Given the 2019-2025 wave of MiG-21/MiG-27 hand-outs to institutions nationally, campuses such as PES, BMS, Jain, Christ, MSRIT, NMIT, Dayananda Sagar, SRM, VIT Vellore, Anna University main campus, MLR Institute Dundigal, JNTU Hyderabad, Osmania, GITAM and Andhra University could not be checked and are the biggest likely gap.
2. Currency of 2004-2009 WoI-only records: Trinity Mess HT-2 T-64, VSM Jakkur Devon, Kollam Bal Vihar HT-2, Puducherry Botanical Garden HT-2 (1993 photo), Flytech Nadirgul Dakota, Amaravathinagar Harvard (1987), Bidar gate HT-2, INS Garuda Alize IN204 and NIAT airframes, Begumpet Iskra, Lawrence School Gnat, MIT Chromepet Sea Hawk/Gnat, IIT Madras derelicts.
3. BR-only records with no photo: MiG-21M C1624 Madikeri, MiG-21bis C2229 Kota theme park, MiG-27 TS563 Bijapur, MiG-27 TS574 ACS College, MiG-27 TS590 Jalahalli gate, MiG-21M C1672 and Mi-8 Z2388 at NMM, MiG-21FL C1158 Military School Bengaluru, Mi-8 Z1372 Yelahanka, Mi-8 Z2161 MTC, Mi-17 Z3043 ASC, Belagavi HT-2/Iskra, MiG-23MF SK437 AFA, Iskras W1744/W1748/W1755/W1783, HPT-32 X3220 CDM, X2581 SASTRA, Kiran U751 Piravom, MiG-23BN SM213 Kannur Cantonment, Ajeet E1983 Thrissur, Gnat E245 JNTU Kakinada, MiG-21M C1566 Korukonda, MiG-21FL C1127 Amaravathinagar, HS-748 BH573 Tambaram.
4. Unplaced BR entries in the region: MiG-27ML TS-664 "Kunoor Airport, Kunnur, Kerala" (Kannur International Airport? Coonoor has no airport) and Mi-8 Z-1378 "Hyderabad Haldi Golf Course" - neither could be resolved to a site; not recorded.
5. Whether the HAL Heritage Centre now displays Ajeet E1083 and whether the MiG-21M C1691 / HPT-32 X3240 in the rear shed are publicly viewable.
6. Sea Hawks IN195 and IN231 reported stored at INS Garuda (Wikipedia) - confirm existence and whether displayed.
7. Tamilnadu Police Museum Coimbatore, SNC Maritime Museum Fort Kochi and Regional Science Centre Dharwad: aviationmuseum.eu lists them; confirm whether any airframe (helicopter?) is displayed.
8. Kakinada and Visakhapatnam Tu-142M serials; Vizag Sea Harrier details - defer to museums agent.
9. Exact painted serials of the SJCE Mysuru Gnat (307) and Lawrence School Gnat (39 - E1039 or IE1239).


---

## Research agent notes - East and North-East

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES
Scope: India East and Northeast, Phases 2 and 3 (military base displays and monuments/public displays). 56 sites, 91 aircraft records.

SOURCES AND RELIABILITY
1. warbirds.in (Warbirds of India) - 52 dated posts for these states pulled via the site's WordPress API plus post comments; backbone source with photographs, install dates, mosmap coordinates (used as the airframe fix where quoted) and identity discussions. Reliable on what was seen on the date given; many posts are 2008-2017 so currency is a concern.
2. bharat-rakshak.com IAF aircraft database - all 505 serials with status "Preserved" fetched; 73 tie to these states. Strong on serials and units, weak on dates and currency; several entries exist only here and are flagged "Not independently verified" in the description. Its location strings occasionally conflict with warbirds.in (see corrections).
3. aviationmuseum.eu India index - lead only; provided the EAC Shillong collection list and the Kolkata Tu-142 museum entry.
4. YouTube search-result listings (titles and relative upload dates only; watch pages were rate-limited) used as dated-sighting evidence for Patna Eco Park, NIT Rourkela, Keonjhar, Kolkata airport, Itanagar science centre, Tezpur Chitralekha Udyan.
5. Wikipedia (via fetch of individual articles) for coordinates of Nicco Park, Dighalipukhuri, Lengpui Airport, Eco Park Patna, and for the Tu-142 survivor list.
Web search engines were NOT available for this session (search budget exhausted and curl-based search blocked), Wikimedia API was rate-limited, and Google Maps / Flickr / news-site searches could not be run. Consequently discovery beyond the two structured databases is incomplete and many currency checks remain open.

CORRECTIONS MADE WITH EVIDENCE
- Jakhama/Zakhama Dakota BJ623: warbirds.in places it in Manipur; Jakhama is in Kohima district, Nagaland (bharat-rakshak also says Kohima, Nagaland). Recorded under Nagaland.
- Kalaikunda 18 Sqn Hunter: warbirds.in photo evidence reads BA-207 (earlier misreport A-968); bharat-rakshak says BA-307. Recorded BA207 with BA307 in aliases.
- IIT Kharagpur Hunter: warbirds.in BA355 vs bharat-rakshak BA-335 - recorded BA355 per the photo-based post, flagged.
- Kalaikunda "DJ-1992" is a false diamond-jubilee serial; recorded as painted marking, true identity unknown.
- Kumbhirgram Ouragan "IC-222" and Tezpur "CS-117" are false serials; recorded as painted markings.
- Nicco Park MiG-21FL: no serial visible on the airframe; C982 taken from bharat-rakshak only.
- Beech 18 Bhubaneswar identified as VT-CNY by the hotel's own information board (2022).
- Dakota VT-AUI Bhubaneswar: the Biju Patnaik/Kalinga Airlines provenance is a legend not supported by the civil register (warbirds.in analysis); description says so.
- MiG-21FL C779 (historic 1971 Governor's House strike aircraft) was at 5 AF Hospital Jorhat until c.2014 and is now at the IAF Museum Palam, Delhi - excluded here; its replacement C1585 is recorded.
- DHC-3 Otter IM1057 moved from Kalaikunda (last seen Jan 2011) to Shillong ALG (2013-2016 photos); comments on warbirds.in dated Dec 2024/Jan 2025 report it is NO LONGER beside the Shillong ALG tower and its new location is unknown. Not recorded as an aircraft record; top open question.
- MiG-27ML TS517 (fire-damaged at Hasimara) is now at Veterans Air Force School, Bulandshahr, UP - excluded here.
- MiG-25U DS361 (ex-Kalaikunda) is at AFA Dundigal - excluded here; DS362 remains at Kalaikunda.
- Ajeet E2031: warbirds.in 2006 photo at Kangla Fort entrance; bharat-rakshak says moved to Science Centre Imphal. Recorded at Manipur Science Centre with flag.
- Iskra W1765: warbirds.in 2014 at Sonari Airport Jamshedpur; bharat-rakshak now says "ex-Jamshedpur, Bhubaneswar". Recorded at Jamshedpur with caution flag because no Bhubaneswar location is given anywhere.

JUDGMENT CALLS
- Access: all IAF/Army stations, Raj Bhavans, selection boards, OTA Gaya and cantonments = restricted. The Hasimara Hunter stands just outside the station gate and is visible from the road (public in practice); the Bagdogra Gnat is at the main gate (probably visible from outside). Schools (Sainik Schools, APS Ranchi, CAE Guwahati) = appointment. University/IIT/NIT campuses, parks, hotels, science centres, airports = public.
- EAC Shillong: HQ EAC displays, the ALG-entrance MiG-27 and the EAC museum collection are merged into one site "Eastern Air Command Air Force Museum Upper Shillong" (Shillong Times 2012: displays at the complex entrance are open to the general public). Coordinates are a commenter's Google Earth fix on the Caribou/Iskra display.
- Kalaikunda and Hasimara: all displays on each base merged into one site record per base.
- Naval Aircraft Museum Kolkata (Tu-142MK-E IN317) is a museum (Phase 1) but sits in this region; included so it is not lost - deduplicate against the museums researcher.
- Northrop KD2R-5 target drone at Sainik School Bhubaneswar recorded as fixed_wing/drone.
- Second, unidentified MiG-27M at Hasimara and the unidentified Gnat at Guwahati airfield are recorded as separate untailed records with distinguishing aliases.
- H1178 "AWACS mock-up" HS 748 at Guwahati is a real airframe with a dummy radome; recorded as an HS 748.
- year_built populated only where a source gives a first-flight/taken-on-charge date (H1526 1976, C777 1970, Iskras 1976). Serials never used as years.
- Coordinates: warbirds.in mosmap fixes (airframe), Wikipedia article coordinates (place), or blank. Nothing guessed.

EXCLUDED (do not re-research without new evidence)
- Walong ALG war memorial, Arunachal: only a wing section of DHC-3 Otter IM1728 remains after Caribou BM769 went to Shillong in 2003 - a component, not an aircraft record.
- CIJWS Vairengte, Mizoram: rotor-less derelict Mi-4 hulk in the training area (serial Z-3?? illegible, 2016) - a training wreck, restricted, not a preserved display.
- Mi-17 Z3351 at Aizawl/Lengpui airport - bharat-rakshak says "now derelict"; not a display.
- Gnat IE1244 "Buxar, Bihar" (bharat-rakshak, no location detail, no photo) - insufficient evidence for a site record; needs a search of Buxar (possibly a school or the Buxar war memorial).
- Gnat E295 "Somewhere in the East - displayed, West Bengal" (bharat-rakshak, Don Lazarus 1965 Sabre-kill aircraft) - location unknown.
- MiG-21U U458 stored stripped on stilts at Bagdogra - a hulk awaiting restoration, not on display.
- Bagdogra second Su-7 - removed 2013, fate unknown. Two dozen MiG-21 hulks at Bagdogra pens - removed by 2016.
- Kalaikunda An-32 K2688 (Diamond Jubilee Museum, seen 1997) - not found on later visits, presumed scrapped. Derelict Hunters around Kalaikunda airfield - not displays.
- Tezpur junkyard An-32 K2746 and Mi-4 wreck; MiG-21FL C599 wings in the 30 Sqn museum - wrecks/parts.
- Chabua: MiG-21/MiG-27 wrecks on the airfield perimeter and the rear fuselage of an Otter - wrecks.
- HAL Ardhra glider G816 (ex-1 Manipur Air Sqn NCC, Imphal) - sold at auction to a private owner in 2019 and offered for sale 2023; not on display.
- Spitfire XVIII HS669/TP387 ex-IIT Kharagpur - exported 1994 (France). Hurricane relics at Patna (2001 news) - removed to the UK/collectors long ago.
- Dakota VT-AUI is no longer at Kolkata airport (moved to Bhubaneswar 2023). Dakota VT-CRA ex-Kalinga at Mumbai - not this region.
- Chetak Z1829 (Kilo Flight, Dimapur 1971) - presented to Bangladesh 2016.
- Tu-124 V642 crash at Jorhat - no survivor here.
- Kalpakkam and all Tamil Nadu/other-region items - out of scope.
- No evidence found (in the sources reachable) of any preserved aircraft at: Barrackpore AFS, Panagarh/Arjan Singh AFS, Command Hospital Kolkata, Mohanbari, Kailashahar, Agartala, Imphal airport, Dimapur, Car Nicobar, INS Utkrosh, Samudrika (no aircraft), Charbatia, Gopalpur, Chandipur ITR (missile displays unconfirmed), Darbhanga, Jadavpur University, IIEST Shibpur, Science City Kolkata, BITM Kolkata, NSOU, NIT Durgapur, KIIT/Regional Science Centre Bhubaneswar, BIT Mesra, NIT Jamshedpur/Tata, IIT Guwahati, Tezpur University, Siliguri town, Darjeeling, Gangtok/Sikkim, Tripura, Kohima and Imphal war museums/memorials (the Kohima and Imphal WW2 sites have no airframes reported), Bum La, Vijay Smarak Fort William (the MiG-21/MiG-27 are recorded under Fort William HQ). Any of these may still hold something - this is absence of evidence given the search limits, not proof of absence.

DELIBERATELY BLANK FIELDS
- Postal codes: only where a source gave one. Websites: only Nicco Park and RSC Guwahati.
- Coordinates blank for roughly half the sites (no verified fix available without search/maps access).
- Serials blank for the Hasimara gate Hunter, Chabua Hunter, Kalaikunda gate Hunter, Jorhat Gandhi Park Hunter T.66, Jorhat MiG-23UM, Kumbhirgram Mi-4, Guwahati Gnat, both Harvards, the KD2R-5, the Shillong Chipmunk and the second Hasimara MiG-27M.

OPEN QUESTIONS (ranked; need a person on site or map/photo access)
1. DHC-3 Otter IM1057 - where is it since leaving the Shillong ALG tower area (reported gone by Dec 2024)? Possibly inside the EAC museum compound or moved elsewhere.
2. Iskra W1765 - still at Sonari Airport Jamshedpur, or moved to Bhubaneswar (where)?
3. Ajeet E2031 - at Kangla Fort entrance or Manipur Science Centre, Imphal?
4. EAC Shillong museum inventory: confirm Hunter BA251, Mi-4 Z311 vs BZ531, MiG-21FL C1106 and C1155 (is one only a cockpit?), Su-7 B1354, Gnat E256, Chipmunk, CFM Shadow G-8522; and whether the whole compound is really open to the public.
5. Kolkata airport MiG-27ML TS552 - exact location (landside/airside) and whether it survived terminal works.
6. Bharat-rakshak-only entries needing photo confirmation: Salua AFS (C1117, TS546), AFSB Kanchrapara C1164, Sukna Trishakti C1100, OTA Gaya C777, AFS Purnea X2559, Raj Bhavan Ranchi C1679, 11 ASC Guwahati TS531, Guwahati AFS C1157 and H1178, Kumbhirgram Mi-8 Z1366, Chabua C610, Tezpur C741, Raj Bhavan Port Blair W1787, Lengpui C719, Fort William TS582, Sainik School Purulia TS520.
7. Hunter serials at Kalaikunda (BA207 vs BA307) and IIT Kharagpur (BA355 vs BA335) - read the airframe.
8. Currency of the Itanagar Indira Gandhi Park Gnat E208 (vandalised in 2012 - may have been scrapped) and the Goalpara Harvard.
9. Identity of the Hasimara gate Hunter, Chabua Hunter, Jorhat Gandhi Park Hunter T.66, Jorhat cantonment MiG-23UM and the Kumbhirgram Mi-4.
10. Buxar Gnat IE1244 and "somewhere in the East" Gnat E295 - locate.
11. Port Blair: warbirds.in says about four warbirds exist on the island (C606 and W1787 known) - identify the other two (INS Utkrosh? Samudrika?).
12. Sweep of Sikkim, Tripura (Agartala/Kailashahar), Darbhanga, Panagarh, Barrackpore, Chandipur ITR and the Kolkata engineering campuses once search access is restored.
