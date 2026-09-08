# Ohio — National Museum of the United States Air Force

Museum id 20. `1100 Spaatz St, Wright-Patterson AFB, OH 45433`.
Real collection is roughly 360 airframes; the largest military aviation museum
in the world.

## Files

| File | Rows | Tails | Status |
|---|---|---|---|
| `nmusaf_topup_a_to_l_aircraft.csv` | 149 | — | imported (157 live) |
| `nmusaf_topup_m_to_z_aircraft.csv` | 126 | 46 (36%) | imported |
| `nmusaf_m_to_z_raw.txt` | — | — | research output, kept for audit |

Split by manufacturer initial per METHODOLOGY.md. M–Z was researched as four
parallel passes (M / N–R / S–T / U–Z) against the museum's own fact sheets at
`nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Indextitle/<letter>/`.

Total: 283 of ~360, verified live.

## Serial coverage is low, and that is the honest number

36%, against 87% for Pima. NMUSAF fact sheets are written as type histories,
not airframe records — most do not state the serial of the aircraft on the
floor. Every blank here is a serial the museum does not publish, not one we
failed to look up. Per METHODOLOGY.md we left them blank rather than sourcing
a plausible serial from a registry and implying the museum said it.

Consequence worth knowing: 80 rows have no tail number, and a blank tail is
NULL, which never collides. Re-running this file without
`scripts/filter_new_aircraft.py` would silently double those 80 rows. The
import script does this automatically for `*topup*` files.

## Judgment calls

**`fetch` had to go through the app's web_fetch, not curl.** The site returns
403 to plain HTTP clients. Noted because the next person will hit it.

**Excluded — not airframes.** Engines (Salmson, Sturtevant, Walter HWK 509),
ground support equipment (MJ-1, MHU, MC-11, MA-1A), guns (M61A1, M102,
ZPU-4), warheads (W53), bomb bodies without propulsion (VB-1 through VB-13),
and exhibit/biography pages. The fact-sheet index mixes all of these in with
aircraft.

**Included as `missile_rocket` though unpowered:** Texas Instruments BOLT-117
(the first laser-guided bomb, later GBU-1) and Ruhrstahl X-4. Both are guided
weapons displayed as complete articles, and this matches how Pima's Fritz X
and Ohka are filed. Consistency across museums matters more here than a
purist reading of "missile".

**Excluded — SS-N-2 Styx.** The fact sheet gives the manufacturer only as a
nationality. The real builder is a Soviet design bureau we could not confirm
from the museum's own page, and `manufacturer` is a required field. Recording
it as "Russian" would put a country in a company column. Left out; worth
adding once someone can source the bureau.

**Not included, needs a second look.** The M pass flagged three it could not
re-verify before finishing: Martin X-24A and X-24B lifting bodies, McDonnell
Douglas AIR-2A Genie, McDonnell ADM-20 Quail. These are very likely genuine
NMUSAF holdings. They are absent rather than guessed at.

**Letters O and Q yielded nothing.** Fully paged through; O contains only
"Operation …" essays and Q only fragments. Recorded so nobody re-runs them.

**Reproductions, recorded as such in aliases:** Martin MB-2/NBS-1 (built 2002
from original drawings — no original survives), Sopwith Camel F.1 (built 1974),
Nieuport 28 (rebuilt using original parts), Wright 1909 Military Flyer (1955).
`year_built` on these is the reproduction's build year, which is the honest
answer for the object on the floor.

**Airframes displayed as something else.** Recorded under what they *are*,
with the markings noted in aliases:

- B-25B "Doolittle Raid" is physically RB-25D 43-3374
- F-82G is physically an F-82B
- F-89J 52-1911 wears the markings of 53-2509
- O-47B 39-112 is displayed in O-47A markings
- P-61C 43-8353 is displayed in P-61B markings

**Northrop B-2** is one of two unpowered structural-test airframes, not a
flying Spirit. Noted in aliases so it isn't mistaken for an operational bomber.

**Spacecraft.** Northrop OV2-5 (a donated mock-up, never flown) and the DSP
early-warning satellite are typed `spacecraft` with `role_type` `space`.

## Cross-museum conflict resolved

**X-15A-2, 56-6671 — NMUSAF holds the real one.** Pima also lists an X-15A-2
with this serial, but Pima's own page calls it a construction mockup and puts
the serial in quotation marks. The tail number is recorded here and blanked at
Pima. See `data/arizona/ARIZONA_NOTES.md`.

## Still open

- Pima's C-130 62-1787 and NMUSAF's are the same serial. Unresolved from
  before this batch; neither file currently claims it.
- ~77 airframes remain unrecorded (283 of ~360). Mostly A–L gaps rather than
  M–Z, since A–L was an earlier, less systematic pass.

---

# Ohio phase 1 — civilian museums and monuments (2026-09-08)

Until this pass Ohio held **one** site: NMUSAF. The state that invented powered
flight had a single record. 16 sites and 112 airframes added, 94 with a serial
(83%). All 16 verified live against the API after import, counts matching the
files exactly.

| Site | Rows | City |
|---|---|---|
| MAPS Air Museum | 50 | North Canton |
| Tri-State Warbird Museum | 12 | Batavia |
| Champaign Aviation Museum | 8 | Urbana |
| WACO Air Museum | 8 | Troy |
| Liberty Aviation Museum | 7 | Port Clinton |
| Crawford Auto-Aviation Museum | 6 | Cleveland |
| Armstrong Air and Space Museum | 4 | Wapakoneta |
| Butler County Warbirds | 4 | Middletown |
| Motts Military Museum | 4 | Groveport |
| Historical Aircraft Squadron | 2 | Carroll |
| Wright B Flyer Inc | 2 | Miamisburg |
| Grimes Flying Lab Museum | 1 | Urbana |
| NASA Glenn Visitor Center | 1 | Cleveland |
| Wright Brothers National Museum | 1 | Dayton |
| Zanesville Municipal Airport Memorial | 1 | Zanesville |
| Licking County Regional Airport Memorial | 1 | Heath |

## Sources and their weight

**Museum-owned pages beat every directory.** MAPS publishes a page per airframe
with acceptance dates, construction numbers and — unusually — explicit
statements about false markings. Fifty-one of those pages were read
individually. That is why MAPS is at 86% serial coverage against NMUSAF's 36%.

**The FAA registry carried the civil collections.** Champaign, WACO and
Tri-State are almost entirely N-numbered, and a live registration naming the
museum as owner is strong presence evidence. It also supplied legitimate
`year_built` values through `YEAR-MFR`.

**Two directories proved actively dangerous.**

`aviationmuseum.eu`'s Tri-State page (dated 2016) has its registration, type
and serial columns **shifted relative to one another**: N7RK is attached to a
"TBM-3S Avenger 42-84779" (42-84779 is a USAAF serial and the FAA type is
AT-6D), N3466G to the Fw 190 (it is the Corsair), N83KD to the B-25 (it is the
Mustang). Every one is contradicted by the museum's own pages and the live FAA
record. Not a second source for anything.

`silverhawkauthor.com` is a good lead generator and unreliable on digits — see
the corrections below. It lists a dozen airframes for MAPS that the museum's own
site does not, including a B-17F "124485" which is Memphis Belle's 41-24485 with
the fiscal prefix mangled, and which that source itself calls a movie replica.

## Corrections made, with evidence

**Tri-State's P-51D "Cincinnati Miss" is 44-73260, not 44-84410.** The museum
and the FAA both say 44-84410 with an RAAF A68-706 history. MustangsMustangs
gives N83KD a fully different provenance: 44-73260, surplus at McClellan 1958,
Cavalier demonstrator, remanufactured 1969, exported to Indonesia as F-361,
recovered from a Java wreck 1979. The decider is arithmetic — c/n 122-39719
maps to 44-73260 and cannot belong to 44-84410. 44-84410 is recorded as an
alias, since that is the identity it is registered and painted under.

**MAPS F-100D is 56-3081, not 66-3081.** F-100D production ended with FY56;
FY66 is impossible.

**Motts A-7D is 73-1006, not 73-1106.** The A-7D FY73 batch runs 73-0989 to
73-1015. 73-1006 also matches an earlier Rickenbacker listing for c/n D-402 —
the same airframe before it moved to Groveport.

**Tri-State's B-25 is 45-8898 with a 44-28765 centre section**, not the
reverse as one directory has it. The 1988 Kissimmee rebuild is documented and
the FAA registers 45-8898.

**Tri-State's HU-16C is BuNo 149836.** The museum's own spec block prints
"51-017", which is not a US military serial for an Albatross; its own narrative
text and the FAA both give 149836.

**Tri-State's P-40M is 43-5813.** The museum prints NZ3119 in the serial
field — that is the RNZAF serial.

**Tri-State's Stearman is an N2S-3, not the PT-17 its page is titled.** Navy
BuNo, Navy service history, FAA type B75N1.

**MAPS F-16A is 80-0513.** The museum's own site prints "8-0513", a dropped
digit.

**Champaign's Culver LFA is c/n 274.** Wikipedia's 247 is a transposition of
the live FAA figure.

## Six airframes wear an identity that is not their own

Recorded under what they *are*, with the bare marking in `aliases` and the
explanation in `description`:

- MAPS MiG-21F-13 **0301** wears **5603** in North Vietnamese 921st FR colours
- MAPS F-16A **80-0513** is painted as F-16D **89-2082** of the 180th FW
- MAPS T-37B **54-2732** is displayed as an **A-37 Dragonfly** — and the museum
  titles its own page "Cessna A-37 Dragonfly", which is exactly how a false
  identity gets into a directory
- MAPS A-4A **139947** wears **A-4F** Blue Angels colours
- MAPS S2F-1 **136464** wears **US-2A** markings and the NAS Dallas 7D code
- HAS Stinson L-5 wears **298730** with code 6C-D

## Judgment calls

**Original versus reproduction, stated explicitly in every case.** Carillon
Park's **1905 Wright Flyer III is the genuine article** — the only original
Wright airframe in this batch and the only aeroplane that is a National
Historic Landmark. Everything else Wright-related in Ohio is not: Wright "B"
Flyer's Brown Bird and White Bird are **lookalikes** (the organisation's own
word — steel-framed, Lycoming-powered, ailerons not wing-warping, and the Brown
Bird is modelled on the *modified museum* Model B rather than a real one).
Tri-State's Fw 190 is a **Flug Werk reproduction** built around a 1944 data
plate; its FAA year of 1944 refers to that plate, not the airframe. WACO's
Cootie and the MAPS Sopwith Triplane are replicas. Champaign's "Champaign
Lady" B-17 is a **multi-airframe rebuild**, recorded `under_restoration`
rather than as a completed aircraft.

**Sections rather than whole airframes**, recorded because each is the site's
principal representation of the type: MAPS F-86D **52-3927** is a cockpit
section only (the rest was consumed for spares and mechanic training) and the
**Loral GZ-22 "Spirit of Akron"** is a control car only — the only
`lighter_than_air` record in the batch.

**MAPS F-104D 57-1322 is included, and it is the reverse of the usual trap.**
It reads like pre-shipment press, but the museum states it took ownership
through GSA and **physically collected the aircraft on 8 August 2024**. That is
arrival evidence. It is wingless — NMUSAF removed them in 2016 to restore
F-104A 56-0754 — and tornado-damaged, hence `under_restoration`.

**Privately owned but museum-presented**, included with ownership in the
description: Tri-State's Ryan PT-22 (registered to a museum pilot), the HAS
Stinson L-5, and the MAPS SB Lim-2 and Sopwith Triplane.

**`access_type` is `public` for all 16.** IWASM-style reasoning: a site inside
an operating public airport terminal is still walk-up. MAPS sits on
Akron-Canton airport land but has its own street entrance with no gate.

## Excluded, and why

**Sites:**
- **International Women's Air & Space Museum** (Cleveland Burke Lakefront) —
  open and free, but holds **no airframes**. Not recorded rather than recorded
  empty.
- **Cincinnati Aviation Heritage Society** (Lunken) — four airframes claimed
  (Rutan VariViggen, a 1903 Flyer reproduction, Hovey Whing Ding II, Smith
  Termite) but all on one page whose copyright stops at 2023, and the society
  is a single room in the airport terminal so where the aircraft physically sit
  is unestablished. Excluded pending a call to (513) 321-0492.
- **Ohio History Center** (Columbus) — no aircraft in any current exhibit. Its
  aviation holdings, largely inherited from the defunct Ohio History of Flight
  Museum, are in storage or on loan; two went to WACO in 2009.
- **Mansfield Memorial Museum** — aviation gallery, no airframes. Building a
  Frank P. Lahm Aviation Museum; worth re-checking once that opens.
- **National Aviation Hall of Fame** — shares the NMUSAF building, holds no
  airframes of its own.
- **Ohio Society of Military History** — has relocated into the MAPS campus and
  is now a MAPS exhibit, not a separate site.
- **Ohio History of Flight Museum** — long defunct, collection dispersed.
  Anything sourced to it is decades stale.

**Airframes:**
- **MAPS "P-51 Mustang"** — a fiberglass mockup formerly at Cleveland's 100th
  Bomb Group Restaurant, now on a pylon at the museum entrance. A shape, not an
  airframe.
- **WACO's CG-4A "glider"** — a replica shell built in 2015 to house the
  museum theatre. A building.
- **Armstrong's outdoor Gemini and Apollo capsules** — walk-in fibreglass
  mockups. The **flown Gemini VIII** and the **flown Skylab 3 command module**
  at NASA Glenn are recorded; the mockups are not.
- **Motts R4D BuNo 99838** — listed by one directory as an R4D-7, but 99838
  falls in an R4D-6 block, no visitor account or photograph mentions a
  C-47-sized aircraft at Groveport, and the museum's own site lists no aircraft
  at all. Not recorded until someone confirms it exists.
- **Champaign's Vampire T.35 A79-633** — N35DS is now a reserved number held by
  Calico Aviation of Seattle (January 2025) and the museum's own index omits
  it. Presumed departed.
- **Champaign's Beech 18 gate guardian and TG-3A glider 42-52948** — Wikipedia
  only, absent from the museum's index, no photograph.
- **HAS Beech C-45B, Burges P-51D N51DZ, VariEze, BT-13A frame, Culver Cadet,
  Baby Ace, Wright 1902 glider replica** — each in exactly one undated
  directory; N51DZ is deregistered.
- **HAS Stinson 10 N26419** — registered to Blackwater Aviation of Holt,
  Florida since July 2022. Left the state.
- **HAS A-26** — the squadron's own page says it "has been sold and is no
  longer at the museum."
- **F-86H 53-1528**, previously listed at Lunken — now preserved at Warner
  Robins, Georgia. Left the state.
- **Liberty's Harvard IV MM53844** — the museum states it does not own it.
- **WACO's YMF-5C N820WF** — a 2004-built Waco Classic operated for paid
  biplane rides. An operating aircraft, not a display.
- **Crawford's other six aircraft** — the museum says it holds twelve and
  publishes six. The rest are unidentified.
- **Fairborn YF-102 52-7995** — reported scrapped.

## Deliberately blank

`year_built` is blank on all four Motts airframes, the Gnat, the HAS L-5, both
F-105s, five of the eight WACOs, the Gemini VIII, the F5D-1 and the HU-16C. In
every case what was available was a fiscal-year serial prefix (an order year),
a model-introduction year, or an empty FAA `YEAR-MFR`. None of those is a
construction, roll-out, first-flight, delivery or acceptance date.

`tail_number` is blank on the Folland Gnat, the Armstrong Aeronca Champ, the
Wright "B" Flyer White Bird, the MAPS CGS Hawk and SB Lim-2, the Liberty PT-17
and Denight Special, and four Crawford airframes. The **Hovey Whing Ding II**
would have been a substantive blank rather than a gap — Part 103 ultralights
carry no registration at all — but it is excluded with the rest of the CAHS
block.

## Still open, ranked by what one call settles

1. **Crawford / WRHS, (216) 721-5722** — the six unpublished aircraft, the
   Chester "Goon"'s actual location, and whether their Howard DGA-3 "Pete" is a
   second airframe or a reproduction (the original went to Oshkosh in 1991).
   Highest-value single call in the batch: settles three records and adds up to
   six.
2. **Motts, (614) 836-1500** — does the R4D exist, and dated confirmation that
   the AH-1F, UH-1H, OH-6A and A-7D are all still standing. Every Motts record
   currently rests on directory data.
3. **Historical Aircraft Squadron, (740) 653-4778** — the Gnat's real serial
   and whether it is a Folland Gnat or a HAL Ajeet; whether the L-5 is still in
   Hangar B. Thinnest-documented site in the sweep.
4. **MAPS, (330) 896-6332** — the F9F-8P BuNo question (144402 sits in the
   F9F-8 block, not the -8P block), the AV-8B's primary identity, the SB Lim-2
   serial, and whether the Martin Glider is the 1908 original or a
   reproduction.
5. **Butler County Warbirds, (513) 702-3062** — registrations for all four
   airframes (none published anywhere) and a BuNo-card check on N2S-1 "3240",
   which does not sit in the published N2S-1 block.
6. **Tri-State, (513) 735-4500** — whether they accept 44-73260 for
   "Cincinnati Miss", and the Flitfire's current registration (N3513N now reads
   unassigned).
7. **Zanesville and Circleville** need dated photographs more than calls.

## Deferred to later phases

- **Springfield-Beckley ANGB** — F-84G 51-0791, F-84F 51-1797, A-7D 72-0178
  "City of Springfield", F-100A 53-1559, all behind a controlled gate.
- **Wright-Patterson AFB, excluding NMUSAF** — the Huffman Prairie "Valentine
  Flyer" (a Wright "B" Flyer Inc asset displayed on the field in warm months)
  and the Wright Brothers Memorial.
- **Defense Supply Center Columbus** — UH-1 69-15939, behind a gate.
- **AMVETS Post 2256, Circleville** — F-105D 59-1771 "Black Bart". Recorded
  nowhere yet because the post's street address could not be established.
- **The wider veterans-post gate-guardian population** — roughly 25 airframes
  identified across Arcanum, Baltimore, Blue Ash, Cincinnati, Pickerington,
  Sidney, Donnelsville, Kettering, Franklin, Middletown, Newark, Cambridge,
  McArthur, Harrod and Centerville. All trace to a single stale list and need
  individual currency checks. This is the phase 3 workload.
