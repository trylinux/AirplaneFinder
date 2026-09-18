-- Add fields used by registration verification and password-reset session
-- invalidation. Safe to re-run: every schema change is guarded.
--
-- Resolve every address reported by the duplicate query before continuing.
-- MySQL's normal utf8mb4 collation compares addresses case-insensitively.

USE airplane_museum_tracker;

UPDATE users SET email = NULL WHERE email IS NOT NULL AND TRIM(email) = '';

SELECT LOWER(TRIM(email)) AS duplicate_email, COUNT(*) AS accounts
  FROM users
 WHERE email IS NOT NULL AND TRIM(email) <> ''
 GROUP BY LOWER(TRIM(email))
HAVING COUNT(*) > 1;

SET @has_verified := (SELECT COUNT(*) FROM information_schema.COLUMNS
                        WHERE TABLE_SCHEMA = DATABASE()
                          AND TABLE_NAME = 'users'
                          AND COLUMN_NAME = 'email_verified_at');
SET @sql := IF(@has_verified = 0,
    'ALTER TABLE users ADD COLUMN email_verified_at TIMESTAMP NULL DEFAULT NULL AFTER email',
    'SELECT ''email_verified_at already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

SET @has_required := (SELECT COUNT(*) FROM information_schema.COLUMNS
                        WHERE TABLE_SCHEMA = DATABASE()
                          AND TABLE_NAME = 'users'
                          AND COLUMN_NAME = 'email_verification_required');
SET @sql := IF(@has_required = 0,
    'ALTER TABLE users ADD COLUMN email_verification_required BOOLEAN NOT NULL DEFAULT FALSE AFTER email_verified_at',
    'SELECT ''email_verification_required already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

SET @has_auth_version := (SELECT COUNT(*) FROM information_schema.COLUMNS
                            WHERE TABLE_SCHEMA = DATABASE()
                              AND TABLE_NAME = 'users'
                              AND COLUMN_NAME = 'auth_version');
SET @sql := IF(@has_auth_version = 0,
    'ALTER TABLE users ADD COLUMN auth_version INT NOT NULL DEFAULT 0 AFTER password_hash',
    'SELECT ''auth_version already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

SET @has_email_uq := (SELECT COUNT(*) FROM information_schema.STATISTICS
                        WHERE TABLE_SCHEMA = DATABASE()
                          AND TABLE_NAME = 'users'
                          AND INDEX_NAME = 'uq_users_email');
SET @sql := IF(@has_email_uq = 0,
    'ALTER TABLE users ADD UNIQUE KEY uq_users_email (email)',
    'SELECT ''uq_users_email already present''');
PREPARE s FROM @sql; EXECUTE s; DEALLOCATE PREPARE s;

SELECT COLUMN_NAME, IS_NULLABLE, COLUMN_DEFAULT
  FROM information_schema.COLUMNS
 WHERE TABLE_SCHEMA = DATABASE()
   AND TABLE_NAME = 'users'
   AND COLUMN_NAME IN ('email_verified_at', 'email_verification_required', 'auth_version');
