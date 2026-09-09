# Siberia, the Russian Far East and the Arctic — research notes

Scope: everything east of the Urals — Tyumen Oblast, KhMAO-Yugra, YaNAO, Omsk, Tomsk,
Novosibirsk, Altai Krai, Altai Republic, Kemerovo, Krasnoyarsk Krai, Khakassia, Tyva,
Irkutsk, Buryatia, Zabaykalsky Krai, Sakha (Yakutia), Amur Oblast, the Jewish AO,
Khabarovsk Krai, Primorsky Krai, Sakhalin, Magadan, Kamchatka and Chukotka.
All sites are filed `region = Asia`.

**Deliberately out of scope, left to the Urals pass:** Kurgan Aviation Museum
(Kurgan Oblast) and the UMMC museum complex at Verkhnyaya Pyshma / Yekaterinburg
(Sverdlovsk Oblast). Both sit in the Urals Federal District and both hold aircraft;
they are named here so they are not silently lost between passes.

Result: **28 sites, 186 aircraft.**

---

## 1. Sources used, and how each behaved

### russianplanes.net — primary registry, and it worked
The site is fully reachable. The useful entry points are not the ones the museum pages
render: the museum index is `https://russianplanes.net/museums` (365 sites worldwide,
~110 in Russia) and the per-airframe data is served as JSON by

```
https://russianplanes.net/?action=mapGetPoints&region=<oblast>&smuseum=<id>&mode=json&lat1=..&lon1=..&lat2=..&lon2=..
```

Each record carries type, modification, bort number or registration, construction
number, coordinates to five decimals, a free-text note, and a status flag
(`monument` = displayed, `stored` = held/instructional, `ex` = moved or destroyed,
`parts` = fragment). Individual `/monument/<id>` cards add the geocoded street and
the museum access line ("свободный доступ" / "доступ по договорённости").

I pulled every record in the 24 regions listed above: **755 airframes**, then clustered
them at 1 km to find collections that russianplanes has **not** flagged as museums.
That is how the Far Eastern Aerospace Museum at Ivanovka, the Gallery of Time park in
Novosibirsk, the Patriot park at the Novosibirsk Technical College, the Yakutsk museum
group and the Kamchatka museum were found — none of them carry a museum id in the
registry.

Currency evidence: the registry is actively edited. The Chita MiG-29UB card records a
removal in **August 2025**; the Mochishche Su-24M card was **added 6 August 2026**.
So the snapshot I worked from is current to mid-2026 for the airframes that people
photograph. It is *not* evidence that a museum is open — see §3.

### ru.wikipedia.org
Fetched through the MediaWiki API (`WebFetch` refuses the domain as cache-only; plain
`curl` to `/w/api.php` works, but rate-limits under load — retry with backoff).
Coverage of Siberian and Far Eastern aviation museums is close to nil. There is **no**
article for a Novosibirsk aviation museum, none for Arsenyev, Khabarovsk, Salekhard,
Ivanovka or the Kamchatka museum. The one genuinely useful article was
*Памятник самолёту Бэлл П-39 «Аэрокобра»*, which dates and explains the Yakutsk
ALSIB monument. A search for Siberian aviation museums returns the Kurgan museum and
then unrelated pages — the Russian Wikipedia simply does not cover this region's
aviation collections.

### Museum sites
- `dvmuseum.ru` (Far Eastern Aviation Museum, Arsenyev) — resolves but returns an empty
  body to a text fetch; the site is a JS app. Details came from the Primorsky Krai
  tourist portal instead.
- `memorial24.ru` (Krasnoyarsk Memorial Pobedy) — reachable, but the pages carry no
  catalogue of the open-air equipment and no mention of ALSIB or an Airacobra.
- `aeromochische.ru` — reachable and useful.
- No other site in the region has a usable public collection list.

### Dated secondary reporting used for currency
- `visit-primorye.ru` — Far Eastern Aviation Museum: ulitsa Novikova 34, opened
  **10 September 2021**, Tue–Sun 09:00–17:00, "12 aviation exhibits".
- `chita.ru`, 4 September 2024 — the Chita Tu-154 cabin museum burned on
  **25 December 2023** and restoration began May 2024.
- `ngs.ru`, 4 December 2021 — Yak-40 delivered to the Novosibirsk Gallery of Time,
  aircraft bought from Sukhoi, aviation pavilion planned.
- `amurvisit.ru` — Far Eastern Aerospace Museum at Ivanovka, Ivanovsky District,
  ~40 km from Blagoveshchensk.
- `mag.russpass.ru` — Museum of the USSR / Gallery of Time, 1-e Mochishchenskoye
  shosse 1/5, daily 11:00–19:00.
- `v-pohode.ru` — Tanay collection, coordinates 54.7536/85.1134, visible from and
  reachable off the Novosibirsk–Leninsk-Kuznetsky road.

### Not used
Grokipedia (barred). aviationmuseum.eu and English survivor lists were not used at all —
for this region they add nothing russianplanes does not have, and everything they do
carry is a decade stale.

---

## 2. The seed leads, checked one by one

**Novosibirsk Museum of Aviation History, Berdsk — not found; probably does not exist
as described.** I searched russianplanes for every airframe in Novosibirsk Oblast (79
records) and found exactly two things at Berdsk: **Tu-104A CCCP-42382** (c/n 8350602)
and **An-2 RF-00348**, both at Berdsk-Tsentralny airfield (54.7393, 83.0980), both
flagged `stored`, neither attached to any museum id. No news coverage of a Berdsk
aviation museum, a land dispute or a move surfaced in Russian-language search.
What *does* exist around Novosibirsk, and is probably what the lead was reaching for:
- **Gallery of Time / Museum of the USSR**, 1-e Mochishchenskoye shosse 1/5 — a private
  retro-technology park that built an aviation pavilion from 2021 (recorded).
- **Mochishche aerodrome museum**, ulitsa Aviatorov 2 — founded 2008 (recorded).
- **Patriot park at the Novosibirsk Technical College named after Pokryshkin** —
  four full-scale WWII reproductions (recorded).
- **Museum of Aviation named after A. I. Pokryshkin** (city-centre, indoor) — holds no
  airframes; not recorded.
The Berdsk Tu-104A is a significant survivor and should be chased in a later pass, but
I will not invent a museum around it.

**Krasnoyarsk.** The *Memorial Pobedy* museum (Dudinskaya 2A) is open and does run an
open-air equipment park, but russianplanes records only **one** aircraft anywhere near
it — a MiG-17 "01" on Ploshchad Pobedy (56.0234, 92.8861), and that record is flagged
`ex` (moved). A second MiG-17 "01 красный" stands 1.7 km away at 56.0391, 92.9081 with
no museum attachment. I could not establish from any source which of these is the
current Memorial Pobedy exhibit, so **no Krasnoyarsk city site was recorded** rather
than guess. The **Yemelyanovo** group (56.1823, 92.4626 — Il-76 EK-76463, Il-62
RA-86453, Tu-154 RA-85165, An-26, two Yak-40s, L-410, An-2, Mi-8, Mi-2) is a rescue-
service **training ground**, every record `stored` or `ex`; not a museum, not recorded.
The **ALSIB memorial in Krasnoyarsk is sculptural** — the RGO competition selected a
monument design, not an aircraft; there is no P-39 airframe or replica there. The one
Krasnoyarsk Krai site I did record is **Zelenogorsk** (Armed Forces museum, 5 aircraft,
free access). Also noted and not recorded: **Li-2 CCCP-04220 at Turukhansk** (67.4574,
86.5416) and **Li-2T CCCP-04219 at Dikson** (73.5168, 80.3897) — the latter described
on russianplanes as the northernmost aviation monument in the world, raised August 1976.
Both are lone plinths, both are ALSIB-era Li-2s, and both deserve the monument pass.

**Irkutsk.** Recorded: **Irkutsk Aviation Plant museum** (9 airframes, by appointment) —
strong collection including a full-scale ANT-31 (I-14) mock-up, Yak-28L, Yak-28PP,
Il-28, MiG-27K and an Irkutsk-built Su-30. The much larger Irkutsk cluster (43 records
at 52.2693, 104.3556) is the **former IVATU/IVVAIU military aviation school**, disbanded
2010 — almost every record there is `ex` or `stored`, aircraft dispersed to schools and
to Belaya airfield. Not a museum in 2026; not recorded. **Nizhneudinsk** (L-410
RA-67079, Mi-4 CCCP-14247, Mi-2) is a three-aircraft town park; treated as monuments,
not recorded. No ALSIB monument in Irkutsk Oblast carries an airframe.

**Ulan-Ude.** There is **no publicly accessible U-UAZ helicopter museum.** What exists
around the plant (51.85, 107.72–107.73) is a scatter of individual items: an I-16
monument to wartime aircraft workers, a MiG-15UTI on the plant airfield, a Ka-25PL
(ex RA-22452) in store, and the **NVA-10 ekranoplan** hull. Ulan-Ude's other clusters
are paratroop and firefighting training airframes at 51.857, 107.874. The plant runs an
internal history museum, but nothing in Russian-language search shows public admission
or an outdoor airframe collection. Nothing recorded; flagged as an open question.

**Yakutsk / Magadan / Kolyma.** Recorded the **Museum of Aviation of the Republic of
Sakha** (ulitsa Gagarina 8) with its four outdoor airframes on Bykovskogo, Gagarina,
Zhukovskogo and Pilotov, plus the **full-scale P-39 Airacobra replica** unveiled
6 November 2002 opposite school No. 24 — the central Russian ALSIB memorial, built by
Yakutsk airport engineers, with the names of the ferry pilots lost on the route cut
around the plinth. It is a replica and is described as such. Recorded **Magadan** as
the *Podvig* club display (Su-15, MiG-21SM away under restoration, Mi-2). Noted, not
recorded: **Il-18D CCCP-74255 cockpit** built into a children's centre at Susuman on
the Kolyma road, **Li-2 fragments at 60.4216, 155.1537** from a forced landing, the
**Il-14 group at Chersky** (68.74–68.75, 161.32–161.35 — including a Li-2 CCCP-04218
and an Il-14 described as Khrushchev's aircraft), and a **wooden propeller over an
unknown airman's grave at 70.6157, 147.8974**. The Chersky and Kolyma airframes are
lend-lease-era survivors sitting in the open and are the highest-value monument-pass
targets in the whole region.

**Khabarovsk.** Recorded the **Museum of Aviation and Air Defence** (48.4696, 135.1374,
by arrangement) — Tu-22M3, Su-22UM3K, An-12BK, An-24KPA, Su-27, MiG-23M, Mi-24V. Two
of these are documented relocations (the Su-27 from Komsomolsk-Dzyomgi, the MiG-23M
from Tsentralnaya Uglovaya), and russianplanes carries the source records as vacated,
so there is no double-count. The **Museum of the History of the Far Eastern Military
District** (Shevchenko 20) is a separate indoor museum with no airframes; not recorded.

**Vladivostok.** Recorded the **Pacific Fleet Naval Aviation Museum** at Knevichi
(43.3810, 132.1700, by arrangement): Mi-8T, Mi-2, Mi-1, Mi-4, Su-27 and a full-scale
**BI rocket-fighter replica** marked "2". The **Pacific Fleet Military History Museum**
(Svetlanskaya 66), the **S-56 submarine** and the **Voroshilov battery** hold no
aircraft — the Vladivostok Fortress museum group at 43.1223, 131.8778 is naval missiles
(P-35, P-70 Ametist, S-125/Volna, M-11 Shtorm, URK-5 Rastrub) and an AT-1 aerial
torpedo, plus a Mi-8T cabin fragment. None of that is an aircraft; none recorded.
Also noted and not recorded: MiG-15UTI "01" (c/n 812923) and Mi-2 RA-23310 in
Vladivostok's Fantaziya park, and a Ka-25PL by the Pacific Fleet air force HQ.

**Komsomolsk-on-Amur.** Recorded the **KnAAZ memorial aircraft** as one restricted
site — the plant's own line of memorials (Li-2 CCCP-L3417, Su-17, Il-4, Tupolev R-6,
MiG-17, two Su-27s, Su-33, Su-30MKK) plus a fire-service An-12B. Access is inside the
plant perimeter, hence `restricted`. The Su-15 "60" that russianplanes carried here was
moved in 2021 and is excluded.

**Sakhalin.** **No aviation museum found.** Everything on Sakhalin and the Kurils is a
plinth or an airfield dump: a Su-15 "40" in the square by the officers' club in
Yuzhno-Sakhalinsk, MiG-17s at Yuzhno-Sakhalinsk and Smirnykh, An-24 RA-47198 at the
airport, a stored Tu-134A RA-65981, and the **Iturup/Burevestnik group** (44.92,
147.62) — MiG-15s, MiG-17s, an An-26 and a possible Mi-14, most flagged with question
marks and rumoured written off by the 1979 typhoon. The Sakhalin Regional Museum holds
no airframes. Nothing recorded.

**Kamchatka.** Recorded the **Kamchatka Civil Aviation Museum** at Yelizovo — one
airframe, **Li-2 CCCP-84699 (c/n 23443408) mounted on the museum roof** beside the
A-401 road. The **Be-12 "15" (c/n 1602301) and Ka-25 "23"** at 53.157, 158.44 are on
Yelizovo naval aviation garrison ground, not museum property; not recorded. A MiG-15
with a KS-1 missile stands inside a closed military compound at 53.1767, 158.3875.

**Chukotka / Anadyr.** **Nothing museum-grade.** Seven records in the whole okrug: a
MiG-19S "01" monument at Anadyr (64.7448, 177.6886), a stored An-2, and the
**Chersky-adjacent Cape Schmidt / Mys Shmidta dump** at 69.79–69.80, 170.60–170.67 —
Mi-6A CCCP-21144, Mi-8T, and three Il-14s (CCCP-41870 plus two part-registrations
CCCP-6178* and CCCP-6170*) rotting on the tundra. Not recorded; flagged.

**Tyumen, Omsk, Tomsk, Barnaul, Kemerovo, Chita, Blagoveshchensk.**
- Tyumen: **no museum recorded.** The Tu-134A RA-65012 and Yak-40 RA-87449 at Roshchino
  are airport plinths; a three-item group at 56.9435, 65.2460 (Yak-40K RA-87222,
  Mi-8T RA-25902, Yak-52 RF-00196, all added to the registry in October 2023) is tagged
  "another aviation museum" but has no name, no address and no geocode, and I could not
  identify it. Ranked as an open question below.
- Omsk: recorded the **Omsk Flight Technical College of Civil Aviation** park (13
  airframes). Every record is `stored`: these are instructional airframes on a college
  training ground, and every row says so and is filed `in_storage`.
- Tomsk: recorded the **Bogashevo airport museum** (5 airframes, free access, though
  russianplanes notes the Tu-154M RA-85685 stands airside and needs booking).
- Barnaul: recorded the **aviation sports club museum** (12 airframes) — the largest
  military collection in Altai Krai.
- Kemerovo: the registry's "Kemerovo" museum is in fact the **Kuzbass museum-polygon at
  Tanay aerodrome**, Zhuravlyovo, Promyshlennovsky District — 115 km from Kemerovo.
  Recorded under its real location. The VL22M glider record at 55.3512, 86.1051 is a
  separate monument in Kemerovo city and is excluded from the Tanay file.
- Chita: recorded the **Raduga Aviation Museum** at the private Raduga zoo,
  Romanovsky trakt 46. Status is honest in the data: Tu-154B-2 RA-85280 is
  `under_restoration` after the December 2023 fire.
- Blagoveshchensk: the aircraft are not in the city but at the **Far Eastern Aerospace
  Museum, Ivanovka**, ~40 km away, recorded as its own site with 14 airframes.

**Polar and lend-lease airframes, chased individually.** No original American lend-lease
airframe survives on display anywhere in this region. What exists is: the Yakutsk P-39
**replica** (recorded); Soviet-built **Li-2s** — Salekhard CCCP-73956, Yelizovo
CCCP-84699, Novosibirsk "39 yellow", Komsomolsk CCCP-L3417 (all recorded), plus
Turukhansk CCCP-04220, Dikson CCCP-04219, Chersky CCCP-04218 and a Li-2 "01" at Kluchi,
Kamchatka (not recorded, monuments); and the **Il-14 group at Chersky and Mys Shmidta**.
The A-20 Havoc and Douglas types the lead expects are not present in any collection I
could verify — the airframes recovered from the route in the 2000s went to Moscow-area
and Novosibirsk restoration shops, not to eastern museums.

---

## 3. Currency — what the evidence actually is

The registry snapshot is mid-2026 for airframes. Museum *opening status* is weaker, and
I say so per site rather than pretending otherwise:

| Site | Best currency evidence |
|---|---|
| Far Eastern Aviation Museum, Arsenyev | opening 10 Sep 2021, hours Tue–Sun 09:00–17:00 from the krai tourist portal; airframes re-catalogued in the registry after the move from the Progress plant |
| Far Eastern Aerospace Museum, Ivanovka | six airframes added to the registry in the 24xxx id range (2025–26 additions) |
| Chita Raduga | dated news 4 Sep 2024 (fire, restoration); MiG-29UB removal recorded Aug 2025 |
| Gallery of Time, Novosibirsk | Tu-124V and Tu-134A cards added June 2023; hours from a 2024-25 travel article |
| Mochishche | Su-24M card added 6 Aug 2026 |
| Tanay | roadside collection described with coordinates in a dated visitor account |
| Salekhard, Berezovo, Nizhnevartovsk, Kogalym | free-access flag in the registry; no dated 2025-26 report found |
| Khabarovsk, Vladivostok, Fokino, Irkutsk IAZ, NAPO, Air Army HQ, KnAAZ | "by arrangement" / plant-perimeter; no dated 2025-26 visitor report found |

Sanctions and the war have made western trip reports (scramble.nl, checksix) effectively
stop after 2021, so for military sites the registry flag is the newest evidence there is.

---

## 4. Corrections made against the sources

1. **Four airframes double-counted between the two Arsenyev sites.** russianplanes lists
   Il-14T CCCP-61784, Yak-40K RA-88172, Tu-134 CCCP-65923 and An-8 RA-69302 under both
   the Progress plant museum (id 318, flagged `ex`) and the Far Eastern Aviation Museum
   (id 400, flagged `monument`). They are one set of aircraft that moved. All four are
   recorded **only** under the Far Eastern Aviation Museum.
2. **Su-27 "23" counted twice.** Listed at both Komsomolsk-on-Amur and the Khabarovsk
   museum. The Komsomolsk record is the vacated one; recorded at Khabarovsk only.
3. **MiG-23M "22" counted twice.** Same pattern, moved from Tsentralnaya Uglovaya;
   recorded at Khabarovsk only.
4. **Magadan Su-15 "91" recorded twice** by russianplanes (monument ids 608 and 4633,
   four metres apart, same bort). Recorded once; the duplication is noted in the row.
5. **Kemerovo museum is not in Kemerovo.** Filed at Zhuravlyovo, Promyshlennovsky
   District, Kemerovo Oblast (54.7537, 85.1136), which is where the airframes are.
6. **Chita museum aircraft count corrected.** The registry lists four; the MiG-29UB "98"
   was dismantled in August 2025 and its location is unknown. Three recorded.
7. **Su-24 "09" at NAPO** is flagged as moved to the NSTU campus; excluded from the
   Chkalov plant file.
8. **MiG-17 "01" (monument id 3867)** is tagged to the Air Army HQ museum but sits at
   55.0662, 82.9954 — 4.5 km away, in the Chkalov plant memorial area. Excluded from
   both files as unresolvable rather than assigned to the wrong site.
9. **Su-15 "60" at Komsomolsk** was moved in 2021; excluded.
10. **Mi-2 RA-23294 at Kogalym** is recorded as removed; excluded, leaving two aircraft.
11. **Yak-52 at Tanay** (monument id 6871) is flagged "former monument / moved /
    erroneous entry"; excluded. A second Yak-52 "50" at the same site is retained.
12. **Yak-40 RA-88244 at Berezovo** appears twice — once as a rescue-training airframe
    (vacated) and once as the current monument. Recorded once.

---

## 5. Judgment calls

**Replicas and mock-ups.** Nine rows are reproductions and every one says so in
`description`, never in `aliases`: the Yakutsk P-39 Airacobra; the BI rocket fighter at
Knevichi; the ANT-31 (I-14) mock-up at the Irkutsk plant; the Yak-9, Il-10, MiG-3 and
I-16 in the Novosibirsk college Patriot park; the I-16 on the pylon at Tanay; and the
Yak-3 on the Nizhnevartovsk alley. Four more — the Il-4 and Tupolev R-6 at KnAAZ, the
UT-2 at Arsenyev and the Yak-9 at the Chkalov plant — are wartime types displayed by the
factories that built them, and I could not establish from any source whether they are
original airframes or plant-built reproductions. Those rows say exactly that rather than
asserting either.

**Access types.**
- `public` where russianplanes records "свободный доступ" and nothing contradicts it:
  Arsenyev DVMA, Ivanovka, Tanay, Tomsk, Zelenogorsk, Chita, Magadan, Salekhard,
  Berezovo, Kogalym, Nizhnevartovsk, Gallery of Time, the college Patriot park,
  Primorskoye Koltso, Yakutsk, Yelizovo.
- `appointment` where it records "доступ по договорённости": the Progress plant museum,
  Khabarovsk, Pacific Fleet Knevichi, Fokino, Irkutsk IAZ, the Novosibirsk Air Army HQ
  museum, the Omsk college park, Mochishche.
- `restricted` for the two sites inside a working perimeter with no booking route for a
  member of the public: **KnAAZ Komsomolsk** (aircraft stand inside a defence plant) and
  **Ukrainka** (aircraft stand on an operational strategic bomber base). russianplanes
  calls both "by arrangement"; that arrangement is not available to the public, and the
  honest answer is `restricted`.

**Two sites are borderline and included deliberately.** The **Omsk college park** is a
training ground, not a curated display — included because it holds 13 complete airframes
including an Il-76 and three Tu-154s, every row flagged `in_storage`. **Primorskoye
Koltso** at Artyom is a motorsport complex, not a museum — included because its four
aircraft are permanently displayed and freely accessible, which is what the access field
is meant to describe.

**Not aircraft, so excluded.** The Ka-30 aerosledge at the Progress museum (a Kamov
product but a snow vehicle); the FAB-1000 bomb at Zelenogorsk; the Topol missile-complex
cupola in the Novosibirsk college park; the VL22M glider monument in Kemerovo city;
Vladivostok Fortress's naval missiles and AT-1 torpedo. The two P-15 Termit and one
P-270 Moskit missiles **are** recorded at the Progress plant museum, because they are
that plant's own products and are displayed as part of its collection.

**Sites excluded as garrison gate guards, town plinths or dumps**, per the spec's
instruction not to chase them in this pass: Chernigovka (4 helicopters on an army
aviation base), the IVATU school remains at Irkutsk, Yemelyanovo rescue-training ground,
the Krasnoyarsk-region ФСИН training area, the Lebyazhye firing range near Surgut,
Iturup/Burevestnik, the Mys Shmidta and Chersky Il-14 groups, Nizhneudinsk park,
Anadyr, Ulan-Ude, the whole of Sakhalin, Khakassia and Tyva (Tyva has zero records).

---

## 6. Fields deliberately left blank

- **`year_built` is blank on all 186 rows.** No construction, roll-out, first-flight or
  delivery date is sourced for any of these airframes. russianplanes supplies
  construction numbers, and a c/n is not a year. The single tempting case — the Barnaul
  An-2 RF-00371, whose registry note reads "1960 г постройки!" — is an unattributed
  exclamation on a user-edited card, so it stays blank and unmentioned.
- **`aircraft_name` is blank throughout.** No airframe in this region carries an
  individual name in any source I saw.
- **`postal_code`** is filled where the settlement has a single unambiguous index and
  left blank nowhere; but for Ivanovka, Zhuravlyovo, Mochishche and Seryshevo the index
  is the settlement's, not the site's.
- **`address`** is blank for 13 sites. Where russianplanes gives only reverse-geocoded
  road names ("Novosibirsk — Sokur", "A-401"), that is not an address and I did not
  invent one; the coordinates carry the location instead.
- **`website`** is filled for two sites only (dvmuseum.ru, aeromochische.ru). No other
  site in the region has one I could confirm resolves.
- **`tail_number`** is blank on 13 rows where no bort number or registration is legible
  in any photograph — most of the Progress plant helicopters, the Pacific Fleet Mi-4,
  the MiG-27K at Irkutsk, the Kogalym and Nizhnevartovsk reproductions.
- **`variant`** is blank where the registry records only a base type (Su-27, MiG-21 at
  Fokino and Zelenogorsk, Mi-24 at Tanay). Guessing a sub-variant from a silhouette is
  exactly the kind of invention the spec forbids.
- **Construction numbers** go in `aliases` as `c/n <number>`, never in `tail_number` or
  `year_built`. Where russianplanes itself hedges the c/n (the Mi-34S1 at Arsenyev,
  "978303хх03003 ?"; the Yak-112 at Irkutsk, "01-002 ?"; the placeholder strings
  beginning "НеизвЗав") the c/n is omitted from aliases and the doubt is described.

---

## 7. Open questions, ranked

1. **The unidentified Tyumen group at 56.9435, 65.2460** — Yak-40K RA-87222, Mi-8T
   RA-25902 and Yak-52 RF-00196, all added to russianplanes in October 2023, tagged
   "another aviation museum", with no name, no address and an empty geocode. Three
   complete airframes at one spot in a region that otherwise has none is a museum
   nobody has written down. Highest-value unresolved lead in the region.
2. **Krasnoyarsk Memorial Pobedy's actual aircraft.** Two MiG-17s 1.7 km apart, one
   flagged as moved, no catalogue on the museum's own site. One of them is very probably
   a current museum exhibit and the site belongs in the database. Needs a dated
   photograph or a phone call.
3. **Tu-104A CCCP-42382 at Berdsk-Tsentralny** (c/n 8350602). One of a handful of
   surviving Tu-104s anywhere. Registry says `stored`, no owner, no museum. Who holds it
   and is it still there?
4. **Does the U-UAZ plant museum at Ulan-Ude admit visitors, and does it hold
   airframes?** The plant has built Mi-8/Mi-171 for sixty years; a helicopter collection
   would be regionally significant, and the absence of any evidence for one is more
   likely a gap in the sources than an absence in fact.
5. **Mochishche's real inventory.** The museum's own page claims Mi-1, Po-2 reproductions
   with original wartime engines, Yak-12, Mi-6, Il-14, Ka-26, Morava L200 and Mi-26.
   russianplanes records four airframes. Some of the museum's aircraft are airworthy and
   therefore not displays; the static remainder needs a site visit to separate.
6. **The Novosibirsk Tolmachevo group** at 55.007, 82.670 — Il-86 RA-86097, Tu-154M
   RA-85684 (erected 2018), Tu-134B-3 RA-65693, Tu-154M RA-85628 and a MiG-3
   reproduction. Four preserved airliners in one place, tagged "another aviation museum",
   no name. Airport monument alley or an actual collection?
7. **Il-14s at Chersky and Mys Shmidta.** Six Il-14 airframes plus Li-2 CCCP-04218 and
   Mi-6A CCCP-21144 sitting on Arctic tundra, one of them reported as Khrushchev's
   aircraft. Not museum pieces today, but they are the region's most significant
   at-risk airframes and someone should record their condition.
8. **Ivanovka's MiG-25 and Po-2.** The museum's own listing claims a MiG-25 and a flying
   Po-2 that russianplanes does not record. Either the listing is aspirational or the
   registry is behind.
9. **Whether the Il-4, R-6, UT-2 and Yak-9 factory memorials are original airframes.**
   Four wartime types on three factory sites; the answer changes what they are worth.
10. **Kamchatka's museum size.** One Li-2 on a roof is what the registry has; a civil
    aviation museum with a single exhibit is implausible, and its indoor holdings are
    unrecorded.

---

## 8. Russian names of the recorded sites

| English name used in the CSV | Russian name | Aircraft file |
|---|---|---|
| Far Eastern Aviation Museum | Дальневосточный музей авиации (Дальневосточный авиационный музейно-выставочный центр, ДАМВЦ) | `far_eastern_aviation_museum_aircraft.csv` |
| Progress Aircraft Plant Museum | Музей ААК «Прогресс» им. Н. И. Сазыкина (Музей ААПО) | `progress_plant_museum_arsenyev_aircraft.csv` |
| Far Eastern Aerospace Museum | Дальневосточный аэрокосмический музей | `far_eastern_aerospace_museum_aircraft.csv` |
| Museum of Aviation and Air Defence | Хабаровск — Музей авиации и средств ПВО | `khabarovsk_aviation_air_defence_museum_aircraft.csv` |
| Pacific Fleet Naval Aviation Museum | Музей авиации Тихоокеанского флота | `pacific_fleet_naval_aviation_museum_aircraft.csv` |
| Fokino Naval Aviation Museum | Музей морской авиации (Фокино) | `fokino_naval_aviation_museum_aircraft.csv` |
| Irkutsk Aviation Plant Museum | Музей Иркутского авиационного завода (ИАЗ / ИАПО) | `irkutsk_aviation_plant_museum_aircraft.csv` |
| Komsomolsk-on-Amur Aircraft Plant Memorial Aircraft | Памятные самолёты на территории КнААЗ им. Ю. А. Гагарина | `knaaz_komsomolsk_aircraft.csv` |
| Chkalov Aircraft Plant Memorial Aircraft | Памятники Новосибирского авиационного завода им. В. П. Чкалова (НАПО) | `novosibirsk_chkalov_plant_memorial_aircraft.csv` |
| Museum of the Air Force and Air Defence Army Headquarters | Музей при штабе Армии ВВС и ПВО (Новосибирск) | `novosibirsk_air_army_museum_aircraft.csv` |
| Gallery of Time Museum Park | Музейный парк «Галерея времени» / Музей эпохи СССР | `gallery_of_time_novosibirsk_aircraft.csv` |
| Patriot Park, Novosibirsk Technical College | Музей авиации в парке «Патриот» при Новосибирском техническом колледже им. А. И. Покрышкина | `novosibirsk_technical_college_patriot_park_aircraft.csv` |
| Mochishche Aerodrome Aviation Museum | Музей раритетной и действующей авиатехники под открытым небом, аэродром Мочище | `mochishche_aerodrome_museum_aircraft.csv` |
| Barnaul Aviation Sports Club Museum | Музей Барнаульского авиаспортклуба | `barnaul_aviation_sports_club_museum_aircraft.csv` |
| Kuzbass Museum-Polygon, Tanay Aerodrome | Кузбасский музей-полигон, аэродром «Танай» | `kuzbass_museum_polygon_tanay_aircraft.csv` |
| Tomsk Airport Aviation Museum | Музей аэропорта Томск (Богашёво) | `tomsk_airport_aviation_museum_aircraft.csv` |
| Omsk Flight Technical College of Civil Aviation Aircraft Park | Музей Омского лётно-технического колледжа гражданской авиации | `omsk_flight_technical_college_park_aircraft.csv` |
| Zelenogorsk Armed Forces Museum | Музей вооружённых сил, Зеленогорск | `zelenogorsk_armed_forces_museum_aircraft.csv` |
| Raduga Aviation Museum | Музей авиации и космонавтики Забайкальского края (зоопарк «Радуга») | `chita_raduga_aviation_museum_aircraft.csv` |
| Podvig Military-Patriotic Club Display | Военно-патриотический клуб «Подвиг», Магадан | `magadan_podvig_club_aircraft.csv` |
| Museum of Polar Aviation | Музей полярной авиации, Салехард | `salekhard_polar_aviation_museum_aircraft.csv` |
| Berezovo Aviation Museum | Музей авиации, Берёзово | `berezovo_aviation_museum_aircraft.csv` |
| Kogalym Military Equipment Park | Парк военной техники, Когалым | `kogalym_military_equipment_park_aircraft.csv` |
| Nizhnevartovsk Alley of Aviation Honour | Аллея почёта авиации, Нижневартовск | `nizhnevartovsk_aviation_alley_aircraft.csv` |
| Museum of Aviation of the Republic of Sakha | Музей авиации Республики Саха (Якутия) | `yakutsk_aviation_museum_aircraft.csv` |
| Kamchatka Civil Aviation Museum | Музей гражданской авиации Камчатки, Елизово | `kamchatka_civil_aviation_museum_aircraft.csv` |
| Ukrainka Garrison Aviation Museum | Музей в гарнизоне Украинка (Белогорск) | `ukrainka_garrison_museum_aircraft.csv` |
| Primorskoye Koltso Sport-Technical Park Aircraft Display | Спортивно-технический парк «Приморское кольцо», Артём | `primorskoye_koltso_artyom_aircraft.csv` |
