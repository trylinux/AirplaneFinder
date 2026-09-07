# Washington — The Museum of Flight

Museum id 24. Boeing Field, Seattle, WA.

| File | Rows | Tails |
|---|---|---|
| `museum_of_flight_raw.txt` | — | research output, kept for audit |
| `museum_of_flight_aircraft.csv` | 108 | 80 (74%) |

Source of record: the museum's own per-aircraft "Specs" panels on
`museumofflight.org`. **No registry identifiers were needed.** Its WordPress
REST endpoint exists but does not expose an aircraft post type, so this was
page-level research rather than a feed like Pima's.

## Offsite aircraft are not on display here

The museum's Restoration Center & Reserve Collection is at **Paine Field,
Everett** — a different airport from Boeing Field. Each aircraft page states
its own "Museum Location", so this is the museum's own answer rather than an
inference. Recorded `under_restoration`: Bowers Fly Baby prototype, Bowlus
BA-100, Cessna O-2A, de Havilland Comet 4C, Fokker D.VII, Goodyear F2G-1,
Learjet 23, Letov LF-107, Lockheed JetStar, Piasecki H-21B, Taylorcraft Model
A, Rutan VariViggen. The Howard DGA-15P is `in_storage` awaiting restoration.

## Judgment calls

- **"Iron Annie" removed from the Beechcraft C-45H.** That is the Junkers Ju
  52's nickname and nothing ties it to a C-45 — almost certainly contamination
  from another record. Caught by the pre-import audit.
- **Alexander Eaglerock** is on loan to Seattle-Tacoma International Airport,
  so it is not physically on the Boeing Field campus. Kept as `on_display`
  with the loan noted, because a visitor can still see it — but flagged, since
  it arguably belongs to a different location entirely.
- **Excluded:** the Rutan Voyager replica, which the museum's own page says is
  on loan to Sea-Tac and therefore displayed at neither campus.
- **Reproductions, flagged in aliases:** Albatros D.Va, Boeing B&W, Boeing
  Model 40B, Chanute-Herring glider, Curtiss JN-4D, all four Fokkers
  (D.VII, D.VIII, Dr.I, E.III), Lilienthal glider, Gee Bee Z, Nieuport 24bis
  and 27, SPAD XIII, Sopwith Triplane and Camel, S.E.5a, Stinson Model O,
  Nakajima Ki-43, and the Mercury capsule.
- **Fieseler Fi 103** is the V-1 flying bomb — typed `missile_rocket`, not a
  piloted aircraft. Consistent with how Pima's Fritz X and the NMUSAF JB-2
  Loon are filed.
- On loan **to** this museum and recorded here, because that is where a
  visitor finds them: the F-4C from NMUSAF, the ex-Blue Angels F/A-18A from
  Pensacola, and the Spitfire Mk.IX from the Apex Foundation.
- The Messerschmitt Bf 109E-3 is a composite airframe incorporating Hispano
  HA-1112 components; noted in aliases.

## Uncertain, flagged rather than guessed

- **Nieuport 28 tail "14"** reads like a squadron side-number rather than a
  serial. It is what the museum publishes.
- **Lockheed D-21B "90-0510"** — the museum's own page pairs a 1990-style
  fiscal-year serial with a 1964 build year, which is internally inconsistent.
  Recorded verbatim rather than corrected.
- **Lockheed F-104C "N56-934"** — a non-standard N-prefix on a USAF serial.
  Moved to aliases; the tail is left blank.
- **Northrop YF-5A 59-4987** — the audit suspects this N-156F prototype may be
  at Edwards rather than Seattle. Unresolved.
- **North American P-51D 44-72423** — the museum describes this identity only
  as "likely". Recorded with that caveat in aliases.
- **SPACEHAB Destiny mock-up** — the ISS Destiny module was built by Boeing;
  SPACEHAB may have built only this training mock-up. Recorded as the museum
  states, `in_storage` since the museum says it is no longer exhibited.

---

# Washington — the rest of the state

The Museum of Flight (above) was done as part of the world's-largest batch.
This is the state sweep: enumerate, verify open, museum records, aircraft.

| File | Museum | Rows | Tails |
|---|---|---|---|
| `wa_museums.csv` | 11 new museum records | — | — |
| `flying_heritage_combat_armor_museum_aircraft.csv` | FHCAM, Paine Field | 29 | 24 |
| `heritage_flight_museum_aircraft.csv` | Burlington | 21 | 10 |
| `port_townsend_aero_museum_aircraft.csv` | Port Townsend | 23 | 6 |
| `mcchord_air_museum_aircraft.csv` | JBLM | 18 | 18 |
| `olympic_flight_museum_aircraft.csv` | Olympia | 8 | 4 |
| `pearson_air_museum_aircraft.csv` | Vancouver | 6 | 0 |
| five one-or-two-row files | PNWNAM, McAllister, Chehalis, Lewis, Future of Flight | 7 | 3 |
| `wa_rest_raw.txt` | research output, kept for audit | — | — |

112 aircraft. Zero collisions against live data or the Museum of Flight file.

## Access

McChord Air Museum is inside JBLM/McChord Field: non-DoD visitors need a base
visitor pass, and the site currently bars foreign nationals. The Lewis Army
Museum is on JBLM Lewis Main but reachable without a pass — park outside the
gate and phone for an escort.

## Excluded — do not re-research

- **Historic Flight Foundation** (Felts Field, Spokane) — closed; aircraft sold
  off by 2024 to settle the founder's debts.
- **Honor Point Military & Aerospace Museum** (Spokane Valley) — vacated its
  building, searching for a new site, nothing on display.
- **North Cascades Vintage Aircraft Museum** (Concrete) — closed 2018; eight
  of its aircraft went to Port Townsend and are in that file.
- **Fairchild AFB Heritage Airpark** — inside the wire, public access only at
  SkyFest. Not a museum.
- **Washington National Guard Museum / Camp Murray** (an F-101B outside) —
  appointment-only on a state military reservation.
- **Wenatchee Valley Museum** — holds only *Miss Veedol*'s bent propeller.
- **MOHAI** (Seattle) hangs the original Boeing B-1, but is a general history
  museum. Arguably belongs here; left out for now.
- Nothing at Arlington, Bremerton, Ephrata, Moses Lake, Walla Walla,
  Tri-Cities or Tacoma Narrows.

## Judgment calls

- **Both "Zeros" are Canadian Car & Foundry Harvards** converted for *Tora!
  Tora! Tora!* — one at Heritage Flight, one at Olympic (N15796). Recorded as
  what they are, with the conversion in aliases, rather than as Mitsubishi.
- **FHCAM's German and Soviet aircraft carry their Werknummer as the tail**,
  with the N-number in aliases. That's the airframe's identity and matches
  how Pima and NMUSAF file the same types. Its US Navy types carry BuNos.
- **FHCAM's Ju 87 is excluded**: it left for The Roost, Bentonville, on
  27 June 2025. The audit believed it still there under restoration; the
  research had the date and destination. Also gone or off-site: MiG-21UM,
  MiG-29UB, F-105G, two F-86s, F-84G, Harrier GR.3, the Crusaders, the CASA
  2.111, the Alpha Jet and B-17E 41-9210 — none of which are on display.
- **Olympic Flight Museum's earlier FG-1D Corsair and L-29 are gone** from the
  museum's rebuilt site, so they're not here even though Wikipedia still
  lists them. Four Olympic aircraft are `in_storage` on the museum's own
  flag. The audit disagreed on both points, citing Wikipedia; the museum's
  current site wins on "what is here now".
- **Port Townsend's Cessna 140, Dormoy Bathtub replica and Ka 6E** are on
  Wikipedia's older list but gone from the museum's current pages. Excluded.
- **Boeing Future of Flight** is a corporate visitor gallery with one real
  airframe — a Wisk Gen 5 eVTOL. Included on the same test as the Carolina
  children's museum: a real, complete aircraft in a formal public exhibit.
  Typed `fixed_wing` because it has a lifting wing; the schema has no VTOL.
- **Pearson's DH-4B** is the US-built Liberty Plane, so the manufacturer is
  Dayton-Wright, not Airco. Its Curtiss Pusher, Voisin III and Fokker Dr.I
  are replicas.
- **McChord's OA-10A serial 43-43847** is what the museum states and does not
  fit the known OA-10A blocks; its UH-19B carries a Navy BuNo (138499), which
  would make it an HO4S-3. Both recorded as the museum has them, flagged.
- **The Museum of Flight's "Bf 109E-3"** is, per its own page, a composite
  with HA-1112 Buchón components. FHCAM's Bf 109E-3 W.Nr 1342 is a genuine
  and separate airframe. Not a duplicate.

## Found by auto-discovering every data file

Switching the validation suite to test every `*_aircraft.csv` under `data/`
(rather than a hand-kept list) turned up one thing in already-live data:
**USS Midway's "Douglas TBD-1 Devastator".** No Devastator is on display
anywhere in the world — the only recovered airframes are wrecks. Midway does
have an SBD Dauntless. That row is live (`data/california/uss_midway_aircraft.csv`
line 18) and is almost certainly wrong. It wasn't touched here; it needs a
look.

The Planes of Fame HA-200 and L-29 "duplicates" the same sweep flagged are
real pairs — different build years — and the test now counts `year_built`.
