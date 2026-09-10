# Russia — plinth and gate-guard pass

Status: **harvested, geocoded, scoped. Not imported.** The import is blocked
on `migrate_airframe_identity.sql` being applied to the live database — these
are bort-numbered airframes, which is precisely the population the old
`UNIQUE (model, tail_number)` key could not hold.

Harvest date: 10 September 2026.

## What the source is

`russianplanes.net/monument?action=mapGetPoints&mode=json` returns the whole
monument database in one call — 9,657 points, 3.3 MB. Per point: type
(Cyrillic), registration or bort number, construction number, coordinates, a
photo, a contributor's note, and a category.

The category field is the reason this dataset is usable at all. It is the
source's own answer to the project's display-vs-derelict test:

| category | count | meaning | taken? |
|---|---|---|---|
| `monument` | 6,773 | plinthed or displayed | **yes** |
| `stored` | 1,181 | held, not presented | no |
| `ex` | 763 | departed this location | no |
| `parts` | 281 | sections, not airframes | no |
| uncategorised | 659 | — | no |

`ex` deserves a note of its own. No other region in this project has had a
source that says "this airframe used to be here and is not any more." Every
currency problem the project keeps hitting — Gweru's 2006 photographs
uploaded in 2013, the Fort Eustis directory still listing an airframe two
years after it left — is a symptom of not having this field. Here we have it.

## Numbers

Of the 6,773 monuments, 5,585 resolve to a manufacturer and model. The 1,188
that don't are dropped, not guessed: category headers ("другие типы ВС"),
bare question marks, and a long tail of 768 one-off type strings.

Clustered at 250 m — two airframes closer than that are one site:

| | sites | airframes |
|---|---|---|
| Russia, new to the database | **802** | **1,034** |
| Russia, at sites already in the database | 139 | ~700 (mostly already recorded) |
| Bulgaria, Poland, Hungary, Slovakia, Finland, Mongolia, China, Albania, Serbia, Georgia, Romania, Norway, Montenegro | 280 | 705 |

The 802 Russian sites are overwhelmingly single-airframe: 923 of the 1,221
raw Russian clusters hold exactly one aircraft. That is the plinth pattern —
one MiG on a pedestal at the edge of one town — and it is why this body of
records has stayed unbuilt while museum-shaped collections got done first.

Evidence density on the 1,034 new Russian airframes:

* 1,565 of 1,739 raw points carry a bort or registration (90%)
* 887 carry a construction number (51%)
* 1,322 carry a photograph (76%)

That is better per-row evidence than most of what Africa or the Middle East
was built from.

**A crude bounding box put 1,082 sites in Russia. Reverse geocoding cut that
to 802.** The 280 it removed are real sites in thirteen other countries — a
bonus tranche, and a reminder that a bounding box is not a country.

## Decisions

**Bort numbers keep their colour.** `46-красный` becomes `46 Red`, not `46`.
The colour is part of the identity: 46 Red and 46 Blue are two aircraft, and
keeping only the digits is how two airframes become one row. This is also
what the old unique key could not express — 347 of the 1,190 Russian aircraft
rows currently in the database have **no tail number at all**, which is far
worse than the 99 recorded in the backlog.

**Operator country is asserted only from evidence.** A registration prefix
carries it (`CCCP-`, `RA-`, `UR-`, `EW-`, `LZ-`), and a colour-suffixed bort
at a site inside Russia is a Soviet/Russian convention firm enough to use.
Everything else stays blank — 542 of the 1,034. An airframe standing in
Bulgaria was very probably Bulgarian-operated, and "very probably" is not a
source. Under the new key a wrong country is worse than no country: it splits
one airframe into two records rather than merging two into one.

**Construction numbers become a column**, not an alias. 887 of these airframes
have one, and a c/n is the only genuinely unique airframe identifier there is.
They were previously being written into `aliases`, where nothing could use
them.

**Factory article numbers are not variants.** `МиГ-29 (9.13)` is a MiG-29;
the 9.13 is a production article number and belongs in the description.

**Transliteration is the aviation one, not a GOST table.** `Х-22` is Kh-22 and
never X-22; `Ан-2Р` is An-2R and never An-2P; `МиГ-21БИС` is MiG-21bis in
lowercase, because that is what the alias tests compare against.

## Site naming

These sites have no institutional names — they are pedestals, not museums.
Names are constructed on the pattern already used for monument-class sites
elsewhere in the project (`American Legion Post 339 -- Oshkosh`,
`Air Force Roundabout Jos`):

* one airframe: `MiG-17 Monument -- Kursk`
* several: `Kursk Aircraft Monuments`

78 sites collide on that pattern — six separate monument sites in
Komsomolsk-on-Amur, six in Moscow — and were given a second, finer reverse
geocode for a street or district to disambiguate. 66 of the 78 resolved; the
remaining 12 need a human decision. Three sites resolved to no city at all
after two passes and are held back, since `city` is a required field.

## What is deliberately not automated

Whether a given airframe is still there. The `ex` category covers departures
the contributors have noticed, which is a floor and not a ceiling. The
contributor notes (`re`, present on 371 of the Russian sites) carry
relocations, repaints and identity doubts — *"Прежде был в г. Кирсанов"*
(previously at Kirsanov), *"Нанесенная регистрация СССР-20019 борту по факту
не принадлежит"* (the registration painted on this airframe is not actually
its own). These are exactly the kind of thing that must not be machine-
translated into a description and asserted. They are carried through
verbatim, labelled as the source's own note.

## To finish this

1. Apply `migrate_airframe_identity.sql` and deploy the code change.
2. `python3 scripts/harvest_russianplanes.py build` to emit the CSVs.
3. Dry-run each per-oblast batch, then import — the rate limit is 200/hour
   and a dry run costs a call, so batch by oblast rather than by file.
4. The 12 unresolved name collisions and 3 city-less sites need a decision.
5. Then the 280-site non-Russian tranche, which is a separate pass and should
   get its own operator-country research rather than inheriting Russia's.
