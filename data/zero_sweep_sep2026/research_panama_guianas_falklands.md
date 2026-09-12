# Zero-record research: Panama, Guyana, Suriname, Falkland Islands

Pass date: 2026-09-10. FETCH pass per CONTRACT_ZERO.md. Wikimedia APIs
throttled hard (429 after 3-5 rapid calls even with sleeps); queries below
were run with 5-60s spacing and multiple 60s backoffs. Overpass ran cleanly
via `maps.mail.ru` and `overpass.private.coffee` mirrors (`overpass.kumi.systems`
timed out both times it was tried and was not pursued further).

## Summary of results

- **Panama** — ZERO confirmed. No new evidence found beyond the prior pass's
  documented zero. Overpass sweep (new) and Spanish MediaWiki sweep (new)
  both came back empty.
- **Guyana** — ZERO. English search plus Overpass plus Wikidata all empty.
- **Suriname** — NOT a clean zero. One SITE/AIRCRAFT candidate found: a 1989
  air-disaster memorial in Paramaribo built from actual engine cowlings of
  the crashed aircraft. Flagged low/medium confidence and marked as an
  uncertain call — it is a memorial assembled from wreckage components, not
  a displayed airframe, and aggregation should decide if it qualifies under
  "deliberate retention plus public presentation."
- **Falkland Islands** — Still effectively ZERO by my sourcing, despite the
  brief's strong expectation otherwise. I could not find any English or
  Spanish Wikipedia source, nor any Wikidata item, placing a preserved
  Pucará or MB-339 airframe physically ON the islands today. Every specific
  survivor of both types that I could source is documented as having been
  removed to the UK (South Yorkshire Aircraft Museum, Norfolk and Suffolk
  Aviation Museum, IWM Duxford, RAF Museum Cosford). See the Falklands
  section below for exactly what I checked and why I did not manufacture a
  positive result the brief seemed to expect.

Counts: Panama 0 sites / 0 aircraft. Guyana 0 / 0. Suriname 1 site / 1
aircraft (low-medium confidence, flagged). Falkland Islands 0 / 0 (from my
sourcing — see notes on why this may be incomplete).

---

### SITES

name: SLM-ramp gedenkmonument (1989 SLM Flight PY764 memorial)
city: Paramaribo
state_province:
country: Suriname
postal_code:
region: South America
address: Begraafplaats Rusthof, Jagernath Lachmonstraat, Paramaribo
website:
access_type: public
latitude:
longitude:
source: nl.wikipedia.org "SLM-ramp" (article extract, section "Monument"), accessed 2026-09-10
confidence: medium — the memorial's existence and description (four white columns each topped with an aircraft engine's cowling/plating, with plaques bearing victims' names) is clearly sourced to the Dutch Wikipedia article on the crash; I have no photo/Commons confirmation and no confirmation of exact coordinates or whether the engine plating is genuinely from the wrecked aircraft (the article implies it is, but does not use the word "wrak" or "authentic"). Evidence is a single textual source, undated beyond "erected" with no year given.

### AIRCRAFT

### SLM-ramp gedenkmonument (1989 SLM Flight PY764 memorial)
Douglas|DC-8|Super 62||Fajalobi; Anthony Nesty|||fixed_wing|civilian|commercial_transport|1969|Memorial at Rusthof cemetery Paramaribo uses the cowling/plating of aircraft engines recovered from this DC-8 which crashed near Zanderij on 7 June 1989 killing 176; the memorial presents four engine cowlings on white columns not a full airframe; this is Suriname's worst air disaster||Suriname Airways|on_display|

---

## Per-country notes: what was searched and found

### Panama — documented zero (re-tested)

**Prior pass** already ran an English-language sweep and returned a zero,
but could not reach OSM Overpass and did not run Spanish MediaWiki. This
pass specifically closed both gaps.

**Overpass (new this pass)**: ran the full sweep —
`historic=aircraft`, `way[historic=aircraft]`, `memorial=aircraft`,
`memorial:type=aircraft`, `aeroway=gate_guardian` — over
`area["ISO3166-1"="PA"]`, `out center;`. Confirmed the area resolves
correctly (Panama, admin_level 2). Ran successfully on **two** working
mirrors:
- `maps.mail.ru/osm/tools/overpass/api/interpreter` — 0 elements
- `overpass.private.coffee/api/interpreter` — 0 elements
- `overpass.kumi.systems` — timed out (40s) both times tried; not usable
  this session.

Result: **zero matching nodes/ways in Panama on both working mirrors.**

**Spanish MediaWiki extracts (new this pass)** — `action=query&prop=extracts`
with `redirects=1`, `explaintext=1`, against es.wikipedia.org, on:
- Fuerza Aérea Panameña — extract returned (24,437 chars), no hit for
  museo/exhib/monumento/preserv/pedestal.
- Servicio Nacional Aeronaval — extract returned (11,646 chars), no hit for
  museo/exhib/monumento/preserv/pedestal/Albrook/Howard.
- Albrook, Base Aérea Howard, Museo del Canal Interoceánico, Aeropuerto
  Marcos A. Gelabert, Río Hato — not individually extracted due to rate-limit
  exhaustion late in the session; a broader `insource:"Panamá" insource:"avión"
  insource:"monumento"` search (154 total hits) returned only irrelevant
  country articles (México, Chile, Perú, Uruguay, etc.) on the first page,
  none Panama-specific — this is weak negative evidence only, not a full
  clearance of those five remaining titles.
- Wikidata `haswbstatement:P131=Q804` (located-in Panama)
  `haswbstatement:P31=Q11436` (instance-of aircraft) — 0 hits. (P131 only
  catches items whose *immediate* administrative-entity claim is Panama
  itself, so this is supplementary evidence only, not conclusive.)

**Confirmed exclusions per brief**: "Museo Aéreo Fénix" is in Panama City,
**Florida, USA** — not Panama the country; excluded as a recurring false
positive, not independently re-verified this pass (per brief's own
instruction). The Fokker 100 "museo aeronáutico" restaurant on Naos Island
was reported (La Prensa, 21 May 2026, per brief) as reclassified as scrap
and removed — excluded, not currently on display, not independently
re-verified this pass (no web search available).

**Conclusion: Panama remains a well-searched zero.** Recommend not
re-researching without either (a) a working overpass.kumi.systems mirror to
triple-confirm, or (b) direct-title Spanish extracts for Albrook, Base Aérea
Howard, Museo del Canal Interoceánico, Aeropuerto Marcos A. Gelabert, and Río
Hato specifically (queued but not completed this pass due to rate limiting).

### Guyana — zero

- English Wikipedia extract for "Guyana Defence Force Air Corps" — page does
  not exist (title missing).
- English Wikipedia extract for "Guyana Defence Force" — 9,646 chars, no hit
  for museum/display/preserv/monument/plinth/Timehri/memorial.
- English Wikipedia extract for "Cheddi Jagan International Airport" —
  9,307 chars, no hit for museum/display/preserv/monument/plinth/memorial/gate
  guard.
- English Wikipedia extract for "Guyana National Museum" — full extract
  read; lists a "pork-knocker" exhibit and a Prime Minister's car ("PR1")
  on display; no aircraft mentioned anywhere in the article.
- `insource:"Guyana" insource:"aircraft" insource:"monument"` (en.wikipedia,
  49 hits) — top results were unrelated country/topic articles (Romania,
  Madeira, JFK Airport, French Algeria, etc.), none Guyana-aviation-specific.
- `insource:"Timehri" insource:"preserved"` (en.wikipedia, 1 hit) — only the
  main "Guyana" article, not aviation-related on inspection of context.
- Overpass sweep (same 5 tags) over `area["ISO3166-1"="GY"]` on
  `maps.mail.ru` mirror — 0 elements.
- Wikidata `haswbstatement:P131=Q734` + `P31=Q11436` — 0 hits.
- Dutch-language check (per brief, for the colonial period) was not run —
  Guyana's aviation history is entirely post-independence/British-era
  English-language material (Guyana Defence Force Air Corps formed 1968
  under British administration; no Dutch colonial aviation history exists
  since Guyana passed from Dutch to British control in 1814, well before
  powered flight). This omission is deliberate, not an oversight.

**Excluded, named, with reason**: Jonestown/Port Kaituma airstrip (site of
the 1978 murders of Congressman Leo Ryan and others as they tried to board
aircraft) — explicitly excluded per the brief's instruction: this is a
crime/crash scene with abandoned equipment, not a site with an aircraft
deliberately mounted or presented. No further research was done on it beyond
confirming via the brief's own description that this exclusion applies.

**Conclusion: Guyana is a well-searched zero.**

### Suriname — not a clean zero (see SITES/AIRCRAFT above)

- Dutch Wikipedia extract "Surinaamse Luchtmacht" — full history of the
  Suriname Air Force (LUMA) read (Britten-Norman Defenders, Cessnas, Pilatus
  PC-7s, Alouette III/Chetak helicopters, CASA 212s, Bell 205, Hughes 500).
  No mention of any retired airframe placed on display, at Zorg en Hoop,
  Zanderij, or any other base.
- Dutch Wikipedia extract "Surinaams Museum" (Fort Zeelandia) — 22,016 chars
  read in full; no mention of "vliegtuig" (aircraft), "luchtvaart"
  (aviation), or "vliegtoestel" anywhere in the article.
- Dutch Wikipedia extract "Zorg en Hoop Airport" — 11,065 chars; no mention
  of a displayed aircraft, monument, or museum at the airport.
- Dutch Wikipedia extract "SLM-ramp" (the 1989 DC-8 crash, Suriname's worst
  air disaster) — found the Rusthof cemetery memorial described above. This
  is the one non-zero finding for Suriname; see SITES/AIRCRAFT.
- Zanderij/Johan Adolf Pengel International Airport itself was not separately
  checked for a static-display aircraft due to rate-limit exhaustion; this is
  a gap, flagged for any future pass.
- Sranan Tongo Wikipedia (srn.wikipedia.org) was not queried this pass — it
  is a very small edition (low article count) and time/rate-limit budget was
  spent on Dutch instead, which is the far larger and more authoritative
  edition for Suriname per the brief's own guidance. Flagged as untested.

**Conclusion: Suriname is not a genuine zero.** The Rusthof memorial is a
real, sourced finding, but it is engine cowlings from a wreck built into a
memorial, not an airframe on display — aggregation should decide whether
this satisfies "deliberate retention plus public presentation" or should be
treated more like the excluded in-situ-wreck category. I did not find
anything resembling a full preserved military or civil airframe anywhere in
Suriname.

### Falkland Islands — zero by my sourcing (see caveats — likely incomplete)

This was flagged in the brief as "by far the strongest candidate" and one
that "should NOT be a zero," specifically pointing at a Pucará and an
MB-339 "known to survive on the islands." I was not able to substantiate
that claim from Wikipedia or Wikidata, and I want to be explicit about
that rather than force a result.

What I checked:
- English Wikipedia extract "RAF Mount Pleasant" — full history read; no
  mention of a gate guardian or any static aircraft display at the base.
- English Wikipedia extract "Falkland Islands Museum and National Trust" —
  full history read (dockyard site, Stanley; 1982-conflict interactive
  room; maritime-history displays); no aircraft mentioned in the article
  text at all.
- English Wikipedia extract "Goose Green" — full article read; describes
  the settlement and the 1982 battle; no mention of any aircraft, wreck, or
  memorial aircraft display.
- English Wikipedia extract "Battle of Goose Green" — full article (54,274
  chars) read; multiple Pucará/MB-339 combat-loss mentions (in-flight and
  crash locations at Blue Mountain, near the settlement, etc.) but every
  one describes wartime destruction, not a subsequent recovery/display; no
  hits for "preserved," "memorial [+aircraft]," or "museum" in an
  aircraft context.
- English Wikipedia extract "Port Stanley Airport" — full history read
  (Argentine occupation, Pucará/MB-339/T-34 basing during the war, Black
  Buck raids, post-war RAF Stanley/Phantom period, present-day FIGAS
  Islander/Bristow S-92 operations); no static-display aircraft mentioned.
- English Wikipedia article "FMA IA 58 Pucará" — full "Aircraft on display"
  section read. Lists: prototype AX-01 in Argentina (Morón), CA-605 in Sri
  Lanka, and five UK-held airframes (A-515 South Yorkshire Aircraft Museum,
  A-522 North East Land Sea and Air Museums, A-528 Norfolk and Suffolk
  Aviation Museum, A-533 South Yorkshire cockpit section, A-549 IWM
  Duxford). **No Falklands entry in this list.**
- Spanish Wikipedia article "FMA IA 58 Pucará" — parallel search of the
  full extract for Malvinas/exhibición/museo/Stanley/Goose Green/pedestal/
  monumento; found only combat narrative and the same UK-museum-transfer
  facts (A-515 ex-Boscombe Down evaluation aircraft returned to RAF
  Cosford), plus a Uruguay-based gate-guard project (unrelated to the
  Falklands). No Falklands-based display found.
- English Wikipedia article "Aermacchi MB-339" — "three MB-339 airframes
  were captured by the British, with one of these preserved at the South
  Yorkshire Aircraft Museum, Doncaster" — again, removed to the UK, not
  retained on the islands.
- Spanish Wikipedia article "Aermacchi MB-339" — same fact confirmed
  ("Una de estas células se conserva en el Museo de Aviones de South
  Yorkshire, Doncaster").
- English Wikipedia article "Argentine Naval Aviation" — full extract read;
  Falklands War section covered but no display/museum content relevant to
  an on-island airframe.
- `insource:"Falkland" insource:"Pucará" insource:"preserved"`
  (en.wikipedia, 5 hits: Argentine Air Force, Operation Black Buck,
  Mitsubishi MU-2, Argentine Naval Aviation, South Yorkshire Aircraft
  Museum) — all already covered above, none placing an airframe on the
  islands.
- `insource:"Falkland Islands" insource:"gate guard"` (en.wikipedia, 3 hits:
  Eurofighter Typhoon, Dassault Mirage III, Gate guardian) — none relevant
  to an actual Falklands gate guardian.
- Commons `list=search` for "Pucará Falkland" — 0 hits.
- Wikidata `haswbstatement:P131=Q9648` (located-in Falkland Islands) +
  `P31=Q11436` (instance-of aircraft) — **0 hits.**
- Overpass sweep (5 tags) over `area["ISO3166-1"="FK"]` — confirmed the area
  resolves correctly (name "Falkland Islands," admin_level 2, capital
  Stanley) — **0 elements** on the `maps.mail.ru` mirror.

**What I did NOT get to, due to rate-limit exhaustion**, and would prioritize
in a follow-up pass:
- Direct-title extracts for "Museo de las Malvinas" (there are Argentina-
  mainland museums by similar names in Buenos Aires and Río Gallegos that
  hold recovered Falklands-conflict material and captured serials — these
  would be Argentina-country sites, not Falklands sites, but are worth
  checking to make sure nothing was misattributed) and for any dedicated
  "1982 Liberation Memorial" or "Wireless Ridge" article.
- A pass over Commons category "Category:Aircraft wrecks in the Falkland
  Islands" or similar (categorymembers query) — attempted once, hit a 429,
  not retried.
- A search of local/military-enthusiast sources outside Wikimedia (e.g.
  aviation-safety databases, warbird registries) — outside this pass's tool
  set per the contract (general web search assumed unavailable).

**My assessment for aggregation**: I take the brief's claim about a
surviving Pucará and MB-339 "on the islands" seriously — it may well be
accurate and simply not documented in the two Wikipedia articles I checked
(both of those articles' "on display"/survivor lists are known to be
incomplete for military types generally). But I was not willing to invent a
site or airframe entry to satisfy that expectation without a source, per
the contract's hard rule against inventing data. **I am flagging Falkland
Islands as an open, not a confirmed, zero** — the strongest candidate in
this batch for a future pass with fresh rate-limit budget, specifically to
chase Commons categories and any dedicated Falklands-war-memorabilia site
that a plain Wikipedia article extract would not surface.

## Uncertain calls for aggregation

1. **Suriname — Rusthof cemetery SLM memorial**: does a memorial built from
   recovered engine cowlings (not an intact or substantially complete
   airframe) satisfy "deliberate retention plus public presentation," or
   should it be treated as excluded wreckage-derived memorial art? I have
   included it at medium/low confidence rather than dropping it, per the
   contract's instruction not to smooth over uncertainty.
2. **Falkland Islands**: genuine zero from my sourcing, but I believe this is
   more likely an artifact of incomplete Wikipedia coverage than an actual
   absence, given the brief's specific, informed claim. Recommend
   re-running with Commons-category and non-Wikimedia sourcing before
   treating this as final.
