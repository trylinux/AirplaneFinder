# Central Africa — DRC, Republic of the Congo, Gabon, Chad, São Tomé and Príncipe

9 sites, 14 airframes, imported September 2026. Greenfield — and the last
un-swept part of the continent, closing the gap left when the first West/Central
pass was cut off before starting any of these countries.

**Two countries returned nothing and are documented negatives, not omissions:
the Central African Republic and Equatorial Guinea.** Reasons below.

---

## Sources and their weight

**`spottingmode.com/wro` carried this survey.** It holds 62 locations across the
seven countries — DRC 28, Congo 9, Gabon 9, Chad 7, CAR 3, Equatorial Guinea 3,
São Tomé 3. Every country index and all 62 location pages were pulled, the
per-airframe status codes extracted, and `pre` used as **the shortlist, not the
answer**. It is alive: its front page showed edits dated 8 September 2026, the
day before this work. Its TLS does fail modern OpenSSL as expected —
`curl --ciphers "DEFAULT:@SECLEVEL=0"` worked throughout. Status codes seen here
were `pre`, `std`, `dum`, `dlt` and `i/a`; the compiler's own comment on the
Kinshasa Sabre confirms `dlt` is a **condition** judgement sitting alongside
`pre`, not a separate ownership category.

**aviationmuseum.eu produced a cleaner negative than expected.** Its Africa index
lists exactly twelve countries and **not one of these seven**, so it could not be
mined for names or serials at all. Its separate blog does carry a useful post on
the São Tomé Super Constellations, which is the source of the restaurant-and-
nightclub detail and the "Asas d'Avião" name.

Secondary weight: **AirHistory.net** contributor captions with dates (this is
what independently confirmed the N'Djili MB-326); **aviationsmilitaires.net**
French-language base and air-arm pages (corroborated the Pointe-Noire pair and
the Gabonese Fouga fleet); osintsahel.com citing Scramble for the Equatorial
Guinea Mi-26 identity; Wikipedia for the Nsele park's ownership and access; and
the Friends of São Tomé and Príncipe campaign report of January 2020.

**Imagery currency.** Esri's `identify` endpoint on the World Imagery MapServer
returns per-tile acquisition dates, and it was used at every site so that "is it
still there?" has a dated answer: Kinshasa city 15 Feb 2025 (WV02, 0.5 m);
N'Dolo, N'Djili and Nsele/Maluku all 3 Jun 2022 (WV02, 0.5 m); Pointe-Noire
21 Apr 2021; N'Djaména 3 Nov 2021; São Tomé 17 Sep 2023 (WV03, 0.31 m); Bangui
15 Jan 2023; Libreville and Franceville **only 2017**; Bata **only 2014**. Esri's
tile cache is capped below z18–19 over Pointe-Noire, Bata, Maluku and parts of
São Tomé, which is why some reads are explicitly less confident than others.

---

## The OpenStreetMap sweep, and the mis-tagging problem

Overpass through the agent proxy is unreliable for anything slow — the tunnel
closes after roughly 7–10 s of server-side compute, so area-based and wide-bbox
queries failed repeatedly. The fallback was a single fast bbox query for
`historic=aircraft` / `memorial=aircraft` / `aeroway=aircraft` over 14°S–24°N,
6°E–32°E, plus per-city museum bboxes. Twelve aircraft nodes came back; five are
inside these seven countries.

**One genuine hit:** Gabon node 4987022766 (−1.62241, 13.44430),
`historic=aircraft` + `tourism=attraction`, named "Fouga-Magister". It matches
the spottingmode location to five decimal places — two independent mappings of
the same monument. It is now a record.

**Four mis-tagged, and worth recording so nobody re-opens them:**

- **DRC, nodes 8785688622, 8785688643, 8785689266** near Beni (≈0.485–0.488 N,
  29.47 E), all `historic=aircraft`, named "Avuenue mabakanga", "Avenue kathi
  kameru" and "Avenue volcan". These are **street nodes**: the names are Beni
  avenues, there are no other tags, and the positions are ordinary road
  junctions.
- **Chad, nodes 12573654003, 12580151203, 13598335101** — the three flagged as
  suspect in the previous pass. **Checked and confirmed mis-tagged.** Each carries
  `historic=aircraft` and nothing but a name: بشير عمر ابكر (a personal name),
  القاسم, مساقيط. Two are far out of town — Ngoura is 60 km east of N'Djaména —
  and the third is 9 km north-east of the genuine Broussard monument, in a
  residential quarter.
- **São Tomé node 13687762807** — described in its own tags as "the orange
  remains of an aircraft that crashed 29 July 2019", `model:wikidata` = An-74.
  Same airframe as spottingmode's UR-CKC, coded `dlt`. A crash wreck on the
  aerodrome. Rejected.

The museum-tag sweep found **no aviation museum in any of the seven countries.**

---

## Where the display/derelict line was drawn in the DRC

This is the country where the line matters, so it is set out airframe by airframe.

**Recorded.** **Parc de la Vallée de la N'Sele** — three airliners cut up at
N'Djili, transported ~35 km east and rebuilt on a landscaped hilltop with a loop
access road, paved walkways and a service building, fitted out as a restaurant, a
nightclub and a VIP lounge. The clearest display in the seven countries, and the
satellite settles it on its own. `public`: open year-round, roughly 1,700 weekend
visitors at 50,000 Congolese francs, live public website. **Worth flagging** that
the aircraft sit on ground adjoining Joseph Kabila's Kingakati farm and much of
the French-language press files the story under "Kingakati" — searching the
park's own name lands 12 km west. The park is the operator and the correct site.
**N'Djili MB-326 FG-479** — two contributor communities agree independently on
construction number 6618 *and* on preservation. **N'Dolo C-47 9Q-CTR** — intact,
complete, alone on mown grass well clear of the working apron, with a path to it.

**Rejected as boneyard, by name.** **N'Djili main storage area** — twenty-one
airframes including B737-210C 9Q-CGW, B727-2S2F 9S-AVZ, DC-9-32 9Q-CNR and
TN-AHQ, An-24RV 9Q-CTR, MD-82 9Q-CIB (`i/a`, minus wings and tail), MD-83
9Q-CSZ, three Fokker 50s, DHC-8-402 9S-AKV, HS.125s and a Sabreliner: all `std`,
`dum` or `i/a`. **N'Djili military line** — C-130H 9T-TCB, HS.748 9T-TCP,
MiG-23UB FG-2000 (unserviceable in a hangar after a rear seat fired
accidentally). **N'Djili B727 9T-TCK**, `std`. **Goma** — C-47B 9Q-CAM `dum` and
already removed, Do.228 9Q-CSL `std`. **Kisangani** — An-2 and An-12B 9T-TCI
`dlt`. **Lubumbashi** — Mi-26T 9T-HM15 `dlt`, C-47Bs ZS-NTD and ZS-OJE `dum`,
plus two Fouga Magisters the compiler describes as almost completely overgrown,
and a Cessna 310; the Katanga-era relics here are vegetation, not exhibits.
**Kananga, Kavumu, Beni, Boende, Tshikapa, Moni** — all `std` or `dlt`.
**Kilembwe C-47B 9Q-CWI** — written off after a landing accident and dumped in a
minefield; famous, photogenic, and firmly out. **Tembo MiG-21** — no airframe
linked, no status code, and Esri imagery of 24 Aug 2022 shows nothing
aircraft-shaped at the village airstrip.

**Kamina produced nothing.** aviationsmilitaires.net covers the base's history —
sixty T-6 Harvards and Fouga Magisters from 1953, then Mirage 5M and MB-326K of
Zaire's 2nd Tactical Air Group in the 1970s — and states plainly that it is not
known whether the site still holds military aircraft. It carries no spottingmode
entry at all.

**Mobutu's fleet, asked directly and answered directly: no presidential airframe
in the DRC was ever preserved, as opposed to abandoned.** The Mobutu-era jets
rotted at N'Djili and were broken up. The nearest live thread is Joseph Kabila's
Boeing 707-138B **9Q-CLK**, c/n 17702 — refurbished in Miami, flown to Kinshasa
in January 2013, listed stored at N'Djili since 2018; DeskEco went looking for it
and could get no answer from the Presidency. A stored withdrawn head-of-state
aircraft is a stored fleet, not a display. The government B727 9S-CBA is a
further loose end: reported at N'Djili, then re-registered 9S-ABC and stored at
Harare, where it is no longer visible. Whereabouts unknown; no row.

**National museums checked and empty of aviation:** the Musée National de la RDC
(inaugurated 2019, ethnographic and fine art, 12,000 objects over 6,000 m²), the
Musée national du Congo in Brazzaville, the Musée National des Arts et Traditions
du Gabon (OSM tags it `museum=art`), the Chad National Museum (palaeoanthropology,
Toumaï casts, Sao culture) and the Museu Nacional Forte São Sebastião.

---

## Corrections made, with evidence

**The N'Djili MB-326 is recorded as a K, not the GB the directory lists.**
AirHistory's caption on the same construction number 6618 explains the
discrepancy: the airframe was **built as a K and modified to GB standard**. Both
sources are right about different things; the K is the airframe.

**The Pointe-Noire fighter is recorded as a MiG-15UTI against
aviationsmilitaires.net's "MiG-17".** The construction number 10994819 falls in
the Ulan-Ude plant 99 MiG-15UTI series; the competing page gives no serial and
reads as a visual guess. The disagreement is stated in the row rather than
silently resolved.

**The 9Q-CTR collision is real and is flagged on the record.** That registration
appears twice in the source: on the N'Dolo C-47A c/n 9452 and on a dumped An-24RV
c/n 77310802 at N'Djili. The Congolese register re-issues marks. 9Q-CTR was kept
on the C-47 because the construction number is type-specific.

---

## Judgment calls worth challenging

**The Kinshasa F-86 is the row least comfortable in the direction of
inclusion.** Its only source calls it derelict, and that source's compiler pushed
back on a contributor who claimed otherwise. It was included because the test is
deliberate retention plus public presentation, **condition is explicitly not the
test**, and a Sabre standing on an institutional lawn beside the Route de Matadi
was put there deliberately. But it rests on one source, an unverifiable Italian
serial (MM19542, c/n 442) that no Italian or Congolese account corroborates, and
a satellite read that would not stand alone. `tail_number` and `variant` are both
blank for that reason.

**The Bata Mi-26 is the exclusion least comfortable in the other direction — and
it is why Equatorial Guinea returns empty.** spottingmode codes **3C-LLV**,
c/n 34001212153, `pre` at Bata on a contributor report dated 18 October 2025,
identity flagged to-be-confirmed. Esri imagery of 16 August 2014 shows an
eight-bladed heavy helicopter, rotors spread, on a purpose-built circular pad —
so it has been there at least eleven years. Three things pushed it out: the pad
sits in the landscaped grounds of the **Palacio de África**, Bata's African Union
conference palace, and reads as a **VIP helipad** rather than a plinth;
osintsahel.com, working from Scramble and SIPRI in November 2024, still lists the
aircraft as **air force inventory** — ex-Ukrainian, contracted 2009, delivered
2011 — with no mention of retirement; and there is no public presentation at all,
it is inside a government compound visible to nobody. **A ground photograph would
settle it in one shot.**

**Access types**, judged by how an ordinary person actually gets in: `public` for
the Nsele park (ticketed, open year-round), the Mvengue Fouga (a monument on a
public road) and Asas d'Avião (a working restaurant and nightclub). `restricted`
for the four air bases and for N'Dolo, where the C-47 is inside the aerodrome
boundary. `public` for the Université de Kinshasa — a state university campus the
public walks onto; owner and access diverge here and **access won**.

**Site naming.** Three needed a decision. **Base Aérienne Adji Kosseï** is not a
guess: point-in-polygon testing of the monument's coordinate against OSM military
landuse polygons places it inside the Chadian air force compound tagged
`name:fr=Base ADJ KOSSEÏ` and **not** inside the adjacent French base, which
matters because both are mapped there. **Base Aérienne de Libreville** is
descriptive — OSM has nothing named in that bbox, and no unit designation was
invented. **Asas d'Avião** is the Portuguese name from the aviationmuseum.eu
blog; OSM maps the same spot as a restaurant named "The Airplane" and the 2020
campaign report renders it "As Asas do Plane". The three do not agree and there is
no authoritative local source; the Portuguese form was taken per the language
rule.

---

## Coordinate provenance

Every coordinate is an airframe fix taken from spottingmode's per-location
coordinate, each reverse-geocoded through Nominatim and then confirmed — or
attempted — against dated Esri tiles. **No coordinate is a town centroid.** Two
need explaining: **Pointe-Noire** holds two display airframes 80 m apart and the
site coordinate is the MiG's own fix rather than a synthesised midpoint, with the
Noratlas offset stated in its row; **Libreville** likewise, using the Broussard's
fix. Where a coordinate could not be visually confirmed, the aircraft description
says so rather than quietly implying confirmation.

---

## Deliberate blanks

**Every `year_built` is blank.** Not one airframe here has a sourced construction,
rollout, first-flight, delivery or acceptance date. Construction numbers are
plentiful and sit in `aliases` where they belong; **none was promoted to a year**.

`tail_number` is blank on two rows for different reasons — the **Franceville
Fouga** (the source records the registration as unknown and prints it as "..."; 
c/n 365 is all anyone has) and the **Kinshasa F-86** (see above). All
`postal_code` fields are blank; none of these countries operates a postal code
system that could be sourced to these addresses. `website` is populated only for
the Nsele park and UNIKIN, both confirmed to return HTTP 200/202.

---

## Documented negative results

**Central African Republic: nothing.** All three Bangui entries fail the display
test — a B737-2H4 TL-AEG `dum` with a Beech and an An-2 already deleted; five
stored FACA airframes north of M'Poko (BN-2A-9 TL-KAA, C-130A TL-KNK, Mi-8T
TL-KFB, Mi-24V TL-KJN and TL-KND), which is a stored fleet; and a new March 2026
entry for an Mi-8 10 km east of the airport with **no airframe linked and no
status code**, which the January 2023 imagery is too dark to resolve.

**Equatorial Guinea: nothing**, on the Mi-26 reasoning above. The Malabo entries —
F.28-4000 TJ-ALF, BAe.146-200 3C-AKK, Avro RJ85 3C-MAA, Yak-40s 3C-RIM and
3C-SIR — are all `dum` airport hulks.

**Republic of the Congo: two records at Pointe-Noire, nothing at Brazzaville.**
Maya-Maya's four entries are DC-9-32 TN-AIR, An-32 TN-227, CN-235 TN-228 and
B737-406F 5N-OTT — a stored line, no gate guards. Also rejected at Pointe-Noire:
five stored MiG-21bis (509, 511, 513, 515, 525) and B737s TN-AHK and TN-AIN; the
An-12 TN-AID has been scrapped and the Yak-40 TN-AIW was scrapped in late 2019.

**Chad: one record.** Rejected: C-47s TT-LAC and TT-LAJ and C-54s TT-EAF and
TT-NAB, all `dlt`; stored An-12s 4L-VAL and UR-LTG; Mi-24V TT-OAL; An-26 TT-LAP,
MiG-29 TT-QAP, PC-7s TT-QAB and TT-QAJ; MD-83 SU-BME `dum`; F.28 TT-EAS `dlt`.
**No French Barkhane-era display was found** — the French base is mapped adjacent
to Adji Kosseï but holds no preserved airframe in any source consulted.

**Gabon: three records.** Rejected: MD-81 T9-AAC `dum`; C-130H TR-KKC `dlt` and
being scrapped (a July 2026 update notes it is now minus wings); Caravelle
F-BVSF `dlt` at M'Vengue; the four M'Vengue Fougas at location 20549, which carry
no linked airframes and no status; the Falcon 50 at location 31478; An-2 SP-KMH
`dlt` at Bilanga.

**São Tomé and Príncipe: one site, two airframes.** Rejected: An-74TK UR-CKC, a
July 2019 crash wreck, and Cessna 402A S9-TAK `dlt` on Príncipe.

---

## Ranked open questions

1. **Are the two São Tomé Super Constellations still standing?** The most
   historically valuable airframes in this slice — the last physical remnant of
   the Biafran airlift — and their currency rests on a January 2020 report plus a
   live OSM restaurant node, against 2023 imagery in which two fuselage-shaped
   objects resolve but no wings. One dated ground photograph settles it. If they
   are gone, two rows come out and a significant loss should be recorded.
2. **What is actually on the lawn at Mbanza-Lemba?** Type, condition, and whether
   the MM19542 identity has any basis. Determines whether the UNIKIN row survives
   and whether its tail number can ever be filled in.
3. **Is the Bata Mi-26 a monument or a parked air force helicopter?** The only
   exclusion here that a single photograph could reverse, and the only thing
   standing between Equatorial Guinea and a record.
4. **Which of the three Nsele park airliners is the restaurant, which the
   nightclub, which the VIP lounge?** Sources describe the fit-out collectively.
5. **MiG-15UTI or MiG-17 at Pointe-Noire**, and does the Noratlas still carry
   TN-232 visibly?
6. **Independent confirmation for the two Libreville airframes.** TR-KAB and
   TR-KNC rest on one source, and the only satellite coverage of that block is
   nine years old.
7. **Kamina.** The largest untested airfield in the region — T-6, Fouga, Mirage 5M
   and MB-326K history, and no wrecks-and-relics coverage at all. If anything
   survives in central Africa that nobody has catalogued, it is most likely there.
