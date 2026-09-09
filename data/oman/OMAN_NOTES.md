# Oman - research notes

9 sites, 19 aircraft. Files in `data/oman/`: `om_museums.csv` plus one `<site_slug>_aircraft.csv` per site.

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



---

## Research agent notes - Oman and Kuwait sweep (shared notes; the other country's items also apply to its own data directory)

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES

RESEARCH CONSTRAINT: the shared web-search budget for this session was exhausted about two-thirds of the way through (all remaining work used direct fetches of known sites: ABPic, Thunder & Lightnings, dstorm.eu, bacstrikemaster.co.uk, aviationmuseum.eu, Flickr, JetPhotos, AirHistory.net, Wikipedia). The Oman town-by-town sweep (Sohar, Nizwa, Sur, Ibri, Buraimi, Khasab, Musannah, Adam, Jebel Akhdar memorial, Ras Al Hadd, universities, Royal Guard, police, navy/army museums) therefore rests on the initial searches only, which produced no leads; treat Oman as incomplete outside Muscat and the RAFO bases.

SOURCES AND RELIABILITY
- ABPic (abpic.co.uk): dated photos with c/n and remarks. Highest weight. Gave the complete SAF Museum outdoor line-up (7 Oct 2017) and Hunter 831 at Seeb (22 Nov 2012), Kuwait Skyhawks (Mar 1994), Lightning 53-418 (Jan 1997), 53-415 at Al Jaber.
- Flickr album 'Aircraft throughout the years' (user 61758703@N07), Kuwait 2016: dated photos of every surviving Kuwaiti Lightning and of the KAF museum Skyhawks/Mirages, with location captions. High weight.
- JetPhotos (Sebastian Sowa, 16 Jan 2020): KAF101, KAF882 at the KAF museum. AirHistory.net (2016, Jan 2020): Al Jaber Lightning trio, Hunter 213 + Lightning 412 at the airport military gate, Ali Al Salem 53-423 and dumped Mirages.
- Thunder & Lightnings (thunder-and-lightnings.co.uk) Lightning survivor pages (current Nov/Dec 2021) and Hunter survivors list (Oman entries current only to Dec 2002). Good for identities, weaker for currency.
- Scramble 'Lightning strikes over Kuwait' (undated, c.2019-21): full disposition of Kuwaiti Lightnings; agrees with Flickr and T&L.
- dstorm.eu Oman/Kuwait individual-aircraft pages: fates for Hunter, Strikemaster, Jaguar, Puma, Skyhawk, Mirage. Undated but detailed; used for Omani gate guards.
- bacstrikemaster.co.uk 'Strikeys' survivors list: Oman gate guards and instructional airframes; data snapshot c.01/2010. Medium weight and stale.
- aviationmuseum.eu: lead generation; contains errors (Strikemaster '023' for 423, Lightning '53-411' for 55-411, Dakota 'G-AMZZ' which is actually at Sharjah, Bell '412ST' for 214ST). Its map pins were used for the two Muscat airport monuments.
- aviagraphers.net (KAF museum visit 17-20 Jan 2018) and tristaraviation.org (Feb 2020) for Kuwait museum contents and access; Tripadvisor / wanderlog reviews for currency (SAF Museum reviews to Nov 2024; Science museum review 16 Dec 2025).
- Wikipedia via curl (render view) for coordinates only; the 'List of surviving Lightnings' page could not be retrieved (rate-limited) - T&L used instead.
- Grokipedia not used.

CORRECTIONS MADE
- Strikemaster at SAF Museum is 423 (ABPic c/n PS.349, bacstrikemaster.co.uk, dstorm.eu), not 023 (aviationmuseum.eu).
- KAF museum two-seat Lightning is T.55K 55-411 (T&L, Scramble, Flickr), not '53-411'.
- Kuwait science museum Dakota is NOT G-AMZZ (that airframe is at Al Mahatta, Sharjah, photographed there 2007-2021). Identity left blank.
- Hunter 841 at SAF Museum is an FGA.73B (ABPic, dstorm.eu), not 'F.6' (aviationmuseum.eu).
- Lightning 53-423 at Ali Al Salem wears the false serial 53-421; the real 53-421 is at Mubarak Camp HQ. Recorded accordingly with alias.
- Beaver at SAF Museum: true identity XP824 (ex-AAC), painted 213 (ABPic code field, aviationmuseum.eu).

JUDGMENT CALLS
- Access: all Kuwaiti and Omani air-base displays are 'restricted' (inside controlled gates), including the KAF museum, which sources say is not open to the public (visited only during the biennial Kuwait Aviation Show). The Al-Mubarak military gate pair (Hunter 213 / Lightning 412) is recorded 'restricted' because no source confirms visibility from a public road; a human check could upgrade it to public. RAFO Seeb Hunter 831 is recorded 'public' because it is a gate guard at the base entrance photographed by visiting enthusiasts in 2002, 2012 and 2016; the Bell 214ST is 'restricted' pending confirmation of where exactly it stands.
- Air Force Technical College Strikemasters (412/415/421/424) are recorded as 'in_storage' instructional airframes of a retired type - they may be display pieces or may have been scrapped since 2010; flagged.
- Bait Al-Othman Jet Provost included on two independent but thin sources (2013 car-park sighting; 2020 statement it moved indoors). Untailed.
- Whirlwind serial 313 and Hunter 214 at the KAF museum are single-source identities and flagged in descriptions.
- Coordinates: SAF Museum = Google/wanderlog pin; Seeb Hunter and Bell 214ST = aviationmuseum.eu pins; KAF museum = aviationmuseum.eu pin (29 14 04.6 N 47 58 53.1 E); Science museum = Google pin (wanderlog); Bait Al-Othman = Expedia map pin; air bases = Wikipedia airfield reference points; RAFO Ghala and RAFO Lansab = Al Ansab locality centroid (Wikipedia) - both flagged; PAAET Shuwaikh and Mubarak Camp left blank deliberately.
- year_built left blank throughout (no sourced build dates except first-flight dates for 53-422 and 53-423, which are given in descriptions only because they are first flights, not builds; add 1969 if the database treats first flight as year_built).

EXCLUDED (do not re-research without new evidence)
Oman:
- Jaguar at Sultan's Armed Forces Museum: mentioned only in one Tripadvisor review (Dec 2018) listing 'Strike Master and a Jaguar'; not in the ABPic Oct 2017 line-up, aviationmuseum.eu, or any photo. Possibly the Hunter mistaken for a Jaguar. Not recorded - check on site. RAFO Jaguars retired 2014; over 20 airframes reported Dec 2025 as going to India for spares, so a museum Jaguar is plausible in future.
- Hunter FR.10 853 (ex XF426): donated to RAF Museum, Hendon (UK). Not in Oman.
- Hunter FGA.73B 842: returned to Jordan (King Hussein Air College, Mafraq).
- Strikemaster 425 (G-SOAF): airworthy in the UK (North Wales Military Aviation Services). Strikemaster 402: to Singapore then USA (Eagle River WI). Strikemaster 422: 'in storage' at Masirah in 2010 - noted in the 414 record only.
- Super Puma 615 (ex Royal Flight A4O-HC): 'to instructional airframe' per dstorm.eu, no location - not recorded.
- Skyvan / BAC 1-11 / Viscount / Britten-Norman displays at Seeb / Muscat International: no evidence found in any source; Wikipedia 'aircraft on display' sections for the One-Eleven and Viscount list nothing in Oman. Skyvans 910 and 915 photographed at Seeb 2012-13 were operational.
- Oman Across Ages Museum (Manah, opened Mar 2023), National Museum Muscat, Bait Al Zubair, Muscat Gate Museum: no aircraft found in any description; the SAF Museum Wikipedia article mentions only an ejection seat indoors.
- No evidence found for aircraft at Sultan Qaboos University, Military Technological College, Royal Guard of Oman Technical College, Royal Army/Navy/Police museums, Oman Air / Oman Aviation Academy, Royal Flight, Sohar, Nizwa, Sur, Ibri, Buraimi, Khasab, Musannah, Adam, Jebel Akhdar, Al Baleed, Ras Al Hadd. Search budget ran out before these could be probed individually - see open questions.
Kuwait:
- Kuwait House of National Works (Memorial Museum): permanently closed since 2017; its Gulf War displays were dioramas/models, no real airframes.
- Historical, Vintage and Classical Cars Museum (Shuwaikh): cars only.
- Kuwait National Museum, Al Qurain Martyrs Museum, Scientific Center, Sheikh Abdullah Al Salem Cultural Centre, Al Shaheed Park, Kuwait Towers: no aircraft found.
- Camp Arifjan / Camp Buehring (US Army): no static displays found.
- Failaka Island Iraqi wrecks, and A-4KU 821 wreckage / Mirage F1CK 710 and 711 dumped at Ali Al Salem / Lightning T.55K 55-410 fire-training wreck at Ali Al Salem: derelict, not preserved displays.
- Kuwait Strikemasters Mk 83: all traded back to BAe and sold to Botswana; none in Kuwait. Kuwait Hunter T.67s: none reported surviving in Kuwait.
- Kuwait Airways: no preserved airliner in Kuwait; 747-269B S2-ADT cockpit is at Sinsheim, Germany.
- Kuwait Aviation Show static parks (Jan 2018, Jan 2020): temporary.
- 2026 Iran-war drone strikes hit Kuwait International Airport (Terminal 1, fuel, radar; Feb-Jun 2026) and Ali Al Salem; no source mentions damage to the preserved aircraft, but currency of the KAF museum and Ali Al Salem displays after March 2026 is unverified.

OPEN QUESTIONS (ranked)
1. Is the Kuwait Air Force Museum still in the Al-Mubarak hangars, or did the 'downtown relocation within a year' mentioned to visitors in Jan 2018 ever happen? Any damage from the 2026 strikes?
2. Oman RAFO base displays (Masirah 414, Thumrait 403, Salalah 417 and Hunter 847, Ghala 420 and Hunter 844, Lansab 418, AFTC Seeb 412/415/421/424) all rest on c.2010 lists with no dated photographs - need any post-2015 confirmation, exact positions, and the correct establishment names for 'Ghala' and 'Lansab'.
3. Is Hunter 831 (and the Bell 214ST) still at the RAFO Seeb gate / Muscat airport after the 2018 new-terminal works? Last photo 2016.
4. Does the Sultan's Armed Forces Museum hold a Jaguar (and is the museum currently open - Tripadvisor shows Nov 2024 reviews, wanderlog showed 'temporarily closed' after Sep 2023)?
5. Identity of the Dakota and confirmation of Jet Provost 103 / Auster 9K-AAI at the Kuwait Science and Natural History Museum; is the aviation hall open?
6. Bait Al-Othman: confirm the Jet Provost is there, indoors, and its serial.
7. Identity/serial of the Whirlwind (313 / WA.319) and the museum Hunter (214) at the KAF museum; whether the gate Hunter is really 213.
8. Condition of the Ahmed Al Jaber Lightning trio after the 2018 windstorm.
9. Exact positions for the PAAET Shuwaikh Lightning and the Mubarak Camp Lightning (coordinates deliberately blank).
10. Full Oman town sweep (Sohar, Nizwa, Sur, Ibri, Buraimi, Khasab, Musannah, Adam, Jebel Akhdar memorial, Ras Al Hadd, SQU, MTC, Royal Guard/Police/Army/Navy museums) still to be done.
