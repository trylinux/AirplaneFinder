# Norway — research notes
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


## Session-level decisions for Norway

**26 sites, 204 airframes imported.**

One row was **excluded at build time**: the "Hol's der Teufel" primary glider
"Mehank II" at Flyhistorisk Museum Sola. The design is the 1920s RRG/Lippisch
pattern and the Sola aircraft is a Norwegian amateur build; no builder could be
sourced, and the importer requires a manufacturer. Blank beats a guess, so the
airframe is documented here and not in the database. It becomes a row the moment
someone establishes who built it.

The **Doppelraab V LN-GAT** at Norsk Teknisk Museum was recorded with
manufacturer *Raab-Flugzeugbau*, the established builder of the Fritz Raab
design, rather than left unattributed.

Three short RNoAF serials (**588**, **103**, **189**) each appear twice in the
Norwegian package on different types. These are genuinely different aircraft —
Norway's three-digit codes repeat across type systems — and they do not collide
under the database's `(model, tail_number)` key. They are exactly the failure
mode described as open item 1 in PROJECT_STATUS, and they survived only because
the two airframes differ in model.

**Northern Norway was never swept.** Andøya, Evenes, Banak, Værnes, Sørreisa,
Mosjøen, Alta, Tromsø and Notodden yielded nothing in Norwegian-language search
and appear on no compilation. This is the largest suspected gap in the country.

**aerialvisuals.ca returned 404s and a domain-parking redirect throughout this
pass** and could not be used at all. It is rung 4 of the methodology's source
hierarchy and needs re-testing before the next region relies on it.



---

# Research pass

# Norway — preserved and displayed aircraft: research notes

Compiled 2026-09-10. Database previously held zero Norwegian records, so all 26 sites and 205 airframes are new.

## 1. Sources and their weight

### Primary structural source
**spottingmode.com "Wrecks & Relics online", Norway country page and per-location pages**
(`https://www.spottingmode.com/wro/norway/`, then `/wro/location/<id>/`).
Fetched with `curl --ciphers "DEFAULT:@SECLEVEL=0"`; plain WebFetch works too but the country page needs parsing.
56 locations listed; each location page carries a table of registration, c/n, type, operator country, service, status code and a "last seen" month. This was by far the highest-yield source and supplied most serials and all coordinates in FILE 1.

Status codes used by that site and how I mapped them:
- `pre` = preserved → `on_display`
- `std` = stored → `in_storage`
- `i/a` = instructional airframe → generally EXCLUDED (see §4)
- `dlt` / `dum` = derelict / dummy → EXCLUDED
- rows flagged `Removed` = no longer there; I dropped them but used several as movement evidence (see §3)

Caveat: currency is uneven. Location "last update" dates range from **Dec 2012** (Kjeller, Kjevik, Kongsberg, Rygge DHC-8/UH-1) to **Jun 2026** (Bodø). The three big museums were re-surveyed **19 Mar 2025**, which is why I trust their lists most. The base gate-guard entries (Ørland Sep 2023, Rygge Nov 2024, Bardufoss Aug 2017, Sessvollmoen 2017/2019) are the weakest link on currency.

### Corroborating sources, in descending weight
1. **International F-104 Society, "Preserved in Norway"** (`i-f-s.nl`) — type-specialist, gave variant, pole/indoor status and the German provenance of Bodø's 12626. Agreed with spottingmode on all twelve Norwegian F-104s except the Sola pole (see §3).
2. **Museum own sites** — `luftfartsmuseum.no`, `forsvarshistoriskmuseum.no/flysamlingen`, `jaermuseet.no/flyhistorisk`, `kffkjeller.no`, `herdlamuseum.museumvest.no`, `dakotanorway.no`. Good for type lists, addresses and access; **poor for serials** — Norsk Luftfartsmuseum's own aircraft pages are largely placeholders ("Tekst kommer", "Siden er under utvikling"), and the F-16 page has no serial at all.
3. **Norwegian Wikipedia** (`no.wikipedia.org`, fetched via `action=raw` — the rendered domain is cache-only to WebFetch). `Flyhistorisk_Museum_Sola` carries a maintained collection list including stored and under-restoration airframes that spottingmode does not show (Arado Ar 196, Fi 156/MS.502, Ju 52 WNr 6791, An-2, Auster T7, Do 28, Harvard IIB, Olympia Meise, Super Puma LN-OMC). `Forsvarets_flysamling` gave the narrative provenance for the Gardermoen aircraft.
4. **English Wikipedia** `Norwegian Armed Forces Aircraft Collection` — good type-level list for Gardermoen and the source for the Rumpler Taube, PK X-1, Spitfire replica and NIKE missiles that spottingmode omits. No serials.
5. **f-16.net aircraft database, preserved RNoAF** — the only source giving 674 → Bodø museum and 687 → Gardermoen. Corroborated by tu.no ("Dette er flyene som skal fortelle F-16-historien til kommende generasjoner", 2021), which names the same two airframes.
6. **en.wikipedia "List of surviving North American F-86 Sabres"** — useful cross-check; it confirmed eight Norwegian Sabres but **misses two that spottingmode has** (41313 Bardufoss, 41248 Risnes). Treated as incomplete, not authoritative.
7. **tracesofwar.com** — supplied the Grenselandmuseet Il-2 crash narrative (Sennagress, 22 Oct 1944, recovered 1984) and museum coordinates/phone.

### Compilations that proved stale or useless — specifically
- **aerialvisuals.ca is dead.** Both `AirframeDossier/AirframeSearch.php` and `/Search.php` return 404 and the domain now serves a `searchvity.com` parking redirect. It cannot be used at all for this country and should be dropped from the source list until it returns.
- **aviationmuseum.eu** — as instructed, lead-generation only. Its Norway index (`/World/Europe/Norway/index.htm`) lists **seven** sites: Bodø, Gardermoen, Herdla, Longyearbyen (Spitsbergen Airship Museum), Oslo Forsvarsmuseet, Oslo Teknisk, Sola. That is a 27 % view of what actually exists; it has no base collections, no gate guards, no monuments. It generated one lead I would otherwise have missed (Herdla) and one I rejected (Longyearbyen, §4).
- **en.wikipedia "Norwegian Armed Forces Aircraft Collection"** lists a **Saab JA 37 Viggen** front fuselage as a Gardermoen exhibit. spottingmode marks 37393 as *Removed* from Gardermoen and present at Sandefjord/Torp. I followed spottingmode and placed it at Torp. Same pattern for F-86K 41290 (Wikipedia/older lists say Gardermoen; it is at Torp) and DH.82A 151 (was Forsvarsmuseet, then Gardermoen; now Sola).
- **starfighter.no** (Starfighterens Venner) — states "In Bodø there is Europe's only airworthy Starfighter" but the homepage carries no serial or registration. Not usable as a fact; recorded as an open question.

## 2. Judgment calls

**Composites, replicas and repaints.** Recorded per instruction: true identity in `tail_number`, worn marking in `aliases`, explained in `description`.
- Sola F-5A **220** is painted as **14896**; 220 is the true identity.
- Sola **MS.502 540** is a composite airframe wearing German marks SB+UY and is presented as a Fieseler Fi 156 C-2 Storch. Recorded as MS.502 with Fi 156 / Storch in aliases.
- Bodø F-104G **12626** is the ex-Luftwaffe **25+64**; it wears code FN-B on the pole.
- Bodø Catalina **C-FIZO** is a Canadian civil PBY-6A painted as RNoAF **FP535**; Bodø Otter **C-FIKT** is likewise civil, in RNoAF marks AM-O. Both are flagged `military` because they are presented as RNoAF aircraft, with the true civil registration in `tail_number`.
- Torp F-84G **A-803** is Danish, displayed as Norwegian **19803**.
- Sola T-33A **DT-571** and Bell 47 **SE-HME** are Danish and Swedish airframes in Norwegian markings (DP-X, LN-ORB).
- The Gardermoen **Spitfire IX** is an explicit full-scale glassfibre replica; recorded as such with no serial.
- The Gardermoen **Rumpler Taube "Start"** is presented as Norway's first aircraft (1912). I could **not** establish whether the displayed object is the original airframe or a reproduction, so the description says so and no year_built is given.

**Nose and cockpit sections are kept**, since deliberate retention plus public presentation is the test: Åmli (four nose/cockpit sections), Gardermoen CF-104 818 forward fuselage and Mirage IIIS J-2315 forward fuselage, Teknisk Museum Vampire F.3 nose, Bodø Pe-2 nose and RF-84F cockpit, Forsvarsmuseet UH-1B front fuselage, Torp Viggen forward fuselage, Bodø 737 forward fuselage (walk-through exhibit).

**Preserved wrecks are kept where a museum shows them deliberately unrestored**: Bodø Ju 88A-4 0881478, Gardermoen Ju 88C-2 0881033, Herdla Fw 190A-2 5425 ("Gul 16", raised from the seabed at Misje 2005), Grenselandmuseet Il-2, Sola He 115B 2398 (raised from Hafrsfjord 3 June 2012, still in restoration). These are curated exhibits, not field wreckage.

**Mountain and Arctic crash sites are excluded** — see §4.

**Airworthy aircraft are included as site records** where the aircraft is the reason a public collection exists and is publicly shown: DC-3 **LN-WND** at Torp (flown on public pleasure flights each summer), and the Kjeller Flyhistoriske Forening DH.82A 189 / DH.60 LN-KFM which the association keeps "i funksjonsdyktig stand". Marked `on_display`.

**A single airframe is a site.** Kongsberg (one CF-104 on a pole outside GKN Aerospace), Risnes (one F-86K), Trondheim (one F-5B), Kristiansand airport arrivals hall (one Miles Gemini) are each their own record with a `-- <City>` suffix.

**Ownership vs location.** Sites are recorded where the aircraft *is*. The Kristiansand terminal Gemini LN-TAH is a Jærmuseet/Flyhistorisk Museum Sola deposit — the loan is noted in `aliases` and the description, and the record sits at Kjevik. CF-104 800 at Bodø is reported as a Forsvarsmuseet loan; noted in the description.

**Missiles.** Only the two named NIKE rounds at Gardermoen are recorded (`missile_rocket` / `surface_to_air`). The Gardermoen anti-aircraft gun collection and the Sola FuMo 214 "Würzburg-Riese" radar and NM-116 tank are not aircraft and are omitted.

## 3. Corrections made, with evidence

| Correction | Evidence |
|---|---|
| Viggen 37393 moved Gardermoen → Sandefjord/Torp | spottingmode marks it *Removed* at loc 6218 and *present* at loc 6225 |
| F-86K 41290 moved Gardermoen → Torp | same, both locations list it, Gardermoen row flagged Removed |
| DH.82A 151 (c/n 161) moved Forsvarsmuseet → Gardermoen → Sola | Removed at loc 6222 and 6218; no.wikipedia Sola list names "de Havilland DH 82 Tiger Moth 151" |
| F-5A 563 moved Norsk Luftfartsmuseum → Sessvollmoen | Removed at Bodø museum (loc 6219), present at Sessvollmoen (loc 17968) |
| F-5A 896 moved Kjeller → Rygge | Removed at Kjeller loc 17955, present Rygge loc 28816 seen Nov 2024 |
| F-5A 895 moved Rygge hangar B → open Rygge display | Removed at loc 6232, present at loc 26879 (Feb 2023) |
| F-5A 572 moved Bodø air station → Bodø museum | Removed at loc 12373, present at museum |
| UH-1B 079 moved Starfighter Group shelter → Bodø museum | Removed at loc 12372, present at museum |
| UH-1B 580 moved Sola museum → Sola air station | Removed at museum loc 6221, present at loc 12371 |
| F-5B 907 moved Kjevik → Gardermoen | Removed at Kjevik loc 6226, present at Gardermoen |
| Lodestar identity at Gardermoen | spottingmode records `OH-SIR c/n 18-2444 "Gulfstar" as G-AGIH`; en.wikipedia lists the same exhibit as "Lockheed C-60A Lodestar … same batch as the Norwegian WWII Stockholm run aircraft". Recorded as a Lodestar C-60A with the Gulfstar conversion name in aliases |
| Sola Sea King 060 | museum news item (23 Jan 2024) said it arrived Jul 2023 and was **not yet** on display; goal was spring 2024. Recorded `on_display` on the museum's own stated plan — this is the single most likely status error in the file and should be re-checked |

## 4. Exclusions, with reasons

**Instructional airframes at technical schools.** Deliberate retention is present but public presentation is not — these sit in maintenance training halls, not exhibitions. Excluded:
- Bodø videregående skole (F-5A 133, EC120B N451V, Beechjet N870BB) — loc 17940
- Sola videregående skole (F-5A 130, PA-31T F-GFVO, EC120B N454V) — loc 17954
- Skedsmo videregående skole, Lillestrøm (F-5A 131, Cessna 340 SE-GGA, IAR.316B G-CDSJ, EC120B N453V) — loc 17953
- UiT School of Aviation, Bardufoss (F-5A 128, UH-1B 584, Safir 324, EC120B N452V) — loc 17936
- Kjevik instructional pool (F-16BM 690, F-16A J-242, F-16A 81-0683, Sea King 068 fuselage, Lynx 228, Hkp-9A 09201, Jetstream 31 LN-FAJ/LN-FAV). Only RF-84F 17055 and F-5A 902 are carried, because spottingmode flags them as preserved.
If the project's rule is that campus airframes count regardless, these four school sites and seven Kjevik airframes can be added quickly — they are fully serialled above.

**Mountain, sea and Arctic crash sites** — field wreckage, no curation, mostly inaccessible:
Grøvelsjøen He 111H-3 5607; Hansakollen Do 17; Øverlihøgda Ju 52; Longyearbyen Ju 88; Svalbard (77.19N) Ju 88; Jan Mayen Ju 88D-1 430265; Tolga (two Ju 88 wrecks "inside" an unidentified building — ambiguous, see §6).

**Fire trainers, dumps and scrap** — DHC-8-103 LN-WIK fuselage fire trainer at Bodø; Convair CV-440 LN-MAP fuselage at Oslo-Gardermoen (`dum`); Rakkestad's five derelict light aircraft (`dlt`); PA-34 N1402T Bergen (`dlt`); Ørland scrapyard PA-38 LN-BFL; Sea Kings ZH540/541/543 and the second Sola pair, all held for spares.

**Spitsbergen Airship Museum / North Pole Expedition Museum, Longyearbyen** — an aviation museum, and an aviationmuseum.eu lead, but I found no evidence of a preserved airframe or airship envelope. The Ny-Ålesund airship mooring mast is a structure, not an aircraft. Excluded pending confirmation.

**Bergen "Puma (or just a training mock-up?)"** at 60.3947N 5.2532E — spottingmode itself is unsure and gives no serial. Excluded.

**Reed PA-38 LN-NFU** — flagged `pre` but with no context establishing display. Excluded as unverified.

**Narvik Krigsmuseum, Lofoten Krigsminnemuseum, Rørosmuseet** — checked, no evidence of a preserved airframe on show. Not in file.

## 5. Deliberate blanks

- **`year_built` is blank on every row but one** (Kjeller PK X-1, 1955, stated as a construction year in the English Wikipedia entry). No other airframe had a sourced construction, rollout or delivery date I could attach to that specific serial. Norwegian and USAF serials were never converted into years.
- **Postal codes** are the town's code where known and are omitted where the site is inside a military perimeter with no civil address.
- **Addresses** are blank for every gate-guard and air-station record — there is no street address, and the coordinate is the fix.
- **Two Norsk Teknisk Museum airframes were dropped rather than guessed**: `LN-BAH c/n C-2` (spottingmode gives no type at all) and `LN-BWD c/n 1 "Norge C"` (type string not resolvable to a manufacturer). Also dropped: Bodø's `LN-DBW c/n 001 "C.5"`. All three are open questions rather than omissions on the merits.
- **Bodø museum has an F-16 in its own type list** but no serial anywhere on its site; 674 comes from f-16.net and tu.no. If those are wrong the airframe is still there, only the serial is at risk.
- Aliases carry the dashless form of every dashed designation as required (F-104/F104, UH-1B/UH1, RF-84F/RF84, etc.).

## 6. Open questions, ranked

1. **Is the Sola CF-104 717 at the museum or inside the air station?** The IFS list says "Sola AB, preserved on pole since 2014"; spottingmode puts it at the museum location (58.8977N 5.6315E) with the remark "On pole outside". The two points are ~1.5 km apart. One call resolves it. **Flyhistorisk Museum Sola: +47 51 77 60 20 / flyhistorisk@jaermuseet.no.** The same call also settles Q2, Q3 and Q6.
2. **Is Sea King 060 actually on display at Sola yet?** The museum's own January 2024 note said not yet, target spring 2024. Same phone number as Q1.
3. **Which Sola airframes are in store versus on show in 2026?** The Norwegian Wikipedia stored list (An-2 LY-AEQ, Auster T7 WE548, Do 28A-1, Ju 52 WNr 6791, Harvard IIB) has no date. Same call.
4. **The northern and Arctic bases were never swept.** Andøya, Evenes, Banak/Lakselv, Værnes, Sørreisa, Mosjøen, Alta, Tromsø and Notodden produced nothing in Norwegian-language search and none appear on spottingmode. Norway retired the P-3 Orion in 2023 and at least one airframe is widely expected to have stayed at Andenes; I found no source and therefore recorded nothing. This is the largest suspected gap in the file. Best single contact: **Luftforsvarsmuseet / Forsvarets museer**, which owns most base gate guards as loans and would know where each one now stands.
5. **Bardufoss, Sessvollmoen, Kjevik, Kongsberg and Kjeller currency.** Their spottingmode records were last touched in 2012–2019. Every airframe there needs an "is it still there?" pass. The Forsvarets museer loan register would close Bardufoss, Sessvollmoen, Ørland and Rygge in one enquiry.
6. **Is the Trondheim F-5B 241 at Luftkrigsskolen?** The coordinate (63.42997N 10.43625E) falls on the Persaunet military site where the Royal Norwegian Air Force Academy sits, and the site name reflects that, but no source names the school explicitly. Verify before publishing the site name.
7. **What is at Tolga (62.4155N 11.0143E)?** "Various wrecks inside" two Ju 88s, updated Jan 2026 — "inside" implies a building and possibly a small private museum. Excluded for now; if it is a museum it is a new site with two airframes.
8. **Is the Bodø CF-104 800 airworthy?** starfighter.no claims Europe's only airworthy Starfighter is at Bodø but names no airframe. If 800 is airworthy the display_status and the site's nature both change.
9. **Rumpler Taube "Start" at Gardermoen — original or reproduction?**
10. **Types for LN-BAH, LN-BWD ("Norge C") and LN-DBW ("C.5")** — three museum airframes left out of FILE 2 purely because the type string could not be resolved. Norsk Teknisk Museum and Norsk Luftfartsmuseum can each answer for their own.
11. **Skien ZS-EVE Boeing 737-230** — "Eastern Warbirds of Norway" is an odd custodian for an ex-airline 737 and the entry is from Sep 2025. Confirm it is a retained display rather than a parted-out hulk.
12. **Herdla Fw 190 identity.** The museum calls it "Gold 16 / Gelbe 16"; spottingmode gives Werknummer 5425 and code "16yw" (yellow 16). Recorded as 5425 / Gul 16; confirm the Werknummer with the museum.
