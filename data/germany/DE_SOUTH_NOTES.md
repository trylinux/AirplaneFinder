# DE-SOUTH — Bayern, Baden-Württemberg, Hessen, Rheinland-Pfalz, Saarland

Output directory: `/home/claude/de/south/`
Files: `de_museums.csv` (58 sites) + 58 `<slug>_aircraft.csv` files (323 airframes,
266 with a tail number / tactical code — 82 % serial coverage).

---

## Sources and how much weight each carried

**Rung 1 — the site's own publication.** Used where it exists: the Bundeswehr
`zms.bundeswehr.de` Museums- und Sammlungsverbund pages (Kaufbeuren TAZLw,
Fürstenfeldbruck TG Fursty, Laupheim HSG 64, and Wunstorf LTG 62 which turned out
to be in Niedersachsen and is not mine); `jabog34allgaeu.de`; `munich-airport.de`;
the Lufthansa Group newsroom for Hangar One; `mgs-lechfeld.de`; `f-104.de`.
These win on "what is here now" and I preferred them over lists.

**Rung 2 — two specialist F-104 registers, both current.**
- `i-f-s.nl` "Preserved in Germany" (International F-104 Society). Entry-by-entry,
  with 2024 and 2025 sightings noted in the text (e.g. Memmingen 24+17 "repainted
  late April 2024", Köln-Wahn 23+98 "since June 2025"). This is the single best
  currency source I found for Germany.
- `916-starfighter.de/F-104_GAF_fate_quicklist.pdf`, the German F-104 fate list,
  with "NEW" flags on 2024–25 changes (23+92 moved to Bad Wildungen; 24+85 to
  Wittmund; 28+22 sold August 2025).
Between them these two carry most of the 39 Starfighter rows in this set and are
the reason serial coverage is as high as it is. **They disagree with German
Wikipedia repeatedly, and where they do I followed them** (see corrections below).

**Rung 3 — `aviationmuseum.eu`.** Per-museum inventories with registration/type
pairs from photo surveys. It is by far the widest net for the small German
museums and supplied the bulk of the non-Starfighter rows. It is *not* reliable
on individual identities — see "Known bad data" — and it carries no visit dates,
so every collection sourced only from it says so in `description`.

**Rung 4 — German Wikipedia** `Liste von Luftfahrtmuseen` was used only to
enumerate candidate sites, never as an aircraft-level fact. It proved stale in
both directions: it lists the Albatros-Flugmuseum Stuttgart (closed), the Albert
Sammt Zeppelin Museum (closed) and Red Stars Bensheim (closed) as if current, and
it omits Luftraum Süd's real inventory, the Lufthansa Hangar One, and every
Bundeswehr traditions collection in the five Länder.

The English Wikipedia `List of surviving Lockheed F-104 Starfighters` is badly
incomplete for Germany (23 entries against ~90 real ones) and
`List of displayed McDonnell Douglas F-4 Phantom IIs` lists five German Phantoms
where there are certainly more. Neither was used as a source of record.

---

## Corrections made, with the evidence

- **F-104G 22+58.** German Wikipedia puts it with the Traditionsgemeinschaft
  JaboG 34 at Memmingen. Both F-104 registers put it indoors at Motorworld
  Böblingen, privately owned by Robert Dietz, wearing the tail of 23+26, and
  note that the venue was renamed from "Meilenwerk" in January 2014 — detail a
  copied list would not carry. Recorded at Böblingen. The Memmingen Starfighter
  is recorded as **20+98 in the false code 20+05**, which is what both registers
  say. The JaboG 34 website does still link a page about 22+58, so this is the
  one conflict I could not close; both rows say so.
- **F-104G 21+53** (Deutsches Museum, Munich) and **F-104F 29+03**. The registers
  record that 21+53 moved to Oberschleißheim in April 2016 and will not go back,
  and that 29+03 went to the Munich Luftfahrthalle in June 2022. Both sites are
  excluded from my assignment; noted here as a lead so the Munich agent gets the
  swap the right way round.
- **F-104G 25+99** was at the Zollernalb-Kaserne in Meßstetten until September
  2014; it has been at the Stetten am kalten Markt collection since end 2016. It
  is recorded at Stetten, not Meßstetten.
- **RF-104G 23+92** left PS Aero at Baarlo (NL) in **August 2024** for the Krausz
  yard at Bad Wildungen-Wega. Recorded in Hessen, not the Netherlands.
- **Grenzmuseum Schifflersgrund** is listed under Hessen by German Wikipedia. Its
  address is Platz der Wiedervereinigung 1, **37318 Asbach-Sickenberg**, which is
  in **Thüringen**. Not recorded here — handed to the eastern agent (see Leads).
- **Munich Besucherpark.** aviationmuseum.eu lists four aircraft including
  Bo 105S D-HILF. The airport's own 2025 page names three historic aircraft
  (Super Constellation, C-53, CASA 352L). I recorded the three the airport names
  and left the Bo 105 out.

## Known bad data in aviationmuseum.eu, and what I did about it

- **Museum Kiemele, Seifertshofen** — the listing gives "McDonnell F-101D Voodoo
  85-0701/SP". There is no F-101D, and 85-0701 is an F-4 serial block; the /SP
  tailcode is Spangdahlem. The row is kept as an F-101 with **no serial** and a
  description saying the identification is not credible.
- The same listing gives MiG-15 "1973" and MiG-21F-13 "1981". Those read as years.
  **1981 is also the serial the same site gives the MiG-21F-13 at the Pflumm
  museum.** I kept 1981 on the Pflumm row (where it is quoted with Hungarian Air
  Force attribution, which fits) and left both Seifertshofen rows blank.
- **Pflumm, Schwenningen** — two SG 38s are both given D-7033, and D-7033 is the
  registration of the Reiher III at the Wasserkuppe. Neither Schwenningen row
  carries a registration.
- **Pflumm** — photo captions on the same page name a Do 27 D-EMKA and a Do 27B1
  D-EJJJ and an "F-86K BB-141" while the inventory table gives Do 27B-2 D-EFFA,
  Do 27B-3 D-ELTT and "Canadair CL-13 Sabre 5 BB+141". I followed the table. BB+1xx
  is the Luftwaffe Canadair Sabre Mk 5 block, not the F-86K block (JD+), so
  Canadair is right and the caption is wrong; the F-86K claim is noted in the row.
- **AMF Fichtelberg** — "Schneider Sch-2 Fledermaus D-HBAT". A D-H registration is
  a helicopter; the type name is not one I can confirm. Kept with the registration
  and an explicit "identification unverified" note.
- **Pflumm** — "Mifka Mi-1 D-HMIA" is not a Mil Mi-1; recorded as listed with a
  description saying so, so it cannot be mistaken for the Soviet type.

## Judgment calls

- **Cockpit and nose sections** are recorded as their own rows and every one says
  "cockpit section only" in `description`: F-104G 24+11 and Fiat G.91T 34+13 at
  Söllingen; F-104G 21+83 at Neuburg; RF-104G 24+49 at Niederalteich; RF-104G
  25+07 at Roth; F-104G 26+25 at Kaufbeuren; TF-104G 27+26 at Memmingen; Convair
  240 N87982 and DC-8 fuselage 5A-DGK at Griesheim; MiG-21MF 23+38 fuselage at
  Bad Wörishofen.
- **Replicas and mock-ups** are recorded (they are what a visitor sees) with the
  replica status in `description`, never in `aliases`: the Do 335 at Schwenningen,
  the Bf 109 G-2 and Me 163/Me 262 at Manching, the Weißkopf No. 21 at
  Leutershausen, the Lilienthal gliders and the Vampyr at the Wasserkuppe, the
  Euler Nr. 33, Fokker Dr.I and "Spirit of St. Louis" at Griesheim, and the
  **MBB Lampyridae** at Niederalteich, which is a full-size manned mock-up that
  never flew.
- **Airworthy aircraft** are recorded where they live: the Messerschmitt Stiftung
  Bf 109 G-4 / G-10 at Manching, the Luftraum Süd warbirds at Elchingen. The
  Lufthansa Ju 52 D-AQUI is recorded at Hangar One because it is retired from
  flying and is now the permanent exhibit there.
- **`access_type`.** 33 `public`, 11 `appointment`, 14 `restricted`. Gate
  guardians visible from a public road are `public` (Büchel Torwächter, Haldenwang,
  Aich, Haßfurt, Ummendorf, Lahr, Söllingen, Speyer Pfalz-Flugzeugwerke, Stuttgart
  roof, Allgäu Airport). Airframes inside a Bundeswehr or USAFE perimeter are
  `restricted` (Fliegerhorst Lechfeld, Manching, Roth, Büchel, Neuburg,
  Fürstenfeldbruck, Erding/WIWeB, Germersheim, Brauheck, Neubiberg, Memmingen
  barracks, Ramstein). Bad Wildungen-Wega is `public` because the aircraft are
  explicitly described as visible from the main road although the yard is not open.
- **Büchel is split into two site records** — `Fliegerhorst Büchel Torwächter`
  (public, 21+67) and `Fliegerhorst Büchel` (restricted, the instructional 26+26)
  — because a visitor can reach one and not the other.
- **Fürstenfeldbruck** is recorded as one site covering both the plinth aircraft
  spread across the former airfield and the TG Fursty collection in the Captain
  Richard Higgins building, since they are the same visit.

## Blank fields left deliberately

- `latitude`/`longitude` are blank everywhere except the Wasserkuppe. Every record
  carries a five-digit PLZ, which the brief says geocodes precisely; I did not
  invent pins.
- `year_built` is filled only four times (Munich Constellation 1957, C-53 1941,
  CASA 352L 1949, Frankfurt C-54 1945, Penzing Noratlas 1956) where a build or
  roll-out date was published.
- 57 rows have no `tail_number`. The largest blocks are the seven
  Fürstenfeldbruck plinth aircraft, five of the six Laupheim helicopters, the
  three JaboG 34 types and 12 unregistered gliders/replicas at the Wasserkuppe.
  In every case the description says the serial is not published.

---

## Excluded, and why — named

**Out of scope by assignment** (another agent has them): Deutsches Museum München,
Deutsches Museum Flugwerft Schleißheim, Technik Museum Speyer, Auto- und
Technikmuseum Sinsheim, Flugausstellung Hermeskeil, Dornier Museum Friedrichshafen,
Zeppelin Museum Friedrichshafen.

**Deutsches Museum Verkehrszentrum, München** (Bo 105C D-HDDX). A third Deutsches
Museum site in Munich. Left out as part of the Deutsches Museum exclusion; flagged
as a lead so it is not lost.

**No airframe held** — checked, nothing to record:
- Zeppelin-Museum Zeppelinheim, Neu-Isenburg — permanent exhibition of airship
  history, models and artefacts, no airframe.
- Zeppelinmuseum Meersburg — same.
- Ballonmuseum Gersthofen — ballooning history; no gas or hot-air envelope
  recorded as a preserved airframe on its own pages.

**Closed**:
- Albatros-Flugmuseum, Flughafen Stuttgart — German Wikipedia's own note is
  "geschlossen".
- Albert Sammt Zeppelin Museum, Niederstetten — closed; held photographs and
  models only.
- Red Stars Museum, Schillerstraße 76, Bensheim (Hessen) — closed. Its former
  collection was substantial and ex-Warsaw Pact (L-39ZO 122, L-410MA 0402, MiG-17F,
  MiG-21UM 23+81, MiG-23UB 20+61, Mi-8T 94+23, Mi-24, TS-11 Iskra 324, Su-20
  6137/20, Mi-2 SP-SAI). Where those airframes went is the single biggest open
  question in this region — see below.
- Sammler & Hobbywelt Collection, Kiesacker 5, 35418 Buseck (Hessen) — "closed, no
  aircraft". Its former collection included Mirage IIIE 499, Mystère IVA 191,
  Fiat G.91R/1 32+58, Fouga CM.170 MT48, three T-33s, F-104F 29+14, MiG-21bis
  24+25, MiG-21MF 91+05, Mi-8T ZS-RUB and Whirlwind XG576. **29+14 is now at
  Eschbach** and is recorded there; the rest are unlocated.

**No public access** — deliberately not recorded as sites:
- F-104G 22+67 (fuselage and tail), privately stored at Rednitzhembach, Bayern.
- F-104G 26+20 cockpit, privately owned at Augsburg.
- F-104G 26+17 cockpit, private collector in Kaiserslautern.
- F-104G 23+27 "KG-101" and F-104G 23+76 "22+90", both sold to unnamed private
  owners in the Stuttgart area / elsewhere in Germany; location unknown.
- F-104G 25+87, "inside a private collection at unknown location".

**Checked and nothing found** (recorded here so the gap is a finding, not an
omission): Heeresflugplatz Fritzlar (Hessen); Heeresflugplatz Niederstetten
(Baden-Württemberg); Flugplatz Aschaffenburg-Großostheim; a "Flugplatzmuseum
Bayreuth" — no such museum is traceable; Spangdahlem, Bitburg, Hahn, Zweibrücken,
Sembach and Pferdsfeld (Rheinland-Pfalz) — no preserved airframe confirmed at any
of them; and **the whole Saarland**, where I could not confirm a single preserved
airframe on public display. The Saarland result should be treated as unproven
rather than proven negative.

**Uncertain, left out**: Museum Flugsicherheit und Rettung, Baden Airpark,
77836 Rheinmünster (a MiG-21 cockpit). aviationmuseum.eu's own note is "We don't
know if the museum is still open". Not recorded rather than recorded wrongly.

---

## Ranked "needs a human on site"

1. **Where did the Red Stars Bensheim collection go?** Ten ex-Warsaw Pact
   airframes, including a Mi-24 and an Su-20, vanished from the record when the
   museum on the Sanner works site closed. Nothing in this region matters more.
2. **Fürstenfeldbruck plinth serials.** Seven airframes recorded with blank tails.
   They are also politically live: the Bund offered them to the town in 2023 and
   the Bundeswehr returns to the site in October 2026 as a training location, so
   they may move. Somebody should read the codes before they do.
3. **Memmingen: is the shelter Starfighter 20+98 or 22+58?** Both registers say
   20+98/"20+05" at Memmingen and 22+58 at Böblingen; the association's own site
   references 22+58. One reading of the nose settles it.
4. **Laupheim HSG 64 serials.** Six helicopters and a Do 27, only the CH-53G
   84+06 identified. Registration in advance is required anyway, so the same visit
   could capture all seven.
5. **Is the 24+11 cockpit at Söllingen or at Brauheck?** The museum lists one;
   the 916-starfighter list puts 24+11's cockpit with TaktLwG 33 at Cochem and its
   tail on 24+38 at Lahr. Recorded once, at Söllingen, with the conflict flagged.
6. Pflumm Schwenningen rotates its display — roughly 40 of ~90 airframes are out
   at a time. The 51 rows here are the published inventory, not a confirmed
   simultaneous sighting.
7. Bad Wildungen-Wega: the Fokker F27 (André Rieu's first aircraft) has no
   published registration, and two further aircraft plus a helicopter are
   mentioned without types.

---

## File and row counts

| file | rows | with tail |
|---|---:|---:|
| `august_euler_flugplatz_museum_aircraft.csv` | 10 | 6 |
| `besucherpark_flughafen_muenchen_aircraft.csv` | 3 | 3 |
| `cf104_denkmal_lahr_aircraft.csv` | 1 | 1 |
| `cf104_denkmal_soellingen_aircraft.csv` | 1 | 1 |
| `curioseum_willingen_aircraft.csv` | 5 | 4 |
| `dd_museum_moedlareuth_aircraft.csv` | 1 | 1 |
| `dt_fahrzeugmuseum_fichtelberg_aircraft.csv` | 10 | 10 |
| `dt_kanadisches_luftwaffenmuseum_aircraft.csv` | 7 | 7 |
| `dt_segelflugmuseum_wasserkuppe_aircraft.csv` | 62 | 50 |
| `f104_denkmal_ummendorf_aircraft.csv` | 1 | 1 |
| `fahrzeugmuseum_marxzell_aircraft.csv` | 3 | 3 |
| `fliegerhorst_buechel_aircraft.csv` | 1 | 1 |
| `fliegerhorst_buechel_torwaechter_aircraft.csv` | 1 | 1 |
| `fliegerhorst_lechfeld_aircraft.csv` | 3 | 3 |
| `fliegerhorst_manching_aircraft.csv` | 5 | 5 |
| `fliegerhorst_roth_aircraft.csv` | 2 | 2 |
| `fliegerhorstmuseum_jg74_neuburg_aircraft.csv` | 7 | 7 |
| `fliegerhorstmuseum_leipheim_aircraft.csv` | 11 | 10 |
| `fliegermuseum_bad_woerishofen_aircraft.csv` | 3 | 1 |
| `flugmuseum_messerschmitt_aircraft.csv` | 10 | 8 |
| `flugpioniermuseum_gustav_weisskopf_aircraft.csv` | 1 | 0 |
| `franks_fahrendes_militaermuseum_aircraft.csv` | 3 | 3 |
| `gerhard_neumann_museum_aircraft.csv` | 11 | 10 |
| `ilm_manfred_pflumm_aircraft.csv` | 51 | 42 |
| `lehrsammlung_tazlw_kaufbeuren_aircraft.csv` | 3 | 2 |
| `luftbrueckendenkmal_frankfurt_aircraft.csv` | 2 | 2 |
| `luftfahrzeugsammlung_bad_wildungen_aircraft.csv` | 2 | 1 |
| `lufthansa_group_hangar_one_aircraft.csv` | 2 | 2 |
| `luftraum_sued_aircraft.csv` | 20 | 20 |
| `memmingen_kaserne_tf104_cockpit_aircraft.csv` | 1 | 1 |
| `mgs_hsg64_laupheim_aircraft.csv` | 6 | 1 |
| `mgs_lechfeld_aircraft.csv` | 4 | 4 |
| `mgs_manching_aircraft.csv` | 1 | 1 |
| `mgs_stetten_am_kalten_markt_aircraft.csv` | 1 | 1 |
| `motorworld_boeblingen_aircraft.csv` | 1 | 1 |
| `muna_museum_marktbergel_aircraft.csv` | 2 | 2 |
| `museum_kiemele_seifertshofen_aircraft.csv` | 19 | 13 |
| `museum_stammheim_aircraft.csv` | 3 | 3 |
| `museum_zivil_wehrtechnik_uffenheim_aircraft.csv` | 1 | 1 |
| `pfalz_flugzeugwerke_speyer_aircraft.csv` | 1 | 1 |
| `point_alpha_rasdorf_aircraft.csv` | 2 | 2 |
| `ramstein_air_base_phantom_aircraft.csv` | 1 | 1 |
| `rolls_royce_museum_oberursel_aircraft.csv` | 2 | 2 |
| `starfighter_denkmal_aich_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_allgaeu_airport_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_brauheck_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_germersheim_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_haldenwang_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_hassfurt_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_neuburg_aircraft.csv` | 1 | 1 |
| `starfighter_denkmal_stuttgart_zuffenhausen_aircraft.csv` | 1 | 1 |
| `tg_fursty_fuerstenfeldbruck_aircraft.csv` | 7 | 0 |
| `tg_jabog34_allgaeu_aircraft.csv` | 3 | 1 |
| `tg_ltg61_penzing_aircraft.csv` | 1 | 1 |
| `traditionsverein_immelmann_eschbach_aircraft.csv` | 1 | 1 |
| `unibw_neubiberg_aircraft.csv` | 1 | 1 |
| `wehrtechnische_studiensammlung_koblenz_aircraft.csv` | 14 | 12 |
| `wiweb_erding_starfighter_aircraft.csv` | 1 | 1 |

**Total: 58 sites, 323 airframes, 266 with a tail number or tactical code (82 %).**
By Land: Bayern 30 sites, Baden-Württemberg 13, Hessen 8, Rheinland-Pfalz 7,
Saarland 0.

---

## Leads for other agents

- **Munich agent (Deutsches Museum / Flugwerft Schleißheim).** F-104G 21+53 moved
  from the Munich Luftfahrthalle to Oberschleißheim in April 2016 and is *not*
  going back; F-104F **29+03** has been in the Munich Luftfahrthalle since June
  2022. F-104G **20+90**'s cockpit is in store at Oberschleißheim. Also: the
  **Deutsches Museum Verkehrszentrum** in Munich holds Bo 105C **D-HDDX** and is
  not covered by anyone in my set.
- **Speyer agent.** The Technik Museum Speyer holds F-104G 22+01 (as "26+63", in
  Vikings colours), F-104G 25+66 (skin partly removed) and TF-104G 28+27 outside
  on stilts. Note that **F-104G 20+46 at the Pfalz-Flugzeugwerke on Speyer
  airfield is a different site** and is in my set, not theirs.
- **Sinsheim agent.** F-104G 22+49, last noted 14 October 2021.
- **Hermeskeil agent.** F-104G 20+43 (last noted 31 July 2021), RF-104G 24+91
  (bare metal, on a wall, very hard to photograph, at 49°41'6.7"N 6°57'37.4"E),
  F-104G 26+61 (lizard camouflage, no markings, in store) and Belgian FX60 with
  the tail of FX65.
- **Eastern agent.** `Grenzmuseum Schifflersgrund`, Platz der Wiedervereinigung 1,
  37318 Asbach-Sickenberg, **Thüringen** — UH-1D D-HAQI, Bo 105M 87+82, Mi-2
  D-HZPH/307, Mi-2RM 386, Mi-8TB 752, **Mi-24V 01**, Alouette II D-HBJA. German
  Wikipedia files it under Hessen; the address is Thuringian. Also F-104G 20+07
  in a private collection near Freiberg, Sachsen.
- **Northern agent.** `Militärgeschichtliche Sammlung Lufttransportgeschwader 62`
  is at Fliegerhorst Wunstorf, Zur Luftbrücke 1, 31515 Wunstorf: Ju 52/3m g4e and
  Do 28 indoors, Noratlas, Piaggio P.149, ex-NVA Mi-8, UH-1D and a walk-through
  Transall C-160D outdoors.
- **Whoever does the national/type sweeps.** `916-starfighter.de`'s German fate
  quicklist (PDF) and `i-f-s.nl`'s "Preserved in Germany" together give a
  near-complete, 2025-current census of every German Starfighter with location and
  false codes. Nothing else I found in this project comes close for a single type.
