# Saudi Arabia - research notes

15 sites, 78 aircraft. Files in `data/saudi_arabia/`: `sa_museums.csv` plus one `<site_slug>_aircraft.csv` per site.

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


### Build-pass correction (Saudi Arabia)

F-86F "709" at the King Abdulaziz Air Base main gate is recorded under its USAF
identity 52-4537 (aerialvisuals), with 709 as an alias, because the Riyadh museum's
F-86H also wears 709 and the two would otherwise collide on the `(model, tail)` key.


---

## Research agent notes - Full sweep

(Verbatim from the research pass; counts quoted inside refer to the pre-merge package, not the final files.)

NOTES

RESEARCH CONDITIONS
- The WebSearch budget for this session was exhausted early, after which discovery relied on direct fetches: aerialvisuals.ca (Locator search for Saudi Arabia and its 15 location dossiers, plus airframe dossiers), ABPic (Riyadh location listing, 44 photos dated April 2012), Wikimedia Commons API (museum category and base photos), Wikipedia (Lightning survivor section raw wikitext, museum article, base articles), thunder-and-lightnings.co.uk and lightningassociation.co.uk survivor tables, JetPhotos and Flickr single photo pages, Saudi Arabic press (Makkah newspaper, Al Bilad, SPA), OSM Nominatim for reverse geocoding. airliners.net, jetphotos search, airhistory.net, key.aero, britmodeller and scramble.nl were blocked (402/403/Cloudflare). Google Maps/Street View could not be consulted.

SOURCE RELIABILITY
- ABPic (Steve Cos / Mark Pattenden, 25-27 Apr 2012): best serial evidence for the Riyadh museum; 14 years old.
- aerialvisuals.ca: the Saudi Arabia Locator is largely satellite-imagery identification ("0:" entries) with a few named airframes; excellent for positions, weak on identities and dates. Its museum dossier says "smaller external exhibits are regularly rotated".
- thunder-and-lightnings.co.uk / Lightning Association: authoritative for Lightning identities; Saudi entries last updated 2008-2009.
- Wikipedia Lightning survivor section: gives GPS fixes for Tabuk, Al Kharj and Khamis Mushait; uncited but consistent with Commons photos dated 2018 and 2023.
- aviationmuseum.eu (two versions of its list, 2017 and undated): used only as a lead; it contains obvious errors (Lightning "F.2 610", "T.4 54-608" which is actually at Al Kharj, F-15 "1315", A-26 "612").
- Visitor reports for currency: allplane.tv May 2022, theotherpaths Aug 2024, Wanderlog/Google review Jan 2026 (museum open, F-15 and C-130 highlighted).

CORRECTIONS MADE
- Lightning at Prince Sultan AB: Wikipedia calls it "486" with no mark; 2023 Commons photo shows a two-seat canopy, so it is a trainer, matching thunder-and-lightnings' T.54 54-608 (ex XM992). Recorded as T.54 54-608 painted 486.
- Tabuk roundabout Lightning: recorded as 53-699 (Lightning Association: plinth-mounted by BAe Aug 1985; JetPhotos 2019 caption 227 / 53-699), not "unidentified".
- Museum F-15: aerialvisuals and thisdayinaviation identify it as the F-15B prototype / Strike Eagle demonstrator 71-0291, not an RSAF F-15C/D as Wikipedia and Commons captions say.
- Museum Boeing 707 c/n: ABPic gives 20181, aerialvisuals 21081; 21081 is the plausible c/n for a 1975 707-368C and is used.
- Museum A-26 painted 302 (photo), not 612 (aviationmuseum.eu) or 301 (blog).
- Dhahran F-86 "709" and museum F-86H "709": two different airframes carry the same code; both recorded with the conflict noted.
- 53-684 for the Taif mall Lightning is doubtful because the Lightning Association records 53-684 as crashed in 1980; recorded by painted code 1303 only.

JUDGMENT CALLS
- Wapiti IIA and DH.9A at the museum are replicas and are flagged as such.
- The Ras Al-Sheikh Hamid Catalina is an abandoned wreck, not a curated display; included and clearly described because it is a publicly visited historic airframe. Delete if the database wants only curated displays.
- Aircraft located only by aerialvisuals satellite identification (Tabuk air park, Taif, Dhahran interior, Jeddah air base) are recorded with blank serials and their coordinates in the description. They are inside bases and marked restricted.
- Dhahran main gate Lightning/F-86/T-33 are marked public on the strength of Wikipedia listing XM989 under "on display" (as opposed to "no public access"); verify from the public road.
- The KFUPM T-33 is a single aerialvisuals imagery point that reverse-geocodes to the university campus; recorded as its own site with access "appointment" but it may belong to the adjacent air base.
- Jeddah Dakota (ex G-AGHM) recorded as in_storage at Prince Majed Park on the municipality's 2021 statement; may be on display in the renovated park or may have gone.
- Sea Kings and Hawks at the museum are included on aviationmuseum.eu serials with a 2022 visitor corroborating Sea Kings; BAe 125-800Bs (HZ-105, HZ-109, HZ-110, HZ-130), Beech UC-45F 55226, Beech T-34A 619, Cessna F.172G 802 and 804, Vampire 541/228, Strikemasters 911 and 1109/1110, AB 206A 1220 and Hunter "60-604 replica" are listed by aviationmuseum.eu only and were NOT entered; a visit is needed to confirm which are present (the museum rotates small outdoor exhibits).
- Wikipedia's "F-15D", "UH-1", "OH-58", "Cessna 172", "Maule M-6" list for the museum: F-15 handled above; the UH-1 and OH-58 are probably the AB 212 and AB 206 recorded; Cessna 172 (aviationmuseum.eu N8846B or 802/804) not entered.

EXCLUDED
- Riyadh Boulevard Runway (Riyadh Season zone, Boulevard City): three ex-Saudia Boeing 777-200ERs trucked from Jeddah in Sept 2024 and converted to restaurants/entertainment venues. Excluded as a seasonal entertainment installation per brief; if the zone becomes permanent these three airliners would qualify as preserved restaurant conversions. Registrations not found.
- Dive Bahrain Boeing 747-236B TF-AAA (aerialvisuals lists it under Dhahran): sunk as a dive reef in Bahraini waters, not in Saudi Arabia.
- Ex-RSAF Lightnings returned to Warton in 1986 (ZF57x-ZF59x series, 53-671 at Gatwick etc.) are outside the Kingdom and not listed.
- 53-684 crashed 1980, 53-667, 53-673/680, 53-697 (shot down 1970), 53-414: losses, no airframe.
- Old Jeddah Kandara airport (closed 1981): the airframes found there (Vampires including 509, T-28As 49-1681 and 51-7723, T-34s, Chipmunks, DC-3s, Convairs) were scrapped, moved to Riyadh (C-54 450, A-26 302) or to the Jeddah displays above; nothing remains on the demolished site.
- Hijaz Railway Museum, Madinah: railway only, no aircraft.
- National Museum of Saudi Arabia / King Abdulaziz Historical Centre, Riyadh: no aircraft found in any source.
- Ithra (King Abdulaziz Center for World Culture), Dhahran, and the Aramco exhibit: no airframe found.
- King Salman Science Oasis, Riyadh; KAUST Museum of Science and Technology in Islam: no aircraft.
- Riyadh Air Show / World Defense Show statics: temporary.
- Active RSAF, Saudia and aero-club aircraft: operational, excluded.
- King Abdulaziz University engineering faculty Vampires (1981 transfer per blog): no evidence they survive; not entered (the Al-Salamah Vampire 515 may or may not be one of them).

OPEN QUESTIONS (ranked)
1. Riyadh museum current outdoor inventory (2025-26): confirm presence and serials of Sea Kings, Hawks, BAe 125s, C-45, T-34, Cessna 172s, second Vampire, extra Strikemasters, O-1; read the RSAF serial painted on the F-15 71-0291.
2. Jeddah: is the ex-G-AGHM Dakota on display in Prince Majed Park, and does the Beech 18 still stand on its King Khalid Street pole?
3. Jeddah Al-Salamah Vampire 515: which institution holds it and is it viewable?
4. Dhahran main gate (Lightning 607, F-86F 709, T-33 1503): visible from the public road?
5. Tabuk: identity/code of the air-park Lightning (53-698?) and whether the F-5 and F-86 on the airport road are on public roundabouts.
6. Taif's Heart Mall Lightning 1303: still present in 2025-26? True identity?
7. Khamis Mushait: painted codes of 53-687 and identity of "224".
8. KFUPM T-33: campus display or base?
9. Dhahran Tornado IDS 765 and ADV 2917: still displayed?
10. Prince Majed Park and other Jeddah roundabouts: the 2019 blog says "most are now preserved in museums or on poles around Jeddah" and mentions a restored Convair CV-340 placed at a roundabout; no location found.
