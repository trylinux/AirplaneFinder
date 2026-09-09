"""Road routes for the trip planner (routing.py + POST /api/v1/trips/route).

Google is never called: ``compute_route`` takes an injectable ``fetch`` and
the endpoint tests monkeypatch ``routing._post``.
"""
import json
from urllib.error import HTTPError, URLError

import pytest

import routing
from config import Config


# Encoded polyline from Google's own docs example, decoded to three points.
GOOGLE_DOC_POLYLINE = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"
GOOGLE_DOC_POINTS = [[38.5, -120.2], [40.7, -120.95], [43.252, -126.453]]


@pytest.fixture(autouse=True)
def _reset(monkeypatch):
    routing.clear_cache()
    monkeypatch.setattr(Config, "GOOGLE_MAPS_API_KEY", "test-key")
    monkeypatch.setattr(Config, "ROUTES_CACHE_TTL", 3600)
    yield
    routing.clear_cache()


def google_response(legs):
    """Build a Routes API response with one leg per (meters, seconds, polyline)."""
    return {"routes": [{
        "distanceMeters": sum(m for m, _, _ in legs),
        "duration": f"{sum(s for _, s, _ in legs)}s",
        "polyline": {"encodedPolyline": legs[0][2]},
        "legs": [{"distanceMeters": m, "duration": f"{s}s", "polyline": {"encodedPolyline": p}} for m, s, p in legs],
    }]}


# ── decode_polyline ───────────────────────────────────────────────────────

def test_decode_polyline_matches_google_reference():
    assert routing.decode_polyline(GOOGLE_DOC_POLYLINE) == GOOGLE_DOC_POINTS


def test_decode_polyline_handles_empty_and_truncated():
    assert routing.decode_polyline("") == []
    with pytest.raises(ValueError):
        routing.decode_polyline("_p~iF~ps|U_ul")   # cut mid-varint


# ── validate_points ───────────────────────────────────────────────────────

@pytest.mark.parametrize("bad", [
    None, [], [{"latitude": 0, "longitude": 0}],                      # too few
    [{"latitude": 0, "longitude": 0}] * 11,                            # too many
    [{"latitude": 91, "longitude": 0}, {"latitude": 0, "longitude": 0}],
    [{"latitude": 0, "longitude": 181}, {"latitude": 0, "longitude": 0}],
    [{"latitude": True, "longitude": 0}, {"latitude": 0, "longitude": 0}],
    [{"latitude": "0", "longitude": 0}, {"latitude": 0, "longitude": 0}],
    ["x", {"latitude": 0, "longitude": 0}],
])
def test_validate_points_rejects_bad_input(bad):
    with pytest.raises(ValueError):
        routing.validate_points(bad)


def test_validate_points_accepts_dicts_and_pairs():
    assert routing.validate_points([{"latitude": 1, "longitude": 2}, (3, 4)]) == [(1.0, 2.0), (3.0, 4.0)]


# ── compute_route ─────────────────────────────────────────────────────────

def test_compute_route_builds_request_and_parses_response():
    seen = {}
    def fetch(body):
        seen.update(body)
        return google_response([(160934, 3600, GOOGLE_DOC_POLYLINE), (80467, 1800, GOOGLE_DOC_POLYLINE)])
    points = [(39.76, -84.19), (41.5, -81.7), (39.76, -84.19)]
    result = routing.compute_route(points, fetch=fetch)

    assert seen["travelMode"] == "DRIVE" and seen["routingPreference"] == "TRAFFIC_UNAWARE"
    assert seen["origin"]["location"]["latLng"] == {"latitude": 39.76, "longitude": -84.19}
    assert seen["destination"]["location"]["latLng"] == {"latitude": 39.76, "longitude": -84.19}
    assert [w["location"]["latLng"]["latitude"] for w in seen["intermediates"]] == [41.5]

    assert result["provider"] == "google"
    assert result["total_miles"] == 150.0 and result["total_minutes"] == 90
    assert [leg["distance_miles"] for leg in result["legs"]] == [100.0, 50.0]
    assert [leg["duration_minutes"] for leg in result["legs"]] == [60, 30]
    assert result["legs"][0]["points"] == GOOGLE_DOC_POINTS
    assert result["points"] == GOOGLE_DOC_POINTS
    assert "cached" not in result


def test_compute_route_two_points_has_no_intermediates():
    seen = {}
    def fetch(body):
        seen.update(body); return google_response([(1609, 60, GOOGLE_DOC_POLYLINE)])
    routing.compute_route([(0, 0), (1, 1)], fetch=fetch)
    assert "intermediates" not in seen


def test_compute_route_caches_by_rounded_points():
    calls = []
    def fetch(body):
        calls.append(body); return google_response([(1609, 60, GOOGLE_DOC_POLYLINE)])
    first = routing.compute_route([(0, 0), (1, 1)], fetch=fetch)
    # 1e-5 degrees is inside the 4-decimal cache rounding.
    second = routing.compute_route([(0.00001, 0), (1, 1.00001)], fetch=fetch)
    assert len(calls) == 1 and second["cached"] is True
    assert {k: v for k, v in second.items() if k != "cached"} == first
    routing.compute_route([(0, 0), (2, 2)], fetch=fetch)
    assert len(calls) == 2


def test_compute_route_cache_expires(monkeypatch):
    calls = []
    def fetch(body):
        calls.append(body); return google_response([(1609, 60, GOOGLE_DOC_POLYLINE)])
    routing.compute_route([(0, 0), (1, 1)], fetch=fetch)
    monkeypatch.setattr(Config, "ROUTES_CACHE_TTL", 0)
    routing.compute_route([(0, 0), (1, 1)], fetch=fetch)
    assert len(calls) == 2


def test_compute_route_without_key_is_unavailable(monkeypatch):
    monkeypatch.setattr(Config, "GOOGLE_MAPS_API_KEY", "")
    with pytest.raises(routing.RoutingUnavailable):
        routing.compute_route([(0, 0), (1, 1)], fetch=lambda b: pytest.fail("must not call Google"))


@pytest.mark.parametrize("response", [{}, {"routes": []}, {"routes": [{"legs": []}]}])
def test_compute_route_rejects_empty_or_short_responses(response):
    with pytest.raises(routing.RoutingError):
        routing.compute_route([(0, 0), (1, 1)], fetch=lambda b: response)


def http_error(code, message=""):
    body = json.dumps({"error": {"message": message}}).encode()
    import io
    return HTTPError(routing.ROUTES_URL, code, "err", {}, io.BytesIO(body))


@pytest.mark.parametrize("exc, fragment", [
    (http_error(403, "API key not valid"), "misconfigured"),
    (http_error(429), "over quota"),
    (http_error(400, "bad"), "failed for this trip"),
    (URLError("dns"), "unavailable right now"),
    (TimeoutError(), "unavailable right now"),
])
def test_compute_route_maps_failures_to_user_messages(exc, fragment):
    def fetch(body):
        raise exc
    with pytest.raises(routing.RoutingError) as info:
        routing.compute_route([(0, 0), (1, 1)], fetch=fetch)
    assert fragment in str(info.value)
    assert routing._cache == {}     # failures are never cached


# ── endpoint ──────────────────────────────────────────────────────────────

def test_route_endpoint_returns_legs(client, monkeypatch):
    monkeypatch.setattr(routing, "_post", lambda body, key, timeout: google_response([(160934, 3600, GOOGLE_DOC_POLYLINE)]))
    r = client.post("/api/v1/trips/route", json={"points": [{"latitude": 0, "longitude": 0}, {"latitude": 1, "longitude": 1}]})
    assert r.status_code == 200
    assert r.json["total_miles"] == 100.0 and len(r.json["legs"]) == 1


def test_route_endpoint_without_key_is_503(client, monkeypatch):
    monkeypatch.setattr(Config, "GOOGLE_MAPS_API_KEY", "")
    r = client.post("/api/v1/trips/route", json={"points": [{"latitude": 0, "longitude": 0}, {"latitude": 1, "longitude": 1}]})
    assert r.status_code == 503 and r.json["available"] is False


def test_route_endpoint_google_failure_is_502(client, monkeypatch):
    def boom(body, key, timeout):
        raise URLError("down")
    monkeypatch.setattr(routing, "_post", boom)
    r = client.post("/api/v1/trips/route", json={"points": [{"latitude": 0, "longitude": 0}, {"latitude": 1, "longitude": 1}]})
    assert r.status_code == 502 and r.json["available"] is True


@pytest.mark.parametrize("body", [None, {}, {"points": [{"latitude": 0, "longitude": 0}]}, {"points": "nope"}])
def test_route_endpoint_bad_input_is_400(client, monkeypatch, body):
    monkeypatch.setattr(routing, "_post", lambda *a: pytest.fail("must not call Google"))
    r = client.post("/api/v1/trips/route", json=body)
    assert r.status_code == 400 and "error" in r.json


def test_plan_reports_routing_availability(client, make_aircraft, monkeypatch):
    a = make_aircraft()
    payload = {"origin": {"latitude": 0, "longitude": 0}, "targets": [{"kind": "airframe", "aircraft_id": a.id}]}
    assert client.post("/api/v1/trips/plan", json=payload).json["road_routing_available"] is True
    monkeypatch.setattr(Config, "GOOGLE_MAPS_API_KEY", "")
    assert client.post("/api/v1/trips/plan", json=payload).json["road_routing_available"] is False


def test_route_endpoint_listed_in_api_docs(client):
    assert b"/api/v1/trips/route" in client.get("/api/v1/docs").data
