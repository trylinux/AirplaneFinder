# New York — research and import notes

Researched and imported 10 September 2026.

**69 new sites · 497 airframes**, plus top-ups to the two museums that already
existed as one-row stubs (Intrepid +33, Empire State Aerosciences +31). This is
the largest US state in the project so far.

Four research passes (downstate museums; upstate and western museums; military
base collections; monuments and single displays), then cross-package
reconciliation, a collision check against the 20,875 then-existing airframes and
3,196 museum names, and per-site verification against the live API after import.

Verified after import: 69 of 69 new sites present with counts matching their
CSVs exactly. The two top-up museums read one higher than their files, which is
correct — each retains its pre-existing row.

Serial coverage 329 of 497. The blanks are overwhelmingly pioneer-era aircraft,
gliders and replicas for which no identity is published.

## The two pre-existing stubs

Both held a single row, and both rows were **seed data** from `seed_data.py`,
not research. They are not equivalent:

- **Empire State Aerosciences Museum** held `YMC-130H 74-1686`. **This one is
  real** — a genuine Credible Sport conversion actually at ESAM, and
  `data/verified_misattributions.md` records it as having been repointed here
  from a wrong seed pairing. It was excluded from the top-up so it is not
  duplicated. Correct as it stands.
- **Intrepid Sea, Air & Space Museum** held `C-130J 99-1431`. **This one is
  bogus.** Intrepid has never displayed a C-130J, and
  `data/DATA_INTEGRITY_2026-09.md` already flags that 99-1431 is recorded as
  written off on 25 January 2001, with the note that "the Intrepid attribution
  needs checking". It was flagged there but never resolved.
  **It should be deleted. I have not deleted it** — removing rows from the live
  database is not something to do unasked — so Intrepid currently reads 34
  aircraft where 33 is correct. One DELETE on aircraft id 39 closes it.

## Sources and their weight

1. **The FAA registry owner-name search is now BROKEN.** Every query to
   `Search/NameResult?Nametxt=` 302s to "Name has unsupported characters",
   state-wide and regardless of punctuation. This was the highest-yield tool in
   the previous two states, so two workarounds were found and both are worth
   keeping:
   * **POST instead of GET** — scrape `__RequestVerificationToken` from
     `/AircraftInquiry/Search/NameInquiry`, then POST `nametxt` + `sort_option`.
   * **Better: download the bulk registry.** `registry.faa.gov/database/
     ReleasableAircraft.zip`, then join `MASTER.txt` to `ACFTREF.txt` locally.
     That gives whole-state owner sweeps instantly and does not depend on the
     web form working at all. This should become the standard method.
2. **The US Army display-helicopter loan list** produced 14 upstate VFW /
   Legion / Marine Corps League / AMVETS monument sites that appear on no
   aviation directory anywhere. For US states with a dense post network this is
   as valuable as the NMUSAF list and is not yet in METHODOLOGY.md.
3. **Aerial Visuals Locator** POST (`Region=New York`, `Scope=3`) returned 149
   NY rows with arc-second fixes, serials and c/ns — the structural backbone for
   monuments. Vintage ~2008-2015: identity source, never currency.
4. **OpenStreetMap** `historic=aircraft` via the `overpass.private.coffee`
   mirror, 2026 extract — the currency counterweight to Aerial Visuals.
5. **NMUSAF "Aircraft on Loan by Location"** (April 2016), 48 New York rows.
   Retrieval is fiddly and worth writing down: the live PDF is 403 to curl, the
   WebFetch summariser truncates before most state sections, and **only the
   `web.archive.org/web/20150925041956id_/` path serves a real PDF** — the
   `2023id_` path returns HTML.
6. Museums' own current collection pages; Joe Baugher; HMdb (WebFetch only,
   Cloudflare blocks curl); dated local news.

## Adjudicated conflicts

- **F-14D 164603 "Felix 101"**, the last US Navy Tomcat to fly. One pass placed
  it at the Cradle of Aviation (flown to Calverton 4 Oct 2006, restored,
  unveiled 2023); another placed it at the Northrop Grumman Bethpage gate on an
  OpenStreetMap name alone. The Cradle account is specific, dated and matches
  the airframe's documented history, so it wins. Bethpage's only row was that
  F-14, so **the Bethpage site was dropped** — a Tomcat may well stand at the
  plant gate, but no identity has been established for it and 164603 is not it.
- **AH-1F 67-15690** — the Army loan list has it at the Niagara Aerospace
  Museum; the monuments pass found it has moved to Veterans Park in the **City**
  of Tonawanda, with HMdb marker 270952 photographed **22 April 2025**. The
  dated photograph wins.
- **AH-1 71-21033** — the loan list says American Legion Post 586, Adams. The
  Cobra physically stands at Alexander Corners in **Henderson**, sponsored by
  that Adams post. Recorded where a visitor finds it; the Adams site was dropped
  because that Cobra was its only aircraft.
- **Two Tonawandas.** The Grumman F9F-6P is at Walter M. Kenney Park in the
  **Town** of Tonawanda; the AH-1F is in Veterans Park in the **City** of
  Tonawanda. Different municipalities that directories routinely conflate. Both
  recorded, separately.
- Griffiss (two names, one B-52G plus an AGM-86B ALCM only one source carried),
  Plattsburgh (museum and Clyde A. Lewis Air Park at identical coordinates),
  Sampson, Oriskany and Eastern Air Defense Sector were each merged from two
  passes into one site.

## Collisions against the live database

Three, all informative:

- **Grumman F-11A "141824" at Intrepid.** A research pass found aviamagazine
  giving BuNo 141884, saw it falls outside the F11F-1 block 141728-141868, and
  "corrected" it to 141824 — which is inventing a serial by changing a digit.
  141824 is a real airframe and it is at the **Pima Air & Space Museum**.
  Imported with a **blank tail**, the reported number in aliases. No serial is
  better than a plausible wrong one.
- **Schweizer SGS 2-32 N8600R.** The National Soaring Museum's own list carries
  it, but that registration is already recorded on an SGS 2-32 at the
  **Evergreen Aviation Museum**, Oregon. Imported with a blank tail and the
  registration in aliases, flagged for adjudication.
- **Schweizer SGS 1-24 N91888 "Brigadoon"** — already in the database at **Wings
  Over the Rockies**, Denver, whose record states it is a long-term loan *from*
  the National Soaring Museum. Record where an aircraft **is**, not who owns it,
  so the row was **dropped** from the NSM file. The museum's own collection page
  lists an airframe that is physically in Colorado — worth checking whether
  others on that page are also out on loan.

## Judgment calls

- **Old Rhinebeck Aerodrome (85 rows)** is the hardest site in the state: a mix
  of original antiques, airworthy airshow aircraft and flying reproductions. The
  museum's own nine collection pages state original-vs-reproduction and display
  status per aircraft, and that is what was followed; every replica is flagged
  in `description`, never in `aliases`.
- **Three pioneer aircraft carry no type designation at all** (an ESAM Nieuport
  scout, and Rhinebeck's Hanriot and Voisin). `model` is a required field, so
  the airframe class was used — "Scout", "Monoplane", "Biplane" — rather than
  inventing a designation number. Flagged here so a later pass knows these are
  deliberate, not sloppy.
- **National Warplane Museum and the 1941 Historical Aircraft Group** are one
  organisation at one site, with FAA registrations under four owner names.
  Recorded as one site.
- The Griffiss **B-52G 58-0225** was knocked off its pedestal by an EF-2 tornado
  on 16 July 2024 and was still under repair as of July 2025 — recorded
  `under_restoration`, not `on_display`.
- Access: Eastern Air Defense Sector and the ANG air parks are `restricted`;
  HARP's Hangar B at Floyd Bennett Field is `public` (open Tue/Thu/Sat).

## Excluded, and why (do not re-research)

- **West Point** — no aircraft or missiles displayed at all, despite being an
  obvious candidate. Checked and confirmed absent.
- **Fort Drum** — the Heritage Center's "Black Hawk" is a foam-and-wood film
  prop, not an airframe.
- **Every New York Nike site.** No displayed Nike missile survives in-state
  outside the Buffalo Naval Park and a fenced private museum at Mattituck.
- **Wings of Eagles Discovery Center is open** with a 15-aircraft published
  list; silverhawkauthor's ~40-airframe entry is roughly twenty years stale and
  those aircraft dispersed (PBY to Farmingdale, P-40E to Oregon, C-46 to NASM).
- Watervliet Arsenal, Fort Hamilton, Fort Totten, Fort Wadsworth, Camp Smith,
  Roslyn, Kings Point, and USCG sites in NY — searched, nothing found.
- The Willow-Grove-style trap did not recur: Griffiss and Plattsburgh both
  retain their displays, and both were merged rather than lost.
- Falsified leads named with evidence in the pass files so nobody re-researches
  them: Curtiss C-46 serial 44-78772 (Aerial Visuals maps it to a UH-1B), NC477N,
  NC924K, N951WM, N99420, N5308K, and a Geneseo B-17.

## Serial failures flagged, not dropped

- Massena American Legion 79 "UH-1V 66-0831" — no such UH-1 block.
- Oriskany "A-4E 148613" — sits in no published A-4E BuNo block. Imported with a
  **blank tail** and the reported BuNo in aliases.
- White Plains T-33 — two sources give different identities against the same
  c/n 580-9594. An FAA lookup on N13007 settles it.
- Niagara Falls ARS C-130H marked "914-1" — true serial unknown.
- EADS Rome's "F-4D 66-7456" is really USN **F-4B BuNo 151021**, an F-4E-lookalike
  test conversion; Baugher states this explicitly.

## Test-suite and importer fixes applied before import

Two rounds, both corrected at source in the raw pipe files and folded into
`build_raw.py` so a rebuild keeps them:

- **Alias hygiene** (8 files): trailing words made serials read as prose
  ("65-0456 reported", "83-0033 painted"), and several long descriptive phrases
  were being used as aliases. A normaliser now strips the trailing
  reported/painted/claimed/marked/noted/listed and moves any alias longer than
  26 characters or 4 words into `description`.
- **Importer rejections** (5 rows, which the builder correctly refused rather
  than guessing at): a comma in a description, three empty `model` fields, and
  an EA-6B whose `role_type` had been written into the `aircraft_type` column.

Full suite green at **43,090 tests** before anything was applied.

## Needs a human (ranked)

1. **Delete Intrepid's C-130J 99-1431 (aircraft id 39).** Bogus seed data on an
   airframe written off in 2001, already flagged in the September 2026 integrity
   audit and still live. Intrepid reads 34 aircraft where 33 is correct.
2. **Adjudicate SGS 2-32 N8600R** — National Soaring Museum or Evergreen? And
   check whether more of the NSM's published 77 gliders are physically out on
   loan, as N91888 proved to be.
3. **Switch to the bulk FAA registry download** (`ReleasableAircraft.zip`) as
   the standard owner-lookup method for remaining US states; the web form's
   owner-name search is broken.
4. **Add the US Army display-helicopter loan list to METHODOLOGY.md** — it found
   14 sites in New York that no aviation directory carries.
5. Is **F-84B 46-600** still at Hancock Field, and what is the true serial of the
   Niagara Falls C-130H? One call to 914th ARW Public Affairs (716-236-2136)
   closes several.
6. **No imagery currency pass was run for New York.** The monument records rest
   on Aerial Visuals (2008-2015) plus the 2026 OSM extract; a satellite and
   Street View pass over the 45 monument sites is the same cheap quality win it
   was in Arkansas and Pennsylvania.
7. 35 of 62 counties produced no records. Weakest coverage: the eastern Southern
   Tier, the Adirondack counties, the mid-Hudson, and New York City outside
   Manhattan and Queens.
