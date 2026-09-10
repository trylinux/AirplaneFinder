"""The uq_airframe identity key: full designation + tail number + operator country.

These pin down the reason the key changed. (model, tail_number) asserted that
a given model carries a given serial once on earth, which is false — serials
are national and short ones repeat. The importer's only way out was to blank
the tail number, and 99 of 1,072 Russian bort numbers were lost that way.

The cases below are the real ones that cost data, not invented examples:

    Mirage F1CZ  207  (SAAF)   vs  Mirage F1C-200  207  (Armée de l'Air)
    MiG-15       "03" (Aden)   vs  MiG-15UTI       "03" (Monino)
    F-86F        709  (Saudi)  vs  F-86F           709  (another air force)

The first two separate on designation alone. The third needs the operator.
"""

import json


def _import(client, rows, dry_run=False):
    r = client.post("/api/v1/aircraft/bulk_import", json={
        "format": "json", "data": json.dumps(rows), "dry_run": dry_run,
    })
    return r.status_code, r.get_json()


class TestVariantSeparatesNationalSerials:

    def test_same_model_different_variant_same_tail_both_import(self, admin_client, db_session):
        """Mirage F1CZ 207 and Mirage F1C-200 207 are two aircraft."""
        code, rep = _import(admin_client, [
            {"manufacturer": "Dassault", "model": "Mirage F1", "variant": "CZ",
             "tail_number": "207", "operator_country": "ZA"},
            {"manufacturer": "Dassault", "model": "Mirage F1", "variant": "C-200",
             "tail_number": "207", "operator_country": "FR"},
        ])
        assert code == 200, rep
        assert rep["errors"] == []
        assert rep["created"] == 2

    def test_trainer_variant_is_not_the_fighter(self, admin_client, db_session):
        """MiG-15 '03' at Aden and MiG-15UTI '03' at Monino."""
        code, rep = _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-15",
             "tail_number": "03", "operator_country": "YE"},
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-15", "variant": "UTI",
             "tail_number": "03", "operator_country": "RU"},
        ])
        assert code == 200, rep
        assert rep["created"] == 2

    def test_identical_designation_and_tail_still_collides(self, admin_client, db_session):
        """The constraint has to still do its job. Same everything is a dupe."""
        code, rep = _import(admin_client, [
            {"manufacturer": "North American", "model": "F-86", "variant": "F",
             "tail_number": "709", "operator_country": "SA"},
            {"manufacturer": "North American", "model": "F-86", "variant": "F",
             "tail_number": "709", "operator_country": "SA"},
        ])
        assert rep["created"] == 0
        assert any("duplicate of an earlier row" in e["message"] for e in rep["errors"])


class TestOperatorCountrySeparatesIdenticalDesignations:

    def test_same_designation_and_tail_under_two_operators(self, admin_client, db_session):
        """Saudi F-86F 709 is not another air force's F-86F 709. This is the
        case that needs the country — the designations are identical."""
        code, rep = _import(admin_client, [
            {"manufacturer": "North American", "model": "F-86", "variant": "F",
             "tail_number": "709", "operator_country": "SA"},
            {"manufacturer": "North American", "model": "F-86", "variant": "F",
             "tail_number": "709", "operator_country": "PK"},
        ])
        assert code == 200, rep
        assert rep["created"] == 2

    def test_unknown_operator_does_not_match_a_known_one(self, admin_client, db_session):
        """NULL means unknown, and matching unknown to known would be a guess.
        Strict matching also keeps this check in agreement with what MySQL
        does on insert, which is the point."""
        code, rep = _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-21", "variant": "bis",
             "tail_number": "07"},
        ])
        assert code == 200, rep
        code, rep = _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-21", "variant": "bis",
             "tail_number": "07", "operator_country": "RU"},
        ])
        assert code == 200, rep
        assert rep["created"] == 1

    def test_that_case_is_reported_as_a_warning(self, admin_client, db_session):
        """...but it is exactly the shape of a re-import of a region loaded
        before the operator was recorded, so it must not pass silently."""
        _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-21", "variant": "bis",
             "tail_number": "07"},
        ])
        code, rep = _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-21", "variant": "bis",
             "tail_number": "07", "operator_country": "RU"},
        ])
        assert len(rep["warnings"]) == 1
        assert "same designation and tail number" in rep["warnings"][0]["message"]

    def test_a_warning_never_blocks_an_import(self, admin_client, db_session):
        import models
        _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-21", "variant": "bis",
             "tail_number": "07"},
        ])
        _import(admin_client, [
            {"manufacturer": "Mikoyan-Gurevich", "model": "MiG-21", "variant": "bis",
             "tail_number": "07", "operator_country": "RU"},
        ])
        assert models.Aircraft.query.filter_by(tail_number="07").count() == 2


class TestOperatorCountryValidation:

    def test_lowercase_is_accepted_and_normalized(self, admin_client, db_session):
        import models
        code, rep = _import(admin_client, [
            {"manufacturer": "Saab", "model": "J 35", "variant": "F",
             "tail_number": "35556", "operator_country": "se"},
        ])
        assert code == 200, rep
        assert models.Aircraft.query.filter_by(tail_number="35556").one().operator_country == "SE"

    def test_a_country_name_is_rejected(self, admin_client, db_session):
        """Free text is what made museums.country useless as a key component."""
        code, rep = _import(admin_client, [
            {"manufacturer": "Saab", "model": "J 35", "tail_number": "35557",
             "operator_country": "Sweden"},
        ])
        assert rep["created"] == 0
        assert any(e["field"] == "operator_country" for e in rep["errors"])

    def test_three_letter_code_is_rejected(self, admin_client, db_session):
        code, rep = _import(admin_client, [
            {"manufacturer": "Saab", "model": "J 35", "tail_number": "35558",
             "operator_country": "SWE"},
        ])
        assert rep["created"] == 0
        assert any(e["field"] == "operator_country" for e in rep["errors"])

    def test_blank_is_fine_and_means_unknown(self, admin_client, db_session):
        code, rep = _import(admin_client, [
            {"manufacturer": "Saab", "model": "J 35", "tail_number": "35559",
             "operator_country": ""},
        ])
        assert code == 200, rep
        assert rep["created"] == 1


class TestConstructionNumber:

    def test_it_round_trips(self, admin_client, db_session):
        import models
        code, rep = _import(admin_client, [
            {"manufacturer": "Aérospatiale", "model": "SA.330", "variant": "C",
             "tail_number": "TU-VAP", "construction_number": "1044",
             "operator_country": "CI"},
        ])
        assert code == 200, rep
        ac = models.Aircraft.query.filter_by(tail_number="TU-VAP").one()
        assert ac.construction_number == "1044"

    def test_same_cn_is_the_same_airframe_even_under_a_new_registration(
            self, admin_client, db_session):
        """A c/n identifies one airframe for life. An airframe that changed
        hands changed registration, and that is precisely when a tail-based
        check misses the duplicate — Sea Heron XR443 is VH-NJP is c/n 14072."""
        code, rep = _import(admin_client, [
            {"manufacturer": "de Havilland", "model": "Sea Heron", "tail_number": "XR443",
             "construction_number": "14072", "operator_country": "GB"},
        ])
        assert code == 200, rep
        code, rep = _import(admin_client, [
            {"manufacturer": "de Havilland", "model": "Sea Heron", "tail_number": "VH-NJP",
             "construction_number": "14072", "operator_country": "AU"},
        ])
        assert rep["created"] == 0, rep
        assert any("already exists" in e["message"] for e in rep["errors"])

    def test_the_same_cn_under_a_different_manufacturer_is_not_a_match(
            self, admin_client, db_session):
        """c/n 1044 is a Puma and also, somewhere, a Cessna. Scoping by
        manufacturer is what makes the signal usable at all."""
        code, rep = _import(admin_client, [
            {"manufacturer": "Aérospatiale", "model": "SA.330", "tail_number": "TU-VAQ",
             "construction_number": "1044"},
            {"manufacturer": "Cessna", "model": "172", "tail_number": "N1044X",
             "construction_number": "1044"},
        ])
        assert code == 200, rep
        assert rep["created"] == 2


class TestSingleRecordEndpoints:

    def test_post_rejects_a_true_duplicate(self, admin_client, db_session):
        payload = {"manufacturer": "Northrop", "model": "F-5", "variant": "E",
                   "tail_number": "01532", "operator_country": "IR"}
        assert admin_client.post("/api/v1/aircraft", json=payload).status_code == 201
        r = admin_client.post("/api/v1/aircraft", json=payload)
        assert r.status_code == 409

    def test_post_allows_the_same_serial_under_another_operator(self, admin_client, db_session):
        assert admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01532", "operator_country": "IR"}).status_code == 201
        assert admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01532", "operator_country": "TR"}).status_code == 201

    def test_patch_onto_an_occupied_key_is_refused(self, admin_client, db_session):
        a = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01532", "operator_country": "IR"}).get_json()
        b = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01533", "operator_country": "IR"}).get_json()
        r = admin_client.patch(f"/api/v1/aircraft/{b['id']}", json={"tail_number": "01532"})
        assert r.status_code == 409
        assert r.get_json()["existing_id"] == a["id"]

    def test_patching_the_operator_frees_the_key(self, admin_client, db_session):
        """Backfilling operator_country is exactly this operation, thousands
        of times over, so it had better work."""
        admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01532", "operator_country": "IR"})
        b = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01533", "operator_country": "IR"}).get_json()
        r = admin_client.patch(f"/api/v1/aircraft/{b['id']}",
                               json={"operator_country": "TR", "tail_number": "01532"})
        assert r.status_code == 200, r.get_json()

    def test_operator_country_is_exposed_by_the_api(self, admin_client, db_session):
        created = admin_client.post("/api/v1/aircraft", json={
            "manufacturer": "Northrop", "model": "F-5", "variant": "E",
            "tail_number": "01534", "operator_country": "IR",
            "construction_number": "V.1034"}).get_json()
        got = admin_client.get(f"/api/v1/aircraft/{created['id']}").get_json()["aircraft"]
        assert got["operator_country"] == "IR"
        assert got["construction_number"] == "V.1034"
