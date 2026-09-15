-- ─────────────────────────────────────────────────────────────────────
-- aircraft_type_aliases
--
-- Run AFTER migrate_aircraft_types.sql and migrate_aircraft_types_scope.sql.
-- Purely additive: one new table. No existing row is read or changed, and
-- an empty table resolves exactly as the code did before it existed.
--
-- Why it exists. Type resolution joins on a normalized designation string,
-- which is right for punctuation and case ("MiG-21" / "MIG 21" / "Mig21")
-- and blind to the fact that aviation gives one aeroplane several names:
--
--   AT-6, SNJ            North American T-6 Texan
--   CF-104, TF-104       Lockheed F-104 Starfighter
--   CL-13                Canadair-built F-86 Sabre
--   Lim-1/2/5/6, S-102   licence-built MiG-15 and MiG-17
--   Su-17, Su-20         export designations of the Su-22 family
--   204, 205, 212, 214   Bell's commercial numbers for the UH-1
--
-- Those airframes are catalogued under whichever designation is painted on
-- them, so they miss the write-up that describes them. The alternative to
-- this table is writing the same description forty-five more times.
--
-- An alias is a second match_key pointing at an existing type. It touches
-- no aircraft row, adds no text, and is superseded automatically if a real
-- type for that designation is written later (resolve_for() ranks a real
-- record above an alias at the same specificity).
--
-- manufacturer_scope works exactly as it does on aircraft_types, and
-- matters MORE here: several of these aliases are bare numbers. "204" is
-- scoped to Bell, so it never lands on an unrelated airframe spelled 204.
-- An alias must ALSO satisfy the scope of the type it points at -- it is a
-- second door into a type, not a way around its scope.
-- ─────────────────────────────────────────────────────────────────────

USE airplane_museum_tracker;

CREATE TABLE IF NOT EXISTS aircraft_type_aliases (
    id                 INT AUTO_INCREMENT PRIMARY KEY,
    type_id            INT          NOT NULL,

    -- The alternate designation as written ("AT-6", "CF-104", "Lim-2").
    -- Stored whole rather than split into model/variant: an alias only ever
    -- needs to produce a match_key, and a split would be a second place for
    -- the join rule to drift away from the one aircraft rows use.
    designation        VARCHAR(100) NOT NULL,
    match_key          VARCHAR(120) NOT NULL,
    manufacturer_scope VARCHAR(100) NOT NULL DEFAULT '',

    FOREIGN KEY (type_id) REFERENCES aircraft_types(id) ON DELETE CASCADE,
    -- One alias designation per scope. Without this, two unscoped aliases
    -- for "SNJ" could point at two different types and the page would pick
    -- between them arbitrarily -- the same failure uq_type_match prevents.
    -- NOT NULL for the same reason: MySQL counts NULLs as distinct here.
    UNIQUE KEY uq_type_alias_match (match_key, manufacturer_scope),
    INDEX idx_type_alias_type (type_id)
) ENGINE=InnoDB;
