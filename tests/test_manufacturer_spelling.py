"""Manufacturer spelling normalisation.

Manufacturer is a facet visitors filter on, so one company spelled two ways
splits its own results. The catalog has three kinds of split and they do not
get the same treatment — which is the whole point of these tests.

The asymmetry that matters: a legitimate name left alone costs nothing, while
a legitimate name "corrected" into something else is a silent data error in a
column the search UI groups by.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from plan_manufacturers import (  # noqa: E402
    ACCENT_EXCEPTIONS, TRANSLITERATION, accent_count, choose_accented, strip_accents,
)


# ── the transliteration map ──────────────────────────────────────────

def test_transliteration_targets_are_not_themselves_misspellings():
    """Every canonical value must be a spelling the map does not also rewrite,
    or applying it twice would keep moving the data."""
    for wrong, right in TRANSLITERATION.items():
        assert right not in TRANSLITERATION, f"{right} is both a target and a source"
        assert wrong != right


def _transcribe(s):
    """Fold the German/Polish conventions onto the English ones, so the two
    renderings of one Russian name land on the same string: J is Y, W is V,
    SCH is SH and CH is KH (Suchoj / Sukhoi)."""
    s = s.lower().replace("-", "")
    for a, b in (("sch", "sh"), ("ch", "kh"), ("j", "y"), ("w", "v")):
        s = s.replace(a, b)
    return s


@pytest.mark.parametrize("wrong,right", sorted(TRANSLITERATION.items()))
def test_transliteration_pairs_are_the_same_name(wrong, right):
    """A guard against a typo in the map itself: after folding the German and
    Polish spelling conventions, the two renderings must agree for at least
    their first four characters — enough to catch "Suchoj" -> "Tupolev"."""
    a, b = _transcribe(wrong), _transcribe(right)
    assert a[:4] == b[:4], f"{wrong} and {right} do not look like the same name ({a} vs {b})"


def test_real_german_names_with_the_same_shape_are_not_in_the_map():
    """Bölkow, Schleicher, Lommatzsch and Barkley-Grow all carry the -ow/-sch
    shapes a naive rule would match. A general rule would rewrite them; the
    curated map must not contain them."""
    for name in ("Bölkow", "Bolkow", "Schleicher", "Lommatzsch", "Barkley-Grow",
                 "Messerschmitt", "Schneider", "Schweizer", "Snow", "Arrow", "Harlow"):
        assert name not in TRANSLITERATION


def test_mikoyan_alone_is_not_rewritten_to_mikoyan_gurevich():
    """Post-Gurevich aircraft (MiG-29, MiG-31) are correctly filed under
    "Mikoyan". It is a different company name, not a short spelling."""
    assert "Mikoyan" not in TRANSLITERATION


# ── the accent rule ──────────────────────────────────────────────────

def test_accent_count_is_not_confused_by_length_changing_strips():
    assert accent_count("Aerospatiale") == 0
    assert accent_count("Aérospatiale") == 1
    assert accent_count("PZL-Świdnik") == 1
    assert accent_count("Messerschmitt-Bölkow-Blohm") == 1
    assert strip_accents("Aérospatiale") == "Aerospatiale"


@pytest.mark.parametrize("forms,expected", [
    (["Aerospatiale", "Aérospatiale"], "Aérospatiale"),
    (["Zlin", "Zlín"], "Zlín"),                       # minority spelling still wins
    (["Bleriot", "Blériot"], "Blériot"),
    (["Bucker", "Bücker"], "Bücker"),
    (["PZL-Swidnik", "PZL-Świdnik"], "PZL-Świdnik"),
    (["Hispano Aviacion", "Hispano Aviación"], "Hispano Aviación"),
    (["Bolkow", "Bölkow"], "Bölkow"),
    (["Goppingen", "Göppingen"], "Göppingen"),
])
def test_accented_form_wins_regardless_of_how_common_it_is(forms, expected):
    """Frequency is not evidence of correctness here. "Zlin" outnumbers "Zlín"
    39 to 28 and is still the transcription loss."""
    assert choose_accented(forms)[0] == expected


def test_breguet_is_the_exception_the_exception_list_exists_for():
    """Louis Charles Breguet's surname takes an accent, but the AIRCRAFT
    COMPANY wrote itself Breguet — Breguet 19, Breguet Atlantic — and the
    references follow it. Prefer-the-accented-form would get this backwards,
    and no rule can infer it."""
    assert choose_accented(["Breguet", "Bréguet"])[0] == "Breguet"
    assert "breguet" in ACCENT_EXCEPTIONS


def test_exception_lookup_is_accent_and_case_insensitive():
    """The exception is keyed on the folded name, so it fires whichever
    spelling happens to appear first."""
    assert choose_accented(["Bréguet", "Breguet"])[0] == "Breguet"


def test_two_differently_accented_forms_go_to_review():
    """Nothing here can choose between them, so the script must not try."""
    winner, reason = choose_accented(["Motörlet", "Mötorlet"])
    assert winner is None and "differently" in reason


def test_forms_with_no_accent_at_all_go_to_review():
    """A pure case split is not this rule's business — ERCO vs Erco is an
    acronym question a person answers."""
    winner, _ = choose_accented(["ERCO", "Erco"])
    assert winner is None
