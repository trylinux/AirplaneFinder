# ESTONIA, LATVIA, LITHUANIA AND IRELAND — MUSEUMS, BASE COLLECTIONS AND MONUMENTS
All four countries had ZERO records in airplane.museum before this file.
Research languages used: Estonian, Latvian, Lithuanian, Russian (for Soviet-era airframe data), English and Irish.
`region` is the literal string `Europe` on every site.
Evidence current to 10 September 2026 unless a row says otherwise.

**Search-tool note (read this first):** general WebSearch was NOT used — the shared quota was
already exhausted when this pass began, and I did not attempt it. Everything below came from
(a) the Estonian/Latvian/Lithuanian/English Wikipedia `action=query` and `action=raw` APIs,
(b) the Wikimedia Commons `categorymembers` API — the single highest-yield source for Baltic
serials, because the aviation photographers who upload there name their files
`<operator>, <serial>, <type>.jpg`, (c) OpenStreetMap via Overpass, (d) Nominatim forward and
reverse geocoding, and (e) direct WebFetch of institutional websites. Wikidata's SPARQL endpoint
was returning `429 Aggressively rate-limiting to 1 req / min — this rule was created during
active wdqs outage` and was abandoned. overpass-api.de is proxy-blocked as documented;
**maps.mail.ru answered every query on the first attempt** and the `area["ISO3166-1"=...]`
filter worked there, so no Polish/Belarusian/Kaliningrad/Finnish contamination had to be
stripped out of the Baltic sweep.

---

## SITES

name: Eesti Lennundusmuuseum -- Lange
city: Lange
state_province: Tartu maakond
country: Estonia
postal_code: 62115
region: Europe
address: Veskiorg; Lange küla; Kastre vald
website: https://www.lennundusmuuseum.ee/
access_type: public
latitude: 58.28792
longitude: 26.76417
source: Museum's own website www.lennundusmuuseum.ee fetched 10 September 2026 (2026 season dates; contact; published coordinates N58°17'16.5" E26°45'51.01"); et.wikipedia "Eesti Lennundusmuuseum" (full departmental inventory); Wikimedia Commons Category:Aircraft at the Estonian Aviation Museum and its 12 type subcategories (operator+serial filenames); OpenStreetMap node/687057014 and way/603619224 (Tu-134A-3 ES-LTA airframe polygon)
confidence: HIGH — evidence is days old. The museum's own site was live on 10 September 2026 and states the 2026 public season runs 25 April to 25 October (25 Apr–22 May 11:00–16:00; 23 May–13 Sep 10:00–18:00; 14 Sep–25 Oct 11:00–16:00; closed 26.10.2026–24.04.2027; public holidays 11:00–16:00) and already advertises Eesti Lennupäevad 2027 for 12–13 June. Groups and researchers are admitted year-round by prior arrangement on +372 58539093. Founded by Mati Meos; officially opened 14 June 2002 after operating from December 1999; run by Sihtasutus Eesti Lennundusmuuseum. Note the administrative name has changed: older sources say Haaslava vald, which merged into Kastre vald in 2017, and OSM still carries the stale "Haaslava vald, 62101" address string.

name: Lennusadam -- Eesti Meremuuseum
city: Tallinn
state_province: Harju maakond
country: Estonia
postal_code: 10415
region: Europe
address: Vesilennuki tänav 6; Kalamaja; Põhja-Tallinna linnaosa
website: https://meremuuseum.ee/lennusadam/
access_type: public
latitude: 59.45172
longitude: 24.73844
source: et.wikipedia "Lennusadam" (construction history; 1996 heritage listing; 2012 museum opening; explicit statement about the Short 184); Nominatim forward geocode of "Lennusadam; Vesilennuki 6; Tallinn" returning the museum polygon and postcode 10415; Eesti Meremuuseum website meremuuseum.ee reachable 10 September 2026
confidence: HIGH on the site and the building; MEDIUM on the exact aircraft inventory because the museum's own site is a JavaScript application whose exhibit pages did not render to plain text and I did not want to assert an inventory I could not read. The seaplane hangar (39 × 109 m; three 36.4 m reinforced-concrete shell domes) was built 1916–17 to a Christiani & Nielsen design and is the world's first large shell-concrete structure; it has been on the Estonian heritage register since 1996. The Maritime Museum opened the hangar as a museum in May 2012 with over 200 full-size exhibits across more than 5000 m². **The internationally significant object is a REPLICA, not an original** — see NOTES.

name: Eesti Sõjamuuseum -- kindral Laidoneri muuseum
city: Viimsi
state_province: Harju maakond
country: Estonia
postal_code: 74001
region: Europe
address: Mõisa tee 1; Viimsi alevik
website: https://esm.ee/
access_type: public
latitude: 59.50146
longitude: 24.83456
source: OpenStreetMap node/687057502 (museum, addr:street Mõisa tee 1, opening_hours We-Sa 11:00-17:00, phone +372 6217410) and node/10748911031 (separate "Sõjatehnika angaar" / heavy artillery hall at 59.50299, 24.84095, url esm.ee); esm.ee reachable 10 September 2026; et.wikipedia "Eesti Sõjamuuseum – kindral Laidoneri muuseum"
confidence: MEDIUM-HIGH on the institution, LOW on any aircraft. Estonia's national war museum, in the former Laidoner manor at Viimsi, with a separate outdoor/hangar heavy-equipment display about 400 m north-east. I found NO evidence of a fixed-wing or rotary airframe in the collection and have therefore recorded NO aircraft rows for it. It is listed here as a site because it is the obvious place a later pass would look, and because a well-searched zero is worth recording. See NOTES.

name: Ämari lennuki mälestusmärk
city: Ämari
state_province: Harju maakond
country: Estonia
postal_code: 76105
region: Europe
address: Ämari alevik; Lääne-Harju vald
website: 
access_type: public
latitude: 59.25504
longitude: 24.20521
source: OpenStreetMap node/13232245984 (historic=memorial; memorial=aircraft); Nominatim reverse geocode placing it in Ämari alevik; Lääne-Harju vald; 76105
confidence: LOW-MEDIUM. An aircraft memorial exists at this point in Ämari village, about 3 km south of Ämari air base itself, in a publicly accessible village setting (hence access_type public — the base gate is a different matter). The OSM node carries NO type, model, manufacturer or ref tag and I could find no photograph, so the airframe is recorded as Unidentified per the contract rather than guessed. Node last touched 2025. See NOTES for what a single site visit would settle.

name: Tupolev Tu-134 ES-AAP -- Tallinna lennujaam
city: Tallinn
state_province: Harju maakond
country: Estonia
postal_code: 
region: Europe
address: Tallinna lennujaam; Lennujaama tee
website: 
access_type: public
latitude: 59.41537
longitude: 24.87161
source: OpenStreetMap way/603591805 (historic=aircraft; aircraft:type=airliner; name "lennuk Tu-134A-3"; ref=ES-AAP; aircraft:colour=yellow-orange; tourism=attraction; wikipedia=ee:Tupolev Tu-134) — a mapped airframe polygon, i.e. someone traced the actual aeroplane from imagery, not a point guess
confidence: MEDIUM-HIGH on the airframe and its identity; MEDIUM on access. The OSM way carries an explicit registration, which is far better sourcing than a typical monument node. It sits in the Tallinn Airport landside area and is tagged tourism=attraction, so I have recorded it public. Registration ES-AAP was an Estonian Air Tu-134A-3. Last OSM edit 2018–2021 era; I have no 2025–26 photograph, so a re-check is warranted.

name: Piirivalvekopter -- Tallinn (Maarjamäe)
city: Tallinn
state_province: Harju maakond
country: Estonia
postal_code: 11911
region: Europe
address: Kase; Maarjamäe; Pirita linnaosa
website: 
access_type: public
latitude: 59.45526
longitude: 24.84155
source: OpenStreetMap node/12983444768 (historic=aircraft; aircraft=helicopter; operator=PPA; description "Vana piirivalvekopter" — old border-guard helicopter); Nominatim reverse geocode: Kase; Maarjamäe; Pirita linnaosa; Tallinn; 11911
confidence: LOW. A retained ex-Politsei- ja Piirivalveamet helicopter is mapped here by a surveyor who described it in Estonian as an old border-guard helicopter, but no type, serial or host institution is given and I could not confirm whether it is a deliberate outdoor display, a training hulk or a yard-kept airframe. Recorded because the contract is explicit that single displayed airframes are site records, but flagged for verification. Do not import this one without a photograph.

name: Rīgas aviācijas muzejs -- Skulte
city: Skulte
state_province: Mārupes novads
country: Latvia
postal_code: LV-1053
region: Europe
address: Skultes iela 35; Skulte; Mārupes novads
website: http://airmuseum.lv/
access_type: public
latitude: 56.91918
longitude: 23.96046
source: The museum's own site airmuseum.lv fetched 10 September 2026 — front page states "Muzeja jauna adrese: Skultes iela 35, Skulte, Mārupes novads", bus 43 to the terminus, tickets €10 adult / €5 child; lv.wikipedia "Rīgas Aviācijas muzejs" (founding, Talpa biography, eviction and relocation history, full exhibit tables with bort numbers); OpenStreetMap way/976058477 (tourism=museum; charge 7 EUR; email muzej@inbox.lv; phone +371 268 62707; wikidata Q81993) plus ~15 individually mapped airframe nodes inside the compound; Wikimedia Commons Category:Aircraft at Riga Aviation Museum (Skulte) — a photographed post-move inventory
confidence: HIGH that the museum exists, has moved and is open; MEDIUM on which individual airframe survived the move. **This is the entry every directory gets wrong.** The museum was NOT evicted into oblivion: it was required to vacate the old site beside the Riga airport terminal by 31 March 2021, raised donations, agreed terms with Lidosta "Rīga", and physically moved its exhibits to Skulte on **24 August 2021** — beside road V14, still on airport land but roughly 1.5 km west of the terminal. English Wikipedia says "In 2022, the entire museum was moved to Skulte", which is a year late; Latvian Wikipedia's dated citation is the better source. The site is live and ticketed in September 2026. **Two prices are in circulation and disagree**: the museum's own page says €10/€5; the OSM way still says `charge=7 EUR`. Trust the museum. Note also that airmuseum.lv's TLS certificate had expired when tested on 10 September 2026 (`curl` over https fails; http works) — that is a housekeeping lapse, not a closure. Founded 1997 by Viktors Talpa, formerly a Soviet Black Sea Fleet naval aviation engineer and director of the Fricis Canders Young Pilots' Club (club founded 1965); 40 airframes on show in 2012, 47 exhibits by 2018. Described in Latvian sources as the largest collection of Soviet-built aircraft and helicopters outside the CIS.

name: VEF I-12 replika -- Lidosta Rīga
city: Skulte
state_province: Mārupes novads
country: Latvia
postal_code: LV-1053
region: Europe
address: Lidosta "Rīga" 10/1; Mārupes pagasts
website: 
access_type: public
latitude: 56.92302
longitude: 23.97986
source: OpenStreetMap node/13900373921 (historic=aircraft; name "VEF I-12 (replica)"); Nominatim reverse geocode: Lidosta "Rīga"; Skulte; Mārupes pagasts; Mārupes novads; LV-1053; Overpass context sweep confirming the node sits in the landside terminal forecourt among terminal POIs and the "Putnu ceļi" public artwork
confidence: MEDIUM. A replica of the VEF I-12, the pre-war Latvian-designed trainer built by Valsts elektrotehniskā fabrika, displayed at the Riga airport terminal forecourt. The node is recent (2025-26 OSM id range) and explicitly says replica, which is exactly the kind of honesty a monument node usually lacks. No serial; none should exist. Distinct site from the Aviation Museum — this is at the terminal, the museum is 1.5 km west.

name: Mil Mi-26 piemineklis -- Rīga (Dārzciems)
city: Rīga
state_province: Rīga
country: Latvia
postal_code: LV-1073
region: Europe
address: Rēzeknes iela; Dārzciems; Latgales apkaime
website: 
access_type: public
latitude: 56.93603
longitude: 24.18011
source: OpenStreetMap node/10611938808 (historic=aircraft; model "Mi-26T Halo"; model:wikidata Q336150; tourism=attraction); Nominatim reverse geocode: Rēzeknes iela; Dārzciems; Rīga; LV-1073; Overpass context sweep (adjacent business park addressing at Rēzeknes iela 5E)
confidence: MEDIUM. A Mi-26T is retained on open ground in the Dārzciems industrial area of eastern Riga and mapped as a visitor attraction. The type identification is explicit and Wikidata-linked; the ownership and whether it is ticketed are not established. No serial recorded by the surveyor.

name: Antonov An-2 -- Rīga (Valērijas Seiles iela)
city: Rīga
state_province: Rīga
country: Latvia
postal_code: LV-1019
region: Europe
address: Valērijas Seiles iela; Latgales apkaime
website: 
access_type: public
latitude: 56.93962
longitude: 24.15805
source: OpenStreetMap way/1303509411 (historic=aircraft; name "Lidmašīna AN-2"; tourism=attraction) — traced as a polygon, so the surveyor saw the aircraft footprint; Nominatim reverse geocode: Valērijas Seiles iela; Latgales apkaime; Rīga; LV-1019
confidence: MEDIUM. A retained An-2 in eastern Riga, mapped as an attraction. No registration, no owner. The polygon tracing is the reason I trust it exists.

name: Ciemupes lidmašīnu ekspozīcija
city: Ciemupe
state_province: Ogres novads
country: Latvia
postal_code: LV-5001
region: Europe
address: Priežu iela; Ciemupe; Ogresgala pagasts
website: 
access_type: public
latitude: 56.78146
longitude: 24.64956
source: OpenStreetMap nodes 12147569345, 12147569346 ("An-2 Ciemupe Belle"), 12726138633 (model:wikidata Q337467 = Antonov An-24) and 12875031667, all historic=aircraft, clustered within about 30 m of each other; Nominatim reverse geocode: Priežu iela; Ciemupe; Ogresgala pagasts; Ogres novads; LV-5001; Overpass 250 m context sweep (immediately beside the A6 Rīga–Daugavpils trunk road; Ciemupe bus and rail stops; residential addressing at Priežu iela 2B)
confidence: MEDIUM on the existence and rough composition of the cluster; LOW on ownership, name and access. Four airframes are mapped in a tight group beside the A6 at Ciemupe — at least an An-2 (nicknamed "Ciemupe Belle" by whoever mapped it) and an An-24. There is no tourism, amenity, name or operator tag on anything nearby, so I could not establish whether this is a private collection, a roadside attraction or a café. The site name above is descriptive and was coined by me for want of a documented one; treat it as provisional. Nodes are from the 2024–25 OSM id range.

name: Nākotnes parka lidaparāti -- Glūda
city: Nākotne
state_province: Jelgavas novads
country: Latvia
postal_code: LV-3719
region: Europe
address: Nākotne; Glūdas pagasts
website: 
access_type: public
latitude: 56.60807
longitude: 23.45459
source: OpenStreetMap nodes 13460578149, 13460578150 and 13460578151 (all historic=aircraft; no other tags), in a line about 60 m long; OpenStreetMap node/9411400098 "Nākotnes parks" (tourism=attraction) 20 m away; Nominatim reverse geocode: Nākotne; Glūdas pagasts; Jelgavas novads; LV-3719
confidence: MEDIUM on the site, LOW on the airframes. Three aircraft are mapped inside or immediately beside a named public park in Nākotne, Jelgava district. The park is tagged as a visitor attraction, which is why access is recorded public. NONE of the three nodes carries a type, so all three are recorded Unidentified rather than guessed. Nodes are 2025-26 OSM ids, so the survey is recent.

name: MiG-15UTI -- Cīravas lidlauks
city: Cīrava
state_province: Dienvidkurzemes novads
country: Latvia
postal_code: LV-3453
region: Europe
address: Cīrava; Cīravas pagasts
website: 
access_type: public
latitude: 56.73646
longitude: 21.36578
source: OpenStreetMap node/8199786231 (historic=aircraft; model "MiG 15UTI"; model:wikidata Q187377; name "Mig-15 Soviet period fighter jet"; wikimedia_commons=File:Cīravas lidlauks - vecais MIG.jpg — i.e. the surveyor linked a photograph); Nominatim reverse geocode: Cīrava; Cīravas pagasts; Dienvidkurzemes novads; LV-3453
confidence: MEDIUM-HIGH on type and existence — this is one of the few Baltic monument nodes with a linked Commons photograph, whose Latvian filename translates as "Cīrava airfield — the old MiG". Cīrava was a Soviet-era agricultural airfield in Kurzeme. Condition and ownership unknown; the Latvian word "vecais" in the filename suggests a weathered airframe rather than a maintained monument, so a condition check is needed before this is described as restored.

name: Antonov An-2R -- Duči (Limbaži)
city: Limbaži
state_province: Limbažu novads
country: Latvia
postal_code: LV-4020
region: Europe
address: Duči; Mārstags; Limbažu pagasts
website: 
access_type: public
latitude: 57.48485
longitude: 24.66995
source: OpenStreetMap node/7595977501 (historic=aircraft; model "Antonov An-2R"; model:wikidata Q207700; name "Antonov An-2R"); Nominatim reverse geocode: Duči — Limbaži; Mārstags; Limbažu pagasts; Limbažu novads; LV-4020
confidence: MEDIUM. A retained An-2R (the agricultural sprayer variant) on the Duči road outside Limbaži. Explicit variant in the tag, no registration. No photograph linked; node predates 2020.

name: Antonov An-2 -- Bārbele (Bauska)
city: Bārbele
state_province: Bauskas novads
country: Latvia
postal_code: LV-3905
region: Europe
address: Bārbeles pagasts; on the Bauska — Aizkraukle road
website: 
access_type: public
latitude: 56.46317
longitude: 24.61874
source: OpenStreetMap node/9897094506 (historic=aircraft; model:wikidata Q207700 = Antonov An-2, no name tag); Nominatim reverse geocode: Bauska — Aizkraukle; Bārbeles pagasts; Bauskas novads; LV-3905
confidence: LOW-MEDIUM. Type comes solely from the Wikidata model link; there is no name, no registration and no photograph. Roadside An-2s of this kind in Latvia are usually former Aeroflot agricultural aircraft turned into roadside signage or café decoration, but I could not confirm which.

name: Lietuvos aviacijos muziejus -- Kaunas
city: Kaunas
state_province: Kauno apskritis
country: Lithuania
postal_code: LT-46337
region: Europe
address: Veiverių g. 132; Aleksotas
website: https://www.lam.lt/
access_type: public
latitude: 54.87797
longitude: 23.89041
source: Museum's own site www.lam.lt fetched 10 September 2026 — pages /apsilankyk/ekspozicija/ and /apsilankyk/darbo-laikas-ir-bilietu-kainos/ (reopening date, holdings counts, ticket prices, opening hours, branch museums); lt.wikipedia "Lietuvos aviacijos muziejus"; en.wikipedia "Lithuanian Aviation Museum"; OpenStreetMap node/1890213866 (wikidata Q6648354) plus 11 individually mapped airframe nodes inside the compound; Wikimedia Commons Category:Aircraft at the Lithuanian Aviation Museum
confidence: HIGH — evidence is hours old and comes from the museum itself. **The museum reopened on 1 April 2026 after a full reconstruction**, which invalidates every pre-2026 description of its layout; the site even offers a virtual tour of "how the exposition looked before the reconstruction". Hours: Monday 10:00–16:00, Tuesday–Saturday 10:00–18:00 (last admission 30 min before close), closed Sundays and public holidays, EXCEPT the last Sunday of each month when entry is free, 10:00–16:00. Tickets €8 / €4 concession / €12–18 family. Flight-simulator centre €6 per 10 minutes on top of admission. A state museum under the Ministry of Culture; founded 19 February 1990 as Lietuvos technikos muziejus, renamed 1 February 1995; its predecessor public sports-aviation museum was begun by Lithuanian aviators in 1971 and opened in 1983. Over 24 000 accessioned items including more than 50 flying machines; roughly 2 ha of outdoor display. Note: the OSM opening_hours tag (Mo-Fr 09:00-17:00) is STALE and contradicts the museum. Address is on the S. Darius and S. Girėnas aerodrome at Aleksotas — the field the 1933 transatlantic flight was expected to reach.

name: Vytauto Didžiojo karo muziejus -- Kaunas
city: Kaunas
state_province: Kauno apskritis
country: Lithuania
postal_code: 44248
region: Europe
address: K. Donelaičio g. 64; Naujamiestis
website: https://vdkm.lt/
access_type: public
latitude: 54.89996
longitude: 23.91200
source: lt.wikipedia "Vytauto Didžiojo karo muziejus" — the collections paragraph names the "Lituanicos" transatlantic-flight relics among the museum's most valuable holdings, alongside the Balys Buračas negatives and the Silvestras Žukauskas material; Nominatim forward geocode returning the museum at K. Donelaičio g. 64, 44248 Kaunas; en.wikipedia "Lithuanian Aviation Museum" (which states explicitly that the remains of the Lituanica are at the Vytautas the Great War Museum and NOT at the aviation museum)
confidence: HIGH that the Lituanica relics are here and MEDIUM on their present display state. Lithuania's national military museum, founded by order of 15 December 1919, opened 16 February 1921, given the Vytautas the Great name in 1930, and housed since 1936 in a purpose-built modernist complex on Vienybės aikštė designed by Vladimiras Dubeneckis, Karolis Reisonas and Kazimieras Kriščiukaitis. This is the internationally significant record for Lithuania: the surviving structure of the aircraft Darius and Girėnas flew across the Atlantic in July 1933.

name: Įstros aviacijos muziejus -- Stanioniai
city: Stanioniai
state_province: Panevėžio apskritis
country: Lithuania
postal_code: 
region: Europe
address: Įstro g. 4; Stanioniai
website: https://www.aviapark.lt/
access_type: public
latitude: 55.82783
longitude: 24.36087
source: OpenStreetMap node/1324535934 (tourism=museum; museum=transport; fee=yes; opening_hours 08:00-22:00; phone +370 616 86996; website aviapark.lt; Lithuanian and English descriptions supplied by the operator)
confidence: MEDIUM, and read the caveat. The Lithuanian description is unambiguous: "Tai vienintelis Lietuvoje **lėktuvų muliažų** muziejus po atviru dangumi" — the only open-air museum of aircraft **mock-ups** in Lithuania, with an indoor aviation-history exposition; the exhibits are described as fighters, jet trainers and helicopters used in the second half of the 20th century. Open seven days a week all year regardless of weather; paid entry. Because the operator's own wording says mock-ups, **I have NOT recorded any of these as real airframes** — see NOTES and the single flagged Unidentified row. Someone needs to establish on site whether any genuine ex-service airframes are mixed in among the replicas.

name: Aero L-39 -- Zokniai (Šiauliai)
city: Šiauliai
state_province: Šiaulių apskritis
country: Lithuania
postal_code: 77122
region: Europe
address: Lakūnų g.; Margiai
website: 
access_type: public
latitude: 55.89781
longitude: 23.37643
source: OpenStreetMap node/13991937480 (historic=aircraft; manufacturer=Aero Vodochody; model=L-39; aircraft:type "military;jet;fixed_wing"); Nominatim reverse geocode: Lakūnų g.; Margiai; Šiauliai; 77122
confidence: MEDIUM-HIGH on type, MEDIUM on role. An Aero L-39 is mounted on Lakūnų gatvė ("Airmen's Street") in the Margiai district of Šiauliai, on the approach to Zokniai / Šiauliai Air Base — the NATO Baltic Air Policing base. The street name and location make a gate-guard or town-boundary monument the overwhelmingly likely reading, and it is on a public street, hence access_type public. The node is a 2025-26 OSM id, so the survey is recent. No serial recorded by the surveyor; Lithuanian Air Force L-39ZAs carry two-digit tactical numbers, so a serial must not be inferred.

name: Lakūno Stepono Dariaus gimtinė-muziejus
city: Dariaus
state_province: Klaipėdos apskritis
country: Lithuania
postal_code: 96292
region: Europe
address: Dariaus kaimas; Judrėnų seniūnija; Klaipėdos rajonas
website: https://www.lam.lt/susipazinkime/lakunu-gimtines-muziejai/
access_type: public
latitude: 55.59427
longitude: 21.84491
source: OpenStreetMap node/3352713896 (tourism=museum; museum=aviation; museum_type=republican; fee=no; opening_hours Tu-We,Fr-Sa 10:00-17:00, Th 10:00-19:00; phone +370 698 81025; email s.dariausgimtine@lam.lt) plus ways 1427756481 (covered=yes), 1427756482 and 1427756483, all historic=aircraft, inside the site; www.lam.lt exposition page 10 September 2026 confirming it as a branch of the Lithuanian Aviation Museum
confidence: MEDIUM-HIGH on the site, LOW on the three airframes. The reconstructed birthplace farmstead of Steponas Darius, a branch of the Lithuanian Aviation Museum since 1991; house and granary rebuilt by 1993 with a memorial exposition; free entry; VR tours of aircraft interiors offered. Three aircraft are mapped as polygons on the property, one of them under cover, but NONE carries a type tag and I found no photograph, so all three are recorded Unidentified. This is a genuinely surprising find — the standard descriptions of this site mention only the farmstead — and it deserves a site visit.

name: Shannon Aviation Museum
city: Shannon
state_province: County Clare
country: Ireland
postal_code: V14 PH34
region: Europe
address: Link Road; Smithstown
website: https://shannonaviationmuseum.com/
access_type: public
latitude: 52.71385
longitude: -8.87018
source: Museum website shannonaviationmuseum.com fetched 10 September 2026 (opening hours; address; /exhibitions/ page listing both collections); Irish Aviation Foundation CLG collection catalogue at irishaviationfoundation.ie/collection/ — the museum's own accessioned object database, 34 pages, individual records with accession numbers, construction numbers and service histories; RTÉ News 27 August 2026 "Shannon Aviation Museum unveils new Air Corps collection"; FlyingInIreland 13 April 2024 "New Irish Air Corps Aircraft for the Shannon Aviation Museum"; en.wikipedia "List of aircraft of the Irish Air Corps" (per-serial disposal notes); OpenStreetMap node/8742962694 (still tagged under the museum's former name Atlantic Air Venture, same address)
confidence: HIGH, and this is the single most important correction in this file. Open Wednesday to Saturday 10:00–16:00; +353 61 363687. **The Irish Air Corps Museum at Casement Aerodrome closed in 2024 and its collection went to Shannon.** The transfer was announced on 13 April 2024 as a loan of historic aircraft plus engines, propellers, models, photographs and photographic equipment, driven by the Air Corps needing the Baldonnel floor space. The collection went on year-round public display for the first time on **27 August 2026** when the **Eddie Ryan Memorial Wing** was opened by Brigadier General Rory O'Connor, GOC Air Corps — two weeks before this file was written. The museum also bought the land and buildings it had occupied for 18 years, funded by the Michael Guinee Charitable Foundation, so its tenure is now secure. Note the identity trail: the site was **Atlantic AirVenture**, is now **Shannon Aviation Museum**, and its collections-holding company is the **Irish Aviation Foundation CLG** — three names, one place, and OSM still carries the oldest of them. Atlantic AirVenture is therefore NOT a separate site and must not be created as one.

name: Foynes Flying Boat & Maritime Museum
city: Foynes
state_province: County Limerick
country: Ireland
postal_code: 
region: Europe
address: Main Street (N69); Foynes
website: https://www.flyingboatmuseum.com/
access_type: public
latitude: 52.61139
longitude: -9.10990
source: Museum website flyingboatmuseum.com fetched 10 September 2026 ("The museum is open Monday-Sunday, 10am-5pm. Last admission 4pm."); OpenStreetMap node/278940500 (tourism=museum; phone +353 69 65416; email info@flyingboatmuseum.com; wikidata Q22340525); Wikimedia Commons Category:Foynes Flying Boat Museum — 30+ geograph.org.uk photographs of the Boeing 314 exhibit, several of which are captioned "B314 Replica" by the photographer
confidence: HIGH on the site, hours and the nature of the aircraft exhibit. Open daily 10:00–17:00, last admission 16:00. The museum occupies the original 1930s–40s flying-boat terminal and control tower and covers the transatlantic flying-boat era, when Foynes was the eastern terminus; it also houses a Maritime Museum, a Maureen O'Hara exhibition and the Irish Coffee Centre. The Boeing 314 is a **full-size walk-through REPLICA of the Pan American "Yankee Clipper"**, not an original — no Boeing 314 survives anywhere — and it is recorded and flagged as such below.

name: National Museum of Ireland -- Decorative Arts and History
city: Dublin
state_province: County Dublin
country: Ireland
postal_code: 
region: Europe
address: Collins Barracks; Benburb Street; Arbour Hill; Dublin 7
website: https://www.museum.ie/en-IE/Museums/Decorative-Arts-History
access_type: public
latitude: 53.34886
longitude: -6.28668
source: en.wikipedia "National Museum of Ireland – Decorative Arts and History" (site history; the Soldiers and Chiefs military gallery opened 2005); en.wikipedia "List of aircraft of the Irish Air Corps", whose lead states that "A De Havilland Vampire and a Miles Magister are on display in the National Museum in Collins Barracks (Dublin)"; Nominatim forward geocode returning the Collins Barracks museum polygon
confidence: MEDIUM-HIGH that two aircraft are displayed here, LOW on their individual identities. Free-admission national museum branch; the Soldiers and Chiefs gallery spans over 1700 m² of Irish military history. **I have deliberately left both tail numbers blank** — see NOTES; the sourcing supports the types but not the serials, and a guessed Irish Air Corps number would collide with the real airframe later. Nominatim returned Eircode "D13 XKV4" for this address, which is internally inconsistent (D13 is Dublin 13, the address is Dublin 7), so I have left postal_code blank rather than propagate a bad code.

name: Focke-Wulf Fw 200 Condor crash memorial -- Dingle
city: Dingle
state_province: County Kerry
country: Ireland
postal_code: 
region: Europe
address: Dingle Peninsula; near Slea Head
website: 
access_type: public
latitude: 52.23457
longitude: -10.23272
source: OpenStreetMap node/12176277636 (historic=aircraft; access=yes; aircraft:type=military; model "Focke-Wulf Fw 200 Condor"; model:wikidata Q157485; operator "Luftwaffe KG 40"; tourism=attraction; name "World War II plane crash site: Engine of Focke-Wulf Fw 200 Condor")
confidence: MEDIUM. A recovered engine from a Luftwaffe Fw 200 Condor of KG 40 is displayed on the Dingle peninsula as a marked, publicly accessible wartime crash memorial. **This is an engine, not an airframe**, and is recorded as such — an honest partial rather than an implied complete aircraft. The KG 40 unit attribution comes from the surveyor and is plausible (KG 40 flew the Condor on Atlantic patrols past south-west Ireland) but is not independently confirmed here. Node is a 2024-25 OSM id.

name: Cavan & Leitrim Railway -- Dromod
city: Dromod
state_province: County Leitrim
country: Ireland
postal_code: 
region: Europe
address: Station House; Station Road; Dromod
website: https://www.cavanandleitrim.com/
access_type: public
latitude: 53.85953
longitude: -7.91649
source: OpenStreetMap node/1293714093 (tourism=museum; museum=railway; fee=yes; phone +353 71 9638599; wikidata Q5054858) plus the associated 914 mm running lines; en.wikipedia "Cavan and Leitrim Railway", preservation section: "There is a transport museum, with narrow-gauge trains of several gauges, buses, **planes**, fire engines and artillery guns from World War I and World War II"
confidence: MEDIUM on the site, ZERO on the aircraft. The heritage railway and transport museum at the former Dromod station is real, ticketed and operating. Wikipedia states that aircraft are among the exhibits but names none, and the operator's own site returned HTTP 421 Misdirected Request on both HTTP/1.1 and HTTP/2 when fetched on 10 September 2026, so I could not read their inventory. **I have recorded NO aircraft rows for this site** rather than invent them. This is the highest-value single phone call in the Irish section — see NOTES.

name: Ulster Aviation Society -- Long Kesh
city: Lisburn
state_province: County Antrim
country: United Kingdom
postal_code: 
region: Europe
address: Maze Long Kesh site; Halftown Road; Lisburn
website: https://www.ulsteraviationsociety.org/
access_type: appointment
latitude: 54.49134
longitude: -6.11262
source: en.wikipedia "Ulster Aviation Society" — collection list stated as of June 2025 with 2025-26 accessions dated individually; OpenStreetMap way/255015683 (club=yes; name "Ulster Aviation Society") and node/1683426112 ("Ulster Aviation Society, Gate 3")
confidence: HIGH on the collection, HIGH on access. **Northern Ireland is the United Kingdom, so country is United Kingdom, not Ireland** — recorded per instruction. I could NOT verify against the database's existing 302 UK sites: the CSV files present in this working environment (/home/claude/build2/museums_final.csv and museums_new.csv) contain zero rows with country "United Kingdom", so they are not the UK slice of the database and a local dedupe check was impossible. **Whoever imports this must check for an existing "Ulster Aviation Society" row before creating it.** Access: the society has no paid staff, casual walk-in visits are NOT permitted, and every visitor must pre-book so that volunteers are present and the gates and hangars are opened — that is `appointment` by the contract's test, not `restricted`, because the barrier is staffing rather than a military gate. There is no admission charge; donations welcome. The collection lives in the last surviving hangars of the wartime airfield, built for Short Brothers' Stirling production and now scheduled monuments; the society moved there in 2005-06 and its lease doubts were finally resolved in early 2024. Founded 1968 at Newtownards, at Langford Lodge by 1994. Registered charity NIC100128; Queen's Award for Voluntary Service 2018. The society itself prefers "collection" to "museum" because visitors are encouraged to touch exhibits and sit in cockpits.

---

## AIRCRAFT

### Eesti Lennundusmuuseum -- Lange
Panavia|Tornado|F.3|ZE256|Tornado||fixed_wing|monoplane|military|fighter||Ex-Royal Air Force air-defence variant; acquired from Jet Art Aviation Ltd of the United Kingdom and delivered to the museum by road on 12 March 2019 per the museum's own type page; serial from the Wikimedia Commons file "Royal Air Force; ZE256"|ZE 256|Eesti Lennundusmuuseum -- Lange|on_display|GB
Hawker Siddeley|Harrier|GR.3|XZ994|Harrier||fixed_wing|monoplane|military|ground_attack||Ex-Royal Air Force; the museum's Estonian page records only "saadud Inglismaalt" (obtained from England); serial from the Commons file "Royal Air Force; XZ994; Hawker Siddeley Harrier GR.3" and from Commons Category:XZ994 (aircraft)|XZ 994|Eesti Lennundusmuuseum -- Lange|on_display|GB
SEPECAT|Jaguar|GR.3|XZ361|Jaguar||fixed_wing|monoplane|military|ground_attack||Ex-Royal Air Force; museum records it as received from England; identity from Commons Category:XZ361 (aircraft) filed under both Royal Air Force aircraft at the Estonian Aviation Museum and SEPECAT Jaguar GR.3 at the Estonian Aviation Museum|XZ 361|Eesti Lennundusmuuseum -- Lange|on_display|GB
Lockheed|F-104||MM6507|Starfighter||fixed_wing|monoplane|military|fighter||Ex-Aeronautica Militare; obtained from the Italian air force. VARIANT IS DISPUTED and is therefore left blank: the museum's own pages call it an F-104 ASA while the Commons photographer filed it as "Italian Air Force; MM6507; Lockheed F-104G Starfighter". MM65xx serials belong to the F-104G batches; ASA was a later F-104S upgrade. Do not assert a variant without the airframe record|MM 6507; F104|Eesti Lennundusmuuseum -- Lange|on_display|IT
Saab|J35||||Draken|fixed_wing|monoplane|military|fighter||Wears Swedish Air Force individual code 10; tail_number left BLANK because a Swedish two-digit code is not a serial and the five-digit airframe number was not recorded by any source I could reach. Owned by the Swedish Air Force Museum and displayed at Lange on loan per et.wikipedia. Identity from Commons file "Swedish Air Force; 10; Saab J35 Draken"|Saab 35; J 35; Draken; J35|Eesti Lennundusmuuseum -- Lange|on_display|SE
Saab|JA 37||||Viggen|fixed_wing|monoplane|military|fighter||Wears Swedish Air Force individual code 4; tail_number left BLANK for the same reason as the Draken. Owned by the Swedish Air Force Museum and on loan. Identity from Commons file "Swedish Air Force; 4; Saab JA37 Viggen"|Saab 37; JA37; Viggen|Eesti Lennundusmuuseum -- Lange|on_display|SE
Saab|J32|E||Lansen||fixed_wing|monoplane|military|electronic_warfare||Wears Swedish Air Force individual code 09; tail_number BLANK as above. The J 32E was the electronic-warfare and target-towing conversion of the Lansen. Owned by the Swedish Air Force Museum and on loan. Identity from Commons file "Swedish Air Force; 09; Saab J-32E Lansen"|Saab 32; J32E; Lansen; J32|Eesti Lennundusmuuseum -- Lange|on_display|SE
Dassault|Mirage III|RS|R-2112|Mirage||fixed_wing|monoplane|military|recon||Ex-Swiss Air Force reconnaissance Mirage; the museum records it as received from the Swiss defence ministry; serial from Commons file "Swiss Air Force; R-2112; Dassault Mirage 3RS"|R2112; Mirage IIIRS; Mirage 3RS|Eesti Lennundusmuuseum -- Lange|on_display|CH
Mikoyan-Gurevich|MiG-21||9011|Fishbed||fixed_wing|monoplane|military|fighter||Ex-Polish Air Force; obtained from Poland. VARIANT DISPUTED and left blank: the museum's own page is headed MiG-21Bis and et.wikipedia says MiG-21bis; the Commons photographer filed it as "Polish Air Force; 9011; Mikoyan-Gurevich MiG-21MF". Bort 9011 is carried on the airframe|MiG21; Fishbed; 9011|Eesti Lennundusmuuseum -- Lange|on_display|PL
Mikoyan-Gurevich|MiG-23|MLD|32|Flogger||fixed_wing|monoplane|military|fighter||Ex-Ukrainian Air Force; the museum records it as received from Ukraine and it wears Ukrainian markings. Bort 32 is a two-digit tactical number and NOT a construction number; the c/n is unknown and must not be inferred. Identity from Commons file "Ukranian Air Force; 32; Mikoyan-Gurevich Mig-23MLD"|MiG23; Flogger|Eesti Lennundusmuuseum -- Lange|on_display|UA
Mikoyan-Gurevich|MiG-25|RBS|25|Foxbat||fixed_wing|monoplane|military|recon||Soviet Air Force reconnaissance-bomber Foxbat-D; bort 25. Only ever a Soviet airframe; no post-1991 national operator; recorded RU accordingly. Identity from Commons file "USSR Air Force; 25; Mikoyan-Gurevich MiG-25RBS"|MiG25; Foxbat; Foxbat-D|Eesti Lennundusmuuseum -- Lange|on_display|RU
McDonnell Douglas|F-4|F|37+91|Phantom II||fixed_wing|monoplane|military|fighter||Ex-Luftwaffe. The museum's own page is headed "F-4C Phantom II" but states "Saadud: Saksamaa" (received from Germany); the Commons file is "German Air Force; 37-91; McDonnell Douglas F-4F Phantom II". Germany never operated the F-4C; the museum's page title is wrong and the airframe is an F-4F. A separate F-4 nose section is also present per Commons|F4F; 3791; 37-91|Eesti Lennundusmuuseum -- Lange|on_display|DE
Sukhoi|Su-22|M4|3212|Fitter||fixed_wing|monoplane|military|ground_attack||Ex-Polish Air Force Su-22M4; serial 3212 from Commons file "Polish Air Force; 3212; Sukhoi Su-22M4 Fitter K"; consistent with the museum's Poland project|Su22; Fitter; Fitter-K|Eesti Lennundusmuuseum -- Lange|on_display|PL
Sukhoi|Su-24||39|Fencer||fixed_wing|monoplane|military|bomber||Ex-Ukrainian Air Force; wears Ukrainian markings; bort 39. VARIANT left blank: the Commons file says Su-24M2 but the M2 was a Russian upgrade programme and Ukrainian Fencers were M and MR; the museum's own page says only Su-24. Do not assert M2|Su24; Fencer|Eesti Lennundusmuuseum -- Lange|on_display|UA
Yakovlev|Yak-28||52|Brewer||fixed_wing|monoplane|military|electronic_warfare||Soviet Air Force; bort 52. VARIANT DISPUTED and left blank: the museum's own page and et.wikipedia both say Jak-28PP (the jamming variant) while the Commons file says "USSR Air Force; 52; Yakovlev Yak-28P" (the interceptor). The museum also displays this aircraft's radar and one of its engines as separate exhibits. Only ever a Soviet airframe|Yak28; Jak-28; Brewer; Firebar|Eesti Lennundusmuuseum -- Lange|on_display|RU
Aero|L-39|C|36|Albatros||fixed_wing|monoplane|military|trainer||Ex-Ukrainian Air Force; bort 36; identity from Commons file "Ukranian Air Force; 36; Aero L-39 Albatros"|L39; Albatros|Eesti Lennundusmuuseum -- Lange|on_display|UA
Aero|L-29||OM-JLP|Delfín||fixed_wing|monoplane|military|trainer||Registration OM-JLP is a Slovak civil registration; the Commons file is titled "Czech Air Force; OM-JLP; L-29 Delfin" which mixes an operator and a civil mark. Recorded with the registration it wears; the military service history is not established|L29; Delfin; Maya; OMJLP|Eesti Lennundusmuuseum -- Lange|on_display|
PZL-Mielec|TS-11||1234|Iskra||fixed_wing|monoplane|military|trainer||Ex-Polish Air Force; the first jet designed and built in Poland; serial 1234 from Commons file "Polish Air Force; 1234; PZL-Mielec TS-11 Iskra". Received from the Polish air force per et.wikipedia|TS11; Iskra|Eesti Lennundusmuuseum -- Lange|on_display|PL
PZL-Okęcie|PZL-104|Wilga 35A|50|Wilga||fixed_wing|monoplane|civilian|utility||Obtained from Ridali Lennuklubi per et.wikipedia; carries the number 50 per Commons file "Private; 50; PZL-Okecie 104 Wilga 35A"; glider-tug and utility type|PZL104; Wilga-35; Wilga 35|Eesti Lennundusmuuseum -- Lange|on_display|
British Aerospace|Hawk|Mk.51A|HW-326|Hawk||fixed_wing|monoplane|military|trainer||Ex-Finnish Air Force; received from Finland per et.wikipedia; Finnish serial HW-326 from Commons file "Finnish Air Force; HW-326; British Aerospace Hawk Mk.51A"|HW326; Hawk 51|Eesti Lennundusmuuseum -- Lange|on_display|FI
Aeroprakt|A-22|L|ES-ULM|Foxbat||fixed_wing|monoplane|civilian|private||Ukrainian-designed microlight; Estonian registration ES-ULM; et.wikipedia notes this aircraft is airworthy ("lendav") — recorded on_display because it is part of the museum's presented collection|A22; A-22L; Foxbat; ESULM|Eesti Lennundusmuuseum -- Lange|on_display|EE
Tupolev|Tu-134|A-3|ES-LTA|||fixed_wing|monoplane|civilian|commercial_transport||Ex-ELK Airways; Estonian registration ES-LTA; the airframe is traced as OpenStreetMap way/603619224 on the museum site with aircraft:colour white-aqua; Commons file "ELK Airways; ES-LTA; Tupolev Tu-134A-3". Cockpit is open to visitors|Tu134; ESLTA|Eesti Lennundusmuuseum -- Lange|on_display|EE
Yakovlev|Yak-40||UR-87590|Codling||fixed_wing|monoplane|civilian|commercial_transport||Ex-UES Avia of Ukraine; registration UR-87590 from Commons file. The museum's own page states this particular aircraft was used by former Ukrainian prime minister Yulia Tymoshenko|Yak40; Codling; UR87590|Eesti Lennundusmuuseum -- Lange|on_display|UA
PZL-Mielec|An-2||YL-LEB|Colt||fixed_wing|biplane|civilian|utility||Polish-built An-2 carrying the Latvian registration YL-LEB; identity from Commons file "Private; YL-LEB; PZL-Mielec An-2"|An2; Antonov An-2; Colt; YLLEB|Eesti Lennundusmuuseum -- Lange|on_display|LV
Antonov|An-2||ES-BAB|Colt||fixed_wing|biplane|civilian|utility||A second An-2 with the Estonian registration ES-BAB; identity from Wikimedia Commons Category:ES-BAB (aircraft) filed under Antonov An-2 at the Estonian Aviation Museum. Whether this and YL-LEB are both currently on the field or one has moved needs a site check|An2; Colt; ESBAB|Eesti Lennundusmuuseum -- Lange|on_display|EE
Let|L-410|UVP-E|ES-PLY|Turbolet||fixed_wing|monoplane|military|transport||Ex-Estonian Border Guard aviation flight (PPA lennusalk) per the museum's own L-410 page; registration ES-PLY from Commons file "Estonian Border Guard; ES-PLY; Let L-410UVP-E Turbolet"|L410; Turbolet; ESPLY|Eesti Lennundusmuuseum -- Lange|on_display|EE
Aero Commander|680|FL|ES-ACO|||fixed_wing|monoplane|civilian|private||Estonian registration ES-ACO; identity from Commons file "Private; ES-ACO; Aero Commander 680FL"|680FL; ESACO|Eesti Lennundusmuuseum -- Lange|on_display|EE
Saab|340|||||fixed_wing|monoplane|civilian|commercial_transport||Registration not established. Commons has a dedicated Category:Saab 340 at the Estonian Aviation Museum containing two 2022 photographs but no serial-bearing filename; et.wikipedia lists the type as "Saab 430" which is not a real designation and is a typo for 340. Tail number deliberately BLANK|Saab340|Eesti Lennundusmuuseum -- Lange|on_display|
Jodel|DR1050||ES-JPL|Ambassadeur||fixed_wing|monoplane|civilian|private||Estonian registration ES-JPL; identity from Commons file "Private; ES-JPL; Jodel DR1050 Ambassadeur"; not listed on the museum's own type index|DR-1050; DR1050; Ambassadeur; ESJPL|Eesti Lennundusmuuseum -- Lange|on_display|EE
Mil|Mi-8|S|ES-PMA|Hip||rotary_wing||military|transport||Ex-Estonian Border Guard; registration ES-PMA from Commons file "Estonian Border Guard; ES-PMA; Mil Mi-8S Hip"|Mi8; Hip; ESPMA|Eesti Lennundusmuuseum -- Lange|on_display|EE
PZL-Świdnik|Mi-2|RL|0615|Hoplite||rotary_wing||military|utility||Ex-Polish Air Force Mi-2RL; serial 0615 from Commons file "Polish Air Force; 0615; PZL-Swidnik Mi-2 Hoplite"; et.wikipedia adds that a second Mi-2 airframe (a wreck from the Estonian Air Force) is also held|Mi2; Mi-2RL; Hoplite|Eesti Lennundusmuuseum -- Lange|on_display|PL
Robinson|R44|Clipper|64|||rotary_wing||military|utility||Ex-Estonian Air Force; tactical number 64 from Commons file "Estonian Air Force; 64; Robinson R44 Clipper". The Estonian Air Force struck its last R44s off charge during 2024|R-44; R44 Clipper|Eesti Lennundusmuuseum -- Lange|on_display|EE
Robinson|R22|Beta|ES-HRJ|||rotary_wing||civilian|private||Estonian registration ES-HRJ; et.wikipedia notes the airframe is engineless ("mootorita"); identity from Commons file "Private; ES-HRJ; Robinson R22 Beta"|R-22; ESHRJ|Eesti Lennundusmuuseum -- Lange|on_display|EE
Schweizer|300|C|ES-PSF|||rotary_wing||military|trainer||Ex-Estonian Border Guard; registration ES-PSF from Commons file "Estonian Border Guard; ES-PSF; Schweizer 300C"|S-300; Schweizer 269; Hughes 300; ESPSF|Eesti Lennundusmuuseum -- Lange|on_display|EE
Kamov|Ka-26||HA-MCQ|Hoodlum||rotary_wing||civilian|utility||Hungarian civil registration HA-MCQ; identity from Commons file "Private; HA-MCQ; Kamov Ka-26 Hoodlum"|Ka26; Hoodlum; HAMCQ|Eesti Lennundusmuuseum -- Lange|on_display|HU
Let|Z-37|A|OK-AIP|Čmelák||fixed_wing|monoplane|civilian|utility||Czech agricultural aircraft carrying registration OK-AIP; identity from Commons file "Air Special; OK-AIP; Let Z-37 Cmelák". Listed by the museum under special-purpose aircraft|Z37; Zlin Z-37; Cmelak; OKAIP|Eesti Lennundusmuuseum -- Lange|on_display|CZ
LAK|LAK-12||ES-1003|Lietuva||fixed_wing|monoplane|civilian|private||Lithuanian-built high-performance glider; Estonian glider registration ES-1003; obtained from Ridali Lennuklubi per et.wikipedia; identity from Commons file "Private; ES-1003; LAK-12 Lietuva"|LAK12; Lietuva; ES1003|Eesti Lennundusmuuseum -- Lange|on_display|EE
Let|L-13||||Blaník|fixed_wing|monoplane|civilian|trainer||Training glider obtained from Ridali Lennuklubi per et.wikipedia. No registration recorded by any source reached; tail_number deliberately BLANK|L13; Blanik|Eesti Lennundusmuuseum -- Lange|on_display|
Fakel|V-750|||||missile_rocket||military|surface_to_air||Complete S-75 system round with launcher and transport set; the museum states it holds a representative of every surface-to-air missile system deployed on Estonian territory during the Soviet occupation. Manufacturer given as the Grushin design bureau MKB Fakel which designed the V-750 round; the system designer was Almaz|S-75; SA-2; Guideline; V750; S75|Eesti Lennundusmuuseum -- Lange|on_display|RU
Fakel|V-601|||||missile_rocket||military|surface_to_air||S-125 system round. Manufacturer given as MKB Fakel which designed the V-600 series round. Commons has a dedicated file "SA-3 missiles at Estonian Aviation Museum"|S-125; SA-3; Goa; V601; S125|Eesti Lennundusmuuseum -- Lange|on_display|RU
Fakel|V-860|||||missile_rocket||military|surface_to_air||S-200 system round with transport set; Commons has a dedicated Category:S-200 at Estonian Aviation Museum. Manufacturer given as MKB Fakel|S-200; SA-5; Gammon; V860; S200|Eesti Lennundusmuuseum -- Lange|on_display|RU
Vympel|3M9|||||missile_rocket||military|surface_to_air||2K12 Kub system round; Commons has a dedicated file "SA-6 missile at Estonian Aviation Museum". Manufacturer given as the Toropov bureau (Vympel) which designed the 3M9 round|2K12; Kub; SA-6; Gainful; 3M9|Eesti Lennundusmuuseum -- Lange|on_display|RU
Fakel|9M33|||||missile_rocket||military|surface_to_air||9K33 Osa system round. Manufacturer given as MKB Fakel which designed the 9M33|9K33; Osa; SA-8; Gecko; 9M33|Eesti Lennundusmuuseum -- Lange|on_display|RU

### Lennusadam -- Eesti Meremuuseum
Short|184|||||fixed_wing|biplane|military|recon||**REPLICA — FLAG THIS.** et.wikipedia states plainly that the exhibit is "maailma ainsat elusuuruses koopiat" — the world's only full-size copy of the Short 184 — and that no original survives anywhere. It is the centrepiece of the seaplane section of the hangar exposition. No serial exists and none must be assigned|Short Type 184; Short 184 replica|Lennusadam -- Eesti Meremuuseum|on_display|
Lake|LA-4||||Buccaneer|fixed_wing|monoplane|civilian|private||Amphibian reported in the hangar exposition and named in the research brief for this pass; I could NOT independently confirm it from Estonian-language sources or from Commons in the time available and the museum's own exhibit pages are a JavaScript application that did not render. Registration and variant deliberately BLANK. VERIFY BEFORE IMPORT|LA-4; Lake Buccaneer; LA4|Lennusadam -- Eesti Meremuuseum|on_display|

### Ämari lennuki mälestusmärk
Unidentified|Aircraft|||||fixed_wing||military|other||OpenStreetMap node/13232245984 records an aircraft memorial (historic=memorial; memorial=aircraft) in Ämari village but supplies NO type; no photograph found. Given the location beside Ämari air base a Soviet-era type is likely but that is a supposition and is not recorded as fact. Every identity field is deliberately blank per the contract||Ämari lennuki mälestusmärk|on_display|

### Tupolev Tu-134 ES-AAP -- Tallinna lennujaam
Tupolev|Tu-134|A-3|ES-AAP|||fixed_wing|monoplane|civilian|commercial_transport||Registration ES-AAP taken from the OpenStreetMap ref tag on way/603591805; a former Estonian Air Tu-134A-3 retained at Tallinn Airport in a yellow-orange scheme (aircraft:colour tag). The airframe is traced as a polygon so its presence at the time of survey is well founded; a 2025-26 photograph would settle current condition|Tu134; ESAAP|Tupolev Tu-134 ES-AAP -- Tallinna lennujaam|on_display|EE

### Piirivalvekopter -- Tallinn (Maarjamäe)
Unidentified|Helicopter|||||rotary_wing||military|search_rescue||OpenStreetMap node/12983444768 records aircraft=helicopter with operator=PPA and the Estonian description "Vana piirivalvekopter" (old border-guard helicopter). No type; no registration. The Estonian border guard has operated Mi-8 and Robinson types among others but naming one here would be a guess. role_type search_rescue reflects the border-guard operator rather than a documented mission fit||Piirivalvekopter -- Tallinn (Maarjamäe)|on_display|EE

### Rīgas aviācijas muzejs -- Skulte
Kamov|Ka-26||CCCP-24057|Hoodlum||rotary_wing||civilian|utility||Light multipurpose helicopter in Aeroflot markings; registration recorded in Cyrillic as СССР-24057 in the Latvian Wikipedia exhibit table and transliterated here. Also mapped as OpenStreetMap node/13902881052 at the Skulte site|Ka26; Hoodlum; CCCP24057; SSSR-24057|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-1||17|Hare||rotary_wing||military|utility||Wears bort 17. Only ever a Soviet airframe; the Latvian air force never operated the type. Mapped as OpenStreetMap node/10033994816 with a linked Commons photograph|Mi1; Hare|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-2||21|Hoplite||rotary_wing||military|utility||Wears bort 21; one of two Mi-2s in the collection. Soviet service only|Mi2; Hoplite|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-2||22|Hoplite||rotary_wing||military|utility||Wears bort 22; the second Mi-2. Mapped as OpenStreetMap node/10034062517. Soviet service only|Mi2; Hoplite|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-4||CCCP-31449|Hound||rotary_wing||civilian|utility||Aeroflot-marked Mi-4; registration recorded as СССР-31449 in the Latvian Wikipedia table. Mapped as OpenStreetMap node/10033994813 with linked Commons photograph|Mi4; Hound; CCCP31449|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-6||09|Hook||rotary_wing||military|transport||Heavy transport helicopter wearing bort 09; mapped as OpenStreetMap node/6683869054 with linked Commons photograph. Soviet service only|Mi6; Hook|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-8|T|17|Hip||rotary_wing||military|transport||Assault-transport Hip wearing bort 17; mapped as OpenStreetMap node/10033994815. Note the bort duplicates the Mi-1's — two-digit Soviet tactical numbers repeat endlessly and are not unique identifiers. Soviet service only|Mi8; Mi-8T; Hip|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mil|Mi-24|A|20|Hind||rotary_wing||military|ground_attack||Early A-model Hind wearing bort 20; mapped as OpenStreetMap node/10033994814 with a linked Commons photograph. Commons also holds "Mi-24 nose at Riga Aviation Museum" from the Skulte site. Soviet service only|Mi24; Mi-24A; Hind; Hind-A|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Antonov|An-2||22|Colt||fixed_wing|biplane|civilian|utility||Wears the number 22; mapped as OpenStreetMap node/10034004967 with a linked Commons photograph. Commons also holds "An-2s at Riga Aviation Museum" plural from the Skulte site so a second An-2 may be present|An2; Colt|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Antonov|An-14||01|Pchelka||fixed_wing|monoplane|civilian|utility||Wears the number 01; light STOL twin|An14; Pchelka; Clod|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Antonov|An-24|B|CCCP-46400|Coke||fixed_wing|monoplane|civilian|commercial_transport||Registration recorded as СССР-46400 in the Latvian Wikipedia table; the Commons photograph of this airframe is filed as "An-24B Latavio YL-LCD"; i.e. it later carried the Latvian registration YL-LCD with Latavio; so the aircraft has TWO documented identities and the museum table gives the Soviet one. Mapped as OpenStreetMap node/11948091019|An24; Coke; YL-LCD; YLLCD; CCCP46400|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Aero|L-29||22|Delfín||fixed_wing|monoplane|military|trainer||One of four L-29s; wears bort 22. Soviet service only|L29; Delfin; Maya|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Aero|L-29||26|Delfín||fixed_wing|monoplane|military|trainer||Wears bort 26; mapped as OpenStreetMap node/13902881053 and photographed at Skulte|L29; Delfin; Maya|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Aero|L-29||38|Delfín||fixed_wing|monoplane|military|trainer||Wears bort 38|L29; Delfin; Maya|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Aero|L-29||92|Delfín||fixed_wing|monoplane|military|trainer||Wears bort 92. Commons "L-29s at Riga Aviation Museum" confirms multiple L-29s made the move to Skulte|L29; Delfin; Maya|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-15|UTI|14|Midget||fixed_wing|monoplane|military|trainer||Two-seat conversion trainer wearing bort 14; Commons has a dedicated Category:Mikoyan-Gurevich MiG-15UTI at Riga Aviation Museum filed under the Skulte site|MiG15; MiG-15UTI; Midget|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-15|UTI|58|Midget||fixed_wing|monoplane|military|trainer||Second MiG-15UTI wearing bort 58|MiG15; MiG-15UTI; Midget|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-21|bis|76|Fishbed||fixed_wing|monoplane|military|fighter||Wears bort 76; Commons "MiG-21s at Riga Aviation Museum" confirms multiple MiG-21s at Skulte. Soviet service only|MiG21; MiG-21bis; Fishbed|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-21|SMT|10|Fishbed||fixed_wing|monoplane|military|fighter||Wears bort 10. The SMT was the enlarged-spine fuel-tank variant|MiG21; MiG-21SMT; Fishbed-K|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-21|UM|94|Mongol||fixed_wing|monoplane|military|trainer||Two-seat trainer wearing bort 94|MiG21; MiG-21UM; Mongol|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-21|US|06|Mongol||fixed_wing|monoplane|military|trainer||Two-seat trainer wearing bort 06; photographed at Skulte as "MiG-21US; Riga Aviation Museum"|MiG21; MiG-21US; Mongol|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-23|BM||Flogger||fixed_wing|monoplane|military|ground_attack||The Latvian Wikipedia table gives no bort for this airframe but does give a construction number: с/н 3910601. tail_number is therefore BLANK and the c/n is carried in aliases as the only unique identifier. MiG-23BM was the ground-attack development that became the MiG-27|MiG23; MiG-23BM; c/n 3910601; 3910601; Flogger|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-23|M|74|Flogger||fixed_wing|monoplane|military|fighter||Wears bort 74; photographed at Skulte as "MiG-23M; Riga Aviation Museum"|MiG23; MiG-23M; Flogger-B|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-23|MF|16|Flogger||fixed_wing|monoplane|military|fighter||Wears bort 16|MiG23; MiG-23MF; Flogger-B|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan-Gurevich|MiG-25|RBS|34|Foxbat||fixed_wing|monoplane|military|recon||Reconnaissance-bomber Foxbat-D wearing bort 34; photographed at Skulte and mapped as OpenStreetMap node/13902881051. Soviet service only|MiG25; MiG-25RBS; Foxbat-D|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan|MiG-27|||Flogger||fixed_wing|monoplane|military|ground_attack||Photographed at the Skulte site as "MiG-27 at Riga Aviation Museum" but ABSENT from the Latvian Wikipedia exhibit table; which was last comprehensive for 2018. No bort or c/n known; tail_number deliberately blank. Its presence is evidenced only by the post-move photograph|MiG27; Flogger-D|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Mikoyan|MiG-29|UB|52|Fulcrum||fixed_wing|monoplane|military|trainer||Two-seat Fulcrum wearing bort 52. The Commons file from the Skulte site is titled "MiG-29UB remains; Riga Aviation Museum" — the airframe is INCOMPLETE and should not be described as a whole aeroplane|MiG29; MiG-29UB; Fulcrum-B|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Ilyushin|Il-28|||Beagle||fixed_wing|monoplane|military|bomber||Photographed at the Skulte site (three separate Commons files including tail and side views) and mapped as OpenStreetMap node/9921285147 "Lidmašīna Il-28". ABSENT from the Latvian Wikipedia table. No bort or c/n known|Il28; Beagle|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Sukhoi|Su-7||27|Fitter||fixed_wing|monoplane|military|ground_attack||Wears bort 27; photographed at Skulte as "Su-7 at Riga Aviation Museum". Soviet service only|Su7; Fitter-A|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Sukhoi|Su-7|U|43|Moujik||fixed_wing|monoplane|military|trainer||Two-seat trainer wearing bort 43|Su7U; Su-7U; Moujik|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Tupolev|Tu-22M|1|53|Backfire||fixed_wing|monoplane|military|bomber||The Latvian Wikipedia table describes this airframe as a "tālās darbības bumbvedēja prototips" — a long-range bomber prototype — and it wears bort 53. Only nine Tu-22M0 and a small number of Tu-22M1 pre-series aircraft were built; an M1 survivor is internationally significant. Mapped as OpenStreetMap node/10034062518 and photographed at Skulte from five angles including cockpit and intake. Soviet service only|Tu22M; Tu-22M1; Backfire-A|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Tupolev|Tu-134|A-3|RA-65717|||fixed_wing|monoplane|civilian|commercial_transport||Russian registration RA-65717; mapped as OpenStreetMap node/11948090997 and photographed at Skulte|Tu134; RA65717|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Yakovlev|Yak-18|T|CCCP-38342|Max||fixed_wing|monoplane|civilian|trainer||Registration recorded as CCCP-38342 in the Latvian Wikipedia table|Yak18T; Yak-18T; CCCP38342|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Yakovlev|Yak-28|P|22|Firebar||fixed_wing|monoplane|military|recon||Wears bort 22; mapped as OpenStreetMap node/13900373921 (named YAK-28R) and photographed both at the old airport site ("Yakovlev Yak-28R Red 22 Soviet AF Riga Msm 04.10.05") and at Skulte ("Yak-28R nose at Riga Aviation Museum"). SUB-VARIANT DISPUTED — the museum table says Yak-28P (interceptor) while OSM and two Commons files say Yak-28R (reconnaissance); variant recorded as the table has it and the dispute noted here. The Skulte photograph shows a NOSE section which may mean only part of the airframe survived the move|Yak28; Yak-28R; Firebar; Brewer|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Cessna|150|||||fixed_wing|monoplane|civilian|private||The Latvian Wikipedia table gives no registration but does give с/н 15059081. tail_number BLANK; the construction number is in aliases as the only unique identifier|c/n 15059081; 15059081; Cessna 150|Rīgas aviācijas muzejs -- Skulte|on_display|
Zlín|Z-37|A|OK-ZKC|Čmelák||fixed_wing|monoplane|civilian|utility||Czechoslovak agricultural aircraft with registration OK-ZKC; photographed at Skulte as "Zlín Z-37A - OK-ZKC; Riga Aviation Museum"|Z37; Z-37A; Cmelak; OKZKC|Rīgas aviācijas muzejs -- Skulte|on_display|CZ
Let|L-13||47|Blaník||fixed_wing|monoplane|civilian|trainer||Training glider wearing the number 47|L13; Blanik|Rīgas aviācijas muzejs -- Skulte|on_display|
Let|L-13||72|Blaník||fixed_wing|monoplane|civilian|trainer||Training glider wearing the number 72|L13; Blanik|Rīgas aviācijas muzejs -- Skulte|on_display|
Sukhoi|Su-24|M||Fencer||fixed_wing|monoplane|military|bomber||COCKPIT SECTION ONLY — the Latvian Wikipedia table lists this under "Lidmašīnu kabīnes" (aircraft cockpits). No bort; construction number s/n 0515318 is the only identifier and is carried in aliases. Photographed at Skulte as "Mi-8 nose and Su-24 canopy" and "Su-24 nose at Riga Aviation Museum"|Su24; s/n 0515318; 0515318; Fencer|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Sukhoi|Su-24|M||Fencer||fixed_wing|monoplane|military|bomber||COCKPIT SECTION ONLY; second example. Construction number s/n 0915306 in aliases as the only identifier|Su24; s/n 0915306; 0915306; Fencer|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Sukhoi|T-10|||||fixed_wing|monoplane|military|experimental||COCKPIT SECTION ONLY of a **Su-27 prototype** — the Latvian Wikipedia table gives the type as "Т-10 (Su-27 prototips)" with s/n 02-04. T-10 was the original Sukhoi prototype configuration that was fundamentally redesigned into the T-10S production Su-27; a surviving T-10 section is internationally significant. Photographed at Skulte as "Su-27 nose at Riga Aviation Museum". Construction number in aliases as the only identifier|T10; s/n 02-04; 02-04; Su-27 prototype; Flanker|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Sukhoi|Su-15|||Flagon||fixed_wing|monoplane|military|fighter||NOSE SECTION ONLY. Evidenced solely by the Commons file "Su-7 and Su-15 nose at Riga Aviation Museum" from the Skulte site; ABSENT from the Latvian Wikipedia tables. No serial|Su15; Flagon|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Tupolev|Tu-104|A|CCCP-42328|Camel||fixed_wing|monoplane|civilian|commercial_transport||COCKPIT SECTION ONLY — listed under aircraft cockpits in the Latvian Wikipedia table with registration СССР-42328. The Tu-104 was the world's second jet airliner to enter service; a surviving section is significant. Photographed at Skulte as "Tu-104А; Riga Aviation Museum" and as part of "Tupolev noses at Riga Aviation Museum"|Tu104; Camel; CCCP42328|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Tupolev|Tu-134|B|CCCP-65698|||fixed_wing|monoplane|civilian|commercial_transport||COCKPIT SECTION ONLY — listed under aircraft cockpits with registration СССР-65698. Distinct from the complete Tu-134A-3 RA-65717 also in the collection. Photographed at Skulte|Tu134; Tu-134B; CCCP65698|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Raduga|KSR-11|||Kelt||missile_rocket||military|air_to_surface||Anti-radiation air-launched missile evidenced by the Commons file "KSR-11 missile at Riga Aviation Museum" from the Skulte site; the KSR-11 was the anti-radar development of the KSR-2 carried by the Tu-16. ABSENT from the Latvian Wikipedia tables|KSR11; AS-5; Kelt|Rīgas aviācijas muzejs -- Skulte|on_display|RU
Fakel|V-750|||||missile_rocket||military|surface_to_air||S-75 system round evidenced by the Commons file "SA-2 at Riga Aviation Museum". Manufacturer given as MKB Fakel which designed the V-750 round. The Latvian Wikipedia "other equipment" table separately lists an РСП-7Т landing radar; an СКП-9МВ mobile control post; a TRUMP D40-D de-icing vehicle and an AA-60 airfield fire tender — none of which are aircraft and none of which are recorded here|S-75; SA-2; Guideline; V750; S75|Rīgas aviācijas muzejs -- Skulte|on_display|RU

### VEF I-12 replika -- Lidosta Rīga
VEF|I-12|||||fixed_wing|monoplane|military|trainer||**REPLICA — FLAG THIS.** The OpenStreetMap node names it explicitly as "VEF I-12 (replica)". The original VEF I-12 was a Latvian trainer designed by Kārlis Irbītis and built by Valsts elektrotehniskā fabrika in the 1930s. No original survives and no serial should be assigned to the replica|VEF I12; I-12; Irbitis I-12|VEF I-12 replika -- Lidosta Rīga|on_display|

### Mil Mi-26 piemineklis -- Rīga (Dārzciems)
Mil|Mi-26|T||Halo||rotary_wing||military|transport||Type and variant from the OpenStreetMap tags model "Mi-26T Halo" with model:wikidata Q336150. No registration or bort recorded by the surveyor and none inferred. The Mi-26 is the largest helicopter ever to enter series production. Operator nationality NOT established — Mi-26Ts served both Soviet military and Aeroflot/civil operators — so operator_country is deliberately blank|Mi26; Mi-26T; Halo|Mil Mi-26 piemineklis -- Rīga (Dārzciems)|on_display|

### Antonov An-2 -- Rīga (Valērijas Seiles iela)
Antonov|An-2|||Colt||fixed_wing|biplane|civilian|utility||Type from the OpenStreetMap name tag "Lidmašīna AN-2" on a traced polygon. No registration recorded and none inferred; Latvian roadside An-2s are usually ex-Aeroflot agricultural airframes but that is not evidenced here|An2; Colt|Antonov An-2 -- Rīga (Valērijas Seiles iela)|on_display|

### Ciemupes lidmašīnu ekspozīcija
Antonov|An-2|||Colt||fixed_wing|biplane|civilian|utility||OpenStreetMap node/12147569346 names it "An-2 Ciemupe Belle" with model:wikidata Q207700. "Ciemupe Belle" appears to be a nickname applied to the airframe rather than a registration and is recorded in aircraft_name; no registration is known|An2; Colt|Ciemupes lidmašīnu ekspozīcija|on_display|
Antonov|An-24|||Coke||fixed_wing|monoplane|civilian|commercial_transport||OpenStreetMap node/12726138633 carries model:wikidata Q337467 (Antonov An-24) and no other tag. No registration; operator nationality not established|An24; Coke|Ciemupes lidmašīnu ekspozīcija|on_display|
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap node/12147569345 is tagged historic=aircraft and NOTHING else. Recorded as Unidentified per the contract rather than assumed to match its neighbours||Ciemupes lidmašīnu ekspozīcija|on_display|
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap node/12875031667 is tagged historic=aircraft and nothing else||Ciemupes lidmašīnu ekspozīcija|on_display|

### Nākotnes parka lidaparāti -- Glūda
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap node/13460578149; tagged historic=aircraft only. military_civilian is a required field and has been set civilian because every other identifiable park or roadside airframe found in this Latvian sweep is a civil An-2 or An-24; that is a pattern argument and NOT evidence about this airframe. Needs a human before import||Nākotnes parka lidaparāti -- Glūda|on_display|
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap node/13460578150; tagged historic=aircraft only. military_civilian set civilian on the same pattern argument as its neighbour and not on evidence||Nākotnes parka lidaparāti -- Glūda|on_display|
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap node/13460578151; tagged historic=aircraft only. military_civilian set civilian on the same pattern argument as its neighbours and not on evidence||Nākotnes parka lidaparāti -- Glūda|on_display|

### MiG-15UTI -- Cīravas lidlauks
Mikoyan-Gurevich|MiG-15|UTI||Midget||fixed_wing|monoplane|military|trainer||Type from OpenStreetMap node/8199786231 (model "MiG 15UTI"; model:wikidata Q187377) with a linked Commons photograph File:Cīravas lidlauks - vecais MIG.jpg. No bort or construction number recorded. Soviet service only — Latvia never operated the type|MiG15; MiG-15UTI; Midget|MiG-15UTI -- Cīravas lidlauks|on_display|RU

### Antonov An-2R -- Duči (Limbaži)
Antonov|An-2|R||Colt||fixed_wing|biplane|civilian|utility||Variant R is the agricultural sprayer; taken from the OpenStreetMap model tag "Antonov An-2R" with model:wikidata Q207700. No registration recorded|An2; An-2R; Colt|Antonov An-2R -- Duči (Limbaži)|on_display|

### Antonov An-2 -- Bārbele (Bauska)
Antonov|An-2|||Colt||fixed_wing|biplane|civilian|utility||Type inferred ONLY from the OpenStreetMap model:wikidata link Q207700 on node/9897094506; the node has no name tag and no photograph. Lowest-confidence airframe row in the Latvian section|An2; Colt|Antonov An-2 -- Bārbele (Bauska)|on_display|

### Lietuvos aviacijos muziejus -- Kaunas
Bellanca|CH-300||||Lituanica|fixed_wing|monoplane|civilian|experimental|1982|**FLYABLE REPLICA — FLAG THIS.** The museum's own exposition page calls it "skraidymams tinkanti legendinės Lituanicos replika" — a flight-capable replica of the legendary Lituanica — designed and built by the aviator Vladas Kensgaila in 1982 for the film "Skrydis per Atlantą". Commons files it as "VK-6 (реплика Литуаники)". The ORIGINAL Lituanica wreckage is at the Vytautas the Great War Museum; do not conflate the two|Lituanica replica; VK-6; VK6; Bellanca Pacemaker|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Mil|Mi-8|T||Hip||rotary_wing||military|transport||Mapped as OpenStreetMap node/13992725041 "Helikopters Mi-8T" inside the museum compound; the museum's exposition page confirms Air Force and State Border Guard Service helicopters in the outdoor display and a walk-in Mi-8 simulator cabin. No bort recorded|Mi8; Mi-8T; Hip|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Mil|Mi-2|||Hoplite||rotary_wing||military|utility||Mapped as OpenStreetMap node/13992766822; one of two Mi-2s on site. No bort recorded|Mi2; Hoplite|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Mil|Mi-2|||Hoplite||rotary_wing||military|utility||Mapped as OpenStreetMap node/14002762485; second Mi-2. No bort recorded|Mi2; Hoplite|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Kamov|Ka-26|||Hoodlum||rotary_wing||civilian|utility||Mapped as OpenStreetMap node/13992766829 and photographed as "LAM 2008-09 Ka-26". No registration recorded|Ka26; Hoodlum|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Antonov|An-26|B||Curl||fixed_wing|monoplane|military|transport||Transferred to the museum from the Lithuanian Air Force by government resolution of 29 September 2010 per lt.wikipedia; the museum's site carries a dedicated page "LĖKTUVO AN-26 KELIONĖ" about the aircraft's journey. No tactical number recorded|An26; An-26B; Curl|Lietuvos aviacijos muziejus -- Kaunas|on_display|LT
Aero|L-39|C||Albatros||fixed_wing|monoplane|military|trainer||Transferred from the Lithuanian Air Force by the same 29 September 2010 government resolution as the An-26B per lt.wikipedia. No tactical number recorded|L39; L-39C; Albatros|Lietuvos aviacijos muziejus -- Kaunas|on_display|LT
Antonov|An-24|||Coke||fixed_wing|monoplane|civilian|commercial_transport||Mapped as OpenStreetMap node/13992766823; Commons has a dedicated Category:Antonov An-24 at the Lithuanian Aviation Museum. No registration recorded|An24; Coke|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Antonov|An-2|||Colt||fixed_wing|biplane|civilian|utility||Mapped as OpenStreetMap node/13992766824. The museum's exposition page identifies its outdoor An-2 as a **participant in the Baltic Way** of 23 August 1989 — a significant provenance claim made by the museum itself. Visitors can sit in an An-2 simulator cabin. No registration recorded|An2; Colt; Baltijos kelias|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Antonov|An-14|||Pchelka||fixed_wing|monoplane|civilian|utility||Mapped as OpenStreetMap node/13992766828 "An-14 Pchelka" and photographed as "Preserved An-14" and "Ан-14; Музей Литовской авиации". No registration recorded|An14; Pchelka; Clod|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Aero|L-29|||Delfín||fixed_wing|monoplane|military|trainer||Mapped as OpenStreetMap node/13992766825 and photographed as "Aero L-29.jpg" in the museum category. No bort recorded|L29; Delfin; Maya|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Mikoyan-Gurevich|MiG-21|||Fishbed||fixed_wing|monoplane|military|fighter||Evidenced by the Commons photograph "LAM 2008-09 Mig-21.jpg" in Category:Aircraft at the Lithuanian Aviation Museum. VARIANT UNKNOWN and deliberately blank; no bort recorded. **The 2008 photograph predates the 2026 reconstruction — confirm this airframe is still on site**|MiG21; Fishbed|Lietuvos aviacijos muziejus -- Kaunas|on_display|RU
Yakovlev|Yak-50|||||fixed_wing|monoplane|civilian|private||Aerobatic monoplane named in the lt.wikipedia description of the museum's holdings ("akrobatinį lėktuvą JAK-50"). No registration recorded|Yak50; Jak-50|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Gustaitis|ANBO I|||||fixed_wing|monoplane|military|trainer||en.wikipedia describes the museum as holding the ANBO I; the first aircraft designed by Antanas Gustaitis; and Commons carries "LAM 2008-09 Anbo-1.jpg". **Whether this is the original or a reproduction is NOT established** and no sourced statement either way was found; do not assert originality. The museum separately holds the ANBO-IV drawings which entered the UNESCO Memory of the World Lithuanian national register in 2006|ANBO-I; ANBO1|Lietuvos aviacijos muziejus -- Kaunas|on_display|LT
Oškinis|BrO-18||||Boružė|fixed_wing|monoplane|civilian|private|1975|Lithuanian glider designed by Bronius Oškinis; photographed as "Lithuanian glider BrO-18 Boružė by Br.Oškinis; 1975". The museum describes the Oškinis glider collection as one of its principal treasures|BrO18; BRO-18; Boruze; Ladybird|Lietuvos aviacijos muziejus -- Kaunas|on_display|LT
Let|L-13||||Blaník|fixed_wing|monoplane|civilian|trainer||Mapped as OpenStreetMap node/14024465478 "Let L-13 Blaník". No registration recorded|L13; Blanik|Lietuvos aviacijos muziejus -- Kaunas|on_display|
Kensgaila|VK-9|||||fixed_wing|monoplane|civilian|private||Lithuanian homebuilt by Vladas Kensgaila; mapped as OpenStreetMap node/13992766827 "VK-9" and photographed as "VK-9.jpg". No registration recorded|VK9|Lietuvos aviacijos muziejus -- Kaunas|on_display|LT
Unidentified|Light aircraft||LY-HBQ|||fixed_wing|monoplane|civilian|private||A Lithuanian-registered light aircraft photographed in the museum category as "LT LY-HBQ.jpg". The type is not stated in the filename or category and I would not guess it; manufacturer and model are therefore Unidentified per the contract while the registration — which IS sourced — is retained|LYHBQ|Lietuvos aviacijos muziejus -- Kaunas|on_display|LT

### Vytauto Didžiojo karo muziejus -- Kaunas
Bellanca|CH-300|Pacemaker|NR688E||Lituanica|fixed_wing|monoplane|civilian|experimental||**WRECKAGE / RELICS; NOT A COMPLETE AIRCRAFT.** lt.wikipedia lists the "Lituanicos transatlantinio skrydžio relikvijos" among the museum's most valuable holdings. Steponas Darius and Stasys Girėnas flew this Bellanca from New York on 15 July 1933 and crashed near what is now Pszczelnik in Poland on 17 July; both men died. en.wikipedia confirms the remains are at this museum and NOT at the Lithuanian Aviation Museum. The registration NR688E is the aircraft's well-documented US mark; if the museum's own accession record disagrees the museum wins|Lituanica; NR-688E; NR688E; Bellanca Pacemaker; CH300|Vytauto Didžiojo karo muziejus -- Kaunas|on_display|US

### Įstros aviacijos muziejus -- Stanioniai
Unidentified|Aircraft mock-up|||||fixed_wing||military|other||**MOCK-UPS; FLAG THIS ENTIRE SITE.** The operator's own OpenStreetMap description states this is "vienintelis Lietuvoje lėktuvų muliažų muziejus po atviru dangumi" — the only open-air museum of aircraft MOCK-UPS in Lithuania — displaying fighters; jet trainers and helicopters used in the second half of the 20th century. Because none of the exhibits is evidenced as a genuine airframe I have recorded a single placeholder row rather than fabricate an inventory of aircraft that may never have flown. A site visit is needed to establish whether any real ex-service airframes are present||Įstros aviacijos muziejus -- Stanioniai|on_display|

### Aero L-39 -- Zokniai (Šiauliai)
Aero|L-39||||Albatros|fixed_wing|monoplane|military|trainer||Manufacturer and model come directly from the OpenStreetMap tags manufacturer=Aero Vodochody and model=L-39 with aircraft:type "military;jet;fixed_wing". SUB-VARIANT NOT ESTABLISHED and deliberately blank — Lithuanian Air Force Albatroses were L-39ZA and L-39C but the node does not say which. No tactical number recorded; Lithuanian L-39s carry repeating two-digit numbers so none must be inferred. operator_country LT is asserted on the basis of the location on the approach to the Lithuanian Air Force base at Zokniai; if it proves to be an ex-Soviet airframe never taken on Lithuanian charge this should become RU|L39; Albatros|Aero L-39 -- Zokniai (Šiauliai)|on_display|LT

### Lakūno Stepono Dariaus gimtinė-muziejus
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap way/1427756481; traced as a polygon and tagged covered=yes so it is under a shelter or inside a building. No type tag||Lakūno Stepono Dariaus gimtinė-muziejus|on_display|
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap way/1427756482; traced polygon; no type tag||Lakūno Stepono Dariaus gimtinė-muziejus|on_display|
Unidentified|Aircraft|||||fixed_wing||civilian|other||OpenStreetMap way/1427756483; traced polygon; no type tag||Lakūno Stepono Dariaus gimtinė-muziejus|on_display|

### Shannon Aviation Museum
de Havilland|DH.115|T.55|191|Vampire||fixed_wing|monoplane|military|trainer|1960|Irish Aviation Foundation accession 1116; the museum's own catalogue records MSN 15815; delivered to the Irish Air Corps in early January 1961 as part of the second batch of six T.55s; **flew the last flight by an Irish Air Corps Vampire on 2 February 1976** after 1143.5 hours. year_built recorded as 1960 on the basis of a January 1961 delivery; the museum states delivery not build so treat 1960 as approximate. Its de Havilland Goblin 35 engine is separately accessioned|DH115; Vampire T55; T55; MSN 15815; 15815|Shannon Aviation Museum|on_display|IE
Fouga|CM.170|-2|219|Super Magister||fixed_wing|monoplane|military|trainer||Irish Aviation Foundation accession 1118; served 1975 to 1999. Six Magisters were bought by the state in 1975 to replace the six ageing Vampire T.55s of No. 1 Fighting Squadron; the type is best known abroad as the **Silver Swallows** display team which won Best Display by an Overseas Team at RIAT Fairford in 1997. Two Turbomeca Marboré VI engines separately accessioned. NOTE: the Irish Air Corps carried these as F219 etc. in some records and 219 in others|CM170; F219; Super Magister; Magister|Shannon Aviation Museum|on_display|IE
Fouga|CM.170|-2|220|Super Magister||fixed_wing|monoplane|military|trainer||Irish Aviation Foundation accession 1021; served 1975 to 1999. The catalogue adds a provenance detail found nowhere else: **"This aircraft was moved to the museum from SETU; Carlow"** — it had been an instructional airframe at the South East Technological University campus at Carlow before coming to Shannon|CM170; F220; Super Magister; Magister|Shannon Aviation Museum|on_display|IE
Fouga|CM.170|-2|216|Super Magister||fixed_wing|monoplane|military|trainer||**RECONCILED FROM CONFLICTING SOURCES — see NOTES.** The museum's Exhibitions page advertises "3x Fouga Magister CM170" but its accession catalogue documents only 219 and 220; en.wikipedia's Irish Air Corps list states that "#216 and #220 are on display at Shannon Aviation Museum". Taking the three sources together the third airframe is 216. Confirm with the museum before import|CM170; F216; Super Magister; Magister|Shannon Aviation Museum|on_display|IE
Percival|Provost|T.53|183|Provost||fixed_wing|monoplane|military|trainer|1955|Irish Aviation Foundation accession 1115; the catalogue records MSN PAC/P53/1029 and delivery in 1955. Armed advanced trainer capable of carrying two .30 calibre machine guns for gunnery training; one Alvis Leonides radial; the engine is separately accessioned. Photographed at Baldonnel as early as 29 July 1967 (Commons)|Provost T53; T53; MSN PAC/P53/1029; PAC/P53/1029; Hunting Percival Provost|Shannon Aviation Museum|on_display|IE
SIAI-Marchetti|SF.260|WE|231|Warrior||fixed_wing|monoplane|military|trainer|1977|Irish Aviation Foundation accession 1119; arrived 1977; served to 2004. The catalogue explains the designation: **the E in SF260WE stands for Éire**. Ten were acquired to replace the Chipmunk and Provost; one 260 hp Avco Lycoming O-540 fuel-injected engine separately accessioned|SF260; SF-260WE; SF260WE; Warrior|Shannon Aviation Museum|on_display|IE
de Havilland Canada|DHC-1|T.20|168|Chipmunk||fixed_wing|monoplane|military|trainer||Irish Aviation Foundation accession 1120; the catalogue records MSN C1-0450 and service from 1952 to 1976. **SERIAL CONFLICT:** en.wikipedia's Irish Air Corps list says "#164 is on display at Shannon Aviation Museum" for the Chipmunk T.20. I have taken the museum's own accession record over Wikipedia; the c/n C1-0450 will settle it definitively|DHC1; Chipmunk T20; T20; MSN C1-0450; C1-0450|Shannon Aviation Museum|on_display|IE
Reims|FR172|H|206|Rocket||fixed_wing|monoplane|military|recon|1972|Irish Aviation Foundation accession 1117 (catalogued as "Irish Air Corps Cessna 172 R206"); built by Reims Aviation in France under Cessna licence in 1972 and bought for IE£20 000 each in response to increased trouble on the Northern Ireland border; used for border surveillance; prisoner escorts; wildlife surveys and general transport. **All Reims Rockets were retired on 4 October 2019** after 63 578 flying hours across 47 years. Continental O-360D engine separately accessioned|FR172H; FR-172; Reims Rocket; Cessna FR172H; R206|Shannon Aviation Museum|on_display|IE
Reims|FR172|H|210|Rocket||fixed_wing|monoplane|military|recon|1972|Second Reims Rocket at Shannon per en.wikipedia's Irish Air Corps list ("#206 and #210 are on display at Shannon Aviation Museum") and consistent with the museum's Exhibitions page advertising "2x Reims Rocket FR172H". NOT separately present in the accession catalogue searches I ran; confirm the accession number with the museum|FR172H; Reims Rocket; Cessna FR172H|Shannon Aviation Museum|on_display|IE
Blackburn|Buccaneer|||||fixed_wing|monoplane|military|ground_attack||Listed on the museum's Exhibitions page under the International Collection. No serial; the Irish Aviation Foundation catalogue returned no Buccaneer record because that catalogue covers only the Irish Air Corps national collection. **Whether this is a complete airframe or a cockpit section is NOT established** — the same page lists several exhibits explicitly as cockpits and this one is not so qualified. Do not confuse with Ulster Aviation Society's Buccaneer S.2B XV361|Buccaneer S2|Shannon Aviation Museum|on_display|GB
BAC|One-Eleven|||||fixed_wing|monoplane|civilian|commercial_transport||COCKPIT SECTION — listed on the museum's Exhibitions page as "BAC One Eleven Cockpit". No registration|BAC 1-11; One Eleven; BAC111|Shannon Aviation Museum|on_display|
English Electric|Lightning|||||fixed_wing|monoplane|military|fighter||COCKPIT SECTION — listed on the museum's Exhibitions page as "English Electric Lightning Cockpit". No serial|Lightning|Shannon Aviation Museum|on_display|GB
SEPECAT|Jaguar|||||fixed_wing|monoplane|military|ground_attack||COCKPIT SECTION — listed on the museum's Exhibitions page as "SEPECAT Jaguar Cockpit". No serial. Distinct from the complete Jaguar GR.3 XZ361 at the Estonian Aviation Museum and from Ulster Aviation Society's XZ389|Jaguar|Shannon Aviation Museum|on_display|GB
Bede|BD-5|||||fixed_wing|monoplane|civilian|private||Listed on the museum's Exhibitions page under the International Collection. No registration|BD5|Shannon Aviation Museum|on_display|
Piper|PA-28||||Cherokee|fixed_wing|monoplane|civilian|private||Listed on the museum's Exhibitions page simply as "Piper Cherokee". Model recorded as the PA-28 family designation; the specific sub-variant is NOT stated and is deliberately blank. No registration|Cherokee; PA28|Shannon Aviation Museum|on_display|
Cessna|150|||||fixed_wing|monoplane|civilian|private||Listed on the museum's Exhibitions page under the International Collection. No registration|Cessna 150|Shannon Aviation Museum|on_display|
Cessna|337||||Skymaster|fixed_wing|monoplane|civilian|private||Listed on the museum's Exhibitions page as "Cessna Skymaster". Model recorded as 337 which is the twin-boom push-pull Skymaster; if the exhibit is in fact a single-engined 336 or a Reims-built FTB337 this needs correcting. No registration|Skymaster; Cessna 337; O-2|Shannon Aviation Museum|on_display|
Supermarine|Spitfire|||||fixed_wing|monoplane|military|fighter||**REPLICA COCKPIT — FLAG THIS.** The museum's Exhibitions page lists "Supermarine Spitfire Cockpit Replica" in the World War II exhibition. Not an airframe and not original; recorded for completeness and clearly flagged|Spitfire cockpit replica|Shannon Aviation Museum|on_display|

### Foynes Flying Boat & Maritime Museum
Boeing|314|||Clipper|Yankee Clipper|fixed_wing|monoplane|civilian|commercial_transport||**FULL-SIZE REPLICA — FLAG THIS.** A walk-through reproduction of the Pan American Airways Boeing 314 "Yankee Clipper" with reconstructed flight deck; navigation and radio room; dining saloon; passenger seating and sleeping berths and lavatories — all photographed in detail by geograph.org.uk contributors and captioned by them as a replica. **No original Boeing 314 survives anywhere in the world.** No registration exists for the replica and none must be assigned|B314; Boeing B314; Yankee Clipper; B-314|Foynes Flying Boat & Maritime Museum|on_display|US

### National Museum of Ireland -- Decorative Arts and History
de Havilland|DH.115|T.55||Vampire||fixed_wing|monoplane|military|trainer||en.wikipedia's List of aircraft of the Irish Air Corps states in its lead that a de Havilland Vampire is on display at the National Museum in Collins Barracks. **tail_number deliberately BLANK.** The Air Corps operated seven T.55s serialled 185-187; 191-193 and 198; #191 is documented at Shannon and #198 was an instructional airframe; but no source I reached says which one is in Dublin and an invented Irish Air Corps number would collide with the real airframe|DH115; Vampire T55; T55|National Museum of Ireland -- Decorative Arts and History|on_display|IE
Miles|M.14A|Magister I||Magister||fixed_wing|monoplane|military|trainer||en.wikipedia's List of aircraft of the Irish Air Corps states in its lead that a Miles Magister is on display at Collins Barracks; the same article's retired-aircraft table says "#34 is on display in the Air Corps Museum" — an institution that closed in 2024. **tail_number deliberately BLANK** because the two statements have not been reconciled by any source: #34 is the only Irish Magister recorded anywhere as preserved and is the probable identity; but probable is not sourced. The Air Corps operated 27 Magisters serialled 31-40; 73-77 and 127-138 from 1939 to 1953|M14; M.14A; Magister I; Miles Magister|National Museum of Ireland -- Decorative Arts and History|on_display|IE

### Focke-Wulf Fw 200 Condor crash memorial -- Dingle
Focke-Wulf|Fw 200|||Condor||fixed_wing|monoplane|military|recon||**ENGINE ONLY — FLAG THIS.** OpenStreetMap node/12176277636 names the exhibit "World War II plane crash site: Engine of Focke-Wulf Fw 200 Condor" with access=yes; aircraft:type=military; model:wikidata Q157485 and operator "Luftwaffe KG 40". A recovered engine from a wartime crash; not an airframe. The KG 40 attribution comes from the surveyor and is plausible for an Atlantic-patrol Condor lost off the Dingle peninsula but has not been confirmed against a loss record. No Werknummer|Fw200; Condor; Kurier; FW-200|Focke-Wulf Fw 200 Condor crash memorial -- Dingle|on_display|DE

### Ulster Aviation Society -- Long Kesh
British Aerospace|Harrier|GR.9|ZD465|Harrier||fixed_wing|monoplane|military|ground_attack||Arrived March 2026 — the collection's most recent major acquisition|ZD 465; Harrier GR9|Ulster Aviation Society -- Long Kesh|on_display|GB
British Aerospace|Hawk|T.1A|XX260|Hawk||fixed_wing|monoplane|military|trainer||Gifted by the Royal Air Force in 2023|XX 260; Hawk T1A|Ulster Aviation Society -- Long Kesh|on_display|GB
Blackburn|Buccaneer|S.2B|XV361|Buccaneer||fixed_wing|monoplane|military|ground_attack||Purchased in 1994 and **flown from Aldergrove to Langford Lodge in a 4 mile flight lasting 92 seconds** before the collection later moved to Long Kesh by road|XV 361; Buccaneer S2B|Ulster Aviation Society -- Long Kesh|on_display|GB
de Havilland|DH.115|T.11|WZ549|Vampire||fixed_wing|monoplane|military|trainer||Donated by the Royal Air Force in 1988. Note this is the RAF T.11 not the export T.55 flown by Ireland|WZ 549; Vampire T11; DH115|Ulster Aviation Society -- Long Kesh|on_display|GB
Embraer|EMB-312||G-BTUC|Tucano||fixed_wing|monoplane|military|trainer||**The seventh prototype**; used by Short Brothers for Tucano development work; acquired 2001. Carries a civil registration|EMB312; G BTUC; GBTUC; Tucano|Ulster Aviation Society -- Long Kesh|on_display|GB
English Electric|Canberra|PR.9|XH131|Canberra||fixed_wing|monoplane|military|recon||Acquired in 2010 with a National Lottery grant. The society separately holds a Canberra cockpit section|XH 131; Canberra PR9|Ulster Aviation Society -- Long Kesh|on_display|GB
Fairchild|F-24|W-41A|HB612|Argus||fixed_wing|monoplane|military|utility||Donated in 2012|F24; F-24W-41A; HB 612; Argus|Ulster Aviation Society -- Long Kesh|on_display|GB
Fairey|Gannet|ECM.6|XA460|Gannet||fixed_wing|monoplane|military|electronic_warfare||Acquired in 2011; recorded in the source as ECM.6/AS.4 — the airframe was converted from the anti-submarine AS.4 to the electronic countermeasures ECM.6|XA 460; Gannet ECM6; Gannet AS4|Ulster Aviation Society -- Long Kesh|on_display|GB
Fairey|Swordfish|II|HS503|Swordfish||fixed_wing|biplane|military|air_to_surface||**Arrived February 2026**; donated by the RAF Museum|HS 503; Swordfish II|Ulster Aviation Society -- Long Kesh|on_display|GB
Fieseler|Fi 103|||V-1||missile_rocket||military|cruise||**FULL-SCALE MODEL — FLAG THIS.** Recorded in the source as a full-scale model carrying the British Aviation Preservation Council number BAPC.403; acquired 2010. Not an original flying bomb|Fi103; V1; V-1; Doodlebug; BAPC.403; BAPC403|Ulster Aviation Society -- Long Kesh|on_display|DE
Fouga|CM.170|R-2|218|Super Magister||fixed_wing|monoplane|military|trainer||**Presented by the Irish Air Corps in 2021** — an Irish airframe on the northern side of the border. Recorded in the source as "Fouga CM-170R-2 Magister 'Super Magister 218'"|CM170; F218; Super Magister; Magister|Ulster Aviation Society -- Long Kesh|on_display|IE
Gloster|Meteor|T.7|WA634|Meteor||fixed_wing|monoplane|military|test||**Martin-Baker ejection-seat test aircraft**; gifted by the RAF Museum in 2022. Recorded in the source as T7.5; a Martin-Baker hybrid conversion designation|WA 634; Meteor T7; T7.5|Ulster Aviation Society -- Long Kesh|on_display|GB
Grumman|F4F||JV482|Wildcat|Martlet|fixed_wing|monoplane|military|fighter||**Ditched in Portmore Lough in 1944 and recovered from the lake in 1984** with the help of other groups and a British Army helicopter; the society's first full airframe; restoration was nearing completion in 2024. Known to the Royal Navy as the Martlet. UNDER RESTORATION rather than complete|F4F; Wildcat; Martlet; JV 482|Ulster Aviation Society -- Long Kesh|under_restoration|GB
Hawker|Sea Hawk|FB.5|WN108|Sea Hawk||fixed_wing|monoplane|military|ground_attack||Donated by Short Brothers in 1989|WN 108; Sea Hawk FB5|Ulster Aviation Society -- Long Kesh|on_display|GB
Hunting|Jet Provost|T.3A|XM414|Jet Provost||fixed_wing|monoplane|military|trainer||On loan from Castlereagh Borough Council since 2003|XM 414; Jet Provost T3A; JP|Ulster Aviation Society -- Long Kesh|on_display|GB
McDonnell Douglas|F-4|K|XT864|Phantom II||fixed_wing|monoplane|military|fighter||Bought from the RAF for £26 000 in 2015; recorded in the source as Phantom FG1/F-4K/M — the Royal Navy F-4K airframe later flown by the RAF as the FG.1|F4K; Phantom FG1; FG.1; XT 864|Ulster Aviation Society -- Long Kesh|on_display|GB
Panavia|Tornado|GR.4|ZG771|Tornado||fixed_wing|monoplane|military|ground_attack||Donated by the Royal Air Force in 2021. The society separately holds a Tornado cockpit section|ZG 771; Tornado GR4|Ulster Aviation Society -- Long Kesh|on_display|GB
Percival|Sea Prince|T.1|WF122|Sea Prince||fixed_wing|monoplane|military|trainer||Acquired in 2017|WF 122; Sea Prince T1|Ulster Aviation Society -- Long Kesh|on_display|GB
Reims|FR172|H|203|Rocket||fixed_wing|monoplane|military|recon|1972|**Ex-Irish Air Corps; arrived 2021.** en.wikipedia's Irish Air Corps list independently confirms "#203 is on display at Ulster Aviation Society Museum". One of the eight FR172H Rockets bought in 1972 for border surveillance and retired 4 October 2019|FR172H; Reims Rocket; Cessna FR172H|Ulster Aviation Society -- Long Kesh|on_display|IE
Scottish Aviation|Bulldog|T.1|XX637|Bulldog||fixed_wing|monoplane|military|trainer||Gifted to the society in 2019. **Wears the FALSE serial XX613** per the source; the true identity is XX637 and the painted marking is in aliases|XX 637; XX613; Bulldog T1|Ulster Aviation Society -- Long Kesh|on_display|GB
SEPECAT|Jaguar|GR.1|XZ389|Jaguar||fixed_wing|monoplane|military|ground_attack||Gifted by the Royal Air Force in 2023|XZ 389; Jaguar GR1|Ulster Aviation Society -- Long Kesh|on_display|GB
Short|SB.4||G-14-1|Sherpa||fixed_wing|monoplane|civilian|experimental||Arrived 2008 on long-term loan from the Imperial War Museum. The SB.4 Sherpa was Short's aero-isoclinic wing research aircraft; G-14-1 is a class-B trials marking|SB4; Sherpa; G14-1; G-14-1|Ulster Aviation Society -- Long Kesh|on_display|GB
Short|SB.5||WG768|||fixed_wing|monoplane|military|experimental||**Arrived 10 December 2025**; donated by the RAF Museum Midlands. The SB.5 was the variable-sweep research aircraft that validated the English Electric Lightning wing planform — an internationally significant airframe|SB5; WG 768|Ulster Aviation Society -- Long Kesh|on_display|GB
Short|SD.2|||Stiletto||drone||military|drone||Supersonic target drone built by Short Brothers|SD2; Stiletto|Ulster Aviation Society -- Long Kesh|on_display|GB
Short|Tucano|T.1|ZF378|Tucano||fixed_wing|monoplane|military|trainer||Moved to the society in late 2024. **Painted in FALSE markings as Spitfire 'P7832 Enniskillen'** — the true identity is ZF378 and the painted marking is in aliases|ZF 378; P7832; Tucano T1|Ulster Aviation Society -- Long Kesh|on_display|GB
Slingsby|Cadet|TX.1|XN239|Cadet||fixed_wing|monoplane|military|trainer||Glider; arrived by 2022. Recorded as being restored off site; hence under_restoration|XN 239; Cadet TX1|Ulster Aviation Society -- Long Kesh|under_restoration|GB
Supermarine|Spitfire|IIa||||fixed_wing|monoplane|military|fighter||**REPLICA — FLAG THIS.** Recorded in the source as "Supermarine Spitfire IIa Replica BAPC.369 marked as 'P7823'"; delivered to the society in 2013. tail_number is BLANK because a replica has no service serial; the painted marking and the BAPC number are in aliases|BAPC.369; BAPC369; P7823; Spitfire IIa replica|Ulster Aviation Society -- Long Kesh|on_display|
Aero Composites|Sea Hawker||EI-BUO|||fixed_wing|monoplane|civilian|private||Recorded in the source as "Aero Composites (Lavery) Sea Hawker"; an Irish-registered amphibian homebuild; acquired 1998|EI BUO; EIBUO; Lavery Sea Hawker|Ulster Aviation Society -- Long Kesh|on_display|IE
Aerosport|Scamp|A||||fixed_wing|biplane|civilian|private||Unflown and unregistered; donated 2013. **Carries the FALSE marking 'NI-UAS'** which is not a real registration; recorded in aliases. tail_number deliberately blank|Scamp A; NI-UAS; NIUAS|Ulster Aviation Society -- Long Kesh|on_display|
Clutton|FRED|Series 2|G-BNZR|||fixed_wing|monoplane|civilian|private||Recorded in the source as "Clutton-Tabenor FRED Series 2"; donated 2010|G BNZR; GBNZR; FRED|Ulster Aviation Society -- Long Kesh|on_display|GB
Eipper|Quicksilver|||||fixed_wing|monoplane|civilian|private||Ultralight; acquired 2012. No registration recorded|Quicksilver|Ulster Aviation Society -- Long Kesh|on_display|
Eurowing|Goldwing||G-MJWS|||fixed_wing|monoplane|civilian|private||Donated in 2000|G MJWS; GMJWS; Goldwing|Ulster Aviation Society -- Long Kesh|on_display|GB
Evans|VP-2||G-BEHX|||fixed_wing|monoplane|civilian|private||Donated; arrived 2016|VP2; G BEHX; GBEHX|Ulster Aviation Society -- Long Kesh|on_display|GB
Ferguson|Flyer||G-CJEN|||fixed_wing|monoplane|civilian|private|2016|**REPLICA — FLAG THIS.** A reproduction of Harry Ferguson's 1911 monoplane; the source records that it flew only once; in 2016; and arrived at the society later that year. year_built 2016 reflects the replica's own completion; the original design dates from 1911|Ferguson Flyer 1911 replica; G CJEN; GCJEN|Ulster Aviation Society -- Long Kesh|on_display|GB
HAPI|SF-2A||||Cygnet|fixed_wing|monoplane|civilian|private||**UNASSEMBLED KIT**; arrived 2013. Not a completed aircraft; recorded under_restoration to reflect that honestly|SF2A; SF-2A; Cygnet|Ulster Aviation Society -- Long Kesh|under_restoration|
Monnett|Monerai|||||fixed_wing|monoplane|civilian|private||Glider; arrived 2017; holds British Gliding Association number BGA.2988 and is **marked 'EVN'** which is a BGA trigraph competition marking rather than a registration. tail_number blank; both identifiers in aliases|BGA.2988; BGA2988; EVN; Monerai|Ulster Aviation Society -- Long Kesh|on_display|GB
Rotec|Rally|2B|G-MBJV|||fixed_wing|monoplane|civilian|private||Ultralight; arrived 2013|Rally 2B; G MBJV; GMBJV|Ulster Aviation Society -- Long Kesh|on_display|GB
Short|330||G-BDBS|||fixed_wing|monoplane|civilian|commercial_transport||Donated by Short Brothers in 1992; a Belfast-built regional airliner in the collection housed in Short's own wartime hangars|SD3-30; Shorts 330; G BDBS; GBDBS|Ulster Aviation Society -- Long Kesh|on_display|GB
Team|Himax|1700R|G-MZHM|||fixed_wing|monoplane|civilian|private||Acquired 2007|Himax 1700R; G MZHM; GMZHM|Ulster Aviation Society -- Long Kesh|on_display|GB
Air & Space|18A||EI-CNG|||rotary_wing||civilian|private||Autogyro; arrived 2012 on what the source calls a "5-year loan" — a loan that has run well past its stated term; ownership should be re-checked|Air and Space 18A; EI CNG; EICNG|Ulster Aviation Society -- Long Kesh|on_display|IE
Bristol|Sycamore|HR.14|XJ918|Sycamore||rotary_wing||military|search_rescue||Gifted from the RAF Museum Midlands in 2022|XJ 918; Sycamore HR14|Ulster Aviation Society -- Long Kesh|on_display|GB
Robinson|R22||G-RENT|||rotary_wing||civilian|private||On loan to the society since 2003|R-22; G RENT; GRENT|Ulster Aviation Society -- Long Kesh|on_display|GB
Sud Aviation|SA 316|B|202|Alouette III||rotary_wing||military|search_rescue||**Ex-Irish Air Corps; gifted in 2009.** en.wikipedia's Irish Air Corps list independently confirms "#202 is on display at Ulster Aviation Society Museum". One of eight SA 316B Alouette IIIs serialled 195-197; 202 and 211-214 which served 1963 to 2007 and assisted 3300 people in search-and-rescue and air-ambulance work|SA316; SA 316B; Alouette III; Alouette 3|Ulster Aviation Society -- Long Kesh|on_display|IE
Westland|Gazelle|AH.1|XZ332|Gazelle||rotary_wing||military|utility||Came to the society in 2024|XZ 332; Gazelle AH1|Ulster Aviation Society -- Long Kesh|on_display|GB
Westland|Lynx|AH.1|XZ666|Lynx||rotary_wing||military|utility||Arrived in 2024|XZ 666; Lynx AH1|Ulster Aviation Society -- Long Kesh|on_display|GB
Westland|Puma|HC.1|XW222|Puma||rotary_wing||military|transport||Arrived in 2014|XW 222; Puma HC1|Ulster Aviation Society -- Long Kesh|on_display|GB
Westland|Scout|AH.1|XV136|Scout||rotary_wing||military|utility||Arrived in 2014. The source gives the serial without a mark; AH.1 was the only Scout variant in British Army service|XV 136; Scout AH1|Ulster Aviation Society -- Long Kesh|on_display|GB
Westland|Wessex|HC.2|XR517|Wessex||rotary_wing||military|transport||Acquired in 2004|XR 517; Wessex HC2|Ulster Aviation Society -- Long Kesh|on_display|GB
Beagle|A.61||G-AVCS|Terrier||fixed_wing|monoplane|civilian|private||**WRECK**; arrived 2017; ex-military WJ363 per the source. Recorded under_restoration to reflect its condition honestly|A61; Terrier; G AVCS; GAVCS; WJ363|Ulster Aviation Society -- Long Kesh|under_restoration|GB
Cameron|N-90||G-TANK|||lighter_than_air||civilian|private||**BASKET ONLY** — the source records a hot-air balloon basket; not a complete balloon with envelope|N90; G TANK; GTANK|Ulster Aviation Society -- Long Kesh|on_display|GB
Chargus|Cyclone|||||fixed_wing|monoplane|civilian|private||Hang glider; acquired 1994; British Aviation Preservation Council number BAPC.263|BAPC.263; BAPC263; Cyclone|Ulster Aviation Society -- Long Kesh|on_display|GB
Rogallo|Hang glider|||||fixed_wing|monoplane|civilian|private||Hang glider acquired in 2000; British Aviation Preservation Council number BAPC.266. The source gives only "Rogallo" which is a wing configuration rather than a manufacturer; recorded as given because inventing a marque would be worse|BAPC.266; BAPC266; Rogallo|Ulster Aviation Society -- Long Kesh|on_display|
Pitts|S-1|A|N80BA|Special||fixed_wing|biplane|civilian|private||**CRASH WRECKAGE**; donated 2016. Recorded under_restoration|S1A; S-1A; Pitts Special; N 80BA; N80BA|Ulster Aviation Society -- Long Kesh|under_restoration|US


---

## NOTES

### 1. Sources and their weight

**What carried this region, in order:**

1. **Wikimedia Commons `categorymembers` API.** This was the decisive source and it is worth
   saying why, because it is not obvious. A small number of aviation photographers upload to
   Commons using a rigid filename convention — `<operator>, <serial>, <manufacturer type>.jpg`
   — and then file the results into per-museum, per-type categories. The result is that
   `Category:Aircraft at the Estonian Aviation Museum` and its twelve type subcategories
   yielded an operator-and-serial inventory of an entire museum that publishes NO serials on
   its own website: XZ994, XZ361, ZE256, MM6507, R-2112, HW-326, 37-91, 3212, 9011, 0615,
   1234, ES-PLY, ES-PMA, ES-PSF, ES-ACO, ES-JPL, ES-HRJ, ES-ULM, ES-1003, UR-87590, HA-MCQ,
   OK-AIP, OM-JLP, YL-LEB, ES-BAB, ES-LTA and the bort numbers 10, 4, 09, 32, 25, 39, 52, 36,
   50, 64. Nothing else I tried came close. The same trick worked at Riga (the
   `(Skulte)` versus `(Riga airport)` subcategory split is itself the proof that the museum
   moved) and partially at Kaunas.
2. **Latvian Wikipedia's exhibit tables.** `lv:Rīgas Aviācijas muzejs` carries five wikitables
   giving type and bort number for 47 exhibits including cockpit sections, with two
   construction numbers where borts were unavailable. English Wikipedia's article on the same
   museum is a 20-line stub with an unsourced type list and a wrong relocation date. **This
   is the single clearest demonstration in this pass of why the contract insists on searching
   in the local language.**
3. **Institutional websites, fetched today.** lennundusmuuseum.ee, lam.lt, airmuseum.lv,
   shannonaviationmuseum.com, flyingboatmuseum.com and esm.ee were all live on 10 September
   2026 and between them settled opening seasons, prices and — at Kaunas and Shannon — two
   events from 2026 that no directory anywhere will have caught up with yet.
4. **irishaviationfoundation.ie/collection/.** The Shannon museum's own accessioned object
   database, searchable, 34 pages, with accession numbers, MSNs, service dates and
   provenance paragraphs. It is a primary source and it beat Wikipedia twice (see Corrections).
5. **OpenStreetMap via Overpass on maps.mail.ru.** Produced 55 Baltic hits and 9 Irish hits.
   Its value is not the museums — it is the monuments: eleven Latvian, Estonian and Lithuanian
   roadside and park airframes that appear in no directory at all. Where a surveyor traced an
   airframe as a *polygon* rather than dropping a point, I have treated the record as much
   stronger, because tracing means someone looked at the aircraft's actual footprint.

**What proved stale, and exactly how:**

- **English Wikipedia, `Riga Aviation Museum`**: says the museum moved to Skulte "in 2022".
  Latvian Wikipedia gives the cited date as **24 August 2021**, following a 31 March 2021
  eviction deadline. One year out on the only fact anyone needs from that article.
- **OpenStreetMap node/1890213866 (Lithuanian Aviation Museum)**: `opening_hours=Mo-Fr
  09:00-17:00`. The museum's own site says Monday 10:00–16:00, Tuesday–Saturday 10:00–18:00,
  closed Sunday. The OSM hours are wrong in three separate ways.
- **OpenStreetMap way/976058477 (Riga Aviation Museum)**: `charge=7 EUR`. The museum says €10
  adult / €5 child.
- **OpenStreetMap node/687057014 (Estonian Aviation Museum)**: still carries the address
  "Haaslava vald, 62101", an administrative unit abolished in the 2017 Estonian municipal
  reform. The museum says Kastre vald, 62115.
- **OpenStreetMap node/8742962694**: still named "Atlantic Air Venture". Same address, same
  phone-book entry, but the institution has been Shannon Aviation Museum for years.
- **en.wikipedia `List of aircraft of the Irish Air Corps`**: two serial statements that
  disagree with the museum's own accession catalogue (see Corrections).
- I did NOT use aviationmuseum.eu or silverhawkauthor.com at any point, and nothing in this
  file derives from them. I did not use Grokipedia.

### 2. Corrections made

- **The Irish Air Corps Museum at Casement Aerodrome is CLOSED.** It shut in 2024; the
  collection went on loan to Shannon (announced 13 April 2024, FlyingInIreland) because the
  Air Corps needed the floor space; and it went on year-round public display for the first
  time on **27 August 2026** in the new **Eddie Ryan Memorial Wing** (RTÉ News, 27 August
  2026). Baldonnel is therefore NOT recorded as a museum site. Every directory that lists it
  as `restricted`/`appointment` is describing something that no longer exists.
- **Atlantic AirVenture is not a separate site.** Same address (Link Road, Smithstown,
  V14 PH34), same phone, same organisation, renamed. Creating both would duplicate.
- **Foynes' Boeing 314 is a full-size replica**, not an original. No Boeing 314 survives
  anywhere. Recorded and flagged.
- **Lennusadam's Short 184 is a full-size replica.** et.wikipedia states this explicitly and
  adds that no original Short 184 survives in the world. The brief described it as "the Short
  184"; the correct record is a replica, and it is flagged as one.
- **Riga Aviation Museum has NOT been evicted out of existence.** It moved, on a specific
  date, to a specific address, and is ticketed and open. Its TLS certificate has expired,
  which is not the same thing as a closure.
- **Estonian Aviation Museum's Phantom is an F-4F, not an F-4C.** The museum's own page is
  headed "F-4C Phantom II" but says the aircraft came from Germany; Germany never operated the
  F-4C. Commons gives it as German Air Force 37-91 F-4F. Recorded as F-4F with the museum's
  own error documented.
- **et.wikipedia's "Saab 430" is a typo for Saab 340.** Recorded as Saab 340.
- **Shannon's Chipmunk: museum says 168, Wikipedia says 164.** The museum's accession record
  (1120) gives MSN C1-0450 as well as the number, so I took the museum. The c/n will settle it.
- **Shannon's Magisters: three sources, three different pairs.** The Exhibitions page says
  "3x Fouga Magister"; the accession catalogue documents F219 and F220; Wikipedia says 216 and
  220. Reconciled as 216 + 219 + 220, which is the only reading consistent with all three.
  Flagged in the row descriptions.
- **Two Ulster Aviation Society airframes wear false serials** and have been recorded with the
  true identity in `tail_number` and the painted marking in `aliases`: Bulldog T.1 **XX637**
  painted as 'XX613', and Short Tucano T.1 **ZF378** painted as Spitfire 'P7832 Enniskillen'.
  A third, the Aerosport Scamp, wears 'NI-UAS' which is not a registration at all.
- **Riga's An-24 has two documented identities.** The lv.wikipedia table gives СССР-46400; the
  Commons photograph of the same airframe is filed as Latavio YL-LCD. Both are recorded.
- **Riga's Yak-28: table says Yak-28P, OSM and Commons say Yak-28R.** Recorded as the table
  has it with the dispute stated in the row.
- **Estonian Aviation Museum's MiG-21: museum says bis, Commons says MF.** Variant left blank
  rather than picked.
- **Its Starfighter: museum says F-104 ASA, Commons says F-104G.** Variant left blank. MM65xx
  is an F-104G serial range, which favours Commons, but that is inference and not evidence.
- **Its Yak-28: museum and et.wikipedia say Jak-28PP, Commons says Yak-28P.** Variant blank.
- **Its Su-24: Commons says Su-24M2.** The M2 was a Russian upgrade; Ukraine flew M and MR.
  Variant blank.

### 3. Judgment calls

- **Replicas recorded and flagged**, never presented as originals: Short 184 (Lennusadam),
  Boeing 314 "Yankee Clipper" (Foynes), Lituanica flyable replica built by Vladas Kensgaila in
  1982 for the film *Skrydis per Atlantą* (Kaunas), VEF I-12 (Riga Airport), Spitfire IIa
  BAPC.369 and the Ferguson Flyer 1911 reproduction and the Fi 103 V-1 full-scale model
  (Ulster), Spitfire cockpit replica (Shannon). The Lituanica replica and the Lituanica
  *original wreckage* are at two different Kaunas museums and are recorded separately and
  explicitly cross-referenced, because conflating them is the standard error.
- **Nose and cockpit sections recorded as such**, not as whole aeroplanes: at Riga, two Su-24M
  cockpits, a Sukhoi T-10 (Su-27 prototype) section, a Su-15 nose, a Tu-104A cockpit, a
  Tu-134B cockpit and a "MiG-29UB remains"; at Shannon, BAC One-Eleven, English Electric
  Lightning and SEPECAT Jaguar cockpits. Each says so in its description.
- **The Dingle Condor is an ENGINE.** Recorded because it is a deliberate, signposted,
  publicly accessible memorial with a stated type and unit, but the description says engine
  only, in capitals, so nobody later reads it as an airframe.
- **The Cameron N-90 at Ulster is a basket** with no envelope. Recorded `lighter_than_air`
  and flagged.
- **Wrecks and unbuilt kits recorded `under_restoration`, not `on_display`**: the Portmore
  Lough Wildcat JV482 (recovered 1984, restoration near complete in 2024), the Beagle Terrier
  wreck, the Pitts S-1A crash wreckage, the unassembled HAPI Cygnet kit, the off-site Slingsby
  Cadet. Calling a kit in boxes "on display" would be false.
- **Airworthy aircraft recorded `on_display`** where they form part of a presented collection:
  the Aeroprakt A-22 at Lange (et.wikipedia calls it "lendav") and the flyable Lituanica
  replica at Kaunas.
- **`access_type` reasoning.** Ulster Aviation Society is `appointment`, not `restricted`:
  the barrier is that an all-volunteer body must roster someone to open the gate, not a
  military checkpoint, and there is no charge. The Estonian Aviation Museum is `public` even
  though it closes for winter — a seasonal museum is still walk-up in season, and it takes
  groups year-round by arrangement. The Ämari memorial is `public` because it sits in the
  village, not inside the base perimeter. The Riga airport VEF replica is `public` because it
  is landside in the terminal forecourt.
- **`operator_country` policy, applied deliberately.** RU on every Riga airframe that only
  ever wore Soviet markings — which is nearly the whole collection, and each row says so.
  Latvia's post-1991 air force never operated MiG-21s, Su-7s, Tu-22Ms or Mi-24s, so LV would
  be wrong on all of them. EE only where the Estonian Air Force or Border Guard actually flew
  the aircraft after 1991 (R44 '64', L-410 ES-PLY, Mi-8 ES-PMA, Schweizer ES-PSF and the
  Estonian civil registrations). LT only for the An-26B and L-39C transferred from the
  Lithuanian Air Force by government resolution of 29 September 2010, for the Lithuanian
  designs (ANBO I, BrO-18, VK-9) and for the Zokniai L-39. IE for Irish Air Corps airframes
  including the three now north of the border at Ulster (Fouga 218, Cessna FR172H 203,
  Alouette III 202) and for the Irish-registered civil aircraft there. GB for RAF and Royal
  Navy airframes. Left BLANK where genuinely unknown — the Mi-26T at Dārzciems, the roadside
  An-2s, the Riga Cessna 150, the L-13 gliders, the Ulster hang glider, and every Unidentified
  row.
- **Construction numbers went into `aliases`, not `tail_number`**, exactly as instructed,
  wherever a bort was unavailable: Riga's MiG-23BM (c/n 3910601), Riga's Cessna 150
  (c/n 15059081), both Su-24M cockpits (0515318 and 0915306), the T-10 section (02-04), and
  Shannon's Vampire (15815), Provost (PAC/P53/1029) and Chipmunk (C1-0450). For the
  bort-numbered Riga and Kaunas airframes the c/n really is the only unique identifier, and
  in most cases nobody has published it.
- **Two-digit Soviet borts are not unique and I have said so in the rows.** The Riga collection
  alone contains a Mi-1 "17" and an Mi-8T "17", an An-2 "22" and an L-29 "22" and a Yak-28
  "22". This is precisely the collision `operator_country` exists to mitigate, and it is why
  no serial anywhere in this file was inferred from a photograph of a similar aircraft.

### 4. EXCLUDED, and why

- **Irish Air Corps Museum, Casement Aerodrome (Baldonnel).** Closed 2024; collection at
  Shannon. Do not create. The Casement Commons category contains only period photographs and
  a handful of museum-interior shots; the Overpass sweep of Ireland found no `historic=aircraft`
  or `aeroway=gate_guardian` node anywhere at Baldonnel. If a gate guard exists there it is
  unmapped and unphotographed on Commons.
- **Atlantic AirVenture, Shannon.** Same site as Shannon Aviation Museum under a former name.
- **Aviācijas muzejs "Spilve", Riga** (OSM node/2803440764, Daugavgrīvas iela 140,
  spilve-rix.lv). Tagged `opening_hours=closed` with a surveyor note: "Some time already
  museum is closed; in survey June 2016 it was still closed." Ten years dark. Not recorded as
  an active site; worth a check by someone local before it is written off permanently.
- **Shannon Airport Aviation Gallery** (OSM node/13608392710, operator Mike Kelly). A large
  and locally admired **model aircraft** collection displayed at the airport. No airframes.
  Excluded on that basis, not on quality.
- **Dolly's Grove aerodrome (EIDG), Culmullin, Co. Meath** — OSM nodes 13607766681, 13607766682
  and 13607766683, three `historic=aircraft` nodes with no other tags, sitting on the apron of
  a **private** aerodrome (way/404325288, `aerodrome=private`, access=private taxiway) attached
  to a manor house. Excluded under the contract's "operational aircraft are not displays" rule:
  three untyped aircraft parked at a private strip are far more likely to be somebody's
  aeroplanes than a display. If someone can show it is a collection, it becomes a site.
- **Latvijas Kara muzejs, Riga.** Latvia's national war museum. I found no aircraft in it —
  no Commons aircraft category, no OSM `historic=aircraft` node in or near the Powder Tower.
  A well-searched zero; do not re-research without new evidence.
- **Ventspils Piejūras brīvdabas muzejs.** ventspilsmuzejs.lv reset the connection on 10
  September 2026 and I found no aircraft evidence from any other source. This is an
  unresolved zero rather than a confident one — see Needs a human.
- **Lielvārde air base.** No `historic=aircraft`, `memorial=aircraft` or `aeroway=gate_guardian`
  node anywhere near it in the Baltic sweep. No Commons category. Nothing found. Latvia's
  air force has flown very little that would make a gate guard.
- **Aviacijos pradininko A. Griškevičiaus memorialinis muziejus, Viekšniai** (OSM
  node/3459082401). A municipal memorial museum to Aleksandras Griškevičius, the 19th-century
  Lithuanian aviation theorist, in his home town. No airframes; the subject predates powered
  flight. Excluded as a site with aircraft; it may still be worth a record as an aviation
  heritage site if the database wants those.
- **Non-aircraft exhibits deliberately not recorded as aircraft rows**: at Lange, a Flak 88 and
  a Danish Madsen anti-aircraft gun, seven radars (P-37, the Yak-28PP set, the Draken 35 set,
  an Il-76 set, a DRL-7SK antenna from Tartu Ülenurme, a Tesla OPRL-4 landing radar from
  Kuressaare and a PN-671 precision approach radar), eleven aero engines, ~450 scale models, a
  T-34-85 and a BTR-60; at Riga, an РСП-7Т landing radar, an СКП-9МВ mobile control post, a
  TRUMP D40-D de-icer and an AA-60 fire tender; at Kaunas, the Tupolev A-3 aerosled-amphibian
  and a large fire-service vehicle collection. None of these is an aircraft.
- **Saaremaa Sõjavara Muuseum, Sõrve militaarmuuseum, Hiiumaa militaarmuuseum, Vaivara
  Sinimägede muuseum, Soomepoiste muuseum, Liepājas okupācijas muzejs, Bumbu patvertne 495,
  Sakaru bunkurs, Memel Automuseum, Retro auto muzejs, Järva-Jaani Vanatehnika muuseumide
  keskus** and the other military and technology museums returned by the second Baltic Overpass
  sweep. Checked, none showed aircraft evidence. Järva-Jaani is the one I would re-check first
  — a large volunteer-run old-technology centre of that kind often acquires an airframe.

### 5. Blank fields, deliberately

- **Every `tail_number` on a Swedish-loaned airframe at Lange** (Draken, Viggen, Lansen).
  Swedish two-digit individual codes are not serials; the five-digit airframe numbers were not
  published in any source I reached. The codes are in the descriptions.
- **Both `tail_number`s at Collins Barracks.** The types are sourced; the serials are not. An
  invented Irish Air Corps number would look authoritative and collide with the real airframe.
- **`variant` on eight airframes where two sources disagree** (listed under Corrections).
  Picking a side would have manufactured certainty.
- **`postal_code` for the National Museum of Ireland.** Nominatim returned "D13 XKV4" for a
  Dublin 7 address; that is internally inconsistent and I would not propagate it.
- **`year_built` on all but four rows.** Nowhere did I have a sourced construction, roll-out,
  first-flight or delivery date. The four exceptions are Shannon's Vampire (1960, inferred from
  a stated January 1961 delivery and flagged as approximate in the row), Provost 183 (1955,
  stated), SF260WE 231 (1977, stated) and the Reims Rockets (1972, stated) plus the Kensgaila
  Lituanica replica (1982, stated) and the BrO-18 glider (1975, from the photograph caption).
  No serial anywhere in this file was read as a year.
- **`operator_country` on 30-odd rows** — see the policy paragraph above.
- **`website` on every monument site.** They have none.

### 6. Needs a human — ranked

1. **Cavan & Leitrim Railway, Dromod, Co. Leitrim — +353 71 9638599.** Wikipedia says the
   transport museum holds "planes" and names none; cavanandleitrim.com returns HTTP 421
   Misdirected Request on both HTTP/1.1 and HTTP/2 (an SNI misconfiguration on their server,
   not a blockage at this end). One phone call gets the whole inventory. Currently zero
   aircraft rows for a site that certainly has some.
2. **South East Aviation Enthusiasts Group, Waterford.** `www.seaeg.ie` does not resolve at
   all (DNS failure, not a 404), there is no Commons category, and the Overpass sweep of the
   Waterford Airport area (52.0,-7.3,52.4,-6.8) returned **no** `historic=aircraft` node and no
   named club. I could not establish that the group is still active or where its airframes
   are. The brief names the **Aermacchi AM.3C Bosbok** as an Irish type and it appears nowhere
   in the Irish Air Corps type list — if a Bosbok is preserved in Ireland, SEAEG is the likely
   holder and this is the thread to pull.
3. **Shannon Aviation Museum — +353 61 363687.** Four things one call would settle: the
   accession number and confirmation of the second Reims Rocket (#210); confirmation of the
   third Fouga (216); whether the Chipmunk is 168 (their catalogue) or 164 (Wikipedia); and
   whether the "Blackburn Buccaneer" in the International Collection is a complete airframe or
   a cockpit. Ask for MSNs on the international collection while you have them.
4. **Ventspils Piejūras brīvdabas muzejs, Latvia.** ventspilsmuzejs.lv reset the connection on
   every attempt. This open-air coastal museum is named in the brief and I could neither
   confirm nor exclude an aircraft. Retry from a different network.
5. **Ämari, Estonia — what is the memorial aircraft?** OSM node/13232245984 at 59.25504,
   24.20521 says `memorial=aircraft` and nothing else. One photograph resolves an entire site
   record from Unidentified to a real airframe. Ämari hosted Su-24 units in the 1970s–80s
   which makes a Fencer or a MiG plausible, but plausible is not a record.
6. **Lakūno Stepono Dariaus gimtinė, Dariaus km., Klaipėda district — +370 698 81025**
   (a branch of Lietuvos aviacijos muziejus, s.dariausgimtine@lam.lt). **Three** aircraft are
   traced as polygons on this property, one of them under cover, and no published description
   of the site mentions them. Three Unidentified rows that ought to be three real ones.
7. **Įstros aviacijos muziejus, Stanioniai — +370 616 86996, aviapark.lt.** The operator
   describes the collection as *muliažai*, mock-ups. Establish whether any genuine ex-service
   airframes are among them. If yes, this becomes a real multi-aircraft site; if no, the single
   flagged placeholder row is the honest record.
8. **Ciemupe, Ogre district, Latvia (56.7815, 24.6496).** Four airframes beside the A6 with no
   owner, no name, no access information and no institution within 250 m. The site name in
   this file is provisional and coined by me. Someone driving the Rīga–Daugavpils road can fix
   this in ten minutes.
9. **Nākotnes parks, Glūda, Jelgava district (56.6081, 23.4547).** Three untyped airframes in
   a named public park. Same fix, same effort.
10. **Estonian Aviation Museum — info@lennundusmuuseum.ee, +372 58539093.** Ask for the
    airframe register: serials for the Saab 340, the L-13 Blaník and both An-2s, and a ruling
    on the four disputed variants (F-104 ASA vs G, MiG-21 bis vs MF, Yak-28 P vs PP, Su-24
    plain vs M2). They are an accredited museum with a published collections policy and a
    2023–2026 research plan, so the register exists.
11. **Valga militaarteemapark, Estonia.** et.wikipedia's Ämari article cites an ERR report of
    18 December 2024 headlined "Viimane õhuväe teenistuses olnud helikopter jõudis Valga
    militaarteemaparki" — the last helicopter in Estonian Air Force service reached the Valga
    military theme park. Estonia struck off its Robinson R44s and An-2s during 2024. This site
    is **not in OpenStreetMap** under any name containing "militaar" and I could not geocode
    it, so it has no site record here. It should have one.
12. **Piirivalvekopter, Maarjamäe, Tallinn (59.45526, 24.84155)** and the untyped
    `historic=aircraft` node at **Karuskose, Sandra küla, Põhja-Sakala vald (58.4675,
    25.04103)**. Two Estonian airframes with no type and no host. The Karuskose one is not
    recorded as a site at all because I could not establish that it is a display rather than
    a derelict — it is listed here so nobody re-researches it blind.
13. **Ireland West Airport Knock (53.909, -8.840)** — OSM way/1282958788, an untyped
    `historic=aircraft` polygon in the apron/taxiway area — and **Bohernabreena, Tallaght
    (53.25491, -6.35218)**, OSM node/14124226926, an untyped `historic=aircraft` node among
    houses on Piperstown Road. Neither is recorded as a site: at Knock I cannot distinguish a
    preserved airframe from a stored or withdrawn one on an apron, and at Bohernabreena I have
    no evidence of public presentation. Both are cheap to check locally.
14. **Ulster Aviation Society — DEDUPLICATION CHECK BEFORE IMPORT.** The brief said to check
    the database's 302 existing UK sites first. I could not: the CSV files in this working
    directory (`/home/claude/build2/museums_final.csv`, `museums_new.csv`, `museums.csv`)
    contain **zero** rows with country "United Kingdom", so they are not the UK slice and no
    local check was possible. Whoever imports this must query the live database for
    "Ulster Aviation Society" / "Long Kesh" / "Maze" before creating the site, and if it exists,
    merge the ~50 airframe rows into it rather than duplicating the site.
