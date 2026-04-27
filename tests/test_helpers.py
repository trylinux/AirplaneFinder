"""Pure-function helpers — no DB, no HTTP, just inputs and outputs.

These are the easiest tests to write and the highest-leverage when one of
these helpers regresses. We caught a SQL-injection-shaped sort_by attempt
silently passing through during development; that's the kind of regression
this file is meant to catch fast.
"""

import pytest


# ─────────────────────────────────────────────────────────────────────
# _safe_next_url — open-redirect protection
# ─────────────────────────────────────────────────────────────────────

class TestSafeNextUrl:
    """The login page reads ?next=… and redirects after success. Without
    the helper, ``?next=https://evil.com/phish`` would happily redirect
    the user to a phishing page after authentication."""

    @pytest.fixture
    def safe_next(self, app):
        import app as appmod
        # _safe_next_url uses request, so call inside a request context.
        def _check(target):
            with app.test_request_context("/"):
                return appmod._safe_next_url(target)
        return _check

    def test_none_input_returns_none(self, safe_next):
        assert safe_next(None) is None

    def test_empty_string_returns_none(self, safe_next):
        assert safe_next("") is None

    def test_relative_path_is_accepted(self, safe_next):
        # The most common legitimate case — ?next=/account
        assert safe_next("/account") == "/account"
        assert safe_next("/admin/aircraft") == "/admin/aircraft"

    def test_same_host_absolute_url_is_accepted(self, safe_next):
        # http://localhost is what the test client uses.
        assert safe_next("http://localhost/aircraft") is not None

    def test_external_url_is_blocked(self, safe_next):
        assert safe_next("https://evil.com/phish") is None
        assert safe_next("http://evil.com/phish") is None

    def test_protocol_relative_url_is_blocked(self, safe_next):
        # //evil.com/x — browsers resolve this against the current scheme,
        # so it'd silently send the user to evil.com over HTTPS.
        assert safe_next("//evil.com/x") is None

    def test_javascript_scheme_is_blocked(self, safe_next):
        # If we redirected to ``javascript:alert(1)``, opening it would
        # execute JS in our origin's context — XSS via redirect.
        assert safe_next("javascript:alert(1)") is None

    def test_data_scheme_is_blocked(self, safe_next):
        assert safe_next("data:text/html,<script>alert(1)</script>") is None


# ─────────────────────────────────────────────────────────────────────
# _apply_sort — column whitelist
# ─────────────────────────────────────────────────────────────────────

class TestApplySort:
    """The sort_by query param must be a member of a whitelist or the
    request silently falls back to the default order. Anything else is a
    SQL-injection vector dressed up as a feature request."""

    def test_valid_column_orders_asc(self, app, db_session):
        import app as appmod, models
        with app.test_request_context("/?sort_by=manufacturer&sort_dir=asc"):
            q = appmod._apply_sort(
                models.Aircraft.query, appmod._AIRCRAFT_SORT_COLUMNS,
                default_order=(models.Aircraft.model,),
            )
            sql = str(q.statement.compile(compile_kwargs={"literal_binds": False}))
            assert "ORDER BY aircraft.manufacturer ASC" in sql

    def test_valid_column_orders_desc(self, app, db_session):
        import app as appmod, models
        with app.test_request_context("/?sort_by=manufacturer&sort_dir=desc"):
            q = appmod._apply_sort(
                models.Aircraft.query, appmod._AIRCRAFT_SORT_COLUMNS,
                default_order=(models.Aircraft.model,),
            )
            sql = str(q.statement.compile(compile_kwargs={"literal_binds": False}))
            assert "ORDER BY aircraft.manufacturer DESC" in sql

    def test_unknown_column_falls_back_to_default(self, app, db_session):
        import app as appmod, models
        with app.test_request_context("/?sort_by=password_hash&sort_dir=asc"):
            q = appmod._apply_sort(
                models.Aircraft.query, appmod._AIRCRAFT_SORT_COLUMNS,
                default_order=(models.Aircraft.model,),
            )
            sql = str(q.statement.compile(compile_kwargs={"literal_binds": False}))
            assert "password_hash" not in sql, "non-whitelisted column leaked into SQL!"
            assert "ORDER BY aircraft.model" in sql

    def test_sql_injection_attempt_is_ignored(self, app, db_session):
        """Probe with classic injection bait — must NOT appear in compiled SQL."""
        import app as appmod, models
        bait = "1; DROP TABLE users--"
        with app.test_request_context(f"/?sort_by={bait}"):
            q = appmod._apply_sort(
                models.Aircraft.query, appmod._AIRCRAFT_SORT_COLUMNS,
                default_order=(models.Aircraft.model,),
            )
            sql = str(q.statement.compile(compile_kwargs={"literal_binds": False}))
            assert "DROP" not in sql.upper()

    def test_no_sort_by_uses_default_order(self, app, db_session):
        import app as appmod, models
        with app.test_request_context("/"):
            q = appmod._apply_sort(
                models.Aircraft.query, appmod._AIRCRAFT_SORT_COLUMNS,
                default_order=(models.Aircraft.model, models.Aircraft.variant),
            )
            sql = str(q.statement.compile(compile_kwargs={"literal_binds": False}))
            assert "ORDER BY aircraft.model" in sql
            assert "aircraft.variant" in sql


# ─────────────────────────────────────────────────────────────────────
# _normalize_tail_number — empty/whitespace folding
# ─────────────────────────────────────────────────────────────────────

class TestNormalizeTailNumber:
    """Tail numbers are optional. Treating "" the same as NULL keeps
    duplicate detection sane — multiple unmarked airframes shouldn't
    collide with each other."""

    @pytest.mark.parametrize("raw,expected", [
        (None,            None),
        ("",              None),
        ("   ",           None),    # whitespace-only collapses to None
        ("\t\n",          None),    # any whitespace
        ("55-0014",       "55-0014"),
        ("  55-0014  ",   "55-0014"),  # padding stripped
        ("ZH662",         "ZH662"),
    ])
    def test_normalizes(self, raw, expected):
        from app import _normalize_tail_number
        assert _normalize_tail_number(raw) == expected


# ─────────────────────────────────────────────────────────────────────
# _validate_password_strength — policy enforcement
# ─────────────────────────────────────────────────────────────────────

class TestPasswordPolicy:
    """Defaults: >=8 chars, requires both letter and digit."""

    def test_rejects_none(self):
        from app import _validate_password_strength
        assert _validate_password_strength(None) is not None

    def test_rejects_too_short(self):
        from app import _validate_password_strength
        # 7 chars even with mixed
        err = _validate_password_strength("abc1234")
        assert err is not None and "8 characters" in err

    def test_rejects_letters_only(self):
        from app import _validate_password_strength
        err = _validate_password_strength("longenoughbutletters")
        assert err is not None and "digit" in err

    def test_rejects_digits_only(self):
        from app import _validate_password_strength
        err = _validate_password_strength("12345678")
        assert err is not None and "letter" in err

    def test_accepts_valid(self):
        from app import _validate_password_strength
        assert _validate_password_strength("letters1") is None
        assert _validate_password_strength("Tester-1234") is None
