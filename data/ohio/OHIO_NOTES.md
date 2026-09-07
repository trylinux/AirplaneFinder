# Ohio — National Museum of the United States Air Force

Museum id 20. `1100 Spaatz St, Wright-Patterson AFB, OH 45433`.
Real collection is roughly 360 airframes; the largest military aviation museum
in the world.

## Files

| File | Rows | Tails | Status |
|---|---|---|---|
| `nmusaf_topup_a_to_l_aircraft.csv` | 149 | — | imported (157 live) |
| `nmusaf_topup_m_to_z_aircraft.csv` | 126 | 46 (36%) | ready |
| `nmusaf_m_to_z_raw.txt` | — | — | research output, kept for audit |

Split by manufacturer initial per METHODOLOGY.md. M–Z was researched as four
parallel passes (M / N–R / S–T / U–Z) against the museum's own fact sheets at
`nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Indextitle/<letter>/`.

Total after import: about 283 of ~360.

## Serial coverage is low, and that is the honest number

36%, against 87% for Pima. NMUSAF fact sheets are written as type histories,
not airframe records — most do not state the serial of the aircraft on the
floor. Every blank here is a serial the museum does not publish, not one we
failed to look up. Per METHODOLOGY.md we left them blank rather than sourcing
a plausible serial from a registry and implying the museum said it.

Consequence worth knowing: 80 rows have no tail number, and a blank tail is
NULL, which never collides. Re-running this file without
`scripts/filter_new_aircraft.py` would silently double those 80 rows. The
import script does this automatically for `*topup*` files.

## Judgment calls

**`fetch` had to go through the app's web_fetch, not curl.** The site returns
403 to plain HTTP clients. Noted because the next person will hit it.

**Excluded — not airframes.** Engines (Salmson, Sturtevant, Walter HWK 509),
ground support equipment (MJ-1, MHU, MC-11, MA-1A), guns (M61A1, M102,
ZPU-4), warheads (W53), bomb bodies without propulsion (VB-1 through VB-13),
and exhibit/biography pages. The fact-sheet index mixes all of these in with
aircraft.

**Included as `missile_rocket` though unpowered:** Texas Instruments BOLT-117
(the first laser-guided bomb, later GBU-1) and Ruhrstahl X-4. Both are guided
weapons displayed as complete articles, and this matches how Pima's Fritz X
and Ohka are filed. Consistency across museums matters more here than a
purist reading of "missile".

**Excluded — SS-N-2 Styx.** The fact sheet gives the manufacturer only as a
nationality. The real builder is a Soviet design bureau we could not confirm
from the museum's own page, and `manufacturer` is a required field. Recording
it as "Russian" would put a country in a company column. Left out; worth
adding once someone can source the bureau.

**Not included, needs a second look.** The M pass flagged three it could not
re-verify before finishing: Martin X-24A and X-24B lifting bodies, McDonnell
Douglas AIR-2A Genie, McDonnell ADM-20 Quail. These are very likely genuine
NMUSAF holdings. They are absent rather than guessed at.

**Letters O and Q yielded nothing.** Fully paged through; O contains only
"Operation …" essays and Q only fragments. Recorded so nobody re-runs them.

**Reproductions, recorded as such in aliases:** Martin MB-2/NBS-1 (built 2002
from original drawings — no original survives), Sopwith Camel F.1 (built 1974),
Nieuport 28 (rebuilt using original parts), Wright 1909 Military Flyer (1955).
`year_built` on these is the reproduction's build year, which is the honest
answer for the object on the floor.

**Airframes displayed as something else.** Recorded under what they *are*,
with the markings noted in aliases:

- B-25B "Doolittle Raid" is physically RB-25D 43-3374
- F-82G is physically an F-82B
- F-89J 52-1911 wears the markings of 53-2509
- O-47B 39-112 is displayed in O-47A markings
- P-61C 43-8353 is displayed in P-61B markings

**Northrop B-2** is one of two unpowered structural-test airframes, not a
flying Spirit. Noted in aliases so it isn't mistaken for an operational bomber.

**Spacecraft.** Northrop OV2-5 (a donated mock-up, never flown) and the DSP
early-warning satellite are typed `spacecraft` with `role_type` `space`.

## Cross-museum conflict resolved

**X-15A-2, 56-6671 — NMUSAF holds the real one.** Pima also lists an X-15A-2
with this serial, but Pima's own page calls it a construction mockup and puts
the serial in quotation marks. The tail number is recorded here and blanked at
Pima. See `data/arizona/ARIZONA_NOTES.md`.

## Still open

- Pima's C-130 62-1787 and NMUSAF's are the same serial. Unresolved from
  before this batch; neither file currently claims it.
- ~77 airframes remain unrecorded (283 of ~360). Mostly A–L gaps rather than
  M–Z, since A–L was an earlier, less systematic pass.
