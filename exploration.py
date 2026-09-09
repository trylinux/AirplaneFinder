"""Airframe histories, map discovery, and aircraft-focused itinerary suggestions."""
from datetime import date
from math import isfinite
from urllib.parse import urlparse

from flask import abort, jsonify, render_template, request
from flask_login import current_user, login_required
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import joinedload

from models import db, Aircraft, AircraftMuseum, AircraftHistoryEvent, Museum, haversine
from logger import change_log
import routing

HISTORY_TYPES = ('built', 'delivered', 'service', 'registration', 'transfer',
                 'restoration', 'retirement', 'display', 'other')


def history_fields(data):
    """Validate a complete milestone; preserve unknown date precision explicitly."""
    clean = {}
    for key, maximum in [('title', 200), ('description', 10000), ('operator', 200),
                         ('location', 200), ('registration', 80), ('source_name', 300),
                         ('source_url', 1000), ('event_type', 30)]:
        value = data.get(key)
        if value is not None and not isinstance(value, str):
            raise ValueError(f'{key} must be text.')
        value = value.strip() if value else ''
        if len(value) > maximum:
            raise ValueError(f'{key} must be at most {maximum} characters.')
        clean[key] = value or None
    if not clean['title']:
        raise ValueError('A title is required.')
    clean['event_type'] = clean['event_type'] or 'other'
    if clean['event_type'] not in HISTORY_TYPES:
        raise ValueError('Unknown event type.')
    if clean['source_url']:
        parsed = urlparse(clean['source_url'])
        if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError('Source URL must be an HTTP or HTTPS link without credentials.')
    if not (clean['source_name'] or clean['source_url']):
        raise ValueError('Add a source URL or a source citation (such as a book and page).')
    for field in ('is_approximate', 'is_published'):
        value = data.get(field, field == 'is_published')
        if not isinstance(value, bool):
            raise ValueError(f'{field} must be a boolean.')
        clean[field] = value
    for field in ('event_year', 'event_month', 'event_day'):
        value = data.get(field)
        if value is not None and (not isinstance(value, int) or isinstance(value, bool)):
            raise ValueError(f'{field} must be an integer or null.')
        clean[field] = value
    year, month, day = (clean[f'event_{part}'] for part in ('year', 'month', 'day'))
    if (month is not None and year is None) or (day is not None and month is None):
        raise ValueError('Month requires a year; day requires a month and year.')
    if year is not None:
        try:
            date(year, month if month is not None else 1, day if day is not None else 1)
        except (ValueError, OverflowError):
            raise ValueError('Enter a valid date (year 1–9999).') from None
    return clean


def museum_map_data():
    """Coordinate-bearing museums, with counts filtered to visible exhibits."""
    query = (db.session.query(Museum, func.count(AircraftMuseum.id))
             .outerjoin(AircraftMuseum, and_(AircraftMuseum.museum_id == Museum.id,
                                            AircraftMuseum.display_status == 'on_display')))
    q = request.args.get('q', '').strip()[:200]
    if q:
        term = f'%{q}%'
        query = query.filter(or_(Museum.name.ilike(term), Museum.city.ilike(term), Museum.country.ilike(term)))
    for field in ('region', 'country'):
        value = request.args.get(field, '').strip()
        if value:
            query = query.filter(getattr(Museum, field) == value)
    # All selected museum columns are grouped for MySQL ONLY_FULL_GROUP_BY.
    rows = query.group_by(*Museum.__table__.columns).order_by(Museum.name, Museum.id).all()
    located, unlocated = [], []
    for museum, count in rows:
        item = {**museum.to_dict(), 'aircraft_count': count}
        (located if museum.has_coordinates else unlocated).append(item)
    return {'results': located, 'no_coordinates': unlocated, 'total': len(rows)}


def positive_int(value, label, maximum):
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= maximum:
        raise ValueError(f'{label} must be an integer between 1 and {maximum}.')
    return value


def number(value, label, minimum, maximum):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value) or not minimum <= value <= maximum:
        raise ValueError(f'{label} must be between {minimum} and {maximum}.')
    return float(value)


def plan_trip(data, resolve_location):
    """Greedy coverage, then nearest-next-stop ordering. Distances are geodesic,
    not a road network or a promise of an optimal/drivable route."""
    targets = data.get('targets')
    if not isinstance(targets, list) or not 1 <= len(targets) <= 12:
        raise ValueError('Choose between 1 and 12 aircraft or models.')
    max_stops = positive_int(data.get('max_stops', 5), 'max_stops', 8)
    radius = number(data.get('radius_miles', 500), 'radius_miles', 1, 5000)
    round_trip = data.get('round_trip', False)
    if not isinstance(round_trip, bool):
        raise ValueError('round_trip must be a boolean.')
    origin = data.get('origin')
    if not isinstance(origin, dict):
        raise ValueError('An origin is required.')
    if 'latitude' in origin or 'longitude' in origin:
        lat = number(origin.get('latitude'), 'latitude', -90, 90)
        lon = number(origin.get('longitude'), 'longitude', -180, 180)
        origin_label = f'{lat:.4f}, {lon:.4f}'
    else:
        location = origin.get('location')
        if not isinstance(location, str) or not location.strip() or len(location) > 200:
            raise ValueError('Enter a starting city or postal code.')
        lat, lon = resolve_location(location.strip())
        if lat is None or lon is None:
            raise ValueError('Starting location could not be found. Try a city and country.')
        origin_label = location.strip()
    normalized, matches, seen = [], {}, set()
    for target in targets:
        if not isinstance(target, dict):
            raise ValueError('Each target must be an object.')
        if target.get('kind') == 'airframe':
            aircraft_id = positive_int(target.get('aircraft_id'), 'aircraft_id', 2147483647)
            key = ('airframe', aircraft_id)
            aircraft = db.session.get(Aircraft, aircraft_id)
            if not aircraft:
                raise ValueError(f'Aircraft #{aircraft_id} no longer exists.')
            records = [aircraft]
            label = f'{aircraft.full_designation} · {aircraft.tail_number or aircraft.aircraft_name or "Airframe #" + str(aircraft.id)}'
            entry = {'kind': 'airframe', 'aircraft_id': aircraft_id, 'label': label}
        elif target.get('kind') == 'model':
            manufacturer, model = target.get('manufacturer'), target.get('model')
            if not all(isinstance(v, str) and v.strip() for v in (manufacturer, model)):
                raise ValueError('Model targets need manufacturer and model.')
            if len(manufacturer) > 100 or len(model) > 50:
                raise ValueError('Model target is too long.')
            manufacturer, model = manufacturer.strip(), model.strip()
            key = ('model', manufacturer.casefold(), model.casefold())
            records = Aircraft.query.filter(func.lower(Aircraft.manufacturer) == manufacturer.lower(),
                                            func.lower(Aircraft.model) == model.lower()).all()
            entry = {'kind': 'model', 'manufacturer': manufacturer, 'model': model,
                     'label': f'{manufacturer} {model} · any variant'}
        else:
            raise ValueError('Target kind must be airframe or model.')
        if key in seen:
            continue
        seen.add(key)
        index = len(normalized)
        matches[index] = {a.id for a in records}
        normalized.append(entry)
    aircraft_ids = set().union(*matches.values())
    links = (AircraftMuseum.query.options(joinedload(AircraftMuseum.museum), joinedload(AircraftMuseum.aircraft))
             .filter(AircraftMuseum.aircraft_id.in_(aircraft_ids), AircraftMuseum.display_status == 'on_display').all()) if aircraft_ids else []
    candidates, reasons, missing_coordinates = {}, {}, {}
    for index, ids in matches.items():
        relevant = [link for link in links if link.aircraft_id in ids]
        within = False
        for link in relevant:
            museum = link.museum
            if not museum.has_coordinates:
                missing_coordinates[museum.id] = museum.to_dict()
                continue
            distance = haversine(lat, lon, float(museum.latitude), float(museum.longitude))
            if distance > radius:
                continue
            within = True
            candidate = candidates.setdefault(museum.id, {'museum': museum.to_dict(), 'targets': set(), 'aircraft': {}})
            candidate['targets'].add(index)
            candidate['aircraft'][link.aircraft_id] = link.aircraft.to_dict()
        if not within:
            reasons[index] = ('No matching aircraft in the catalog.' if not ids else
                              'No recorded on-display exhibit.' if not relevant else
                              'Matching museums have no coordinates.' if all(not l.museum.has_coordinates for l in relevant) else
                              'No located match within the search radius.')
    remaining = set(matches)
    selected = []
    point = (lat, lon)
    def distance_to(item, start):
        m = item['museum']
        return haversine(*start, m['latitude'], m['longitude'])
    while len(selected) < max_stops:
        choices = [c for c in candidates.values() if c['targets'] & remaining]
        if not choices:
            break
        choice = min(choices, key=lambda c: (-len(c['targets'] & remaining), distance_to(c, point), c['museum']['id']))
        selected.append(choice)
        remaining -= choice['targets']
        point = (choice['museum']['latitude'], choice['museum']['longitude'])
    # Reorder only the chosen museums; each wanted aircraft remains covered.
    stops, total, point = [], 0.0, (lat, lon)
    while selected:
        choice = min(selected, key=lambda c: (distance_to(c, point), c['museum']['id']))
        selected.remove(choice)
        distance = distance_to(choice, point)
        total += distance
        stops.append({'museum': choice['museum'], 'target_indexes': sorted(choice['targets']),
                      'aircraft': list(choice['aircraft'].values()), 'leg_straight_line_miles': round(distance, 1)})
        point = (choice['museum']['latitude'], choice['museum']['longitude'])
    return_leg = haversine(*point, lat, lon) if round_trip and stops else 0
    total += return_leg
    return {'origin': {'location': origin_label, 'latitude': lat, 'longitude': lon},
            'targets': normalized, 'stops': stops, 'radius_miles': radius, 'round_trip': round_trip,
            'total_straight_line_miles': round(total, 1), 'return_straight_line_miles': round(return_leg, 1),
            'unmatched': [{'target_index': i, 'label': normalized[i]['label'],
                           'reason': reasons.get(i, 'Not included within your stop limit.')} for i in sorted(remaining)],
            'no_coordinates': list(missing_coordinates.values()),
            'distance_basis': 'straight_line', 'method': 'coverage_then_nearest_neighbor',
            # Tells the client whether POST /api/v1/trips/route is worth calling.
            'road_routing_available': routing.is_enabled()}


def register_exploration(app, api_auth_required, get_user, increment_contribution, resolve_location, limiter):
    # Read once; Config is a class, so tests can still override before import.
    from config import Config
    routing_rate_limit = getattr(Config, 'ROUTES_RATE_LIMIT', '20 per minute')

    @app.route('/map')
    def museum_map_page():
        return render_template('museum_map.html')

    @app.route('/trips')
    def trip_planner_page():
        return render_template('trips.html')

    @app.route('/aircraft/<int:aircraft_id>/history')
    def airframe_history_page(aircraft_id):
        return render_template('airframe_history.html', aircraft=Aircraft.query.get_or_404(aircraft_id), editing=False, history_types=HISTORY_TYPES)

    @app.route('/admin/aircraft/<int:aircraft_id>/history')
    @login_required
    def manage_airframe_history_page(aircraft_id):
        if not current_user.is_manager:
            abort(403)
        return render_template('airframe_history.html', aircraft=Aircraft.query.get_or_404(aircraft_id), editing=True, history_types=HISTORY_TYPES)

    @app.route('/api/v1/museums/map')
    def api_museum_map():
        return jsonify(museum_map_data())

    @app.route('/api/v1/trips/plan', methods=['POST'])
    @limiter.limit('30 per minute')
    def api_plan_trip():
        try:
            return jsonify(plan_trip(request.get_json() or {}, resolve_location))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    @app.route('/api/v1/trips/route', methods=['POST'])
    @limiter.limit(routing_rate_limit)
    def api_trip_route():
        """Driving route through an ordered list of points (Google Routes API).

        Body: ``{"points": [{"latitude": .., "longitude": ..}, ...]}`` — the
        plan's origin, its stops in order, and the origin again for a round
        trip. 503 when no API key is configured, 502 when Google can't route
        it; either way the straight-line plan still stands.
        """
        data = request.get_json(silent=True) or {}
        try:
            return jsonify(routing.compute_route(data.get('points')))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400
        except routing.RoutingUnavailable as exc:
            return jsonify(error=str(exc), available=False), 503
        except routing.RoutingError as exc:
            return jsonify(error=str(exc), available=True), 502

    def events_for(aircraft_id, drafts=False):
        Aircraft.query.get_or_404(aircraft_id)
        query = AircraftHistoryEvent.query.filter_by(aircraft_id=aircraft_id)
        if not drafts:
            query = query.filter_by(is_published=True)
        return query.order_by(AircraftHistoryEvent.event_year.is_(None), AircraftHistoryEvent.event_year,
                              AircraftHistoryEvent.event_month, AircraftHistoryEvent.event_day,
                              AircraftHistoryEvent.id).all()

    @app.route('/api/v1/aircraft/<int:aircraft_id>/history')
    def api_airframe_history(aircraft_id):
        return jsonify([event.to_dict() for event in events_for(aircraft_id)])

    @app.route('/api/v1/aircraft/<int:aircraft_id>/history/manage')
    @api_auth_required('readwrite')
    def api_manage_airframe_history(aircraft_id):
        return jsonify([event.to_dict() for event in events_for(aircraft_id, drafts=True)])

    @app.route('/api/v1/aircraft/<int:aircraft_id>/history', methods=['POST'])
    @api_auth_required('readwrite')
    def api_create_history(aircraft_id):
        Aircraft.query.get_or_404(aircraft_id)
        try:
            fields = history_fields(request.get_json() or {})
        except ValueError as exc:
            return jsonify(error=str(exc)), 400
        user = get_user()
        event = AircraftHistoryEvent(aircraft_id=aircraft_id, created_by=user.id, updated_by=user.id, **fields)
        db.session.add(event)
        increment_contribution()
        db.session.commit()
        change_log.info(f'HISTORY_CREATE id={event.id} aircraft={aircraft_id} by={user.username}')
        return jsonify(event.to_dict()), 201

    @app.route('/api/v1/history/<int:event_id>', methods=['PUT', 'PATCH'])
    @api_auth_required('readwrite')
    def api_update_history(event_id):
        event = AircraftHistoryEvent.query.get_or_404(event_id)
        try:
            fields = history_fields({**event.to_dict(), **(request.get_json() or {})})
        except ValueError as exc:
            return jsonify(error=str(exc)), 400
        for key, value in fields.items():
            setattr(event, key, value)
        event.updated_by = get_user().id
        increment_contribution()
        db.session.commit()
        change_log.info(f'HISTORY_UPDATE id={event.id} by={get_user().username}')
        return jsonify(event.to_dict())

    @app.route('/api/v1/history/<int:event_id>', methods=['DELETE'])
    @api_auth_required('admin')
    def api_delete_history(event_id):
        event = AircraftHistoryEvent.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        change_log.info(f'HISTORY_DELETE id={event_id} by={get_user().username}')
        return jsonify(deleted=True, id=event_id)
