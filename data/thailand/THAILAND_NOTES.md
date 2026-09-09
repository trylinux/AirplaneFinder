# Thailand — research notes

75 sites, 519 aircraft. Files in `/home/claude/seasia/thailand/`:
`th_museums.csv` plus one `<site_slug>_aircraft.csv` per site.

Research date: September 2026. Currency target: 2025–26.

---

## 1. Sources used, and how good each proved

### Primary backbone (best source found by a wide margin)

**The Thai Aviation Historical Website (thai-aviation.net), compiled by Steve Darke**
(`steveozel@outlook.com`). Three of his PDFs carry almost the whole of this dataset:

| Document | Revision date on the file | What it covers |
|---|---|---|
| *Thailand — Preserved Aircraft* (“Wrecks & Relics in Thailand”) | **6 July 2026** | ~200 locations nationwide, province by province, with GPS coordinates to six decimals, data-plate readings, and dated sighting histories going back to 1967 |
| *Royal Thai Air Force Museum, Don Mueang* | **23 January 2026** | full museum inventory, item by item |
| *Tango Squadron* | **31 January 2026** | Chiang Mai, Don Mueang, Saraburi Aero Park and the Takhli store |

This is a first-hand observational register, not a compilation. Entries carry the
convention: serials in `(brackets)` are **not** painted on the airframe; serials in
`“quotes”` are painted **in Thai script**; codes in *italics* are **false markings**.
That convention is what makes it possible to separate true identity from painted
marking, which is the single hardest problem in Thailand. Almost every `tail_number`
in these CSVs comes from it, and almost every `description` reproduces its provenance
chain and its doubts.

An older (26 December 2016) copy of the RTAF Museum file is still linked from Thai
Wikipedia via a dead `media.wix.com` URL; it still resolves, and I used it only to
cross-check the 2026 revision. It is nine years stale — it lacks the L-39s, Alpha
Jet, F-16B, F-5T, PC-9s, CT/4s, T-41s, AV-8S, A-7E, RTAF-6 prototypes and the
UH-1Hs, and it still lists the Boeing 737 that left in April 2025.

### Secondary / cross-check

- **en.wikipedia.org “Royal Thai Air Force Museum”** — the aircraft table is roughly
  2017-vintage and materially wrong in places. It gives the F-84G as `Kh16-06/99`
  (correct) but the F-86F as `Kh17-10/04` while omitting the second F-86F; it lists
  Bell 412/412SP/412EP and an AS-332L-2 Super Puma that no observer has recorded on
  site; it lists a `C-45 Expeditor`, `Bonanza 35` and `Widgeon` with no serials that
  are in fact identifiable from data plates. Used for lead generation only.
- **th.wikipedia.org** — the article body is a good administrative history of the
  museum (founded by Cabinet resolution 13 Aug 1952; present building opened
  29 Jan 1969) and is the source for the note that in **November 2025 the museum was
  designated the operations centre for national flood-relief coordination**. Its
  aircraft table is a translation of the English one and inherits its errors.
- **aviationspottersonline.com** (visit report, Dec 2017) — genuinely photo-based, and
  the only source that puts serial-level detail on the U-Tapao naval collection. Its
  RTAF Museum list is otherwise consistent with Darke.
- **aviationmuseum.eu** — useful only for *finding* sites (Khao Kho, Ram Intra police,
  the Golden Jubilee agriculture museum, the Kanchanaburi veterans museum, the Samut
  Prakan naval museum all came from its Thailand index). Its data tables are laid out
  as two parallel un-joined columns of serials and types; on the RTAF Museum page the
  two columns are **misaligned by one row** from the MiG-21 entry onward, which
  silently pairs the F-84G's serial `878/1231` with a non-existent “North American
  F-86G Sabre”. Do not trust its serial-to-type pairings.
- **silverhawkauthor.com** — lists a `Curtiss P-40C Kittyhawk AK498` at the RTAF Museum
  and a `Curtiss Tomahawk Mk.IIb AK500` at a “Chiang Mai Air Museum”. Neither is
  supported by any observer report. The only P-40 in Thailand is the **wreck of
  Tomahawk IIB `P8115`** at Tango Chiang Mai (AVG pilot William McGarry, shot down
  24 March 1942, recovered 1991), which is what these entries are almost certainly a
  garbled version of. Not used.
- Official museum sites: `museum.rtaf.mi.th` is **unreachable from this environment**
  (the egress proxy refuses the host and its robots.txt times out); the Wayback copies
  are blocked too. `jesadatechnikmuseum.com` was reachable and states Tue–Sun and
  public holidays, 09:00–17:00, free admission for individual visitors.

### Sources deliberately not used
Grokipedia (prohibited). `airfighters.com` and `db.sac.or.th` both return a JS/cookie
wall (HTTP 403) to any non-browser client. `airhistory.net` returns 403.

---

## 2. Corrections made, with the evidence

Everything below is a case where a widely repeated identity is wrong and the CSV
carries the corrected one, with the wrong value pushed into `aliases` or explained in
`description`.

**RTAF Museum**

- **F-84G `Kh16-06/99`.** Wikipedia and aviationmuseum.eu both record it as serial
  `878` code `1231`. The data plate reads **51-10582**; it was displayed as serial
  `582` code `4314` from 1967 to 1983, mispainted `878`/`1231` in 1994, and was
  **repainted back to 582 by October 2023**. `878` and `1231` are in aliases.
- **F-86 count.** Wikipedia gives two Sabres, aviationmuseum.eu appears to give four
  (including a fictional “F-86G”). There are **three**: F-86F `Kh17-42/06`
  (ex 51-13220), F-86F `Kh17-10/04` (ex 52-5060), F-86L `Kh17k-5/06` (ex 53-0681).
- **F-5A `69159`/`1311`.** Marked as if RTAF. It is **ex USAF 69-7110 / RoCAF 1275**,
  c/n N-6476, and **never served with the RTAF** — Wikipedia flags this correctly but
  gives no identity. Three further ex-RoCAF F-5As (67-21167, 69-7101, 71-0276) are on
  site, two of them now on the dump; all four are separate rows.
- **Kaman HH-43B.** Airframe is painted `H5-4/04`. Cockpit plate c/n **115** means the
  RTAF serial should be **H5-2/05** (which is what Wikipedia prints). Recorded as
  displayed, with both alternatives in aliases.
- **Beech C-45F `L1-5/90`.** Reported ex 44-87152 c/n 8411, which would make it
  `L1-6/90`. Displayed serial kept; alternative in aliases.
- **Helio U-10B.** Marked `63-8103` / `7135`, but `66-14332` was visible under the
  paint in 1994. The data plate (model H-395, c/n 576, mfg 1962) supports **63-8103**.
  66-14332 belongs to the U-10D at the Vajiravudh Scout Camp, Si Racha, which is a
  separate row at a separate site.
- **Bearcat `Kh15-178/98`.** Universally reported as ex Bu94956 c/n D.205 — but that
  airframe went to the South Vietnamese Air Force in May 1956. Identity flagged as
  doubtful in `description`; `year_built` left blank.
- **Skyraider.** Listed by Wikipedia as an `A-1H` with no serial. It is an **A-1J**,
  ex Bu142072 → USAF 52-142072, combat-damaged over northern Laos 27 Dec 1968,
  displayed at Nakhon Phanom, donated by Gen. Harry “Heine” Aderholt by 1979.
  Restored 2025 and now marked `42072`/`TT` with *The Proud American* nose art.
- **Boeing “P-12E”.** The RTAF aircraft were export **Model 100E** (c/n 1488).
  Recorded as Boeing 100E with `P-12E` in aliases.
- **Tachikawa.** Wikipedia lists both a Ki-36 and a Ki-55 (and its own photo gallery
  captions the same airframe as a Ki-36). There is **one** aircraft and it is confirmed
  a **Ki-55**.
- **Gripen.** Wikipedia calls it a JAS-39C/D. It is **JAS 39A c/n 39-178**, ex Swedish
  F10 then F17, last flown 20 Sep 2010, shipped to Laem Chabang 15 Mar 2012. It wears
  RTAF marks `70100` to port and Swedish marks `178` to starboard.
- **Boeing 737-2Z6 `L11-1/26`** and **HS 748 `L5-1/08`** are listed as museum exhibits
  almost everywhere. Both **have left**: the 737 was dismantled in spring 2025 and
  roaded to the RTAF Academy at Muak Lek on 8 April 2025 (it is filed there, now marked
  `60201`); the HS 748 was disassembled in October 2024 and had gone by mid-November
  2024 (reported destined for a royal palace — current location unconfirmed, so it is
  **not** filed anywhere).

**Elsewhere**

- **A-37B `J6-12/15`.** This serial appears on three separate airframes: the RTAF
  Museum aircraft (ex 71-0807, the real one, itself mispainted as 70-0807), the Takhli
  HQ aircraft, and the Ubon Ratchathani gate aircraft. All three are filed; the two
  non-museum ones carry the serial in `aliases`, not `tail_number`, with the conflict
  explained.
- **OV-10C at Tango Chiang Mai.** Two Broncos there both wear `J5-05/14 / 158400 /
  41105`. Data plates read **c/n 342-5** (the real `J5-05/14`, Bu158400) and
  **c/n 342-9** (really `J5-09/14`, Bu158404). Filed under their true identities with
  the shared painted marks in aliases. A *third* “OV-10C 158400/41105” exists at
  Kamphaeng Saen and is a **large model**, not an airframe — excluded.
- **Naval Aviation Museum UH-1H “2204”.** Data plate c/n 13311 ex 72-21612 → the
  aircraft is really RTN **2202**. It escaped from South Vietnam in April 1975, spent
  years at RTAF Lopburi displayed as RTAF `20311`, and was moved to U-Tapao in
  November 2022 and mispainted `2204`. Filed as 2202.
- **U-Tapao AV-8S / TAV-8S.** aviationspottersonline lists both `3101` AV-8S and `3101`
  TAV-8S with the same BuNo — a duplication error. The museum aircraft is the
  **two-seat TAV-8S `3101` (Bu159563)**, marked as a TAV-8A. The single-seaters are
  distributed: `3105` and `3106` on U-Tapao base, `3107` at the Marine Corps museum,
  `3104` and `3108` at Sattahip Navy Base, `3109` at the RTAF Museum.
- **Police KH-4 “1119” and Hiller UH-12E “1009”** at Tha Raeng: cockpit plates give
  c/n 2198 and 2314, whose real serials are **1116** and **1006**. Filed as 1116 / 1006.
- **Kaman/Bird Dog serial reuse in general.** Thai Army O-1s were repeatedly repainted
  with each other's numbers as they were shuffled between Lopburi, Tango's Amphur
  Khaeng Koi and Saraburi yards, Jesada and half a dozen surplus dealers. Where a data
  plate or panel radio call disagrees with the paint, the plate wins and the painted
  number is in aliases (e.g. Jesada's “2353” is really 56-2618; the museum's “5020” is
  really 51-5026; “7350” is really 51-7390).
- **Wren 460 at Loei.** Displayed as 5075 but has worn 5190, 515 and no marks at
  various times; ex **HS-PCA c/n 55190/4**.
- **F-16s on plinths are almost all spares airframes.** `10200` at the museum is really
  79-0324; `10206`/`86378` at the RTAF Academy is really 79-0375; Takhli's `90028` is
  really 82-0987. None of them flew as the aircraft they are painted as.

---

## 3. Judgment calls

**Replicas and mock-ups.** Recorded as records, flagged in `description`, never
silently as real: RTAF Museum Breguet 14P (a real 1979 Salis flying replica traded for
Bearcat Bu122095), the small-scale Breguet 14 converted in 2023 from a small-scale
Nieuport 17, the Breguet Type III, the Nieuport IIN, two Boripatra three-quarter-scale
replicas at the museum and a third at Bang Sue, the Hawk III replica at Prachuap Khiri
Khan, and the Nakajima B5N “Kate” at Tango Chiang Mai (a converted CCF Harvard IV built
for film work) and the North American P-64 “Hanuman” at Tango Don Mueang (rebuilt from
an AT-6). The **AU-23A on a pole at Prachuap Khiri Khan is probably a large-scale
model**, is flagged as such, and is the one borderline case I chose to keep.

**Wreckage and sections.** Kept, per the spec: the Nakajima Ki-27 “Nate” wreckage and
the Ki-43 “Oscar” recovery (propeller, engine, wing centre section, cockpit, one main
gear) at the RTAF Museum; the Curtiss P-40C `P8115` wreck at Tango Chiang Mai; the
F-5A tail fragments and UH-1H wreckage at Khao Kho; the Beech Musketeer wreck on a
pedestal at Wat Weluwan; the C-47 tail section on a pole (ex 42-100536) now inside the
RTAF Museum. **Dropped** as components rather than airframes: the museum's P-51D engine
and propeller (and it was last reported May 2019 anyway), and two loose F-16B fins.

**Composites.** Recorded once, under the identity the plate supports, with the
composite nature in `description`: the Army Aviation Museum's “8626” UH-1 (a UH-1C/M/E
front end apparently mated to a UH-1H tail), the Bangpho C-123B (fin from one airframe,
wings from two others), the Wing 7 F-5E built mainly from Kh18Kh-35/31, the Army
Aviation Museum's L-4 “2689”.

**`access_type`.** Judged by how a member of the public actually gets in.
- `public` (26 sites) — walk-up. The RTAF Museum is free and has its own BTS station
  (Royal Thai Air Force Museum, Sukhumvit Line, opened 16 Dec 2020). Jesada is free,
  Tue–Sun. Roadside plinths, temples, parks, cafés and markets are all `public`.
- `appointment` (8 sites) — must be arranged: Tango Squadron at both sites (both are
  on RTAF property inside the airport perimeter; Chiang Mai visits are organised as
  booked group tours, typically ฿200), the CATC ground school, Don Mueang Technical
  College, Rajamangala Krungthep, the Nakhon Sawan rainmaking museum, the Sakae Rat
  learning centre, and two private/charity compounds (Hope International, Vajiravudh
  Scout Camp).
- `restricted` (41 sites) — behind a controlled military or police gate. This includes
  the Army Aviation Museum at Lopburi and the Naval Aviation Museum at U-Tapao. Note
  that U-Tapao's *civil* terminal is open to the public but the museum and the base
  displays are not; the airport being “international” does not make the collection
  accessible.

**Site granularity.** Don Mueang RTAF base contains a dozen separate small display
groups. I collapsed the scattered ones (Wing HQ, Parachute Battalion, Directorate of
Education, Wing 6 officers mess, Institute of Aviation Medicine, Convention Hall,
kindergarten, fire-training ground) into one record, **Royal Thai Air Force Base Don
Mueang Heritage Displays**, and kept the three that a visitor would name separately —
the Academy Aviation Park, the Air Technical Training School parade ground, and the
Security Force Training Centre. Lopburi is split the same way: the museum, the Aviation
Centre's gate/plinth aircraft, Koke Kathiem air base, Camp Erawan's parachute trainers
and the Special Forces Museum are five records.

**Local-language names** (the CSV carries English names, as required):
- National Aviation Museum of the RTAF — พิพิธภัณฑ์กองทัพอากาศและการบินแห่งชาติ
- Royal Thai Army Aviation Museum — พิพิธภัณฑ์การบินทหารบก
- Royal Thai Naval Museum — พิพิธภัณฑ์ทหารเรือ
- Jesada Technik Museum — เจษฎา เทคนิค มิวเซียม
- Khao Kho Weapon Museum — พิพิธภัณฑ์อาวุธ เขาค้อ
- Vietnam Veterans Memorial Museum — พิพิธภัณฑ์ทหารผ่านศึกเวียดนาม
- Golden Jubilee Museum of Agriculture — พิพิธภัณฑ์การเกษตรเฉลิมพระเกียรติ
- National Science Centre for Education — ศูนย์วิทยาศาสตร์เพื่อการศึกษา (ท้องฟ้าจำลองกรุงเทพ)
- Royal Thai Police Aviation Division — กองบินตำรวจ
- National Memorial — อนุสรณ์สถานแห่งชาติ
- Navaminda Kasatriyadhiraj RTAF Academy — โรงเรียนนายเรืออากาศนวมินทกษัตริยาธิราช

**RTAF serial transliteration.** Thai RTAF serials are written in Thai script on the
airframe (e.g. ข.๑๗-๑๐/๐๔). They are recorded here in the standard Latin
transliteration used by Thai aviation researchers — `Kh17-10/04`, `Kh18k-1/09`,
`H6-7/12`, `F11-23/13`, `L2-39/15`, `JTh2-34/20`, `ThOr-5`, `KhF1-3/37`. The letter
group is the role (ข = ขับไล่ fighter, บ.จ = attack, บ.ล = transport, ฝ = trainer,
ต = observation, ฮ = helicopter, ทอ = RTAF-designed), the first number is the type
sequence, the number after the dash is the individual aircraft, and the number after
the slash is the Buddhist-era year of acquisition (last two digits). **The number after
the slash is not a construction year** and has not been used to populate `year_built`
anywhere.

---

## 4. Excluded — do not re-research

**The Bangkok “airplane graveyard”, Ramkhamhaeng Soi 105** (13.7650, 100.6523).
**Gone.** Two Orient Thai MD-82 hulks (HS-OMB, HS-OMD) lay there in two sections each
from about 2013. HS-OMD's remains had gone by January 2021. The site was **badly
damaged by fire on 26 March 2021** and was **completely cleared by April 2023**.
HS-OMB's forward fuselage survives, but not there: it went to the Fly n Senses airline
academy at Lak Si, then in 2023 to the **Airways Land Café on Highway 2 at Sida,
Nakhon Ratchasima**, restored into One-Two-Go livery. The famous 747 photographs from
that site are of a different location — the nearest real 747 relics are HS-STA at the
747 Café, Lat Krabang (filed) and the fuselage built into a house at Ang Thong on
Highway 32 km 45. Recommendation: do not file the graveyard.

**Aircraft stored at royal palaces.** Dusit Palace holds about eight ex-RTAF airframes
(five F-5s, a T-33, a T-37 and an SF-260, plus Thai Airways 737-400 HS-TDE displayed as
HS-TDK inside a purpose-built structure since 2019). Sukhothai Palace held an F-5A and
an SF-260 until they disappeared between February 2024 and January 2025. Taweewattana
Palace held a G.222, a C-47, an HS 748, a Bell 212 and a UH-1, of which the C-47, HS 748
and Bell 212 had gone by August 2025. Excluded because **none of the individual
identities can be established** (no observer has ever got close enough to read a serial;
the counts are made from satellite imagery and long-lens views), the aircraft move
without notice, and the sites are wholly inaccessible. Filing them would mean inventing
identities.

**Army-surplus dealers and scrapyards.** The largest concentrations of ex-Thai military
airframes in the country are commercial stock, not display: the “K. Beer” store at Muak
Lek and its three satellite yards, “War Camping & Coffee War” at Sattahip, “Soldier Car
Auction” at Ban Bang Prap, “Jirapat Wora” and “Vintage Power Wagons” in Nakhon Pathom,
the Si Racha and Rayong yards. Dozens of UH-1s, Bird Dogs and Fantrainers pass through
them, often repainted with invented serials and nose art before resale. They are
excluded as trade stock. Individual airframes that have *left* a dealer for a fixed
display are filed at the display (e.g. Wat Phuet Udom, Lam Phak Kut, Chang Chui).

**Stored, dumped and derelict airframes not on display.** Excluded throughout: the
U-Tapao beach-access-road line (P-3s, S-2s, C-47s moved out of the east revetments in
February 2022), the Koke Kathiem dump, the Tha Raeng police storage line (~20 Bell
205/206/212 hulls), the Takhli revetment and TAI stores (including two HS 748s and
several Fantrainers), the Hat Yai T-33 store (emptied by 2013), stored THAI A380s and
777s at Suvarnabhumi and U-Tapao, and the withdrawn airliners parked on the Don Mueang
west side. The exception is a small number of items that sit inside a museum's own
perimeter and are part of its holding — those are filed with `display_status`
`in_storage` (the RTAF Museum's dump line of uncompleted Fantrainers and two ex-RoCAF
F-5As, the T-37C fuselage, the Tango Blaniks).

**Saraburi Aero Park** (14.4465, 101.0116). Tango's outdoor storage field, which held
about 40 Bird Dogs. **Cleared during 2019**; the site is empty. Several of its aircraft
are filed elsewhere (Don Mueang Technical College, Army Aviation Museum, Tango Don
Mueang). Do not file the site.

**Chatuchak Thailand Railway Hall of Fame.** Held the wreckage of a Japanese Army
Kawasaki Ki-48 (long labelled a Mitsubishi Ki-21) recovered near the Death Railway.
The museum **closed in late 2012 and the fate of the exhibits is unknown**. Not filed;
this is the single most interesting untraced airframe in the country.

**Other closed or emptied sites:** The Camp Flea Market Chatuchak (closed early 2021,
its C-47 “Black Tiger” untraced), Runway 3119 Night Market (closed June 2020),
Thung Buachom Floating Market Wang Noi (cleared November 2025), Elephant Kingdom
Crocodile Farm Jomtien (closed July 2016), Nong Khai Chic Chic Market (closed 2020;
a 747 and a TriStar 500 were last reported March 2023 and need re-checking).

**Airworthy / operational aircraft.** Excluded per the spec: Tango's flyable Bearcat
was grounded and is filed as a display, but nothing currently airworthy is filed. The
active RTAF, Army, Navy and Police fleets are not filed. Bangphra's N591NC (unflown for
years but not a display) is excluded.

**Outside Thailand.** The Darke register tracks ex-Thai airliners now in Cambodia,
China, Japan, Malaysia, Pakistan, Singapore, South Korea, Taiwan and the USA. Not filed
here; a couple are worth picking up in the relevant country files, notably the ex-THAI
747-400 HS-TGG at the Betworld Casino, Poipet, Cambodia.

---

## 5. Fields left deliberately blank, and why

- **`year_built`** is blank on 512 of 519 rows (7 populated). Thai RTAF serials embed a Buddhist-era
  *acquisition* year, not a build year, and it would have been trivial — and wrong — to
  harvest it. The seven populated values come from an explicit build or first-flight
  date in a source: the Breguet 14P replica (built 1979), the Gripen (first flight
  8 Dec 1999), the Hawk 75N (delivered 29 Nov 1938 per its data plate), the Fantrainer
  400 F18-01/27 (mfg 1984 per plate), the Breguet Type III replica (2011), the
  small-scale Breguet 14 replica (2023) and the Nieuport IIN replica (2011).
- **`tail_number`** is blank on 110 rows. In every case either the airframe carries no
  identity at all (unmarked museum pieces such as the Hawk III, the Corsair, the
  Widgeon, the T-6G, the gliders), or the only marking present is demonstrably not a
  serial (the three CATC airframes all marked “HS-CATC”; the two RTAF-6 prototypes both
  marked only “ThOr-6”), or the identity is genuinely unresolved (several Khao Kho and
  Kamphaeng Saen airframes, the AFAPS T-28D, the Takhli F-84G).
- **`postal_code`** is blank on the base and monument records where I could not tie the
  site to a specific postcode; town-level postcodes were used where the district is
  unambiguous.
- **`website`** is blank except for the seven sites with a working official page.
- **`aircraft_name`** is used only where the airframe genuinely carries a name:
  *The Proud American*, *Miss Siam* (two aircraft), *Hanuman*, *Dragon Fire*,
  *Pimantip*.

**Coordinate quality.** Almost every coordinate is a mapped airframe or gate position
taken from the Darke register (six decimals, truncated here to four), not a town
centroid. The exceptions, which are site-centroid rather than airframe positions, are:
Korat, Takhli, Prachuap Khiri Khan, Surat Thani, Ubon Ratchathani, Udon Thani,
Chiang Mai, Phitsanulok, Hat Yai, Kamphaeng Saen and Koke Kathiem air bases (where the
displayed aircraft are spread over several kilometres inside the wire and I used the
main gate or HQ area), and the Armed Forces Academies Preparatory School.

---

## 6. Open questions, ranked

1. **Where did the RTAF Museum's HS 748 `L5-1/08` (code `60301`) go?** Disassembled at
   the museum in October 2024, gone by mid-November 2024, “to go to a Royal Palace”;
   later reported roaded to Takhli and stored with TAI through January 2025. It is
   currently filed **nowhere**, and it is a complete, identifiable airframe.
   *One email to the RTAF Museum (`+66 2 534 1853` / `+66 2 534 2113`) would close this
   and questions 2 and 3 at once.*
2. **Current RTAF Museum floor state after the November 2025 flood-relief operation.**
   Thai Wikipedia records that on 26 November 2025 the museum was designated the
   national flood-relief coordination centre under Lt Gen Adul Boonthamcharoen. The
   Darke inventory is dated 23 January 2026, so it post-dates that, but no source says
   whether exhibits were moved or whether the museum reopened to visitors normally. The
   `public` access_type is an assumption based on its pre-2025 status.
3. **Does the RTAF Museum still hold its UAVs?** CyberEye Lite, CyberEye II, the
   Lear-Siegler/BAe Skyeye R4E-30 and a Meggitt Snipe Mk.4 target drone were all
   recorded 2015–2018 and have not been reported since. Not filed. If they are still
   there, four rows are missing.
4. **Is Jesada Technik Museum actually open?** Its own site advertises Tue–Sun,
   09:00–17:00, free. The Darke register says the site flooded in October 2021, stayed
   closed through 2022, had a “soft opening” of the restored museum with a new
   exhibition hall on 29 September 2023, but was **still closed as of February 2025**.
   I filed it `public` on the strength of the operator's own page. Worth a phone call
   before anyone travels. Its Bird Dog line was being re-assembled and restored through
   2024, so the four `under_restoration` rows there may now be `on_display`.
5. **Kawasaki Ki-48 wreckage from the Death Railway.** Held by the Thailand Railway
   Hall of Fame at Chatuchak until the museum closed in late 2012; fate unknown.
   A single enquiry to the State Railway of Thailand would settle whether one of the
   very few Ki-48 relics anywhere still exists.
6. **U-Tapao Naval Aviation Museum access and current line-up.** The register's last
   full survey there is January 2025. It is unclear whether the museum can be visited
   by arrangement now that U-Tapao's civil terminal has expanded. Contact:
   Royal Thai Naval Air Division, U-Tapao. Two AV-8S (`3102` TAV-8S, `3103` AV-8S) and
   several TA-7Cs were moved out of the shelters in February 2022 to unknown locations
   and are not filed.
7. **Wing 21 Ubon Ratchathani** was last surveyed **September 2019** — the oldest data
   in this set. All four gate aircraft (two A-37Bs, a T-28D, a C-123B) need a currency
   check. Wing 23 Udon Thani's new “Wing 23 Museum” (established mid-2023, holding an
   Alpha Jet and an RF-5A) has never been surveyed in detail and probably holds more
   than the four aircraft filed.
8. **Takhli F-84G `Kh16-5/04`** and the second Takhli A-37B: both carry serials that
   belong to other airframes and neither has a confirmed identity. The RTAF historical
   branch could resolve them from unit records.
9. **Train Night Market Srinakarin** — the C-47 (ex 43-49210) was last reported March
   2024, but the market's own trading status has been unstable. Worth confirming the
   aircraft is still on site before treating the record as current.
10. **Chiang Rai Old Airport** access. The Fantrainer `F18k-8/30` is displayed there;
    I could not establish whether the former airfield is now open ground, a police
    facility or a military camp, so `access_type` is a conservative `restricted`.

**Best single contact for the whole country:** Steve Darke, `steveozel@outlook.com`,
who maintains the register and explicitly invites corrections and additions. He holds a
Google Earth KMZ of every location in the preserved-aircraft file. A single exchange
with him would close items 1, 3, 6, 7, 8, 9 and 10.

## Post-research processing (import pass, 9 Sep 2026)

- Every row was validated against the real importer (`tests/test_flagship_topup_files.py`)
  and the alias-hygiene suite before import. Two mechanical corrections were applied across
  this file set: dashless search variants were added where missing (`MiG-21` → `MiG21`,
  `MiG-21PF` → `MiG21PF`), and attribute words that had been filed as aliases (`replica`)
  were moved into `description`, where the convention puts them.
- Duplicate aliases within a row were removed; the database de-duplicates them anyway, and
  leaving them in the CSV made the file and the live record disagree.
- Serials were diffed against all 3,542 tail-numbered aircraft already in the database before
  import: zero collisions. Museum names were diffed against all 424 existing sites: zero
  collisions, exact or normalised.
- Museums were imported first, then aircraft, and the result was verified per site against
  the live API — every site's aircraft count matches this directory exactly.
