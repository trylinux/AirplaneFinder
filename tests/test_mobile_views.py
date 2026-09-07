"""Device choice must not block authenticated management or weaken access gates."""
import pytest

PHONE = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) Mobile Safari'}
MANAGEMENT_PAGES = ['/admin', '/admin/museums', '/admin/museums/new', '/admin/aircraft',
                    '/admin/aircraft/new', '/admin/exhibits', '/admin/templates',
                    '/admin/import', '/admin/facts', '/admin/api-keys', '/admin/users']

@pytest.mark.parametrize('path', MANAGEMENT_PAGES)
def test_mobile_management_requires_login(client, path):
    response = client.get(path, headers=PHONE)
    assert response.status_code == 302
    assert '/login' in response.location

@pytest.mark.parametrize('path', MANAGEMENT_PAGES)
def test_mobile_admin_can_open_management(admin_client, path):
    response = admin_client.get(path, headers=PHONE)
    assert response.status_code == 200
    assert b'Admin tools are not available on mobile' not in response.data


def test_mobile_viewer_cannot_open_user_management(viewer_client):
    assert viewer_client.get('/admin/users', headers=PHONE).status_code == 403


def test_mobile_login_preserves_destination(client):
    response = client.get('/login?next=/admin/museums', headers=PHONE)
    assert b'action="/login?next=/admin/museums"' in response.data


def test_legacy_desktop_only_link_opens_management(admin_client):
    response = admin_client.get('/desktop-only', headers=PHONE, follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/admin'
