"""Dependency-free designation rules shared by the server and maintenance tools."""

_DIGITS = "0123456789"


def join_designation(model, variant):
    """Join a model and variant the way the generated column does."""
    model = (model or "").strip()
    variant = (variant or "").strip()
    if not variant:
        return model
    if variant[0] in _DIGITS:
        return f"{model}-{variant}"
    if model and model[-1] in _DIGITS:
        return f"{model}{variant}"
    return f"{model} {variant}"


def airframe_key(row):
    return (join_designation(row.get('model'), row.get('variant')).casefold(),
            (row.get('tail_number') or '').strip().casefold(),
            (row.get('operator_country') or '').strip().casefold())


_CN_PLACEHOLDERS = {'unknown', 'unk', 'n/a', 'na', 'none', 'nil', '-', '--',
                    '?', '??', 'tbd', 'x', 'xx'}


def is_usable_construction_number(value):
    value = (value or '').strip()
    return bool(value) and value.casefold() not in _CN_PLACEHOLDERS


def identity_keys(row):
    """Strong application duplicate keys; never infer identity from a blank tail."""
    keys = set()
    if row.get('tail_number') and row['tail_number'].strip():
        keys.add(('tail',) + airframe_key(row))
    if row.get('manufacturer') and is_usable_construction_number(row.get('construction_number')):
        keys.add(('cn',) + tuple((row.get(field) or '').strip().casefold()
                                for field in ('manufacturer', 'model', 'construction_number')))
    return keys
