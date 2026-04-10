-- Migration: User Management Enhancements
-- Run against existing airplane_museum_tracker database
-- Safe to re-run (uses IF NOT EXISTS / column existence checks)

USE airplane_museum_tracker;

-- Add last_login_ip to users (tracks IP behind Nginx via X-Forwarded-For)
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'users' AND COLUMN_NAME = 'last_login_ip');
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE users ADD COLUMN last_login_ip VARCHAR(45) DEFAULT NULL AFTER last_login',
    'SELECT "last_login_ip already exists"');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

-- Add last_logout to users
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'users' AND COLUMN_NAME = 'last_logout');
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE users ADD COLUMN last_logout TIMESTAMP NULL DEFAULT NULL AFTER last_login_ip',
    'SELECT "last_logout already exists"');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

-- Add contribution_count to users
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'users' AND COLUMN_NAME = 'contribution_count');
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE users ADD COLUMN contribution_count INT DEFAULT 0 NOT NULL AFTER last_logout',
    'SELECT "contribution_count already exists"');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

-- Add key_prefix to api_keys (stores first 12 chars of raw key for identification)
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'api_keys' AND COLUMN_NAME = 'key_prefix');
SET @sql = IF(@col_exists = 0,
    'ALTER TABLE api_keys ADD COLUMN key_prefix VARCHAR(16) DEFAULT NULL AFTER key_hash',
    'SELECT "key_prefix already exists"');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
