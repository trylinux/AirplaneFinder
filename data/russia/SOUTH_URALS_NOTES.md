# Southern Russia, the North Caucasus and the Urals — research notes for airplane.museum

Pass covers 26 sites and 260 airframes/missiles, swept as:
Rostov Oblast → Volgograd → Astrakhan → Krasnodar Krai and the Black Sea → Stavropol and the
North Caucasus republics → Crimea and Sevastopol → Sverdlovsk → Chelyabinsk and Kurgan →
Orenburg → Bashkortostan and Udmurtia.

Everything below is what a future researcher needs in order not to repeat this work or its
mistakes. Evidence date for the whole pass: **September 2026**.

---

## 1. Crimea and Sevastopol — say the quiet part out loud

Four sites in this pass are in Crimea and Sevastopol:

| Site | Location |
|---|---|
| Patriot Park Sevastopol | Karantinnaya Balka, former Yuzhny airfield |
| Patriot Park Belbek | Belbek |
| Mikhailovskaya Battery Military History Museum | Northern Side, Sevastopol |
| *(excluded)* Yevpatoria repair plant, Kacha memorial, Simferopol | see §7 |

**`country` is recorded as `Russia`** for all of them. That is the spec's instruction
(`country` is `Russia` for this build-out) and it is a schema choice, not a legal finding.
Crimea and Sevastopol are internationally recognised as **Ukrainian territory under Russian
occupation since 2014**; the UN General Assembly, and essentially every state outside Russia,
does not recognise the annexation. Every one of the four Crimean aircraft records carries a
sentence saying so in `description`, so the choice is visible in the data rather than silent.
If the database later grows a "disputed / de facto administration" field, these are the rows
to revisit, and `state_province` is `Sevastopol` for all of them.

Two second-order consequences worth knowing:

- The airframes at Belbek and Patriot Park Sevastopol are on or beside active military
  installations that have been struck repeatedly since 2022. Their survival is not a safe
  assumption; russianplanes' newest photographs for Belbek date from before the heaviest
  strikes on that airfield. Treat these three Belbek rows as the least reliable in the file.
- The **Kacha naval aviation museum does not exist any more** and has not since 2006 — see §4.

---

## 2. Sources

**Primary: russianplanes.net.** Far more usable than its front page suggests. Three endpoints
did nearly all the work and are worth writing down:

- `/museums` — the full museum index with numeric IDs.
- `/monuments/?...&smuseum=<id>&kmlExport=1` — a **KML export of every recorded airframe at
  that museum**, with type, bort number, per-airframe coordinates and a link to the monument
  card. The same endpoint with `region=<Russian oblast name>` instead of `smuseum` dumps every
  recorded airframe in a region, which is how the sites *missing* from the museum index were
  found (cluster the points, look at every cluster of 3+).
- `/monument/<id>` — construction number, bort number, museum, coordinates and, critically,
  **status**: `памятник/музейный экспонат` (monument/exhibit), `просто борт на
  хранении/тренажер` (just a stored airframe or trainer), `бывший памятник/перемещён`
  (former monument, moved away), `фрагмент` (fragment).
  `/reginfo/<id>` then gives build date, first flight, operator history and comments.

The status field is the single most valuable thing on the site and is what caught the two
biggest errors in this pass (§3). It is not exposed in the KML — you must fetch the card.

**Secondary:** ru.wikipedia (via the API — `ru.wikipedia.org` is cache-only to the fetch tool
and must be pulled through `action=query&prop=extracts`), museum websites, and dated
photography referenced from the russianplanes cards.

### Sources that proved stale, specifically

- **`avia-museum.ru`** — the Taganrog museum's official domain, still linked by russianplanes
  and by every Russian tourism directory. The domain has lapsed and now serves an
  airline-ticket affiliate site with no museum content whatsoever. `website` is left **blank**
  for Taganrog rather than pointing at the squatter.
- **`museum.elem.ru`** — the URL russianplanes gives for the Verkhnyaya Pyshma museum. It is
  now a bare login page. The live site is **`mkugmk.ru`**, which is what is recorded.
- **russianplanes museum cards' opening hours** are frequently years out of date; the site
  itself warns about this on every card. Kurgan is a worked example: the card says Tue–Sun
  10–17, ru.wikipedia says 10:00–16:00 closed Monday and Tuesday. Neither is recorded in the
  CSV (there is no hours field), but do not trust either without a fresh check.
- **ru.wikipedia's Taganrog article** has no dated content later than November 2016 and does
  not list the two most significant recent arrivals (the A-50 and the An-12B).
- **ru.wikipedia's Kurgan article** lists 15 aircraft including a Yak-52 and an An-2 that
  russianplanes shows as removed in 2015 and 2024 respectively. The CSV records 13.

---

## 3. The two findings that change the shape of the region

### 3.1 Mamayev Kurgan has no aircraft. The site is excluded.

The seed list asked for Mamayev Kurgan and the Museum-Panorama of the Battle of Stalingrad.
russianplanes museum #287 (Волгоград — Мамаев курган) lists seven aircraft: MiG-23M 03,
MiG-21U 21, MiG-19S 24, Il-2, MiG-17 240, L-39 39, L-29 29. **All seven monument cards carry
the status `бывший памятник/перемещён`** — former monument, moved away.

They moved twice. The aircraft were originally the collection of the **Kacha Higher Military
Aviation School for Pilots**. When Kacha was disbanded in 2006 the airframes passed to the
Stalingrad Battle Museum-Reserve, stood for several years on the ramp of the museum-panorama,
were moved to Mamayev Kurgan in 2010, and in **June 2020** were transferred out again to the
Chislov aero club at **Srednyaya Akhtuba**, about 30 km east across the Volga. The individual
monument cards for the Srednyaya Akhtuba airframes say so explicitly and cite the local press
report of the move.

So: Volgograd city has no museum aircraft. Everything the seed expected to find at Mamayev
Kurgan is now in the `srednyaya_akhtuba_aircraft.csv` file, and five of those rows carry the
Kacha → museum-panorama → Mamayev Kurgan → Srednyaya Akhtuba provenance in `description`.
The Museum-Panorama of the Battle of Stalingrad itself holds no aircraft.

### 3.2 The Taganrog museum is alive and still acquiring.

The seed flagged funding and premises trouble, and the museum's history justifies the worry:
it was founded in April 1995 out of the aircraft-scrapping base set up under the CFE Treaty
(around 300 fighters and fighter-bombers were cut up at Taganrog), it has a **staff of two**,
it sits on the guarded site of the 325th Aircraft Repair Plant as a subdivision of the plant
rather than as an institution in its own right, and its curator has spent thirty years
petitioning for municipal museum status without getting it.

But it is open and growing. Two recent acquisitions establish this from primary registry data:

- **A-50 "15 red"** (c/n 073410311) — airframe completed September 1977, converted to A-50
  AEW configuration October 1983, served with 143 OAO DRLO at Ukurey until the unit disbanded
  in late 1992. Now a museum exhibit.
- **An-12B "20 blue"** (c/n 5342806, built 1965) — a registry comment dated 11 April 2025
  records the transfer to the "Museum of Aviation Technology of OAO 325 ARZ, Taganrog" in
  **November 2024**, and the aircraft was photographed on the museum site in **2025**.

Neither aircraft appears in any directory listing or in the Wikipedia article. `access_type`
is `appointment`: the museum takes bookings (weekdays 08:00–14:00, by prior arrangement) but
entry is onto a defence-plant site, so it sits right on the appointment/restricted line.

---

## 4. Local-language names

| CSV name | Russian |
|---|---|
| Taganrog Aviation Museum | Таганрогский музей авиационной техники (при 325 АРЗ) |
| Aksay Military History Museum | Аксайский военно-исторический музей, площадка «Мухина балка» |
| Rostvertol Helicopter Plant Museum | Музей ПАО «Роствертол» |
| Patriot Park Kamensk-Shakhtinsky | Парк «Патриот», Каменск-Шахтинский |
| Chislov Aero Club Aviation Museum | Волгоградский областной АСК им. А. М. Числова, Средняя Ахтуба |
| Kamyshin Victory Park Military Equipment Display | Парк Победы, Камышин |
| Akhtubinsk Flight Test Centre Aviation Museum | Музей при ГЛИЦ им. В. П. Чкалова, Ахтубинск |
| Military Hill Open-Air Museum | Музей под открытым небом «Военная горка», Темрюк |
| Anapa Military Equipment Park | Сквер (парк) военной техники, Анапа |
| Bakhchivandzhi Memorial Park | Парк им. Г. Я. Бахчиванджи, ст. Бриньковская |
| ARZ-411 Aviation Repair Plant Museum | Музей АРЗ № 411, Минеральные Воды |
| Patriot Park Derbent | Парк «Патриот», Дербент |
| Patriot Park Sevastopol | Парк «Патриот», Севастополь (Карантинная балка) |
| Patriot Park Belbek | Парк «Патриот», Бельбек |
| Yeysk Naval Aviation Combat Training Centre | 859-й ЦБП и ПЛС морской авиации ВМФ, Ейск |
| Mikhailovskaya Battery Military History Museum | Военно-исторический музей фортификационных сооружений — Михайловская батарея |
| Battle Glory of the Urals Museum of Military Equipment | Музей военной техники «Боевая слава Урала» (Музейный комплекс УГМК) |
| Yekaterinburg Air Force and Air Defence Headquarters Aircraft Display | Музей штаба 2-го командования ВВС и ПВО |
| Kurgan Aviation Museum | Курганский авиационный музей |
| Orenburg Civil Aviation Museum | Оренбургский музей авиации (Музей гражданской авиации) |
| Frunze Garden Aviation Display | Городской сад им. М. В. Фрунзе, Оренбург |
| Ufa Aviation Technical University Training Ground | Учебная площадка УУНиТ (УГАТУ), Уфа |
| Victory Garden Military Equipment Museum | Музей военной техники в Саду Победы, Челябинск |
| Chelyabinsk Air Force Navigator School Museum and Display Park | ЧВВАКУШ, ныне филиал ВУНЦ ВВС «ВВА», военный городок 11 |
| Troitsk Aviation Technical College Training Park | Троицкий авиационный технический колледж ГА |
| Vertolyot Aviation Park | Авиапарк «Вертолёт», Кумертау |

---

## 5. Verkhnyaya Pyshma — recorded as one site, and why

The UGMK Museum Complex is the largest thing in this pass by a wide margin: 52 airframes
recorded here, on a 13-hectare campus with **five separate exhibition centres**, one address
and one ticket office:

1. Музей военной техники (2013, three storeys) — the "Boevaya Slava Urala" military museum
2. Музей автомобильной техники (2018, second building 2022)
3. **Музей авиации «Крылья Победы» (2021)** — the aviation hall, >10,000 m²
4. Музей «Парадный Расчёт» (2020)
5. Выставочный центр «Буран» (2026)

I recorded **one site**, named as the seed named it. Splitting it into "Battle Glory of the
Urals" and "Wings of Victory" would be more precise in principle, but I could not do it
honestly: russianplanes' indoor coordinates are approximate and in several cases predate the
2021 opening of the aviation hall, and only five airframes (R-5, Hurricane IIB, MBR-2, P-39F,
P-63C-5) reverse-geocode to the hall's own address, ul. Aleksandra Kozitsyna 4V. Assigning the
other WWII types by eye would have been a guess. **This is the highest-value split for a
future pass** — see §9.

### The collection is under-counted here, and by how much

The museum's own site says the Wings of Victory hall holds **"more than 40 aircraft"** on two
floors out of a collection of 70+ items. russianplanes' monument database carries far fewer
indoor exhibits. A dated (November 2022) visitor account lists these types in the hall for
which **no airframe identity was found and which are therefore NOT in the CSV**:

I-153 Chaika, I-15, La-5F, La-5FN, Messerschmitt Bf 109G-6, Avro 504 (modern flying replica),
Supermarine Spitfire Mk Vb (new-build static), Focke-Wulf Fw 190A-8 (1990s Flug+Werk replica),
Douglas DC-3, North American B-25J, Douglas A-20H, Consolidated PBY-5A Catalina, Po-2,
Avro Lancaster fuselage sections, MDR-6 wreckage.

That is a substantial Western-type collection sitting outside this file. It was left out
because a blog post is not an airframe identity — no registrations, no construction numbers,
no way to satisfy "never invent". Anyone continuing this work should start there.

### Replicas and mockups at Verkhnyaya Pyshma

Five exhibits are recorded by russianplanes as `макет` (mockup) and are described as such,
never as originals: **I-16 "13 white"** (marked ZA SSSR!), **U-2 "9"**, **MiG-3 "5"**,
**Yak-1B "44"**, **LaGG-3 "43"**.

A sixth, the **I-16** with no bort number, carries a placeholder construction number
("НеизвЗавИ16-УГМК" — literally "unknown factory") and a build date of about 2000. That is a
modern full-scale reproduction, not a wartime airframe; `year_built` is left **blank** because
a placeholder c/n beside a round-number date is not a sourced construction date. It was
previously displayed as "34 red".

For the restored wartime types (SB, R-5, Yak-9U, MBR-2, Yak-3, Tu-2, Pe-2FT, and the two
MiG-3s numbered 31 and 8) I say in `description` that how much original structure survives the
restoration is not established. Soviet wreck-recovery restorations range from genuinely
original to effectively new-build, and I found no per-airframe evidence either way. The one
that *is* documented is the **Il-2M "12 white"** (c/n 1874839), built 10 January 1943 and
delivered to 57 PShAP of the Baltic Fleet air force — that history is in the registry and is
recorded.

**Buran 2.01 "Baikal"** is the real thing: the third flight article of the Energiya-Buran
programme and the first of the second series, construction abandoned in 1993, brought to
Verkhnyaya Pyshma on 5 August 2024 and now in the Buran exhibition centre opened in 2026.
Restoration is ongoing; `display_status` is `on_display` because it is exhibited, but the
museum says external and internal restoration work continues.

---

## 6. Corrections made, with evidence

- **Mamayev Kurgan → Srednyaya Akhtuba.** Seven airframes. Evidence: `бывший
  памятник/перемещён` status on all seven Volgograd cards, plus the transfer note and press
  citation on the Srednyaya Akhtuba cards. Site excluded, airframes filed at the aero club.
- **Kurgan Aviation Museum: 13 aircraft, not 15.** An-2 RA-62458 was removed from the museum
  to the airport apron in 2024; Yak-52 RF-01084 was taken away by DOSAAF to its own airfield
  in September 2015. Both dropped. ru.wikipedia still lists both.
- **Kurgan MiG-17: bort 07, not 05.** The aircraft was repainted; russianplanes carries
  before-and-after photographs. `05` is in `aliases` as the number the airframe formerly wore.
  Handed to the museum in 1991 by the Kurgan higher military political aviation school and
  restored 1991–1994; c/n 54210609, built 1952.
- **Ufa: MiG-23MLA "69 red" is not at Ufa.** Its Ufa card is marked as moved; the airframe was
  taken to the Chelyabinsk navigator school in **September 2020**, and the Chelyabinsk card
  says "brought from Ufa 2020.09". Same c/n on both cards (0390310635). Filed once, at
  Chelyabinsk.
- **Kamensk-Shakhtinsky Mi-2 double-count.** Two monument cards, one annotated "moved closer
  to the road" and marked as a former monument, the other annotated "new position". One
  helicopter, one row.
- **Verkhnyaya Pyshma double-counts.** Mi-4A (cards 22553 and 23758, same registry ID 166236)
  and MiG-17 "17" (cards 23297 and 23767, same registry ID 274197 and the same photograph)
  are each a single airframe recorded twice. One row each.
- **Rostvertol Mi-6A wears a false registration.** The registry note states plainly that
  RA-21076 as painted at the plant museum belonged to the last Mi-6 to leave the Rostov
  factory in 1980, not to this 1966 airframe, and that the service history needs confirmation.
  Recorded as worn, with the doubt in `description`.
- **Chelyabinsk Sad Pobedy: c/n dropped from both L-29s.** russianplanes gives the same
  construction number (792470) for both machines, which cannot be right. Neither row claims
  a c/n; the conflict is stated in `description`.
- **Tu-154B-1 RA-85287 is recorded in two places.** russianplanes has an active card at
  Verkhnyaya Pyshma and another at the (closed) Perm Aviation Museum, whose registry comment
  says the *nose section* is at Perm. Filed once, at Verkhnyaya Pyshma, with the conflict
  stated. This is an open question (§9).
- **Taganrog c/n corrections.** MiG-23MLD "31 red" (c/n 0390310562, built 15 June 1978) left
  the factory as a **MiG-23MLA** for 32 GvIAP at Shatalovo and was converted to MLD standard
  at the 121st ARZ; recorded as MiG-23/MLD as it now stands, with the build identity in
  `description`.

---

## 7. Excluded, and why

**Excluded sites.** The spec's rule is major museums; gate guards and town plinths are a later
pass. I applied a working test: a named museum or organised military-technology park, or an
open-air collection of five or more airframes at an identifiable institution.

| Excluded | Why |
|---|---|
| **Mamayev Kurgan, Volgograd** | All seven aircraft moved to Srednyaya Akhtuba by June 2020 (§3.1). Zero aircraft remain. |
| **Museum-Panorama of the Battle of Stalingrad** | Holds no aircraft. It was a way-station for the Kacha collection, nothing more. |
| **Perm Aviation Museum** | **Closed in July 2023** and announced the sale of its exhibits; a new sponsor was announced in July 2024 but noise barriers block vehicle access and no reopening has happened. Most exhibits are reportedly still in place. 27 airframes are recorded by russianplanes. Also a boundary case for this brief — Perm Krai is in the Ural economic region alongside Ufa and Izhevsk, which *were* assigned, but Perm was not named in the seed list. **If the brief did mean to include Perm, this is the biggest single gap in the file.** |
| **183rd Training Centre, Rostov-on-Don** | 12 airframes on a closed MoD site, including a Su-34 (RF-92251), MiG-31, two Mi-28Ns and a Yak-130 — recent combat types, all recorded as stored airframes/trainers rather than monuments. I could not establish that they are withdrawn rather than serviceable, and "operational aircraft are not displays". Excluded deliberately; see §9. |
| **Krasnodar (KVVAUL and 275th ARZ)** | The seed expected a Krasnodar collection. **There isn't one.** There are about 15 individual airframes scattered across two closed sites — the Krasnodar flying school campus (ul. Dzerzhinskogo 135) and the 275th Aircraft Repair Plant (ul. Aviagorodok 30) — as gate guards, anniversary monuments (the MiG-29UB "50" for the 50th anniversary of Victory, the MiG-21U "60" for the 60th of the Soviet armed forces, the L-39C "60" for the plant's own 60th) and simulator-park airframes. No museum, no public access, no coherent site. One of them, MiG-21M "30", was **dismantled in late October 2018**. This is plinth-pass material. |
| **Yevpatoria aircraft repair plant, Crimea** | Four Yak-38/38M/38U and an Il-14 as plant-grounds monuments. The Il-14 is locally said to have been Bulganin's personal aircraft — unverified. Not a museum. |
| **Kacha, Crimea** | The Kacha school museum was dispersed in 2006 (§3.1). What remains at Kacha today is a memorial group of three items — an Il-2M, a Ka-27PL and a KS-1 missile — erected as a monument to the defenders of the sky, not a museum. |
| **Simferopol** | The cluster there is a space-technology exhibit (Vostok, Voskhod and Soyuz descent modules, Kedr/Delta/TNA-2.5 antennas). Its one aircraft, Il-18B CCCP-75689, is marked as a former monument. No aviation museum. |
| **Kushchevskaya, Cherkessk, Orenburg-Rostoshi, Maykop, Nalchik, Grozny, Vladikavkaz, Stavropol, Sochi, Astrakhan city, Izhevsk, Magnitogorsk, Buguruslan, Koltsovo** | City parks, aeroclubs, training grounds and single plinths — two to five aircraft each, no museum. Notable individual items are listed below. |
| **Nizhny Tagil (Uralvagonzavod / RAE range)** | Checked specifically because the seed asked. **The Nizhny Tagil arms range holds no aircraft.** The whole of northern Sverdlovsk Oblast has only scattered plinths — a Su-9 at 57.9623/59.9875 near Nizhny Tagil, a MiG-25RB and an Mi-8 outside the officers' house at Nizhnyaya Salda (58.036/60.386), an An-24B being erected in a Victory Park from August 2025 at 58.370/59.852. |

**Notable excluded individual airframes**, for whoever does the plinth pass:

- **Sochi**: a Buran full-scale article at 43.4145/39.9492, plus Tu-134AK RA-65939 and
  Tu-154M RA-85632 preserved at Adler, and a Su-7B inside the Air Force sanatorium grounds.
- **Stavropol**: Il-18V CCCP-75767 (repainted, original titles and registration overpainted),
  and a MiG-21FL moved to a **Patriot Park under construction at Stavropol, for restoration
  and installation in August 2026** — a future site, worth re-checking.
- **Adygea**: Retro-technology museum "Faeton" near Maykop (An-2R RA-31495, Mi-2, and an
  Mi-8-family helicopter that appeared in summer 2025). Small but genuinely a museum.
- **Kabardino-Balkaria**: Nalchik aero club (Mi-4A CCCP-14113, MiG-15UTI, Yak-52 RA-00237,
  Yak-40 RA-87436, An-2 RF-00397) and a Tu-124 CCCP-45032 in Nalchik.
- **Dagestan**: Tu-134B-3 RA-65579 and An-2T RA-35410 at Makhachkala.
- **Ingushetia**: MiG-29 "25 red", the Sulambek Oskanov memorial at Magas airport (2012).

**Excluded objects inside included sites**: an aerosani NKL-26 mockup and an autolift and
passenger stairs at Kamensk-Shakhtinsky and Verkhnyaya Pyshma (not aircraft); the "Baikal"
reusable booster demonstrator and an Angara-1 at Verkhnyaya Pyshma (space exhibits I could not
establish as flight hardware or model — note that this "Baikal" is a *different* object from
Buran 2.01 "Baikal", which is included); an unidentified biplane at Akhtubinsk with no type
attribution; two aero-engine displays (M-105, AM-38) at Temryuk.

---

## 8. Judgment calls

**`region` — Europe or Asia.** The spec says Europe west of the Urals, Asia east. Applied by
oblast: Sverdlovsk, Chelyabinsk and Kurgan are **Asia**; Rostov, Volgograd, Astrakhan,
Krasnodar, Stavropol, Dagestan, Sevastopol, Bashkortostan and Orenburg are **Europe**.
Orenburg is the awkward one — the Ural River runs through the city and the airport sits on
the far bank, so the Orenburg Civil Aviation Museum is arguably in Asia by the strict river
boundary. Both Orenburg sites are filed as Europe because Orenburg Oblast is administratively
in the Volga Federal District and conventionally counted as European Russia. Flag if the
database prefers the strict watershed.

**`access_type`.**
- `restricted` — inside an active military establishment needing a pass: Akhtubinsk (929th
  GLIC), Yeysk (859th Centre), the Yekaterinburg headquarters display, the Chelyabinsk
  navigator school, the Ufa university training area, the Troitsk college park.
- `appointment` — takes bookings: Taganrog (weekdays 08:00–14:00, by prior agreement, on a
  guarded plant site), Rostvertol, Mineralnye Vody (ARZ-411), Srednyaya Akhtuba, Kumertau.
- `public` — everything else, including all four Patriot Parks, Temryuk, Kamensk-Shakhtinsky,
  Verkhnyaya Pyshma (10:00–19:00, closed Monday, paid), Kurgan, Aksay (09:00–17:00 daily) and
  the Orenburg airport display.

**`display_status = in_storage`.** Used for airframes russianplanes marks as `просто борт на
хранении/тренажер` — stored airframes and ground trainers rather than monuments. That is all
13 Ufa rows, all 7 Troitsk rows, the Yeysk Mi-8 parachute trainer, and the Mineralnye Vody
Tu-154 RA-85330 (in a hangar as a survival trainer, wings and tailplane cut down, ~3 km from
the plant museum). It is the honest reading: these are preserved airframes used for teaching,
not exhibits.

**Two sites are teaching parks, not museums** — Ufa and Troitsk. They are included because
each is a coherent collection of 7–13 preserved airframes at a named institution, which the
spec's "big open-air collections" clause covers. If the database wants museums only, drop
`ufa_ugatu` and `troitsk`.

**The Lun ekranoplan** at Derbent is recorded as `fixed_wing` / `monoplane` / `other`. It is a
ground-effect vehicle, not an aeroplane, but it is the single most notable preserved object in
the North Caucasus and losing it to a taxonomy argument would be worse than the imprecision.
Project 903, the only one built, completed at Gorky in December 1989 and beached at Derbent in
July 2020; hull only, launchers and most equipment absent.

**Missiles.** Kept where they are part of an aviation display: R-17 (Scud) at Kamyshin;
P-5 and P-15 at Temryuk; KS-1, P-15 and P-35 at the Mikhailovskaya Battery; MR UR-100 and the
R-36M2 transport-launch container at the Frunze Garden. Manufacturers are attributed to the
design bureau (Makeyev, Raduga, Chelomey, Yuzhnoye, Mikoyan-Gurevich for the KS-1).

**Cockpit sections and fragments are recorded as rows**, with the fact stated in
`description`: Taganrog's Su-17UM3 cockpit and Tu-154M RA-85726 nose section, and the
Chelyabinsk school's MiG-31 and Su-24 cockpits held indoors.

**Fields deliberately left blank.**
- `year_built` — blank on 147 of 260 rows. Only populated from a sourced construction,
  roll-out, first-flight or delivery date in the russianplanes registry. Construction numbers
  are never treated as dates. Where the registry itself flags the year as an estimate (the
  Yeysk Yak-38M, the Mikhailovskaya Battery Yak-38U) the year is recorded and the estimate is
  stated in `description`.
- `tail_number` — blank where the card carries no bort number or a bare `?`. A bort number
  that cannot be read is not a bort number.
- `postal_code` — only where a source gave one: Taganrog 347916, Aksay 346720, Verkhnyaya
  Pyshma 624091, Mineralnye Vody 357202, Kurgan 640015.
- `website` — blank where none exists or the domain has lapsed (Taganrog, §2).
- `model_name` — blank where the NATO or popular name merely echoes the designation, and on
  types that never got one (Yak-1, Yak-3, MiG-3, LaGG-3, Su-34 rows where the reporting name
  adds nothing).
- `aircraft_name` — used twice only: Buran 2.01 "Baikal" and the Be-12P "Stoykiy".

**Untailed rows** are made distinguishable per the spec: `first of two` / `second of two`
aliases at Srednyaya Akhtuba (two L-29s, two MiG-17s), Kamensk-Shakhtinsky (two Mi-8s),
Kumertau (two Ka-26s), Verkhnyaya Pyshma (three MiG-3s: `first of three` is the mockup,
`second` and `third` the restorations), and the Chelyabinsk school (two Su-24s, one complete
and one a cockpit).

---

## 9. Open questions, ranked

1. **Split Verkhnyaya Pyshma, and identify the Wings of Victory collection.** The museum
   claims 40+ aircraft in the aviation hall; 52 are recorded here for the whole complex and
   the Western types (Bf 109G-6, Spitfire Vb, Fw 190A-8, DC-3, B-25J, A-20H, PBY-5A Catalina,
   Avro 504, La-5F/FN, I-153, I-15, Lancaster sections, MDR-6) have no airframe identities in
   any source reachable from here. This needs the museum's own catalogue or a serial-level
   survey. It is the single largest unrecorded collection in the region.
2. **Is the Perm Aviation Museum in scope, and does it still exist?** Closed July 2023,
   sponsor announced July 2024, no reopening; ~27 airframes reportedly still on site, and
   Verkhnyaya Pyshma has already bought at least one of them (An-2R RA-33353, 2023). Someone
   needs to decide whether Perm Krai belongs to this brief and then establish, on the ground,
   what is left.
3. **Tu-154B-1 RA-85287 — Verkhnyaya Pyshma or Perm, and is it one airframe or two pieces?**
   Registry says the nose section is at Perm; a live card exists at Verkhnyaya Pyshma. Filed
   at Verkhnyaya Pyshma. An airframe is in exactly one place, so one of these cards is wrong.
4. **The 183rd Training Centre, Rostov-on-Don.** Twelve airframes, deliberately excluded
   because I could not establish that the Su-34, MiG-31, Mi-28Ns and Yak-130 are withdrawn.
   If they are ground instructional airframes like Ufa's Su-34, this is a real 12-aircraft
   site and should be added as `restricted`.
5. **Do the Belbek and Sevastopol Patriot Park aircraft still exist?** Both sites are on or
   beside airfields struck repeatedly since 2022 and the newest photography predates the worst
   of it. Seven rows depend on this.
6. **Kumertau duplicate cards.** russianplanes carries a Ka-32, a Ka-26 and a Tu-143 at the
   KumAPP plant gate (ul. Palatnikova 4) and a Ka-32, a Ka-26 and a Tu-143/243 at the
   Vertolyot park 400 m away. Same three types. These are probably the same three machines
   recorded before and after the park was laid out. Five rows are filed at the park; if the
   plant-gate cards are live, up to three are missing.
7. **What exactly is the Yekaterinburg site at Pervomayskaya 94?** russianplanes calls it the
   museum of the headquarters of the 2nd Air Force and Air Defence Command — a formation since
   renamed. Six aircraft. There is a separate and better-known "Museum of the Battle Glory of
   the Urals" at the Officers' House, Pervomayskaya 27, about 1.5 km west, at which no
   aircraft were found. Confirm which institution owns the six airframes and whether the
   public can reach them.
8. **Anapa, Brinkovskaya, Aksay and Rostvertol have no construction numbers for most rows**,
   and Aksay's An-2 and Yak-52 have no bort numbers at all. Low value individually, but these
   are the weakest identities in the file.
9. **Kurgan opening hours** conflict between russianplanes and ru.wikipedia (see §2). Not a
   CSV field, but it will matter to anyone visiting.

## Crimea — country field (decided 9 Sep 2026)

The three Sevastopol-area sites (Patriot Park Sevastopol, Patriot Park Belbek, Mikhailovskaya
Battery Military History Museum — 14 airframes between them) are filed with `country` =
**Ukraine**, matching international recognition, even though all three are Russian-run and
russianplanes.net files them under Russia. The occupation is stated in the affected
`description` fields and above in these notes, so the situation is visible in the data rather
than hidden behind the country code. If the database is ever re-sorted on de facto control,
these are the three records to revisit.
