# Arizona — build notes

Strategy shift from California: rather than sweeping a whole state, this
phase tops up the **big museums already in the database that are showing
almost nothing**. Arizona first, because Pima is the largest single gap
anywhere in the dataset.

## Pima Air & Space Museum (id 23) — 5 recorded, ~366 real

Pima publishes a WordPress REST feed at
`pimaair.org/wp-json/wp/v2/museum_aircraft`, which is far better than
scraping the HTML: it exposes per-airframe Manufacturer / Markings /
Designation / Registration / Serial Number fields. **366 aircraft records
site-wide.** That also corrects the widely-quoted "~425" figure.

Split by manufacturer initial so each slice is a manageable research pass.

| File | Slice | Rows | Tails |
|---|---|---|---|
| `pima_topup_a_to_f_aircraft.csv` | manufacturers A–F | 142 | 140 (98%) |
| `pima_topup_g_to_m_aircraft.csv` | manufacturers G–M | 112 | 106 (95%) |
| `pima_topup_n_to_z_aircraft.csv` | manufacturers N–Z | 106 | 93 (87%) |

A–F and G–M are imported (259 live). N–Z completes the collection: 365 of
366 records, the one exclusion being the MiG-21PF recorded at CAF Mesa below.

The feed is now parsed by `scripts/parse_pima_feed.py` and turned into CSV by
`scripts/build_pima_csv.py`, rather than by hand.

**98% serial coverage is the best in the whole project** — better than
Travis or Joe Davies, and far better than the 44% California average.
Pima publishes a serial for nearly every airframe.

Already recorded, excluded from the top-up: Boeing VC-137B 58-6971 (A–F),
plus Lockheed C-130E 62-1787, P-38L 44-53236, F-16C 84-1301 and
SR-71A 61-7951, which fall in the L slice.

### A–F caveats

- **8 aircraft are `in_storage`** and 2 `under_restoration`, taken from
  Pima's own "not currently on public display" wording rather than assumed.
- **Four are on loan or displayed off Pima's own grounds** but remain in
  their catalogue, so they are kept: the Curtiss F6C-4 Hawk (National
  Museum of the Marine Corps), the AIR-2 Genie (NMUSAF), the Bell UH-1F
  (physically at the adjacent **Titan Missile Museum**), and the B-17G
  (at the **390th Memorial Museum** on the same campus). If you ever add
  those two as separate museums, these three should move.
- **Three are missiles**, in Pima's own aircraft catalogue: AIR-2 Genie,
  SM-75 Thor, Fi 103 (V-1). Typed `missile_rocket`.
- **One `lighter_than_air`** — the Avian Falcon II balloon.
- A source bug: Pima's own Manufacturer field reads "Brewster" for the
  Bowers Fly Baby, an obvious copy/paste error. Corrected to Bowers.
- The Bolingbroke is recorded under **Fairchild Aircraft Ltd** (the Canadian
  licensee), which is what Pima's page says, rather than Bristol.
- No AMARG/boneyard aircraft appeared in this slice — the adjacent boneyard
  is not part of the museum and is excluded by policy.

### G–M caveats

- **One aircraft moved museums.** Pima's MiG-21PF serial **507** is on loan
  *from* Pima *to* the CAF Arizona Wing in Mesa — it is in Pima's catalogue
  but physically in another building. Since this app answers "where can I
  go and see it", it is recorded at **CAF Airbase Arizona**
  (`caf_airbase_arizona_aircraft.csv`), not Pima.
- **One collision, dropped:** Lockheed C-130A **57-0457** is already in the
  database under another museum. Left where it is rather than forced.
- **On loan to Pima** (kept, since they are physically there): S-3B 160604
  and the Blue Angels F/A-18A 163093 from Pensacola; MiG-15UTI and MiG-23MLD
  from NMUSAF; the Mi-24D Hind from IWM Duxford.
- In storage: Lark 95, P-2H 150281, Bf 109F-4, WB-57F.
  Under restoration: P-38G "Dumbo", B-26B Marauder, MiG-23MLD.
- Pima's own manufacturer field uses compound credits in two places
  ("General Dynamics/McDonnell-Douglas" for the Gryphon,
  "Martin/General Dynamics" for the WB-57F); recorded under the first.
- No AMARG boneyard aircraft in this slice. Several passed through
  Davis-Monthan storage historically, but all are museum collection now.

### N–Z caveats

- **Pima's two X-15s are not X-15s.** The museum's own pages call them a
  *replica* (X-15A) and a *construction mockup* (X-15A-2), and it writes their
  serials in quotation marks — `“56-6670”`, `“56-6671”` — to say the numbers
  are painted on rather than the airframes' identities. The real X-15A-2
  **56-6671 is at the National Museum of the USAF**. Both rows here carry an
  empty `tail_number`, the marking in `aliases`, and a description saying
  plainly that it is a replica. Importing the quoted serial would have claimed
  a famous airframe Pima does not have *and* collided with the museum that
  does, under the unique index on `(model, tail_number)`.

  The quoted-serial convention turns out to be reliable and rare — exactly
  three records site-wide use it, and all three are replicas. The parser now
  treats it as a signal.

- **One record lists two serials:** the AGM-28A Hound Dog, `59-2866 AND
  60-2092`. That is either two missiles on one page or uncertainty about
  which. The row imports with a blank tail and both serials in aliases rather
  than picking one.

- **Radioplane drones** (OQ-3, OQ-19D, MQM-57) have no serials at all in the
  feed. Kept, untailed.

- **Source spellings corrected:** `SIKORKSY` → Sikorsky, `Schemmp-Hirth` →
  Schempp-Hirth, `Rhurstahl` → Ruhrstahl, `P51D` → P-51D. The museum's own
  typos.

- **Three records publish no Designation field** and are keyed on their title
  instead: the Thiokol Space Shuttle SRB, the TL-Ultralight Stream, and the
  Wright 1903 Flyer.

- **The Taylorcraft BC-12D's Registration field contains the string
  "BC-12D"** — its own model, not a registration. Imported with a blank tail;
  the construction number 7243 is in aliases.

- **Model-vs-mark corrections.** Three Westland Lynxes were being filed under
  models `AH.1`, `AH.7` and `HMA.8`, which would scatter one type across three
  models; they are now Lynx with those as variants. Same for the two SEPECAT
  Jaguars (`GR3A`, `T4`) and the Short Tucano (`T1`).

- **5 in storage, 1 under restoration**, from Pima's own wording.

### Caught by the pre-import audit

An independent review of the finished file found four real errors, all now
fixed at source and covered by tests in `tests/test_flagship_topup_files.py`:

- **Pitts S-1C and PZL Mielec An-2R were recorded as monoplanes.** Both are
  biplanes. The cause was a dead lookup key: the BIPLANE table was keyed on
  the designation `"S-1C"` while rows carry the split model `"S-1"`, so the
  entry never matched and failed silently. Now keyed on the split model.
- **F-105G was `fighter`.** It is the Wild Weasel SAM-suppression conversion;
  NMUSAF's F-105G was already `electronic_warfare` and they now agree.
- **Piper PA-48 Enforcer was `private`** because it carries a civil
  registration. It was a turboprop COIN demonstrator built for USAF
  evaluation — now `experimental`.

### Still uncertain — flagged, not guessed at

- **Supermarine Spitfire MT847.** Pima's own page gives this serial, but
  MT847 is generally recorded as a Mk XIVe at the RAF Museum Cosford. Either
  Pima's page is wrong, or this is a different airframe, or one of them is a
  replica. Imported as the museum states it, with no variant. Worth a look.
- **Ryan/TEMCO D-16A Twin Navion.** The Twin Navion was a TEMCO conversion,
  so "Temco" is arguably the better manufacturer. Recorded as **Ryan**, which
  is the first name in Pima's own compound credit and consistent with how the
  Gryphon and WB-57F were handled in the A–F and G–M slices.
- **Two Yokosuka MXY7 Ohkas** (serials 62 and 1174). Two at one museum is
  unusual, but the feed lists them as separate records with distinct serials.
  Kept.

### Corrections owed to the already-imported A–M rows

`pima_a_to_m_corrections.csv` lists the 15 A–M records the improved parser
flags. Checked against live data by `scripts/apply_pima_corrections.py`,
**14 of the 15 are already correct** — the A–F and G–M passes did capture the
museum's status wording, so only one real correction remains:

- **Hawker Hurricane Mk. IIB, tail `BG974`.** Pima writes this serial in
  quotation marks, its marker for a painted-on marking rather than an
  identity. The aircraft is a replica and should not hold `BG974` as a tail
  number.

Two lessons worth keeping. First, a correction list generated from the source
alone says nothing about whether the target needs correcting — it has to be
diffed against live data, which is why the script does that and reports "N
already correct" rather than blindly PATCHing. Second, matching has to use
whichever identifier we actually *stored*: the builder files a civil airframe
under its registration, so the Boeing 727 is live as `N7004U` while the feed
calls its serial `18296`. Matching on the serial alone reported three
already-correct records as missing.

These are PATCHes against live records, not an import, so they ship as a
script rather than a CSV.

## Other Arizona museums in the database

**Commemorative Air Force Airbase Arizona** (id 29, Mesa) — has 1 aircraft
now (the MiG-21 above). Its own collection is not yet researched.

Worth adding later: Titan Missile Museum (Sahuarita), Planes of Fame Valle
— note the Valle site is the one whose aircraft were deliberately excluded
from the Chino file, so it has a ready-made starting list in
`../california/CALIFORNIA_NOTES.md`.
