-- Drop the ambiguous `on_loan` value from aircraft_museum.display_status.
--
-- BACKGROUND
--   `on_loan` conflated two opposite perspectives:
--     - curator at owning museum: "we lent it out — not viewable here"
--     - curator at borrowing museum: "we borrowed it — viewable here"
--   Same value, opposite meanings. Visitors had no way to tell which.
--
-- NEW SEMANTICS
--   `display_status` is now strictly the *visitor's* answer to
--   "can I see this aircraft at this museum?" The allowed values are:
--     on_display         — viewable
--     in_storage         — present but not viewable
--     under_restoration  — present but not viewable
--
--   A museum that has loaned an aircraft out should simply delete the
--   link row (or never create one). A borrowing museum creates the link
--   as `on_display`. Anything more nuanced goes in `notes`.
--
-- MIGRATION
--   Any pre-existing `on_loan` rows get folded into `on_display`. Curators
--   can re-classify to `in_storage` / `under_restoration` after the fact
--   if needed. (In our seed data there are zero `on_loan` rows.)

-- Step 1: fold any existing on_loan rows.
UPDATE aircraft_museum
   SET display_status = 'on_display'
 WHERE display_status = 'on_loan';

-- Step 2: tighten the ENUM so the DB itself rejects on_loan going forward.
-- Safe to run because step 1 leaves zero rows using the value. If this
-- ALTER fails, check first: SELECT COUNT(*) FROM aircraft_museum WHERE
-- display_status='on_loan' should be 0.
ALTER TABLE aircraft_museum
  MODIFY COLUMN display_status
  ENUM('on_display','in_storage','under_restoration')
  DEFAULT 'on_display';

-- The API-level allowlist in app.py (_DISPLAY_STATUS_VALUES) gives a
-- nicer error message than the ENUM check, but having both is the
-- belt-and-suspenders that catches a direct SQL write bypassing the API.
