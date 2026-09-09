"""The Pima N–Z and NMUSAF M–Z top-up files must survive the real importer.

METHODOLOGY.md step 3: validate against the *real* importer, not a
reimplementation of it. `_validate_aircraft_row` is what the API will run on
these rows, so it is what the test runs. A reimplementation would drift, and
the drift would only show up as a rolled-back import against production.

The import is atomic: one bad row rejects the whole file. So the assertions
here are per-file and exhaustive rather than "mostly fine".
"""

import csv
from pathlib import Path

import pytest

# NOTE: `app` is imported inside the tests, not here. conftest's session-scoped
# _test_env fixture rewrites Config to point at SQLite before the app is
# constructed; importing at module scope runs create_app() during collection,
# against the real MySQL URI, and the suite dies on a missing pymysql.

DATA = Path(__file__).resolve().parent.parent / "data"

def _discover():
    """Every aircraft CSV under data/, keyed by filename stem.

    Hand-maintaining this dict was fine for two files and wrong by ten. The
    museum is read from the file itself: each file names exactly one, which
    test_every_row_names_the_right_museum then enforces.
    """
    found = {}
    for path in sorted(DATA.rglob("*_aircraft.csv")):
        stem = path.stem[:-len("_aircraft")]
        with open(path, newline="", encoding="utf-8") as f:
            first = next(csv.DictReader(f), None)
        if first is None:
            continue
        found[stem] = (path, first.get("museum_name", ""))
    return found


FILES = _discover()


def rows_of(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@pytest.fixture(params=sorted(FILES), ids=sorted(FILES))
def dataset(request):
    path, museum = FILES[request.param]
    assert path.is_file(), f"missing data file: {path}"
    return request.param, rows_of(path), museum


class TestImporterAccepts:

    def test_every_row_validates(self, dataset):
        from app import _validate_aircraft_row
        name, rows, _ = dataset
        assert rows, f"{name} is empty"
        failures = []
        for i, row in enumerate(rows, start=2):   # +2: header is line 1
            clean, errors = _validate_aircraft_row(row)
            if errors:
                failures.append(
                    f"line {i} ({row.get('manufacturer')} {row.get('model')}): "
                    + "; ".join(f"{e['field']}: {e['message']}" for e in errors))
        assert not failures, (
            f"{len(failures)} row(s) would be rejected, and because the import "
            f"is atomic that means NOTHING in the file imports:\n  "
            + "\n  ".join(failures[:10]))

    def test_every_row_names_the_right_museum(self, dataset):
        name, rows, museum = dataset
        wrong = {r["museum_name"] for r in rows} - {museum}
        assert not wrong, f"{name} has rows pointing at {wrong}"

    def test_no_row_sets_both_museum_id_and_name(self, dataset):
        _, rows, _ = dataset
        assert not [r for r in rows if r.get("museum_id")], \
            "museum_id and museum_name together is a validation error"


class TestDuplicateSafety:
    """The unique index is (model, tail_number), and NULL never collides."""

    def test_no_duplicate_model_and_tail_within_a_file(self, dataset):
        name, rows, _ = dataset
        seen = {}
        dupes = []
        for r in rows:
            tail = (r["tail_number"] or "").strip().lower()
            if not tail:
                continue
            key = (r["model"].strip().lower(), tail)
            if key in seen:
                dupes.append(key)
            seen[key] = True
        assert not dupes, f"{name} would violate the unique index: {dupes}"

    def test_untailed_rows_are_distinguishable(self, dataset):
        """A blank tail is NULL, so two identical untailed rows would both
        insert and then be indistinguishable forever.

        A museum holding two of a type is normal — Monino has two I-16s and
        two Po-2s with no published borts — so the rule is that the rows must
        differ in *something* a reader could use: variant, name, aliases or
        description. Two rows identical on all of those are the hazard.
        """
        name, rows, _ = dataset
        seen, dupes = set(), []
        for r in rows:
            if (r["tail_number"] or "").strip():
                continue
            key = tuple((r.get(k) or "").strip().lower() for k in
                        ("manufacturer", "model", "variant", "aircraft_name",
                         "aliases", "description", "year_built"))
            if key in seen:
                dupes.append(key[:3])
            seen.add(key)
        assert not dupes, (
            f"{name} has untailed rows that are identical in every "
            f"descriptive field: {dupes}")


class TestFieldHygiene:

    def test_wing_type_only_on_fixed_wing(self, dataset):
        name, rows, _ = dataset
        bad = [f"{r['manufacturer']} {r['model']} ({r['aircraft_type']})"
               for r in rows
               if r["aircraft_type"] != "fixed_wing" and r["wing_type"].strip()]
        assert not bad, f"{name}: helicopters and missiles have no wing type: {bad}"

    # Airframes that are fixed_wing only because the vocabulary has nowhere
    # else to put them, and that have no wing to describe. Both are recorded
    # with the reason in their own description field; filling in "monoplane"
    # would be a fabrication. Keep this list closed and argued.
    WINGLESS_BY_DESIGN = {
        # Q-designated, so fixed_wing by the drone convention - but a
        # ducted-fan lift vehicle with no wing at all.
        ("Honeywell", "RQ-16"),
        # Ground-effect machine (GEM-2X). Recorded fixed_wing for want of a
        # ground-effect category.
        ("Curtiss-Wright", "Model 2500"),
    }

    def test_fixed_wing_always_has_a_wing_type(self, dataset):
        name, rows, _ = dataset
        bad = [f"{r['manufacturer']} {r['model']}" for r in rows
               if r["aircraft_type"] == "fixed_wing"
               and not r["wing_type"].strip()
               and (r["manufacturer"], r["model"]) not in self.WINGLESS_BY_DESIGN]
        assert not bad, f"{name}: fixed-wing rows missing wing_type: {bad}"

    def test_year_built_is_a_year_not_a_serial(self, dataset):
        """The most common research error is filing a serial as a year."""
        name, rows, _ = dataset
        bad = [(r["model"], r["year_built"]) for r in rows
               if r["year_built"].strip()
               and not (r["year_built"].strip().isdigit()
                        # Le Bourget holds the only surviving original
                        # Chanute glider, built 1896.
                        and 1850 <= int(r["year_built"]) <= 2030)]
        assert not bad, f"{name}: year_built holds something that is not a year: {bad}"

    def test_model_does_not_swallow_the_variant(self, dataset):
        """'F-4E' in model defeats both full_designation and the unique index.

        Only flags the modern hyphenated pattern; legacy Navy designations
        (F4U, HO3S) and type names (Spitfire, Camel) are legitimately whole.

        A handful of designations genuinely end in a letter with no variant —
        the Northrop N-1M is the whole designation, not an N-1 mark M — so
        they are listed rather than allowed to fail the file forever.
        """
        import re
        WHOLE_DESIGNATIONS = {"N-1M", "D-558", "X-1E", "P-6E",
                              "S-1A",   # Interstate Cadet
                              "SM-8A",  # Stinson Junior
                              "FC-2W",  # Fairchild / LAN-built copy
                              "B-8M"}   # Bensen Gyro-Copter
        name, rows, _ = dataset
        bad = [f"{r['model']} (variant={r['variant']!r})" for r in rows
               if not r["variant"].strip()
               and r["model"].strip() not in WHOLE_DESIGNATIONS
               and re.fullmatch(r"[A-Z]{1,3}-\d+[A-Z]", r["model"].strip())]
        assert not bad, f"{name}: model contains the variant: {bad}"

    def test_no_untrimmed_whitespace(self, dataset):
        name, rows, _ = dataset
        bad = [(k, v) for r in rows for k, v in r.items()
               if isinstance(v, str) and v != v.strip()]
        assert not bad, f"{name}: untrimmed values: {bad[:5]}"

    def test_no_placeholder_values(self, dataset):
        """'Unknown' and 'None' are how a blank arrives dressed as data."""
        name, rows, _ = dataset
        junk = {"unknown", "none", "n/a", "na", "tbd", "unk", "-", "null"}
        # "NA" in the variant column is a designation, not "not applicable":
        # the Douglas AD-4NA is a real Skyraider variant. Only flag it there
        # when it is written as a placeholder would be (lowercase, or N/A).
        bad = [(r["model"], k, v) for r in rows for k, v in r.items()
               if isinstance(v, str) and v.strip().lower() in junk
               and not (k == "variant" and v.strip() == "NA")
               # "TBD" is also the Douglas Devastator's designation. A model
               # of TBD with a model_name set is a designation, not a
               # placeholder — though see WASHINGTON_NOTES on the Midway row.
               and not (k == "model" and v.strip() == "TBD"
                        and r.get("model_name", "").strip())]
        assert not bad, f"{name}: placeholder values that should be blank: {bad[:5]}"


class TestKnownBiplanes:
    """Types whose wing configuration is not in doubt.

    The BIPLANE lookup in build_pima_csv.py was keyed on the *designation*
    ("S-1C") while rows carry the split model ("S-1"), so two entries never
    matched and the Pitts Special — about the most recognisable aerobatic
    biplane there is — shipped as a monoplane. A dead lookup key fails
    silently; this test is what makes it fail loudly.
    """

    KNOWN_BIPLANES = [
        ("pima_topup_n_to_z", "Pitts", "S-1"),
        ("pima_topup_n_to_z", "PZL Mielec", "AN-2"),
        ("pima_topup_n_to_z", "Naval Aircraft Factory", "N3N"),
        ("pima_topup_n_to_z", "Sopwith", "Camel"),
        ("pima_topup_n_to_z", "Steen", "Skybolt"),
        ("pima_topup_n_to_z", "Waco", "RNF"),
        ("pima_topup_n_to_z", "Waco", "UPF-7"),
        ("pima_topup_n_to_z", "Waco", "ZKS-6"),
        ("pima_topup_n_to_z", "Wright Brothers", "Flyer"),
        ("nmusaf_topup_m_to_z", "Martin", "MB-2"),
        ("nmusaf_topup_m_to_z", "Nieuport", "28"),
        ("nmusaf_topup_m_to_z", "SPAD", "XIII"),
        ("nmusaf_topup_m_to_z", "SPAD", "VII"),
        ("nmusaf_topup_m_to_z", "Standard", "J-1"),
        ("nmusaf_topup_m_to_z", "Stearman", "PT-13"),
        ("nmusaf_topup_m_to_z", "Thomas-Morse", "S4"),
        ("nmusaf_topup_m_to_z", "Packard-LePere", "LUSAC 11"),
        ("nmusaf_topup_m_to_z", "Sopwith", "Camel"),
        ("nmusaf_topup_m_to_z", "Wright", "1909 Military Flyer"),
        # Udvar-Hazy
        ("udvarhazy", "Curtiss", "JN-4"),
        ("udvarhazy", "Curtiss", "F9C"),
        ("udvarhazy", "Boeing", "FB"),
        ("udvarhazy", "Boeing-Stearman", "N2S"),
        ("udvarhazy", "Nieuport", "28"),
        ("udvarhazy", "SPAD", "XVI"),
        ("udvarhazy", "Halberstadt", "CL.IV"),
        ("udvarhazy", "Caudron", "G.4"),
        ("udvarhazy", "Wright", "EX"),
        # EAA — an unusually biplane-heavy collection
        ("eaa", "Pitts", "S-1"),
        ("eaa", "Pitts", "S-2"),
        ("eaa", "Waco", "ARE"),
        ("eaa", "Waco", "Model 10"),
        ("eaa", "Waco", "CTO"),
        ("eaa", "Travel Air", "E-4000"),
        ("eaa", "Spartan", "C3"),
        ("eaa", "Pitcairn", "PA-7"),
        ("eaa", "Stearman", "Model 75"),
        ("eaa", "Great Lakes", "2T-1"),
        ("eaa", "Nieuport", "11"),
        # Museum of Flight — the Personal Courage Wing
        ("museum_of_flight", "Albatros", "D.Va"),
        ("museum_of_flight", "Aviatik", "D.I"),
        ("museum_of_flight", "Nieuport", "24"),
        ("museum_of_flight", "Nieuport", "27"),
        ("museum_of_flight", "Nieuport", "28"),
        ("museum_of_flight", "SPAD", "XIII"),
        ("museum_of_flight", "Sopwith", "Camel"),
        ("museum_of_flight", "Royal Aircraft Factory", "S.E.5"),
        ("museum_of_flight", "Fokker", "D.VII"),
        ("museum_of_flight", "Stearman", "PT-13"),
        ("museum_of_flight", "Stearman", "C-3"),
        ("museum_of_flight", "Boeing", "Model 100"),
        # Pensacola — many 1920s-30s Navy biplanes
        ("nnam_pensacola", "Boeing", "F4B"),
        ("nnam_pensacola", "Curtiss", "F6C"),
        ("nnam_pensacola", "Curtiss", "F7C"),
        ("nnam_pensacola", "Curtiss", "BFC"),
        ("nnam_pensacola", "Curtiss", "NC"),
        ("nnam_pensacola", "Curtiss", "N2C"),
        ("nnam_pensacola", "Grumman", "FF"),
        ("nnam_pensacola", "Grumman", "F3F"),
        ("nnam_pensacola", "Grumman", "J2F"),
        ("nnam_pensacola", "Naval Aircraft Factory", "N3N"),
        ("nnam_pensacola", "Thomas-Morse", "S-4"),
        ("nnam_pensacola", "Hanriot", "HD.1"),
        ("nnam_pensacola", "Vought", "VE-7"),
        # Duxford
        ("duxford", "Airco", "DH.9"),
        ("duxford", "Bristol", "F.2B"),
        ("duxford", "Fairey", "Swordfish"),
        ("duxford", "Gloster", "Gladiator"),
        ("duxford", "Hawker", "Fury"),
        ("duxford", "Hawker", "Nimrod"),
        ("duxford", "Royal Aircraft Factory", "R.E.8"),
        ("duxford", "Royal Aircraft Factory", "B.E.2"),
        ("duxford", "Fiat", "CR.42"),
        ("duxford", "Boeing-Stearman", "PT-17"),
        # Evergreen
        ("evergreen", "Beechcraft", "UC-43"),
        ("evergreen", "Naval Aircraft Factory", "N3N"),
        ("evergreen", "Pitts", "S-2"),
        ("evergreen", "Sopwith", "Camel"),
        # The PZL M-15 Belphegor is the only jet biplane ever built.
        ("monino", "PZL", "M-15"),
        # Le Bourget — a very large pre-1920 collection
        ("musee_de_lair", "Bréguet", "14"),
        ("musee_de_lair", "Bréguet", "19"),
        ("musee_de_lair", "Caudron", "G.4"),
        ("musee_de_lair", "Farman", "F.60"),
        ("musee_de_lair", "Nieuport", "11"),
        ("musee_de_lair", "SPAD", "VII"),
        ("musee_de_lair", "SPAD", "XIII"),
        ("musee_de_lair", "Voisin", "LAS"),
        ("musee_de_lair", "Fokker", "D.VII"),
        ("musee_de_lair", "Polikarpov", "I-153"),
        ("musee_de_lair", "Chanute", "Glider"),
        # Monino
        ("monino", "Antonov", "An-2"),
        ("monino", "Polikarpov", "I-15"),
        ("monino", "Polikarpov", "Po-2"),
        ("monino", "Polikarpov", "R-5"),
        ("monino", "Sikorsky", "Ilya Muromets"),
        ("monino", "Voisin", "LAS"),
    ]

    KNOWN_TRIPLANES = [("parque_museo_aeronautico_de_la_fard", "Zoilo Hermógenes García", "Poliplano")]

    @pytest.mark.parametrize("dataset_name,manufacturer,model", KNOWN_TRIPLANES)
    def test_recorded_as_a_triplane(self, dataset_name, manufacturer, model):
        rows = [r for r in rows_of(FILES[dataset_name][0])
                if r["manufacturer"] == manufacturer and r["model"] == model]
        assert rows and all(r["wing_type"] == "triplane" for r in rows)

    @pytest.mark.parametrize("dataset_name,manufacturer,model", KNOWN_BIPLANES,
                             ids=[f"{m}-{mo}" for _, m, mo in KNOWN_BIPLANES])
    def test_recorded_as_a_biplane(self, dataset_name, manufacturer, model):
        rows = rows_of(FILES[dataset_name][0])
        match = [r for r in rows if r["manufacturer"] == manufacturer
                 and r["model"] == model]
        assert match, f"{manufacturer} {model} is missing from {dataset_name}"
        for r in match:
            assert r["wing_type"] == "biplane", (
                f"{manufacturer} {model} is a biplane, recorded as "
                f"{r['wing_type']!r}")


class TestRoleConsistencyAcrossMuseums:
    """The same type in the same configuration should not be a fighter at one
    museum and electronic warfare at another."""

    def test_f105g_is_electronic_warfare_everywhere(self):
        for name in FILES:
            for r in rows_of(FILES[name][0]):
                if r["model"] == "F-105" and r["variant"] == "G":
                    assert r["role_type"] == "electronic_warfare", (
                        f"{name}: the F-105G is the Wild Weasel conversion")


    def test_q_designated_drones_are_aircraft_not_missiles(self):
        """The Q in AQM/BQM/OQ/MQM denotes an unmanned aircraft."""
        import re
        bad = []
        for name in FILES:
            for r in rows_of(FILES[name][0]):
                if re.match(r"^X?[ABMO]QM-", r["model"]) \
                        and r["aircraft_type"] != "fixed_wing":
                    bad.append(f"{name}: {r['model']} is {r['aircraft_type']}")
        assert not bad, bad


class TestReplicaHandling:
    """Pima's X-15s are a replica and a mockup; the real 56-6671 is at NMUSAF.

    Importing Pima's painted-on serial would claim an airframe it doesn't have
    AND collide with the museum that does.
    """

    def test_pima_x15s_carry_no_serial(self):
        rows = rows_of(FILES["pima_topup_n_to_z"][0])
        x15 = [r for r in rows if r["model"] == "X-15"]
        assert len(x15) == 2, f"expected Pima's two X-15s, found {len(x15)}"
        for r in x15:
            assert not r["tail_number"].strip(), (
                "Pima's X-15 is a replica/mockup — its painted serial must not "
                "be imported as a tail number")
            assert "replica" in r["description"].lower() \
                or "mockup" in r["description"].lower(), \
                "a replica should say so"

    def test_nmusaf_holds_the_real_x15a2(self):
        rows = rows_of(FILES["nmusaf_topup_m_to_z"][0])
        match = [r for r in rows
                 if r["model"] == "X-15" and r["tail_number"] == "56-6671"]
        assert len(match) == 1, "NMUSAF should hold X-15A-2 56-6671"

    def test_the_two_files_do_not_claim_the_same_airframe(self):
        pima = rows_of(FILES["pima_topup_n_to_z"][0])
        nmusaf = rows_of(FILES["nmusaf_topup_m_to_z"][0])

        def keyed(rows):
            return {(r["model"].strip().lower(), r["tail_number"].strip().lower())
                    for r in rows if r["tail_number"].strip()}

        overlap = keyed(pima) & keyed(nmusaf)
        assert not overlap, (
            f"the same (model, tail) appears at both museums: {overlap} — an "
            f"aircraft is in exactly one place")
