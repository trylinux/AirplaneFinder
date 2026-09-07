"""scripts/parse_pima_feed.py — reading Pima's own WordPress feed.

Every test here encodes a mistake the parser made against the real feed
before it was fixed. The feed is the source of record for 366 airframes, so a
parsing bug is a data bug across a third of the largest collection in the file.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import parse_pima_feed as P  # noqa: E402


def rec(title, html):
    return {"id": 1, "title": {"rendered": title},
            "content": {"rendered": html}, "link": "https://pimaair.org/x/"}


FIELD_HTML = (
    '<div><p><span><strong>Manufacturer</strong></span><br />North American</p></div>'
    '<div><p><span><strong>Designation</strong></span><br />F-100C</p></div>'
    '<div><p><span><strong>Serial Number</strong></span><br />54-1823</p></div>'
)


class TestFieldExtraction:

    def test_reads_the_museums_own_fields(self):
        r = P.parse_record(rec("North American F-100C", FIELD_HTML))
        assert r["manufacturer"] == "North American"
        assert r["designation"] == "F-100C"
        assert r["serial"] == "54-1823"

    def test_inline_tags_do_not_split_a_line(self):
        """`45<sup>th</sup> Squadron` must not become three lines — 'th' would
        then look like a field label."""
        html = ('<div><p><span><strong>Markings</strong></span><br />'
                '45<sup>th</sup> Fighter Squadron, Italy</p></div>')
        r = P.parse_record(rec("X", html))
        assert r["markings"] == "45th Fighter Squadron, Italy"

    def test_a_value_is_one_line_not_everything_up_to_the_next_label(self):
        """Service-history prose sits unlabelled below the serial on many
        records. Joining until the next label swallowed 5,000 characters of it
        into the B-25J's serial."""
        html = (
            '<div><p><span><strong>Serial Number</strong></span><br />43-27712</p>'
            '<p>Jul 1946 170th AAF Base Unit, Brooks AAF, San Antonio, Texas.</p>'
            '<p>Feb 1947 Converted to TB-25J.</p></div>'
        )
        r = P.parse_record(rec("North American B-25J", html))
        assert r["serial"] == "43-27712"

    def test_an_empty_field_does_not_absorb_the_next_label(self):
        html = ('<div><p><strong>Registration</strong></p>'
                '<p><strong>Serial Number</strong><br />12345</p></div>')
        r = P.parse_record(rec("X", html))
        assert r["registration"] == ""
        assert r["serial"] == "12345"


class TestBuilderBlobIsIgnored:

    def test_only_the_visible_html_is_read(self):
        """The YOOtheme page-builder blob is a template, not content. Regexing
        it leaked escape artifacts (`56-6671\\`, `P51D \\"Bad Angel\\"`) into
        the data, and it contains fields the museum has disabled."""
        html = FIELD_HTML + (
            '<p><!-- {"type":"layout","children":[{"type":"text","props":'
            '{"content":"Serial Number\\nSHOULD-NOT-APPEAR","status":"disabled"}}]} -->')
        r = P.parse_record(rec("North American F-100C", html))
        assert r["serial"] == "54-1823"
        assert "SHOULD-NOT-APPEAR" not in str(r)

    def test_visible_html_cut_handles_both_blob_markers(self):
        for marker in ('<!-- {"name":"Aircraft Layout"', '{"type":"layout"'):
            assert P.visible_html("VISIBLE" + marker + "junk") == "VISIBLE"


class TestReplicaDetection:
    """Pima's X-15A-2 is a construction mockup; the real 56-6671 is at the
    National Museum of the USAF. Importing the painted serial would claim an
    airframe Pima doesn't have and collide with the museum that does."""

    def test_a_quoted_serial_is_flagged_as_a_marking(self):
        html = ('<div><p><strong>Designation</strong><br />X-15A</p>'
                '<p><strong>Serial Number</strong><br />“56-6670”</p></div>')
        r = P.parse_record(rec("North American X-15A Replica", html))
        assert r["serial_is_marking"] is True
        assert r["serial"] == "56-6670", "quotes stripped, value kept for aliases"

    def test_an_unquoted_serial_is_not_flagged(self):
        r = P.parse_record(rec("North American F-100C", FIELD_HTML))
        assert r["serial_is_marking"] is False

    @pytest.mark.parametrize("title", [
        "North American X-15A Replica",
        "North American X-15A-2 Mockup",
        "Sopwith Camel Reproduction",
    ])
    def test_replica_wording_is_detected(self, title):
        assert P.parse_record(rec(title, FIELD_HTML))["is_replica"] is True

    def test_a_normal_record_is_not_a_replica(self):
        assert P.parse_record(rec("North American F-100C",
                                  FIELD_HTML))["is_replica"] is False


class TestDisplayStatus:

    @pytest.mark.parametrize("sentence,expected", [
        ("This aircraft is not currently on public display.", "in_storage"),
        ("This aircraft is currently undergoing restoration offsite.",
         "under_restoration"),
    ])
    def test_the_museums_own_status_sentence_is_read(self, sentence, expected):
        r = P.parse_record(rec("X", f"<p>{sentence}</p>" + FIELD_HTML))
        assert r["display_status"] == expected

    def test_service_history_prose_is_not_mistaken_for_current_status(self):
        """"January 1983 In storage Corpus Christi Aviation Depot" describes
        where an airframe sat decades ago. Matching a bare "in storage" marked
        a dozen aircraft standing on the floor as invisible."""
        html = ('<p>January 1983 In storage Corpus Christi Aviation Depot.</p>'
                '<p>The aircraft was placed in storage at Davis-Monthan in 2005.</p>'
                + FIELD_HTML)
        assert P.parse_record(rec("X", html))["display_status"] == "on_display"

    def test_default_is_on_display(self):
        assert P.parse_record(rec("X", FIELD_HTML))["display_status"] == "on_display"


class TestValueCleaning:

    @pytest.mark.parametrize("raw", ["UNKNOWN", "Unknown", "None", "n/a", "-"])
    def test_placeholder_serials_become_blank(self, raw):
        html = f'<div><p><strong>Serial Number</strong><br />{raw}</p></div>'
        assert P.parse_record(rec("X", html))["serial"] == ""

    def test_multiple_registrations_split_into_current_plus_aliases(self):
        html = ('<div><p><strong>Registration</strong><br />'
                'CCCP-32682, N75AN, HR-ARR</p></div>')
        r = P.parse_record(rec("X", html))
        assert r["registration"] == "CCCP-32682"
        assert r["other_registrations"] == ["N75AN", "HR-ARR"]

    def test_two_serials_are_flagged_rather_than_picked_between(self):
        """A record listing two serials covers two airframes, or the museum is
        unsure which this is. Either way, guessing is wrong."""
        html = ('<div><p><strong>Serial Number</strong><br />'
                '59-2866 AND 60-2092</p></div>')
        assert P.parse_record(rec("X", html))["serial_ambiguous"] is True

    def test_a_nickname_is_lifted_out_of_the_designation(self):
        """`F-105D "Big Sal"` — the nickname must not end up in the designation
        the unique index is built on."""
        html = ('<div><p><strong>Designation</strong><br />'
                'F-105D “Big Sal”</p></div>')
        r = P.parse_record(rec("Republic F-105D", html))
        assert r["designation"] == "F-105D"
        assert r["nickname"] == "Big Sal"


class TestTitleFallback:
    """Seven records publish no Manufacturer field at all."""

    def test_falls_back_to_splitting_the_title(self):
        r = P.parse_record(rec("Shorts C-23B+ Sherpa", "<p>No fields here.</p>"))
        assert r["manufacturer"] == "Shorts"
        assert r["designation"] == "C-23B+ Sherpa"

    def test_multiword_manufacturers_are_not_split_at_the_first_space(self):
        r = P.parse_record(rec("Naval Aircraft Factory N3N-3", "<p>x</p>"))
        assert r["manufacturer"] == "Naval Aircraft Factory"
        assert r["designation"] == "N3N-3"
