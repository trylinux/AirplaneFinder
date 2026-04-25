-- Aircraft templates
-- Reusable "type info" records an admin can apply when creating a new Aircraft.
-- Templates describe the aircraft TYPE (manufacturer, model, variant, etc.);
-- per-airframe fields (tail_number, aircraft_name, year_built) stay on Aircraft.

USE airplane_museum_tracker;

CREATE TABLE IF NOT EXISTS aircraft_templates (
    id                 INT AUTO_INCREMENT PRIMARY KEY,
    name               VARCHAR(200) NOT NULL UNIQUE,   -- short label, e.g. "C-130H Hercules"
    manufacturer       VARCHAR(100) NOT NULL,
    model              VARCHAR(50)  NOT NULL,
    variant            VARCHAR(50)  DEFAULT NULL,
    model_name         VARCHAR(200) DEFAULT NULL,       -- type common name
    aircraft_type      ENUM('fixed_wing','rotary_wing','lighter_than_air','spacecraft')
                        NOT NULL DEFAULT 'fixed_wing',
    wing_type          ENUM('monoplane','biplane','triplane') DEFAULT NULL,
    military_civilian  ENUM('military','civilian') NOT NULL DEFAULT 'military',
    role_type          VARCHAR(30)  DEFAULT NULL,
    description        TEXT         DEFAULT NULL,
    created_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at         TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_manufacturer (manufacturer),
    INDEX idx_model        (model)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS aircraft_template_aliases (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    template_id  INT NOT NULL,
    alias        VARCHAR(200) NOT NULL,
    FOREIGN KEY (template_id) REFERENCES aircraft_templates(id) ON DELETE CASCADE,
    INDEX idx_alias (alias)
) ENGINE=InnoDB;
