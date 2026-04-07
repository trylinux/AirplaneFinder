# Aircraft Museum Tracker

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
