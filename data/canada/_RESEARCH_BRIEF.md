# Canada aviation-preservation research brief

You are one of several parallel research agents building out CANADA for
airplane.museum, a database that answers "where can I go and see this
aircraft". Your output is CSV files plus a notes file, written to the output
directory named in your assignment. Do not touch the live database.

Read this whole brief before starting. Then read
`/home/claude/AirplaneFinder/data/METHODOLOGY.md` (short) for the house rules.

## Current state of Canada in the database

**One site, two aircraft.** `Canada Aviation and Space Museum` (Ottawa) is
recorded with only a Lancaster B.X KB726 and a Mosquito B.35, against a real
collection of roughly 130 airframes. If your assignment covers it, produce a
**top-up file** whose `museum_name` is exactly `Canada Aviation and Space
Museum`, listing every other airframe, and do NOT add it to a museums CSV.
Everything else in Canada is greenfield.

## Scope

All ten provinces and three territories. `country` = `Canada`,
`region` = `North America`, `state_province` = the province or territory in
full (`Ontario`, `Quebec`, `British Columbia`, `Alberta`, `Saskatchewan`,
`Manitoba`, `Nova Scotia`, `New Brunswick`, `Prince Edward Island`,
`Newfoundland and Labrador`, `Yukon`, `Northwest Territories`, `Nunavut`).

**Cockpit and nose sections are in scope**, as are visitable private
collections that admit the public by appointment. Say plainly in `description`
when a row is a cockpit or nose section only.

## What counts as a site

**Any place where a real airframe (or cockpit section, missile or rocket) is
preserved and can be seen:**

- Aviation, military, science and general museums holding aircraft.
- **Canadian Armed Forces sites**: wing and base gate guardians, heritage air
  parks, memorial airframes, technical-training airframes. Nearly every RCAF
  wing has an air park or at least a gate guardian.
- **Monuments**, which Canada has in unusual density: aircraft on pedestals
  outside Royal Canadian Legion branches, in municipal parks, at cenotaphs, at
  airport entrances, in "air parks" and on highway pull-offs. The classic
  Canadian plinth aircraft are the **CF-100 Canuck, CF-101 Voodoo, CF-104
  Starfighter, CF-5/CF-116 Freedom Fighter, T-33/CT-133 Silver Star, Sabre,
  CT-114 Tutor, Harvard, CP-107 Argus, CP-121 Tracker, Dakota, and the
  CIM-10 Bomarc missile**.
- Bush-flying and float-plane heritage, which is a Canadian speciality: Beaver,
  Otter, Norseman, Fairchild and Junkers airframes preserved in northern
  communities, sometimes on poles or pedestals in town centres.
- Airliner heritage and oddities: retired airframes at airports, aircraft in
  restaurants, playgrounds, campgrounds and on farms.

A single CF-101 on a pedestal outside a Legion branch **is a site record**. Do
NOT record: aircraft in service, airframes in closed storage or dismantlers
with no public access, or aircraft since scrapped (say so in the notes).

## Method

- **`rwrwalker.ca` — Canadian Military Aircraft Serial Numbers — is your
  spine.** It carries a per-serial disposition history for every RCAF/CAF
  airframe, and for preserved aircraft it names the location, often with a
  date. Work through it by type for the plinth types listed above. This is the
  single most valuable Canadian source and it is structured by serial.
- **`aerialvisuals.ca`** is Canadian-run and unusually strong on Canada:
  per-airframe dossiers with mapped display coordinates. Query
  `aerialvisuals.ca/Airframes.php?Seeds=<serial>`; its Locator pages list
  airframes by site.
- **`pinetreeline.org`** for former radar-station and Cold War sites, and the
  Bomarc missiles.
- Museums' own collection pages — most Canadian museums publish one.
- **Wikipedia**: `List of aerospace museums in Canada`, plus the survivor
  articles (`List of surviving Avro Canada CF-100 Canucks`,
  `Surviving McDonnell CF-101 Voodoos`, CF-104, CT-133, Sabre, Argus). Leads,
  error-prone on individual serials.
- **`abpic.co.uk`, `jetphotos.com`, `airliners.net`, Flickr** — dated
  photographs are the best currency evidence. (Note: airhistory.net is blocked
  from this environment; do not waste calls on it.)
- **Transport Canada's Civil Aircraft Register** (`wwwapps.tc.gc.ca/saf-sec-sur/2/ccarcs-riacc/`)
  for `C-F` / `C-G` civil registrations and their status.
- Canadian military serials are five-digit (`18393` Sabre, `100504` CF-104,
  `101006` CF-101, `133358` T-33), sometimes shown with the last three digits
  as a tail code. **Put the full serial in `tail_number`** and the code, the
  civil registration and any false marking in `aliases`.

Assume every list is stale. For every airframe ask: **is it still there in
2025-26?** Canadian plinth aircraft are often repainted into another unit's
markings — record the true identity in `tail_number` and the marking in
`aliases`.

## Hard rules

- **Never invent a serial, registration, year, or coordinate.** Blank beats a
  guess. A serial is never a `year_built`.
- **`model` is the BASE designation, variant separate**: `CF-100` + `Mk 5`,
  `CF-101` + `B`, `CF-104` + `D`, `CF-5` + `A`, `CT-133` + `Silver Star 3`,
  `CT-114` + `Tutor`, `CP-107` + `Argus 2`, `CH-113` + `Labrador`,
  `DHC-2` + `Beaver`, `DHC-3` + `Otter`, `F-86` + `Mk 5`. Manufacturer is the
  maker (`Avro Canada`, `Canadair`, `de Havilland Canada`, `Canadian Vickers`,
  `Noorduyn`, `Fleet`, `Bombardier`, `McDonnell`, `Lockheed`).
- **An aircraft is in exactly one place.** Resolve conflicts, say how in notes.
- **`aliases` are NAMES only**, semicolon-separated, NO commas, each <=4 words
  and <=34 chars, no verbs: other designations, the dashless form of every
  dashed designation (`CF100`, `CF104`, `CT133` — ALWAYS include it, a test
  enforces it), popular names (`Canuck`, `Voodoo`, `Silver Star`), the civil
  registration, previous serials, false markings worn. Never `replica`,
  `on loan`, `airworthy` — those belong in `description`.
- **`description`**: provenance, section-only status, replica status, markings,
  condition, the date last confirmed present, doubts. 1-3 sentences.
- `year_built`: only from a sourced build or delivery date. Usually blank.
- `display_status`: `on_display` | `in_storage` | `under_restoration`.
- Keep French Quebec site names as written, with accents
  (`Musée de l'aviation de Montréal`).

## CSV formats (exact headers)

Museums file, one per assignment, named `ca_museums.csv`:

```
name,city,state_province,country,postal_code,region,address,website,access_type,latitude,longitude
```

- `region` = `North America`. `postal_code`: Canadian postal code (`K1K 2X5`)
  where you have it.
- `name` must be unique across the whole database. Legion and monument sites
  need the place in the name: `Royal Canadian Legion Branch 63 CF-101 Voodoo,
  Bagotville`, `Cold Lake Air Force Museum Air Park`. **Legion branch numbers
  repeat across the country** — always qualify with the town.
- `access_type`: `public` | `appointment` | `restricted` (inside a base gate).
  A gate guardian visible from a public road is `public`.
- `latitude,longitude` decimal degrees, the airframe's position if known;
  blank if unknown — NEVER guess. A correct postal code beats a guessed pin.

Aircraft — **ONE FILE PER SITE**, `<slug>_aircraft.csv` (ASCII slug), every row
carrying the same `museum_name`, matching the museums file (or the DB name for
the Ottawa top-up) character for character:

```
manufacturer,model,variant,tail_number,model_name,aircraft_name,aircraft_type,wing_type,military_civilian,role_type,year_built,description,aliases,museum_name,display_status
```

- `aircraft_type`: `fixed_wing` | `rotary_wing` | `lighter_than_air` |
  `spacecraft` | `missile_rocket`.
- `wing_type`: `monoplane` | `biplane` | `triplane` — fixed_wing ONLY and
  required for fixed_wing; blank otherwise.
- `military_civilian`: `military` | `civilian`.
- `role_type` from EXACTLY this vocabulary: `fighter, trainer, private,
  experimental, utility, ground_attack, recon, transport, bomber, test,
  commercial_transport, drone, search_rescue, other, space,
  electronic_warfare, air_to_surface, cruise, ballistic, tanker,
  surface_to_air, sounding, air_to_air, freighter, launch_vehicle,
  artillery_rocket, anti_tank, anti_ship`. Bomarc is `surface_to_air`.
- Two untailed rows of the same type at one site must be distinguishable.
- Write with python's `csv` module, `lineterminator="\n"`, UTF-8.

## Notes file

`CA_<AREA>_NOTES.md`: sources and their weight (which list proved stale, how
you know); corrections made with evidence; judgment calls (replicas, sections,
airworthy aircraft, access types); **excluded and why** — NAME them; blank
fields left deliberately; ranked "needs a human on site" questions; a
file/row-count table with serial coverage; and **"Leads for other agents"**.

## Effort

Canada is a top-ten preservation country with a very large plinth population
for its size. Be thorough. Capture whole published collections. Serial coverage
should be high — rwrwalker.ca is organised by serial, so use it to fill them.

Finish by listing: output directory, files written, site count, aircraft
count, rows with tail numbers, and the top 5 open questions.
