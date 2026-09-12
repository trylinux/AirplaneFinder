"""Aliases are alternative NAMES for an airframe, not notes about it.

`aliases` is a separate table joined into aircraft search (see
`_build_aircraft_filter`), so prose stored there becomes a search term:
a note reading "confirmed still in place March 2026" makes the airframe
match a search for "place". Notes belong in `description`.

These tests guard the convention across every research CSV under data/.
"""
import csv
import glob
import io
import os
import re

import pytest

import models

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
FILES = sorted(f for f in glob.glob(os.path.join(DATA, "**", "*_aircraft.csv"),
                                    recursive=True)
               # data/_to_delete/ holds superseded builds the bridge cannot
               # remove. Validating them fails the suite on data that is not
               # part of the project any more.
               if "_to_delete" not in f.split(os.sep))

# A verb in an alias means it is a sentence, not a name.
PROSE = re.compile(
    r"\b(is|are|was|were|has|have|had|been|delivered|served|flew|flown|"
    r"displayed|restored|arrived|painted|moved|sold|stood|stands|confirmed|"
    r"reported|acquired|donated|transferred|retired|wears|carries|represents|"
    r"honou?rs|dedicated|remains|includes|assigned|operated|listed|recorded|"
    r"appears|shown|placed|installed|loaned|owned|used|until|since|according)\b",
    re.I,
)
MAX_WORDS = 4
MAX_CHARS = 34

# Descriptive attributes that are not names either; they belong in description.
NOT_A_NAME = {
    "replica", "reproduction", "airworthy", "inert", "outdoors", "indoors",
    "flying", "flyable", "static", "prototype", "mockup", "mock-up",
    "full scale", "full-scale", "pylon-mounted", "pole-mounted",
    "museum-owned", "privately owned", "on loan", "unverified",
}


def _rows(path):
    with open(path, "rb") as fh:
        text = fh.read().decode("utf-8")
    return list(csv.DictReader(io.StringIO(text, newline="")))


def _aliases(row):
    return [p.strip() for p in (row.get("aliases") or "").split(";") if p.strip()]


@pytest.mark.parametrize("path", FILES, ids=[os.path.basename(p) for p in FILES])
def test_aliases_contain_no_prose(path):
    bad = []
    for row in _rows(path):
        for alias in _aliases(row):
            # Royal Navy mark prefixes -- HAS, HAR, HU, AEW -- are
            # designations, not prose. "Wasp HAS.1" is a name; the detector
            # sees the verb "has".
            if re.match(r"^[A-Za-z][A-Za-z0-9 .\-]*\bHAS[.\-]?\d", alias, re.I) \
                    or re.match(r"^HAS[.\-]?\d", alias, re.I):
                continue
            if PROSE.search(alias):
                bad.append((row.get("model"), alias, "reads as a sentence"))
            elif len(alias.split()) > MAX_WORDS or len(alias) > MAX_CHARS:
                bad.append((row.get("model"), alias, "too long to be a name"))
            elif alias.lower() in NOT_A_NAME:
                bad.append((row.get("model"), alias, "an attribute, not a name"))
    assert not bad, "aliases must be alternative names; move these to description:\n" + "\n".join(
        f"  {m}: {a!r} — {why}" for m, a, why in bad
    )


DESIG = re.compile(r"^([A-Za-z]{1,4})-(\d{1,3}[A-Za-z]{0,3})$")


@pytest.mark.parametrize("path", FILES, ids=[os.path.basename(p) for p in FILES])
def test_dashed_designations_have_a_dashless_alias(path):
    """PT-22 must also be findable as PT22."""
    missing = []
    for row in _rows(path):
        aliases = _aliases(row)
        have = {a.lower() for a in aliases}
        model, variant = (row.get("model") or "").strip(), (row.get("variant") or "").strip()
        # Use the real joining rule rather than a second copy of it, so this
        # test cannot drift from what full_designation actually contains.
        sources = [model, models.join_designation(model, variant)] + aliases
        for src in sources:
            m = DESIG.match(src)
            if m:
                flat = (m.group(1) + m.group(2))
                if flat.lower() not in have:
                    missing.append((row.get("tail_number") or model, src, flat))
    assert not missing, "dashless search variants missing:\n" + "\n".join(
        f"  {t}: {src} needs alias {flat}" for t, src, flat in missing
    )
