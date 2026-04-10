-- Aircraft Museum Tracker - MySQL Schema
-- Run this to set up the database

CREATE DATABASE IF NOT EXISTS airplane_museum_tracker
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE airplane_museum_tracker;

-- ─────────────────────────────────────────────
-- Users (admin login for web UI)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS users (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    username        VARCHAR(80)  NOT NULL UNIQUE,
    email           VARCHAR(200) DEFAULT NULL,
    password_hash   VARCHAR(256) NOT NULL,
    role            ENUM('admin','manager','viewer') NOT NULL DEFAULT 'viewer',
    is_active       BOOLEAN      DEFAULT TRUE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- API Keys (token auth for programmatic access)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS api_keys (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT          NOT NULL,
    key_hash    VARCHAR(256) NOT NULL,
    label       VARCHAR(100) NOT NULL DEFAULT 'default',
    is_active   BOOLEAN      DEFAULT TRUE,
    permissions VARCHAR(50)  DEFAULT 'read',       -- 'read', 'readwrite', 'admin'
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_used   TIMESTAMP    NULL DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_key_hash (key_hash)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- User ↔ Museum assignments (scoped access)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_museum_assignments (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT NOT NULL,
    museum_id   INT NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)  REFERENCES users(id)   ON DELETE CASCADE,
    FOREIGN KEY (museum_id) REFERENCES museums(id) ON DELETE CASCADE,
    UNIQUE KEY uq_user_museum (user_id, museum_id)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- User ↔ Country assignments (scoped access)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_country_assignments (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT NOT NULL,
    country     VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY uq_user_country (user_id, country)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- Museums (international support)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS museums (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(200)  NOT NULL,
    city            VARCHAR(100)  NOT NULL,
    state_province  VARCHAR(100)  DEFAULT NULL,      -- state, province, county, etc.
    country         VARCHAR(100)  NOT NULL DEFAULT 'United States',
    postal_code     VARCHAR(20)   DEFAULT NULL,       -- optional; format varies by country
    region          VARCHAR(50)   NOT NULL,            -- North America, Europe, Asia-Pacific, etc.
    address         VARCHAR(300)  DEFAULT NULL,
    website         VARCHAR(300)  DEFAULT NULL,
    latitude        DECIMAL(10,7) DEFAULT NULL,        -- nullable: not all museums have geocoords
    longitude       DECIMAL(10,7) DEFAULT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_region  (region),
    INDEX idx_country (country),
    INDEX idx_state   (state_province),
    INDEX idx_postal  (postal_code)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- Aircraft
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS aircraft (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    tail_number     VARCHAR(20)  DEFAULT NULL,
    model_name      VARCHAR(200) DEFAULT NULL,     -- type/model common name, e.g. "Cobra", "Hercules"
    aircraft_name   VARCHAR(200) DEFAULT NULL,     -- individual aircraft name, e.g. "Daisy Duke", "Bockscar"
    manufacturer    VARCHAR(100) NOT NULL,
    model           VARCHAR(50)  NOT NULL,         -- base designation, e.g. "AH-1", "C-130"
    variant         VARCHAR(50)  DEFAULT NULL,     -- e.g. "D", "J", "H"
    full_designation VARCHAR(100) GENERATED ALWAYS
                     AS (CONCAT(model, IFNULL(CONCAT('-', variant), ''))) STORED,
    aircraft_type   ENUM('fixed_wing','rotary_wing','lighter_than_air','spacecraft')
                     NOT NULL DEFAULT 'fixed_wing',
    wing_type       ENUM('monoplane','biplane','triplane') DEFAULT NULL,
    military_civilian ENUM('military','civilian') NOT NULL DEFAULT 'military',
    role_type       VARCHAR(30)  DEFAULT NULL,        -- depends on military_civilian
                    -- Military: bomber, transport, recon, electronic_warfare, fighter,
                    --           tanker, search_rescue, ground_attack
                    -- Civilian: commercial_transport, freighter, private, experimental,
                    --           space, other
    year_built      INT          DEFAULT NULL,
    description     TEXT         DEFAULT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_tail       (tail_number),
    INDEX idx_model      (model),
    INDEX idx_variant    (variant),
    INDEX idx_full_desig (full_designation),
    FULLTEXT idx_ft_search (model_name, aircraft_name, model, variant, tail_number, manufacturer)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- Aircraft aliases (alternate names / search terms)
-- e.g. B-29 → "B29", "Superfortress"
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS aircraft_aliases (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    aircraft_id INT NOT NULL,
    alias       VARCHAR(200) NOT NULL,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(id) ON DELETE CASCADE,
    INDEX idx_alias (alias)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- Junction: which aircraft are at which museums
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS aircraft_museum (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    aircraft_id INT NOT NULL,
    museum_id   INT NOT NULL,
    display_status ENUM('on_display','in_storage','on_loan','under_restoration') DEFAULT 'on_display',
    notes       TEXT DEFAULT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(id) ON DELETE CASCADE,
    FOREIGN KEY (museum_id)   REFERENCES museums(id)  ON DELETE CASCADE,
    UNIQUE KEY uq_aircraft_museum (aircraft_id, museum_id)
) ENGINE=InnoDB;

-- ─────────────────────────────────────────────
-- Geocoding table for proximity lookups
-- Stores zip/postal codes and city names with coordinates
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS zip_codes (
    zip_code    VARCHAR(20) PRIMARY KEY,
    city        VARCHAR(100) NOT NULL,
    state       VARCHAR(100) NOT NULL,
    country     VARCHAR(100) NOT NULL DEFAULT 'United States',
    latitude    DECIMAL(10,7) NOT NULL,
    longitude   DECIMAL(10,7) NOT NULL,
    INDEX idx_city (city),
    INDEX idx_country (country)
) ENGINE=InnoDB;
