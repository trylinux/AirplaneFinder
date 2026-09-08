# Aircraft Finder

A Flask application for tracking historic aircraft at aviation museums worldwide,
with searchable directories, museum collections, and proximity searches.

## Requirements and setup

- Python 3.9+ and MySQL 8.0+ (or MariaDB 10.6+).
- Browser access to the configured public CDNs for jQuery, Three.js, fonts,
  icons, and globe boundary data. Geolocation requires HTTPS or localhost.

Create a virtual environment and install the application dependencies:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
mysql -u root -p < schema.sql
```

Configuration is read from `web.config` first, then environment variables, then
built-in defaults. Copy `web.config.example` or set the environment:

```bash
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=yourpassword
export MYSQL_DB=airplane_museum_tracker
export SECRET_KEY=replace-with-a-long-random-secret
```

For local development, debug defaults to true and the server uses port 5000:

```bash
.venv/bin/python app.py
```

Open [the local app](http://localhost:5000). For production set `SERVER_DEBUG=false`,
use a non-default secret, serve HTTPS, and install `requirements-prod.txt` for
Gunicorn. Secure session/remember cookies and security headers default to enabled
when debug is false. An explicit value in `web.config` overrides the matching
environment variable.

### First administrator on a fresh database

Create an administrator without loading demonstration data:

```bash
.venv/bin/flask --app app shell
```

In that shell, choose an unused username and enter a password that meets the
policy (at least eight characters, including a letter and a digit):

```python
from getpass import getpass
from models import db, User
from app import _validate_password_strength
password = getpass("Administrator password: ")
assert _validate_password_strength(password) is None
user = User(username="admin", role="admin")
user.set_password(password)
db.session.add(user)
db.session.commit()
exit()
```

### Optional demonstration data

**`seed_data.py` clears existing catalog, account, assignment, and API-key data.**
Run it only against a disposable demonstration database:

```bash
.venv/bin/python seed_data.py
```

It creates sample aircraft and museums, four users (`admin`, two managers, and a
viewer), and prints the generated admin API key and demonstration credentials.
The admin demonstration password is `admin`; change all demonstration passwords
before using that database beyond local testing. Seeding is not an upgrade step.

### Existing databases

`schema.sql` describes a fresh database. `db.create_all()` and `CREATE TABLE IF
NOT EXISTS` do not upgrade existing columns. Review and apply the relevant SQL
migration files for an older installation:

- `migrate_missile_rocket.sql`
- `migrate_display_status_drop_on_loan.sql`
- `migrate_aircraft_facts.sql`
- `migrate_airframe_history.sql`
- `migrate_full_designation.sql`

Apply one with, for example:

```
mysql -u YOUR_DB_USER -p airplane_museum_tracker < migrate_full_designation.sql
```

## Features and views

- **Aircraft directory:** search manufacturer, model, variant, names, tail number,
  or aliases; sort and paginate results; open details and museum locations.
- **Museum directory:** search by name or location, filter by region, sort, and
  view aircraft collections. Country/state filters are also available in the API.
- **Discovery globe:** country borders and labels, US state detail at close zoom,
  steady markers, hover/tap museum information, drag rotation, button/wheel/pinch
  zoom, reset, and pause. Desktop and mobile use the same globe implementation.
- **Proximity:** the dashboard finds museums displaying a specific aircraft;
  the museum directory finds nearby museums by typed location. `/near-me`
  supports device location, a typed location, a radius, collections, and directions.
- **Facts and contributors:** aviation facts at `/facts`; contributor rankings at
  `/contributors`.
- **Management:** aircraft, museums, exhibit links, reusable aircraft templates,
  facts, CSV/JSON bulk import, API keys, and administrator user management.
- **Mobile:** dedicated public templates and responsive management pages. Museum
  editing works on phones; login and role requirements are the same on every device.
  The fixed Home, Aircraft, Museums, Near Me, and Facts tabs also appear on
  management pages and desktop layouts at widths up to 900px.
  `?desktop=1` forces the desktop layout for the session; `?desktop=0` clears that
  override and resumes user-agent detection. `/desktop-only` is a legacy redirect
  to `/admin`.

Public aircraft/museum details request `visible_only=true`, so visitors see only
`on_display` exhibits. `in_storage` and `under_restoration` remain available in
management views and unfiltered detail API responses. Dashboard `link_count` and
globe aircraft counts include only `on_display` links. Museums without coordinates
remain searchable; `/nearest` and `/museums/nearby` return them separately, while
`/museums/nearest` and the globe require coordinates.

## Histories, street map, and trip planning

Aircraft details now link to sourced individual airframe histories. Editors can
add dated or approximate milestones, retain source citations, and publish drafts.
The museum directory links to `/map`, a conventional map with clustered markers
and area search, and `/trips` finds museum stops for several wanted aircraft.
Trips can target a specific airframe or any example of a model, and saved plans
stay in the current browser. Distances are straight-line estimates; external
directions provide road navigation.

Existing installations must apply `migrate_airframe_history.sql` before using
the new history pages. See [the feature and upgrade guide](docs/exploration.md)
for commands, map provider configuration, API fields, permissions, and limitations.

## Authentication and permissions

Web sessions use Flask-Login. Registration creates a viewer account. Management
pages require login; the write APIs enforce role and museum scope. Session writes
need a CSRF token, sent as `X-CSRFToken` by the UI.

| User role | Capabilities |
|---|---|
| `viewer` | Public catalog reads; own account and read-only API keys |
| `manager` | Create/update shared aircraft, templates and facts; create museums; edit assigned museums and their exhibit links |
| `aircraft_admin` | Full catalog CRUD and bulk import, including all museums; own account and keys |
| `admin` | All catalog operations plus user, role, assignment, and other users' key management |

Museum/country assignments restrict managers' museum and exhibit writes.
Aircraft records, facts, and templates are shared catalog data; their write gates
are role-based. Reads are public and are not restricted to assigned museums.

The JSON API accepts Bearer tokens on catalog write endpoints:

```text
Authorization: Bearer amt_your_api_key_here
```

Key permissions are `read`, `readwrite`, or `admin`. Effective access is limited
by both the key permission and its owner's **current** role and scope. Disabling
a user disables their keys; lowering a role also lowers access through old keys.
A supplied invalid Authorization header does not fall back to a logged-in session.
User and key management endpoints require sessions rather than Bearer auth.

Create/revoke your keys at `/account` or `/admin/api-keys`. Raw keys are returned
only at creation. `POST /api/v1/keys` supports `expires_in_days`; omit it for no
expiration. Session idle timeouts default to 15 minutes for admins, 30 for managers
and aircraft admins, and 60 for viewers; the absolute timeout is 12 hours. Login
lockout defaults to five failed attempts for 15 minutes. Password policy defaults
to eight characters including a letter and a digit.

## API overview

All paths below are prefixed with `/api/v1`. The built-in
[API documentation](http://localhost:5000/api/v1/docs) includes a complete route
index generated from the running application, plus field and query descriptions.

| Public GET endpoint | Purpose |
|---|---|
| `/aircraft/search` | Aircraft search with `q`, pagination, and sorting |
| `/aircraft/{aircraft_id}` | Aircraft detail; optional `visible_only=true` |
| `/museums/search` | `q`, `region`, `country`, `state`, pagination, sorting |
| `/museums/{museum_id}` | Museum collection; optional `visible_only=true` |
| `/museums/regions`, `/museums/countries` | Region/country counts |
| `/museums/globe` | Museums with coordinates and on-display aircraft counts |
| `/museums/nearby` | Typed `location`, optional `region`; limit 10 by default, maximum 50 |
| `/museums/nearest` | `lat`/`lon` or `location`, optional `radius` in miles; limit 10 by default, maximum 50 |
| `/nearest` | Required `aircraft` and `location`; optional `museum`; limit 5 by default, maximum 25 |
| `/exhibits` | All exhibit links; optional `q`, `sort_by`, `sort_dir` |
| `/templates`, `/templates/{template_id}` | Aircraft templates; optional `q` on the list |
| `/facts`, `/facts/random` | Facts, optional `aircraft_id`; list accepts `include_inactive=true` |
| `/contributors`, `/stats`, `/docs` | Rankings, counts, API reference |

Aircraft/museum search returns `{results, total, page, pages}`. The default page
size is `RESULTS_PER_PAGE` (20); the per-request `per_page` cap is 100. Request
successive pages for the complete result set. `sort_dir` is `asc` or `desc`;
unsupported `sort_by` values use default ordering. Museum sort fields include
`name`, `city`, `state_province`, `country`, `region`, and `id`; aircraft fields
include designation, names, manufacturer, type, class, role, year, and ID.

| Write endpoints | Required key permission / corresponding session role |
|---|---|
| POST `/aircraft`, `/museums`, `/exhibits`, `/templates`, `/facts` | `readwrite`; manager or data admin, subject to museum scope |
| PUT or PATCH `/aircraft/{aircraft_id}`, `/museums/{museum_id}`, `/exhibits/{link_id}`, `/templates/{template_id}`, `/facts/{fact_id}` | `readwrite`; partial updates, subject to scope |
| DELETE on those same detail paths | `admin`; admin or aircraft_admin |
| POST `/aircraft/bulk_import`, `/museums/bulk_import` | `admin`; admin or aircraft_admin |

| Session endpoints | Access |
|---|---|
| GET/POST `/keys`, DELETE `/keys/{key_id}` | Own keys; admins may revoke others' keys |
| GET `/users`, GET `/users/{user_id}` | Admin sees all; other users see only themselves |
| POST `/users`, PUT/PATCH/DELETE `/users/{user_id}` | Admin only; cannot delete your own account |
| GET/POST `/users/{user_id}/keys` | Own keys or admin managing another user |

Send JSON objects for API writes. `is_active` and `dry_run` are JSON booleans,
not strings. Legacy `/api/...` aliases remain for older clients and templates;
new clients should use `/api/v1/...`.

## Museum fields

Create requests require `name`, `city`, `country`, and `region`. Museum bulk import
defaults omitted/empty `country` to `United States`. Other fields are
`state_province`, `postal_code`, `address`, `website`, `access_type`, `latitude`, and
`longitude`.

Valid regions are `North America`, `Europe`, `Asia`, `Asia-Pacific`, `Middle East`,
`South America`, `Africa`, and `Oceania`.

`access_type` records whether an ordinary visitor can get in: `public` (walk in),
`appointment` (call ahead or open-house only), or `restricted` (military base,
escort or DoD ID required). It defaults to `public`, so museum CSVs written before
the column existed import unchanged. Proximity endpoints — `/api/v1/nearest` and
`/api/v1/museums/nearest` — omit `restricted` museums by default, since the app
answers "where can I go and see it"; pass `include_restricted=1` to include them.
Restricted museums remain fully searchable and still serve their detail pages. Supply both coordinates or neither;
latitude must be -90 through 90 and longitude -180 through 180. Zero is a valid
coordinate. Partial edits validate the resulting coordinate pair.

```bash
curl 'http://localhost:5000/api/v1/aircraft/search?q=C-130'

curl -X POST http://localhost:5000/api/v1/museums \
  -H 'Authorization: Bearer amt_YOUR_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"name":"RAF Museum","city":"London","country":"United Kingdom","region":"Europe"}'
```

## Bulk Import

Aircraft and museums can be imported in bulk from CSV or JSON.

**Web UI:** `/admin/import` — file upload or paste, with a Validate (dry-run)
button before the real Import. The page is in the admin nav under
**Bulk Import**.

**API:** `POST /api/v1/aircraft/bulk_import`, `POST /api/v1/museums/bulk_import`.
Either send a multipart `file` upload, or a JSON body of the form

```json
{ "format": "csv",
  "data":   "<the CSV or JSON text>",
  "dry_run": false }
```

`format` accepts `csv`, `json`, or `auto`. The response is a per-row report:

```json
{ "created": 4, "linked": 4, "skipped": 0, "errors": [], "dry_run": false }
```

`linked` counts how many rows also produced a museum exhibit link (see the
link columns below).

**Rules**

- Permission: `admin` or `aircraft_admin`.
- Cap: 5,000 rows per request and `MAX_CONTENT_LENGTH` bytes (1 MiB by default). Split larger imports.
- Rate limit: `BULK_IMPORT_RATE_LIMIT`, default **200 per hour**. A
  multi-file load (one file per museum, plus a dry run) is easily 80+
  requests, so the old 10/hour cap returned `429 Too Many Requests` — an
  HTML error page, not a JSON report, which reads like a failed import
  rather than throttling. Raise it in `config.py` or via the
  `BULK_IMPORT_RATE_LIMIT` env var if you need more.
- Atomic: any validation error rolls back the whole batch — partial
  imports are too painful to debug after the fact.
- Both dry runs and imports check existing duplicates: `(model, tail_number)`
  for aircraft with known tail numbers, and `(name, city, country)` for museums.
  Duplicates are reported as skipped and prevent the batch from being written.
  Remove them before importing again.

**Aircraft column / field names** (CSV header order = JSON keys)

`manufacturer`, `model`, `variant`, `tail_number`, `model_name`,
`aircraft_name`, `aircraft_type`, `wing_type`, `military_civilian`,
`role_type`, `year_built`, `description`, `aliases`. Required:
`manufacturer`, `model`. `aliases` in CSV is **semicolon**-separated
(`Herc;Hercules`); in JSON it's an array.

**Optional link columns** — `museum_id`, `museum_name`, `display_status`.
Supplying `museum_id` *or* `museum_name` (not both) also creates the
exhibit link, so one file can say what the aircraft is and where to go see
it. The museum must already exist — import museums first. `museum_name`
matches case-insensitively but must be exact and unambiguous; if two
museums share a name the row errors and tells you their ids.
`display_status` defaults to `on_display` (`in_storage`,
`under_restoration` also valid). An unresolvable museum fails the whole
batch like any other validation error.

**Museum field names**

`name`, `city`, `state_province`, `country`, `postal_code`, `region`,
`address`, `website`, `access_type`, `latitude`, `longitude`. Required: `name`,
`city`, `region`. `latitude` and `longitude` must both be present or both empty.
`access_type` is `public` (the default when omitted), `appointment`, or
`restricted` — see below.

Sample files: `scripts/sample_aircraft.csv`, `scripts/sample_museums.csv`.

## Python Scripts

A small set of CLI tools in `scripts/` that talk to the public REST API.
They depend only on the [`requests`](https://pypi.org/project/requests/)
library — install once: `pip install requests`.

**Configuration** (env vars; flags override)

```
AIRPLANE_BASE_URL    # default http://127.0.0.1:5000
AIRPLANE_API_KEY     # needed for writes; bulk import requires admin-level data access
```

**Tools**

| Script | What it does |
|---|---|
| `airplane_api.py` | Reusable `AirplaneClient` class — used by every script below; also fine to `import` from your own one-offs. |
| `export_aircraft.py` | Dump every aircraft to CSV or JSON in the bulk-import format. |
| `export_museums.py` | Same for museums. |
| `import_data.py` | POST a CSV/JSON file to the bulk-import endpoint with `--dry-run` support. |
| `find_nearest.py` | CLI wrapper for `/api/v1/nearest`. |
| `health_check.py` | Smoke-tests `/api/v1/stats`, exits non-zero on failure. Cron-friendly. |

**Common workflows**

```bash
# Backup the catalog (no API key needed; reads are public)
python3 scripts/export_aircraft.py --format json --out aircraft_backup.json
python3 scripts/export_museums.py  --format json --out museum_backup.json

# Prepare NEW records using the export column format
python3 scripts/export_aircraft.py --format csv --out aircraft.csv
# Replace the exported rows with new aircraft; import inserts, it does not update.
# To edit existing records, use the management UI or PATCH endpoints.
AIRPLANE_API_KEY=amt_... \
    python3 scripts/import_data.py --entity aircraft --file aircraft.csv --dry-run
AIRPLANE_API_KEY=amt_... \
    python3 scripts/import_data.py --entity aircraft --file aircraft.csv

# Quick lookups (no auth)
python3 scripts/find_nearest.py "C-130" "Dayton, OH"

# Cron-friendly status probe (exits 0 on success, non-zero on failure)
* * * * *  python3 /opt/AirplaneFinder/scripts/health_check.py --quiet \
              || curl -s https://status-collector.example.com/airplane-down
```

## Maintenance

### Running the test suite

```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

The suite uses an **in-memory SQLite** database — no MySQL needed locally.
Coverage includes authentication, role/scope enforcement, CRUD and deletion,
imports, public display filtering, proximity, facts, mobile route access, API
contracts, maintenance scripts, and helpers. Get the current test count with
`pytest --collect-only -q`; it changes as regressions are added. Browser checks
use an isolated fixture server: see [tests/browser/README.md](tests/browser/README.md).

Run a single file or test:

```bash
pytest tests/test_auth.py
pytest tests/test_auth.py::TestLogout::test_logout_actually_logs_out_with_remember_cookie -v
```

### Deploying (gunicorn + systemd)

The server runs the app under gunicorn, launched by a systemd unit pointing
at `.venv/bin/gunicorn`. Install the production requirements — **not** just
`requirements.txt`, which deliberately omits gunicorn:

```bash
cd /home/debian/AirplaneFinder
.venv/bin/pip install -r requirements-prod.txt
sudo systemctl restart airplanefinder
```

**If the service dies with `ModuleNotFoundError: No module named 'gunicorn'`,**
the `.venv/bin/gunicorn` launcher exists but its package doesn't. Two usual
causes:

1. The venv was rebuilt from `requirements.txt` alone, so gunicorn was never
   reinstalled.
2. The system Python was upgraded (a Debian dist-upgrade from, say, 3.11 to
   3.13). The venv still has `lib/python3.11/site-packages`, which the new
   interpreter ignores — so *every* package looks missing, and gunicorn is
   simply the first import to fail.

Tell them apart:

```bash
ls /home/debian/AirplaneFinder/.venv/lib/     # which pythonX.Y the venv holds
python3 -V                                    # which the system now has
.venv/bin/python -c "import flask"            # fails too? then it is case 2
```

Case 1 — reinstall into the existing venv:

```bash
.venv/bin/pip install -r requirements-prod.txt
```

Case 2 — the venv is orphaned; rebuild it:

```bash
cd /home/debian/AirplaneFinder
rm -rf .venv
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements-prod.txt
sudo systemctl restart airplanefinder
```

Verify before restarting, so a broken venv fails in your shell rather than
in systemd:

```bash
.venv/bin/gunicorn --version
sudo systemctl status airplanefinder --no-pager
```

### TLS: serve the full certificate chain

**Symptom.** Scripts that talk to `https://airplane.museum` fail with
`CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate`, or curl's
`SSL certificate problem: unable to get local issuer certificate` — while the
site loads fine in a browser.

**Cause.** The server sends only the leaf certificate. Check it:

```bash
echo | openssl s_client -connect airplane.museum:443 -servername airplane.museum \
     -showcerts 2>/dev/null | grep -c 'BEGIN CERTIFICATE'
```

A count of `1` means only one certificate was sent. Check your CA's required
chain; the correct count depends on the certificate issuer. To validate a
downloaded leaf against its intermediate:

```bash
openssl verify -untrusted intermediate.pem leaf.pem      # -> leaf.pem: OK
```

Browsers hide the problem because they fetch the missing intermediate
themselves using the AIA extension. `curl`, `requests` and `urllib` do not —
so this breaks every script while the site looks healthy.

**Fix.** Point the web server at the full chain, not the bare certificate.
Let's Encrypt and most CAs ship both files:

```nginx
ssl_certificate      /etc/ssl/certs/airplane.museum/fullchain.pem;  # not cert.pem
ssl_certificate_key  /etc/ssl/private/airplane.museum/privkey.pem;
```

Apache: `SSLCertificateFile` should be the fullchain, or set
`SSLCertificateChainFile` alongside it. Reload, then re-run the openssl check
above and confirm that the server supplies the required intermediate certificates.

Do **not** work around this with `verify=False`, `curl -k`, or by pinning a
custom CA bundle in the scripts. That disables certificate checking for every
host those scripts talk to, to paper over a one-line server config.

### Pre-deploy security check

Before each deploy, run:

```bash
bash scripts/security_check.sh
```

This runs **`pip-audit`** against `requirements.txt` and `requirements-prod.txt` to flag dependencies
with known CVEs in the [PyPI Advisory Database](https://pypi.org/security/),
and prints a summary of outdated packages in your `.venv` for visibility.

The script installs `pip-audit` into a one-shot temporary venv if it isn't
already on your `$PATH`, so it doesn't pollute the app's runtime
environment. Exit code is non-zero on findings, so it can fail a CI pipeline
or a deploy script — wire it in as the first step of whatever you use.

## Project structure

- `app.py`: Flask routes, session/API auth, validation, imports, and API docs route index.
- `exploration.py`: airframe history, museum-map API, and trip-planning logic.
- `models.py`, `schema.sql`, `migrate_*.sql`: ORM models, fresh schema, and upgrades.
- `config.py`, `web.config.example`: file/environment configuration and defaults.
- `geocoder.py`, `logger.py`: location resolution/cache and structured logs.
- `templates/`: desktop/public and responsive management views; `templates/mobile/`
  contains dedicated phone views. `_admin_nav.html` is the shared management navigation.
- `static/js/app.js`: shared desktop helpers, escaping, sorting, and paginated catalog loading.
- `static/js/museum-globe.js`: shared mobile/desktop globe.
- `static/css/style.css`, `static/css/mobile.css`: responsive shared and phone layouts.
- `scripts/`: API clients, import/export, research conversion, and data maintenance.
- `data/`: catalog CSVs and historical research/source notes; see
  [data/METHODOLOGY.md](data/METHODOLOGY.md).
- `tests/`: pytest regressions and optional Playwright browser checks.
