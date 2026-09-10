# France aviation-preservation research brief

You are one of several parallel research agents building out FRANCE for
airplane.museum, a database that answers "where can I go and see this
aircraft". Your output is CSV files plus a notes file, written to the output
directory named in your assignment. Do not touch the live database.

Read this whole brief before starting. Then read
`/home/claude/AirplaneFinder/data/METHODOLOGY.md` (short) for the house rules.

## Current state of France in the database

Two sites, and one of them is already thorough:

| DB name (use verbatim) | recorded now |
|---|---|
| `Musee de l'Air et de l'Espace` (Le Bourget) | **170 aircraft** — live list at /home/claude/fr/lebourget_live.txt |
| `Musee de la Batterie de Merville` | 1 (C-47A 43-15073) — correct, a single airframe |

Everything else in France is greenfield. Do NOT put either of these in a
museums CSV. Le Bourget needs only a **diff** — see the assignment that owns it.

## Scope

Metropolitan France plus Corsica. `country` = `France`, `region` = `Europe`,
`state_province` = the **région** (`Île-de-France`, `Occitanie`,
`Nouvelle-Aquitaine`, `Auvergne-Rhône-Alpes`, `Provence-Alpes-Côte d'Azur`,
`Grand Est`, `Hauts-de-France`, `Normandie`, `Bretagne`, `Pays de la Loire`,
`Centre-Val de Loire`, `Bourgogne-Franche-Comté`, `Corse`). Put the
département in the address. Overseas départements are out of scope; note any
you find as leads.

**Cockpit and nose sections are in scope**, as are visitable private
collections that admit the public by appointment. Say plainly in `description`
when a row is a cockpit or nose section only.

## What counts as a site

**Any place where a real airframe (or cockpit section, missile or rocket) is
preserved and can be seen:**

- Aviation, military, science and general museums holding aircraft.
- **Armée de l'Air et de l'Espace, Aéronavale and ALAT sites**: gate guardians
  (*avion gardien* / *gate guard*), *traditions* displays, base memorials,
  technical-school instructional airframes, and the aircraft parks that several
  bases keep. France has a very large base-display population.
- **Monuments**: aircraft on plinths (*avion sur socle*) at roundabouts, in
  town squares, at aeroclubs, outside écoles and lycées techniques, at
  motorway aires, campsites, restaurants and hotels. Mirage III, Mirage F1,
  Mirage 2000, Super Étendard, Étendard IV, Jaguar, Fouga Magister, Noratlas,
  Vautour, Mystère IV, Super Mystère, F-100, T-33, Alouette II/III, and the
  Breguet Atlantic are the classic French plinth aircraft.
- Airliner heritage and oddities: retired Concordes, Caravelles, Air France
  and Aéropostale relics, aircraft in theme parks and playgrounds.

A single Mirage on a roundabout **is a site record**. Do NOT record: aircraft
in service, airframes inside closed dumps or dismantlers with no public
access, memorial *stèles* with no airframe (aerosteles.net lists thousands of
these — a plaque or a propeller on a pillar is NOT an aircraft record), or
airframes since scrapped (say so in the notes).

## Method

- **`aerosteles.net`** is the reference for French aviation memorials and
  monuments, searchable by département, with photographs and dates. Use it as
  a spine for the monument sweep — **but filter hard**: most of its entries are
  commemorative stèles with no aircraft. Record only entries where a real
  airframe (or a substantial section) stands there.
- **`traditions-air.fr`** covers Armée de l'Air unit heritage and base
  displays; **`anciens-aerodromes.com`** and **`aeroplans`** for airfield
  history; per-base association pages for gate guards.
- **French Wikipedia**: `Liste des musées aéronautiques`, plus per-type
  survivor articles. Treat as leads, verify serials.
- **`abpic.co.uk`, `airhistory.net`, `jetphotos.com`** — dated photographs are
  the best currency evidence; airhistory's "[Off-Airport]" taxonomy suits
  monuments exactly.
- Museums' own collection pages where they publish one (Aeroscopia, Espace Air
  Passion, Montélimar, Savigny, ANAMAN Rochefort, Dax all do).
- French civil registrations are `F-` prefixed (`F-BXXX`, `F-GXXX`,
  `F-WXXX` for prototypes/test, `F-AZXX` for collection aircraft). Military
  serials are plain numbers, often shown with a unit code: Mirage F1 `521`
  coded `30-SB`, Jaguar `A91`, Alouette III `1234`. **Put the serial in
  `tail_number` and the unit code in `aliases`.**

Assume every list is stale. For every airframe ask: **is it still there in
2025-26?** Require evidence of presence, not intent.

## Hard rules

- **Never invent a serial, registration, year, or coordinate.** Blank beats a
  guess. A serial is never a `year_built`.
- **`model` is the BASE designation, variant separate**: `Mirage III` + `E`,
  `Mirage F1` + `C`, `Mirage 2000` + `C`, `Super Étendard` + `M`,
  `Étendard IV` + `M`, `Jaguar` + `A`, `Fouga` + `CM.170`, `Noratlas` + `2501`,
  `Alouette III` + `SA 316B`, `Atlantic` + `ATL1`, `Rafale` + `M`.
  Manufacturer is the maker (`Dassault`, `Dassault-Breguet`, `Sud-Aviation`,
  `Aérospatiale`, `Nord Aviation`, `Morane-Saulnier`, `Potez`, `Breguet`,
  `SNCASE`, `SNCASO`, `Fouga`, `Socata`).
- **An aircraft is in exactly one place.** Resolve conflicts, say how in notes.
- **`aliases` are NAMES only**, semicolon-separated, NO commas, each <=4 words
  and <=34 chars, no verbs: other designations, the dashless form of every
  dashed designation (`F104G`, `T33A`, `CM170` — ALWAYS include it, a test
  enforces it), popular names (`Magister`, `Mystère`), the unit code
  (`30-SB`), the c/n, previous identities, false markings worn. Never
  `replica`, `maquette`, `on loan` — those belong in `description`.
- **`description`**: provenance, section-only status, replica status, markings,
  condition, the date last confirmed present, doubts. 1-3 sentences, English.
- `year_built`: only from a sourced build or delivery date. Usually blank.
- `display_status`: `on_display` | `in_storage` | `under_restoration`.
- Keep French site names as the site writes them, with accents:
  `Musée européen de l'Aviation de Chasse`, `Espace Air Passion`.

## CSV formats (exact headers)

Museums file, one per assignment, named `fr_museums.csv`:

```
name,city,state_province,country,postal_code,region,address,website,access_type,latitude,longitude
```

- `postal_code`: five-digit French code postal — fill it wherever you have it.
- `name` must be unique across the whole database; monument sites need the
  place in the name: `Mirage III Monument, Dijon`,
  `Base Aérienne 118 Mont-de-Marsan Gate Guards`.
- `access_type`: `public` | `appointment` | `restricted` (inside a military
  gate). A gate guardian visible from a public road is `public`.
- `latitude,longitude` decimal degrees, the airframe's position if known;
  blank if unknown — NEVER guess. A correct code postal beats a guessed pin.

Aircraft — **ONE FILE PER SITE**, `<slug>_aircraft.csv` (ASCII slug), every row
carrying the same `museum_name`, matching the museums file (or the DB name for
a top-up) character for character:

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
  artillery_rocket, anti_tank, anti_ship`.
- Two untailed rows of the same type at one site must be distinguishable.
- Write with python's `csv` module, `lineterminator="\n"`, UTF-8.

## Notes file

`FR_<AREA>_NOTES.md`: sources and their weight (which list proved stale, how
you know); corrections made with evidence; judgment calls (replicas, sections,
airworthy aircraft, access types); **excluded and why** — NAME them, and say
explicitly how many aerosteles entries you rejected as plaques-without-aircraft;
blank fields left deliberately; ranked "needs a human on site" questions; a
file/row-count table with serial coverage; and **"Leads for other agents"**.

## Effort

France is a top-five preservation country: the big museums hold 40-150
airframes each and the plinth population runs to several hundred. Be thorough.
Capture whole published collections. Serial coverage should be high.

Finish by listing: output directory, files written, site count, aircraft
count, rows with tail numbers, and the top 5 open questions.
