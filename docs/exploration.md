# Airframe histories, museum map, and trip planning

## Install / upgrade

Fresh databases use `schema.sql`. For an existing database, apply the additive
migration before starting the updated application (use the database/user from
`web.config` or your environment):

```sh
mysql -u YOUR_DB_USER -p airplane_museum_tracker < migrate_airframe_history.sql
```

The migration creates `aircraft_history_events`; it does not alter current
registrations, aircraft records, or museum assignments. `CREATE TABLE IF NOT
EXISTS` makes it safe to rerun on an installation with the same table definition.
Restart the Flask/Gunicorn process after deploying the updated files. On the
systemd installation documented in the README:

```sh
sudo systemctl restart airplanefinder
```

Historical research is entered separately; existing descriptions are not converted
into invented milestones. The initial public history is empty until entries are
published by an editor.

## Individual airframe history

Aircraft details link to `/aircraft/{id}/history`. Aircraft management's edit dialog
links to `/admin/aircraft/{id}/history`. Both work on desktop and mobile.

Each milestone belongs to the stable aircraft ID, so editing its current tail
number does not detach its history. Fields:

- Required `title` (200 characters), and either `source_name` (citation, 300
  characters) or `source_url` (HTTP/HTTPS, 1000 characters).
- `event_type`: built, delivered, service, registration, transfer, restoration,
  retirement, display, or other (default).
- `description` (10,000 characters), `operator` and `location` (200 each),
  historical `registration` (80 characters).
- Optional integer `event_year`, `event_month`, `event_day`. Omit unknown parts.
  A day requires month/year; a month requires year. Dates must be valid and years
  between 1 and 9999. Year-only entries stay year-only.
- Boolean `is_approximate` (default false) and `is_published` (default true).

Dated entries sort chronologically; undated entries follow. Drafts appear only
in the protected management API/editor, even if an administrator uses the public
history page. These are sourced historical events, independent of current exhibit
status or registration. They do not automatically move an aircraft between museums.

| API route | Access |
|---|---|
| GET `/api/v1/aircraft/{id}/history` | Public, published entries only |
| GET `/api/v1/aircraft/{id}/history/manage` | `readwrite`, includes drafts |
| POST `/api/v1/aircraft/{id}/history` | `readwrite` |
| PUT/PATCH `/api/v1/history/{event_id}` | `readwrite`, partial edits |
| DELETE `/api/v1/history/{event_id}` | `admin` data permission |

The existing account-role cap applies to keys. Managers and data admins may edit
shared aircraft histories; only data admins delete entries. Deleting an airframe
also deletes its history; deleting an author preserves the entries and clears
that author reference. Creation and edits retain author IDs and timestamps, and
writes are recorded in the application change log.

## Conventional museum map

`/map` complements the museum directory and globe. It has small steady markers,
counted clusters, street-level zoom, collection links, region/text filters, and
“Search this area.” At maximum zoom a group of colocated museums opens a list.
“Show all matches” restores the full current filter result. Cards are progressively
revealed in groups of 30; marker data is not limited to those first 30 cards.
Museums without coordinates are listed separately.

GET `/api/v1/museums/map` accepts `q`, `region`, and `country`. The response contains
`results` (located museums), `no_coordinates`, and `total`. Each museum includes
`aircraft_count`, counting only `on_display` exhibit links. The endpoint returns
all matches without pagination so the map can filter the viewport consistently.

Leaflet 1.9.4 and its BSD license are bundled under `static/vendor/leaflet`.
Map backgrounds default to OpenStreetMap's standard tiles. Configuration:

| Environment | `web.config` key | Default |
|---|---|---|
| `MAP_TILE_URL` | `[map] tile_url` | `https://tile.openstreetmap.org/{z}/{x}/{y}.png` |
| `MAP_ATTRIBUTION` | `[map] attribution` | Linked OpenStreetMap copyright attribution |

Attribution is trusted administrator-configured HTML and remains visible on the
map. Use HTTPS for an external provider. Standard OSM tiles are a best-effort
service; obey their attribution/caching policy, and do not add offline downloads
or prefetching. Automated browser tests use local fixture tiles rather than OSM.
See the [OSM tile usage policy](https://operations.osmfoundation.org/policies/tiles/)
and [Leaflet documentation](https://leafletjs.com/examples/quick-start/).

Device location requires browser permission and HTTPS or localhost. The production
Permissions-Policy permits same-origin geolocation while disabling unused device
APIs. A denied location or tile failure leaves search/list access available.

## Aircraft-focused trip planner

`/trips` starts from aircraft search, map discovery, or an aircraft's “Plan a visit”
link. Visitors can select a specific airframe by ID or any example of a model.
Model targets match manufacturer plus base model, across variants. They do not
use loose text search to decide whether a wanted aircraft is covered.

The first version supports:

- 1–12 unique aircraft/model targets; duplicates are collapsed.
- Starting city/postal code, a 1–5000-mile radius (default 500), 1–8 museum stops
  (default 5), and an optional return to start.
- Museums with coordinates and matching aircraft recorded as `on_display`.
- Explanations for unmatched targets: missing catalog data, unavailable exhibits,
  missing coordinates, outside the radius, or the stop limit.
- Numbered stops, matching airframes, museum/history links, and driving-directions
  links. Long itineraries split into chunks with at most three intermediate
  waypoints for mobile browser compatibility.
- Up to 10 named plans saved in this browser's local storage. Saving the same
  name replaces that plan. There is no account sync. Loading a saved plan checks
  the current catalog again, rather than treating old display status as current.

The algorithm first picks the museum covering the most remaining targets, breaking
ties by straight-line distance from the previous choice. It then orders the chosen
stops by the nearest next stop from the origin. This is a heuristic, not a global
shortest-route solver. Radius and mileage use straight-line distance. Dashed lines
show stop order, not roads. Road travel time, opening hours, ferries, and border
crossings are not calculated; users can review actual routes in Maps and museum
visitor information before travelling.

POST `/api/v1/trips/plan` is public with the normal session CSRF requirement and
an IP rate limit of 30 requests per minute. It has no account write side effects.
Example JSON body:

```json
{
  "origin": {"location": "Dayton, Ohio, United States"},
  "targets": [
    {"kind": "model", "manufacturer": "Boeing", "model": "B-17"},
    {"kind": "airframe", "aircraft_id": 1}
  ],
  "radius_miles": 500,
  "max_stops": 5,
  "round_trip": true
}
```

The API also accepts `origin: {latitude, longitude}`. The sample aircraft ID is
illustrative: callers must use an ID from their actual catalog. Responses include
`origin`, normalized `targets`, ordered `stops` (museum, airframes, covered target
indexes, leg mileage), `unmatched`, `no_coordinates`, return/total mileage,
`distance_basis: "straight_line"`, and the algorithm `method`.

[Google Maps URLs](https://developers.google.com/maps/documentation/urls/get-started)
provide the external directions handoff without an API key. This application does
not fetch or store road routes from Google.
