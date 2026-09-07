#!/usr/bin/env python3
r"""Extract Pima Air & Space Museum's collection from its own WordPress feed.

WHY A FEED AND NOT A SCRAPE
---------------------------
Pima publishes every airframe at /wp-json/wp/v2/museum_aircraft. Scraping the
rendered pages yielded serials for roughly 44% of the collection; the feed
carries the museum's own Manufacturer / Designation / Registration / Serial
Number fields and takes coverage past 90%. Per data/METHODOLOGY.md a feed from
the museum itself is rung 1 and a scrape is rung 2, so this is Pima's source
of record.

WHAT WE PARSE, AND WHAT WE DELIBERATELY IGNORE
----------------------------------------------
`content.rendered` holds two things back to back:

1. the rendered HTML a visitor actually sees, where each field is
   `<span><strong>Serial Number</strong></span><br />42-54654`
2. a YOOtheme page-builder JSON blob inside an HTML comment, which is the
   *template* — including fields carrying `"status":"disabled"` that the
   museum has chosen not to show.

We read only (1) and cut the content at the builder comment. Two reasons.
The blob is JSON embedded in HTML embedded in JSON, and regexing it leaked
escape artifacts into the data ("56-6671\, P51D \"Bad Angel\"). More
importantly, a disabled field is one the museum has decided not to stand
behind — reading only the visible HTML honours that for free, and
METHODOLOGY.md holds that a blank field beats a value we can't source.

`acf` is not an option: the REST endpoint exposes it as [].

LINE STRUCTURE
--------------
Block-level tags (<p>, <br>, <div>...) end a line; inline tags (<span>,
<sup>, <strong>...) must not, or "45<sup>th</sup> Squadron" splits into three
lines and 'th' reads as a field label. Every known label also terminates the
preceding value, otherwise an F-105D's serial reads
"61-0086 Designation F-105D Big Sal".

Usage:
    python3 scripts/parse_pima_feed.py --raw /tmp/pima_all.json --letters N-Z
    python3 scripts/parse_pima_feed.py --raw /tmp/pima_all.json --out /tmp/pima.jsonl
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

NBSP = " "

# Every label the museum uses. All act as value terminators, including the
# ones we don't keep, so a value can never run on into the next field.
LABELS = {
    "manufacturer": "manufacturer",
    "designation": "designation",
    "registration": "registration",
    "serial number": "serial",
    "serial no.": "serial",
    "serial": "serial",
    "markings": "markings",
    "service history": None,
    "crew": None, "engines": None, "engine": None, "weight": None,
    "length": None, "height": None, "wingspan": None, "range": None,
    "max. speed": None, "service ceiling": None,
}

# "We don't know", spelled several ways. Treated as blank.
NULLISH = {"unknown", "none", "n/a", "na", "-", "--", "tbd", "unk", "not known"}

BLOCK_TAG = re.compile(
    r"</?(?:p|div|br|hr|h[1-6]|li|ul|ol|tr|td|th|table|section|article)\b[^>]*>",
    re.I,
)
ANY_TAG = re.compile(r"<[^>]+>")

# Nicknames the museum appends to the designation: P-47D "Frankie".
NICKNAME = re.compile(r"[\"“‘']([^\"”’']{2,40})[\"”’']")

# Pima states current visibility in a fixed sentence directly under the title.
# This is exactly our visitor-perspective display_status, from the museum's own
# mouth, so it beats assuming everything is on display.
#
# It must be anchored to "This aircraft is ...". The service-history prose
# further down is full of lines like "January 1983 In storage Corpus Christi
# Aviation Depot" and "placed in storage at Davis-Monthan AFB in 2005", which
# describe where an airframe sat decades ago, not where it is now. Matching
# a bare "in storage" would mark a dozen aircraft on the floor as invisible.
STATUS_SENTENCE = re.compile(
    r"This aircraft is (?:currently )?(?P<state>"
    r"not currently on public display|not on public display|"
    r"undergoing restoration|being restored|in storage)", re.I)

STATUS_MAP = {
    "not currently on public display": "in_storage",
    "not on public display": "in_storage",
    "in storage": "in_storage",
    "undergoing restoration": "under_restoration",
    "being restored": "under_restoration",
}

# Multi-word manufacturers, longest first, for the title-split fallback only.
MULTIWORD = sorted([
    "Naval Aircraft Factory", "General Dynamics", "North American",
    "McDonnell Douglas", "De Havilland", "Lockheed Martin", "Rotary Air Force",
    "Pacific Airwave", "PZL Mielec", "Focke Wulf", "Focke-Wulf",
    "Curtiss Wright", "Consolidated Vultee", "Fairchild Republic",
    "Fairchild Hiller", "Rockwell International", "British Aerospace",
    "Hawker Siddeley", "Scaled Composites", "Sud Aviation", "Nord Aviation",
    "Dassault-Breguet/Dornier", "Dassault-Breguet", "Boeing Vertol",
    "Mikoyan Gurevich", "Mikoyan-Gurevich", "Northrop Grumman",
    "Short Brothers", "Bell Boeing", "Martin Marietta", "Piasecki Helicopter",
], key=lambda s: -len(s.split()))


def clean(s: str) -> str:
    s = html.unescape(s or "")
    s = s.replace(NBSP, " ")
    s = BLOCK_TAG.sub("\n", s)
    s = ANY_TAG.sub("", s)
    s = re.sub(r"[ \t]+", " ", s)
    return "\n".join(l.strip() for l in s.split("\n")).strip()


def visible_html(content: str) -> str:
    """Everything before the page-builder comment — i.e. what a visitor sees."""
    cut = content.find('<!-- {"name"')
    if cut == -1:
        cut = content.find('{"type":"layout"')
    return content if cut == -1 else content[:cut]


def nullish(v: str) -> str:
    return "" if v.strip().lower().strip("\"'“”") in NULLISH else v.strip()


def main_fields(text: str) -> dict:
    """Each field's value is the ONE line following its label.

    The museum renders every field as `<strong>Serial Number</strong><br />
    42-54654`, so after block tags become newlines the value is always the
    next line. An earlier version joined lines until it hit another known
    label, which is only correct when every field is labelled — and it isn't.
    Service-history prose sits unlabelled below the serial on many records, so
    joining swallowed it: the B-25J's serial came out as "43-27712 Jul 1946
    170th AAF Base Unit, Brooks AAF..." (5,000+ characters). Take one line.
    """
    out = {"manufacturer": "", "designation": "", "registration": "",
           "serial": "", "markings": ""}
    lines = [l for l in text.split("\n") if l]
    for i, line in enumerate(lines):
        label = line.lower().rstrip(":").strip()
        if label not in LABELS:
            continue
        key = LABELS[label]
        if not key or out[key] or i + 1 >= len(lines):
            continue
        value = lines[i + 1].strip()
        # A "value" that is itself a label means the field was left empty.
        if value.lower().rstrip(":").strip() in LABELS:
            continue
        out[key] = value
    return out


def split_title(title: str):
    """Fallback for records with no Manufacturer field: split the title.

    Seven of Pima's records (the ones rebuilt in 2026) publish only Markings
    and Serial Number, so manufacturer and designation have to come from the
    title. Longest match wins so "Naval Aircraft Factory N3N-3" doesn't become
    manufacturer="Naval".
    """
    t = " ".join(title.split())
    low = t.lower()
    for mw in MULTIWORD:
        if low.startswith(mw.lower() + " "):
            return mw, t[len(mw):].strip()
    parts = t.split(" ", 1)
    return (parts[0], parts[1].strip()) if len(parts) == 2 else (t, "")


def parse_record(rec: dict) -> dict:
    text = clean(visible_html(rec["content"]["rendered"]))
    out = {"id": rec["id"], "title": clean(rec["title"]["rendered"]),
           "link": rec.get("link", "")}
    out.update(main_fields(text))

    # Records with no Manufacturer field fall back to splitting the title.
    if not out["manufacturer"]:
        man, des = split_title(out["title"])
        out["manufacturer"] = man
        out["designation"] = out["designation"] or des
        out["from_title"] = True

    sm = STATUS_SENTENCE.search(text)
    out["display_status"] = (
        STATUS_MAP.get(sm.group("state").lower(), "on_display")
        if sm else "on_display")
    out["offsite"] = bool(sm and "offsite" in text[sm.end():sm.end() + 20].lower())

    # A serial the museum wraps in quotation marks is a painted-on marking,
    # not the airframe's identity. All three at Pima are replicas or mockups:
    # the X-15A "56-6670" and X-15A-2 "56-6671" are a replica and a
    # construction mockup, and the real 56-6671 is at the National Museum of
    # the USAF. Importing the quoted serial as a tail number would both claim
    # a famous airframe Pima does not have and collide with the museum that
    # does, under the unique index on (model, tail_number).
    raw_serial = (out["serial"] or "").strip()
    out["serial_is_marking"] = bool(raw_serial and raw_serial[0] in "\"“'‘")
    out["is_replica"] = bool(re.search(
        r"\b(replica|mockup|mock-up|reproduction)\b",
        f"{out['title']} {text[:400]}", re.I))

    out["serial"] = nullish(out["serial"]).strip("\"“”'‘’")
    out["registration"] = nullish(out["registration"])
    out["markings"] = nullish(out["markings"])

    # A nickname in the designation belongs in aircraft_name, not in the
    # designation the unique index is built on.
    out["nickname"] = ""
    nm = NICKNAME.search(out["designation"])
    if nm:
        out["nickname"] = nm.group(1).strip()
        out["designation"] = NICKNAME.sub("", out["designation"]).strip()
    out["designation"] = re.sub(r"\s+", " ", out["designation"]).strip(" -,")

    # Some airframes list every registration they have worn:
    # "CCCP-32682, N75AN, HR-ARR". First is current, the rest are aliases.
    regs = [r.strip() for r in out["registration"].split(",") if r.strip()]
    out["registration"] = regs[0] if regs else ""
    out["other_registrations"] = regs[1:]

    # Likewise a record that lists two serials is covering two airframes, or
    # is uncertain which it is. Flag rather than guess.
    out["serial_ambiguous"] = bool(
        re.search(r"\b(and|or)\b|,", out["serial"], re.I))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", required=True)
    p.add_argument("--out", default=None)
    p.add_argument("--letters", default=None,
                   help="restrict to manufacturer initials in this range, e.g. N-Z")
    args = p.parse_args()

    parsed = [parse_record(r) for r in json.load(open(args.raw, encoding="utf-8"))]

    missing = [r for r in parsed if not r["manufacturer"]]
    if missing:
        print(f"note: {len(missing)} of {len(parsed)} records have no "
              f"Manufacturer field:", file=sys.stderr)
        for r in missing:
            print(f"      #{r['id']} {r['title']}", file=sys.stderr)

    if args.letters:
        lo, hi = args.letters.upper().split("-")
        parsed = [r for r in parsed
                  if lo <= (r["manufacturer"] or r["title"])[:1].upper() <= hi]

    parsed.sort(key=lambda r: (r["manufacturer"].lower(), r["designation"].lower()))

    got = sum(1 for r in parsed if r["registration"] or r["serial"])
    print(f"{len(parsed)} records; {got} with a registration or serial "
          f"({got * 100 // max(len(parsed), 1)}%)", file=sys.stderr)
    amb = [r for r in parsed if r["serial_ambiguous"]]
    if amb:
        print(f"{len(amb)} records list more than one serial — needs a human:",
              file=sys.stderr)
        for r in amb:
            print(f"      {r['title']}: {r['serial']}", file=sys.stderr)

    if args.out:
        with Path(args.out).open("w", encoding="utf-8") as f:
            for r in parsed:
                f.write(json.dumps(r) + "\n")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        for r in parsed:
            print(f"{r['manufacturer']:26} | {r['designation']:24} | "
                  f"{r['registration']:14} | {r['serial']:16} | {r['nickname']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
