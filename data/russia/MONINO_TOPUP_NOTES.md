# Monino top-up — Central Air Force Museum

Russian name: **Центральный музей Военно-воздушных сил** (ЦМ ВВС), пгт Монино,
г.о. Щёлково, Московская область, ул. Музейная, д. 1. Branch of the Central Museum
of the Armed Forces (ЦМ ВС РФ). Site: https://cmvvs.ru/ (reachable, HTTP 200,
checked 2026-09-09).

Scope of this pass: **top-up only**. 132 airframes were already in the database; no
museums CSV was written. Output: `monino_topup_aircraft.csv`, **61 rows**, every row
`museum_name = Central Air Force Museum`.

## Sources used, and how each behaved

1. **russianplanes.net — primary and decisive.** The museum's collection is
   enumerated in its "авиапамятники" (aviation monuments) registry as museum id 3.
   The list is not rendered in the page HTML — it is loaded by script — but the same
   query has a KML export:
   `https://russianplanes.net/monuments/?...&smuseum=3&smonument=0&...&kmlExport=1`
   That returned **220 placemarks** with per-airframe coordinates, type, modification,
   bort number, construction number and a link to a monument card. All 220 monument
   cards were fetched individually for the `Текущий статус` field, which is what makes
   this source usable: it distinguishes
   - `памятник/музейный экспонат` — present as an exhibit,
   - `фрагмент воздушного судна/двигатель/винт/прочее` — a section, engine or propeller,
     not a complete airframe,
   - `бывший памятник/перемещён/ошибочная запись` — gone, moved, or an erroneous card.
   Several cards also carry dated provenance notes, which supplied most of the
   currency evidence below.
2. **ru.wikipedia.org, Центральный музей Военно-воздушных сил — stale in a specific
   way.** The prompt expected this article to carry a fuller exhibit table than the
   English one. **It does not.** The current article has no exhibit table at all: the
   "Экспонаты музея" section is five bullet points of categories, followed by photo
   galleries. Its only usable contributions were the headline count (194 aircraft as
   of 2020) and two gallery captions — Ка-26 and Ми-6Б — that flagged types missing
   from the 132-row extract. The English `List of aircraft at the Central Air Force
   Museum` is in fact the fuller list of the two, and it is what pointed at the
   L-29, A-20G, P-63, Li-2, Mi-1, Yak-11/12/18/50/52 and BI-1 before russianplanes
   confirmed them. It is nonetheless stale in places — see the Li-2 note below.
3. **cmvvs.ru (museum's own site) — reachable, thin, but authoritative where it
   speaks.** No inventory list. The hall pages do carry a definitive roll for the
   Great Patriotic War halls 6a/6b, which settled several questions (see below), and
   a news item confirming the Tu-134's restoration state.
4. **kpopov.ru survey of the Monino collection** — used for the Diskoplan-1/-2
   attribution to M. V. Sukhanov and their 1950/1962 dates, the SSSR-1 and Volga
   balloon gondolas, the BOR-5 airframe number 502 and its 17 April 1985 flight, and
   the Farman IV being a flying replica built in 1975 for the film *Воздухоплаватель*.
5. **aviation21.ru ("Авиация России"), 16 June 2025** — the Museum of Victory
   transfer, independent of russianplanes.
6. **russianrockets.net** — checked and **does not cover Monino**. Its museum index
   lists nine sites and Monino is not among them; the KML query for museum 3 returns
   an empty document. So there is no registry cross-check available for the missile
   and space exhibits; the BOR-5 rests on russianplanes plus kpopov.

## What the 61 new rows are

- **8 airframes transferred from the Museum of Victory (Поклонная гора) in June 2025**:
  MiG-17 "66", Aero CS-102 "06", MiG-21PFS "09", MiG-23ML "14", Su-15TM "11",
  Su-22UM3K "81", Ka-25PL "77", Ka-26 "36". Confirmed by both russianplanes monument
  cards and the 16 June 2025 aviation21.ru report, which describes the move as a
  *temporary* relocation of about a dozen airframes totalling near 100 tonnes. That
  wording is in each row's `description`; if the loan is reversed these eight go back.
  The press report names "MiG-21PF" where russianplanes says MiG-21PFS — noted in the row.
- **The western row of the open park** (roughly 38.178–38.180 E), added in the 2010s
  and absent from the old extract: three Yak-28PP jammers ("45", "53", "43"),
  Yak-28U "63", MiG-23ML "125", M-17 CCCP-17401, Mi-24P "37".
- **Recent single arrivals**: An-26KPA RA-46707 (moved in 27 Aug 2021), Sh-2 replica
  (in the museum since 2021), Tu-134AK RA-65982, An-12B RA-12126, MiG-21PFM "47".
- **The light-aircraft and helicopter rows**: three Ka-26, Ka-18, Ka-15, Mi-1, Mil V-7,
  Yak-30, two Yak-11, Yak-12R, four Yak-18 variants plus the Yak-18T prototype,
  Yak-50, Yak-52B, Su-26, L-200D, Molniya-1, L-29.
- **Lend-Lease**: A-20G "14" and P-63 Kingcobra, both named in the museum's own
  halls 6a/6b description.
- **Gliders and rotorless oddities**: Antonov A-11, A-13M, A-15; KAI-19; MAI-63;
  Sukhanov Diskoplan-1 and Diskoplan-2; Nevdachin Burevestnik S-4; the Rafaelyants
  Turbolyot.
- **Lighter-than-air**: the SSSR-1 (1933) and Volga (1962) stratospheric balloon
  gondolas — the classes the prompt expected and the only lighter-than-air records here.
- **Spacecraft**: BOR-5 airframe 502.

## Airframes I believe have LEFT Monino — flagged, not recorded

All are `бывший памятник/перемещён/ошибочная запись` on russianplanes.

| Type | Identity | Evidence |
|---|---|---|
| Lavochkin La-11 | c/n 51210468 | russianplanes registry card id227535: released for restoration to "Inter Avia" in 1992, passed to an English private museum in March 1993; only the engine came back to Monino in May 2001, "самолёт по сей день находится в Англии". This is a real loss, not a bookkeeping artefact. |
| Ilyushin Il-14M | CCCP-41860 | Burned in 1992; only wing consoles, a nose-gear fragment and the instrument panel survive. |
| Lisunov Li-2T | CCCP-63905 | Burned in 1992; only wing consoles and gear legs survive. |
| Lisunov Li-2 | c/n 18418809 | Arrived Jan 1959, struck off and scrapped in 1977. **The English Wikipedia list still carries this construction number as a present exhibit — that entry is stale by half a century.** |
| Yakovlev Yak-18A | RA-0394G | In storage at the museum only during 2020–2023. |
| Glider PI-6 «Иосиф Уншлихт» | — | Wooden glider of the late 1930s, badly damaged in a hangar roof collapse; photograph 2014, now off the exhibit list. |
| KS-1 Kometa cruise missile | bort 108 | Last photograph at Monino 20 October 2012; card now marked as a former monument. This is the only cruise missile russianplanes ever recorded at Monino. |
| Tupolev Tu-143 Reys ×2 | c/n 761431843211600 and bort "05" | Both cards marked former/erroneous, with no explanatory note. See open question 2. |

## Airframes present but recorded as sections, not complete aircraft — excluded

The prompt asked for complete airframes rather than sections; these all carry
russianplanes status `фрагмент воздушного судна/двигатель/винт/прочее`:

- **Petlyakov Pe-8** — a section only. The museum's own halls 6a/6b roll does not list
  a Pe-8 among its wartime aircraft.
- **Polikarpov I-153** — a section only, and likewise absent from the museum's own roll.
- **Tupolev TB-3 / ANT-6**, c/n 22687 — section; photographed at Monino 8 Dec 2021.
- **Ilyushin Il-10** — armoured hull only (the complete Il-10M is already recorded).
- **Ilyushin Il-86 RA-86095** — section (cabin).
- **Yakovlev Yak-42 "06160"** — cabin only, ex-MAI.
- **MiG-15UTI**, unknown c/n — section; this is probably what the existing database row
  `Mikoyan-Gurevich | MiG-15 | -` refers to.
- **FAB-9000 M-54 bomb**, a loose **M-22 engine**, and a **MiG-21 simulator** — not airframes.
- **Аэросани «Север-2»** — an aerosled, a ground vehicle, not an aircraft.

## Corrections and judgment calls

- **The Great Patriotic War hall does not hold what the prompt guessed.** The museum's
  own hall description names exactly 15 aircraft and 3 full-scale mock-ups: I-15, I-16,
  Yak-9U, La-7, MiG-3, SB, Tu-2, DB-3, Pe-2, Po-2, Su-2, Il-2, Il-10M, R-5, Li-2, plus
  A-20, P-63, B-25. There is **no LaGG-3, no Yak-1/3/7, no Pe-8 and no captured German
  type** at Monino. The only additions this pass could make from that hall are the
  Li-2, the A-20G and the P-63, all three of which are in the CSV.
- **No cruise-missile or target-drone row survives.** Tu-123 Yastreb and La-17 were
  searched for specifically and no evidence places either at Monino; russianplanes,
  which does carry Tu-141 and Tu-143 cards, has none at museum 3 that is current, and
  russianrockets.net does not cover the site. The KS-1 is gone (above). The already-
  recorded Tu-141 "05" therefore remains Monino's only drone record. **No
  `missile_rocket` rows were written.**
- **Su-15TM "11" collides with the existing `Su-15 | 11`.** They are two different
  airframes: the existing one is the prototype T-58D-2 (c/n 310002, russianplanes card
  174) and the new one is a series Su-15TM (c/n 1015329, card 24143) that arrived from
  Poklonnaya Gora in June 2025. Both genuinely wear bort 11. Per the spec I recorded
  what is there; this needs resolving at import, not by inventing a number.
- **The Aero CS-102** is filed as `Aero` / `MiG-15` / variant `UTI` rather than as its
  own model, to sit alongside the existing `MiG-15UTI | 03`. `CS-102` and `CS102` are
  in aliases.
- **Su-22UM3K** is filed under model `Su-22`, not `Su-17`, because that is the
  designation the airframe carries; `Su-17UM3`/`Su17UM3` are in aliases.
- **MiG-23 "233"** is the third MiG-23 prototype, c/n 23-11/3, filed as model `MiG-23`
  variant `23-11` to match the existing `MiG-23-23-11 | 231` (the first prototype).
  Note that the existing extract also holds a row `MiG-23BM | 01` alongside
  `MiG-27 | 01`; russianplanes has only one airframe at that spot (card 862, MiG-27
  bort 01, c/n 61912511018), so **the existing database may hold a duplicate there.**
  I did not touch it.
- **Replicas and mock-ups** are recorded and said so in `description`, never in aliases:
  UT-2 (replica), BI-1 (mock-up), Sh-2 (replica, in museum since 2021), Farman IV
  (flying replica built 1975 for a film). The already-recorded Su-2 and ANT-25 are
  likewise mock-ups per russianplanes, for whoever revisits those rows.
- **Diskoplan-1 and Diskoplan-2** are filed as two models rather than variants of one,
  because a shared blank tail number would have collided on the (model, tail_number) key.
  russianplanes carries a third disc-wing card, "Дисколёт", which I take to be a
  duplicate of one of these two and did not record.
- **MAI-63** has two russianplanes cards (7697 and 24360) for one airframe; recorded once.
- **Yak-18P** likewise has two cards for c/n 1160303, one of them flagged a fragment.
  Recorded once, with the doubt stated in `description`.
- **No third I-16, Po-2, MiG-29K or Yak-38 exists.** russianplanes has exactly two I-16
  (both mock-ups), two Po-2 airframes (Po-2 and Po-2LNB), five MiG-29 of all kinds
  (all five already in the extract) and two Yak-38. Worth noting the other way round:
  the existing extract lists **three** Polikarpov two-seaters — `Po-2`, `Po-2`, `U-2LNB`
  — where russianplanes has only two. That looks like an existing duplicate.
- **Fields deliberately left blank.** `year_built` is blank on 60 of 61 rows; the only
  populated one is the Farman IV replica (1975), which is sourced to a build date for
  that specific airframe. Construction numbers are in aliases as `c/n <number>` and
  never in `year_built` or `tail_number`. Bort numbers are the painted digits without
  the Russian colour suffix ("66", not "66-красный"). Tail number is blank where
  russianplanes records none — P-63, Ka-15, Yak-30, V-7, the gliders, the gondolas and
  the BOR-5. `manufacturer` is blank on exactly two rows, the SSSR-1 and Volga balloon
  gondolas, because no builder could be sourced and a guess is worse than a blank.

## Exhibits present but not recorded, for want of a sourced identity

These are on russianplanes as current Monino exhibits, but I could not source a
designer or manufacturer without inventing one, so they were left out rather than
filed with a fabricated attribution: the gliders **Аист-2** (CCCP-06), **ЛАК-9**
(CCCP-408), **Планер А-1-83** and **Планер Кашук**; the ultralights **ЭВС-017** ("017")
and **А-6 «Фрегат»** ("08", designer given only as V. K. Vyugov); the **Автожир
Рысюка** amateur autogyro; the hang-glider wings **«Славутич»** and **«Мираж-М»**
(two wings, not one airframe); and an unnamed **Tupolev glider mock-up**. Nine to ten
records are recoverable here by anyone with access to the museum's own catalogue.

## Coverage arithmetic

220 russianplanes placemarks − 9 departed − 10 sections/non-aircraft − 3 duplicate
cards − 132 already recorded − 10 unidentifiable (above) ≈ **56**; 61 were written
because five come from sources russianplanes files differently or splits (the
Diskoplan pair, the Yak-18 group, the two Li-2). Against the museum's own 2020 figure
of 194 aircraft, 132 + 61 = 193 is the right order of magnitude. Note that the VVA-14
and the Voisin LAS, both already in the database, do **not** appear in the
russianplanes monument export at all, so that export is complete but not exhaustive.

## Open questions, ranked

1. **Is the June 2025 Museum of Victory loan still at Monino, and will it stay?** The
   aviation21.ru report calls it a temporary relocation. Eight of the 61 rows depend on
   it. Re-check before the next survey; if the aircraft go back, they belong to the
   Museum of Victory record, not this one.
2. **Where did the two Tu-143 Reys go?** Both cards are marked former/erroneous with no
   note. They may never have been separate airframes — Monino's Tu-141/Tu-241 also
   wears bort "05", and one of the Tu-143 cards carries the same number, which smells
   like a mis-typed duplicate. Worth one on-site photograph to settle.
3. **The Li-2 construction numbers do not reconcile.** russianplanes gives the
   surviving hall aircraft c/n 1266008 (bort 39) and the open-park one c/n 23440808
   (CCCP-93914); the kpopov survey and English Wikipedia give 18418809 and 23440808.
   russianplanes says 18418809 was scrapped in 1977. One of the two Li-2 records here
   probably carries the wrong construction number.
4. **Does the existing database hold duplicate MiG-23BM/MiG-27 and Po-2 rows?** Both
   look like one airframe entered twice. Outside this pass's remit, but it would change
   the museum's headline count.
5. **The Tu-134AK's opening date.** It is recorded `under_restoration` on the strength
   of an August 2026 museum news item saying reassembly is finished but the aircraft is
   still being prepared for the exhibition. It may already be on display by the time
   this is imported.
6. **Sh-2 registration.** The replica wears a Soviet-style civil marking beginning
   `СССР-П` that russianplanes records only as that fragment. Left blank rather than
   guessed at.

## Excluded at import (9 Sep 2026)

- **SSSR-1 and Volga stratospheric balloon gondolas** — both are present at Monino and both were
  researched, but no builder could be sourced for either, and `manufacturer` is a required field
  the importer rejects when blank. Rather than invent a builder they were dropped from
  `monino_topup_aircraft.csv`. Re-add both the moment a sourced manufacturer turns up; the
  russianplanes monument cards are 7699 (SSSR-1) and 7714 (Volga).
