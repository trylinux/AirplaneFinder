# Argentina — Pass 1 notes (public civilian museums + nationwide discovery sweep)

Output directory: `/home/claude/sa/argentina_p1/`. Museums file `ar_museums.csv` (20 sites);
one `<slug>_aircraft.csv` per site (166 rows, 155 with tail numbers). Research date: September 2026.

Scope reminder: this pass records museums, visitable private collections, aeroclub museums and
other public institutions holding aircraft. Air-force/navy/army base displays, gate guards, plaza
monuments, schools and aeroclub gate guardians are **not** recorded here — everything of that kind
that turned up is listed under "Leads for other agents" at the end, with serials.

## Sources and their weight

| Rung | Source | Used for | Weight / staleness |
|---|---|---|---|
| 2 | mna.ar `el-museo.html` (museum's own collection page, 2025) | MNA holdings, serials, hangar/exterior split | Highest for "what is here now". Lists 51 airframes. |
| 2 | elmuan.blogspot.com "Nuestros aviones" / "Hangar de restauración" / "Restauraciones" (Museo de la Aviación Naval friends' pages) | MUAN holdings, serials 0xxx/x-x-xxx, status | Museum-run; undated but consistent with 2018-2025 photos. Page truncated after 25 entries in fetch; remainder cross-checked with es.wikipedia and aviationmuseum.eu. |
| 2 | museoaeronaval.wixsite.com/muan, argentina.gob.ar/armada/museos/aviacion-naval | MUAN address, hours (Sat/Sun/holidays 14-19), access | Current |
| 2-3 | Roll Out / aerospotter.blogspot.com (Carlos Abella) — 3,780 posts, feed pulled in full, 2021-2026 bodies read | MNA layout changes (Mar 2025, Jun 2025), Hangar 4 restorations (Sep 2023, Nov 2024, May 2026), Dagger C-432 arrival (Jul 2022), Ranquel PG-423 (Mar 2025), Fleet LV-ZCL (Mar 2023), CIATA (Mar 2024, Jul 2026), Trelew (Jun 2026), Oliva (Jan/Apr 2023), Bariloche (Sep 2025), Santa Romana (2017), Museo Fuerte Independencia (2017), Museo Mouras (2017), Luján Tracker (Nov 2025), etc. | The best Argentine currency source: dated visits, c/n and full identity chains. Treated as rung 3 registry + dated photo evidence. |
| 3 | aeron-aves.blogspot.com "Aeronaves Preservadas en Argentina y el Cono Sur" (Fabián Pesikonis) — 355 Argentine entries, feed pulled in full | Serials/c/n for MNA, MUAN, Tigre, Oliva, Santa Romana, Museo del Ejército; province sweep leads | Dated photographs (2009-2026). Many entries are 2010-2019 photos; treated as leads unless corroborated. |
| 3 | aerialvisuals.ca Location Dossier 4109 (MNA) | c/n and ex-identities for MNA; long unassigned list | Compilation; includes airframes that are actually at CIATA and several unverified civil lightplanes (see exclusions). |
| 3 | arqueologiaaeronautica.blogspot.com (2012-2018), aeropuertocordoba.blogspot.com Córdoba survey (2015), gacetaeronautica.com Mirage survivors (Aug 2023), Wikipedia F9F Panther survivors | Cross-checks, Córdoba Museo de la Industria, Mirage identities | Stale (2013-2018) except the Gaceta Mirage article. |
| 4 | en.wikipedia MNA / es.wikipedia MUAN / aviationmuseum.eu lists | Gap-filling only | en.wikipedia MNA list is 2013-2019 vintage and contains several airframes not on the museum's 2025 page; aviationmuseum.eu lists (Bob Ogden-style) include departed aircraft (AE-335 now at Oliva, E-608 at Santa Romana). |
| news | zonales.com, castelar-digital.com.ar, diarioanticipos.com, vivieloeste, noticiasenvuelo.faa.mil.ar, lanacion, barilocheopina, canal26 | MNA status 2024-26, Hangar 4 open days, Bariloche Mirage | Current (2024-2026) |

WebSearch budget was exhausted mid-run (shared session limit); the second half of the sweep was
done by pulling the Blogger JSON feeds of the two preservation blogs and grepping them, plus
targeted WebFetch. Bing/DDG/Google via curl were not usable through the proxy.

## Museo Nacional de Aeronáutica — status 2024-26

- Not relocating. The museum has been at Base Aérea Militar Morón since November 2001 (moved from
  Aeroparque); 2026 press marked the 25th anniversary of the move. It closed for works in December
  2024 and reopened for the 2025 season in March 2025; reopened again after summer on 27 Feb 2026.
  Open Fri-Sun (2026: Fri-Sun 09:00-14:00, ARS 4,000, free for under-18/retirees/veterans; the
  argentina.gob.ar page gives Fri 10-15, Sat-Sun 10-17). Hangar 4 (GTRA restoration hangar) holds
  open days several times a year (Oct 2024, Nov 2024, May 2026, Aug 2026).
- Layout changes March 2025: Learjet LV-OEL into Hangar 3; Bo 105 LV-LGR swapped into LQ-AOF's
  place, LQ-AOF to Hangar 2; former engine hall reopened with Fw 44 Ee-122, Blériot XI, Ranquel
  PG-423 and the Anasagasti car. June 2025: C-130B TC-60 towed inside Hangar 2.
- Hangar 4 (visible only on open days) as of May-June 2026: Avro Lincoln B-004, A-4P C-240,
  Chinook H-93, Ju 52 T-158, IA-63 Pampa mock-up EX-03, C-54 nose T-45. All recorded as
  `under_restoration` / `in_storage`.

## Corrections made (with evidence)

- **MNA Huanquero is A-316, not A-305** (en.wikipedia): museum page, 2013 and 2015 photographs.
- **MNA Meteor is C-041** (delivered I-041, ex EE586): museum page; Wikipedia's "I-041" kept as alias.
- **MNA "Kfir C.2 C-432"** (aerialvisuals) is IAI Dagger C-432, c/n S-20 — museum ceremony 28 Jul 2022.
- **MNA DC-3 "Independencia"**: museum placard shows LQ-GJT; aerialvisuals and Aeronaves
  Preservadas identify the airframe as C-47A-30-DK c/n 14010, ex LQ-ACF air ambulance, FAA T-101.
  Recorded as T-101 with LQ-GJT/LQ-ACF/LV-ACF as aliases. Needs a placard/data-plate check.
- **MNA "Fleet 16B LV-ZCL"** (museum page): Roll Out identifies it as a Fleet Model 10A; recorded as Fleet 10A with "Fleet 16B" alias.
- **MNA UH-1H**: three Hueys have passed through; the current one is H-15 (c/n 5483). The earlier
  H-19 went to Santa Romana in Nov 2008 (Aeronaves Preservadas correction, Jan 2024). aviationmuseum.eu still lists H-19 at Morón — wrong.
- **MNA Chinooks**: two airframes — H-91 (displayed, Aug 2022 photo) and H-93 (Hangar 4).
- **MNA MS.760**: recorded E-207 (museum page). aerialvisuals also lists E-247 at "site B"; not corroborated, excluded.
- **Boeing 737 LV-WTX and BAC 1-11 LV-MZM** are instructional airframes at CIATA (the civil
  training centre on the same base), not museum exhibits — recorded under the CIATA site per
  Roll Out's March 2024 visit. BAC 1-11 **LV-OAX** is the museum's (awaiting restoration, post updated Dec 2025).
- **Beech C-45H LV-WEX** likewise at CIATA (Mar 2024), not at the museum.
- **MUAN Panther is 0425/3-A-113**; es.wikipedia's "3-A-311" is an error (Wikipedia F9F survivors list and the museum roster agree on 3-A-113).
- **MUAN Alouette 3-H-112** is 0735 per the museum roster (es.wikipedia: 0737).
- **MUAN Bell 47D 2-HE-3**: museum roster 0289; aviationmuseum.eu 0834. Tail recorded as 2-HE-3, both numbers as aliases.
- **Tigre Panther**: 0453/3-A-118 (previously 3-A-123 and 3-A-119).
- **Oliva Mirage**: an old (2018) blog note called it a Mirage IIIEA disguised as Dagger C-415; the
  2023 Roll Out pictorial gives c/n S-04 (a Nesher) and Gaceta Aeronáutica (Aug 2023) calls it the
  most faithful Dagger restoration in the country. Recorded as Dagger/Finger C-415.
- **Santa Romana Tracker** wears 0703/2-AS-24 but is 0862/2-AS-29 (c/n 325C). Recorded as 2-AS-24 painted / true identity in description and aliases (Roll Out 2017, Aeronaves Preservadas 2019).
- **Santa Romana A-4 "C-304"** is really an A-4F (c/n 13786) spares airframe; "C-222" is A-4B/P C-232 (c/n 11811); "C-937/C-938" are ex-USN A-4F/TA-4J spares airframes painted as A-4AR/OA-4AR; "C-721" is IIIBJ C-722; "H-19" is UH-1H c/n 10080. All recorded with true identity where known and false marking in aliases.
- **Santa Romana Sea King** wears fictitious 0696/2-H-235 (c/n 61-433); recorded under the painted serial with c/n, since the true serial is not published.
- **A-109A AE-335** moved from Morón (aviationmuseum.eu list) to Oliva (Army 2019; photo Apr 2021). **T-28A E-608** is at Santa Romana on loan from the MNA (since Nov 2005), not at Morón.

## Judgment calls

- **Access types**: MUAN is inside Base Aeronaval Comandante Espora but opens to walk-up visitors
  Sat/Sun/holidays 14:00-19:00 → `public`. MNA is inside BAM Morón but has its own public entrance → `public`.
  CIATA (instructional airframes inside the base, seen only on arranged visits) → `restricted`.
  Santa Romana is a private estancia that hosts group visits (Navegueta 2019) but publishes no hours → `appointment`.
  Aero Club Trelew (aircraft on an aeroclub apron, museum fit-out in progress) → `appointment`.
  Museo Hangar Zero (private, "coordinate visits") → `appointment`. Museo del Automóvil de Campana (airframe stored, not exhibited) → `appointment`, row `in_storage`.
- **Nose/forward sections recorded** (flagged in description): MNA C-54A T-45 cockpit (Hangar 4, `in_storage`); MUAN A-4Q 0744/3-A-318 nose in the Hangar Tecnológico; MUAN V-65F Corsair fuselage (unique survivor). Tail boom of UH-1H AE-404 at the Museo del Ejército **not** recorded (boom only).
- **Composites/hybrids recorded with the story**: Oliva Pucará A-581 (fuselage A-581 + wings AX-06); Museo de la Industria Guaraní (F-34 fuselage + T-121/T-127 parts); Santa Romana A-4Q "3-A-308"; Tigre A-4B "3-A-312" (BuNo 145050 painted); Santa Romana Sabre C-113 (rebuilt with C-105/C-121 parts).
- **IA-63 Pampa "EX-03" at MNA is a full-scale wooden factory mock-up**, not an airframe; recorded and flagged because it is a genuine FMA development artefact (as the brief allows for clearly-flagged replicas). Delete if the importer wants airframes only.
- **Wright Flyer replica** (MNA) and **Farman HF.7** (Wikipedia list; not on the museum page) excluded. **Nieuport 28** on the aviationmuseum.eu list excluded (no evidence it is original or present).
- **Plus Ultra** (Luján) is the original Dornier Wal of the 1926 flight, held by the transport museum since 1936 — recorded as `military` (Spanish/Argentine naval aircraft) with role `transport`.
- **Museo Histórico del Ejército** (Ciudadela) and **Museo Histórico Militar de San Rafael** are army-run but are public museums in town, so they are in this pass; **Museo de la Aviación de Ejército** (inside Campo de Mayo) is left to the base pass.
- **Cierva C.30A LV-FBL at MNA** kept (Wikipedia + 2014 photo) but flagged: it is not on the museum's 2025 web list.
- **Museo de la Industria (Córdoba)** rows other than the Guaraní rest on the 2015 Córdoba survey only; flagged in descriptions. The museum's own tourism page mentions engines and a Link trainer but no aircraft list.
- **Museo Mouras Finger C-416** rests on a single 2017 report; kept because nothing indicates removal, flagged for verification.
- `year_built` left blank everywhere except the Hangar Zero Stearman (museum states 1943).
- Coordinates: only where a source gave them (es.wikipedia article coordinates for MNA, MUAN, Tigre,
  Museo Malvinas, República de los Niños; Aeródromo de Baradero article for the aeroclub museum). These are museum/site
  positions, not airframe positions. All others blank — town centroids were deliberately not used.

## Excluded (do not re-research)

- **Tecnópolis (Villa Martelli)**: the Pucará, Pulqui II and Pampa mock-up exhibited there in 2011-12 were MNA loans; the Pulqui II and Pampa mock-up are back at Morón (the mock-up damaged by the exposure). No evidence any airframe remains at Tecnópolis in 2025-26. Not recorded.
- **Museo Nacional de Aeronáutica — listed but not corroborated** (en.wikipedia/aviationmuseum.eu/aerialvisuals only, absent from the museum's 2025 page and from any 2021-26 report): IA-41 Urubú flying-wing glider, Iriarte "Ladrillo"/LV-X-114 monoplane, Dittmar Condor IV LV-EGG, Luscombe 8A LV-NMQ, Cessna 170A LV-YCJ, Ercoupe 415C LV-NUY, Piper PA-12 LV-RRN, Piper Apache LV-BZM, Aero Boero AB-95 LV-IZU, Beech H18S LV-JFH, Beech C-45H HI-531CT/A-216, Jetstream 32 LV-VEI, Learjet 35A "T-26", MS.760 E-218/E-247, a second F-86F, Cessna 310 T-12 (a CIATA/private restoration "project" per Aug 2026 Roll Out), Sikorsky S-51 LV-XXS (only the cabin survives, in the relics room), Ansaldo SVA-10 remains, Agusta A109 AE-335 (now Oliva), T-28A E-608 (now Santa Romana). Ask the museum for a current inventory before adding any of these.
- **Junkers Ju 52 "LQ-ZBD"** and **"T-158"** are one airframe (c/n 4043) — recorded once.
- **MUAN**: SNJ-5C 0464/2-G-106 appears on the museum roster with an incomplete entry — not recorded. Quimar MQ-1 Chimango target drone under restoration — not recorded (no evidence of display). Super Étendard 0752/3-A-202 photographed on MUAN's helicopter apron on Navy Day 2008 and described in Nov 2025 as "preserved at Base Aeronaval Comandante Espora" — not on the museum roster → passed to the base agent.
- **Museo Marítimo/Presidio de Ushuaia, Museo del Fin del Mundo, Museo de la Patagonia (Bariloche), Museo de Ciencias Naturales sites, Museo Ferroviario, Museo de Armas de la Nación, Museo Aeronáutico Rosario, Villa Reynolds "museum", Museo Municipal Villa Gesell, Museo Ciudad de Necochea, Fundación Museo del Automóvil (Buenos Aires), Colección Bassotti, Museo del Automóvil Termas de Río Hondo**: no evidence of any aircraft found in either preservation blog (355 + 3,780 posts) or elsewhere. Not recorded; the DC-3 5-T-22 at Ushuaia is at the aeroclub gate (lead below).
- **KidZania Buenos Aires DC-9 section** (2012): a fuselage section in a children's theme park, no 2020s evidence — not recorded.
- **Oncativo (Córdoba) Boeing 737-2E1 c/n 21112** — fuselage converted into a nightclub ("1880") at Campo Hotel Nono Luigi (2023). Commercial venue, not a museum; passed as a lead.
- **Baradero Boeing 737-228 LV-ZTE** (private property, 2015) — lead, not museum.
- **Airworthy but not exhibited**: nothing recorded as airworthy outside a museum (MUAN's Stearman, Luscombe and Tracker are museum aircraft and are recorded).

## Blank fields, deliberately

- `tail_number` blank: MNA Blériot XI, Pulqui I, Pulqui II, Horten Ho Xb; MUAN Vultee BT-13 (serial not published); Museo de la Industria Clen Antú (no marks known); Hangar Zero Stearman (registration not published); San Rafael UH-1H (painted AE-413 is false, true identity unknown); Campana OA-4M (BuNo in aliases — no Argentine serial); Santa Romana second UH-1H (painted H-19 false; c/n 10080 in aliases); CIATA F337G (serial not published).
- `latitude/longitude` blank for 14 of 20 sites (see judgment calls).
- `website` blank where the site has none that could be verified.
- `postal_code` only where known (Morón 1708, Bahía Blanca 8107, Tigre 1648, Luján 6700).

## Needs a human on site (ranked)

1. **MNA full inventory** — the museum says "more than 65 aircraft" while its web list has 51 and this file 63. Confirm which of the excluded lightplanes/gliders (Urubú, Iriarte, Condor IV, Luscombe, Cessna 170, Ercoupe, PA-12, Apache, Aero Boero) still exist and where; confirm the Cierva C.30A is still present; confirm the DC-3 "Independencia" true identity (T-101/c/n 14010?) from its data plate.
2. **MUAN**: confirm current status of the Panther, Cougar, CW-16E, SNJ-4, T-28 1-A-250 and BT-13 (restoration hangar vs display), whether Electra 6-P-106 is on display or stored, and whether Tracker 2-G-51 lives at the museum or with the squadron.
3. **Museo de la Industria (Córdoba)**: confirm which of Clen Antú, Aero Commander LV-FYF and Ranquel LV-HLV are still there (2015 source).
4. **Museo Mouras (La Plata)**: is Finger C-416 still at the autodrome museum (2017 source)?
5. **Museo Histórico de General Pacheco**: confirm DC-3 TC-27 still displayed and the museum's exact name/address.
6. **Museo Histórico del Ejército**: confirm the garden UH-1H's serial (AE-421 fuselage?) and whether any other airframe (e.g. an OH-58 or Bell 205) has been added since 2019 besides the Super Puma AE-525 (2024).
7. **Santa Romana**: visiting arrangements; whether the Mi-2 (c/n 529614016) and Finger C-421 reported "in the collection" are actually present; true serial of the Sea King.
8. **Oliva**: confirm the F-28 5-T-20 is reassembled and displayed (arrived Apr 2023).

## File / row-count table

| File | Rows | With tail |
|---|---|---|
| ar_museums.csv | 20 sites | — |
| museo-nacional-de-aeronautica-moron_aircraft.csv | 63 | 59 |
| museo-de-la-aviacion-naval-bahia-blanca_aircraft.csv | 31 | 30 |
| museo-interfuerzas-santa-romana_aircraft.csv | 22 | 21 |
| ciata-moron_aircraft.csv | 12 | 11 |
| museo-historico-del-ejercito-ciudadela_aircraft.csv | 7 | 7 |
| museo-nacional-de-malvinas-oliva_aircraft.csv | 7 | 7 |
| museo-de-la-industria-cordoba_aircraft.csv | 4 | 3 |
| museo-naval-de-la-nacion-tigre_aircraft.csv | 3 | 3 |
| museo-aeronautico-aeroclub-baradero_aircraft.csv | 3 | 3 |
| aero-club-trelew_aircraft.csv | 3 | 3 |
| republica-de-los-ninos-gonnet_aircraft.csv | 2 | 2 |
| museo-malvinas-buenos-aires_aircraft.csv | 1 | 1 |
| museo-udaondo-lujan_aircraft.csv | 1 | 1 |
| museo-historico-general-pacheco_aircraft.csv | 1 | 1 |
| museo-fuerte-independencia-tandil_aircraft.csv | 1 | 1 |
| memorial-malvinas-bariloche_aircraft.csv | 1 | 1 |
| museo-mouras-la-plata_aircraft.csv | 1 | 1 |
| museo-hangar-zero-general-rodriguez_aircraft.csv | 1 | 0 |
| museo-historico-militar-san-rafael_aircraft.csv | 1 | 0 |
| museo-del-automovil-campana_aircraft.csv | 1 | 0 |
| **Total** | **166** | **155 (93%)** |

Display status: 150 on_display, 12 under_restoration, 4 in_storage.

## Leads for other agents

Everything below was found during the sweep but is out of scope for Pass 1 (base displays,
gate guards, plazas, schools, aeroclub gate guardians, private grounds). Source in brackets
(AP = aeron-aves.blogspot "Aeronaves Preservadas" with photo date; RO = Roll Out/aerospotter with post date;
AA = arqueologiaaeronautica 2012-18; GA = Gaceta Aeronáutica Mirage survey Aug 2023).

### Pass 2 — military bases, academies, schools
- **BAM Morón (outside the museum)**: Hughes 369HE/RACA 500 PGH-05 (ex H-20, c/n 89-0107E) on a pedestal at the base entrance plaza [RO Jun 2025]; Piper PA-31P Navajo PG-397/VR-22 (c/n 31P-52) in the garden in front of the old terminal [RO Jun 2023]; Fairchild F-27 LV-RLB (c/n 42, ex CATA) behind the IAAC/Instituto Argentino de Aviación Civil, visible from Figueroa Alcorta 500, Castelar [RO Mar 2024].
- **Base Aeronaval Comandante Espora (Bahía Blanca)**: S-2A Tracker 0512/2-G-53 gate guard; S-2T Turbo Tracker 0702/2-AS-23 (ESSA, Punta Alta, Dec 2025); Super Étendard 0752/3-A-202 preserved on base [AP Nov 2025]; Alouette III 3-H-309 [AA 2015]; UH-1H 3-H-303 [AA 2013]; HU-16B BS-03? [AA 2014].
- **Base Naval Puerto Belgrano**: F9F-2B Panther 0421/3-A-106 gate guard; MB-326GB 4-A-107; Sea King at Baterías [AP 2015].
- **Base Aeronaval Punta Indio**: F9F-2B 0452/3-A-111 gate guard; MB-326; T-28F; AT-6 Texan; Beech B-80 Queen Air 0689/6-G-83 reserved for MUAN [AP Nov 2025].
- **Base Aeronaval Almirante Zar (Trelew)**: T-28F Fennec restored as 0565/1-A-283 at the gate [AP 2014]; P-3B 0868/6-P-52 went to the Centro de Veteranos de Guerra de Trelew, 14 Jun 2026 [RO].
- **Escuela de Aviación Militar / IUA Córdoba**: F-86F, Meteor, Pucará (EAM and IUA), MS.760, T-28A, Mentors, A-4B, Sala Malvinas [AP 2012-16].
- **Escuela de Suboficiales FAA (Ezeiza)**: A-4B C-225, A-4C, Canberra, Pucará, Mirage, MS.760 x2, GII, Hughes, Mentor [AP 2010-18]; A-4B C-224 at Instituto de Formación Ezeiza [AP 2013].
- **Área Material Quilmes / Escuela Técnica N° 7 "IMPA" (Quilmes)**: Gloster Meteor F.4 (engines run again 2022), Sikorsky S-55 H-08 (run 2024), UH-1H, Mentor, MS.760, Aero Commander x2, Hughes 500 x2, Cessna 336 PG-391 [RO Dec 2024; AP 2022-25].
- **Área Material Río Cuarto (Las Higueras)**: A-4B C-222 "El Tordillo"?, A-4P, Mirage IIIEA I-007, Mirage IIICJ C-717 "Pepsi", IA-58C AX-06 (Museo Tecnológico Aeroespacial), DC-3 TC-37, MS.760 x2, Aero Commander, Sabreliner, Dagger C-433 monument [AP/AA/GA]; Dagger at the "rotonda de la Universidad" Las Higueras since 28 Mar 2022 [RO].
- **II Brigada Aérea Paraná**: Canberra B-111, Huanquero A-317, Guaraní F-35, F-27 T-43 and TC-78 stored [AP 2014-16].
- **III Brigada Reconquista**: Pucará, Huanquero [AP 2013-22]. **IV Brigada Mendoza**: A-4B, MS.760 [AP]. **V Brigada Villa Reynolds**: A-4P, Lincoln B-0xx [AP 2010-13]. **VI Brigada Tandil**: Mirage IIIEA x2, Mirage 5 x2 on the brigade monument; Dagger in Tandil plaza; Meteor Tandil [AP 2012-18]. **VII Brigada Moreno / José C. Paz**: Meteor, Hughes [AP 2010]. **El Palomar (I Brigada)**: Boeing 707 (LV-WXL and others), C-130B TC-56 cockpit memorial, Fiat G.46, Guaraní [AP/AA]. **Comodoro Rivadavia**: Pucará A-566 at the airport roundabout [AP 2018]; F-27 T-45 abandoned at airport [AP 2020]. **Tucumán**: C-130H TC-62 [AA 2015].
- **Campo de Mayo**: Museo de la Aviación de Ejército (base museum) with Mohawk, UH-1H x several, A-109, Citation, Sabreliner, G-222 AE-260/261/262, Robinson (Gendarmería) [AP 2013-25; museosaeronauticos 2015]; Bell OH AE-392 and Hiller at the Campo de Polo [AP 2015]; Regimiento de Asalto Aéreo 601 UH-1D [AP 2022].
- **Edificio Cóndor / Edificio Libertad (CABA)**: Meteor C-095 moved 18 Jul 2025 from Edificio Cóndor to the Casino de Suboficiales (Av. Sarmiento y L. Lugones), an A-4 from Río Cuarto to replace it [RO]; A-4Q 0657/3-A-204 (c/n 12161) gate guard at Edificio Libertad [RO Jul 2023, AP Jun 2026]; A-4C at Edificio Cóndor [AP Jun 2026].
- **Schools**: EET N° 8 "Jorge Newbery", Villa Luzuriaga/San Justo — Meteor, A-4Q, Prentice, BAC 1-11 (T-28 Fennec sent to Salta 17 Dec 2025) [AP/RO]; EET N° 3144 "Capitán Marcelo Lotufo", Salta — T-28P 0632/3-A-212 (Dec 2025) [RO]; UNLP Aerotalleres Tolosa hangar (Aeroclub La Plata, Ensenada) — Hiller UH-12E LV-HEM, OV-1D Mohawk cockpit, engines [RO Dec 2024]; Escuela General Lemos etc.

### Pass 3 — monuments, plazas, aeroclub gate guards, private grounds
- **Mirage/Dagger family** [GA Aug 2023 + RO/AP]: Dolores (BA) Mirage IIIEA I-015 monument RP63 & Av. Belgrano [RO May 2024]; Villa Ramallo I-008 (Paseo de la Estación, since 27 May 2023); Rosario del Tala (ER) Nesher C-436 painted C-411 (Sep 2025); Río Grande (TdF) C-414; Comandante Luis Piedra Buena (SC) Mirage 5P C-610; Puerto San Julián Mirage; Río Gallegos Mirage; Rufino (SF) Mirage 5 C-633; Laboulaye (Cba) Mirage 5; Luján de Cuyo (Mza) Mirage 5P ex-FAP painted C-433 (true C-419/C-619) with an AMX-13 [RO Jul 2024]; Maipú (Mza) IIICJ; Tres Arroyos IIICJ C-704 painted C-437; Villa Lugano (CABA) IIICJ C-706; Funes (SF); San Lorenzo (SF); Villa Carlos Paz; Balneario El Cóndor (RN); Mendoza city.
- **Gloster Meteor**: Aeroclub Chivilcoy C-088 (engine restoration with EEST N° 8, 2026) [RO]; Loreto (SE); Neuquén airport I-099; Santa Rosa (LP); Resistencia; Goya; Junín; Merlo; Mar del Plata C-073; Salta (2023); Funes; Baradero (recorded, museum).
- **F-86 Sabre**: Lanús Oeste C-104 (Av. Remedios de Escalada 800, repainted Apr 2024) [RO].
- **A-4 Skyhawk**: Villa Mercedes (SL) A-4B; Leones (Cba) A-4M/F; Aeroclub Morteros (Cba) A-4F; Aeroparque A-4B (moved?); Mar del Plata aeroclub A-4Q 3-A-314; Puerto San Julián A-4F; Mendoza IMPSA A-4B; Río Cuarto A-4B C-222? [AP 2010-23].
- **Pucará**: Campana plaza A-577 (c/n 078) [AP Jul 2022]; Villa Cañás aeroclub A-512 [AP Sep 2023]; Ataliva (SF); Río Tercero; Pilar (Cba); Reconquista city; Oliva (recorded).
- **Trackers**: Luján — S-2G 0860/2-AS-27 (c/n 297C, BuNo 152828) monument to Malvinas veterans, Av. Nuestra Señora de Luján y Ugarte, inaugurated 22 Nov 2025 [RO/AP]; Navarro — S-2G 0861/2-AS-28 (c/n 310C, BuNo 152841) monument inaugurated 2 Apr 2023 [RO]; Justo Daract — S-2G 0862/2-AS-29 (this is the Santa Romana airframe, recorded).
- **MB-326/MB-339**: Sunchales (SF) MB-339A 4-A-115 (Owen Crippa's aircraft, recovered from the USA, displayed Jul 2025) [AP]; MB-326 at Coronel Vidal 4-A-103, Luque (Cba) 4-A-102, Chascomús aeroclub, Verónica, Santa Fe, Río Grande.
- **Transports**: Ushuaia — DC-3 5-T-22 "Cabo de Hornos" at the Aero Club Ushuaia entrance (Bien de Interés Histórico Nacional, Dec. 1593/2008) [AP Mar 2025]; Paraná — C-47B 0498/CTA-25 (LQ-MSP) at the Sindicato de Empleados de Comercio [AP 2014]; Ezpeleta — DC-3 TC-34 moved in Mar 2021 to a private factory [RO Mar 2026]; Diamante (ER) costanera Guaraní c/n 26; Crespo (ER) Guaraní on RN12 (since 2002, deteriorating 2026) [RO]; Aeroclub San Francisco (Cba) Guaraní T-118 painted T-117 (gate, RN19) [RO Dec 2022]; Aeroclub Paraná Guaraní LV-LAI; Tancacha, Tiro Federal Córdoba, Aeroclub Córdoba (T-127), Aeroclub Argentino San Justo (T-122, derelict 2023) Guaranís; Loreto (SE) Curtiss C-46A LQ-IYV fuselage "Huaira Sorckoj" on RN9 (repainted Apr 2025, vandalised Nov 2025) [RO]; Aeroclub Rafaela Lockheed Lodestar c/n 18-2361 painted LV-ACR (restoration 2023); Baradero private 737-228 LV-ZTE; Oncativo 737-2E1 nightclub; Camino de Cintura Electra; Rosario airport Metro II c/n TC-419 and Cessna 401A LV-JMT abandoned.
- **Doves**: Aeroclub La Plata (Tolosa) LV-LES (repainted Jun 2022); Aeroclub Neuquén LV-XZX; Aero Club San Antonio Oeste LV-YAO (stored); Parque Mizujo, Colonia Urquiza (La Plata) fuselage, probably LV-LEP [RO Aug 2023].
- **Others**: Aeroclub Colón (BA) GAL.42 Cygnet II LV-KGA at the entrance; Aeroclub Carlos Casares T-28A; Aeroclub Bell Ville Prentice E-372; Club de Planeadores Los Caranchos Grunau Baby LV-EEF; Club de Planeadores Tres Arroyos Fleet 10A LV-ZCP; General Rodríguez aerodrome Fleet 10A LV-ZCI and Mohawks (private); Aeroclub Pueblo Esther (Rosario) PA-23 LV-JSX gate guard; Concordia (ER) Cessna 320 LV-IFV on private land, RN14; La Cruz (Cba) Mentor E-022; Juárez Celman (Cba) Beech Queen Air LV-JGV derelict; San Juan Plaza España MS.760 E-244; San Juan airport MD-83/88 LV-BGZ, LV-VBZ, LV-VAG stored (2021); Las Heras (Mza) MS.760; Aeroclub Ameghino MS.760; Mendoza FAA camping MS.760 x2; Salar Tolillar (Salta) A-4B C-209 wreck [AA]; Pinamar monument to the crew of TC-63 [RO 2022]; Museo/Huaira Bajo project B-25 Mitchell (private restoration to fly) [RO Jun 2023].


---

# Argentina — Passes 2 and 3 (military base collections, monuments, aero clubs, schools)

Output: `/home/claude/sa/argentina_p23/` — `ar_museums.csv` (129 sites) + 129 `*_aircraft.csv`
files (221 rows, 199 with tail numbers = 90%). Pass 1 (`/home/claude/sa/argentina_p1/`) holds the
named museums; nothing in this directory duplicates a Pass 1 site (see "Boundary with Pass 1").

## Sources and their weight

| Rung | Source | What it gave | Weight / staleness |
|---|---|---|---|
| 2 | argentina.gob.ar/fuerzaaerea "Patrimonio cultural – Museos" pages (2025) | Official list of FAA salas históricas and base museums with addresses; Museo Tecnológico Aeroespacial Río IV exhibit list (Pampa inside; MS-760, A-4P, C-47, Pucará Charlie, Mirage IIICJ C-717, AC-500 outside); V Brigada page confirms A-4B monument and Lincoln B-016 at the gate | Current, but names types only, no serials |
| 3 | Roll Out / aerospotter.blogspot.com (Carlos Abella) — all 444 "Preservado" posts pulled via the Blogger JSON feed and read for 2013-2026 | Dated visits with full identity chains (c/n, ex-serials), arrival/inauguration dates for Dolores, Ramallo, Rosario del Tala, Luján, Navarro, Pilar, Campana, Villa Cañás, Salsipuedes, Chascomús, Trelew, Río Grande, Edificio Cóndor/Casino, Las Higueras, EEST N°8, EET 3144 Salta, CIATA/IAAC, etc. | Best currency source; treated as dated photographic evidence |
| 3 | aeron-aves.blogspot.com "Aeronaves Preservadas en Argentina" (Fabián Pesikonis) — all 343 Argentine labels fetched | Serial + c/n for almost every base display and plaza airframe; photo dates 2009-2026 | Many entries are 2010-2014 photos; used as the identity source and flagged in descriptions where no later sighting exists |
| 3 | aeronavespreservadasdelaaviacionnaval.blogspot.com (Lorenzo Borri) — full feed (79 posts, updated to Jun 2026) | Naval airframe histories: Trackers 0860/0861/0862, Turbo Tracker 0702 to ESSA (May 2026), T-28s, Panthers, Xavantes, Electras, SNJs | Museum-adjacent author; current for naval items |
| 3 | gacetaeronautica.com (Carlos Ay, Marcelo Mustone, Esteban Brea): "Hoja de ruta a los Mirages argentinos sobrevivientes" (Aug 2023), "Aviones monumento entrerrianos" (2020), "Custodios aéreos para el Cenotafio" (2018), "¿El IA-50 Guaraní es una aeronave en peligro de extinción?" (2020), "Indios jubilados" (Punta Indio 2015), "Parque Aerojurásico" (EEST N°8), Skyhawks Illustrated | Type-by-type censuses with true vs painted identities (Mirage/Dagger, Guaraní); settles several serial questions | Current to 2023-26 |
| 4 | en.wikipedia "List of surviving Gloster Meteors", "List of displayed Douglas A-4 Skyhawks", "List of surviving F-86 Sabres", "surviving C-47s"; es.wikipedia base articles | Leads and cross-checks only | A-4 list is 2013 vintage; Meteor list (Padín 2007) is good on identities but stale on locations |
| news | lanacion (Bariloche Mirage Aug/Sep 2025), Los Andes (IMPSA A-4B, Oct 2023), Más Neuquén (Meteor, Jun 2022), Qué Pasa Salta (Meteor, Mar 2026), Minuto Fueguino (Río Grande monument 2022), argentina.gob.ar news (Río Gallegos Marjory Glen memorial 2023), puraciudad (Retiro A-4B plan, Dec 2025), Full Aviación (V Brigada museum visit 2022) | Currency | 2022-2026 |

The WebSearch budget was exhausted early (shared session limit, 200 calls). The bulk of the work was
done by pulling the three preservation blogs' Blogger feeds, the Gaceta Aeronáutica WordPress REST API
(`wp-json/wp/v2/posts?search=`), Wikipedia raw wikitext, and targeted WebFetch/curl of news pages.
Bing/DuckDuckGo via curl were unusable through the proxy; Overpass was down (server busy) every time.

## Boundary with Pass 1 (do not duplicate)

Sites already recorded by Pass 1 and therefore **omitted here** even though they hold base/monument-type
airframes: MNA Morón, MUAN Bahía Blanca, Santa Romana, CIATA Morón, Museo Naval Tigre, Museo Malvinas CABA,
Udaondo Luján, Museo Histórico del Ejército, Museo Nacional de Malvinas Oliva, Museo de la Industria Córdoba,
Aero Club Baradero museum (Meteor C-051, DC-3 TC-33, Dove), Museo Histórico Gral. Pacheco, Hangar Zero,
Museo Histórico Militar San Rafael (UH-1 "AE-413"), Fuerte Independencia Tandil (Meteor I-005),
Memorial Malvinas Bariloche (Mirage IIIEA I-014), Museo del Automóvil Campana (OA-4M rear section),
Aero Club Trelew (Electras, P-3B 6-P-55), República de los Niños Gonnet (737 LV-JTD, Jetstream), Museo Mouras.

Adjacent items recorded **here** because Pass 1 did not: Base Aérea Morón entrance plaza Hughes 369HE
H-20 "PGH-05" and Navajo VR-22 (both outside the museum and the CIATA hangar); IAAC Castelar Boeing 737
LV-WGX and Fairchild F-27 LV-RLB; Centro de Veteranos Trelew P-3B 0868/6-P-52; BACE Espora gate/apron
Trackers 0512, 0511 and Turbo Tracker 0703 (not on the MUAN roster). The MUAN Super Étendard 0752/3-A-202
passed to me by Pass 1 is **not** recorded: the only evidence is a 2014 photo on the base; a 2025 blog caption
repeats "preserved at BACE" without a new photo — needs an on-site check (open question 4).

## What is in scope here

- **FAA**: I Brigada El Palomar (GII "T-122"/F-33, C-130B TC-56 cockpit as TC-63, 707 TC-94 cockpit), II Brigada Paraná (Canberra B-111, GII F-35, Huanquero, GII T-110), III Brigada Reconquista, IV Brigada Mendoza, V Brigada Villa Reynolds, VI Brigada Tandil (Meteor "I-057", Bosque de los 55 Mirage I-003 + Dagger C-412, hangar Daggers C-408/C-426 and Mirage I-018), VII Brigada Moreno, Área Material Río Cuarto (12 airframes incl. the FAA museum), Área Material Quilmes/Escuela Técnica N°7 (12), Escuela de Aviación Militar (7), Escuela de Suboficiales FAA (11), Liceo Aeronáutico Funes, BAM Mar del Plata, BAM Merlo, Instituto de Formación Ezeiza, Edificio Cóndor plazoleta (A-4C since 2026) and the Meteor C-095 now at the Casino de Suboficiales, IUA Córdoba Pucará, the two FAA NCO campsites in Mendoza with MS-760s.
- **Armada**: BACE Espora gate, BAN Punta Indio (5), BAN Almirante Zar gate, Base Naval Puerto Belgrano (Panther, Sea King), Escuela de Suboficiales de la Armada (MB-326, Alouette, Turbo Tracker 0702 — May 2026), Edificio Libertad A-4Q, Aero Club Ushuaia DC-3, Centro de Veteranos Trelew P-3B.
- **Ejército / Gendarmería / Policía**: Campo de Mayo (Batallón/Museo de la Aviación de Ejército/aeródromo, 14 rows), Escuela de Suboficiales Sargento Cabral (3), Gendarmería Agrupación Buenos Aires R-44, IV Brigada Aerotransportada Córdoba C-47 fuselage "ETA-1", Los Polvorines plaza (Puma + Mohawk), Pilar Cenotafio (Finger "C-434", C-130H TC-67, UH-1H boom), Escuela de la Policía Federal Bo 105.
- **Monuments** (plazas, roundabouts, aero clubs, technical schools, veterans' centres): 12 Meteors, 1 Sabre, 6 Skyhawks, 18 Mirage-family, 8 Pucarás, 9 MS-760s, Mentor, 3 T-28s, C-45, Prentice, 2 DC-3/C-47, 7 Guaraníes, 8 MB-326/339, 2 Trackers, Electra 5-T-3, and the civil monuments (C-46 Loreto, Navion Rivadavia, 737s at Oncativo/Petión, Lodestar Rafaela, Cygnet Colón, Doves La Plata/Neuquén, Aztec Pueblo Esther, Cessna 320 Concordia).

## Corrections made (with evidence)

- **Mar del Plata gate Meteor is I-073 (G-5-173) painted I-071**; the EEST N°8 Villa Luzuriaga Meteor is therefore recorded as **I-071** (Wikipedia/Padín) although Roll Out (2018) also calls it G-5-173/I-073 — conflict noted in the row; one of the two sources has the airframes swapped.
- **Neuquén airport Meteor is C-099 (I-099, G-5-199)** per Padín/aeron-aves and Arqueología Aeronáutica; the Más Neuquén article's "C-093" is the VII Brigada gate guard, and the Wikipedia claim that the VII Brigada aircraft is "painted as C-099" is kept only as an alias. The Neuquén airframe was repainted "C-071" in the 2000s.
- **Villa Mercedes "C-207" is a spares A-4F/A-4E rebuild**, not the Malvinas veteran C-207 (which is in the MNA) — Carlos Ay via Roll Out 2017; tail left blank, C-207 as alias.
- **Leones "C-939" is A-4M BuNo 159473** (c/n 14414), Roll Out July 2020 / Gaceta 2023.
- **IMPSA Godoy Cruz A-4B is C-239 painted C-221** (aeron-aves 2011, Los Andes Oct 2023).
- **Mendoza IV Brigada A-4B C-233 wears C-301**; the composite "C-301" at the ESFA moved to the Edificio Cóndor plazoleta in 2026 (aeron-aves Jun 2026) after the Meteor C-095 was removed to the Casino de Suboficiales on 18 Jul 2025 (Roll Out).
- **Paraná II Brigada Huanquero**: Gaceta/Mustone give A-320 (c/n 22); aeron-aves gives A-317 (c/n 38). Recorded A-320 with A-317 as alias — placard check needed.
- **Guaraní swaps**: Crespo is T-117 (c/n 09) painted T-118; San Francisco is T-118 (c/n 10) painted T-117; Tancacha is the prototype c/n 00 (TX-110) painted T-121; San Justo derelict is c/n 32 (ex LV-LAM/T-111) carrying T-122's identity; El Palomar gate GII is F-33 (c/n 19) painted T-122 (Gaceta census 2020, Roll Out 2018/2026).
- **Rufino Mirage is C-633 (ex FAP-185/C-433)** and is the aircraft that fell off its Río Gallegos plinth in 2013; the current Río Gallegos monument aircraft is Mara **C-636** (aeron-aves Jan 2023).
- **Luján de Cuyo "C-433" is Mirage 5P C-419/C-619**; Laboulaye's "C-433" is a Mirage IIIC hybrid; Pilar's "C-434" is Finger C-423; Rosario del Tala's "C-411" is Nesher C-436; Tres Arroyos' "C-437" is IIICJ C-704; Carlos Paz "I-019" is IIICJ C-714; San Julián "C-421" is C-424 (S-17); Dolores is I-004 (not I-015, which was lost in 1982 — Pass 1's lead said I-015).
- **Quilmes UH-1H**: c/n 10080 / 67-18577 is the Escuela Técnica N°7 airframe (aeron-aves Nov 2022); the Santa Romana "H-19" is c/n 10044 / 67-17846 (Roll Out Jan 2024) — aeron-aves' 2019 Santa Romana caption attributing 10080 to it is superseded.
- **Trelew BAAZ gate T-28F is 0638** (ex Rawson zoo, rebuilt 2011) painted 1-A-283; aeron-aves' "0565" kept as alias.
- **Salta EET 3144 T-28 is 0553** (c/n 174-493, ex 51-7640) wearing "0632/JN-212"; it left EEST N°8 on 17 Dec 2025 and arrived Salta 19 Dec 2025 (Roll Out, naval blog).
- **CIATA C-45H "0529" is c/n AF-535** (Roll Out Mar 2024 list), not AF-561 (which is 0531 at EEST N°8). Not recorded here (CIATA is Pass 1).
- **Área Material Río Cuarto Aero Commander**: aeron-aves photographed T-139 there (Aug 2014); Roll Out (2015) said T-134. Recorded T-139 (photo) — placard check.

## Judgment calls

- **Access types**: everything inside a military perimeter is `restricted` even where an airframe is visible from the road (noted in descriptions: EAM Meteor on Av. Fuerza Aérea, Paraná II Brigada park by the fence, Ezeiza A-4B, Edificio Libertad). BAM Mar del Plata gate guards stand beside Ruta 2 outside the fence → `public`. FAA museums that publish hours but sit inside a base (V Brigada, Río Cuarto) → `appointment`. Technical schools and veterans' centres → `appointment`. Plazas, roundabouts, aero-club gates → `public`.
- **Sections/fragments recorded** (flagged in description): El Palomar C-130B TC-56 cockpit and Boeing 707 TC-94 cockpit; Pilar UH-1H AE-420 tail boom (it is a named monument); Campo de Mayo OV-1D "AE-043" cockpit trainer; UNLP Mohawk AE-033 cockpit; Oliva bus-terminal Dagger tail section; Puerto San Julián A-4F rear half; Córdoba IV Brigada Aerotransportada C-47 fuselage; Luján de Cuyo, Piedra Buena and Bariloche (Pass 1) Mirage fuselages on pillars.
  **Not recorded**: the Mirage fin marked C-411 at the Mercado Central (a fin only, May 2025); Pinamar TC-63 crew monument (no airframe).
- **Composites/hybrids with the story**: Tandil Meteor "I-057" (C-001 + parts), Reconquista Pucará A-514 (+A-505/A-573), Río Cuarto A-4P C-212 (wings of C-205), Laboulaye "Mirage IIIC" hybrid, Edificio Cóndor "A-4C C-301" (TA-4J-based composite), Bahía Blanca aero-club MS-760 hybrid.
- **Derelicts kept as rows** because they are still visible, with condition stated: Guaraní T-122 at the abandoned San Justo aerodrome, T-28F 0584 at Puerto San Julián, Goya and Neuquén Meteors, Verónica Xavante, Piedra Buena C-45.
- **Civil monuments** (Pass 3 "everything else") are included when on a plinth/gate or otherwise exhibited: Loreto C-46, Rivadavia Navion, Oncativo 737 nightclub (a commercial venue — delete if unwanted), Petión 737 (private school, `restricted`), IAAC 737/F-27, Rafaela Lodestar, Colón Cygnet, La Plata and Neuquén Doves, Pueblo Esther Aztec, Concordia Cessna 320.
- **model/variant conventions** (consistent within Argentina): Argentine designations kept — `IA-58`+A/C/D, `IA-50`, `IA-35`, `IA-63`, `MS-760`+A; US types by US designation (`A-4`+B/C/P/Q/F/M, `T-28`+A/F/S, `T-34`+A with B45 alias, `C-47`, `S-2`+A/E/G/T, `F9F`+-2B, `OV-1`+B/D/V, `UH-1`+D/H, `C-45`+H, `L-188`+C/PF, `P-3`+B); French/Israeli: `Mirage III`+CJ/EA/C, `Mirage 5`+P, `Dagger`+A/B (IAI Nesher in aliases; Finger in model_name where converted); `Meteor`+F.4; `Canberra`+B.62/T.64; `MB-326`+GB (Aermacchi-built) vs `EMB-326`+GB (Embraer-built Xavantes); `Hughes 369`+HE/HM/HS/D.
- **tail_number = true identity**; false markings in aliases and description. Naval aircraft use the 0xxx serial (e.g. 0657) with the x-x-xxx code in aliases; where only the code is known (4-A-136, 4-A-115, 3-H-307, 5-T-22) the code is the tail.
- `year_built` blank throughout (no build dates sourced beyond c/n).
- **Coordinates** (43 of 129 sites): OpenStreetMap/Nominatim positions of the named POI (base, aero club, park, airport, building) — not the airframe. Accepted only where the returned feature was the intended object; town centroids and doubtful matches were discarded. 86 sites have blank coordinates.
- Names: every site name carries the city; slugs are ASCII.

## Excluded, and why (do not re-research)

- **Pending/announced, not arrived**: A-4B for Av. de los Inmigrantes 2400, Retiro (city legislature approval Dec 2025, not installed); Corrientes airport Malvinas monument (announced, page blocked); UH-1H AE-495 for Berazategui (donated Jan 2022, stored in Parque Industrial Plátanos — no emplacement report; AE-495 last photographed at Campo de Mayo 2021 and is not recorded there either).
- **Departed/scrapped**: Ezpeleta C-47 TC-34 (Club Aeromodelista, dismantled Mar 2021, sold); Coronel Pringles SNJ-3 0208 (sold to the USA 1992); Coronel Suárez aero-club SNJ-5C 0462 (now MUAN); Escuela Naval Río Santiago Panther 0455 (to ESMA then sold to the USA); El Palomar C-130Bs TC-57/58/59 and 707s LV-WXL, VR-21, T-95 (scrapped/auctioned; TC-68 returned to service 2018); Boeing 737 LV-ZYN (Aerolíneas cabin mock-up at Ezeiza, not visitable); Tiro Federal La Calera Guaraní T-128 (destroyed as a paintball target, Gaceta 2020); Oro Verde Guaraní T-116 (burnt 2009); Tandil hangar Mirage I-004 (now Dolores, recorded there); Río Gallegos Mara C-633 (now Rufino).
- **Not display**: Comodoro Rivadavia airport F-27 T-45 and Paraná II Brigada F-27s T-43/TC-78 (abandoned/stored), Ezeiza naval station F-28 0740 (abandoned 2014), Rosario airport Metro II and Cessna 401A, San Juan MD-80s, Juárez Celman Queen Air fuselage, La Plata airport police FH-1100, Salar Tolillar A-4B C-209 wreck, private Córdoba Guaraní T-120 (in a house yard), Tucumán "C-130H TC-62" (an AA 2015 lead; TC-62 was destroyed in 1975 — no airframe found), Escuela Naval Río Santiago AT-6A 0206 (1960s "ornament", no modern evidence), Espora Alouette 3-H-309/UH-1H 3-H-303/HU-16 (2013-15 leads, no later evidence), Campo de Mayo Mohawk AE-037 (2013 photo; the airframe is at Santa Romana since 2019), Campo de Mayo G.222s AE-260/261/262 (stored 2014, no display evidence), Chamical/CELPA, Marambio, Ushuaia BAN, Río Gallegos X Brigada, Comodoro IX Brigada base interior: nothing found.
- **es.wikipedia Meteor roster leftovers**: C-029 "on the San Luis city access road in poor condition (2005)" — en.wikipedia says it was being restored for Santa Romana (Pass 1 territory); no 2010s sighting, not recorded. C-037 sent to Río Gallegos, whereabouts unknown since 2005. The 1962 composite Meteor painted C-093 at BAM Comodoro Rivadavia — fate unknown. C-027 "indoors at the Universidad Nacional de Córdoba" contradicts Gaceta/aeron-aves (I-027 at Santa Romana) — ignored.
- **Airworthy, not exhibited**: EAM Escuadrilla Histórica Mentors E-097/E-098, EAA General Rodríguez warbirds (B-25 "Huaira Bajo", Beech 18, Harvard, Broussard), Stearman LV-GLW.

## Blank fields, deliberately

- `tail_number` blank (22 rows): Villa Mercedes, Morteros and Puerto San Julián A-4Fs (spares airframes, false serials in aliases); Leones A-4M (BuNo in aliases); Edificio Cóndor A-4C composite; Las Higueras Dagger; Oliva tail section; Laboulaye Mirage IIIC hybrid; Río Cuarto Pampa; VII Brigada Hughes 369D; EAM T-28A; Sauce Viejo and Carlos Casares T-28As; Bahía Blanca MS-760 hybrid; Campo de Mayo UH-1D (never serialled), OV-1D cockpit, Hiller UH-12E; ET N°4 El Palomar Hiller; Quilmes UH-1H (c/n in aliases) and S-62A; Ataliva Pucará (painted A-574 doubted); Puerto Belgrano Sea King (BuNo in aliases).
- `website` blank except official FAA museum pages.
- `postal_code` only Villa Reynolds (5733).

## Needs a human on site (ranked)

1. **Río Grande Dagger C-414** — at the naval air base (Nov 2022 photo) or already on the "monumentos a los Caídos" site (Mar 2025 report says "será emplazada")? Also confirm the MB-326 0647 roundabout.
2. **EEST N°8 Villa Luzuriaga vs BAM Mar del Plata Meteors** — read the data plates: which is G-5-171 and which G-5-173.
3. **Paraná II Brigada Huanquero** — A-317 (c/n 38) or A-320 (c/n 22)?
4. **BACE Espora** — are Trackers 0511 and Turbo Tracker 0703 and Super Étendard 0752 on the base apron, in the MUAN, or gone?
5. **Old sightings never re-confirmed (2010-2014)**: Merlo Quinta Municipal Meteor I-002, Goya Meteor I-014, Junín Meteor I-038, IUA Pucará A-518, Coronel Vidal MB-326 0615, Luque 0783, Punta Alta 0777, Aeroclub Córdoba Guaraní T-127, Bell Ville Prentice, Carlos Casares and Sauce Viejo T-28s, Bahía Blanca MS-760, Río Tercero Pucará, Pilar (Cba) Pucará, Puerto Belgrano Sea King "76", Punta Indio Beech B80.
6. **Edificio Cóndor / Casino de Suboficiales** — is Meteor C-095 staying at the Casino, and is the "A-4C" now installed on the plazoleta the ESFA composite or the Río Cuarto A-4 announced in 2025?
7. **Área Material Río Cuarto** — identity of the IA-63 Pampa and of the Aero Commander (T-139 or T-134); whether Sabreliner T-11 still exists.
8. **Ataliva Pucará** true identity (painted A-574).
9. **Campo de Mayo** — which UH-1Hs (AE-350/AE-400/0880/3-H-307) are displayed vs merely parked; whether the Museo de la Aviación de Ejército is open to visitors by appointment.
10. **Escuela Naval Militar Río Santiago** — any airframe still on the campus?

## File / row-count table

| File | Rows | With tail |
|---|---|---|
| ar_museums.csv | 129 sites | — |
| campo-de-mayo-army-aviation-displays_aircraft.csv | 14 | 11 |
| museo-tecnologico-aeroespacial-area-material-rio-cuarto_aircraft.csv | 12 | 11 |
| area-material-quilmes-escuela-tecnica-n7-collection_aircraft.csv | 12 | 10 |
| escuela-de-suboficiales-de-la-fuerza-aerea-cordoba-instructional-colle_aircraft.csv | 11 | 11 |
| escuela-de-aviacion-militar-cordoba-displays_aircraft.csv | 7 | 6 |
| vi-brigada-aerea-tandil-bosque-de-los-55-monument-and-heritage-hangar_aircraft.csv | 6 | 6 |
| escuela-tecnica-n8-jorge-newbery-aircraft-collection-villa-luzuriaga_aircraft.csv | 5 | 5 |
| iv-brigada-aerea-el-plumerillo-displays_aircraft.csv | 5 | 5 |
| base-aeronaval-punta-indio-gate-guards-and-plaza-de-armas_aircraft.csv | 5 | 5 |
| (other 119 files) | 1-4 each | — |
| **Total** | **221** | **199 (90%)** |

Display status: 217 on_display, 3 in_storage (Sabre C-124 Mendoza, Sabreliner T-11, Beech B80 0689), 1 under_restoration (C-130H TC-67 Pilar).

## Leads for other agents

- **Pass 1 (museums)**: Oncativo "1880" 737 could be argued either way (recorded here). The Museo Histórico Militar San Rafael, Bariloche memorial, Aero Club Trelew, República de los Niños, Campana automobile museum and Museo Mouras were left to Pass 1 as instructed. Museo Prefectura Naval Tigre — Hughes 369H PA-30 in the gardens (aeron-aves photo 2010), not covered by either pass as far as I can see. Museo Fuerte Barragán (Ensenada) — SNJ-4 0205/1-E-215 "EAN-213", incomplete (aeron-aves 2010) — not in Pass 1's list either.
- **Other countries**: none found.
- **Not recorded anywhere yet, weak evidence**: Parque Mizujo, Colonia Urquiza (La Plata) Dove fuselage LV-LEP (Roll Out Aug 2023); Club de Planeadores Los Caranchos Grunau Baby LV-EEF and Club de Planeadores Tres Arroyos Fleet 10A LV-ZCP (may be airworthy); UH-1H AE-495 at Berazategui (see exclusions).
