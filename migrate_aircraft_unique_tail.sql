-- Aircraft (model, tail_number) uniqueness
--
-- Backstop for the API-level duplicate check: if two readwrite clients race
-- to create the same airframe at the same time, the API check could both
-- pass and the database would end up with duplicates. The UNIQUE INDEX
-- below stops that.
--
-- IMPORTANT: MySQL/MariaDB allow multiple NULLs through a UNIQUE index, so
-- aircraft without a tail number (NULL) won't collide with each other —
-- which is what we want. Empty-string tails ARE constrained, so the API
-- normalizes "" to NULL before insert/update; existing rows with empty
-- strings should be cleaned up first.

USE airplane_museum_tracker;

-- 1. Find any pre-existing duplicates so you know what to fix BEFORE the
--    index addition fails. Run this and address each row before continuing.
--
--    SELECT model, tail_number, COUNT(*) AS n
--      FROM aircraft
--      WHERE tail_number IS NOT NULL AND tail_number <> ''
--      GROUP BY model, tail_number
--      HAVING n > 1;

-- 2. Normalize empty-string tail numbers to NULL so the unique index
--    treats "no tail" rows as non-colliding.
UPDATE aircraft SET tail_number = NULL WHERE tail_number = '';

-- 3. Add the constraint.
ALTER TABLE aircraft
  ADD UNIQUE INDEX uq_model_tail (model, tail_number);
