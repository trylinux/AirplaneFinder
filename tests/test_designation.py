"""full_designation joins model + variant the way aviation writes it.

The rule exists in three places that must agree:
  - ``models.join_designation``  — the readable original
  - ``schema.sql``               — the MySQL generated column (prod)
  - ``tests/conftest.py``        — the SQLite mirror (tests)

The last two can only be checked by running them, which is what
``test_sql_matches_python`` does: it inserts real model/variant pairs and
compares the database's answer to the Python function's.
"""

import pytest

import models

# One row per bucket, plus the edge cases that shaped the rule.
CASES = [
    # model ends in a digit, variant starts with a letter -> no separator
    ("SR-71", "A", "SR-71A"),
    ("F-4", "C", "F-4C"),
    ("B-52", "D", "B-52D"),
    ("UH-1", "H", "UH-1H"),
    ("MiG-21", "PF", "MiG-21PF"),
    ("Model 47", "B", "Model 47B"),
    # variant starts with a digit -> a dash
    ("747", "100", "747-100"),
    ("PA-28", "180", "PA-28-180"),
    ("L-1011", "500", "L-1011-500"),
    ("FJ", "1", "FJ-1"),
    ("R4D", "6S", "R4D-6S"),
    ("ZPG", "2", "ZPG-2"),
    # both sides alphabetic -> a space
    ("Vampire", "T.35", "Vampire T.35"),
    ("Hurricane", "Mk.IIC", "Hurricane Mk.IIC"),
    ("Titan", "II", "Titan II"),
    ("Lysander", "III", "Lysander III"),
    # no variant at all
    ("DC-3", None, "DC-3"),
    ("B-29", "", "B-29"),
    ("Navion", None, "Navion"),
]


@pytest.mark.parametrize("model,variant,expected", CASES)
def test_python_rule(model, variant, expected):
    assert models.join_designation(model, variant) == expected


@pytest.mark.parametrize("model,variant,expected", CASES)
def test_sql_matches_python(make_aircraft, model, variant, expected):
    """The generated column must produce what join_designation() says."""
    a = make_aircraft(model=model, variant=variant, tail_number=None)
    assert a.full_designation == expected
    assert a.full_designation == models.join_designation(model, variant)


def test_the_old_double_dash_form_is_gone(make_aircraft):
    """Regression: the whole point of the change."""
    a = make_aircraft(model="SR-71", variant="A")
    assert a.full_designation != "SR-71-A"
    assert a.full_designation == "SR-71A"


def test_to_dict_fallback_agrees_with_the_column(make_aircraft):
    """to_dict falls back to Python for unflushed rows; same answer either way."""
    a = make_aircraft(model="F-105", variant="G", tail_number="63-8320")
    assert a.to_dict()["full_designation"] == a.full_designation == "F-105G"


def test_designation_is_searchable(client, make_aircraft):
    a = make_aircraft(model="SR-71", variant="A", tail_number="61-7976")
    hits = client.get("/api/v1/aircraft/search", query_string={"q": "SR-71A"}).get_json()
    assert any(r["id"] == a.id for r in hits["results"]), "new form must be searchable"
    hits = client.get("/api/v1/aircraft/search", query_string={"q": "SR-71"}).get_json()
    assert any(r["id"] == a.id for r in hits["results"]), "base model must still match"
