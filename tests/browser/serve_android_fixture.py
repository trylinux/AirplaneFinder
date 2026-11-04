"""Local-only snapshot server for emulator sync tests. No production DB access."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from config import Config
Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
Config.SQLALCHEMY_ENGINE_OPTIONS = {}
Config.SECRET_KEY = 'android-local-fixture-only'
Config.SESSION_COOKIE_SECURE = False
Config.SECURITY_HEADERS_ENABLED = False
Config.OFFLINE_CATALOG_DIR = tempfile.mkdtemp(prefix='airplane-android-fixture-')

from app import app, csrf, limiter
from flask import jsonify
from offline_catalog import publish_snapshot

limiter.enabled = False
data = {
    'aircraft': [{'id': 1, 'manufacturer': 'Fixture', 'model': 'X-1', 'full_designation': 'X-1',
                  'tail_number': 'TEST-1', 'aliases': ['Offline Test'], 'description': '<script>window.injected=true</script>', 'type_id': None}],
    'museums': [{'id': 1, 'name': 'Offline Test Museum', 'city': 'Test City', 'country': 'United States',
                 'latitude': 0, 'longitude': 0, 'access_type': 'public', 'website': 'https://example.org'}],
    'exhibits': [{'id': 1, 'aircraft_id': 1, 'museum_id': 1, 'display_status': 'on_display', 'notes': ''}],
    'types': [], 'facts': [{'id': 1, 'aircraft_id': 1, 'fact': 'Local sync test fact.', 'source_url': None}],
    'history': [{'id': 1, 'aircraft_id': 1, 'title': 'Test delivery', 'event_year': 1950, 'is_published': True}],
}
publish_snapshot(data, Config.OFFLINE_CATALOG_DIR, catalog_id='android-sync-fixture', source='Local emulator test catalog')

@app.post('/__test__/delete-aircraft')
@csrf.exempt
def delete_aircraft():
    data['aircraft'] = []; data['exhibits'] = []; data['history'] = []
    data['facts'][0]['aircraft_id'] = None
    manifest = publish_snapshot(data, Config.OFFLINE_CATALOG_DIR, catalog_id='android-sync-fixture', source='Local emulator test catalog')
    return jsonify(manifest)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5058, use_reloader=False)
