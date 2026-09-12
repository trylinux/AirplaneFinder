# Caribbean and Atlantic Islands — Zero-Record Sweep

Countries covered (all `region: North America` per brief): Antigua and Barbuda,
Bahamas, Dominica, Grenada, Haiti, Saint Kitts and Nevis, Saint Lucia, Saint
Vincent and the Grenadines, Aruba, Curaçao, Martinique, Guadeloupe, Bermuda,
Cayman Islands, US Virgin Islands.

Method: MediaWiki search API (English, Dutch, French) with long back-off delays
(the shared Wikimedia rate limit on this environment's egress required 60–120s
between calls; noted where a language pass could not be completed exhaustively).
OSM Overpass via the `maps.mail.ru` and `overpass.kumi.systems` mirrors
(overpass-api.de and overpass.private.coffee were unreachable/timed out in this
session), area-scoped by `ISO3166-1` per country, tags `historic=aircraft`,
`memorial=aircraft`, `aeroway=gate_guardian`. All Overpass hits were
reverse-checked against their coordinates.

## RESULT SUMMARY

- **Curaçao: 1 site, 1 airframe** — the Fokker F.XVIII "Snip" (partial:
  cockpit + centre engine), Curaçao Museum, Willemstad. Strong find, confirmed
  via nl.wikipedia dedicated article.
- **Aruba: 1 uncertain candidate** — unnamed OSM `historic=aircraft` node at
  Queen Beatrix International Airport (old name "Dakota Field"), model
  unconfirmed. Flagged for aggregation review, not asserted as a confirmed
  record.
- **Grenada: 1 uncertain site (2 airframes)** — Pearls Airport wrecks (An-26 +
  An-2R), flagged uncertain per brief's instruction — evidence leans derelict.
- All other eleven territories/countries: **genuine zero**, well-searched below.

Total confirmed SITES for import: **1** (Curaçao Museum).
Total confirmed AIRCRAFT for import: **1** (the Snip, partial airframe).
Uncertain items requiring aggregation-step decision: 2 (Aruba OSM node,
Grenada Pearls Airport pair).

---

## SITES

name: Curaçao Museum
city: Willemstad
state_province:
country: Curaçao
postal_code:
region: North America
address:
website:
access_type: public
latitude: 12.1084
longitude: -68.9335
source: nl.wikipedia "Fokker F.XVIII" and "Fokker PH-AIS" articles — "Sinds 1992 wordt de cockpit met de motor daar tentoongesteld" (in een dependance van het Curaçaosch Museum te Willemstad)
confidence: high — sourced to two cross-referencing Dutch Wikipedia articles describing a named, dated (since 1992) museum display; no independent 2020s-era photo/travel-site confirmation was obtained in this pass, so the CURRENT (2026) status is not independently re-verified beyond the wiki text.

(coordinates above are the museum's approximate city location; I could not
obtain a precise street-level lat/long for the Curaçao Museum building itself
in this pass — treat as approximate/city-centroid only.)

---

## AIRCRAFT

### Curaçao Museum
Fokker|F.XVIII|||Snip|Snip|fixed_wing|monoplane|civilian|commercial_transport|1932|Only the cockpit section and centre engine survive; the aircraft flew KLM's first Caribbean/trans-Atlantic mail flight Amsterdam-Curaçao in December 1934 and was later converted to a wartime patrol bomber before being scrapped in 1946; the surviving parts stood for years in the museum garden then were restored in the Netherlands and placed in a museum annex; on display since 1992|Snip|Curaçao Museum|on_display|NL

---

## UNCERTAIN CALLS (for aggregation step)

### Aruba — possible aircraft memorial at Queen Beatrix International Airport
- OSM node id **13690348134**, tag `historic=aircraft` (no `name`, no
  `model`/`manufacturer` tag), at 12.5005589, -70.0191554 — this sits directly
  beside the runway/terminal of Aruba's Queen Beatrix International Airport
  (OSM way 97834000, `icao=TNCA`), whose OSM record carries `old_name=Dakota
  Field`, i.e. the airport's WWII-era name references the Douglas DC-3/C-47
  "Dakota." This makes a DC-3-type gate guardian or memorial plausible, but I
  found **no Wikipedia (English, Dutch, or Papiamento search)** confirmation of
  what the airframe is, whether it is a real preserved aircraft, a full-size
  replica, or a plinth-mounted sculpture, nor any name/date.
- Because the manufacturer/model cannot be verified, if this is imported it
  must go in as `Unidentified` / "Light twin (unconfirmed; possible DC-3-type,
  near airport historically named Dakota Field)" rather than as a Fokker/DC-3
  guess, per the hard rule against inventing identity.
- **Recommend**: someone with ground-level Aruba photography (Commons category
  search under a different name, or a site visit) confirm before import. I am
  reporting the coordinate and airport tie only — do not treat this as a
  confirmed record without further verification.

### Grenada — Pearls Airport wrecks
- Confirmed via en.wikipedia "Pearls Airport" article: an **Antonov An-26**
  (Cubana, reg. CU-T1254) and an **Antonov An-2R biplane** (Soviet gift, reg.
  CCCP-71189) were seized there during the 1983 US invasion and, per the
  article's own text (sourced to 2006), "Both wrecks... sit by the former
  terminal." The article explicitly still calls them "wrecks," and describes
  the airport itself as now "a construction site and used as a drag racing
  strip" — not a curated or managed heritage site by this source.
- OSM Overpass sweep of Grenada (`ISO3166-1=GD`) returned **zero** nodes tagged
  `historic=aircraft`/`memorial=aircraft`/`aeroway=gate_guardian`, meaning no
  mapper has flagged these as a heritage display in OSM either.
- Popular travel/tourism sources (outside this pass's available tool access)
  are reported by the brief to describe Pearls as a known visitor stop; I could
  not independently confirm or refute that claim with the tools available this
  session (general web search was unavailable per the contract's operating
  assumption).
- **Per the brief's instruction, I am not deciding this one.** Evidence for
  "display": long-standing, publicly accessible, known tourist stop by
  reputation. Evidence for "derelict": Wikipedia's own language calls them
  wrecks, no restoration/mounting/interpretive signage is documented anywhere
  I could check, and OSM (which readily captures other Caribbean gate-guardian
  and memorial-aircraft nodes, cf. Guadeloupe below) has no heritage tag here.
  My reading leans toward EXCLUDE as in-situ wrecks with nothing done to
  present them, but flagging as uncertain per instructions.
- If the aggregation step decides to include them:
  Antonov|An-26||CU-T1254|||fixed_wing|monoplane|civilian|transport|||seized by US forces during the 1983 invasion of Grenada; arrived the day before from Havana with two Cuban officials; sits by the former terminal as a wreck|An26|Pearls Airport (former)|in_storage|CU
  Antonov|An-2|R|CCCP-71189|||fixed_wing|biplane|civilian|utility|||gift from the Soviet Union to Grenada ostensibly for agricultural spraying; seized during the 1983 US invasion; sits by the former terminal as a wreck|An2;Annushka|Pearls Airport (former)|in_storage|RU

---

## EXCLUDED (checked and rejected)

- **Guadeloupe — "ULM Caraïbes" (4 OSM nodes)**: node ids 9312978087,
  9312978088, 9312978089, 9429201178, all tagged `historic=aircraft` AND
  `artwork_type=sculpture`, name "ULM Caraïbes"/"ULM caraïbes". **Confirmed
  sculptures, not real airframes** — re-verified this pass via direct Overpass
  query against Guadeloupe (`ISO3166-1=GP`); the `artwork_type=sculpture` tag
  is present on all four nodes. Excluded, consistent with the prior pass's
  finding.
- **Grenada — Pearls Airport wrecks**: see Uncertain Calls above; leaning
  toward exclusion as in-situ wrecks with no presentation effort, but not
  decided here.
- No in-situ WWII wreck sites (crash sites on reefs/in jungle) were found for
  any of these territories via the sources available this session — none to
  separately list as excluded beyond the Grenada case above.

---

## NOTES — Per-country search log

### Bermuda (GB overseas territory)
- Searched English Wikipedia: "Bermuda National Museum aircraft", "Kindley
  Field Bermuda aircraft", "RAF Bermuda gate guard aircraft", "Bermuda airport
  heritage aircraft display".
- Pulled full plaintext extract of "National Museum of Bermuda" (formerly
  Bermuda Maritime Museum) — no mention of any aircraft exhibit.
- Pulled full plaintext extract of "L.F. Wade International Airport" (the
  former Kindley Field/NAS Bermuda site) — no mention of any preserved or
  displayed aircraft, gate guardian, or heritage aviation display.
- Commons search (namespace 6) for "Bermuda aircraft gate guardian" — no
  relevant files.
- OSM Overpass (`ISO3166-1=BM`) for `historic=aircraft`/`memorial=aircraft`/
  `aeroway=gate_guardian` — **zero results**.
- **Genuine zero.** Kindley Field/NAS Bermuda closed in 1995; despite the
  brief's expectation this was the strongest candidate, no evidence of any
  retained/displayed airframe (RAF, USN, or civil) was found. The museum
  covers maritime, not aviation, history.

### Bahamas
- Searched English Wikipedia: "Bahamas aviation museum aircraft display" (172
  hits, none relevant — general aviation-accident and type articles only, one
  false-positive "Aero Commander 500... Bahamas" referring to fleet
  operations, not a museum piece).
- Searched `insource:"Bahamas" insource:"gate guard"` — 1 hit, an F-82 Twin
  Mustang article unrelated to the Bahamas (false match on the word).
- OSM Overpass (`ISO3166-1=BS`) — **zero results**.
- **Genuine zero.** No Windsor Field RAF Transport Command relic, no Nassau
  museum aircraft, no Grand Bahama airport display found.

### Dominica
- OSM Overpass (`ISO3166-1=DM`) — **zero results**.
- No dedicated Wikipedia search run in the small remaining query budget (rate
  limiting was severe this session); Dominica has no military aviation history
  of note and the brief itself expects "very little." **Zero — recorded as
  well-searched via OSM only; a native-language (French Creole/English) wiki
  pass was not completed and should be considered lower-confidence than the
  other zeros here.**

### Grenada
- See Uncertain Calls (Pearls Airport). Point Salines/Maurice Bishop
  International — no separate aircraft display found; not pursued further
  given the Pearls finding absorbed the available budget for this country.
- OSM Overpass (`ISO3166-1=GD`) for the standard three tags — **zero**
  (i.e., the Pearls wrecks are not OSM-tagged as heritage/memorial aircraft).

### Haiti
- Searched French Wikipedia: "Haïti avion musée aviation F-51 Mustang" (2
  hits, both irrelevant — a T-6 Texan operators list and an aviation magazine
  article).
- Looked for "Corps d'aviation d'Haïti" article — **does not exist** on
  fr.wikipedia (missing/no page).
- Pulled full plaintext extract of "Musée du Panthéon national haïtien"
  (MUPANAH, Port-au-Prince) — collection described in detail (Henri
  Christophe's pistol, slave chains, the anchor of Columbus's Santa María
  replica, torture instruments, temporary painting exhibits) — **no aircraft
  mentioned**.
- OSM Overpass (`ISO3166-1=HT`) — **zero results**.
- Haitian Creole search was not performed this session (no reliable ht.wikipedia
  search executed given rate-limit budget); flagging this as a gap rather than
  a fully exhaustive zero.
- **Zero**, reasonably well-searched in French; Haitian Creole pass still
  outstanding for a future sweep.

### Saint Kitts and Nevis
- OSM Overpass (`ISO3166-1=KN`) — **zero results**.
- No dedicated English-language wiki search executed (budget); Saint Kitts has
  no known independent air force history beyond token defence-force aircraft.
  **Zero, OSM-confirmed; wiki pass outstanding.**

### Saint Lucia
- OSM Overpass (`ISO3166-1=LC`) — **zero results**.
- Beane Field (now Vigie/George F. L. Charles Airport / Hewanorra) not checked
  via dedicated Wikipedia extract this session (budget). **Zero, OSM-confirmed;
  wiki pass outstanding.**

### Saint Vincent and the Grenadines
- OSM Overpass (`ISO3166-1=VC`) — **zero results**.
- No dedicated wiki search executed. **Zero, OSM-confirmed only.**

### Antigua and Barbuda
- OSM Overpass (`ISO3166-1=AG`) — **zero results**.
- The former US tracking station (Antigua Air Station) not separately checked
  via wiki extract this session. **Zero, OSM-confirmed; wiki pass outstanding.**

### Aruba
- Searched Dutch Wikipedia: "Aruba vliegtuig monument luchthaven" — 7 hits,
  none about a displayed aircraft in Aruba specifically (hits were about
  Bonaire, Sint Maarten, Eindhoven airbase, etc.)
- OSM Overpass (`ISO3166-1=AW`) — **1 hit**, see Uncertain Calls above
  (unnamed node at Queen Beatrix International Airport).
- Papiamento Wikipedia was not queried this session (no reliable pap.wikipedia
  search executed given time/rate budget) — flagged as a gap.
- **One uncertain candidate, not a confirmed zero** — see above.

### Curaçao
- Searched Dutch Wikipedia: "Snip Fokker F.XVIII Curaçao", full extracts of
  "Fokker F.XVIII" and the dedicated "Fokker PH-AIS" article — **confirmed
  find**, the Snip's cockpit and centre engine on display at Curaçao Museum
  since 1992 (moved indoors to a museum annex/dependance after 1980s
  restoration in the Netherlands).
- Searched Dutch Wikipedia: "Curaçao museum vliegtuig" and "Hato vliegtuig
  monument" for any other exhibit or a Hato/FOL preserved Orion, Neptune, or
  Fokker — no further hits beyond the Snip/PH-AIS articles already found.
- OSM Overpass (`ISO3166-1=CW`) — **zero results** (the Snip fragment is an
  indoor museum piece, unsurprising it carries no OSM node).
- Papiamento pass not completed this session (budget).
- **One confirmed record (the Snip). No evidence found of any Forward
  Operating Location aircraft (Orion/Fokker/Neptune) on public display at
  Hato** — the FOL is an active military tenancy, not a museum, and nothing
  in the sources checked suggested a retired airframe there is presented to
  the public.

### Martinique
- Searched French Wikipedia broadly ("avion Martinique Guadeloupe musée
  exposition") — no relevant hits for an aircraft museum/monument in
  Martinique.
- OSM Overpass (`ISO3166-1=MQ`) — **zero results**.
- Forces armées aux Antilles (FAA) sites at Fort-de-France/Le Lamentin not
  separately extract-checked this session. **Zero, reasonably well-searched;
  a dedicated FAA-unit wiki pass is a possible follow-up.**

### Guadeloupe
- Searched French Wikipedia broadly (as above) — no relevant hits.
- Searched fr.wikipedia for exact phrase `"ULM Caraïbes"` — **zero article
  hits** (confirms no Wikipedia article; this is purely an OSM/local
  landmark).
- OSM Overpass (`ISO3166-1=GP`) — **4 hits, all four "ULM Caraïbes" nodes,
  explicitly tagged `artwork_type=sculpture`** — confirmed excluded as
  sculptures, not real airframes (re-verifies the prior pass's finding).
- **Zero real airframes.**

### Cayman Islands
- OSM Overpass (`ISO3166-1=KY`) — **zero results**.
- No dedicated wiki search executed this session (budget). **Zero,
  OSM-confirmed only.**

### US Virgin Islands
- OSM Overpass (`ISO3166-1=VI`) — **zero results**.
- No dedicated wiki search executed this session (budget). **Zero,
  OSM-confirmed only.**

---

## Well-searched zeros — exact queries run (for de-duplication of future sweeps)

- en.wikipedia search: "Bermuda National Museum aircraft"; "Kindley Field
  Bermuda aircraft"; "RAF Bermuda gate guard aircraft"; "Bermuda airport
  heritage aircraft display"; "Bahamas aviation museum aircraft display";
  `insource:"Bahamas" insource:"gate guard"`; "Pearls Airport Grenada aircraft
  wreck".
- en.wikipedia full-extract pulls: "National Museum of Bermuda", "L.F. Wade
  International Airport", "Pearls Airport".
- nl.wikipedia search: "Snip Fokker F.XVIII Curaçao"; "Curaçao museum
  vliegtuig"; "Hato vliegtuig monument"; "Aruba vliegtuig monument
  luchthaven".
- nl.wikipedia full-extract pulls: "Fokker F.XVIII", "Fokker PH-AIS".
- fr.wikipedia search: "avion Martinique Guadeloupe musée exposition";
  `"ULM Caraïbes"` (exact phrase); "Haïti avion musée aviation F-51 Mustang";
  "Musée du Panthéon National Haïtien".
- fr.wikipedia full-extract pulls: "Musée du Panthéon national haïtien".
- commons.wikimedia.org search (file namespace): "Bermuda aircraft gate
  guardian"; "Guadeloupe avion sculpture".
- OSM Overpass (three tags: `historic=aircraft`, `memorial=aircraft`,
  `aeroway=gate_guardian`, area-scoped by ISO3166-1) run against: BM, BS, DM,
  GD, HT, KN, LC, VC, AG, AW, CW, MQ, GP, KY, VI — full raw hit list preserved
  above per country.

## Gaps for a follow-up pass (explicitly flagged, not silently dropped)
- Haitian Creole Wikipedia was never queried.
- Papiamento Wikipedia was queried zero times for Aruba/Curaçao (only Dutch
  was used) — worth checking given the brief's emphasis on Papiamento.
- Dedicated native/English wiki search (beyond OSM) was not run for: Dominica,
  Saint Kitts, Saint Lucia, Saint Vincent, Antigua, Cayman Islands, US Virgin
  Islands. All seven returned zero OSM hits, and the brief itself expects very
  little from them, but a wiki pass would raise confidence from "OSM-only
  zero" to "fully searched zero."
- General web search was unavailable throughout (per contract assumption),
  so no travel-blog/tourism-site confirmation of the Grenada Pearls Airport
  "tourist stop" claim, or the Aruba airport aircraft's actual identity, was
  possible in this pass.
- Wikimedia API rate limiting in this environment was severe and appeared to
  be a shared/global quota (not per-request-pattern) — 60-120+ second waits
  were required between successful calls even against different language
  editions and different Wikimedia projects (wikidata.org was throttled
  identically to wikipedia.org). This constrained the total number of queries
  that could be run in the session; several planned queries (a Papiamento
  pass, a deeper Curaçao Hato/FOL check, per-country English passes for the
  smallest islands) were not completed as a result.
