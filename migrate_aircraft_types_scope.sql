-- ─────────────────────────────────────────────────────────────────────
-- aircraft_types.manufacturer_scope
--
-- Run AFTER migrate_aircraft_types.sql. Additive: one nullable column,
-- no existing row changed, and NULL (the default for every existing row)
-- preserves exactly the behaviour those rows already had.
--
-- Why it exists. The type join is deliberately manufacturer-agnostic,
-- because a designation identifies an aircraft regardless of who built it
-- -- that is what lets a Fuji-built UH-1H inherit Bell's write-up, and
-- 791 of 4,877 designations in this collection carry more than one
-- manufacturer spelling for exactly that reason.
--
-- A few designation STRINGS, though, are reused by unrelated aircraft:
--
--   S-2   52 Grumman Trackers, 10 Pitts biplanes, 3 Ayres cropdusters
--   T-38  63 Northrop Talons, 2 Slingsby gliders
--   47    Bell 47 -- a bare number that would match anything spelled "47"
--   737   same problem
--   T-6   129 North American Texans, 2 Sukhoi T-6 (the Su-24 prototype)
--
-- Without this column an S-2 write-up would land on 14 wrong pages.
-- Setting manufacturer_scope restricts a type to airframes whose
-- manufacturer matches, and a scoped type NEVER applies to one it does
-- not match -- so a Pitts S-2 correctly shows nothing rather than
-- falling through to the Grumman text. Matching is by normalized prefix
-- in either direction, so scope "Bell" accepts "Bell Helicopter".
-- manufacturer_matches() in models.py is authoritative.
--
-- Leave it NULL for everything else. Scoping a type that does not need it
-- silently strips the write-up from every licence-built airframe, which is
-- the exact failure this feature was designed to avoid.
-- ─────────────────────────────────────────────────────────────────────

USE airplane_museum_tracker;

-- '' rather than NULL for "unscoped", because the uniqueness rule below is
-- (match_key, manufacturer_scope) and MySQL counts every NULL as distinct in
-- a UNIQUE index -- a nullable column would accept two unscoped F-104
-- write-ups and leave the page choosing between them arbitrarily.
ALTER TABLE aircraft_types
    ADD COLUMN manufacturer_scope VARCHAR(100) NOT NULL DEFAULT '' AFTER slug;

-- Replace the designation-only key. A Grumman S-2 and a Pitts S-2 are two
-- legitimate records; two unscoped S-2s are not.
ALTER TABLE aircraft_types
    DROP INDEX uq_type_match,
    ADD UNIQUE KEY uq_type_match (match_key, manufacturer_scope);
