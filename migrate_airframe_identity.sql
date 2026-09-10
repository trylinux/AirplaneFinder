-- Replace UNIQUE (model, tail_number) with a key that can tell national
-- serial systems apart, and give the aircraft table the two identity fields
-- that made the old key wrong.
--
-- ─────────────────────────────────────────────────────────────────────────
-- WHY
-- ─────────────────────────────────────────────────────────────────────────
-- uq_model_tail said: one model may carry a given tail number once, anywhere
-- on earth. That is false. Serial numbers are national, and short ones repeat
-- constantly:
--
--   Mirage F1CZ  207  (SAAF, Swartkop)   vs  Mirage F1C-200 207  (Le Bourget)
--   MiG-15       "03" (Aden)             vs  MiG-15UTI      "03" (Monino)
--   F-86F        709  (Saudi)            vs  F-86F          709  (elsewhere)
--
-- The importer's only escape was to blank the tail number, and it took it:
-- 99 of 1,072 Russian airframes (9%) went in with no tail at all because
-- Soviet bort numbers are two or three digits and repeat endlessly. Every one
-- of those is a real, known, recorded serial that the schema threw away.
--
-- ─────────────────────────────────────────────────────────────────────────
-- WHAT CHANGES
-- ─────────────────────────────────────────────────────────────────────────
-- The key becomes (full_designation, tail_number, operator_country).
--
--   full_designation instead of model. Already a STORED generated column, so
--     this is free. It alone separates F1CZ from F1C-200 and MiG-15 from
--     MiG-15UTI — the two cases above that need no new data at all.
--
--   operator_country, new. ISO 3166-1 alpha-2 of the operator whose marks the
--     airframe wears — SAAF is ZA, not the country it is displayed in. This is
--     what separates Saudi 709 from any other F-86F 709.
--
--     Alpha-2 and not a country name, deliberately: museums.country holds free
--     text ("Côte d'Ivoire"), which is right for an address and useless in a
--     key. "USA" / "United States" / "US" as three spellings would defeat the
--     constraint entirely. Two letters, validated by shape, or NULL.
--
--   construction_number, new. The manufacturer's c/n or msn — the only
--     genuinely unique airframe identifier there is, and until now it was
--     being stuffed into the aliases column (Puma c/n 1044, SF.260 343/29-037,
--     Aero Commander 680-537-206). It is NOT in the unique key: c/n is
--     transcribed inconsistently across sources and a fourth mostly-NULL
--     column would gut the constraint, since MySQL treats any NULL as
--     distinct. It is indexed and used by the application's duplicate finder
--     as a strong signal, which is where judgement belongs.
--
-- NULL still means unknown and still never collides. That is unchanged and is
-- why this migration cannot fail on existing data: every current row keeps a
-- NULL operator_country, so the new key is strictly weaker than the old one
-- until the backfill runs. Nothing that fits today stops fitting.
--
-- ─────────────────────────────────────────────────────────────────────────
-- ORDER OF OPERATIONS
-- ─────────────────────────────────────────────────────────────────────────
-- Run this, then backfill operator_country, then recover the blanked tails.
-- Recovering tails BEFORE the country backfill will collide.
--
-- Safe to re-run: every statement is guarded.

USE airplane_museum_tracker;

-- ── 1. Where we are now ────────────────────────────────────────────────────
SELECT COUNT(*) AS total_airframes,
       SUM(tail_number IS NULL) AS without_a_tail
  FROM aircraft;

-- ── 2. The two new identity columns ────────────────────────────────────────
SET @add_cn := (SELECT COUNT(*) FROM information_schema.COLUMNS
                 WHERE TABLE_SCHEMA = DATABASE()
                   AND TABLE_NAME = 'aircraft'
                   AND COLUMN_NAME = 'construction_number');
SET @sql := IF(@add_cn = 0,
    'ALTER TABLE aircraft ADD COLUMN construction_number VARCHAR(50) DEFAULT NULL AFTER variant',
    'SELECT ''construction_number already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

SET @add_oc := (SELECT COUNT(*) FROM information_schema.COLUMNS
                 WHERE TABLE_SCHEMA = DATABASE()
                   AND TABLE_NAME = 'aircraft'
                   AND COLUMN_NAME = 'operator_country');
SET @sql := IF(@add_oc = 0,
    'ALTER TABLE aircraft ADD COLUMN operator_country CHAR(2) DEFAULT NULL AFTER construction_number',
    'SELECT ''operator_country already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

-- ── 3. Index the construction number, scoped by manufacturer ───────────────
-- Not unique. A c/n is unique within a manufacturer in principle, but not in
-- transcription, and a bad UNIQUE here would block honest imports.
SET @add_ix := (SELECT COUNT(*) FROM information_schema.STATISTICS
                 WHERE TABLE_SCHEMA = DATABASE()
                   AND TABLE_NAME = 'aircraft'
                   AND INDEX_NAME = 'idx_mfr_cn');
SET @sql := IF(@add_ix = 0,
    'ALTER TABLE aircraft ADD INDEX idx_mfr_cn (manufacturer, construction_number)',
    'SELECT ''idx_mfr_cn already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

-- ── 4. Swap the unique key ─────────────────────────────────────────────────
-- Add the new one first. If it fails, the old key is still standing and the
-- database is unchanged — which is the point of doing it in this order.
SET @add_uq := (SELECT COUNT(*) FROM information_schema.STATISTICS
                 WHERE TABLE_SCHEMA = DATABASE()
                   AND TABLE_NAME = 'aircraft'
                   AND INDEX_NAME = 'uq_airframe');
SET @sql := IF(@add_uq = 0,
    'ALTER TABLE aircraft ADD UNIQUE KEY uq_airframe (full_designation, tail_number, operator_country)',
    'SELECT ''uq_airframe already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

SET @drop_uq := (SELECT COUNT(*) FROM information_schema.STATISTICS
                  WHERE TABLE_SCHEMA = DATABASE()
                    AND TABLE_NAME = 'aircraft'
                    AND INDEX_NAME = 'uq_model_tail');
SET @sql := IF(@drop_uq > 0,
    'ALTER TABLE aircraft DROP INDEX uq_model_tail',
    'SELECT ''uq_model_tail already dropped''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

-- ── 5. Confirm ─────────────────────────────────────────────────────────────
SELECT INDEX_NAME, SEQ_IN_INDEX, COLUMN_NAME
  FROM information_schema.STATISTICS
 WHERE TABLE_SCHEMA = DATABASE()
   AND TABLE_NAME = 'aircraft'
   AND INDEX_NAME IN ('uq_airframe', 'uq_model_tail', 'idx_mfr_cn')
 ORDER BY INDEX_NAME, SEQ_IN_INDEX;
