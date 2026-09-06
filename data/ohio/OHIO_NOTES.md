# Ohio — National Museum of the United States Air Force

The world's largest military aviation museum, and the second-biggest gap in
the database after Pima. **8 recorded, ~360 real.**

Split by manufacturer initial, same approach as Pima.

| File | Slice | Rows | Serials |
|---|---|---|---|
| `nmusaf_topup_a_to_l_aircraft.csv` | manufacturers A–L | 149 | 54 (36%) |
| _(pending)_ | M–Z | ~150 | |

Import with:

    AIRPLANE_DATA_DIR=data/ohio bash scripts/import_data_dir.sh

There is no museums file here — NMUSAF is already in the database (id 28-ish,
"National Museum of the United States Air Force"). The import script now
skips step 1 cleanly when a directory has no `*museums*.csv`.

## Serial coverage is low, and that is the museum's choice

Only 36% — far below Pima's 98%. NMUSAF fact sheets lead with delivery and
service history rather than the airframe's serial, and for the WWI, X-plane
and missile galleries they frequently publish no serial at all. Every blank
here is a genuine absence, not a research shortfall.

## Collisions: checked, zero

All 54 serials were diffed against the live database before shipping.
Several near-misses were removed during the build because they duplicate
records already present, in some cases attributed to a *different* museum:

- **C-130E 62-1787** — NMUSAF's own fact sheet claims it ("Spare 617"), but
  your database has it at **Pima**. One of the two is wrong. Left out of
  this file rather than force a collision; worth resolving separately.
- SR-71A 61-7976, F-22A 91-4003, C-17 87-0025, VC-137C 62-6000 (SAM 26000)
  are all already recorded.

## Caveats

- **Reproductions**, as expected for the WWI gallery: Bleriot Monoplane,
  P-26A Peashooter, 1911 Curtiss Model D (built 1987), Fokker Dr.I,
  Fokker D.VII, DH-4, and the Kettering Bug. All flagged in `aliases`.
- **On loan**: the Fw 190D-9, from the Smithsonian.
- **In storage**: Culver PQ-14B, Learjet C-21A, Lockheed NT-33A, XGAM-63
  Rascal. **Under restoration**: the A-26B (only a cockpit section is shown)
  and the Bleriot.
- **Two identity oddities the museum documents itself**: the VC-54C "Sacred
  Cow" is displayed wearing a wartime decoy serial (42-72252) rather than
  its real 42-107451, which is what's recorded here; and the A-1H "The
  Proud American" is physically an ex-Navy airframe (BuNo 134600) repainted
  as USAF 52-139738.
- **Sit-in cockpit exhibits excluded** (A-7D, F-4D, F-16, FB-111A, T-38) —
  they are not complete airframes.
- Missiles are included and typed `missile_rocket`: Minuteman I and III,
  Jupiter, Atlas, Thor, Agena, Scout, Titan IV, Bull Goose, SRAM II, Rascal.
