-- Rewrite full_designation to join model + variant the way aviation does.
--
-- Before: CONCAT(model, '-', variant)  ->  "SR-71-A", "F-4-C", "B-52-D"
-- After:  three cases                  ->  "SR-71A",  "F-4C",  "B-52D"
--
--   model ends in a digit, variant starts with a letter -> no separator
--       SR-71 + A   = SR-71A        (2,673 rows)
--   variant starts with a digit                          -> a dash
--       747   + 100 = 747-100, FJ + 1 = FJ-1   (418 rows)
--   both sides alphabetic                                -> a space
--       Vampire + T.35 = Vampire T.35           (241 rows)
--
-- The column is STORED, so MySQL recomputes every row during the ALTER and
-- rebuilds idx_full_desig. On ~5,000 rows that is quick, but it does take a
-- metadata lock — run it during a quiet moment.
--
-- Nothing else needs changing: uq_model_tail is (model, tail_number) and is
-- untouched. Searches that used to match the literal "SR-71-A" will now match
-- "SR-71A"; the model column still matches "SR-71" either way.
--
-- The readable statement of this rule is join_designation() in models.py.
-- Keep the two in agreement.

USE airplane_museum_tracker;

-- Have a look before and after; both should return the same row count.
SELECT COUNT(*) AS rows_with_a_variant FROM aircraft WHERE variant IS NOT NULL AND variant <> '';

ALTER TABLE aircraft
    MODIFY COLUMN full_designation VARCHAR(100) GENERATED ALWAYS
        AS (CONCAT(model, CASE
              WHEN variant IS NULL OR variant = '' THEN ''
              WHEN LOCATE(LEFT(variant, 1), '0123456789') > 0 THEN CONCAT('-', variant)
              WHEN LOCATE(RIGHT(model, 1), '0123456789') > 0 THEN variant
              ELSE CONCAT(' ', variant)
            END)) STORED;

-- Spot-check: one of each case.
SELECT model, variant, full_designation
  FROM aircraft
 WHERE (model = 'SR-71' AND variant = 'A')
    OR (model = '747')
    OR (variant REGEXP '^[A-Za-z]' AND model REGEXP '[A-Za-z]$')
 LIMIT 10;
