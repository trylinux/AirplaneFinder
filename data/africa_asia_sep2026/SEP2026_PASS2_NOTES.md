# Russia's plinth pass, Africa, the Caribbean and the last zeros — 10 September 2026

The second half of the September sweep. Four things happened: the Russian
monument backlog was built and imported, Africa was reopened, the Caribbean and
Vietnam were filled in, and the last cluster of zero-record countries was closed.

Evidence: `data/russia_monuments/`, `data/africa_asia_sep2026/` and the six
`research_*.md` dossiers alongside them.

## What went in

| Pass | Sites | Airframes |
|---|---|---|
| Russia — plinths and gate guards | 786 | 993 |
| Africa — north, east, southern, west | 215 | ~700 |
| Caribbean + Vietnam | 29 | 122 |
| Malta, Myanmar, Cambodia, PNG and the last zeros | 28 | 160 |

Africa went from **107 sites / 360 airframes across 30 countries** to **323 sites
across 37**. South Africa alone went 20 → 79. Russia went 107 → 893.

## The Russian plinth pass

`build` had been documented in `harvest_russianplanes.py`'s usage block since the
script was written and **was never implemented** — the region sat "ready" for a
day without being buildable. It is written now, along with a `live` stage that
caches the database's Russian museums so the builder can tell a new plinth from
a top-up onto a site already recorded.

Four data faults were found and fixed while building it, each of which was
silently destroying airframes:

- **`?` was being imported as a serial.** The source writes `?` where the bort is
  unknown. Passing it through made every unknown-bort airframe of a type collide
  with every other one; twenty rows were deduped away before it was caught.
- **The bort-colour regex missed every `ё` spelling** — `жёлтый`, `чёрный`,
  `зелёный` — so Yellow, Black and Green borts never got their `operator_country`.
  Fixing it took the field from 483 rows to 502.
- **Two-digit borts repeat town after town.** "01 Red" recurs across Russia, and
  the unique key cannot hold two of them apart. Where the same
  (designation, tail, operator_country) appeared at more than one site, the bort
  is now blanked and recorded in the description as a marking, with the
  construction number (51% coverage) doing the identifying work. **48 rows.**
  Silently deduping them — which is what the builder does downstream — would have
  thrown away real aircraft.
- **The same registration mapped twice at one site.** russianplanes maps some
  airframes from two points; a civil registration is unique, so that is one
  aircraft entered twice. Merged on (model, tail) within the site: 4 rows.

**Reading the dry run's `warnings` list, not just its `errors`, earned its place
in the standing rules.** Seven warnings resolved to **six airframes already
recorded at the same place** — three of them at Monino, which a 500 m
site-matching radius missed because its open park is bigger than that. Those six
would have gone in as duplicates of records the project already had.

## Three bugs in the shared pipeline

**1. `tail_number` is `VARCHAR(20)` and nothing checked it.** A single
24-character bort-plus-dedication string (`01-красный/Марат Таранда` — the
airframe is dedicated to a person) passed every validator and every dry run, then
died inside the INSERT with a `DataError` that took **all 400 rows of its atomic
batch** with it. There is now a test for it. The row itself was split correctly:
bort to `tail_number`, name to `aircraft_name`.

**2. `data/_to_delete/` was inside test discovery.** The bridge cannot delete
files, so superseded builds are moved there — and both test modules were
rglob'ing straight through it, validating five stale copies of every Russian file
and failing the suite on data that is not part of the project. Excluded in both.

**3. Two test false positives, both real bugs in the tests.** `NA` is Namibia's
ISO 3166-1 code and was being rejected as the placeholder "n/a" — the same trap
waits for `NO`, Norway. And `HAS` is a Royal Navy mark prefix (Wasp HAS.1, Wessex
HAS.3) that the alias prose detector reads as the verb "has". Both fixed at the
test, not by mangling the data.

## A destructive mistake, and the repair

**The reconciler I wrote deleted 89 pre-existing African airframes.** Its
"surplus" logic assumes the files it is given are the *complete* inventory for
each museum. That is true for a region built from scratch and false for a
**top-up** file, which lists only the airframes being added — so every row
already at the site looked like a duplicate and was deleted.

All 85 recoverable rows were restored from the repo's own per-museum CSVs, which
is exactly what that one-file-per-museum convention is for; a re-run of the
repair reports zero missing. (Four deletes had failed with a 500 and were already
still present.) **Deletion is now opt-in behind `--delete-surplus`** and the
reasoning is written into the script.

The lesson generalises: **a reconciler must know whether a file is an inventory
or a top-up, and must never infer it.**

## Sources

- **`spottingmode.com/wro` carried the whole of Africa**, and it is the only
  source on that continent with a display-versus-derelict vocabulary
  (`pre`/`std`/`dum`/`dlt`/`i/a`), per-location coordinates and construction
  numbers. Mechanics for next time: it needs
  `curl --ciphers "DEFAULT@SECLEVEL=1"` (small DH key), WebFetch fails on it, and
  the per-**location** pages matter because the country lists collapse a
  six-plinth air base into one city name. 517 location pages, 185 preserved South
  African airframes, 35 Nigerian, 23 Ghanaian, 23 Angolan.
- **OSM is close to useless in Africa and must not be read as absence.** One pass
  returned **exactly one element across eighteen countries**; South Africa's
  entire `historic=aircraft` population is a single node. The same warning
  applies to Cambodia (three known displayed airframes, zero nodes) and to ten of
  the fourteen countries in the small-zeros sweep.
- Mirror behaviour keeps shifting: `overpass.private.coffee` worked for East
  Africa while kumi 504'd and maps.mail.ru 301'd; `maps.mail.ru` worked for
  southern Africa while the other two timed out. **Try all three.**

## Currency findings

- **The Royal Malaysian Air Force Museum has not been in Kuala Lumpur since 15
  March 2018.** Its ~30 airframes are at Sendayan under restoration and the
  permanent museum will not open before 2028. Every directory still lists the
  closed Sungai Besi address.
- **Cuba's Museo del Aire is not in Havana.** The La Lisa site closed 2008–2010
  and the collection went to San Antonio de los Baños air base.
  `aviationmuseum.eu` says only "permanently closed" — following it would have
  deleted a site that moved.
- **The Vietnam Military History Museum moved** to Nam Từ Liêm on 1 November 2024;
  the old Điện Biên Phủ site folded into the Thăng Long Citadel that December.
  Any record on either old address is stale.
- **PNG's Aviation Heritage Centre opened 8 September 2025** — two days before
  this sweep — with A-20G 42-86786 *Hell'N Pelican II*.

## Judgment calls

- **The B-52 question, answered.** Hanoi's Hữu Tiệp Lake section and the B-52
  Victory Museum yard wreck are both recorded, flagged as wreckage in every
  description, on the project's own test: the lake has been kept clear for 54
  years, is heritage-listed, walled and interpreted. By the same test **Đà Nẵng's
  "Old Jets" were excluded** — they sit on a military apron, which is storage.
- **Vietnamese serials were treated as radioactive**, as the project's own
  measurement of `aviationmuseum.eu` repeating one serial block across three
  Vietnamese museums requires. Only eight of 71 airframes carry one, and not one
  came from a directory.
- **Egypt repaints systematically.** The Citadel museum's MiG-17, MiG-21, Su-7,
  Yak-18, Wilga and Zlin all wear false numbers, two borrowed from Almaza
  airframes. True identities in `tail_number`, worn markings in `aliases`.
- **Excluded, with reasoning**: Wonderboom and OR Tambo's storage lines (~40
  airframes), Windhoek Eros's dump, Mali's 32 derelicts, Angola's Catumbela and
  Cabo Ledo wreckage, the UTA 772 Ténéré memorial (built *from* debris, not a
  retained airframe), Curaçao's stripped Air Aruba YS-11, Guadeloupe's four
  aircraft *sculptures*, the Laos Plain of Jars scrap reuse, and Malta's OSM
  `memorial=aircraft` node at Luqa, which is a **scrap line at SR Technics** and
  was the single strongest trap in the sweep.
- **Well-searched zeros**, each with what was searched named: Rwanda, Bhutan,
  Maldives, Timor-Leste, Fiji, Guyana, Suriname, Kosovo, Haiti, the Bahamas, and
  Namibia's Okahandja Military Museum (built 2004, never opened) and Outapi War
  Museum (open, no aircraft).

## Ranked open items

1. **`operator_country` backfill on the pre-existing ~20,000 rows.** Unchanged
   from this morning and still the top data-quality job. The Russian plinth pass
   made the cost concrete: an ex-Soviet **L-29 at the Chico Air Museum in
   California**, with a blank country code, was blocking a Russian plinth's bort
   "38". Russia's own 1,190 rows first, then the tail-number recovery — 347 of
   them still have no tail at all and are all recoverable from this dataset.
2. **The non-Russian russianplanes tranche — 280 sites, 705 airframes** in
   thirteen countries a crude bounding box had counted as Russian. **Several of
   those countries were imported today from other sources**, so this is now a
   diff, not an import, and it needs its own operator-country research.
3. **The `stored` and `parts` categories** in the russianplanes data — 1,181 and
   281 points — were skipped deliberately and are worth a considered second pass.
4. **Nha Trang Air Force Officers' College holds eleven unrecorded airframes** —
   the largest untouched Vietnamese collection found.
5. **The relocated Cuban Museo del Aire's 29 airframes** are unlisted anywhere
   reachable; San Antonio de los Baños is a working air base.
6. **One visit to Malta closes twelve open questions**; one email to RAAF
   Heritage closes the entirely unpublished PNG Aviation Heritage Centre roster;
   the RSAF Museum publishes eighteen types and not one serial.
7. **Mekelle's Hawulti aircraft park** — four airframes, last confirmed 2015, in
   the 2020–22 war zone. Recorded and explicitly unverified.
8. **Casablanca's Royal Air Maroc collection**, including an L-749
   Constellation, is likely to move under the Casa Anfa redevelopment.
9. **Two Russian rows could not be placed** — a Mi-6A at Nyurba and a Su-24 "29"
   at Nizhny Tagil — because the server also dedupes on `construction_number`,
   which no dry run models. Both are already represented in the database.
