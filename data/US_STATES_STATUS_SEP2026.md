# United States — remaining states completed, 10 September 2026

The overnight run of 10 September finished the US state sweep. Twenty-seven
jurisdictions went in as seven regional batches plus one top-up pass:
**542 site records and 2318 airframes**, every one dry-run clean against the live
importer before anything was applied.

| Region | States | Sites | Airframes |
|---|---|---|---|
| New England | Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont | 41 | 270 |
| Mid-Atlantic | Delaware, District of Columbia, Maryland, New Jersey, West Virginia | 57 | 391 |
| Carolinas | North Carolina, South Carolina | 69 | 302 |
| Mid-South | Kentucky, Louisiana, Mississippi, Tennessee | 96 | 329 |
| Great Lakes | Illinois, Indiana, Michigan | 133 | 515 |
| Upper Midwest | Iowa, Minnesota, North Dakota, South Dakota | 112 | 370 |
| Northern Rockies and Alaska | Alaska, Montana, Wyoming | 34 | 141 |
| **Total** | 26 states + DC | **542** | **2318** |

## Per state

| State | Sites | Airframes |
|---|---|---|
| Michigan | 47 | 242 |
| North Carolina | 43 | 201 |
| Illinois | 51 | 181 |
| Maryland | 20 | 144 |
| Tennessee | 30 | 133 |
| Connecticut | 10 | 124 |
| Minnesota | 40 | 117 |
| Iowa | 32 | 115 |
| South Carolina | 26 | 101 |
| New Jersey | 18 | 95 |
| Louisiana | 29 | 94 |
| Indiana | 35 | 92 |
| North Dakota | 25 | 87 |
| District of Columbia | 6 | 86 |
| Massachusetts | 10 | 75 |
| Alaska | 13 | 71 |
| Mississippi | 24 | 62 |
| Delaware | 6 | 56 |
| South Dakota | 15 | 51 |
| Maine | 9 | 44 |
| Montana | 10 | 43 |
| Kentucky | 13 | 40 |
| Wyoming | 11 | 27 |
| Vermont | 4 | 18 |
| West Virginia | 7 | 10 |
| New Hampshire | 7 | 8 |
| Rhode Island | 1 | 1 |

## Method

Each region was researched by two agents working in parallel — one on public
museums plus a town-by-town discovery sweep, one on base collections and
monuments — against the source hierarchy in `data/_research/brief_template.md`.
The two lists were then reconciled by `data/_research/run_region.py`, which
collapses duplicate site entries by name-stem and by coordinate proximity,
normalises every row, merges duplicate airframes, blanks any serial that
collides with an existing record, separates new sites from top-ups onto museums
already in the database, and dry-runs the whole batch before applying it.

Import order matters and is enforced by the runner: dry-run museums → apply
museums → dry-run every aircraft batch → apply. Aircraft resolve their museum by
exact name and a dry run creates nothing, so aircraft cannot be validated until
the museums actually exist.

Verification after import: every one of the 537 site records was read back from
the live API and its aircraft count compared with its CSV row count. **Zero
mismatches, zero missing sites.** Database totals moved by exactly the number of
rows applied.

## Two bugs found and fixed in the pipeline

- **Coordinate dedup was dropping aircraft.** When two research passes entered
  one site under two names at the same coordinates, the runner kept one site
  record and silently discarded the other's aircraft — 20 rows in New England
  alone. The surviving site now inherits the merged name's rows.
- **Merging ran before normalising.** Normalisation blanks placeholder values and
  rewrites fields, so two rows describing one airframe only become identical
  *after* it. Merging first let the pairs through. Reversed; eight surviving
  duplicates from the earlier order are listed in
  `data/REVIEW_DUPLICATES_SEP2026.md`.

Both fixes are in `data/_research/run_region.py` and matter for every future
region.

## What needs a decision — see `data/REVIEW_DUPLICATES_SEP2026.md`

Nothing was deleted from the live database. Sixteen aircraft records and three
museum records are flagged in their own descriptions and listed in that file
with a ready-to-run `scripts/delete_reviewed_sep2026.sh`. Two of them are
substantive:

- **Aviation Museum of New Hampshire holds no full-size aircraft.** The C-47 in
  its material is the *virtual* aircraft of a flight-simulator programme. The
  only airframe on the property is an EMB-110 nose section.
- **P-51D 44-63615 left Seymour Johnson AFB in April 2016** for the National WWII
  Museum in New Orleans, where it hangs in Tuskegee Red Tail markings. The 2016
  NMUSAF loan list and Baugher both predate the move. It is recorded correctly in
  Louisiana; the North Carolina record is the wrong one.

Also unresolved: **Don F. Pratt Memorial Museum** and **Don F. Pratt Memorial
Museum Air Park** are the same air park at Fort Campbell, entered 700 m apart by
two passes, with nine airframes in both. The museum building closed 22 November
2024 and the Tennessee Wings of Liberty Museum opened outside the gate on 15 May
2026, so which record should survive is a naming decision rather than a merge.

## Coverage that is thin rather than complete

Rhode Island ends with one site and one airframe, New Hampshire with seven
sites and eight, West Virginia with seven sites and ten. Wyoming was thin too
until a dedicated top-up pass found the Museum of Flight and Aerial Firefighting
at Greybull with nine airframes. The top-up agent's WebSearch budget was already
exhausted when it reached NH, RI and WV, and those three states need exactly the
local-news and VFW/Legion-post searching that was unavailable — so treat their
thinness as unproven, not confirmed. A town-by-town HMdb sweep is the cheapest
next step.

Two leads worth a few minutes each: satellite imagery for a reported F-84 at
Blacksville WV (39.721175, -80.200675), and a re-check of Greybull in six to
twelve months — sixteen ex-Hawkins and Powers airframes went to auction there in
2025 and the FAA now shows the survivors registered to a private owner.

## A source-hierarchy addition worth keeping

Aerial Visuals' `AirframeDossier.php?Serial=<id>` carries a **"Latest Owner or
Location"** field that is maintained well past the vintage of its location pages,
which turns Aerial Visuals from an identity-only source into a cheap staleness
test. Dossier ids scrape straight out of `LocationDossier.php`. It overturned
three records in Wyoming alone. Note that Aerial Visuals rate-limits, and a
throttled fetch returns a 102-byte `429` body that parses like a successful
page — 16 of 52 dossiers came back that way in one pass and would have vanished
from the sweep silently.
