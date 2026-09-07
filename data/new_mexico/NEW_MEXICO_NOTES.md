# New Mexico — build notes

Twenty museum records, 214 aircraft — the largest state pass so far, and the
first to carry missiles, rockets and spacecraft in volume.

| File | Site | Access | Rows | Tails |
|---|---|---|---|---|
| `nm_museums.csv` | 20 new museum records | — | — | — |
| `white_sands_missile_range_museum_aircraft.csv` | WSMR | restricted | 50 | 3 |
| `us_southwest_soaring_museum_aircraft.csv` | Moriarty | public | 43 | 40 |
| `war_eagles_air_museum_aircraft.csv` | Santa Teresa | public | 42 | 31 |
| `national_museum_of_nuclear_science_aircraft.csv` | Albuquerque | public | 22 | 7 |
| `holloman_afb_heritage_park_aircraft.csv` | Holloman AFB | restricted | 14 | 14 |
| `new_mexico_museum_of_space_history_aircraft.csv` | Alamogordo | public | 14 | 1 |
| `cannon_afb_static_displays_aircraft.csv` | Cannon AFB | restricted | 12 | 12 |
| `kirtland_afb_air_park_aircraft.csv` | Kirtland AFB | restricted | 5 | 3 |
| `caf_lobo_wing_aircraft.csv`, `balloon_museum_aircraft.csv` | Moriarty, ABQ | public | 2 each | — |
| 8 single-airframe park/monument files | statewide | mixed | 1 each | — |
| Walker Aviation Museum, Western NM Aviation Heritage Museum | — | public | 0 | — |

119 of 214 rows carry a tail (56%) — the lowest of any state so far, and
almost entirely because **no missile at either missile park has a published
serial**. Excluding missiles and rockets, aircraft coverage is good.

## Three new role_type values

`role_type` is VARCHAR(30), not an enum, so this pass added three values
rather than forcing bad fits:

- **`surface_to_air`** (15 rows) — Nike Ajax, Nike Hercules, Hawk, Patriot,
  Lark, Terrier, Talos, Tartar, Roland, HIBEX, ERINT, BOMARC, SA-2. The
  alternative was inverting `air_to_surface`, which would corrupt any query
  that filters on launch platform.
- **`anti_tank`** (3) — Shillelagh, SS-11/AGM-22, TOW. `anti_ship` is wrong.
- **`artillery_rocket`** (4) — Honest John, Little John. Unguided battlefield
  rockets are not `ballistic` in the strategic sense the schema comment implies.

If these should be folded into existing values, they are easy to `UPDATE` —
but the distinction is real and the alternatives all lose information.

## The verification pass earned its keep

Five entries from the single-source gazetteer were wrong, and one museum no
longer exists. All of these would have shipped as fact:

- **CAF New Mexico Wing, Hobbs — DEFUNCT.** Directories still list a WWII
  museum in an ex-B-17 hangar with nine aircraft. The CAF's own current unit
  roster has only two New Mexico units, Lobo Wing and Border Eagles, and no
  Hobbs wing. Air Museum Network's own listing for it now redirects its website
  field to lobowing.org. Its Bf 108D-1 Taifun (c/n 3059, N2231) went to the
  American Airpower Heritage Flying Museum in Dallas in **August 2015**. The
  Lobo Wing's projects page describes acquiring gear "from the New Mexico
  Wing" — the language of an estate being distributed. Closure date not
  established; the other seven aircraft are untraced.
- **The ENMU-Roswell F-105D moved in 2021.** 61-0110 is now at **Hobbs
  Veterans Memorial Park**, dedicated 30 May 2022. Aerial Visuals still shows
  it at Roswell. Recorded at Hobbs.
- **The Carlsbad AT-11 does not exist.** The only airframe at Cavern City Air
  Terminal is a Sikorsky SH-34G, itself flagged "can you confirm this is
  stored here?" The only documented AT-11 in New Mexico is the Lobo Wing's
  41-9451 at Moriarty — almost certainly the source of the confusion.
- **Santa Fe's F-100 and Ryan Navion are gone.** The F-100 record's coordinate
  is in the Barrio de Analco Historic District downtown — identical to the
  dossier for the long-defunct "Wings of Yesterday" museum. Only the F-111F
  70-2408 "City of Santa Fe" is actually at the airport.
- **Santa Fe's "F4H-1F" is not a display.** It is F-4A BuNo 145310, ex-N815WF,
  a **private return-to-flight project** held by F4 Phantom II Corp since 2017;
  registration cancelled 2020. Excluded.
- **Portales is an F-111F, not an F-111D.** Aerial Visuals mislabels 70-2364;
  Baugher places it in the F-111F block and records its fate verbatim as "on
  display on stick in Portales, New Mexico."

**Aerial Visuals and silverhawkauthor are probably not independent** — Aerial
Visuals repeatedly credits Andy Marden's *U.S. Military Out of Service*, likely
silverhawk's source too. Where those two agree and nothing else does, treat it
as one source.

## Identity versus markings

Nine airframes wear a number that is not their own:

| Airframe | Wears |
|---|---|
| Holloman F-104C 56-0886 | 60764 / FG-764 |
| Holloman F-4C 63-7537 | 63-535 |
| Holloman YF-117A 79-10782 | 85-816, or 793, depending on repaint |
| Holloman F-80 45-8557 | 9853 |
| Kirtland A-7D 72-0177 | 72-0245 |
| Kirtland MiG-21 | "150 red", formerly "562" / "Red 13" |
| Cannon RF-101C 56-0187 | 32426 |
| War Eagles P-40E AL152 | 41-36402 and AVG Flying Tigers colours |
| War Eagles PT-13D 42-17250 | PT-17 41-8275 |

Two reported "extra aircraft" at Cannon collapsed into markings: the "JF-101A
53-2426" is RF-101C 56-0187's paint, and the "F-100A 56141" is F-100D
56-2940's tail marking — no F-100A has ever carried a 56-series serial.

## Judgment calls

- **The two Alamogordo Tornados are different aircraft.** Heritage Park at
  Holloman has ex-Marineflieger **43+75**; the Space History museum has
  Luftwaffe **45+11**, which served at Holloman 1999–2009. Sources conflate
  them constantly. Aerial Visuals still shows 45+11 outside the German Air
  Force HQ on base — stale.
- **Holloman's YF-117A 79-10782 is "Scorpion 3"**, FSD-3, one of five Senior
  Trend development jets. Nellis has FSD-1, 79-10780, recorded in Nevada. Both
  are genuine.
- **War Eagles has one Mustang, not two.** The site lists a P-51D under
  Fighters and a TEMCO TF-51D under Trainers; only 44-84658 / N51TF could be
  corroborated, and Wikipedia and Aerial Visuals list one. Recorded once as a
  TF-51D.
- **War Eagles' collection has NOT been sold down** since John MacGuire died in
  2016. 19 of 20 FAA registrations are current and held by the museum
  corporation, expiring 2027–2030. Only the Mi-2 is deregistered, consistent
  with its listed restoration. No aircraft are privately owned or on loan.
- **Its "Storch" is a Morane-Saulnier MS.502 Criquet** — the French postwar
  derivative, not a Fieseler Fi 156. Its "MiG-15bis" and "MiG-15UTI" are Polish
  WSK/PZL-Mielec Lim-2 and SBLim-2A, filed under PZL-Mielec to match Utah,
  Idaho and Nevada. Its "T-33A" is a Canadair Silver Star Mk.3.
- **The CAF Border Eagles Squadron is folded into War Eagles**, not given its
  own record. Its single PT-19 is housed there per the CAF's own unit page, and
  the squadron has no independent public access. Its registration is not
  established.
- **The Cherokee II N3034 is recorded once, at the Balloon Museum**, on loan
  from the Soaring Museum. It appears in both institutions' lists; an aircraft
  is in exactly one place.
- **Cannon AFB is not an air park.** The circular park by the main gate was
  broken up in early 2013 and the aircraft scattered — the F-16 to Eagle Claw
  Blvd, the EF-111A to the Joe Cannon Estates entrance, the AC-130W to the
  "Steadfast Line" in March 2024. Recorded as scattered base displays under one
  record.
- **Kirtland's "P-51D 45-11400" is a reproduction.** That serial appears in no
  surviving-Mustang list, and US Demobbed — which catalogues genuine ex-military
  airframes and lists everything else in the park — omits it. Recorded as a
  full-scale reproduction with a blank tail.
- **Two museums are recorded with zero aircraft**: Walker Aviation Museum
  (Roswell) is a memorabilia and photo exhibit in the airport terminal, and the
  Western New Mexico Aviation Heritage Museum (Milan) is about airway
  navigation infrastructure — a 1953 Flight Service Station on the National
  Register, a 1929 beacon tower, a generator shed. Both are real museums; the
  empty aircraft list is the finding.

## Space hardware — mostly replicas, and that matters

The New Mexico Museum of Space History displays **mock-ups and training units**
of most of its famous artifacts; the originals are in orbit, on the Moon, or at
the Smithsonian. Recorded as `spacecraft` with the status stated:

- **X-37B — the museum's own catalogue title says "Mockup."**
- **Apollo boilerplate** capsules, one of them atop the Little Joe II.
- **Little Joe II is not a flown vehicle.** It was built up from leftover test-
  programme components, delivered 1985, and is **owned by the Smithsonian** with
  the museum as custodian. A refurbishment began November 2025, so its display
  status in 2026 may be in flux.
- Sputnik, Explorer, Echo II, Alouette I, TIROS, Syncom, Landsat — all replicas
  or scale models. Not recorded.
- **Genuinely flown**: the Mercury Primate Capsule (recorded), plus shuttle
  thermal tiles, a forward booster, a lunar sample return container, a Viking
  lander camera and a moon rock — artifacts rather than vehicles, not recorded.

**Sonic Wind No. 1 has left New Mexico.** The rocket sled Stapp rode is a
Smithsonian artifact (NASM A19680015000), transferred by the USAF in 1966 and
only ever on long-term loan to Alamogordo. It is now on display at NASM in the
"Nation of Speed" exhibition. Wikipedia and newmexicoculture.org both still list
it at Alamogordo. What remains at Stapp Park is a different article, the "Rocket
Sled (PTV)". The Daisy Track **is** still on site.

**The Balloon Museum does not have the Double Eagle II gondola.** The flown
article is at the Udvar-Hazy Center (NASM A19790532000). Albuquerque displays a
model. This is the single most-conflated fact about that museum. Only the
*Jules Verne* gondola is recorded as a real airframe; Double Eagle V, Breitling
Orbiter 3 and Two Eagles could not be confirmed as originals and were left out.

## Excluded — do not re-research

- **CAF New Mexico Wing, Hobbs** — defunct, see above.
- **Artesia F-84F 51-9486** — Aerial Visuals and silverhawk give the same
  serial, but they share a source, the coordinate falls on a nature trail 500 m
  from Baish Veterans Park, no city page or photo mentions an aircraft, and the
  serial is in no surviving-F-84 list. **Unverified rather than refuted** —
  worth a call to the City of Artesia.
- **Truth or Consequences T-33A 51-9022** — moved from Ralph Edwards Park into
  a hangar at T or C Municipal Airport for restoration, which is incomplete.
  No published public viewing arrangement, so no honest access classification.
  Also repainted by high-school students, making the serial doubtful. Revisit
  when the restoration finishes.
- **Kirtland's Antonov An-2T** — a contractor-operated flying asset under DoD
  contract, not a static display.
- **Ground-instructional airframes**, which are not displays: Holloman Tornado
  43+83; Cannon C-130E 63-7856; Kirtland's CV-22Bs, C-130s, HU-25B and TH-57C.
  Kirtland F-102A 57-0812 is derelict.
- **Cannon's departed aircraft** — F-86H 53-1251 and F-84C 47-1530 (which wore
  "11027" and appears in older lists as a phantom "F-84E 51-1027"). Gone by the
  Feb 2019 survey.
- **Spaceport America** — an operational commercial spaceport; VSS Unity and
  Eve are Virgin Galactic operating assets, not exhibits.
- **Cavalcade of Wings**, Albuquerque Sunport — 900+ scale models, no airframes.
  Also curates the Santa Fe and Carlsbad terminal displays.
- **International UFO Museum**, Roswell — no aircraft.
- **Bradbury Science Museum**, Los Alamos — Fat Man and Little Boy replicas.
- **Las Cruces International Airport** (Southwest Aviation's C-46, A-26B, PV-2,
  F-100F) — a private aerial-firefighting operator's ramp.
- **Roswell Air Center boneyard** — commercial airliner storage.
- **Melrose Bombing Range F-100A** — an active range target.
- **Deming Luna Mimbres Museum**; Silver City, Taos, Socorro, Hobbs municipal
  airports — no displays found.

## Needs a human on site

- **War Eagles Sea Fury**: WJ231 (FAA) versus ex-Iraqi 253 (Aerial Visuals).
- **War Eagles P-38 c/n**: 8057 (FAA) versus 422-8091 (Aerial Visuals).
- **Every missile serial at both missile parks** — none published anywhere.
- **The Gateway Freedom Monument has no published coordinates.** Recorded with
  the address only; it post-dates every gazetteer. A second "final dedication"
  was scheduled for 2 July 2026.
- **Hobbs F-105D position** — the coordinate is a street geocode of the park
  address, not a survey of the aircraft.
- **Cannon T-33A 58-0503** — last confirmed October 2012, the weakest entry
  there. **Kirtland's MiG-21** last confirmed 2010.
- **WSMR's VC-6A 66-15361 and UH-1M 66-0616** rest on a single source each.
- **The Balloon Museum's Double Eagle V, Breitling Orbiter 3 and Two Eagles** —
  original or replica, unresolved. Not recorded either way.
- Whether the **Portales F-111's 2023 restoration** was completed. The aircraft
  is definitely still displayed; the repaint is unconfirmed.
