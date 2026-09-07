"""Regressions confirmed during the application/documentation audit."""
import json
import pytest


def bearer(user, db_session, permission='admin'):
    from models import ApiKey
    key, raw = ApiKey.generate(user.id, permissions=permission)
    db_session.add(key)
    db_session.commit()
    return {'Authorization': 'Bearer ' + raw}


def test_viewer_cannot_mint_write_key(viewer_client):
    assert viewer_client.post('/api/v1/keys', json={'permissions':'readwrite'}).status_code == 403


def test_data_admin_can_mint_data_admin_key(aircraft_admin_client):
    assert aircraft_admin_client.post('/api/v1/keys', json={'permissions':'admin'}).status_code == 201


def test_existing_key_cannot_exceed_current_role(client, admin_user, db_session):
    headers = bearer(admin_user, db_session)
    admin_user.role = 'viewer'
    db_session.commit()
    assert client.post('/api/v1/aircraft', headers=headers, json={'manufacturer':'Test','model':'X'}).status_code == 403


def test_disabled_user_key_stops_working(client, admin_user, db_session):
    headers = bearer(admin_user, db_session)
    admin_user.is_active_user = False
    db_session.commit()
    assert client.post('/api/v1/aircraft', headers=headers, json={'manufacturer':'Test','model':'X'}).status_code == 401


def test_invalid_bearer_does_not_use_admin_cookie(admin_client):
    r = admin_client.post('/api/v1/aircraft', headers={'Authorization':'Bearer invalid'}, json={'manufacturer':'Test','model':'X'})
    assert r.status_code == 401


def test_disabled_session_stops_working(admin_client, admin_user, db_session):
    admin_user.is_active_user = False
    db_session.commit()
    assert admin_client.get('/admin').status_code == 302


def test_data_admin_can_edit_and_link_any_museum(aircraft_admin_client, make_museum, make_aircraft):
    m = make_museum()
    a = make_aircraft()
    assert aircraft_admin_client.patch(f'/api/v1/museums/{m.id}', json={'city':'New City'}).status_code == 200
    assert aircraft_admin_client.post('/api/v1/exhibits', json={'museum_id':m.id,'aircraft_id':a.id}).status_code == 201


def test_delete_user_with_keys(admin_client, viewer_user, db_session):
    from models import ApiKey, User, AircraftFact
    user_id = viewer_user.id
    bearer(viewer_user, db_session, 'read')
    fact = AircraftFact(fact='Keep this fact', created_by=user_id)
    db_session.add(fact)
    db_session.commit()
    fact_id = fact.id
    assert admin_client.delete(f'/api/v1/users/{user_id}').status_code == 200
    db_session.expire_all()
    assert db_session.get(User, user_id) is None
    assert ApiKey.query.filter_by(user_id=user_id).count() == 0
    assert db_session.get(AircraftFact, fact_id).created_by is None


def test_delete_assigned_museum_with_exhibits(admin_client, manager_user, make_museum, make_aircraft, make_link, db_session):
    from models import UserMuseumAssignment, AircraftMuseum
    m = make_museum()
    link = make_link(make_aircraft(),m)
    mid, lid = m.id, link.id
    db_session.add(UserMuseumAssignment(user_id=manager_user.id,museum_id=mid))
    db_session.commit()
    assert admin_client.delete(f'/api/v1/museums/{mid}').status_code == 200
    db_session.expire_all()
    assert db_session.get(AircraftMuseum,lid) is None
    assert UserMuseumAssignment.query.filter_by(museum_id=mid).count() == 0


@pytest.mark.parametrize('payload', [[], ['x'], 'text', 5, None])
def test_json_object_required(admin_client, payload):
    r=admin_client.post('/api/v1/aircraft', data=json.dumps(payload), content_type='application/json')
    assert r.status_code == 400
    assert r.is_json


@pytest.mark.parametrize('field,value', [('manufacturer',None),('model',' '),('aircraft_type','bogus'),('year_built','not a year')])
def test_invalid_aircraft_edit_is_atomic(admin_client, make_aircraft, field, value):
    a=make_aircraft()
    r=admin_client.patch(f'/api/v1/aircraft/{a.id}',json={field:value,'description':'must not save'})
    assert r.status_code == 400
    assert admin_client.get(f'/api/v1/aircraft/{a.id}').json['aircraft']['description'] is None


@pytest.mark.parametrize('value', ['NaN','Infinity',91,-91,{},[]])
def test_invalid_coordinates_rejected(admin_client,value):
    r=admin_client.post('/api/v1/museums',json={'name':'Bad coordinates','city':'Test','country':'US','region':'North America','latitude':value,'longitude':0})
    assert r.status_code == 400


def test_aircraft_creation_with_missing_museum_fails_atomically(admin_client):
    r=admin_client.post('/api/v1/aircraft',json={'manufacturer':'Test','model':'Missing Museum','museum_id':9999})
    assert r.status_code == 404
    assert admin_client.get('/api/v1/aircraft/search?q=Missing+Museum').json['total'] == 0


@pytest.mark.parametrize('value',['bad',{},[]])
def test_bad_exhibit_ids_return_400(admin_client,value):
    assert admin_client.post('/api/v1/exhibits',json={'museum_id':value,'aircraft_id':1}).status_code == 400


@pytest.mark.parametrize('kind',['aircraft','museums'])
def test_dry_run_checks_database_duplicates(admin_client,make_aircraft,make_museum,kind):
    if kind=='aircraft':
        make_aircraft(model='Duplicate',tail_number='DUP')
        row={'manufacturer':'Lockheed','model':'Duplicate','tail_number':'DUP'}
    else:
        make_museum(name='Duplicate',city='Test')
        row={'name':'Duplicate','city':'Test','region':'North America'}
    payload={'format':'json','data':json.dumps([row]),'dry_run':True}
    report=admin_client.post(f'/api/v1/{kind}/bulk_import',json=payload).json
    assert report['errors'] and report['created']==0 and report['skipped']==1


@pytest.mark.parametrize('value',['false','true',0,1])
def test_user_active_flag_requires_json_boolean(admin_client,viewer_user,value):
    assert admin_client.patch(f'/api/v1/users/{viewer_user.id}',json={'is_active':value}).status_code == 400


def test_duplicate_aliases_normalized(admin_client):
    r=admin_client.post('/api/v1/aircraft',json={'manufacturer':'Test','model':'X','aliases':['Example','Example',' Example ']})
    assert r.status_code == 201
    assert r.json['aliases'] == ['Example']


def test_bearer_header_cannot_exempt_session_endpoint_from_csrf(app, admin_client):
    app.config['WTF_CSRF_ENABLED'] = True
    response = admin_client.post('/api/v1/keys', headers={'Authorization': 'Bearer invalid'}, json={})
    assert response.status_code == 400
    assert 'csrf' in response.get_data(as_text=True).lower()


def test_bearer_auth_works_with_expired_cookie(app, admin_client, admin_user, db_session):
    headers = bearer(admin_user, db_session)
    app.config['WTF_CSRF_ENABLED'] = True
    with admin_client.session_transaction() as session:
        session['last_activity'] = '2000-01-01T00:00:00+00:00'
        session['login_time'] = '2000-01-01T00:00:00+00:00'
    response = admin_client.post('/api/v1/aircraft', headers=headers, json={'manufacturer':'Test', 'model':'Token'})
    assert response.status_code == 201


@pytest.mark.parametrize('country', [' ', None, 42])
def test_museum_country_cannot_be_cleared(admin_client, make_museum, country):
    museum = make_museum()
    assert admin_client.patch(f'/api/v1/museums/{museum.id}', json={'country': country}).status_code == 400


@pytest.mark.parametrize('radius', ['-1', 'NaN', 'Infinity', 'text'])
def test_invalid_nearest_radius(client, radius):
    assert client.get('/api/v1/museums/nearest', query_string={'lat': 0, 'lon': 0, 'radius': radius}).status_code == 400


@pytest.mark.parametrize('flag', ['false', 1])
def test_import_dry_run_requires_boolean(admin_client, flag):
    response = admin_client.post('/api/v1/museums/bulk_import', json={'data': '[]', 'format': 'json', 'dry_run': flag})
    assert response.status_code == 400


def test_search_uses_configured_page_size(client, make_museum, monkeypatch):
    from config import Config
    monkeypatch.setattr(Config, 'RESULTS_PER_PAGE', 1)
    make_museum(name='First')
    make_museum(name='Second')
    result = client.get('/api/v1/museums/search').json
    assert result['total'] == 2 and result['pages'] == 2 and len(result['results']) == 1
    assert len(client.get('/api/v1/museums/search?per_page=-1').json['results']) == 1


@pytest.mark.parametrize('location,expected', [
    ('Sydney, Australia', 'au'), ('Vienna, Austria', 'at'), ('Moscow, Russia', 'ru'),
    ('London, United Kingdom', 'gb'), ('Austin, United States', 'us'),
])
def test_country_guess_does_not_match_us_substring(location, expected):
    from geocoder import _guess_country_code
    assert _guess_country_code(location) == expected


def test_api_reference_includes_every_current_route(app, client):
    from markupsafe import escape
    html = client.get('/api/v1/docs').get_data(as_text=True)
    for rule in app.url_map.iter_rules():
        if rule.rule.startswith('/api/v1/'):
            assert str(escape(rule.rule)) in html


def test_fresh_schema_defines_foreign_key_targets_first():
    """MySQL checks referenced tables while processing CREATE TABLE statements."""
    import re
    from pathlib import Path
    sql = (Path(__file__).resolve().parents[1] / 'schema.sql').read_text()
    defined = set()
    for statement in sql.split(';'):
        match = re.search(r'CREATE TABLE IF NOT EXISTS (\w+)', statement)
        if not match:
            continue
        for referenced in re.findall(r'REFERENCES (\w+)', statement):
            assert referenced in defined, f'{match[1]} references {referenced} before it exists'
        defined.add(match[1])
    assert 'user_museum_assignments' in defined
