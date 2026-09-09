# United Arab Emirates - research notes

3 sites, 9 aircraft. Files in `data/uae/`: `ae_museums.csv` plus one `<site_slug>_aircraft.csv` per site.

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

## Research agent notes - Full sweep

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES
Research date September 2026. The session's web-search budget was exhausted part-way through the sweep, so later checks relied on direct page fetches only; several leads below remain open for that reason.

SOURCES USED AND RELIABILITY
- sharjahmuseums.ae (Al Mahatta Museum page): official; gives address, hours and fees; shows no renovation notice but is not necessarily current.
- ruudleeuw.com (Al Mahatta 2010 visit): very reliable on the DC-3 false-identity story with full registration chain.
- sites.google.com/site/lgarey (RAF Sharjah / Al Mahatta page): detailed identities and c/ns for all museum aircraft; good, but c/n for the Heron conflicts with Wikipedia.
- ABPic photos dated 18 Sep 2013 (Jean Marc Braun) for all Al Mahatta airframes; ABPic photos 2007 and 2011 for the CERT MB-326KD; ABPic 2008 photos of HCT Dubai instructional airframes.
- airhistory.net photo 147632 (12 Apr 2005): confirms Anson identity TX183/G-BSMF painted as G-AKVW.
- Flickr (Alan Wilson 14 Sep 2015; Michael Kelly 22 Jan 2020): dated confirmation of Anson and VC10 nose.
- vc10.net airframe page: authoritative VC10 timeline (c/n 883, dates of move to Sharjah).
- aerialvisuals.ca dossier 114418: Comet XK655 history and nose at Sharjah.
- The National 7 Nov 2016, Khaleej Times 1 Oct 2023 and 1 Aug 2024, Gulf News: local press confirming displays; Khaleej Times mis-identifies the ENAM TriStar as a three-engined Douglas.
- JetPhotos registration page TT-DWE: nine dated photos 2010-2025 at the Emirates National Auto Museum; the 2 Oct 2025 photo is the currency evidence.
- dubicars.com (20 Jul 2024) identifies the ENAM aircraft as a Lockheed L-1011 TriStar; airteamimages (6 May 2012) gives its operating history.
- Wikipedia (Mahatta Fort, Al Mahatta Museum, Umm Al Quwain Il-76, Emirates National Auto Museum, Al Bateen Executive Airport): leads and coordinates only; the museum article says the fort was closed for renovation as of June 2025; the Heron c/n 14034 there is unverified.
- glimpsesofuae.com (updated 27 Oct 2024): states Al Mahatta Museum temporarily closed.
- aviationmuseum.eu: lead generation only; lists Al Mahatta and an Etihad Museum entry claiming a UAE Army Gazelle SA342L serial 139 (see open questions).
- thunder-and-lightnings.co.uk Hunter survivors: lists only one Hunter in the UAE, F.51 E-423 privately owned in Abu Dhabi, with no location; not recorded (private, no public access, no site).
- helis.com, scramble.nl orbat, keymilitary, Flickr tag pages, JetPhotos airport pages: checked, no preserved/displayed UAE airframes found.

CORRECTIONS MADE WITH EVIDENCE
- DC-3 "G-AMZZ" is c/n 12254 / 42-92452 (ruudleeuw.com, lgarey), not the real G-AMZZ; recorded under true identity with the painted marks as an alias.
- Anson "G-AKVW" is TX183 / G-BSMF (airhistory.net, Flickr Alan Wilson, lgarey).
- Dove "G-AJPR" is Dove 6 G-ARDE ex I-TONY (ABPic, lgarey).
- Heron "G-ANFE" is Sea Heron C.20 XR443 / VH-NJP (ABPic, lgarey).
- VC10 nose is ZA149 ex 5X-UVJ (vc10.net, Flickr); Wikipedia lists only 5X-UVJ. vc10.net page title and body give c/n 883; airportspotting.com says 884; recorded 883 with the conflict noted.
- Umm Al Quwain Il-76: the assignment's suggested identity UP-I7605 is wrong; the airframe was Centrafrican Airlines TL-ACN (Flickr caption; Khaleej Times). It was dismantled and scrapped in May 2022 for the Siniyah Island bridge works (Wikipedia; Khaleej Times 29 Dec 2022); skin was upcycled by Wings Craft of Ajman. Excluded.

JUDGMENT CALLS
- Al Mahatta Museum recorded as public / on_display even though two sources (Oct 2024 blog, Wikipedia June 2025) say it is temporarily closed for renovation; the official SMA page still lists hours and the collection has not been reported moved. Needs confirmation of reopening.
- Comet and VC10 forward fuselages recorded as aircraft with "nose section" in aliases and description.
- Comet recorded under RAF identity XK655 (last operational identity) with BOAC marks G-AMXA as alias; role given as electronic_warfare for the R.2 conversion.
- VC10 recorded as variant K.3 under RAF serial ZA149 (its last identity) although displayed in Gulf Air airline colours; role commercial_transport reflects the display presentation.
- MB-326KD 204 at the CERT complex is recorded despite the last dated evidence being 2011, because it is an outdoor preserved display on a college campus rather than a training fleet; flagged as unverified. Access set to appointment (college campus). Coordinates are the Abu Dhabi city centroid.
- Emirates National Auto Museum TriStar: coordinates are the museum building (Wikipedia 24.09890 54.42011); the aircraft is beside it.

EXCLUDED AND WHY
- Umm Al Quwain Ilyushin Il-76 TL-ACN (ex Air Cess / Centrafrican, Viktor Bout associated): scrapped May 2022. Do not re-research.
- Handley Page HP.42 "Hanno" at Al Mahatta: a miniature model, not an airframe.
- Higher Colleges of Technology, Dubai (Dubai Men's College) instructional airframes photographed 18 Feb 2008 on ABPic: Short Skyvan 3-100 "320" (ex UAE AF), Aermacchi MB-326KD "207", MBB Bo 105C "786", Jet Provost T.3A G-BXBJ, Piper PA-23-250 Aztec A6-ZAZ, Agusta-Bell 47G-2 A6-BEL, Beech J50 Twin Bonanza D-INES; also Agusta-Bell 206B "167" and Piper PA-28-140 A6-ACE at the Abu Dhabi CERT complex (2007). These are ground-instructional airframes inside college hangars with no evidence after 2008 and the Dubai college has since moved campus; not recorded. Worth a site visit (see open questions).
- Boeing 747-300 upper deck ex VH-EBV / XT-DMA at Falcon Aircraft Recycling, Ras Al Khaimah: offered for sale April 2018 (The National); a scrap-yard section, not a public display; fate unknown.
- Antonov An-2 wreck near Al Aweer, Dubai (Smithsonian Air & Space 2021): a crash wreck in the desert, not preserved.
- Dubai Miracle Garden "Emirates A380": a floral structure on a steel frame, not an airframe.
- Etihad Museum, Dubai: no aircraft per Wikipedia, museum reviews and the official description; aviationmuseum.eu's Gazelle claim unverified (see open questions).
- Emirates first A380 A6-EDA and other retired Emirates/Etihad airliners: scrapped or parted out; no preserved Emirates or Etihad airframe found in the UAE.
- Hawker Hunter F.51 E-423 "privately owned, Abu Dhabi" (thunder-and-lightnings): no site, no public access, unverified.
- Solar Impulse 2 at Al Bateen (2015): a departed operational aircraft, not a display.
- Emirates National Auto Museum cars, Al Ain Classic Car Museum, Sharjah Classic Cars Museum, Sharjah Science Museum, Al Murabba Police Museum: no aircraft found.
- Active fleets: Al Fursan, UAEAF, Abu Dhabi Aviation, Dubai Police Air Wing, Fujairah Aviation Academy, Emirates Flight Training Academy, Al Jazeirah Aviation Club, Skydive Dubai, Umm Al Quwain Aero Club: operational, not recorded.
- Planned UAE Military Museum / Armed Forces Museum, Abu Dhabi (RAF Museum MoU 2013): no evidence of opening or of aircraft; not recorded.

BLANK FIELDS LEFT DELIBERATELY
- Postal codes: the UAE has no postal-code system.
- year_built blank for Heron (1955 is a delivery year from a single secondary source), Auster and MB-326KD (no sourced build date).
- Heron c/n not put in tail fields because sources conflict (14072 vs 14034).

OPEN QUESTIONS NEEDING A HUMAN ON SITE (ranked)
1. Is Al Mahatta Museum open again after the 2024-25 renovation closure, and are all eight airframes/sections still inside (Comet nose, VC10 nose, DC-3, Anson, Heron, Dove, Auster)? Check for any new arrivals.
2. Is the MB-326KD 204 still outside the CERT complex / Abu Dhabi Men's College, and are the Jet Ranger 167 and Cherokee A6-ACE still there? Get exact coordinates.
3. Do the former HCT Dubai instructional airframes (Skyvan 320, MB-326KD 207, Bo 105 786, Jet Provost G-BXBJ, Aztec A6-ZAZ, Bell 47 A6-BEL, Twin Bonanza D-INES) survive at the Dubai Men's College Academic City campus or anywhere else?
4. Military gate guards: no dated evidence was found for any preserved Hunter, Mirage 5/2000, Hawk, Alpha Jet, MB-339, SF-260, Puma, Alouette or Bell 205 at Al Dhafra, Al Bateen, Al Minhad, Sweihan/Zayed Military City, Khalifa bin Zayed Air College (Al Ain) or Sharjah air base. Each of these bases should be checked from the public road; the Abu Dhabi Defence Force Hunter FGA.76/T.77 fleet appears to have gone to Somalia with no UAE survivor documented.
5. Etihad Museum, Dubai: aviationmuseum.eu lists a UAE Army Aerospatiale SA342L Gazelle serial 139 there; no other source mentions it. Confirm whether it exists (possibly a temporary exhibition) and whether it is still displayed.
6. Hawker Hunter F.51 E-423 reported privately owned in Abu Dhabi: locate and determine whether it is publicly visible.
7. Zayed National Museum (opened Dec 2025) and its 2026 UAE Armed Forces 50-years exhibition: check whether any real airframe is included.
8. Ras Al Khaimah: whether any Falcon Aircraft Recycling sections (747-300 upper deck) were installed anywhere publicly.
9. Emirates / Etihad: whether any retired airframe (777, A380, A340) has been preserved at Emirates Aviation University, Emirates Engineering, Etihad Aviation Training or Expo City; none found.
