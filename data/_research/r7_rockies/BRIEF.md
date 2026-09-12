# Research brief — the Northern Rockies and Alaska preserved-aircraft sweep (airplane.museum database)

You are researching preserved/displayed aircraft in Montana, Wyoming and Alaska for a public database
that answers "where can I go and see this airframe". Today is September 2026.
All three states are GREENFIELD - zero records exist.

## What counts as a record
Any deliberately-retained, publicly-presented aircraft, helicopter, missile/rocket
or spacecraft: museums, base air parks, gate guards, VFW/American Legion post
displays, city park plinths, airport displays, school/college campus displays,
restaurants, rooftops. **A single F-4 in front of a VFW post IS a site record.**
Do NOT record: operational aircraft (police, ag, aero club, airworthy private
warbirds merely based at a field), scrap/derelict hulks, closed museums, aircraft
that have left. Record replicas only when clearly flagged as a replica in
`description` (never in `aliases`).

## Stale-data discipline
Aviation directories are compiled once and never revisited. Assume every claim is
stale until a 2023-2026 source confirms it. Ask "is it still there in 2025-26?"
for every airframe, and state the currency evidence and its date in `description`.

## Source hierarchy and known mechanics (READ THIS — it saves hours)
1. **The museum's own current collection pages.** Authoritative on presence,
   frequently WRONG on serials (construction numbers land in the serial field).
2. **The FAA bulk registry.** The owner-name WEB search is BROKEN (every query
   302s to "Name has unsupported characters"). Download
   `https://registry.faa.gov/database/ReleasableAircraft.zip` — **it 403s to bare
   curl, so send a browser User-Agent** — then join `MASTER.txt` to `ACFTREF.txt`
   locally and filter by state and owner name. Excellent for museums; it finds
   almost no monument sites, because posts and parks do not register aircraft.
3. **Joe Baugher** serial pages for USAF/USN identity and disposition. Broken
   years via the crouze.com mirror or `web.archive.org/web/2023id_/`.
4. **Aerial Visuals.** ALIVE, but `Locator.php` and `LocationDossier.php` are at
   the **site root**. POST `Country=United States&Region=<State>&Scope=3` (GET is
   broken). Gives per-location serials, c/ns and arc-second fixes. Vintage
   ~2008-2015: an identity source, never a currency source.
5. **OpenStreetMap** `historic=aircraft` / `memorial=aircraft` nodes via
   `https://overpass.private.coffee/api/interpreter` (the main API is
   proxy-blocked; POST the query; plain tag queries work, regex ones time out).
   The extract is current, so this is the currency counterweight to Aerial Visuals.
6. **HMdb** — `results.asp?Search=Place&Town=<town>&State=<State>` (WebFetch only,
   Cloudflare blocks curl). Exact coordinates, photos, a dated catalogue stamp and
   often the serial in the inscription. County listings paginate at 100 and a
   page-1 summary silently hides markers, so page through.
7. **NMUSAF "Aircraft on Loan by Location"** (April 2016). The live URL 403s to
   curl and WebFetch truncates; only `web.archive.org/web/20150925041956id_/`
   reliably serves a real PDF. Authoritative on custody, useless on currency.
8. Wikipedia survivor lists; dated local news; ABPic and dated visitor photos.
**aviationmuseum.eu and silverhawkauthor are LEAD LISTS ONLY** — their tables are
column-shifted in every state checked so far. Re-anchor every serial or drop it.
Never use Grokipedia.

## Hard rules
- **NEVER invent a serial, registration, year_built or coordinate.** A blank is
  the correct answer. Do not "fix" a serial that fails a block check by changing
  a digit — that has produced real errors in this project.
- A fiscal-year prefix is NEVER `year_built`. Populate it only from a sourced
  construction/delivery/acceptance date or an FAA `YEAR-MFR`.
- **Production-block-check every serial** and flag failures in the row.
- Painted markings are not identity. Record the true identity in `tail_number`
  and the painted number in `aliases`, with the evidence in `description`.
- An aircraft is in exactly one place. Flag anything two sites both claim.
- Record where an aircraft IS, not who owns it. A museum's own list can include
  airframes physically out on loan elsewhere — check.
- `model` = BASE designation, variant separate: F-4|E, T-33|A, UH-1|H, RF-4|C.
- Q-designated drones are `fixed_wing`. F-105G is `electronic_warfare`.
- `wing_type` only for fixed_wing. `aircraft_type`: fixed_wing | rotary_wing |
  lighter_than_air | spacecraft | missile_rocket. `military_civilian`:
  military | civilian. `display_status`: on_display | in_storage | under_restoration.
- `role_type` from: fighter, trainer, private, experimental, utility,
  ground_attack, recon, transport, bomber, test, commercial_transport, drone,
  search_rescue, other, space, electronic_warfare, air_to_surface, cruise,
  ballistic, tanker, surface_to_air, sounding, air_to_air, freighter,
  launch_vehicle, artillery_rocket, anti_tank, anti_ship.
- `aliases` = other NAMES only, semicolon-separated, **NO commas**: alternate
  designations, popular names, `c/n 1234`, BuNo, painted false serials, tail
  codes. Never prose, never attributes like "replica", nothing over ~26 chars.
- `description` = prose, **NO commas** (use semicolons/dashes), under ~60 words.

## Output contract — AIRCRAFT (pipe-delimited, exactly 14 fields, one per line)
manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status

## Output contract — SITES (pipe-delimited, 11 fields)
name|city|state_province|country|postal_code|region|address|website|access_type|latitude|longitude

- country = United States ; region = North America ; state_province = the full
  state name.
- access_type: public (walk-up or ticketed) | appointment | restricted (behind a
  controlled/military gate).
- Monument-class sites get a `-- <City>` suffix, e.g. `VFW Post 2952 -- Searcy`;
  post numbers repeat across states.
- Coordinates: prefer a fix on the airframe (OSM node, HMdb marker, Aerial
  Visuals map, satellite), then a geocoded street address, then the airport
  reference point. Say which in the notes. **A blank beats a wrong fix.**

## CRITICAL — group your aircraft under site headings
Put each site's aircraft under a markdown heading whose text is the site's name
EXACTLY as it appears in your SITES block. The reconciler matches on that.

## Deliverable
Write the complete file to the path given in your task: the SITES block, then
AIRCRAFT blocks under per-site headings, then NOTES (sources and their weight;
corrections with evidence; judgment calls; EXCLUDED sites/airframes with reasons,
named so nobody re-researches them; deliberately blank fields; ranked open
questions with phone numbers where one call would close several).
If you run low on search budget, WRITE WHAT YOU HAVE TO THE FILE BEFORE STOPPING
and say what was not reached.
