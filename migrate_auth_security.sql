-- Auth security columns
-- Adds failed-login tracking + lockout fields to the users table.
-- Pair this with the Python-side changes in app.py and models.py.

USE airplane_museum_tracker;

ALTER TABLE users
    ADD COLUMN failed_login_count INT NOT NULL DEFAULT 0
        AFTER contribution_count,
    ADD COLUMN locked_until TIMESTAMP NULL DEFAULT NULL
        AFTER failed_login_count;

-- Optional cleanup: clear any stale state for existing accounts (no-op
-- on fresh installs; useful if you re-run the migration on a populated DB).
UPDATE users SET failed_login_count = 0, locked_until = NULL;
