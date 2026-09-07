# Virginia — Steven F. Udvar-Hazy Center

Museum id 22. Chantilly, VA. The Smithsonian National Air and Space Museum's
annex — **a separate site from the Mall building** (museum id 21), which is
the single most important thing to get right here.

| File | Rows | Tails |
|---|---|---|
| `udvarhazy_raw.txt` | — | research output, kept for audit |
| `udvarhazy_aircraft.csv` | 144 | 76 (52%) |

Source of record: `airandspace.si.edu` object pages. Wikipedia was used to
enumerate the roster and its citations followed to the underlying sources.
**No third-party registry serials were needed** — the Smithsonian publishes
object records, so every identifier here came from the museum itself.

## A wrong record already live: the B-2

Our database credits Udvar-Hazy with a **Northrop Grumman B-2A, 82-1066**.
That is wrong. The Smithsonian holds only archival B-2 material (accessions
NASM.1997-0014 and NASM.2019-0013); the only complete B-2 on public display
anywhere is the structural-test airframe at the National Museum of the USAF.
**That record should be deleted**, not corrected.

## Mall vs Chantilly

Aircraft excluded because they are at the Mall building, not here:

- **North American X-15** — Udvar-Hazy has only a static model
- Fulton Airphibian FA-3-101 — moved to the Mall's "We All Fly" gallery
- Huff-Daland Duster — moved to the Mall
- Laird-Turner Meteor LTR-14 — now in the Mall's "Nation of Speed"

The MQ-1L Predator was reported by one pass and contradicted by another,
which found the museum's own record saying it is not on display. Excluded.

## Judgment calls

- **Sperry M-1 Messenger is a biplane.** Caught by the pre-import audit; it
  had gone in as a monoplane.
- **Beechcraft King Air** had its model and marketing name swapped relative to
  every other Beechcraft row (`model=King Air, variant=65-90`). Now
  `model=65-90, model_name=King Air`.
- **Composite and reconstructed airframes**, recorded but noted: the Nieuport
  28 is "an amalgam of component parts of several aircraft"; the Wright EX
  *Vin Fiz* has no single continuous airframe and its engine is a mock-up;
  the Verville-Sperry M-1 was converted by the Smithsonian from a two-seat
  Sport Plane; the Pegasus XL combines a flown wing with a ground-test motor.
- **Representational markings:** the F4U-1D wears "Sun Setter" markings applied
  during its 1980 restoration, not its wartime identity.
- **Compound manufacturer credits** resolved to the first name: CASA 352L
  (Junkers licence), Concorde (Aérospatiale/BAC), P-V Engineering Forum PV-2
  (later Piasecki), Vought-Sikorsky XR-4C.
- **Spacecraft** are typed `spacecraft` with role `space`.
- Horten Ho 229 V3 is `under_restoration` — visible in the restoration hangar
  but explicitly undergoing conservation.

## Uncertain, flagged rather than guessed

- **Aeronca C-2 model_name "Collegian".** "Flying Bathtub" is the documented
  C-2 nickname; "Collegian" is associated with the later C-3. Left as the
  museum states it, but worth checking a placard.
- Aero L-39C "American Spirit" was transferred June 2026 with display expected
  later that summer. Recorded `on_display`; re-check.
- Grumman F-14 159610 and A-6E 154167 came from search snippets that partially
  conflated two records — worth a direct page fetch to confirm.
- Two catalogue entries could not be resolved to a detail page and are absent:
  a Republic P-84 Thunderjet and a Vickers Viscount in Malév colours.
