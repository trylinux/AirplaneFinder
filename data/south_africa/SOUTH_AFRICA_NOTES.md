# South Africa

First African country in the database. 36 sites, 197 airframes, imported
September 2026. Nothing on the continent existed before this pass, so there was
no stub to update — but that also means there was no prior work to check the new
data against.

Four research passes (SAAF Museum sites; civilian museums and a discovery sweep;
military base collections; monuments and gate guards) plus a fifth adjudication
pass to resolve the airframes that came back at two places.

---

## Sources and their weight

**The whole country runs off one compilation.** Dean Wingrin's Unofficial SAAF
Website (`saairforce.co.za`) maintains two tables nobody else does: airframes at
the SAAF Museum's sites, and complete ex-SAAF airframes displayed elsewhere in
South Africa. Almost everything else in South African preservation writing
descends from it. In particular:

- **defenceWeb's 2021 gate-guard article is Wingrin restated** — it says so
  itself, and quotes him conceding the list "might need updating". Treating
  those two as agreeing sources is double-counting.
- **Aerial Visuals, silverhawkauthor and aviationmuseum.eu** appear to share an
  ancestor. aviationmuseum.eu carries a "last page update" of December 2016 and
  lists seven South African sites; it has no entry for Springs (which did not
  exist yet), Stellenbosch, Simon's Town, Kimberley or Aerotel.

Wingrin's list is genuinely maintained — diffing Wayback snapshots from 2017,
2020 and December 2025 against the live page shows the Johannesburg entries
rebranded to Ditsong in 2026 and seven rows added (Cheetah E 826, Cheetah R 855,
Mirage IIICZ 813, DH-9 2005, C-47 6850, Hartbees 851, Hurricane 5285). **But
every military-property entry has been byte-identical since January 2017.** Nine
years unchanged on a list whose maintainer is demonstrably editing other rows is
ambiguous: either those base displays have not moved, or nobody can get behind
the gate to re-check them. That ambiguity is why the base rows below lean on
satellite imagery rather than on the list.

Currency came from three places that are independent of that family:

1. **ABPic** (Air-Britain's photo library), searchable by serial *and by
   construction number*. The c/n search settled the Harvard 7573 duplicate that
   no amount of reading the lists could.
2. **airhistory.net** — every photo dated and located, with an "[Off-Airport]"
   taxonomy that is exactly right for monuments. Two photographer sweeps carry
   most of the monument currency here: an unidentified 15–22 September 2018 tour
   and Erik Sleutelberg's 25 September 2022 tour. Cloudflare rate-limits hard;
   several type pages 403'd mid-run.
3. **Esri World Imagery**, pulled and inspected directly. This produced the only
   genuinely 2026 evidence for the base displays.

One book-length source deserves its own line: **Reid and Strümpfer, *The Dassault
Mirage F1 in South African Air Force service*, Revision 2, August 2025**, hosted
on saairforce.co.za. Written from squadron diaries and direct examination of the
airframes. It corrected two records on its own.

**Not used:** Grokipedia. **Unreachable:** aerialvisuals.ca timed out on every
`Airframes.php?Seeds=` request from the research environment, so the per-airframe
dossier cross-check the methodology calls for could not be run on any serial.
That is the single biggest gap in verification depth here. aviagraphers.net's
"South African aircraft monuments" page — the one dedicated compilation of
exactly this subject — 403s to direct fetch; a Wayback snapshot dated 15 October
2025 exists at `web/20251015092033` and is the highest-value document to retrieve
before the next South African pass.

---

## Corrections made

**Mirage F1CZ 210 and 212 are transposed on the SAAF's own list.** Wingrin gives
210 to the University of Pretoria's Sci-Enza centre and 212 to the CSIR. A
JetPhotos image dated 15 October 2021 is captioned 212 at the University of
Pretoria, with provenance matching UP's own 2010 news item (donated 1996,
reassembled 2009, displayed from 2010). Independently, the August 2025 Mirage F1
monograph publishes detail photographs of a V3B launch rail "as mounted to CZ
#210 at CSIR", credited to a CSIR staff photographer. Two sources with no common
ancestor, each naming a different one of the pair, both contradicting the list in
the same direction. Swapped.

**Harvard 7573 is at Swartkop, not Dunnottar.** Wingrin carries 7573 *twice* —
as a sectioned AT-6C at Swartkop and as a Harvard III in Dunnottar town centre.
ABPic searched by **construction number 88-15336** returns exactly two records,
both at SAAF Museum Swartkop (Graham Hutchinson 29/03/2011; Derek Heley
04/10/2019). The c/n in the Dunnottar identity chain resolves to the Swartkop
airframe. A source that contradicts itself cannot outweigh two dated photographs
tied to the c/n. **The Dunnottar site was dropped entirely** — see exclusions.

**Impala 507 and Albatross 887 moved into the museum on 7 May 2022.** defenceWeb,
13 May 2022, "New home at SAAF Museum for Dawid Stuurman gate guards": both came
off the airport plinths and crossed the airfield to the SAAF Museum's Port
Elizabeth branch, badly corroded by the coastal climate. This closes the loop
opened by defenceWeb's 21 April 2021 "Port Elizabeth gate guards down", which
reported them down and said it *appeared* they were going to the museum. The
2022 piece confirms it happened. **No airport gate-guard site was created.**

**Bosbok 920 is airworthy at Swartkop, not static at Port Elizabeth.** Commons
holds two dated geotagged photos of 920 *at PE* — Bob Adams 01/12/2006, and NJR
ZA 20/09/2007 captioned "Bosbok undergoing restoration". ABPic then has it at
SAAF Museum Swartkop, Derek Heley 04/10/2019, and Wingrin lists it "Airworthy |
Swartkop". The restoration succeeded and the aircraft moved. The PE Bosbok is
**948**, which is itself single-sourced and was held out.

**The Port Elizabeth Harvard is 7289, not 7480.** Harvard 7480 is ZU-DML: Commons
categorises the 2006 PE photograph under ZU-DML and a 2005 hangar caption reads
"Harvard 7480 is ZU-DML geregistreer"; ABPic then has ZU-DML at PE on 11/02/2007
and at Swartkop on 04/10/2019. 7480 left. 7289 is the one with continuous PE
photo coverage (2001, 2005, 2006, 2007).

**Vampire 205 is an FB.5, not an FB.52.** The SAAF FB5 batch was serialled 201 to
210 and 205 sits inside it; FB52 is a later export block (227, 229, 235, 241,
253, 254). ABPic captions the 11/02/2007 PE photograph "De Havilland DH.100
Vampire FB5".

**Impala 519 is not at Swartkop.** ABPic holds zero photographs of an Impala 519
anywhere in South Africa, while Swartkop's Impala population is well covered
(532, 562, 589, 1065 all have dated shots). Wingrin's Swartkop list names 532,
562, 589, 1000 and 1065 and actively excludes 519, placing it instead at AFB
Hoedspruit. The Swartkop row (Aerial Visuals only) was dropped. The Hoedspruit
row was kept but is the weakest in the set — see open questions.

**The Stellenbosch Mirage is F1CZ 207 and is indoors.** Wingrin's list omits it
entirely. The 2025 monograph names it, confirms the ex-University of Stellenbosch
Mechanical Engineering provenance, notes the engine is absent and the repaint
colours are wrong, and records it moved into a hangar.

**The Stellenbosch Vampire is 241, not 231.** dehavilland.co.za places 231 at
Stellenbosch and 241 at Bloemfontein, both hedged with question marks. Against
that, a 2011 SAAF-forum thread started by a club member records Vampire **241**
unveiled at the club on 18 November 2006 after a restoration, with Wingrin
confirming in-thread that 241 is an FB52. First-hand club testimony beats a
hedged type list.

**Puma 145 did not move; its unit was renamed.** Wingrin's 2017 snapshot says
"GSB Potchefstroom"; the live page says "School of Tactical Intelligence
(Potchefstroom)". Same place. The site is named for the current unit.

---

## One airframe, one place

Seven collisions surfaced when the four packages were diffed against each other
before anything was written. Six were the same airframe recorded twice at the
same site by two passes (Wasp 85, and four Port Elizabeth airframes) and were
merged. Three were genuine two-site conflicts — Impala 519, Harvard 7573,
Impala 507 — and are resolved above. In every case one row was kept and one was
dropped; no airframe was carried at two sites "to be safe".

Two same-serial pairs are **not** collisions and were deliberately kept: Vampire
FB.52 **235** at Langebaanweg and Mirage F1AZ **235**, and the several Alouette
III sections at Port Elizabeth (632, 105, 635). Different SAAF type blocks reuse
numbers; the `(model, tail_number)` key handles this correctly.

---

## The unique-key problem this pass exposed

**SAAF Mirage F1CZ 207 has been imported with a blank `tail_number`.** The serial
is 207 and is not in doubt. But the database enforces `UNIQUE (model,
tail_number)` and a French Armée de l'Air **Mirage F1C-200 serial 207** is
already recorded at the Musée de l'Air et de l'Espace. Two different aircraft,
two different national serial systems, one collision. The serial is preserved in
that airframe's aliases and the reason is written into its description.

This is the first time a non-US serial system has entered the database at scale
and **it will recur and get worse**. SAAF, French, Israeli, Indian and Swedish
serials are all bare three- and four-digit numbers drawn from independent
sequences, and `(model, tail_number)` cannot tell them apart. The honest fix is a
key that includes something national — operator country, or `full_designation`
plus tail — rather than blanking real serials one at a time. Worth deciding
before the next non-US country goes in, because every blanked serial is a
permanent loss of the field the airframe is most searched by.

---

## Judgment calls

**Access type, judged by how a visitor actually gets in, not by who owns the
land.** The SAAF Museum sites at Swartkop and Ysterplaat sit on air force bases
and are `public` — normal opening hours, ordinary visitors walk in. The South
African Naval Museum is inside the West Yard of Naval Base Simon's Town, open
seven days a week with free entry and its own street entrance: `public`. The
Waterkloof gate guards are `public` because both confirmed airframes stand 20–50
m back from ordinary suburban streets in Valhalla, behind a fence, photographable
from the pavement. Langebaanweg, Bloemspruit, Hoedspruit, SAAF HQ, Thaba Tshwane,
Saldanha and Potchefstroom are `restricted` — controlled gates, no visiting
arrangements found. None of them was marked `appointment`: inventing an
appointment process would be worse than calling it restricted. Dickie Fritz is
`appointment` because the aircraft sit inside a walled compound (the standing
enthusiast advice is to climb the tree outside the wall). Aerotel Hoedspruit is
`appointment` because the only way to see the aircraft is to book a room.

**Replicas are recorded, flagged, and carry no serial.** The Port Elizabeth
Spitfire is a full-size wooden model — ABPic catalogues it "Supermarine Spitfire
IX (Replica)" under replica-register number BAPC.519, and Wikipedia calls it a
1:1 wooden model. `tail_number` is blank; BAPC.519 is an alias. Not to be
confused with the museum organisation's genuine Spitfire LF Mk IXe **5553**,
which is a long-term restoration at Swartkop. The two Compton Paterson biplane
replicas (Kimberley and Sci-Bono) likewise carry no serial.

**Untailed rows made distinguishable.** The two INDLELA Impalas are the clearest
case in the country of a blank serial being the honest answer. The pair are known
to be ex-SAAF 486 (c/n 131/6362/A11) and 541 (c/n A66), but the photographer who
documented them on 25 September 2022 said flatly that they could not be told
apart. Assigning either serial to either airframe would be a coin-flip written
permanently into the database. Both carry both candidate serials in aliases and
are separated as "first of two examples" / "second of two examples".

**Airworthy museum aircraft are recorded `on_display`** — the SAAF Museum
Historic Flight's Bosboks, Harvards and Mirages are museum holdings that happen
to fly. Operational SAAF aircraft, aero-club trainers and privately owned
airworthy warbirds based at a field are not records at all.

**Sections are recorded, and said to be sections.** Alouette III 105 (nose) and
635 (cabin) at Port Elizabeth are `in_storage` with the section stated in the
description, not passed off as complete airframes.

**The Jörg IV Skimmerfoil is recorded as `fixed_wing`** despite being a
wing-in-ground-effect craft rather than an aeroplane, because it has fixed wings
and the vocabulary has nothing better. Role `experimental`, no serial.

**Coordinate provenance, because most of these are not geocodes.** The Waterkloof
Buccaneer and Canberra, the Bloemspruit Impala and the SAAF HQ airframe are
**satellite fixes on the airframe itself** (Esri z19–z20), anchored for
Waterkloof on the EXIF camera location of two dated 24 May 2014 Wikimedia
photographs and then centred on the aircraft. Langebaanweg is a fix on the
occupied plinth in the base traffic circle. Swartkop, Ysterplaat and Ditsong are
Aerial Visuals mapped airframe positions. Vic's Viking Garage is a
photographer's own GPS caption on the roof-mounted Shackleton. Dunnottar,
Laerskool Impala, Sir Pierre van Ryneveld and Stellenbosch come from Google Earth
coordinates published with street-level directions to the specific aircraft.
Hoedspruit gate is an **airfield reference point, not a fix** — the Impala was
never located on imagery. Potchefstroom is a **geocoded unit polygon**, not the
helicopter. Port Elizabeth is the weakest coordinate in the set: an approximate
Wikipedia map plot, ±300 m, and it should be re-surveyed.

---

## Excluded, and why — do not re-research these

**Sites that no longer have an aircraft:**

- **Dunnottar Harvard Memorial, Gauteng.** The 7573 identity resolves to
  Swartkop (above), and no dated photograph of the Dunnottar plinth after the
  2000s could be found in ABPic or Commons. No airframe could be honestly
  attributed, so the site was not created. Note the loose end: the Springs
  museum's coverage mentions someone asking whether "the Dunnottar Harvard" has
  arrived there — see open questions.
- **Port Elizabeth Airport gate guards.** Both airframes moved into the museum on
  7 May 2022 (above). The plinths are empty.
- **Emperors Palace casino, Kempton Park.** C-47 6850 hung in the roof from June
  2000, but was **donated to the military history museum in April 2009** and is
  now a Ditsong aircraft. The casino entry survives on stale lists.
- **The "Vampire Nursery", 22 Engelbrecht Street, Krugersdorp.** Vampire T55 274
  is recorded by dehavilland.co.za as a private rebuild project with Hendrik
  Venter at Wonderboom, "Ex Krugersdorp". The display is gone and the airframe is
  a private restoration — excluded on both counts.
- **Vickers Viking ZS-DKH at Vic's Viking Garage.** The garage is named for it,
  but it came down on 5 March 1987 when the Shackleton replaced it, and went to
  the SAA Museum at Rand Airport on 22 January 2017. Only the Shackleton is there.
- **Air Force Gymnasium.** Both its airframes went into Swartkop storage —
  Vampire FB5 207 and Harvard 7731. No display remains.
- **AFB Durban.** Still an operational base, but its display is gone: Mirage F1CZ
  204 went to Ysterplaat, Wasp 85 to the Naval Museum. Nothing left behind.
- **Shackleton 1720, Ysterplaat.** Cut up and sold as scrap after severe
  salt-air corrosion — confirmed by two separate forum members, one of whom used
  it as a corrosion-training airframe at 2 Air Depot.
- **GSB Potchefstroom Bosbok 948.** Moved to Port Elizabeth. Which is why the
  Potchefstroom site holds only Puma 145.

**Bases checked and found to have nothing — a negative result, not a gap:**
AFB Makhado (ex Louis Trichardt), AFB Overberg / Test Flight and Development
Centre, AFB Swartkop's gate area (everything there is museum stock), AFB
Ysterplaat's gate area, SA Air Force College Thaba Tshwane, and every SAAF
technical training unit. **No preserved instructional airframe was found at any
SAAF technical training school anywhere in the country**, which was an explicit
target of the sweep. TFDC's only candidate is an Impala cockpit converted to a
simulator — a cockpit, not a display airframe.

**Not displays:** Impalas 476 and 491, dumped at the **Roodewal bombing range**
in Silver Falcons colours — range targets. Two ex-Thunder City Hawker Hunters
reported September 2023 at a private residence beside the R44 near Stellenbosch —
no public dimension, no confirmed identities. The **Gooney Bar at Reuben's,
Franschhoek**, where the bar counter is a polished C-47 wing — a wing is not an
airframe. Thunder City's other Lightnings, sold for export.

**Excluded for want of an identity:** the "Meteor military drone" under
restoration at the Springs Mine and Military Museum, reported by the Springs
Advertiser on 15 January 2026. Manufacturer, variant and serial were all
unstated, the designation could not be corroborated against any South African
drone type, and `manufacturer` and `model` are both required fields. A row that
would have to invent both is not a row. **This needs one phone call, not more
research.**

---

## Deliberate blanks

**`year_built` is blank on all 197 rows.** Not one construction, rollout,
first-flight, delivery or acceptance date was sourced anywhere in this pass. SAAF
serials are not fiscal-year encoded, so there was not even a bad inference
available to make — but the rule stands and the field stays empty.

**`postal_code` is blank except where a source stated it** (Swartkop 0137,
Ysterplaat 7425, Ditsong 2196, SAA Museum 1401, Kimberley MOTH 8301, Springs
1560). South African postal codes were not guessed, and no reverse-geocoding was
possible — Nominatim and Overpass were both unreachable from the research
environment, which also means **not one coordinate here is a geocode of an
address**; they are satellite fixes, published coordinates, or blank.

**`website` is blank throughout the military sites.** The official base pages on
`af.mil.za` appeared in search results but the domain failed connection checks,
and an unverified URL is worse than none.

**Coordinates blank** at GSB Thaba Tshwane, SANDF Military Academy Saldanha,
Denel Aviation, and most of the monument sites. Street addresses were held for
several of them (33 Memorial Road Kimberley; 115 Dickie Fritz Avenue Edenvale;
Galloway Street Meyerton; 19 1st Avenue Armadale) but a town centroid dressed up
as a coordinate is worse than nothing.

**`tail_number` blank and deliberate** on: the two INDLELA Impalas; the Westland
Scout at Port Elizabeth (carries code GT, no serial established); both Compton
Paterson replicas; the PE Spitfire replica; the Jörg IV; the Springs Mirage III
and Impala (serials never published in any of the 2025–26 coverage); and Mirage
F1CZ 207 at Stellenbosch (the unique-key collision described above — that one is
a schema limitation, not a doubt).

---

## Needs a human on site — ranked

1. **Springs Mine and Military Museum, +27 11 366 1554.** One call closes the
   most gaps of any single action available: the Mirage III serial, the Impala
   Mk I serial, the identity of the "Meteor drone", the site's coordinate, and
   whether the Dunnottar Harvard has arrived there. Founder Tony da Cruz is
   quoted throughout the 2025–26 coverage. This is also the highest-value call
   for *growth* — it is a young museum actively acquiring airframes and no
   directory has caught up with it.
2. **Is the Bloemfontein "Military Museum" holding Impala 591, Impala II 1032
   and Mirage IIIRZ 837 the same institution as the Queen's Fort Military
   Museum?** These three are currently filed under Queen's Fort on the strength
   of a city-centre museum identification. If it is actually the SA Armour Museum
   on the Tempe army base, the site record is wrong and the access type with it.
3. **Where are Sabre Mk 6 369 and Mirage F1CZ 211 at AFB Waterkloof?** Neither
   appears on satellite imagery anywhere on the base; the Sabre is additionally
   absent from Wikipedia's surviving-Sabres list, which records only 361, 367 and
   372 in South Africa. Both rows are single-sourced. If they turn out to be
   inside the controlled area, they need a second `restricted` site record.
4. **Which airframe survives at SAAF Headquarters, Dequar Road — Mirage F1CZ 202,
   Impala 524, or both?** Imagery shows one plinth where the list says two. One
   of those two rows may be a ghost.
5. **Is Impala 519 still on its pad at AFB Hoedspruit?** Single-sourced, absent
   from the 2013 gate-guard inventory, refuted at its alternative location, never
   photographed. **The weakest row in the country.**
6. **Which of the three Langebaanweg airframes is which?** Three plinths
   confirmed occupied on 2026 imagery, three serials listed (Vampire 235, Impala
   576, Harvard 7449), no way to pair them at z18 — Esri publishes no z19 there.
   One ground photograph settles it.
7. **Cheetah R 855 at the Denel campus entrance.** The only reconnaissance
   Cheetah ever built. Its presence on Atlas Road rests on one list; the only
   dated photograph is from 11 August 1991 at Jan Smuts.
8. **Are Puma 126 and Ventura 6432 both still inside the Dickie Fritz compound?**
   The Ventura is traceable to October 2021 and is one of very few complete
   Ventura/PV-1 airframes anywhere; its condition matters. The Puma has nothing
   after 2013.
9. **Has Lightning XR773 at Stellenbosch been finished?** It moved in September
   2023; a forum enquiry in October 2024 drew no progress report. Recorded
   `under_restoration` and may now be on display.
10. **Vampire 235 at Langebaanweg: FB.52 or FB Mk 9?** Two pages on the same
    website disagree.
11. **Does the SAAF Museum's own gate-guard inventory exist in writing?**
    defenceWeb asked in 2021 and was told the request "will be responded to later
    after consultation with higher authority". Nothing has surfaced. It would
    supersede everything in the military-property section of this file.

---

## Coverage gaps worth naming

**KwaZulu-Natal and North West returned almost nothing.** North West has one
record (the Potchefstroom Puma); KZN has **zero**. That is very unlikely to be
true — King Shaka, Virginia and Pietermaritzburg are all obvious candidates — but
nothing surfaced in the sweep. Treat KZN as unsearched rather than empty.

**No Alouette III on a pole exists anywhere in the country**, as far as this pass
could establish, despite it being the type most likely to be one. Every preserved
Alouette III traced is at Swartkop, Ysterplaat or Port Elizabeth.

**OpenStreetMap is useless here.** An Overpass query for `historic=aircraft` or
`memorial=aircraft` across the whole of South Africa returned **zero elements**.
Do not plan a monument sweep around it.

**The "Javelin".** In a September 2023 Stellenbosch thread the club chairman
refers to saving "the Javelin", describing it as "a massive aircraft, way up in
the air" needing a very large crane — i.e. something currently pole- or
roof-mounted. No Gloster Javelin survivor is recorded in South Africa. It is
probably a colloquial name for something else. One call to Stellenbosch Flying
Club.
