# Sweden — research notes
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


## Session-level decisions for Sweden

**66 sites, 353 airframes imported.**

The museums/bases pass and the monuments pass overlapped at 16 sites. In every
case the pair was resolved to a single site record, keeping the institutional
name and the union of airframes; 19 duplicate rows were dropped. Specifics
worth knowing:

- **Karlsborg** was returned as one combined site by the monuments pass and as
  two by the museums pass. Kept as **two** — `Karlsborgs fästning` (Tp 79
  79002, at the parachute ranger camp) and `Karlsborgs garnison F 6` (A 32A
  32259, on the pole at the old wing gate) are different places.
- **Frösön Draken.** The two passes disagreed: 35386 (sv.wikipedia) against
  35388 (Svensk Flyghistorisk Förening plus a dated 2004 on-site photograph).
  Recorded as **35388**, with 35386 kept as an alias and the conflict written
  into the description. Not resolved — needs a reading off the airframe.
- **35584 at Mannaminne** is recorded as J 35J; one secondary source gives
  J 35F-2. Both spellings are in the aliases.
- **Optand** — the JA 37 "roadside marker" at the E14/Rv45 junction and the
  Jämtlands flyg- och lottamuseum airframe 37448 are the same aircraft at the
  same place. One record, at the museum.
- **Ljungbyhed golf SK 60 60132** likewise belongs to Ljungbyheds
  Militärhistoriska Museum and is recorded there, not as a separate site.
- `AD-4W` was split to model `AD-4` + variant `W` to satisfy
  `test_model_does_not_swallow_the_variant`.

**Three sites carry no airframes**: F 14 Förbandsmuseum, Krigsflygfält 16
Brattforsheden and Siljan Airpark Museum. These are real aviation sites whose
holdings could not be established from any reachable source — the blank is
deliberate, not a dropped import, and each needs a collection list.

**Coordinates.** Seven Swedish sites were geocoded after import and are *not*
fixes on the airframe: Flygmuseet F 21 and Le Caravelle Club Arlanda (airport
reference points), Karlsborgs garnison F 6 and the Ljungbyhed training airframes
(airfield reference points), Lansen Campus Airframe Arvidsjaur (airport
reference point), GKN Aerospace Trollhättan and Saab AB Linköping (street
level). Eight more were left blank rather than guessed — the Linköping E4
pylons (three separate interchanges, and it is not established which airframe
stands at which), the Grästorp and Ronneby rest-area Viggens, the Norrtälje
Bloodhound, Eurostop Arlandastad, Fyrisskolan Uppsala and Hässlögymnasiet
Västerås.



---

# Phase 1–2: museums and base collections

# Sweden — Phase 1 & 2 research notes (civil museums, discovery sweep, military base collections)

Compiled 2026-09-10. 52 sites, 330 airframe/vehicle records. The database previously held zero Swedish records, so everything here is new.

---

## 1. Sources and the weight given to each

| Source | Weight | Use |
|---|---|---|
| **sv.wikipedia "Lista över svenska bevarade militära luftfarkoster"** (fetched raw via the MediaWiki REST API, 2026-09-10) | **Primary backbone.** Very detailed, per-airframe, with `Fpl nummer`, c/n, exhibitor, town and provenance prose. Maintained by Swedish enthusiasts and generally serial-accurate. But it is crowd-sourced and **stale in places** — see corrections below. | Supplied ~300 of the 330 airframe records. Every record traceable to a row in that list. |
| **Svensk Flyghistorisk Förening (SFF), "Flygmuseer eller museer med flyganknytning i Sverige"** (flyghistoria.org) | **Primary for site discovery.** The authoritative Swedish list of aviation-related museums — 42 entries with towns and URLs. | The discovery sweep skeleton. Anything not on this list was found via targeted Swedish searches and cross-checked. |
| **Museums' own websites** (aeroseum.se, flygmuseum.engelholm.se, soderhamnflygmuseum.se, flygmuseum.com, arlandaflygsamlingar.se, svedinos.se, f11museum.se, f7museum.se, bungeflygfalt.se, gotlandsforsvarsmuseum.se, robotmuseum.se, stenbacksflygmuseum.com, forcedlandingcollection.se, vannasmotormuseum.se, storforsen.se/rfn-museum, kalixlinjen.se, teknikland.se, fkvf.se, f17kamratforening.se, klubbhus.flygsport.se, siljanairpark.se) | **Highest weight for status, address, access and opening hours.** | Every address, postcode, access_type and closure statement below comes from a museum's own page where one exists. |
| **sv.wikipedia individual museum articles** | Medium. Used for collection composition where the museum's own site gives no list. | Aeroseum, Västerås, F11, F 15, Flygmuseet F 21, Ängelholm, RFN, Jämtlands flyg- och lottamuseum. |
| **sv.wikipedia "Lista över bevarade Saab 35 Draken"** | Medium — used only as a *cross-check* against the main list. Where the two disagree the more detailed/more recently edited main list won, and the conflict is recorded in the airframe's `description`. | See §3. |
| **IPMS Stockholm museum walk-round reports** | Medium-low. Undated on the pages fetched. Used only where nothing better existed (Segelflygmuseet Ålleberg glider list, Ängelholm's Rb 68). Every record derived from them says so in its `description`. |
| **Nominatim / OpenStreetMap geocoding** | Used for coordinates. Only accepted where the returned object was the museum itself, its street address, or the named airfield. Where the geocoder returned only a town centroid, **the coordinate fields were left blank**. |
| **aviationmuseum.eu** | Lead generation only. No fact in either output file rests on it. |

Not reachable in this session: `lmhm.se`, `forsvarsmuseumboden.se`, `linkoping.se` (robots.txt/TLS failures via the proxy), `f13.kamratforening.se` (server error), `sv.wikipedia.org` via WebFetch (cache-only — worked fine over the REST API instead). Where a site could not be fetched directly, a secondary description (IPMS, SFHM, regional tourism board) was used and is named in the record.

---

## 2. Discovery sweep — how the site list was built

Started from the SFF museum list (42 entries), then swept for the categories the SFF list does not cover:
* **flottilj/wing heritage** — F 3, F 4, F 5, F 6, F 7, F 10, F 11, F 12, F 13, F 14, F 15, F 16, F 17, F 21, plus Malmen and Karlsborg.
* **on-base gate guards and air parks** — searched `gate guard`, `flygplan på stolpe`, `flottiljvakten`, `pelare`.
* **airport gate guards** — Luleå, Kalmar, Örnsköldsvik, Visby.
* **company/industry displays** — Saab, GKN Aerospace (ex-Volvo Aero), Innovatum/Saab Car Museum, SCAMA, Flygteknikcentrum.
* **län sweep** — every airframe row in the master list carrying a Swedish town was resolved to a site or explicitly excluded (see §5). No Swedish row was silently dropped.

---

## 3. Corrections made, with evidence

1. **Lockheed Tp 84 Hercules 841 and 843 — the biggest correction.** Swedish Wikipedia lists both as complete aircraft "at Aeroseum, Göteborg". Aeroseum's own press item *"Demontering av Herculesplan på Aeroseum"* (6–7 July 2022) says both arrived from Cambridge **to be dismantled and partly scrapped** under an Armed Forces contract; 841's **forward fuselage** was earmarked for Flygvapenmuseum in Linköping and 843's sections were "being evaluated for public viewing" at Aeroseum. Both records were rewritten: 841 → Flygvapenmuseum, `in_storage`; 843 → Aeroseum, `in_storage`; complete-airframe claim removed. Wikipedia's "C/N 841 / 843" values were also wrong — those are Swedish Air Force *codes*, not construction numbers; the Lockheed c/n (4039, 4628) were moved to `aliases` and the codes into `tail_number`, which is what the museum's own text states.
2. **AJ 37 Viggen 37050 at the F 7 gate — deleted.** The source row itself says "(Borttagen 20140716)" — removed from the gate on 16 July 2014. No current location found. Excluded, not relocated.
3. **J 35J 35496 — Västerås vs Söderhamn.** The dedicated Draken list still shows Västerås flygmuseum. The main list carries the detailed transfer history: ownership passed from Försvarsmakten to Flygvapenmuseum in autumn 2017, and the aircraft was moved to F 15 Söderhamn in autumn 2018 where it is displayed outdoors. Recorded at **F 15 Flygmuseum**; the conflict is stated in the record's description.
4. **J 35J 35616 — Volvo Museum vs Österlens.** The Draken list says Volvo Museum, Göteborg. The Volvo Museum at Arendal **closed permanently in December 2023** (Swedish motoring press, Dec 2023; the collection went to World of Volvo, a different downtown venue). Recorded at **Österlens Flygmuseum** per the main list, with the conflict flagged. Volvo Museum was therefore **not** created as a site, and AJS 37 37058, which the main list also puts there, was **excluded** — its post-closure location is unknown.
5. **J 28C Vampire at Ängelholms flygmuseum — not recorded.** The sv.wikipedia museum article lists a J 28C among "utställda kompletta flygplan", but the IPMS report states the Vampire was on loan from Ljungbyheds militärhistoriska museum and "has been removed due to unclear ownership matters", and the master airframe list assigns no Vampire to Ängelholm. No Vampire record created for Ängelholm.
6. **J 26 Mustang 26020 (Flygvapenmuseum).** Description carries the source's own caveat that this is an ex-Israeli Air Force gift (IDF/AF 54) whose true identity is disputed — the "26020" identity should not be treated as firm.
7. **AJ 37 37016 (Svedinos)** — source itself flags "osäkerhet kring serienr". Carried into the description; the serial is recorded as given but should be treated as unconfirmed.
8. **Hkp 2 02403 (RFN Vidsel)** wears 02203/02409; **J 28B 28219 (F 15)** wears the false serial 28391 and is not to be confused with the real 28391 at Vännäs; **J 35F-2 35528 (Aeroseum)** wears fictitious F 9-00; **AJ 37 37025 (Västerås)** is now incorrectly marked in the 16-series. All four false markings are recorded in `description` and, where they are a distinct designation-like string, mirrored in `aliases`.
9. **Hawker Osprey S 9 (Flygvapenmuseum)** — the source's "S/N = S 9" is the *type* designation, not an individual serial. `tail_number` left **blank**.
10. **Model/variant split.** Every Swedish type was normalised to base designation + separate variant per the brief: `J 35`+`F-2`, `AJ 37`+``, `JA 37`+`DI`, `SK 60`+`B`, `Sk 50`+`B`, `A 32`+`A`, `S 29`+`C`, `Hkp 3`+`C`. Popular names (Tunnan, Lansen, Draken, Viggen, Gripen, Safir) are in `model_name` and repeated in `aliases`, together with the dashless form of every dashed designation.

---

## 4. Judgment calls

* **Nose sections, forward fuselages and simulators are kept**, with the extent stated plainly in the description ("Forward fuselage only", "converted into a simulator"). They are deliberately retained and publicly presented. Examples: J 35J 35606 (nose only, Ängelholm), JA 37 37397 (forward fuselage with a wheelchair ramp, Aeroseum), Draken 35-9 (rocket-sled forward fuselage, Österlens), SF 37 37958 (simulator, F11).
* **Composites and rebuilds are kept, flagged.** S 14 Storch 3815 is built from two airframes. Several S 35E Draken are conversions from J 35D and their donor serials are named.
* **The Andrée balloon Örnen (Grenna Museum)** is recorded as `lighter_than_air` but the description states explicitly that only components and fabric recovered from Kvitøya in 1930 survive — this is *not* a complete airframe. Manufacturer entered as Henri Lachambre (Paris), which is documented.
* **Museum-held airworthy aircraft are kept** (Västerås says most of its ~25–30 aircraft are airworthy; Aeroseum's Hkp 4C 04070/SE-JLY flies). They are a museum's displayed collection.
* **Privately owned flying aircraft are excluded** — see §5.
* **Two co-located Optand sites** are recorded separately (`Jämtlands flyg- och lottamuseum` and `Teknikland`) because both the SFF list and sv.wikipedia treat them as separate operations sharing the Optand site; the wiki explicitly says the flygmuseum is "samgrupperat Teknikland, men med fristående verksamhet".
* **Base gate guards are mine and are recorded as sites** — Blekinge flygflottilj F 17 (A 32A 32151 on its pole in front of the wing guardhouse since 1990), Karlsborgs garnison F 6 (A 32A 32259), Jämtlands flygflottilj F 4 Frösön (J 29F 29401 and J 35D 35386 by the mess building), Malmens flygplats (Hkp 3C 03302 outside the Helicopter Wing HQ, AJSH 37 37904), Valhall Park (J 35F-1 35409 at the former F 10), F 16 Flygmuseum/Ärna (J 35F-1 35490 and JA 37C 37425).
* **Airport gate guards are kept** (Luleå, Kalmar, Örnsköldsvik) — an airport forecourt is not a town square or roundabout.
* **`year_built` is blank on every single record.** No sourced construction, rollout or delivery date was obtained for any individual airframe. Several descriptions carry a *delivery* year from the source prose (e.g. "Delivered 1964"), but that is a delivery date in narrative form and was deliberately not promoted into `year_built`.

---

## 5. Everything excluded, and why

**Closed / departed**
* **Volvo Museum, Arendal, Göteborg** — closed December 2023. AJS 37 37058 and (per one source) J 35J 35616 were there; current whereabouts of 37058 unknown. No site, no records.
* **Gotlands flygmuseum, Visby** — closed. Its aircraft (J 32D 32548, J 35F-1 35429, J 35J 35545, JA 37D 37432, JA 37 37305 nose) dispersed to Bunge, Gotlands Försvarsmuseum and elsewhere; recorded at their current homes.
* **AJ 37 37050** — removed from the F 7 gate on 16 July 2014.
* **J 35J 35572** — was a gate guard at Flygtekniska Försöksanstalten, Bromma; taken down and **scrapped 28 May 2008**.
* **F 17 Kamratförening traditionsrum, Kallinge** — the wing "har beslutat att avveckla traditionsrummet på F 17" (association's own site, planning 2026 activities around lunches instead). Not created as a museum site; the F 17 base gate guard is recorded separately.
* **Teknikens och sjöfartens hus, Malmö** — its AJS 37 37027 was transferred out in 2019 and is now stored at Stenbäcks Flygmuseum. No aircraft confirmed remaining, so no site created.
* **Landskrona Museum** and **Beredskapsmuseet (Djuramossa/Viken)** appear on the SFF list but no airframe could be confirmed at either; Landskrona's Thulin material appears to be photographs and a propeller. Not created as sites — see open questions.

**Currently closed but retained as sites** (because the collection is intact and the closure is temporary)
* **Ängelholms Flygmuseum** — "stängt för renovering 1/9 2025 – hösten 2026", reopening date not announced (museum's own site). Kept, `public`.
* **F 7 Gårds- och Flottiljmuseum** — the booking page states "Bokning är inte möjligt för närvarande". Kept as `appointment`.
* **Arlanda Flygsamlingar** — the collection was put into storage in **September 2023** when Swedavia ended the previous Arlanda location; the association's own site says it "har tills vidare magasinerats och är således inte tillgängligt". Kept as a site with `restricted` access and **all four airframes set `in_storage`** (Junkers W 34 SE-BYA, Sk 15A 5049/SE-BHF, Nord NC.701 SE-KAL, Douglas AD-4W SE-EBB). Address is the Rosersberg store, not Arlanda.

**Operational / privately owned flying aircraft — excluded, listed here so a human can decide**
* **Swedish Air Force Historic Flight (SwAFHF), Såtenäs** — J 29F 29670/SE-DXB, A 32A 32070, J 32E 32542/SE-RMD, J 32D 32606/SE-RME, J 32B 32620/SE-RMF, J 35J 35556/SE-DXR, Sk 35C 35810/SE-DXP, AJS 37 37098/SE-DXN, SK 37E 37809/SE-DXO, SK 60E 60140/SE-DXG, Sk 50B 50040/SE-FVV, SK 61A 61025/SE-FVX, Sk 16A 16028/SE-FUB, Sk 16A 16073/SE-FVU. These are a flying heritage fleet on an active air base, not a display collection.
* **Stiftelsen Flygande Veteraner** DC-3 79006/SE-CFP "Daisy" — airworthy, hangared at Västerås.
* Privately owned airworthy: Sk 25 25084/SE-BMN, Sk 11 517/SE-AMR and 568/SE-ADF (KSAK, Ålleberg — the world's oldest flying D.H.82), Sk 12 629/SE-EGT and 657/SE-BWU, Sk 15 5033/5054/5060/5087, Sk 16 16009/16068/16144, Sk 50 50011/50025/50047/50053/50061/50066/50070/50075/50081/50083/50085 and SE-IRY, SK 61D 61035/SE-LLH, all Fpl 51 Super Cubs, MFI-9B 801-43/45/48/49, B 17A 17239/SE-BYH, Tp 101 101002/SE-KXM.
* Under private restoration, not displayed: Sk 11 553/SE-BYL (Säter), Sk 16 16106 (Uddevalla), Sk 16 16112 and AD-4W SE-EBI (Karlskoga), J 22 22216 and 22236 (Håtunaholm), Hawker Hart wreck, Sk 12 5773 (Ljungbyhed, owner undetermined, stored dismantled).

**Technical-school and fire-training airframes — excluded (not publicly presented)**
FMTS / Försvarsmaktens tekniska skola Halmstad (JA 37DI 37415 and 37428, SK 60C 60009, SK 60B 60049, Hkp 3C 03313, Hkp 10B 10403); Brand- och räddningsskolan Halmstad (AJS 37 37057); Ronneby Flygteknikutbildning (SK 60A 60098/60100/60116, Hkp 3C 03305, Hkp 6B 06049, Hkp 9A 09208/09211/09214); Klippans gymnasieskola, Ljungbyhed (SK 60A 60108, SK 60E 60148); Lapplands flygtekniska gymnasium, Arvidsjaur (J 32B 32611, SK 60B 60050, SK 60D 60131); Hässlögymnasiet, Västerås (SK 60D 60097); Flygteknikcentrum, Västerås (Hkp 2 02201); Nordiskt Flygteknikcentrum, Luleå (SK 60D 60052, Hkp 3C 03303/03308); Flygteknik Technical Training, Nyköping/Skavsta (SK 60C 60001, Hkp 2 02409); Combitech Arboga (JA 37 37309, an antenna-measurement rig). Also excluded: the F 7 Såtenäs fire-training dump (J 35A 35073, J 35F-2 35504, 35519, 35535) — a scrap line, not a display.

**Roadside plinths, roundabouts and advertising pylons — handed to the other agent**
* **The E4 line at Linköping** — six aircraft on poles along the motorway, recorded here so they are not lost: **J 29F 29441, J 32E 32507, J 35F 35477, JA 37 37367, Sk 50B 50016, SK 60B 60080.** Linköpings kommun maintains a public page about them ("Flygplan längs E4:an"), which could not be fetched here (robots.txt).
* **AJS 37 37072**, Grästorp, riksväg 44 at the Tun exit (wings and fin from 37958).
* **JA 37DI 37440**, Sörby rastplats on the E22 near Kallinge, erected 24 May 2014.
* **A 32A 32094 "Gul Petter"**, at the entrance to Flygstaden, Halmstad since 14 December 2019 — a composite of 32094 and 32025 (earlier 32094 + 32127).
* **Kareby Bil AB, Kungälv** — S 29C 29945 and J 35B 35248 as commercial advertising pylons.
* **Biltema Luleå** — AJSH 37 37927.
* **AJS 37 37031**, gifted to Söderhamns kommun in 1995 — exact display location unverified, so excluded rather than guessed.

**Other exclusions**
* **J 35J 35531** (Novelair AB, Gävle) and **JA 37 37305** (private individual, Skövde) — nose sections in private company/individual hands being turned into simulators, not publicly presented.
* **Hkp 3C 03316** (Jeep Tom Event, Timrå) — privately owned since 2021.
* **F 13 Kamratförening, Norrköping** — JA 37 37366 and a J 35F-2 35609 nose simulator are held there, but access arrangements could not be confirmed (site returned a server error). Excluded pending confirmation.
* **"Ljungby maskin"** rows in the source (an unidentified "29?" and an unidentified "35?") — no serial, no type, no confirmed location. Excluded.
* **Grenna's Örnen** kept but flagged as remains, not an airframe (see §4).

---

## 6. Fields deliberately left blank

* **`year_built` — blank on all 330 records.** No sourced construction/rollout/delivery date per airframe was obtained. Serials were never converted into years.
* **`tail_number`** blank where the source gives none or gives a type designation instead of an individual (Hawker Osprey S 9; all Segelflygmuseet gliders; Aeroseum's Twin Bonanza/MFI-15/DH.60/BHT-1/SG 38; Västerås's Chipmunk/Apache/Heron/Yak-52/Anfänger; F11's Bergfalke and Holmberg Racer; Ängelholm's Rb 68; the Örnen balloon).
* **`aircraft_name`** blank except where a name is documented: Munin (Tp 79 79002), Jubileumsflygplanet (J 29F 29507), Johan Blå (J 35J 35540), Petter Blå (JA 37D 37432), Örnen.
* **Coordinates blank** for 9 sites where geocoding returned only a town centroid or nothing usable: Flygmuseet F 21, F 14's precise museum building, Saab AB Linköping gate, GKN Aerospace Trollhättan, Karlsborgs garnison F 6, Eurostop Arlandastad, Le Caravelle Club Arlanda, plus a few company sites. **No coordinate was guessed.**
* **`postal_code` and `address`** blank where no source states them (several base and airport entries).
* **`variant`** blank where the type has no sub-variant or where the source records none (e.g. AJ 37, AJS 37, SF 37, J 33, Hkp 2).

---

## 7. Open questions needing a human on site

1. **Lockheed Tp 84 841 and 843.** How much of each airframe actually survives after the 2022 Aeroseum dismantling, and is 841's forward fuselage now at Flygvapenmuseum in Linköping or still in store? Both records are `in_storage` on that assumption.
2. **Ängelholms Flygmuseum reopening and post-renovation content.** Closed 1 Sep 2025 → autumn 2026, no reopening date announced. Which of the 13 recorded airframes (including the J 22A, JAS 39A 39101, Draken 35606 nose and 35630, Sk 60B 60082, SK 61A 61006, Hkp 3B 03424, Re.2000 tail section 2305) are still on site, and is the Rb 68 Bloodhound still outdoors?
3. **AJS 37 37058 (ex-Volvo Museum) and J 35J 35616.** Where did each actually go after the Arendal museum closed in December 2023? Two sources disagree about 35616 (Volvo vs Österlens) and 37058 has no confirmed home at all.
4. **F 7 Gårds- och Flottiljmuseum, Såtenäs.** Bookings are shown as unavailable. Is it temporarily or permanently closed, and are J 32D 32603 and the JAS 39A 39113 outside the guardhouse still in place? Access is via a military skyddsobjekt and requires the wing's permission.
5. **Arlanda Flygsamlingar.** Where physically are the four airframes now (Rosersberg store address is the association's contact address, not necessarily the airframe store), and is there any prospect of re-display? Also unresolved: whether Caravelle 85210 is still with Le Caravelle Club at Arlanda and how a member of the public can see it.

**Second tier of open questions**
* Does **Landskrona Museum** hold an actual Thulin airframe or only photographs, drawings and a propeller?
* Does **Beredskapsmuseet (Viken)**, **Marinmuseum (Karlskrona)**, **Fästningsmuseet (Karlsborg)** or **Bodens Försvarsmuseum**'s indoor exhibition hold any airframe beyond the two Hkp 3 recorded at Boden?
* **Siljan Airpark Museum** (Siljansnäs) is a recently opened homebuilt/experimental aviation museum and is recorded as a site with **no airframes** — its inventory is not published anywhere reachable.
* **Krigsflygfält 16 Brattforsheden** is recorded as a site with no airframes; it preserves the field, barracks and aircraft shelters. Is any airframe or replica displayed in the shelters?
* **F 14 Förbandsmuseum, Halmstad** is recorded with no airframes — it is a traditions room inside a military area (two weeks' notice, ID check at the guard). A VR walkthrough exists; a physical airframe inventory does not.
* **F11 Museum's "Caproni"** — the museum's own page mentions a Caproni among the exhibits but the airframe list gives seven aircraft that do not include one. Fragment? Model? Not recorded.
* **Arboga Robotmuseum** holds "most Swedish missile systems from the late 1940s to the 2000s" but publishes no inventory; only its three aircraft (J 35B 35244 nose simulator, J 35Ö 35373, AJSH 37 37910 nose) are recorded. A missile inventory needs an on-site visit.


---

# Phase 3: monuments and plinths

# Sweden — Phase 3 (standalone monuments and plinthed aircraft) — research notes

Scope worked: aircraft displayed **outside** museums and **outside active air-base gate parks** —
roadside and roundabout plinths, civil-airport gate guards, school/technical-college airframes,
veterans'/kamratförening displays, company and commercial display airframes, park aircraft.

**Result: 30 sites, 42 airframes.**

---

## 1. Sources and weight

| Source | Weight | Notes |
|---|---|---|
| **Svensk Flyghistorisk Förening — "Förteckning flygminnesmärken", type "Bevarade flygplan (ej museer)"** (`https://flyghistoria.org/forteckning-flygminnesmarken/`) | **Primary / highest** | 234 memorial records, 29 of them under "preserved aircraft (not museums)". The compilation was begun by Försvarsmakten and is now maintained by SFF. This is the single best national inventory for exactly this phase and it is the backbone of the site list. Note the live page is the index at `/forteckning-flygminnesmarken/`; the URL that search engines return (`/for-flygintresserade/forteckning-flygminnesmarken/bevarade-flygplan-ej-museer/`) is dead (404) — the whole dataset is embedded inline in the index page's `mm-card` elements. |
| **sv.wikipedia "Lista över svenska bevarade militära luftfarkoster"** | **High** | Per-airframe master list with fate, custodian and location. Best cross-check on identity and on *removal*. |
| **sv.wikipedia "Lista över Saab 37 Viggen"** | **High** | Per-individual Viggen list with delivery/withdrawal dates and codes. Contains removal/scrapping information the SFF list has not caught up with. |
| **sv.wikipedia "Lista över bevarade Saab 35 Draken"** | Medium | Useful but demonstrably incomplete for Sweden — it omits the Ängelholm, Kalmar, Frösön, Kareby, Rinkaby and Kulltorp airframes entirely. Do not treat its silence as evidence of absence. |
| **en.wikipedia "List of surviving Saab 35 Drakens"** | Medium | Independent confirmation of 35404 (Kalmar), 35409 (Ängelholm), 35477 (Linköping E4), 35583 (Västerås). |
| **corren.se, "Sju flygplan på pelare vid E4"** | Medium | Confirms the Linköping E4 installation: **seven** Saab aircraft on ten-metre pylons near the three E4 interchanges serving Linköping, a permanent municipal exhibition costing ~4 MSEK, created for the 2003 centenary of powered flight. Does not name the airframes — the seven serials come from SFF. |
| **JetPhotos photo 11921318** | Corroborating | 35388, Saab J-35D, location "Östersund Frösön – ESNZ", dated 5 March 2004. Used to break the Frösön serial conflict. |
| **Nominatim / OpenStreetMap** | Coordinates only | All coordinates in FILE 1 are POI- or street-level geocodes of the display location, never invented. |

**Sources tried and rejected:** aviationmuseum.eu (lead-generation only, not cited). Overpass/OSM `historic=aircraft`
returns 23 hits inside the Swedish bounding box but **every one is in Finland** — Swedish plinth aircraft are
essentially untagged in OSM, so that route yielded no Swedish coordinates. `spottingmode.com/wro` and aerialvisuals
were not reachable/productive within the time budget and are listed as open questions below.

---

## 2. Corrections made, with evidence

- **Luleå / Biltema Viggen — SFF prints "AJSH 37 Viggen, Fv-nr 35927".** That is impossible: a Viggen cannot
  carry a 35xxx serial. sv.wikipedia's Viggen list gives **37927**, "Bevarad på pelare utanför Biltema i Luleå",
  delivered 28 Dec 1978, withdrawn 14 Nov 1997, code 21-63. **Recorded as 37927.**
- **SFF files Linköping, Malmen and Östergötland under "Västmanland".** Wrong. Linköping and Väderstad are
  **Östergötlands län**; recorded correctly.
- **SFF still lists an AJ 37 at Innovatum, Trollhättan (37034).** sv.wikipedia's Viggen list: *"F.d. utställt i
  Trollhättan, nedmonterat och skrotat i Vetlanda juni 2017."* The SFF entry is stale. **Excluded** (see §4).
- **SFF still lists AJ 37 37050 as a gate guard at F 7 Såtenäs.** The master list records *"(Borttagen 20140716)"*.
  Excluded on both grounds (removed, and active base).
- **Frösön Draken serial conflict.** SFF says **35388** on a pole at the former F 4. sv.wikipedia's master list
  says **35386**, gate guard by the mess building, placed on its pole in 1986, with a circumstantial story about
  a strap breaking and the nose being damaged during the lift. A JetPhotos image of **35388** is logged at
  Östersund/Frösön in 2004. I recorded **35388** in `tail_number` and carried **35386** in `aliases`, with the
  conflict stated in the description. This is the single weakest identity in the set.
- **Halmstad Lansen is a composite.** Recorded as **32094** (the identity both SFF and the master list lead with),
  with **32127** and **32035** in aliases, and the rebuild stated in the description. It moved from inside the
  FMTS/F 14 area to the public Karlsrovägen roundabout at Flygstaden, re-inaugurated **14 December 2019** — so
  this one is now firmly in Phase 3 scope rather than a base gate guard.
- **Grästorp Viggen is a composite too:** 37072 with wings and fin from **37958** (37958 itself survives as a
  simulator at F11 Museum). Recorded 37072, 37958 in aliases.

## 3. Currency — is it still there in 2025–26?

- **Luleå Airport S 35E 35949 — verified still present.** Taken down March 2019 for restoration, **back on its pole
  20 November 2019**. This is exactly the kind of removal that could have been mis-reported as a scrapping.
- **Halmstad A 32A 32094 — verified present**, re-inaugurated December 2019 on its new roundabout.
- **Arvidsjaur J 32B 32611 — verified moved spring 2022** onto the aviation school grounds (previously beside the
  Arvidsjaur Airport runway for ~18 years).
- **Väderstad J 35F-2 35566 — verified moved 2022** from Vännäs motormuseum to SCAMA.
- **Trollhättan/Innovatum 37034 — verified gone (scrapped Vetlanda, June 2017).**
- **Såtenäs 37050 — verified removed 16 July 2014.**
- The remainder rest on the SFF compilation (actively curated, "uppdateras löpande") plus the master list. I could
  **not** obtain dated 2024–26 photographic or Street View confirmation for every individual plinth within this
  pass; §6 ranks the ones where that gap matters most.

## 4. Exclusions, with reasons

**Removed or scrapped**
- **AJ 37 37034, Innovatum Trollhättan** — dismantled and scrapped at Vetlanda, June 2017.
- **AJ 37 37050, F 7 Såtenäs gate** — removed 16 July 2014.
- **J 35F 35498, Rinkaby** — formerly displayed marked "F 10 – 69"; later scrapped. (35582 replaced it and *is* recorded.)

**Active air bases / base air parks — Phase 2, not Phase 3**
- **Uppsala–Ärna (F 16 / Luftstridsskolan, now an active wing again):** J 35F-1 **35490** gate guard on the base,
  and JA 37C **37425** on a pole inside Ärna airfield since summer 2006.
- **Såtenäs (F 7, active):** J 32D **32603**, JAS 39A **39113** outside the guardhouse.
- **Kallinge (F 17, active):** A 32A **32151** on a pole in front of the wing guardhouse since 1990.
  *(The Ronneby/Sörby E22 rest-area Viggen 37440 IS included — it is a public roadside plinth, not the base gate.)*
- **Luleå–Kallax (F 21, active):** S 29C **29929** at the wing entrance.
  *(The Luleå civil-terminal Draken 35949 and the Biltema Viggen 37927 ARE included.)*
- **Malmen (Helikopterflottiljen, active):** Hkp 3C **03302** on a plinth in front of the wing HQ.

**Inside or belonging to a museum (would duplicate a Phase 1 record)**
- **Hkp 3 03301, Försvarsmuseum Boden** — gate guardian *of* the museum.
- **J 35J 35598, Aeroseum, Säve** — gate guardian *of* Aeroseum, on Aeroseum's approach. Judgment call; excluded to
  avoid double-counting. If the importer treats museum gate guards as separate monument records, add it back.
- **S 35E 35916 / S 35E 35959, F11 Museum Skavsta; J 35J 35604 and Sk 37 37801, RFN Museum Vidsel; J 35J 35624,
  Bunge; 35545 and 37432/37972, Gotlands försvarsmuseum; 35945, Autoseum Simrishamn; 35551, Kalixlinjens museum;
  35606/35630/37976, Ängelholms flygmuseum; 35496/35555/37080, Västerås flygmuseum; 37009/37056/37067, F 15
  Flygmuseum; 35612/37027/37800, Stenbäcks flygmuseum; 35616/37058, Volvo Museum; 37410, Österlens flygmuseum;
  Arboga robotmuseum airframes** — all museum holdings.
- **Rb 02 and CT 20 target drones at the RFN/Vidsel base entrance** — inside the closed test-range perimeter and
  effectively part of the RFN museum estate. The **Rb 340 on the public square in Vidsel village IS included.**

**Not display airframes**
- **Fire-training hulks:** J 35A 35073, J 35F-2 35504, 35519, 35535 (F 7 Såtenäs fire ground); J 35D 35391
  (Kalmar fire brigade training ground); AJS 37 37057 (Brand- och räddningsskolan, Halmstad).
- **FMTS Halmstad JA 37DI 37415 and 37428** — since 2015 hands-on teaching rigs for basic airframe/aerodynamics
  instruction inside the garrison, not displays.

**Insufficient evidence to create a record**
- **Esrange, Kiruna.** SFF says only *"gate guardian vid raketuppskjutningsbasen Esrange i Kiruna."* No type, no
  identity, no confirmation it is an aircraft rather than a launcher or a rocket. Left out; see §6.
- **J 35D 35329, "på privat område i Landfjärden."** Single archived JPEG as the only reference; no current status.
- **J 35J 35572** — "var en tid uppställt som gate guard" at FFA Bromma (past tense); F 18 kamratförening wanted it
  for Tullinge; outcome unstated.
- **JA 37 37319** — sv.wikipedia itself writes *"Bevarad vid Fyrisskolan Uppsala?"* with a question mark. Only the
  firmly-attested **37921** is recorded at Fyrisskolan.
- **JA 37 37301** — master list says "Deponerad till gymnasieskola" (Linköping) while the Viggen list says preserved
  at Flygvapenmuseum. Contradictory; no record created.
- **AJSF 37 37358 nose at Kreativum, Karlshamn** — science centre, nose section, indoor/outdoor status unknown.

## 5. Deliberate blanks and judgment calls

- **`year_built` is blank on every row.** No source consulted gives construction years for these individuals, and
  Swedish Fpl numbers are *not* years. Delivery and withdrawal dates, where known, are written into `description`
  instead — they are not build dates.
- **Coordinates are blank for 11 sites.** Where Nominatim returned only a *municipality centroid* (Grästorp,
  Norrtälje, Arvidsjaur, Karlsborg municipality) I left the field blank rather than pass off a centroid as a fix.
  Every coordinate that IS present is a POI or street geocode of the actual display location. Halmstad
  (56.675347, 12.838356) is a **street-level** fix on Karlsrovägen, not the roundabout itself.
- **`variant` for the Draken** is recorded at sub-mark level where sources give it (`F-1`, `F-2`, `D`, `B`, `J`, `E`),
  with the base designation split off as `model` (`J 35`, `S 35`). Viggen marks are carried whole in `model`
  (`AJ 37`, `JA 37`, `AJSH 37`, `AJSF 37`) with empty `variant`, since the letters denote role, not sub-mark.
- **Karlsborg is one site with two airframes** (A 32A 32259 at the old F 6 gate; Tp 79 79002 at the parachute
  ranger camp). They are a few hundred metres apart inside/adjacent to an active garrison; `access_type` is
  **restricted**. Split into two sites if the importer prefers strict one-plinth-one-record.
- **Linköping E4 is one site with seven airframes** although the pylons stand at three different E4 interchanges.
  SFF treats it as one installation and it was commissioned as one municipal exhibition; coordinates left blank
  because no single point represents it.
- **Optand (JA 37 37448)** is a roadside signpost at the E14/Rv 45 junction that happens to sit *immediately beside*
  Teknikland / Jämtlands flyg- och lottamuseum. Included as a roadside monument, but **flag for de-duplication**
  against any Teknikland museum record.
- **Mannaminne (35584) and Vännäs motormuseum (03307)** are museums, but *not aviation* museums, so there is no
  Phase 1 record to collide with and both airframes are outdoor standalone displays. Included, flagged.
- **High Chaparral, Kulltorp**: J 29F 29589 stands outdoors at the entrance; J 35B 35220 hangs from the ceiling of
  the souvenir shop. Both recorded `on_display`; `access_type` for the site is `public` on the strength of the
  outdoor Tunnan.
- **Kareby Bil (29945 + 35248)** are commercial advertising pylons at a car dealership on the old E6 — exactly the
  "commercial display aircraft" class, and squarely in scope.
- **Bloodhound at Norrtälje** recorded as `missile_rocket` / `surface_to_air`, manufacturer Bristol, variant "1"
  from SFF's "försökslvrobot Bloodhound 1". I deliberately did **not** assign a Swedish Rb designation — the Swedish
  service Bloodhound designation is not something I could confirm for this trials round.
- **Polismuseet helicopter**: SFF says "Agusta-Bell 2006 a/b", an obvious typo for AB 206. Recorded as AB 206A,
  military `Hkp 6B` **06045** in aliases; `military_civilian` = military because the airframe's true identity is the
  Air Force Hkp 6B, with the police markings noted in `description`.

## 6. Open questions, ranked

1. **Frösön Draken: 35388 or 35386?** Two authoritative Swedish sources disagree by one digit, and the sv.wikipedia
   entry carries the more circumstantial detail (placed 1986, nose damaged during the lift) while SFF plus a 2004
   on-site photograph support 35388. Resolve with a dated close-up of the plinth placard or the airframe's fin.
   Currently 35388 in `tail_number`, 35386 in `aliases`.
2. **2024–26 physical confirmation for the plinths not independently re-verified**, in priority order:
   Kareby Bil (29945 + 35248 — a private dealership; ownership changes routinely end such displays),
   Kulltorp/High Chaparral (29589), Rinkaby (35582 — behind a photography ban, hardest to verify),
   Ljungbyhed golf (60132), Söderhamn (37031), Grästorp (37072), Frösön (29401 + Draken).
   Google Street View and satellite imagery would settle most of these quickly; I could not exercise imagery in
   this pass.
3. **Esrange, Kiruna — what is the "gate guardian"?** SFF asserts one exists but names no type. If it is an
   airframe this is a missing site; if it is a sounding rocket it is a missile_rocket record. Needs a photo.
4. **Which of the seven Linköping E4 pylons stands at which interchange?** Needed to give the site a coordinate,
   or to split it into three sites. corren.se confirms the count and the three-interchange layout but names no
   airframes; SFF names the seven airframes but gives no positions.
5. **Towns from the brief that produced no plinth at all: Nyköping, Norrköping, Växjö, Umeå, Sundsvall, Örebro,
   Jönköping, Gävle, Hudiksvall, Visby, Skövde, Boden (town), Kiruna (town).** The SFF national compilation lists
   no "bevarade flygplan (ej museer)" entry for any of them, which is meaningful negative evidence from a
   Försvarsmakten-derived inventory — but it is negative evidence, not proof. Nyköping's and Visby's airframes are
   accounted for by museums (F11 Museum, Gotlands försvarsmuseum, Bunge). Norrköping/Bråvalla holds 35609 with the
   F 13 kamratförening as a simulator, not a display.

## 7. Secondary open items (lower priority)

- Confirm whether **J 35J 35598 outside Aeroseum** should exist as its own monument record.
- Confirm the status of **35572** (ex-FFA Bromma) and **35329** (Landfjärden).
- Confirm whether **37319** joins **37921** at Fyrisskolan.
- Postal codes are populated for only 13 sites (from geocoder output); the rest are blank rather than guessed.
