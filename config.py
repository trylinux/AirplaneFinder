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

    # Logging
    LOG_DIR = _get("app", "log_dir", "LOG_DIR", os.path.join(os.path.dirname(__file__), "logs"))

    # Pagination
    RESULTS_PER_PAGE = int(_get("app", "results_per_page", "RESULTS_PER_PAGE", "20"))
