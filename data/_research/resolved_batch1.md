# Resolved airframe conflicts — batch 1

Research date: 2026-09-12. OSM data used is the overpass.private.coffee mirror,
base timestamp **2026-07-24T11:04:51Z** (queried directly for `historic=aircraft`
nodes within 0.8–1.5 km of every coordinate pair in this batch).

Note on method: I could not obtain dated satellite/Street-View imagery through the
tooling available in this session, so the imagery leg of the method was replaced by
(a) the July 2026 OSM extract queried by coordinate, and (b) Aerial Visuals airframe
dossiers, NMUSAF loan data, HMdb marker transcriptions and site-owner pages. Where
that left a site unverified I have said so rather than guessing.

---

## 1. Douglas TA-4J 158479 (c/n 14284)
VERDICT: NEITHER
CONFIDENCE: high
EVIDENCE:
- Aerial Visuals dossier for TA-4J 158479 c/n 14284
  (https://www.aerialvisuals.ca/AirframeDossier.php?Serial=75876) gives Latest Owner
  or Location as **Veterans Memorial Park of Delta County, Gladstone, Michigan**
  (previously K.I. Sawyer Heritage Museum, Marquette MI by 2010). Neither Illinois
  site appears anywhere in its history.
- Oglesby, Memorial Park holds exactly one airframe, UH-1H 71-20066 c/n 12890
  (https://www.skytamer.com/IL-Oglesby.html; silverhawkauthor Illinois survivors list).
  No Skyhawk.
- Dixon, Veterans Memorial Park holds F-105D 60-0455 and AH-1G 67-15475
  (silverhawkauthor Illinois list; https://dixonveteranspark.org/visit/ names only the
  F-105D "Kay's Baby" and a Cobra). OSM July 2026 has a single aircraft node at the
  Dixon fix, named "F-105D Thunderchief" (node 12726224043, 41.8479/-89.5029).
  No Skyhawk. No OSM aircraft node at all at the Oglesby fix.
- Diagnosis: a "Veterans Memorial Park" name collision — the Delta County MI park was
  matched to Dixon IL, then the text was pasted onto Oglesby.
ACTION: delete id 26718 and id 26698; re-file TA-4J 158479 under Veterans Memorial
Park of Delta County, Gladstone, Michigan.

## 2. Grumman A-6E 152603 (c/n I-151)
VERDICT: NEITHER
CONFIDENCE: high
EVIDENCE:
- Aerial Visuals dossier for A-6E 152603 c/n I-151
  (http://aerialvisuals.ca/AirframeDossier.php?Serial=72308): at Richmond Municipal
  Airport, Richmond **Indiana** since c.1995; moved by road **10 April 2022** to the
  **Wayne County Indiana Veterans Memorial Park, Richmond, Indiana**, where it is on
  permanent display.
- The description text on both rows ("beside Richmond Municipal Airport") is literally
  describing the Indiana site; it was pasted onto two Illinois parks.
- Same negative evidence as #1: Oglesby has only a UH-1H; Dixon has only the F-105D
  and the AH-1G; OSM July 2026 shows no Intruder at either fix.
ACTION: delete id 26716 and id 26696; re-file A-6E 152603 under Wayne County Indiana
Veterans Memorial Park, Richmond, Indiana.

## 3. Bell AH-1F 66-15307 (c/n 20063)
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- aviationmuseum.eu page for the Brooke-Hancock County Veterans Memorial Bridge and
  Park, Weirton WV
  (http://www.aviationmuseum.eu/World/North_America/USA/West_Virginia/Weirton/Brooke-Hancock_County_Veterans_Memorial_Bridge_Park.htm)
  lists exactly two airframes: **Bell AH-1F Cobra 66-15307** and Vought A-7D
  69-6241/PT. That matches the row-A description "second airframe in the same
  memorial park".
- The Aerial Visuals fix quoted in *both* descriptions, 40.390150 / -80.593842, is in
  Weirton WV — ~55 m from the row-A site coordinate and ~1,000 km from Burlington
  Township NJ. The source coordinate is the giveaway: the Weirton dossier was pasted
  onto the New Jersey site.
- No evidence found of any AH-1 at Veterans Memorial Park, Burlington Township NJ.
ACTION: delete id 25622, keep id 25670 (and populate its tail 66-15307 / c/n 20063).

## 4. Bell AH-1F 70-15956 (c/n 20900)
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- HMdb marker for McLeod County Veterans Memorial Park, Hutchinson MN
  (https://www.hmdb.org/m.asp?m=78791) transcribes the aircraft plaque:
  **"Bell AH-1S Huey Cobra", serial 70-15956, production no. 20900**, ex-Intrepid Sea
  Air & Space Museum, dedicated at Hutchinson **2 November 2013**.
- Breckenridge MN does have a Cobra, but it is a different airframe: HMdb marker
  https://www.hmdb.org/m.asp?m=103089 (5th St N / Beede Ave, Breckenridge) gives
  serial **67-1565[1]**, D Troop 1/1 Air Cavalry, memorialising Capt. Alvie J. Ledford
  and WO William C. Pierson III.
ACTION: keep id 27122 (populate tail 70-15956 / c/n 20900); on id 27109 blank the tail
and c/n — Breckenridge's Cobra is real but is 67-15651, not this airframe.

## 5. Douglas C-47A 43-15200 (c/n 19666)
VERDICT: B
CONFIDENCE: high
EVIDENCE:
- Robins AFB official article "A C-47 journey: From Normandy to Robins AFB",
  published **4 October 2024**
  (https://www.robins.af.mil/News/Article-Display/Article/3925487/): C-47A **43-15200**
  "Francis L", NMUSAF loan, flown out of the **Museum of Alaska Transportation and
  Industry, Wasilla** and delivered by C-5 to Robins on **19–20 July 2024** for
  restoration and permanent display.
- Vintage Aviation News restoration article corroborates the move and the ongoing
  rebuild. The Wasilla museum no longer holds it — which is exactly why Aerial Visuals
  flags "not on site" at the Wasilla fix, as row A's own text notes.
ACTION: delete id 27318, keep id 24868.

## 6. McDonnell GF-4C 63-7417 (c/n 0349)
VERDICT: B
CONFIDENCE: high
EVIDENCE:
- Aerial Visuals dossier for GF-4C 63-7417 c/n 0349
  (https://aerialvisuals.ca/AirframeDossier.php?Serial=35201) gives Latest Owner or
  Location as **"American Legion Post 4655, Casselton Robert Miller Regional Airport,
  Casselton, North Dakota"**; loaned to VFW Post 4655 Casselton c.1991, later with
  American Legion Post 4655 at the same airport; most recent photo October 2020 after
  a cosmetic restoration that autumn.
- This also settles the "post affiliation" note carried in both descriptions: the
  NMUSAF loan was raised to VFW Post 4655 and the airframe is now with American Legion
  Post 4655 — same post number, same site, Casselton.
- Row A (Hillsboro ND, Post 4) carries no tail, no c/n, and a description that is
  entirely about Casselton. Note the "Post 4" collision also appears in conflict 15.
ACTION: delete id 27174, keep id 27167.

## 7. Republic F-84F 51-1735
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- Aerial Visuals dossier for F-84F-25-RE 51-1735
  (https://aerialvisuals.ca/AirframeDossier.php?Serial=22802): entered the NMUSAF loan
  programme 1971 and "**August 1971–Present** … on display with Correctionville, IA.
  Displayed in Veterans Memorial Park." Latest Owner or Location: Correctionville, Iowa.
  Its service history includes 101st FIS Massachusetts ANG — which is where row B's
  narrative came from, so B was written off the same dossier.
- OSM July 2026 confirms **two** `historic=aircraft` nodes ~20 m apart at the
  Correctionville fix (nodes 12836763398 at 42.47217/-95.78663 and 12836763399 at
  42.47214/-95.78638), matching "Thunderstreak alongside the Corsair II".
- Hancock Field Syracuse does have aircraft on display (OSM nodes 11948618522/23 and
  13338771191/92), and row B already carries a *different* tail, 46-600. So Syracuse
  holds something, but not 51-1735, which has not moved since 1971.
ACTION: keep id 27148; on id 24421 strip the 51-1735 identity (leave the record, its
tail is already 46-600 — re-research what Syracuse actually has).

## 8. North American F-86F — c/n 191-658
VERDICT: BOTH
CONFIDENCE: high
EVIDENCE:
- Roll Out / Aerospotter census of surviving Argentine Sabres, May 2020
  (https://aerospotter.blogspot.com/2020/05/borrador-los-north-american-f-86f-sabre.html):
  **C-111, c/n 191-658**, on a pedestal at the Escuela de Aviación Militar, Córdoba
  since 1999 (previously Nueva Palmira 1988). Separately, **C-113** at Estancia Santa
  Romana, San Luis, is listed with **c/n unknown** — a composite assembled from parts
  of C-105, C-121 and C-106, in aerobatic-team markings.
- So both sites genuinely hold a Sabre; the c/n 191-658 belongs to Córdoba's C-111 and
  was wrongly attached to the Santa Romana composite. (Row A's own text admits the
  Santa Romana aircraft is a rebuild from C-105/C-121 parts.)
ACTION: keep both; blank the c/n on id 11535 (C-113 at Santa Romana — c/n unknown,
composite), keep c/n 191-658 on id 11398.

## 9. Ilyushin Il-86 CCCP-86000 (c/n 0101)
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- The Il-86 first prototype CCCP-86000 is a documented exhibit of the State Aviation
  Museum of Ukraine at Kyiv-Zhulyany (museum's own exposition page
  https://aviamuseum.com.ua/en/exposition/exposition/kb-ilyushina/177-il-86;
  aviationmuseum.eu photo record; planes.cz photo "CCCP-86000 … preserved Kiev
  Zhulyany").
- The Bykovo site is not an Il-86 at all. OSM July 2026 at 55.6085/38.0870 carries
  three named monument nodes: **"Самолёт Ил-103 RA-10300"** (node 10883969140),
  "Самолёт Aero L-29 01801 ФЛАРФ" (10883969141) and "Самолёт Молния-1 00103"
  (10883969142). RA-10300 — the tail already on row B — is an **Ilyushin Il-103**
  light piston trainer, not the Il-86 prototype. c/n 0101 was misapplied.
ACTION: keep id 32591; on id 34192 blank c/n 0101 and correct the type to Ilyushin
Il-103 (RA-10300) — the Bykovo monument is real, the identity was wrong.

## 10. McDonnell Douglas RF-4C 67-0438 (c/n 2828)
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- East Mississippi Veterans Foundation's own page for the aircraft
  (https://www.emsvf.org/the-phantom) states the park's Phantom is "a former 186th
  Meridian Air Guard RF-4C Phantom II aircraft **67-0438**". The park is at Key Field,
  Meridian — which is what both rows' shared description says.
- Corroborated by Vintage Aviation News ("RF-4C Phantom II arrives in Meridian,
  Mississippi for memorial park") and Meridian Star coverage of its arrival at the
  veterans park.
- D'Iberville is 240 km away on the Gulf coast and has no connection to Key Field or
  the 186th ARW.
ACTION: delete id 26251, keep id 26280 (populate tail 67-0438 / c/n 2828).

## 11. Sukhoi Su-24MR "26" (c/n 0115305)
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- russianplanes.net photo id 345447 (https://russianplanes.net/id345447) of Su-24
  bort **26**, zav. n. **0115305**, is captioned as shot at **ЦМ ВС — the Central
  Museum of the Armed Forces, Moscow, in 2008**, with a note in the record that the
  airframe is actually the Su-24MR prototype T6MR-26. Aircraft card:
  https://russianplanes.net/reginfo/256137.
- Medyn does not appear to hold a Su-24. The detailed Medyn museum survey by igor113
  (https://igor113.livejournal.com/1403378.html, "Медынь ч11: самолеты Су-27 и Л-29")
  documents the site's aircraft as **Su-27 bort 20, zav. n. 36911005705** (plinthed
  September 2017) and an **Aero L-29 bort 74** — nothing else. OSM July 2026 has one
  `historic=aircraft` node at the Medyn fix, node 6558501195 at 54.9496/35.8554,
  named **"Сухой Су-27"**.
ACTION: keep id 11799; on id 37273 blank the c/n 0115305 (and re-check whether Medyn
holds a Su-24 at all — the evidence says its aircraft are a Su-27 and an L-29).

## 12. Lockheed T-33A 52-9171 / QT-33A BuNo 156077 (c/n 580-7225)
VERDICT: A
CONFIDENCE: high
EVIDENCE:
- Aerial Visuals dossier for QT-33A 156077 c/n 580-7225
  (https://www.aerialvisuals.ca/AirframeDossier.php?Serial=74610): taken on USAF
  charge c.1953 as **52-9171**; to USN as **BuNo 156077, QT-33A, 23 March 1973**;
  passed through **Hill AFB (south side), Ogden UT**; and has been at **American Legion
  Post 87, Alexandria Municipal Airport / Chandler Field, Alexandria MN since August
  1992**, photographed on site 2013 and 2019. The "2013 and 2019" sightings quoted in
  row B are in fact the Alexandria sightings.
- silverhawkauthor Minnesota survivors list independently records "Lockheed T-33A
  Shooting Star, s/n **52-9171, c/n 580-7225**, mounted on a pylon" at Chandler Field,
  210 Nokomis Street, Alexandria.
- Hill's holding of this airframe ended in 1992, 34 years ago.
ACTION: delete id 10656, keep id 27102 (add c/n 580-7225; note the Navy BuNo 156077 as
an alternate identity).

## 13. "c/n 1090" — two unrelated Bell airframes
VERDICT: BOTH
CONFIDENCE: high
EVIDENCE:
- The Horsham aircraft is a **Bell H-13G Sioux**, not a Huey: the museum's own exhibit
  page (https://update.wingsoffreedommuseum.org/bell-h-13g-sioux-2/) and the Vintage
  Aviation News museum profile both describe it as an H-13G, restored by volunteers at
  Carson Helicopters and displayed indoors. The museum quotes only "Serial Number 1090",
  which is a **Bell model 47** construction number.
- The Gardermoen aircraft is a **Royal Norwegian Air Force UH-1B, tail 966**, delivered
  1966 and flown by 720 Skvadron — a Bell model 204 with its own, unrelated c/n series.
- Bell 47 c/n 1090 and Bell 204 c/n 1090 are different sequences. The match is spurious;
  there is no single airframe here.
ACTION: keep both; blank c/n 1090 on id 23210 (or tag it as a model-204 c/n distinct
from the model-47 series) so the two stop colliding. No record should be deleted.

## 14. Bell UH-1H 66-16109 (c/n 5803)
VERDICT: B
CONFIDENCE: high
EVIDENCE:
- HMdb marker **"Huey 109"** (https://www.hmdb.org/m.asp?m=233049) is at the **Marion
  County Vietnam Veterans Memorial Park, Fairmont, West Virginia**, by the entrance
  road to East Marion Park Wave Pool, and transcribes the airframe as **UH-1H
  66-16109**, 336th Assault Helicopter Company 1968–71, call sign "Super Slick". The
  memorial's own site (marioncountyvietnammemorial.org) and WV Press coverage of the
  original crew visiting "their old ship" corroborate.
- The Aerial Visuals fix quoted in *both* rows, 39.470564 / -80.131494, **is** the
  Fairmont coordinate — the Fairmont dossier was pasted onto Townsend DE, 400 km away.
ACTION: delete id 25678, keep id 25671.

## 15. Bell UH-1H 67-17562 (c/n 9760)
VERDICT: B
CONFIDENCE: low
EVIDENCE:
- Site A is positively excluded. The silverhawkauthor Michigan survivors list
  (https://silverhawkauthor.com/aviation/aviation-united-states-of-america/warplanes-of-the-usa-michigan-adrian-to-ypsilanti/)
  records the aircraft at **American Legion Post 4, Mount Clemens** as a **McDonnell
  F-101B Voodoo, 57-0430, c/n 608** — not a Huey. The nearest Huey it lists in the
  region is 017031 at VFW Post 1584, Adrian. OSM July 2026 has no `historic=aircraft`
  node within 1 km of the Mount Clemens fix.
- Note the same "American Legion Post 4" mis-join that produced conflict 6 (Hillsboro).
- I could **not** positively confirm a Huey at American Legion Post 423, Orland IN:
  the post's own site (orlandinpost423.org) and Facebook page surfaced nothing, there
  is no OSM aircraft node within 1 km of the Orland fix, and the Aerial Visuals
  dossier for 67-17562 could not be located (the site's search index was returning PHP
  errors during this session; a direct dossier ID for this serial was not findable via
  search). So B is the surviving candidate rather than a verified one.
ACTION: delete id 26814 (Mount Clemens holds an F-101B, not a Huey); keep id 26768 but
flag it for confirmation — verify Orland Post 423 by dated imagery before trusting it.

## 16. Bell UH-1 68-16450 (c/n 11109)
VERDICT: B
CONFIDENCE: high
EVIDENCE:
- Two on-site Flickr photographs explicitly captioned **"UH-1H Iroquois (Huey), U.S.
  Army (68-16450), 1st Cavalry Division (Airmobile), Kentucky, Jeffersontown, Veterans
  Memorial Park"** (https://www.flickr.com/photos/23711298@N07/5823549444 and
  .../5822985675).
- Corroborated by the silverhawkauthor Kentucky survivors list, which carries 68-16450
  at Jeffersontown Veterans Memorial Park.
- Row A's own text undermines itself: it justifies the identity with a block check
  against **FY64 64-13492 to 64-14206**, a range that does not contain 68-16450, and
  its claim that "OpenStreetMap carries a current node on this airframe" does not hold
  — there is no `historic=aircraft` node within 1.5 km of the D'Iberville fix in the
  July 2026 extract.
ACTION: keep id 26234; on id 26246 blank the tail and c/n. Do **not** delete 26246
blind — D'Iberville is described as holding three airframes and the FY64 block note
suggests a genuine but different Huey there; re-research that site's contents.

---

## Verdict tally

| Verdict | Count | Conflicts |
|---|---|---|
| A | 7 | 3, 4, 7, 9, 10, 11, 12 |
| B | 5 | 5, 6, 14, 15, 16 |
| BOTH | 2 | 8, 13 |
| NEITHER | 2 | 1, 2 |
| UNRESOLVED | 0 | — |

**Total: 16.** Fifteen at high confidence, one (15) at low confidence — site A there is
positively disproven, but site B is unconfirmed rather than proven.

### Cross-cutting patterns worth fixing upstream
1. **"Veterans Memorial Park" name collision** caused conflicts 1, 2, 3, 14 and
   contributed to 4 and 16. In 1 and 2 it sent the airframe to the wrong *state*
   entirely (Gladstone MI → Dixon IL; Richmond IN → Dixon IL). Any future match on a
   bare "Veterans Memorial Park" string should be treated as unresolved until the
   state is confirmed.
2. **"American Legion Post 4" collision** caused conflicts 6 (Hillsboro ND vs
   Casselton Post 4655) and 15 (Mount Clemens Post 4).
3. **The Aerial Visuals coordinate quoted in a pasted description is diagnostic.** In
   conflicts 3 and 14 the fix embedded in *both* rows' text points unambiguously at
   one of the two sites. That check alone resolves this class of error cheaply.
4. **Construction-number collisions across different Bell models** (conflict 13:
   model 47 c/n 1090 vs model 204 c/n 1090) are false positives. The dedup key needs
   to be scoped by manufacturer type series, not by bare c/n.
