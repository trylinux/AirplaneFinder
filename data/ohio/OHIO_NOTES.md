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

---

# Ohio phases 2 and 3, and the NMUSAF gap-fill (2026-09-08)

**105 airframes and 31 sites added.** Ohio now stands at **48 sites and 500
aircraft**, from 1 site and 283 at the start of the day.

| Pass | Sites | Airframes | Files |
|---|---|---|---|
| NMUSAF gap-fill | 0 (existing site) | 64 | `nmusaf_topup_gapfill_aircraft.csv` |
| Phase 2 — military bases | 8 | 16 | `oh_bases_museums.csv` + 8 |
| Phase 3 — monuments | 23 | 25 | `oh_monuments_museums.csv` + 23 |

---

## NMUSAF: 283 -> 347

The A–L half was catalogued in an early unsystematic pass; M–Z was done
properly. The gap-fill paged **all 26 letters** of the fact-sheet index —
194 pages, 1,823 unique fact sheets — and then fetched ~110 individual sheets
to confirm each candidate is an artifact the museum actually holds.

**M–Z was not as complete as assumed.** The supposedly-finished half still
yielded MiG-23MLD, MiG-23MS, MiG-25RB, MiG-29A, XP-81, X-19, XB-42A, O-46A,
XF-85, XF-90, XH-20, XR-8, X-24A, X-24B, X-29, YF-4E, Q-2, NF-16A, a second
Standard J-1, SV-5D, Mercury and Teal Ruby.

**The gallery pages are a subset of the fact-sheet index, not a supplement.**
All ten gallery pages were checked: 452 links, 9 absent from the index, and
**none of the 9 was an airframe** (trophies, a camera, a 37 mm cannon, HVAR
rockets). Worth knowing — it means the index alone is sufficient, and saves
the next pass the work.

**The X-24A on display is not an X-24A.** It is the jet-powered Martin SV-5J
built for flight training; the real X-24A was rebuilt in 1973 into the X-24B
that stands beside it. Both are recorded, with the substitution stated.

**Four cross-museum conflicts found and left unresolved rather than guessed.**
Each is an airframe the NMUSAF fact sheet claims while the database already
records it elsewhere. Importing any of them would have collided on
`uq_model_tail`, which is how they surfaced:

| Airframe | Database says | NMUSAF fact sheet says |
|---|---|---|
| C-130E 62-1787 | Pima Air & Space Museum | NMUSAF (the Air Force Cross mission aircraft) |
| SR-71A 61-7976 | Museum of Flight, Seattle | NMUSAF |
| C-17A 87-0025 "T-1" | Steven F. Udvar-Hazy Center | NMUSAF (the prototype) |
| AC-130A 54-1630 "Azrael" | already at NMUSAF | — a true duplicate, not a conflict |

The C-130E case was already flagged as open in these notes before this pass;
the other three are new. **All four excluded from the import.** Resolving them
means checking the *other* museum's own page, not NMUSAF's — one of the two is
wrong in each case, and the AC-130A finding suggests the real NMUSAF gap there
is the **prototype gunship** (retired May 1976), not Azrael.

**16 rows excluded for want of a sourced manufacturer.** `manufacturer` is a
required field, and the fact sheets for these name none. This follows the rule
already applied to the SS-N-2 Styx in the earlier pass — recording a
nationality or a from-memory attribution would put a guess in a company
column. Excluded: **AGM-45 Shrike, AGM-65 Maverick, AGM-78 Standard ARM,
AIM-9 Sidewinder, SA-2 Guideline, SA-4 Ganef, SS-N-2 Styx, Wasserfall, V-2,
GAM-67 Crossbow, Discoverer XIV, Sputnik I, Grid-Sphere, Caquot Type R**, and
the three balloon gondolas **Man High, Stargazer, Excelsior** (Excelsior is
also a stated replica). Every one is a real museum holding — they need a
sourced builder, not more research into whether they exist. This is the
single most actionable open item in Ohio.

Where the museum's own text named the builder it was used: the KH-7 and KH-8
GAMBIT vehicles and the KH-9 HEXAGON are recorded as **Lockheed** because the
fact sheets say Lockheed built the Agena and was the vehicle contractor.

**Serial coverage is 11 of 64.** That is the museum's gap, not the
researcher's: NMUSAF fact sheets are written as type histories and mostly do
not state which airframe is on the floor. B-52D, B-57B, F-15 Streak Eagle,
F-15C, XF-85, XF-90, both X-24s, HH-60G, Ju 52, XP-81, O-46A, T-46A and C-5A
all have no serial published by the museum. Left blank rather than sourced
from a registry and implied to be the museum's own claim.

---

## Phase 2 — military bases

Eight sites, 16 airframes, every serial checked against its production block
and **all 16 inside their block**.

**Currency is the whole story here, and it is uneven.** Base displays are
harder to verify than museums because you cannot walk up to most of them:

- **Rickenbacker (3 gate jets), the AASF Cobra, and the NOSC A-7** — reported
  present **March 2026**, six months ago. Strongest evidence in the pass.
- **Toledo (4 jets)** — last dated sighting **July 2022**.
- **Springfield-Beckley (4 jets)** — last evidence is a **2012** coordinate log
  and **2005** photographs. Fourteen years. The 178th has since lost its flying
  mission entirely (F-16s gone 2010, now MQ-9 and intelligence), and all four
  are NMUSAF loan-programme airframes, which the museum recalls and reassigns.
  **Treat as unverified.**
- **Mansfield Lahm (2 jets)** — last evidence **2014**; the pole-mount note is
  from **2001**. The 179th redesignated from Airlift Wing to Cyberspace Wing in
  September 2023 and its last C-130H departed. A unit that stops flying is
  exactly when displays get moved.
- **Camp Perry** — 2013 photographs, 2017 log.
- **DSCC Columbus** — no dated sighting of any kind.

Every one of these carries its currency evidence in `description`, so the
record states its own weakness.

**Corrections with evidence.** Toledo's F-84F **51-9525 was built by General
Motors** at Kansas City (block F-84F-40-GK), not Republic as the directories
say — manufacturer recorded accordingly. A published account gives Toledo's
F-16 as 80-0159; the wing's own article and two serial lists give **80-0519**.
DSCC's UH-1H is a **Bell** airframe, not the Aerospace Industrial Development
Corporation build one directory claims.

**The "Valentine Flyer at Huffman Prairie" lead was wrong.** Wright "B" Flyer
Inc's own page places it at **Fairfield Commons Shopping Mall, Beavercreek** —
not on Wright-Patterson, and not a base display. Huffman Prairie Flying Field
itself holds **no airframe**: a reconstructed 1905 hangar, a catapult and an
interpretive centre. No site record created. (For the record, Huffman Prairie
would be `public` — NPS states the memorial is open to the public and Gate 16A
is a public access point.)

**Excluded:** Youngstown Air Reserve Station (searched wing PA, AFRC and three
directories — **no display airframe found**, recorded as nothing rather than as
an empty site); Camp Ravenna (same); Rickenbacker's civil-side stored airframes
(privately owned, on the airport, not installation displays); and the
**NASIC MiG-29UB** at Wright-Patterson Area B — a real outdoor static display
confirmed by a NASIC photo release, but **no serial, Bort number or
construction number exists in any reachable source**, so it was left out rather
than invented. That is a genuine gap worth a second pass.

---

## Phase 3 — monuments

23 sites, 25 airframes. **Every serial checked against its production block and
all are internally valid** — but a valid serial says nothing about whether the
airframe is still on its pad, and that is this category's whole problem.

**Only four rest on evidence newer than five years:** Harrod (photographs
20 April 2022), Baltimore (photo set 4 December 2022), Belmont (unveiled
25 April 2026), and Union Township Cincinnati (visitor photography through
2026). **The other twenty are carried on aggregator compilations with no dated
imagery.** Each says so in its own `description`. These are the first
candidates for a Street View sweep.

**Harrod UH-1H 65-9587 is the best-documented monument in the state** and a
clean example of the marking trap: bought by the Army December 1965, flown in
Vietnam by the 173rd Assault Helicopter Company, shot down August 1967,
repaired, and now **painted in the markings of the 176th AHC** — not its own
unit — because the memorial honours the 176th's dead. Patched bullet holes are
still visible. True identity in `tail_number`, the worn number 587 in
`aliases`.

**Union Local High School, Belmont** is the freshest record in the database:
a retired Thunderbirds F-16 unveiled **25 April 2026**, the first given to an
American high school, pursued by the community for sixty years because the
school teams are the Union Local Jets. One compilation gives the serial as
87-0329 but none of the extensive news coverage confirms it, so **the tail
number is blank** and the candidate serial sits in aliases.

**Leads refuted — named here so nobody re-chases them:**
- **Sidney VFW Post 4239 AH-1 66-15250 does not exist.** The Army *allocated*
  a Cobra to Post 4239 on 24 October 2003 and **never delivered it**. Every
  compilation carrying this is propagating an allocation record. The Sidney
  Cobra is at the **AMVETS** post.
- **Blue Ash A-7 "75-0368" is an impossible serial** — there is no FY1975 A-7D
  block. Blue Ash Air Station is also an active ANG installation, so its real
  A-7D (71-0360) belongs to a base pass, not this one.
- **Middletown T-33A 51-8911** — the Middletown Veterans Memorial marker
  describes no aircraft at all.
- **Marion VFW 7201 AH-1 66-15286** — that airframe is at the Army Aviation
  Heritage Foundation in Hampton, Georgia.
- **Newark T-33A 51-9173, F-100D 54-2223 and Mystère IVA** — these belonged to
  the museum at **Newark Air Force Base, closed 1996**, collection dispersed.
- **Vandalia VFW Post 9582 UH-1 65-9696** — the post's own website and its 2024
  Veterans Day coverage make no mention of a helicopter. **Not imported.**
- **Donnelsville T-33A 51-8623, Kettering T-33A 52-9788, Franklin F-86D
  53-1058, Centerville BT-13A N93** — zero corroboration beyond one stale
  compilation. No post, park, marker, photo or news item. Likeliest of the
  whole lead list to be long gone. Not imported.
- **Harrod has ONE helicopter, not two.** The park's other exhibits are an
  M60A3 tank and a 155 mm howitzer, which probably generated the error.

**Found by sweeping rather than from the lead list:** Union Local High School
(Belmont), Brooklyn City Hall, Harrison County Airport (Cadiz), Wood County
Regional (Bowling Green), Williams Park (Gibsonburg), Alliance High School,
VFW 3334 Jefferson, VFW 4953 Rock Creek, VFW 5532 Washingtonville, VFW 5137
Medina, American Legion 551 Holmesville, VVA Chapter 55 Newark, and Wilmington
Airborne Airpark — 13 of the 23 sites.

**Site naming.** Every monument site carries its city in the name
("VFW Post 5137 Medina Ohio"), because "Veterans Memorial Museum" already
collided nationally in this database and had to be renamed.

---

## Open, ranked

1. **The 16 NMUSAF rows needing a sourced manufacturer** — highest yield per
   unit of effort in the state. They are confirmed holdings; only the builder
   field blocks them.
2. **The four cross-museum conflicts** — C-130E 62-1787, SR-71A 61-7976,
   C-17A 87-0025, plus which AC-130A is the recorded one. Check the *other*
   museum's page in each case.
3. **A Street View / dated-photograph sweep of the 20 unconfirmed monuments**
   and the 10 base airframes at Springfield and Mansfield. Cheap, and it would
   move a third of Ohio's records from "compilation says so" to "confirmed".
4. **The NASIC MiG-29UB** at Wright-Patterson needs an identity.
5. **Green Township Veterans Park, Cincinnati** — a Vietnam Huey with visible
   combat patching is in restoration, targeted for installation by 4 July 2027.
   Add it after it lands.
6. **Firelands Museum of Military History, Norwalk** (AH-1 70-16080) — a
   museum missed by the phase 1 geography split. Worth a pass.
