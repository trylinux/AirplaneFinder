-- Add 'missile_rocket' as an aircraft_type
--
-- Covers air-to-air missiles, ICBMs, cruise missiles, sounding rockets,
-- launch vehicles — anything that flies, isn't crewed, and doesn't fit
-- the existing fixed_wing / rotary_wing / lighter_than_air / spacecraft
-- categories. Discrimination within the category lives in role_type
-- (ballistic, cruise, air_to_air, launch_vehicle, etc.).

USE airplane_museum_tracker;

-- Both Aircraft and AircraftTemplate tables have the same ENUM and need
-- the same change. Order matters only insofar as both must succeed.

ALTER TABLE aircraft
    MODIFY COLUMN aircraft_type
    ENUM('fixed_wing', 'rotary_wing', 'lighter_than_air',
         'spacecraft', 'missile_rocket')
    NOT NULL DEFAULT 'fixed_wing';

ALTER TABLE aircraft_templates
    MODIFY COLUMN aircraft_type
    ENUM('fixed_wing', 'rotary_wing', 'lighter_than_air',
         'spacecraft', 'missile_rocket')
    NOT NULL DEFAULT 'fixed_wing';
