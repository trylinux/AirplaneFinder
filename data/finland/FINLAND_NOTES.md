# Finland — research notes
<!-- assembled 10 September 2026 -->

## How this pass was run

Three phases per country, run as parallel research agents: public civilian
museums plus a discovery sweep; military base collections, air parks and gate
guards; standalone monuments — town plinths, airport gate guards, campus and
school airframes, veterans' displays. A single displayed airframe is a site
record here, which is why roadside plinths and shopping-centre aircraft appear
alongside national museums.

Every package was field-count checked, enum-checked against the importer's own
vocabularies, join-checked against its museums file, and diffed serial-by-serial
against every other Nordic package **and** against all 19,409 airframes already
in the live database before anything was written. **Zero `(model, tail_number)`
collisions with the existing database.** The full repo suite (40,352 assertions)
passes.


## Session-level decisions for Finland

**47 sites, 261 airframes imported.**

The museums/bases pass and the monuments pass overlapped at 7 sites; each was
resolved to a single record keeping the institutional name and the union of
airframes. 16 duplicate rows were dropped and **one row was rescued** — Hawk
Mk 51 **HW-338** at Kauppakeskus Tuulonen, which only the monuments pass found,
now sits on the museums pass's site record. Both passes independently caught
the same trap at Lappeenranta: **MiG-21F-13 MG-77 is repainted as "MG-127"
while the real MG-127 is at the same museum** — recorded on true identity with
the painted number in aliases.

**No Hornet is recorded anywhere.** Both passes went looking, because the
2024–26 F/A-18 drawdown is the obvious source of new Finnish monuments, and
neither found a single confirmed plinthed HN- airframe. The only evidence is
the Air Force Museum director publicly expecting several *tolppakoneet*. This
is the highest-yield thing to re-check in 6–12 months.

**Coordinates.** Fifteen Finnish sites were geocoded after import. Four are
airport or airfield reference points, not airframe fixes — Satakunnan Lennosto
(Tampere-Pirkkala), Lapin Lennosto (Rovaniemi), Ilmasotakoulu (Jyväskylä),
Karjalan Lennosto (Kuopio-Rissala) — and WinNova Pori is the Pori airport
reference point. Kauhavan Lentokonepuisto is the Kauppatie 86 street address.
Seven sites were left blank on purpose: Torpin Tykit, Utin Jääkärirykmentti,
the Kouvola and Savo vocational college airframes, Lapland Vocational College
Rovaniemi, and the four service-station / kindergarten / antique-shop-roof
monuments whose sources describe them only as "beside Valtatie 8" or "on the
shop roof".



---

# Phase 1–2: museums and base collections

# Finland — Phase 1 (civilian museums + discovery sweep) and Phase 2 (military base collections / air parks / gate guards)

Compiled 2026-09-10. Database previously held zero Finnish records, so every row here is new.
Scope handled by a **separate** agent: standalone town plinths and campus monuments. Those are listed under EXCLUSIONS below with the reason "other agent" so nothing is silently dropped.

Output: 23 sites, 224 airframes.

---

## 1. Sources and their weight

### Primary / heavy weight

**`ilmailumuseot.fi` — "Suomen Ilmailumuseot / Finnish Aviation Museums"** (Ilmailumuseoyhdistys ry, the Aviation Museum Society).
This is the single best Finnish preserved-aircraft source and it carried the great majority of the serial-level data here. It is a structured product catalogue: every airframe has its own page giving (a) the type history, (b) the individual airframe history, (c) an explicit `Koneen tunnus / Aircraft code` line, and (d) an explicit `Kone on … / The aircraft is …` location-and-condition line, in both Finnish and English. I crawled it exhaustively: 333 airframe pages across 15 category indexes (`id=20170` FAF Museum exhibition, `20171` Hallinportti, `20172` all old military aircraft, `20737` stored, `20738` Finnish Aviation Museum exhibition, `20776` Päijät-Häme, `20825` outside museums, `20827` Karjalan, `21290` still flying, `22009` Karhula, `22278` under restoration, `24986` helicopters, `25534` Kauhava aircraft park, `33435` Kauppakeskus Tuulonen, `60246` Society-owned). The category memberships were used as the authoritative "which museum" signal and the per-airframe text for status.
Blog dates on the site run to July 2026, so the site is actively maintained — but see §2 for a page that is nonetheless stale.

**Museums' own sites**, used for address / hours / access and to cross-check holdings:
`ilmailumuseo.fi` and `uusiilmailumuseo.fi` (Vantaa), `ilmavoimamuseo.fi` (Tikkakoski), `lahdenilmasilta.fi` (Vesivehmaa), `karjalanilmailumuseo.fi` (Lappeenranta), `karhulanilmailukerho.fi/lentomuseo` (Kymi), `ilmatorjuntamuseo.fi` (Tuusula), `caravelle-projekti.fi` (Turku).

**Finavia** newsroom (Turku Caravelle placement, 2024) — operator of the airport where the exhibit stands, so first-hand.

**`visitkauhava.fi` / `kauhava.fi` / Siivet / Jälkipeli** for Kauhavan Lentokonepuisto composition and its street address (Kauppatie 86).

### Medium weight

**Finnish Wikipedia** — used for coordinates (which carry `{{coord}}` templates) and for lead generation. Its aircraft *content* proved stale in two places (see §2), so it was never allowed to override `ilmailumuseot.fi`.
Coordinates taken from fi-wiki `{{coord}}`: Suomen Ilmailumuseo, Suomen Ilmavoimamuseo, Hallinportti, Karjalan Ilmailumuseo, Karhulan Ilmailukerhon Lentomuseo, Merikeskus Vellamo, Museokeskus Vapriikki, Kauppakeskus Tuulonen. Everything else has **blank** coordinates rather than a guessed fix.

**fi.wikipedia "McDonnell Douglas F/A-18 Hornet Suomessa"** — used only to establish that the Hornet drawdown had *not* yet produced any confirmed plinth aircraft (see §5, open question 1).

### Rejected / not used as fact
- **aviationmuseum.eu** — lead generation only, per instruction. Nothing was taken from it.
- **Facebook embeds** on the Karhula club site — undated in the scrape ("7 years ago"), used only to raise an open question about the Gauntlet, not as a fact.

---

## 2. Corrections, and which compilation proved stale

1. **fi.wikipedia `Hallinportin ilmailumuseo` is stale on two airframes.** It still lists **VL Sääski II (LK-1)** as a Hallinportti exhibit while its own following sentence admits the aircraft moved to Merikeskus Vellamo in Kotka in 2007; and it lists **Focke-Wulf Fw 44J (SZ-5)**, which `ilmailumuseot.fi` places in storage in Vaasa. The Hallinportti category index (`id=20171`) contains neither. Recorded: LK-1 at **Merikeskus Vellamo**; SZ-5 (Vaasa) excluded as stored privately with no public presentation. Wikipedia also omits **Karhumäki Karhu 48 (OH-VKK)**, which the museum index does list — that one is recorded.

2. **`ilmailumuseot.fi` is itself stale on the Caravelle.** Its product page for **Sud Aviation SE 210 Caravelle III SE-DAF** still sits in the "under restoration" category (`id=22278`) and still reads *"Kone on kunnostettavana hallissa Pansion telakalla Turussa"* — under restoration in a hall at the Pansio dockyard, Turku — and forward-dates the move as *"kesällä 2023"*. In fact the aircraft was placed on **permanent display beside the Turku Airport terminal in June 2023** and Finavia announced public access in 2024; the Society's own `caravelle-projekti.fi` confirms it is at the airport and open seasonally. This is the one compilation entry that demonstrably lags reality, and it is worth flagging because the same page also strands the **Hietanen HEA-23B OH-XEA**, whose only recorded location is "in the Pansio Caravelle hall, visible until spring 2023" — i.e. an expired statement (see EXCLUSIONS).

3. **Karjalan Ilmailumuseo postcode.** `ilmailumuseot.fi` gives **53600** in the Finnish text and **54600** in the English text of the same page. The museum's own site gives **53600 Lappeenranta**. Recorded 53600.

4. **Suomen Ilmavoimamuseo postcode.** Same page gives **41160** (Finnish) and **41660** (English). Tikkakoski is 41160 and the museum's own site gives 41160. Recorded 41160.

5. **False markings.**
   - **MiG-21F-13 MG-77** at Karjalan Ilmailumuseo has been converted and repainted to *resemble a MiG-21bis wearing the serial "MG-127"*. The real **MG-127** (a genuine MiG-21bis) is **also at the same museum**. Both are recorded, MG-77 with the false serial in aliases and the explanation in the description. Anyone matching on painted marks at Lappeenranta will double-count.
   - **Caravelle SE-DAF** wears **OH-LEA** and the name *Sinilintu*. OH-LEA is not its registration; SE-DAF is. Recorded SE-DAF in `tail_number`, OH-LEA in aliases.
   - **Breguet 14.A2 (3C30)** carries **BR-30** on the wings. `tail_number` = 3C30.
   - **LET L-13 Blanik** at Vantaa wears **"OH-VLK"**, which `ilmailumuseot.fi` itself puts in quotes; it is an ex-DOSAAF airframe. `tail_number` left blank, OH-VLK in aliases.
   - **Focke-Wulf Fw 44J at Karhula** is displayed as **SZ-5**, but its own catalogue entry records the code as `?` while a *different* airframe genuinely coded SZ-5 is stored in Vaasa. `tail_number` left blank; SZ-5 in aliases with the doubt stated.
   - **Saab 35BS DK-208** (Turku Airport, other agent's scope): the site's English "Aircraft code" line says DK-202, the Finnish line and the title say DK-208. The English line is a copy-paste error — DK-202 is the Tikkakoski parade-square aircraft. Same copy-paste error on **DK-211** (English line says DK-201). Flagged for the plinth agent.

6. **Wing/fuselage split airframes counted once each, at the place the part actually is.** The recovered **MiG-3** exists as two separate exhibits: rear fuselage + small parts at the **Ilmatorjuntamuseo** and wings at the **Päijät-Hämeen Ilmailumuseo**. Two rows, one per site, each describing what is present. Neither carries a serial — the catalogue's "code: 1" is not a credible Soviet serial and was **not** used.

7. **Museum name history.** The Tikkakoski museum was *Keski-Suomen Ilmailumuseo* until 1 January 2016 and is now **Suomen Ilmavoimamuseo** (Finnish Air Force Museum). The starting-point brief listed both as if separate; they are one site. Likewise "Suomen Ilmavoimien museo" is the same place. One record.

8. **"Turun lentokonemuseo" does not exist** as a museum. The aviation presence at Turku is the Caravelle exhibit at the airport (recorded) plus the Society's restoration hall at Pansio (not a public museum). Recorded as `Caravelle-näyttely Turun lentoasema`.

---

## 3. Judgment calls

- **Display vs. derelict vs. instructional.** The test applied was deliberate retention *plus* public presentation. Finland has a large population of ex-Air Force airframes handed to vocational colleges as `opetusväline` (teaching aid) — Tredu (Tampere/Pirkkala), WinNova (Pori), Savon koulutuskuntayhtymä, Kouvolan seudun ammattiopisto, Lapin ammattiopisto. These are working training rigs in workshops, not exhibits, and are all excluded. Same for the **Pelastusopisto** rescue-training MiG-21bis MG-125 in Kuopio and the two Drakens (DK-229, DK-263) used as targets on the **Taipalsaari** range — deliberate retention, yes; presentation, no.
- **Storage inside a museum counts.** Where the catalogue says an airframe is `varastoituna` at a named museum, it is recorded at that museum with `display_status = in_storage`. Museum reserve collections are part of the site.
- **Wreck recoveries and composites.** Finland's collections are unusually full of salvaged airframes. These are recorded as real airframes with the condition stated in the description rather than being dropped: Brewster 239 **BW-372** (lake recovery, conserved not restored — the only Brewster 239 in the world), Bf 109F-4 **NE+MH** (wreck, German factory code is the only identity), Bf 109G-2 **MT-208** (front fuselage only), VL Myrsky II **MY-5** and **MY-9** (steel-tube frames), VL Pyry **PY-5** and **PY-26**, Fokker C.X **FK-113/FK-115**, SB-2 rear fuselages, Il-2M3 wings only, Polikarpov I-15bis. Where only a nose or cockpit survives (MiG-21bis MG-136, Draken DK-233, Saab 35A simulator nose, MiG-21bis MG-134, Vampire VT-6) that is stated.
- **Replicas.** Recorded, and labelled as replicas in the description: **Thulin Typ D "F1"** (Suomen Ilmavoimamuseo), **Nieuport 17 "1.D.453"** (Karjalan Ilmailumuseo). Mignet HM-14 **OH-BFA** is described by the museum as "a replica or more accurately the last Flying Flea built in Finland" — recorded as an airframe with that nuance in the description.
- **Commercial sites that are nevertheless real heritage displays.** Included: **Kauppakeskus Tuulonen** (five genuine ex-service airframes including the Sotamuseo's DC-2 *Hanssin-Jukka* in a purpose-built glazed hangar, a Draken, a MiG-21bis, an Mi-8P and a suspended Fw 44J — this is a curated collection that happens to sit at a shopping centre); **Verkkokauppa.com Jätkäsaari** (MiG-21bis MG-130 on a public rooftop viewing terrace); **PowerPark** (An-24B gate guard). Excluded as advertising props rather than presentation: helicopters repainted into a fuel-chain's livery in service-station yards (Mi-2 at Hyrynsalmi, Ka-26 at Revonlahti), the Aztec on a service-station forecourt at Pirkkala, the AA-5 at Crazyland Nivala, the Mi-8T at ABC Rantinhovi, the TS-11 Iskra outside an ABC at Pyhtää, the Jet Ranger OH-HRD on an antique shop roof in Tuusula, and the **Viri replica** inside the K-Citymarket at Seppälänkangas, Jyväskylä (single replica used as store decor). The line drawn: does the object exist to be *looked at as an aircraft*, or to point at a shop?
- **Kauhavan Lentokonepuisto is treated as an air park (Phase 2), not seven separate plinths.** It is a single named, municipally-established site in the town centre (Kauppatie 86) consisting of two glazed display cabinets and two plinth-mounted aircraft, created by the City of Kauhava and Lentosotakoulun Kilta. Its seven airframes are recorded under it. **FM-21 and FM-82**, described only as "muistomerkkinä Kauhavalla", are *not* part of the park's seven and are left to the plinth agent.
- **Base sites use `access_type = restricted`.** Karjalan Lennosto (Rissala), Satakunnan Lennosto (Pirkkala), Lapin Lennosto (Rovaniemi), Ilmasotakoulu Tikkakoski and Utin Jääkärirykmentti are closed garrisons; a member of the public gets in on an open-day or not at all. Patria Halli likewise (factory site).
- **Museum with seasonal-only hours is still `public`** (Päijät-Häme, Karjalan, Karhula, Caravelle) — a member of the public buys a ticket and walks in during the season. `appointment` was used only for **Torpin Tykit**, whose access could not be confirmed as scheduled walk-in.

---

## 4. Deliberate blanks

- **Coordinates** are blank for 15 of 23 sites. No coordinate was derived from an address, a town centroid or an airport reference point. Turku Airport's own `{{coord}}` exists but points at the aerodrome reference, not at the Caravelle beside the terminal, so it was not used.
- **`year_built` is blank on all but three rows** (Fokker F27 FF-1 = 1965; Mi-8T CCCP-25267 = 1968). Finnish sources overwhelmingly give first-flight and delivery dates for the *type*, and service dates for the individual, but not construction year. No serial was ever converted into a year.
- **`tail_number` blank** where the source records `-`, `?` or an implausible code: Adaridi AD 3, Blomqvist & Nyberg, Kyrölä, Saab 35A simulator nose, P-39Q Airacobra, MiG-3 (both parts), Fokker C.V (unidentified), Arado Ar 66c, SB-2bis, second Caudron G.3, Po-2, Ka-6E fuselage, Polikarpov I-15bis, Karhula's Fw 44J and its gliders, IVL K.1 Kurki, the Suomala light helicopter and the Harakka-family primary gliders at Karhula.
- **Street address blank** for Uudenkaupungin Automuseo, Kauppakeskus Tuulonen, Torpin Tykit, PowerPark, Patria Halli and the five military sites — not verified to street level from a first-hand source.
- **Karhula glider registrations** are blank. The club's own site names the types (Bocian, PIK-5c, K-8b, Ka-6CR, Utu, Harakka I, Muna-Harakka, Moottori-Harakka) without registrations, and `ilmailumuseot.fi` does not index them. Types alone keep the rows distinguishable.

---

## 5. EXCLUSIONS with reasons

**Outside Finland** (Finnish airframes, foreign sites — for another country's sweep):
Caudron-Renault C.R.714 **CA-556** → Muzeum Lotnictwa Polskiego, Kraków. BAe Hawk Mk.51 **HW-326** → Estonian Aviation Museum, Veskiorg.

**Other agent (standalone town plinths, airport/campus monuments):**
Fouga FM-21 and FM-82 (Kauhava, outside the park); Gnat GN-110 (Someronharju, Rovaniemi); Draken DK-201 (Halli centre), DK-203 (Kittilä airport), DK-208 (Turku airport), DK-219 (Pudasjärvi airfield); Vampire VA-7 (Koskue village, Jalasjärvi); VL Viima I VI-1 (display cabinet, Valmetinkatu/Lentovarikonkatu, Tampere); Piper PA-28 OH-PKV (Jämi Areena, Jämijärvi).

**Instructional airframes, not exhibits:** Fokker F27 FF-2 and FF-3, Redigo RG-4, Learjet 24D N311LJ, Piper PA-28R PA-3 (all WinNova, Pori); Redigo RG-5 and RG-7, Falcon 20F, Hawk HW-336, Piper PA-31P OH-PHR, Piper PA-31-350 PC-6 (Tredu, Tampere/Pirkkala); Redigo RG-8, Cessna 402B OH-CHS, Fouga FM-33 nose (Savon koulutuskuntayhtymä); Mi-8T HS-3 and AB 206 OH-HRG (Kouvola); Redigo RG-10 (Lapin ammattiopisto); Mi-8T HS-2 (Karjalan Prikaati, Vekaranjärvi); MiG-21bis MG-129 (Karjalan Lennosto teaching aid — the wing's *memorial* MG-119 and presentation cockpit MG-134 are included, the workshop trainer is not).

**Targets / consumed:** Draken DK-229 and DK-263 (Taipalsaari range); MiG-21bis MG-125 (Pelastusopisto, Kuopio).

**Private ownership with no public presentation:** Fouga FM-4 (Porin Ilmasilta store), FM-16 (Ruotsinpyhtää), FM-37, FM-51, FM-78; Draken DK-209 (moved to a private Central Finland collection on 13 May 2025); Gnat GN-113 (stored at Malmi); MiG-21R "2097" (private, Riihimäki); MiG-21MF "8003" (for sale, Alajärvi); MiG-17/Lim-5 1C-1505 (Iitti); Su-25 "49" and MiG-23MLD "35" cockpits stored at Tampere-Pirkkala; An-2 RA-70171 and Ka-26 RA-24349 (Sipoo); An-2 HA-MDO (summer house, Lempäälä); Saab 340B YL-RAF (being converted into a hotel at Uurainen); VL Myrsky MY-10 frame (Seinäjoki); Fw 44J SZ-5 (stored, Vaasa); Klemm OH-ILL (restoration, Ilmajoki); Alouette II OH-HIS (restoration, Turku); Schleicher Ka-7 OH-KKH (restoration, place unstated); VL Viima OH-VIE, DH.82A OH-ELC, VL Myrsky MY-14 (restorations, place unstated); all airworthy privately-flown types in the site's "flying old aircraft" category.

**Advertising props / decor:** Mi-2 (Hyrynsalmi service station), Ka-26 (Revonlahti, hwy 8), Mi-8T RA-25525 (ABC Rantinhovi, Suomenniemi), Piper PA-23-250 marked "OH-ABC" (Pirkkala service station), AA-5 OH-AYN (Crazyland, Nivala), AB 206 OH-HRD (antique shop roof, Tuusula), TS-11 Iskra "610" (Pyhtää ABC), Viri replica OH-IIK (K-Citymarket Jyväskylä), Mignet HM-14 fuselage (Kurikka kindergarten play equipment), Reims/Cessna F150J OH-CBQ (sold in 2016 for use as a film prop).

**No fixed location:** **Hawk-elämyskeskus / Hawk Experience Center** with **BAe Hawk Mk.51 HW-314** (7.6 m cockpit section). This is the Aviation Museum Society's *transportable exhibition container*, shown at fairs and airshows to its own schedule. It has no address, so it is not a site. Recorded here rather than in the data.

**Reserved but not yet installed** (nothing to record until unveiled): Hawk **HW-301** earmarked as a monument for Air Force Command at Tikkakoski; **HW-304** earmarked for the Suomen Ilmavoimamuseo; **HW-306** earmarked for the Karhula museum. Douglas C-47 **DO-5** — catalogue says only "stored", with no location, so it was dropped rather than guessed at.

**Expired statement, current location unknown:** Hietanen HEA-23B **OH-XEA** — last recorded as visible in the Pansio Caravelle hall "until spring 2023". The Caravelle has since left Pansio. Not recorded.

**Checked and found to hold no aircraft:** Panssarimuseo (Parola), Sotamuseo / Suomenlinna, Räyskälä (no gliding museum found), Tekniikan museo. Also swept without result: Forssa, Immola, Menkijärvi, Nummela, Oulu, Vaasa, Joensuu, Mikkeli.

---

## 6. Open questions, ranked

1. **Hornet plinths (highest value, most time-critical).** The F/A-18 drawdown began with HN-401 retiring to Halli on 26 April 2024, and the Air Force Museum's director publicly expected "a few" Hornets to end up as *tolppakoneet* (pole aircraft) like the Draken and Friendship at Pirkkala's gate. As of this sweep **no unveiled Hornet monument or museum Hornet could be confirmed anywhere in Finland** — no ilmavoimat.fi announcement, no entry on `ilmailumuseot.fi`. Zero Hornet rows are recorded. This will change, probably at Pirkkala, Rissala, Rovaniemi and Tikkakoski, and should be re-checked every few months.
2. **Gloster Gauntlet II GL-400 — where is it actually?** `ilmailumuseot.fi` places it on display at Karhula in airworthy condition. The Karhula club's own page carries an undated notice that the Gauntlet was moving to **Räyskälä** on 31 August for re-covering of the wings and an engine change from an Alvis Leonides supplied by the Air Force Museum. This is the only surviving Gauntlet in the world, so its location matters. Recorded at Karhula with the doubt in the description; needs eyes-on confirmation.
3. **Thulin Typ D "F3" — Vantaa or Tikkakoski?** The airframe page says stored at the **Suomen Ilmailumuseo** (Finnish, unambiguous: *"varastoituna Suomen Ilmailumuseossa"*), but the same site's Air Force Museum *exhibition* index lists it. Recorded at Vantaa, in storage. One of the two placements is wrong.
4. **Bf 109G-6 MT-507 — on the floor or in conservation?** The Tikkakoski museum's own site notes the Messerschmitt has "recently been transferred to the museum's conservation facilities" for maintenance. Recorded `on_display` because that is its exhibition status, but it may be physically off the floor right now; if a snapshot-accurate status is wanted this should be re-checked.
5. **Hallinportti Ilmailumuseo opening regime.** The aggregator's English text is frozen at a 2015/2016 season and the Finnish text gives June–July daily hours "otherwise by appointment"; the museum has also been the subject of volunteer renovation appeals. It sits beside a working military airfield at Halli. Recorded `public`, but whether it is reliably open in 2026 — and whether access is now conditional on the Patria/Air Force area — is unresolved.

Lower-priority residue: exact street addresses and coordinates for the 15 sites left blank; registrations for the eight Karhula gliders; whether **Karjalan Ilmailumuseo's An-2 RA-70623** has been assembled and put on display since the catalogue entry was written; and confirmation that the **Saab 91D SF-5** is still in the Uusikaupunki car museum.


---

# Phase 3: monuments and plinths

# Finland — Phase 3 (standalone monuments, plinthed aircraft, campus and roadside airframes)

**Result: 31 sites, 53 airframes.** Database previously held zero Finnish records.

---

## 1. Sources and weight

| Source | Weight | Use |
|---|---|---|
| **ilmailumuseot.fi** (Ilmailumuseoyhdistys ry / Aviation Museum Society, Finland) — category *"Vanhat lentokoneet museoiden ulkopuolella / Old Aircraft Around Finland"* (id 20825) and *"Kauhavan lentokonepuisto"* (id 25534), *"Kauppakeskus Tuulonen"* (id 33435) | **Highest.** This is the national inventory of preserved airframes and it explicitly separates museum from non-museum holdings. Bilingual FI/EN, per-airframe pages, current. | Primary spine. All 88 non-museum entries were fetched individually and read. |
| **fi.wikipedia** — *Suomen ilmavoimien Saab J35 Drakenit* (full per-airframe fate list with c/n, first/last flight, pilot), *Mikojan-Gurevitš MiG-21 Suomessa*, *De Havilland Vampire*, *Saab 91 Safir*, *Folland Gnat* | High for serials, dates and fates; the Draken article is unusually well sourced (Laukkanen 2006, Apali). | Cross-check and enrichment (first/last flight dates, nicknames, c/n). |
| **OpenStreetMap via Overpass** (`historic=aircraft`, name searches) | High for coordinates — these are surveyed objects, several tagged with the serial. | 14 of 31 site coordinates. |
| **Nominatim** geocoding | Medium. Used only for named POIs (PowerPark, Crazyland, K-Citymarket, Pelastusopisto, Kittilä Airport, street addresses). | Remaining coordinates. |
| lentoposti.fi, Yle, Hämeen Sanomat, siivet.fi, lentosotakoulunkilta.fi, tuulonen.fi, caravelle-projekti.fi | Medium-high, dated news reporting. | Unveiling dates, display method (plinth vs. vitrine vs. pole), true-identity questions. |
| aviagraphers.net | Low. Thin and partly wrong (see corrections). | Lead generation only. |
| aviationmuseum.eu | Lead generation only, per brief. Not cited for any field. | — |

Everything was searched in Finnish first: *lentokone jalustalla, muistomerkkinä, porttivartija, lentokonemuistomerkki, patsas, näytteillä, opetusvälineenä, lentokonepuisto*, plus town + type names.

---

## 2. Corrections made, with evidence

- **Draken at Kauppakeskus Tuulonen is DK-247, not DK-249.** aviagraphers.net says "SAAB J-35FS DK-249 ... Tuulonen shopping centre". Both fi.wikipedia (citing Laukkanen 2006 p.166 and the Hanssin-Jukan Perinneyhdistys unveiling record of 20.9.2016) and ilmailumuseot.fi give **DK-247**. DK-249 is separately recorded as stored at Halli in the military area. Corrected to DK-247.
- **MiG-21bis MG-114 is NOT at WinNova Pori.** fi.wikipedia still says "Porissa lentokoneasentajakoulutuksen käytössä (Winnova)". ilmailumuseot.fi's current per-airframe page says it is on show at the **Torpin Tykit** military museum in Inkoo. Torpin Tykit is a museum, so MG-114 is excluded from Phase 3 entirely and handed to Phase 1. The Wikipedia line is stale.
- **Two separate Fouga monuments at Kauhava, not one.** ilmailumuseot.fi says only "FM-21 muistomerkkinä Kauhavalla" and "FM-82 muistomerkkinä Kauhavalla", which reads as one site. OSM has two distinct objects: `Fouga Magister (FM-21) -muistomerkki` at 63.11341 / 23.04090 (the former Air Force Academy heritage square, unveiled 15.8.1986, restored 2020) and a `Fouga Magister` memorial at 63.10250 / 23.05819 inside Lentokonepuisto (Kauppatie 86), which lentoposti and jalkipeli identify as **FM-12**, pole-mounted July 2018. Two site records.
- **Caravelle true identity is SE-DAF, not OH-LEA.** It wears 1963 Finnair colours and the name *Sinilintu* with registration OH-LEA, but caravelle-projekti.fi states plainly it is the ex-SAS SE-DAF stored at Arlanda since 1974 and acquired from SMTM in February 2021. OH-LEA and Sinilintu are in `aliases`; `tail_number` is SE-DAF.
- **Vampire "VA-7" is a false serial and gets a blank tail_number.** fi.wikipedia is explicit: the airframe never flew in Finland, was an ex-Swedish Air Force **J 28B** (DH.100 Vampire FB Mk.50) bought as a Lentosotakoulu ground instructional airframe, and was marked "VA-7" afterwards. The real Swedish serial is not stated in any source I found, so `tail_number` is blank and `VA-7;J 28B` are aliases. Blank beats a guess.
- **Aztec at ABC Pirkkala wears an invented registration.** ilmailumuseot.fi says the aircraft "on saanut epävirallisen rekisteritunnuksen OH-ABC". True identity OH-PPS (ex N6744Y, N612RS) in `tail_number`; OH-ABC in `aliases`.
- **DK-208 is a Saab 35BS, not a 35S.** fi.wikipedia's per-airframe list and ilmailumuseot both class DK-208 (ex-Swedish J 35B, ferried 29.5.1972) as BS. Variant set accordingly; DK-201/203/211/219 are S, DK-247 is FS.
- **DK-209 removed from Tredu in 2025.** fi.wikipedia, citing an ilmailumuseot news item, records that DK-209 served as a Tredu instructional airframe until **13 May 2025**, when it went to a private collection in Central Finland. It is therefore *not* included at Tredu Pirkkala. This is exactly the kind of currency change the brief warned about.

---

## 3. Judgment calls

- **Vocational-college airframes are included as sites.** The brief names "school/technical-college/university/polytechnic campus airframes" and "vocational aviation schools" as in scope. WinNova (Pori), Tredu (Pirkkala and Tampere), Savo Consortium (Kuopio), KSAO (Kouvola) and REDU (Rovaniemi) each get one site record, with `access_type=appointment` because these are working workshops behind a school gate, not roadside displays.
- **Tredu is split into two sites** because ilmailumuseot consistently distinguishes "Tredulla Tampereella" (RG-5, RG-7) from "Tredussa Pirkkalassa" (HW-336, OH-PHR, PC-1, Falcon 20F). Tredu's aviation programme is at Myötätuuli 71, Pirkkala; the Tampere-tagged Redigos may in fact sit at the same campus. Merge candidate — flagged as open question 4.
- **DK-211 at the Lapland Wing main gate IS included** although the wing is active. It is a roadside gate guard at a joint civil/military airport, publicly viewable, and is the classic "gate guard" category the brief calls for — not a base air park. `access_type=public`. **If Phase 2 also captures it, dedupe in favour of whichever record has the better coordinate; mine is blank.**
- **The Emergency Services College MiG-21 (MG-125) is included** even though it is a rescue-training hulk rather than a monument, because it is a campus airframe on a college site, which is squarely in scope. `display_status=on_display` is generous; it is a working training object.
- **Kauppakeskus Tuulonen is treated as one Phase 3 site**, covering the four outdoor airframes (MG-124, DK-247, HW-338, HS-6) plus the Fw 44J SZ-18 suspended inside the mall. The site also hosts the **Hanssin-Jukka hangar** containing a DC-2 (DO-1) and the Hanssin-Jukka replica; that hangar is a museum and its two aircraft are excluded here and handed to Phase 1.
- **Glass-vitrine displays count as plinthed aircraft.** Kauhava's Lentokonepuisto, the VL Viima VI-1 vitrine at Valmetinkatu in Tampere and the Patria Redigo vitrine at Halli are all standalone display cabinets in public or semi-public space, not museums.
- **Kauhava Lentokonepuisto is not a museum.** It is a 250 m strip of the town centre at Kauppatie 86 established by the City of Kauhava and Lentosotakoulun kilta, with two vitrines and two plinthed aircraft. It has no building, staff or collection function. Phase 3.
- **`year_built` is blank on every row.** Not one source gave a construction year, and a serial or a first-flight date is not a build year. 53 deliberate blanks rather than 53 guesses.

---

## 4. EXCLUSIONS, with reasons

### On active military installations — hand to Phase 2, not Phase 3
| Airframe | Location | Note |
|---|---|---|
| MiG-21bis MG-119 | Karjalan Lennosto parade square, Rissala | Monument inside the base. OSM 62.99819 / 27.79503. |
| MiG-21bis MG-129 | Karjalan Lennosto, Rissala | Taxiable instructional airframe, still Air Force property. |
| MiG-21bis MG-134 | Karjalan Lennosto | Cockpit only, mounted in a truck trailer and toured to public events. Mobile, not a site. |
| Saab 35BS DK-202 | Ilmasotakoulu parade ground, Tikkakoski | OSM 62.39950 / 25.60182, Upseerikatu. |
| Saab 35FS DK-237 | Satakunnan Lennosto, near the mess, Pirkkala | Erected 15.7.1998, military area. |
| Fokker F27 FF-1 | Military area at Pirkkala | Monument but inside the perimeter. |
| Saab 35FS DK-229, DK-263 | Taipalsaari firing range | Range targets/practice hulks. |
| Mil Mi-8T HS-2 | Karjalan Prikaati, Vekaranjärvi | Army instructional airframe. |
| Bf 109G-6 MT-452 | Vitrine at Utti garrison | A genuine standalone monument vitrine, but inside a garrison. Borderline — reconsider if Phase 2 does not pick it up. |
| Saab 35FS DK-245, DK-249, DK-251, DK-265 | Stored at Halli, military area | Stored, not displayed. |

### Inside museums — Phase 1
Gnat GN-103 and MiG-21bis MG-127 and MiG-21UM MK-106 and Draken DK-213 and Safir SF-31 (Karjalan ilmailumuseo, Lappeenranta); Gnat GN-101/GN-104, MiG-21F-13 MG-92, MiG-21U MK-103, MiG-21UM MK-105/MK-126, MiG-21bis MG-138, Draken DK-223/DK-241/DK-270, Vampire VT-8, DC-2 DO-3 (Suomen Ilmavoimamuseo, Tikkakoski); MiG-21bis MG-135, Draken DK-206/DK-262, Vampire VA-2/VT-9 (Suomen ilmailumuseo, Vantaa); MiG-21F-13 MG-78, MiG-21bis MG-116, Draken DK-259 (Karhulan ilmailukerhon lentomuseo, Kymi); MiG-21bis MG-131/MG-140, Draken DK-207, Vampire VA-3/VT-6 (Päijät-Hämeen ilmailumuseo, Vesivehmaa); **MiG-21bis MG-114 and Mi-8T CCCP-25267 (Torpin Tykit, Inkoo)**; Safir SF-5 (Uudenkaupungin automuseo); Safir SF-34/SF-36 (Woikosken automuseo); VL Sääski LK-1 and DHC-2 OH-MVM (Merikeskus Vellamo, Kotka); Mignet HM-14 OH-KAA (Vapriikki, Tampere); RC-3 Seabee OH-EGA (Lusto, Punkaharju); P-39Q (Ilmatorjuntamuseo, Tuusula); Hawk HW-326 (Estonian Aviation Museum — outside Finland); C.R.714 CA-556 (Kraków, Poland).

### Scrapped, removed or gone
- **Drakens scrapped:** DK-204, DK-210, DK-212, DK-261 (June 1997); DK-264 (May 1999); DK-205, DK-215, DK-217, DK-225, DK-227, DK-235, DK-239, DK-243, DK-253, DK-266, DK-268 (August 2001); DK-257, DK-267. DK-206A scrapped at Ähtäri August 2002.
- **MiG-21F-13 decoys:** most surviving F-13s were converted into MiG-21bis decoys and scrapped in the late 1990s. Only MG-32, MG-35 and MG-77 escaped, all to museum/instructional use.
- **Draken DK-209** — left Tredu 13.5.2025 for a private collection in Central Finland. No public display known.
- **Draken DK-221** — fire-training airframe at Rissala. **DK-269** — fire training, Tikkakoski. **DK-263** — fire training, Satakunnan Lennosto. Consumable hulks, not displays.

### In scope by type but excluded as private property / storage, not display
- **An-2 HA-MDO** used as a summer cabin at Lempäälä (OSM 61.29557 / 23.77223, Koivuniementie). A dwelling, not a display.
- **An-2 RA-70171** and **Ka-26 RA-24349**, privately owned at Sipoo. **MiG-17 (Lim-5) 1C-1505**, privately owned at Iitti. **MiG-21R "2097"**, private collection at Riihimäki. **VL Myrsky MY-10** wreck, private, Seinäjoki. **Fouga FM-37 (OH-FMA)** airworthy and **FM-51 (OH-FMM)** under repair, private. **Fouga FM-4**, stored by Porin Ilmasilta.
- **PZL TS-11 Iskra "610"**, Pyhtää — ilmailumuseot describes it as privately owned and *stored outdoors* near an ABC station, not displayed. Borderline; see open question 5.
- **Fouga FM-16** at Helsinki-East Aerodrome (Redstone AERP), Ruotsinpyhtää — "on the airfield" with no indication it is a monument, a plinth or a display. See open question 5.
- **Reims/Cessna F150J OH-CBQ** — intended as a film prop. No fixed display location.
- **Schleicher Ka-7 OH-KKH** — under restoration, no location given.
- **Cessna U206** — itinerant, "displayed in various places around Finland since spring 2016". No fixed site.

### Monuments with no airframe
- **Vampire jet-age memorial, Pori Airport** — a 3 m Kuru granite sculpture by Marko Tienhaara unveiled 22.1.2013 by Satakunnan Lennoston kilta, marking the first Vampire landing on 22.1.1953. It carries a Vampire silhouette but is a stone monument, not an aircraft. Excluded from an aircraft database; worth a note if the schema ever admits non-airframe memorials.
- **Junkers JK-263 forced-landing memorial, Lentokonejänkä, Rovaniemi**, and the **Meltaus crash-victims memorial** (66.50052 / 25.745109). Crash-site markers, no airframe.

---

## 5. Deliberate blanks

- **`year_built` — blank on all 53 rows.** No source gave one. Finnish serials (MG-, DK-, FM-, GN-, VA-, HW-, VN-, HS-, PY-, VI-, SZ-, SF-, RG-, PC-, FF-) are sequence numbers, never years, and were not repurposed.
- **`tail_number` blank on 4 rows,** each distinguishable by manufacturer + model + museum_name: the Koskue Vampire (true identity unknown, wears false VA-7), the Hyrynsalmi Mi-2, the Revonlahti Ka-26 and the Kurikka kindergarten HM-14. For the last three, ilmailumuseot records "Koneen tunnus: -" outright.
- **Coordinates blank on 10 sites.** Left blank rather than fabricated wherever I had only a municipality name and no mappable POI: WinNova Pori, Tredu Tampere, Savo Consortium Kuopio, KSAO Kouvola, REDU Rovaniemi, ABC Pirkkala, Revonlahti service station, ABC Rantinhovi Suomenniemi, the Tuusula antique shop, the Kurikka kindergarten, and the DK-211 gate at Rovaniemi.
- **Coordinates I *did* use that are coarser than a plinth fix, flagged:** Halli (61.86131 / 24.82839 is the village centroid — the monument is "in the centre of Halli"), Kittilä (67.70037 / 24.84983 is the terminal geocode — the monument is "at the terminal"), Koskue (62.35984 / 22.84494 is the village centroid).
- **`postal_code` populated on only 8 sites** — the ones with a confirmed street address or a known institutional address.
- **`aircraft_name` populated on one row only** (Caravelle *Sinilintu*). Draken service nicknames (Kake, Jussi, Mikko, Kari, Vihtori, Hantta, Kreivi von Rosen) are pilot-assignment names painted on the airframe in service, not display names, so they went into `aliases` where the airframe is a record here (DK-201 Kake, DK-208 Jussi) and were dropped otherwise. Rysky, the Pudasjärvi Draken's local name, is in aliases.

---

## 6. Open questions, ranked

1. **Where is Saab 35FS DK-255?** fi.wikipedia (citing Laukkanen 2006 p.170) records it as "näyttelykoneena Lentosotakoulussa Kauhavalla" — a display aircraft at the Air Force Academy at Kauhava. But Lentosotakoulu was disbanded and Kauhava garrison closed at the start of 2015, DK-255 does **not** appear in ilmailumuseot's non-museum inventory, and it is **not** among the seven aircraft in Kauhava Lentokonepuisto. It is either at Hallinportti Ilmailumuseo, moved with the school to Tikkakoski, or scrapped. This is the single most likely missing Phase 3 record. Resolve via Hallinportti's object list and Lentosotakoulun kilta.

2. **Will the Hornet drawdown produce plinthed HN- airframes, and has any been erected yet?** No confirmed F/A-18 monument exists as of this research. The only forward-looking source is Finnish Air Force Museum director Kai Mecklin, quoted on fi.wikipedia, predicting that "a few of the Hornets will end up as so-called tolppakoneet (pole aircraft), like the Saab Draken and the Fokker Friendship at the Satakunta Wing gate at Pirkkala". The rest of the fleet is expected to be scrapped, with the US export licence restricting onward transfer. **This will need re-checking within 6–12 months** — it is the most likely source of *new* Finnish Phase 3 records.

3. **What is the unidentified aircraft at 63.11598 / 21.75805, Kivijärventie, Pilvilampi, Vaasa?** An OSM node tagged `historic=aircraft` with `source=orthophoto` and no name, type, operator or serial. It appears in no Finnish inventory I searched. Somebody traced an airframe off aerial imagery near Vaasa and never identified it. Needs street-level or satellite verification and a type identification. Vaasa is one of the towns the brief flagged and this is the only lead there.

4. **Are the Tredu Tampere and Tredu Pirkkala airframes actually one site?** ilmailumuseot places RG-5 and RG-7 "Tredulla Tampereella" and HW-336, OH-PHR, PC-1 and the Falcon 20F "Tredussa Pirkkalassa". Tredu's whole aviation programme runs from Myötätuuli 71, Pirkkala. The Tampere attribution may be a legacy of Tredu's old Hervanta premises or simply loose usage of "Tampere" for the region. If they are one site, sites 15 and 16 merge and two airframes move.

5. **Are Fouga FM-16 (Ruotsinpyhtää / Helsinki-East Aerodrome) and PZL TS-11 Iskra "610" (Pyhtää) displayed or merely parked?** Both are described only as "located at" / "stored outdoors near" and both are at or beside an aerodrome, which is exactly the brief's "aircraft outside flying clubs" category. If either is on a plinth or gate-mounted, it is a missing site record. Both are in the same corner of eastern Uusimaa and could be settled with one field visit or one good dated photo.

6. Minor, but each blocks a clean record: the **VN-6 vs VN-9** discrepancy for the Kauhava vitrine Vinka (lentoposti names both, ilmailumuseot names only VN-9); the **PC-1 vs PC-6** contradiction for the Tredu Chieftain (ilmailumuseot's own page title says PC-6 while its identity line says "PC-1, OH-PAV"); the identity of **which of the seven registrations on the Tredu Falcon 20F is current** (N569D assumed as first-listed); and the exact street address of the **Tuusula antique shop** with the AB 206A OH-HRD on its roof.
