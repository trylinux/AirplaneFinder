"""Role-based access control.

The role hierarchy is:
    admin > aircraft_admin > manager > viewer

The two boundaries that matter:
  - Anyone can read public endpoints (aircraft search, museum search, etc.).
  - Only admin can manage users (create/edit/delete users + their API keys).
  - admin AND aircraft_admin can delete data (aircraft/museums/exhibits/templates).
  - admin, aircraft_admin, manager can create/update data.

This file verifies the role property matrix, then probes the actual
endpoints to ensure the decorators wire those properties up correctly.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────
# Role property matrix
# ─────────────────────────────────────────────────────────────────────

class TestRoleProperties:
    """If this test passes the decorators are getting the right answers
    from the User model — most authorization bugs become visible here."""

    @pytest.mark.parametrize("role,expected", [
        # (role, (is_admin, is_aircraft_admin, is_data_admin, is_manager))
        ("admin",          (True,  False, True,  True)),
        ("aircraft_admin", (False, True,  True,  True)),
        ("manager",        (False, False, False, True)),
        ("viewer",         (False, False, False, False)),
    ])
    def test_role_property_matrix(self, role, expected):
        import models
        u = models.User(username=f"probe_{role}", role=role, password_hash="x")
        got = (u.is_admin, u.is_aircraft_admin, u.is_data_admin, u.is_manager)
        assert got == expected, (
            f"role={role!r}: expected (is_admin, is_aircraft_admin, "
            f"is_data_admin, is_manager) = {expected}, got {got}"
        )


# ─────────────────────────────────────────────────────────────────────
# Endpoint reachability per role
# ─────────────────────────────────────────────────────────────────────

class TestUserManagementGate:
    """User management is the strict-admin-only line. aircraft_admin must
    NOT be able to reach it — that's the whole point of the role split."""

    def test_admin_can_list_all_users(self, admin_client):
        r = admin_client.get("/api/v1/users")
        assert r.status_code == 200
        users = r.get_json()
        # Admin sees all users (the fixture has at least the admin itself).
        assert isinstance(users, list) and users

    def test_aircraft_admin_only_sees_self_in_user_list(
        self, app, db_session, aircraft_admin_user, admin_user
    ):
        """Non-admins get a list containing only their own user record."""
        client = app.test_client()
        client.post("/login",
                    data={"username": aircraft_admin_user.username, "password": "Tester-1234"})
        r = client.get("/api/v1/users")
        assert r.status_code == 200
        usernames = [u["username"] for u in r.get_json()]
        assert usernames == [aircraft_admin_user.username]

    def test_aircraft_admin_cannot_create_users(
        self, app, db_session, aircraft_admin_user
    ):
        client = app.test_client()
        client.post("/login",
                    data={"username": aircraft_admin_user.username, "password": "Tester-1234"})
        r = client.post(
            "/api/v1/users",
            json={"username": "newby", "password": "Tester-1234", "role": "viewer"},
        )
        assert r.status_code == 403, (
            "aircraft_admin should NOT be able to create users — that's "
            "the whole boundary that distinguishes the role from admin"
        )

    def test_manager_cannot_reach_users_endpoint_post(
        self, app, db_session, manager_user
    ):
        client = app.test_client()
        client.post("/login",
                    data={"username": manager_user.username, "password": "Tester-1234"})
        r = client.post(
            "/api/v1/users",
            json={"username": "newby", "password": "Tester-1234", "role": "viewer"},
        )
        assert r.status_code == 403


class TestDataAdminGate:
    """Data deletes need admin-or-aircraft_admin. Manager and viewer must
    not be able to delete."""

    @pytest.fixture
    def aircraft_id(self, make_aircraft):
        return make_aircraft(model="C-130", tail_number="55-0014").id

    def test_admin_can_delete_aircraft(self, admin_client, aircraft_id):
        r = admin_client.delete(f"/api/v1/aircraft/{aircraft_id}")
        assert r.status_code == 200

    def test_aircraft_admin_can_delete_aircraft(
        self, aircraft_admin_client, aircraft_id
    ):
        r = aircraft_admin_client.delete(f"/api/v1/aircraft/{aircraft_id}")
        assert r.status_code == 200, (
            "aircraft_admin should be able to delete data — "
            "that's the whole role"
        )

    def test_manager_cannot_delete_aircraft(self, manager_client, aircraft_id):
        r = manager_client.delete(f"/api/v1/aircraft/{aircraft_id}")
        assert r.status_code == 403

    def test_viewer_cannot_delete_aircraft(self, viewer_client, aircraft_id):
        r = viewer_client.delete(f"/api/v1/aircraft/{aircraft_id}")
        assert r.status_code == 403


class TestWriteGate:
    """create/update is everyone-but-viewer."""

    def _create_aircraft(self, client):
        return client.post(
            "/api/v1/aircraft",
            json={"manufacturer": "Boeing", "model": "B-29", "tail_number": "44-86292",
                  "aircraft_type": "fixed_wing", "military_civilian": "military"},
        )

    def test_admin_can_create(self, admin_client):
        r = self._create_aircraft(admin_client)
        assert r.status_code == 201

    def test_aircraft_admin_can_create(self, aircraft_admin_client):
        r = self._create_aircraft(aircraft_admin_client)
        assert r.status_code == 201

    def test_manager_can_create(self, manager_client):
        r = self._create_aircraft(manager_client)
        assert r.status_code == 201

    def test_viewer_cannot_create(self, viewer_client):
        r = self._create_aircraft(viewer_client)
        assert r.status_code == 403


class TestUnauthenticatedAccess:
    """Anonymous users get redirected to /login on protected pages and 401
    JSON on protected APIs."""

    def test_anonymous_account_page_redirects_to_login(self, client):
        r = client.get("/account", follow_redirects=False)
        assert r.status_code in (301, 302)
        assert "/login" in r.headers["Location"]

    def test_anonymous_api_create_returns_401(self, client):
        r = client.post("/api/v1/aircraft",
                        json={"manufacturer": "X", "model": "Y"})
        assert r.status_code == 401

    def test_anonymous_can_search_aircraft(self, client, make_aircraft):
        # Public endpoint, no auth required.
        make_aircraft(model="C-130")
        r = client.get("/api/v1/aircraft/search")
        assert r.status_code == 200
