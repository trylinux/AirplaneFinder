# Zero-record sweep: Bhutan, Maldives, Timor-Leste, Macau, Palestine

FETCH pass per CONTRACT_ZERO.md. Method: MediaWiki API (native-language extracts
and searches) plus WebSearch/WebFetch where the Wikimedia proxy was rate-limited
or the topic is not well covered on Wikipedia (the Nablus 707 restaurant).
Wikimedia APIs on this environment's shared egress needed ~90-120s between
successful calls (repeated 429s at 5-60s spacing); this cut the number of
queries actually achievable well below the "dozen extracts per country" budget
for the harder-throttled window. Overpass/OSM sweep was NOT run this pass due
to time spent on rate-limit backoff — flagging this as an uncertain/incomplete
item rather than silently skipping it.

## SITES

name: The Palestinian-Jordanian Airline Restaurant and Coffee Shop Al-Sairafi
city: Nablus (Wadi al-Badhan, adjacent to a waste-sorting station)
state_province: West Bank
country: Palestine
postal_code:
region: Middle East
address: Wadi al-Badhan, near Nablus
website:
access_type: public
latitude:
longitude:
source: VOA Learning English "Palestinian Brothers Open Restaurant in Old Airplane" (Aug 2021); Times of Israel "Palestinian twins turn Boeing 707 into West Bank restaurant" (Jul 2021); corroborated by France24, Arab News, Al Bawaba, Seattle Times, Wings Magazine wire-service versions of the same AP story
confidence: medium — good contemporaneous (2021) sourcing at opening, but NO post-2021 confirmation found; asked-for check of current status (given events in the West Bank since October 2023) could not be completed within this pass's search budget. Treat opening-era details as solid, current operating status as unconfirmed.

## AIRCRAFT

### The Palestinian-Jordanian Airline Restaurant and Coffee Shop Al-Sairafi
Boeing|707|N/A|||707 airliner turned restaurant|fixed_wing|monoplane|civilian|commercial_transport|1961|Ex-Israeli-government-operated 707; purportedly flew PM Menachem Begin to the US in 1978 for the Egypt peace-treaty signing; retired with engines removed near Kiryat Shmona; bought in 1999 by Palestinian twin brothers Ata and Khamis al-Sairafi for USD 100000 and trucked in 13 hours (wings removed) to Wadi al-Badhan near Nablus; conversion stalled ~20 years (Second Intifada; checkpoints; COVID-19) before opening as a cafe/restaurant on 21 July 2021|N/A|Al-Sairafi Restaurant (Palestinian-Jordanian Airline Restaurant and Coffee Shop)|on_display|IL

## NOTES

### Palestine — what was searched and found
- English WebSearch (general web search WAS reachable this pass, contrary to
  the contract's default assumption — used it once Wikipedia searches for this
  topic came back empty): "Abu al-Sabaa brothers Boeing 707 Nablus airplane
  restaurant Al-Sawiya", "Palestinian Airport restaurant Nablus Boeing 707",
  "Abu al-Sabaa OR Abu Sbeih airplane restaurant West Bank Boeing 707",
  "al-Sairafi Boeing 707 restaurant Nablus 2024 2025 status", "Ramallah OR
  Bethlehem OR Gaza museum preserved aircraft airplane monument".
- Arabic Wikipedia (ar.wikipedia, `list=search`): `مطار فلسطيني نابلس طائرة`,
  `مطعم الطائرة السوية نابلس` — no article on the restaurant; Arabic Wikipedia
  appears not to cover this site at all (it is a commercial/human-interest
  story, sourced entirely to AP/wire-service English-language reporting and
  its syndication, not to an encyclopedia article in any language). Hebrew
  Wikipedia (he) was NOT reached this pass — time ran out to it; flagging as
  an open gap, not a checked zero.
- **Important discrepancy with the brief**: the brief names "the Abu Al-Sabaa
  brothers" and a location in "Jabal Al-Nar / Al-Sawiya," and describes the
  site as **two** Boeing 707s. Every source actually found (all English-
  language wire coverage, consistent across AP/Reuters syndication to VOA,
  Times of Israel, France24, Arab News, Seattle Times, Al Bawaba, Wings
  Magazine) describes **one** Boeing 707, owned by twin brothers named
  **Ata and Khamis al-Sairafi**, at **Wadi al-Badhan** near Nablus — a
  different name and a neighbouring but distinct location from what the brief
  specifies. I could not find any source for an "Abu Al-Sabaa" family or a
  second 707 near Nablus; either (a) the brief's naming is imprecise and
  refers to this same al-Sairafi aircraft, (b) there is a second, separate
  707-restaurant project this pass did not find, or (c) the brief conflated
  two different real projects. **Flagging for aggregation**: verify owner
  name and check whether a second airframe exists before finalizing the
  `aircraft_name`/`aliases` fields, and note the site name I used
  ("...Al-Sairafi") may need correcting or merging against whatever record
  the brief's source had in mind.
- Only one aircraft is confirmed by sourcing (a single fuselage), so AIRCRAFT
  lists one row, not two.
- **CURRENT STATUS UNCERTAIN, FLAGGED FOR AGGREGATION**: all sourcing dates
  to July–August 2021 (opening). No article after that date was found in this
  pass confirming the restaurant is still open, given the marked change in
  circumstances across the West Bank since October 2023 (increased
  checkpoints, settler violence, military operations in northern West Bank
  governorates including Nablus). Recommend a targeted check before import if
  currency matters, or import with `display_status: on_display` flagged low
  on recency.
- Prior/failed ownership: VOA reporting says the aircraft was retired by the
  Israeli government (operated ~1961–1993) then briefly owned by three
  Israeli business partners who themselves attempted and abandoned a
  restaurant conversion before selling to the al-Sairafi brothers in 1999.
  Coded `operator_country: IL` on that basis (the airframe's actual flying
  service was Israeli-government/Israeli-operated; no earlier airline history
  before that was found, so this is the operator, not merely the seller).
- EXCLUDED: **Yasser Arafat International Airport**, Gaza — destroyed by
  Israeli forces in 2001–2002; this is destruction of an active facility, not
  retention/display, and no aircraft is described as preserved there. Not a
  record.
- EXCLUDED: general search for museums in Ramallah, Bethlehem, and Gaza City
  turned up no aviation museum or preserved-aircraft holding (the "List of
  museums in Palestine" en.wikipedia article and general web search were
  checked; Gaza's heritage-site destruction coverage since Oct 2023, e.g. Al
  Jazeera "cultural genocide" report, discusses archaeology/heritage sites,
  not aircraft).
- Coordinates for the Wadi al-Badhan site were not published in any source
  found; left blank per the hard rule against inventing coordinates.

### Macau — what was searched and found
- zh.wikipedia (`prop=extracts`, exact titles): `澳門格蘭披治大賽車博物館`
  (Macau Grand Prix Museum — this title does not exist verbatim; the actual
  article is `大賽車博物館`, found via search: it is entirely about the motor
  race, no aircraft), `澳門科學館` (Macau Science Center — full extract read;
  no aircraft mentioned anywhere in exhibits, history, or building
  description), `澳門博物館列表` (List of Macau museums — full extract read;
  notably records that Macau's *only* historical link between aviation and a
  museum was a pre-WWII air-force aircraft hangar at 新口岸 (Novo Porto/NAPE)
  used from 1934 to store transferred maritime-and-fishery-museum exhibits —
  that hangar and its entire contents were destroyed by US air raids in 1945;
  nothing to preserve today).
- zh.wikipedia (`list=search`): `美麗號 飛機 劫機` (Miss Macao aircraft
  hijacking) and `澳門科學館 飛機` / `澳門博物館 飛機` (aircraft + museum) — no
  hits describing any preserved/displayed airframe in Macau.
- en.wikipedia (`prop=extracts`): `Miss Macao` — confirms the Catalina flying
  boat (Macau Air Transport Co., a Cathay Pacific subsidiary) hijacked 16 July
  1948 (the world's first commercial-aircraft hijacking) **crashed into the
  sea** with only one survivor; the airframe was never recovered. This is a
  crash/loss, not a retained-and-displayed record — EXCLUDED.
- pt.wikipedia and zh-yue (Cantonese) were budgeted but NOT reached this pass
  (rate-limit backoff consumed the time); this is an acknowledged gap, not a
  checked zero — Macau's unusually good Portuguese-language coverage makes
  this the single highest-value follow-up for a future pass.
- Taipa Houses and the Macau Museum (in the citadel of the old fortress) were
  not directly queried this pass (time-limited); both are house-museum /
  history-museum types with no indication from the museums-list overview
  extract that either holds an aircraft.
- **Conclusion**: no current aircraft record found for Macau. This should be
  treated as a **partial/incomplete search**, not a confident zero — the
  Portuguese-language and Cantonese sweeps the brief specifically called out
  as highest-value were not completed.

### Timor-Leste — what was searched and found
- WebSearch: "Timor-Leste Dili preserved aircraft monument museum wreck WWII
  Comoro airfield" → led to Pacific Wrecks (pacificwrecks.com), a
  detailed English-language wreck-documentation site (not Wikipedia, but the
  most authoritative source for this region's WWII aircraft).
- WebFetch of `pacificwrecks.com/airfield/timor/dili/index.html` and its
  linked `aircraft/a-26/dili.html`: records **one candidate** — a Douglas
  A-26 Invader (ex-Indonesian Air Force, post-war civil conversion) reported
  "parked at Dili Airport" **in the 1980s**, left sitting on its wheels after
  a mechanical failure. No registration/serial recovered. Crucially, the
  source itself gives **no evidence this was ever intentionally preserved,
  mounted, or presented** — it reads as an abandoned/derelict aircraft left
  where it stopped, with no more recent (post-1980s) sighting recorded on the
  page (last page update 2025 but no newer observation date given).
  **EXCLUDED per contract** ("a hulk in a scrap line" / stored-not-presented
  aircraft is explicitly not a record) — but flagged as an **uncertain call**
  for aggregation: if this airframe is still extant and visible from the
  airport grounds today, it could arguably still count as informally
  "displayed" simply by long-term visible presence; recommend a follow-up
  photo/Commons check before fully discarding.
- pt.wikipedia (`list=search`): `avião monumento Timor-Leste` — surfaced only
  a WWII Portuguese-victims memorial ("Monumento a vítimas portuguesas da 2ª
  Guerra Mundial em Timor-Leste," reported under restoration) with no aircraft
  component, and general WWII-paratrooper-history articles. No aircraft
  museum or monument hit.
- id.wikipedia (Indonesian) and tet.wikipedia (Tetum) were NOT reached this
  pass — acknowledged gap. Tetum Wikipedia is extremely small; Indonesian
  Wikipedia is large and was the more promising of the two for Indonesian-
  era airfield history at Comoro/Baucau — recommend for follow-up.
- **Conclusion**: no confirmed record. Treat as a partial search (Indonesian-
  language sweep outstanding) rather than an exhaustive zero.

### Bhutan — what was searched and found
- WebSearch: "Bhutan National Museum Paro preserved aircraft airplane
  display" — results are entirely general Ta Dzong/National Museum of Bhutan
  tourism pages (textiles, thangka, historic artifacts); no aircraft
  mentioned. (Search incidentally surfaced unrelated "Aircraft Museum
  Dhangadhi" and "TU 142 Aircraft Museum," both in Nepal/India, not Bhutan —
  confirms no Bhutan-specific aircraft museum exists in indexed sources.)
- dz.wikipedia (Dzongkha, `list=search`): ran a Tibetan-script query for
  "museum" (འགྲེམས་སྟོན་ཁང་). Dzongkha Wikipedia is very small (~thousands of
  articles); hits were the general Bhutan article, the National Museum
  article, and the Ta Dzong/Paro Museum article, plus unrelated foreign
  articles that happen to use the word "museum" — no aircraft content
  anywhere. Given the edition's size and the general-tourism-only English
  coverage, an aviation-specific record is very unlikely to exist and be
  unindexed.
- ne.wikipedia (Nepali) was NOT reached this pass (time). Given Bhutan has no
  air force and Druk Air is its sole operator (small, still-flying civil
  fleet, nothing retired/displayed known), this is a low-value follow-up.
- **Conclusion: documented zero**, consistent with the brief's own
  expectation ("Bhutan has no air force... Expect zero").
- Exact queries run (for the record, so they are not repeated): en WebSearch
  "Bhutan National Museum Paro preserved aircraft airplane display"; dz
  Wikipedia list=search on the Dzongkha word for "museum."

### Maldives — what was searched and found
- WebSearch: "Maldives National Museum preserved aircraft airplane display
  Male" — results are all general National Museum (Malé) tourism/history
  pages (pre-Islamic artifacts, sultanate relics, coral-stone carvings); no
  aircraft mentioned. The Maldives National Defence Force's air element only
  dates from 2020 and is a small, active, non-retired fleet — nothing to
  preserve yet.
- dv.wikipedia (Dhivehi) was NOT reached this pass — acknowledged gap (time
  spent on rate-limit backoff for the higher-priority Macau/Palestine/Timor
  queries). Dhivehi Wikipedia is a small edition; recommend a follow-up pass
  with a Thaana-script query for "museum"/"aircraft" before treating this as
  fully exhaustive, though the brief's own expectation of zero here is very
  likely correct given no air force and only a five-year-old small defence
  air element.
- **Conclusion: documented zero** (highly likely, but the native-language
  Dhivehi sweep is an outstanding gap rather than a completed check).

### Overpass/OSM sweep
Not run this pass for any of the five territories — the time budget was
consumed by Wikimedia rate-limit backoff (repeated 429s requiring 90-120s
waits between successful calls) and by the Palestine WebSearch/WebFetch
investigation, which was judged the higher-value use of the available budget
given the strength of that lead. This is a genuine gap against the contract's
method section, not a zero result — flag for a follow-up pass, particularly
for Macau (small dense urban area, good OSM coverage) and the Nablus 707 site
(to attempt to recover coordinates that no article source gave).

### Uncertain calls for aggregation (summary)
1. Palestine 707 restaurant — name mismatch (al-Sairafi vs. brief's "Abu
   Al-Sabaa") and single-vs-two-aircraft mismatch; current (2024-2026)
   operating status unconfirmed.
2. Timor-Leste A-26 at Dili — 1980s "parked" airframe, ambiguous whether it
   was ever a deliberate display; excluded here but flagged for a
   photographic/Commons check.
3. Macau — Portuguese and Cantonese language sweeps outstanding; treat the
   zero as provisional pending that follow-up.
4. Bhutan (Nepali) and Maldives (Dhivehi) — native-language sweeps in the
   specific small-population language not reached; zero is very likely
   correct but not fully exhaustive per the contract's method.

## Per-country site/aircraft counts
- Palestine: 1 site, 1 aircraft (confidence medium; status/name flagged for
  aggregation)
- Macau: 0 sites, 0 aircraft (partial search — pt/zh-yue outstanding)
- Timor-Leste: 0 sites, 0 aircraft (one excluded candidate — Dili A-26;
  id/tet sweeps outstanding)
- Bhutan: 0 sites, 0 aircraft (documented zero, ne.wikipedia outstanding)
- Maldives: 0 sites, 0 aircraft (documented zero, dv.wikipedia outstanding)
