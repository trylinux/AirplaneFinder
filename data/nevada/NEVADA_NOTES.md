# Nevada — build notes

Eight museum records, 40 aircraft. Nevada was the first state built with
`museums.access_type`, and it is the state that forced the column to exist.

| File | Site | Access | Rows | Tails |
|---|---|---|---|---|
| `nv_museums.csv` | 8 new museum records | — | — | — |
| `nas_fallon_heritage_air_park_aircraft.csv` | NAS Fallon | restricted | 24 | 24 |
| `nellis_afb_freedom_park_aircraft.csv` | Nellis AFB | restricted | 8 | 8 |
| `nevada_air_national_guard_152nd_aircraft.csv` | Reno ANGB | restricted | 2 | 2 |
| `howard_w_cannon_aviation_museum_aircraft.csv` | Harry Reid Int'l, Las Vegas | public | 1 | 1 |
| `winnemucca_veterans_memorial_park_aircraft.csv` | Winnemucca | public | 2 | 2 |
| `hawthorne_ordnance_museum_aircraft.csv` | Hawthorne | public | 2 | 0 |
| `indian_springs_school_air_park_aircraft.csv` | Indian Springs | public | 1 | 0 |
| `USAF Thunderbirds Museum` | Nellis AFB | restricted | 0 | — |

## Nevada has no conventional public aviation museum

That is the finding, not a gap. **34 of Nevada's 40 recorded airframes are
behind a base gate.** The public side of the state is one record-setting
Cessna hanging in an airport terminal, two aircraft in a Winnemucca park, two
rotorcraft outside an ordnance museum, and an F-84F on a school lawn.

Without `access_type` this state had only bad options: omit 34 real,
documented airframes, or list Fallon and Nellis as though a visitor could turn
up. Both are now recorded honestly and neither wins a proximity search unless
the caller passes `include_restricted=1`.

## Cactus Air Force — the trap, and it was live

Wikipedia lists a ~28-airframe Cactus Air Force Wings and Wheels Museum at
Carson City Airport. **It is dispersing right now.** The Carson City Airport
Authority board packet for **19 August 2026**, item H-3, is a motion to approve
*"Cactus Airforce, LLC lease assignment to AADF Legacy Airbase, Inc."* — the
sale of Hangar 33 to the Dream Flights organisation, whose own access plan is
call-ahead-and-be-escorted, not a museum.

The collection left over 2021–2025, all FAA-confirmed:

| Airframe | Went to | Date |
|---|---|---|
| B-26C Invader N126HK | Stockton Field Aviation Museum, CA | Jul 2024 |
| CT-133 Silver Star N613RC | S&S Land and Cattle, Ione CA | Jan 2021 |
| CT-133 Silver Star N615RC | Chris Galloway, Jordan Valley OR | Jan 2021 |
| TS-2A Tracker N508JR | William Garrison, Nickerson KS | Feb 2019 |
| T-6G N29933 | Green Country Warbirds, Sapulpa OK | Feb 2021 |
| T-34A N3799G | Chris Rounds, Waller TX | Mar 2023 |
| PT-13B N52740 | Tanya Nightingale, Rancho Cucamonga CA | Jul 2021 |
| AH-1S N102JG | registration cancelled | Aug 2022 |

Seven airframes still carry the Cactus name, four of them registered at a
**Dayton NV residential address**. The nonprofit files a 990-PF — a private
foundation with zero public contributions. The last first-hand visitor account
is **January 2016**, and it records being told the place "really wasn't a
museum but I was welcome to look around." Vintage Aviation News confirmed the
Stockton sale in December 2025.

**Excluded. Do not re-research from Wikipedia — that article is a c. 2014
snapshot.**

Related correction: **"Yesterday's Flyers"** (also Carson City, also closed) is
a *separate* collection, not an earlier name for Cactus. It held Bleriots,
Nieuports, a Pfalz D.III and Stinsons — Golden Age and WWI types with **zero
airframe overlap**. An earlier pass of mine assumed they were the same
collection under two names. They are not.

## Three corrections to what the directories say

- **The Cannon Museum's "Ford Trimotor" is a Ford Thunderbird.** Every primary
  source lists one aircraft plus a restored 1956 Thunderbird convertible —
  George Crockett's Alamo Airways airport crash-wagon. A secondary source
  turned the car into a 5-AT. There is no Trimotor. The museum has exactly one
  airframe: **Cessna 172 N9172B**, which stayed aloft 64 days, 22 hours and 19
  minutes over Las Vegas in 1958–59 and still holds the record.
- **The Indian Springs F-84F is not in the community park and not on Creech
  AFB.** It stands on the grounds of Indian Springs Middle/High School, whose
  mascot is the Thunderbirds. Clark County's park page correctly lists no
  aircraft — the jet is next door on school land. Publicly viewable. Recorded
  under its true site name.
- **The Nevada ANG airframes are not "accessible to the public."** One source
  says so; the RF-101B and RF-4C are pylon-mounted inside the wire at the main
  gate, and the one published visit account describes a family being received
  at the gate and escorted. Recorded as restricted.

## Identity versus markings

Nevada's rate of false serials is the highest of any state built so far.

- **Nellis F-100D 55-3595 is painted as 56-3298**, and **F-5E 74-1571 as
  73-0865**. Neither wears its own serial.
- **Nellis F-4C 64-0806 carries four kill stars.** Its dossier records no MiG
  credits. Commemorative, not this airframe's record.
- **Fallon UH-1B 60-3593 is a USAF airframe wearing US Navy HA(L)-3 "Seawolves"
  markings** coded 313.
- **Fallon's two "MiGs" are Polish.** The Lim-2 (1614) and Lim-5 (1319) are
  WSK/PZL-Mielec licence aircraft, displayed as "546" and "3020". Filed under
  PZL-Mielec to match Hill, Western Sky and Warhawk.
- **The MiG-23ML is 20+23**, an ex-East German NVA jet that passed to the
  Luftwaffe on reunification, repainted back to "353 red".
- **The MiG-29 is ex-Moldovan**, one of the 21 the United States bought in
  1997, displayed as "Black 15" though its own bort was 10.
- **Fallon's squadron codes are unreliable.** The E-2C, F-14, S-3B and A-7C
  have each been photographed in two or three *different* squadron schemes in
  different years. Every code in the aliases is "as last photographed", not
  service history.

## Judgment calls

- **Nellis YF-117A 79-10780 is genuine** — FSD-1, the first F-117 ever to fly,
  18 June 1981, on a pylon since May 1992. Not a mockup. Named "Scorpion 1".
- **Four "built as X, converted to Y" airframes** are filed under what they are
  now, with the origin in aliases: F-105G 63-8276 (ex-F-105F), Nellis; F-4G
  69-7551 (ex-F-4E) and AH-1F 67-15496 (ex-AH-1G) and UH-1M 66-15229 (ex-UH-1C)
  at Gowen Field.
- **Winnemucca's F-86 is an F-86L**, built as an F-86D-55-NA and converted. The
  on-site sign says F-86D; warbird registries say F-86L. Both describe the same
  airframe at different points in its life. Its "30568" marking *is* its own
  serial, 53-0568 — one of the few honest ones here.
- **The Winnemucca UH-1H serial is not settled.** 66-16654 vs 69-16654 across
  two sources. The last four digits agree and the July 1967 build date favours
  FY66, which is what is recorded. Flagged.
- **Hawthorne's two rotorcraft have no published BuNo** anywhere. Imported with
  blank tails. The HUP's sub-variant is uncertain: one source says HUP-1, but
  only one HUP-1 is otherwise recorded as extant, so it may be an HUP-2/-3.
- **The Thunderbirds Museum is recorded with zero aircraft.** Its single static
  jet outside the hangar is real but unidentified; the museum record exists so
  the aircraft can be added once someone reads the tail.

## Excluded — do not re-research

- **Cactus Air Force** — see above.
- **Reno Aviation Museum** — an active nonprofit, but its holdings are a Jenny
  *fuselage*, a Learfan *test article*, a Link Trainer, an F-16 simulator and a
  de Havilland *cockpit section*. At most one complete airframe (a Cessna T-50),
  attributed by a single 2016 article with no registration. Appointment-only,
  no published admission. Revisit if the T-50 is confirmed.
- **Battle Mountain Air Museum** — defunct, and **nothing is left on site**.
  The claim that "a few aircraft remain in public view" is stale boilerplate
  that the same database's own table contradicts. F-86L 53-1045 was airlifted
  out by Chinook on 5 Nov 2008 to Historic Wendover; the T-33 was actually a
  Navy **TV-2, BuNo 138064**, also gone; F-4E 66-0286 relocated; F-111A 66-0012
  went to a Texas non-profit in 2017–18; C-119G N5216R was containerised for an
  Alaska project that is now dormant; a second C-119G was scrapped by 2014.
- **Nellis Threat Training Facility** — 20+ Soviet types including Mi-24 and
  Su-7. A classified training facility, not a museum, with no escort route.
- **Reno-Stead Army National Guard** (UH-1H, CH-54A) — different unit, different
  branch, different site, no public display. Do not merge into the 152nd's
  record.
- **National Atomic Testing Museum** — no aircraft, despite appearing in
  aviation-museum directories.
- **Nevada State Museum** (both), **Central Nevada Museum**, **Clark County
  Museum**, **Museum at the Brig** — no airframes.
- **Scroggins Aviation, Las Vegas** — 130+ "aircraft", all film-industry
  mockups and props.
- **Nelson NV** — 150+ T-28 airframes in a private yard, not a display.
- **Sparks Marina F-4** — deliberately sunk as a scuba attraction.
- **Lake Mead B-29** — an underwater wreck, permitted technical dives only.
- **Amargosa Valley VFW Post 6826** (UH-1H) and **Elko VFW Post 2350** (a
  helicopter received in 2023 for a future park) — plausible park monuments,
  but neither has a confirmed serial or a confirmed installed location. Left out
  rather than recorded on two directory listings. Worth a phone call.
- **Fiesta Henderson casino Beech 18** — the casino was demolished from 2022;
  the aircraft's fate is unknown.
- **American Museum of Aviation, Las Vegas** — solicits donations and has said
  it "will be" Nevada's first Las Vegas aviation museum for 18 years, with no
  address, no aircraft and no opening date. Three directories carry it as real.
  It is not.

## Needs a human on site

- Fallon's **F-4**: is it 151510 (F-4N) or 151014 (F-4B)? Two visitor reports
  read 151014 off the airframe; Baugher confirms 151510 was converted to F-4N.
  A photo of the data block settles it.
- Fallon's **F-14 159626**: F-14A or F-14D(R)?
- Fallon's reported **E-2C 160701 cockpit section** — single-source, in no
  walkaround list. Not recorded here.
- Fallon's **park coordinates**. The one published figure plots 50 miles west,
  near Carson City. Left blank rather than guessed.
- **Year built is blank for all 24 Fallon airframes.** No source publishes
  build dates for them and none were estimated.
- Hawthorne's **QH-50D and HUP** BuNos, and the HUP's true sub-variant.
- The **Indian Springs F-84F** serial. "1776" is a display marking.
- Whether **Nellis F-15D 78-0567** (placed on display Nov 2023) is formally part
  of Freedom Park. Its coordinates continue the display row at the same spacing,
  but no base release ties it to the park. Not recorded here.
