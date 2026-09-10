# West Africa — second pass

Closes the gap left when the first West/Central sweep was cut off. **9 new sites,
14 airframes**, imported September 2026, added to the 7 sites and 13 airframes
from pass one (Ghana, Mali, Nigeria, Cameroon). Files here are top-ups:
`wa_museums_topup.csv` plus one aircraft CSV per new site. Pass one's notes are in
`WEST_AFRICA_NOTES.md` and still stand.

Countries newly covered: **Côte d'Ivoire, Burkina Faso, Niger, Guinea-Bissau**,
plus one new Nigerian record. **Eight of the twelve countries in scope returned
nothing** and are documented negatives below.

---

## The headline finding: OSM and the directories both failed here

Everywhere else in West Africa, an **OpenStreetMap Overpass sweep** was the
productive channel — every Ghanaian, Malian and Cameroonian record in the
database came from it rather than from any directory. In these twelve countries it
found **nothing at all in nine of them**. A bounding-box query (lat −2 to 28, lon
−26 to 17) for `historic=aircraft`, `memorial=aircraft`, `memorial=plane`,
`aeroway=aircraft`, `museum=aviation` and `museum=military` returned thirty hits,
of which only twelve fell inside these countries: ten at Banjul, plus the two
already-excluded items. A second sweep for **all** `tourism=museum` returned **191
museums and not one** tagged aviation or military.

**Every record in this pass except Banjul's exclusion came from
`spottingmode.com/wro`** — the reverse of the pattern elsewhere in the region. It
carried 57 locations across the twelve countries and, uniquely, per-airframe
status codes; all 57 location pages were pulled and the airframe tables parsed,
yielding exactly 15 rows coded `pre`, one `i/a`, and the rest `std`, `dum` or
`dlt`. The site is live — its front page showed photos added 8 September 2026,
one day before this research.

**aviationmuseum.eu has zero coverage of all twelve countries**, and it produced a
*new* failure mode worth recording. Probing its `Blogvorm` slug pattern by country
name, `/Blogvorm/niger/` returns HTTP 200 — which looks like a hidden Niger page.
It is not: it 301-redirects to `/Blogvorm/2015/05/08/nigeria/`, titled "Nigeria",
containing only the National War Museum at Umuahia. **A slug collision that would
trap anyone probing that site by country name.** Scramble.nl, the other obvious
orbat source, is behind Cloudflare and returned 403 to every request including
with browser headers, and the Wayback copy is blocked too — so serial-level orbat
data was unavailable and this pass leans on spottingmode's construction numbers
instead. Wikimedia Commons has essentially no corpus here: a category query across
all twelve countries returned exactly one file, an in-flight photo of an Ivorian
Super Puma.

---

## Satellite verification

Esri World Imagery tiles at z18 (z19 is not published over most of this region),
cropped tightly and upscaled, with Google's tile layer as cross-check, and the
acquisition date pulled from the ArcGIS `identify` endpoint for every point.
Dates: Bouaké 11 Feb 2025 (0.34 m); Abidjan air base 15 Mar 2025 (WV02, 0.5 m);
Yopougon 24 Jan 2025 (GeoEye-1, 0.46 m); Ouagadougou both sites 10 Dec 2025 (WV03,
0.31 m); Bobo-Dioulasso 28 Oct 2025 (0.34 m); Conakry 15 Mar 2025 (WV03, 0.31 m);
Bissau **16 Mar 2026** — the most current imagery in the survey; Niamey 29 Jan 2024
(WV03, 0.31 m); Cotonou 15 Jul 2025 (WV02, 0.5 m); Banjul 25 Feb 2026 (0.34 m).
That is the "is it still there in 2026?" evidence for every row.

**All twelve airframe coordinates came from spottingmode's per-location fields,
and every one landed on a visible aircraft-shaped object** — no spottingmode
coordinate in these twelve countries was off, in contrast to the Mali error
documented in pass one. Site coordinates are the source point where a site holds
one cluster; for Abidjan the midpoint of the Puma and Dauphin points (61 m apart)
and for Bouaké the midpoint of the parade-square pair and the traffic-island jet
(118 m apart). Every site was reverse-geocoded and cross-checked with a 130–350 m
Overpass radius query — which is how the Niamey point was tied to "Mess de la BA
101" 200 m away, the Bissau point to the terminal (123 m) and the Osvaldo Vieira
memorial (207 m), the Bobo point to a polygon tagged `military=Base Aérienne 210`,
and the Yopougon compound to a place OSM names "Cité Mangou".

---

## Corrections and judgment calls

**Guinea's MiG-17F "715" is excluded, and this overturns a `pre` code.** The
source records it preserved at 9.58537 / −13.60780, but that update dates from
October 2018, and Esri WorldView-3 0.31 m imagery of **15 March 2025 shows a large
blue-roofed hangar occupying the spot**, confirmed on Google imagery. A wider z17
sweep found no aircraft-shaped object nearby. Either it was scrapped or moved when
the hangar went up. A relocation was searched for — the Monument du 22 Novembre
1970 in Conakry commemorates Operation Green Sea but incorporates no aircraft —
and none found. **Guinea therefore yields nothing.**

**Benin's TY-AAM "Petrel" is excluded and is a deliberate blank.** The source
codes it `pre` with a May 2025 update and gives c/n 049, but **"Petrel" matches no
aircraft type that could be resolved** — absent from the source's own type index,
and none of the Percival, Nash, Slingsby, Huff-Daland, Shenyang or EDRA Petrels
plausibly fits a Beninese Air Force airframe. No aircraft-shaped object is visible
at 6.35143 / 2.38286 on 15 July 2025 imagery. Recording a manufacturer and model
here would be invention.

**The 2004 French destruction question is answered in the negative.** The
airframes destroyed under Opération Licorne were the *active* fleet — two Su-25s
at Yamoussoukro and Mi-24/Mi-8 helicopters at Abidjan. French Ministry of Defence
image archives describe the Yamoussoukro Su-25 hulks going through *dépollution
des épaves* — wreck clearance — so they were scrapped, not memorialised. The
Bouaké Alpha Jets and the Abidjan Puma, Dauphin and Broussard are all former-fleet
types listed under *anciens appareils*; none was part of the 2004 destruction.
**No 2004-destroyed Ivorian airframe survives as a display anywhere.**

**The Cité Mangou site is the weakest record here**, and that belongs on the
record. Two airframes are unambiguously present on maintained grass at a compound
frontage on 24 January 2025 GeoEye-1 imagery, which satisfies the
deliberate-retention-plus-presentation test on its own. But **both types rest on a
single 2019 field note whose own contributor declined to create airframe
records**, and 0.46 m is not enough to confirm a Puma silhouette independently. It
was recorded because a displayed pair is a site; the identities are provisional.

**Access types.** Seven of eight new non-Nigerian sites are `restricted`: six sit
inside working military bases, and OSM carries an explicit note that the Avenue de
l'Aéroport section past the Ouagadougou air base **"has been closed to the public
since 2018 due to security concerns."** The Ouagadougou Cessna is `restricted`
too — set back inside a walled compound with a gated frontage, visible from the
avenue but not enterable. **Bissau is `public`**: the Do 28 stands on the landside
forecourt between the terminal and the Osvaldo Vieira memorial, where anyone
walking to the terminal reaches it. **Jos is `public`** — a plinth in a public road
roundabout.

**Variant blanks and conflicts.** The Abidjan Broussard is left at MH.1521 with no
variant, although Côte d'Ivoire's Broussards were MH.1521M — the source gives
none. The Bobo SF.260 is recorded WL following the construction-number-backed
entry, but GlobalSecurity describes Burkina Faso's armed SF.260s as **WP** — four
of which came direct from Italy and were stationed at Bobo-Dioulasso, exactly
where this airframe stands. Unresolved, and stated in the row. The Ouagadougou
light twin's own source **contradicts itself**, its airframe record saying Ce.310
and its location description Ce.402; both are carried, the conflict is in the
description, and the row is flagged unconfirmed.

**`tail_number` is blank on four rows** for four different reasons: the Abidjan
Broussard (no serial recorded anywhere), the Ouagadougou Cessna (the source's own
record uses the placeholder "XT-XXX", meaning no readable registration), and both
Cité Mangou airframes (no airframe records exist).

**`year_built` is blank on every row.** No source gave a construction, rollout,
first-flight, delivery or acceptance date. Serials such as **BF8401 and BF8423
look like date-bearing serials and are emphatically not treated as such.**

---

## The four open questions from pass one — three closed

**Airforce Roundabout, Jos — CLOSED, and now a record.** It is an **Aero L-29
Delfín, NAF420, c/n 491015**, a plinthed gate guard outside the Air Force Military
School. The spottingmode location record sits 7 m from the plinth centre with
status `pre`. Serial-block corroboration: the NAF's L-29 block is NAF4xx (NAF409,
c/n 993330, is a second preserved L-29 at Kano) while the L-39ZA block is NAF3xx,
which rules out the obvious confusion. Measured from Google z21 imagery the
planform is ~11–12 m in both span and length against the L-29's 10.29 × 10.81 m,
inconsistent with any larger twin — and **the "twin-engine" read from the earlier
pass is explained by the L-29's wingtip tanks**, which from directly overhead look
like nacelles. High confidence on type, medium on the individual serial.

**Airport Road plinth, Ikeja — STILL UNRESOLVED, and probably not an aircraft.**
Deferred, not permanently excluded. Full note:

> Aircraft-shaped white object on a circular plinth in an unnamed walled compound
> on the west side of Airport Road, Ikeja (6.589127, 3.333805). Checked Sep 2026:
> **OSM node 4882134391 "Aircraft"/`tourism=museum` is a single-version 2017
> Potlatch armchair tag with no source — do not cite it as evidence of a museum.**
> Esri has no imagery above z19 here. KartaView sequence 553811 (24 Jul 2017)
> passes within 20 m but every frame faces along the road; the plinth is behind
> the compound wall. Commons geosearch, Wikimapia and spottingmode all negative;
> the compound is unnamed in every gazetteer checked, and the FAAN HQ, Nigeria
> Airways and A1 Hotel polygons all exclude the point. **Measured from Google z21
> imagery the object is only ~7–8 m long** (method calibrated against the Jos
> L-29, which over-reads by 1.5–2 m), too small for any swept-wing T-tailed
> aircraft — it is probably a decorative scale model. Only two things will close
> this: a ground photograph from Airport Road, or identification of the compound's
> occupier. **Do not re-run satellite or gazetteer searches.**

**Camp Lieutenant Amadou Lindor Fall, Thiaroye — CLOSED, permanent exclusion.**
The two aircraft are **parachute ground-training airframes at "Place Dina"**,
inside the camp of the Bataillon des Parachutistes. APS embedded reportage via
SenePlus, 2 January 2025: *"Deux maquettes d'avion, la Fokker F27 et la Casa C-200
pour l'entraînement au sol sont installées dans les lieux"* — followed by an
instructor teaching harness and deployment drills there. Corroborated by OSM ways
1521522205/1521522206 (`historic=aircraft`, traced 25 May 2026) whose measured
outlines, 26.5 × 24.0 m and 17.4 × 14.4 m, match an F27 (29.0 × 23.6 m) and a
C-212 (19.0 × 15.2 m). **Fails the test on both limbs**: the purpose is
instruction and the site is a closed active army camp. **No connection to the 1944
Thiaroye massacre commemoration** — the camp's memorials are a Saint-Michel statue
and a monument aux morts by the command post, and the Thiaroye-80 ceremony of
1 December 2024 was held on the football pitch. Do not re-research.

**"Nigerian Air Force Museum, Kaduna" — CLOSED, does not exist.** The NAF's own
site carries no museum, heritage centre or preserved-aircraft content anywhere.
spottingmode categorises museum sites explicitly — it labels *"Umuahia – National
War Museum, Nigeria, Category: Museums (other)"* — and **none of its 20 Kaduna
locations carries a museum category**. Kaduna's holdings are ~10 individually
plinthed gate guards (`pre`) spread over 9 km, a technical school with 6
instructional airframes (`i/a`) and a dump of 26 (`dum`). **Casual references to
"Kaduna MiG-21s on display" resolve to a single gate guard** — NAF684, c/n
75097106, `pre` since c.2023, pulled out of the Makurdi store; the remaining
Nigerian MiG-21s are stored at Makurdi (13) and Maiduguri (3) and were part of the
fleet advertised for sale in December 2020. Do not re-research the claim.

---

## The two pre-excluded items, independently re-checked and upheld

**UTA Flight 772 Memorial, Ténéré** — appears in OSM as **two duplicate nodes**,
both `memorial=aircraft`. Still a memorial *to* a destroyed aircraft, not a
preserved airframe.

**Cotonou "Avion sur la plage"** — the exclusion is now on firmer evidence, and it
went the other way from what a `pre` code would suggest. It is Benin's only `pre`
entry: 9L-LFB, a Lockheed L-1011-1, c/n 193P-1156, last updated January 2016. The
aircraft was stranded at Cotonou after a 2005 Hajj charter was refused landing in
Saudi Arabia, bought by a Beninese entrepreneur and restored as a leisure complex
called "Barakah" due to open in April 2015; by 2021 it was being written up as an
*abandoned* TriStar on a beach, and the Commons filename describes it as the
*épave d'un avion-restaurant*. **The venture failed and the airframe is now a
wreck.** Exclusion upheld on independent evidence.

---

## Documented negative results — eight of twelve countries

**Togo** — nine locations, every airframe `std`, `dum` or `dlt`. The four
Niamtougou MB-326/EMB-326GB airframes are scattered on unpaved ground with no
display geometry and the source created no airframe records for the location. The
two Ivorian MiG-23MLDs at Lomé, TU-VCH and TU-VCI, are `dlt` — gone. The Musée
National du Togo holds ethnographic, archaeological and zoological material and no
aviation.

**Benin** — the beach TriStar is a wreck; the "Petrel" is unresolvable.

**Guinea** — the MiG-17 is gone under a hangar. The FAG Mi-25s, MiG-21bis 331/552/883
and An-12 EY-408 at Conakry are all `std`; 3X-GEE, 3X-GGN and N139CF `dlt`/`dum`.

**Sierra Leone** — one location, both airframes (9L-LBN, L-410UVP; SLAF-001,
Mi-24V) `dlt`. Both gone. The Sierra Leone National Museum and the Peace Museum
hold no aviation.

**Liberia** — two locations at Roberts Field, both civil and `std` (N747JX, a
G.1159-SP, plus an unrecorded small prop). No monument found at Roberts, Spriggs
Payne or in Monrovia.

**Cape Verde** — one location at Palmeira on Sal: OE-GIZ, a Cessna 650 recorded as
**fuselage only** and `dlt`. Nothing preserved at Sal-Amílcar Cabral; no aviation
content in the Sala-Museu Amílcar Cabral.

**Mauritania** — the Nouakchott L-29 and UH-1 sit on a paved apron with painted
taxi lines and parking markings on Google imagery. **Parking, not display.** Atar
(5T-MAB AB.205A, 5T-MAD Y-12-II) is `std`. The Musée National de la Mauritanie
shows no aviation.

**The Gambia — the specific question asked, answered.** All eight
`historic=aircraft` OSM nodes plus the Il-62 node at 13.34411 / −16.65745 sit in
laterite scrub off the airfield edge with **no plinth, no landscaping, no path, no
signage, and vehicle drag-marks around them**; five of the eight carry
`ruins=yes`. The source codes them `dum` and `std` and marks C5-GNM (Il-62MK) and
the Su-25 as removed. Independently, the two Boeing 727-100s (C5-GAF, C5-GOG) and
the Il-62 were **sold at auction for $500,000 in 2019** to a Gambian commercial
bidder as part of the disposal of Yahya Jammeh's abandoned presidential fleet.
**That is a disposal lot, not a collection. No single Banjul airframe is a
maintained display.** One correction worth recording: the disposal reporting says
the Il-62 has since departed Banjul, but an intact Il-62 is unambiguously present
at that coordinate on 25 February 2026 imagery — so either it never left or a
second Il-62 remains.

**Niger** yields exactly one airframe and it is not in a museum. **The Musée
National Boubou Hama, the large open-air museum that looked like a genuine
candidate, has no aircraft at all** — its outdoor exhibits are the Arbre du Ténéré
mausoleum, a zoo, five traditional-architecture houses and Issoufou Lankondé's
sculptures. The **Mémorial Thomas Sankara** in Ouagadougou likewise has none: the
presidency's own account of a visit naming the statue of Sankara and his twelve
companions, the mausoleum and his office mentions no airframe. Also rejected in
Niger: An-2s LZ-1102 and LZ-1118 at Agadez, recorded as wrecks lying upside down,
and **5U-MAF**, a Noratlas fuselage at Niamey coded `i/a` — instructional, not a
display.

**Also rejected in covered countries.** Abidjan and Jacqueville: TU-VAF (G.III),
TU-VHL (Mi-8PS), TU-VHW/TU-VHX (AS.365N2), TU-TGX/TU-TSP (Jetstreams) all `std`;
TU-VBA (Cessna 421B at Bouaké) `std`; the whole Jacqueville fuselage farm
(XT-FZP, XU-RKA, XU-RKC, TU-TDC, TU-TDN, TU-TIX, 3C-LLF, 3C-LGP, SX-CVP sectioned,
TU-TLA) `dum`/`dlt`; TU-TIH an F.27 burned-out wreck. Ouagadougou: XT-BBE and
XT-BFA (B727s) `std`, XT-MAL/XT-MAN (HS.748), XT-MAK (N.262C), XT-MBE (CN-235),
XT-MAE (MH.1521M), XT-MAS (Cessna 150), XT-MAV (MS.890B) all `dum`. **BF8473**, an
SF.260W the source codes `pre` at Ouagadougou, is marked *Removed* and is not
recorded.

---

## Ranked open questions

1. **What is TY-AAM at Cotonou?** A `pre`-coded airframe with a construction
   number, a type name matching nothing, and no satellite signature. Resolving
   "Petrel" either adds Benin's only record or closes the country properly.
2. **The ~10 preserved gate guards at NAF Base Kaduna.** Each has a registration,
   c/n, coordinate and `pre` status — Do 27A-4 NAF157 and NAF153, Do 28D-2 NAF177
   and NAF198, MiG-21bis NAF684, Bulldog 123 NAF233 and NAF229, P.149D NAF210,
   MiG-17 NAF634 and MiG-17F NAF630, F.27 NAF907, Mi-34S NAF555, L-39ZA NAF363.
   **This is the largest single block of unrecorded verified African airframes
   left**, and it fell out of the Kaduna-museum investigation rather than being
   searched for. A Nigeria base pass should start here.
3. **A second preserved Jos airframe**, 450 m east of the roundabout at 9.87064N
   8.89072E — a Piaggio P.149D, registration unknown, remark "As 211", `pre`.
   Almost certainly at the Air Force Military School itself and a separate site.
   Caution: NAF211 (P.149D c/n 291) is listed `dum` at Kaduna, so the Jos aircraft
   **wears** 211 rather than necessarily being it.
4. **Where did Conakry's MiG-17F "715" go?** Scrapped when the hangar went up, or
   relocated within the base? One ground photo dated after 2019 settles it.
5. **What institution owns the Ouagadougou Avenue de la Révolution Cessna, and is
   it a 310 or a 402?** The ASECNA-DGAC recreation ground is 135 m north-east and
   the Aéro-club de Ouagadougou is a plausible operator, but the compound could
   not be tied to either.
6. **What are the two Cité Mangou airframes, and are they publicly viewable?** A
   street-level photograph would upgrade or demolish this record.
7. **Do the three Bouaké Alpha Jets carry the serials assigned to them?** No
   airframe there has been photographed at ground level in any reachable source,
   and painted markings on retired trainers are notoriously unreliable.
8. **Does the Banjul Il-62 still exist as of late 2026**, given the 2019 sale, the
   report of its departure, and its clear presence in February 2026 imagery?
