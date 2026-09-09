# Northwest Russia and the Volga — research notes

Scope worked: Northwestern Federal District (St Petersburg, Leningrad, Murmansk, Arkhangelsk,
Kaliningrad, Pskov, Novgorod, Vologda), the Volga Federal District as far east as Perm Krai,
and the specifically named central oblasts Tver, Yaroslavl, Voronezh, Kursk, Smolensk, Ryazan.
Moscow and Moscow Oblast, Ivanovo, Kostroma, Kaluga and everything east of the Urals were left
to other passes.

37 sites, 340 aircraft. Files: `nw_volga_museums.csv` plus one `<slug>_aircraft.csv` per site.

---

## 1. Sources

### Primary — russianplanes.net
The decisive source. Two parts of the site were used:

* `https://russianplanes.net/museums` — a worldwide museum register with, for the Russian section,
  111 entries carrying museum name, address, declared access mode (`Свободный доступ` /
  `По договоренности`) and an exhibit count. The page also embeds a Leaflet marker array giving each
  museum an internal id and a coordinate pair; those coordinates are what the `latitude`/`longitude`
  columns in `nw_volga_museums.csv` are built from, rounded to 4 decimals.
* An undocumented JSON endpoint the museum pages call:
  `https://russianplanes.net/?action=mapGetPoints&smuseum=<id>&mode=json&lat1=..&lon1=..&lat2=..&lon2=..`
  It returns, per airframe: type designation (`t`), registration or bort number (`g`), construction
  number (`s`), per-airframe coordinates, and a condition flag (`c`) with values
  `monument` (displayed), `stored`, `parts` (fragment only), `ex` (no longer present).
  Almost every construction number and bort number in the aircraft CSVs comes from this endpoint.

The same endpoint with no museum filter and a bounding box was used to sweep whole oblasts for
airframes the museum register does not carry — that is how the Kronstadt, Pulkovo, Lebyazhye,
Vsevolozhsk, Kaliningrad-Chkalovsk and Nizhny Novgorod Kremlin items below were found.

The `ex` flag was treated as authoritative: an airframe marked `ex` is **not** recorded, because the
spec's rule is that an airframe is in exactly one place and `ex` means it left. `parts` rows were
also excluded (fragments, not airframes) and are itemised in section 5.

### Secondary
* **ru.wikipedia.org** — used for the Ulyanovsk museum article (which carries the 2025 restoration
  citations), the Motovilikha museum article (which settles that its flight vehicles are ballistic
  missiles, not aircraft), and the Ostrov Fortov article. Note: `WebFetch` on ru.wikipedia.org is
  refused by the proxy ("domain is cache-only"); `curl` with `?action=raw` works and was used instead.
* **aviamirinfo.ru** — a 2019 photo survey of Ulyanovsk with registrations, construction numbers and
  per-airframe provenance. Used to cross-check russianplanes and to supply build/service history.
* **erofey_manager on LiveJournal**, a seven-part 2017-2019 survey of Engels; **russos**, **igor113**,
  **culttourism.ru**, **da-sv.ru**, **airmuseum.ru** for Engels context and access rules.
* **business-class.su**, **chitaitext.ru**, **aviamusey.ru** for the Perm closure.
* **spbguga.ru** and **aviamuseumspb.ru** for the St Petersburg civil aviation museum.
* **autotravel.ru** visitor threads for Engels and Safonovo access.

### What proved stale, and how
* **airmuseum.ru's Engels page** is a 2009 text reproduced unchanged; its comment thread (2012-2023)
  is the only current part of it, and it says visitors are turned away at the gate.
* **culttourism.ru's Engels entry** still prints a duty-officer phone number and 09:00-17:00 hours as
  if the museum were bookable. Nothing on the page is dated later than the 2010s.
* **autotravel.ru** for both Engels and Safonovo has no review later than 2012 and 2021 respectively,
  so neither can evidence 2025 opening.
* **russianplanes.net's own museum register** prints the warning
  "Внимание! Режим и условия работы музея могли измениться!" on every museum page, and it is right:
  the register still lists the **Perm Aviation Museum** (27 exhibits, "Свободный доступ") two years
  after that museum shut for good. The register is excellent for *what airframe is where*; it is not
  evidence a museum is open.
* **aviamusey.ru** (Perm) now serves nothing but the words "Авиамузей Пермь закрыт", and has an
  expired TLS certificate so `WebFetch` refuses it; the closure was confirmed from news reporting instead.
* Museum's own sites: `uvauga.ru/museum` (Ulyanovsk), `pkitis.tltsu.ru` (Togliatti), `sargmbs.ru`
  (Saratov), `avia-ryazan.ru` (Ryazan), `vatuga.ru` (Vyborg), `mvms.ru` (Kronstadt) are all recorded in
  the CSV `website` column but were not individually fetched; treat them as pointers, not as verified
  2026 opening evidence.

**Grokipedia was not used.**

---

## 2. Currency — what the evidence date actually is, per site

| Site | Best currency evidence | Confidence |
|---|---|---|
| Ulyanovsk | Aug 2025 press: twelve airframes under restoration for the institute's anniversary | strong, open |
| Perm Aviation Museum | Aug 2023 press: closed permanently, collection dispersed | strong, **excluded** |
| Kronstadt Museum of Naval Glory | opened 2023, K-3 submarine hall, current ticket prices published | strong, open |
| Engels | no dated visitor account after 2012; base repeatedly struck by long-range drones 2022-2025 | weak; recorded `restricted` |
| Safonovo | ZATO pass rule documented; latest visitor account 2021 | weak; recorded `restricted` |
| Kazan KAI Tu-144 | move to ul. Chetaeva reported 2020, university interactive-exhibit programme since | moderate |
| Everything else | russianplanes.net register and per-airframe records, most photographs 2014-2024 | moderate |

Nothing in this set was verified by a 2026 visit. Where a site's status could not be evidenced later
than about 2019 that is said in the airframe `description` text as well.

---

## 3. Judgment calls

### access_type
* **`restricted`** was used wherever a member of the public cannot get in without a military or ZATO
  pass, even if a phone number is published: **Engels** (inside the Engels-2 bomber base; entry only by
  written application to the unit commander, and the base has been an active target since 2022),
  **Ryazan-Dyagilevo**, **Savasleyka**, **Syzran VVAUL**, **Torzhok 344th Centre**, **Safonovo** and
  **Severomorsk** (both inside the closed town of Severomorsk; the Safonovo pass is normally arranged
  through the Northern Fleet museum in Murmansk or a Murmansk travel agency).
  The temptation with Engels is to call it `appointment` because a duty-officer number is printed on
  several tourist sites. It is not an appointment museum in any sense a visitor would recognise, and
  the most recent first-hand accounts describe being stopped by armed guards.
* **`appointment`** was used for institutional collections that genuinely take bookings from the
  public or from schools: Sokol plant, Kazan Helicopter Plant, KNITU-KAI, Sasovo, Vyborg, Rzhev
  ARZ-514, Voronezh Air Force academy, Gatchina engine museum, St Petersburg civil aviation museum,
  Samara University's Smyshlyaevka park.
* **`public`** follows russianplanes' `Свободный доступ` where the site is an open-air park or an
  ordinary ticketed museum.

### Replicas, reproductions and mock-ups
Recorded, and said so in `description`, never in `aliases`:
* **Ulyanovsk**: the **AK-1** is a full-scale mock-up (the ru.wikipedia article says `макет`); the
  **Po-2** carries a notional registration CCCP-1988 and no construction number and is almost certainly
  a reproduction; the **Tu-124Sh** wears the notional Aeroflot registration CCCP-45017 applied in 1984
  over its real service identity, bort 22 of the Chelyabinsk navigator school.
* **Safonovo**: the **I-153** is recorded by russianplanes with a construction-number field that
  literally reads "Макет", i.e. mock-up. The **MBR-2, I-16, Yak-9R, Yak-7B, SB, Il-4T, Hurricane IIC,
  P-39Q and Bf 109G-2** are wartime types restored from recovered material; the proportion of original
  structure could not be established from the sources used, and the descriptions say exactly that
  rather than claiming or denying originality.
* **Sokol plant**: the **La-5FN** and **I-16 type 28** carry no construction numbers and are very
  likely reproductions.
* **Kazan**: the **Pe-2** and both **Po-2s** (one in Victory Park, one at the helicopter plant) are
  reproductions; both Po-2s wear "3", which is why each row says which site the other is at.
* **Chkalovsk**: the **I-17** is necessarily a reproduction — no I-17 survives, only three prototypes
  were built. Recorded with its OKB designation TsKB-15 in aliases.
* **Saratov**: the **Yak-3** and **Nizhny Novgorod Kremlin**: the **La-7** have no construction number
  and no provenance in any source consulted; both descriptions say reproduction is likely.
* **Gatchina**: the **Farman** is a full-scale reproduction of an early Farman pusher; the exact type
  (Farman IV or another) is not established anywhere consulted, so `model` is left as `Farman` with a
  blank variant rather than guessing.
* **St Petersburg civil aviation museum**: the **DH.2** is a full-scale reproduction hung indoors.

### Missiles and rockets
`missile_rocket` rows were recorded only where the round is a headline exhibit of an aviation or
rocket collection: the Kh-20/Kh-22/Kh-55/KSR series at **Engels** and **Ryazan**, the Kh-22 at
**Saratov**, the P-15 at **Kaliningrad**, the RT-2 at **Togliatti**, the R-12 and RT-2 at
**Motovilikha**, the R-2 at the **Artillery Museum**, and the Soyuz launch vehicle at **Samara
Космическая**. Generic S-75 / S-125 / S-200 surface-to-air launchers standing in half a dozen of
these parks were deliberately **not** recorded — they are ground equipment displayed by the dozen and
would swamp the aircraft data. Their presence is noted in the relevant site descriptions.

### Aero-engines
Excluded everywhere. Ulyanovsk's D-30KP/D-36/TA-6A/VSU-10/Walter M-601E line and the whole of the
Gatchina engine museum bar the Farman are engines, and russianplanes files them under the same
endpoint as airframes. Only the Farman was recorded at Gatchina, which is why that site has one row.

### Ships, armour and rail
Excluded. Togliatti's Project 641B submarine, Kaliningrad's B-413 / Vityaz / Viktor Patsayev,
Kronstadt's K-3 and the Togliatti BZhRK missile trains are all recorded by russianplanes under the
same museum ids and were filtered out by the `tc` (transport class) field.

### Aircraft-adjacent craft not recorded
* **Nizhny Novgorod Victory Park** holds an *ATTK Akvaglayd* ground-effect craft named
  "Viktor Razzhivin". It is a wing-in-ground-effect vehicle, not obviously an aircraft under this
  schema, and no reliable type data was found. Excluded; flagged here.
* **Ulyanovsk** shows a Tu-22M aerodynamic model. Not an airframe. Excluded.
* **Togliatti** holds *Che-20* and one of two *Pchela-1TM* drones marked `ex`. Only the surviving
  Pchela-1T is recorded.

---

## 4. Corrections made, with evidence

1. **Perm Aviation Museum removed entirely.** russianplanes still lists it as a free-access museum
   with 27 exhibits at shosse Kosmonavtov 262. It closed in **August 2023** after the investor
   withdrew (director Sergey Pavlov, quoted by business-class.su, 23 Aug 2023); the collection of
   fuselages, gliders, helicopters and over 100 models went to private hands, and the museum's own
   site now shows only the words "Авиамузей Пермь закрыт". Recording it as an open site with 27
   aircraft would have imported a museum that no longer exists and 27 airframes whose present
   locations are unknown. **Perm is represented instead by the Motovilikha museum**, which is open —
   and which turns out to hold no aircraft at all, only ballistic missiles and artillery.
2. **Tu-144S CCCP-77107 relocated.** Several English lists still put it at the Kazan aircraft plant.
   russianplanes has the plant position flagged `ex` and an active record at ulitsa Chetaeva; Tatar
   press reported the move to the KNITU-KAI campus, where the university has developed it as an
   interactive exhibit (tu-144.kai.ru). Recorded at KAI, not the plant.
3. **MiG-23M c/n 021001104 (bort 141) relocated.** russianplanes carries it twice: `ex` at the Samara
   University Smyshlyaevka park and `monument` at Togliatti. Recorded once, at Togliatti.
4. **MiG-21bis c/n 75025087 (bort 06 blue) relocated.** Listed as `stored` at the Sokol plant and as a
   `monument` in Nizhny Novgorod Victory Park. One airframe. Recorded once, at the Victory Park, which
   is where the display record is.
5. **MiG-19SV c/n 0715372 relocated.** Listed as `stored` at Pushkin (59.777N 30.109E) and as a
   `monument` at Gatchina wearing bort 954 blue. Recorded once, at Gatchina.
6. **Tu-134UBL c/n 64182 (bort 34 red) is at Saratov, not Engels.** The erofey_manager Engels survey
   describes it as part of the Engels story but locates it in Victory Park, Saratov, and notes it
   previously wore bort 25 blue. russianplanes files it under Saratov. Recorded at Saratov.
7. **Engels An-24: two aircraft, not one, and the variants conflict.** Published accounts describe an
   "An-24T bort 01 red, built 1969 in Irkutsk, transferred 1998" and an "An-24VSR bort 57 red c/n
   8910609, 1968". russianplanes has both: An-24T bort 01 c/n 8910903 and An-24**RT** bort 57
   c/n 8910609. Both are recorded; the variant conflict on bort 57 is stated in its description.
8. **Engels An-12: unresolved conflict recorded rather than smoothed over.** erofey_manager gives
   An-12BP c/n 402512, 1962; russianplanes gives An-12A c/n 2400401. The row uses russianplanes and
   the description names the alternative reading. `year_built` is left **blank** because the two
   sources disagree about which airframe this is.
9. **Ulyanovsk Il-14P construction number.** aviamirinfo prints 146000709; russianplanes prints
   146000909. russianplanes was preferred as the registry of record. Flagged here.
10. **Ulyanovsk Yak-40 registration.** The aviamirinfo article body reads RA-87299 while its own
    keyword list reads RA-87229. russianplanes has RA-87299. RA-87299 used.
11. **Ulyanovsk Yak-18T construction numbers.** aviamirinfo gives CCCP-44422 c/n 22202023918;
    russianplanes gives c/n 2200401 for that registration and separate c/ns for the other two
    (RA-44251 c/n 0335, RA-44292 c/n 0236). russianplanes used; all three are distinguished by
    registration, so there is no key collision.
12. **Engels Tu-22 airframes are four distinct aircraft.** RDM bort 18, U bort 20, KD bort 77 and
    PD bort 46 — the four that arrived with the 203rd Air Regiment from Belarus. The Tu-22U is the
    only surviving trainer of the type. All four recorded separately with their own construction numbers.
13. **Operational aircraft excluded from Engels and Ryazan.** The erofey_manager survey's parts 5 and 6
    photograph Tu-160s (bort 03 "Pavel Taran", 05, 07, 10, 12, 17), Tu-95MS, Il-78M, Su-24M and
    Mi-8 wearing RF- registrations at Engels. These are in service, not exhibits, and are **not**
    recorded. Likewise the VM-T Atlant RA-01402 stored at Dyagilevo is airfield inventory, not a
    Ryazan museum exhibit — see open questions.
14. **Sokol plant: stored production stock separated from the display line.** russianplanes files
    eight unsold M-101T Gzhels (RA-15101/02/04/06/08/09/10/12) and six MiG-21 upgrade-programme
    airframes (bort 75, 901, 08, 06, 07 and the MiG-21-93 demonstrator) under the plant museum id.
    They sit 2-3 km from the display avenue on plant property. They are factory inventory, not museum
    holdings, and are **excluded**; only the eight aircraft on the display avenue are recorded.

---

## 5. Excluded, and why

### Sites excluded
* **Perm Aviation Museum** — closed August 2023 (above).
* **Kaliningrad Baltic Fleet Museum (Baltiysk)** — swept the whole oblast by bounding box; there is
  **no** preserved airframe recorded anywhere near Baltiysk. The museum holds no aircraft.
* **Central Naval Museum, St Petersburg** — swept; no aircraft at ploshchad Truda. The cluster of
  aviation items near it (I-16 bort 51, a P-15 and a VK-1 engine) geocodes to **Bolshaya Morskaya 69**,
  i.e. the **State University of Aerospace Instrumentation (GUAP)**, not the naval museum. GUAP was
  not recorded as a site: one reproduction I-16 outside a university building is a monument, not a
  museum collection.
* **Kursk** — sweep found six airframes in the oblast (three MiG-19PMs, a Mi-24, a MiG-29, a Mi-8T),
  all standalone monuments or airfield gate guards. **There is no aviation museum in Kursk.**
* **Smolensk** — sweep found nine, including the Yak-42 CCCP-10985 outside the Smolensk aviation
  plant, a Tu-16 c/n 1881501, MiG-23Ms and a MiG-21F-13. All monuments. **No aviation museum.**
* **Yaroslavl and Vologda** — sweep found the Il-18B CCCP-75518 and an Il-28U at Vologda, the
  Tu-104 CCCP-42460 at Rybinsk, and MiG-23s, an L-29, a Tu-141 and a Mi-1 around Yaroslavl. All
  standalone monuments. **No aviation museum in either oblast.**
* **Pskov and Veliky Novgorod** — sweep found only monuments (Su-25 bort 25 at Pskov, MiG-17s and
  Il-28s around Novgorod, an Il-76M fragment at Pskov). **No aviation museum.**
* **Ivanovo Museum of Military Transport Aviation** (Il-76MD CCCP-86913, An-22A RA-08830,
  An-12BK-PP, Li-2T, Il-14T, An-2TD, An-26, An-12BK — 8 airframes) and **Kostroma Victory Park** —
  real museums with aircraft, but Ivanovo and Kostroma oblasts are Central Federal District and
  outside the brief. Flagged for whoever covers central Russia.
* **Zelenodolsk Victory Park** (3 aircraft), **Dementyev Park at Staroye Drozhzhanoye** (4),
  **Gorodets Salyut rest home** (4) — small town park displays in Tatarstan and Nizhny Novgorod
  Oblast, below the "major museum" threshold this pass was told to apply. Their contents are in the
  russianplanes register under museum ids 324, 323 and 314 if a later pass wants them.

### Airframes excluded from included sites
* **Marked `ex` (no longer present)**: Ulyanovsk Tu-134A CCCP-65648 and An-10 CCCP-11154; Saratov
  An-2T bort 02; Togliatti MiG-27D and Che-20; Samara University An-2TP CCCP-41361, An-2T CCCP-28853,
  An-24T CCCP-29101, An-10 CCCP-L5723, MiG-23 bort 165, MiG-23M bort 47, MiG-23 bort 141,
  Mi-8T CCCP-25696; Savasleyka thirteen airframes (L-39C 82, MiG-15UTI 02, MiG-31 32, MiG-21UM 04,
  MiG-21 09, MiG-17 01, MiG-23UB 70, MiG-23M 15, MiG-23M 05, Su-15UM 30, Su-15 71, Su-9 07,
  MiG-19PML 04, MiG-19S 03); Syzran Ka-27, Mi-8 and Mi-24; Vyborg Mi-2 CCCP-15782; Perm items.
* **Marked `parts` (fragment only)**: Ulyanovsk SB (ANT-40) remains and Yak-18T CCCP-44287;
  Saratov Yak-52 bort 40; Engels Tu-22 KTS simulator.
* **Engels Lyotny Gorodok**: a **Tu-16 missile carrier bort 11 red c/n 5202605** and a
  **Tu-22KD bort 74 red** (repainted from bort 80) stand in the residential quarter about 2 km from
  the museum, described in erofey_manager part 7 as an "additional" location. russianplanes does not
  file them under the museum. They are gate-guard-class monuments and were left for the later pass.
  The Mi-2 bort 80 and Mi-8MT bort 70 in the same quarter **are** filed under the museum by
  russianplanes and were recorded, with their offset position stated in the description.
* **Pulkovo, St Petersburg**: **Il-86 RA-86106** stands preserved near the 15-ya liniya in the
  Aviagorodok. Not attached to any museum; monument, later pass.
* **Lebyazhye, Leningrad Oblast**: an **Il-2** monument to the defenders of the Leningrad sky, moved
  there from the Leningrad military aviation technical school. Monument, later pass — and the reason
  it is worth flagging is that the seed list's "Naval Aviation collection" in the St Petersburg area
  most likely refers to this Baltic Fleet aviation site rather than to anything in the city.
* **Vsevolozhsk, Leningrad Oblast**: a full-scale **Pe-2** mock-up built around recovered parts at the
  Dom Aviatorov on the Road of Life, and an **Il-4 bort 47**. Memorial complex, later pass.
* **Kaliningrad-Chkalovsk**: **Su-27UB bort 689 red c/n 96310405011**, put up at the airfield
  checkpoint on 15 October 2020 for the 689th Guards Fighter Regiment's regimental day, plus a
  **Su-24 bort 72** and a **Mi-24**. Classic gate guards, later pass. Also excluded: an **Il-28** and
  a **MiG-15** inside the Baltic Fleet warrant officers' school at Pionersky, and an
  **Su-27 / Mi-8 / Su-24** group on a training area at Chernyakhovsk.
* **Khrabrovo airport, Kaliningrad**: the **Li-2 bort 05** that older lists place there is marked `ex`.
  Nothing else aviation-preserved is recorded at Khrabrovo.
* **Kurumoch airport, Samara**: **Tu-134AK RA-65554 c/n 66320** preserved on the airport road.
  Monument, not a museum, later pass.
* **Samara Il-2**: the famous **Il-2 c/n 1872932** on Moskovskoye shosse is a city monument recovered
  from a wartime crash site, not a museum holding. Later pass. Also excluded from the Samara Space
  Museum row: the NK-33 and NK-12 engines and the MiG-17 / Su-9 / MiG-23ML / MiG-21MF cluster on the
  Samara University campus at Moskovskoye shosse 34, which is a separate teaching site from the
  Smyshlyaevka park and is only partly documented.
* **Ryazan**: an **An-2 bort 01**, a **Mi-8MT bort 02** and an S-125 launcher that russianplanes files
  under the Long-Range Aviation Museum id sit about 5 km away at 54.613N 39.667E, nowhere near
  Dyagilevo. They were **not** recorded under the museum — see open questions.
* **Severomorsk**: three further airframes in the museum line are recorded by russianplanes with no
  type at all. Not recorded; three unknown airframes remain outstanding there.

---

## 6. Fields deliberately left blank

* `year_built` is blank on the great majority of rows. It was populated **only** where a source gave a
  construction, roll-out or delivery date in words — chiefly the Ulyanovsk provenance texts and the
  erofey_manager Engels captions. Construction numbers were never converted into years, even where the
  c/n visibly encodes one (Tu-154 `74A061`, `79A386`, `81A470`, `90A863`; Yak-38 `7977861706107`).
* `tail_number` is blank wherever russianplanes records no bort number or registration, or records one
  with a query mark. Specific cases: the Samara University **Li-2**, whose registration is recorded
  only as "CCCP-503??" with two unreadable digits; the Vyborg **Mi-8T** recorded as "СССР-22434?".
  Both have their situation stated in `description`. Colour qualifiers (`красный`, `синий`, `жёлтый`,
  `контурный`) were stripped from bort numbers into `description`, per the existing Monino convention.
* `model_name` is blank where the NATO reporting name merely echoes the designation or where no
  standard popular name exists (Yak-3, Yak-9, Yak-18T, Yak-52, I-16, I-153, La-5, Mi-18, Rotor R-33,
  Sh-2, AK-1, ANT-4, ANT-25, R-2, R-12, RT-2, Kh-55 is given as Kent, Kh-20 as Kangaroo).
* `aircraft_name` is blank except for the four named airframes: Engels Tu-22M3 **Pyotr Bochin**,
  Safonovo MiG-25RB **Vasily Kirilenko**, Borshchevo MiG-25RBT **Valentin Sugrin**, Samara **Soyuz**.
* `website` is blank for the military and plant sites, which publish nothing.
* `postal_code` is a best-effort district code for several sites and should be treated as soft.

---

## 7. Open questions, ranked

1. **Is the Engels museum in any sense still a museum?** Engels-2 has been hit by long-range drone
   attack repeatedly since December 2022, most seriously in early 2025, and the aircraft park sits
   inside the base perimeter close to the operational apron. No dated visitor report, photograph or
   official statement later than about 2019 was found for the collection itself. The 30 airframes are
   recorded on 2014-2019 evidence. Someone should establish whether any of them have been damaged or
   removed before this data is treated as current.
2. **Su-15TM bort 02 c/n 1015332 — Severomorsk or Safonovo?** russianplanes assigns it to the
   Severomorsk Air Defence Corps museum but plots its coordinates (69.0621N 33.2896E) squarely inside
   the Safonovo naval aviation park, 6 km away. It is recorded at Severomorsk with the discrepancy
   stated. One of the two entries is wrong and a photograph would settle it.
3. **The 22 airframes at Samara-Smyshlyaevka, including Tu-144S CCCP-77108.** Everything there is
   flagged `stored`, several neighbours are already flagged `ex`, and no dated evidence after about
   2019 was found. Given the Perm precedent, a university teaching park with a Tu-144 in it is exactly
   the kind of collection that quietly disperses. Worth a targeted check.
4. **What happened to the Perm Aviation Museum's 27 airframes?** The closure report says the collection
   went to "private collections" without naming any. Several were already fragments
   (Tu-16K, Tu-16R, Il-76K CCCP-86638, Il-14P CCCP-13353, Mi-6, Su-24M, MiG-23ML, MiG-23 bort 167),
   but the MiG-29 bort 04, Su-27 bort 26, MiG-25PU bort 17, Mi-24A bort 41, Yak-40 RA-87418,
   Tu-134 RA-65064, An-24B RA-47756, An-2s and Mi-2s were whole aircraft. They are somewhere.
5. **Ryazan's An-2 bort 01 and Mi-8MT bort 02 at 54.613N 39.667E.** russianplanes files them under the
   Long-Range Aviation Museum but they are 5 km from Dyagilevo, in the city. The seed list asks about
   the Ryazan **VDV (Airborne Forces) museum**, which is in that part of the city; the most likely
   explanation is that these two belong to the airborne museum or the Ryazan airborne school, not to
   the long-range aviation museum. If confirmed, the VDV museum is a missing site.
6. **Does the Kronstadt destroyer Bespokoyny still carry the Ka-27 on its deck?** The helicopter is
   recorded there by russianplanes and the ship is a Patriot Park branch exhibit, but the ship's own
   descriptions mention the Ka-27 only as wartime capability. Also unresolved: whether the
   Su-27P bort 20 and Su-24 bort 08 on Sovetskaya ulitsa, recorded in 2019 as belonging to a
   "future" park, have since been formally incorporated, moved, or left standing where they are.
   Whether Kronstadt should be one site or the three it is currently spread across (Naval Glory
   museum, Bespokoyny, Sovetskaya ulitsa) is a curatorial call worth revisiting.
7. **Ulyanovsk Tu-104A CCCP-42322's construction number.** russianplanes gives 6350103, which does not
   look like a Tu-104 number — it reads like a Tu-134 c/n. Recorded as sourced, with the anomaly noted
   in the row's description, but it may be a data error in the registry.
8. **Engels An-12 identity.** An-12A c/n 2400401 versus An-12BP c/n 402512, 1962. Both cannot be right.
9. **Gatchina's Farman.** Which Farman is it a reproduction of? Recorded as bare `Farman` rather than
   guessing at Farman IV.
10. **Three unidentified airframes at Severomorsk** and the un-typed entries in the Voronezh and
    Kaliningrad sweeps. Small, but they are holes in otherwise complete site lists.
11. **The Nizhny Novgorod Victory Park Akvaglayd.** A wing-in-ground-effect craft named
    "Viktor Razzhivin". Whether it belongs in an aircraft database at all is a schema question, not a
    research one, but it should be decided rather than silently dropped a second time.
