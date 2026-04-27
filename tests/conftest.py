"""Shared pytest fixtures.

Goals:
- Tests should run with ``pytest`` from the project root, no extra setup.
- No MySQL needed: SQLite in-memory database created per test (or per module
  where it's expensive to rebuild).
- Real Flask-WTF and Flask-Limiter, but with CSRF + rate limits disabled so
  individual tests don't have to think about either.
- Real SECRET_KEY so security checks don't refuse to boot.

Notes on the SQLite fallback:
- Aircraft has a STORED generated column (``full_designation``). SQLite
  understands GENERATED ALWAYS AS but not MySQL's CONCAT/IFNULL. We work
  around this by overriding the Computed expression to a SQLite-compatible
  one in ``_install_test_schema`` — keeps the model unchanged, swaps only
  the per-test DDL.
- Foreign-key constraints aren't enforced by default in SQLite; we turn
  them on so cascade-delete tests behave like prod.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone

import pytest
from sqlalchemy import event

# Make the project root importable from inside tests/ regardless of cwd.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PROJECT_ROOT)


# ─────────────────────────────────────────────────────────────────────
# App-wide configuration overrides
# ─────────────────────────────────────────────────────────────────────

@pytest.fixture(scope="session", autouse=True)
def _test_env():
    """Override Config BEFORE app.py is imported anywhere.

    Sets:
      - SQLite in-memory DB
      - A real (non-default) SECRET_KEY so create_app() doesn't refuse.
      - Empty SQLAlchemy engine options (SQLite ignores MySQL pool flags).
    """
    import config
    config.Config.SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    config.Config.SQLALCHEMY_ENGINE_OPTIONS = {}
    config.Config.SECRET_KEY = "test-secret-key-not-for-production"
    # Disable security headers in tests so we don't have to special-case
    # the test client's HTTP transport. test_security.py flips this back on.
    config.Config.SECURITY_HEADERS_ENABLED = False
    config.Config.SESSION_COOKIE_SECURE = False
    config.Config.REMEMBER_COOKIE_SECURE = False
    yield


# ─────────────────────────────────────────────────────────────────────
# App / DB / client
# ─────────────────────────────────────────────────────────────────────

@pytest.fixture
def app():
    """Fresh Flask app per test, with disabled CSRF + rate limiting.

    Two non-obvious bits:

    1. Flask-Limiter caches its enabled state at ``init_app`` time, so
       setting ``app.config["RATELIMIT_ENABLED"] = False`` here is too
       late — the extension is already wired up. Flip the limiter
       object's ``enabled`` flag directly.

    2. Several security knobs are read from the ``Config`` class at
       request time, not from ``app.config``. So the conftest also flips
       the Config class attributes, and tests that *want* them on flip
       them at the Config class level themselves.
    """
    import app as appmod
    import config

    flask_app = appmod.app
    flask_app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        RATELIMIT_ENABLED=False,
        SECRET_KEY="test-secret-key-not-for-production",
    )

    # Disable rate limiter at the extension level (config flag is too late).
    appmod.limiter.enabled = False

    # Off by default for tests; test_security.py flips back on.
    config.Config.SECURITY_HEADERS_ENABLED = False
    config.Config.SESSION_COOKIE_SECURE = False
    config.Config.REMEMBER_COOKIE_SECURE = False

    yield flask_app

    # Best-effort cleanup so a test that flips Config back on doesn't
    # leak headers into the next test.
    config.Config.SECURITY_HEADERS_ENABLED = False


@pytest.fixture
def db_session(app):
    """Build the schema in-memory and yield the session.

    Drops + recreates per test to keep tests isolated.
    """
    import models

    with app.app_context():
        # Aircraft has a Computed column whose MySQL CONCAT/IFNULL syntax
        # SQLite can't compile. We rewrite it to SQLite-compatible
        # CONCAT_WS-equivalent for the DDL, then restore.
        original = models.Aircraft.__table__.c.full_designation.computed
        try:
            from sqlalchemy import Computed
            models.Aircraft.__table__.c.full_designation.computed = Computed(
                "model || COALESCE('-' || variant, '')",
                persisted=True,
            )
            models.db.create_all()
        finally:
            models.Aircraft.__table__.c.full_designation.computed = original

        # SQLite doesn't enforce FKs by default — turn it on so cascades fire.
        @event.listens_for(models.db.engine, "connect")
        def _enable_sqlite_fk(dbapi_conn, _):
            cur = dbapi_conn.cursor()
            cur.execute("PRAGMA foreign_keys=ON")
            cur.close()

        # Apply to the existing connection too (the listener is for new ones).
        models.db.session.execute(models.db.text("PRAGMA foreign_keys=ON"))
        models.db.session.commit()

        yield models.db.session

        # Cleanup
        models.db.session.remove()
        models.db.drop_all()


@pytest.fixture
def client(app, db_session):
    """Plain (anonymous) test client."""
    return app.test_client()


# ─────────────────────────────────────────────────────────────────────
# Users for each role + matching authed clients
# ─────────────────────────────────────────────────────────────────────

# A password that satisfies the policy (>=8 chars, letter + digit).
_TEST_PW = "Tester-1234"


def _make_user(db_session, username, role):
    import models
    u = models.User(username=username, role=role, email=f"{username}@example.com")
    u.set_password(_TEST_PW)
    db_session.add(u)
    db_session.commit()
    return u


@pytest.fixture
def admin_user(db_session):
    return _make_user(db_session, "admin_test", "admin")


@pytest.fixture
def aircraft_admin_user(db_session):
    return _make_user(db_session, "ac_admin_test", "aircraft_admin")


@pytest.fixture
def manager_user(db_session):
    return _make_user(db_session, "manager_test", "manager")


@pytest.fixture
def viewer_user(db_session):
    return _make_user(db_session, "viewer_test", "viewer")


def _login(client, username, password=_TEST_PW):
    """POST /login as ``username``; returns the test client (logged-in)."""
    r = client.post("/login", data={"username": username, "password": password},
                    follow_redirects=False)
    assert r.status_code in (301, 302), (
        f"login as {username} expected redirect, got {r.status_code}: "
        f"{r.get_data(as_text=True)[:200]}"
    )
    return client


@pytest.fixture
def admin_client(client, admin_user):
    return _login(client, admin_user.username)


@pytest.fixture
def aircraft_admin_client(client, aircraft_admin_user):
    return _login(client, aircraft_admin_user.username)


@pytest.fixture
def manager_client(client, manager_user):
    return _login(client, manager_user.username)


@pytest.fixture
def viewer_client(client, viewer_user):
    return _login(client, viewer_user.username)


# ─────────────────────────────────────────────────────────────────────
# Domain helpers
# ─────────────────────────────────────────────────────────────────────

@pytest.fixture
def make_aircraft(db_session):
    """Factory: ``make_aircraft(model='C-130', tail_number='55-0014', ...)`` ."""
    import models

    def _factory(**kwargs):
        defaults = dict(
            manufacturer="Lockheed",
            model="C-130",
            tail_number=None,
            aircraft_type="fixed_wing",
            military_civilian="military",
        )
        defaults.update(kwargs)
        a = models.Aircraft(**defaults)
        db_session.add(a)
        db_session.commit()
        return a
    return _factory


@pytest.fixture
def make_museum(db_session):
    """Factory: ``make_museum(name='Test Museum', city='Dayton', ...)``."""
    import models

    def _factory(**kwargs):
        defaults = dict(
            name="Test Museum",
            city="Dayton",
            country="United States",
            region="North America",
        )
        defaults.update(kwargs)
        m = models.Museum(**defaults)
        db_session.add(m)
        db_session.commit()
        return m
    return _factory


@pytest.fixture
def make_link(db_session):
    """Factory: link an aircraft to a museum, returning the AircraftMuseum."""
    import models

    def _factory(aircraft, museum, display_status="on_display", notes=None):
        link = models.AircraftMuseum(
            aircraft_id=aircraft.id, museum_id=museum.id,
            display_status=display_status, notes=notes,
        )
        db_session.add(link)
        db_session.commit()
        return link
    return _factory
