# West Africa zero-record sweep

Countries: Benin, Cape Verde, Gambia, Guinea, Liberia, Mauritania, Sierra Leone,
Togo, Western Sahara. `region` = `Africa` for all.

## Method actually used

- **Primary source: spottingmode.com/wro** (per-location pages, not the country
  list page, which collapses multi-airframe bases into one row). Fetched with
  `curl --ciphers "DEFAULT@SECLEVEL=1"` (WebFetch indeed fails on it — confirmed).
  The country list page (`/wro/list/`) is a form shell with no data; the actual
  per-country listing lives at `/wro/<country_slug>/` (slug = lowercase country
  name, spaces as `%20` or `_`, e.g. `/wro/sierra_leone/`, `/wro/cape_verde/`,
  `/wro/western_sahara/`). Each row there is a *location*; I then opened every
  `/wro/location/<id>/` page to read the `main_table` (registration, c/n, type,
  operator country, service, **status**, remarks). Status codes actually seen in
  this region: `pre` = Preserved, `std` = Stored, `dlt` = Derelict, `dum` =
  Dumped. I applied the display-vs-derelict test to the STATUS FIELD, not to the
  location description: only `pre` was treated as a presentation candidate;
  `std`/`dlt`/`dum` were treated as NOT meeting "deliberate retention plus public
  presentation" and excluded (a "Stored" military hulk behind a base fence is not
  a displayed record).
- **MediaWiki API** (`en`, `fr`, `es`, `pt`) — severely rate-limited for nearly
  this entire session ("You are making too many requests to the API" on almost
  every `action=query` call, including `search` and `prop=extracts`, across
  en/fr/es/pt, with successful calls only after ~90–180s backoffs). This capped
  how much native-language searching I could actually complete — see per-country
  notes below for exactly what ran vs. what is still open. Direct `/wiki/<title>`
  page fetches (not the API) were NOT rate-limited and were used as a workaround
  where I already had a specific title to check.
- **OSM Overpass**: ran one combined query across all 9 countries'
  `ISO3166-1` areas for `historic=aircraft`, `memorial=aircraft`, and
  `aeroway=gate_guardian` via `maps.mail.ru`'s Overpass mirror (succeeded on the
  first mirror tried). **Result: 0 elements.** Per the brief, this is explicitly
  **not evidence of absence** for this region — OSM coverage of West Africa is
  extremely thin — and should not be read as a confirmed zero on its own.
- Wikidata SPARQL and Commons category search were **not** reached given the
  MediaWiki rate-limiting above; this is a real gap, not a completed zero, for
  every country below except where a Commons/Wikidata check is explicitly noted.

## SITES

### Conakry MiG-17 (Guinea)
name: Preserved MiG-17F, Conakry
city: Conakry
state_province:
country: Guinea
postal_code:
region: Africa
address:
website:
access_type: restricted
latitude: 9.58536625
longitude: -13.60779953
source: spottingmode.com/wro location 21125 (https://www.spottingmode.com/wro/location/21125/) — single airframe, status field "pre" (Preserved), last updated 30 Oct 2018
confidence: low-medium. Only source found is spottingmode's own status classification; I could not corroborate with Wikipedia/Commons/Wikidata (MediaWiki API was rate-limited for essentially this whole session — see notes). No photo, no placard/plinth description recorded on the source page. "Preserved" per this source is a formal step above "Stored," so it is a genuine record candidate, but I cannot independently confirm PUBLIC presentation (vs. deliberately kept but fenced off on a Guinean AF base, which would fail the display test). Evidence dated 2018.

### Cotonou TriStar (Benin)
name: Preserved Lockheed TriStar, Cotonou
city: Cotonou
state_province:
country: Benin
postal_code:
region: Africa
address:
website:
access_type: restricted
latitude: 6.34769583
longitude: 2.37984014
source: spottingmode.com/wro location 8712 (https://www.spottingmode.com/wro/location/8712/) — reg 9L-LFB, c/n 193P-1156, ex Sierra Leone civil register, status "pre", last updated 15 Jan 2016
confidence: low. Same caveat as above: "pre" status from spottingmode only, no corroborating source found (rate-limited before I could check Commons/Wikidata for this registration). A derelict ex-Sierra Leone Airlines TriStar sitting at Cotonou is plausible (SLA/related carriers had TriStars seized/abandoned around West Africa in the 1990s-2000s) but I have no source describing it as presented to the public rather than simply parked and retained. Evidence over 10 years old (2016) — flag for re-verification.

### Cotonou "Petrel" (Benin)
name: Preserved Benin Air Force "Petrel", Cotonou
city: Cotonou
state_province:
country: Benin
postal_code:
region: Africa
address:
website:
access_type: restricted
latitude: 6.35143280
longitude: 2.38285589
source: spottingmode.com/wro location 16138 (https://www.spottingmode.com/wro/location/16138/) — reg TY-AAM, c/n 049, Benin Air Force, status "pre", last updated 25 May 2025
confidence: low. Type identity is UNCERTAIN — spottingmode's own "Plane type" field just says "Petrel", which I could not resolve to a real manufacturer/model despite trying the spottingmode types database and general web lookups (both unsuccessful in the time available; general web search was effectively unavailable this session per the brief). Do not import a manufacturer/model guess for this — see AIRCRAFT section, which uses "Unidentified".

## AIRCRAFT

### Preserved MiG-17F, Conakry
Mikoyan-Gurevich|MiG-17|F|715||||fixed_wing|monoplane|military|fighter||on Air Force base at Conakry; identified only by tail number 715; source records it as "Preserved" status, distinct from the several "Stored" MiG-21bis/Mi-25 airframes at the other Conakry location; presentation to the public NOT independently confirmed|MiG17|Musée National de Sandervalia (unconfirmed link)|on_display|GN

### Preserved Lockheed TriStar, Cotonou
Lockheed|L-1011|-1|9L-LFB|TriStar|||fixed_wing|monoplane|civilian|commercial_transport||ex Sierra Leone civil register; airframe c/n 193P-1156; source records "Preserved" status as opposed to derelict/dumped; presentation to the public NOT independently confirmed; likely a former Sierra Leone-linked airline TriStar that ended up at Cotonou|L1011;TriStar|Cotonou-Cadjehoun airport area (unconfirmed)|on_display|SL

### Preserved Benin Air Force "Petrel", Cotonou
Unidentified|Light aircraft (recorded locally as "Petrel")||TY-AAM||||fixed_wing||military|utility||Type identity unresolved; source lists "Plane type" as simply "Petrel" which does not match a manufacturer/model I could confirm; c/n 049; Benin Air Force; "Preserved" status per source|Petrel|Cotonou-Cadjehoun (unconfirmed)|on_display|BJ

## NOTES

### Per-country searches and results

**Liberia** — Checked spottingmode `/wro/liberia/`: 2 locations, both "Roberts
Field, Liberia". Both airframes are civil, status `std` (Stored): a small
prop-type at 6.24722195N 10.35041523W, and a Gulfstream G.1159-SP (N747JX, c/n
33) at 6.23819447N 10.35546589W, last updated 2020, remarks note it was "parked
outside by 2019, US registration cancelled" — i.e. an abandoned business jet,
not a presented exhibit. **EXCLUDED as derelict/stored, not displayed.**
English Wikipedia searches run: "Liberia preserved aircraft monument" (no
relevant hits — dominated by unrelated "Liberia" ship-flag hits), "National
Museum of Liberia aircraft" (no hits — surfaced only DHC-4 Caribou fleet history,
not a museum record), and a direct fetch of `en.wikipedia.org/wiki/National_Museum_of_Liberia`
which 404s (no such article; the actual article, if any, may be titled
differently — NOT exhaustively checked due to API rate-limiting). Did not reach
Wikidata/Commons for Liberia. **Well-searched zero for the Robertsfield/Spriggs
Payne "graveyard" candidates specifically** (confirmed derelict, not a record);
the National Museum of Liberia itself is an **open gap**, not a confirmed zero.

**Sierra Leone** — spottingmode `/wro/sierra_leone/`: 1 location,
"Freetown-Lungi, Sierra Leone" (8.62029552N 13.20031261W), a single L-410UVP
(reg 9L-LBN, c/n 851337, civil), status `dlt` (Derelict). **EXCLUDED.** No
Hastings-airport entries appear in spottingmode's per-location Sierra Leone list
at all (the Mi-24s/An-12s the brief flags may not be tracked by this source, or
may be filed under a different location name I did not find). Direct fetch of
`en.wikipedia.org/wiki/Sierra_Leone_National_Museum` succeeded (200) and its
text has no mention of aircraft, airplane, or plane. **Documented zero for the
National Museum article as it stands on English Wikipedia** (checked 2026-09-10).
Did not get a working native-source pass on Hastings specifically before running
out of API budget — flag as open, not confirmed zero.

**Togo** — spottingmode `/wro/togo/`: 9 locations across Lomé (6 locations) and
Niamtougou (3 locations). All statuses recorded are `std` (Stored), `dlt`
(Derelict) or `dum` (Dumped) — an An-26 (dum), 2x MiG-23MLD (one dlt, ex Côte
d'Ivoire tail), a PA-31, a Beech 200/Puma/Alouette III set (all std), 2x
Fokker F.28-1000 (std), a DC-8-62H (std, ex Togo government), and at Niamtougou
a small twin prop, a DC-8 (std, military), and 4x MB-326 (no status recorded /
empty rows). **None reach "pre" — all EXCLUDED as stored/derelict/dumped, none
independently corroborated as displayed.** French Wikipedia: fetched
`Musée national du Togo` via REST summary/extract — it is a **maritime** museum
housed in the Palais des Congrès, no aviation content
("musée maritime, Togo" / installed in the congress-palace building — no
aircraft mentioned). **Documented zero for that specific museum** (checked
2026-09-10). Did not reach a working `fr.wikipedia.org` `action=query&list=search`
pass for "Togo avion musée monument" combined query (rate-limited, retried once
successfully on a narrower query that returned no aviation hits). Base displays
at Lomé-Tokoin (military side) and any *avion monument* in town were **not
independently checked beyond spottingmode** — open gap.

**Benin** — spottingmode `/wro/benin/`: 6 locations at Cotonou. Two are `pre`
(Preserved) — the TriStar and the "Petrel" above, both reported as SITES.
The rest are `std` (Stored): 2x Agusta A.109BA (military, one location), an
HS.748-2A (TY-21A, military; description also mentions a DHC-6 at the same
location but only the HS.748 row was populated in the source table), 2x more
A.109BA/AS.350B rows, and an unidentified small prop/"ultra light?" with no
status recorded. **EXCLUDED, stored not displayed, except the two `pre` rows
above.** French Wikipedia: fetched `Musée Honmè` (royal palace museum at
Porto-Novo, ethnographic/historical, no aircraft mentioned) and searched
"Bénin avion monument musée" (no relevant hits) and "Fondation Zinsou avion" (no
relevant hits — surfaced only unrelated Bénin political/history articles).
**Documented zero for Musée Honmè and for a general "avion monument" search on
frwiki** (checked 2026-09-10). Did not reach a dedicated check of the Fondation
Zinsou's own site or of Cotonou-Cadjèhoun base displays beyond spottingmode.

**Guinea** — spottingmode `/wro/guinea/`: 4 locations at Conakry. One is `pre`
(the MiG-17F above, reported as SITES). The rest are `std`/`dlt`/`dum`: 3x
Mi-25, 3x MiG-21bis, and an An-12B (Tajik civil) all `std` at one location; an
HS.748 (dlt) and Gulfstream (dum) at another; an MH.1521M (dum, French civil)
at a third. **EXCLUDED except the one `pre` MiG-17F.** French Wikipedia search
"Guinée avion monument musée Sandervalia" surfaced "Aéroport international
Ahmed-Sékou-Touré" and "Camp Camayenne" (a former internment camp, no aviation
content) — neither article mentions a preserved aircraft or the Musée National
de Sandervalia by name in a way that ties to aviation. English Wikipedia search
"Guinea Air Force MiG-17 monument" returned no relevant hits (all noise: generic
MiG-17/F-86/Mi-24 articles). **The Musée National de Sandervalia itself was not
directly checked** (no article found under an obvious title within the rate
budget) — open gap, not a confirmed zero for that specific museum.

**Mauritania** — spottingmode `/wro/mauritania/`: 2 locations. Atar
(20.50268555N 13.04856873W): a Harbin Y-12-II (5T-MAD, no status shown in one
row) and an AB.205A (5T-MAB, Mauritania AF, `std`). Nouakchott
(18.29848099N 15.99271393W): an L-29 and a UH-1 per the location description,
but only "std" rows were retrievable in the plane table for that page. **All
EXCLUDED as stored, not displayed.** Direct fetch of
`en.wikipedia.org/wiki/National_Museum_of_Mauritania` succeeded (200); grepped
the full page text for "aircraft"/"airplane"/"plane" — **no hits**.
**Documented zero for the National Museum of Mauritania on English Wikipedia**
(checked 2026-09-10). French search "Mauritanie avion monument musée" turned up
only the unrelated "Nord 2501" (Noratlas) article and general French-aviation
history pages — no Mauritania-specific aviation-monument hit. Arabic-language
search was **not reached** (API budget exhausted) — this is a real gap for
Mauritania specifically, since the brief calls for French AND Arabic.

**Cape Verde** — spottingmode `/wro/cape_verde/`: 1 location, Palmeira
(16.76369858N 22.98835182W), a Cessna 650 Citation III (OE-GIZ, c/n 650-7070,
Austrian civil), status `dlt`, remarks "fuselage only". **EXCLUDED, wreck
fragment, not displayed.** No Sal (Amílcar Cabral) or Praia entries appear in
spottingmode's Cape Verde list at all, despite Sal's known history as a
Cold-War-era refueling stop — this source appears to have essentially nothing
for Sal. Checked `en.wikipedia.org/wiki/Amílcar_Cabral_International_Airport`
and `en.wikipedia.org/wiki/Sal,_Cape_Verde` directly: no mention of a preserved
or displayed aircraft (the airport article only mentions generic maritime-patrol
aircraft basing and a photo of a generic silhouette icon, not a preserved
airframe). **Documented zero for both articles on English Wikipedia** (checked
2026-09-10). Portuguese-language search ("Cabo Verde avião monumento museu")
was attempted but returned only unrelated Brazil-aviation-history hits (João
Ribeiro de Barros, Santos Dumont, Catetinho) — no Cape Verde hit. Museu da
Tabanka / Museu Municipal (Praia/Sal) were **not individually checked** by
direct article title — open gap.

**Gambia** — spottingmode `/wro/gambia/`: 3 locations at Banjul. One is `dum`
(a North American Sabre 60, N103TA, `dum`) — **excluded**. The other two have
mixed/`std` rows: an Ilyushin Il-62MK (C5-GNM, Gambian government, `std`,
remarks "Removed") and a Sukhoi Su-25 (`.../81bl`, Gambia AF, `std`, remarks
"Removed") at one location; a Boeing 727-1H2 (C5-GOG, government, `std`) and
another 727-95 (C5-GAF, government, `std`) at the third. "Removed" in the
remarks plus `std` status reads as these having been taken away from public
view/scrapped rather than presented — **all EXCLUDED**. Checked
`en.wikipedia.org/wiki/Gambia_National_Museum` directly (200): grepped for
aircraft/airplane/plane — the only hits were unrelated citation boilerplate
(a Lonely Planet URL for Banjul sights). **Documented zero for the National
Museum of The Gambia on English Wikipedia** (checked 2026-09-10).

**Western Sahara** — spottingmode `/wro/western_sahara/`: 1 location, "Sahara
Desert, Western Sahara" (22.63059044N 13.23743248W), an Avro Shackleton MR.3
(reg 1716, c/n 1526, **South African Air Force**), status `dlt` (Derelict).
This is a South African military aircraft lost/downed in the Sahara — an in-situ
wreck, not a presented exhibit. **EXCLUDED as an in-situ wreck**, consistent
with the brief's warning about wrecks-lying-where-they-crashed. I treated this
neutrally: it is factually a South African aircraft loss recorded by
coordinates inside Western Sahara, and I am not asserting a political status for
the territory in recording that fact. French-language search ("Sahara
occidental avion monument") surfaced only "Tifariti" (the Polisario-proclaimed
SADR capital) — fetched the Tifariti article directly: it describes the town's
history and its role as a wartime stronghold/military base (1976-1991) and now
mostly in ruins, with no mention of a war museum or preserved aircraft/equipment
display. Spanish-language search ("Sahara Occidental museo guerra avión") also
returned no relevant hit (only generic Sahara/Legión Española/Cabo Juby
history). **This is a documented zero for Western Sahara** based on the sources
reached: no verifiable preserved-aircraft or aviation-museum record found in
French, Spanish, or the one Arabic-title check attempted implicitly via
Wikidata/Commons (not reached). Given the sensitivity flagged in the brief, I
am reporting this as a zero rather than guessing, and explicitly noting that a
Polisario or Moroccan war-trophy/equipment display (captured hardware) may
exist and simply wasn't found by these searches — this should be treated as an
open gap, not a hard negative, given how little of the Arabic-language web was
actually reachable this session.

### EXCLUDED (full list, with reasons)

- Roberts Field, Liberia — small prop (std) + Gulfstream G.1159-SP N747JX (std,
  "parked outside by 2019, US registration cancelled") — abandoned civil
  aircraft, not presented.
- Freetown-Lungi, Sierra Leone — L-410UVP 9L-LBN (dlt) — derelict.
- Lomé/Niamtougou, Togo — An-26 (dum), 2x MiG-23MLD (dlt/std, one an ex-Côte
  d'Ivoire tail), PA-31 (no status), Be.200/Puma/Alouette III (std), 2x F.28
  (std), DC-8-62H (std), small twin prop (no status), DC-8 at Niamtougou (std),
  4x MB-326 (no status) — all stored/derelict/dumped military and civil
  airframes at operational or semi-operational bases, none presented.
- Cotonou, Benin — 2x A.109BA + AS.350B (std), HS.748-2A TY-21A (std),
  small prop/ultralight (no status) — stored on Air Force ramp, not displayed.
- Conakry, Guinea — 3x Mi-25 + 3x MiG-21bis + An-12B (std), HS.748-2/228 (dlt),
  Gulfstream N139CF (dum), MH.1521M (dum) — stored/derelict/dumped.
- Atar/Nouakchott, Mauritania — Y-12-II, AB.205A (std), L-29, UH-1 (std) —
  stored on Air Force ramps.
- Palmeira, Cape Verde — Cessna 650 fuselage (dlt) — wreck fragment.
- Banjul, Gambia — Sabre 60 (dum), Il-62MK (std, "Removed"), Su-25 (std,
  "Removed"), 2x B727 (std) — stored/dumped, "Removed" remarks suggest taken
  out of any public view.
- Sahara Desert, Western Sahara — Avro Shackleton MR.3 (South African AF, dlt)
  — in-situ wartime wreck, not recovered or presented.

### Uncertain calls for the aggregation step

1. All three `pre`-status spottingmode entries (Conakry MiG-17F, Cotonou
   TriStar, Cotonou "Petrel") are reported as SITES/AIRCRAFT above but with
   LOW-MEDIUM confidence: spottingmode's "Preserved" classification is the best
   available signal that these are deliberately retained rather than simply
   abandoned, but I found **no independent corroboration** (photo, article,
   museum listing) that any of the three is actually presented to the public
   the way the contract's "record" definition requires. Aggregation should
   weigh whether a single-source "Preserved" tag is enough to import, or
   whether these need to be held pending a photo/second source.
2. The "Petrel" type at Cotonou (TY-AAM) is a genuine identification gap, not a
   guess — I could not resolve what aircraft type this actually is. Flagged as
   `Unidentified` per the contract's rule rather than dropped.
3. Guinea, Mauritania, and Cape Verde all have real native-language (French /
   Arabic / Portuguese) search work that was cut short by MediaWiki API
   rate-limiting for most of this session. These should not be treated as
   fully exhausted zeros — only the specific queries listed per-country above
   were completed.

### Well-searched zeros (exact queries run — do not repeat these)

- en.wikipedia search: "Liberia preserved aircraft monument"
- en.wikipedia search: "National Museum of Liberia aircraft"
- en.wikipedia direct fetch: `Sierra_Leone_National_Museum` (text-scanned for
  aircraft/airplane/plane — none)
- en.wikipedia direct fetch: `Gambia_National_Museum` (text-scanned — none)
- en.wikipedia direct fetch: `National_Museum_of_Mauritania` (text-scanned —
  none)
- en.wikipedia direct fetch: `Amílcar_Cabral_International_Airport` and
  `Sal,_Cape_Verde` (text-scanned — none)
- en.wikipedia search: "TriStar Cotonou Benin"
- en.wikipedia search: "Guinea Air Force MiG-17 monument"
- fr.wikipedia REST summary/extract: `Musée national du Togo` (maritime museum,
  no aviation)
- fr.wikipedia extract batch: `Musée Honmè`, `Camp Camayenne`, `Tifariti`
  (none aviation-related)
- fr.wikipedia search: "Bénin avion monument musée"
- fr.wikipedia search: "Fondation Zinsou avion"
- fr.wikipedia search: "Guinée Conakry avion monument musée Sandervalia"
- fr.wikipedia search: "Mauritanie avion monument musée"
- fr.wikipedia search: "MiG-17 Conakry musée"
- fr.wikipedia search: "Sahara occidental avion monument"
- pt.wikipedia search: "Cabo Verde avião monumento museu"
- es.wikipedia search: "Sahara Occidental museo guerra avión"
- OSM Overpass (maps.mail.ru mirror): combined query for
  `historic=aircraft`/`memorial=aircraft`/`aeroway=gate_guardian` across
  area["ISO3166-1"] = LR, SL, TG, BJ, GN, MR, CV, GM, EH — **0 elements
  returned; not evidence of absence, per the brief's own caveat about OSM
  coverage in Africa.**

### Not reached (genuine gaps, flag for follow-up, not zeros)

- Wikidata SPARQL and Wikimedia Commons category searches for any of the 9
  countries (e.g. "Category:Aircraft in Guinea", "Category:Aircraft in Benin")
  — MediaWiki rate-limiting prevented running these this session.
- Arabic-language search for Mauritania and Western Sahara (both explicitly
  requested by the brief) — not run.
- Musée National de Sandervalia (Guinea) — not directly checked by article
  title.
- Musée da Tabanka / Museu Municipal (Cape Verde, Praia/Sal) — not directly
  checked by article title.
- Lomé-Tokoin and Cotonou-Cadjèhoun base-display checks beyond what
  spottingmode already covers.

## Summary counts

| Country | Sites (candidate) | Aircraft (candidate) | Status |
|---|---|---|---|
| Benin | 1 (Cotonou, 2 airframes) | 2 | Candidates only, low confidence |
| Cape Verde | 0 | 0 | Zero (partial coverage — see gaps) |
| Gambia | 0 | 0 | Zero (English-language coverage complete) |
| Guinea | 1 (Conakry) | 1 | Candidate only, low-medium confidence |
| Liberia | 0 | 0 | Zero (partial coverage — National Museum not confirmed) |
| Mauritania | 0 | 0 | Zero (French/English checked; Arabic not reached) |
| Sierra Leone | 0 | 0 | Zero (partial coverage — Hastings not directly checked) |
| Togo | 0 | 0 | Zero (French Wikipedia + spottingmode checked) |
| Western Sahara | 0 | 0 | Zero (documented; sensitive area, treated neutrally, real gaps in Arabic sources) |

**Total candidate sites: 2 (Cotonou, Conakry) / candidate aircraft: 3.** All
three candidates are LOW or LOW-MEDIUM confidence pending a second source. All
9 countries were run through spottingmode.com/wro completely (every location
page fetched and its plane-status table read); Wikipedia/Wikidata/Commons
coverage is incomplete for several countries due to sustained MediaWiki API
rate-limiting this session, and is flagged per-country above.
