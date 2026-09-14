"""The variant-column cleanup classifier.

`variant` holds a mark or suffix and is half of the generated
`full_designation`. Research passes have also used it for the TYPE NAME,
which belongs in `model_name` — so the catalog renders headings like
"CT-133 Silver Star 3" and "SE 210 Caravelle".

The classifier's job is to separate the mechanical fixes from the judgement
calls, and the contract that matters is asymmetric: a row it declines to
touch costs nothing, while a row it edits wrongly is a silent data error in
a column that feeds a unique key. So every test below that asserts "leave
alone" is as load-bearing as the ones that assert a fix.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from plan_variants import classify, is_mark_token  # noqa: E402


# ── rows that must be left completely alone ──────────────────────────

@pytest.mark.parametrize("model,variant,model_name", [
    ("T-33", "A", "Shooting Star"),          # the ordinary case
    ("MiG-21", "bis", "Fishbed"),
    ("Hunter", "F.6", None),
    ("Spitfire", "Mk IX", None),             # British marks are written this way
    ("Canberra", "Mk 20", None),
    ("F-4", "EJ", "Phantom II"),
    ("Mi-8", "T", "Hip"),
    ("Su-22", "M4", "Fitter"),
    ("T-33", "", "Shooting Star"),           # already blank
    ("Impala", "Mk I", None),                # a real designation, not a stray name
])
def test_correct_rows_are_not_touched(model, variant, model_name):
    cls, patch, _ = classify(model, variant, model_name)
    assert cls is None and patch is None


# ── the mechanical classes ───────────────────────────────────────────

def test_class_D_blanks_a_variant_that_duplicates_model_name():
    cls, patch, _ = classify("SE 210", "Caravelle", "Caravelle")
    assert cls == "D" and patch == {"variant": None}


def test_class_D_is_case_insensitive():
    cls, patch, _ = classify("CM.170", "magister", "Magister")
    assert cls == "D" and patch == {"variant": None}


def test_class_B_strips_a_model_restated_in_the_variant():
    assert classify("A-4", "A-4KU", "Skyhawk")[1] == {"variant": "KU"}
    assert classify("1.131", "1.131E", "Jungmann")[1] == {"variant": "E"}


def test_class_B_does_not_fire_when_the_variant_only_looks_like_a_prefix():
    """"A" does not repeat "A-4" — and truncating it to nothing would erase
    a correct variant."""
    cls, patch, _ = classify("A-4", "A", "Skyhawk")
    assert cls is None and patch is None


def test_class_A_plus_keeps_the_mark_and_drops_the_duplicated_name():
    cls, patch, note = classify("CL-13", "Sabre Mk.6", "Sabre")
    assert cls == "A+" and patch == {"variant": "Mk.6"}
    assert "Sabre" in note


def test_class_A_plus_blanks_the_variant_when_nothing_but_the_name_is_left():
    cls, patch, _ = classify("DH-115", "Vampire", "Vampire Trainer")
    assert cls == "A+" and patch == {"variant": None}


def test_whitespace_is_tidied():
    cls, patch, _ = classify("T-33", "  A ", "Shooting Star")
    assert cls == "C" and patch == {"variant": "A"}


# ── the judgement calls, which must never be automatic ───────────────

@pytest.mark.parametrize("model,variant,model_name", [
    ("Pusher", "Model A", None),             # "Model" is a generic designator
    ("Taube", "Model F", None),
    ("47", "J-2 Ranger", "Sioux"),           # would overwrite a real model_name
    ("108", "2 Flying Station Wagon", "Voyager"),
    ("95", "B55 Baron", "Travel Air"),
])
def test_unaccounted_names_go_to_review_not_to_the_plan(model, variant, model_name):
    cls, patch, _ = classify(model, variant, model_name)
    assert cls == "A" and patch is None, "a name we cannot vouch for must not be auto-applied"


def test_known_limitation_a_designation_with_no_word_in_it_is_invisible():
    """"Alouette II" + "SE 3130" is a manufacturer designation sitting in the
    variant column, and it should be cleaned — but "SE" and "3130" both read
    as marks, so no rule here sees it. Documented rather than hacked around:
    widening the name test to catch it would start eating correct variants
    like "F.6" and "M4". These rows stay in the catalog until someone
    reviews them by eye."""
    assert classify("Alouette II", "SE 3130", None)[0] is None


def test_generic_designator_words_are_never_stripped():
    """"Type 91" is a whole designation. The A+ rule would otherwise see
    "Type" inside model_name "Type 91 Fighter", strip it, and leave the
    variant as the bare number "91" — worse than doing nothing."""
    cls, patch, _ = classify("Ki-11", "Type 91", "Type 91 Fighter")
    assert cls == "A" and patch is None


def test_review_rows_carry_no_patch_at_all():
    """Belt and braces: apply_variants.py only ever writes keys that do not
    start with underscore, so a review row leaking into the plan with a
    stray field would PATCH something. It must produce None."""
    for variant, model_name in (("J-2 Ranger", "Sioux"), ("Model A", None),
                                ("B55 Baron", "Travel Air")):
        assert classify("Whatever", variant, model_name)[1] is None


# ── the token test the classes are built on ──────────────────────────

@pytest.mark.parametrize("tok,expected", [
    ("A", True), ("F.6", True), ("Mk", True), ("IX", True), ("20", True),
    ("bis", True), ("M4", True), ("EJ", True),
    ("Magister", False), ("Junior", False), ("Caravelle", False),
    ("Silver", False), ("Musketeer", False),
])
def test_is_mark_token(tok, expected):
    assert is_mark_token(tok) is expected


# ── all-caps variant CODES are marks, not names ──────────────────────

@pytest.mark.parametrize("model,variant,model_name", [
    ("37", "AJSF", "Viggen"),          # a real Saab 37 variant designation
    ("7", "GCBC", "Citabria"),         # Citabria 7GCBC
    ("A.109", "A-II", "Hirundo"),
    ("Atlantic", "BR 1150 SIGINT", "Atlantic"),
    ("451", "T-MM Stršljen II", "Stršljen II"),
])
def test_uppercase_designation_codes_are_not_treated_as_names(model, variant, model_name):
    """An earlier version read these as type names and routed 61 correct rows
    to review. Names in this catalog are Title Case, so requiring upper case
    costs nothing and rescues all of them."""
    cls, patch, _ = classify(model, variant, model_name)
    assert cls in (None, "A+", "D"), f"{variant!r} was classified {cls}"
    if patch:
        assert patch.get("model_name") is None, "a code must never become a model_name"


# ── class E: move the name to the column it belongs in ───────────────

@pytest.mark.parametrize("model,variant,mark,name", [
    ("31-55", "A Senior Skyrocket", "A", "Senior Skyrocket"),
    ("19", "TF Super Bidon", "TF", "Super Bidon"),
    ("18", "A Flymobil", "A", "Flymobil"),
    ("24", "C8E Argus", "C8E", "Argus"),          # digit makes C8E a mark
    ("47", "J-3B1 Ranger", "J-3B1", "Ranger"),
    ("1002", "Pingouin", None, "Pingouin"),        # no mark at all
    ("757", "Viscount", None, "Viscount"),
])
def test_class_E_splits_mark_from_name_when_model_name_is_empty(model, variant, mark, name):
    cls, patch, _ = classify(model, variant, None)
    assert cls == "E"
    assert patch == {"variant": mark, "model_name": name}


@pytest.mark.parametrize("model,variant,mark,name", [
    ("CW-1", "Junior", None, "Junior"),          # Curtiss-Wright CW-1 Junior
    ("CM.170", "Magister", None, "Magister"),
])
def test_names_with_no_model_name_to_vouch_for_them_are_now_moved(model, variant, mark, name):
    """These used to go to review because nothing could confirm the name. With
    model_name empty there is nothing to lose: moving it is strictly better
    than leaving a name in the variant column."""
    cls, patch, _ = classify(model, variant, None)
    assert cls == "E" and patch == {"variant": mark, "model_name": name}


def test_class_E_takes_marks_from_both_ends():
    """"Silver Star 3" is the Silver Star, mark 3 — the trailing number is a
    mark that happens to sit last."""
    cls, patch, _ = classify("CT-133", "Silver Star 3", None)
    assert cls == "E" and patch == {"variant": "3", "model_name": "Silver Star"}


def test_class_E_never_overwrites_an_existing_model_name():
    """A Bell 47 is a Sioux in military service and a Ranger as the civil
    J-2. Both are right, so the script must not pick one."""
    cls, patch, note = classify("47", "J-2 Ranger", "Sioux")
    assert cls == "A" and patch is None
    assert "Sioux" in note and "Ranger" in note


def test_class_E_does_not_fire_when_there_is_no_name():
    """All marks and no name is an ordinary variant, not a split."""
    for variant in ("Mk I", "F.6", "A", "Mk 20"):
        cls, _, _ = classify("Whatever", variant, None)
        assert cls != "E", f"{variant!r} was split"


def test_split_helper_reports_no_name_for_pure_marks():
    from plan_variants import split_mark_and_name
    assert split_mark_and_name("Mk I") == ("", "")
    assert split_mark_and_name("AJSF") == ("", "")
    assert split_mark_and_name("A Senior Skyrocket") == ("A", "Senior Skyrocket")
