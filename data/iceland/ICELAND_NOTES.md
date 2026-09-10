# Iceland — research notes
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


## Session-level decisions for Iceland

**6 sites, 48 airframes imported.**

The judgment call that matters is **Sólheimasandur**, and it was made
deliberately: **included**. The C-117D 17171 is a 1973 crash site, which would
normally fail the display test, but the landowners have closed vehicle access,
built a paid car park and run a commercial shuttle, and have stated they intend
to keep a DC-3 on the sand. That is deliberate retention plus continuous public
presentation. The second aircraft there, **DC-3 TF-ISB "Gunnfaxi"**, was trucked
onto the sand in June 2025 purely as a display and is monument-class, not a
wreck. Eyvindarholt is included on the same reasoning — a fuselage hauled 716 km
and given a car park.

Excluded, with reasons: the Eyjafjöll B-17G (glacier wreckage), the Höfn R4D-8
(private cottage), the Vík An-2 hulk, and four derelict or instructional
airframes at Reykjavík Airport.



---

# Research pass

# Iceland — preserved and displayed aircraft: research notes

Research date: 10 September 2026. Database previously held zero Icelandic records.
Result: **6 sites, 48 airframes.**

## 1. Sources and weight

| Source | Weight | Use |
|---|---|---|
| flugsafn.is `/is/safngripir` ("Loftför til sýnis í safninu") | **Primary** | Museum's own aircraft descriptions in Icelandic. Used for registrations, histories, build years, and airworthy-so-sometimes-absent caveats. Scraped in full 2026-09-10. |
| spottingmode.com/wro (Wrecks & Relics online), Iceland planes + locations | **High** | 43 airframes, 12 locations, with c/n, status codes and coordinates. Akureyri location last updated 19 Mar 2025; Eyjafjöll 9 Apr 2026. This is the only source that enumerates the museum's *outdoor/stored* airframes that the museum site omits. |
| Vísir (visir.is) 2025 news series on Gunnfaxi TF-ISB | **Primary, current** | Establishes the June 2025 placement of a second DC-3 on Sólheimasandur and the unresolved dispute with Skógasafn. |
| planewreck.is and eyvindarholt.is (operator sites) | **Primary for site**, weak for identity | Establish the Eyvindarholt DC-3 as a deliberately relocated, ticketed public display. Give type (C-47J / R4D-6), build year 1944, USN Keflavík service, 25 July 1969 accident near Sauðanes. Do not give a BuNo. |
| en.wikipedia "1973 Sólheimasandur Douglas C-117D crash" | High | BuNo 17171, msn 43309, ex-R4D-5 msn 12554 converted Nov 1951, crash 21 Nov 1973, coordinates. |
| keilir.net news item "Phantom F4 Jet at Keilir Aviation Academy" | Primary for presence | Confirms an F-4E of the 57th FIS "Black Knights of Keflavik" displayed at Ásbrú and maintained by aircraft-engineering students. Serial 72-1407 comes from Wikipedia's displayed-F-4 list, aerialvisuals dossier c/n 4398, and spottingmode — three independent agreements. |
| is.nat.is/orlygshofn and the 2006 ministry report *Skýrsla nefndar um flugsögu og flugminjar á Íslandi* | High | Independently confirm two aircraft (An-2 and a Douglas) in the Hnjótur aviation-heritage collection, and that the aviation collection is legally distinct from Minjasafn Egils Ólafssonar though co-located. |
| Feykir.is 06.02.2025 | Primary, current | The Stóragerði display Piper Cherokee was flipped inverted by a storm in early Feb 2025. |
| mbl.is 10 Feb 2024 / Fiskifréttir | High | TF-LIF Super Puma delivered to Flugsafn Íslands, Feb 2024. |
| findingtheuniverse.com 2026 Sólheimasandur guide | Medium (currency check only) | Confirms both aircraft present, parking 750 ISK via Parka, shuttle 10:00–17:00. |
| aviationmuseum.eu | **Lead generation only** | Its Iceland page 404'd; nothing taken from it as fact. |

## 2. Judgment calls on wrecks

The test applied throughout: **deliberate retention plus public presentation.**

- **Sólheimasandur C-117D 17171 — INCLUDED.** This is a 1973 crash site left in situ, which normally fails the test. It passes here because the landowners have converted it into a managed attraction: vehicle access to the wreck is deliberately closed, a paid car park (750 ISK, Parka app) was built ~4 km north, a commercial shuttle runs 10:00–17:00, and the landowners have publicly stated (Vísir, Aug 2025) that they intend to keep a DC-3 on that spot for tourism. Retention is unambiguously deliberate and the presentation is commercial and continuous. Site coordinates 63.45908 / -19.36483 (the airframe), not the car park (63.49122 / -19.36339).
- **Sólheimasandur DC-3 TF-ISB "Gunnfaxi" — INCLUDED, and this is the newest record in the set.** Bought from Þristavinafélagið by the Sólheimasandur landowners and trucked onto the sand in June 2025 explicitly as a display. Not a wreck at all — it is a deliberately placed monument-class airframe. **Currency risk:** the Vinir Gunnfaxa group set a 1 December 2025 deadline to buy it for Samgöngusafnið í Skógum; the landowners countered that they would only release it if a replacement DC-3 were delivered free of charge. No source found resolving this. A 2026 visitor guide still describes both aircraft on the sand, which is the best currency evidence available. If it has since moved to Skógar, this record needs a new site (Samgöngusafnið í Skógum, Skógar, Suðurland) rather than a deletion.
- **Eyvindarholt C-47J — INCLUDED.** Decisive fact: this fuselage did not crash here. It was damaged near Þórshöfn in 1969 and hauled 716 km across the country to Eyvindarholt around 2023 by a landowner who then built a car park, toilets and a charging point around it and charges 1000 ISK. That is a purpose-built roadside monument, not a crash site.
- **Eyjafjöll B-17G 43-38471 — EXCLUDED.** Crashed 16 Sep 1944; scattered wreckage on/under a glacier, re-emerging as ice melts (spottingmode, updated Apr 2026). No retention decision, no presentation, no access management. Derelict.
- **Höfn R4D-8 17281/281 — EXCLUDED.** Listed by spottingmode as "DC-3 in use as cottage" at 64.39613 / -15.32683. A private summer dwelling on private land. Repurposed, not presented; no public access found. Flagged as an open question below because a converted airframe used as a cabin is arguably preserved.
- **Vík An-2 SP-AOI — EXCLUDED.** spottingmode records only "An-2 fuselage (visible on GE image from 2019)", status stored. No Icelandic-language source, no museum, no signage, no presentation found. Treated as a stored/derelict hulk.
- **Reykjavík Airport airframes — EXCLUDED (4).** TF-JVE Aerolites AL-60B2 (derelict), TF-TPB Cessna 172M (derelict), TF-JMA Piper PA-23-250D (derelict) and TF-HOF Piper PA-23-160 (instructional/"dummy" airframe). Three separate airside/back-lot locations. None is a display. If the TF-HOF instructional airframe is at Tækniskólinn's aircraft-engineering shop it would be a `restricted`-access campus airframe and worth revisiting — this was not confirmed.
- **Junkers F.13 model at Flugsafn Íslands — EXCLUDED.** A hand-built scale model, not an airframe.

## 3. Corrections and cautions

- **Wikipedia's English article on the Icelandic Aviation Museum is thin and partly wrong in emphasis.** It names only ~9 aircraft. The museum's own Icelandic collection index lists ~30, and spottingmode adds eight more airframes the museum website does not publish a page for (TF-LOW Do 28B, TF-ADD Do 228, TF-PZL PZL-101A, TF-KFX Kitfox I, TF-BCW Yak-18T, TF-ART RV-6, TF-ZZZ Ercoupe 415C, N610LC DHC-2 Beaver). Those eight are entered on spottingmode's authority alone — **single-sourced, flag for verification.**
- Wikipedia calls TF-ÖRN the museum's Waco YKS-7. The museum's own page gives its registration as **TF-DRN**, displayed *marked* TF-ÖRN. TF-DRN used as tail_number; "Örninn" recorded as the aircraft_name/alias.
- TF-SIF is a registration that has been used twice by the Coast Guard: the SA-365N Dauphin 2 in the museum, and the Bombardier Dash 8-300 that entered service in 2009 and inherited the marks. Only the Dauphin is in this data.
- TF-JFA: the Icelandic register says "Beechcraft C-45H, built 1953". The museum's own research (via Beech 18 historian Bob Parmerter) establishes it was built in **1942** as an AT-11, s/n 1286, USAAF 41-27441, and rebuilt in 1953 as C-45H 52-10672 with new c/n AF-602. **1942 used as year_built**; 1953 is a rebuild date and the "AF-602" is a c/n, not a year.
- No serial was used as a year_built anywhere in this set.
- **Two Pitts S-1S** are listed (TF-ABJ and TF-PHG). This is not a duplicate — the museum publishes separate pages for both.

## 4. Deliberate blanks

- `year_built` left blank for: TF-LIF, TF-IUB, TF-ESD, TF-EAA, TF-AST, TF-KEA, TF-SUX, TF-CUB, TF-JMH, TF-HER, both Pitts, TF-AZX, TF-DRN, TF-SGL, TF-SBA, TF-SBD, TF-SBB, TF-LOW, TF-ADD, TF-PZL, TF-KFX, TF-BCW, TF-ART, N610LC, TF-LBP, TF-JFP, TF-129, RA-50502, TF-OAA, F-4E 72-1407, C-117D 17171, DC-3 TF-ISB. In every case the sources gave an *acquisition*, *first flight*, *arrival* or *registration* year and no build year. 72-1407 in particular: FY72 is a fiscal-year serial block, not a build year.
- `tail_number` blank for the Grunau 9 primary glider — the museum records no registration for it.
- Coordinates recorded only where spottingmode published a fix or Wikipedia gave one. All six sites have a real fix; none was estimated.
- `postal_code` for Stóragerði given as 566 (Hofsós) on the strength of the museum's Hofsós address; the mapped position 65.80681 / -19.31537 is ~10 km south of Hofsós village, so this is the least certain postcode in the set.

## 5. Sweep coverage — places checked that produced nothing

Searched in Icelandic ("flugsafn", "flugvél á stalli", "varðveittar flugvélar", "flugvélaflak", "flugminjasafn", "minnisvarði flugvél") and in English. **No** preserved or plinth-mounted aircraft found at: Reykjavík Airport (public side), Egilsstaðir, Ísafjörður, Vestmannaeyjar, Selfoss, Höfn town, Vík town, Akureyri town (outside the museum), Reyðarfjörður (Íslenska stríðsárasafnið holds wartime material but no airframe), Samgönguminjasafnið á Ystafelli, Skógasafn / Samgöngusafnið í Skógum (wants Gunnfaxi, has no aircraft yet), Duus Safnahús, or any Icelandic school or flying-club site. Iceland appears genuinely to have only one aviation museum, one aviation-heritage annexe, one gate guard, one auto-museum airframe and two roadside DC-3 monuments.

## 6. Open questions, ranked

1. **Is Gunnfaxi TF-ISB still on Sólheimasandur, or has it gone to Skógar?** The Vinir Gunnfaxa deadline was 1 Dec 2025 and no source found resolves the outcome. This is the single highest-value currency check in the file, and it would create a seventh site if resolved the other way.
2. **Verify the eight single-sourced Flugsafn Íslands airframes** (Do 28B, Do 228, PZL-101A, Kitfox I, Yak-18T, RV-6, TF-ZZZ Ercoupe, N610LC Beaver). Only spottingmode lists them and its Akureyri record was last touched 19 Mar 2025. Several may be outdoor/stored rather than exhibited — display_status for these is an inference, not a sourced fact. TF-ADD and TF-ESD are marked in_storage; the rest were defaulted to on_display.
3. **BuNo of the Eyvindarholt C-47J.** Recorded as 150187 on spottingmode's authority (c/n 20842) but 150187 sits in a 1961-series Bureau Number block, which is an odd fit for a 1944 R4D-6. Neither operator site publishes a serial. This is the weakest identifier in the file — verify or blank it.
4. **Condition and current status of TF-HER at Stóragerði.** Blown inverted in February 2025; no follow-up reporting found. Is it re-erected, scrapped, or still lying over? Entered as on_display.
5. **The Höfn R4D-8 (17281/281) used as a cottage.** Excluded, but a converted DC-3 fuselage lived in for decades is a plausible preservation record if the owner presents it at all. Needs a look at street/satellite imagery and a local source. Also unresolved: whether TF-OAA's DC-6B nose at Hnjótur is exhibited to visitors or merely parked behind the buildings — spottingmode says "stored", the site description says "DC-6 nose section" among the display items.

Lower priority: whether the F-4E at Keilir survived the restructuring of Keilir Aviation Academy (last dated photo evidence via spottingmode is 30 Dec 2022); and whether the four derelict Reykjavík Airport airframes include a genuine instructional exhibit at Tækniskólinn that would qualify as a `restricted` site.
