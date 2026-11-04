"""A failed merge must leave the original catalog intact."""
from models import Aircraft, AircraftFact, AircraftHistoryEvent, AircraftMuseum, Museum, UserMuseumAssignment


def test_aircraft_merge_preserves_history_facts_and_notes(admin_client, make_aircraft,
                                                        make_museum, make_link, db_session):
    keep = make_aircraft(description='Keep provenance', tail_number=None)
    drop = make_aircraft(description='Drop provenance', tail_number='SERIAL')
    keep_id, drop_id = keep.id, drop.id
    museum = make_museum()
    make_link(keep, museum, notes='Keep notes')
    make_link(drop, museum, notes='Drop notes')
    fact = AircraftFact(fact='Sourced fact', aircraft_id=drop_id)
    history = AircraftHistoryEvent(aircraft_id=drop_id, title='Draft milestone',
                                    source_name='Archive', is_published=False)
    db_session.add_all([fact, history])
    db_session.commit()
    response = admin_client.post(f'/api/v1/aircraft/{keep_id}/merge', json={'drop_id': drop_id})
    assert response.status_code == 200, response.json
    db_session.expire_all()
    assert db_session.get(Aircraft, drop_id) is None
    assert fact.aircraft_id == history.aircraft_id == keep_id
    assert not history.is_published
    assert response.json['tail_number'] == 'SERIAL'
    assert response.json['description'] == 'Keep provenance\n\nDrop provenance'
    assert AircraftMuseum.query.one().notes == 'Keep notes\n\nDrop notes'


def test_conflicting_merge_rolls_back_all_changes(admin_client, make_aircraft,
                                                make_museum, make_link, db_session):
    keep, drop = make_aircraft(), make_aircraft(tail_number=None)
    keep_id, drop_id = keep.id, drop.id
    museum = make_museum()
    make_link(keep, museum, display_status='on_display')
    make_link(drop, museum, display_status='in_storage')
    response = admin_client.post(f'/api/v1/aircraft/{keep_id}/merge', json={'drop_id': drop_id})
    assert response.status_code == 409
    assert Aircraft.query.count() == 2
    assert AircraftMuseum.query.count() == 2


def test_museum_merge_preserves_assignments_and_zero_coordinates(admin_client, manager_user,
                                                               make_museum, make_aircraft,
                                                               make_link, db_session):
    keep = make_museum(name='Keep', latitude=None, longitude=None)
    drop = make_museum(name='Drop', latitude=0, longitude=0, website='https://example.org')
    keep_id, drop_id = keep.id, drop.id
    aircraft = make_aircraft()
    make_link(aircraft, drop, notes='Source exhibit notes', display_status='under_restoration')
    db_session.add(UserMuseumAssignment(user_id=manager_user.id, museum_id=drop_id))
    db_session.commit()
    response = admin_client.post(f'/api/v1/museums/{keep_id}/merge', json={
        'drop_id': drop_id, 'expected_aircraft_ids': [aircraft.id],
    })
    assert response.status_code == 200, response.json
    db_session.expire_all()
    assert db_session.get(Museum, drop_id) is None
    assert UserMuseumAssignment.query.one().museum_id == keep_id
    link = AircraftMuseum.query.one()
    assert link.museum_id == keep_id and link.notes == 'Source exhibit notes'
    assert link.display_status == 'under_restoration'
    assert response.json['latitude'] == response.json['longitude'] == 0


def test_stale_collection_plan_cannot_delete_new_records(admin_client, make_museum,
                                                        make_aircraft, make_link):
    keep, drop = make_museum(name='Keep'), make_museum(name='Drop')
    make_link(make_aircraft(), drop)
    response = admin_client.post(f'/api/v1/museums/{keep.id}/merge', json={
        'drop_id': drop.id, 'expected_aircraft_ids': [],
    })
    assert response.status_code == 409
    assert Museum.query.count() == 2 and AircraftMuseum.query.count() == 1


def test_managers_cannot_merge(manager_client, make_aircraft):
    keep, drop = make_aircraft(), make_aircraft(tail_number=None)
    assert manager_client.post(f'/api/v1/aircraft/{keep.id}/merge',
                               json={'drop_id': drop.id}).status_code == 403


def test_failed_airframe_preservation_never_reaches_museum_delete():
    from scripts.apply_merge import apply_pair
    from scripts.airplane_api import ApiError
    import pytest
    calls = []
    class Client:
        def get_museum(self, museum_id):
            return {'aircraft': [{'id': 20}]}
        def post(self, path, **kwargs):
            calls.append(path)
            raise ApiError(409, {'error': 'conflict'}, path)
    plan = {'keep': {'id': 1}, 'drop': {'id': 2}, 'proven': True,
            'delete_aircraft': [20], 'matched': [{'keep_aircraft': 10, 'drop_aircraft': 20}],
            'relink_links': []}
    with pytest.raises(ApiError):
        apply_pair(Client(), plan)
    assert calls == ['/api/v1/aircraft/10/merge']


def test_remote_merge_plan_preserves_repointed_collection(admin_client, make_museum,
                                                        make_aircraft, make_link):
    from scripts.apply_merge import apply_pair
    keep_site, drop_site = make_museum(name='Keep'), make_museum(name='Drop')
    keep, drop = make_aircraft(), make_aircraft(tail_number=None)
    keep_site_id, drop_site_id = keep_site.id, drop_site.id
    keep_id, drop_id = keep.id, drop.id
    make_link(keep, keep_site)
    make_link(drop, drop_site, notes='Preserved provenance')
    class Client:
        def get_museum(self, museum_id):
            return admin_client.get(f'/api/v1/museums/{museum_id}').json
        def post(self, path, **kwargs):
            response = admin_client.post(path, **kwargs)
            assert response.status_code == 200, response.json
            return response.json
    apply_pair(Client(), {'keep': {'id': keep_site_id}, 'drop': {'id': drop_site_id},
                         'proven': True, 'delete_aircraft': [drop_id], 'relink_links': [],
                         'matched': [{'keep_aircraft': keep_id, 'drop_aircraft': drop_id}]})
    assert Museum.query.count() == Aircraft.query.count() == AircraftMuseum.query.count() == 1
    assert AircraftMuseum.query.one().notes == 'Preserved provenance'


def test_remote_merge_rejects_path_injection_before_requests():
    from scripts.apply_merge import apply_pair
    import pytest
    with pytest.raises(ValueError, match='Invalid aircraft IDs'):
        apply_pair(None, {'keep': {'id': 1}, 'drop': {'id': 2}, 'proven': True,
                          'delete_aircraft': [20], 'relink_links': [],
                          'matched': [{'keep_aircraft': '../users/1', 'drop_aircraft': 20}]})
