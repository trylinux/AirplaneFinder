# Utah — build notes

Hill Aerospace Museum is the state. It already existed in the database
(id 28) with zero aircraft; the other four museums are new.

| File | Museum | Rows | Tails |
|---|---|---|---|
| `ut_museums.csv` | 4 new museum records | — | — |
| `hill_aerospace_museum_aircraft.csv` | Hill Aerospace Museum, Roy | 76 | 70 (92%) |
| `western_sky_aviation_warbird_museum_aircraft.csv` | St. George | 13 | 12 |
| `historic_wendover_airfield_museum_aircraft.csv` | Wendover | 3 | 3 |
| `utah_military_museum_at_historic_fort_do_aircraft.csv` | Fort Douglas, SLC | 3 | 3 |
| `caf_utah_wing_museum_aircraft.csv` | Heber City | 2 | 1 |
| `hill_raw.txt`, `ut_rest_raw.txt` | research output, kept for audit | — | — |

97 aircraft. Hill's own per-aircraft pages have a "Serial Number" field,
which is why coverage is 92%.

## Hill's site is stale, and it matters

Hill deaccessioned about 18 aircraft in 2014 and its collection pages were
not all updated. The concrete case: **its C-7B Caribou 63-9757 left for the
March Field Air Museum in 2024** — Hill had no indoor room and offered it up —
and Hill's page still lists it. The collision check caught it (March Field
already holds 63-9757 live); Vintage Aviation News confirmed the move. Dropped
from Hill. Also dropped as absent from the current floor map: a C-123K, an
A-37, a T-39A and an F-86L that Wikipedia still lists.

The research used the museum's own layout map (`museum-map.pdf`) to confirm
physical presence, not just the collection pages.

## Judgment calls

- **B-29 "Straight Flush" is 44-86408.** Hill's own B-29 page misprints the
  C-45H's serial (52-10862); the correct number is from the museum's own
  article and Vintage Aviation News. The name is markings — the real
  Straight Flush, 44-27301, was scrapped.
- **Composites carrying borrowed identities:** the P-51D wears 44-13371, the
  serial of an aircraft lost in 1944, on a 1992 Kal Aero rebuild; the P-40N
  wears 42-105270 borrowed from another P-40 because its plates were
  unreadable (the museum says so). Both serials are valid-looking and both
  are noted as representative in aliases.
- **AT-6A "039"** is a placard number, not a serial, on an airframe assembled
  from parts. Tail blank; the number is in aliases.
- **A-1E 52-0247** doesn't fit any AD-5 block (USAF used 52-132xxx). Recorded
  as the museum states it, flagged in aliases.
- **The Lim-5 is filed under PZL-Mielec**, not Mikoyan-Gurevich as the museum
  credits it, to match Western Sky's Lim-5 and the SBLim-2. Its tail is a
  construction number because that is the only identifier the museum gives.
- **Wright Flyer** is a three-quarter-scale replica on loan from the USAF
  Heritage Program; the **Burgess Model F** is a replica of the Burgess-Wright
  Model B. The **C-130E** is a fuselage-only classroom.
- **F-22A 91-4002** is genuinely there — the EMD test airframe, arrived 2019.
  The audit doubted it; the museum's page and press coverage don't.
- **Missiles:** Hill's ICBM exhibit is documented only as components and a
  launch-control mock-up; the vertical Minuteman/Peacekeeper park is at the
  base's west gate, not the museum. Only the Snark, Quail and Firebee are
  recorded.

## The smaller museums

- **Wendover:** the C-54E (ex-firefighting tanker, identity registry-sourced),
  the *Con Air* C-123K, and the F-86L are the museum's. The flightline
  HU-16E, PA-18 and several CT-133s are privately owned, described as "not
  guaranteed present", and have no confirmed identities — excluded rather
  than guessed. The C-123K's "N709RR" is the film registration of a
  different airframe; this one's data plate reads msn 20245 / 56-4361.
- **Western Sky:** identities verified in the FAA registry for the L-29, both
  Jet Provosts, GN-1, Lim-5, SBLim-2 and C-54Q. The two T-37Bs, F-5B and
  T-38A serials are Baugher-derived; the second T-37B (60-0122) is the least
  corroborated. The GN-1 Aircamper is a parasol monoplane, corrected from
  biplane. Visiting aircraft (T-33, P-51, Yak-52) excluded.
- **CAF Utah Wing:** seasonal, May–October weekends. The T-6 is member-owned
  with no published identity; the N2S-5 has been in restoration since 2017.
- **Fort Douglas** is a general military museum with three helicopters
  outdoors, all with serials on interpretive markers. The building is
  temporarily closed until November; the grounds stay open.

## Excluded — do not re-research

- **Vintage Aviation Museum, Spanish Fork** — under development, no public
  hours yet; two PV-2 Harpoons donated 2026 and a Draken planned. Revisit.
- **Utah Aviation Hall of Fame** — an exhibit inside Hill, not a museum.
- Camp Williams and Dugway — closed to the public.
- Ogden Union Station, Tooele, Brigham City, Vernal, Price, Moab, Logan,
  Cedar City — no complete aircraft.
