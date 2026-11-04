import gzip
import hashlib
import json

from models import AircraftFact, AircraftHistoryEvent, AircraftType
from offline_catalog import database_snapshot, publish_snapshot


def test_snapshot_contains_public_relations_not_drafts_or_accounts(client, admin_user,
                                                                 make_aircraft, make_museum,
                                                                 make_link, db_session, tmp_path):
    aircraft = make_aircraft(model='OFFLINE', tail_number='SNAPSHOT')
    museum = make_museum(website='javascript:bad()')
    make_link(aircraft, museum, notes='Exhibit provenance')
    for published in (True, False):
        db_session.add(AircraftHistoryEvent(aircraft_id=aircraft.id, title=f'history-{published}',
                                            is_published=published, source_name='Archive'))
        db_session.add(AircraftFact(fact=f'fact-{published}', is_active=published,
                                    created_by=admin_user.id))
        item = AircraftType(model='OFFLINE' if published else 'PRIVATE',
                            display_name=f'type-{published}', description='Source text',
                            slug=f'offline-{published}', is_published=published)
        item.sync_key()
        db_session.add(item)
    db_session.commit()
    snapshot = database_snapshot()
    assert [h['title'] for h in snapshot['history']] == ['history-True']
    assert [f['fact'] for f in snapshot['facts']] == ['fact-True']
    assert [t['display_name'] for t in snapshot['types']] == ['type-True']
    assert snapshot['aircraft'][0]['type_id'] == snapshot['types'][0]['id']
    assert snapshot['exhibits'][0]['notes'] == 'Exhibit provenance'
    assert snapshot['museums'][0]['website'] is None
    raw = json.dumps(snapshot)
    assert admin_user.password_hash not in raw and 'created_by' not in raw
    manifest = publish_snapshot(snapshot, tmp_path)
    client.application.config['OFFLINE_CATALOG_DIR'] = str(tmp_path)
    response = client.get('/api/v1/offline/manifest')
    assert response.status_code == 200 and response.json == manifest
    packed = client.get(manifest['download_path'])
    assert packed.status_code == 200
    assert hashlib.sha256(packed.data).hexdigest() == manifest['sha256']
    document = json.loads(gzip.decompress(packed.data))
    assert document['aircraft'] == snapshot['aircraft']
    assert len(packed.data) == manifest['byte_size']
    assert len(gzip.decompress(packed.data)) == manifest['uncompressed_size']
    assert client.get(manifest['download_path'], headers={'If-None-Match': packed.headers['ETag']}).status_code == 304


def test_new_snapshot_handles_deletions_and_preserves_inflight_version(client, make_aircraft, db_session, tmp_path):
    aircraft = make_aircraft()
    first = publish_snapshot(database_snapshot(), tmp_path)
    db_session.delete(aircraft)
    db_session.commit()
    second = publish_snapshot(database_snapshot(), tmp_path)
    client.application.config['OFFLINE_CATALOG_DIR'] = str(tmp_path)
    assert client.get('/api/v1/offline/manifest').json['revision'] == second['revision']
    assert client.get(first['download_path']).status_code == 200
    assert json.loads(gzip.decompress(client.get(second['download_path']).data))['aircraft'] == []


def test_unpublished_and_invalid_snapshot_paths(client, tmp_path):
    client.application.config['OFFLINE_CATALOG_DIR'] = str(tmp_path)
    assert client.get('/api/v1/offline/manifest').status_code == 503
    for token in ('manifest', 'bad', 'a'*64):
        assert client.get(f'/api/v1/offline/snapshots/{token}.json.gz').status_code == 404


def test_offline_export_type_resolution_matches_server(client, make_aircraft, db_session):
    from models import AircraftTypeAlias
    aircraft = make_aircraft(manufacturer='Bell Helicopter', model='204')
    for scope in ('', 'Bell', 'Grumman'):
        item = AircraftType(model='UH-1'+scope, display_name='Iroquois', description='History',
                            slug='uh1'+scope.lower(), manufacturer_scope=scope, is_published=True)
        item.sync_key()
        alias = AircraftTypeAlias(designation='204', manufacturer_scope=scope)
        alias.sync_key()
        item.aliases.append(alias)
        db_session.add(item)
    db_session.commit()
    expected = AircraftType.resolve_for('204', manufacturer='Bell Helicopter')
    assert database_snapshot()['aircraft'][0]['type_id'] == expected.id
