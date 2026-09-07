# Wisconsin — EAA Aviation Museum

Museum id 30. Oshkosh, WI. The Experimental Aircraft Association's museum.

| File | Rows | Tails |
|---|---|---|
| `eaa_raw.txt` | — | research output, kept for audit |
| `eaa_aircraft.csv` | 117 | 100 (85%) |

Source of record: EAA's own aircraft collection listing (126 catalogued
airframes across a paginated, client-side-rendered gallery). **No registry
identifiers were needed** — EAA publishes N-numbers for nearly everything,
which is why coverage is 85% against Pensacola's 33%.

## This collection is not shaped like an air force museum

Mostly homebuilt, experimental, aerobatic and antique **civil** aircraft, so
the mix is heavily `civilian` / `private` / `experimental` with N-number
registrations, and unusually biplane-heavy. Manufacturers are often
individuals rather than companies — Wittman, Poberezny, Loving, Rider,
Corben, Driggers — which is correct, not a data error.

## Judgment calls

- **Compound "X/Y" titles resolved to the actual builder of that airframe**,
  which is the museum's own framing: "Howard/Poberezny Pete III" → Poberezny,
  since Poberezny personally built *Little Audrey* from a Howard-lineage
  fuselage. "Messerschmitt/Hispano Buchon" → Hispano Aviación, which built it
  under licence.
- **Replicas, recorded and flagged in aliases:** Chanute hang glider, Laird
  Super Solution (1981, depicting a 1931 aircraft), Bücker Bü 133 N258H,
  Blériot XI bis, Curtiss P-6E (Rosanik-built), Fokker Dr.I (Redfern-built),
  Ford Flivver (EAA Chapter 159), Nieuport 11 (Huntley), Ryan NYP *Spirit of
  St. Louis*, Waco Primary Glider, Nicholas-Beazley Pobjoy Special, Wittman
  "Hardly Abelson" (1995, Pat Packard), Wright Model B (EAA Chapter 610),
  Rutan Voyager (partial replica). `year_built` on these is the replica's own
  build year, which is the honest answer for the object on the floor.
- **Excluded — touring, not on display:** the B-17 *Aluminum Overcast* and the
  Ford Tri-Motor both fly and were not in the static collection listing.
- **Excluded — temporary display that has ended:** a Supermarine Spitfire,
  MiG-15, de Havilland Vampire, Republic F-84 and an Me 262 reproduction were
  shown together only until mid-August 2025, per EAA's own article.
- The **North American XP-51** (NX51NA) looks implausible — an XP-51 prototype
  surviving — and the audit initially flagged it. It is genuine: the fourth
  and last XP-51, a real survivor at EAA. Recorded as-is.
- **Antares MA-30** is a Rogallo-wing weight-shift trike. Forced to
  `monoplane` because the schema has no better wing type; flagged as atypical.
- **Uncertain identifiers:** the Folkerts Henderson Highwing's "8902" and the
  Ford Flivver's "268" may be contest or chapter numbers rather than
  registrations. Both moved to aliases rather than the tail column.

## Cross-slice duplicates — a hazard of splitting alphabetically

Six airframes came back in **both** the A–L and M–Z passes under different
manufacturer credits: the Schreder/Helisoar HP-10 (N319Y), Lancair/Neibauer
Model 200 (N384L), Howard/Poberezny Pete III (N111PL), Boeing/Stearman Model
75 (N121R), Chance Vought/Vought F4U-4 (N6667), and the Bücker Bü 133.

Splitting research by manufacturer initial assumes every airframe has one
canonical manufacturer, and compound credits break that assumption. The
builder now dedupes on tail number, which is the airframe's actual identity.
