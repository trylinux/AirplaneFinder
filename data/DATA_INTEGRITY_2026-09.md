# Data integrity audit — September 2026

Run against the live database at 244 museums / 4,292 aircraft, after the
Oklahoma build. Four defect classes were found and closed; a fifth is
deliberately left open. Everything below was also written back into the source
CSVs, so a re-import cannot reintroduce it.

## What was checked

Orphaned aircraft; aircraft linked to more than one museum; museums with no
aircraft; missing, null-island and out-of-range coordinates; missing postal
codes; duplicate and near-duplicate museum names; the same tail number under
different models; `year_built` sanity and serial-derived years; blank
manufacturers and models; `role_type` and `aircraft_type` vocabulary; missing
`wing_type` on fixed-wing rows; and `wing_type` wrongly set on rotary-wing rows.

Clean on first pass: no duplicate museum names, no aircraft linked to two
museums, no blank manufacturer or model, no invalid enum values, no rotary-wing
row carrying a `wing_type`, no out-of-range coordinates. The only cross-model
tail collision is bort "09" at Monino, which is two different aircraft wearing
the same two-digit bort — inherent to Soviet bort numbers, not an error.

## Defect 1 — `year_built` laundered from serial fiscal-year prefixes

**228 rows.** A US military serial's prefix is the fiscal year the aircraft was
ordered, not built; for post-war types the airframe is typically delivered one
to three years later. 297 rows carried a `year_built` exactly equal to their
serial's FY prefix. 69 of those were pre-1946, where FY and build year usually
do coincide, and were left alone. The other 228 were treated as unsourced.

Each of the 228 was researched against Joe Baugher's serial pages, Aerial
Visuals airframe dossiers, museum publications (the Dyess Linear Air Park
booklet proved unusually good, carrying per-airframe delivery dates), and
type-specific production lists.

- **86 verified** from a real construction, roll-out, first-flight or
  delivery/acceptance date. **76 of those differed from the FY prefix**,
  usually by one to three years — confirming the diagnosis. The other 10 land on
  the FY year but now rest on a sourced date rather than inference.
- **142 could not be sourced and were blanked.** In almost every case the only
  thing any source offered was Aerial Visuals' "Circa &lt;FY&gt;" placeholder,
  which is the same inference this cleanup exists to remove.

Yield varied sharply by museum, and it tracks whether the institution publishes
airframe-level history: Dyess 18/25, Castle 20/43, Lackland 10/22, HAMM 4/9,
Fort Worth Aviation Museum 0/9.

## Defect 2 — missing `wing_type` on fixed-wing rows

**272 rows, and not a research problem.** 270 of them were at exactly two
museums — Planes of Fame (143) and Yanks (127) — and **their source CSVs already
carried the values**. Neither museum had a single live row with a `wing_type`,
so an import path dropped the column for those two files. The values were
reconciled from the CSVs and re-applied.

Two genuinely blank rows remain. One is a Piper J-3 Cub, since fixed
(monoplane). The other is an MMIST CQ-10A Snowgoose — a powered parafoil cargo
UAV that arguably should not be `fixed_wing` at all; left alone pending a
decision on how to classify parafoils.

## Defect 3 — orphaned aircraft

**11 aircraft linked to no museum**, all low-numbered early seed records,
invisible in every museum view but still counted in the global total. Each was
traced:

- **8 linked** to their actual holders, six of which were new museum records:
  B-17G 44-83624 and C-5A 69-0014 to the Air Mobility Command Museum, Dover;
  C-123K 54-0612 to March Field; C-47A 43-15073 ("The SNAFU Special", a D-Day
  paratroop aircraft) to the Merville Battery Museum in Normandy; Concorde
  G-BOAA to the National Museum of Flight, East Fortune; F/A-18A 161749 to the
  Flying Leatherneck Aviation Museum's new Irvine site; UH-1H 66-16579 to The
  Helicopter Museum, Weston-super-Mare.
- **74-1686 was misidentified and had moved.** It is not a plain C-130H but the
  **YMC-130H "Credible Sport II"** — one of three rocket-modified airframes from
  the 1980 Iran hostage rescue programme — and it left Robins AFB for the Empire
  State Aerosciences Museum, Glenville NY, around 2018. Type and location both
  corrected.
- **3 deleted.** Spitfire Mk.IX **MK356 was destroyed** in the fatal BBMF crash
  at RAF Coningsby on 25 May 2024 and no rebuild is announced. UH-60A
  **79-23298 is not a museum aircraft** — it is N600PV, Sikorsky's optionally
  piloted Black Hawk autonomy testbed, still flying. And a Ford 5-AT-B Trimotor
  with no registration and no construction number cannot be pinned to any of the
  ~18 surviving airframes.

## Defect 4 — a missing coordinate

One museum, the Gateway Freedom Monument at Alamogordo, which was already
documented as coordinate-less in the New Mexico notes. Geocoding the US-70/US-54
intersection returned only a town centroid, so it stays blank rather than gain
false precision.

## Left open — museums with no aircraft

**10 museums hold no aircraft record.** Several are deliberate: the New Mexico
pass recorded Walker Aviation Museum and the Western New Mexico Aviation
Heritage Museum without verifiable airframes. The notable gap is the
**Cosmosphere** in Hutchinson, Kansas — a major space collection recorded as an
empty shell — which will be filled as part of the Kansas build rather than as
separate work.

## Identity problems surfaced during verification — flagged, NOT changed

These came out of the year research. None has been applied to the data: each
needs a second source or a curator before the serial or type is rewritten.

**Serials that cannot be right**
- ~~**Castle Air Museum HH-43B "62-4213"**~~ — **RESOLVED September 2026.**
  Confirmed as **62-4513** by an independent survey and corrected. The error is
  upstream: castleairmuseum.org prints 62-4213 itself.
- ~~**Castle Air Museum VC-9C "73-1781"**~~ — **RESOLVED September 2026.**
  Confirmed as **73-1681** and corrected. 73-1682 is at the AMC Museum and
  73-1683 at Evergreen.
- **Gateway Freedom Monument F-4E "74-0625"** — in the FY74 list, 74-0189
  through 74-0642 is a block of AGM-69A SRAM missiles; the FY74 F-4E block is
  74-0643/0666 and those were Iranian. This serial needs re-sourcing from
  Holloman or the Alamogordo chamber.
- **Hangar 25 T-37A "55-4305"** — recorded as converted to A-37A and reserialled
  67-14504, so a surviving airframe wearing 55-4305 is either mis-marked or two
  airframes conflated.
- **Texas Military Forces Museum F-84 "49-2285"** — recorded as dismantled at
  the Niagara Aerospace Museum, New York, in 2009, not at Camp Mabry, with a
  further unresolved identity question of its own.

**Types that look wrong**
- Lackland's "F-5B 73-1630" is an **F-5E**, and a serial allocated for
  production administration only — the aircraft went straight to the ROKAF.
- War Eagles' "F-84F 52-7343" is an **RF-84F Thunderflash**.
- Fort Worth's "OH-58A 70-15469" is an **OH-58C**.
- Camp Mabry's "UH-1H 64-14142" is a **UH-1C**, and is reportedly marked as
  68-16189 — which is the serial of the *other* Huey at the same museum. Those
  two rows may be swapped or overlapping.
- Camp Mabry's "UH-1M 68-16189" is recorded elsewhere as a **UH-1H**.
- Castle's "EB-57A 55-4253" is a **B-57E converted to EB-57E**.

**Location doubts**
- **C-130A 57-0457 and C-130E 62-1787** may be swapped between the NMUSAF and
  Pima records.
- **U-2C 56-6680** is recorded at the Smithsonian NASM, not the NMUSAF.
- **C-130J 99-1431** is recorded as written off on 25 January 2001; the Intrepid
  attribution needs checking.
- **Fort Worth's F-100F 56-3996** does not appear in that museum's own list, and
  its recorded history runs through the Danish air force to Mojave.
- **Tomorrow's Aeronautical Museum's UH-1H 66-0765 and T-37B 60-0103** are
  placed elsewhere by Aerial Visuals.
- **White Sands' UH-1M 66-0616** is recorded as shot down and destroyed in
  Vietnam in 1971, with the source itself flagging the conflict.
- **Mid America's TAH-1P 76-22599** was last recorded on loan to the Lone Star
  Flight Museum.
- **National Vietnam War Museum's UH-1H 73-21707** was last recorded as a
  stripped hulk sold at GSA auction in 2016.
- **Holloman's "MQ-9A 02-4001"** is recorded as a YQM-9A active with General
  Atomics at El Mirage in 2006.

**Also worth knowing**: joebaugher.com's own index has broken year links for
FY1945-53, 1956-57, 1966-68, 1972 and 1976; those pages are reachable on the
crouze.com mirror. Aerial Visuals is queryable at
`aerialvisuals.ca/Airframes.php?Seeds=<serial>`, and six of its dossiers
currently return a server-side PHP error.


---

## Addendum — Castle Air Museum audit, September 2026

Prompted by the Hawaii pass, Castle's 94 rows were audited against the museum's
current collection page and an independent survey. **Nothing had departed**, but
**fifteen rows carried bad identifiers and two airframes were missing.**

The pattern is diagnostic: seven of the fifteen errors reproduce
castleairmuseum.org's own collection page **verbatim** — construction numbers
sitting in the `tail_number` field (the EC-121's `1049A-4335`, the Cessna 150's
`150-69128`, the Stinson L-5's `76-3419`, the C-56's `18-2035`), an SBD BuNo
with an extra digit (`100508` for `10508`), and the two invalid serials above.
That record was almost certainly scraped from that page. **Treat the museum's
page as authoritative on what is present and unreliable on serials.**

Corrected: HH-43B to 62-4513; VC-9C to 73-1681; EC-121 to 52-3417 variant T;
SBD-4 to 10508 and `under_restoration`; L-5 to 44-18145 variant E; Cessna 150 to
N50198, reclassified civilian, 1968; HC-131A to 53-7786; TBM to 91188 variant 3E
and `under_restoration`; UH-12 to variant A; C-56 to N1020V.

Added: **Lim-5 010** — a Polish-built MiG-17F, ex-Afghan Air Force, carried in
the AMARC MiG disposal register as transferred to Castle but absent from the
museum's public page — and **TF-102A 56-2364**.

Left recorded with the conflict in aliases: the F-104D 57-1314, which is correct
and painted as 57-1312 (an older museum page gave 57-1330); and three
digit-transposition disputes between the museum and the survey — the BT-13
(42-89678 vs 42-86978), the PT-22 (41-20850 vs 41-20580) and the A-6E (159579
vs 157579).

Not entered: a **C-130A 56-0473** on the museum's sponsorship page that may be
the same airframe as the recorded MC-130P 66-0212, and a **PV-2 Harpoon** with
no published serial.

**The Barbers Point question that prompted this is answered**: of the five
airframes reported in 2021 as shipping from Hawaii to Castle, only the AH-1W and
the SH-60B are evidenced as having arrived, and both were already recorded.

---

## Addendum: `aliases` misuse, corrected 2026-09-08

### The defect

Research passes from California onward were instructed to leave `description`
blank and to record provenance in `aliases`. That is inverted. `aliases` is a
separate table (`aircraft_aliases`) joined into aircraft search by
`_build_aircraft_filter`, so every note written there became a search term:
"confirmed still in place March 2026" made an airframe match a search for
*place*. `description`, the field intended for prose, was empty across the
whole corpus — 120 of 4,881 CSV rows had one.

The root cause was upstream of the research: `data/METHODOLOGY.md` defined a
12-field output contract that had no `description` field at all.

### Scale

Of 9,377 alias strings across 5,082 aircraft:

| bucket | count |
|---|---|
| genuine names/identifiers, retained | 4,992 |
| identifier wrapped in prose, rewritten to the bare identifier | 133 |
| prose or attributes, moved to `description` | 4,385 |

2,211 aircraft were affected; 1,165 lost every alias they had. Worst states by
strings moved: Texas 890, Colorado 569, Kansas 544, Oklahoma 413, New Mexico
301, Nebraska 249, Hawaii 218.

The moved set included pure attributes that are not names either — `replica`
(116), `airworthy` (94), `NMUSAF loan` (71), `inert` (32), `pylon-mounted` (26).

### Rule now in force

`aliases` holds only other ways of naming the airframe: alternate designations,
the dashless form of each designation, popular/export names, block and
construction identifiers, civil registrations, and the bare identifier of any
false serial worn. Everything else is `description`. Recorded in
METHODOLOGY.md; enforced by `tests/test_alias_hygiene.py`.

### Dashless search variants

Added in the same pass: every dashed designation now carries its dashless form
as an alias (`PT-22` → `PT22`, `F-16C` → `F16C`), generated from `model`,
`model`+`variant`, and each designation alias. 3,772 new alias rows across
3,388 aircraft. Without these, a search for "PT22" returned nothing.

### Method

A shape heuristic was tried first and rejected — it left a 2,298-item review
band and still kept `airworthy` and `replica` as aliases. It was replaced with
a *positive* name test: a string survives only if it matches a designation,
popular-name, registration, serial, BuNo, c/n or block pattern. Everything
failing the test moves. The full 2,211-record dry run was reviewed before
anything was written.

Four rule bugs were caught during execution rather than after:

- the operator deny-list matched bare `Wing`, killing genuine names
  (`Mitchell Wing`, `Blended Wing Body`, `Oblique Wing`) — narrowed to unit
  contexts (`138th Fighter Wing`); 9 records re-patched;
- identifier shapes like `4-469` and `707-320B` had no pattern — added;
- the `mark`/`model` pattern was unanchored and swallowed `marked …` strings,
  keeping 32 notes verbatim as aliases — anchored; 32 records re-patched;
- the `c/n` pattern accepted trailing prose (`c/n 6 the sixth Learjet built`),
  which the new hygiene test caught in 5 files after the migration had
  "finished"; 11 strings split into `c/n <id>` + description.

### Verification

- DB: 4,056 aircraft patched (148 transient 500s at 6 concurrent workers, all
  clean on serial retry), plus 41 rule-fix re-patches and 90 reconciliation
  patches.
- CSVs: 335 of 336 files rewritten, preserving each file's original line
  terminator. All 336 round-tripped byte-identically before the rewrite, so the
  diff is exactly the changed cells: 4,326 insertions / 4,303 deletions.
- Reconciliation: every CSV row matched to its database id by
  (museum, model, tail). 4,767 rows had an unambiguous match; **4,767 of 4,767
  now have identical alias and description sets in the CSV and the live
  database.** 114 rows (untailed duplicates within one museum) have ambiguous
  keys and were verified only through the migration itself.
- Test suite: 4,952 passing, including 672 new alias-hygiene assertions.
