-- Migration: Quick Wins (API key expiry)
-- Run against existing airplane_museum_tracker database
-- Safe to re-run (uses column existence checks)

USE airplane_museum_tracker;

-- Add expires_at to api_keys (NULL = never expires)
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'api_keys' AND COLUMN_NAME = 'expires_at');
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE api_keys ADD COLUMN expires_at TIMESTAMP NULL DEFAULT NULL AFTER created_at',
    'SELECT "expires_at already exists"');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
