# Germany aviation-preservation research brief

You are one of several parallel research agents building out GERMANY for
airplane.museum, a database that answers "where can I go and see this
aircraft". Your output is CSV files plus a notes file, written to the output
directory named in your assignment. Do not touch the live database.

Read this whole brief before starting. Then read
`/home/claude/AirplaneFinder/data/METHODOLOGY.md` (short) for the house rules.

## Current state of Germany in the database

**One site, one aircraft.** `Deutsches Museum Flugwerft Schleissheim`
(Oberschleissheim) is recorded with a single Bf 109 G. If your assignment
covers it, produce a **top-up file** whose `museum_name` is exactly
`Deutsches Museum Flugwerft Schleissheim`, listing every other airframe, and
do NOT add it to a museums CSV. Everything else in Germany is greenfield.

## Scope

Germany only (all 16 Bundesländer). `country` = `Germany`, `region` = `Europe`,
`state_province` = the Bundesland in German (`Bayern`, `Baden-Württemberg`,
`Nordrhein-Westfalen`, `Niedersachsen`, `Hessen`, `Sachsen`, `Brandenburg`,
`Berlin`, `Mecklenburg-Vorpommern`, `Sachsen-Anhalt`, `Thüringen`,
`Rheinland-Pfalz`, `Saarland`, `Schleswig-Holstein`, `Hamburg`, `Bremen`).

**Cockpit and nose sections are in scope**, as are visitable private
collections that admit the public by appointment. Record the section as its own
row and say plainly in `description` that it is a cockpit or nose section.

## What counts as a site

**Any place where a real airframe (or cockpit section, missile or rocket) is
preserved and can be seen.** That includes:

- Aviation, military, technology and general museums holding aircraft.
- Luftwaffe / Marineflieger / Heeresflieger sites: gate guardians
  (*Torwächter*), *Traditionsräume* and *Luftwaffenmuseum* satellite displays,
  technical-school instructional airframes, and airfield memorials.
- **The ex-NVA and ex-Soviet population**, which is enormous and specific to
  Germany: MiG-21, MiG-23, MiG-17, Su-22, L-39, Mi-2/Mi-4/Mi-8/Mi-24, An-2,
  Il-14, Tu-134, Let L-410 and Zlin airframes scattered across the eastern
  Länder in *Technikmuseen*, on plinths, in playgrounds, at car dealerships,
  in beer gardens and at *Ferienpark* sites. Many were sold off cheaply after
  1990 and moved repeatedly — currency matters more here than anywhere.
- Monuments and oddities: aircraft on poles, motorway-services displays,
  hotel/restaurant/discotheque aircraft, playground airframes, driving-school
  and fire-training airframes that are displayed, aircraft on buildings.
- Airliner heritage: Lufthansa Technik and the Lufthansa Traditionsflug fleet,
  the Super Constellation, retired 747s/A340s at museums and airports.

A single MiG-21 on a plinth in a village **is a site record**. Do NOT record:
aircraft in active service, airframes inside closed scrapyards or dismantlers
with no public access, or aircraft that have been exported or scrapped (say so
in the notes instead).

## Method

- **Wikipedia (German) is unusually good here.** Start from
  `Liste von Luftfahrtmuseen`, `Liste der Militärmuseen in Deutschland`, and
  the per-type survivor articles. German Wikipedia articles on individual
  airframes often carry the *Werknummer* and current location.
- **`abpic.co.uk`, `airhistory.net`, `jetphotos.com`, `planespotters.net`** —
  dated photographs are the best currency evidence.
- **`aerialvisuals.ca`** dossiers; **`flugzeug-lorenz.de`**, **`ostflug`- and
  NVA-heritage sites**, **`Interessengemeinschaft`** and *Traditionsverein*
  pages for eastern airframes; `luftfahrtmuseum.com` listings as leads only.
- **The Luftwaffenmuseum der Bundeswehr (Berlin-Gatow)** publishes its own
  collection; use it directly.
- German registration is `D-` prefixed (`D-ABCD` airliners, `D-EABC` light
  aircraft, `D-HXXX` helicopters, `D-Kxxx` motorgliders). Bundeswehr serials
  are the five-digit *Taktisches Kennzeichen* written with a plus:
  `98+59`, `22+35`, `JA+111`. **Record the Bundeswehr code in `tail_number`
  exactly as displayed, with the plus sign**, and put the Werknummer, the
  ex-NVA number, the ex-Soviet bort number and any civil registration in
  `aliases`.
- NVA aircraft carry four-digit tactical numbers (`577`, `814`) and were often
  re-coded on transfer to the Bundeswehr in 1990 — say in `description` which
  identity is displayed.

Assume every list is stale. For every airframe ask: **is it still there in
2025-26?** Require evidence of presence, not intent.

## Hard rules

- **Never invent a serial, registration, year, or coordinate.** Blank beats a
  guess. A serial is never a `year_built`.
- **`model` is the BASE designation, variant separate**: `MiG-21` + `SPS`,
  `MiG-23` + `MF`, `Su-22` + `M4`, `F-104` + `G`, `F-4` + `F`, `Bf 109` + `G-6`,
  `Do 27` + `A-4`, `Mi-8` + `T`, `Tornado` + `IDS`, `Alpha Jet` + `A`,
  `Transall` + `C-160`, `Sea King` + `Mk 41`. Manufacturer is the maker
  (`Mikoyan-Gurevich`, `Sukhoi`, `Messerschmitt`, `Dornier`, `Heinkel`,
  `Junkers`, `Focke-Wulf`, `VEB Flugzeugwerke Dresden`, `Let`, `PZL-Mielec`,
  `MBB`, `Dassault-Breguet/Dornier`, `Panavia`).
- **An aircraft is in exactly one place.** Resolve conflicts, say how in notes.
- **`aliases` are NAMES only**, semicolon-separated, NO commas, each <=4 words
  and <=34 chars, no verbs: other designations, the dashless form of every
  dashed designation (`MiG21`, `F104G`, `Su22` — ALWAYS include it, a test
  enforces it), NATO reporting names (`Fishbed`, `Flogger`, `Hip`), the
  Werknummer (`Wnr 163824`), ex-identities, false markings worn. Never
  `replica`, `Nachbau`, `on loan` — those belong in `description`.
- **`description`**: provenance, cockpit-section status, replica status,
  markings, condition, the date last confirmed present, doubts. 1-3 sentences,
  in English.
- `year_built`: only from a sourced build or delivery date. Usually blank.
- `display_status`: `on_display` | `in_storage` | `under_restoration`.
- Write site and museum names in German as the site writes them
  (`Luftwaffenmuseum der Bundeswehr`, `Technik Museum Speyer`,
  `Militärhistorisches Museum Flugplatz Berlin-Gatow`), keeping umlauts.

## CSV formats (exact headers)

Museums file, one per assignment, named `de_museums.csv`:

```
name,city,state_province,country,postal_code,region,address,website,access_type,latitude,longitude
```

- `postal_code`: German PLZ, five digits — fill it wherever you have it, it
  geocodes precisely.
- `name` must be unique across the whole database. Monument and gate-guard
  sites need the place in the name: `MiG-21 Denkmal, Cottbus`,
  `Fliegerhorst Wittmund Torwächter`.
- `access_type`: `public` | `appointment` | `restricted` (inside a military
  gate). A gate guardian visible from a public road is `public`.
- `latitude,longitude` decimal degrees, the airframe's position if known;
  blank if unknown — NEVER guess. A correct PLZ beats a guessed pin.

Aircraft — **ONE FILE PER SITE**, `<slug>_aircraft.csv` (ASCII slug), every row
carrying the same `museum_name`, matching the museums file (or the DB name for
the Schleissheim top-up) character for character:

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

`DE_<AREA>_NOTES.md`: sources and their weight (which list proved stale, how
you know); corrections made with evidence; judgment calls (replicas, cockpit
sections, airworthy aircraft, access types); **excluded and why** — NAME them;
blank fields left deliberately; ranked "needs a human on site" questions; a
file/row-count table with serial coverage; and **"Leads for other agents"**.

## Effort

Germany is one of the densest preservation countries in Europe: the big
museums hold 40-150 airframes each and the ex-NVA plinth population runs to
hundreds. Be thorough. Capture whole published collections. Serial coverage
should be high — German practice displays the code.

Finish by listing: output directory, files written, site count, aircraft
count, rows with tail numbers, and the top 5 open questions.
