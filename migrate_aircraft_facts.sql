-- Add the aircraft_facts table.
--
-- Backs the /facts page (random aviation trivia), the /admin/facts
-- management screen, and the /api/v1/facts endpoints.
--
-- DESIGN NOTES
--   aircraft_id is NULLABLE and ON DELETE SET NULL.
--     Most facts are general aviation trivia with no single airframe to
--     attach to. Where a fact IS about a specific aircraft, the link lets
--     it surface on that aircraft's detail page. SET NULL rather than
--     CASCADE because deleting an aircraft record should not silently
--     delete the writing about it — the fact stays, it just becomes a
--     general one.
--
--   is_active lets a disputed fact be hidden without losing the text.
--     The public endpoints filter on it; the admin page does not.
--
--   created_by is SET NULL so removing a user doesn't erase their
--     contributions, consistent with how contribution_count works.
--
-- Safe to re-run: CREATE TABLE IF NOT EXISTS.

USE airplane_museum_tracker;

CREATE TABLE IF NOT EXISTS aircraft_facts (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    fact        TEXT         NOT NULL,
    source_url  VARCHAR(500) DEFAULT NULL,
    aircraft_id INT          DEFAULT NULL,
    is_active   BOOLEAN      NOT NULL DEFAULT TRUE,
    created_by  INT          DEFAULT NULL,
    created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(id) ON DELETE SET NULL,
    FOREIGN KEY (created_by)  REFERENCES users(id)    ON DELETE SET NULL,
    INDEX idx_fact_aircraft (aircraft_id),
    INDEX idx_fact_active   (is_active)
) ENGINE=InnoDB;

-- A few starter facts so the page isn't empty on first load. Each is
-- checkable; none is tied to a specific airframe.
INSERT INTO aircraft_facts (fact, source_url) VALUES
('The SR-71 Blackbird leaked fuel on the ground. Its panels were deliberately loose-fitting, sealing only once friction heating expanded the airframe at speed.', 'https://www.lockheedmartin.com/en-us/news/features/history/blackbird.html'),
('The Boeing B-52 has been in continuous service since 1955, and the Air Force expects it to fly past 2050 — a service life approaching a century.', 'https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104465/b-52-stratofortress/'),
('The Convair B-36 Peacemaker used six piston engines mounted backwards as pushers, plus four jet engines: crews described it as "six turning, four burning".', 'https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/195800/convair-b-36j-peacemaker/'),
('The Lockheed U-2 is so difficult to land that a second pilot chases it down the runway in a high-performance car, calling out altitude over the radio.', 'https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104560/u-2s-tu-2s/'),
('The Harrier''s ability to hover comes from four rotating nozzles that redirect engine thrust downwards — a system called thrust vectoring in forward flight.', 'https://www.nasm.si.edu/'),
('Wright Flyer flights in December 1903 were shorter than the wingspan of a modern Boeing 747.', 'https://airandspace.si.edu/collection-objects/1903-wright-flyer/'),
('The Antonov An-225 Mriya, the heaviest aircraft ever built, had six engines and 32 wheels. Only one was ever completed.', 'https://www.antonov.com/'),
('A Cessna 172 Skyhawk has been in production longer than any other aircraft in history — first delivered in 1956 and still built today.', 'https://cessna.txtav.com/');
