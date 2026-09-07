-- Sourced airframe milestones. Run once on an existing database before deploying
-- the history feature. Existing aircraft and exhibit records are unchanged.
CREATE TABLE IF NOT EXISTS aircraft_history_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aircraft_id INT NOT NULL,
    event_type VARCHAR(30) NOT NULL DEFAULT 'other',
    title VARCHAR(200) NOT NULL,
    description TEXT,
    event_year INT,
    event_month INT,
    event_day INT,
    is_approximate BOOLEAN NOT NULL DEFAULT FALSE,
    operator VARCHAR(200),
    location VARCHAR(200),
    registration VARCHAR(80),
    source_name VARCHAR(300),
    source_url VARCHAR(1000),
    is_published BOOLEAN NOT NULL DEFAULT TRUE,
    created_by INT,
    updated_by INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL,
    FOREIGN KEY (updated_by) REFERENCES users(id) ON DELETE SET NULL,
    INDEX ix_aircraft_history_events_aircraft_id (aircraft_id)
) ENGINE=InnoDB;
