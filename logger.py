"""Structured logging for Aircraft Finder.

Three dedicated log files under ``logs/``:
  - **auth.log** — login attempts, logouts, failed auth, API key usage
  - **changes.log** — all POST / PUT / PATCH / DELETE that modify data
  - **access.log** — every GET request (page views + API reads)
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler

_LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
_MAX_BYTES = 5 * 1024 * 1024   # 5 MB per file
_BACKUP_COUNT = 5               # keep 5 rotated copies

_FMT = logging.Formatter(
    "[%(asctime)s] %(levelname)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def _build_handler(filename):
    """Try to build a RotatingFileHandler for ``logs/<filename>``.

    Falls back to a stderr StreamHandler if the file path can't be opened —
    most commonly a PermissionError when ``logs/`` was created by a different
    user (e.g. someone ran ``sudo python app.py`` for testing and now
    gunicorn-as-debian can't write the file). The previous behavior was to
    raise during module import, which crashed every gunicorn worker on every
    request and brought the entire site down.
    """
    try:
        os.makedirs(_LOG_DIR, exist_ok=True)
        handler = RotatingFileHandler(
            os.path.join(_LOG_DIR, filename),
            maxBytes=_MAX_BYTES,
            backupCount=_BACKUP_COUNT,
        )
        return handler, None
    except OSError as exc:
        # OSError covers PermissionError, FileNotFoundError, ENOSPC (disk
        # full), read-only filesystem, etc. — anything that would prevent
        # the file from being opened. Fall through to stderr.
        return logging.StreamHandler(sys.stderr), exc


def _make_logger(name, filename):
    """Create a named logger that writes to ``logs/<filename>`` if possible,
    or to stderr if the file can't be opened. Either way, callers always get
    a working logger and the app stays up."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if logger.handlers:
        # Already configured — happens if the module is reloaded (e.g. in a
        # test harness or under flask --debug auto-reloader).
        return logger

    handler, fallback_reason = _build_handler(filename)
    handler.setFormatter(_FMT)
    logger.addHandler(handler)

    # If we fell back, leave a single line on stderr at startup so an
    # operator notices the misconfig — without this, structured logs
    # silently start going to stderr and look "missing".
    if fallback_reason is not None:
        sys.stderr.write(
            f"[logger] WARNING: could not open {filename} "
            f"({fallback_reason.__class__.__name__}: {fallback_reason}); "
            f"logging '{name}' to stderr instead\n"
        )
    return logger


auth_log = _make_logger("amt.auth", "auth.log")
change_log = _make_logger("amt.changes", "changes.log")
access_log = _make_logger("amt.access", "access.log")
