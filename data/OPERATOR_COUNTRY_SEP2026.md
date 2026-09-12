# `operator_country` backfill — 12 September 2026

**Coverage 20% → 54%.** 10,712 records given an operator country; 0 existing
values changed; 27 conflicts surfaced, each of them a duplicate airframe.

## Why it mattered

`uq_airframe (full_designation, tail_number, operator_country)` is what stops
two different national airframes sharing a serial from being merged, and what
stops one airframe being split in two. But **NULL never collides with NULL in
MySQL**, so the key only protects a row when both sides carry a code. At 20%
coverage it was mostly notional — an ex-Soviet L-29 at the Chico Air Museum,
country blank, was blocking a Russian plinth's bort "38".

## The principle used

The country comes from **the serial system the `tail_number` belongs to**, never
from where the aircraft now stands. A Matricola Militare is `IT` in a British
museum; an RNZAF serial is `NZ` in a UK one. That is what keeps one airframe one
record — if two passes filed the same serial under different countries the key
would split it, which is the failure it exists to prevent.

Two sources of evidence, no guessing:

- **Civil registrations.** ICAO allocates nationality marks uniquely, so a
  well-formed registration names its country outright — 4,600 rows across 80
  prefixes.
- **Military serial systems with a unique shape** — USAF/US Army fiscal-year
  serials, RAF serials, Bundeswehr `NN+NN`, RAAF A-series, RNZAF, Matricola
  Militare — about 6,100 rows.

Anything whose shape is shared between systems is refused and left blank, with
the reason recorded. Of the 24,961 blanks, 43% resolved. Of the remainder, 6,108
have **no tail number at all** — they cannot collide on country either, so they
lose nothing by staying blank — and the rest need research, Soviet and Russian
bort numbers above all.

## Two adversarial review passes, five classes of systematic error

The first generated file looked fine and was wrong in five places. Both passes
were run as independent adversarial reviews with instructions to find wrong
rows, and between them they caught ~390 bad assignments before anything was
written. Every one was a shape collision between national systems:

1. **Unanchored prefix matching.** `CCCP-13373` matched the Chilean `CC-` entry,
   turning **135 Soviet aircraft into Chilean ones**. `P4-KFD` (Aruba) matched
   `P-` (North Korea); the Spanish code `G1-AD` matched `G-`. Prefixes are now
   matched exactly, never as a prefix-of-a-prefix.
2. **Military serials shaped like registrations.** RAAF `A72-176` read as Qatar,
   `A20-627` as Botswana, Indonesian `TT-0411` as Chad, the Finnish Hurricane
   type code `HC-452` as Ecuador.
3. **Fiscal-year serials with a three-digit suffix aren't American.** A real one
   always has four or five. The short ones were Danish (`41-401` Spitfire),
   Saudi and Kuwaiti Lightning (`53-412` — the USAF never flew the Lightning),
   Turkish C-160 (`69-022`), and Australian RAAus registrations (`10-0665`),
   which are civil marks by construction class, not serials at all.
4. **The RAF never used I, Q, U or Y as a serial letter**, being confusable with
   1 and 0 — so `IN238` is Indian Navy, `IB427` an IAF Vampire, `QF420` a USAF
   drone and `U2146` a MiG-21. Beyond that, several air arms reuse the RAF shapes
   outright: India, where the prefixes genuinely overlap RAF Spitfire and
   Mosquito blocks, plus Zimbabwe (`R2504`) and Zambia (`AF506`).
5. **`N####` is a US registration and also an RNAS/RAF serial**; `A####` is also
   the pre-1935 US Navy bureau-number series — the Curtiss NC-4, `A2294`, was
   being filed as British. These are now settled by the manufacturer, and where
   even that fails (`N7471`, a British-built Viscount on the US register) the row
   is refused.

The second pass also caught a fall-through: a tail the registration table
refused as ambiguous was being handed to the serial table, which matched it on a
different rule. 143 US civil aircraft — including `N7470`, the Boeing 747
prototype — were about to be recorded as British.

## The 27 conflicts are the point

Every failed write was an HTTP 409, and every 409 means the new country made two
rows collide — i.e. **the same airframe is in the database twice**, one copy
already carrying a code. They are listed in `data/OPERATOR_COUNTRY_CONFLICTS.md`.
Most are African second-sweep sites entered twice under different names:

- Aero Beach / Aero Beach Entebbe (707 `5X-CAU`)
- Club 034 Kitengela / Kitengela Boeing 720 Restaurant (`5Y-BBX`)
- Parc de la Vallée de la N'Sele / Kingankati Airliner Display (two airliners)
- Tigray Martyrs' Memorial / Hawulti Museum Aircraft Park (`ST-PRC`)
- Asmara Expo Park, twice (`5Y-BMW`)
- Tobruk Museum / Tobruk Museum Lady Be Good Remains (B-24D `41-24301`)

Nothing was overwritten and nothing deleted — both rows of each pair are still
live. Each needs a merge decision.

## What is left

- **Soviet and Russian bort numbers.** Bare one- to three-digit numbers, often
  with a colour that is part of the identity. No shape rule reaches them; they
  need russianplanes. Russia now sits at 986 coded rows, almost all from `RA-`
  and `CCCP-` registrations.
- **~195 bare `N####` rows** where the manufacturer does not settle whether the
  tail is a US registration or an RNAS serial.
- **~145 fiscal-year serials at MAP-recipient sites** — Turkish, Philippine,
  Saudi. They are recorded `US` because the number belongs to the USAF system,
  but the airframes wear their recipient's national marks. That is a convention
  question worth deciding once and applying everywhere.
- **East German `DDR-` and `DM-` registrations** are recorded `DE`. If the
  project wants historic states kept separate, ISO reserves `DD` for the GDR and
  `SU` for the USSR.

## Then, and only then

Per `AIRFRAME_IDENTITY_KEY.md`, the blanked-tail recovery comes **after** this
backfill. It can now start — 8,387 rows have no tail number, and 347 of the
Russian ones are recoverable from russianplanes.

Method and re-run instructions: `scripts/README_operator_country.md`.
