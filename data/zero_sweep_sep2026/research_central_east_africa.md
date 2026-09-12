# Central, East & Southern Africa + Indian Ocean — Zero-Record Sweep

Countries: Burundi, Central African Republic, Comoros, Equatorial Guinea, Eswatini,
Lesotho, Mauritius, Seychelles, South Sudan, Réunion. All `region: Africa`.

## Method summary
- MediaWiki API search + extracts on native-language Wikipedias (fr, es, ar, af) plus English.
- Wikimedia Commons category and full-text search (Commons full-text search is
  dominated by scanned-book OCR noise for these small countries — mostly useless).
- `spottingmode.com/wro` per-country and per-location pages, fetched with
  `curl --ciphers "DEFAULT@SECLEVEL=1"`. This was the highest-value source by far.
- OSM Overpass sweep via `maps.mail.ru` and `overpass.kumi.systems` mirrors
  (`overpass.private.coffee` timed out / no response) for `historic=aircraft`,
  `memorial:type=aircraft`, `aeroway=gate_guardian` across all 10 countries
  (Réunion via `RE` ISO code) in one combined query.
- Wikidata SPARQL attempted (query.wikidata.org) — timed out, not used further.

**OSM result: zero elements returned from both mirrors that answered.** Per the
contract, this is explicitly NOT evidence of absence — Overpass area coverage in
this region is simply too thin to trust a null result.

## spottingmode.com/wro — vocabulary note
The site's own status codes (pre/std/dum/dlt/i-a) were not accompanied by an
explicit legend I could find on the pages fetched. Working interpretation from
context across many location pages: `pre` = preserved/complete airframe kept
intentionally; `std` = static/stored intact (as opposed to `dum`=dumped,
`dlt`=deleted/scrapped, `i/a`=instructional airframe). Critically, `std`/`pre` on
this site denote **airframe completeness/retention status, not necessarily public
presentation**. I have NOT assumed every `std`/`pre` hit is a qualifying "record"
under the contract's display-vs-derelict test — I report what was found and flag
the public-access question explicitly per site below. This distinction is an
**uncertain call for the aggregation step.**

---

## SITES

### 1. Bujumbura airport aircraft group — DC-3 pair
name: Bujumbura Airport Static Douglas DC-3 Pair
city: Bujumbura
state_province:
country: Burundi
postal_code:
region: Africa
address: Melchior Ndadaye International Airport (BJM/HBBA) vicinity
website:
access_type: restricted
latitude: -3.323596
longitude: 29.3234005
source: spottingmode.com/wro/location/19096/ (2x DC-3, status "std", both civil,
  registrations 9U-BRY c/n 9369 and 9U-BRZ c/n 13460; photo credit Savvas Garozis,
  May 2014; last site update 19 December 2017)
confidence: low — WRO shows two complete/static DC-3s at coordinates essentially
  on top of the airport perimeter, photographed in 2014. No corroborating
  Wikipedia/Commons source found, and no evidence found either way of public
  visibility (fence-line, gate guard, or genuinely inaccessible ramp storage).
  Evidence is 12 years old at the photo, site record itself last touched 2017 —
  current status unverified.

### 2. Bujumbura airport aircraft group — Mi-8 pair
name: Bujumbura Airport Static Mil Mi-8 Pair
city: Bujumbura
state_province:
country: Burundi
postal_code:
region: Africa
address: Melchior Ndadaye International Airport (BJM/HBBA) vicinity
website:
access_type: restricted
latitude: -3.32957602
longitude: 29.32314873
source: spottingmode.com/wro/location/20346/ (2x Mi-8T, status "std", Burundi Air
  Force, registrations 9U-BFJ c/n 99357573 and 9U-BFK c/n 99357581; last update
  21 July 2018)
confidence: low — same caveats as site 1: coordinates ~70m from the DC-3 pair,
  suggesting one continuous static/stored area at or beside the airport rather
  than a deliberately curated museum row. No independent public-display
  confirmation found.

### 3. Bujumbura airport aircraft group — Caravelle
name: Bujumbura Airport Static Sud Aviation Caravelle
city: Bujumbura
state_province:
country: Burundi
postal_code:
region: Africa
address: Melchior Ndadaye International Airport (BJM/HBBA) vicinity
website:
access_type: restricted
latitude: -3.32466197
longitude: 29.32271576
source: spottingmode.com/wro/location/22507/ (SE.210-3 Caravelle, status "std",
  civil, registration 9U-BTA c/n 144, "Air Burundi" titles; photo credit Savvas
  Garozis, March 2014; last update 23 March 2019)
confidence: low — again ~100m from sites 1-2, part of the same airport-area
  static group. Aggregation should treat sites 1-3 as possibly ONE site
  ("Bujumbura Airport static aircraft area") rather than three, and should
  decide whether "std" at an airport perimeter meets the public-presentation bar.

### 4. Maseru — Lesotho Defence Force Mi-2 pair
name: Lesotho Defence Force Air Wing Static Mil Mi-2 Pair
city: Maseru
state_province:
country: Lesotho
postal_code:
region: Africa
address: Lesotho Defence Force Air Wing base, Maseru
website:
access_type: restricted
latitude: -29.30628395
longitude: 27.49965477
source: spottingmode.com/wro/location/23510/ (2x Mi-2, status "std", Lesotho Air
  Force/Air Wing, registrations PMU-7 c/n 567033031 and PMU-8 [c/n unlisted];
  credited to user "Witje"; user comment dated 27 September 2023: "Both can be
  seen from outside the fence. If you ask at the gate they will allow you to
  take pictures."; last site update 2 October 2019)
confidence: medium — this is the strongest case in the whole sweep for meeting
  the contract's "public presentation" bar: an eyewitness comment explicitly
  confirms both airframes are visible from outside the perimeter fence and that
  gate staff will let visitors photograph them, i.e. deliberate/tolerated public
  viewing of static, non-flying airframes at a defence-force gate. Comment dates
  to 2023; underlying "Oct 22" remark on the airframes suggests they were placed/
  noted static as of October 2022. Not a formal museum, but plausibly a
  "gate guardian" style record.

### 5. Wau — preserved Antonov An-26
name: Wau Antonov An-26 (ST-APO)
city: Wau
state_province:
country: South Sudan
postal_code:
region: Africa
address:
website:
access_type: restricted
latitude: 7.72037935
longitude: 27.98045158
source: spottingmode.com/wro/location/20890/ (An-26, status "pre", registration
  ST-APO c/n 9805, operator listed as "Sudan" civil; last update 1 October 2018)
confidence: low — single airframe marked "pre" (preserved-class) by the site,
  but no description of context (crash site vs. deliberately retained display),
  no photo, and evidence is 8 years old. Genuinely uncertain whether this
  qualifies as a retained/presented record or an intact-but-abandoned wreck
  that WRO simply didn't code as scrapped. Flagging for aggregation rather than
  asserting it as a record.

### 6. Bata — preserved Mil Mi-26
name: Bata Mil Mi-26 (3C-LLV)
city: Bata
state_province:
country: Equatorial Guinea
postal_code:
region: Africa
address:
website:
access_type: restricted
latitude: 1.84097087
longitude: 9.75225258
source: spottingmode.com/wro/location/30866/ (Mi-26, status "pre", Equatorial
  Guinea Air Force, registration 3C-LLV [identity "to be confirmed" per site
  comment] c/n 34001212153; credited to user "Antheii"; last update 18 October
  2025 — the most recent evidence in this whole sweep)
confidence: low-medium — recent sighting (Oct 2025) of a large, distinctive
  Air Force heavy-lift helicopter marked "preserved" class by the source. No
  independent Wikipedia/Commons corroboration found despite Spanish-language
  searches. Registration identity itself flagged as unconfirmed by the source's
  own commenter, so treat the airframe ID as provisional.

### 7. Moroni — Mi-8/Mi-14 pair (Ukrainian-registered)
name: Moroni Static Mil Mi-8MT and Mi-14PZh
city: Moroni
state_province:
country: Comoros
postal_code:
region: Africa
address:
website:
access_type: restricted
latitude: -11.5335083
longitude: 43.27571869
source: spottingmode.com/wro/location/24971/ (Mi-8MT UR-CBC c/n 94698 and
  Mi-14PZh UR-BYE c/n 74036, both status "std", both civil-registered Ukraine;
  linked in a comment to a nearby dumped Fokker F.27 at location #24970;
  last update 21 April 2026)
confidence: low — both airframes carry Ukrainian civil marks rather than a
  Comorian operator, consistent with contractor/mercenary-linked aviation
  history around Moroni, but the record gives no indication these are presented
  to the public rather than simply parked intact next to a derelict-airframe
  dump (the neighbouring F.27 at #24970 is coded "dlt" = scrapped). Uncertain
  call — could well be an active/inactive-but-not-"displayed" ramp, not a record.
  `operator_country` for these two airframes would be `UA` if imported, not a
  Comorian air arm.

---

## AIRCRAFT

### Bujumbura Airport Static Douglas DC-3 Pair
Douglas|DC-3||9U-BRY||||fixed_wing|civilian|transport||Static at/near Melchior Ndadaye International Airport; retained complete per spottingmode.com/wro (status "std") as of last site update 2017; photographed May 2014; public accessibility not confirmed|C/N 9369|Bujumbura Airport Static Douglas DC-3 Pair|on_display|BI
Douglas|DC-3||9U-BRZ||||fixed_wing|civilian|transport||Static at/near Melchior Ndadaye International Airport; retained complete per spottingmode.com/wro (status "std") as of last site update 2017; photographed May 2014; public accessibility not confirmed|C/N 13460|Bujumbura Airport Static Douglas DC-3 Pair|on_display|BI

### Bujumbura Airport Static Mil Mi-8 Pair
Mil|Mi-8|T|9U-BFJ||||rotary_wing|military|transport||Static at/near Melchior Ndadaye International Airport; Burundi Air Force marks; retained complete per spottingmode.com/wro (status "std") as of last update July 2018; public accessibility not confirmed|Mi8T; C/N 99357573|Bujumbura Airport Static Mil Mi-8 Pair|on_display|BI
Mil|Mi-8|T|9U-BFK||||rotary_wing|military|transport||Static at/near Melchior Ndadaye International Airport; Burundi Air Force marks; retained complete per spottingmode.com/wro (status "std") as of last update July 2018; public accessibility not confirmed|Mi8T; C/N 99357581|Bujumbura Airport Static Mil Mi-8 Pair|on_display|BI

### Bujumbura Airport Static Sud Aviation Caravelle
Sud Aviation|SE-210 Caravelle|III|9U-BTA||||fixed_wing|civilian|commercial_transport||Static at/near Melchior Ndadaye International Airport; wore Air Burundi titles; retained complete per spottingmode.com/wro (status "std") as of last update March 2019; photographed March 2014; public accessibility not confirmed|SE210; Caravelle III; C/N 144|Bujumbura Airport Static Sud Aviation Caravelle|on_display|BI

### Lesotho Defence Force Air Wing Static Mil Mi-2 Pair
Mil|Mi-2||PMU-7||||rotary_wing|military|utility||Kept static at the Lesotho Defence Force Air Wing base in Maseru; a September 2023 eyewitness comment on spottingmode.com/wro states both airframes are visible from outside the perimeter fence and gate staff permit photographs; noted static as of around October 2022|Mi2; C/N 567033031|Lesotho Defence Force Air Wing Static Mil Mi-2 Pair|on_display|LS
Mil|Mi-2||PMU-8||||rotary_wing|military|utility||Kept static at the Lesotho Defence Force Air Wing base in Maseru; a September 2023 eyewitness comment on spottingmode.com/wro states both airframes are visible from outside the perimeter fence and gate staff permit photographs; noted static as of around October 2022|Mi2|Lesotho Defence Force Air Wing Static Mil Mi-2 Pair|on_display|LS

### Wau Antonov An-26 (ST-APO)
Antonov|An-26||ST-APO||||fixed_wing|civilian|transport||Single airframe coded "preserved-class" by spottingmode.com/wro at Wau; no corroborating source found; context (crash site vs deliberate retention) unconfirmed|An26; C/N 9805|Wau Antonov An-26 (ST-APO)|on_display|SD

### Bata Mil Mi-26 (3C-LLV)
Mil|Mi-26||3C-LLV||||rotary_wing|military|transport||Large Equatorial Guinea Air Force heavy-lift helicopter coded "preserved-class" by spottingmode.com/wro at Bata (October 2025); registration/identity flagged as unconfirmed by the source's own contributor|Mi26|Bata Mil Mi-26 (3C-LLV)|on_display|GQ

### Moroni Static Mil Mi-8MT and Mi-14PZh
Mil|Mi-8|MT|UR-CBC||||rotary_wing|civilian|transport||Static at Moroni; Ukrainian civil registration; adjacent to a separately-coded scrapped Fokker F.27 at a nearby location; public presentation unconfirmed|Mi8MT; C/N 94698|Moroni Static Mil Mi-8MT and Mi-14PZh|on_display|UA
Mil|Mi-14|PZh|UR-BYE||||rotary_wing|civilian|other||Static at Moroni; Ukrainian civil registration; amphibious ASW-derived type; public presentation unconfirmed|Mi14PZh; C/N 74036|Moroni Static Mil Mi-8MT and Mi-14PZh|on_display|UA

---

## NOTES

### Per-country findings

**South Sudan** — Searched Arabic ("متحف جنوب السودان الوطني طائرة", "القوات
الجوية جنوب السودان طائرة نصب تذكاري", "مطار جوبا طائرات مهجورة") and English
("South Sudan National Museum aircraft", "Juba airport aircraft boneyard
monument", "South Sudan gate guardian aircraft") on Wikipedia — no hits for a
preserved/displayed aircraft. The South Sudan National Museum in Juba has no
aircraft in its English or (searched) Arabic Wikipedia coverage. **spottingmode
was the only productive source**: 35 Juba-area WRO location entries exist. Two
Juba-airport "dump" pages (location 32375 "Various on the dump" and 32376
"Various") list a mix of foreign civil registrations (Armenia, DR Congo, Kenya,
Russia, Gambia, Tajikistan, Swaziland) with mixed dum/dlt/std codes — **this is
the well-known abandoned-Antonov/Ilyushin dump the brief warned about, and it is
EXCLUDED as derelict**: it reads as an active/passive aircraft graveyard, not a
curated display, despite a few airframes there carrying "std" status codes
individually. A South Sudan Air Force L-410UVP at the same dump is coded "dum"
(dumped) and excluded. Only the separate Wau An-26 (site 5 above, at a different
location ID, described alone rather than as part of "the dump") was flagged as
a possible individual record, with low confidence. All other South Sudan WRO
locations (Abodit, Agok, Aweil x2, Bor x2, Gogrial, Lankien x3, Maban, Malakal,
Old Fangak, Pieri x2, Raga, Raja, Rubkona, Wau x4 more, Yambio, Yei, Yida x2)
were checked and are dlt/dum/blank — genuine crash-site or scrap wrecks,
excluded.

**Réunion** — Searched French extensively: "avion monument Réunion",
"Musée de Villèle avion", "Détachement Air 181 Réunion avion", "Musée
aéronautique Réunion", "gate guardian Réunion", plus CirrusSearch `insource:`
queries combining "avion"/"stèle"/"exposé" with "La Réunion". Read the full
French Wikipedia article on Base aérienne 181 Saint-Denis-La Réunion (formerly
Détachement Air 181) — no mention of any preserved/plinthed aircraft, only
active CN-235 transports. Checked the Musée de Villèle Commons category in
full (30+ files) — it is a slavery/plantation-history museum with no aviation
content. Checked Commons categories "Aircraft in Réunion" and "Aviation in
Réunion" — only active-service aircraft and airport categories, no monument
category. **spottingmode/wro lists exactly one Réunion location** (Piton
Saint-Leu) which is coded "i/a" (instructional airframe, excluded per the
contract's non-public-display categories) — not investigated further as a
record candidate. **Réunion is a well-searched zero** despite being flagged as
the most likely find in this brief.

**Mauritius** — Searched English and French: "Mauritius Police Force
Helicopter Squadron museum", "Musée d'histoire naturelle Maurice avion". No
aviation-monument hits. spottingmode/wro's country list shows Mauritius is
**not among the 53 African countries carrying entries at all** (absent from
the /wro/list/ country index for this batch, unlike Comoros/Equatorial
Guinea/etc. which each had 1-35). **Well-searched zero.**

**Seychelles** — Searched English/French: "Seychelles People's Defence Forces
air wing museum". No hits. Commons category "Aircraft in Seychelles" checked in
full — only active-service and airport categories, one stamp-design category,
no monument. Like Mauritius, Seychelles has **no entries at all in
spottingmode/wro's country index**. **Well-searched zero.**

**Comoros** — Searched French: "avion Comores monument", "avion monument
Moroni Comores" — no hits. spottingmode/wro has 3 Moroni entries; only one
(#24971) has non-derelict codes, reported above as an uncertain candidate
(site 7). The other two Moroni entries (#24970 dlt/dum Fokker F.27, #32373 not
yet fully reviewed for status) were consistent with scrap, not display.

**Equatorial Guinea** — Searched Spanish (the best-covered edition per the
brief): "avión monumento Malabo Guinea Ecuatorial", "Fuerza Aérea Guinea
Ecuatorial museo avión" — no hits for a museum or monument aircraft. Only
spottingmode/wro's Bata Mi-26 (site 6) surfaced as a candidate; the Malabo
entries (#17453, #19135) were both "dum" (dumped, excluded).

**Burundi** — Searched French: "avion monument Bujumbura Burundi", "Force
aérienne burundaise Douglas DC-3", "musée Bujumbura avion". Read the full French
Wikipedia article on Bujumbura's Melchior Ndadaye International Airport — no
mention of preserved aircraft, only current airline service and a 2000 Sabena
shooting incident. All positive evidence for Burundi comes from
spottingmode/wro (sites 1-3 above); this is the strongest concentration of
"std"-coded airframes found anywhere in this sweep, but their proximity and lack
of independent public-display confirmation keeps confidence low.

**Central African Republic** — Searched French: "avion exposé Bangui
Centrafrique", "musée national Bangui Boganda avion", "aéroport Bangui M'Poko
avions abandonnés". No Wikipedia hits for a preserved aircraft; the CAR National
Museum (Barthélemy Boganda) article, checked via search snippets, has no
aviation content. spottingmode/wro's single Bangui "std" location (#19120: BN-2A
Islander, C-130A, Mi-8T, 2x Mi-24V, all Central African Republic Air Force, all
"std") looks like an intact-but-grounded operational air force ramp at Bangui
M'Poko — given CAR's well-documented history of an essentially non-functional
air force with grounded/derelict aircraft sitting at M'Poko, this reads far
more like "stored, not flying" than "deliberately presented to the public," and
I am NOT including it as a site candidate — flagging it here only as an
**uncertain call** the aggregation step may want to weigh, since five distinct
type/serial combinations coded uniformly "std" at one CAR Air Force location is
a larger, more coordinated-looking set than the Burundi or Comoros cases.

**Lesotho** — Searched Afrikaans ("vliegtuig gedenkteken Lesotho") per the
brief's suggestion that South African sources cover it well — no hits.
spottingmode/wro's single Maseru location (site 4) is the best-evidenced find
in this entire sweep thanks to the eyewitness fence-line comment, and is the one
I'd rate closest to meeting the contract's bar.

**Eswatini** — Searched Afrikaans ("vliegtuig gedenkteken Eswatini Swaziland")
— no hits. spottingmode/wro's two Matsapha locations were reviewed: #22663 has
one Nigerian civil B727 coded "i/a" (instructional airframe, excluded) and one
Eswatini Air Force IAI Arava coded "std" but with no public-access evidence
(comments only discuss a de-linked DC-9/fire-trainer confusion, not public
visibility) — not included as a site candidate, flagged as **uncertain**.
#30727 (Matsapha) was fetched but returned no std/pre codes worth reporting.

### EXCLUDED (with reasons)
- Juba airport "dump" locations (WRO #32375, #32376) — mixed-status
  aircraft graveyard of mostly foreign-registered airliners/transports;
  matches the brief's explicit warning about Juba's abandoned-Antonov/Ilyushin
  collection; excluded as derelict even though individual airframes there
  carry "std"/other non-scrap codes, because the site itself (and its own
  description text, "Various on the dump") indicates a graveyard, not a
  presentation.
- All other South Sudan WRO locations coded dlt/dum (Abodit, Agok, both Aweil,
  both Bor, Gogrial, all three Lankien entries, Maban, Malakal, Old Fangak,
  both Pieri entries, Raga, Raja, Rubkona, four more Wau entries, Yambio, Yei,
  both Yida entries) — in-place wrecks/scrap, excluded.
- Malabo, Equatorial Guinea (WRO #17453, #19135) — both coded "dum" (dumped),
  excluded.
- Moroni, Comoros (WRO #24970) — Fokker F.27 coded "dlt" (scrapped), excluded.
- Matsapha, Eswatini (WRO #22663) Nigerian B727 coded "i/a" (instructional
  airframe — used for training, not public display per the contract's
  definition of what does not count), excluded.
- Piton Saint-Leu, Réunion (WRO #21043) coded "i/a" — excluded on the same
  instructional-airframe basis.

### Well-searched zeros (exact queries run, for the record)
- Réunion (fr): "avion monument Réunion", "Musée de Villèle avion",
  "Détachement Air 181 Réunion avion", "Musée aéronautique Réunion",
  "gate guardian Réunion", `insource:"avion" insource:"stèle" Réunion`,
  `insource:"exposé" insource:"avion" "La Réunion"`; also read full text of
  "Base aérienne 181 Saint-Denis-La Réunion" and checked Commons categories
  "Aircraft in Réunion", "Aviation in Réunion", "Musée de Villèle" in full.
- Mauritius (en/fr): "Mauritius Police Force Helicopter Squadron museum",
  "Musée d'histoire naturelle Maurice avion"; spottingmode/wro has zero
  Mauritius entries.
- Seychelles (en): "Seychelles People's Defence Forces air wing museum";
  Commons category "Aircraft in Seychelles" checked in full; spottingmode/wro
  has zero Seychelles entries.
- Equatorial Guinea (es): "avión monumento Malabo Guinea Ecuatorial",
  "Fuerza Aérea Guinea Ecuatorial museo avión".
- Comoros (fr): "avion Comores monument", "avion monument Moroni Comores".
- Burundi (fr): "avion monument Bujumbura Burundi", "Force aérienne
  burundaise Douglas DC-3", "musée Bujumbura avion"; full text of "Aéroport
  international Melchior Ndadaye" read.
- Central African Republic (fr): "avion exposé Bangui Centrafrique", "musée
  national Bangui Boganda avion", "aéroport Bangui M'Poko avions abandonnés".
- Lesotho (af): "vliegtuig gedenkteken Lesotho".
- Eswatini (af): "vliegtuig gedenkteken Eswatini Swaziland".
- South Sudan (ar): "متحف جنوب السودان الوطني طائرة", "القوات الجوية جنوب
  السودان طائرة نصب تذكاري", "مطار جوبا طائرات مهجورة"; (en): "South Sudan
  National Museum aircraft", "Juba airport aircraft boneyard monument",
  "South Sudan gate guardian aircraft".
- OSM Overpass combined query across all 10 countries (BI, CF, KM, GQ, SZ,
  LS, MU, SC, SS, RE ISO codes) for historic=aircraft, memorial:type=aircraft,
  aeroway=gate_guardian: zero elements from two responding mirrors
  (maps.mail.ru, overpass.kumi.systems); overpass.private.coffee did not
  respond within timeout. **Per the contract, this null result is NOT treated
  as evidence of absence** given the region's known poor OSM coverage.

### Uncertain calls for the aggregation step
1. Are sites 1-3 (Bujumbura) one site or three? They sit within ~150m of each
   other at/near the airport perimeter. I reported them as three per WRO's own
   location-ID granularity, but they may represent a single "Bujumbura Airport
   static aircraft area."
2. Does WRO's "std" code, on its own and absent any independent public-access
   confirmation, meet the contract's "deliberate retention plus public
   presentation" bar? I leaned toward including Bujumbura/Bata/Moroni/Wau with
   low confidence rather than dropping them, per the instruction not to smooth
   over uncertainty — but they could equally be intact-but-inaccessible ramp
   storage, which the contract explicitly excludes ("airframe stored out of
   public view").
3. CAR's Bangui M'Poko "std" group (BN-2, C-130A, Mi-8T, 2x Mi-24V) was
   deliberately NOT promoted to a site candidate given CAR's well-documented
   grounded/non-functional air force, but the aggregation step may want to
   weigh it — it is a larger, more uniform set than the ones I did include.
4. Wau An-26 (site 5) and Bata Mi-26 (site 6): single airframes with no
   supporting narrative beyond a one-line WRO description; genuinely
   uncertain whether "preserved-class" here means "displayed" or just "not
   yet scrapped."
