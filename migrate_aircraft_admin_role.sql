-- New role: aircraft_admin
--
-- Has full CRUD on aircraft, museums, exhibits, and templates (everything
-- the 'admin' role can do for data) but cannot manage users or other users'
-- API keys. Use this role for content stewards who shouldn't have access
-- to authentication/authorization controls.

USE airplane_museum_tracker;

ALTER TABLE users
    MODIFY COLUMN role ENUM('admin', 'aircraft_admin', 'manager', 'viewer')
        NOT NULL DEFAULT 'viewer';
