# Zero-Record Sweep: European Microstates, Crown Dependencies & North Atlantic Territories

Countries covered: Andorra, Liechtenstein, Monaco, San Marino, Vatican City,
Kosovo, Gibraltar, Jersey, Greenland, Faroe Islands.

**Result: no confirmed preserved-aircraft records found in any of the ten
territories.** All are reported as documented zeros below, with one flagged
uncertain lead (Greenland/Narsarsuaq) for the aggregation step to weigh.

No SITES and no AIRCRAFT blocks are included — nothing met the bar for a
record (deliberate retention + public presentation) with a traceable source.

---

### SITES
(none — see NOTES for the documented-zero rationale for each country)

### AIRCRAFT
(none)

---

## NOTES

### Method note on rate limiting
Wikimedia APIs on this environment's shared egress hit HTTP 429 repeatedly
during this pass, including on en.wikipedia.org and da.wikipedia.org. Backoff
of 60s per 429 was applied per the contract; several single calls took 1-2
minutes as a result. Roughly 25 targeted API calls were made across all ten
countries (extracts on known titles + a handful of `list=search` queries),
spaced 4-5s apart with 60s backoff on throttling. No Overpass/OSM sweep was
run this pass (overpass-api.de blocked; the three fallback mirrors
[maps.mail.ru, overpass.kumi.systems, overpass.private.coffee] were not
reached given the call budget already consumed by Wikimedia throttling) — this
is a gap, flagged below per country. No Wikidata SPARQL queries were run for
the same reason; only Wikimedia Commons category/search lookups were used.

### Per-country findings

**Gibraltar** — Checked en.wikipedia `RAF Gibraltar` (full extract read: covers
RNAS/RAF North Front history 1918-2016, no mention of a preserved aircraft,
gate guard, or memorial airframe) and `Gibraltar National Museum` (full extract
read, no aircraft/aviation keyword anywhere in the article). Ran
`list=search` for "Gibraltar gate guardian aircraft" (163 hits, none
Gibraltar-specific — top hits were Duxford, Heathrow, unrelated). Checked
Wikimedia Commons categories `Category:Aviation in Gibraltar`,
`Category:Aircraft in Gibraltar`, `Category:Aircraft at Gibraltar Airport` —
all contain only current-operations/aircraft-spotting subcategories, nothing
that reads as a static/memorial display. Did NOT reach Spanish Wikipedia for
Gibraltar (call budget spent on English sources first) — **this is a genuine
gap**: the brief specifically asked for a Spanish-language pass
("avión monumento Gibraltar", "Museo Nacional de Gibraltar aviación") which
was not completed. Recommend a follow-up pass in Spanish before calling this
a final zero — flagging as **uncertain (under-searched)**, not a clean zero.
Queries run (do not repeat): en.wikipedia extract "RAF Gibraltar"; en.wikipedia
extract "Gibraltar National Museum"; en.wikipedia search "Gibraltar gate
guardian aircraft"; Commons category search "Gibraltar preserved aircraft
monument"; Commons categorymembers on the three Aviation/Aircraft-in-Gibraltar
categories.
Queries NOT yet run (do next): es.wikipedia search "avión monumento
Gibraltar", es.wikipedia search "Museo Nacional de Gibraltar aviación",
Overpass sweep of `area["ISO3166-1"="GI"]`.

**Greenland** — Strongest partial lead in this batch, but it did not resolve
into a confirmed record. da.wikipedia `Narsarsuaq` (full extract, current as
of the article's 2026 population figure) states the settlement's museum
**closed** as of 17 April 2026 when Narsarsuaq's airport was downgraded to a
heliport and services moved to the new Qaqortoq Airport — the museum, school,
kindergarten, health clinic and hotel all closed together. The article does
not say what the museum held. Search `da.wikipedia list=search` for
"Narsarsuaq museum fly udstillet" turned up only the `Consolidated PBY
Catalina` and `Douglas C-54 Skymaster` articles (both describe types that flew
through Bluie West One historically; neither states a Narsarsuaq airframe was
preserved locally — the preserved C-54 example named is at the USAF museum in
Dayton, Ohio, not Greenland). en.wikipedia `Narsarsuaq Airport` (full extract)
covers WWII history (Bluie West One, PBY Catalina and B-25 squadrons) in
detail with no mention of a museum or preserved aircraft on site.
en.wikipedia `Northeast Air Command` extract (24,986 chars) fetched but not
fully keyword-scanned for aircraft/museum due to call-budget pressure —
**gap**. Commons search for "Narsarsuaq museum aircraft" returned only a 1943
wartime photo of a PBY-5A Catalina (historical, not a modern preserved
display). `Bluie West One` redirects but returned an empty extract on first
try. `Pituffik Space Base` (formerly Thule AB) full extract (23,506 chars)
read for keywords museum/preserved/memorial/gate guard/plinth/monument/on
display — none found; article covers a 1954 C-124 crash and a 1968 B-52
nuclear-weapons crash as historical incidents only, no static display
mentioned, and the base is a restricted US facility regardless.
`Grønlands Nationalmuseum` (da.wikipedia) returned an empty extract — title
likely wrong or the article is a stub/redirect not resolved; not confirmed
either way. Kangerlussuaq: da.wikipedia search "Kangerlussuaq fly udstillet
monument" returned zero hits.
**Uncertain call for aggregation**: the closed Narsarsuaq museum is a real
site that plausibly held Bluie West One-era material (this was the base for
thousands of transiting WWII aircraft and had a dedicated local museum) but
no source found in this pass names an aircraft in its collection, and it has
now closed (as of April 2026) with no stated relocation of its contents.
Recommend: (a) fetch the museum's own former web presence via Wayback Machine
for a collections list, (b) check kl.wikipedia (Greenlandic) which was not
reached this pass, (c) check whether the collection transferred to
Qaqortoq or the Greenland National Museum in Nuuk.
Queries run: da.wikipedia extract "Narsarsuaq Museum" (missing, no such
title); da.wikipedia extract "Narsarsuaq"; da.wikipedia search "Narsarsuaq
museum fly"; da.wikipedia search "Narsarsuaq museum fly udstillet";
en.wikipedia search "Narsarsuaq museum aircraft"; en.wikipedia extract
"Northeast Air Command"; en.wikipedia extract "Bluie West One" (empty);
en.wikipedia extract "Narsarsuaq Airport"; en.wikipedia extract "Pituffik
Space Base"; Commons search "Narsarsuaq museum aircraft"; da.wikipedia extract
"Grønlands Nationalmuseum" (empty); da.wikipedia search "Kangerlussuaq fly
udstillet monument" (zero hits).
Queries NOT yet run: kl.wikipedia (Greenlandic) equivalents of all the above;
Wayback Machine capture of any former narsarsuaq-museum.gl or similar site;
en/da wikipedia on "Kangerlussuaq" settlement/airport article directly (only
searched, article itself not pulled); Overpass sweep of
`area["ISO3166-1"="GL"]`.

**Faroe Islands** — fo.wikipedia search "flogfar minnesmerki" (aircraft +
memorial): zero hits. da.wikipedia search "Færøerne fly museum monument":
3 hits, none relevant (Shetland Islands, Trondheim, a Soviet-POW memorial in
Norway — all false positives from the multi-word OR-style match). en.wikipedia
`Vágar Airport` full extract (7,706 chars) checked for museum/preserved/
memorial/gate guard/plinth/display — only hit was an unrelated "marble
memorial" for a maritime rescue and a 1975 runway excursion incident, no
aircraft display. en.wikipedia `Faroe Islands in World War II` returned an
empty extract (title may not resolve directly — needs redirect handling,
not confirmed as a true zero).
**Gap**: fo.wikipedia and da.wikipedia were only lightly queried (2 searches
total) before moving on for budget reasons; the brief's suggested searches for
"Tjóðsavnið" (National Museum of the Faroe Islands) and a dedicated RAF Vágar
wartime-airfield article were not run.
Queries run: fo.wikipedia search "flogfar minnesmerki"; da.wikipedia search
"Færøerne fly museum monument"; en.wikipedia extract "Vágar Airport";
en.wikipedia extract "Faroe Islands in World War II" (empty, redirect not
resolved).
Queries NOT yet run: en/fo/da wikipedia extract "Tjóðsavnið" / "National
Museum of the Faroe Islands"; fo.wikipedia search for "RAF Vágar" history;
Overpass sweep of `area["ISO3166-1"="FO"]`.

**Kosovo** — en.wikipedia `Slatina Air Base` full extract (1,204 chars) read
in full: confirms the 83rd Fighter Aviation Regiment (123rd/124th squadrons,
MiG-21bis and MiG-21UM) was based there pre-1999, and that Russian
paratroopers famously seized the base in June 1999 — but the article makes no
mention of any airframe being preserved or displayed there today. sq.wikipedia
search "MiG-21 Kosovë monument": zero hits. sr.wikipedia (Cyrillic) search
"MiG-21 spomenik Kosovo": no relevant hits (results were about the Kosovo War
generally, unrelated Serbian monuments, and Serbian Orthodox topics — no
airframe-on-plinth hit). en.wikipedia search "Kosovo MiG-21 plinth OR monument
OR museum": returned `Slatina Air Base`, `83rd Fighter Aviation Regiment`,
`Air Force of Serbia and Montenegro`, `NATO bombing of Yugoslavia`, and (as a
tantalizing but off-target hit) `General Dynamics F-16 Fighting Falcon
operational history` mentioning an F-16 "on display in the Yugoslav
Aeronautical Museum, Belgrade International Airport" — that is in Serbia
proper (Belgrade), not Kosovo, so it is excluded here. No Kosovo-based
airframe display was found.
Queries run: en.wikipedia extract "Slatina Air Base"; sq.wikipedia search
"MiG-21 Kosovë monument"; sr.wikipedia search "MiG-21 spomenik Kosovo";
en.wikipedia search "Kosovo MiG-21 plinth OR monument OR museum".
Queries NOT yet run: sq/sr wikipedia extract on "Forcat e Sigurisë së Kosovës"
/ "Kosovo Security Force" directly; sr.wikipedia (Latin script) pass; Prizren
air-base-adjacent searches; Overpass sweep of `area["ISO3166-1"="XK"]` (note:
XK is not a valid ISO code per the brief, but OSM commonly tags Kosovo this
way regardless — worth trying if Overpass access is restored).

**Jersey** — en.wikipedia `Jersey War Tunnels` redirects to `Hohlgangsanlage
8`; full extract read (German WWII underground hospital complex, now a
occupation museum) — no aircraft, plane, Messerschmitt, Junkers, Spitfire, or
"aviation" keyword anywhere in the extract. `Channel Islands Military Museum`
returned an empty extract (title likely does not resolve as given — needs a
disambiguation check, not confirmed as a genuine zero). Jersey Airport itself
was not queried this pass — **gap**.
Queries run: en.wikipedia extract "Jersey War Tunnels" → redirects to
"Hohlgangsanlage 8" (full extract, no aircraft mention); en.wikipedia extract
"Channel Islands Military Museum" (empty).
Queries NOT yet run: en/fr wikipedia extract "Jersey Airport"; fr.wikipedia
search "Jersey avion musée occupation"; en.wikipedia search "Channel Islands
Military Museum" via list=search (title resolution retry); Overpass sweep of
`area["ISO3166-1"="JE"]`.

**San Marino** — it.wikipedia search "San Marino aereo museo monumento": no
San-Marino-specific hits (results were about Marino/Italy, Francesco Baracca's
memorial in Italy, San Benedetto del Tronto, etc. — all false positives from
the ambiguous "San" + "Marino" tokens matching unrelated Italian places/
people). it.wikipedia extract "Museo dell'Emigrante (San Marino)": page does
not exist under that title. No air force, no airport, no aviation museum found
for the Republic of San Marino. Treated as a **documented zero**.
Queries NOT yet run: correctly-scoped it.wikipedia search restricted to the
Republic (e.g. searching within `Categoria:Musei di San Marino`); Overpass
sweep of `area["ISO3166-1"="SM"]`.

**Andorra** — ca.wikipedia search "Andorra avió museu monument": hits were
Museu Nacional de l'Automòbil (cars, not aircraft), general Andorra articles,
art/church topics — nothing aviation-related. No air force, no airport, no
aviation collection identified. Treated as a **documented zero**.
Queries NOT yet run: Overpass sweep of `area["ISO3166-1"="AD"]`.

**Monaco** — fr.wikipedia search "Monaco avion musée héliport": hits were
unrelated (Ayrton Senna F1, a contemporary-art museum in Montélimar, a
biography, a helicopter-history article, the Héliport de Monaco confirmed to
exist and still operate — built for the 1992 Exposition Universelle — but no
mention of any preserved aircraft there or at the Musée des Timbres et des
Monnaies). No aviation museum content found for Monaco. Treated as a
**documented zero**.
Queries NOT yet run: fr.wikipedia extract "Musée des Timbres et des Monnaies"
directly (only reached via generic search, not a direct title fetch);
fr.wikipedia extract "Héliport de Monaco" directly; Overpass sweep of
`area["ISO3166-1"="MC"]`.

**Liechtenstein** — de.wikipedia search "Liechtenstein Flugzeug Museum
Denkmal": no Liechtenstein-specific hits (results were Vienna's
Heeresgeschichtliches Museum, a WWII bomber shootdown near Reichenau an der
Rax in Austria, Lake Constance regional funding, and general
mentions-in-passing of the Principality in unrelated articles). No aviation
museum or preserved aircraft found for Liechtenstein. Treated as a
**documented zero**.
Queries NOT yet run: de.wikipedia extract "Liechtensteinisches
Landesmuseum" directly; Overpass sweep of `area["ISO3166-1"="LI"]`.

**Vatican City** — it.wikipedia search "Vaticano aereo museo monumento": no
relevant hits (results were Città del Vaticano generally, the Museo storico
dell'Arma dei Carabinieri in Rome, papal-travel and unrelated-monument
articles). The Vatican has no air force, no airport (helicopter pad only for
official use), and no identified aviation collection. Treated as a
**documented zero**.
Queries NOT yet run: Overpass sweep of `area["ISO3166-1"="VA"]` (moot — the
Vatican's tiny area makes OSM tagging unlikely to add anything beyond
Wikipedia).

## EXCLUDED
Nothing was found and excluded as an in-situ wreck or non-qualifying find in
this pass — no candidate airframe surfaced at all for any of the ten
countries, so there was nothing to apply the wreck/hulk exclusion rule to.

## Summary of site/airframe counts
All ten countries: **0 sites, 0 aircraft** confirmed this pass.

- Clean, reasonably well-searched zeros: San Marino, Andorra, Monaco,
  Liechtenstein, Vatican City, Kosovo.
- Zeros with acknowledged search gaps (recommend a follow-up pass before
  treating as final): Gibraltar (Spanish-language pass not done — this was
  flagged in the brief as the strongest candidate and deserves a second look),
  Jersey (Jersey Airport and French-language sources not checked), Faroe
  Islands (fo/da wikipedia only lightly queried, Tjóðsavnið not checked).
- Uncertain, not a clean zero: Greenland — a museum plausibly holding
  Bluie West One-era aviation history existed at Narsarsuaq and closed in
  April 2026; its former holdings were not identified in this pass and should
  be chased via Wayback Machine / Greenlandic-language sources before
  concluding zero.
- No Overpass/OSM sweep and no Wikidata SPARQL queries were completed for any
  of the ten countries in this pass, due to the call budget being consumed by
  Wikimedia rate-limit backoffs. This is the single biggest coverage gap in
  this report and should be the first thing a follow-up pass does.
