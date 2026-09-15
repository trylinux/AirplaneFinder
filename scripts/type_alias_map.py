#!/usr/bin/env python3
"""The curated alias map: alternate designations -> an existing type.

Every entry here asserts one thing — *these are the same aeroplane, written
down under a different name* — and that assertion is the entire safety
argument for the feature. An alias is cheap to add and invisible when
wrong: the reader sees a confident write-up on a page it does not belong
to, with nothing marking it as a guess. So the bar for this file is not
"plausibly related" but "the same airframe, redesignated".

What that bar excludes, deliberately, is listed in JUDGEMENT below. Those
are real relationships — derivative, navalised, licence-built-with-changes
— that are close enough to tempt and different enough to be wrong. They
want their own write-up, not someone else's.

Target is given as (designation, manufacturer_scope) because the target
must be identified the same way uq_type_match identifies it.
"""

# (alias designation, alias manufacturer_scope, target designation, target scope, why)
CONFIRMED = [
    # ── Pre-1962 US designations. The 1962 Tri-Service system renamed
    # aircraft already in service; the airframes did not change. ──
    ("AT-6",   "", "T-6",   "North American", "USAAF advanced trainer designation for the Texan"),
    ("SNJ",    "", "T-6",   "North American", "US Navy designation for the Texan"),
    ("BC-1",   "", "T-6",   "North American", "the Texan's first USAAC designation"),
    ("A4D",    "", "A-4",   "", "the Skyhawk's pre-1962 Navy designation"),
    ("S2F",    "", "S-2",   "Grumman", "the Tracker's pre-1962 Navy designation"),
    ("L-19",   "", "O-1",   "", "the Bird Dog was L-19 until the 1962 renaming"),
    ("PBJ",    "", "B-25",  "", "US Marine Corps designation for the Mitchell"),
    ("L-4",    "Piper", "J-3", "", "the militarised Piper Cub. Scoped because L-4 is a generic\n     # enough string that a future import could mean something else"),
    ("RT-33",  "", "T-33",  "", "reconnaissance Shooting Star"),
    ("AT-33",  "", "T-33",  "", "armed-trainer Shooting Star"),

    # ── Reconnaissance and drone conversions of a type already written. ──
    ("RF-4",   "", "F-4",   "", "the unarmed reconnaissance Phantom"),
    ("QF-4",   "", "F-4",   "", "Phantoms converted to target drones"),
    ("RF-84",  "", "F-84",  "", "the Thunderflash, the recon F-84F airframe"),
    ("RF-104", "", "F-104", "", "reconnaissance Starfighter"),
    ("RF-5",   "", "F-5",   "", "reconnaissance F-5"),

    # ── Licence production and export designations of one airframe. ──
    ("CF-104", "", "F-104", "", "Canadair-built F-104G"),
    ("TF-104", "", "F-104", "", "the two-seat Starfighter"),
    ("CL-13",  "", "F-86",  "", "Canadair's own number for the Sabre it built"),
    ("CA-27",  "", "F-86",  "", "Commonwealth Aircraft's Avon Sabre"),
    ("CF-5",   "", "F-5",   "", "Canadair-built F-5"),
    ("NF-5",   "", "F-5",   "", "Dutch F-5 designation"),
    ("SF-5",   "", "F-5",   "", "CASA-built F-5 for Spain"),
    # The Czechoslovak S-10x numbers are scoped to Aero for the same reason
    # the Bell numbers are: "S-104" is a short, generic-looking string, and a
    # wrong match here would be silent.
    ("Lim-1",  "", "MiG-15", "", "PZL Mielec licence-built MiG-15"),
    ("Lim-2",  "", "MiG-15", "", "PZL Mielec licence-built MiG-15bis"),
    ("SB Lim-1", "", "MiG-15", "", "Polish two-seat MiG-15UTI"),
    ("SB Lim-2", "", "MiG-15", "", "Polish two-seat MiG-15UTI"),
    ("S-102",  "Aero", "MiG-15", "", "Czechoslovak licence-built MiG-15"),
    ("S-103",  "Aero", "MiG-15", "", "Czechoslovak licence-built MiG-15bis"),
    ("Lim-5",  "", "MiG-17", "", "PZL Mielec licence-built MiG-17F"),
    ("Lim-6",  "", "MiG-17", "", "Polish ground-attack development of the Lim-5"),
    ("S-104",  "Aero", "MiG-17", "", "Czechoslovak licence-built MiG-17"),
    ("J-5",    "Shenyang", "MiG-17", "", "Shenyang licence-built MiG-17"),
    ("S-105",  "Aero", "MiG-19", "", "Czechoslovak licence-built MiG-19"),
    ("S-106",  "Aero", "MiG-21", "", "Czechoslovak licence-built MiG-21F-13"),
    ("J-6",    "Shenyang", "MiG-19", "", "Shenyang licence-built MiG-19"),
    ("J-7",    "Chengdu",  "MiG-21", "", "Chengdu licence-built MiG-21F-13"),
    ("F-7",    "Chengdu",  "MiG-21", "", "the J-7's export designation"),
    ("Z-5",    "Harbin",   "Mi-4",   "", "Harbin licence-built Mi-4"),
    ("Ajeet",  "", "Gnat",  "", "HAL's developed Gnat for India"),
    ("Impala", "", "MB-326", "", "Atlas-built MB-326 for South Africa"),
    ("Dakota", "Douglas", "C-47", "", "the RAF's name for the C-47. Scoped: Piper also sells a\n     # PA-28 Dakota, and nothing in a bare model string separates them"),
    ("R4D",    "", "C-47",  "", "US Navy designation for the C-47"),

    # ── Export designations: same helicopter, different customer. ──
    ("Mi-17",  "", "Mi-8",  "", "export designation of the Mi-8MT"),
    ("Mi-171", "", "Mi-8",  "", "Ulan-Ude built Mi-8/17"),
    ("Mi-25",  "", "Mi-24", "", "export Mi-24D"),
    ("Mi-35",  "", "Mi-24", "", "export Mi-24V"),
    ("Su-17",  "", "Su-22", "", "Soviet-service designation of the swing-wing Fitter"),
    ("Su-20",  "", "Su-22", "", "export designation of the Su-17"),

    # ── One aeroplane, two marketing names. ──
    ("DH.100", "", "Vampire", "", "de Havilland's own number for the Vampire"),
    ("DH.115", "", "Vampire", "", "the Vampire Trainer"),
    ("Me 109", "", "Bf 109",  "", "the wartime-Allied spelling of the Bf 109"),
    ("Kittyhawk", "Curtiss", "P-40", "", "Commonwealth name for the P-40D and later"),
    ("Tomahawk",  "Curtiss", "P-40", "", "Commonwealth name for the early P-40. Scoped: the\n     # Piper PA-38 Tomahawk is a trainer, and would otherwise inherit this"),
    ("L-100",  "Lockheed", "C-130", "", "the civil Hercules"),

    # ── Bell's commercial numbers for the Huey. Bare numbers, so every one
    # of these is scoped: unscoped "204" would land the UH-1 write-up on
    # anything in the collection spelled 204. ──
    ("204", "Bell", "UH-1", "", "Bell's commercial number for the UH-1A/B"),
    ("205", "Bell", "UH-1", "", "Bell's commercial number for the UH-1D/H"),
    ("214", "Bell", "UH-1", "", "Bell's enlarged single-engine Huey"),
    ("HU-1", "", "UH-1", "", "the Huey's original designation, and where the nickname came from"),
]

# Real relationships that are NOT the same aeroplane. Each of these would
# buy coverage and each would put a subtly wrong write-up on a real page,
# so they stay out until someone writes them a record of their own. Listed
# rather than deleted so the next person does not have to re-derive why.
JUDGEMENT = [
    ("212",       "UH-1",     "twin-engine (UH-1N). Same lineage, different powerplant and "
                              "performance — the spec block would be wrong on every page"),
    ("MiG-27",    "MiG-23",   "dedicated ground-attack derivative: different nose, engine "
                              "intakes and undercarriage. 56 airframes, and all of them "
                              "deserve their own text"),
    ("B-57",      "Canberra", "Martin rebuilt the Canberra around a new fuselage and cockpit"),
    ("Mirage 5",  "Mirage III", "simplified ground-attack model — same airframe, different "
                              "aircraft to describe. 39 airframes, worth its own record"),
    ("Li-2",      "C-47",     "Soviet licence-built DC-3 with different engines, and enough "
                              "changes that Lisunov is credited as the designer"),
    ("Seafire",   "Spitfire", "navalised: folding wings, arrestor hook, strengthened airframe"),
    ("Strikemaster", "Jet Provost", "armed development, different engine and role"),
    ("HA-1112",   "Bf 109",   "the Spanish Buchón — Merlin-engined, and visibly a different "
                              "aeroplane"),
    ("Avia S-199","Bf 109",   "Jumo bomber engine and paddle prop; a notoriously different "
                              "machine to fly"),
    ("CS2F",      "S-2",      "de Havilland Canada built; the Grumman S-2 record is scoped "
                              "to Grumman, so this needs its own record rather than an alias"),
    ("F-6",       "P-51",     "the recon Mustang — but F-6 is also the export Shenyang J-6, "
                              "and nothing in the data separates them"),
    ("Fennec",    "T-28",     "the Sud Aviation T-28 — but 'Fennec' is also the Eurocopter "
                              "AS550, which is a helicopter"),
]
