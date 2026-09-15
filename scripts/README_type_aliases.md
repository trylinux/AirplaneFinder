# Aircraft type aliases

## What this pass does

Type resolution joins an airframe to a write-up on a normalized designation
string. That sees through punctuation and case — `MiG-21`, `MIG 21` and
`Mig21` are one type — but not through the fact that aviation gives one
aeroplane several names, and the catalogue records whichever one is painted
on the airframe.

So the T-6 Texan write-up misses 59 AT-6s and 41 SNJs. The F-104 one misses
56 CF-104s. The Vampire one misses 87 airframes filed under de Havilland's
own numbers, DH.100 and DH.115. None of those are different aircraft.

An alias is a second match key pointing at an existing type. It changes no
aircraft row, duplicates no text, and needs no backfill.

**58 aliases across 28 types: +921 airframes, 35.7% → 38.6% coverage.**
That is a third of what fifty newly researched write-ups would buy, for an
afternoon rather than a week.

## The bar for adding one

An alias asserts *this is the same aeroplane under a different name*, and
when that assertion is wrong the failure is silent: a confident write-up
appears on a page it does not belong to, with nothing marking it as a
guess. So the bar is not "plausibly related".

`type_alias_map.py` keeps the rejected cases in `JUDGEMENT` rather than
deleting them, with the reason. A MiG-27 is not a MiG-23 — different nose,
intakes and undercarriage. A Bell 212 is not a UH-1 — twin-engine, so the
spec block would be wrong on every page. A Seafire is not a Spitfire. Those
56, 39 and however many airframes want their own records, and listing them
here is what stops the next person re-deriving the same conclusion.

## Scope

An alias carries its own `manufacturer_scope`, and it matters more here
than on a type, because several aliases are short or generic strings. The
live data says exactly why:

| alias | unscoped would also catch |
|---|---|
| `J-5` | Piper J-5 (5), Auster J-5 (2), Janowski J-5 (1) |
| `205` | LFU 205 |
| `214` | Ikarus 214 |
| `Tomahawk` | Piper PA-38 Tomahawk |
| `Dakota` | Piper PA-28 Dakota |

A bare-number alias without a scope is refused by the API outright. An
alias must also satisfy the scope of the *type* it points at — it is a
second door into a type, never a way around its scope, or the Pitts S-2
exclusion could be defeated by aliasing.

Scope is a prefix match in either direction, so `Bell` accepts `Bell
Helicopter` and `PZL` accepts `PZL-Mielec`. Leave it blank for a
licence-built alias: `Lim-2` is unscoped on purpose, because WSK, PZL,
`WSK PZL-Mielec` and `WSK-Mielec` all appear in the data for the same
aeroplane.

## Running it

```bash
# once, against the live database
mysql -u root -p airplane_museum_tracker < migrate_aircraft_type_aliases.sql

export AIRPLANE_BASE_URL=https://airplane.museum
export AIRPLANE_API_KEY=amt_...

python3 scripts/plan_type_aliases.py       # writes nothing; prints the gain
python3 scripts/apply_type_aliases.py --dry-run
python3 scripts/apply_type_aliases.py      # resumable
python3 scripts/type_coverage.py           # verify
```

`apply` sends one PATCH per *type*, not per alias, and unions with whatever
aliases are already on the record — the API replaces the list it is sent,
so a per-alias loop would have each request clobber the one before it, and
a hand-added alias would be lost. Resume state is
`scripts/applied_type_alias_ids.txt`.

## Adding more

Edit `CONFIRMED` in `scripts/type_alias_map.py` and re-run the plan. It
refuses an alias that collides with a real type, one already owned by a
different type, a duplicate within the map, and a bare number with no
scope; it reports the rest with the airframe count each one actually
reaches, and flags any that reach nothing so a wrong spelling shows up
immediately rather than looking like a success.

A zero-reach alias is not always wrong — `Me 109`, `A4D` and `QF-4` are all
defensive, waiting for an import that spells it that way — but a run with
many zeros usually means the map is using a spelling the catalogue does
not.
