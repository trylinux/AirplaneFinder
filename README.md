# Aircraft Finder

A Flask web application for tracking which aircraft are displayed at which aviation museums worldwide, with proximity search to find the nearest museum with a given aircraft.

## Prerequisites

- Python 3.9+
- MySQL 8.0+ (or MariaDB 10.6+)

## Setup

### 1. Create the database

```bash
mysql -u root -p < schema.sql
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment (optional)

```bash
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=yourpassword
export MYSQL_DB=airplane_museum_tracker
export SECRET_KEY=your-secret-key-here
```

### 4. Seed sample data

```bash
python seed_data.py
```

This creates a default admin account and prints an API key. Save the API key for programmatic access.

### 5. Run the application

```bash
python app.py
```

Visit **http://localhost:5000** in your browser.

## Features

- **Aircraft Search** -- search by tail number, model, variant (e.g. C-130J vs C-130H), name, or manufacturer
- **Museum Directory** -- browse and filter museums by region or country
- **International Support** -- museums from any country; coordinates are optional
- **Proximity Search** -- enter an aircraft and zip/postal code or city to find the nearest museum with that aircraft
- **Admin Panel** -- login-protected panel with full CRUD: list/create/edit/delete for aircraft, museums, and exhibit links
- **REST API** -- versioned JSON API (`/api/v1/`) with Bearer token authentication
- **API Key Management** -- generate, list, and revoke API keys from the web UI
- **API Documentation** -- built-in interactive docs at `/api/v1/docs`

## Authentication

### Web UI

Session-based authentication via Flask-Login. Register at `/register` or use the seeded admin account. The admin panel and API key management pages require login.

### REST API

Bearer token authentication. Include your API key in the `Authorization` header:

```
Authorization: Bearer amt_your_api_key_here
```

Three permission levels:

| Level | Can do |
|-------|--------|
| `read` | Search, view details, proximity lookups (public endpoints also work without a key) |
| `readwrite` | All of read, plus create and update records |
| `admin` | All of readwrite, plus delete records |

Generate API keys from the web UI at `/admin/api-keys`, or the first key is printed when you run `seed_data.py`.

## API Endpoints (v1)

All endpoints are prefixed with `/api/v1/`.

### Public (no auth required)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/aircraft/search?q=` | Search aircraft |
| GET | `/aircraft/{id}` | Aircraft detail with museums |
| GET | `/museums/search?q=&region=&country=&state=` | Search museums |
| GET | `/museums/{id}` | Museum detail with aircraft |
| GET | `/museums/regions` | List regions with counts |
| GET | `/museums/countries` | List countries with counts |
| GET | `/nearest?aircraft=&location=` | Find nearest museum |
| GET | `/stats` | Dashboard counts |
| GET | `/docs` | API documentation page |

### Authenticated (readwrite)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/aircraft` | Create aircraft |
| PUT | `/aircraft/{id}` | Update aircraft |
| POST | `/museums` | Create museum |
| PUT | `/museums/{id}` | Update museum |
| POST | `/exhibits` | Link aircraft to museum |
| PUT | `/exhibits/{id}` | Update exhibit |

### Authenticated (admin)

| Method | Endpoint | Description |
|--------|----------|-------------|
| DELETE | `/aircraft/{id}` | Delete aircraft |
| DELETE | `/museums/{id}` | Delete museum |
| DELETE | `/exhibits/{id}` | Delete exhibit link |

### Key Management (session auth)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/keys` | List your API keys |
| POST | `/keys` | Generate new API key |
| DELETE | `/keys/{id}` | Revoke an API key |

## Museum Data Model

Museums now support international locations:

| Field | Required | Notes |
|-------|----------|-------|
| `name` | Yes | Museum name |
| `city` | Yes | City |
| `state_province` | No | State, province, county, etc. |
| `country` | Yes | Country name (defaults to "United States") |
| `postal_code` | No | Zip/postal code (format varies by country) |
| `region` | Yes | North America, Europe, Asia-Pacific, Middle East, South America, Africa, Oceania |
| `address` | No | Full street address |
| `website` | No | URL |
| `latitude` | No | Decimal degrees (for proximity search) |
| `longitude` | No | Decimal degrees (for proximity search) |

Museums without coordinates are still searchable and browsable, but won't appear in distance-sorted proximity results. They are listed separately when relevant.

## Example API Usage

```bash
# Search (no auth needed)
curl http://localhost:5000/api/v1/aircraft/search?q=C-130

# Create museum (readwrite key) — only name, city, country, region required
curl -X POST http://localhost:5000/api/v1/museums \
  -H "Authorization: Bearer amt_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"RAF Museum","city":"London","country":"United Kingdom","region":"Europe"}'

# Update museum with coordinates
curl -X PUT http://localhost:5000/api/v1/museums/1 \
  -H "Authorization: Bearer amt_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude":51.5953,"longitude":-0.2376}'

# Delete (admin key only)
curl -X DELETE http://localhost:5000/api/v1/aircraft/42 \
  -H "Authorization: Bearer amt_YOUR_KEY"
```

## Bulk Import

Aircraft and museums can be imported in bulk from CSV or JSON.

**Web UI:** `/admin/import` — file upload or paste, with a Validate (dry-run)
button before the real Import. The page is in the admin nav under
**Bulk Import**.

**API:** `POST /api/v1/aircraft/bulk_import`, `POST /api/v1/museums/bulk_import`.
Either send a multipart `file` upload, or a JSON body of the form

```json
{ "format": "csv" | "json" | "auto",
  "data":   "<the CSV or JSON text>",
  "dry_run": false }
```

The response is a per-row report:

```json
{ "created": 4, "skipped": 0, "errors": [], "dry_run": false }
```

**Rules**

- Permission: `admin` or `aircraft_admin`.
- Cap: 5,000 rows per request. Split larger imports.
- Atomic: any validation error rolls back the whole batch — partial
  imports are too painful to debug after the fact.
- Existing duplicates (same `(model, tail_number)` for aircraft, same
  `(name, city, country)` for museums) are reported as skipped *and*
  cause the batch to roll back. Re-import after removing them.

**Aircraft column / field names** (CSV header order = JSON keys)

`manufacturer`, `model`, `variant`, `tail_number`, `model_name`,
`aircraft_name`, `aircraft_type`, `wing_type`, `military_civilian`,
`role_type`, `year_built`, `description`, `aliases`. Required:
`manufacturer`, `model`. `aliases` in CSV is **semicolon**-separated
(`Herc;Hercules`); in JSON it's an array.

**Museum field names**

`name`, `city`, `state_province`, `country`, `postal_code`, `region`,
`address`, `website`, `latitude`, `longitude`. Required: `name`, `city`,
`region`. `latitude` and `longitude` must both be present or both empty.

Sample files: `scripts/sample_aircraft.csv`, `scripts/sample_museums.csv`.

## Maintenance

### Running the test suite

```bash
pip install -r requirements.txt -r requirements-dev.txt
pytest
```

The suite uses an **in-memory SQLite** database — no MySQL needed locally.
86 tests covering: auth flow (login, logout, lockout, session timeout,
session-fixation defense), role-based access, security hardening (headers,
open-redirect, default-secret guard), the aircraft API regression-prone
paths (link_id, uniqueness, sort whitelist), pure helpers, and the logger
fallback.

Run a single file or test:

```bash
pytest tests/test_auth.py
pytest tests/test_auth.py::TestLogout::test_logout_actually_logs_out_with_remember_cookie -v
```

### Pre-deploy security check

Before each deploy, run:

```bash
bash scripts/security_check.sh
```

This runs **`pip-audit`** against `requirements.txt` to flag any dependencies
with known CVEs in the [PyPI Advisory Database](https://pypi.org/security/),
and prints a summary of outdated packages in your `.venv` for visibility.

The script installs `pip-audit` into a one-shot temporary venv if it isn't
already on your `$PATH`, so it doesn't pollute the app's runtime
environment. Exit code is non-zero on findings, so it can fail a CI pipeline
or a deploy script — wire it in as the first step of whatever you use.

## Project Structure

```
airplane-museum-tracker/
├── app.py              # Flask app: routes, auth, API
├── models.py           # SQLAlchemy models (User, ApiKey, Aircraft, Museum, etc.)
├── config.py           # Configuration
├── schema.sql          # MySQL schema (includes users + api_keys tables)
├── seed_data.py        # Sample data + default admin user/key
├── requirements.txt
├── static/
│   ├── css/style.css
│   └── js/app.js
└── templates/
    ├── base.html       # Layout with auth-aware nav
    ├── index.html      # Dashboard + proximity search
    ├── aircraft.html   # Aircraft directory
    ├── museums.html    # Museum directory
    ├── login.html      # Login page
    ├── register.html   # Registration page
    ├── admin.html      # Admin panel (CRUD)
    ├── api_keys.html   # API key management
    └── api_docs.html   # API documentation
```
