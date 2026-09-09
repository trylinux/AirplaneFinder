# Philippines — research notes

29 sites, 78 airframes. Files: `ph_museums.csv` plus one `<slug>_aircraft.csv` per site.

The country has one real aviation museum, one public air park, and a long tail of single
airframes on plinths — inside base wires, in town plazas, at a resort, at a children's
museum, in a mansion's back garden. The single-airframe sites are the majority of the
record count and were the hardest part of the sweep.

---

## 1. Sources used, and how each behaved

**Primary / on-site**

- **`wrecks.hatenablog.com`** (Japanese "用廃機ハンターが行く！" / retired-airframe hunter).
  The single most valuable source for this country. The author physically visits, reads
  data plates where he can, and dates every visit — Air Force City Park April 2025,
  AFP Museum February 2026, Naval Station Jose Andrada April 2025, Marikit Park, Anne
  Raquel's Resort, the NAIA-T3 S.211. He also publishes access instructions (which gate,
  which jeepney, whether photography is allowed). Almost every currency judgement below
  rests on him. His overview page estimates ~70 retired airframes in the Philippines
  across ~30 locations, fewer than 10 of them reachable by a civilian — which matches
  what this sweep found (78 airframes, 12 of 29 sites `public`).
- **`aerialvisuals.ca`** — worked reliably by direct `curl` to
  `Airframes.php?Seeds=<serial>`; the WebFetch path is blocked. Used to confirm c/n and
  ex-US serial for ~15 airframes (see §3).
- **Duncan's F-86 Sabre website (`yocumusa.com/sweetrose/duncan/...`)** — a 1990s-vintage
  worldwide F-86 register, but the only source that distinguishes the Villamor gate guard
  from the Villamor museum aircraft, and the only one that gets the Mactan Sabre serial
  right. Its Philippine data is from 1987–1997 sightings; treat locations as needing
  re-confirmation, serials as good.
- **AirHistory.net collection 260** — dated photographs of the PAF Museum, most recently
  4 February 2024. This is the proof that the museum park aircraft were still in place
  after the October 2023 closure.

**Compilations**

- **Wikipedia type-survivor lists** (`List of surviving North American F-86 Sabres`,
  `List of displayed Bell UH-1 Iroquois`, `List of displayed Lockheed T-33 Shooting Stars`,
  `List of surviving North American P-51 Mustangs`, and the Philippines sections of the
  `Northrop F-5`, `Vought F-8 Crusader`, `SIAI-Marchetti S.211`, `MBB Bo 105`,
  `North American T-28 Trojan`, `Fairchild C-123 Provider`, `Fokker F27 Friendship`,
  `Lockheed C-130 Hercules`, `Grumman HU-16 Albatross`, `Sikorsky H-34` and `NAMC YS-11`
  articles). Fetched as raw wikitext, which is far more reliable than the rendered page.
  These are where roughly two-thirds of the *sites* came from — including Cantilan,
  Tagaytay, Villa Escudero, Passi, Silay, Camp Cape Bojeador and the two Zamboanga
  entries, none of which appear in any aviation-museum directory. Error-prone on serials
  (three corrections in §3) and thin on citations: Tagaytay, Camp Navarro and the two
  Zamboanga airframes carry no reference at all.
- **`aviationmuseum.eu`** — lists exactly two Philippine sites (PAF Museum, Air Force
  City Park). Its Clark page was last updated December 2016 and its serial list is
  otherwise sound; its Villamor serial table is right where the blog-post version of the
  same site (`aviationmuseum.eu/Blogvorm/...`) is badly scrambled — that Blogvorm page
  pairs serials with the wrong aircraft types (it hands the Sikorsky UH-34's BuNo to the
  F-8, and so on) and should not be used.
- **`silverhawkauthor.com`** — lead generation only; four aircraft, all at the PAF Museum,
  and it repeats the 44-74627 mix-up described below.

**Stale, blocked or useless**

- **`paf.mil.ph`** — the Philippine Air Force's own site was unreachable through the proxy
  for the whole session (`ws_closed_mid_exchange`) and is `robots.txt`-blocked for
  WebFetch. Several of the most useful references in Wikipedia point at
  `paf.mil.ph/news-articles/...` pages that are now dead links and **are not in the
  Wayback Machine** — specifically the Air Power Park inauguration article and the Passi
  City Huey turnover article. Those two would settle several open questions.
- **`airhistory.net/collections`** index — Cloudflare-challenged; individual collection
  pages are reachable, the index is not, so I could not enumerate other Philippine
  collections that may exist there.
- **Wikimedia Commons** has no "aircraft on display in the Philippines" category tree.
- **Grokipedia** appeared in search results for Basa, Mactan, Fernando and PATTS. Not used,
  per the spec.
- WebSearch quota was exhausted partway through; the later half of the sweep ran on the
  MediaWiki search API, direct `curl`, and following citations out of wikitext. Bing via
  `curl` was tried and returned generic junk for every aviation query — not usable.

---

## 2. Site-level judgement calls

**Philippine Air Force Aerospace Museum, access_type = `public`.** It sits inside Villamor
Air Base but a member of the public has always simply walked or taxied in and paid ₱20.
It closed 16 October 2023 for rehabilitation; TripAdvisor still shows "Temporarily closed"
and has no review after 2023. However the PAF has published a "PAF RELAUNCHES AIR FORCE
MUSEUM" news item and a 2026 travel aggregator quotes the PAF's own "gearing up for its
grand relaunch" post plus recent visitor comments, and AirHistory has dated 4 February 2024
photographs of ten of the park aircraft. I have therefore recorded it as open and public.
**This is the single most important thing to re-verify before import** — see §5.

**`restricted` was assigned to every serving air base and army camp** (Basa, Rabina, Camp
Servillano Aquino, Fernando, Danilo Atienza, Mactan, Edwin Andrews, Camp Navarro, the
Villamor gate guard, Philippine Navy Museum at Fort San Felipe, PNP Museum at Camp Crame)
because a civilian needs a gate pass. Camp Servillano Aquino is the sharpest example: a
visitor pass is issued in exchange for a passport but photography inside is prohibited, so
the aircraft are in practice only photographable from the road through the fence.

**Armed Forces of the Philippines Museum = `restricted`, not `public`.** Quezon City's
tourism page advertises walk-in hours and a ₱100 foreigner fee, but a foreign visitor was
turned away at the Camp Aguinaldo gate in February 2026 for lack of an invitation letter
or pre-issued pass. Judged by how a member of the public actually gets in, this is
restricted.

**Air Power Park (PMA Baguio) = `appointment`.** Fort Gregorio del Pilar takes tourists,
but entry is capped at 300 visitors a day and requires advance registration at
`bisita.pma.edu.ph`.

**Naval Station Jose Andrada = `public`.** The Bo 105 stands in a small fenced plot beside
the main gate facing Roxas Boulevard; it is viewable and photographable from the public
pavement 24 hours a day, and the guard will usually let you into the plot if you ask. The
land is Navy land, but the access test in the spec is about the visitor, not the owner.

**Camp Cape Bojeador = `public`.** The Philippine Marine Corps camp was opened to
"military tourism" in March 2024.

**Anne Raquel's Resort = `public`.** A roadside eyecatcher at a two-star hotel on the
Roman Superhighway; the intercity bus stops in front of it.

**Palacio de Memoria = `public`.** A private events venue in Parañaque with paid entry and
a bar built inside the An-24; the two airliners are on the grounds, not operated.

---

## 3. Corrections made, with the evidence

1. **P-51D 44-74627 is at the PAF Museum, not at Basa Air Base.** Wikipedia's P-51
   survivor list carries *two* Philippine entries that are the same aeroplane —
   "44-74627 – Cesar Basa Air Base" and "3733/4823 – 'Shark of Zambales', PAF Aerospace
   Museum". Warbird Registry's page for 44-74627 gives the whole chain: USAAF 44-74627 →
   PAF 73373 → displayed at Basa AB 1977-79 as 3733/001 "The Shark of Zimbales" → PAF
   Museum since 2000. AirHistory adds c/n 122-41167 and states plainly that the museum
   aircraft was "incorrectly serialled 3733 … and now falsely marked as 4823". Recorded
   once, at the museum, tail 44-74627, with 4823/3733/73373 in aliases. **There is no P-51
   at Basa Air Base**; do not create one.
2. **Mactan's Sabre is 52-4835, not 52-4845.** Wikipedia's F-86 list cites Duncan's
   register for this entry, and Duncan says "52-4835, F-86F, Mactan AB, on pole by
   30Jan97". Recorded as 52-4835 with 52-4845 in aliases.
3. **The two "524140" F-86Ds.** Duncan records 52-10015 as the Villamor Air Base gate
   guard "as '524140' by .95", and separately an unidentified F-86D at the PAF Museum
   marked '69411'. Wikipedia's current text agrees that the airframe wearing 524140 on the
   base is really 52-10015, and puts a true 52-4140 in the museum park in Centennial
   livery. Since a 2025 on-site survey found the '69411' machine at the **AFP Museum in
   Camp Aguinaldo**, not at Villamor, the picture is: 52-4140 in the museum park;
   52-10015 as base gate guard wearing 524140; the ex-Villamor unidentified airframe now
   at Camp Aguinaldo wearing 69411. Recorded that way, as three separate airframes at
   three site records.
4. **AFP Museum Huey.** Wikipedia gives 12503; the February 2026 on-site survey read
   70-15931 (displayed as 15931). Used 70-15931, kept 12503 in aliases.
5. **PAF Museum F-8H is 147056.** AirHistory has one 2019 caption reading 147506; its own
   2012 and 2024 captions and Aerial Visuals both give 147056 (c/n 798, PAF number 313).
   Digit transposition in the one caption.
6. **PAF Museum Albatross is 48607, not 49607.** Aerial Visuals: HU-16B, s/n 48607 PhiAF,
   c/n G-026, ex 48-607. A 2019 blog list gives 49607, which matches nothing.
7. **Air Force City Park T-33A is ex-USAF 52-9257**, not a 1955-block serial as Wikipedia's
   Baugher citation implies (Aerial Visuals: c/n 7323, PAF 52257 = 52-9257). Likewise the
   museum T-33A 29806 = 52-9806, c/n 8066.
8. **Air Force City Park T-28 "645" = AT-28D 114645.** The park inventories list a bare
   "645"; Wikipedia's T-28 list has "114645 – Clark Air Base". Same aircraft, merged.
9. **Air Force City Park F-8 "48661" = BuNo 148661** (Aerial Visuals). Same pattern as
   PAF F-5A "13326" = 64-13326, T-41D "8958" = 68-8958, T-6G "150162" = 51-15162.
10. **PAF Museum T-28 is a T-28C.** BuNo 140533 falls inside the T-28C BuNo block
    (140447–140662), which agrees with the museum's own labelling; Aerial Visuals gives
    c/n 226-110 without a variant.
11. **Silay, not Negros Oriental.** Manila Bulletin's headline says the F-27 went to
    "Negros Oriental"; the Philippine News Agency story and Wikipedia both put it in
    People's Park, Barangay E. Lopez, **Silay City, Negros Occidental**. Used Silay.

---

## 4. Painted markings that are not identities

Recorded per the spec: true identity in `tail_number`, visible marking in `aliases`,
explanation in `description`.

| Site | Aircraft | Wears | Actually |
|---|---|---|---|
| Villamor AB gate | F-86D | 524140 | 52-10015 |
| PMA Air Power Park | F-8H | 148696 | 148686 (the real 148696 never served with the PAF) |
| Marikit Park | RA-5C 156627 | NASA scheme of A-5A 147858 "WST858" | 156627, ex-USS Kitty Hawk NH-605 |
| PAF Museum | P-51D | 4823 (earlier 3733) | 44-74627 / PAF 73373 |
| Naval Stn Jose Andrada | Bo 105C | 142 | 414 (c/n S-168, ex P021) |
| PAF Museum | Temco TT-1 | 44233/233 | 44234 |
| Anne Raquel's Resort | F-8J | BuNo 145544, modex UE-12 | unknown; probably 150911 |

**Four `tail_number` fields were left deliberately blank** because no source is decisive:

- **AFP Museum F-86D** — "69411" is not a valid USAF F-86D serial and Duncan carries the
  airframe as unidentified.
- **Anne Raquel's Resort F-8J** — 145544 is demonstrably false (that airframe was an F-8B
  lost off Okinawa in 1968). Forgotten Jets / the hatenablog author infer 150911, an F-8J
  burnt at Cubi Point on 8 September 1975, but that is inference, not a reading.
- **Museo Pambata UH-1H** — Wikipedia's entry is the uninterpretable string "16328 8522".
  Both numbers are in aliases.
- **PAF Museum Boeing PT-13D** — displayed as "551"; sources variously give 76-759,
  76-7551 and US Army 42-17488, and one calls it an N2S-3. All four in aliases.

`year_built` is blank on **every** row. No source consulted gave a construction, roll-out,
first-flight or delivery date for any individual Philippine airframe; the only dates
available are US serial-block years, which are not the same thing.

`wing_type` is blank on all rotary-wing rows, as required. `variant` is blank on the PAF
Museum HU-16 (Aerial Visuals says HU-16B, Wikipedia says HU-16A, aviationmuseum.eu says
SA-16A) and on the two SIAI-Marchetti S.211s at Basa and the one at PMA, which are
identified only by construction number.

---

## 5. Excluded — do not re-research these

- **Philippine Army Museum, Fort Bonifacio, Taguig.** Real museum, real outdoor park, but
  the outdoor exhibits are artillery, tanks and APCs only. No aircraft. Excluded.
- **Corregidor Island / Pacific War Memorial Museum, Mount Samat, Capas National Shrine,
  the Leyte landing memorials.** All checked; all are ordnance, relics and monuments. No
  airframe, no recovered aircraft wreck on display at any of them. Excluded.
- **Basa Air Base F-86F 52-4832 and 52-4843.** Duncan records 52-4832 "stored partly
  stripped by 27Jan97" and 52-4843 as a "wreck by Mar93", plus "many Sabres … in a
  scrapyard near Basa AB" in the 1980s. These are scrap, not displays, and there is no
  post-1997 sighting of either. Excluded.
- **Clark Air Base F-5A 67-21190 and F-5B 74-0780.** Wikipedia's F-5 list puts both at
  "Clark Air Base", and the 74-0780 citation is a forum thread titled "Air Force Park
  Clark Field". But the April 2025 on-site survey of Air Force City Park itemises exactly
  five aircraft and neither is among them, and the Flickr photograph cited for 74-0780
  carries no caption or location data. Rather than invent a phantom site or inflate the
  park, both are left out — see the open questions.
- **PATTS College of Aeronautics, FEATI University, WCC Aeronautical and Technological
  College, Indiana Aerospace University (Cebu).** All four were checked. None publishes
  an airframe inventory and no third-party source records a specific aircraft with an
  identity at any of them. These campuses do hold instructional airframes; I could not get
  a single sourced serial, so nothing was recorded. Left as an open question rather than
  an exclusion.
- **Lumbia (Cagayan de Oro) OV-10 Bronco.** Wikipedia's OV-10 article carries a photo
  captioned "PAF OV-10A SLEP at Lumbia Airport", but the Broncos were only withdrawn from
  service on 28 December 2024 and nothing indicates this airframe was ever a display
  rather than a parked operational aircraft. Operational aircraft are not displays.
  Excluded pending evidence of a plinth or a turnover.
- **Sangley Point AH-1S Cobras.** Same reason — retired 28 December 2024, no turnover or
  display reported.
- **Philippine Aerospace Development Corporation.** PADC's Hummingbird and its Britten-
  Norman assembly line are industrial, not display. Nothing found on a preserved PADC
  airframe.
- **Philippine Airlines heritage aircraft.** No sourced preserved PAL airframe was found
  anywhere in the country. The only preserved civil airliners located are the two at
  Palacio de Memoria (An-24B RP-C7205, ex-Mosphil Aero; DC-9-31 RP-C1544, ex-Cebu Pacific)
  and the Aero Commander 681 RP-C775 sitting engineless at Camp Servillano Aquino.
- **Wartime wreck recoveries.** No Philippine museum was found holding a recovered P-38,
  A6M Zero or other WWII airframe on display. The four WWII-era aircraft in the country
  (P-51D, PT-13D, C-47 and T-6 at the PAF Museum) are ex-service aircraft, not recoveries.

---

## 6. Coordinates

To 4 decimals throughout. Where a precise airframe or gate position was available it was
used — Air Force City Park (15.1753/120.5413), Marikit Park, Anne Raquel's Resort, the
NAIA-T3 S.211, Naval Station Jose Andrada, the PAF Museum, Camp Servillano Aquino and the
AFP Museum all come from a visitor's own GPS readings; Basa, Museo Pambata, Villa Escudero,
Fort San Felipe, Camp Crame, Danilo Atienza, PMA, Cantilan and Zamboanga airport come from
OpenStreetMap or Wikipedia infobox coordinates for the facility.

**Six rows are town or facility centroids, not airframe positions**, and should be
tightened before or after import:

- **Tagaytay City Aircraft Display** — town centroid. No sourced location for the F-5A at all.
- **Passi City Eco-Park** — Passi city centroid; the Eco-Park itself is not in OSM.
- **People's Park, Silay City** — Silay city centroid; the park is not in OSM.
- **Greenbelt Park, Gumaca** — Gumaca town centroid; the park is not in OSM.
- **Camp Cape Bojeador** — Cape Bojeador headland; the camp perimeter is not mapped.
- **Camp Navarro, Zamboanga** — camp centroid, and the site identification itself is
  provisional (below).

Two others are approximations within a known facility: the Villamor gate guard
(14.5136/121.0154, base main gate area, not a surveyed airframe position) and the
Mactan-Benito Ebuen aircraft park (base coordinates).

---

## 7. Open questions, ranked

**1. Has the PAF Aerospace Museum actually reopened, and is the full park intact?**
Everything about the largest site in the country hangs on this: it closed 16 October 2023,
the PAF has published a relaunch announcement without a date reachable through the proxy,
and the newest independent review is from 2023. Also needed from the same call: whether
the T-33A 29806 and the Aero Commander 11250 are still in the park (neither appears in the
2019 walk-round inventory; the Aero Commander was photographed in February 2024), and
whether the Aero Commander is a 500 or a 690A.
→ **Philippine Air Force Public Information Office / the museum itself.** The AFP Museum
gives `afpmuseum@gmail.com`, +63 2 8911-6001 loc. 6777 and +63 2 8912-7664; the PAF PIO is
the right route for the Aerospace Museum. **One call here closes four or five records.**

**2. The Air Power Park inauguration article and the Passi City Huey turnover article at
`paf.mil.ph` are dead and not archived.** Between them they would confirm the full Air
Power Park inventory (I have five aircraft from three type articles and cannot tell whether
that is the complete park), the Passi Huey's identity, and probably the exact display
positions. Same contact as above.

**3. What is at Clark Air Base outside Air Force City Park?** F-5A 67-21190 and F-5B
74-0780 are both credited to "Clark Air Base" and neither was in the park in April 2025.
Are they inside the PAF's Haribon/600th Air Base Wing area, are they gone, or is the park
inventory simply incomplete? Also unresolved: Wikipedia's UH-1H "8911 – Clark Air Base",
which may be a duplicate of park machine 09171 (66-16905).
→ 600th Air Base Wing, Clark Air Base.

**4. Is "Camp Enrile, Zamboanga City" Camp Navarro?** The C-123K 54-0525 is sourced only
to an unreferenced Wikipedia line naming a camp I cannot otherwise locate; I placed it at
Camp General Basilio Navarro (WestMinCom HQ) and flagged the site name and coordinates as
provisional. The same call would confirm AT-28D 100310 at Edwin Andrews Air Base and the
P-51D "Red Knight" 475562 at the airport — three airframes in one city, all thinly sourced.
→ Western Mindanao Command / Edwin Andrews Air Base public affairs.

**5. Aeronautical school airframes.** PATTS (Parañaque), FEATI (Manila), WCC Aeronautical
(Bocaue/Antipolo) and Indiana Aerospace University (Lapu-Lapu City) all run airframe
laboratories and are very likely to hold real retired aircraft, but not one identity could
be sourced. Four emails would probably add four to eight airframes and up to four sites.

**6. Basa Air Base needs a physical survey.** Eleven airframes are recorded there — the
largest concentration after the museum — but the four Sabres rest on 1987–1997 sightings,
and the two S.211s and the F-8H have no dated sighting at all. Basa is an active 5th
Fighter Wing base hosting FA-50s, so a media-day visit is the realistic route.

**7. Tagaytay F-5A 66-9143** has no source, no address and no photograph. It may not exist.
Worth one check with the Tagaytay city tourism office before importing the site.

**8. Serial-to-US-serial mapping for the plinth Sabres and Mustangs.** Cantilan's F-86F
24317 and Zamboanga's P-51D 475562 are recorded with their PAF numbers only. The PAF
pattern (52-4468 → 24468, 64-13326 → 13326, 51-15162 → 150162) suggests obvious candidates,
but the spec forbids guessing, so the US serials are absent. Joe Baugher's serial pages or
a Philippine Air Force historical office query would close both.

---

## 8. Local-language names

The site names in the CSV are the English/visitor-recognisable forms. Local names:

- Philippine Air Force Aerospace Museum — *Museo ng Himpapawid ng Hukbong Himpapawid ng Pilipinas*
- Armed Forces of the Philippines Museum — the outdoor half is **Kagitingan Park**
- Museo Pambata — Filipino for "children's museum"; the English name is not used
- Marikit Park, Olongapo — also transliterated "Markit Park" in some reports
- Camp General Servillano Aquino — the on-base heritage display is separate from the
  Aquino Center and Museum (Ninoy & Cory Aquino Foundation), which reopened in 2025 and
  holds no aircraft
- Air Power Park is signed in English at Fort Gregorio H. del Pilar (Fort del Pilar)

Searches in Filipino (*museo ng himpapawid*, *eroplano monumento*, *monumento na eroplano*)
returned nothing that English-language searching had not already found; the productive
non-English source for this country turned out to be Japanese, not Filipino.

## Excluded after review (post-research pass)

- **"Shriver Skylark" (full-scale pioneer-aircraft replica), PAF Aerospace Museum** — dropped
  from `paf_aerospace_museum_aircraft.csv`. The row carried no source trail in these notes, the
  museum is not listed with it on any page reachable in this pass, and its wing configuration
  (biplane vs monoplane) could not be established. Recording it would have required guessing
  `wing_type`, which the file test suite enforces as non-blank for fixed-wing rows. Re-add it
  only with a photograph or a museum gallery listing. Everything else in the file is unchanged.

## Post-research processing (import pass, 9 Sep 2026)

- Every row was validated against the real importer (`tests/test_flagship_topup_files.py`)
  and the alias-hygiene suite before import. Two mechanical corrections were applied across
  this file set: dashless search variants were added where missing (`MiG-21` → `MiG21`,
  `MiG-21PF` → `MiG21PF`), and attribute words that had been filed as aliases (`replica`)
  were moved into `description`, where the convention puts them.
- Duplicate aliases within a row were removed; the database de-duplicates them anyway, and
  leaving them in the CSV made the file and the live record disagree.
- Serials were diffed against all 3,542 tail-numbered aircraft already in the database before
  import: zero collisions. Museum names were diffed against all 424 existing sites: zero
  collisions, exact or normalised.
- Museums were imported first, then aircraft, and the result was verified per site against
  the live API — every site's aircraft count matches this directory exactly.
