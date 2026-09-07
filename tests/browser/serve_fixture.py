"""Serve deterministic browser-test data; never connects to the configured database.

Run with the application's Python environment, then run mobile_views.cjs.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from config import Config
Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
Config.SQLALCHEMY_ENGINE_OPTIONS = {}
Config.SECRET_KEY = 'local-browser-test-secret'
Config.SECURITY_HEADERS_ENABLED = False
Config.SESSION_COOKIE_SECURE = False

import app as appmod
from models import db, Aircraft, Museum, AircraftMuseum, User
from sqlalchemy import Computed
appmod.limiter.enabled = False
appmod._resolve_location = lambda location: (0, -90)
with appmod.app.app_context():
    Aircraft.__table__.c.full_designation.computed = Computed("model || COALESCE('-' || variant, '')", persisted=True)
    db.create_all()
    user = User(username="browser-admin", role="admin")
    user.set_password("browser-test-password")
    db.session.add(user)
    museum = Museum(name='Alpha Aviation Museum', city='Dayton', country='United States', region='North America', latitude=0, longitude=-90, website='https://example.com', address='1 Museum Way')
    hidden = Museum(name='Zulu Museum', city='London', country='United Kingdom', region='Europe')
    aircraft = Aircraft(manufacturer='Lockheed', model='C-130', model_name='Hercules', aircraft_name='Test Airframe', tail_number='TEST-1', aircraft_type='fixed_wing', military_civilian='military')
    stored = Aircraft(manufacturer='Boeing', model='B-17', aircraft_type='fixed_wing', military_civilian='military')
    db.session.add_all([museum, hidden, aircraft, stored])
    db.session.flush()
    db.session.add_all([AircraftMuseum(aircraft_id=aircraft.id, museum_id=museum.id, display_status='on_display'), AircraftMuseum(aircraft_id=stored.id, museum_id=museum.id, display_status='in_storage')])
    db.session.commit()

if __name__ == '__main__':
    appmod.app.run(host='127.0.0.1', port=5057, debug=False, use_reloader=False)
