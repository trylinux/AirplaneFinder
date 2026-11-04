"""Shared validation at catalog, API, and rendering trust boundaries."""
import re
from urllib.parse import urlsplit


def safe_http_url(value):
    """Return an absolute HTTP(S) URL, or None for unsafe/invalid input.

    Escaping HTML alone does not make a javascript: URL safe. Apply this
    when rendering old records too, since validation only protects new writes.
    """
    if not isinstance(value, str) or not value.strip():
        return None
    value = value.strip()
    if re.search(r'[\x00-\x20\x7f\\]', value):
        return None
    try:
        parsed = urlsplit(value)
        if (parsed.scheme.lower() not in ('http', 'https') or not parsed.hostname
                or parsed.username is not None or parsed.password is not None):
            return None
        parsed.port  # Reject malformed ports as well as malformed IPv6 hosts.
    except ValueError:
        return None
    return value


def model_text_errors(data, model):
    """Validate supplied text against ORM column lengths before DB writes.

    SQLite does not enforce VARCHAR sizes, while production MySQL does.
    TEXT is bounded by UTF-8 bytes to fit MySQL's 65,535-byte TEXT storage.
    """
    from sqlalchemy import String, Text
    errors = []
    for column in model.__table__.columns:
        if column.name not in data or not isinstance(column.type, String):
            continue
        value = data[column.name]
        if value is None:
            continue
        if not isinstance(value, str):
            errors.append({'field': column.name, 'message': 'must be a string'})
        elif column.type.length and len(value) > column.type.length:
            errors.append({'field': column.name, 'message': f'must be at most {column.type.length} characters'})
        elif isinstance(column.type, Text) and len(value.encode('utf-8')) > 65535:
            errors.append({'field': column.name, 'message': 'must be at most 65535 UTF-8 bytes'})
    return errors


def alias_errors(value):
    if value is None or value == '':
        return []
    aliases = value.split(';') if isinstance(value, str) else value
    if not isinstance(aliases, list) or any(not isinstance(a, str) for a in aliases):
        return [{'field': 'aliases', 'message': 'must be an array of strings or semicolon-separated text'}]
    if len(aliases) > 500 or any(len(a.strip()) > 200 for a in aliases):
        return [{'field': 'aliases', 'message': 'at most 500 aliases of 200 characters each'}]
    return []
