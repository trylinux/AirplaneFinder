"""Application configuration.

Reads settings from web.config (INI format) if present, then falls back
to environment variables, then to built-in defaults.  Copy
web.config.example to web.config and edit for your environment.
"""

import os
import configparser

_cfg = configparser.ConfigParser()
_cfg.read(os.path.join(os.path.dirname(__file__), "web.config"))


def _get(section, key, env_var, default):
    """Read from web.config → env var → default."""
    try:
        return _cfg.get(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return os.environ.get(env_var, default)


class Config:
    SECRET_KEY = _get("app", "secret_key", "SECRET_KEY", "change-me-in-production")

    # Server (used by app.run in __main__)
    SERVER_HOST = _get("server", "host", "SERVER_HOST", "0.0.0.0")
    SERVER_PORT = int(_get("server", "port", "SERVER_PORT", "5000"))
    SERVER_DEBUG = _get("server", "debug", "SERVER_DEBUG", "true").lower() in ("1", "true", "yes")

    # MySQL connection
    MYSQL_HOST = _get("database", "host", "MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = int(_get("database", "port", "MYSQL_PORT", "3306"))
    MYSQL_USER = _get("database", "user", "MYSQL_USER", "root")
    MYSQL_PASSWORD = _get("database", "password", "MYSQL_PASSWORD", "")
    MYSQL_DB = _get("database", "database", "MYSQL_DB", "airplane_museum_tracker")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Engine pool: MySQL closes idle connections after wait_timeout (default
    # 8 hours, but shorter on many managed providers). pool_pre_ping issues a
    # cheap SELECT 1 before handing a connection to the app so stale
    # connections are replaced instead of surfacing as OperationalError, and
    # pool_recycle caps the lifetime of a pooled connection below the server's
    # timeout.
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": int(_get("database", "pool_size", "DB_POOL_SIZE", "10")),
        "max_overflow": int(_get("database", "max_overflow", "DB_MAX_OVERFLOW", "20")),
        "pool_recycle": int(_get("database", "pool_recycle", "DB_POOL_RECYCLE", "1800")),
        "pool_pre_ping": True,
    }

    # Logging
    LOG_DIR = _get("app", "log_dir", "LOG_DIR", os.path.join(os.path.dirname(__file__), "logs"))

    # Pagination
    RESULTS_PER_PAGE = int(_get("app", "results_per_page", "RESULTS_PER_PAGE", "20"))

    # ─── Auth security ────────────────────────────────────────────────────
    # Idle timeout: log a user out after this many seconds of no activity.
    # Tighter for higher-privilege roles since they can do more damage if
    # someone walks up to an unattended browser.
    SESSION_IDLE_TIMEOUT_ADMIN   = int(_get("auth", "idle_timeout_admin",   "SESSION_IDLE_TIMEOUT_ADMIN",   str(15 * 60)))   # 15 min
    SESSION_IDLE_TIMEOUT_MANAGER = int(_get("auth", "idle_timeout_manager", "SESSION_IDLE_TIMEOUT_MANAGER", str(30 * 60)))   # 30 min
    SESSION_IDLE_TIMEOUT_VIEWER  = int(_get("auth", "idle_timeout_viewer",  "SESSION_IDLE_TIMEOUT_VIEWER",  str(60 * 60)))   # 60 min

    # Absolute timeout: regardless of activity, log out after this many
    # seconds since login. Caps the blast radius of a stolen session cookie.
    SESSION_ABSOLUTE_TIMEOUT     = int(_get("auth", "absolute_timeout",     "SESSION_ABSOLUTE_TIMEOUT",     str(12 * 60 * 60)))   # 12 hours

    # Failed-login lockout: lock the account for this many seconds after
    # this many consecutive failed attempts. Keyed by username; clears on
    # any successful login.
    LOGIN_LOCKOUT_MAX_ATTEMPTS   = int(_get("auth", "lockout_max_attempts", "LOGIN_LOCKOUT_MAX_ATTEMPTS", "5"))
    LOGIN_LOCKOUT_DURATION       = int(_get("auth", "lockout_duration",     "LOGIN_LOCKOUT_DURATION",     str(15 * 60)))   # 15 min

    # Password policy: minimum length and required character classes.
    # Enforced on register, admin-create-user, and any password change.
    PASSWORD_MIN_LENGTH          = int(_get("auth", "password_min_length",  "PASSWORD_MIN_LENGTH",  "8"))
    # When True, password must contain at least one letter AND one digit.
    PASSWORD_REQUIRE_MIXED       = _get("auth", "password_require_mixed", "PASSWORD_REQUIRE_MIXED", "true").lower() in ("1", "true", "yes")
