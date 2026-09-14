# -*- coding: utf-8 -*-
"""Hand-encoded outcome of the 46 airframe-conflict adjudications.

PATCH = non-destructive. Moves an identity onto the record that actually holds
the airframe, blanks an identity wrongly applied, or corrects a type. These run
first, so the surviving record carries the good data before any delete.

DELETE = destructive, listed for scripts/delete_conflicts_sep2026.sh.
"""

# id -> fields to set. "" clears a field.
PATCH = {
    # --- identity moved onto the site that actually has the airframe ---
    25670: {"tail_number": "66-15307", "construction_number": "20063"},   # AH-1F, Weirton WV
    27122: {"tail_number": "70-15956", "construction_number": "20900"},
    26280: {"tail_number": "67-0438", "construction_number": "2828"},     # RF-4C
    27102: {"construction_number": "580-7225"},                          # T-33A
    26801: {"tail_number": "158479", "construction_number": "14284"},    # TA-4J, Gladstone MI
    26769: {"tail_number": "152603", "construction_number": "I-151"},    # A-6E, Richmond IN
    27188: {"tail_number": "67-15546", "construction_number": "20210"},  # AH-1S, Chamberlain SD
    27187: {"tail_number": "53-6100"},                                   # T-33A, Chamberlain SD
    27125: {"tail_number": "63-8701", "construction_number": "0926"},    # UH-1B, Long Prairie MN
    29543: {"tail_number": "35-5870", "construction_number": "JT-66"},   # T-1B, Gyoda
    6927:  {"tail_number": "44-77109", "construction_number": "16693",
            "aircraft_name": "Texas Zephyr"},                            # C-47B, Burnet TX

    # --- identity wrongly applied: keep the record, clear what isn't its own ---
    27109: {"tail_number": "", "construction_number": ""},
    27164: {"tail_number": "", "construction_number": ""},               # Ryan IA Cobra: real, identity not
    26246: {"tail_number": "", "construction_number": ""},
    11535: {"construction_number": ""},                                  # C-113 Santa Romana
    23210: {"construction_number": ""},                                  # Bell 204 c/n 1090
    37273: {"construction_number": ""},                                  # Medyn Su-24
    11524: {"construction_number": ""},                                  # S-2, painted as 2-AS-24
    11530: {"tail_number": "", "construction_number": ""},               # UH-1H Santa Romana
    12716: {"construction_number": ""},                                  # MiG-27 duplicate works no.

    # --- type corrections found during adjudication ---
    34192: {"manufacturer": "Ilyushin", "model": "Il-103", "variant": "",
            "tail_number": "RA-10300", "construction_number": ""},       # was filed as an Il-86
    25705: {"manufacturer": "Grumman", "model": "G-1159", "variant": "",
            "model_name": "Gulfstream II"},                              # was filed as a G-63
    24421: {"model": "F-84", "variant": "B", "tail_number": "46-600"},   # Hancock Field: F-84B, not F-84F
    26668: {"construction_number": "382-3826"},                          # C-130E 62-1862
    # Kisarazu really has 35-5867; c/n JT-66 belongs to 35-5870 at Gyoda
    29007: {"tail_number": "35-5867", "construction_number": ""},
}

# The airframe is not at this site. Ordered so the reason is auditable.
DELETE = [
    (26718, "TA-4J 158479 is at Gladstone MI (26801); Oglesby holds only a UH-1H"),
    (26698, "TA-4J 158479 is at Gladstone MI (26801); Dixon holds an F-105D and an AH-1G"),
    (26716, "A-6E 152603 moved to Richmond IN (26769) on 10 Apr 2022"),
    (26696, "A-6E 152603 is at Richmond IN (26769)"),
    (25622, "AH-1F 66-15307 is at Weirton WV (25670); AV fix 40.390672 -80.594217"),
    (25621, "A-7D 69-6241 is at Weirton WV (25669); same AV fix embedded in its own text"),
    (27318, "C-47A 43-15200 c/n 19666 is at the site kept as 24868"),
    (27174, "GF-4C 63-7417 c/n 0349 is at the site kept as 27167"),
    (26251, "RF-4C 67-0438 is at the site kept as 26280"),
    (10656, "T-33A 52-9171 is at the site kept as 27102"),
    (25678, "UH-1H 66-16109 c/n 5803 is at the site kept as 25671"),
    (26244, "AH-1F 67-15642 is at Collegedale (26189); D'Iberville holds no aircraft"),
    (26249, "UH-1H 68-16450 is at Jeffersontown (26234); D'Iberville holds no aircraft"),
    (26248, "A-4M 158430 is at Sequatchie County (26200); D'Iberville holds no aircraft"),
    (26247, "T-33A 53-6132 is at Dunlap (26199); D'Iberville holds no aircraft"),
    (26245, "TA-4J 159795 is at Collegedale (26190); D'Iberville holds no aircraft"),
    (6947,  "C-47B 43-49942 burned out on takeoff at Burnet 21 Jul 2018 - a write-off, not a preserved airframe"),
    (27163, "T-33A 53-6100 is at Chamberlain SD (27187)"),
    (27161, "UH-1H 65-9667 c/n 4711 is at Sleepy Eye MN (27132)"),
    (27110, "UH-1B 63-8701 is at Long Prairie MN (27125)"),
    (26815, "AH-1F 67-15805 c/n 20469 is at the site kept as 26795"),
    (26713, "F-105D 60-0455 c/n D143 is at the site kept as 26694"),
    (26794, "UH-1H 67-17562 c/n 9760 is at the site kept as 26768"),
    (26814, "UH-1H 67-17562: Mount Clemens Post 4 displays F-101B 57-0430, not a Huey "
            "- LOW CONFIDENCE, the Orland Post 423 placement is unconfirmed"),
]
