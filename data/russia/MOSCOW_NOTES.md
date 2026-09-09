# Moscow city and Moscow Oblast — research notes

Area: the federal city of Moscow and Moscow Oblast, **excluding Monino** (Central Air
Force Museum), which another agent covers. Research done 9 September 2026.

18 sites, 227 aircraft/spacecraft records.

---

## 1. Sources, and how each behaved

| Source | Use | Staleness found |
|---|---|---|
| **russianplanes.net** | Primary. Its `/museums` directory lists every collection with three or more Soviet-built airframes, and the undocumented JSON endpoint `/?action=mapGetPoints&smuseum=<id>` returns, per museum, each airframe's type, bort number, construction number, per-exhibit coordinates and a **status flag** (`monument` / `stored` / `parts` / `ex` = gone). The `ex` flag with its free-text remark is what made the currency work possible at all. | Current. It carried the June 2025 Poklonnaya→Monino move, which the museum's own website has *not* yet reflected. |
| **kpopov.ru** (Константин Попов) | Detailed per-museum photo surveys with works numbers, unit histories and repaint records. Best source for provenance prose. | Page-dated: Zadorozhny page last updated 09/05/2021, Patriot 30/09/2022, Central Museum of the Armed Forces 24/08/2019, Poklonnaya open-air 12/05/2019. Several bort numbers on those pages are one repaint behind russianplanes.net. |
| **ABPic** (photographer John Bennett) | Dated photographic evidence, 30/08/2019 and 05/09/2021 visits to Patriot Park and Zadorozhny. Used to pin what an airframe *wore* on a known date. | Fine for what it is; five years old. |
| **OpenStreetMap via Overpass** (`historic=aircraft`, bbox 54.2–56.95 N, 35.1–40.3 E) | Systematic sweep to find collections the seed list missed — 107 tagged aircraft nodes plus clusters. Found the Egoryevsk college, the Sheremetyevo trainer airframes, the MEI military training centre, the Lukhovitsy plant and the Dubna monuments. | Names are patchy; most Patriot Park and Central Museum of the Armed Forces nodes are untagged beyond `historic=aircraft`. Useful for *counts* and *positions*, not identities. |
| **Nominatim** | Coordinates for museum buildings. | Failed on VDNKh pavilion 34, Mil/Panki and Kuzminki; russianplanes.net's mapped museum positions were used for those instead. |
| Museum websites (tmuseum.ru, victorymuseum.ru, parkpatriot.ru, vdnh.ru) | Opening hours, access, addresses. | **victorymuseum.ru is stale**: its "Площадка военной техники 50-80 гг" page still lists the MiG-15, MiG-17, MiG-21, MiG-23ML, Su-15TM, Ka-25 and Ka-26 that left for Monino in June 2025. |
| checksix.de | Nothing usable — the Zadorozhny and Patriot Park aviation reports are behind a members' paywall. |
| ru.wikipedia.org | Reachable only through the MediaWiki API with a real User-Agent (WebFetch returns "cache-only"; bare curl gets HTTP 429). Used for Patriot Park background. Its museum articles carry no aircraft lists worth having. |
| LiveJournal (saidpvo, igor113, max-sky) | Readable via WebFetch only — direct curl is IP-banned. Useful narrative, weak on numbers. |

Grokipedia was not used.

---

## 2. The two big currency corrections

### 2.1 Victory Museum → Monino, June 2025

Roughly a dozen post-war airframes left Poklonnaya Hill for the Central Air Force
Museum at Monino in June 2025, reported by aviation21.ru on 16 June 2025 and flagged
individually on russianplanes.net. The museum described it as a **temporary** move for
an exhibition called "Post-war aviation development", but they are physically at Monino
now, so under the "one place in 2025-26" rule they are **not** recorded at Poklonnaya:

| Type | Bort | c/n |
|---|---|---|
| Aero CS-102 (licence MiG-15UTI) | 06 red | 922272 |
| MiG-17 | 66 red | — |
| MiG-21PFS | 09 red | 94210425 |
| Su-15TM | 11 red | 1015329 |
| Su-22UM3K | 81 red | 17532372510 |
| MiG-23ML | 14 red | 0390310255 |
| Ka-25PL | 77 yellow | 2912205 |
| Ka-26 | 36 black | 7001407 |

**For whoever holds Monino:** these eight are new arrivals that the 132 already-recorded
Monino rows will not contain, and at least two will collide on the (model, tail_number)
key with existing Monino rows (Monino already has an Su-15 "11" and a Ka-25 "17"; the
MiG-17 "66 red" and MiG-21PFS "09" are safe). Also note the museum calls the loan
temporary, so a re-check in a year is warranted.

Separately, Poklonnaya's **An-12B "42 red" (c/n 5343503)** went the other way — it is now
at Patriot Park and is recorded there, not at Poklonnaya. Parts of it were originally
brought from Kirzhach in April 2015.

### 2.2 Zadorozhny → Verkhnyaya Pyshma and Medyn

The Zadorozhny museum has been shedding aircraft to the UGMK "Battle Glory of the Urals"
museum at Verkhnyaya Pyshma (Sverdlovsk Oblast) and to its own branch at Medyn airfield
(Kaluga Oblast). Neither is in this area, so these are **excluded** from the Arkhangelskoye
site record:

- MiG-15UTI c/n 2029053 → Verkhnyaya Pyshma, 2021 (kpopov.ru states this explicitly)
- UTI MiG-15 "47 red" c/n 10995413 → Verkhnyaya Pyshma
- MiG-17 "17 red" (earlier "61 red") c/n 54211860 → Verkhnyaya Pyshma
- Il-28B c/n 36603607 → Verkhnyaya Pyshma
- Su-15TM "37 red" c/n 1215327 → Verkhnyaya Pyshma
- Il-102 c/n 102010303010 → Medyn
- Yak-38 "60 white" c/n 7977864060699, Yak-12A CCCP-Л5275, Yak-18T CCCP-81434 → marked
  gone by russianplanes.net without a stated destination

kpopov.ru also records **two more Su-15 interceptors, borts "85" and "37", at the Medyn
branch**, one of them the 1966 prototype Su-15T. Anyone covering Kaluga Oblast should
expect Medyn to hold ~39 airframes, a large share of them ex-Zadorozhny and ex-Khodynka.

---

## 3. Khodynka Field — no site record created

The Museum of Aviation Technology on Khodynka Field (Центральный аэродром им. М.В. Фрунзе,
Moscow) **no longer exists**. The last flight from the field was an Il-38SD delivery to
the Indian Navy on 3 July 2003; the museum was formally disbanded (расформирован) in 2012,
and by then the collection had degraded into what Russian press called an "авиасвалка"
(aircraft dump) — canopies smashed, cockpits looted. The site is now residential
development and a park; nothing aeronautical remains on it. **No museum record was
created, and no aircraft were assigned to it.**

Where the Khodynka aircraft went, so far as the sources establish:

- **To the Zadorozhny museum, 2011–2012** and recorded here at Arkhangelskoye:
  Il-28 c/n 36603607 (2011, since moved on to Verkhnyaya Pyshma), MiG-17 c/n 54211860
  (2012, in pieces; since moved on), MiG-19SV c/n 0615337 (2012, half-dismantled — still
  at Arkhangelskoye), Yak-38 c/n 7977864060699 (early 2012, restored and renumbered "60
  white" on 25 September 2012; since gone), the Mi-24D (at Khodynka until 2012 — still at
  Arkhangelskoye), MiG-21SMT and the Tu-143 drone.
- **To Medyn (Kaluga Oblast)**, the Zadorozhny branch — the English Wikipedia article on
  the museum records that by 2012 it "began moving abandoned military aircraft from the
  former Khodynka Aerodrome to the former Medyn Airfield".
- The remainder was scrapped or dispersed without record.

The OSM sweep finds three `historic=aircraft` nodes at 55.783–55.784 N, 37.541–37.544 E
— a Su-27 and two Su-25. These are **not** Khodynka museum survivors: they sit on the
Sukhoi design bureau grounds at Ulitsa Polikarpova 23A on the eastern edge of the former
field, and are recorded here as the Sukhoi Design Bureau display.

---

## 4. Per-site notes and judgment calls

### Technical Museum of Vadim Zadorozhny (Музей техники Вадима Задорожного) — 35 records
Public, daily 10:00–18:00, tickets 400/500 RUB adult (russianplanes.net contact card).
Aviation is a separately ticketed part of the combined ticket on tmuseum.ru.
- The **MiG-27 "51"** is included on kpopov.ru's 2021 survey (works number 61912538152)
  and was photographed in 2016, but russianplanes.net holds **no card for a MiG-27 at
  this museum**. Recorded, with the doubt stated in the description. If it has to go, it
  is the row to drop.
- The **Hawker Hurricane Mk II** and the **two Messerschmitt Bf 109G** are in the indoor
  "Соколы России" hall and are absent from russianplanes.net (which indexes Soviet types);
  they come from kpopov.ru with recovery histories. All three are restorations from
  recovered wreckage — said so in `description`, not in `aliases`.
- **AIR-1 "R-RAIR"** is a full-scale reproduction of Yakovlev's 1927 first aircraft.
  Recorded as such in the description.
- **Il-2** is held as fragments under long-term restoration (`under_restoration`), raised
  from Lake Krivoye in 2012 with the museum's Yak-1.
- **MiG-25BM "47 blue"**, **MiG-25PU "22 blue"**, **Su-24 "15 white"**, **Mi-24V "92
  yellow"**, **Be-12PS "04 yellow"**, **MiG-29 "62 blue"** and the **F-84F** are all
  post-2021 additions absent from kpopov.ru. The MiG-25PU came from the Gromov Flight
  Research Institute at Zhukovsky.
- kpopov.ru calls the museum's MiG-29 "the fifth prototype"; the russianplanes.net card
  gives a series works number (2960518450). The prototype claim was **not** carried over.
- Two Ka-30 aerosani (propeller-driven snow machines) are in the collection and were
  **excluded** — they are not aircraft.
- Bort-number drift between visits is real here: the MiG-21SMT was "59 red" in 2019 and
  is "71 blue" now; the MiG-17 went 61 red → 17 red before leaving. Former numbers are in
  `aliases`.

### Patriot Park Museum Complex (Военно-патриотический парк «Патриот») — 50 records
Public, free entry to museum site No.1 at 55 km of the Minsk highway. The aviation and
air-defence cluster is advertised by the park as "more than 30 units of aviation
equipment"; russianplanes.net records 55 cards of which 45 are current airframes.
- **The bort numbers here are the least stable of any site in the region.** The 121st
  Aircraft Repair Plant repaints airframes as they are prepared, and a volunteer group
  works on them on the base. Where the 2019/2021 photographs and russianplanes.net
  disagree, russianplanes.net was taken as later and the photographed number put in
  `aliases`: MiG-31 15 red → 19 red; MiG-23UB 17 red → 19 red → 15 red; MiG-23MLD 44 blue
  → 16 red; MiG-21UM 106 red → 21 red; Su-9 07 blue → 52 blue; MiG-29UB 55 white → 83
  blue; Ka-29 10 red → 16 yellow; Su-25T 81 red → 11 white.
- The **Su-27 c/n 36911027514** was photographed as "12 red" in 2019 and is now in a
  Su-57-style camouflage with no readable bort. The **Su-27UB c/n 96310422069** was
  repainted "17 red" in 2015 and russianplanes.net now shows no bort. Both recorded with
  blank `tail_number`; a bort you cannot read is not a bort you know.
- A third Su-27 is displayed in **Russian Knights** colours with neither bort nor works
  number recorded — that phrase is in `aliases` because it names the airframe's scheme,
  and the description says what it is.
- Several russianplanes.net cards are duplicated (the same works number filed twice, once
  under an old paint scheme flagged `ex` and once current). Deduplicated by works number:
  Su-25T 25508601008, MiG-29 2960509182, An-2 111347315, An-26 2101, Su-27UB 96310422069,
  Mi-2 548705054, Il-2M 7826.
- Two untailed **Mi-8T** rows would otherwise be indistinguishable; the second carries
  "second of two examples" in `aliases`.
- The **MiG-17 "01 blue"** will collide on (model, tail_number) with Monino's existing
  MiG-17 "01". Different airframes — Patriot's is works number 2090, ex-Savasleyka.
- The Tu-143, Pchela-1T and La-17MM come from kpopov.ru (September 2022) rather than
  russianplanes.net, which does not card them here.
- The park's separate **"Поле Победы"** open-air museum by the Main Cathedral of the
  Armed Forces (five OSM aircraft nodes around 55.568 N, 36.830 E) is Great Patriotic War
  ground equipment; no aircraft identities were established and none were recorded.

### Victory Museum, Poklonnaya Hill (Музей Победы) — 19 records
Public. Two open-air grounds: 1930s–40s equipment and 1950s–80s wars and local conflicts.
- **Heavy replica content.** The museum's own site describes the I-16, LaGG-3, La-5,
  Yak-3, Il-2, Bf 109F-2, Po-2, Ju-88A-1 (cockpit only) and Ki-43 as "макеты и
  ретрокопии". russianplanes.net independently marks the I-16, La-5, Su-2 and I-15bis
  with mock-up placeholders in the works-number field. Said so in every affected
  description; the word "replica" is nowhere in `aliases`.
- The **Ju-88A-1** is a cockpit section only and was **excluded**.
- **Type dispute on the Bell fighter**: the museum and kpopov.ru both call it a **P-63
  Kingcobra**; russianplanes.net's card for the same airframe (bort 08) says **P-39**.
  Recorded as P-63 on the two-to-one split, with "P-39"/"P39" in `aliases` and the
  conflict stated in the description. This is the single least settled identification in
  the whole set.
- The **Il-2 "21"** is carried by russianplanes.net without a works number and the museum
  groups it with its retro-copies; no original identity is asserted.
- Genuine airframes with works numbers: Li-2 (18438101), Il-4 (17404), Su-25 (25508103012),
  MiG-29 (2960705560), Mi-8 (9710819), Mi-24D.

### Central Museum of the Armed Forces (Центральный музей Вооружённых Сил) — 18 records
Public. Aircraft are on the open-air ground behind the building at 55.7848 N, 37.6178 E
(the museum building itself geocodes to 55.7852, 37.6159).
- **Correction made:** kpopov.ru's page captions this museum's MiG-17 with works number
  **54211860**. That is the works number of the MiG-17 that was at the Zadorozhny museum
  and has since gone to Verkhnyaya Pyshma. Treated as a copy-paste error on kpopov.ru;
  russianplanes.net's **0515347** is used instead.
- The **Su-24MR "26 red"** is the first prototype of the type (T6M-26 / T6MR-26), works
  number 0115305 — a significant airframe.
- **Excluded from the aircraft file** but present on the ground: an AMD-500 air-dropped
  naval mine, an S-125 SAM launcher, R-9A / R-13 / R-21 / R-11FM missiles, and
  cockpit-only sections of a Su-25 (25508101035) and a MiG-21F-13. Cockpits are fragments,
  not airframes; missiles here are ordnance displays inside a general military museum
  rather than an aviation collection, and were left out to avoid inflating the count.
- kpopov.ru's 2019 survey lists 13 aircraft; russianplanes.net adds a MiG-25PD, L-29,
  Yak-50, Su-25 and Mi-2. Went with russianplanes.net.

### Cosmonautics and Aviation Centre, VDNKh — 12 records
Public, pavilion 34 "Космос" plus the aircraft on Ploshchad Promyshlennosti.
- **Yak-42 CCCP-42304** (c/n 11820201) has stood at VDNKh since 1981, was restored to its
  original livery and is open as an exhibition and simulator space. **Mi-8T "70 yellow"**
  and **Su-27 "27 red"** were installed in April 2015.
- **Buran "БТС-001 / ОК-МЛ-1"** is a full-scale mock-up (izdeliye 0.15), moved from Gorky
  Park in summer 2014 and opened as a walk-in exhibit in 2017. Recorded as `spacecraft`,
  described explicitly as a mock-up.
- **The Vostok descent module row is the weakest record in the file.** kpopov.ru captions
  it "спускаемый аппарат космического корабля «Восток-1»", but the flown Vostok-1 capsule
  is normally displayed at RKK Energia in Korolyov. Recorded with the doubt stated; if in
  doubt, drop it.
- russianplanes.net's VDNKh page carries 21 cards, but **16 of them are historical** —
  aircraft exhibited at the exhibition in 1956–2008 and long gone (Tu-104 CCCP-Л5400,
  Tu-154 CCCP-85005 which stood 1976–2008, Yak-40 CCCP-19661 which went on to MAI,
  Mi-6P, An-24, Ил-18А and others; the Tu-104A CCCP-42338 and Il-18A CCCP-75644 both went
  on to Egoryevsk). None were recorded here.

### Memorial Museum of Cosmonautics — 9 records
Public, in the base of the Conquerors of Space monument. Flown hardware: the Vostok 3KA
No.2 descent module (25 March 1961, the dog Zvezdochka, the last rehearsal before
Gagarin), Soyuz-37 and Soyuz TM-7 descent modules, and the Raduga return capsule.
Mock-ups: Mir, Soyuz, the N1-L3 lunar lander. `year_built` is populated only for the
3KA capsule and even there it is the flight year, not a build date — reconsider at import
if that is not wanted.

### Mil Moscow Helicopter Plant Museum, Tomilino (Panki), Lyubertsy — 13 records
By appointment; the collection is on plant grounds. This answers the "Lyubertsy" lead.
- **The V-12 here is a registration problem.** russianplanes.net gives the Panki V-12
  works number 001 and the registration CCCP-21142 — but the already-recorded Monino
  V-12 also carries CCCP-21142, and only two were built. Both cannot wear it.
  **`tail_number` left blank** for the Panki machine with the conflict written into the
  description. Resolving which airframe legitimately carries CCCP-21142 is open question 2.
- Also here: the Mi-28A prototype "032" (c/n 00-03), the Mi-24VM first prototype "51",
  the Mi-34 prototype (C1/OP-3), and a "НГУ" full-scale rotor test rig which was
  **excluded** as ground test equipment, not an aircraft.
- Two Mi-8T rows; the untailed one carries "second of two examples".

### Gromov Flight Research Institute, Zhukovsky — 7 records
Restricted; the airfield is a working flight-test centre and the museum is
"по договорённости" only.
- Recorded: the six aircraft of the **Аллея Славы ЛИИ** (Alley of Glory) — Il-102 "10201",
  MiG-23UB "09", Yak-38U "24", Su-22UM3K "09", Su-24 "10", MiG-25PU "02" — plus the
  **Tu-144 CCCP-77114** (c/n 08-2) preserved as a monument on the field.
- **Deliberately not recorded:** the ~76 further airframes russianplanes.net files under
  "Музей ЛИИ им. М.М. Громова". These are the institute's stored and derelict test fleet
  parked on the airfield — Tu-155 CCCP-85035, Tu-144D CCCP-77115, VM-T Atlant RF-01502,
  MiG 1.44 "144 blue", S-37/Su-47 "01 blue", Su-35 "901", Tu-334 RA-94001, four Tu-204
  development airframes, two M-55 Geophysica, Il-114 RA-54002 and so on. They are
  **stored, not displayed**, several are still airworthy or nominally so, and the spec
  says operational aircraft are not displays. They are a substantial and genuinely
  significant holding and deserve a decision at a higher level than this pass — see open
  question 1.
- The **Buran orbiter 2.01** is marked `ex` at Zhukovsky by russianplanes.net; it left for
  Kronstadt (St Petersburg) and is not in this area.
- The L-29 "ФЛАРФ-01801" that OSM places at 55.6086 N, 38.0871 E stands on church ground
  in the town, with an Il-103 RA-10300 and a "Молния-1" alongside — a town display, not
  recorded (see section 5).

### Sukhoi Design Bureau display, Moscow — 9 records
Restricted (plant grounds, "по договорённости"). Ulitsa Polikarpova 23A, on the eastern
edge of the former Khodynka field.
- The **Su-15 "01" is the very first Su-15 built at Novosibirsk** (c/n 0015301, first
  flight 6 March 1966 by I.F. Sorokin, later a Sakhalin-programme tanker testbed) —
  confirmed against the russianplanes.net Su-15 type register.
- The **Su-7B "28"** came here from the Moscow Aviation Institute.
- The **I-153 "42 white"** is a monument aircraft; whether it is original was not
  established and the description says so.
- A Su-2 mock-up that stood here moved to Volgograd in 2010 — excluded.

### Moscow Aviation Institute — 11 records
Restricted (campus, teaching hangar; russianplanes.net lists it "по договорённости").
- Outdoors and effectively viewable: **Su-27SM (RF-92211 / bort 04)** at the entrance and
  an **Mi-8 "30 yellow"**.
- In the teaching hangar, recorded `in_storage`: Yak-38 "45" (izdeliye VM-4), the
  **MiG-23 prototype 23-11/4 (bort 234)** — a genuinely rare airframe, sibling of the
  23-11 already at Monino — Yak-40 CCCP-19661 (c/n 019, ex-VDNKh 1970–80), Su-25, MiG-29,
  MiG-21, a second Su-27, an Aviatika-MAI-890 and a Pchela-1 drone. Most have no bort
  number recorded and none is asserted.
- An "Квант 02" airframe and an X-22 missile section are listed by russianplanes.net;
  the Kvant could not be identified to a type and was **excluded**.

### Kubinka — three separate collections, all restricted
The air base at Kubinka is active and none of these is walk-in. They are three distinct
locations, so they are three site records rather than one:
- **121st Aircraft Repair Plant Museum** (55.6057, 36.6931) — 13 restored airframes, the
  best of the three. Nearly every one has been renumbered at least once; former borts are
  in `aliases`. The **Yak-38 "38 yellow"** here will collide on the key with Monino's
  Yak-38 "38"; different aircraft (this one is c/n 7977863605715).
- **Kubinka Air Base Museum** (55.6057, 36.6271) — 5 airframes. The Su-27M/T-10M-1 that
  was here is now at Monino (already in the Monino 132 as Su-35 T10M-1 "701"), and an
  L-29 went to Patriot Park; both excluded.
- **Kubinka Air Force Aeroclub display** (55.6179, 36.6675) — 10 airframes, all moved in
  2019 from the air defence aviation museum at Savasleyka (Nizhny Novgorod Oblast).
  Only one has a works number on record; nine are recorded on bort number alone.

### State Military-Technical Museum, Ivanovskoye (Chernogolovka) — 3 records
Public. A large armour and vehicle museum with almost no aviation: a Yak-38 (c/n
7977861052651), An-2 CCCP-16068, and an **EKIP** lenticular ground-effect research
vehicle (russianplanes.net cards it with a query over the identification; recorded as
`fixed_wing`/`monoplane` for want of a better category, with the doubt in the
description). A Ka-30 aerosani and a hovercraft were excluded as not aircraft. The
museum's **MiG-23P has left for Zarya, Balashikha** and is recorded at the Air Defence
Forces Museum instead.

### Museum of Industrial Culture, Kuzminki, Moscow — 2 records
Public and free. Only a MiG-21PF "07 red" (c/n 76211525) and an Mi-2 (c/n 544850076, ex
ROSTO training centre) belong to the museum. An An-2 "60" and a second Mi-2 "25" stand on
the adjoining **paintball club** ground and were **excluded** — different operator, and
russianplanes.net marks them stored rather than displayed. A "Мечта" glider and an Il-18
UN-75111 are marked gone. Small site; included because it is a genuine, free, public
museum with real airframes.

### RSK MiG Lukhovitsy plant display — 6 records
Restricted. Five monuments on the central avenue and by the main gate of MiG production
complex No.1 (MiG-29 "01 grey", Il-28 "30 red", Il-103SKh, MiG-23UB "55 red", MiG-15bis
"01 blue") plus a stored Mi-26 "04". **Judgment call:** the spec defers gate guards and
town plinths, and these are arguably factory gate guards; they were included because five
aircraft on one avenue is a coherent display and because this is the substantive aviation
site in the Kolomna/Lukhovitsy corner the brief asked about. Drop the site if the rule is
read strictly.
**Discrepancy:** OSM records a **"МиГ-23МЛ №96"** at 54.947 N, 39.0276 E, about 3 km
north of the plant avenue, while russianplanes.net records a MiG-23UB "55 red" at the
plant. Either there are two MiG-23s in Lukhovitsy or one of the two sources is wrong; not
resolved.

### Air Defence Forces Museum, Zarya, Balashikha — 3 records
A branch of the Central Museum of the Armed Forces, in a military settlement; visits by
arrangement, so `appointment`. Coordinates 55.7585 / 38.0880 from Nominatim, corroborated
by an OSM `historic=aircraft` node ("МиГ-19") 20 m away. Aircraft: MiG-19P, MiG-31 and
the MiG-23P that came from Ivanovskoye. **No bort numbers were established for any of
the three** — kpopov.ru's survey is text-and-photograph and quotes none, and
russianplanes.net does not card this museum. All three `tail_number` fields are blank
rather than guessed. This is the site most in need of a photographic re-check.

### Gagarin Cosmonaut Training Centre Museum, Star City — 2 records
Restricted; Zvyozdny Gorodok is a closed town and entry is by organised excursion.
Recorded: the **MiG-15UTI "19"**, one of the trainers that flew the first cosmonaut
intake (Gagarin and Seryogin died in the near-identical bort 18), and the descent module
of the uncrewed **Soyuz-2**. Coordinates are those of the Dom Kosmonavtov, where the
museum is; the MiG-15UTI is in the training complex a short distance away, so the site
coordinate is approximate at building level, not airframe level.

---

## 5. Sites and airframes found and deliberately not recorded

Everything below turned up in the sweep and was set aside, with the reason.

**Not a display / operational:**
- **Sheremetyevo area, ~55.985 N, 37.442 E** — Il-86, Tu-154 and Il-76 tagged in OSM
  "Real plane, being used as training simulator". Aeroflot Aviation School ground trainers,
  not displays. Also an Il-62M at 55.9825/37.4191 and Tu-154s at 55.9854/37.4432 and
  56.0132/37.4680 (Lobnya) whose status was not established.
- **Gromov Flight Research Institute stored fleet** — see above.
- **MARZ ROSTO, Chernoye (55.7600, 38.0577)** — four Mil helicopters (Mi-1 "01",
  Mi-2 RF-00060, Mi-4 "04", Mi-6 "90") at the repair plant gate. Factory gate guards.

**Town plinths and gate guards (deferred by the spec):**
- Zhukovsky town: L-29 ФЛАРФ-01801, Il-103 RA-10300, "Молния-1 00103" on church ground
  (55.6086, 38.087).
- Odintsovo local history museum (55.6708, 37.2765) — MiG-29 "27 blue" (c/n 2960520592)
  and Mi-24 "59" (c/n 3532434116201), both installed summer 2012, plus Kh-22, Kh-55 and
  Zenit-2 missiles and a K-36DM ejection seat. Six russianplanes.net cards; a town display
  rather than a museum with a collection.
- Kubinka town MiG-23 (55.5792, 36.6922); Noginsk Su-27 (55.8757, 38.4657); Dubna Il-2,
  Su-24M and MiG-25 (56.74–56.76 N, 37.13–37.25 E); Mytishchi Po-2 (55.9034, 37.7147) and
  MiG-21 (55.9258, 37.7953); Khimki La-7 at NPO Lavochkin (55.8925, 37.4269); Dolgoprudny
  "Volga" stratospheric gondola (55.9447, 37.5064); Voskresensk MiG-19 (55.1688, 38.3865);
  Chekhov Mi-2 (55.2534, 37.5300); Vnukovo-area Tu-104 monument (55.5978, 37.3079,
  formerly in front of the Vnukovo terminal building); Myachkovo An-30 (55.5608, 37.9622);
  Korolyov Tu-134A-3 "Roscosmos" (55.8940, 37.9762); Kuntsevo MiG-17 / MiG-15UTI / L-29
  (55.7295, 37.4016); "Электрон" MiG-15 and two Yak-25M (55.8841, 38.6074).
- **General Staff Academy, Troparyovo (55.6496, 37.4751)** — MiG-27 "49", MiG-29B "51
  white", Mi-24A. Closed military academy.
- **MEI military training centre (55.7567, 37.7022)** — Su-27, Su-34, Mi-8MT, OSM-tagged
  "для нужд ВУЦ МЭИ". University military department training airframes, no public access.

**Educational airframes:**
- **Egoryevsk Aviation Technical College (ЕАТК ГА им. В.П. Чкалова)**, 55.380–55.382 N,
  39.007–39.009 E — **seven** `historic=aircraft` nodes in OSM, unnamed. This is a real
  cluster of preserved training airframes (two of them, a Tu-104A CCCP-42338 and an Il-18A
  CCCP-75644, are traceable through russianplanes.net as ex-VDNKh exhibits sent to
  Egoryevsk). russianplanes.net does **not** carry it as a museum, and no per-airframe
  identification could be made for the other five. **Recorded here as a lead, not as a
  site.** It is the largest single gap left in this area.

**Seed-list items that yielded nothing:**
- **Snegiri** (Ленино-Снегирёвский военно-исторический музей) — the open-air display is
  tanks, self-propelled guns, artillery, an S-75 SAM on its loader and an S-125 launcher.
  **No aircraft at all.** No site record created.
- **Dubosekovo** — the 28 Panfilov Guardsmen memorial. Sculpture and a small museum; no
  aircraft.
- **Ostafyevo** — nothing found. No `historic=aircraft` node in OSM anywhere near the
  airfield, and no russianplanes.net entry.
- **Chkalovsky** — active air base; no accessible display and no museum entry.
- **Serpukhov, Noginsk, Kolomna** — only town plinths (listed above), no museum aircraft.
- **A-90 Orlyonok ekranoplan**, Severnoye Tushino park, Moscow (55.8516, 37.4563) —
  displayed at the Navy museum alongside the submarine B-396. Genuinely borderline: it is
  a wing-in-ground-effect vehicle, not an aeroplane, and none of `fixed_wing` /
  `lighter_than_air` fits it honestly. **Excluded**; flagged here in case the database
  wants it.
- **Tupolev company display** — searched for; no publicly viewable preserved airframe at
  the Tupolev works on Naberezhnaya Akademika Tupoleva was found. russianplanes.net cards
  a Sukhoi OKB site and a MAI site but no Tupolev one.
- **Preserved airliners on public display in the region** — the only ones are the VDNKh
  Yak-42 CCCP-42304 (recorded) and the Tu-144 CCCP-77114 at Zhukovsky (recorded). Every
  other Tu-134/Tu-154/Il-86/Il-62 found in the sweep is a ground trainer, a restaurant/
  club conversion or a plinth (list above); the best known of those, the Tu-104 that
  stood in front of the Vnukovo terminal, is a plinth aircraft and is deferred.

---

## 6. Fields deliberately left blank

- **`year_built`** is blank on 216 of 227 rows. It is populated only where a construction,
  roll-out or first-flight date is directly sourced: the Su-15 type register on
  russianplanes.net (Su-15 0815331 → 1968, Su-15TM 1215309 → 1974, Su-15 0015301 → 1966)
  and kpopov.ru's dated build statements (MiG-19P 62210431 → March 1956, MiG-23UB 0903716
  → 3 April 1980, Su-27UB 96310422069 → 30 November 1990, Su-27 36911027514 → 9 February
  1989). One soft case is flagged in the description: the Zadorozhny MiG-19SV year is the
  sub-type's production year from kpopov.ru, not a nameplate.
- **`tail_number`** is blank on 27 rows — every case where no bort number is on record or
  where the airframe demonstrably wears none (the Patriot Su-27 in Su-57 camouflage, the
  Su-27UB, all three Air Defence Forces Museum aircraft, most MAI hangar airframes, the
  Panki V-12 for the registration conflict above).
- **`website`** is blank for the Mil plant, the Sukhoi bureau, the three Kubinka
  collections and the Lukhovitsy plant — none has a museum web presence.
- **`postal_code`** for the Kubinka sites is the town's (143070); the base has its own
  military postal arrangements which were not established.
- **`model_name`** is blank wherever the NATO or popular name would merely echo the
  designation, and on all spacecraft rows.
- **`aircraft_name`** is blank throughout — no airframe in this area carries an individual
  name that is part of its identity.

---

## 7. Open questions, most consequential first

1. **The Gromov Flight Research Institute stored fleet at Zhukovsky.** Around 76
   airframes, including several of the most historically important aircraft in Russia —
   Tu-155 (the hydrogen/LNG testbed, CCCP-85035), Tu-144D CCCP-77115, the VM-T Atlant
   RF-01502, the MiG 1.44 demonstrator, the S-37/Su-47 Berkut "01 blue", the Su-35 "901"
   and four Tu-204 development airframes. They are stored on an active flight-test
   airfield, not displayed, and the spec excludes operational aircraft. Whether the
   database wants them at all, and under what site, is a policy call this pass could not
   make. If yes, that is one large additional site.
2. **Which V-12 carries CCCP-21142** — Monino's or the Mil plant's at Panki?
   russianplanes.net puts the registration on the Panki machine (works number 001) while
   the already-live Monino record uses it too. Only two were built. Left blank at Panki.
3. **Egoryevsk Aviation Technical College** — seven airframes mapped, none identified. A
   real collection with no registry coverage. Needs a Russian-language photo report or a
   VK album.
4. **The Air Defence Forces Museum at Zarya** — three aircraft, zero bort numbers, and no
   registry coverage. Also unconfirmed whether the MiG-31 is a complete airframe or a
   nose/cockpit section.
5. **Poklonnaya Hill's June 2025 transfer: temporary or permanent?** The museum called it
   temporary. If the eight aircraft come back, this site record needs reversing and
   Monino's needs trimming.
6. **The Poklonnaya Bell fighter: P-63 or P-39?** Two sources against one.
7. **The Zadorozhny MiG-27 "51"** — on kpopov.ru in 2021, absent from russianplanes.net.
   Present or gone?
8. **The VDNKh "Vostok-1 descent module"** — flown capsule, engineering duplicate, or
   mock-up? The label as reported does not square with the flown capsule being at RKK
   Energia.
9. **Lukhovitsy: MiG-23UB "55 red" (russianplanes.net) versus MiG-23ML "96" (OSM)** — one
   aircraft mis-sourced, or two aircraft?
10. **Patriot Park bort numbers generally.** The 121st ARZ repaints on a rolling basis and
    every source disagrees with every other by one repaint cycle. The numbers recorded
    here are russianplanes.net's as of September 2026 and should be re-verified against
    2026 photography before anyone treats them as fixed.
