-- ─────────────────────────────────────────────────────────────────────
-- Aircraft types — shared, inherited type information
--
-- One write-up per designation, inherited by every airframe that matches.
-- Replaces the pattern of pasting the same paragraph onto hundreds of
-- Aircraft rows: 372 T-33As, 328 UH-1Hs and 199 F-104Gs in this database
-- all want the same answer to "what is this aeroplane".
--
-- The join is match_key — model+variant uppercased with everything that
-- isn't a letter or a digit removed — and is deliberately NOT scoped by
-- manufacturer. 791 of 4,877 designations here carry more than one
-- manufacturer spelling, and most are licence builders rather than typos:
-- Fuji UH-1, Kawasaki T-33, HAL MiG-21, Aeritalia F-104. Those are the
-- same type and inherit the same text; the airframe keeps its own builder.
--
-- Resolution is two-tier at render time, not a foreign key on aircraft:
-- an exact model+variant type wins, a variant-NULL base type catches the
-- rest. Nothing to backfill, and a newly imported airframe inherits on the
-- next page load. See AircraftType.resolve_for() in models.py.
--
-- Safe to re-run. Changes no existing table and no existing row:
-- aircraft.description keeps holding per-airframe research notes, which
-- is a different thing and stays where it is.
-- ─────────────────────────────────────────────────────────────────────

USE airplane_museum_tracker;

CREATE TABLE IF NOT EXISTS aircraft_types (
    id                INT AUTO_INCREMENT PRIMARY KEY,

    -- Designation this type describes. variant NULL = the base type, the
    -- fallback for every variant without a record of its own.
    model             VARCHAR(50)  NOT NULL,
    variant           VARCHAR(50)  DEFAULT NULL,
    -- Normalized model+variant, maintained by the application rather than
    -- generated: the test suite runs on SQLite, which cannot compile the
    -- MySQL string functions this would need, and the rule is clearer read
    -- as Python (type_match_key() in models.py, which is authoritative).
    match_key         VARCHAR(120) NOT NULL,
    slug              VARCHAR(120) NOT NULL,

    -- manufacturer here is the ORIGINAL designer, shown as provenance.
    -- The airframe keeps its own builder, so a Fuji-built UH-1H still
    -- reads "Fuji" in its own spec table while inheriting Bell's write-up.
    display_name      VARCHAR(200) NOT NULL,
    manufacturer      VARCHAR(100) DEFAULT NULL,
    model_name        VARCHAR(200) DEFAULT NULL,
    also_built_by     VARCHAR(300) DEFAULT NULL,
    origin_country    CHAR(2)      DEFAULT NULL,

    description       TEXT         NOT NULL,

    aircraft_type     ENUM('fixed_wing','rotary_wing','lighter_than_air','spacecraft','missile_rocket')
                       NOT NULL DEFAULT 'fixed_wing',
    role_type         VARCHAR(30)  DEFAULT NULL,
    wing_type         ENUM('monoplane','biplane','triplane') DEFAULT NULL,
    military_civilian ENUM('military','civilian') NOT NULL DEFAULT 'military',

    first_flight_year INT          DEFAULT NULL,
    introduced_year   INT          DEFAULT NULL,
    retired_year      INT          DEFAULT NULL,
    number_built      INT          DEFAULT NULL,
    -- Which variant the figures below describe. A base type covers every
    -- variant but its numbers cannot, so the spec block says whose they are.
    spec_basis        VARCHAR(100) DEFAULT NULL,
    crew              VARCHAR(60)  DEFAULT NULL,
    engines           VARCHAR(200) DEFAULT NULL,
    length_m          DECIMAL(6,2) DEFAULT NULL,
    wingspan_m        DECIMAL(6,2) DEFAULT NULL,
    height_m          DECIMAL(6,2) DEFAULT NULL,
    max_speed_kmh     INT          DEFAULT NULL,
    range_km          INT          DEFAULT NULL,
    ceiling_m         INT          DEFAULT NULL,

    source_name       VARCHAR(300)  DEFAULT NULL,
    source_url        VARCHAR(1000) DEFAULT NULL,
    wikipedia_url     VARCHAR(1000) DEFAULT NULL,

    -- Unpublished types stay editable in admin and never reach a public page.
    is_published      BOOLEAN   NOT NULL DEFAULT TRUE,
    created_by        INT       DEFAULT NULL,
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL,
    -- One write-up per designation. This is the constraint that makes the
    -- whole feature work: it is what stops two half-finished F-104
    -- descriptions from both existing and the page picking arbitrarily.
    UNIQUE KEY uq_type_match (match_key),
    UNIQUE KEY uq_type_slug  (slug),
    INDEX idx_type_model     (model),
    INDEX idx_type_published (is_published)
) ENGINE=InnoDB;
