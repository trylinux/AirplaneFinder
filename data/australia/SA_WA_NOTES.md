# South Australia & Western Australia — research notes

23 sites, 118 aircraft. Research current to September 2026; the most recent
first-hand evidence used for any airframe is stated in that airframe's
`description`.

---

## 1. Sources used, and how each behaved

### ADF-Serials (adf-serials.com.au) — primary, used for every ADF airframe
The site has been rebuilt on a new CMS since the URLs most references cite.
**`www.adf-serials.com.au` no longer resolves with a valid certificate and
`adf-serials.com` fails TLS entirely; only bare `adf-serials.com.au` works.**
The old flat `2a94.htm`-style paths are partly retired in favour of
`/raaf2/2a94`, `/raaf3/3a3`, `/ran/n4` — but not consistently: A79 (Vampire),
A84 (Canberra), A92 (Jindivik), A24, A58, A65, A77 and A85 are still served
from the old flat paths, while A2, A3, A7, A8, A9, A17, A20, A21, A94 have
moved. Anyone re-running this should scrape `/raaf2`, `/raaf3`, `/ran` and
`/otherraafadf` for the current link table rather than guessing.

Every ADF serial in the CSVs was read off the per-serial disposition rows.
The site is the reason for most of the corrections in section 2.

### Museum and owner sites
- **aviationmuseumwa.org.au** (Bull Creek) — good on narrative, thin on serials;
  its collection index omits several airframes the museum plainly holds
  (Anson, Proctor, Moth Minor, the gliders, the Sabre in storage).
- **saam.org.au** — **blocks scripted requests (HTTP 403) and its
  `/collections.html` is disallowed to fetchers.** The SAAM aircraft list here
  is Wikipedia's, which cites the museum's own per-aircraft pages, cross-checked
  serial by serial against ADF-Serials. `saam.org.au/rockets.html` was readable
  and is the source for the four Woomera-programme rockets recorded at SAAM.
- **classicjets.com** and its `projects/CJFM projects.html` page — current, and
  the only reliable statement of what is left at Parafield.
- **beverley.wa.gov.au** — the Shire's own *Significance Assessment: Beverley
  Aeronautical Collection* is the best source on that town and the only one that
  correctly separates the two Vampires by street address.

### AviationWA (aviationwa.org.au)
Two list pages — "RAAF Association of WA Aviation Heritage Museum, Bull Creek"
and "Other preserved (non-flying) aircraft in Western Australia" — are by a long
way the best WA sweep in existence, with construction numbers and provenance.
**They are stale: the Bull Creek page is © 2013 and the preserved-aircraft page
© 2022**, and the site's last post is October 2025. They therefore miss the
Tornado (2022) and the Hornet (2023) at Bull Creek, and they still show
A79-603 at Pearce and A7-041 at Pearce, both of which have moved. Used for
everything they cover that has not since changed, with ADF-Serials overriding
on ADF airframes.

### aviationmuseum.eu
Leads only, and it proved wrong or stale on almost every list it supplied:
- Its Bull Creek list has a **DH.104 Dove VH-CJS**. There is no Dove: VH-CJS is
  the *prototype DH.114 Heron*, and it left Bull Creek in 2013 for Moorabbin.
- Its Bull Creek list has a **Junkers W.33 D-1925**; the replica went to Camden
  in October 2008 and only an original float section remains.
- Its Lincoln Nitschke list is **row-shifted** — it pairs `A79-602` with
  "DH.104 Devon", `VH-SSX` with "DH.115 Vampire T.35" and labels `A52-28`
  (a Mosquito) a "CA-16 Wirraway III". Nothing from that table was used
  without independent confirmation.
- Its Australia index files **Greenock (South Australia) under Western
  Australia**.
- Its Classic Jets page still lists the full pre-2019 sixteen-aircraft
  line-up as current.

### Others
Wikipedia survivor lists (Vampires, displayed UH-1s) and article wikitext, read
through the MediaWiki API — `en.wikipedia.org` is cache-only to the fetch tool
but the API is reachable by curl. Aviation Spotters Online (a dated March 2021
photo report) is the currency evidence for the Woomera and Edinburgh displays.
airhistory.net photo records dated 2004/2008/2018 are the evidence for the
Greenock replicas. OpenStreetMap Nominatim supplied mapped coordinates.

---

## 2. Corrections made, with evidence

1. **Classic Jets Fighter Museum did not survive as a jet museum.** It closed in
   mid-July 2019 and its collection was dispersed at a final auction. Founder
   Bob Jarrett kept the Corsair and moved the remnants into an adjacent hangar
   at Parafield, which still operates as a public restoration workshop
   (Hangar 107, Anderson Drive). The site record is therefore real and current
   but holds **two** airframes, not sixteen. Confirmed departures from
   ADF-Serials: **Sabre A94-974** sold 2016; **Mirage A3-16** to Queensland Air
   Museum, trucked out of Parafield 19 October 2016; **Macchi A7-025** sold and
   moved to Scone NSW in December 2013; **Meteor A77-867** sold to the Ashburton
   Aviation Museum, New Zealand and exported in 2010.
2. **The Macchi at Bull Creek is A7-066, not A7-025.** It is painted "A7-025"
   in No. 25 Squadron markings and rebuilt using a wing from A7-009. ADF-Serials
   states this on all three serial rows. Recorded as A7-066 with A7-025 in
   aliases.
3. **The Wirraway at Bull Creek is A20-688 but is painted "A20-668"** — a
   restoration error, and it also wears No. 5 Squadron codes BF-R although it
   never served with that unit.
4. **SAAM's F-111C is A8-132, not A8-134.** A8-134 was delivered to SAAM in
   March 2013, then relocated to the Australian War Memorial; A8-132 came from
   ARDU at Edinburgh as its replacement, its stripped cockpit refurbished using
   the forward fuselage of ex-USAF FB-111A 68-0246.
5. **Mirage A3-115 has moved from RAAF Edinburgh to SAAM** (gifted May 2018),
   so it is recorded at Port Adelaide, not inside the Edinburgh wire.
6. **The Beverley Aeronautical Museum building has been demolished** and the
   collection dispersed — items were returned to donors or deaccessioned, and
   the aviation interpretation moved to the Cornerstone Building at 141 Vincent
   Street. The two Vampires remain outdoors in the town and are recorded as a
   single site, "Beverley Aeronautical Collection". ADF-Serials still shows both
   at "Beverley Aeronautical Museum" and asks for news.
7. **The Silver Centenary is no longer at Beverley.** WA's oldest aircraft, built
   1929-30 by Selby Ford and Tom Shackles, was removed from the collection in
   2006 by owner Rodney Edwards and restored to flying condition; it is reported
   kept in the Serpentine area. It is an airworthy privately owned aircraft, not
   a museum holding, and is not recorded.
8. **A79-603 is no longer at RAAF Pearce.** The pole-mounted Vampire outside the
   Officers' Mess broke apart during a 2001 restoration attempt; its flying
   surfaces went onto the pod of A79-620, and the remainder of -620 is now at the
   Amberley Heritage Centre. Pearce therefore has one preserved airframe.
9. **A7-041 has left Pearce for Merredin** (May 2018), so it is recorded at
   Merredin under restoration, not at Pearce.
10. **A94-923 has left Western Australia entirely** — restored at Jandakot by
    Western Warbirds, traded away, and now displayed indoors at a museum in
    Prague. Not recorded.
11. **VH-CJS is a DH.114 Heron prototype, not a DH.104 Dove**, and left Bull
    Creek in 2013 (see section 1).
12. **SAAM's Meteor A77-851 is a cockpit only.** Temora's airworthy Meteor
    VH-MBX is *painted* as A77-851 but is ex-RAF VZ467; the real A77-851 is at
    Port Adelaide. Recorded accordingly so the two do not collide.
13. **SAAM's Sea Venom is RAN N4-931**, wearing its ex-RAF serial WZ931. Recorded
    with WZ931 as the tail number (the identity worn) and N4-931 in aliases.
    Note this is a *different* aircraft from Sea Venom **WZ939**, which left
    Classic Jets in the 2019 auction to an unnamed buyer.

---

## 3. Judgment calls

- **Woomera Missile Park and the Woomera Heritage Centre are one site record.**
  They are one visitor precinct on Dewrang Avenue with a single mud-map of
  exhibits, and the Thunderbird sits at the Heritage Centre end of it. Recorded
  as `public` — Woomera village is open; the range is not.
- **Missiles and rockets are recorded as site aircraft.** Woomera Missile Park
  is a real site record dominated by `missile_rocket` rows (ten of thirteen),
  and SAAM's DSTG-owned Woomera heritage rocket collection contributes four
  more. Models, scale models and instrumentation heads were **not** recorded —
  SAAM's Saturn V model, Europa model, Black Knight model, Skylark
  instrumentation head, Waxwing and Dorado motors and the kinetheodolite are
  components or models, not vehicles.
- **Ikara is coded `anti_ship`.** It is an anti-*submarine* missile and the
  controlled vocabulary has no such value; `anti_ship` is the nearest anti-naval
  category and the description says so.
- **The Mignet Flying Flea is coded `biplane`.** The Pou-du-Ciel is a tandem-wing
  aircraft with two lifting surfaces and the vocabulary offers only
  monoplane/biplane/triplane. Flagged here as a forced call.
- **The Vickers Vimy is `civilian` + `transport`.** The airframe is a converted
  bomber, but it flew the 1919 England-Australia flight on a British civil
  registration as a long-range aircraft, and that is the identity it is
  preserved under.
- **Instructional airframes are recorded.** The six ground-instruction hulks at
  South Metropolitan TAFE, Jandakot are `restricted` and mostly fuselage-only,
  but the spec explicitly covers TAFE campuses and they are real airframes in a
  fixed place.
- **Roadside and private-premises single airframes are recorded** — Bill's
  Machinery at Landsdale, the Forrestdale Mooney, the Northam Aztec, the Myalup
  DC-3 — all as `restricted`, because although each is visible from a public
  road, a member of the public cannot get in.
- **Access types.** Bull Creek, SAAM, Woomera, Merredin, Cunderdin, Geraldton,
  Carnarvon, Beverley, the Vimy at Adelaide Airport, Edwards Wines and The Lily
  are `public`. RAAF Edinburgh and RAAF Pearce are `restricted` — both gate
  guards sit inside a guarded perimeter. The Lincoln Nitschke collection is
  `appointment`: it is a private collection, and the only published opening
  hours come from a directory whose other content about the site proved
  unreliable.
- **Replicas** are recorded with the replica status in `description`, never in
  aliases: the Bull Creek Spitfire "TB592", Sopwith Camel "M6394",
  Santos-Dumont Demoiselle, Bristol Tourer "G-AUDK", Sindlinger Hurricane
  (5/8 scale) and Terrier-Sandhawk; the Geraldton Bristol F.2B VH-UDC (a *flying*
  replica built for television, crashed 1992, rebuilt static); the Greenock
  Mustang "A68-150" and Mosquito "A52-28"; the Cunderdin highway Tiger Moth;
  and both Carnarvon Apollo spacecraft.
- **The two Carnarvon Apollo replicas are `spacecraft` + `space`.** They are
  full-scale walk-in replicas, corroborated by multiple visitor accounts, at a
  museum built on the original OTC Carnarvon tracking station. They are the
  only non-aeroplane airframe records in WA.

---

## 4. Sites and airframes deliberately excluded

- **Broome flying-boat wrecks, Roebuck Bay.** Fifteen Dutch and Allied flying
  boats destroyed in the Japanese raid of 3 March 1942 lie on the bay floor and
  are exposed only on very low tides. They are protected in-situ wreck sites and
  war graves, not preserved or displayed airframes, and no member of the public
  can approach most of them at all. Excluded, with the reasoning recorded here
  rather than silently. The nearby Broome memorials are plaques, not airframes.
- **RAAF Base Learmonth.** A bare base. No preserved airframe or gate guard is
  documented in any source consulted.
- **Whyalla Maritime Museum.** A ship museum built around the corvette HMAS
  Whyalla. No aircraft appear in the council's own listing, the state museum
  network entry, or any aviation directory. Excluded.
- **Royal Flying Doctor Service visitor centres in SA and WA.** The RFDS
  visitor centres holding retired airframes are at Broken Hill (NSW), Alice
  Springs (NT) and Longreach (QLD). No SA or WA RFDS facility with a retired
  airframe on public display was found; the Jandakot RFDS base is operational.
  The nearby Mooney memorial to Robin Miller *is* recorded, as its own site.
- **Vampire A79-606, Serpentine WA.** A private restoration in a shed, owner
  Lenard Cotgrove, last reported progress March 2020. Not on display and not
  accessible. ADF-Serials separately reports the booms of a Belmont Vampire
  marked TA-34 on a property at Hazelmere and calls the airframe's status
  unknown, so the two accounts do not even agree on where it is. Excluded.
- **Winjeel A85-430 (VH-XXV).** Registered to a private owner at Ingle Farm SA.
  A privately owned registered warbird, not a display.
- **Simulators and components.** Bull Creek's Link Trainer and F-111F cockpit
  procedures trainer, its Junkers W.33 float section, its unidentified
  ultralight and mining UAV; Classic Jets' Mirage cockpit rebuilt from a flight
  simulator and its Mustang fuselage build-up; the Canberra A84-220 tailplane
  displayed at the Air Warfare Centre, Edinburgh; the A9-754 fin at 492 Squadron
  HQ, Edinburgh. Cockpit *sections* of real airframes with a known identity
  **are** recorded (SAAM's Meteor A77-851, Bull Creek's F-111C crew module
  A8-140, Bull Creek's Anson VH-WAC, Greenock's Oxford V3475).
- **SAAM "Cessna CC-1" and "Sheppard CS2".** Both appear on the museum's own
  list. Neither designation could be resolved to a manufacturer, configuration
  or provenance from any second source, and `wing_type` cannot be left blank on
  a fixed-wing row. Rather than guess, both are excluded and flagged as open
  questions.
- **Mount Gambier Aviation Museum.** A live proposal, not yet open; the only
  identified holding is an Avro Anson engine. Excluded until it has airframes.
- **Avro Anson Memorial, Clackline WA.** A stone cairn commemorating a 1942
  crash. No airframe.
- **Parafield Aviation Heritage Centre.** Memorabilia in the old fire station on
  Kings Road, appointment-only for groups. No aircraft.
- **Airworthy warbirds based in WA** (the Jandakot and Serpentine L-39, Fouga
  Magisters, T-28, S-211, MiG-15UTIs, CT/4s, Tiger Moths, Stearmans and Yaks).
  These are privately owned flying aircraft hangared at an airfield — explicitly
  outside the spec.

---

## 5. Fields deliberately left blank

- **`latitude`/`longitude` on eight sites** — The Lily (Amelup), Lake Preston
  (Myalup), Bill's Machinery (Landsdale), South Metropolitan TAFE and the Robin
  Miller Memorial (both Jandakot Airport), Forrestdale, Northam and Edwards
  Wines (Cowaramup). Geocoding returned only a street centreline or a locality
  centroid for each, which is not the site. Blank rather than approximate.
- **`year_built` on every row.** No sourced construction, roll-out, first-flight
  or delivery *year* was carried through to a year field; several descriptions
  carry sourced first-flight and delivery *dates* in prose instead. RAAF
  A-serials were kept well away from this field.
- **`tail_number` blank** where the airframe has no recorded identity: the
  Classic Jets P-39Q, the Bull Creek Demoiselle, Heath Parasol, Flying Plank,
  BD-5, Slingsby Gull, Skycraft Scout, Bensen B-8M, Challenge WG362, RotorWay
  Scorpion II and Sandhawk, the Cunderdin memorial Tiger Moth replica, the two
  Carnarvon Apollo replicas, the TAFE R22, the Call-Air A-9 at Landsdale, and
  the Woomera and SAAM rockets. Each untailed row within a file is distinguished
  by manufacturer/model/variant.
- **SAAM Gipsy Moth**: the museum records it only by what appears to be a
  constructor's number, "1074". That is in aliases as `c/n 1074`; the tail number
  is blank.
- **SAAM Fokker F27 variant**: the mark number is left blank. Wikipedia gives
  "F-27-109" citing the museum, which is not a standard mark designation.
- **Bill's Machinery Call-Air**: registration blank. AviationWA believes it is
  VH-MPB and says so is unconfirmed.

---

## 6. Open questions, most consequential first

1. **Auster J/5B Autocar VH-KCC, Kalgoorlie.** AviationWA records it suspended
   from the ceiling of the Business of Mining Gallery at the Australian
   Prospectors and Miners Hall of Fame, donated in 2000. The Hall of Fame's
   trading status could not be established, and if it has closed the aircraft's
   whereabouts are unknown. **Kalgoorlie is not in the site list solely because
   of this** — it is otherwise a straightforward site record. This is the single
   most likely missing site in the two states.
2. **PC-9/A A23-009 at RAAF Base Pearce.** ADF-Serials records it transferred to
   Air Force History and Heritage and displayed as a gate guard at HQ RAAF
   Pearce — and then, in the same row, queries its own entry and notes that c/n
   509 was registered N509RA to Redline Aviation in the USA on 29 February 2024.
   The two cannot both be true. Excluded from the Pearce record pending
   resolution; if the gate-guard entry is correct, Pearce has two airframes.
3. **Jindivik WRE-529 at Parafield.** ADF-Serials places this composite
   (built from parts of at least six Jindiviks) at Classic Jets Fighter Museum,
   previously at the Rohrlach Collection, Tanunda SA. Given the 2019 dispersal
   it is probably gone, but neither its departure nor its retention is
   documented. Not recorded at Classic Jets.
4. **Black Arrow versus Black Knight at Woomera.** A dated 2021 photo report
   lists a Black Knight; two other accounts list a Black Arrow. Both are
   recorded, but one may be a misidentification of the other and the park may
   hold only one large British rocket.
5. **Sea Slug, Blue Streak and Skylark at Woomera** rest on a single undated
   visitor account of the park's mud-map. They are plausible for Woomera but
   are the weakest three rows in that file.
6. **Two Vampires or one at Bill's Machinery, Landsdale?** AviationWA lists
   A79-660 and A79-663 as separate entries and then annotates *both* with the
   same note — "believed to be A79-663 with wings of A79-660, can anyone confirm
   this?" ADF-Serials places only A79-663 there. One airframe recorded.
7. **The rest of the Lincoln Nitschke collection.** Only WH700, A79-602 and
   three photo-documented replicas plus an Oxford front fuselage are recorded.
   Secondary sources also claim Wirraways A20-408 and A20-686, an Edgar Percival
   EP.9 VH-DAV, a Piper Aztec VH-COO, a DH Dove, a Fairey Battle fuselage and an
   Anson MG390 — but that table is demonstrably row-shifted, and ADF-Serials'
   A20-408 history ends in 1945 with no Greenock mention. The collection needs a
   site visit or a current owner list; it is likely under-recorded here.
8. **Greenock Anson identity.** Photographed as AX350 in 2008; a directory says
   MG390. AX350 used.
9. **SAAM "Cessna CC-1" and "Sheppard CS2"** — identities unresolved (section 4).
10. **The Cunderdin crop-duster.** The Wheatbelt tourism listing says the museum
    displays "a crop-dusting plane" as well as the Tiger Moth. No type or
    registration is given anywhere, so it is not recorded; the site may hold two
    airframes rather than one.
11. **Bull Creek Catalina "46624".** The museum displays it in US Navy colours
    with that number, and AviationWA gives c/n 1988. The number is recorded as
    the identity worn; whether it is the airframe's own Bureau Number is not
    established.
12. **Bull Creek Spitfire replica mark.** AviationWA calls it an LF.XIVe replica,
    the museum's own material implies a Mk 22 was the pole-mounted original. It
    is recorded as an LF.XVIe replica painted TB592/NI-V, which matches the real
    TB592; the mark is the least certain field on that row.
13. **Coordinates for the eight blank sites** (section 5) need a satellite pass.
