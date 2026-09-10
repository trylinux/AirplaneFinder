# Denmark — research notes
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


## Session-level decisions for Denmark

**24 sites, 147 airframes imported.** Greenland and the Faroe Islands produced
**zero** records: every Greenland entry found was a crash site, and Narsarsuaq's
Bluie West One museum displays no aircraft.

One row was repaired at build time. The **ST-25 at Danmarks Tekniske Museum**
came back with no manufacturer; it is a **General Aircraft Monospar ST-25,
OY-DAZ, c/n 95**, confirmed against the Danish civil aircraft register
(oy-reg.dk). Recorded with that attribution rather than dropped.

The **Værløse dispersal** was handled as instructed: Hangar 2 carries only the
seven airframes its own 2026 site claims, and the five that a 2020 snapshot
attributes there are traced individually to Helsingør, Stauning, Karup, or
removal.

**The F-16 fleet was retired 18 January 2026** and museum and gate-guard
allocations are still settling. Only E-174, E-176 and E-177 are recorded. New
Danish monument sites are being created right now; this needs a re-check inside
a year.



---

# Research pass

# Denmark (+ Greenland, Faroe Islands) — preserved and displayed aircraft
Research notes, 2026-09-10. Database previously held zero Danish records; all 24 sites / 147 airframes are new.

## 1. Sources and their weight

**Tier 1 — museum's own current site (2025–2026 content). Overrides everything.**
- `historiskhangar.dk` (Værløse Flyhistoriske Hangar / Hangar 2). Page "Hvad kan du opleve i hangaren" plus 2026 news posts. Definitive for the Hangar 2 inventory.
- `flymuseum.dk` (Danmarks Flymuseum, Stauning). Wix site; the per-aircraft pages are dynamic and the registrations do **not** appear in the served HTML, but the **URL slugs** carry identities (`lockheed-t-33a-"t-bird",-dt-884`, `lockheed-t-33a-"t-bird",-dt-102`, `saab-rf-35-draken-(a-109)`). Address confirmed as Lufthavnsvej 1, 6900 Skjern from `besoegsinformation`.
- `tekniskmuseum.dk`, `forsvarsmuseum.dk`, `egholmmuseum.dk`, `langelandsfortet.dk` — used for addresses and existence, not for serials (none publish inventories).

**Tier 2 — `spottingmode.com/wro` (Wrecks & Relics Online).** 61 Danish locations, 228 linked airframes, each location carrying a *dated* last-update and a coordinate. This is the backbone of the dataset: it is the only source that is both comprehensive and dated. Fetched with `curl --ciphers "DEFAULT:@SECLEVEL=0"` as instructed. Per-location plane counts in the country table match the plane list exactly (Stauning 59, Helsingør 28, Aalborg museum 7, Hangar 2 twelve) — that consistency was used as a completeness check (see §3 Aalborg).

**Tier 3 — `da.wikipedia.org/wiki/F-35_Draken`.** Unusually well maintained and actively updated; the best single tracker for Danish Draken fates and the source that caught three stale compilations. Its A-002/A-005 assignment is nevertheless wrong (see §3).

**Tier 4 — `flyhis.dk` (Flyvevåbnets Historiske Samling), specifically the legacy image-map index `Hvor blev de af.html` and its 25 `Sider-hvor blev de af/*.html` pages.** This is the *dispersal tracker* the task asked for — one page per site, each with a Type / RDAF-nr / Serie-nr / Status table. Compiled by Ulrich Krogh. Invaluable for finding sites nobody else lists (kindergarten playgrounds, fire-service training grounds, a youth club roof). **Undated and demonstrably frozen around 2009–2012** — every currency conflict in §3 resolved against it.

**Tier 5 — `sv.wikipedia.org/wiki/Lista_över_bevarade_Saab_35_Draken`.** Proved the *stalest* compilation checked: it still lists AR-102 at Tønder (removed 2023, scrapped), AR-104 at Terma Grenaa (now at a demolition contractor in Bjerringbro), AR-118 at the Stauning entrance (removed), and swaps A-001/A-005. Used only as lead generation.

**Tier 6 — `aerialvisuals.ca` LocationDossier.** Used for the Aalborg garrison museum only; undated, and it lists two airframes (A-010, 51-10622) that spottingmode's 2025 survey does not (see §3).

**aviationmuseum.eu** was used for lead generation only, as instructed. Its Narsarsuaq page contains no aircraft facts at all.

**Blocked/unusable:** `draken.dk` (WAF blocks non-browser clients, 454). `flymuseum.dk/flysamling` 404s.

## 2. Corrections made, with evidence

| Claim | Source making it | Correction | Evidence |
|---|---|---|---|
| AR-102 gate guard at Tønder Flyveplads | sv-wiki, flyhis | **Removed 2023, trucked to Karup for scrapping** — site excluded entirely | da-wiki F-35 Draken |
| AR-104 gate guard at Terma, Grenaa | sv-wiki, flyhis | **Now at demolition firm Jatop ApS, Bjerringbro** — not a display; excluded | da-wiki; spottingmode locates it at Bjerringbro 56.373N 9.615E |
| A-008 gate guard at Randers Flyveplads | flyhis | **Removed end of 2017** — excluded | da-wiki |
| A-017 landmark at Skive Kaserne | flyhis | **Moved to Hjallerup Mekaniske Museum** — recorded there | da-wiki, sv-wiki, spottingmode all agree on Hjallerup |
| A-002 landmark at Jonstruplejren (officer school) | flyhis | School site vacated; A-002 recorded at Langelandsfort | spottingmode (3 Jul 2025) |
| A-005 at Langelandsfort | flyhis, da-wiki, sv-wiki | **A-005 is in Hangar 2, Værløse** | Museum's own 2026 pages: inventory page names A-005 and a 2026 news post "Draken A-005 forberedes for montering af efterbrænder" |
| A-001 at Værløse Historisk Hangar | spottingmode (2020) | **At Danmarks Tekniske Museum** | flyhis DTM page + da-wiki + sv-wiki; Hangar 2's own 2026 inventory does not list it |
| DT-884 at Værløse Historisk Hangar | spottingmode (2020) | **At Danmarks Flymuseum, Stauning** | museum's own aircraft-page URL slug; flyhis had it under restoration at Skrydstrup, consistent with a later move to Stauning |
| E-176 at Danmarks Flymuseum | flyhis | **At Hangar 2**; Stauning's F-16 is E-174 | Hangar 2 news post "F-16 kom tilbage til hangaren tirsdag d. 24. marts" (2026); spottingmode puts E-174 at Stauning |
| A-014 at Gedhus Museet, Karup | flyhis | **At Egholm Museum** | spottingmode |
| RT-654 on 3-year loan to Hjallerup / under restoration at Aalborg | flyhis (two pages) | **At Hangar 2, Værløse** | Hangar 2 inventory page 2026 |
| M-070 Alouette III at the Aalborg garrison museum | aerialvisuals | **At Springeren Maritimt Oplevelsescenter** (the Aalborg naval museum) | flyhis "Marinemuseum, Aalborg"; spottingmode names Springeren explicitly |
| Meteor TT.20 WM387 *and* Meteor NF.11 51-504 as two aircraft at Aalborg | aerialvisuals lists both | **One airframe.** Danish NF.11 51-504 is ex-RAF WM387, later converted to TT.20 | Serial correlation; spottingmode lists only 51-504 there |

## 3. Judgment calls

**Værløse dispersal (the task's specific question).** Flyvestation Værløse closed in 2004 but the site is *not* empty: Hangar 2 is a live, publicly-open museum (Saturdays, plus booked tours) run by Værløse Flyhistoriske Hangar together with FLYHIS and Furesø Museer, and it is recorded as a site. Its inventory is taken **solely from the museum's own 2026 pages**: A-005, AT-160, RT-654, an F-84G marked SE-G, GT-927, S-134, E-176. spottingmode's Værløse–Historisk Hangar entry (last updated 12 Dec 2020) lists five more — J-49, A-001, A-008, S-249, DT-884 — none of which the museum itself claims; J-49 and A-001 are at Danmarks Tekniske Museum, DT-884 at Stauning, A-008 was removed from Randers in 2017 and A-249/S-249 is a Karup airframe. **Those five are not recorded at Værløse.** The separate spottingmode point "Værløse 55.76537N 12.32332E" (T-33s DT-404, DT-450, DT-905, all "std") is an open-air storage row, not a display, and is excluded.

**Aalborg Forsvars- og Garnisonsmuseum — two airframes deliberately handled differently.** spottingmode's location row says 7 aircraft and its plane list names exactly 7. aerialvisuals additionally lists **F-84G 51-10622** and **F-35 A-010**. da-wiki independently records that A-010 "is not visible on aerial photos spring 2018" and is in poor condition outdoors with no restoration funding. I kept **A-010** (three sources name it; the museum advertises "autentiske fly" outdoors) but flagged the doubt in its description, and **dropped 51-10622** (single undated source, no corroboration). This is the least confident pair in the file.

**Kindergarten playground aircraft are site records.** Børnehaven Lynghuset (Karup) holds F-84G 51-9838 with the tail of 51-10752 — a genuine composite, stated as such by FLYHIS, and recorded as a monument-class site with `access_type: restricted`. The same-class site at **Povlsbjerg Børnehave, Vojens** (F-84G A-525 / 51-10525, delivered 1964) is documented only by the frozen FLYHIS page and appears in no dated survey — **excluded**, and it is open question #1.

**Gate guards split into separate sites.** Karup has two distinct monument points with distinct coordinates (AR-112 at the main gate, DT-497 outside the flying school) and they are recorded as two sites rather than one "Karup" bucket, per the instruction that a single airframe is a site.

**Flyvestation Aalborg gate guards share one site record.** spottingmode has two separate F-104 points at Aalborg (57.10926/9.85713 and 57.08319/9.87427) but does not say which airframe is at which. Rather than guess, both R-771 and RT-657 are attached to one site carrying the first (verified) fix. R-855, which FLYHIS also calls a gate guard, has no corroboration in any dated source and is omitted.

**F-100D 55-2739 at Stauning.** Denmark transferred its entire F-100D fleet to Turkey, so no original Danish F-100D exists. Team Tordenjet built a composite from a French F-100D forward fuselage and a Danish TF-100F rear fuselage and painted it as **G-183**. True identity recorded as USAF 55-2739; G-183 is in aliases; the composite nature is in the description. Its donor TF-100F **GT-870** is therefore *not* recorded as a separate airframe.

**Meteor NF.11 51-504 / TT.20 WM387** — a single airframe, base designation "Meteor", variant NF.11, with WM387 and the TT.20 designation in aliases.

**Saab B 17C at Helsingør** is the Swedish SAAB dive bomber, not a Boeing B-17. Recorded as manufacturer Saab, model "B 17", variant "C", role bomber.

**Kramme og Zeuthen aircraft** are recorded with manufacturer "SAI" (Skandinavisk Aero Industri) and model "KZ II"/"KZ III"/… with the sub-mark in `variant` (Sport / Traener / U-4 / Mk.2). The dashless forms are in aliases as required.

## 4. Deliberate blanks

- **`year_built` is blank on every row.** No source consulted gave a sourced construction, rollout or delivery date for any individual Danish airframe. Danish military serials (A-009, R-888, DT-102, GT-927, E-174) look date-like and were never allowed near this field.
- **Manufacturer blank on one row:** OY-DAZ, listed by spottingmode only as type "ST-25" c/n 95, at Danmarks Tekniske Museum. No source identified the manufacturer; guessing was declined and the doubt is stated in the description.
- **Untailed F-84G rows:** five Thunderjets carry no Danish `tail_number` because the sources give only a USAF serial and/or a squadron code (51-9792/KP-K, 51-9966/KR-A, 51-9978/FS-978, 51-9838/SI-A, and the Hangar 2 aircraft marked SE-G). Those go in `aliases`; each row is distinguishable by alias and museum.
- **Addresses** left blank wherever no municipal or museum source stated one. Coordinates are spottingmode fixes (verified against aerial imagery by that project) or blank — none invented.

## 5. Exclusions and why

**Fire, rescue and battle-damage-repair training airframes** — deliberate retention but no public presentation:
- Beredskabsgården Langvang, Randers — F-84G 51-10482 (SE-A), on the rescue-service training ground since June 2001.
- Beredskabstjenesten Herning — TF-100F GT-874 on the training ground since Nov 1994; FLYHIS itself calls it "stærkt forfaldent".
- Københavns Lufthavn Kastrup BOR area — Draken A-018, fire trainer since 1998.
- Aalborg — CRJ-200 OY-RJG at the Danish Emergency Management Agency training ground.
- Flyvestation Skrydstrup BOR pad — A-004, F-946, 51-10487, Swedish S-35E 35-922.
- Flyvestation Karup BDR centre — R-812, AR-108, H-206, S-256, and others.
- Flådestation Frederikshavn — Lynx S-196 cockpit tactical trainer.
- Aalborg TechCollege — PA-28 instructional airframe.

**Storage, scrap and derelict, not display:**
- Billund (9 airliners in short-term storage), Copenhagen airport storage/scrapping rows (CRJs, DC-8 LN-PIP, BAe 146s, Caravelle OY-STD, Metro OY-BZW), Thisted (4 Do 328 + Jetstream, "dlt"), Herning Do 328 D-BGAQ, Sønderborg ERJ-145 UR-DNO, Stauning "various, to be scrapped" (6 airframes incl. Devon OY-BHZ and four SD.360s), Kolding PA-28 fuselages, Roskilde airfield derelicts (OY-DPL, OY-DLT, 2-MAPP, Be.1900 5Y-DHW).
- Jatop ApS, Bjerringbro — Draken AR-104 and CF-104D RT-655 at a demolition contractor. FLYHIS calls RT-655 a "gate guard" but it is standing at a scrap dealer; excluded.
- Bent Pouli, Ringkøbing — RF-84F C-865 cockpit in a private collection, not publicly presented.

**Theming and decor rather than preservation:**
- Djurs Sommerland, Nimtofte — a Rallye "wreck" with PA-28 parts dressed as a crash scene on the Jungle Safari canoe ride.
- Odense Paintball, Beldringe — Cessna 182 OY-BUG as terrain furniture.
(The Flyvergrillen An-2 and the Air Pub Hughes 269 *were* kept: both are complete airframes deliberately mounted and publicly presented, which is the stated test.)

**Insufficient currency — real candidates, deliberately held back:** Povlsbjerg Børnehave Vojens (F-84G A-525); Hjørring Mi-8 D-HOXF (spottingmode "pre", 2017); Stilling Boeing 727 G-BNNI ("pre", 2016); Hedensted Jetstream 1 OY-CRR ("pre", 2016); Ryå Rallye OY-DMD. Each is a plausible phase-3 monument that no source dated after 2021 confirms.

**Langelandsfort RF-84F C-651 and C-253** — FLYHIS lists them "under renovering" at the fort; spottingmode's 2025 survey counts only two aircraft there (Draken + MiG-23). Excluded pending confirmation.

**Egeskov Harvard 31-324 and Hunter F-426 cockpit** — FLYHIS puts both at Egeskov; spottingmode (2025) puts 31-324 at Karup and does not list F-426 anywhere. Excluded; Egeskov holds ten aircraft in both counts without them.

**Greenland — no records.** All six spottingmode Greenland locations are crash sites, not displays: two T-33 wrecks near Kangerlussuaq (1968 accident), a P2V-5 on the Kronborg Glacier (1962), a DC-3 at Kulusuk, a B-29 at Nunatame (destroyed during the 1995 recovery attempt), and an An-2 fuselage at Narsarsuaq (LY-AJG, status "deleted"). **Narsarsuaq Museum (Bluie West One)** was checked against VisitSouthGreenland, Visit Greenland and aviationmuseum.eu — it is a Second World War base museum of photographs and artefacts with **no aircraft named by any source**. Kangerlussuaq Museum likewise. No Greenland site is recorded.

**Faroe Islands — no records.** The Faroes do not appear at all in the spottingmode country index (Denmark 61, Greenland 6, Faroes absent), and no Danish- or Faroese-language search surfaced a preserved airframe at Vágar or elsewhere.

## 6. Open questions, ranked

1. **Povlsbjerg Børnehave, Vojens — F-84G A-525 (51-10525), on the playground since 1964.** Only FLYHIS documents it and that page is ~15 years stale. A single street-level or satellite check would either add a site or close the question. Highest-value single unknown in the country.
2. **A-002 vs A-005 at Koldkrigsmuseum Langelandsfort.** Hangar 2's own 2026 site puts A-005 in Værløse, which forces Langelandsfort's aircraft to be A-002 — and spottingmode (Jul 2025) agrees. But da-wiki asserts the opposite pairing *and* carries a 2020 photo captioned "A-005 udstillet på Koldkrigsmuseum Langelandsfort". One of the two serials in this file is wrong. Needs a photograph of the fort's Draken nose.
3. **Aalborg Forsvars- og Garnisonsmuseum — is Draken A-010 still there, and what became of F-84G 51-10622?** A-010 was reported invisible on 2018 aerial imagery; spottingmode's 2025 survey counts 7 aircraft and excludes both. A-010 is recorded here with a caveat; 51-10622 is not recorded at all.
4. **Where did the retired Danish F-16 fleet go?** The RDAF formally retired the F-16 at Skrydstrup on 18 January 2026 (last landing E-008; farewell four-ship E-008, E-018, E-605, ET-612). Nineteen went to Ukraine and others to Argentina, but the museum and gate-guard allocations of the remainder are unsettled and almost certainly generating new Danish monument sites right now. Only E-174 (Stauning), E-176 (Hangar 2) and E-177 (Skrydstrup) are recorded. Worth re-sweeping in 2027.
5. **Pembroke 69-697 and the Stauning/Karup boundary.** FLYHIS puts the Pembroke on display at Danmarks Tekniske Museum; spottingmode places it at Karup with status "stored". Recorded at Helsingør and flagged. The same uncertainty affects several FLYHIS-only Gedhus entries (DT-905, KZ-VII O-620) which spottingmode places elsewhere or not at all, and which are omitted here.
