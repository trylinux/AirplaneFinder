# Eurasia, the Balkans and Mexico — overnight sweep, 10 September 2026

One session, four waves, **36 countries**. Thirty-three of them were at **zero records**
when this started; Japan had one site and Ukraine three.

Evidence lives in the `research_*.md` dossiers beside this file in
`data/eurasia_sep2026/`, `data/eurasia_sep2026_w3/` and `data/eurasia_sep2026_w4/`.
Each one carries its own sources, corrections, exclusions and ranked open questions.
This file is the cross-cutting summary — what was learned that outlives any one country.

## What went in

**1,369 sites · 5,414 airframes.** All imported, all verified live, full suite green.

| Wave | Countries | Sites | Airframes |
|---|---|---|---|
| 1 — Europe core | Poland, Italy, Spain, Portugal, Netherlands, Belgium, Luxembourg, Czechia, Slovakia, Austria, Switzerland, Hungary | 590 | 2,373 |
| 2 — East Asia | Japan, South Korea, Taiwan, China | 259 | 1,383 |
| 3 — Balkans, Greece, Mexico | Greece, Serbia, Croatia, Slovenia, Bosnia, North Macedonia, Montenegro, Albania, Romania, Bulgaria, Moldova, Mexico | 235 | 817 |
| 4 — East Europe, Baltics, South and Central Asia | Ukraine, Belarus, Estonia, Latvia, Lithuania, Ireland, Pakistan, Bangladesh, Sri Lanka, Nepal, Kazakhstan, Uzbekistan, Kyrgyzstan, Tajikistan, Turkmenistan, Mongolia, Georgia, Armenia, Azerbaijan | 285 | 841 |

Largest single countries added: **Japan 257 sites / 1,383 airframes**, **Ukraine 118 /
410**, **Italy 129 / 477**, **Poland 95 / 479**, **Greece 93 / 227**, **Taiwan 59 / 166**.

## Two bugs in the pipeline, both of which were silently destroying data

**1. `build_from_research.py`'s filename slug folded to ASCII and dropped everything
else.** A museum named only in Cyrillic, Greek or Japanese produced an *empty* slug, so
fourteen Bulgarian and Macedonian sites all wrote to `_aircraft.csv` and overwrote each
other — **119 rows vanished with no warning, and the test suite passed**, because the one
surviving file was internally consistent. A second mode: two long names sharing their
first 40 slug characters collided the same way and cost two Taiwanese rows before it was
caught. Both are fixed — an empty fold now falls back to `site_<sha1>`, and any slug
already claimed by a different museum gets a hash suffix. **This would have hit the
Russian plinth pass hard**, where most site names are Cyrillic.

**2. `region` is a closed enum** — Africa, Asia, Asia-Pacific, Europe, Middle East, North
America, Oceania, South America. There is no Central America, Caribbean or Latin America
value. A research pass told to emit a geographic region name fails the museums import on
every row. Central America and Mexico file under North America; Cyprus files under Middle
East, matching the nine sites already there.

## The method that carried this sweep

**OSM Overpass is not a supplementary source. In any country whose monument culture is
not documented in English, it is the primary one**, and it should lead a pass rather than
follow it. `historic=aircraft` over a bounding box returns airframe-level nodes with
airframe-level coordinates — better than anything Nominatim will geocode — and mappers
routinely carry the type in `description`, the serial in `ref` or `inscription`, the
erection date in `start_date`, and a `check_date` as recent as April 2026. It produced
almost the whole of Poland's 63-site monument layer, 117 Italian locations, two Guatemalan
sites nothing else surfaced, and the great majority of the Balkans and Central Asia.

Practicalities, all learned the hard way and all worth writing into `METHODOLOGY.md`:

- **`overpass-api.de` is blocked by this environment's proxy — every time, in every
  wave.** Working mirrors, in rough order of reliability: **`maps.mail.ru`** (best
  coverage of the post-Soviet space and the only one that answered for Mexico, South
  Asia and Central Asia), **`overpass.kumi.systems`**, **`overpass.private.coffee`**.
- Send a real browser User-Agent and **POST the query from a file**, not inline.
- **Whether `area["ISO3166-1"="XX"]` works is mirror-dependent and the agents disagreed
  about it**, so try the area filter first and fall back to a bbox. It matters: a bbox
  pass for Romania was **42% contaminated**, sweeping in the entire Belgrade and Szolnok
  museum collections; the Ukraine sweep found only 74% of its 533 nodes were actually
  Ukrainian; the Pakistan bbox was mostly India and Afghanistan. **Reverse-geocode every
  node and verify the country either way** — this pass moved three "Croatian" airframes
  to Slovenia and caught two Amritsar traps that would have been filed as Pakistani.
- A broad name-regex query over a whole country will time out. Narrow by tag first.
- Nominatim 403s through this proxy intermittently; **`photon.komoot.io`** is a working
  substitute for reverse geocoding.

**National-language per-type survivor lists are the other half of the method.** Polish
Wikipedia's per-type articles (`MiG-21`, `TS-11`, `Il-28`, `I-22 Iryda`) list museum plus
tactical number plus construction number airframe by airframe and opened 28 Polish sites.
Chinese Wikipedia's `中華民國空軍F-104` table did the same for Taiwan. English Wikipedia's
survivor lists have **no Central American entries at all** and **no per-type 保存機
sections for any JASDF jet** — that was checked directly, they do not exist.

## Sources that carried whole countries and belong in the hierarchy

- **`用廃機ハンターが行く！` (wrecks.hatenablog.com)** — a dated, revision-tracked Japanese
  national census with two cross-checkable axes: 248 per-prefecture site articles and ~90
  per-type national censuses, with visit dates as recent as **19–23 April 2026**. It is
  the functional equivalent of a national register and it produced most of Japan's 632
  base and civic airframes.
- **`flotilla-aerea.com`** — airframe-level Salvadoran inventory, revised through 2025.
- **`iar93.ro`** — all 31 surviving IAR-93s with exact factory roll-out *dates*. This is
  the rare source that makes `year_built` sourceable rather than inferred.
- **`aviahistory.ucoz.ru`** — a Russian monument registry with construction numbers,
  factory dates and write-off dates, and honest enough to mark scrapped airframes, which
  let the Central Asia pass *exclude* six confirmed losses. Transports and trainers only;
  its sister `aviamonuments.ru` likely covers the fighters and is proxy-blocked here.
- **`spottingmode.com/wro`** — already in the hierarchy, and it carried Greece: 245 Greek
  locations with c/n, status codes and last-noted dates, two thirds of them 2025–26.
- **`kozterkep.hu`**, Hungary's public-art register — erection dates, construction numbers
  and service histories for monument aircraft.
- **Museum-published structured feeds, which are commoner than assumed.** Kraków runs
  WordPress with a public `eksponaty` REST endpoint (725 records, 191 airframes). Dęblin's
  Yoast sitemap puts the tactical number in every page title. Volandia exposes an
  undocumented `velivolo-sitemap.xml` with 79 per-aircraft pages. `collectie.nmm.nl` has a
  `subcollection=vliegtuigen` facet. **Always probe for one before scraping.**
- **Wikimedia Commons filenames and category structure as a data source in their own
  right** — they recovered ~24 PLAAF tactical numbers at Datangshan that appear in no text
  source in any language, and the Riga museum's move was *proved* by a Commons category
  split into `(Riga airport)` and `(Skulte)`.

## Currency findings — the ones that would have poisoned the data

Every one of these contradicts what English directories still say:

- **China Aviation Museum, Datangshan closed to the public on 9 October 2025** and is
  relocating to Changchun with 376 aircraft, target 2027. Recorded `restricted`.
- **Aeronautical Museum Belgrade has been closed for over a year**, facade damaged,
  collection deteriorating outdoors, reconstruction contracted to 2027. All 210 rows carry
  the closure; its own domain now redirects to parked hosting.
- **Muzeul Naţional al Aviaţiei Române (Pipera) has been shut since 2023** for a EUR 20m
  rebuild and stays shut until at least 2027.
- **The State Aviation Museum Kyiv is closed at Medova 1** and working from a hangar on
  the KAI campus.
- **The Minsk aviation museum moved** — Borovaya closed 20 Oct 2023, reopened at Lipki
  19 Oct 2024. ru.wikipedia's coordinate points at the housing estate built on the old
  airfield.
- **Riga Aviation Museum moved to Skulte on 24 August 2021** — English Wikipedia says 2022
  and is wrong. It was not evicted out of existence.
- **The Irish Air Corps Museum shut in 2024**, its collection went on loan to Shannon, and
  it reopened to the public for the first time on **27 August 2026** — two weeks ago.
- **Letecké muzeum Koněšín lost its site on 30 June 2026** and was cleared. ~25 airframes
  including unique prototypes (XL-29 003, XL-39 007, XL-410 OK-020, Mi-24D 0103) are
  **unaccounted for**. This is the single most urgent open item in the sweep.
- **VHM Piešťany reopened its rebuilt exhibition on 8 September 2026 — two days ago.**
  Recorded as a site with zero aircraft rather than importing a stale roster.
- **Tokorozawa is closed Sept 2025 – March 2027 with three airframes scheduled for
  scrapping**; Aichi closed June 2026 – Jan 2027; Old Car Center Kudan lost all fifteen of
  its airframes in March 2025.
- **Two Japanese removals are imminent**: the Matsudo S-62 goes in **early October 2026**,
  and the Fukuoka Kaizuka Heron — the last in Japan — ends its display **31 March 2027**.

## `aviationmuseum.eu` failed again, measurably, in four new ways

Its record in `PROJECT_STATUS.md` was already long. Add: an **F-5E invented** at the Museo
del Aire de Honduras against the museum's own list and the enabling Congress decree; a
**Guatemala City coordinate ~11 km west** of the site; **three Austrian and Hungarian
coordinates wrong by 11, 11 and 21 km, all drifting west**; and **column-shifted serial
tables at Dübendorf, Luzern and Košice** — it pairs a Mirage IIIRS with a Hunter's serial,
a PC-9 with an F-5E's, and hands a Z-37 Čmelák an Italian MM serial. Its Costa Rica,
Nicaragua and Panama pages are empty or stubs. Every serial from those tables was
discarded.

## Judgment calls worth knowing about

- **Repainting is endemic and is the norm, not the exception, for monument aircraft.**
  Japan's base displays alone have 16 airframes wearing a serial that is not theirs.
  Italy's monuments usually wear a *unit code* and no MM serial at all — and a unit code is
  reassigned constantly, so it is not an identity. Guatemala's Mustang wears "336" over an
  earlier "360" and no source agrees which is real. In every case the true identity went in
  `tail_number`, the worn marking in `aliases`, and the reason in `description`; where the
  true identity was unknown, `tail_number` was left **blank**. Importing the paint would
  have flattered the serial-coverage numbers and corrupted the airframe records.
- **`Unidentified` + a descriptive model** is the house treatment where a site is well
  sourced and the airframe genuinely is not, following the two autogyros already in the
  database. Roughly 90 rows across the sweep. The alternative — dropping the row — loses a
  real site; the other alternative, guessing a type, is worse than both.
- **Albania's fleet is Chinese**, and is recorded that way: Shenyang J-6/F-6 and
  Shijiazhuang Y-5 with the Chinese builder as `manufacturer`, MiG-19 and An-2 only as
  aliases. The same rule gave Czechoslovak licence types their own designations
  (S-102, S-103, CS-102, S-105, B-33, Avia 14, S-199, CS-92, C-11) and Polish types theirs
  (Lim-1, Lim-2, Lim-5, Lim-6, SBLim).
- **Storage and disposal are not display.** Excluded with reasoning: Albania's ~50 stored
  airframes at Kuçovë and the Gjadër cavern fleet; the ~35-airframe Bentivoglio scrapyard
  in Rome; PS Aero Baarlo's dealer stock (16 airframes including the first Caravelle
  built); the Pápa aircraft store, cleared and cut up per an October 2025 source; the
  Nicosia buffer-zone airliners, which confirms the existing adjudication in
  `MIDDLE_EAST_STATUS.md`. Eight "MiG-21/MiG-23" nodes at Nadarzyce were rejected as
  **bombing-range targets**.
- **Conversions and unusual hosts are records** where publicly presented. Japan alone
  contributed kindergarten and clinic rooftops, roadside stations, a love hotel, an eel
  restaurant and an airsoft field. Costa Rica is almost entirely hotel and restaurant
  conversions.

## Deferred, deliberately — pick these up first

- **Cyprus (11 airframes) and the Ulster Aviation Society (53 airframes) were researched
  and NOT imported.** Both duplicate existing database sites under different names — every
  proposed Cypriot site maps to one of the nine already recorded (Özgürlük Milli Parkı *is*
  Alsancak National Freedom Park; the Cengiz Topel Monument *is* the Lefke F-100D), and
  Ulster already holds 52 airframes. They need a diff against the live records, not an
  import. The rows are in `data/eurasia_sep2026_w3/research_greece_cyprus.md` and
  `data/eurasia_sep2026_w4/research_baltics_ireland.md`.
- **Seven unresolved one-airframe-two-places conflicts** are listed in
  `data/eurasia_sep2026/UNRESOLVED_CONFLICTS.txt`. The row was kept at the
  better-evidenced site and dropped at the other rather than silently duplicated. They are
  Yak-11 4C-AH (Zeltweg vs Graz), UH-1H 41705 (Kasuminome vs Sendai — 2.5 km apart, two
  genuinely different camps), UH-1H 41708 (Jinmachi vs Yamato — different prefectures),
  Cessna 150 JA3187 (Chofu vs Chikusei), Buhwalho 1007 (Seoul vs Cheongju), TS-11 721
  (Dęblin vs Stalowa Wola) and T-37C 2420 (Sintra vs Alverca).
- **17 Ukrainian sites in occupied or annexed territory were imported** with
  `confidence: low` and the occupation stated in the description. **This is a policy call
  that belongs to Zach, not to this session** — they are trivially removable as a group if
  the answer is that the database should only carry what a visitor can reach.
  **Vovchansk was dropped**: its monument should be presumed destroyed after the 2024
  offensive, and `display_status` has no honest value for that.

## The `operator_country` field is now earning its keep

`uq_airframe` is `(full_designation, tail_number, operator_country)`, the builder carries
the column, and this sweep populated it on essentially every row. It was needed
immediately: a Dutch MiG-21PFM bort "47" collided with **Monino's** MiG-21PFM "47", whose
`operator_country` was blank. Fixed by setting Monino's to `RU` — a Monino open-park
airframe is Soviet Air Force by provenance — after which the Dutch row imported cleanly.

**That is the shape of the remaining work.** Every airframe imported before the column
existed still has it blank, and blank does not collide with blank in MySQL, so the
protection only holds where both rows carry a code. Poland, Hungary, Romania, Bulgaria,
Ukraine, Belarus and Central Asia are now full of two- and three-digit bort numbers that
are only kept apart by this field. **Backfilling `operator_country` across the pre-existing
20,000 rows — starting with Russia's 1,072 — is the highest-value data-quality job left in
the project**, and it should happen before the Russian plinth pass, which is almost
entirely bort-numbered airframes.

## Ranked open items

1. **Letecké muzeum Koněšín's ~25 airframes are unaccounted for** since the site was
   cleared on 30 June 2026, including six unique Czech prototypes. Time-critical.
2. **Backfill `operator_country`** on the pre-existing rows (see above).
3. **Honduras outside Tegucigalpa, and Pakistan's base and town-park layer, are
   *unsearched* zeros, not well-searched ones.** Both need a local-language press pass —
   Spanish for Honduras, Urdu (`طیارہ یادگار`) for Pakistan.
4. **`lotnictwo.net.pl`'s "Muzea i pomniki lotnicze" gallery** has captions of the form
   "[Pomnik] City, Type Serial" across at least nine pages and would close most of
   Poland's blank `tail_number` fields. Unreachable here only because its TLS chain is
   broken; a browser session would harvest it. Same story for `swissair00.ch` (weak TLS
   key) and `museocaproni.it`, which between them would roughly double the Swiss monument
   count and put serials on ~60 identity-less Italian airframes.
5. **The AAA "Aviatori d'Italia" per-section directory** at assoaeronautica.it — this pass
   confirmed section-held airframes at five sections; walking the ~200 sections would
   likely add 40–80 Italian sites, and ~45 further i-f-s F-104 locations are named and
   awaiting corroboration.
6. **Two phone calls with unusually high yield**: the Aeronautical Museum Belgrade
   (+381 11 2670992) would re-status 210 rows at once; the Fundación Museo del Aire de
   Honduras (+504 9992 4543) closes a serial conflict, an unverified F-5E claim and
   several coordinates.
7. **Coordinates are blank on a large minority of sites**, deliberately — a town or
   air-base centroid dressed up as a fix is worse than nothing. Poland is the worst case:
   31 of 32 museum sites have none.
8. **A WebSearch quota exhausted mid-sweep** and every later agent worked without general
   web search, falling back to the Wikipedia and Commons APIs, Overpass, Nominatim and
   direct fetches. That worked better than expected but it specifically cost the
   Greek-, Spanish-, Romanian-, Bulgarian- and Korean-language press passes. South Korea
   in particular (22 sites, almost every `tail_number` blank) is thin for that reason and
   deserves a re-run.
9. **Mongolia is genuinely under-searched** and needs a Mongolian speaker. Tajikistan
   returned zero OSM objects nationwide. Neither zero should be trusted.
