# Georgia — research and import notes

Researched and imported 10 September 2026.

**52 new sites · 293 airframes**, of which **127 are a top-up to the Museum of
Aviation at Robins Air Force Base** — which held exactly one record before this
work and now holds 128. That was the single largest gap in the database.

Four research passes (Robins alone; other museums plus a discovery sweep;
military base collections; monuments and single displays), then cross-package
reconciliation, a collision check against the 21,372 then-existing airframes and
3,265 museum names, and per-site verification against the live API.

Verified after import: 52 of 52 new sites present with counts matching their
CSVs exactly. Robins reads one higher than its file, which is correct — it keeps
its pre-existing SR-71A.

Serial coverage 222 of 293.

## The Robins top-up

The stub row was **SR-71A 61-7958**, and it is correct — that airframe is
genuinely there — so it was excluded from the top-up rather than flagged. (This
is the opposite of New York's Intrepid stub, which was bogus seed data.)

Two things about this site are worth recording:

- **The museum's own website is effectively gone as a source.** museumofaviation.org
  now serves a 114-byte JavaScript "lander" stub to every client and user-agent
  tried. All 80 of its `/portfolio/` pages had to be harvested from Wayback
  captures dated 2021-2025, which is where roughly 73 museum-stated serials came
  from. Rung 1 of the source hierarchy is not available here.
- **The best currency source was a dated walk-through**: an Oxford Aviation Group
  visit of 15 October 2022 covering all four buildings plus the non-public
  storage and ALC-ramp areas. It caught the MiG-21, MQ-1B 08-3243, OH-58A
  73-21905, T-34A, Pitts and WACO CG-4A that no directory carries.

## Corrections made

At Robins, with evidence:
- **B-1B is 83-0069**, not Aerial Visuals' 86-0098.
- **F-80C is 45-8357** — AV's "54-8357" fails its block check; no FY54 F-80 exists.
- **C-130E is 63-7868**, not 64-0496. **OV-10A is USAF 67-14623**, not USMC.
- **C-45G is 51-11653** — the museum's own "52-11653" is out of block.
- **One airframe, two identities, resolved and recorded once**: C-47 43-49442 is
  the same aircraft as USN R4D-6 BuNo 50811 c/n 15258. Likewise U-2C 56-6682 =
  NASA 709 / N709NA.

Elsewhere:
- **Two false painted serials at Robins' 116th ACW display** — F-4C **63-7559**
  is painted **68-566**, and F-105G **63-8345** is painted **62-4425** (the real
  62-4425 is in Blissfield, Michigan). True identities from Baugher.
- Wikipedia still places F-105G 63-8345 at Dobbins; it moved to Robins in 2020.
  Wikipedia was stale or wrong on two of six Georgia rows checked.
- **Douglasville's F-105D is 61-0164 painted as 59-1746**; silverhawk's
  "64-0164" is not a valid serial.
- **Tallapoosa's site is Helton Howland Memorial Park**, not the "Haralson
  County Veterans Association" directories name.
- Cordele's B-29 is an **RB-29A/F-13A**, and its Fury is **FJ-4B 143557** (= AF-1E).
- **The Museum of Flight has split into two sites** — flying aircraft at Rome
  (by appointment), displays at Paulding County Airport in Dallas GA (Tue-Sat).
  Every directory still says "Rome" only. Two site records written.
- **AHTC Marietta's F-86D 52-3651 has left** for the Museum of Aviation, per
  AHTC's own article.

## Adjudicated conflicts

- **F-84F 51-9507** was claimed by both the Robins museum pass (physically logged
  in the museum storage area at the north end of the ALC ramp on a dated
  walk-through of 15 October 2022) and the bases pass (NMUSAF's April 2016
  custody list, assigning it to 116 MXG/CC). A dated physical sighting beats a
  custody list, so it is recorded with the museum as `in_storage` and removed
  from the 116th ACW display. Note Baugher still says Dobbins — unresolved
  upstream, and worth one call.
- **Aviation History & Technology Center, Marietta** was enumerated by both the
  museums pass and the bases pass, each citing the museum's own aircraft page,
  yet only 5 of 14 rows overlapped. Both lists were merged into one site (22
  rows) rather than either being trusted alone — a useful reminder that a single
  agent reading one page does not exhaust it.
- **The two Cairo VFW Post 8433 entries are NOT duplicates**: a UH-1B kept on a
  trailer at the post grounds, and a UH-1H on a pad in Davis Park about a
  kilometre away, independently confirmed by an OpenStreetMap node. Both kept.

## Collisions against the live database

Two, both H-34s, both imported with a **blank tail_number** and the serial
preserved in aliases because the existing records were better supported:

- **53-4477** is live at the Air Force Flight Test Museum, Edwards CA. The
  Georgia row (a Locust Grove restaurant display) carries a c/n and civil
  registration but cannot outweigh an existing placement on its own.
- **54-2874** is live at the US Army Aviation Museum, Fort Rucker AL. The
  Georgia row derives from aviationmuseum.eu printing "CH-43A" — not a real
  designation — so its serial is inferred, not sourced.

## Tooling findings

- **The FAA bulk registry zip 403s to bare curl** — it needs a browser
  user-agent. Once fetched, `MASTER.txt` × `ACFTREF.txt` gave 488 Georgia
  museum-shaped owners in one sweep. It produced **zero monument sites**,
  though: its Georgia owner hits were flight schools, sheriff aviation and
  drones. Good for museums, useless for posts and parks.
- **Aerial Visuals is alive, and the URL matters.** One pass reported the domain
  parked and dead; three others used it successfully. `Locator.php` and
  `LocationDossier.php` are at the **site root**, not under `/AirframeDossier/`.
  POST `Country=United States&Region=Georgia&Scope=3` returned ~138 Georgia
  locations. Do not let the "dead" report propagate.
- **The US Army display-helicopter loan list does not exist publicly.** TACOM's
  program page publishes no roster (phone 520-706-8680). Wikipedia's UH-1/AH-1
  display lists are the substitute and yielded exactly one Georgia monument.
  This corrects the New York note that treated it as a first-class source.
- **The NMUSAF loan PDF path is fragile.** The bases pass got the whole 30-row
  Georgia block in one call from the 2015 wayback `id_` URL; the monuments pass
  found that same path returning the Wayback HTML wrapper, with the CDX API
  blocked by egress policy. Expect to retry across archive captures.

## Judgment calls

- **CAF Airbase Georgia and the Army Aviation Heritage Foundation are counted**
  as sites even though their airframes are airworthy — both are ticketed public
  museum hangars, which is the test used in earlier states for Old Rhinebeck.
- Replicas recorded and flagged as replicas in `description`; blank registrations
  left blank rather than guessed (CAF's PT-19A, T-34B, LT-6D).
- **Mighty Eighth's B-24J 44-48781 "Rupert the Roo II" is NOT in Pooler** — the
  museum's own page (August 2026) says components are off-site with arrival
  targeted for early spring 2027. No row written.
- Three Robins serials remain unresolved and carry all candidates in aliases:
  PT-22 (41-1987 / 41-1978 / 41-21039), PT-19A (42-2802 / 42-2809 / 42-83633),
  L-5 (42-98184 / 42-98180 / 44-17421).

## Excluded, and why (do not re-research)

- Four phantom Mighty Eighth airframes that directories carry: B-52D 56-0666,
  MiG-21 23+13, Liberator BZ755, Bf 109G.
- The Douglas warbirds (P-40E, SNJ-6, XP-82) have all **left Georgia**, per FAA.
- Robins' 2013 downsizing: 9 airframes transferred, 3 scrapped, 11 departed —
  all named in the pass file. Also the D-21, Bensen X-25A and Mk 53 shape.
- Negative results deliberately reported rather than left ambiguous: Fort Stewart
  / 3rd ID Museum, Hunter AAF, MCLB Albany, Kings Bay, Fort Eisenhower, Clay
  National Guard Center, Lockheed Plant 6, and all six former bases (Turner,
  Chatham, Spence, Souther, Cochran, Bush) yielded no substantiable airframe.
- The 57th Fighter Group restaurant's aircraft are replicas (recorded as such);
  Atlanta Technical College's compound is not public; the McCollum Field F-100
  is a phantom; eight closed museums named.
- **No aircraft is registered to the Museum of Aviation in the FAA database**, and
  nearly every historic N-number its airframes wear (N82446, N32086, N217DB,
  N5585, N842MB, N11HC, N9119) has been re-issued to unrelated aircraft. Those
  markings are not identities — a useful negative.

## Test-suite fixes, and a normaliser worth keeping

Ten failures on first pass, all in three generic patterns, now handled inside
`build_raw.py` so a rebuild cannot revert them:

- aliases with a **leading** "painted as" / "marked" wrapper (the earlier
  normaliser only stripped trailing words like "reported");
- **attribute words** used as aliases — "replica", "reproduction", "mockup" —
  which move into `description` as a flagged statement;
- **placeholder field values** (`-`) in `variant`, which must be blank.

Full suite green at **43,779 tests** before anything was applied.

## Needs a human (ranked)

1. **Museum of Aviation, (478) 926-6870** — closes the three unresolved serials
   above, confirms the new C-47A 43-15200 "Francis L." arrival, and settles
   whether F-84F 51-9507 is museum or 116th ACW. Also worth asking whether the
   collection pages will return; the website being a JS stub makes this museum
   permanently hard to re-verify.
2. **Hawkinsville MGM-1 Mace 52-1872** (478-892-3240) — potentially Georgia's
   only Mace, unconfirmed.
3. **Cordele Titan I 60-3694 and its A-7** (229-276-2371).
4. **South Georgia Technical College** (229-931-2394) — one call closes eleven
   airframe lines at the Griffin B. Bell Aerospace Technology Center.
5. Unidentified but OSM-confirmed airframes at **Kennesaw Aviation Park** and
   **Middle Georgia State University Eastman**.
6. **No imagery currency pass was run.** As in New York, a satellite and Street
   View sweep over the 39 monument sites is the cheapest remaining quality win.
7. 126 of 159 counties produced no records.
