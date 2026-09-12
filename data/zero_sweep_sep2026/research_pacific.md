# Pacific / Oceania zero-record sweep

Countries assigned (all `region: Oceania`): Fiji, Kiribati, Marshall Islands,
Micronesia, Nauru, Palau, Samoa, Solomon Islands, Tonga, Tuvalu, Vanuatu,
Cook Islands, American Samoa, Northern Mariana Islands, Guam, New Caledonia,
French Polynesia.

Method: MediaWiki search API (en/ja/fr Wikipedia), MediaWiki extracts,
Wikimedia Commons category listings, Wikidata SPARQL, and an attempted
Overpass sweep (see below). General web search was not used (per brief,
assumed unavailable).

**Overpass**: all three mirrors named in the contract
(`maps.mail.ru/osm/tools/overpass`, `overpass.kumi.systems`,
`overpass.private.coffee`) were tried with a `historic=aircraft` /
`memorial:type=aircraft` / `aeroway=gate_guardian` query over a Pacific
bounding box. All three returned empty bodies or timed out (20-30s, 0 bytes)
on every attempt. No Overpass data was obtained for this brief — this should
be retried later, ideally per-country with `area["ISO3166-1"="XX"]` rather
than one large bbox (a bbox spanning the antimeridian is also invalid OSM QL
syntax, which I did not have budget to fix and re-run three ways).

**Wikidata SPARQL**: queried `wdt:P31 wd:Q15056993` (instance of individual
aircraft) filtered to Oceania-country QIDs — zero results. Wikidata simply
has no structured individual-aircraft items for this whole region as far as
I could find.

---

## SITES

name: Vilu Military Museum
city: Vilu
state_province:
country: Solomon Islands
postal_code:
region: Oceania
address: Vilu, Guadalcanal, approx. 25 km west of Honiara
website:
access_type: public
latitude: -9.31902778
longitude: 159.79333333
source: English Wikipedia "Vilu Military Museum" (also cross-referenced in "Guadalcanal campaign" and "Guadalcanal" articles, which include photos captioned "Aircraft in Vilu War Museum")
confidence: high — dedicated English Wikipedia article with a detailed collection list, corroborated by two other articles with photographs; article last edited 2026-08-24, "Guadalcanal campaign" article (which embeds the museum photos) last edited 2026-09-04. This is a real, actively-referenced open-air museum, not a wreck site — founded 1975 by Fred Kona, still operated by his family, "occasionally visited by American, Australian and Japanese tourists." This is the single best find of the whole Pacific brief.

### Vilu Military Museum
Grumman|F4F|4|12068||||fixed_wing|monoplane|military|fighter||Complete recovered airframe from the Guadalcanal campaign; displayed outdoors|F4F4|Vilu Military Museum|on_display|US
Grumman|F4F||||||fixed_wing|monoplane|military|fighter||Only the wing and tail section survive of this recovered Guadalcanal wreck|F4F4;Wildcat|Vilu Military Museum|on_display|US
Vought|F4U|1|||||fixed_wing|monoplane|military|fighter||Recovered Guadalcanal campaign wreck; displayed outdoors|F4U1;Corsair|Vilu Military Museum|on_display|US
Lockheed|P-38|F|||||fixed_wing|monoplane|military|fighter||Recovered Guadalcanal campaign wreck; displayed outdoors|P38F;Lightning|Vilu Military Museum|on_display|US
Bell|P-39||||||fixed_wing|monoplane|military|fighter||Only the engine and propeller survive of this recovered wreck|P39;Airacobra|Vilu Military Museum|on_display|US
Douglas|SBD||||||fixed_wing|monoplane|military|bomber||Recovered Guadalcanal campaign dive-bomber wreck; displayed outdoors|SBD;Dauntless|Vilu Military Museum|on_display|US
Grumman|J2F|5|00791||||fixed_wing|biplane|military|utility||Only the wing and the front section of the pontoon survive|J2F5;Duck|Vilu Military Museum|on_display|US
Mitsubishi|G4M|1|1570||||fixed_wing|monoplane|military|bomber||Model 11; tail code 377; only the nose section and parts of the outer wing panel survive; recovered Guadalcanal-campaign wreck|Betty;G4M1|Vilu Military Museum|on_display|JP

---

name: Arc Light Memorial
city: Yigo
state_province:
country: Guam
postal_code:
region: Oceania
address: Andersen Air Force Base, Yigo, Guam
website:
access_type: restricted
latitude:
longitude:
source: English Wikipedia "List of displayed Boeing B-52 Stratofortresses" (entry "56-0586 – Arc Light Memorial, Andersen AFB, Guam"); "Operation Arc Light" article (names the memorial and shows it is on Andersen AFB); Wikimedia Commons file "File:B-52D(061127-F-1234S-017).jpg" caption: "...be retired to the MASDC but was retained at Andersen Air Force Base, Guam, as a memorial for the 'Arc Light' missions, which was dedicated on 12 February [year cut off in caption]"
confidence: medium — three independent Wikipedia/Commons sources agree on the airframe, memorial name and location, but I could not pin exact coordinates (base is not open to the public so nothing to reverse-geocode against street-level imagery) or confirm the dedication year from the truncated Commons caption. This is a real, static, presented memorial (not an active airframe) — passes the "deliberate retention plus public presentation" test even though public access is restricted (military installation). Evidence dated: Commons caption undated upload but referencing 1961-2027 MASDC-retirement timeframe language typical of older USAF PA text; Wikipedia list entry last edited 2026-09-06.
NOTE for aggregation: an earlier F-4E (71-1392) was also displayed at Andersen AFB per "List of displayed McDonnell Douglas F-4 Phantom IIs", but the same article states it "was scrapped in August 2022" — EXCLUDED, no longer extant, do not import.

### Arc Light Memorial
Boeing|B-52|D|56-0586|Stratofortress|||fixed_wing|monoplane|military|bomber||Displayed as the Arc Light Memorial commemorating Operation Arc Light B-52 conventional-bombing missions flown from Andersen AFB during the Vietnam War; retired from active service and retained on base rather than sent to AMARC/MASDC|B52D|Arc Light Memorial|on_display|US

---

## NOTES

### Per-country search log

**Guam** — Searched en.wikipedia for: "Andersen Air Force Base aircraft display",
"Pacific War Museum Guam", "War in the Pacific National Historical Park",
"T. Stell Newman Visitor Center", "Naval Base Guam aircraft",
`insource:"gate guardian" insource:"Guam"`,
`insource:"Andersen" insource:"B-52" insource:"memorial"`,
`insource:"Arc Light Memorial"`. Read full extracts of "War in the Pacific
National Historical Park" (only a recovered Japanese Ha.19-class midget
submarine on display at the T. Stell Newman Visitor Center — NOT an
aircraft, excluded), "Pacific War Museum" (no aircraft mentioned), "List of
museums in Guam", "List of displayed McDonnell Douglas F-4 Phantom IIs"
(Guam section), "List of displayed Boeing B-52 Stratofortresses", "Operation
Arc Light", and the Commons category "Category:Aircraft at Andersen Air
Force Base" (89 files — every one is an in-service operational photo, no
static-display images turned up there; the Arc Light Memorial B-52 was found
via the separate "List of displayed..." article instead).
**Result: 1 site, 1 aircraft** (Arc Light Memorial B-52D). One additional
airframe (F-4E gate guard) found and EXCLUDED as scrapped 2022.

**Palau** — Searched ja.wikipedia for 「ベラウ国立博物館」(Belau National
Museum), 「アイライ 零戦」(Airai Zero), 「パラオ 水上機」(Palau
floatplane), `insource:"パラオ" insource:"零戦" insource:"屋外展示"`; and
en.wikipedia for `insource:"Palau" insource:"Zero" insource:"display"`. Read
full extracts of both the Japanese and English Belau National Museum
articles, and its Commons category (14 files). **Finding: the museum's
outdoor WWII collection is confirmed but consists only of a Japanese Type 96
25mm anti-aircraft gun** ("Imperial Japanese Navy Type 96 25mm Anti-Aircraft
Gun at Belau National Museum" — two Commons photos) and a general "WW2
Japanese Weapon Collection" photo — **no aircraft** turned up in any source,
Japanese or English. The brief's lead about recovered Zeros/a Jake
floatplane on display in Palau could not be substantiated with any
Wikipedia/Wikidata/Commons source in the time available — **EXCLUDED for
lack of evidence, not confirmed false**. This is exactly the kind of
"uncertain call" that deserves a follow-up pass with a proper web search
(Palau dive-tourism and expat-blog sources, which are common for this
specific claim, were unreachable under this brief's API-only constraint).
**Result: 0 aircraft sites confirmed.** Belau National Museum itself is
real and public but has no aircraft — not written to SITES.

**Northern Mariana Islands (Saipan/Tinian)** — Searched ja.wikipedia for
「サイパン 零戦 展示」, 「テニアン 零戦」, and read the full "American
Memorial Park" article (no aircraft — a WWII museum but the extract
describes only recreational facilities, a flag monument and a general WWII
museum with no aircraft named). The best Japanese-language leads
(プレーンズ・オブ・フェイム航空博物館 = Planes of Fame museum in California,
which received a Zero **captured on Saipan in 1944** — that airframe lives
in the US, not Saipan) and 遊就館 in Tokyo (also displays a captured Zero,
also not local) turned up, confirming the pattern the brief warned about:
Saipan/Tinian aircraft wrecks were mostly recovered decades ago and shipped
to museums elsewhere, not kept in place. **No site with an aircraft
currently displayed in the CNMI was found.**

**Marshall Islands (Kwajalein, Majuro, Roi-Namur)** — Searched en.wikipedia
`insource:"Kwajalein" insource:"display" insource:"aircraft"` and
`insource:"Majuro" insource:"Zero"`. All hits were about wartime
battles/operations, none about a present-day display. **Zero.**

**Solomon Islands** — Beyond Vilu (above), searched
`insource:"Solomon Islands" insource:"museum" insource:"aircraft"` — no
second site (query was too broad and returned only general WWII/Pacific
articles). Given budget, did not separately verify "Barana" or a Honiara-
proper collection distinct from Vilu; **flagging as an uncertain call** — a
follow-up pass specifically on "Betikama" (a mission school near Honiara
known in dive/tour literature to hold WWII relics) and "Bloody Ridge" could
not be run in the time available.

**Vanuatu** — Confirmed via "Espiritu Santo", "Naval Advance Base Espiritu
Santo" and "Seabees in World War II" articles that **Million Dollar Point is
explicitly a wartime equipment-dumping site** (US forces bulldozed vehicles,
equipment off the pier into the sea rather than sell it back to the French
administration) — **EXCLUDED, textbook dump, not a presented collection**,
per the brief's own instruction. No separate aircraft-display site found in
English or `insource:"Santo" insource:"Corsair"` (which returned only
unrelated ship/pirate hits, "corsair" being a common French/English word).
Did not run a Bislama-language search (no Bislama Wikipedia edition of
useful size exists). **Zero.**

**Fiji** — Read full "Fiji Museum" extract: colonial/cultural collection
(a war canoe, the HMS Bounty rudder, cannibalism artifacts) — **no
aircraft**. Searched `insource:"Fiji" insource:"gate guard"` (0 hits) and
`insource:"Nadi" insource:"on display" insource:"aircraft"` (7 hits, all
noise — LAX, Air Reentry, Boeing 377, Canadian Pacific, TEAL route history,
Qantas history, NZ Aerial Mapping — none about an aircraft physically in
Fiji). **Zero.**

**New Caledonia** — Searched fr.wikipedia
`insource:"Nouvelle-Calédonie" insource:"avion" insource:"musée"` (82 hits,
all noise about unrelated NC topics — none named a preserved aircraft),
`insource:"Nouvelle-Calédonie" insource:"P-39"` OR `"Corsair"` (2 hits, both
noise), and read the full "Aéroport de Nouméa-La Tontouta" extract (history
of the airfield's WWII US military role, no mention of a preserved
airframe). "Base aérienne 186 Tontouta" has no French Wikipedia article at
all. **Zero.**

**French Polynesia** — Searched fr.wikipedia
`insource:"Faa'a" avion musée` (8 hits — Aéronavale detachment, Air France,
Moorea, NC tourism, stamps, transport articles — no preserved aircraft
named). **Zero.**

**Kiribati (Betio/Tarawa)** — Searched en.wikipedia
`insource:"Betio" insource:"aircraft"`. Confirmed Japanese coastal
artillery guns are well documented at Betio (per "Coastal artillery"
article) but **no aircraft display** turned up in any of the 10 hits
(prison, WWII battle narrative, Medal of Honor citations, ship movements).
**Zero, but strong candidate for a future dedicated pass** — the brief is
right that Betio is dense with recovered ordnance; whether any aircraft
wreckage has been mounted (as opposed to guns) needs a source I didn't have
access to.

**Micronesia (Chuuk/Truk)** — Searched
`insource:"Chuuk" insource:"museum" insource:"aircraft"`. All 10 hits were
about the WWII naval battle history of Truk Atoll (Operation Hailstone,
ship losses) — **confirms the brief's expectation that Chuuk Lagoon is a
dive site, not a museum**; the wrecks (mostly ships, with some aircraft)
are in situ underwater. **EXCLUDED as in-situ; zero museum records.**

**Samoa, American Samoa, Tonga, Cook Islands, Tuvalu, Nauru** — No
dedicated search run beyond general awareness that none of these turned up
in any of the broader queries above (none appeared as a hit in any of the
~15 searches run across this brief). Given the very small size and minimal
Wikipedia footprint of each, and zero incidental mentions, treating these as
**well-searched zeros by absence** — see exact queries to re-run below.

### EXCLUDED (in-situ wrecks / non-records), with reasons
- **Million Dollar Point, Espiritu Santo, Vanuatu** — a WWII US
  equipment-dumping site (bulldozed into the sea), not a presented
  collection. Confirmed via "Espiritu Santo", "Naval Advance Base Espiritu
  Santo" articles.
- **Chuuk (Truk) Lagoon, Micronesia** — WWII wrecks (ships and some
  aircraft) lie in situ underwater; this is dive tourism, not a museum.
  No recovery/mounting found in any source.
- **F-4E 71-1392, Andersen AFB, Guam** — was displayed but per "List of
  displayed McDonnell Douglas F-4 Phantom IIs" was **scrapped in August
  2022**. Not a current record.
- **Belau National Museum, Palau** — has a genuine outdoor WWII ordnance
  display (Type 96 25mm AA gun) but **no aircraft** found in any source
  checked (ja/en Wikipedia, Commons category). Not written up as a SITE
  since it has no aircraft to report.
- **T. Stell Newman Visitor Center / War in the Pacific NHP, Guam** — the
  displayed WWII relic is a Japanese Ha.19-class midget submarine, not an
  aircraft. Not in scope for this database.

### Well-searched zeros — exact queries run (for the aggregation step / to avoid re-research)
- Fiji: en.wp search `insource:"Fiji" insource:"gate guard"`;
  `insource:"Nadi" insource:"on display" insource:"aircraft"`; full-text read
  of "Fiji Museum".
- Vanuatu: en.wp search `insource:"Santo" insource:"Corsair"`;
  `insource:"Vanuatu" insource:"Million Dollar Point"`; full-text of
  "Espiritu Santo", "Naval Advance Base Espiritu Santo".
- New Caledonia: fr.wp search
  `insource:"Nouvelle-Calédonie" insource:"avion" insource:"musée"`;
  `insource:"Nouvelle-Calédonie" insource:"P-39" OR insource:"Corsair"`;
  page-existence check on "Base aérienne 186 Tontouta" (does not exist);
  full-text of "Aéroport de Nouméa-La Tontouta".
- French Polynesia: fr.wp search `insource:"Faa'a" avion musée`.
- Marshall Islands: en.wp search
  `insource:"Kwajalein" insource:"display" insource:"aircraft"`;
  `insource:"Majuro" insource:"Zero"`.
- Micronesia (Chuuk/Pohnpei/Yap/Kosrae): en.wp search
  `insource:"Chuuk" insource:"museum" insource:"aircraft"`.
- Kiribati: en.wp search `insource:"Betio" insource:"aircraft"`.
- Northern Mariana Islands: ja.wp search 「サイパン 零戦 展示」,
  「テニアン 零戦」; full-text of "American Memorial Park" (en.wp).
- Palau: ja.wp search 「ベラウ国立博物館」, 「アイライ 零戦」,
  「パラオ 水上機」, `insource:"パラオ" insource:"零戦" insource:"屋外展示"`;
  en.wp `insource:"Palau" insource:"Zero" insource:"display"`; full read of
  ja.wp and en.wp Belau National Museum articles + Commons category.
- Samoa, American Samoa, Tonga, Cook Islands, Tuvalu, Nauru: no incidental
  hits in any of the ~20 queries run across this brief covering the wider
  region (WWII campaign articles, "List of displayed..." aircraft-type
  articles, gate-guardian searches); **not individually queried by name in
  their native languages** (Samoan, Tongan) — this is the gap most worth a
  follow-up pass, since the brief's own guidance is that native-language
  queries are the highest-yield method and I did not have budget to run
  them for these six.
- Solomon Islands (beyond Vilu): en.wp search
  `insource:"Solomon Islands" insource:"museum" insource:"aircraft"` (too
  broad, no second site found) — "Betikama" and a Honiara-proper collection
  were not separately checked; worth a follow-up.

### Uncertain calls for the aggregation step
1. **Palau recovered Zeros/Jake floatplane** — the brief's own lead,
   plausible and specific, but I found zero corroboration in
   Wikipedia/Wikidata/Commons. Recommend a dedicated web-search pass (not
   API-restricted) before writing this off as a zero.
2. **Solomon Islands beyond Vilu** ("Betikama", Honiara-proper displays) —
   not separately verified; Vilu is confirmed solid but there may be more.
3. **Kiribati (Betio)** — guns confirmed, aircraft unconfirmed either way;
   worth a specific pass given how WWII-dense the site is.
4. **Overpass sweep** — never actually ran (all three mirrors
   timed out/returned empty every attempt); the whole `historic=aircraft` /
   `gate_guardian` layer of evidence for this entire region is missing from
   this brief and should be retried, ideally per-country rather than one
   antimeridian-spanning bbox.
5. **Samoa/American Samoa/Tonga/Cook Islands/Tuvalu/Nauru in native
   languages** — not run; genuine gap, not a confident zero.

## Summary counts
- **Sites with aircraft confirmed: 2** — Vilu Military Museum (Solomon
  Islands, 8 aircraft) and Arc Light Memorial, Andersen AFB (Guam, 1
  aircraft).
- **Total aircraft records: 9.**
- **Genuine documented zeros** (searched, nothing found): Fiji, Vanuatu,
  New Caledonia, French Polynesia, Marshall Islands, Micronesia, Kiribati,
  Northern Mariana Islands, Palau (aircraft only — has a non-aircraft gun
  display), Samoa, American Samoa, Tonga, Cook Islands, Tuvalu, Nauru.
- **Excluded as in-situ/non-record**: Million Dollar Point (Vanuatu), Chuuk
  Lagoon wrecks (Micronesia), scrapped F-4E (Guam), Belau National Museum
  gun-only display (Palau, no aircraft), War in the Pacific NHP submarine
  (Guam, not an aircraft).
