"""logger.py — file → stderr fallback.

Pinned regression: a permission error on /home/.../logs/auth.log used to
crash gunicorn workers on every request, taking the site down. The fix
falls back to stderr; this test makes sure that fallback stays.
"""

import contextlib
import importlib
import io
import logging
import logging.handlers
import os
import shutil
import sys
import tempfile

import pytest


@pytest.fixture
def reset_loggers():
    """Drop any handlers attached to our named loggers so each test starts
    from a clean state. Reload the module so module-level loggers are
    rebuilt against whatever _LOG_DIR we want for this test."""
    names = ["amt.auth", "amt.changes", "amt.access",
             "amt.auth.test", "amt.changes.test", "amt.access.test"]
    yield names
    for n in names:
        lg = logging.getLogger(n)
        lg.handlers.clear()


def test_writable_log_dir_uses_rotating_file_handler(reset_loggers):
    """Happy path — when logs/ is writable, the file handler is used."""
    import logger
    importlib.reload(logger)
    handlers = logger.auth_log.handlers
    assert handlers, "auth_log has no handlers"
    assert isinstance(handlers[0], logging.handlers.RotatingFileHandler)


def test_unwritable_log_dir_falls_back_to_stderr(reset_loggers):
    """The bug we're protecting against: an unwritable logs/ directory
    used to raise on import. It should now produce a fallback handler
    AND a one-time warning on stderr, without raising."""
    import logger
    importlib.reload(logger)

    # chmod 000 the dir — opening a file inside is now PermissionError.
    unwritable = tempfile.mkdtemp(prefix="logger-test-")
    os.chmod(unwritable, 0o000)
    try:
        logger._LOG_DIR = unwritable

        captured = io.StringIO()
        with contextlib.redirect_stderr(captured):
            auth = logger._make_logger("amt.auth.test", "auth.log")
            chg  = logger._make_logger("amt.changes.test", "changes.log")
            acc  = logger._make_logger("amt.access.test", "access.log")
            # Emit records inside the same redirect window so we can
            # verify they actually flow through. Note: the StreamHandler
            # captures whatever sys.stderr was at construction, which
            # IS the StringIO here — so records land in `captured`.
            auth.info("auth-probe")
            chg.info("changes-probe")
            acc.info("access-probe")

        text = captured.getvalue()

        # ── Behavioral assertions ─────────────────────────────────
        # 1. Each logger has a StreamHandler, NOT a RotatingFileHandler.
        for lg in (auth, chg, acc):
            h = lg.handlers[0]
            assert isinstance(h, logging.StreamHandler)
            assert not isinstance(h, logging.handlers.RotatingFileHandler), (
                f"{lg.name} kept the file handler — fallback didn't engage"
            )

        # 2. One warning per logger surfaced on stderr (operator visibility).
        warnings = text.count("[logger] WARNING: could not open")
        assert warnings == 3, (
            f"expected 3 fallback warnings, got {warnings}\n--- captured ---\n{text}"
        )

        # 3. Records actually flowed through.
        for needle in ("auth-probe", "changes-probe", "access-probe"):
            assert needle in text, f"fallback handler dropped: {needle!r}"

    finally:
        os.chmod(unwritable, 0o755)
        shutil.rmtree(unwritable, ignore_errors=True)


def test_repeated_make_logger_does_not_double_attach(reset_loggers):
    """If the module is reloaded (auto-reloader, test harness, etc.) the
    logger should NOT end up with N copies of the same handler — that
    causes duplicated log lines and was a real footgun before."""
    import logger
    importlib.reload(logger)
    n_before = len(logger.auth_log.handlers)
    logger._make_logger("amt.auth", "auth.log")
    logger._make_logger("amt.auth", "auth.log")
    n_after = len(logger.auth_log.handlers)
    assert n_after == n_before, (
        f"handlers grew from {n_before} to {n_after} — _make_logger isn't idempotent"
    )
