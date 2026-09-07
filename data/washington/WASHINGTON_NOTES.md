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
