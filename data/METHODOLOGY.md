# How museum data gets researched and loaded

Written down because the process was implicit, and because most of the
rules below exist as a reaction to something that actually went wrong.

---

## Source hierarchy

Always work down this list, and record which rung a fact came from:

1. **A structured feed from the museum itself.** Pima publishes
   `wp-json/wp/v2/museum_aircraft` with per-airframe Manufacturer /
   Designation / Registration / Serial fields. This is the gold standard —
   it gave 98% serial coverage. Always probe for one before scraping.
2. **The museum's own collection pages.** What the placard says is what a
   visitor sees, so it wins on questions of markings and current holdings.
3. **Airframe registries** — aerialvisuals.ca, warbirdregistry.org — for
   resolving a specific serial's history and current location.
4. **Wikipedia**, only to fill gaps, and treated as a lead rather than a
   fact. Its museum lists are frequently years stale.

When sources conflict, the museum's own site wins for "what is here now",
and registries win for "which airframe is this really". Record the
conflict in the region's NOTES.md rather than silently picking one.

## The output contract

Every research pass returns pipe-delimited lines, exactly 13 fields
(14 with an optional `display_status`):

    manufacturer|model|variant|tail_number|model_name|aircraft_name|
    aircraft_type|wing_type|military_civilian|role_type|year_built|
    description|aliases

Rules that matter more than they look:

- **`model` is the base designation, variant goes in its own field.**
  "F-4" + "E", never "F-4E". The generated `full_designation` column
  depends on this.
- **Enum values verbatim.** `aircraft_type`, `military_civilian`,
  `display_status`, and `wing_type` are validated server-side. `role_type`
  is a free-text field; use the role names offered in the admin UI for consistency.
- **`wing_type` only for fixed-wing.** A helicopter with "monoplane" set
  is a data error.
- **Never invent a tail number or a year.** A blank field is honest and
  imports safely; a guessed serial is worse than no serial, because it
  looks authoritative and will collide with the real airframe later.
- **A serial never goes in `year_built`.** Researchers do this constantly;
  the builder now detects and moves it, but the rule stands.

- **`aliases` holds names, not notes.** `aliases` is a separate table that
  is joined into search, so anything put there becomes a search term for
  the airframe. It takes only *other ways of naming this aircraft*:
  alternate designations (`SR-71`, `A-12`), the dashless form of each
  designation (`SR71`, `PT22`, `F16C` — always include it, people search
  without the dash), popular and export names (`Blackbird`, `Harvard`,
  `Lim-5`), block and construction identifiers (`Block 10C`, `c/n 61-226`,
  `BuNo 91188`), and any false serial the airframe visibly wears — the
  bare identifier, never the sentence around it.

- **Everything else goes in `description`.** Provenance, condition,
  ownership, loan status, unit history, sighting dates, markings, the
  reason a serial is doubted: all of it is prose and belongs in
  `description`. If a string has a verb in it, it is not an alias.
  A useful test: would someone type this into a search box to find this
  aircraft? If no, it is a description.

  Wrong: `aliases: stood at VFW Post 382 until the post sold the property`
  Right: `aliases: F-4C; F4C` + `description: stood at VFW Post 382 until
  the post sold the property in 2025`

## Splitting large collections

Anything over ~150 aircraft gets split **by manufacturer initial**
(A–F, G–M, N–Z) and researched in separate passes. Alphabetical splitting
is arbitrary but has two useful properties: the slices are roughly even,
and no aircraft can fall between two of them.

Each pass is told which airframes are already recorded so it can exclude
them at source.

## The build pipeline

    research → build → validate → collision-check → import → verify live

1. **Build.** A generator turns the raw lines into CSV, normalising as it
   goes: literal `"None"` → empty, `model_name` that merely echoes the
   designation → blank, restoration notes in `aliases` → `display_status`,
   prose in `aliases` → `description`, dashless designation variants added,
   serials misfiled in `year_built` → `tail_number`.
2. **Validate** against the *real* importer in tests, not a reimplementation
   of it. If `_validate_aircraft_row` would reject a row, the test fails.
3. **Collision-check** every tail against the live database before shipping.
   The importer is atomic, so one existing row rejects the whole file.
4. **Import** one file per museum, so a bad file can only ever affect that
   museum.
5. **Verify against the live site afterwards.** The dry run catches errors;
   it does not catch *skips*. Twice, a file reported success and imported
   nothing.

## Ordering

**Across museums — biggest gap first.** Aircraft-per-unit-effort, measured
as (real collection size − what's recorded). This is why Pima (5 of 366)
and NMUSAF (8 of 360) came before a whole-state sweep: two museums beat
thirty small ones.

**Within a region — museums before aircraft, always.** Aircraft rows
resolve their museum by name; run them first and every row fails.

**Housekeeping before building into a museum.** Udvar-Hazy had two records;
merging them first avoided splitting 170 aircraft across both.

**Top-ups get diffed first.** Any museum that already has aircraft gets its
live list pulled and subtracted before the file is written.

## Rules learned the hard way

- **Blank tail numbers never collide.** NULL doesn't equal NULL, so a file
  with no serials will duplicate silently on a re-run. USS Midway got
  imported four times this way. Hence `filter_new_aircraft.py`.
- **Guards must fail closed.** An idempotency check that silently disables
  itself when a dependency is missing is worse than no check.
- **An aircraft is in exactly one place.** One record linked to several
  museums is always wrong. Either it's a misattribution, or it's a
  type-level record that should be split into one per museum.
- **Record where an aircraft *is*, not who owns it.** On loan to a museum
  → record it there. On loan *out* → record it where a visitor would find
  it. This app answers "where can I go and see it".
- **`display_status` is the visitor's view.** In storage or under
  restoration means they can't see it, whoever owns it.
- **Exclude what you can't stand behind.** Closed museums, fibreglass
  replicas presented as airframes, aircraft at a different site than the
  museum's mailing address. Every exclusion goes in NOTES.md with a reason
  — an omission that is documented is a finding, not a gap.

## What gets written down

Each region has a `NOTES.md` recording: files and row counts, serial
coverage, every excluded museum with its reason, source conflicts left
unresolved, and anything needing a human to verify on site. That file is
the deliverable as much as the CSVs are — it is what makes the numbers
trustworthy later.
