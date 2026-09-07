# Idaho — build notes

Idaho was a clean slate: the live database held zero Idaho museums and zero
Idaho aircraft before this pass. Nine museum records and 64 aircraft.

| File | Site | Rows | Tails |
|---|---|---|---|
| `id_museums.csv` | 9 new museum records | — | — |
| `warhawk_air_museum_aircraft.csv` | Warhawk Air Museum, Nampa | 15 | 12 (80%) |
| `legacy_flight_museum_aircraft.csv` | Legacy Flight Museum, Rexburg | 15 | 14 (93%) |
| `bird_aviation_museum_aircraft.csv` | Bird Aviation Museum, Hayden | 10 | 10 (100%) |
| `spirit_of_flight_center_aircraft.csv` | Spirit of Flight Center, Nampa | 10 | 4 (40%) |
| `warbirds_museum_driggs_aircraft.csv` | Warbirds Museum, Driggs | 7 | 7 (100%) |
| `idaho_military_history_museum_aircraft.csv` | Boise, Gowen Field | 4 | 3 |
| `id_parks_aircraft.csv` | Carl Miller / Lakeview / Malad City parks | 3 | 3 |

52 of 64 rows carry a tail (81%). Zero tail collisions and zero museum-name
collisions against the live database at build time.

## Two corrections to every published Idaho list

**The Bird Aviation Museum is not in Sagle.** It left the Bird Ranch in spring
2019 and reopened in a hangar at Coeur d'Alene Airport, 2678 W. Cessna Ave,
**Hayden**. aviationmuseum.eu still lists the Sagle address with 21 aircraft;
aerialvisuals still files it under "Sandpoint" with 40+. Both are six years
stale. The Sagle site is permanently closed. Dr. Forrest Bird died in 2015 and
his personal fleet of roughly twenty aircraft was largely sold off; eleven
departures are FAA-confirmed, including his father's Piper J-3 **N26044**,
which went to the **Palm Springs Air Museum** — not the Smithsonian, as the
museum's own legacy page had predicted. What remains is ten airframes.

**Two museums were missing from every source consulted.** The **Spirit of
Flight Center** relocated from Colorado and opened at Nampa Municipal in
October 2022. The **Warbirds Museum at Driggs-Reed Memorial Airport** appears
in no aviation-museum directory at all.

## Serial coverage is the weak point here, and it is a real finding

Idaho's museums do not publish serials. Warhawk's fifteen per-aircraft pages
carry full spec tables — engine, thrust, service ceiling — and **not one
serial or registration**. Every identity in that file came from the FAA
registry, aerialvisuals, warbirdregistry, or Vintage Aviation News, not from
the museum. This is the inverse of Hill, where the museum's own pages gave 92%
coverage.

Three Warhawk aircraft have **no published serial anywhere** — the F-86F, the
F-84G and the F9F-2 under restoration. They appear in no registry, in no
surviving-aircraft list, and on no FAA record. Imported with blank tails
rather than guessed. Same for the Legacy A-4's BuNo, the Warhawk PT-23 at
Boise, and six Spirit of Flight airframes. **Blank tails never collide**, so
any re-run of these files must go through `filter_new_aircraft.py` first.

`383175/75` is circulating as the Boise PT-23's serial. It comes from
aviationmuseum.eu alone, does not parse as a USAAF serial, and sits in a
garbled table cell next to the RF-4C's 69-0350. Recorded as blank.

## Identity versus markings

Idaho has an unusually high rate of aircraft wearing serials and schemes that
are not their own. Recorded as what the airframe *is*, with the marking noted:

- **Warhawk's P-51C 43-25057** wears QP-B, Duane Beeson's *Boise Bee*. Beeson's
  aircraft is not this one. The museum is named for the marking.
- **P-40E is AK933** (RAF/RCAF 1057), restored with P-40F wings, wearing 112
  Sqn shark-mouth SU-E.
- **F-86F "Bernie's Bo"** wears Capt. Robert J. Love's 335th FIS markings; his
  jet was 51-2769. The museum's "built 1949, Dallas" is doubtful — F-86F
  production began in 1952. Flagged, not recorded.
- **F-84G** wears a Thunderbirds scheme with no evidence it served with the team.
- **Boise's F-86** is the one confirmed false-serial case: **51-2826**, an
  F-86E-10-NA completed as an F-86F-2 Project Gunval 20mm testbed, repainted
  in 2012 as "91050 / City of Coeur D'Alene". Wikipedia's caption calls it an
  "F-86A replica"; aerialvisuals documents a continuous real-airframe
  provenance. Wikipedia is wrong on both counts.
- **Legacy's P-63C is 43-11223** painted as 42-69021. Aerialvisuals and
  aviationmuseum.eu record the marking as the identity; FAA and warbirdregistry
  agree on 43-11223, and warbirdregistry explicitly explains the repaint.
- **Legacy's A-4** is in Blue Angels colors. It came off the Davis-Monthan line
  via an Ontario, Oregon auction. Do not read the paint as provenance.

## Judgment calls

- **Warhawk's "MiG-17F" is a Polish Lim-5**, batch 1C 14-17, filed under
  PZL-Mielec to match Hill and Western Sky in Utah. The museum credits
  Mikoyan-Gurevich.
- **Warhawk's MiG-21 is a Czechoslovak Aero S-106**, i.e. a licence-built
  MiG-21F-13, not the Soviet aircraft the placard implies. Filed as
  Mikoyan-Gurevich MiG-21 F-13 to match the Prop and Jet Air Museum row.
- **Legacy's "Mormon Mustang" is filed under Cavalier**, not North American.
  67-22579 is a 1967 Cavalier Mustang II built for the USAF's Peace Condor
  programme and sold to Bolivia — a post-war remanufacture, not a WWII P-51D.
  This is the only Cavalier row in the database.
- **The Norseman N164UC is at Legacy but absent from Legacy's own website.**
  Included on FAA ownership plus an aerialvisuals sighting dated 1 Jan 2026.
- **Boise's RF-4C 69-0350** is recorded as an airframe. aviationmuseum.eu says
  "(cockpit)"; aerialvisuals lists it as a complete airframe with a site
  coordinate. Unresolved — needs eyes on it.
- **Ownership is not custody.** Warhawk's three warbirds are held by Mustang
  LLC and War Hawk LLC, and six of Legacy's fifteen sit in single-purpose
  Bagley-family LLCs. All recorded where a visitor finds them.

## Excluded — do not re-research

**Visiting and based aircraft.** Warhawk publishes a separate "Visitors" page —
FM-2 Wildcat, Piper L-4, T-28A, Stearman, SNJ, TBM Avenger, P-51D. Excluded.
aviationmuseum.eu lists the L-4 (N51992, privately owned in Nevada) and a
Stearman as collection aircraft; they are not.

**The Driggs Corsair.** A genuine, airworthy F4U — photographed flying over the
Tetons, taxiing at Driggs, and parked indoors under the Warbirds Café banner
with stanchions. But it appears in none of Richard Sugden's eleven FAA
registrations, has no spec block on the page that features it (the only
aircraft page there without one), and appears in no surviving-Corsair list at
Driggs. Excluded as a visiting warbird rather than recorded with a guessed
identity.

**Driggs' T-28 Trojan** is listed by the airport but not by Teton Aviation, is
not among Sugden's registrations, and has no photographic evidence. Excluded as
a probable error on the airport's page.

**MiG Fury Fighters** — FJ-4B N400FS (the last flying FJ-4B of 374 built),
MiG-15bis and MiG-17F — operate from Driggs as an airshow team, not as
exhibits. The **Aviat Husky N51HU** is Teton's glider tug, owned by Teton
Aircraft Sales. Excluded.

**Spirit of Flight aircraft that could not be placed in Nampa:** the Learjet
24D N721SF (on long-term loan to Redstone College, Denver since 2009), the
Falcon 20 N722SF, and the ARC Special N8400H. All three are registered to the
foundation at its Nampa address, but a registration address is the owner's, not
the airframe's. The **Bf 109F-4 Wk.Nr. 10145** ("Yellow 3", recovered near
Murmansk in 1994) is listed by Wikipedia as on display; the director's own
company lists it as a wreck under restoration and **for sale**. Excluded. The
**Evel Knievel Skycycle X-2** is an acknowledged 2015 television replica, and
the 1:7 A-10 is a radio-control model.

**Gowen Field ANGB airpark** — nine complete airframes (C-130E, A-10A, T-33A
NASA 815, RF-4C 68-0594, F-102A, F-4G, UH-1F, AH-1F, UH-1M) about a mile from
the museum, inside the wire. Requires a military sponsor, background check and
a REAL ID. Not public. Note that its RF-4C **68-0594** is routinely confused
with the museum's **69-0350**.

**Aeroplanes Over Idaho, Caldwell** — closed. No record of where its ten-plus
aircraft went. Worth a look if anyone has a lead.

**Holt Heritage Airpark, Mountain Home AFB** (30+ airframes, on-base escort
only); **Saylor Creek Range** (90+ derelict target hulks); **Idaho State
University** (instructional airframes); **Airpower Unlimited, Jerome** and
**Pacific Fighters, Idaho Falls** (private restoration shops); **Museum of
Idaho** (its 2024 aviation exhibit was a travelling simulator show, no
airframes); **Museum at the Brig, Farragut** (naval training station, not
aviation); **Cabela's Post Falls**; **Silverwood** (its Schweizer 2-33A went to
the Bird museum). Ramp and FBO aircraft at Burley, Caldwell, Lewiston,
Pocatello, Twin Falls, McCall, St. Maries and Sandpoint are based aircraft that
aerialvisuals' airframe locator counts as sites — that tool is a locator, not a
museum list.

## Park monuments

Three single-airframe city-park displays are included as museum records on
Zach's call: the **F-111A** at Carl Miller Park, the **F-89B** at Lakeview
Park, and the **T-33A** at Malad City Park. All three are complete airframes,
free, always accessible, and none is playground equipment. All three remain
**USAF property on NMUSAF loan** — the cities hold them, they do not own them.

The F-111A's "AF67058" is its true serial, **67-0058**, not a marking: an A
model, c/n A1-103, a Linebacker II combat veteran with the 429th TFS out of
Takhli, later 389th TFS at Mountain Home, on the pole since 1990.

The F-89B **49-2457** is the standout — one of only 36 F-89Bs built, flown by
the 190th FIS Idaho ANG at Gowen Field, on display in the same park since
**December 1959**. Restored in 2004 by a pilot who had flown it, and again in
2018.

aerialvisuals' Idaho index shows "2" against Malad, Nampa and Mountain Home;
each location dossier lists exactly one airframe. The index number is a count
bucket, not an airframe count — it shows "20+" against Gowen Field's nine.

## Needs a human on site

- Boise's RF-4C 69-0350: complete airframe or nose section.
- Boise's PT-23: any serial at all.
- Warhawk's F-86F, F-84G and F9F-2 serials — a phone call to the museum would
  likely close all three at once.
- Whether Warhawk's Waco CG-4A fuselage is still displayed. Ruud Leeuw saw it in
  2014; it is absent from the museum's current collection page and from
  aerialvisuals, so it is not recorded here.
- Lakeview Park's ZIP: the City of Nampa gives 83651, third-party listings 83687.
