"""Histories and itineraries must preserve identity, date precision and display availability."""
import pytest
from models import AircraftHistoryEvent, db


def login_as(client, user):
    client.get('/logout')
    response = client.post('/login', data={'username':user.username,'password':'Tester-1234'})
    assert response.status_code == 302


def milestone(**changes):
    return {'title': 'Delivered to operator', 'event_type': 'delivered', 'event_year': 1954,
            'source_name': 'Museum archive, page 12', **changes}


def trip_payload(aircraft, **changes):
    return {'origin': {'latitude': 0, 'longitude': 0}, 'radius_miles': 500,
            'targets': [{'kind':'airframe','aircraft_id':aircraft.id}], **changes}


def test_history_crud_preserves_airframe_identity(admin_client, client, make_aircraft, make_museum, make_link):
    a = make_aircraft(tail_number='OLD')
    m = make_museum()
    make_link(a, m)
    response = admin_client.post(f'/api/v1/aircraft/{a.id}/history', json=milestone(registration='PAST', location='Historic base'))
    assert response.status_code == 201
    event = response.json
    assert event['event_year'] == 1954 and event['event_month'] is None and event['event_day'] is None
    assert a.tail_number == 'OLD' and a.museum_links.count() == 1
    assert admin_client.patch(f'/api/v1/aircraft/{a.id}', json={'tail_number':'NEW'}).status_code == 200
    public = client.get(f'/api/v1/aircraft/{a.id}/history').json
    assert public[0]['registration'] == 'PAST'
    assert admin_client.patch(f"/api/v1/history/{event['id']}", json={'is_approximate':True}).json['is_approximate'] is True
    assert admin_client.delete(f"/api/v1/history/{event['id']}").status_code == 200
    assert client.get(f'/api/v1/aircraft/{a.id}/history').json == []


def test_drafts_never_leak_through_public_list(admin_client, admin_user, viewer_user, make_aircraft):
    a = make_aircraft()
    admin_client.post(f'/api/v1/aircraft/{a.id}/history',json=milestone(is_published=False))
    assert admin_client.get(f'/api/v1/aircraft/{a.id}/history?include_inactive=true').json == []
    assert len(admin_client.get(f'/api/v1/aircraft/{a.id}/history/manage').json) == 1
    login_as(admin_client, viewer_user)
    assert admin_client.get(f'/api/v1/aircraft/{a.id}/history/manage').status_code == 403


@pytest.mark.parametrize('fields', [
    {'event_year':1900,'event_month':2,'event_day':29}, {'event_year':None,'event_month':1},
    {'event_day':1}, {'event_year':0}, {'event_year':True}, {'event_year':'1954'},
    {'event_month':0}, {'event_month':13}, {'event_day':32},
    {'source_name':'','source_url':None}, {'source_url':'javascript:alert(1)'},
    {'source_url':'https://user:pass@example.com'}, {'is_published':'false'},
    {'event_type':'invalid'}, {'title':'  '}, {'description':{}},
])
def test_bad_history_update_is_atomic(admin_client, make_aircraft, fields):
    a = make_aircraft()
    created = admin_client.post(f'/api/v1/aircraft/{a.id}/history', json=milestone()).json
    response = admin_client.patch(f"/api/v1/history/{created['id']}",json=fields)
    assert response.status_code == 400
    assert admin_client.get(f'/api/v1/aircraft/{a.id}/history').json[0]['title'] == 'Delivered to operator'


def test_history_date_order_and_leap_day(admin_client, make_aircraft):
    a = make_aircraft()
    url = f'/api/v1/aircraft/{a.id}/history'
    for fields in [{'event_year':None,'title':'Undated'}, {'event_year':2000,'event_month':2,'event_day':29,'title':'Leap day'}, {'event_year':1900,'title':'Earlier'}]:
        assert admin_client.post(url,json=milestone(**fields)).status_code == 201
    assert [e['title'] for e in admin_client.get(url).json] == ['Earlier','Leap day','Undated']


def test_history_role_gates(client, viewer_user, manager_user, aircraft_admin_user, make_aircraft):
    a = make_aircraft()
    url = f'/api/v1/aircraft/{a.id}/history'
    assert client.post(url,json=milestone()).status_code == 401
    login_as(client, viewer_user)
    assert client.post(url,json=milestone()).status_code == 403
    login_as(client, manager_user)
    created = client.post(url,json=milestone())
    assert created.status_code == 201
    eid = created.json['id']
    assert client.delete(f'/api/v1/history/{eid}').status_code == 403
    login_as(client, aircraft_admin_user)
    assert client.delete(f'/api/v1/history/{eid}').status_code == 200


def test_history_aircraft_deletion_cascades(admin_client, make_aircraft):
    a = make_aircraft()
    eid = admin_client.post(f'/api/v1/aircraft/{a.id}/history',json=milestone()).json['id']
    assert admin_client.delete(f'/api/v1/aircraft/{a.id}').status_code == 200
    assert db.session.get(AircraftHistoryEvent,eid) is None


def test_map_filters_and_counts(client, make_museum, make_aircraft, make_link):
    located = make_museum(name='Located',latitude=0,longitude=0)
    hidden = make_museum(name='Unlocated',latitude=None,longitude=None)
    make_link(make_aircraft(),located)
    make_link(make_aircraft(),located,display_status='in_storage')
    response = client.get('/api/v1/museums/map').json
    assert response['results'][0]['aircraft_count'] == 1
    assert response['results'][0]['latitude'] == 0
    assert response['no_coordinates'][0]['id'] == hidden.id
    assert client.get('/api/v1/museums/map?q=Located').json['total'] == 2
    assert client.get('/api/v1/museums/map?region=Europe').json['total'] == 0


def test_trip_exact_airframe_differs_from_model(client, make_aircraft, make_museum, make_link):
    a = make_aircraft(model='C-130',tail_number='A')
    b = make_aircraft(model='C-130',variant='H',tail_number='B')
    m = make_museum(latitude=0,longitude=1)
    make_link(b,m)
    exact = client.post('/api/v1/trips/plan',json=trip_payload(a)).json
    assert not exact['stops'] and len(exact['unmatched']) == 1
    model = client.post('/api/v1/trips/plan',json=trip_payload(a,targets=[{'kind':'model','manufacturer':a.manufacturer,'model':a.model}])).json
    assert len(model['stops']) == 1 and model['stops'][0]['aircraft'][0]['id'] == b.id


def test_trip_combines_targets_in_one_stop(client, make_aircraft, make_museum, make_link):
    a,b = make_aircraft(),make_aircraft(model='B-17')
    near = make_museum(name='Near',latitude=0,longitude=.1)
    both = make_museum(name='Both',latitude=0,longitude=1)
    make_link(a,near);make_link(a,both);make_link(b,both)
    targets=[{'kind':'airframe','aircraft_id':x.id} for x in (a,b)]
    response = client.post('/api/v1/trips/plan',json=trip_payload(a,targets=targets,max_stops=1)).json
    assert [s['museum']['id'] for s in response['stops']] == [both.id]
    assert response['unmatched'] == [] and response['stops'][0]['target_indexes'] == [0,1]


def test_trip_never_routes_to_storage_or_unknown_coordinates(client, make_aircraft, make_museum, make_link):
    a = make_aircraft()
    make_link(a,make_museum(latitude=0,longitude=1),display_status='under_restoration')
    unlocated = make_museum(latitude=None,longitude=None)
    make_link(a,unlocated)
    result = client.post('/api/v1/trips/plan',json=trip_payload(a)).json
    assert result['stops'] == []
    assert result['no_coordinates'][0]['id'] == unlocated.id
    assert 'coordinates' in result['unmatched'][0]['reason']


def test_trip_radius_and_stop_limit_explain_unmatched(client, make_aircraft, make_museum, make_link):
    a,b,c = make_aircraft(),make_aircraft(),make_aircraft()
    for aircraft,lon in [(a,1),(b,2),(c,20)]:make_link(aircraft,make_museum(latitude=0,longitude=lon))
    payload=trip_payload(a,targets=[{'kind':'airframe','aircraft_id':x.id} for x in (a,b,c)],max_stops=1)
    result=client.post('/api/v1/trips/plan',json=payload).json
    assert len(result['stops']) == 1 and len(result['unmatched']) == 2
    assert any('stop limit' in t['reason'] for t in result['unmatched'])
    assert any('radius' in t['reason'] for t in result['unmatched'])


def test_trip_duplicates_and_round_trip_distance(client, make_aircraft, make_museum, make_link):
    a=make_aircraft();make_link(a,make_museum(latitude=0,longitude=1))
    target={'kind':'airframe','aircraft_id':a.id}
    result=client.post('/api/v1/trips/plan',json=trip_payload(a,targets=[target,target],round_trip=True)).json
    assert len(result['targets']) == 1
    assert 138 < result['total_straight_line_miles'] < 139
    assert result['return_straight_line_miles'] > 69
    assert result['distance_basis'] == 'straight_line'


def test_trip_handles_date_line(client, make_aircraft, make_museum, make_link):
    a=make_aircraft();make_link(a,make_museum(latitude=0,longitude=-179))
    result=client.post('/api/v1/trips/plan',json=trip_payload(a,origin={'latitude':0,'longitude':179})).json
    assert len(result['stops']) == 1 and 138 < result['total_straight_line_miles'] < 139


@pytest.mark.parametrize('override', [
    {'targets':[]}, {'targets':[{}]}, {'targets':[{'kind':'airframe','aircraft_id':True}]},
    {'targets':[{'kind':'model','manufacturer':[],'model':'X'}]}, {'max_stops':0},
    {'max_stops':9}, {'radius_miles':float('nan')}, {'radius_miles':-1},
    {'round_trip':'false'}, {'origin':None}, {'origin':{'latitude':91,'longitude':0}},
])
def test_trip_bad_input(client, make_aircraft, override):
    response=client.post('/api/v1/trips/plan',json=trip_payload(make_aircraft(),**override))
    assert response.status_code == 400 and response.is_json


def test_trip_typed_origin_and_failure(client, make_aircraft, monkeypatch):
    import app as appmod
    monkeypatch.setattr(appmod,'_resolve_location',lambda location:(0,0))
    payload=trip_payload(make_aircraft(),origin={'location':'Test City'})
    assert client.post('/api/v1/trips/plan',json=payload).json['origin']['location']=='Test City'
    monkeypatch.setattr(appmod,'_resolve_location',lambda location:(None,None))
    assert client.post('/api/v1/trips/plan',json=payload).status_code==400


@pytest.mark.parametrize('phone',[False,True])
def test_feature_pages_and_edit_access(client, manager_user, viewer_user, make_aircraft, phone):
    a=make_aircraft()
    headers={'User-Agent':'iPhone Mobile Safari'} if phone else {}
    for route in ['/map','/trips',f'/aircraft/{a.id}/history']:
        response=client.get(route,headers=headers)
        assert response.status_code==200
        assert (b'mobile-layout' in response.data) == phone
    login_as(client, manager_user)
    assert client.get(f'/admin/aircraft/{a.id}/history',headers=headers).status_code==200
    login_as(client, viewer_user)
    assert client.get(f'/admin/aircraft/{a.id}/history',headers=headers).status_code==403


def test_history_bearer_with_csrf_enabled(app, client, manager_user, make_aircraft, db_session):
    from models import ApiKey
    a=make_aircraft()
    key,raw=ApiKey.generate(manager_user.id,permissions='readwrite')
    db_session.add(key);db_session.commit()
    app.config['WTF_CSRF_ENABLED']=True
    assert client.post(f'/api/v1/aircraft/{a.id}/history',headers={'Authorization':'Bearer '+raw},json=milestone()).status_code==201
    assert client.post('/api/v1/trips/plan',json=trip_payload(a)).status_code==400
