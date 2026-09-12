# Backfilling `operator_country`

`operator_country` is the ISO 3166-1 alpha-2 code of the operator whose marks an
airframe wears — a SAAF Mirage is `ZA` wherever it stands today. It is the third
component of `uq_airframe (full_designation, tail_number, operator_country)`, and
because **NULL never collides with NULL in MySQL**, the key only protects a row
when *both* sides carry a code. 80% of the database was blank, so the protection
was mostly notional: an ex-Soviet L-29 at the Chico Air Museum, country blank,
was blocking a Russian plinth's bort "38".

## The principle

The value is derived from **the serial system the `tail_number` belongs to**, not
from where the aircraft now stands. A Matricola Militare is `IT` in a British
museum; an RNZAF serial is `NZ` in a UK one. That is what keeps one airframe one
record: if the same serial were filed under two different countries by two
different passes, the key would split it in two — the exact failure it exists to
prevent.

## How it runs

    python3 scripts/snapshot.py            # live database -> local cache
    python3 scripts/map_sites.py           # aircraft id -> site country
    python3 scripts/plan_country.py        # writes country_plan.json + country_audit.tsv
    AIRPLANE_KEY=amt_... python3 scripts/apply_country.py

`plan_country.py` changes nothing and writes an audit row for every proposed
assignment: id, country, the rule that fired, tail, manufacturer, designation and
site country. **Read `country_audit.tsv` before applying.** `apply_country.py` is
resumable and logs each id it lands.

`regs.py` holds the civil-registration table; `mil.py` the military serial
systems. Both refuse rather than guess: a shape shared by two national systems
returns `None` with the reason, and those rows are left blank for research.

## What the rules learned the hard way

Two adversarial review passes over the generated file found **five classes of
systematic error**, every one a shape collision between national systems. They
are fixed, and the fixes are the reason the rules look defensive:

- **Unanchored prefix matching.** `CCCP-13373` matched the Chilean `CC-` entry,
  turning 135 Soviet aircraft into Chilean ones; `P4-KFD` (Aruba) matched `P-`
  (North Korea); the Spanish code `G1-AD` matched `G-`. Prefixes are now matched
  **exactly**, never as a prefix-of-a-prefix.
- **Military serials shaped like registrations.** RAAF `A72-176` read as Qatar,
  `A20-627` as Botswana, Indonesian `TT-0411` as Chad, the Finnish Hurricane type
  code `HC-452` as Ecuador. A registration now needs an alphabetic suffix unless
  its country is one of the handful that issues numeric ones.
- **A fiscal-year serial always has a four- or five-digit sequence.** A
  three-digit suffix means a foreign type-coded system of the same shape: Danish
  `41-401` Spitfire, Saudi and Kuwaiti Lightning `53-412`, Turkish C-160
  `69-022`, and Australian RAAus `10-0665` — which is a civil registration by
  construction class, not a serial at all.
- **The RAF never used I, Q, U or Y as a serial letter** (confusable with 1 and
  0), so `IN238`, `IB427`, `QF420` and `U2146` are other air arms — Indian Navy,
  IAF, a USAF drone and a MiG-21. Beyond that, several air arms reuse the RAF
  shapes outright: India (HAL Ajeet `E1046`, Bell 47G `BZ544`, and prefixes that
  genuinely overlap RAF Spitfire and Mosquito blocks), Zimbabwe (`R2504`), Zambia
  (`AF506`). Those sites are excluded, as are types the RAF never operated.
- **`N####` is a US registration and also an RNAS/RAF serial**, and `A####` is
  also the pre-1935 US Navy bureau-number series — the Curtiss NC-4, `A2294`, was
  being recorded as British. These are settled by the manufacturer: a UK airframe
  builder means a British serial, anyone else means a registration. Where even
  that is not enough — a British-built airliner on the US register, `N7471`, a
  Capital Airlines Viscount — the row is refused.

## Coverage

Roughly 43% of the blanks resolve from the tail alone. The rest divide into rows
with **no tail number at all**, which cannot collide on country either and so
lose nothing by staying blank, and rows whose serial system needs research —
Soviet and Russian bort numbers above all, which are bare one- to three-digit
numbers and resolve only against russianplanes.

## What a 409 means here

A conflict on apply is not a failure. It means setting the country revealed that
two rows are **the same airframe recorded twice**, one of which already carried a
code. Those are listed in `OPERATOR_COUNTRY_CONFLICTS.md` as duplicate candidates
— the key doing exactly the job it was added for.
