# Records to review — created 10 September 2026

Nothing here has been deleted. Removing rows from the live database is not
something to do unasked, so every row below is flagged in its own
`description` and listed here for a decision.

## 1. Erroneous records — the aircraft is not at the site

- **id 25228** — Douglas C-47 (no serial)
  
  VERIFICATION 10 September 2026: the museum holds NO complete full-size aircraft. The only airframe on the property is an Embraer EMB-110 Bandeirante nose/cockpit section indoors (museum maintenance posts 30 Oct 2024 and 13 Oct 2025). The C-47 in the museum's material is the VIRTUAL aircraft of its Around the World Flight Adventure simulator programme; a real DC-3 visited Manchester in August 2020 but is not resident. This record is erroneous and should be deleted.

- **id 25892** — North American P-51D 44-63615
  
  VERIFICATION 10 September 2026: NOT present. Aerial Visuals records this airframe (P-51D-20-NA c/n 122-31341, later Fuerza Aerea Uruguaya 270) as placed on display with the National WWII Museum New Orleans on 21 April 2016 in Tuskegee Red Tail markings; the museum's US Freedom Pavilion page still lists it. The 28 December 2024 OpenStreetMap survey of the Seymour Johnson air park maps six aircraft and no Mustang. The 2016 NMUSAF loan list and Baugher are both pre-move. This record is erroneous and should be deleted; the airframe is recorded at the National WWII Museum.

## 2. Duplicate records — two rows for one airframe at one site

| delete | keep | aircraft |
|---|---|---|
| 26490 | 26479 | Sperry Messenger |
| 26491 | 26480 | Baker Special |
| 26492 | 26481 | Jeffair Barracuda |
| 26493 | 26482 | Rand KR-2 |
| 26494 | 26483 | Pereira Osprey-2 |
| 26486 | 26485 | Waco CG-4A |
| 26595 | 26594 | Bell UH-1 |
| 26473 | 26471 | McDonnell ADM-20 |
| 31095 | 27255 | Lockheed T-33 |
| 31094 | 27253 | Bell UH-1H |

## 3. Duplicate SITE record

`Don F. Pratt Memorial Museum` and `Don F. Pratt Memorial Museum Air Park`
are the same air park at Fort Campbell, entered by two different research
passes 700 m apart. Nine airframes appear in both; the nine in the Air Park
record carry blank tail numbers because the serials collided. The museum
building itself closed 22 November 2024 and the new Tennessee Wings of
Liberty Museum opened outside the gate on 15 May 2026 — so the surviving
record should probably be the air park, under whichever name the Army now
uses. Needs a decision before either record is merged away.

## Deleting, once reviewed

```bash
# AIRPLANE_KEY=amt_... bash scripts/delete_reviewed_sep2026.sh
```

## 4. Wyoming duplicate sites — added by the top-up pass

The 10 September top-up named three Cheyenne sites with a ` -- Cheyenne` suffix,
so the reconciler did not recognise the records the main Rockies pass had
already created three hours earlier. Three museum records and four aircraft
records are duplicates. All six are flagged in their own descriptions.

| delete museum | keep museum | site |
|---|---|---|
| 4723 | 3855 | Warren ICBM and Heritage Museum |
| 4724 | 3854 | Wyoming National Guard Museum |
| 4725 | 3853 | Wyoming Air National Guard Air Park |

| delete aircraft | keep aircraft | airframe |
|---|---|---|
| 31090 | 27247 | Bell UH-1F 65-7953 |
| 31091 | 27246 | Lockheed T-33A 56-3661 |
| 31092 | 27245 | North American F-86 23351 — variant conflict, E or L |
| 31093 | 27243 | Lockheed C-130E 63-7861 |

The repo-side CSVs for the three duplicate sites have already been moved to
`_to_delete/wy_dupes/` and the duplicate rows removed from `wy_museums.csv`, so
the repo is clean; only the live database still carries them.

## 5. Corrections applied in place, not deleted

- **aircraft 27242** — Wyoming ANG Air Park F-84F. Its `variant` was written as
  `F-84F`, which made `full_designation` read `F-84F-84F`; corrected to `F`.
  Its description now carries the conflict that the Aerial Visuals dossier for
  52-7019 gives Western Nebraska Technical College in Sidney NE as the airframe's
  latest location. Needs a photograph.
- **aircraft 26340** — Air Zoo TF-9J. Model was `TF-9J` with an empty variant;
  corrected to model `TF-9`, variant `J`.
- **aircraft 26009** — National WWII Museum P-51D. Its description now carries
  the c/n chain identifying it as 44-63615. The serial cannot be attached while
  the erroneous Seymour Johnson record (25892) holds it.
