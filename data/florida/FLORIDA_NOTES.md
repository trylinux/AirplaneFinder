# Florida — National Naval Aviation Museum

Museum id 26. NAS Pensacola, FL.

| File | Rows | Tails |
|---|---|---|
| `nnam_pensacola_raw.txt` | — | research output, kept for audit |
| `nnam_pensacola_aircraft.csv` | 165 | 56 (33%) |

Sources: the museum's own site (which fetched fine, despite returning 403 to
some clients), the Naval History and Heritage Command's "Aircraft on Display"
catalogue — which has a **per-letter JSON API** and was the best structured
source available for this museum — and Wikipedia with its citations followed.

## 33% BuNo coverage, and why that is the honest number

Neither the museum nor NHHC publishes a BuNo for most airframes. Where one
was filled from a registry, it is listed below so it stays auditable:

- **joebaugher.com** (via Wikipedia citations): BFC-2 9332, F6C-1 A6969,
  F7C-1 A7667, JN-4D A995, N2C-2 A8529, N2Y-1 A8605
- **Navy serial number registry (cgibin.rcn.com):** PB2Y-5R 7099,
  PBY-5 08317, SNC-1 05194, OY-1 60507
- **Enthusiast sites** (Skyhawk Association, avgeekery, transporttags): the
  four Blue Angels A-4F BuNos 150076 / 154217 / 154983 / 155033, TC-130G
  151891, KC-130F 149798

Everything else with a blank tail is one nobody publishes, not one we failed
to look up.

## Judgment calls

- **The AV-8C Harrier was entered twice** — once as Hawker Siddeley without a
  BuNo, once as McDonnell Douglas with BuNo 158975. The museum holds exactly
  one, suspended in Hangar Bay One. The untailed copy was dropped. Caught by
  the pre-import audit; it would have double-counted a real aircraft.
- **Ford RR-5 is `military`.** "RR" is the US Navy's own designation for its
  Ford Trimotors, so a Navy-designated airframe at a naval aviation museum
  filed as civilian was internally inconsistent.
- **Curtiss P-40 variant corrected from "IIB" to "B".** "Tomahawk IIB" is the
  British mark, not a Curtiss variant letter; it moved to aliases.
- **Boeing F4B-4, serial "32-92".** This looks like the classic error of a
  USAAC serial on a Navy aircraft — but it is correct and deliberate: the
  airframe genuinely is a P-12F carrying its original Army serial, restored
  and displayed in Navy F4B-4 "Felix the Cat" markings. Noted in aliases so
  nobody "fixes" it later.
- **Brewster SB2A-1 "FF860"** is an RAF serial (Bermuda Mk.I), likewise noted.
- **HH-3F "1486"** is a Coast Guard tail number, not a Navy BuNo.
- **Untailed rows that are genuinely two aircraft** were given distinguishing
  aliases rather than being merged: two FM-2 Wildcats (Quarterdeck and Pacific
  Island exhibits), two N3N Yellow Perils (floatplane and conventional gear),
  two Dauntlesses (restored, and an unrestored Lake Michigan recovery in the
  Underwater Treasures exhibit).
- **Dropped as a listing artifact:** Wikipedia shows both a "Bell HTL-4" and a
  plain "Bell HTL"; only one could be confirmed, so only one is recorded.
- **Excluded — no longer at Pensacola**, per Wikipedia's own post-2024
  updates: de Havilland Canada NU-1B Otter (to Hickory Aviation Museum),
  Curtiss-Wright R5C Commando (to the Air Mobility Command Museum), and a
  PBY-5A loaned to the Air Zoo for restoration.
- **Replicas:** the Curtiss A-1 Triad (built 1961 for the 50th anniversary of
  naval aviation), the Vought VE-7 Bluebird, the Apollo 17 Lunar Module
  *Challenger* (2012), and the *Freedom 7* Mercury capsule.
- The **NC-4** is original, and is on loan from the Smithsonian.

## Uncertain, flagged rather than guessed

- **Fokker D.VII.** A WWI German Army fighter is an odd fit for a naval
  aviation museum — not impossible as a war trophy, but worth a placard check.
- **Douglas A3D variant "A"** does not match either the pre-1962 factory
  designation (A3D-1/A3D-2) or the post-1962 A-3A. Left as sourced.
- **Boeing Vertol CH-46** was filed under "Boeing Vertol", which put it in the
  A–L slice. Defensible either way.

## A pre-existing record to fix

The one aircraft already live at this museum — Beechcraft GB-2 — has its tail
number stored as **`USN BuNo 23688`**, prefix and all. The builder now strips
`BuNo` / `S/N` / `Serial` prefixes, but this row predates that and should be
corrected to `23688`.
