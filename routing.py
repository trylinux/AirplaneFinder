"""Road routes for the trip planner via the Google Routes API.

The planner itself (exploration.plan_trip) picks and orders museum stops with
straight-line distances and needs no external service. This module adds the
optional second step: given the ordered points, ask Google for the drivable
route so the map can draw roads and the stop cards can show driving miles and
time. The API key stays server-side — the browser never talks to Google.

Design notes:
- Only stdlib HTTP (urllib). Adding ``requests`` for one endpoint isn't worth
  the dependency.
- Responses are cached in-process, keyed by the rounded point list, for
  ``ROUTES_CACHE_TTL`` seconds. Reloading a saved plan or toggling the
  round-trip box shouldn't cost a second billable request.
- Everything is best-effort. Any failure (no key, quota, network, a leg
  Google can't drive) degrades to the straight-line plan the caller already
  has; the endpoint reports why so the UI can say so.
"""

import json
import logging
import threading
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from config import Config

log = logging.getLogger(__name__)

ROUTES_URL = "https://routes.googleapis.com/directions/v2:computeRoutes"
# Ask only for what we render — the field mask is what Google bills on.
FIELD_MASK = ",".join([
    "routes.distanceMeters",
    "routes.duration",
    "routes.polyline.encodedPolyline",
    "routes.legs.distanceMeters",
    "routes.legs.duration",
    "routes.legs.polyline.encodedPolyline",
])
MAX_POINTS = 10          # 8 stops + origin + optional return
METERS_PER_MILE = 1609.344


class RoutingUnavailable(Exception):
    """No key configured — routing is switched off for this deployment."""


class RoutingError(Exception):
    """Google could not produce a route (bad key, quota, undrivable leg, outage)."""


def is_enabled():
    return bool(getattr(Config, "GOOGLE_MAPS_API_KEY", "") or "")


# ── Polyline decoding ─────────────────────────────────────────────────────

def decode_polyline(encoded, precision=5):
    """Decode a Google encoded polyline into [[lat, lon], ...].

    Standard algorithm: each coordinate is a zig-zag/varint-encoded delta
    from the previous one, in base-64-ish 5-bit chunks offset by 63.
    """
    factor = 10 ** precision
    points, index, lat, lon = [], 0, 0, 0
    length = len(encoded)
    while index < length:
        for axis in ("lat", "lon"):
            result, shift = 0, 0
            while True:
                if index >= length:
                    raise ValueError("Truncated polyline.")
                byte = ord(encoded[index]) - 63
                index += 1
                result |= (byte & 0x1F) << shift
                shift += 5
                if byte < 0x20:
                    break
            delta = ~(result >> 1) if result & 1 else result >> 1
            if axis == "lat":
                lat += delta
            else:
                lon += delta
        points.append([round(lat / factor, precision), round(lon / factor, precision)])
    return points


# ── Cache ─────────────────────────────────────────────────────────────────

_cache = {}
_cache_lock = threading.Lock()
_CACHE_MAX = 512


def _cache_key(points):
    # 4 decimals ≈ 11 m — the same museum geocoded twice still hits.
    return tuple((round(p[0], 4), round(p[1], 4)) for p in points)


def _cache_get(key):
    ttl = int(getattr(Config, "ROUTES_CACHE_TTL", 86400) or 0)
    with _cache_lock:
        entry = _cache.get(key)
        if entry and time.time() - entry[0] < ttl:
            return entry[1]
        _cache.pop(key, None)
        return None


def _cache_put(key, value):
    with _cache_lock:
        if len(_cache) >= _CACHE_MAX:
            oldest = min(_cache, key=lambda k: _cache[k][0])
            _cache.pop(oldest, None)
        _cache[key] = (time.time(), value)


def clear_cache():
    with _cache_lock:
        _cache.clear()


# ── Google call ───────────────────────────────────────────────────────────

def _waypoint(point):
    return {"location": {"latLng": {"latitude": float(point[0]), "longitude": float(point[1])}}}


def _parse_duration(value):
    # Routes API durations are protobuf-style strings like "5432s".
    try:
        return float(str(value).rstrip("s"))
    except (TypeError, ValueError):
        return 0.0


def _post(body, api_key, timeout):
    request = Request(
        ROUTES_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": FIELD_MASK,
        },
        method="POST",
    )
    with urlopen(request, timeout=timeout) as response:   # noqa: S310 — fixed HTTPS URL
        return json.loads(response.read().decode("utf-8"))


def validate_points(points):
    """Normalise a request's point list to [(lat, lon), ...] or raise ValueError."""
    if not isinstance(points, list) or not 2 <= len(points) <= MAX_POINTS:
        raise ValueError(f"Provide between 2 and {MAX_POINTS} points.")
    clean = []
    for item in points:
        if isinstance(item, dict):
            lat, lon = item.get("latitude"), item.get("longitude")
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            lat, lon = item
        else:
            raise ValueError("Each point needs latitude and longitude.")
        for value, limit in ((lat, 90), (lon, 180)):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not -limit <= value <= limit:
                raise ValueError("Each point needs latitude and longitude.")
        clean.append((float(lat), float(lon)))
    return clean


def compute_route(points, *, fetch=None):
    """Driving route through ``points`` in order.

    Returns::

        {"provider": "google", "total_miles": 812.4, "total_minutes": 763,
         "legs": [{"distance_miles": 210.1, "duration_minutes": 198,
                   "points": [[lat, lon], ...]}, ...],
         "points": [[lat, lon], ...]}   # whole route, for drawing

    ``fetch`` is injectable for tests; it receives the request body and must
    return the decoded JSON Google would.
    """
    api_key = getattr(Config, "GOOGLE_MAPS_API_KEY", "") or ""
    if not api_key:
        raise RoutingUnavailable("Road routing is not configured on this server.")
    points = validate_points(points)
    key = _cache_key(points)
    cached = _cache_get(key)
    if cached is not None:
        return {**cached, "cached": True}

    body = {
        "origin": _waypoint(points[0]),
        "destination": _waypoint(points[-1]),
        "travelMode": "DRIVE",
        # TRAFFIC_UNAWARE is the cheapest SKU and deterministic — a museum
        # trip planned weeks out doesn't want today's traffic anyway.
        "routingPreference": "TRAFFIC_UNAWARE",
        "polylineQuality": "OVERVIEW",
        "units": "IMPERIAL",
        "languageCode": "en-US",
    }
    if len(points) > 2:
        body["intermediates"] = [_waypoint(p) for p in points[1:-1]]

    timeout = float(getattr(Config, "ROUTES_TIMEOUT", 10) or 10)
    try:
        data = (fetch or (lambda b: _post(b, api_key, timeout)))(body)
    except HTTPError as exc:
        detail = ""
        try:
            detail = json.loads(exc.read().decode("utf-8")).get("error", {}).get("message", "")
        except Exception:  # noqa: BLE001 — error body is optional
            pass
        log.warning("Routes API HTTP %s: %s", exc.code, detail or exc.reason)
        if exc.code in (401, 403):
            raise RoutingError("Road routing is misconfigured on this server.") from exc
        if exc.code == 429:
            raise RoutingError("Road routing is temporarily over quota. Try again later.") from exc
        raise RoutingError("Road routing failed for this trip.") from exc
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        log.warning("Routes API request failed: %s", exc)
        raise RoutingError("Road routing is unavailable right now.") from exc

    routes = data.get("routes") if isinstance(data, dict) else None
    if not routes:
        raise RoutingError("No drivable route was found between these stops.")
    route = routes[0]
    legs = []
    for leg in route.get("legs") or []:
        encoded = (leg.get("polyline") or {}).get("encodedPolyline") or ""
        legs.append({
            "distance_miles": round(float(leg.get("distanceMeters", 0)) / METERS_PER_MILE, 1),
            "duration_minutes": int(round(_parse_duration(leg.get("duration")) / 60)),
            "points": decode_polyline(encoded) if encoded else [],
        })
    if len(legs) != len(points) - 1:
        raise RoutingError("Road routing returned an unexpected number of legs.")
    encoded = (route.get("polyline") or {}).get("encodedPolyline") or ""
    result = {
        "provider": "google",
        "total_miles": round(float(route.get("distanceMeters", 0)) / METERS_PER_MILE, 1),
        "total_minutes": int(round(_parse_duration(route.get("duration")) / 60)),
        "legs": legs,
        "points": decode_polyline(encoded) if encoded else [p for leg in legs for p in leg["points"]],
    }
    _cache_put(key, result)
    return result
