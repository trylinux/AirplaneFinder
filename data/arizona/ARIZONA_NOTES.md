# Arizona

Before this pass the database held **two** Arizona sites: Pima Air & Space
(366 aircraft, complete) and Commemorative Air Force Airbase Arizona recorded
with **one** aircraft. Now **17 sites and 405 aircraft**.

| Site | Rows |
|---|---|
| Pima Air & Space Museum | 366 (pre-existing, untouched) |
| Commemorative Air Force Airbase Arizona | 21 (was 1) |
| Gila Bend Municipal Airport Display | 2 |
| South Mountain High School Display Phoenix | 2 |
| Veterans Memorial Freedom Garden Quartzsite | 2 |
| 12 further single-airframe sites | 12 |

## Planes of Fame Valle is closed and the collection has dispersed

The headline finding, and a clean example of why presence must be tested
rather than assumed. Planes of Fame announced on **9 February 2023** that the
Valle facility closed to the public; artefacts went to Chino or into storage.

This was verified independently rather than taken on the announcement: a pull
of the live FAA releasable aircraft database shows **every one of the 70-plus
Planes of Fame registrations now carries a Chino, California address.** The
museum's own aircraft index returns only "Chino" or "Storage" — nothing at
Valle.

Individual airframes traced out of the state:

- **Ford 5-AT-C Trimotor N414H** -> Western Antique Aeroplane & Automobile
  Museum, Hood River, Oregon (2022)
- **Martin 4-0-4 N636X** -> 404 Foundation, Camarillo CA (registered
  27 September 2025) — note the museum's *own* Martin 404 page still says it
  "now resides at Valle, AZ", which is stale on the museum's own website
- **AD-4N N409Z and G-32A N100TF** -> Comanche Warbirds, Houston TX
- **BT-13B N56867** -> Mid-Atlantic Air Museum, Reading PA (2023)
- **Convair 240 N240HH and RB-26C N8026E** -> Chino
- **VC-121A "Bataan" 48-613** -> Air Legends Foundation, airworthy and flying
  (Oshkosh 2023 and 2025)

**No site record was created and no airframe recorded there.** Any directory
still listing aircraft at Valle is at least three years out of date.

## Sources and their weight

**Skytamer's Arizona chain** enumerated 33 display locations and carries good
per-airframe data — serials with construction numbers and walk-around
photographs. But **every Arizona survey on it is dated 2007 to 2012**. It is a
fifteen-year-old snapshot and was used for identity, never for presence.

**The live FAA registry was the currency instrument** and by far the most
productive: 316,462 records pulled and joined locally on 2026-09-09. A live
registration naming a museum is strong presence evidence; a registration that
has moved to a private owner in another state is strong evidence against.

**silverhawkauthor's Mesa page is a historical accumulation, not an
inventory.** Nine of its registrations were tested against the FAA: `N7757U`
is a Cessna 172E in Kentucky, `N9012` an American Airlines A319, `N7436B` a
Champion 7EC in Las Vegas, `N17357` a Ryan ST-A in Texas, `N9158B` an L-5E in
South Dakota, and `N6735`, `N47DJ` and `N589D` are not on the register at all.
It also lists a Canberra TT.18, a C-54, an F-16C and a DC-7 nose at CAF Mesa,
none on the museum's own 2026 page. Not a presence source.

**aviationmuseum.eu scrambles under naive extraction** — its registration and
type columns are separate blocks and a summariser mis-pairs them. The raw HTML
has to be re-aligned by hand. Same failure mode seen at Tri-State in Ohio.

## Corrections with evidence

**The Champlin Fighter Museum question is settled.** It closed 26 May 2003 and
the collection went to the Museum of Flight in Seattle. Exactly one airframe
demonstrably stayed in Arizona: **F-4N BuNo 153016**, photographed on
Champlin's inventory in April 2000. No other Champlin successor collection
survives in state.

**Quartzsite's second Phantom is 66-0384.** One directory prints `66-038`
(truncated) and the 1994 roadside marker prints `60384` (fiscal-year separator
dropped). Both resolve to 66-0384, inside the RF-4C block 66-0383 to 66-0478.

**A directory places an "NF-4E" at Quartzsite.** That is a confusion with
**NF-4E 66-0294 at Corona de Tucson**. Quartzsite holds two RF-4Cs.

**`N145AZ` "serial 44511"** is not a USAAF C-45 serial — the FAA gives
construction number **A-235**. A construction number in a serial field, the
single most common museum-page error.

**Two FAA `YEAR MFR` values rejected as impossible:** `N3246G` (SNJ-5) reads
1959 and `N9993Z` (AF-2S) reads 1940. Neither can be right, so both years are
blank. The field was used only where plausible.

## Two cross-museum conflicts, excluded rather than guessed

Both surfaced through the pre-import collision check:

| Airframe | Database says | This research says |
|---|---|---|
| F-4N BuNo 153016 | Pima Air & Space | CAF Airbase Arizona (ex-Champlin) |
| UH-1F 63-13141 | Pima Air & Space | Titan Missile Museum grounds |

The UH-1F may not be a conflict at all — **the Titan Missile Museum is
operated by Pima**, so an airframe on the Titan site could legitimately be
recorded under the parent museum. Worth deciding as a policy question: does a
satellite site get its own record, or roll up to its operator? Both left as
they stand.

## Excluded, and why

- **All Davis-Monthan AMARG / 309th inventory**, Pinal Air Park (Marana) and
  the Kingman storage yard. Stored or awaiting reclamation is not display.
- **Lauridsen Aviation Museum, Buckeye** — seven airframes are still
  FAA-registered to Hans Lauridsen, but the museum's domain has lapsed and now
  serves an unrelated site, there is no working phone, and no independent
  source places any aircraft on display at Buckeye. Ownership is not presence.
  Excluded entirely pending confirmation; this is the largest single block
  left on the table in Arizona.
- **Kingman Army Air Field Museum** — carries a CLOSED flag as of March 2026.
- **Wingspan Air Museum, Mesa** — appears only in the stale compilation; long
  defunct.
- **Meteor Crater's Apollo boilerplate BP-29** — a genuine, still-displayed
  exhibit, but no source names its builder (boilerplates came variously from
  North American Aviation and General Electric) and `manufacturer` is
  required. One citation would add it.
- **CAF Mesa scale models**: a 1/6-scale B-24, a hanging Trimotor model, an SNJ
  model, a child's pedal SNJ, nose-art boards, a propeller, a deck gun and a
  Link Trainer. **The hanging P-40 and P-47 are also excluded** — they sit in
  the museum's own list among explicitly-labelled models, and the museum
  describes its collection as running "from full-size to scale models". If
  either turns out to be full-size it should be added.
- **CAF Mesa's Huey** — the museum's own page labels it "VISITING AIRCRAFT".
- **CAF Mesa's AV-8B** — reported as arriving June 2025 on long-term loan but
  absent from the museum's own 2026 collection page. Arrival not evidenced.
- **Operational and private aircraft**: two PV-2 Harpoons at Falcon Field,
  P-51D N151RJ (now privately held and off the museum's page), two L-39Cs at
  Deer Valley, nine A-4N Skyhawks at Advanced Training Systems (a contract
  adversary fleet), Marsh Aviation's HU-16 and ES-2D.
- **390th Memorial Museum, Tucson** — legally separate but sits on the Pima
  campus and its B-17G is normally counted in Pima's inventory. Left alone to
  avoid duplicating the 366 already recorded. Flagged as the same policy
  question as the Titan Missile Museum.

## Deliberately blank

`year_built` is blank on every outdoor display and most CAF airframes: what
was available was a fiscal-year serial prefix, which is an order year.
`tail_number` is blank on twelve CAF airframes — the MiG-15bis, H-19, TG-3A,
L-16, OQ-3, C-45, O-1E, Nieuport 28, Fokker Dr.I, Fokker D.VIII, S.E.5a and
the Mesa SPAD XIII — because in each case the circulating identity failed
verification against the FAA register or no identity exists. Coordinates are
blank on 13 of 15 new sites; no coordinate was published that had not actually
been fixed.

## Deferred to the base pass

Luke AFB Air Park (Glendale); Warrior Park at Davis-Monthan; Kurth Memorial
Airpark, 162nd FW Tucson; 161st ARW Phoenix; Gila Bend AF Auxiliary Field;
MCAS Yuma; **Fort Huachuca Memorial Air Park** (RQ-7B, RQ-6, RC-12G 80-23372,
OV-1D 67-18930); and **Papago Park Military Reservation**, Phoenix, holding
A-7D "74-1741" and AH-1S 68-15064.

**Note for that pass: "74-1741" is almost certainly wrong.** A-7D production
ended in the FY73 block, so an FY74 A-7D serial cannot exist.

## Open, ranked

1. **CAF Airbase Arizona, 480-924-1940.** One call settles five things: is the
   A-26C "Miss Murphy" still there (N202R now titles to a Colorado LLP)? Is
   the AV-8B on site? Is the Nieuport 17 N124RX still there after its October
   2023 ownership change? Are the hanging P-40 and P-47 full-size or models?
   Which O-1E is theirs? Asking for data plates on the MiG-15bis, H-19 and
   SPAD XIII would close three blank tail numbers at once.
2. **Lauridsen Aviation Museum** — no working contact. Try Buckeye Municipal
   Airport management. Seven airframes hang on it.
3. **Phoenix Sky Harbor SPAD XIII** — Terminal 3 was gutted and rebuilt
   2019-2022 and no photograph after January 2012 has been found. Call the
   Phoenix Airport Museum.
4. **San Carlos F-86D 51-5915** — reported severely vandalised in August 2011
   and may be scrapped. Recorded with that caveat; needs a look before it is
   trusted.
5. **Glendale F-100D 54-2281** — was mid-restoration in 2009.
6. **Border Air Museum, 520-417-7344** — the city site lists opening hours
   while a review site flags it temporarily closed. Also confirm the reported
   An-2 used in *Indiana Jones and the Kingdom of the Crystal Skull*, which
   could not be verified and is not recorded.
