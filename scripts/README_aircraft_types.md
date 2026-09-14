# Writing aircraft types through the API

A type is **one write-up per designation**, inherited at render time by every
airframe whose normalized `model` + `variant` matches. There is no foreign key on
`aircraft` and nothing to backfill: a newly imported F-104G inherits the F-104
write-up on its next page load, and deleting a type touches no aircraft row.

This is the reference for adding and revising them by hand. For bulk loading a
researched batch, use `scripts/import_aircraft_types.py`, which is idempotent and
dry-run-first.

## Auth

    export AIRPLANE_BASE_URL=https://airplane.museum
    export AIRPLANE_API_KEY=amt_...          # readwrite creates and edits; admin deletes

    curl -H "Authorization: Bearer $AIRPLANE_API_KEY" ...

## The five things to get right

**1. Write base types.** Omit `variant` and the record serves every variant of the
designation — one `UH-1` covers all 702 of them. Add a variant record (`model`
`T-33`, `variant` `A`) only when that variant genuinely needs different text; it
then wins over the base for those airframes, and everything else still falls back
to the base.

**2. `model` must match what the catalog actually records.** The key is `model` +
`variant`, uppercased, with every non-alphanumeric character dropped. `("F-4","C")`
and `("F-4C",null)` both land on `F4C` — correct, since the importer has recorded
that designation both ways. Check before writing:

    curl -s "$AIRPLANE_BASE_URL/api/v1/aircraft-types/resolve?model=T-33&variant=A"

`matched_on` comes back as `variant`, `base`, or null. A null tells you the
designation string you assumed is not the one in the data — which is how a
write-up ends up reaching nothing.

**3. Do not set `manufacturer_scope`.** The key ignores manufacturer on purpose: a
Fuji-built UH-1H is still a UH-1H and wants Bell's write-up, and 791 of 4,877
designations here carry more than one manufacturer spelling for that reason.
Scoping an ordinary type strips it from every licence-built airframe.

Set it only where an unrelated aircraft shares the designation *string* — `S-2` is
52 Grumman Trackers and also 10 Pitts biplanes; `47` and `737` are bare numbers.
A scoped type never applies to an airframe it does not match, so the Pitts shows
nothing rather than the Tracker text. Matching is normalized prefix in either
direction, so `Bell` accepts `Bell Helicopter`.

**4. Set `spec_basis` whenever you publish a figure.** A base type covers every
variant but its numbers cannot: a T-33A and a T-33SF are not the same aeroplane on
paper. The page prints "Figures below describe the T-33A." above the spec block.
Max 100 characters — a bare variant designation, not a sentence.

**5. Paragraphs are `\n\n`.** The card splits the description on blank lines. A
single `\n` does nothing.

## Create

`model`, `display_name` and `description` are required; everything else is
optional.

    curl -X POST "$AIRPLANE_BASE_URL/api/v1/aircraft-types" \
      -H "Authorization: Bearer $AIRPLANE_API_KEY" \
      -H "Content-Type: application/json" \
      -d @my-type.json

With `my-type.json` (see `data/aircraft_types/TEMPLATE.json` for a blank one):

    {
      "model": "T-33",
      "display_name": "Lockheed T-33 Shooting Star",
      "manufacturer": "Lockheed",
      "model_name": "Shooting Star",
      "also_built_by": "Canadair, Kawasaki",
      "origin_country": "US",
      "description": "First paragraph.\n\nSecond paragraph.",
      "aircraft_type": "fixed_wing",
      "role_type": "trainer",
      "wing_type": "monoplane",
      "military_civilian": "military",
      "spec_basis": "T-33A",
      "first_flight_year": 1948,
      "number_built": 6557,
      "crew": "2",
      "engines": "1 x Allison J33-A-35 turbojet",
      "length_m": 11.51, "wingspan_m": 11.85, "height_m": 3.56,
      "max_speed_kmh": 966, "range_km": 2052, "ceiling_m": 14630,
      "wikipedia_url": "https://en.wikipedia.org/wiki/Lockheed_T-33",
      "is_published": true
    }

Vocabularies, all identical to an aircraft record:

| field | values |
|---|---|
| `aircraft_type` | `fixed_wing` `rotary_wing` `lighter_than_air` `spacecraft` `missile_rocket` |
| `military_civilian` | `military` `civilian` |
| `wing_type` | `monoplane` `biplane` `triplane` — null for helicopters |
| `role_type` | `bomber` `transport` `recon` `electronic_warfare` `fighter` `tanker` `search_rescue` `ground_attack` `utility` `trainer` `test` `drone` |

Units are metric throughout: `length_m` / `wingspan_m` / `height_m` in metres
(main rotor diameter goes in `wingspan_m` for a helicopter), `max_speed_kmh`,
`range_km`, `ceiling_m`. `origin_country` is ISO 3166-1 alpha-2 of the country of
**design**, not the operator.

## Revise

PUT is a partial update — send only what changes. This is the normal way to edit
prose you have rewritten:

    curl -X PUT "$AIRPLANE_BASE_URL/api/v1/aircraft-types/42" \
      -H "Authorization: Bearer $AIRPLANE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"description": "Rewritten first paragraph.\n\nAnd the second."}'

Before revising a base type, see how far the edit reaches:

    curl -s "$AIRPLANE_BASE_URL/api/v1/aircraft-types/42" | jq .inherits_count

Changing `model`, `variant` or `manufacturer_scope` moves the entire inheriting
set and rebuilds the slug. That is how you fix a typo'd designation, but it is not
a small edit.

## Draft and publish

`is_published: false` keeps a record editable in admin and off every public page.
It is the reversible way to pull a write-up; DELETE is not.

    curl -X PUT ".../aircraft-types/42" -d '{"is_published": false}'    # hide
    curl -X PUT ".../aircraft-types/42" -d '{"is_published": true}'     # restore

Anonymous `GET` returns published records only. Any authenticated identity sees
drafts too, so you can stage a batch and publish it once you have read it back.

## Responses you should expect

| code | meaning |
|---|---|
| 201 | created; the body is the full record including `id`, `slug` and `match_key` |
| 400 | missing `model` / `display_name` / `description`, or a number that would not parse |
| 401 / 403 | no key, or a key without `readwrite` (create/edit) or `admin` (delete) |
| 409 | this designation and scope already exist; the body carries `existing_id` |

A 409 is the useful one: a repeated POST is safe to retry as a PUT against
`existing_id`, which is exactly what `import_aircraft_types.py` does.

## Finding what to write next

    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/type_coverage.py --worklist 50

Reports the share of airframes currently inheriting a write-up and ranks the
uncovered designations by how many pages each would light up. `--json` emits the
worklist ready to seed a research run.

Two cautions on that list. It does not yet model `manufacturer_scope`, so its
number reads slightly high where a scoped type exists. And a designation near the
top may be an **alias of something already written** rather than a gap: `AT-6` and
`SNJ` are the T-6, `CL-13` is the Canadair F-86, `Su-17` is the Su-22, and a Bell
`205` is a commercial UH-1. Resolve it first before writing a fourth description
of the same aeroplane.
