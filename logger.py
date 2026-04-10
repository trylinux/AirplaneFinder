"""Structured logging for Aircraft Finder.

Three dedicated log files under ``logs/``:
  - **auth.log** — login attempts, logouts, failed auth, API key usage
  - **changes.log** — all POST / PUT / PATCH / DELETE that modify data
  - **access.log** — every GET request (page views + API reads)
"""

import os
import logging
from logging.handlers import RotatingFileHandler

_LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
_MAX_BYTES = 5 * 1024 * 1024   # 5 MB per file
_BACKUP_COUNT = 5               # keep 5 rotated copies

_FMT = logging.Formatter(
    "[%(asctime)s] %(levelname)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def _make_logger(name, filename):
    """Create a named logger that writes to ``logs/<filename>``."""
    os.makedirs(_LOG_DIR, exist_ok=True)
    handler = RotatingFileHandler(
        os.path.join(_LOG_DIR, filename),
        maxBytes=_MAX_BYTES,
        backupCount=_BACKUP_COUNT,
    )
    handler.setFormatter(_FMT)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)
    logger.propagate = False
    return logger


auth_log = _make_logger("amt.auth", "auth.log")
change_log = _make_logger("amt.changes", "changes.log")
access_log = _make_logger("amt.access", "access.log")
