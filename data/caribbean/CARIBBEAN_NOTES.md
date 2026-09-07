# Caribbean — build notes

A region sweep, like California. Enumerate first, verify each museum is open
and displays real aircraft, then museum records, then aircraft.

The headline: **the Caribbean is thin.** Six museums qualify, holding 19
aircraft between them, and the enumeration excluded as many museums as it
kept. Most of the region's notable airframes sit either on active air bases
or in museums that have closed.

## Files

| File | Museum | Rows | Tails |
|---|---|---|---|
| `caribbean_museums.csv` | 6 museum records | — | — |
| `parque_museo_aeronautico_de_la_fard_aircraft.csv` | Parque Museo Aeronáutico de la FARD, Santo Domingo | 12 | 11 |
| `museo_giron_aircraft.csv` | Museo Girón, Playa Girón, Cuba | 1 | 1 |
| `jamaica_military_museum_and_library_aircraft.csv` | Kingston | 1 | 0 |
| `chaguaramas_military_history_and_aerospa_aircraft.csv` | Trinidad | 4 | 3 |
| `museo_del_nino_de_carolina_aircraft.csv` | Carolina, Puerto Rico | 1 | 1 |
| `caribbean_raw.txt` | research output, kept for audit | — | — |

**Borinquen Field/Ramey AFB Museum** (Aguadilla, PR) has a museum record but
no aircraft file. It is open, but its one airframe — a Beechcraft D-50 Twin
Bonanza N10AM — was at the site destroyed by Hurricane María in 2017, and the
museum's current pages describe only artefacts. Presence today could not be
confirmed, so nothing is claimed. The museum still shows up in nearest-museum
searches, which is right: it exists and can be visited.

Region is recorded as **North America**, which is where the UN geoscheme and
the schema's own enum put the Caribbean. There is no "Caribbean" region value.

## Museum names

Recorded as each museum styles itself. **Museo Girón** is the Bay of Pigs
museum; **Parque Museo Aeronáutico de la FARD** is the Dominican Air Force
Aeronautical Museum Park; **Museo del Niño de Carolina** is the Carolina
Children's Museum. The file names are ASCII slugs of these.

## Access

Two are on active military bases. The FARD park is inside Base Aérea de San
Isidro (photo ID, checkpoint; public entry confirmed by recent reviews). The
Jamaica Military Museum is inside Up Park Camp, a JDF base — entry via the
guardhouse, weekdays.

## Judgment calls

- **Museo del Niño de Carolina is a children's museum, not an aviation
  museum.** It's included because it displays a real, complete ex-American
  Airlines MD-82 (N292AA, cockpit accessible) as a formal exhibit — which is
  the test, rather than what the museum calls itself.
- **The FARD's AT-6D wears "1031" as a display serial**; its true identity is
  possibly 1054. Recorded as displayed, with the caveat in aliases. Its
  Dauphin's serial was corrected to 3022 — one source had printed 1031 for it
  too, an obvious transcription error since that duplicated the AT-6.
- **The FARD's Poliplano is a replica** of Zoilo Hermógenes García's 1911
  three-winged aircraft, the first built in the Dominican Republic. Recorded
  as a triplane, civilian, experimental, with the manufacturer as the
  designer since there was no company.
- **The Jamaican UH-1H has no tail number.** The JDF fleet was H-19 to H-22
  and the museum's pole-mounted airframe couldn't be matched to one. Left
  blank rather than guessed.
- **Chaguaramas' 747 is excluded.** Visitors describe a stripped, abandoned
  fuselage; no registration, operator or msn could be found. It is not a
  recognisable airframe. The Gazelle's serial "NS1" is low confidence.
- Registry-sourced identifiers: N292AA (MD-82), 9Y-TGN's 1980 build year and
  msn, and the FARD serials 1611, 1702, 3403, 1544, 3016, 3004 — all from
  aviationmuseum.eu rather than the museum itself.

## Excluded — do not re-research

- **Museo del Aire, Havana** — closed August 2010; the collection moved to
  San Antonio de los Baños Air Base. Cuban tourism pages still describe it in
  the present tense, but that is recycled pre-2010 copy.
- **San Antonio de los Baños Air Base** — holds the ex-Museo del Aire aircraft
  (An-2, An-26, MiG-15bis, two MiG-23UB, MiG-29, Mi-4, Mi-8) on an active
  base with no public access. Not a museum.
- **Museo de la Revolución / Granma Memorial, Havana** — holds Sea Fury FB.11
  "542" and an OS2U-3 Kingfisher, but the building has been closed for
  renovation since ~2021 and the memorial is marked permanently closed. Too
  ambiguous to list; worth revisiting if it reopens.
- **Barbados Concorde Experience** — closed to the public since 2010. Concorde
  G-BOAE is still in the hangar, which is now a secure cruise-ship departure
  terminal. Reopening has been promised repeatedly and not happened.
- **Puerto Rico National Guard Museum, Camp Santiago** — holds six airframes
  (AH-1G, OH-13E, UH-1H, C-7A, F-16A 80-0612, A-7D 74-1760) but is marked
  permanently closed and access is limited to Guard members. The best
  candidate to add if it reopens.
- **Museo Aeronautiko Curaçao** — real and open by appointment, but models
  and photographs only. No full-size aircraft.
- Nothing qualifying in Haiti, the Bahamas, Cayman, Aruba, Bonaire, Sint
  Maarten, Guadeloupe, Martinique, Antigua, St Kitts, St Lucia, Grenada,
  Dominica, St Vincent, the Virgin Islands, or Turks and Caicos.
- **Bermuda** is North Atlantic, not Caribbean, and has no aviation museum.
