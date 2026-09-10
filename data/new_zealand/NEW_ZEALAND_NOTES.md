# New Zealand — research notes

Greenfield build. Before this pass the database held **no** New Zealand records at all.

**Result:** 23 sites, 343 aircraft. `country` = `New Zealand`, `region` = `Oceania`
on every row; `state_province` is the New Zealand region name.

Research window: September 2026. Every museum's own website was checked live in
that window where one exists.

---

## 1. Sources used, and how each performed

### Primary — museum-published, current

| Source | Used for | Verdict |
|---|---|---|
| `airforcemuseum.co.nz/aircraft/` and its 38 per-airframe pages | Air Force Museum of New Zealand | **Best source in the country.** Each page gives the RNZAF serial, the display identity if different, the manufacturer's number, *and the current display location inside the building* ("On display in the Aircraft Hall", "Currently stored in the Reserve Collection", "In storage in No. 2 Hangar"). This is where every AFM `display_status` came from. |
| `aviationmuseum.co.nz/our-exhibits/` (Ashburton) | Ashburton Aviation Museum | Excellent — an accordion entry per airframe with registration in the heading and provenance in the body. Two aircraft (Chrislea Super Ace, Percival Provost) genuinely have no registration published. |
| `classicflyersnz.com/museum/Aircraft+Exhibits.html` | Classic Flyers NZ | Good prose per exhibit, registrations for most. Does not cover the whole collection. |
| `ferrymeadaero.org.nz/about/` | Ferrymead Aeronautical Society | Complete inventory with registrations; no display status. |
| `nzwarbirds.org.nz/visit-us/ardmore-collection/` | NZ Warbirds | Types and a status word per airframe, but **no registrations at all**. |
| `omaka.org.nz` | Omaka | Rich exhibition prose, **no inventory list and no registrations**. Its address changed to 14 Rosina Corlett Lane (via Aerodrome Road); older sources still say 79 Aerodrome Road. |
| `croydonaviation.co.nz` | Croydon | Marketing-level only; names six aircraft, no registrations. |
| `southwardcarmuseum.co.nz/aircraft` | Southward Car Museum | Short catalogue with the Vampire serial and Tiger Moth registration. |
| `gam.org.nz` / `gisborneairport.nz` | Tairāwhiti Aviation Museum | Names four aircraft types, no registrations. |
| `tatatm.co.nz` | Taranaki (TATATM) | Names only "Harvard". |

### Registry / serials

- **adf-serials.com.au `/nz-serials/`** — the NZ arm of ADF-Serials. Decisive for the
  Skyhawk thread: gave fate and current holder for every NZ62xx serial. Note the
  server returns HTTP 406 to `curl`; it is reachable through a normal browser
  user-agent path only.
- **skyhawk.org (The Skyhawk Association)** — independent second source on the same
  fleet; agrees with adf-serials on every museum allocation.
- **nzdf-serials.co.nz** — the successor site. **Stale/broken in 2026:** its TLS
  certificate does not match the hostname and the type pages 404. Could not be used.

### Secondary

- **aviationmuseum.eu** — surprisingly the single most productive discovery source
  for New Zealand. Its NZ index turned up six sites no other list mentioned
  (Geraldine, Gore Air Force and Ag-Aviation, NZ Helicopter Heritage, Founders
  Heritage Park, South Canterbury Aviation Heritage Centre, and Te Papa's single
  aircraft). It also publishes registration lists for museums that publish none
  themselves. Treated as secondary because its lists are undated and, as noted
  below, it duplicates several registrations across two sites.
- **motataircraft.blogspot.com** — a volunteer's per-airframe blog on MOTAT.
  Deep provenance and the only source that tracks aircraft *out* of MOTAT
  (V-1 to the Air Force Museum, Swordfish replica to Classic Flyers, Wasp to
  Torpedo Bay). Last major update February 2024.
- **nzcivair.blogspot.com** — dated field reports; the July 2024 Classic Flyers
  post is the currency evidence for the Vampire/Skyhawk hangar shuffle there.
- **Wikipedia** survivor lists (Vampires, Skyhawk in NZ service) and museum
  articles — leads only, and several were wrong (below).
- **kiwiaircraftimages.com** — thorough per-type survivor lists, but its own pages
  are stamped "Last Text Update 22 February 1999". Leads only.

### Sources that proved stale, and how

- **Wikipedia, Air Force Museum of New Zealand** — its aircraft list is materially
  out of date against the museum's own pages:
  - Bell 47G-3 Sioux given as **NZ3705**; the museum's page says **NZ3706**.
  - Skyhawk **NZ6205** listed as an "A-4C". It is an A-4K; there were never any
    RNZAF A-4Cs.
  - Curtiss listed as a **P-40F**; the museum's page calls it a P-40E.
  - Omits the Schleicher Ka 4 glider ZK-GBQ entirely.
- **Wikipedia, MOTAT** — no inventory at all; the separate `MOTAT collections`
  article is far better and is what was used.
- **kiwiaircraftimages Vampire page** — 1999 vintage: places NZ5765 and NZ5751 in
  RNZAF Museum store and NZ5767 at Ohakea. All three have moved since (NZ5765 went
  to the Fighter Pilots Museum and then Warbirds & Wheels; NZ5751 and NZ5767 are
  now at Classic Flyers).
- **New Zealand Fighter Pilots Museum, Wanaka** — the prompt asked whether it still
  operates. **It does not.** It closed in March 2011 and was replaced in December
  2011 by Warbirds & Wheels. Not recorded as a site.
- **Warbirds & Wheels, Wanaka** — also closed, in September 2021, after the death
  of one of the owners and the COVID collapse in tourism. Its domain
  `warbirdsandwheels.co.nz` now 302-redirects to an unrelated business. Not
  recorded as a site; see open questions for its airframes.
- **Agricultural Heritage Museum, Mystery Creek, Hamilton** — listed by
  aviationmuseum.eu as **Closed**, with DC-3 ZK-SAL "Highland Duster". Not
  recorded; current whereabouts of ZK-SAL unknown.
- **The Vintage Aviator Museum, Hood Aerodrome, Masterton** — TripAdvisor reviews
  report "Closed until further notice" and the company describes itself as a
  manufacturer offering occasional hangar tours, not a museum. No per-airframe
  inventory is published. Not recorded; see open questions.

---

## 2. Corrections made, with evidence

1. **Bell 47 Sioux at the Air Force Museum is NZ3706, not NZ3705.** The museum's own
   page for the airframe gives "RNZAF serial no. NZ3706, Manufacturer's no. 6518".
   Wikipedia's NZ3705 was not followed. Noted in the row's `description`.
2. **Skyhawk NZ6205 recorded as an A-4K, not an A-4C.** The RNZAF operated A-4K,
   TA-4K, ex-RAN A-4G and TA-4G only. The museum page is titled
   "McDonnell Douglas A-4K Skyhawk – NZ6205".
3. **"NZ6207" at the Air Force Museum is not NZ6207.** adf-serials records the real
   NZ6207 as destroyed near Bulls on 18 October 1974, and says the display aircraft
   is a substitute; the Skyhawk Association names it as ex-USN **A-4L 149516** on
   loan. Recorded with `tail_number` = `149516` and `NZ6207` in aliases, not the
   reverse. The museum's own 2026 index no longer lists it at all — flagged in the
   description and in the open questions.
4. **Beaver "NZ6001" at the Air Force Museum is not the Antarctic Beaver.** The real
   NZ6001/NZ6010 was written off on the Beardmore Glacier in January 1960 and is
   still there. The museum airframe is ex-VH-AAL / **ZK-CMW**, a 1957 Australian
   aircraft brought to New Zealand in 1965 for topdressing. `tail_number` = `ZK-CMW`.
5. **Mustang at the Air Force Museum.** Wikipedia gives its identity as "F-367", the
   Indonesian Air Force serial. The primary identity is USAAF **44-74827**; F-367
   and the display identity NZ2410 are aliases. Never served with the RNZAF.
6. **Devon NZ1813 is at Ohakea, not MOTAT.** The MOTAT collections record states it
   went to MOTAT in 2010, was displayed from 2012, and **returned to Ohakea in
   August 2018**. Recorded once, at RNZAF Base Ohakea, on loan from the Air Force
   Museum.
7. **The V-1 / JB-2 is at the Air Force Museum, not MOTAT.** The MOTAT aircraft blog
   post is titled "JB-2 (V-1) 'Loon' Flying Bomb — Donated to RNZAF Museum,
   Christchurch" and quotes the Air Force Museum's own delivery announcement.
8. **The Swordfish replica is at Classic Flyers, not MOTAT.** MOTAT collections lists
   it under aircraft that have left; Classic Flyers' inventory contains it (DK791/4C).
   aviationmuseum.eu still lists it at both.
9. **Vampire NZ5767 is at Classic Flyers, not Ohakea.** Kiwi Aircraft Images (1999)
   has it as a fuselage on display at Ohakea; the July 2024 nzcivair report has it at
   Classic Flyers being prepared for a plinth.
10. **Fletcher ZK-CTZ is at MOTAT, not on the Hamilton Airport plinth.** The MOTAT
    blog says so explicitly and adds the plinth-display history.
11. **Corsair NZ5648/ZK-COR is at Omaka, not Masterton or MOTAT.** MOTAT collections
    records the move. Not recorded as a site holding — it is privately owned (see
    exclusions).
12. **Mangaweka DC-3 is ZK-APK and it is gone.** Removed from the hillside in 2021
    over structural concerns; moved first towards Shannon and then, per the
    Mangaweka community's own 2024 account, to Auckland for restoration. No public
    display site exists for it now, so no record was created.

---

## 3. Judgment calls

**Replicas.** Recorded, with replica status in `description` only, never in
`aliases`. Fifty-one rows record a replica or reproduction — a very
high proportion, driven by Omaka's Knights of the Sky exhibition (roughly two thirds
of that WWI collection is replica) and by the New Zealand habit of full-scale
pioneer reconstructions (three Pearse monoplanes at MOTAT, one each at Classic
Flyers, South Canterbury and the Waitohi memorial; the Pither 1910 monoplane at
Croydon and again at South Canterbury; the Blériot XI at the Air Force Museum and
another at Southward).

**Airworthy museum collections — recorded.** Following the spec's HARS/Temora rule:
- **Croydon Aviation Heritage Centre** is the extreme case — "nearly all of the
  aircraft on display actually fly", maintained by the co-located Croydon Aircraft
  Company. All 28 are recorded as the museum's display collection.
- **NZ Warbirds at Ardmore** — the association's own "Ardmore Collection" page marks
  each airframe. Everything marked *"On Display"* is recorded, airworthy or not.
  Two airframes marked *"Airworthy — At Ardmore"* rather than "On Display" — the
  **Goodyear FG-1D Corsair** and the **Cessna L-19/O-1 Bird Dog** — were **excluded**;
  that wording reads as based-at-the-field rather than on display, and the Corsair
  is separately documented as privately owned. This is the least certain inclusion
  boundary in the whole set.
- **Omaka's WWI collection** is on long-term loan from the 14-18 Aviation Heritage
  Trust (Sir Peter Jackson) and several airframes are flyable. The prompt asked to
  record what the museum displays, not the private hangar residents; that is what
  was done, and the loan is stated in every WWI row's `description`.
- **Classic Flyers** holds several syndicate-owned but publicly displayed aircraft
  (Harvard ZK-ENE, Yak-52 ZK-YAC, Stearman ZK-XAF). Recorded, ownership noted.

**Access types.**
- `public` on 21 sites, including the two that are single airframes in the open
  (Wanaka Airport gate guard, Richard Pearse Memorial lay-by).
- `appointment` on the **New Zealand Helicopter Heritage Museum**, Eyreton — its own
  listing says "open via reservation".
- `restricted` on **RNZAF Base Ohakea** only. Its Vampire gate guardian, composite
  Skyhawk and Devon are all inside the wire; a member of the public cannot walk up
  to them.

**Sites that are one airframe.** Six records exist purely because a single aircraft
is displayed there: Te Papa (Tiger Moth ZK-AJO), Founders Heritage Park Nelson
(Bristol Freighter ZK-CLU), Geraldine (Simmonds Spartan ZK-ABZ), Torpedo Bay Navy
Museum (Wasp), Wanaka Airport (MB-339 NZ6468 on a pole), Waitohi (Pearse memorial
replica). Per the spec these are site records, not exclusions.

**`model` / `variant` splits.** Base designation only in `model`:
`MB-339`+`CB`, `A-4`+`K`, `TA-4`+`K`, `P-40`+`E`, `UH-1`+`H`, `P-3`+`K2`,
`C-130`+`H`, `DH.100`+`FB.5`, `DH.115`+`T.11`, `S.25`+`MR.V`. Dot forms
(`DH.82`, `AS.10`, `S.45`) do not trigger the dashless-alias rule but the popular
name is always present as an alias.

**Local manufacturers used where the airframe was locally built:**
`Pacific Aerospace` and `New Zealand Aerospace` for CT/4 Airtrainers,
`Air Parts (NZ)` for Fletcher FU-24s, `AESL` for the Airtourer,
`de Havilland Australia` for the MOTAT Mosquito (built at Bankstown as A52-19),
`Government Aircraft Factories` for both GAF Canberras,
`Commonwealth Aircraft Corporation` for the CA-28 Ceres.

---

## 4. Excluded, and why

**Closed sites** — New Zealand Fighter Pilots Museum (closed 2011); Warbirds &
Wheels, Wanaka (closed September 2021); Agricultural Heritage Museum, Mystery Creek
(listed as closed).

**Not open to the public / no published inventory** — The Vintage Aviator Ltd and
its Masterton museum; Old Stick and Rudder Company, Masterton. Both are private
operations at Hood Aerodrome; the museum is reported closed indefinitely.

**Privately owned airframes merely based at a museum's field**, excluded per the spec:
- Goodyear FG-1D Corsair NZ5648 / ZK-COR (Old Stick and Rudder; now at Omaka).
- Spitfire Tr.9 MJ730 / ZK-WDQ, listed at Classic Flyers by aviationmuseum.eu but
  absent from the museum's own exhibits page.
- Spitfire LF Mk.IXc PV270 / ZK-SPI (Brendon Deere, based at RNZAF Ohakea) —
  privately owned and airworthy, not a base display.
- Catalina ZK-PBY (NZ Catalina Preservation Society), Mustangs ZK-TAF and ZK-SAS,
  the several privately owned Harvards, and the various airworthy Tiger Moths at
  clubs around the country.
- The Spitfire Mk.XIV and Fw 190 replica **were** included at Omaka, because both
  Wikipedia and the museum's own exhibition text place them inside the Dangerous
  Skies displays even though they belong to the Chariots of Fire collection. Their
  descriptions say so.

**Not aircraft** — MOTAT's Link Trainer and Ashburton's Link Trainer and ATR 72-500
simulator (ground trainers); Ashburton's Bofors 40 mm gun; Classic Flyers' ATR
72-212A ZK-MCJ (reassembled by the museum's engineers but now in use by JNP Aviation
Ltd as a ground-crew training airframe, not a museum exhibit); MOTAT's unidentified
early hang glider (no identity of any kind published).

**Departed New Zealand** — Republic P-47D 42-8066, formerly MOTAT then donated to
the Air Force Museum, since in Australia with HARS and advertised for sale in 2024;
Mosquito T.43 NZ2308 / ZK-PWL, restored by Avspecs and now with Lewis Air Legends,
Texas (first post-restoration flight March 2024); Corsair NZ5612 (now airworthy in
the USA); TA-4G NZ6255 (Fleet Air Arm Museum, Nowra, Australia — an Australian
record, not a New Zealand one); the eight A-4Ks and TA-4Ks sold to Draken
International (N141EM–N147EM).

---

## 5. Fields deliberately left blank

- **`latitude`/`longitude` on 7 sites**: Gore Air Force and Ag-Aviation Museum,
  Taranaki (TATATM), Tairāwhiti Aviation Museum, Geraldine, South Canterbury
  Aviation Heritage Centre, NZ Helicopter Heritage Museum, Richard Pearse Memorial.
  No mapped position could be confirmed to 4 dp for the museum building itself, and
  a town centroid is not the site. The 16 coordinates that are populated come from
  Wikipedia/Wikidata `coord` values for the museum or its airfield.
- **`tail_number` on 74 rows.** Blank beats a guess. The largest blocks are
  NZ Warbirds (14 of 25 — the association publishes no registrations) and the WWI
  and replica airframes at Omaka and elsewhere that carry only period markings.
  Where an airframe carries only a false or period marking (Omaka's Fokker E.III
  `105/15`, Morane-Saulnier `316`, Bristol Fighter `D-8040`), that marking is used
  as `tail_number` because it is what the airframe wears, per the spec.
- **`year_built` on 308 of 343 rows.** Populated only where a construction,
  roll-out or delivery date was actually sourced. **No RNZAF `NZ`-serial and no
  BuNo was ever read as a year.** NZ6201 is not 6201; NZ5757 is not 5757.
- **`model_name`** blank wherever it would merely echo the designation
  (Avro 626, MiG-17, Yak-52, B-17 has one so it is populated, MB-339 has none).
- **`aircraft_name`** populated on only 8 rows — the airframes that genuinely carry
  individual names: *Britannia*, *Aranui*, *Miss Jacy*, *Manu Ruuri*, *Mokai*,
  *Matapouri*, *Gloria Lyons*, *Full Noise*.

---

## 6. Registration conflicts left unresolved in the data

Four registrations are claimed by two sites in the available sources. In each case
the museum's own page was preferred and the other row's `tail_number` was blanked,
with the conflict written into both descriptions:

| Registration | Claimed by | Recorded at | Blanked at |
|---|---|---|---|
| `ZK-HFU` (Bell 47G-3B) | Ashburton's own exhibits page; aviationmuseum.eu for NZ Helicopter Heritage | Ashburton | NZ Helicopter Heritage |
| `ZK-HHY` (Hughes 269C/300C) | Ashburton's own exhibits page; aviationmuseum.eu for NZ Helicopter Heritage | Ashburton | NZ Helicopter Heritage |
| `ZK-AIN` (Tiger Moth) | MOTAT's own records; aviationmuseum.eu assigns it to a Croydon **Moth Minor** | MOTAT | Croydon Moth Minor |
| `ZK-GCD` | aviationmuseum.eu gives it to both a Classic Flyers Cessna 337 **and** a Classic Flyers Slingsby Swallow | Slingsby Swallow | Cessna 337 |

Two further conflicts are recorded in the row description rather than resolved:

- **Wasp at Torpedo Bay** — the Air Force Museum's own Wasp page says the surviving
  RNZN Wasp in the Navy Museum collection is **NZ3902**; MOTAT collections says the
  Wasp that returned to Torpedo Bay from MOTAT was **NZ3909**; aviationmuseum.eu
  still lists NZ3902 at MOTAT. Recorded once, at Torpedo Bay, as NZ3902 with
  NZ3909 in aliases.
- **Ferrymead Vampire** — the society's own page says **NZ5775** (composite);
  aviationmuseum.eu and Kiwi Aircraft Images both say **NZ5758** (ex VZ838,
  INST196). The society's own page was followed.
- **Air Force Museum Skyhawk c/n** — the museum's pages give manufacturer's number
  **14097** for both NZ6205 and NZ6254. One of the two is a copy-paste error on the
  museum's site; neither was written into `aliases`.

---

## 7. Open questions, ranked

1. **Where are the six Warbirds & Wheels airframes now?** The Wanaka museum closed in
   September 2021 holding Skyhawk **NZ6202** (BuNo 157905), Vampire FB.5 **NZ5765**,
   Strikemaster Mk.88 **NZ6374**, Hurricane Mk.IIa replica P3351/K, Hiller UH-12E
   ZK-HBL and an S.E.5a replica. Nothing found in 2026 says where they went. This is
   the single largest gap: six airframes, one of them an RNZAF Skyhawk, unaccounted
   for. The MB-339 NZ6468 now on a pole at Wanaka Airport is a *different* aircraft
   and is recorded.
2. **Is A-4L 149516 (displayed as NZ6207) still at the Air Force Museum?** Two
   independent registries say yes; the museum's own 2026 aircraft index lists only
   NZ6205 and NZ6254. Recorded with `in_storage`, but it may have been disposed of.
3. **The Mangaweka DC-3 ZK-APK.** Removed 2021, reported in Auckland for restoration.
   Who holds it, and will it become a public display? A famous roadside airframe with
   no current site record.
4. **DC-3 ZK-SAL "Highland Duster"** — was at the now-closed Agricultural Heritage
   Museum at Mystery Creek, Hamilton. Present location unknown. Waikato currently has
   **zero** sites in this data set, which is implausible for a region with Hamilton
   Airport, the Fieldays site and a long topdressing history.
5. **RNZAF Base Auckland (Whenuapai) and RNZAF Base Woodbourne.** Both were swept and
   no confirmable preserved airframe or gate guard was found for either. Ohakea is the
   only base recorded. Woodbourne in particular held stored Skyhawks and instructional
   airframes for years and almost certainly retains something; base-side displays are
   simply not documented on the open web.
6. **NZ Warbirds registrations.** Fourteen of the 25 Ardmore rows have no tail number
   because the association publishes none. The Vampire T.11, the Bell 47 Sioux and all
   six WWI replicas are the priority — a visit or a direct enquiry would close this.
7. **Omaka's per-airframe identities.** The museum publishes no inventory. The 44 rows
   rest on aviationmuseum.eu registrations cross-checked against Wikipedia; nothing
   from the museum itself confirms them. In particular the Fokker D.VIII and the
   Thomas-Morse S-4 appear on Wikipedia but not in the eu inventory, and the Skyhawk
   NZ6216 appears in both registries but in none of the museum's own text.
8. **Tairāwhiti (Gisborne) and TATATM (New Plymouth) inventories.** Four rows each,
   all from third-party or one-line descriptions. Gisborne's DC-3, Avenger, Fletcher
   and Tiger Moth all need registrations.
9. **The RSA and town-park thread was not productive.** Systematic searching for
   Returned and Services' Association clubs, playgrounds and town parks with an
   airframe turned up references (the Blenheim playground Vampire NZ5701, the
   playground Vampire that became Ashburton's NZ5769) but every specific example
   found had *already* been recovered into a museum. If roadside single airframes
   still exist in New Zealand they are not indexed anywhere reachable; this would
   need Google Street View sweeping rather than text search.
10. **Northland, Hawke's Bay, West Coast and Waikato have no records.** Dargaville
    Museum, Kaitaia, Napier/Hastings and the West Coast were all swept without
    result. Four regions with nothing is the clearest signal that the discovery
    sweep is incomplete rather than that the aircraft do not exist.
