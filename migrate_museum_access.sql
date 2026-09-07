-- Add museums.access_type.
--
-- Why this exists: the app answers "where can I go and see it". Some of
-- the largest airframe collections in the country are inside the wire —
-- NAS Fallon's Heritage Air Park has roughly 25 aircraft and Nellis AFB's
-- Freedom Park has eight, and neither is reachable without a DoD ID or a
-- sponsored escort. Idaho's Gowen Field air park is the same story, a mile
-- from a museum that IS public. Before this column the only options were to
-- omit them (losing real, documented airframes) or to list them as if a
-- visitor could turn up (sending people to a gate they can't pass).
--
-- Values:
--   public       walk in during opening hours
--   appointment  call ahead, by arrangement, or open-house only
--   restricted   military base, escort, DoD ID, or otherwise closed to
--                the general public
--
-- Everything already in the table predates the column and was researched
-- under a public-access assumption, so 'public' is the correct backfill.
-- Sites needing another value are corrected individually afterwards.
--
-- Safe to re-run: the ADD COLUMN is guarded, the backfill is idempotent.

SET @ddl = (
    SELECT IF(
        COUNT(*) = 0,
        "ALTER TABLE museums
             ADD COLUMN access_type ENUM('public','appointment','restricted')
                 NOT NULL DEFAULT 'public' AFTER website,
             ADD INDEX idx_access (access_type)",
        "SELECT 'museums.access_type already present' AS note"
    )
    FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME   = 'museums'
      AND COLUMN_NAME  = 'access_type'
);
PREPARE stmt FROM @ddl;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Belt and braces: NOT NULL DEFAULT 'public' already fills existing rows,
-- but an earlier hand-run of the ALTER without the default would not have.
UPDATE museums SET access_type = 'public'
 WHERE access_type IS NULL OR access_type = '';

SELECT access_type, COUNT(*) AS museums
  FROM museums GROUP BY access_type ORDER BY access_type;
