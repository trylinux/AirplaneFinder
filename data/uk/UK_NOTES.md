# United Kingdom — coordinator summary

Imported live 9 September 2026. Nine research passes (RAF Museum; naval and
London national museums; East Anglia museums plus the Duxford top-up; East
Anglia gate guards and monuments; Scotland / Northern Ireland / Crown
Dependencies; Northern England; the Midlands and Lincolnshire; South-East
England; South-West England and Wales). The per-pass research notes follow
this summary unchanged; where they disagree with this section, this section
is what was imported.

**Files:** `uk_museums.csv` (300 new sites) and 304 `*_aircraft.csv`
files, one per site — including four **top-up** files against sites that
already existed in the database: `rafm-london_topup` (89 rows added to the 2
already there), `duxford_topup` (65 added to 115),
`nmf-east-fortune_topup` (60 added to 1) and
`helicopter-museum_topup` (108 added to 1).

**Rows:** 2386 aircraft · 2212 with tail numbers (92%) ·
1979 on_display / 310 in_storage / 97 under_restoration.

**Sites by nation:** England 270, Wales 18, Scotland 7, Northern Ireland 3, Isle of Man 1, Guernsey 1.
**Access:** 191 public · 53 appointment · 56 restricted.

**Coordinates:** every site has one. Most were fixed by the researchers on the
airframe or the site; 36 blanks were filled from the site's postcode via
postcodes.io (postcode-centroid level, good to a street), and two Crown
Dependency sites from Nominatim. No town centroids were used.

## The source that made this pass work

`eurodemobbed.org.uk` — successor to the dead `demobbed.org.uk` — carries every
preserved ex-military airframe in the UK with a **dated last sighting**, indexed
by county. Seven of the nine agents walked its county pages programmatically
(roughly 1,000 location pages between them) and used the sighting dates as
currency evidence, then added the civil aircraft, gliders, replicas and missiles
it structurally cannot see from the museums' own inventories. Many sightings
read July-September 2026. **Update the skill: demobbed.org.uk is a parking page
now; eurodemobbed.org.uk is the spine.**

## Cross-pass adjudications (one airframe, one place)

Sixteen airframes came back at two sites. Resolved as follows, all by dated
evidence over undated lists:

- **The RAF Museum's 2025 disposals programme has actually dispersed.** Meteor
  F.8 prone-pilot **WK935** is at Newark (on loan since 2024); Devon C.2
  **VP952** at Gatwick (Aug 2025); Spitfire PR.XIX **PM651** at Hooton Park
  (Apr 2026); Swordfish **HS503** with the Ulster Aviation Society; Valetta C.2
  **VX573** at Blackbushe (Jun 2026). All five dropped from the Cosford file.
- **Montrose** — Sea Hawk **XE340** and Vampire T.11 **XD542** appear on stale
  lists there; the museum's own exhibits page has neither. XE340 recorded at the
  Fleet Air Arm Museum's Cobham Hall store, XD542 at Patrington (Aug 2026).
- **XG594** (Whirlwind) and **G-ATFG** (Brantly) were claimed by East Fortune;
  ABPic photographs put them at Yeovilton (2012) and Weston-super-Mare (2010).
- **G-BIRW** (MS.505 Criquet) claimed by Duxford; ABPic has never photographed
  it anywhere but East Fortune.
- **G-BRNM** (Chichester-Miles Leopard) — Bournemouth Aviation Museum's own page
  says G-BRNM went to the Midland Air Museum and G-BKRL stayed. Bournemouth row
  dropped.
- **XX899** (Buccaneer cockpit) left Newark in June 2026 for Oxfordshire, where
  Aces High photographed it in August; **XV490** (Phantom cockpit) left Newark
  for the British Phantom Aviation Group at Kemble. Both dropped from Newark.
- **RAF Wittering** was recorded twice, by the East Anglia and Midlands agents.
  The East Anglia version was kept — it correctly splits the publicly visible
  gate guardian (ZD469) from the restricted heritage museum.
- **False identities blanked** rather than imported: NELSAM's Amy Johnson
  Gipsy Moth is a replica wearing **G-AAAH** (the original is in the Science
  Museum); Hooton Park's Hoverfly is a composite built from KK995 wearing
  **KL110** (the RAF Museum has the real one).

## Live-database corrections made during this pass

- **Sea Fury WJ231.** The database carried WJ231 at the War Eagles Air Museum,
  New Mexico, on a record whose own description flagged a serial conflict with
  the ex-Iraqi Fury 253. WJ231 is the Korean War Sea Fury FB.11 in Hall 2 at
  Yeovilton, documented with its pilot and markings. The New Mexico record's
  tail was blanked live and the reasoning written into its description.
- **Harvard FE695** was already in the database as an airworthy Duxford
  resident (G-BTXI). The Aces High row claiming it was dropped.

## Coordinator corrections applied before import

- 191 dashless designation aliases added (`F4`, `T33A`, `AV8B` …) for the alias
  test.
- Model spelling normalised across the country: `F-4` + `FGR.2`/`FG.1` →
  `Phantom` + variant, `AV-8B` + blank → `AV-8` + `B`, with the old spellings
  kept as aliases so both find the aircraft.
- `FC-2W` and `B-8M` added to the test suite's whole-designation list.

**Validation:** every row passed `_validate_aircraft_row` and the alias suite;
zero museum-name collisions against the 1,783 museums then live; a combined dry
run of all 2386 rows reported `created: 2386, linked: 2386, errors: []`;
after import, all 304 per-site live counts equal the file counts.

## What is still thin

- **Scotland is under-swept.** Seven Scottish sites is too few for a country with
  a dense gate-guard and monument population; the pass covered the museums well
  but not the plinths. This is the single best next job in the UK.
- Kent Battle of Britain Museum's replica fleet (6-8 airframes) was deliberately
  omitted for lack of sourced BAPC identities.
- Brooklands and the Army Flying Museum both have broken collection pages;
  enthusiast lists disagree by ~15 airframes at Brooklands.
- Several large collections were excluded for genuinely having no public access
  and are named in the pass notes: Everett Aero (Sproughton, 19 airframes),
  HMS Sultan's 53 training airframes, Predannack's fire-school hulks,
  Chippenham Lodge, Bentwaters' stored jets, Marshall's stored Hercules.
- **RAF Halton and RAF Scampton are closing** and their airframes are moving;
  both need a re-check within a year.

---

# Research pass: RAF Museum (Hendon and Cosford)

# UK — Royal Air Force Museum (London / Hendon and Midlands / Cosford)

Output directory: `/home/claude/uk/rafm/`

| File | Rows | Notes |
|---|---|---|
| `uk_museums.csv` | 1 site | RAF Museum Midlands only. RAF Museum London already exists in the DB and is deliberately absent. |
| `rafm-london_topup_aircraft.csv` | 89 aircraft, 81 with a serial (91%) | `museum_name` = `Royal Air Force Museum London`, verbatim. Excludes the two already recorded (Bf 109 G, Mosquito B.35). |
| `rafm-midlands_aircraft.csv` | 128 aircraft, 97 with a serial (76%) | `museum_name` = `Royal Air Force Museum Midlands`. 84 on display, 40 in storage, 4 under restoration. Serial coverage is depressed by 26 missile/rocket rows that carry no serial. |

Excluding missiles and rockets, Midlands is 102 airframe rows with 97 serials (95%).

---

## Site naming

The Cosford site is recorded as **`Royal Air Force Museum Midlands`**. It opened in 1979 as
*The Aerospace Museum*, became *RAF Museum Cosford* in 1998, and was renamed *RAF Museum
Midlands*. The assignment gave the rename as 2024; the museum's own Annual Report and Financial
Statements 2022–23 dates it to **March 2022**, and the museum uses "Midlands" throughout its
current site. Recorded under the current name, with `RAF Museum Cosford` and `Cosford` findable
through the address and city fields. Note that the "Midlands" name is a common source of
confusion in stale lists, which still index the site as Cosford.

## Sources and how much weight each carried

1. **RAF Museum's own per-object collection pages** (`rafmuseum.org.uk/research/collections/<slug>/`) —
   the spine. There is no JSON feed (no `wp-json` collection endpoint), but every object page
   carries a structured block: **Serial No / Period / Reference / Museum (London|Midlands) /
   Location (hangar) / On Display (Yes|No)**. I harvested the full set from
   `collection-sitemap.xml` (248 URLs) plus 8 more found only in the paginated
   `…/things-to-see-and-do/on-display/` listings — 103 London objects and 146 Midlands objects,
   aircraft, vehicles, engines and missiles mixed together. This is as close to a structured
   museum feed as the RAF Museum offers and it is what fixes hangar location and the
   on-display flag.
   **But its sitemap `lastmod` is 2025-11-06 and it is materially stale for the Midlands site**
   (see corrections below). Six object pages listed in the on-display index now redirect to a
   generic page; for those I took museum and hangar from the listing card
   (Argosy, Harrier GR9A, B-17G, Devon, Dakota parts, Crossley vehicle).
2. **demobbed.org.uk** (Wolverhampton Aviation Group) — the decisive currency check.
   `Hendon, Barnet` (location 1613) noted **October 2025**; `RAF Cosford Museum` (1329) noted
   **August 2026**; `RAF Cosford Museum Store` (8454) noted **November 2025**. Where demobbed
   and the museum's web pages disagreed on *where* an airframe is, demobbed won, because it is
   more recent and gives a sighting date. Demobbed is **not exhaustive** — it covers ex-British-
   military airframes, so it silently omits the German, Japanese, American and civil types, and
   it also misses some genuine Hendon exhibits (Beaufort DD931, Bulldog K2227, Grasshopper
   WZ791). Absence from demobbed was therefore never treated as evidence of departure.
3. **Wikipedia `List of aircraft at the Royal Air Force Museum Midlands` / `… London`** — edited
   through June 2026 and much fresher than the museum's own pages. Used for leads and for the
   Cosford hangar re-shuffle. Its Midlands article carries a long commented-out block of
   "JUNE 2026 NOT LISTED ON WEBSITE" entries which turned out to be wrong in several cases
   (Hunter XG225, VC10 XR808 and Varsity WL679 are all still listed by the museum and all
   confirmed on site by demobbed in August 2026) — treated as a lead, not a fact.
4. **Vintage Aviation News, "RAF Museum Midlands (Cosford) – Restoration, Storage, and Disposals
   Update"** — the only source that itemises the Michael Beetham Conservation Centre and the
   March 2025 disposals list with serials. Used for MBCC contents and disposal status.
5. **RAF Museum site pages** for the Hangar 1 closure, the Test Flight/War in the Air gallery
   texts, and the MBCC access statement.

---

## Corrections made, with evidence

**The RAF Museum's own collection pages are wrong about which site several aircraft are on.**
The museum shuffles airframes between Hendon and Cosford and the web pages lag by a year or more.

| Airframe | Museum web page says | Recorded here as | Evidence |
|---|---|---|---|
| Chipmunk T.10 **WP912** (Duke of Edinburgh's) | Midlands, Hangar 1 | **London**, Hangar 5 | demobbed Hendon, Oct 2025; Wikipedia London |
| Pembroke C.1 **WV746** | Midlands, Hangar 1 | **London**, Historic Hangars | demobbed Hendon, Oct 2025; Wikipedia London |
| Twin Pioneer CC.1 **XL993** | Midlands, National Cold War Exhibition | **London**, Historic Hangars | demobbed Hendon, Oct 2025 ("XL993 at Cosford" only on an old photo caption); Wikipedia London notes "Formerly at RAFM Midlands" |
| Whirlwind HAR.10 **XP299** | London, Historic Hangars | **Midlands**, National Cold War Exhibition | demobbed Cosford, Nov 2025; Wikipedia Midlands NCW |
| Gazelle **XW855** | London, Historic Hangars (as "HT.3") | **Midlands**, Beetham Centre, not viewable | demobbed Cosford, Aug 2026. Left as an open question below — it is the one move I am least sure of. Also a variant correction: XW855 is an **HCC.4** Queen's Flight aircraft, not an HT.3. |
| Argosy **XP411** | Midlands, Hangar 1 | Midlands, **National Cold War Exhibition** | Hangar 1 is closed; Wikipedia June 2026 places it in the NCW hangar |
| Provost T.1 **WV562** | Midlands, Hangar 1 | Midlands, **National Cold War Exhibition** | same |
| Andover E.3A **XS639** | Midlands, Hangar 1 | Midlands, **external display** | demobbed "Museum, outside", Aug 2026 |
| Hampden TB.I **P1344** | not on the collection pages at all | **London**, Historic Hangars | demobbed Hendon Oct 2025; VAN reports it finished at the MBCC and ready for transfer to Hendon |

**Departed — recorded nowhere in these files:**

- **Avro Anson C.19 TX214** — the museum's collection page still shows it at Midlands, Hangar 1,
  On Display Yes. It has been **transferred to the Avro Heritage Museum, Woodford**. Excluded.
- **de Havilland Comet 1XB G-APAS / XM823** — collection page still shows Midlands, Hangar 1,
  On Display Yes. Put up for disposal in 2025 and **transferred to the South Wales Aviation
  Museum in September 2025**. Excluded from the Midlands file. This is the airframe most likely
  to be wrongly carried at Cosford by any other list.
- **Bristol Sycamore HR.14 XJ918** — the museum's Sycamore page and its own document archive use
  XJ918, but XJ918 appears to be **on loan to the Ulster Aviation Society**, and demobbed records
  the Hendon airframe as **HR.12 WV783** (ex G-ALSP). I recorded WV783 at Hendon and flagged the
  serial as needing confirmation. If XJ918 is in fact the Hendon machine, only the serial changes.

**Serial corrections**

- Hendon's **Bf 109** is an **E-3, Werknummer 4101 / RAF DG200**. The DB's existing
  "Messerschmitt Bf 109 G" at London is almost certainly the famous **Black 6**, Bf 109G-2/Trop
  Werknummer 10639 / RAF **RN228** — which is at **Cosford**, in the Test Flight hangar, and is
  in `rafm-midlands_aircraft.csv`. See open questions.
- Hendon's **Anson I** fuselage: the museum and Wikipedia both give **W2068**; demobbed identifies
  the airframe as **LT773** *marked as* W2068. Recorded per the brief's rule (true identity in
  `tail_number`, marking in `aliases`) as LT773 / alias W2068.
- **Bristol 188** is **XF926**, not XF923 (XF923 was the first airframe and did not survive).
  It is in the Cosford reserve store, not on display, and has been proposed for transfer to
  Aerospace Bristol.
- The three V-bombers at Cosford are Vulcan **XM598**, Victor **XH672** ("Maid Marian") and
  Valiant **XD818**. **Victor XH563 is not in this collection** and does not appear in any file
  here; the museum's Victor at Hendon is the **nose section of XM717** ("Lucky Lou").
- Hendon's **Fiat CR.42** is recorded as **BT474** (the RAF serial applied after its 1940 forced
  landing) with the Italian **MM5701** as an alias.
- Hendon's **Hudson** recorded as **A16-199** (the RAAF identity it wore in service and the one
  displayed) with the RAF contract serial **FH174** as an alias.
- Hendon's **B-17G** is **44-83868**; the museum's own page carries no serial.
- Hendon's **Harrier GR.9** is **ZG477** and the **Typhoon** is **ZH588** (DA2); again the museum's
  own pages carry no serials.

**Hangar 1 at Cosford is closed until summer 2027.** This is the single biggest fact about the
Midlands site right now and no third-party list reflects it properly. Everything the museum's web
pages place in Midlands Hangar 1 is therefore recorded `in_storage` unless demobbed confirmed it
somewhere visible in August 2026. That covers the Comper Swift, Hawker Cygnet, Flying Flea,
the prone-pilot Meteor WK935, the Fairchild Argus, the Devon, and the whole German guided-weapons
collection (BV 246, Hs 293, Enzian, Feuerlilie, X-4, Taifun) plus Fireflash, Red Dean and the
Fairey STV. Miles Magister T9708 is the exception — demobbed had it indoors in August 2026, so it
is recorded on display.

---

## Judgment calls

- **Replica and reproduction status is stated in `description`, never in `aliases`.** Recorded
  plainly as replicas/reproductions: Albatros D.Va (New Zealand-built, wears the false German
  identity D.7343/17), Vickers F.B.5 Gunbus 2345 (built 1966 for *Those Magnificent Men*),
  R.A.F. F.E.2b A6526 (new-build completed 2009), Bristol M.1c C4994 and Sopwith 1½ Strutter
  A8226 at Cosford. Hedged rather than asserted: R.A.F. B.E.2b 687 and R.E.8 'A3930', where the
  museum treats them as originals and other lists call them reproductions — the description says
  so. The Sopwith Snipe is described as a composite reconstruction; the Sopwith Dolphin as a
  composite incorporating D5329.
- **The Lockheed F-35 in Hendon Hangar 1 is a full-scale mock-up (BAPC.341), not an airframe.**
  Included, because a visitor sees it and asks about it, with the mock-up status stated first in
  the description and no serial invented.
- **Cockpit and nose sections are included as their own rows**, with "nose section only" or
  "forward fuselage only" leading the description: Victor K.2 XM717, CH-47D 83-24104 and
  WC-130E 64-0553 at Hendon; Hunter F.4 XE670, Buccaneer S.1 XN962 (wears the false XN972),
  Phantom FG.1 XV591, Dakota III KG437 and Jet Provost T.3A XM463 (fuselage) at Cosford.
  Salvaged remains recorded the same way: Gladiator II N5628 (forward fuselage), Southampton
  N9899 (hull), Halifax W1048 (recovered wreck, conserved as found), Stirling LK488 (sections),
  Hampden P1344, Wallace K6035, Defiant N3378 (wreckage), Brigand RH746 (fuselage).
- **The Michael Beetham Conservation Centre is not a gallery.** The museum's own words: "with it
  being an engineering environment it is rarely open to visitors, but we do have an annual Open
  Week." Everything there is `in_storage` or `under_restoration`, never `on_display`. Contents
  recorded: SR.53 XD145, Hunting H.126 XN714, Wessex HC.2 XR525, Gazelle XW855, Bulldog XX654,
  Harrier GR.3 XZ997, Chinook HC.4 ZA718 *Bravo November*, the Dornier Do 17Z-2 (wing shown
  inside the centre, fuselage in store) and the LVG C.VI.
  **The Vickers Wellington MF628 is the exception and is `on_display`** — it left the MBCC,
  was reassembled in 2023 and is now the centrepiece of the *Strike Hard, Strike Sure* Bomber
  Command exhibition in the War in the Air hangar. Any list that still shows it "under
  restoration" is out of date.
- **The 2025 disposals programme** (Varsity WL679, Jet Provost T.1 XD674, Fairchild Argus,
  Devon VP952, Swordfish HS503, Valetta VX573, Pucará A-515, Ventura AJ469, Sea Balliol WL732)
  is recorded as fact in the descriptions but the airframes are still recorded at Cosford,
  because demobbed and the museum still place them there. They will need re-checking.
- **`access_type` for Midlands is `public`** — ticketed but walk-up, on RAF Cosford's public
  museum side with its own entrance and car park. The MBCC and reserve store rows sit inside the
  same site record with a non-display `display_status` rather than a separate appointment site,
  which is what the schema is for.
- **Latitude/longitude left blank** for the Midlands site. Postcode **TF11 8UP** is published and
  geocodes precisely; a guessed pin would be worse.
- **New 2026 arrivals** (Hawk T.1A XX294, Reaper ZZ202, Puma HC.1 XW210) are recorded `in_storage`.
  They appeared publicly at the Cosford Air Show in June 2026 and then went into store pending the
  "The RAF: 1980 to Today" exhibition in the rebuilt Hangar 1 — a visitor cannot see them today.

## Excluded, and why — named

- **Aero engines.** Both sites hold large engine collections (the Midlands collection pages alone
  carry 26 individual engine objects in Hangar 1, and Wikipedia lists ~45 more at each site).
  Not airframes, missiles or rockets. Excluded wholesale.
- **Vehicles.** Alvis Saladin, Alvis Scorpion, Centurion, Leopard 1, BMP-1, Tracked Rapier
  carrier, Hägglunds Bv 202, Bedford "Green Goddess", Land Rover, BMC Mini, Trabant, VW Beetle,
  Morris Minor, Daimler Ferret, Remotec Wheelbarrow, David Brown / Lister / Douglas Mercury
  aircraft tractors, Crossley PTN, Corgi folding motorcycle. All excluded.
- **Marine craft at Hendon** — Pinnace 63ft Mk.1 1374, RTTL 2757, Seaplane Tender ST 206
  (two collection entries for the same boat). Real RAF vessels and on display outdoors, but boats.
- **Hucks starter, Martin-Baker Mk 2 ejection seat, uniforms, paintings, medals** and the rest of
  the small-object entries that share the collections feed.
- **"Douglas Dakota C47 (Parts only)"** in the Aeronauts Interactive Centre at Hendon — loose
  components used as a hands-on exhibit, not an airframe or a defined section.
- **Handley Page Hereford L6012** (damaged rear fuselage, said to be at Hendon). Only source is
  a Wikipedia row already tagged "citation needed"; not in the museum's collections feed, not in
  demobbed. Left out rather than asserted.
- **Hawker "Afghan" Hind** — listed on Wikipedia's Midlands Test Flight table with no serial and
  found nowhere else. Left out.
- **Avro Anson C.19 TX214** and **Comet 1XB G-APAS** — departed, see above.
- **Junkers Ju 52/3m (CASA 352L)** — deaccessioned from the Midlands collection.
- **RAF Cosford DCTT** (Defence College of Technical Training) holds a separate batch of
  instructional airframes on the *station* side of Cosford, behind the wire. It is a different
  site from the museum and is not in these files — see leads.

## Blank fields left deliberately

- `year_built` is blank on every row. Neither the museum's object pages nor demobbed give a
  sourced build or first-flight date per airframe, and the brief forbids inventing one.
- `latitude` / `longitude` blank on the museum row (postcode supplied instead).
- `tail_number` blank on 8 London rows and 31 Midlands rows. London: the F-35 mock-up, Kawasaki
  Ki-100, Mitsubishi Ki-46, Yokosuka Ohka, P-51D, R.E.8 and Sopwith Snipe (the museum publishes
  only a quoted display marking, which is in `aliases`). Midlands: 26 of the 31 are missiles and
  rockets, which carry no individual identity, plus the Dornier Do 17 and LVG C.VI (works numbers
  only, put in `aliases`) and the three V-weapons.
- `model_name` and `aircraft_name` blank throughout — the popular names are already the model or
  are carried in `aliases`.

## Ranked "needs a human on site"

1. **What exactly is the DB's existing "Messerschmitt Bf 109 G" at Royal Air Force Museum
   London?** Hendon's Bf 109 is an **E-3 (DG200 / Wnr 4101)**, which I have added to the London
   top-up as a distinct airframe. The only Bf 109G the RAF Museum owns is **Black 6, RN228 /
   Wnr 10639, at Cosford**, which is in the Midlands file. **If the existing DB row carries the
   serial RN228 or 10639 it will collide with the Midlands import and should be deleted or
   re-pointed at Midlands before loading.** Check this first.
2. **Gazelle XW855 — Hendon or the Cosford Beetham Centre?** demobbed says Beetham Centre
   (Aug 2026); the museum's own page and Wikipedia both say Hendon Historic Hangars. I put it at
   Midlands, `in_storage`. One walk through Hendon Hangars 3–4 settles it.
3. **Which Sycamore is at Hendon — WV783 (HR.12) or XJ918 (HR.14)?** And is XJ918 at the Ulster
   Aviation Society? The placard will say.
4. **Which Chipmunk is where?** WP912 (Duke of Edinburgh's) is recorded at Hendon Hangar 5 and
   WP962 at Hendon Historic Hangars; a Chipmunk also appears on the Midlands 2025 disposals list
   without a serial. It is possible WP962 is actually at Cosford in store.
5. **Cosford outdoor line-up.** Neptune 204 was "scheduled for disposal" and the Catalina L-866
   is deteriorating outdoors. Confirm both are still on the site, and confirm Canberra WH725,
   Varsity WL679, Jet Provost XD674/XM351/XM463, Hunter FR.10 XF426 and Jetstream XX496, none of
   which appear on the museum's current collection web pages but all of which demobbed saw
   outside in August 2026.

Lower priority: whether the Fieseler Storch VP746 is still on display in War in the Air or has
gone; whether the Stirling LK488 sections are split between the two sites (Wikipedia lists
sections at both — I recorded them only at Hendon, `in_storage`); and whether Spitfire F.24
PK724 and Sopwith Snipe 'E6655' have returned to the Hendon floor since the museum flagged them
off display.

## Leads for other agents

- **RAF Cosford DCTT** (Defence College of Technical Training), Shropshire — a separate demobbed
  location (id 8455) on the military side of RAF Cosford, holding instructional airframes.
  `access_type` would be `restricted`. Not covered here.
- **Avro Heritage Museum, Woodford, Cheshire** — now has **Avro Anson C.19 TX214** ex-RAF Museum.
- **South Wales Aviation Museum, St Athan** — now has **de Havilland Comet 1XB G-APAS / XM823**
  ex-RAF Museum Cosford, transferred September 2025.
- **Ulster Aviation Society, Long Kesh** — reportedly holds **Bristol Sycamore HR.14 XJ918** on
  loan from the RAF Museum.
- **Fleet Air Arm Museum, Yeovilton** — a transfer of **Boulton Paul Sea Balliol T.21 WL732**
  from the Cosford store has been proposed; check before recording it at Cosford long-term.
- **Aerospace Bristol, Filton** — a transfer of **Bristol 188 XF926** has been proposed.
- Other airframes offered in the RAF Museum's March 2025 disposals round and likely to surface at
  new UK sites over 2025–27: Vickers Varsity WL679, Vickers Valetta VX573, Lockheed Ventura
  AJ469, FMA IA-58 Pucará A-515/ZD485, Fairey Swordfish IV HS503, de Havilland Devon C.2 VP952,
  Fairchild Argus G-AIZE, Jet Provost T.1 XD674, a de Havilland Chipmunk. Any agent finding one
  of these at a new site should take it and flag the conflict.
- **Battle of Britain Memorial Flight, RAF Coningsby** and the RAF Museum's travelling Spitfire
  PR.XIX **PM651** — PM651 is often away from Cosford as a travelling exhibit; if another agent
  finds it displayed somewhere, that beats the Cosford `in_storage` row here.
- Both RAF Museum sites hold large **aero engine** and **military vehicle** collections that are
  out of scope for this database as currently specified, but are substantial if the scope ever
  widens.


---

# Research pass: Naval aviation, Science Museum and IWM

# UK naval aviation preservation — research notes

Assignment area: UK naval aviation (Fleet Air Arm Museum, RNAS Yeovilton and
Culdrose, Royal Navy Historic Flight / Navy Wings, other Royal Navy sites),
plus the Science Museum London, IWM London and IWM North.

Output directory: `/home/claude/uk/navy/`

---

## 1. Sources and how much weight each carried

| Source | Weight | Comment |
|---|---|---|
| **demobbed.org.uk (Wolverhampton Aviation Group)** | **Spine.** Used for every serial and for hall/store placement. | Per-location tables with a *last-confirmed date* per airframe. Yeovilton Museum list dated Oct 2023, Museum Store Mar 2022 (one item Jul 2025), RNAS Yeovilton Jul 2024–Jul 2026, RNAS Culdrose **Mar 2026**, Gosport Jul 2025, IWM Lambeth May 2025. The dated column is what makes this usable as a currency check. |
| **Museum's own pages (royalnavymuseums.org.uk / nmrn.org.uk, sciencemuseum.org.uk, iwm.org.uk)** | Authoritative on "what is here now", access and tour arrangements. | Confirmed the FAAM is now branded *Royal Navy Museums: Naval Aviation*, "more than 90 aircraft", four halls plus the Aircraft Carrier Experience; confirmed the Science Museum Flight gallery is open daily; confirmed the IWM object record for Harrier ZD461. |
| **Wikipedia (Royal Navy Museum, Naval Aviation)** | Leads only — used for replicas and civil airframes demobbed does not cover. | Its per-hall tables are the 2023 refresh and are broadly right. **Its "Reserve Collection" list is stale**: it is sourced to Ellis, *Wrecks & Relics* 24th ed. (2014) and still lists WW138, WV856, XA466, XD317, XV333, XZ699 and XS508 as reserve aircraft when demobbed places all seven in the halls. It also mis-attributes the HP.115 to serial XP980 (that is the P.1127; the HP.115 is XP841). demobbed won every one of these conflicts. |
| **Navy Wings (navywings.org.uk)** | Used for ownership and airworthiness, **not** for location. | Its "our aircraft" page implies everything is at Yeovilton. Cross-checking against demobbed shows Seafire XVII SX336 is at Old Warden under restoration, and Wessex XT761, Sea King ZA314 and Gazelle XX436 are not on the Yeovilton list. Only aircraft demobbed places at Yeovilton were recorded. |
| Forces News, airportspotting.com, Science Museum Group pages | Access questions (Culdrose Hawk gate guardian; Wroughton). | |

---

## 2. Sites recorded (12)

| Site | Aircraft | Access | Note |
|---|---|---|---|
| Fleet Air Arm Museum, Yeovilton | 97 | public | 49 on display in Halls 1–4 + restoration exhibit; 48 in the Cobham Hall reserve store |
| RNAS Yeovilton Gate Guardians | 3 | public | Sea Harrier ZD578, Lynx XZ670, Lynx XZ728 |
| Navy Wings Collection, RNAS Yeovilton | 14 | restricted | ex-Royal Navy Historic Flight + resident private warbirds |
| RNAS Yeovilton Station Heritage Aircraft | 3 | restricted | inside the wire |
| RNAS Culdrose Gate Guardians | 2 | public | Sea Hawk WF225, Hawk T.1A XX280 |
| RNAS Culdrose Station Heritage Aircraft | 1 | restricted | Sea King HU.5 XV673 in 771 NAS SAR colours |
| National Museum of the Royal Navy, Portsmouth | 1 | public | Sea Harrier F/A.2 ZD611, outdoors |
| Explosion Museum of Naval Firepower | 3 | public | missiles only, no aircraft |
| HMS Sultan Gate Guardian, Gosport | 1 | public | Lynx HMA.8 XZ692 |
| Science Museum, London | 31 | public | Flight gallery + Making the Modern World + Exploring Space |
| Imperial War Museum London | 7 | public | atrium |
| Imperial War Museum North | 1 | public | USMC AV-8A Harrier |

**Totals: 12 sites, 164 aircraft rows, 146 with a tail number (89.0% serial coverage).**

Per-file counts:

| File | Rows | With tail |
|---|---|---|
| `fleet_air_arm_museum_yeovilton_aircraft.csv` | 97 | 93 |
| `science_museum_london_aircraft.csv` | 31 | 23 |
| `navy_wings_collection_rnas_yeovilton_aircraft.csv` | 14 | 14 |
| `imperial_war_museum_london_aircraft.csv` | 7 | 5 |
| `rnas_yeovilton_gate_guardians_aircraft.csv` | 3 | 3 |
| `rnas_yeovilton_station_heritage_aircraft_aircraft.csv` | 3 | 3 |
| `explosion_museum_of_naval_firepower_aircraft.csv` | 3 | 0 |
| `rnas_culdrose_gate_guardians_aircraft.csv` | 2 | 2 |
| `rnas_culdrose_station_heritage_aircraft_aircraft.csv` | 1 | 1 |
| `national_museum_of_the_royal_navy_portsmouth_aircraft.csv` | 1 | 1 |
| `hms_sultan_gate_guardian_gosport_aircraft.csv` | 1 | 1 |
| `imperial_war_museum_north_aircraft.csv` | 1 | 0 |

---

## 3. Fleet Air Arm Museum — display vs. reserve

The museum's own material and the halls list give **49 airframes on public view** in
Halls 1–4 (including the Barracuda rebuild exhibit), and demobbed's separate
"Yeovilton – Museum Store" location gives **40 stored airframes**; eight further
reserve items appear only in published reference lists (Argentine Falklands
captures, four First World War replicas, a Bensen autogyro and a hang glider),
giving 48 reserve rows.

**Cobham Hall is recorded as `in_storage`, not `on_display`.** Access is real but
narrow: the NMRN's "Collections Uncovered" store tours explicitly *exclude the
aircraft reserve aero hall*, and the only route to the airframes is the private
guided tour — £50 per person plus a £100 Cobham Hall surcharge, maximum 4 people,
two weeks' notice. Every reserve row's description says so. A visitor who buys a
normal ticket cannot see these aircraft, so `in_storage` is the visitor's view.

### Hall/store conflicts resolved
- **WV856, WW138, XA466, XD317, XV333, XZ699, XS508** — Wikipedia (Ellis 2014)
  says reserve; demobbed (Mar 2022) says Halls 1/3. Recorded `on_display`. These
  moved into the halls for the 2023 refresh and the Aircraft Carrier Experience.
- **XL580 Hunter T.8M** — the reverse: an old Wikipedia photograph caption puts it
  in Hall 4, demobbed (Mar 2022) puts it in the store. Recorded `in_storage` with
  the doubt stated in the description. **Worth a human check.**
- **WT983 / "WT121"** — Wikipedia lists two Skyraiders, WV106 *and* WT121. There is
  one airframe: WT983, which wears the false serial WT121. Recorded once, as
  WT983, with `WT121` as an alias. WV106 is a genuine second Skyraider.
- **N4172 Albacore** wears `N4389`; **HS618 Swordfish** wears `P4139`;
  **N2078 Sopwith Baby** is a composite of 8214 and 8215. True identity in
  `tail_number`, worn marking in `aliases`, story in `description`.
- **XZ493 Sea Harrier FRS.1** is a composite incorporating the fuselage of XV760.
  Recorded once, as XZ493, with XV760 as an alias.
- **XP841 vs XP980** — Wikipedia's reserve list calls the HP.115 "XP980". XP980 is
  the Hawker P.1127; XP841 is the HP.115. Both are in Hall 4; recorded correctly.

### Replicas and non-airframes at the FAAM
Short S.27, Sopwith Pup N6452, Bristol Scout D N5419 (a reproduction shown without
fabric), Fairey Flycatcher S1287, Sopwith Camel B6401 and Sopwith Triplane N5459
are replicas/reproductions. Each says so plainly in `description`; per the brief
`replica` is never an alias. The Short 184 (8359) and Sea Vampire T.22 XA127 are
fuselage/pod sections; Sea Hawk WF219 is a tail section; Skua L2940 is a recovered
wreck displayed as recovered; Barracuda DP872 is an incomplete rebuild on public
view. All stated in `description`.

---

## 4. Judgment calls

- **DP872 Barracuda recorded `on_display`, not `under_restoration`.** It is the
  museum's "Barracuda Live – The Big Rebuild" exhibit: the visitor can see it, and
  `display_status` is the visitor's view. The description makes the state clear.
  The Sea Gladiator N5518 frame, by contrast, is in the store and is `in_storage`.
- **Royal Navy Historic Flight has no separate record.** The RNHF stood down on
  31 March 2019 and its aircraft passed to the Navy Wings charity (Fly Navy
  Heritage Trust). Recording an RNHF site as well as Navy Wings would put the same
  airframes in two places. One site, `Navy Wings Collection, RNAS Yeovilton`, with
  the history in the descriptions.
- **Navy Wings site is `restricted`, not `appointment`.** The hangar is inside a
  working naval air station; the reliable public sighting is the Yeovilton Air Day
  and the display circuit, not a bookable visit.
- **Airworthy aircraft recorded `on_display`** per the brief; NF389 (Swordfish III),
  VR930 (Sea Fury) and WB657 (Chipmunk) are long-term rebuilds and are recorded
  `under_restoration`.
- **Gate guardians split from station airframes.** At both Yeovilton and Culdrose,
  aircraft at the gate that a member of the public can see from the road are a
  separate `public` site from the airframes inside the wire, which are
  `restricted`. Bundling them would have made a `public` site that mostly isn't.
- **Explosion Museum recorded on missiles alone.** It holds no aircraft. Its
  Exocet, Sea Dart and Sea Wolf are inert display rounds and are in scope under the
  brief's "missile or rocket" rule. No individual identities are published, so all
  three rows have a blank `tail_number` and are distinguished by type and text.
- **Science Museum**: the Thrust Measuring Rig XJ314 and the Soyuz TMA-19M descent
  module are not conventional aircraft but are real flown hardware and are recorded
  (as `fixed_wing`/`experimental` and `spacecraft`/`space` respectively). Apollo 10
  CM-106 likewise.
- **Model / variant split** follows British practice per the brief: `Sea Harrier` +
  `F/A.2`, `Phantom` + `FG.1`, `Wessex` + `HU.5`, `Sea King` + `HAS.6`,
  `Hunter` + `T.8M`. US-built types keep the US pattern: `F6F` + `-5`,
  `TBM` + `-3E`, `AD` + `-4W`, `T-34` + `C-1`, `UH-1` + `H`, `C-47` + `B`.

---

## 5. Excluded, and why — every one named

| Excluded | Reason |
|---|---|
| **Imperial War Museum Duxford** | Assigned to another agent. Not touched. |
| **Churchill War Rooms, London** | Holds no aircraft, airframe section, missile or rocket. Explicitly checked; excluded. |
| **Predannack Airfield, Cornwall** | RN School of Flight Deck Operations / fire-school hulks on an active MoD satellite airfield of RNAS Culdrose. **No public access whatever** — no gate display, no open days, no visitor route; the only published accounts are urban-exploration trespass reports. demobbed does not even carry Predannack as a Cornwall location. Excluded outright: the airframes there cannot be seen by a visitor. |
| **Science Museum National Collections Centre, Wroughton** | **Established as not visitable for aircraft in 2025-26.** Public tours of the Hawking Building began in late 2024 (limited to ~50 people a day, three days a month, minimum two tickets) but they **exclude the large aircraft collection** in the wartime hangars. Access to the airliners still requires prior permission with a research justification. Under the brief's rule on "aircraft merely stored... with no public access", excluded as a site. Contents for the record: Lockheed L-749 Constellation, HS.121 Trident 3B, Comet 4B, Douglas DC-3, Boeing 247D, DH Dragon Rapide, plus DH.89 Dominie NF865 (G-ALXT), DH Devon C.2 VP975 and Folland Gnat T.1 XP505. **Re-check if the Science Museum Group opens the hangars.** |
| **HMS Gannet, Prestwick** | No preserved airframe or gate guardian found. The SAR Flight closed in 2016 and the site is now a forward operating base. The four airframes demobbed lists at Prestwick (Chipmunks WB682, WD297, WP808 and Bulldog XX612) are privately owned, stored or storm-damaged and unconnected to HMS Gannet; two are in a container or dumped. No site record. |
| **RNAS Merryfield** | The single airframe there, Lynx HMA.8SRU XZ719 (marked 'ZZ511'), is recorded by demobbed as **Dumped** (Aug 2025) on an active Yeovilton satellite airfield with no public access. Excluded. |
| **RNAS Yeovilton dumped and ground-instructional airframes** | WV911 (Sea Hawk FGA.4), XS513 and XW630 (Wessex HU.5 / Harrier GR.3), XZ674 (Lynx AH.7) — all "Dumped"; XZ230, XZ257 (cabin only), XZ736, ZZ400, ZZ401 — ground-instructional or weapons-load training. None is displayed; all inside the wire. Excluded. |
| **HMS Sultan, Gosport — the other 53 airframes** | demobbed lists 54 at Gosport. All but the gate guardian are Royal Navy Air Engineering and Survival School / DSAE ground-training airframes and withdrawn stored helicopters in the Cockerell, Newcomen, Whittle and Stephenson hangars or outside on the park — Sea Kings (some 25 of them), Merlin HM.1s, Lynx, Wildcat ZZ402, Tornado GR.1 ZA323, Gazelle XX431 and XX930, EH-101 ZF649. It is a training establishment, not a museum, with no public access. Only gate guardian XZ692 recorded. Gazelle HT.3 XZ930 is "preserved, outside" but inside the wire — excluded for the same reason. |
| **RNAS Culdrose SFDO airframes** | XV696 and ZD634 (Sea King HAS.6), XX510 and XZ248 (Lynx), ZF641 (EH-101) are School of Flight Deck Operations deck-handling trainers — working equipment on the airfield, not displayed. Excluded. |
| **Fairey Firefly TT.1 Z2033** | Listed in the FAAM reserve collection by Wikipedia (from Ellis 2014). demobbed places it **at Duxford**, "Museum, inside", marked 'N-275' *Evelyn Tentions*, last confirmed **Dec 2024**. It is Duxford's to record, not the FAAM's. Excluded here — flagged to the Duxford agent below. |
| **Seafire XVII SX336** | Listed by Navy Wings as core collection, but demobbed places it **at Old Warden (Shuttleworth), under restoration in the hangar, Mar 2026**. Not at Yeovilton. Excluded here. |
| **Navy Wings "associate collection" aircraft** | Wessex HU.5 XT761, Sea King HC.4 ZA314, Gazelle HT.2 XX436, Swordfish HS554, Tiger Moth G-BWMK, Bristol Scout 1264, Avro 504K, Waterbird, Skyraider, AT-6D, Harvard G-NWHF — privately owned and not on the demobbed Yeovilton list. An aircraft is in exactly one place; recording them at Yeovilton on the strength of an ownership page would be a misattribution. Excluded pending a location for each. |
| **Explosion Museum aircraft** | None — no airframe. Only missiles recorded. |
| **Fleetlands (Gosport), Lee-on-Solent Museum** | Outside this assignment. Fleetlands is a DE&S maintenance site; the Lee-on-Solent Museum entry is the Hovercraft Museum (hovercraft, not aircraft). Passed on as leads. |

---

## 6. Blank fields left deliberately

- **All latitude/longitude blank.** Postcodes are supplied for all 12 sites and
  geocode precisely; the brief prefers a correct postcode to a guessed pin.
- **Serials left blank (18 rows), each because no source publishes one:** FAAM
  Short S.27 replica, Fa 330, MXY-7 Ohka (BAPC 58 is in aliases, not a serial),
  MiG-15; Science Museum Vickers Vimy (demobbed records it as "Unconfirmed,
  possibly F8608" — not good enough to record), Antoinette VII, Roe Triplane,
  Wright Flyer replica, V-1, V-2, Black Arrow R4, Soyuz TMA-19M; IWM London V-1 and
  V-2; IWM North's USMC AV-8A **Bureau Number is not published by IWM and is not
  recorded** — a blank beats a guess.
- `year_built` blank throughout: no build/first-flight dates were sourced to the
  standard the brief requires.
- `aircraft_name` used only where the airframe genuinely carries a name
  (Humphrey, Gilbert, The Jabberwock, Old Fred, Jason, Charlie Brown, City of
  Leeds, Foxy Lady, Flying Bedstead).

---

## 7. Needs a human on site — ranked

1. **Hunter T.8M XL580** — Hall 4 or Cobham Hall? Recorded `in_storage`; sources
   disagree and the museum's Hall 4 photography shows it inside.
2. **Cobham Hall inventory currency.** 34 of the 48 reserve rows were last
   confirmed in **March 2022**, and three (Shelduck XS574, Chukar XW994, Sea Hawk
   tail WF219) not since 2010–2013. The eight Wikipedia-only items (Turbo Mentor
   0729, UH-1H AE-422, Flycatcher S1287, Camel B6401, Triplane N5459, Bensen
   G-AZAZ, Super Eagle G-BGWZ, plus the store's Skyraiders) rest on a 2014
   reference. A single guided tour would re-verify the whole store.
3. **The FAAM's own count.** The museum advertises "more than 90 aircraft"; this
   file has 97 rows. That is close, but the museum may count sections and replicas
   differently. A published current inventory from the museum would settle it.
4. **IWM North's Harrier Bureau Number.** One placard photograph would fill the
   only completely unidentified airframe in this set.
5. **Culdrose Hawk T.1A XX280** — confirmed "preserved, outside" and reported as a
   new gate guardian. Is it actually at the main gate (public view) or on the
   station side? It is currently in the `public` gate-guardian site.
6. **Explosion Museum missiles** — are the Exocet, Sea Dart and Sea Wolf real inert
   rounds or sectioned/mock-up displays? Recorded as inert display rounds.
7. **FAAM postcode** — BA22 8HT is used (widely published, including on rated-visit
   listings). The NMRN's own visit page currently gives BA22 8HW. Both are within
   the Yeovilton village postcode area; BA22 8HT geocodes to the museum.

---

## 8. Leads for other agents

- **Imperial War Museum Duxford top-up:** Fairey Firefly TT.1 **Z2033**, marked
  'N-275' *Evelyn Tentions*, is at Duxford (demobbed, Dec 2024) — owned by the FAAM
  but displayed at Duxford. Also Firefly I **DT989** (G-CGYD) under restoration
  there, Apr 2026.
- **Shuttleworth / Old Warden:** Seafire XVII **SX336** (VL-105, G-KASX) under
  restoration in the hangar, Mar 2026; also Seafire F.46 LA564, Seafire XV SR462,
  Seafire XVII SX300, Spitfire F.22 PK664, Spitfire LF.Vc AR501.
- **HMS Sultan / Gosport (whoever takes Hampshire):** 54 airframes at Gosport, the
  largest single concentration of stored Sea Kings and Merlins in the UK. Not
  visitable, but worth documenting as an exclusion in that region's notes too.
  Also in Hampshire: **Farnborough Museum** (14), **Lee-on-Solent Solent Airport**
  (12 + 10 Britten-Norman), **Middle Wallop Museum** (28) and **AAC Middle Wallop**
  (22), **Fleetlands** (4), **Southampton Museum / Solent Sky** (14),
  **Lasham** (13), **Portsmouth Dockyard** (Sea Harrier ZD611 — recorded here).
- **Somerset (non-naval):** Weston-super-Mare (37 — The Helicopter Museum, an
  existing DB stub badly under-recorded at 1 aircraft), Somerton (11), Henstridge
  (10), Middlezoy (8), Chard – Higher Purtington Showfield (7), Babcary (4),
  Yeovil Airfield (5), Bridgwater area (4).
- **Cornwall:** Cornwall Aviation Heritage Centre, Newquay (5); Davidstow Airfield
  (7); Newquay Airport (3).
- **Wiltshire:** Old Sarum Museum (44 — Boscombe Down Aviation Collection),
  MoD Lyneham (30), MoD Boscombe Down (27), AAC Netheravon (8), Oaksey Park (7),
  and Wroughton (3 recorded by demobbed, plus the airliner collection) — see the
  exclusion above.
- **London (beyond this assignment):** Hendon (58 — RAF Museum London, an existing
  DB stub recorded at 2 aircraft; a very large gap), Biggin Hill (13) and The
  Spitfire Company Biggin Hill (16), RAF Northolt (4), National Army Museum (1),
  Battersea Park (1), Upminster – Damyns Hall (2).
- **Scotland:** Morayvia at Kinloss (35), East Fortune (23 — National Museum of
  Flight, an existing DB stub at 1 aircraft), Dumfries (22), Montrose (9),
  Stoneykirk (9), Prestwick (4), RAF Lossiemouth (5), Leuchars (2).
- **Method note for everyone:** `demobbed.org.uk/locations.php?country=20&county_state=<id>`
  gives a per-county location index with airframe counts, and
  `locations.php?location=<id>` gives a per-site table of serial, type, markings,
  status and a **last-confirmed month**. County ids: Somerset 43, Cornwall 9,
  Hampshire 20, Wiltshire 58, London 29, Scotland 41, Wales 53, Northern Ireland 31.
  This is the fastest route into any UK assignment.


---

# Research pass: East Anglia museums and Duxford

# UK East Anglia — research notes

Assignment: IWM Duxford top-up plus every other museum and preserved airframe in
Cambridgeshire, Norfolk, Suffolk, Essex, Bedfordshire and Hertfordshire.
Output directory `/home/claude/uk/east/`.

## Sources and how much weight each carried

| Source | Weight | What happened |
|---|---|---|
| **eurodemobbed.org.uk** (`locations.php?location=…`) | **Spine.** Nearly every serial and every currency judgement below comes from it. | Its UK location pages carry a *dated sighting* per airframe, many as recent as **August/September 2026**. I walked all 160 location pages for the six counties programmatically and used the date column as the presence test. |
| **demobbed.org.uk** | **Dead.** | The domain now returns an IONOS/Sedo parking page. The brief names it as "the single best UK survivors database"; it is no longer reachable. `eurodemobbed.org.uk` is the live sister site and carries the same data — **future agents should be told to use eurodemobbed, not demobbed**. |
| Museums' own collection pages | Won on "what is here now" where consulted (ARCo, The Fighter Collection, Suffolk Aviation Heritage, Bentwaters). | Used to add civil-registered warbirds that eurodemobbed (a *military* survivors database) does not list. |
| Wikipedia per-museum lists | Leads only. | Proved stale in three specific places, listed under Corrections. |
| thunder-and-lightnings.co.uk | Used for two disputed airframes (Hunter N-250, Hunter XG210). | Its dated visitor comments settled both. |

## The Duxford top-up

`duxford_topup_aircraft.csv` — 66 rows, museum_name `Imperial War Museum Duxford`,
none of which appear in `/home/claude/uk/duxford_live.txt` (114 lines).

The 115 already recorded are essentially the Wikipedia "List of aircraft at the
Imperial War Museum Duxford" — i.e. the IWM-owned static collection plus a slice
of the airworthy residents. The gap is almost entirely:

- **Resident operators' aircraft that Wikipedia omits** — The Fighter Collection
  (P-36A 38-210, FM-2 86711, FG-1D G-FGID, Sea Fury VX653, Beech D17S G-BRVE),
  Aircraft Restoration Company (Mustang 44-72035 *Tall in the Saddle*, Buchón
  C.4K-154, Spitfire T.9 BS548), Plane Sailing's Catalina G-PBYA.
- **The light/vintage tail** — nine Stearmans, Cubs, Chipmunks, Tiger Moths,
  Dragon Rapides, Yak-52s, Bü 131, MS.505 Storch, Nord 1002, Broussard, T-6J.
- **Restoration projects visible in the conservation hangars** — Fw 189 2100,
  Typhoon RB396, Walrus W2718, Firefly DT989, Lysander V9546, Spitfires PL258 /
  RK858 / SM845 / P3966, Sea Fury VX653.
- **Sections and small exhibits nobody lists** — Halifax VII nose PN323, Valiant
  B(K).1 nose XD826, Bolingbroke IVT nose 10201, A6M5 Zero cockpit,
  Fa 330 Bachstelze, Shelduck D.1 target drone XT581, MQ-1B Predator 03-33120.
- **Recent arrivals** — Sea Harrier FA.2 ZA175, Lynx AH.7 XZ194, Bf 110 D-0 3869,
  Kittyhawk AK803 (noted September 2026), Trident 2E G-AVFB.

Duxford is **not** in `uk_museums.csv`, per the brief.

## Corrections made, with evidence

1. **Sea Harrier FA.2 ZA175 is at Duxford, not Flixton.** Wikipedia's
   Norfolk and Suffolk Aviation Museum article still lists it. eurodemobbed has it
   at Duxford (museum, inside, June 2025) and it is absent from the Flixton page
   at April 2026. Recorded at Duxford; excluded from Flixton.
2. **Eurofighter Typhoon DA4 ZH590 has left Duxford.** The IWM Duxford Wikipedia
   article still lists it in AirSpace; the RAF's own news page records it going to
   RAF Cosford. Not recorded here — **lead for the West Midlands agent.**
3. **Meteor T.7 WL349 has left the Jet Age Museum (Gloucestershire).** ABPic and
   Aerial Visuals still place it there; eurodemobbed has it preserved outdoors at
   Thornwood near Epping, Essex, painted as WL462, October 2025. Recorded in Essex
   — **lead for the South West agent to remove it from Jet Age.**
4. **Blenheim L6739 / Bolingbroke 10201 are one airframe and two records.** The
   flying "Blenheim L6739" (G-BPIV) is Bolingbroke 10201's wings and fuselage with
   L6739's nose; 10201's own nose is displayed separately in Hangar 3 South. The
   existing DB row covers the flyer; the top-up adds the nose section only, and
   both descriptions say so.
5. **Hispano HA-1112 identity.** Long recorded as C.4K-102 (c/n 172); eurodemobbed
   carries an explicit correction to c/n 223, **C.4K-154**. Used the corrected
   identity, with C.4K-102 in aliases.
6. **Valiant XD857 and Victor XL160 at Norwich** came from the Fenland and West
   Norfolk Aviation Museum, which closed in 2022. Recorded at Norwich, where a
   visitor now finds them.
7. **Duxford's "Sea Fury SR661"** in the live list is the ex-Iraqi Hawker Fury
   G-CBEL *wearing* SR661. I did not add a second row for it; TFC's genuine Sea
   Fury FB.11 **VX653** is a separate airframe and is added.

## Judgment calls

- **Replicas** are recorded only where they are the exhibit a visitor sees, and the
  word "replica" is in `description`, never in `aliases`: Shuttleworth's Roe IV
  Triplane, Bristol Boxkite, Bristol M.1C, Hawker Cygnet, Sopwith Camel and
  Triplane, and the Me 163 fuselage mock-up; dHAM's DH.88 G-ACSR; Flixton's
  Felixstowe F5 nose (BAPC.390); Stow Maries' B.E.2e and S.E.5a; Muckleburgh's V-1.
- **Cockpit and nose sections** are full rows with the section stated plainly in
  `description` (37 such rows across the region). Duxford alone contributes four.
- **Airworthy residents are recorded.** The brief says so explicitly. Where an
  aircraft is privately owned but exhibited at the site between flights, the owner
  or operator is named in the description, not in aliases.
- **`tail_number` choice.** UK military serial where the airframe wears one
  (Spitfires, Hurricanes, Harvards, all gate guards); civil registration where the
  aircraft is known and displayed by it (Dragon Rapides G-AKIF/G-AIDL, Tiger Moths
  G-ANZZ/G-AGPK, Shuttleworth's whole collection, Yak-52s, Beech D17S, FG-1D). The
  other identity is always in `aliases`.
- **Maintenance serials** (7496M, 8092M, 9222M…) go in `aliases` and `description`,
  never in `tail_number`.
- **Access types.** `restricted` is used only for airframes inside a live military
  gate (Wittering Heritage Museum, Marham, Lakenheath, Merville Barracks).
  Gate guardians visible from a public road are `public`. Paintball sites are
  `public` because the public gets in by paying.
- **Two untailed rows of one type at one site** does not occur; the only untailed
  rows are single instances per site, each distinguished in `description`.

## Excluded, and why — named

**Sites with no airframe**
- **100th Bomb Group Memorial Museum, Thorpe Abbotts** — control tower, huts,
  artefacts and recovered parts, no complete airframe or section. No record.
- **Parham Airfield Museum (390th BG Memorial Air Museum / Museum of the British
  Resistance Organisation)** — engines and recovered aircraft parts only.
- **Rougham Tower Association, Bury St Edmunds** — control-tower museum; the only
  airframe eurodemobbed lists at Rougham is a privately owned L-18C on the strip.
- **Bassingbourn** — the Tower Museum's airfield holdings produced no preserved
  airframe in any county sweep; nothing recorded.
- **Bircham Newton, Metheringham** — Metheringham is Lincolnshire, not my area;
  Bircham Newton (Norfolk) returned no preserved airframe.

**Airframes not visitable**
- **Bentwaters Airfield stored aircraft** (Hunter XG196, Harrier T.4 XW267,
  Jaguars XX838/XX842, Sea Harriers ZH806/ZH812, JP XW418, Phantom nose XV460) —
  stored in hardened shelters on the industrial estate, not part of the museum and
  not viewable. The nine museum airframes *are* recorded.
- **Sproughton, Suffolk (18 airframes)** and **Stapleford Tawney, Essex
  (14 Gazelles)** — commercial storage/disposal yards with no public access.
- **Chippenham Lodge (Jaguar XX116, Tornado F.2 ZD899, Sea Harrier ZH811)** —
  a private estate near Newmarket. Airframes confirmed present May 2026 and
  visible in photographs, but I could not establish any public or by-appointment
  access. **Highest-value single exclusion; see open questions.**
- **Billericay, Essex (Meteor NF.14 WS726, Hunter T.7 XL586, C-54 fuselage)** —
  private ground, access not established.
- Dozens of privately owned airworthy light aircraft on farm strips
  (Audley End, Old Buckenham, Little Gransden, Earls Colne, Tibenham, Great
  Oakley, Crowfield, Norton, Monewden, Hardwick, Rayne Hall Farm, Langham,
  Felthorpe, Seething, Raveningham, Podington…). These are aeroplanes at
  airfields, not exhibited collections, and the brief excludes them.

**Airframes with stale or negative evidence**
- **Hunter F.6 nose N-250, Duxford** — eurodemobbed has it in Hangar 1 (Dec 2024),
  but thunder-and-lightnings records IWM **offering it for disposal in December
  2024**, with Newark Air Museum interested. Not recorded at Duxford. **Lead for
  the East Midlands agent: check Newark.**
- **Handley Page Dart Herald G-APWJ, Duxford** — displaced from the DAS apron by
  BAe 146 ZE701 in 2022 and not in any current listing. Not recorded.
- Duxford items last seen too long ago to stand behind: CASA 2.111 B.2I-37
  (Jan 2015), Spitfire EP122 (Oct 2021), Seafire MB293 (deregistered to the USA in
  2016), Spitfires RK912 / RM873 / RN203 / Seafire RX168 (2010–2018 or undated),
  Sea Fury T.20 WG655 (written off 2020), Aero L-39 (scrapped 2013),
  Lavochkin La-11 (2007), Harvard KF487 (spares, 2007), DH.89 HG691 (2022),
  DH.89 X7344 (2023), Leopard Moth G-ACMN (2022), Sea Fury T.20S VX281 (2021),
  P-51D 44-74391/NL351MX (2023), P-40B wrecks 39-0285/39-0287 (undated).
- **Avro Lancaster PA474** was at Duxford for maintenance in August 2026. It
  belongs to the Battle of Britain Memorial Flight at RAF Coningsby and is
  recorded there, not here. **Lead for the East Midlands agent.**
- **Ramsey ATC Chipmunk WK584** (Mar 2019) and **Houghton Canberra nose WJ567**
  (Jul 2019) — evidence too old; no record.
- **de Havilland Museum's Dove 6 D-IFSB** is on loan out to ARG Fishburn
  (Co. Durham). Not recorded here. **Lead for the North East agent.**

## Blank fields left deliberately

- `tail_number` blank on 11 of 311 rows: Duxford's A6M5 Zero cockpit and SPAD-type
  exhibits with no published airframe serial; Norwich's Scimitar cockpit module and
  its second Hunter nose (reported XE612, unconfirmed); West Raynham's composite
  Vampire painted WA123; the Bottisham Tiger Moth composite; the de Havilland
  Museum's unidentified Comet 2 nose; Muckleburgh's V-1 replica; Stow Maries'
  two WWI replicas; Flixton's Felixstowe F5 replica nose.
- `year_built` is blank except where Wikipedia's Shuttleworth table gives a sourced
  build year and for the dHAM/Duxford airliners where the delivery year is known.
  No serial has been used as a year.
- `latitude`/`longitude` blank only for RAF Wittering's gate guardian (position of
  the airframe not published; the postcode is correct). All other coordinates are
  eurodemobbed's published airframe positions.

## Needs a human on site — ranked

1. **Chippenham Lodge, Cambridgeshire.** Jaguar XX116, Tornado F.2 ZD899 and
   Sea Harrier ZH811, all restored and displayed outdoors as of May 2026. Is there
   any arranged access? If yes this is a three-airframe site currently missing.
2. **Hunter nose N-250** — did it leave Duxford for Newark after the December 2024
   disposal offer, or is it still in Hangar 1?
3. **Avro 504K H2311/G-ABAA at Stow Maries.** eurodemobbed puts it there
   (August 2025); the airframe is normally credited to the Science and Industry
   Museum, Manchester. One of the two is wrong.
4. **RAF Henlow Hunter WT612.** Last seen July 2023; the station has been
   progressively disposed of. Is the gate guardian still in place?
5. **Bentwaters stored fleet.** Eight airframes in hardened shelters. If the
   Cold War Museum has since taken any of them onto the tour, they become records.

## Files written

| File | Site | Rows | With serial |
|---|---|---|---|
| `abbots_ripton_paintball_jet_provost_aircraft.csv` | Abbots Ripton Paintball Jet Provost | 1 | 1 |
| `bentwaters_cold_war_museum_aircraft.csv` | Bentwaters Cold War Museum | 9 | 9 |
| `bottisham_airfield_museum_aircraft.csv` | Bottisham Airfield Museum | 1 | 0 |
| `boxted_airfield_museum_aircraft.csv` | Boxted Airfield Museum | 1 | 1 |
| `city_of_norwich_aviation_museum_aircraft.csv` | City of Norwich Aviation Museum | 31 | 29 |
| `cranfield_university_aircraft_collection_aircraft.csv` | Cranfield University Aircraft Collection | 6 | 6 |
| `de_havilland_aircraft_museum_aircraft.csv` | de Havilland Aircraft Museum | 35 | 34 |
| `duxford_topup_aircraft.csv` | Imperial War Museum Duxford | 66 | 65 |
| `east_essex_aviation_museum_aircraft.csv` | East Essex Aviation Museum | 1 | 1 |
| `gloster_meteor_t_7_thornwood_aircraft.csv` | Gloster Meteor T.7, Thornwood | 1 | 1 |
| `gnat_display_team_aircraft.csv` | Gnat Display Team | 3 | 3 |
| `halesworth_airfield_memorial_museum_aircraft.csv` | Halesworth Airfield Memorial Museum | 1 | 1 |
| `hangar_11_collection_aircraft.csv` | Hangar 11 Collection | 1 | 1 |
| `hawker_hunter_gate_guard_beck_row_aircraft.csv` | Hawker Hunter Gate Guard, Beck Row | 1 | 1 |
| `jaguar_gr_3a_monument_tattersett_aircraft.csv` | Jaguar GR.3A Monument, Tattersett | 1 | 1 |
| `marham_aviation_heritage_centre_aircraft.csv` | Marham Aviation Heritage Centre | 1 | 1 |
| `merville_barracks_dakota_gate_guardian_aircraft.csv` | Merville Barracks Dakota Gate Guardian | 1 | 1 |
| `muckleburgh_military_collection_aircraft.csv` | Muckleburgh Military Collection | 3 | 2 |
| `norfolk_and_suffolk_aviation_museum_aircraft.csv` | Norfolk and Suffolk Aviation Museum | 37 | 36 |
| `norwich_county_hall_jaguar_monument_aircraft.csv` | Norwich County Hall Jaguar Monument | 1 | 1 |
| `raf_air_defence_radar_museum_aircraft.csv` | RAF Air Defence Radar Museum | 3 | 3 |
| `raf_henlow_gate_guardian_aircraft.csv` | RAF Henlow Gate Guardian | 1 | 1 |
| `raf_honington_gate_guardian_aircraft.csv` | RAF Honington Gate Guardian | 1 | 1 |
| `raf_lakenheath_preserved_aircraft_aircraft.csv` | RAF Lakenheath Preserved Aircraft | 4 | 4 |
| `raf_marham_preserved_aircraft_aircraft.csv` | RAF Marham Preserved Aircraft | 3 | 3 |
| `raf_west_raynham_preserved_aircraft_aircraft.csv` | RAF West Raynham Preserved Aircraft | 4 | 3 |
| `raf_wittering_gate_guardian_aircraft.csv` | RAF Wittering Gate Guardian | 1 | 1 |
| `raf_wittering_heritage_museum_aircraft.csv` | RAF Wittering Heritage Museum | 6 | 6 |
| `raf_wyton_gate_guardian_aircraft.csv` | RAF Wyton Gate Guardian | 1 | 1 |
| `shuttleworth_collection_aircraft.csv` | Shuttleworth Collection | 58 | 57 |
| `spirit_of_coltishall_association_aircraft.csv` | Spirit of Coltishall Association | 4 | 4 |
| `stow_maries_great_war_aerodrome_aircraft.csv` | Stow Maries Great War Aerodrome | 5 | 3 |
| `suffolk_aviation_heritage_museum_aircraft.csv` | Suffolk Aviation Heritage Museum | 5 | 5 |
| `swaffham_air_cadets_auster_aircraft.csv` | Swaffham Air Cadets Auster | 1 | 1 |
| `thetford_paintball_whirlwind_aircraft.csv` | Thetford Paintball Whirlwind | 1 | 1 |
| `vulcan_restoration_trust_aircraft.csv` | Vulcan Restoration Trust | 1 | 1 |
| `wattisham_station_heritage_museum_aircraft.csv` | Wattisham Station Heritage Museum | 8 | 8 |
| `wickford_paintball_aircraft_aircraft.csv` | Wickford Paintball Aircraft | 2 | 2 |
| **Total** | **38 sites** | **311** | **300 (96.5%)** |

Plus `uk_museums.csv` — **37 sites** (Duxford deliberately absent; it is a top-up).

## Leads for other agents

- **West Midlands** — Eurofighter Typhoon DA4 **ZH590** moved from IWM Duxford to
  RAF Cosford; Duxford's Wikipedia article is stale on this.
- **East Midlands** — Lancaster **PA474** (BBMF, RAF Coningsby) was at Duxford for
  maintenance in Aug 2026; record it at Coningsby. Hunter F.6 nose **N-250** may
  have moved from Duxford to Newark Air Museum.
- **South West** — Meteor T.7 **WL349** has left the Jet Age Museum and is now at
  Thornwood, Epping, Essex, marked WL462.
- **North East** — de Havilland Aircraft Museum's Dove 6 **D-IFSB** is on loan to
  ARG Fishburn, Co. Durham; record it there.
- **North West** — Avro 504K **G-ABAA** may have moved from the Science and
  Industry Museum, Manchester, to Stow Maries; verify before recording it in
  Manchester.
- **Whoever writes the next UK brief** — `demobbed.org.uk` is a dead/parked
  domain. The live database is **`eurodemobbed.org.uk`**, whose
  `locations.php?country=20&county=<n>` index gives every UK county and whose
  location pages carry dated sightings. It is by far the most productive UK source
  and should replace demobbed in the brief.
- **Greater London / Hertfordshire border** — Elstree Studios holds a Devon C.2
  nose (XA880, 2015) and Sawbridgeworth a Mil Mi-24D (2020); both too stale to
  record but worth a check by anyone working London.


---

# Research pass: East Anglia gate guards and monuments

# East Anglia — gate guardians, station displays, ATC airframes, cockpit collections, monuments and oddities

Assignment: everything in Cambridgeshire, Norfolk, Suffolk, Essex, Bedfordshire and
Hertfordshire that is **not** a museum. Output directory `/home/claude/uk/east_gates/`.

## Method and sources

- **`eurodemobbed.org.uk` was the spine.** I walked the UK country index
  (`locations.php?country=20`) to recover the county numbers, then took the six
  county pages — Bedfordshire (2), Cambridgeshire (6), Essex (17), Hertfordshire (22),
  Norfolk (32), Suffolk (47) — and fetched **all 160 location pages** beneath them,
  parsing serial / type / code / status / last-noted date and the per-airframe history
  tooltip. That table is the currency evidence behind every row below; each
  description quotes the dated last sighting.
- **The museum agent's file was subtracted first.** I read
  `/home/claude/uk/east/uk_museums.csv` (37 sites) and all its per-site aircraft CSVs,
  plus `/home/claude/uk/midlands/uk_museums.csv` (RAF Wittering is recorded there and in
  the east file — I did not touch it). No site name and no tail number in my files
  collides with either. Checked programmatically.
- **Web verification** for the judgement calls that eurodemobbed cannot answer —
  can a visitor actually see it. thunder-and-lightnings.co.uk (Buccaneer survivors),
  501st CSW USAFE news release (Alconbury F-5E), rafsculthorpeheritagecentre.org,
  sim2do.com / Tripadvisor, quirkyaccom.com (Kessingland Lynx), hotfrog (Four Acre Farm).

Which source proved stale: eurodemobbed's *lists* are excellent but its *dates* vary
enormously — Wattisham and Chippenham Lodge carry 2026 sightings, while Bovingdon
(Jan 2018), Sim2do (Aug 2017) and Colchester ATC (Mar 2018) have not been re-reported in
years. I have recorded the ones where the airframe's role makes disappearance unlikely
(paintball props, a fitted-out simulator, a cadet unit's own airframe) and said in each
description exactly when it was last confirmed.

## Sites recorded — 15 sites, 26 airframes

| county | site | airframes |
|---|---|---|
| Cambs | 511 Squadron ATC Chipmunk, Ramsey | 1 |
| Cambs | Blue Bell Inn Lynx, Werrington | 1 |
| Cambs | High Harthay Outdoor Pursuits Aircraft Display | 1 |
| Cambs | Chippenham Lodge Aircraft Display | 3 |
| Herts | Delta Force Paintball Bovingdon Lynx | 1 |
| Essex | Mayhem Paintball Aircraft, Abridge | 6 |
| Essex | Four Acre Farm Aircraft Collection, Billericay | 4 |
| Essex | Jet Provost XM473, Wethersfield | 1 |
| Essex | 308 Squadron ATC Viking, Colchester | 1 |
| Essex | Dassault Mystere IVA, Andrewsfield | 1 |
| Suffolk | Rock Barracks Lynx Display, Woodbridge | 1 |
| Suffolk | Blenheim Camp Aircraft Display, Bury St Edmunds | 2 |
| Suffolk | Lynx Helicopter Glamping Pod, Kessingland | 1 |
| Suffolk | Sim2do Flight Simulators Lynx Nose, Mildenhall | 1 |
| Norfolk | RAF Sculthorpe Heritage Centre | 1 |

Serial coverage: **25 of 26 rows carry a tail number (96%)**. The one blank is the
Alconbury/Sculthorpe F-5E, which is a glass-fibre replica and has no airframe serial —
inventing one would be a fabrication.

Bedfordshire produced **no** recordable site: everything eurodemobbed lists there is
either already the museum agent's (Shuttleworth, Cranfield, RAF Henlow gate guard) or a
private farm strip / private garden. That is a finding, not a gap.

## Judgement calls

- **Replicas.** The only replica recorded is the ex-RAF Alconbury F-5E Tiger II, and the
  description says plainly it is full-size glass-fibre and not an airframe. It is
  recorded because the USAF's own 501st CSW release documents its removal on
  1 April 2026 and donation to RAF Sculthorpe Heritage Centre, which makes it the single
  best-evidenced new display in the region.
- **RAF Sculthorpe Heritage Centre is arguably a museum** and therefore arguably the east
  agent's. It is not in their file, it is inside my six counties, and it now holds a
  displayed airframe, so I have recorded it rather than leave it missing. If the
  coordinator prefers, move it wholesale — nothing else references it.
- **Cockpit and nose sections** are recorded as their own rows and said so in the
  description: Grob Viking ZE556 (nose, Colchester ATC), Lynx XZ195 (nose, Sim2do),
  Lynx XZ655 (cabin only, Blue Bell Inn), C-54 42-72525 (forward fuselage), Sea King
  Mk.47 776 (nose mated to ZA136's fuselage).
- **Two Sea Kings at one site.** ZA136 (ex-RN, complete) and 776 (ex-Egyptian, composite
  built on ZA136's fuselage) are at Mayhem, Abridge. Both descriptions state which is
  which so the rows are distinguishable.
- **False markings** go in `aliases` as bare identifiers and the story in `description`:
  Tornado F.2 ZD899 wears `ZG757`; Jaguar XX116 previously flew as Indian AF `JI-008`.
- **Access types.** `public` where the airframe stands where a paying or walking visitor
  reaches it (paintball sites, pub garden, activity centre, roadside JP at Wethersfield,
  Andrewsfield's public-café airfield, Sculthorpe's open days). `appointment` where a
  visit must be booked (Sim2do sessions, the Kessingland glamping Lynx, which you see by
  staying in it). `restricted` for the two Army sites (Rock Barracks, Blenheim Camp) and
  the two ATC squadron compounds, where the aircraft is inside a fence.
- **Chippenham Lodge is my least certain access call.** Three jets — Jaguar GR.3A XX116,
  Tornado F.2 ZD899, Sea Harrier FA.2 ZH811 — sit outdoors on a private estate near
  Newmarket with a 2026 sighting and enthusiast photographs from February 2024, which
  implies a public vantage point. I have set `public`; a human should confirm whether
  they are visible from the road or only by arrangement. Note also that eurodemobbed
  files Chippenham under Suffolk; the village of Chippenham is in **Cambridgeshire**, and
  I have used Cambridgeshire in the address.
- **Coordinates** are eurodemobbed's published per-location decimal positions, which are
  airframe-level for these small sites. Sculthorpe has no published pin, so latitude and
  longitude are blank and the postcode NR21 7LX is given instead. Postcodes are blank for
  Mayhem/Abridge, Wethersfield, Andrewsfield, Chippenham Lodge, Rock Barracks and
  Kessingland — I could not source them and a guessed postcode geocodes to the wrong
  village. Coordinates are supplied for all six.

## Excluded, and why — named

Access failures (the airframe exists, a visitor cannot see it):

- **Everett Aero, Sproughton, Suffolk** — the largest single find in the region and the
  biggest exclusion: 19 airframes including Hawks XX157/XX199/XX220/XX246/XX332,
  Jaguars XX139/XX144/XX836, Jet Provost XW330, Sea Harrier ZD581, Harrier GR9 ZG478 and
  five Lynx, most re-sighted August 2025. It is a trading and dismantling yard, not a
  visitor attraction; it is also the source of half the preserved airframes elsewhere in
  this file. Worth a human asking whether they admit visitors by arrangement.
- **Bentwaters Airfield (the wider Bentwaters Parks site), Suffolk** — Hunter XG196,
  Phantom XV460 nose, Harrier T.4 XW267, Jet Provost XW418, Jaguars XX838/XX842,
  Sea Harriers ZH806/ZH812, in and around hardened aircraft shelters. Separate from the
  Bentwaters Cold War Museum already recorded by the east agent at the same postcode;
  ownership and whether any of these are seen on museum tours is unclear. Flagged rather
  than duplicated.
- **AAC Wattisham residue** — Gazelles XX380 (ex main gate) and ZA729, Lynx XZ642/ZF537
  and XZ653 (fire training), Apaches ZJ177/ZJ192. Stored or in use on an active Army Air
  Corps station outside the heritage museum the east agent recorded; not seen by visitors.
- **RAF Lakenheath F-15C 84-0001**, **RAF Honington** Tornados ZA587/ZA613 and Gazelle
  XW860, **RAF Wittering** Puma XW198, Tornado ZA553, Hawk XX351 and AV-8B cockpit
  162737, **RAF Henlow** Gazelle XZ312 and Lynx ZD250 — instructional or stored airframes
  on live stations. eurodemobbed itself annotates several "cannot be seen from the
  outside". The gate guards at all four stations are already recorded by the east agent.
- **STANTA (Stanford Training Area), Norfolk** — Jet Provost XM386, Scout XT643 at East
  Wretham and Wessex XS872 at Tottington. Live Army training area, closed to the public.
- **Cambridge Airport, Marshall Aerospace** — sixteen Hercules C.4/C.5 (ZH865-ZH889) and
  Hercules W2 nose XV208 stored outside, re-sighted November 2025. This is maintenance
  and disposal storage with no public access; it is also not preservation.
- **Blackburn Buccaneer S.2A nose XT284, Felixstowe** — at a private residence,
  "viewable by invitation only" per thunder-and-lightnings. Exactly the case the brief
  says is not a record.
- **Rowneybury House, Sawbridgeworth (Mi-24D)**, **Danbury MiG-23BN**, **Great Dunmow
  Hunter F.5 WP185**, **Rayleigh Vampire T.11 pod WZ608**, **Ingatestone C-119G nose**,
  **Preston/Hitchin Harrier GR.3 nose XV759**, **Cantley Vampire T.11 pod XE979**,
  **Houghton Canberra B.2 nose WJ567**, **Clophill Lynx ZG885**, **Burwell Lynx XZ196**,
  **Green Barn Farm, Badwell Green** (Hunter GA.11 WV256 plus four helicopters) — private
  land, no evidence of any public access.
- **Stapleford Tawney** — fourteen ex-AAC Gazelles stored in a hangar by a trader.
- **Elstree Studios Devon C.2 nose XA880** — film-prop store, last noted 2015.
- **Old Buckenham Lynx XZ608/XZ609** — private restoration in a hangar.
- **Southend Airport** ex-RAAF HS.748s, Bolivian BAe 146 and two Dauphins — commercial
  storage and spares recovery. The Vulcan Restoration Trust's XL426 there is already
  recorded by the east agent.
- **Norwich Airport** — a single stored ex-Bahrain BAe 146 RJ85 inside a hangar. There is
  **no terminal display** at Norwich, Stansted, Luton, Southend or Cambridge; I checked
  each and found none. That answers the airport-display part of the assignment: nil.
- **Upwood** (Lightning F.6 nose XR754, ex-RAAF Boeing 707), **Whittlesey/Gildenburgh
  Lake** (Jet Provost XM467 submerged in a dive lake, last noted 2010),
  **Shipdham Industrial Estate** (three gliders dumped in trailers), **"Suffolk area"**
  (six stored Tucanos at an undisclosed location), **"Ipswich area"** (six stored Scouts,
  several with no sighting date at all) — location or access too vague to stand behind.
- **Private farm strips and airworthy private aircraft** throughout the six counties —
  Audley End, Andrewsfield's Cubs and Tiger Moths, Earls Colne, Clacton, Great Oakley,
  Laindon, Rayne Hall Farm, Wormingford, Crowfield, Elmsett, Monewden, Norton, Rougham,
  Lavenham, Mendlesham, Beccles, Milden, Old Buckenham, Tibenham, Seething, Hardwick,
  Felthorpe, Guist, Langham, North Elmham, Raveningham, Swaffham/Etthornes, East Winch,
  Little Gransden, Fowlmere, Gransden Lodge, Croydon/Top Farm, Cottenham, Winwick,
  Haddon, Riseley, Dunstable, Meppershall, Hatch, Eaton Bray, Graveley, Rush Green,
  Benington, Wilden. These are flying aeroplanes at private strips, not exhibits.
  The brief's "airworthy collections whose aircraft are exhibited when not flying" means
  Shuttleworth and Hangar 11 — already recorded — not a Tiger Moth in a farmer's barn.

Gone or moved (recorded here so nobody re-adds them):

- **Gunsmoke Paintball, Layer Marney, Essex** — Jet Provosts XN579 and XP686 were both
  **sold around 2021 and are no longer present**. Do not record this site.
- **Waterbeach Barracks, Cambridgeshire** — the Hunter that stood outside the gate is now
  at **Sywell Aviation Museum, Northamptonshire** (Hunter F.2 WN904), which is in the
  Midlands agent's file. Waterbeach has no gate guardian.
- **RAF Alconbury** — the F-5E replica gate guardian was **removed on 1 April 2026** and
  is now at RAF Sculthorpe (recorded above). Alconbury has no gate display left.
- **RAF Molesworth** — no preserved airframe on eurodemobbed and none found.
- **RAF Mildenhall** — no preserved airframe on the station. The nearby Hunter F.6 XG210
  at Beck Row, which people call "the Mildenhall gate guard", is already the east agent's
  record `Hawker Hunter Gate Guard, Beck Row`.
- **Bassingbourn Barracks Tower Museum** — no airframe.

## Blank fields left deliberately

- `year_built` is blank on every row. eurodemobbed gives first-flight and delivery dates,
  which I put in `description` as prose; none of them is a sourced build year, and the
  brief forbids deriving one.
- `tail_number` blank only for the Sculthorpe F-5E replica (see above).
- `postal_code` blank on six sites, `latitude`/`longitude` blank only on Sculthorpe.
- `website` blank except Sim2do and Sculthorpe; the rest have no aviation-specific page.
- `model_name` and `aircraft_name` are blank where the type has no separate popular name
  or the airframe has no individual name.

## Needs a human on site — ranked

1. **Chippenham Lodge, Newmarket.** Are XX116, ZD899 and ZH811 visible from a public
   road, or is access by arrangement only? This is the difference between `public` and
   `appointment` on a three-jet site.
2. **Everett Aero, Sproughton.** Do they admit visitors by arrangement? If yes, that is
   19 airframes, the densest unrecorded concentration in East Anglia.
3. **Bentwaters Parks HAS site.** Which of the eight stored jets, if any, are seen on
   Bentwaters Cold War Museum tours? If some are, they belong on the museum's record.
4. **Delta Force Paintball, Bovingdon (Lynx XZ612)** and **Sim2do, Mildenhall
   (Lynx nose XZ195)** — both last reported 2017-18. Confirm still present.
5. **308 Sqn ATC, Colchester (Viking nose ZE556)** — last reported March 2018, and ATC
   squadrons dispose of cockpit sections quietly. Also confirm whether the two ATC sites
   here should be `restricted` while the east agent's Swaffham Air Cadets Auster is
   `public`; the three should be consistent.

## Leads for other agents

- **RAF Croughton, Northamptonshire** was named in my assignment but is outside my six
  counties and outside eurodemobbed's East Anglia pages. It belongs to whoever has
  Northamptonshire (county 35).
- **Sywell Aviation Museum, Northamptonshire** now holds **Hunter F.2 WN904** ex the
  Waterbeach Barracks gate — already in the Midlands file as a site; worth checking the
  Hunter is on its aircraft list.
- **RAF Sculthorpe Heritage Centre, Norfolk (NR21 7LX)** was missed by the east museums
  agent. I have recorded it; if the coordinator wants all museums in one file, move it.
  It also displays B-29, RB-66 and B-45 **wreckage**, which I did not record as airframes
  — a human should decide whether substantial wreckage sections count.
- **Hillside Primary School, Ipswich** formerly used Lynx XZ613 as a classroom; the
  airframe left for Billericay by August 2022. Other East Anglian schools may hold
  airframes that eurodemobbed does not index; I found no current example.
- eurodemobbed county 52 ("United Kingdom") and the "…area" pseudo-locations hold
  airframes whose county is unknown; whoever does a national sweep should re-check them.


---

# Research pass: Scotland, Northern Ireland and the Crown Dependencies

# UK research notes — Scotland, Northern Ireland, Isle of Man, Jersey, Guernsey

Output directory: `/home/claude/uk/scot_ni/`

## Files and row counts

| File | Site | Rows | With tail number |
|---|---|---|---|
| `uk_museums.csv` | 12 sites | 12 | n/a |
| `nmf-east-fortune_topup_aircraft.csv` | National Museum of Flight (TOP-UP, existing DB site) | 62 | 46 |
| `ulster-aviation-society_aircraft.csv` | Ulster Aviation Society | 52 | 37 |
| `dumfries-galloway_aircraft.csv` | Dumfries and Galloway Aviation Museum | 30 | 26 |
| `morayvia_aircraft.csv` | Morayvia Sci-Tech Experience | 18 | 17 |
| `montrose_aircraft.csv` | Montrose Air Station Heritage Centre | 13 | 10 |
| `ulster-transport-museum_aircraft.csv` | Ulster Transport Museum, Cultra | 13 | 11 |
| `manx-aviation_aircraft.csv` | Manx Aviation and Military Museum | 3 | 3 |
| `kelvingrove_aircraft.csv` | Kelvingrove Art Gallery and Museum | 1 | 1 |
| `nms-edinburgh_aircraft.csv` | National Museum of Scotland | 1 | 0 |
| `lossiemouth-gate_aircraft.csv` | RAF Lossiemouth Gate Guardian | 1 | 1 |
| `brighouse-bay_aircraft.csv` | Meteor NF.14 WS792, Brighouse Bay Holiday Park | 1 | 1 |
| `crumlin-road-gaol_aircraft.csv` | Crumlin Road Gaol Wessex Helicopter | 1 | 1 |
| `oatlands-guernsey_aircraft.csv` | Oaty and Joey's Playbarn, Oatlands Village | 1 | 1 |

**197 aircraft rows across 13 sites (12 new + 1 top-up); 161 rows (82%) carry a tail number.**

## Sources and how much weight each carried

- **`aviationmuseum.eu`** per-museum inventories were the densest single source for East
  Fortune, Dumfries, Montrose, Morayvia and the Manx museum. They are broad but demonstrably
  stale in places — see the corrections below. Treated as leads, not facts.
- **A dated spotter's site log (Oxford Aviation Group, 2 October 2021)** listing exactly what
  was standing at Dumfries and Galloway that day was the single most useful currency evidence
  in this assignment. It corrected three serials that the general lists had wrong. Rows in the
  Dumfries file say in `description` whether they were on that dated list or not.
- **Museums' own pages** (`morayvia.org.uk/exhibits`, `nms.ac.uk/.../our-aircraft`,
  `dumfriesaviationmuseum.com`, `ulsteraviationsociety.org`, `visitguernsey.com`) won on
  "what is here now". Morayvia's own exhibit page carries six airframes that the third-party
  lists miss entirely (Vulcan XH563, Valiant XD875, Lightning XM169, Hunter WN957,
  Whirlwind XJ723, Nimrod XV244).
- **`thunder-and-lightnings.co.uk` Phantom survivors** (updated 2025) placed Phantom FG.1
  XV586 at Morayvia — absent from every museum list I found — and flagged the East Fortune
  F-4S as stored rather than displayed.
- **ABPic** dated photographs used as a presence check at East Fortune.
- **Wikipedia** used only for leads. Its National Museum of Flight article lists the civil
  aircraft only and omits the entire military hangar; taken alone it would have produced a
  13-row file instead of 62.

## Corrections made, with evidence

1. **Spitfire F.21 LA198 is at Kelvingrove, Glasgow — not at East Fortune.** The
   `aviationmuseum.eu` East Fortune inventory lists it there; that reflects its 1998–2002
   *restoration* at East Fortune. It has hung in Kelvingrove since 2006 (lowered for
   conservation in 2015, re-hung) and Glasgow's own visitor material still describes it
   suspended in the West Court. Recorded at Kelvingrove; removed from the East Fortune file.
2. **BAC One-Eleven G-AVMO "Lothian Region" was scrapped at East Fortune in March 2026.**
   Excluded from the top-up file. It appears on essentially every published list.
3. **Dumfries: North American F-100D is 54-2163, not 54-005.** 54-2163 is what a dated 2021
   site visit recorded; 54-005 comes from the older general lists. Noted in the row.
4. **Dumfries: Wessex HU.5 is XT486; the Sioux AH.1 is XT236.** `aviationmuseum.eu` has these
   two rows shifted against each other and labels the Wessex a "Sea King UH.5", a designation
   that does not exist. A Flickr image captioned "XT486 Westland Wessex HU.5 | Dumfries &
   Galloway Aviation Museum" settles it.
5. **Dumfries: Twin Pioneer is G-AYFA (ex-RAF XM285), a complete airframe**, not a cockpit
   section as one list has it; and the Jetstream is a **T.2** cockpit, XX483.
6. **Dumfries: Sycamore is WA576, not WA756** (dated 2021 log).
7. **East Fortune: Avro Anson is C.19 G-APHV** (the museum's own aircraft page). One list
   gives its serial as XM597, which is the Vulcan — a straightforward row-shift error.
8. **Highland Aviation Museum, Inverness, closed permanently in October 2019** and its
   aircraft were sold and dispersed. Four of them — Valiant XD875, Lightning XM169,
   Jet Provost XS176 and Herald G-ASVO — are now at Morayvia and are recorded there.
9. **Aldergrove's Wessex gate guardian XR529 moved to Crumlin Road Gaol in January 2019**
   and is on public display there. Aldergrove therefore has no gate guard to record.
10. **Trislander G-JOEY is at Oatlands Village, Guernsey, not at Guernsey Airport.** It was
    stored airside for several years after retirement; it is now installed inside the
    Oaty and Joey's Playbarn and visitors can board it.
11. **East Fortune Phantom F-4S 155848** is listed as stored, not displayed, as of July 2025.
    Recorded `in_storage` with the conflict stated in the description.
12. **East Fortune Viscount G-AMOG** is held but not on display (Wikipedia, museum listings
    agree). Recorded `in_storage`.

## Judgment calls

- **Replicas** are recorded only where the description says so plainly: Montrose's B.E.2c,
  Sopwith Camel and Spitfire Vb (all full-scale replicas, and the Spitfire glass-fibre);
  the Ulster Aviation Society Spitfire IIa BAPC.369 and V-1 BAPC.403; East Fortune's Pilcher
  Hawk replica BAPC.49 (the **original** Pilcher Hawk is in Edinburgh and is recorded there).
- **Cockpit and nose sections** are individual rows with the section status stated in
  `description`, per the brief: 11 at Morayvia, 6 at Dumfries, 6 at East Fortune, 3 at
  Cultra, 1 at Montrose, 1 at the Manx museum.
- **Substantial recovered wreckage as an exhibit** is recorded: Dumfries's Loch Doon
  Spitfire IIa P7540 and its Hudson IV AE489. Loose fragments elsewhere are not recorded.
- **Ulster Aviation Society access.** Recorded `appointment`. There is no admission charge
  but there are no paid staff and casual walk-ins are refused; all visits and tours must be
  booked in advance (`bookvisit@ulsteraviationsociety.org`). Open days are held separately.
- **RAF Lossiemouth's gate guardian** is recorded `public` because it stands at the main
  gate and is visible from the public road; the station itself is not open.
- **Brighouse Bay Holiday Park** (Meteor NF.14 WS792) is recorded `public`: it is a
  commercial holiday park with a leisure club open to non-residents, and the aircraft is a
  landmark outdoor exhibit. This is exactly the "Lightning in the pub car park" category the
  brief asks for.
- **Hang gliders and sailplanes are airframes** and are recorded. At East Fortune I recorded
  the four hang gliders that carry BAPC numbers plus the Pilcher replica, and left out four
  or five further unnumbered hang gliders and microlight wings listed by third parties,
  because untailed rows of the same type at one site cannot be told apart. Named in
  "Left out" below.
- **Ferguson Monoplane appears twice** — a flying replica G-CJEN at the Ulster Aviation
  Society and a static replica (IAHC.6) at Cultra. These are two different objects, not one
  aircraft in two places.
- **Short 330 G-BDBS** is at the Ulster Aviation Society (one row only; a duplicate row was
  removed before writing).

## Excluded, and why — named

- **Highland Aviation Museum, Inverness** — closed October 2019, aircraft dispersed.
- **BAC One-Eleven G-AVMO**, East Fortune — scrapped March 2026.
- **Grampian Transport Museum, Alford** — checked; the collection is road transport only,
  no aircraft.
- **Riverside Museum / Glasgow Museum of Transport** — checked; no aircraft. Glasgow's
  aircraft is the Spitfire at **Kelvingrove**, which is recorded.
- **Summerlee Museum of Scottish Industrial Life, Coatbridge** — no aircraft found in any
  source; not recorded.
- **Jurby Transport Museum, Isle of Man** — occupies a former RAF Jurby hangar but holds
  buses, trams and a locomotive, no aircraft.
- **German Occupation Museum, Guernsey** — no aircraft or substantial airframe section found
  in its published exhibit list. Fragments of crashed aircraft may be in the cases; fragments
  are not records.
- **Jersey** — no preserved airframe found anywhere on the island: not at Jersey Airport,
  not at Jersey War Tunnels, not at Jersey Museum. **No Jersey site is recorded and the
  `Jersey` country value is unused.** This is a negative finding, not an unfinished search,
  but see the open questions.
- **Glasgow Prestwick Airport / Scottish Aviation heritage** — no publicly displayed airframe
  confirmed. The Scottish Aviation Bulldog demonstrator G-ASAL has been photographed at
  Prestwick but I could not establish a public display arrangement. Not recorded.
- **RAF Leuchars / Leuchars Station** — no gate guardian confirmed under Army occupancy. The
  station's Phantom gate guard and the Edinburgh/Leuchars Spitfire replicas are gone; I could
  not establish where to.
- **Kinloss Barracks** — the Nimrod that stood at Kinloss is XV244, now at Morayvia and
  recorded there. No separate Kinloss gate guard confirmed.
- **HMS Gannet, Prestwick; Tain; Machrihanish; Benbecula; Almondbank; Aberdeen/Dyce;
  Castle Archdale; Killadeas; City of Derry/Eglinton; Belfast City Airport;
  Shorts/Bombardier/Spirit Belfast** — searched, no publicly visible preserved airframe
  confirmed at any of them. Belfast's Shorts heritage airframes are at Cultra and at the
  Ulster Aviation Society and are recorded there.
- **East Fortune hang gliders / wings without identifiers** — Albatros ASG.21, Catto CP-16,
  Electra Floater, Hiway Cloudbase, Hiway Skytrike, Firebird Sierra 2, Airwave Magic Kiss,
  Montgomerie-Parsons autogyro, "Dragonfly" man-powered aircraft G-BDFU. Reported by
  secondary sources; left out for want of a usable identifier or confirmed presence.
- **Miles M.17 Monarch G-AFJU**, East Fortune — a single ABPic photograph from 2001 and
  nothing since; the museum's own aircraft pages list the M.18 only. Left out.
- **Westland Lynx "XV699"**, Dumfries — one list carries this, but XV699 falls in a Wessex
  serial block, not a Lynx one, and the code 823 is a Fleet Air Arm Wessex code. Rather than
  import a serial I cannot stand behind, the airframe is left out. See open questions.
- **Blackburn Buccaneer S.1 cockpit**, East Fortune — recorded with a **blank** tail number
  because no source gives one.

## Blank fields left deliberately

- `year_built` is blank throughout. British preservation sources give serials, not build
  dates, and a serial is not a year.
- `latitude`/`longitude` are blank for eleven of the twelve sites. Every site carries a UK
  postcode (or Guernsey/Isle of Man postcode), which geocodes better than a pin I would have
  had to guess. Only the Ulster Aviation Society carries coordinates, from a published
  gazetteer entry for its Gate 3 entrance.
- 36 aircraft rows have no tail number: hang gliders, gliders carrying only BGA trigraphs,
  replicas identified only by BAPC number (put in `description`), and ex-Irish Air Corps
  aircraft identified only by a two- or three-digit number.

## Needs a human on site — ranked

1. **Dumfries and Galloway Aviation Museum: which of the nine airframes not on the dated
   2021 log are still there?** Auster G-AHAT, Vampire XD547, Chipmunk WD386, Trident 1C
   G-ARPP, Jaguar XZ390, Sioux XT236, Tiger Cub G-MMIX, the Canberra fuselage "Q497" and the
   reported Lynx. The 2021 log may simply not have covered the indoor and stored items.
2. **The reported Westland Lynx at Dumfries — what is its real serial?** Left out entirely
   pending an on-site reading.
3. **East Fortune: is the F-4S Phantom 155848 in the military hangar or in the reserve
   collection?** Sources disagree and this changes `display_status`.
4. **East Fortune: the Buccaneer S.1 cockpit's serial**, and whether the Flying Flea is
   BAPC.12 or BAPC.76 (published lists give both).
5. **Jersey: is there genuinely no preserved airframe on the island?** A negative is hard to
   prove from a desk. The Channel Islands Occupation Society and the Jersey Aviation Group
   would settle it.

## Leads for other agents

- **`aviationmuseum.eu`** carries a per-museum inventory page for most UK museums in the same
  format used here. It is the fastest way into a new site, but **treat every entry as a lead**
  — in this assignment it produced a wrong museum for a Spitfire, a shifted serial pair, a
  Vulcan's serial attached to an Anson, and a non-existent "Sea King UH.5".
- **`oxfordaviationgroup.co.uk`** publishes dated multi-site spotter logs with full serial
  lists. Searching it by site name gives you dated presence evidence, which is exactly what
  the brief asks for and is otherwise hard to come by.
- **Solway Aviation Museum, Carlisle** — geographically adjacent to Dumfries, but in England;
  belongs to whoever has the North West.
- **Yorkshire Air Museum, Elvington** holds Meteor NF.14 **WS788**, which is easily confused
  with the WS792 at Brighouse Bay recorded here.
- **RAF Museum Midlands / National Cold War Exhibition, Cosford** holds another Meteor NF.14
  and is the previous home of WS792.
- **Spitfire F.21 LA198 is owned by the Royal Air Force Museum** and displayed on loan at
  Kelvingrove. Whoever does the RAF Museum top-up should not also record it.
- **Nimrod MR.2 XV254** left the closed Highland Aviation Museum in 2019 and I could not
  trace it; it is somewhere in the UK and worth a search by any agent covering scrapyards
  and private collections.
- **Bristol Sycamore WA576** was formerly at the Discovery Museum, Newcastle. If an England
  agent still has it there, that is a conflict to resolve in favour of Dumfries.


---

# Research pass: Northern England

# UK NORTH — Northern England research notes

**Assignment area:** Yorkshire (North, South, West, East Riding), Lancashire,
Greater Manchester, Merseyside, Cheshire, Cumbria, Northumberland, Tyne and Wear,
County Durham. Lincolnshire, Nottinghamshire and Derbyshire deliberately excluded
(another agent). IWM North at Salford Quays deliberately excluded (another agent).

**Output:** `/home/claude/uk/north/` — `uk_museums.csv` (41 sites) plus one
`<slug>_aircraft.csv` per site (41 files, 329 aircraft rows, 304 with a
tail number = 92.4% serial coverage). No top-up files: none of the four
already-in-database UK sites falls in this area.

---

## Sources and how much weight each carried

**1. eurodemobbed.org.uk — the spine, and it earned it.**
I walked all twelve county pages in my area programmatically
(`locations.php?country=20&county=<n>` for counties 8, 10, 14, 16, 19, 26, 30,
34, 36, 45, 51, 57), which returned **119 locations holding ~440 ex-military
airframes**, then fetched every one of the 119 location pages and parsed the
per-airframe serial / type / markings / status / last-noted table plus the
tooltip history text. Its currency is genuinely good: the big museums carry
"noted" dates of **Jul–Aug 2026**, i.e. within two months of this research.
Every serial in this delivery that comes from eurodemobbed carries its
last-confirmed date in the `description` field, so a later reader can see
exactly how fresh each row is.

Its one structural limitation: **it records only ex-military airframes.** It
misses civil aircraft, replicas and BAPC-numbered airframes entirely. That is
why NELSAM shows 27 airframes on eurodemobbed but 43 here, and why Yorkshire
Air Museum shows 37 there but 53 here.

**2. Museums' own collection pages — used to fill the civil/replica gap.**
Yorkshire Air Museum (via `airmuseums.co.uk` and Wikipedia, cross-checked),
NELSAM's own `Exhibits` page, Runway Visitor Park's `explore-our-aircraft`,
Solway Aviation Museum's news pages, the Science and Industry Museum's own
closure page, Eden Camp, Hangar 42.

**3. thunder-and-lightnings.co.uk** — decisive on one movement (Javelin XH767,
below). Excellent for British Cold War types; its per-airframe pages carry
dated site visits.

**4. ABPic** — used to establish the BAPC identities of the Eden Camp replicas
and to confirm the Hangar 42 airframes are all replicas.

**5. Wikipedia — demonstrably stale, used only as a lead.** Its Yorkshire Air
Museum article still lists Gloster Javelin FAW.9 XH767 as being at Elvington;
it left in January 2025. See "Corrections".

---

## Corrections made, with evidence

- **Gloster Javelin FAW.9 XH767 is NOT at Yorkshire Air Museum.** Wikipedia and
  the airmuseums.co.uk collection listing both still carry it. Thunder &
  Lightnings' survivor page records it as donated by YAM to the **East Midlands
  Aeropark, Castle Donington**, arriving January 2025 and photographed there
  1 November 2025. Excluded from the YAM file. **Lead for the Midlands agent.**

- **Blackburn Beverley XB259 — the Fort Paull question, answered.** Fort Paull
  closed in 2020 and its collection was auctioned. XB259, the sole surviving
  Beverley, was saved by the **Solway Aviation Museum** and moved by road from
  Hull to Carlisle Lake District Airport in 2020–21. It is recorded here at
  Solway, `under_restoration` (restoration in the open), last confirmed
  **June 2026**. It did NOT go to Selby. Source: Solway Aviation Museum's own
  news posts plus the eurodemobbed Carlisle entry.

- **RAF Millom Museum (closed 1 September 2010) — where its airframes went.**
  Traced two by name through eurodemobbed history text: Vampire T.11 **XD624**
  went to the Griffin Trust at **Hooton Park** (20 March 2011) and Vampire T.11
  pod **XK637** is now at **Stalybridge**, Cheshire. Millom itself is excluded —
  it no longer exists as a site.

- **Museum of Science and Industry, Manchester — the Air and Space Hall is
  permanently closed and holds no aircraft.** The museum's own page confirms it
  vacated Lower Campfield Market Hall and that **no aircraft remain on display**
  at the main Liverpool Road site. Dispersal, per the museum: Avro Shackleton
  (RAF Museum-owned) → **Avro Heritage Museum, Woodford** (recorded here as
  WR960); Avro 707A and English Electric P.1A → **Boscombe Down Aviation
  Collection**; Avro 504K → **Stow Maries**; Avro 594 Avian → The Aeroplane
  Collection. MOSI is therefore **excluded, with reason**, not omitted.
  **Leads for other agents:** Boscombe Down (south-west) and Stow Maries (east).

- **Avro Anson C.19 TX214 at Woodford** is recorded as an ex-RAF Museum airframe,
  as the assignment flagged; eurodemobbed confirms it present May 2025.

- **RAF Linton-on-Ouse** ceased flying October 2019, closed as an aerodrome
  18 December 2020, and is being sold. **eurodemobbed's North Yorkshire county
  page contains no Linton-on-Ouse location at all** — no gate guardian survives
  on site. No record created. Similarly **RAF Topcliffe, RAF Dishforth,
  Catterick Garrison, RAF Fylingdales and RAF/NSA Menwith Hill produced no
  eurodemobbed entries** and no evidence of a displayed airframe was found; no
  records created. RAF Church Fenton appears only as **Leeds East Airport**
  (privately owned aircraft, excluded below).

- **Variant spelling normalised to British practice** throughout: eurodemobbed's
  `T11`, `FGA9`, `HAR3`, `B2` are written as `T.11`, `FGA.9`, `HAR.3`, `B.2`,
  with the base designation in `model` and the mark in `variant`.

---

## Judgment calls

**Replicas.** Recorded only where a real, identifiable exhibit exists, always
with the word "replica" and "Not an original airframe" written plainly in
`description`, never in `aliases`. BAPC numbers go in `aliases` because they are
identifiers people search on. Replica records: Yorkshire Air Museum (10 — Avro
504K, Blackburn Mercury BAPC.130, Cayley glider, B.E.2c, S.E.5a, P.V.8 Eastchurch
Kitten, Wright Flyer, Hurricane, Spitfire, Bf 109 G-6); Eden Camp (all 3 —
Hurricane BAPC.236, Spitfire IX BAPC.230, Fi 103 flying bomb BAPC.235); Hangar 42
(all 4 — BAPC.268, BAPC.523, BAPC.524, BAPC.525); NELSAM (5 — Hurricane, Morane
Type N, Brown Helicopter BAPC.96, DH.60 Moth 'Jason' G-AAAH, Westland Wapiti).

**False identities.** Where an airframe wears another aircraft's serial, the true
identity is in `tail_number`, the false marking in `aliases`, and the story in
`description`. Worked examples: Solway's Lightning **ZF583** wearing 'XP748';
Solway's Grasshopper **WZ784** displayed as 'WZ792'; YAM's Meteor F.8 **WL168**
as 'WK864'; YAM's Hunter T.7 **XL572** as 'XL571'; YAM's Dakota **XF747** as
'KN353'; NELSAM's Lightning **ZF594** as 'XS933'; Wirral's Avenger **69327** as
'46214'; Doncaster's Skeeter **XM561** as 'XM651' and Whirlwind/Scout composites.

**Cockpit, nose and fuselage sections** are recorded as their own rows with the
section stated first in `description` ("Nose section only.", "Cockpit section
only."). There are many — Doncaster alone is largely a nose-section collection,
and the whole Lakes Lightnings site is cockpits. Per the brief these are in scope.

**Aircraft that are also accommodation or scenery** are in scope and recorded:
the Lynx **XZ676** at Ream Hills Holiday Park is a glamping unit guests sleep in;
Sea King **ZE368** at Holmside Park is a children's play structure; nine airframes
across four paintball sites (Bawtry, Knowsley/Delta Force, Newcastle, East
Rounton, Burnley) are scenery on commercial sites the public pays to enter.

**Underwater airframes.** Hunter F.6A **XJ639** is sunk in the Blue Lagoon dive
lake at Womersley; recorded `on_display` with the description saying plainly it
is visible only underwater, because the site sells access to divers and Hunter
T.8 WT799 stands complete on the bank at the same venue. The far older submerged
airframes at Capernwray and Eccleston Delph are excluded (below).

**Airworthy collections.** Breighton's Real Aeroplane Company fleet is largely
airworthy; recorded `on_display` per the brief, since the museum is open and the
aircraft are there when not flying. Vulcan **XH558** is recorded as `on_display`
at Doncaster with `access_type: appointment` (Vulcan to the Sky runs booked
visits); the airport itself closed to flying in November 2022 but the aircraft
remains.

**Access types.** Gate guardians outside the wire at RAF Boulmer, RAF Spadeadam
and RAF Woodvale are `public` — a visitor can stand on the road and see them.
RAF Leeming and BAE Warton and BAE Brough are `restricted` because most or all of
their airframes are inside the fence; the Leeming file says in `description`
which one (ZH552) is visible from the main gate and which two are not. Lakes
Lightnings and the Sheffield University laboratory are `appointment`.

**Two untailed rows of the same type at one site** — the rule bites once, at
Hangar 42, where two Spitfire replicas would collide. They are distinguished by
BAPC number in `aliases` (BAPC.268 complete aircraft, BAPC.523 cockpit section)
and by the section wording in `description`.

---

## Excluded, and why — named

**Sites that no longer exist**
- **Fort Paull, Paull, East Riding** — closed 2020, collection auctioned. Its
  Beverley XB259 is recorded at Solway. No record.
- **RAF Millom Museum, Cumbria** — closed 1 September 2010. No record.
- **Museum of Science and Industry Air and Space Hall, Manchester** — permanently
  closed, no aircraft remain at the museum. No record.

**Deliberately out of area**
- **IWM North, Salford Quays** (Harrier AV-8A 159233) — assigned elsewhere.
- **Newark, East Midlands Aeropark, and everything in Lincs/Notts/Derbys.**

**Active service or work in progress, not preservation**
- **Teesside International Airport** — the fifteen Aero L-159E Albatros
  (6009–6044, G-DKN- marks) belong to **Draken Europe** and are operational
  contractor aircraft, not preserved. Lynx **XZ652** at the fire school is
  recorded by eurodemobbed as **not present in June 2026**. No record.
- **BAE Systems Warton Typhoons** ZJ801 / ZJ914 / ZJ917 / ZJ926 / ZJ933 / ZJ941,
  Hawk ZJ951 and PC-9 ZG969 — reduce-to-produce and fatigue-test airframes, not
  displayed. Only the Lightning XS928 is recorded.
- **BAE Systems Samlesbury** (Tornado ZA328, Hawks ZK532/ZK533) — "stored,
  outside – bagged" and "instructional, inside". No public display, no gate
  guardian. Excluded; worth a human check.
- **RAF Leeming Hunters** XE688, XF318, ZZ190, ZZ191, ZZ194 — Hawker Hunter
  Aviation contractor airframes, not preserved exhibits.

**Live weapons ranges — real airframes, but no visitor can reach them**
- **RAF Spadeadam mock airfield** (15 airframes: eight Dassault Mystère IVA,
  Su-22M-4K 98+10, four Belgian T-33As, Lynx XZ215/XZ216), **RAF Spadeadam
  Wiley Sike** (Harriers XW768, XZ966, T-33 FT-02) and **Berry Hill** (Mi-24D
  3137, ex-Iraqi). These are 19 genuine airframes used as targets on an active
  electronic-warfare range with no public access whatsoever. Excluded as
  unvisitable. Only the **Spadeadam gate guardian, Jaguar XZ374**, is recorded.

**Private property with no public access** (all confirmed present but not
visitable — recorded here so a later reader knows they were considered, not
missed): Knutsford, Cheshire (6 airframes incl. Spitfire IIa **P8088**, Bf 109
G-2 **13605**, Tornado **ZA399**, Harrier T.8 **ZD992** — a private owner /
Oliver Valves site); **Thorpe Wood, Selby** (27 airframes — Jet Art Aviation /
similar trade storage, "stored outside – dismantled"); **Deighton, York**
(12 Gazelles, dealer stock); **Storwood** (4 helicopters); **Leeds East Airport /
former RAF Church Fenton** (5, incl. Sea Harrier ZH798); **Newburgh, Lancs**
(Phantom noses XT895, ZE352, Sea King ZG875); **Rufforth** (10 gliders);
**Eshott, Northumberland** (14); **Bagby**, **Sherburn in Elmet**,
**Netherthorpe**, **Beckwithshaw**, **Saltergate**, **Egton**, **Newby Wiske**,
**Burn**, **Pocklington**, **Manchester Barton**, **Blackpool Airport** private
hangars, **Weeton army camp** Lynx, **Leeds Coney Park**, **Atherton** (Draken
A-011), **Stalybridge**, **Elworth/Sandbach** (Andover XS641 in a scrapyard),
**Winsford Ash House Farm**, **Frandley**, **Chester area**, **Bolton area**,
**Stockport area**, **Prenton**, **Warrington area**, **Liverpool Airport**,
**Gilberdyke**, **Ellerton**, **Elloughton**, **Skirpenbeck**, **Hexham**,
**Currock Hill**, **Heddon-on-the-Wall**, **Goathland**, **Ingleby Arncliffe**,
**Ravensworth**, **Leyburn**, **Over Dinsdale**, **Harrogate area**, **Helperby**,
**Yearby**, **Crosland Moor**, **Halifax area**, **South Kirkby**, **Upper
Cumberworth**, **Banks (Southport)**, **Hoddlesden**, **Nethertown**, **Hapton**,
**Chipping**, **Appley Bridge** (Devon VP955 and Pembroke XK885 under restoration
*for* Solway — they will belong at Solway once delivered), **Preston Brook Farm**,
**Accrington**, **Brierley**, **Finningley area**, **Doncaster area**,
**Lake District area** (Swift WK275), **Lancashire area** (Spitfire I P9451
remains), **North/West Yorkshire "area"** entries with no precise location.

**Excluded for staleness or unresolvable identity**
- **Cumbria's Museum of Military Life, Carlisle Castle** — a Waco Hadrian glider
  restoration project, last recorded July 2012 with **no identity at all** and
  no evidence in fourteen years that a substantial airframe is on show. Excluded;
  a human on site could settle it in five minutes.
- **Capernwray dive centre, Lancashire** (Dragonfly WP503, Wessex XS491) and
  **Eccleston Delph** (Jet Provost XP688) — last recorded 2003 and 2006, twenty
  years stale. Excluded pending evidence.
- **North Cave** (Puma XW234, submerged, last noted 2008). Excluded.
- **Folland Gnat T.1 XM708, Lytham** — genuine and complete, in Red Arrows
  markings, "preserved inside" since 2002, but Thunder & Lightnings has nothing
  after February 2003 and no public venue could be established. Excluded; this
  is the single most likely false negative in this delivery.
- **Bawtry Hall / Doncaster "area", Finningley "area"** and the other
  precise-location-unknown eurodemobbed entries.

**Pennine and moorland crash-site memorials** — the assignment asked explicitly.
Northern England's moors are dense with them (Bleaklow B-29 *Over Exposed*
44-61748, the Saddleworth and Kinder wreck fields, the Buckden Pike Wellington
memorial cross, the many Dark Peak scatter sites). **None is recorded.** A
scattered wreck field or a memorial cairn is not a preserved airframe: there is
no substantial airframe a visitor can see as an aircraft. This is a deliberate
exclusion under the brief's own test, applied consistently.

---

## Blank fields left deliberately

- **`year_built` is blank on every row.** Not one airframe in this area gave me a
  sourced build or first-flight date I would stand behind; eurodemobbed's history
  tooltips give delivery dates (`d/d`) for many, but a delivery date is not a
  build date and the brief forbids guessing. This is the single largest
  improvable gap in the delivery.
- **Coordinates** are eurodemobbed's own per-location figures, which are
  airframe-precise. Eden Camp and Hangar 42 are left blank — they came from the
  museums' own pages, not eurodemobbed, and I would have been guessing. Both have
  good postcodes (YO17 6RT, FY4 2QY).
- **Postcodes** are blank at eleven small monument and paintball sites where no
  published postcode could be confirmed. Each has coordinates instead.
- **25 rows have no tail number**: 22 replicas (which have no serial, only BAPC
  numbers, recorded in `aliases`), plus NELSAM's Carman MS.100S, Morane Type N
  replica and Wapiti replica.

---

## Needs a human on site — ranked

1. **Folland Gnat XM708 at Lytham.** Complete Red Arrows Gnat, unaccounted for in
   any public source since 2003. Is there a venue the public can visit? If yes
   this is a site record; if it is in a private garden it is not.
2. **The "Blackpool campsite" (Sea Prince WF118 + Lynx ZD258).** Confirmed
   present September 2025 with good coordinates, but I could not establish the
   park's trading name. It is **not** Ream Hills — that is a separate site a
   couple of miles away holding Lynx XZ673/XZ676/XZ173. Someone needs to read the
   sign at the gate.
3. **The Wykeham Sea Kings (XZ589, ZE369).** Both arrived in 2026 and are
   preserved outside near Scarborough, but the venue is unnamed in every source.
   Is this a holiday park, a farm, or a private field? Access type is a guess.
4. **Cumbria's Museum of Military Life, Carlisle Castle.** Does a Waco Hadrian
   airframe exist on display, and what is its identity? Excluded on a fourteen-
   year-old sighting.
5. **Hangar 42, Blackpool.** The centre advertises "five Spitfire replicas" plus
   a "restored original" Hurricane Mk I and Bf 109 E. The BAPC register accounts
   for only four airframes (BAPC.268, .523, .524, .525) and lists all as
   replicas. The "restored original" claim needs testing against a placard.

Also worth a check, lower priority: **BAE Samlesbury** (is Tornado ZA328 on any
kind of display?); **Patrington** (what venue is Vampire XD542 at?); **Banks,
Southport** (AB.47 052 — public or private?); and whether the **Real Aeroplane
Museum at Breighton** holds civil aircraft beyond the 23 ex-military airframes
recorded here (it almost certainly does; eurodemobbed cannot see them).

---

## Leads for other agents

- **East Midlands Aeropark, Castle Donington** — Javelin FAW.9 **XH767** arrived
  January 2025 from Yorkshire Air Museum, photographed there 1 November 2025.
- **Boscombe Down Aviation Collection** — received the **Avro 707A** and the
  **English Electric P.1A** from the closed Manchester Air and Space Hall.
- **Stow Maries Great War Aerodrome, Essex** — received MOSI's **Avro 504K**.
- **The Aeroplane Collection** — MOSI's **Avro 594 Avian Mk IIIA** returned to it.
- **Montrose Air Station Museum, Scotland** — once owned Vampire T.11 **XD542**,
  now at Patrington in East Yorkshire; the Scottish agent should not list it.
- **Tangmere Military Aviation Museum, Sussex** — Meteor F.8 **WA984** left
  Tangmere in May 2022 and is now at Fishburn, County Durham.
- **Gatwick Aviation Museum, Charlwood** — Sea Prince **WF118** left and is now
  on the Blackpool campsite.
- Solway's **Devon VP955** and **Pembroke XK885** are physically at **Appley
  Bridge, Lancashire** under restoration for Solway. Recorded at neither site,
  because a visitor can see them at neither; flag if either changes.

---

## File and row counts

| File | museum_name | rows | with tail |
|---|---|---:|---:|
| `atc_ashton_aircraft.csv` | 247 Squadron Air Training Corps, Ashton-under-Lyne | 2 | 2 |
| `avro_heritage_museum_aircraft.csv` | Avro Heritage Museum | 9 | 9 |
| `bawtry_paintball_aircraft.csv` | Bawtry Paintball Helicopters, Doncaster | 4 | 4 |
| `blackpool_campsite_aircraft.csv` | Blackpool Campsite Aircraft Display | 2 | 2 |
| `breighton_aircraft.csv` | Real Aeroplane Museum, Breighton | 23 | 23 |
| `brough_aircraft.csv` | BAE Systems Brough Gate Guardian | 2 | 2 |
| `burnley_wessex_aircraft.csv` | Burnley Paintball Wessex | 1 | 1 |
| `coneygarth_hawk_aircraft.csv` | Red Arrows Hawk, Coneygarth | 1 | 1 |
| `east_rounton_aircraft.csv` | East Rounton Paintball Aircraft, Yarm | 2 | 2 |
| `eden_camp_aircraft.csv` | Eden Camp Modern History Museum | 3 | 0 |
| `fishburn_aircraft.csv` | Fishburn Airfield Preserved Aircraft | 5 | 5 |
| `fort_perch_rock_aircraft.csv` | Fort Perch Rock, New Brighton | 1 | 1 |
| `hack_green_aircraft.csv` | Hack Green Secret Nuclear Bunker | 1 | 1 |
| `hangar_42_aircraft.csv` | Hangar 42 Spitfire Visitor Centre | 4 | 0 |
| `hartlepool_college_aircraft.csv` | Hartlepool College of Further Education Jet Provosts | 3 | 3 |
| `holmside_park_aircraft.csv` | Holmside Park Sea King Collection, Edmondsley | 9 | 9 |
| `hooton_park_aircraft.csv` | The Griffin Trust, Hooton Park | 16 | 16 |
| `knowsley_paintball_aircraft.csv` | Delta Force Paintball Lynx, Knowsley | 1 | 1 |
| `lakes_lightnings_aircraft.csv` | Lakes Lightnings Collection, Spark Bridge | 9 | 9 |
| `nelsam_aircraft.csv` | North East Land Sea and Air Museums | 43 | 38 |
| `newcastle_airport_aircraft.csv` | Newcastle Airport Instructional Jet Provosts | 2 | 2 |
| `newcastle_paintball_aircraft.csv` | Newcastle Paintball Lynx | 1 | 1 |
| `patrington_vampire_aircraft.csv` | Vampire T.11 Display, Patrington | 1 | 1 |
| `raf_boulmer_aircraft.csv` | RAF Boulmer Gate Guardian | 1 | 1 |
| `raf_leeming_aircraft.csv` | RAF Leeming Gate Guardian and Station Aircraft | 3 | 3 |
| `raf_spadeadam_aircraft.csv` | RAF Spadeadam Gate Guardian | 1 | 1 |
| `raf_woodvale_aircraft.csv` | RAF Woodvale Gate Guardian | 1 | 1 |
| `ream_hills_aircraft.csv` | Ream Hills Holiday Park, Weeton | 3 | 3 |
| `runway_visitor_park_aircraft.csv` | Runway Visitor Park, Manchester Airport | 5 | 5 |
| `sheffield_university_aircraft.csv` | University of Sheffield Laboratory for Verification and Validation | 2 | 2 |
| `solway_aviation_museum_aircraft.csv` | Solway Aviation Museum | 21 | 21 |
| `south_yorkshire_aircraft_museum_aircraft.csv` | South Yorkshire Aircraft Museum | 83 | 83 |
| `speke_meteor_aircraft.csv` | Meteor F.8 Display, Speke | 1 | 1 |
| `strensall_puma_aircraft.csv` | Strensall Barracks Puma | 1 | 1 |
| `vulcan_xh558_aircraft.csv` | Vulcan XH558 Hangar, Doncaster | 2 | 2 |
| `warton_lightning_aircraft.csv` | BAE Systems Warton Lightning | 1 | 1 |
| `winsford_sea_harrier_aircraft.csv` | Sea Harrier Gate Guard, Winsford | 1 | 1 |
| `wirral_transport_museum_aircraft.csv` | Wirral Transport Museum | 1 | 1 |
| `womersley_dive_aircraft.csv` | Blue Lagoon Diving Centre, Womersley | 2 | 2 |
| `wykeham_seakings_aircraft.csv` | Sea King Display, Wykeham | 2 | 2 |
| `yorkshire_air_museum_aircraft.csv` | Yorkshire Air Museum and Allied Air Forces Memorial | 53 | 40 |

**Totals: 41 sites, 41 aircraft files, 329 aircraft rows, 304 with a tail
number (92.4%).** Serial coverage excluding the 22 replica rows is
**304 of 307 = 99.0%**.


---

# Research pass: The Midlands and Lincolnshire

# UK — The Midlands and Lincolnshire: research notes

Assignment area: Lincolnshire, Nottinghamshire, Derbyshire, Leicestershire, Rutland,
Northamptonshire, Warwickshire, West Midlands, Staffordshire, Shropshire,
Herefordshire, Worcestershire. RAF Museum Midlands (Cosford) was recorded by another
agent and is **not** in these files.

Output: `/home/claude/uk/midlands/` — `uk_museums.csv` (63 sites) plus one
`<slug>_aircraft.csv` per site (63 files, 464 aircraft rows).

---

## 1. Sources and how much weight each carried

**`eurodemobbed.org.uk` — the spine.** All twelve county index pages
(`locations.php?country=20&county=<n>`) were walked programmatically, then every one
of the 186 location pages under them was fetched and parsed: 888 ex-military airframe
records with a dated last-sighting each. This is the only UK source that gives a
*per-airframe* sighting date, and its Midlands coverage runs to July–September 2026,
which is current enough to use as a presence test rather than a lead. Its location
pages also carry decimal coordinates, which is where most of the `latitude`/`longitude`
values in `uk_museums.csv` come from — they are the site's coordinates as published by
Euro Demobbed, not guesses.

Its limits: it records **ex-military airframes only**. Every civil aeroplane, glider,
microlight, replica, missile and space vehicle in these files had to come from
somewhere else. It also mixes genuinely visitable sites with private farm strips, so it
cannot be used as a site list without judgement (see §4).

**Museums' own collection pages — authoritative on "what is here now".** Used, and
preferred over Euro Demobbed for holdings, at:
- Newark Air Museum (`newarkairmuseum.org/discover-explore/zones/aircraft-list`) — a
  full 97-row inventory table with in-store (`*`) and off-site (`**`) flags. This is
  the best single source used in the whole assignment.
- Midland Air Museum (`midlandairmuseum.co.uk/exhibits/`) — 51 complete aircraft, 5
  cockpit sections, an engine list and a **missile list**. Page carries 2026 news items,
  so it is current.
- East Midlands Aeropark (`eastmidlandsaeropark.org/aeropark-exhibits.html`) — 37-row
  table, last edited April 2025.
- Sywell Aviation Museum, Metheringham Airfield Visitor Centre,
  Lincolnshire Aviation Heritage Centre.

**Wikipedia** was used only to arbitrate (e.g. confirming Newark holds a Canberra PR.7
*and* a PR.9 cockpit, which resolved an apparent duplicate) and for the Cold War Jets
Collection's status. Treated as a lead throughout.

**thunder-and-lightnings.co.uk** and **forces.net** resolved the RAF Scampton dispersal
(§3). Both give dated, specific movements.

### Which list proved stale
- Euro Demobbed's own entry for **Vulcan K.2 nose XL445 at RAF Scampton** is dated
  Oct 2021 and is wrong: thunder-and-lightnings records the nose moving to the Vulcan
  Flight Simulator team at **Welshpool, Wales** in July 2024 after Scampton closed. Not
  recorded here; see Leads.
- Euro Demobbed carries **Sea Hawk FGA.6 XE368** at both "Bruntingthorpe" (its older
  Cold War Jets entry) and "Lubenham"; the Lubenham sighting is Jul 2026 and the
  Bruntingthorpe one is not. Recorded once, at Lubenham.
- Newark Air Museum's own inventory prints the prone-pilot Meteor as **"WR935"**. It is
  **WK935** — the museum's own 2024 news item announcing the loan says so. Recorded as
  WK935.
- The Victor XM715 support site's "Forthcoming Events" page still advertises an event in
  **August 2019**. Not usable as evidence of current access.
- The Snibston Discovery Park entries (Coalville) are Euro Demobbed rows for a museum
  that closed in 2015; both airframes are flagged "Stored, offsite". Excluded.

---

## 2. Corrections made, with evidence

| Row | What the common list says | What was recorded | Why |
|---|---|---|---|
| Newark, Meteor F.8 | "WR935" (museum inventory) | `WK935` | Museum's own 2024 loan announcement; Euro Demobbed agrees |
| Newark, Hunter T.7 | "XL605" (museum inventory) | `XL605` in `aliases`, `XX467` in `tail_number` | The museum's own list annotates it "(later-XX467)"; XL605 is the marking worn |
| Newark, F-100D | "42223" (Euro Demobbed) | `54-2223` | 42223 is the abbreviated tail stencil; museum gives the full USAF serial. Wears `0-63008` — in aliases |
| Newark, T-33A | "5547" (museum) vs "19036" (Euro Demobbed) | `19036`, both markings in aliases/description | Euro Demobbed is registry-grade on identity; conflict flagged in the row description |
| Midland AM, Lightning T.55 | "55-713" (museum) | `ZF598`, `55-713` in aliases | 55-713 is the ex-Royal Saudi serial; ZF598 is the UK identity |
| Midland AM, F-86A | "8242" | `48-0242` | 8242 is the fin stencil of USAF 48-0242 |
| Midland AM, T-33As | "51-4419" / "51-7473" | as given | Euro Demobbed's 14419/17473 are the same stencilled short forms |
| Midland AM, HH-43 | HH-43B (museum) vs HH-43F (Euro Demobbed) | `HH-43B` variant, conflict stated in description | Museum wins on "what the placard says" |
| Aeropark, Hunter | "BAPC548" (Euro Demobbed) | `XJ714`, composite parts in aliases | Museum lists it as Hunter FR.10 XJ714; BAPC548 is the composite-airframe number |
| Aeropark, Whirlwind | "XG588" (Euro Demobbed) | `XG588`, `VR-BEP` in aliases | Museum lists it as VR-BEP wearing XG588; same airframe |
| Coningsby, XL564 / ZD710 | listed under RAF Coningsby | not recorded | Euro Demobbed itself marks them "Private, off-site" |

---

## 3. RAF Scampton — what happened to it

Asked for specifically. RAF Scampton closed as an RAF station in 2022–23 and the site
passed to the Home Office / West Lindsey District Council; as of February 2026 the Home
Office was still seeking expressions of interest in the site. It is **not recorded as a
site here** and none of its airframes appear in these files. The dispersal:

- **Avro Vulcan K.2 nose XL445** — the only surviving K.2 nose. Left Scampton in
  **July 2024** for the Vulcan Flight Simulator team at **Welshpool, Powys, Wales**.
  Euro Demobbed has not caught up. *Lead for the Wales agent.*
- **BAe Hawk T.1A XX306** (Red Arrows gate guardian, and the last jet to fly out of
  Scampton) — sold at auction for £90,000 in 2023 to Exelby Services and is now a
  permanent display at **Coneygarth Services, A1(M) at Leeming Bar, North Yorkshire**.
  *Lead for the North agent.*
- **The RAF Scampton Heritage Centre** (which held XL445) is closed.
- **Hawker Hunter Aviation's fleet** — Hunter T.8B XF995, Buccaneer S.2B XX885
  (G-HHAA), ex-German Phantom F-4F 37+89 and Su-22M-4K 98+14 — was still stored
  outside at Scampton in July 2026, but behind a closed gate with no public access.
  Under the brief's rule on "aircraft merely stored at a maintenance facility with no
  public access" these are **excluded**. If the site reopens as a heritage attraction
  they become a site record immediately.
- **BAe Hawk T.1W XX349** forward fuselage is on the Scampton fire dump. Excluded.

The Red Arrows moved to **RAF Waddington**, and the two Hawks now preserved/stored
there in team markings (XX311, XX266) are recorded under `waddington_gate_aircraft.csv`.

---

## 4. Judgement calls

**Private airstrips and farm-based owner collections are excluded.** Euro Demobbed's
county pages are dominated by them — Egginton, Spanhoe Lodge, Sywell's resident
warbirds, Wickenby's resident Tiger Moths, Sleap's, Halfpenny Green's, Leicester's,
Fenland's, Gamston's, Strubby's, Bidford's, Alscot Park's, Shobdon's, Hibaldstow's,
Messingham's, Tatenhill's. These are flying aeroplanes at working aerodromes, not
preserved exhibits a visitor can go and see, and the brief excludes them. Roughly 250
of the 888 Euro Demobbed rows in the area fall in this class.

**Farm and roadside *displays* are included**, because the brief names them: Holly Berry
Farm at Corley Moor, Papillon Hall Farm at Lubenham, Salt Box Farm at North Somercotes,
Homer's Lane at Freiston, the lake at Friskney, the Wainfleet control tower. Where the
public's right of access is not established these carry `access_type: appointment` and
the row description says what is known.

**Paintball parks are included as sites** (Brailsford, Bassetts Pole, Tong, Rednal,
Bicton, Kidderminster, and one south of Birmingham). They admit paying members of the
public and a real airframe can be seen. Only sites with a sighting in 2019 or later
were taken; the airframes are described plainly as props, and several are cabins or
pods only. Bilsthorpe (2017) and Kegworth (2021) Lynx cabins were left out as too
fragmentary and too stale.

**Bruntingthorpe** is recorded as one site, `Bruntingthorpe Cold War Jets Collection`,
`access_type: appointment`. The story: the walk-up museum closed in June 2020, the
collection moved to a new hardstanding on the north edge of the airfield, and it
reopened on an invitation/event basis from November 2022. Euro Demobbed maintains a
separate location "Bruntingthorpe - Museum" whose airframes were all re-sighted in
**November 2025**, so the collection is demonstrably still there and still shown. The
Lightning Preservation Group (XR728, XS904) and the Victor XM715 team run their own
public event days. It is not a museum you can turn up at; hence `appointment`. The two
Euro Demobbed locations have been merged into one site record.

**RAF Cosford Defence College of Technical Training** is recorded as a site separate
from RAF Museum Midlands, `access_type: restricted`, 80 airframes. The brief explicitly
puts "apprentice and technical-training airframes" in scope. Most are inside workshops
and hangars and are given `in_storage` because a visitor cannot see them; the gate
guardian (JP T.5A XW327) and the small on-base display line (Harrier XZ991, Tornado
ZA320, Tornado F.3 ZE340, Sea Harrier ZH796, Jaguar XX110, Wessex XR498) are
`on_display`. This is the single largest Jaguar and Hawk concentration in the country
and it would be a real gap to omit it, but nothing here is walk-up visitable.

**Replicas** are recorded only where the replica status is stated in the description:
Newark's Lee-Richards Annular Biplane (BAPC 20), Midland Air Museum's 1910 Humber
monoplane replica (BAPC 9), Sywell's Dragon Rapide cockpit mock-up (G-AJHO "Rachel").
No fibreglass "gate guard Spitfires" were found in this area — every gate guardian
recorded here is a real airframe.

**False markings** are in `aliases` with the true identity in `tail_number` and the
story in `description`: XS897 wearing XP765 and ZF580 wearing XS935 at Binbrook, XR713
wearing XR718 at Bruntingthorpe, XX467 wearing XL605 at Newark, J-1542 wearing WR470 at
Bruntingthorpe, WN904 wearing WN921 at Sywell, XN632 wearing XN623 at Chetton, KX829
wearing P3395 at Thinktank, 56-0312 in RCAF marks as 17447 at Midland Air Museum,
XX457 wearing TAD001 at the Aeropark, H259 wearing 9L-MLTL at Melbourne Hall.

**Cockpit and nose sections** are in scope and are recorded as their own rows with the
section stated plainly in `description` — 60-odd rows across the area, e.g. Newark's
Beverley, Argosy and Buccaneer cockpits, the Aeropark's VC10 forward fuselage and
Vanguard/Viscount flight decks, Chetton's four noses, Tettenhall's Balliol and Canberra
noses, Sleap's Balliol cockpit, Defford's Canberra nose, Rolls-Royce Derby's Canberra
B.15 nose.

**Airworthy collections are recorded** where the aircraft are exhibited between flights:
the Battle of Britain Memorial Flight at RAF Coningsby (11 rows including Lancaster
PA474, which Euro Demobbed does not list because it is not out of service), and the
ground-running collections at Bruntingthorpe, East Kirkby (NX611, HJ711) and
Wellesbourne (XM655).

**Missiles and space vehicles.** Midland Air Museum's published missile list is recorded
as seven `missile_rocket` rows (Blue Steel, Thunderbird, Red Top, Firestreak, Fireflash,
Red Dean, Skyflash), all with blank serials because none is published. The WE.177
tactical nuclear bomb and the 1000lb bomb displayed with Vulcan XL360 are **not**
recorded — they are bombs, not missiles or rockets. At the National Space Centre, Blue
Streak and Thor Able (both genuine, both upright in the Rocket Tower) and the Soyuz
spacecraft in the entrance hall are recorded; the Vostok capsule, the Apollo lunar
lander and the Sputnik are **excluded** because I could not establish from a source
whether they are flight hardware or mock-ups, and the Centre's own text calls the
Sputnik a "mock Sputnik".

**Blank fields left deliberately.** 16 of 464 rows have no `tail_number`: the seven
Midland Air Museum missiles, the three National Space Centre vehicles, Newark's unmarked
Sherwood Ranger and Slingsby T.67 cockpit trainer, Midland Air Museum's Harrier II
cockpit and Cadet TX.1 (the museum quotes only `BGA.804`), the Aeropark's Ka 8 glider,
and the Percival Proctor at East Kirkby. In every case the identifier is genuinely not
published and a guess would have been worse than a blank. `year_built` is blank
throughout — no build/first-flight date was sourced to the standard the brief requires.

---

## 5. Excluded, and why — named

**Closed, dispersed, or moved out of the area**
- *RAF Scampton* and all six of its Euro Demobbed airframes — see §3.
- *Vulcan nose XL445* — now Welshpool, Wales.
- *Hawk XX306* — now Coneygarth Services, North Yorkshire.
- *Snibston Discovery Park, Coalville* — museum closed 2015; Taylorcraft HL535 and
  Auster AOP.9 XP280 both "stored offsite".
- *RAF Museum reserve collection, Stafford (MoD Stafford Hangars)* — 16 airframes
  including Spitfire F.21 LA226, Spitfire LF.IX SL674, Halifax II R9371 cockpit, Seagull
  V A2-4, Bleriot XI. This is the Royal Air Force Museum's storage site: no public
  access, and it belongs to the RAF Museum agent's brief, not mine. Named here so the
  omission is a finding rather than a gap.
- *RAF Cosford Museum* and *RAF Cosford Museum Store (Hangar 9)* — RAF Museum Midlands,
  recorded by another agent as instructed.

**Not visitable**
- *Pontrilas, Herefordshire* — Chinook CH-47A (serial unconfirmed) inside the UK Special
  Forces training facility.
- *Beckingham Training Camp, Notts* — Puma XW225 on a live training area.
- *RAF Barkston Heath* — Canberra B(I).8 WT339, derelict airfield furniture, not a
  display.
- *Coventry University, Gulson Road* — Harrier T.4 XW270, a ground-instructional
  airframe inside an engineering department.
- *Loughborough University* — Hawk 200 ZH200, ditto.
- *Solihull College Woodlands Campus* — Jetstream T.2 XX478; last sighting 2016.
- *Willenhall (Cable & Alloys) and Irthlingborough (Allens Metals)* — working
  scrapyards, not open to visitors; Lansen 32028 nose, Lynx ZD281, Whirlwind XR458.
- *RAF Shawbury stored Hawk and Chinook fleet* (≈40 airframes) — an active MoD storage
  and reduce-to-produce line. Only the gate guardian, Wessex XR516, is recorded.
- *Stoney Cove, Leicestershire* — Wessex HU.5 XT768 and XT770 submerged as dive
  attractions. Genuinely visitable, but by qualified divers only, and the last
  sightings are 2005 and 2008. Left out; a good candidate if the database ever wants
  underwater sites.

**Too stale to stand behind**
- *384 (Mansfield) Squadron ATC* — Canberra PR.7 nose WT507, last noted **January 2009**.
  The brief asks for ATC airframes and this is the only ATC-held airframe Euro Demobbed
  lists in the area, but seventeen years is not evidence of presence. Ranked as an open
  question below.
- *Walcott, Lincolnshire* — a three-item cockpit collection (Lightning XS932, Harrier
  XV810, Sea Harrier ZD614), last noted 2018–19, ownership and access unknown.
- *Corby area* Vampire XE849 (2010), *Little Addington* JP nose XN137 (2011),
  *Wigston* Harrier cockpit XW763 (2010), *Welbeck* Gazelle XX381 (2010),
  *Kenilworth* Wellington forward fuselage Z1206 (2006), *Stockton* Vampire pod WZ553
  (2010), *Stone* Sea Venom XG629 (2012), *Tamworth* Cadet XE793 (2008),
  *Cannock* Canberra PR.9 nose XH174 (2012), *Bewdley* Canberra PR.9 nose XH175 (2009),
  *Redditch* AV-8B nose 162074 (2016), *Bromsgrove* Hunter nose XE597 (2020),
  *Wolverhampton area* Harrier nose XZ131 (2020), *Biddulph* Jaguar cockpit XZ385
  (2020), *Gateford* Harrier T.10 nose ZH655 (2017), *Grimsby area* Vampire cockpit
  WZ584 (2019), *Kirton in Lindsey area* Vampire pod XD595 (2020), *Caistor area*
  Lightning nose XS899 (2018), *Stamford area* Lightning cockpit XP757 (2015),
  *Lincolnshire area* three noses (2019–21), *Potterspury* Lightning nose XR759 and
  ZF595/ZF596 composite (Euro Demobbed itself flags both "NOT confirmed"),
  *Bramcote / Gamecock Barracks* Andover nose XS643 and Bulldog cockpit XX655 (2022),
  *Telford* Lynx XZ213 (location not pinned down), *Barby* Lynx AH.7 XZ664/XZ665
  (Euro Demobbed says sold to a dealer in 2018).
  All of these are private cockpit holdings in unnamed locations; none has a stated
  public-access arrangement.

**No airframe found**
- *RAF Digby* — has the Sector Operations Room Museum, but no preserved airframe appears
  on Euro Demobbed's Lincolnshire pages and none was found elsewhere. Not recorded.
- *Kendrew Barracks (former RAF Cottesmore), Rutland* — no airframe on Euro Demobbed's
  Rutland page. St George's Barracks at North Luffenham *is* recorded (Sea Harrier
  ZD607 gate guardian, Whirlwind XP344).
- *Pershore, Worcestershire* — no preserved airframes.
- *Sir Frank Whittle memorials* — the Lutterworth and Coventry memorials are sculptures,
  not airframes. Whittle is properly represented by the **Sir Frank Whittle Jet Heritage
  Centre**, which is part of the Midland Air Museum and is recorded within that site
  record (the museum's own strapline is "Incorporating The Sir Frank Whittle Jet
  Heritage Centre").
- *RAF Wickenby Memorial* — the memorial and the small museum in the control tower hold
  no airframe. Everything Euro Demobbed lists at Wickenby is privately owned and flying.

---

## 6. Boundary and collision risks (read before importing)

1. **RAF Wittering** is administratively in **Cambridgeshire** (Peterborough), not
   Northamptonshire, but was named explicitly in my assignment. It is recorded here as
   `RAF Wittering Heritage Museum` (7 rows: Harriers XV779, XZ146, XW923, ZD318, P.1127
   XV279, AV-8B nose 162964, and gate guardian ZD469). **If the East of England agent
   also recorded it, drop one copy.** The airframes came from Euro Demobbed location
   2498, so the two versions should be reconcilable serial-for-serial.
2. **Midland Air Museum** sits at Baginton in **Warwickshire** (postcode CV3, a Coventry
   code); Euro Demobbed files it under West Midlands. Recorded with a Warwickshire
   address, city Baginton.
3. **Humberside Airport** is in **North Lincolnshire** and appears on Euro Demobbed's
   Lincolnshire page. Recorded here. If a Yorkshire/Humber agent also took it, dedupe.
4. **East Midlands Aeropark** is at East Midlands Airport, which straddles the
   Leicestershire/Derbyshire boundary; Euro Demobbed files it under Leicestershire.
   Recorded once, city Castle Donington.

---

## 7. Ranked "needs a human on site"

1. **Bruntingthorpe access.** Is the new-site collection open to individual visitors in
   2026, or only at LPG/Victor event days and by invitation? The access type recorded
   (`appointment`) is a judgement, and the site could equally be `public` on event days.
   Also worth confirming whether Comet XS235, Nimrod XV226 and Victor XM715 are all on
   the new hardstanding or still on the old dispersal.
2. **384 (Mansfield) Squadron ATC, Canberra PR.7 nose WT507** — present or long gone?
   Seventeen years without a sighting. This is the one ATC airframe in the whole area
   and it would be worth having.
3. **Newark's Auster AOP.9.** The museum inventory says `XR268`, fuselage and wings, in
   store; Euro Demobbed says `XS238`, on display inside, March 2025. One airframe, two
   identities. I recorded `XS238` and flagged the conflict in the row. A placard photo
   settles it.
4. **RAF Scampton.** Does anything remain accessible? Hawker Hunter Aviation's four
   airframes were still there in July 2026. If the site reopens for heritage access it
   becomes an immediate site record.
5. **Coventry Airport Nimrod XV232.** Coventry Airport announced closure in 2026
   (flagged on the Midland Air Museum's own news page). XV232's last Euro Demobbed
   sighting is April 2021. Its future — and its access arrangements — need checking.
6. Lesser: the Percival Proctor's serial at East Kirkby; the Ka 8's registration at the
   Aeropark; whether Melbourne Hall's Puma glamping pod can be *seen* by a day visitor
   or only by someone who books the pod.

---

## 8. Leads for other agents

- **Wales:** Vulcan K.2 nose **XL445** went from RAF Scampton to the Vulcan Flight
  Simulator team at **Welshpool, Powys** in July 2024. Only surviving K.2 nose.
- **North of England:** ex-Red Arrows Hawk T.1A **XX306** is now a permanent display at
  **Coneygarth Services, A1(M), Leeming Bar, North Yorkshire** (bought at auction 2023).
  Also **Lightning T.55 ZF595's nose section is at North Weald, Essex** while its centre
  fuselage is at Binbrook — the two halves are in different agents' areas.
- **South West / Gloucestershire:** the **tail section of Wellington L7775** is at
  **Moreton-in-Marsh town**, while the rest of the aircraft is at East Kirkby.
- **East of England:** **RAF Wittering** (Cambridgeshire) — see §6.1. Also **Conington**
  (2 airframes) sits on the same Euro Demobbed Cambridgeshire page.
- **RAF Museum agent:** the **Stafford reserve collection** (MoD Stafford, 16 airframes
  including Spitfire F.21 LA226 and Seagull V A2-4) and **RAF Cosford Museum Store,
  Hangar 9** (10 airframes including Meteor F.9/40 DG202/G, Bristol 188 XF926, EE P.1A
  WG760) are RAF Museum holdings I have deliberately not touched.
- **Anyone doing a "moved to a pub / theme park" sweep:** Alton Towers holds Lynx AH.9A
  ZG887; the Fourways Bar and Grill at Rowley Regis holds Lynx AH.9A ZG884; the Stag at
  Red Hill, Alcester has Sea Prince WM735 in the farmyard behind it.

---

## 9. File and row counts

| file | site | rows | with serial |
|---|---|---:|---:|
| `aeropark_aircraft.csv` | East Midlands Aeropark | 35 | 34 |
| `alton_towers_aircraft.csv` | Lynx ZG887, Alton Towers | 1 | 1 |
| `bassetts_pole_aircraft.csv` | Whirlwind XP350, Bassetts Pole Paintball | 1 | 1 |
| `bbmf_coningsby_aircraft.csv` | Battle of Britain Memorial Flight Visitor Centre | 11 | 11 |
| `bicton_paintball_aircraft.csv` | Whirlwind XP360, Bicton Paintball | 1 | 1 |
| `binbrook_lightning_aircraft.csv` | Lightning Association Collection, Binbrook | 13 | 13 |
| `binbrook_village_aircraft.csv` | Lightning F.6 XR725, Binbrook Village | 1 | 1 |
| `birmingham_paintball_aircraft.csv` | Jaguar GR.1 XX739, Birmingham Paintball | 1 | 1 |
| `brailsford_aircraft.csv` | Lynx Helicopters, Brailsford Paintball | 3 | 3 |
| `bruntingthorpe_aircraft.csv` | Bruntingthorpe Cold War Jets Collection | 27 | 27 |
| `chetton_aircraft.csv` | Chetton Heritage Aircraft Collection, Bridgnorth | 5 | 5 |
| `coningsby_gate_aircraft.csv` | RAF Coningsby Gate Guardians | 4 | 4 |
| `corley_moor_aircraft.csv` | Holly Berry Farm Aircraft Display, Corley Moor | 3 | 3 |
| `cosford_dctt_aircraft.csv` | RAF Cosford Defence College of Technical Training | 80 | 80 |
| `coventry_nimrod_aircraft.csv` | Nimrod XV232, Coventry Airport | 1 | 1 |
| `cranwell_gate_aircraft.csv` | RAF Cranwell Gate Guardians | 2 | 2 |
| `cranwell_heritage_aircraft.csv` | Cranwell Aviation Heritage Centre | 2 | 2 |
| `credenhill_aircraft.csv` | Agusta A109 ZE412, Stirling Lines, Credenhill | 1 | 1 |
| `defford_aircraft.csv` | Defford Airfield Heritage Group Museum, Croome | 1 | 1 |
| `donnington_aircraft.csv` | Harrier XZ971, MoD Donnington | 1 | 1 |
| `fleet_hargate_aircraft.csv` | Hunter F.1 Gate Guard, Fleet Hargate | 1 | 1 |
| `freiston_aircraft.csv` | Freiston Aircraft Display | 2 | 2 |
| `friskney_aircraft.csv` | Sea King ZG822, Friskney | 1 | 1 |
| `halfpenny_green_aircraft.csv` | Jet Provost Gate Guard, Wolverhampton Halfpenny Green Airport | 1 | 1 |
| `hemswell_aircraft.csv` | Jet Provost, Hemswell Antiques Centres | 1 | 1 |
| `honeybourne_aircraft.csv` | Whirlwind XP346, Honeybourne | 1 | 1 |
| `hucknall_aircraft.csv` | Hucknall Flight Test Museum | 3 | 3 |
| `humberside_aircraft.csv` | Humberside Airport Aircraft Displays | 2 | 2 |
| `kidderminster_paintball_aircraft.csv` | Lynx XZ193, Kidderminster Paintball | 1 | 1 |
| `lahc_east_kirkby_aircraft.csv` | Lincolnshire Aviation Heritage Centre | 10 | 9 |
| `longton_jp_aircraft.csv` | Jet Provost XM425, Longton | 1 | 1 |
| `lubenham_aircraft.csv` | Papillon Hall Farm Aircraft Collection, Lubenham | 4 | 4 |
| `mam_aircraft.csv` | Midland Air Museum | 71 | 62 |
| `melbourne_hall_aircraft.csv` | Puma Glamping Pod, Melbourne Hall | 1 | 1 |
| `metheringham_aircraft.csv` | Metheringham Airfield Visitor Centre | 1 | 1 |
| `mod_stafford_aircraft.csv` | MoD Stafford Beacon Barracks Aircraft Display | 2 | 2 |
| `newark_aircraft.csv` | Newark Air Museum | 99 | 97 |
| `north_luffenham_aircraft.csv` | St George's Barracks Gate Guardian, North Luffenham | 2 | 2 |
| `north_somercotes_aircraft.csv` | Whirlwind Collection, Salt Box Farm, North Somercotes | 3 | 3 |
| `potteries_aircraft.csv` | The Potteries Museum and Art Gallery | 1 | 1 |
| `red_hill_alcester_aircraft.csv` | Sea Prince WM735, Red Hill, Alcester | 1 | 1 |
| `rednal_paintball_aircraft.csv` | Wessex XT480, Rednal Paintball | 1 | 1 |
| `rowley_regis_aircraft.csv` | Lynx ZG884, Fourways Bar and Grill, Rowley Regis | 1 | 1 |
| `rr_derby_aircraft.csv` | Rolls-Royce Heritage Trust Derby | 1 | 1 |
| `shawbury_gate_aircraft.csv` | RAF Shawbury Gate Guardian | 1 | 1 |
| `sheepbridge_aircraft.csv` | Jet Provost XM480, Sheepbridge | 1 | 1 |
| `skegness_lightning_aircraft.csv` | Lightning T.5 XS456, Skegness | 1 | 1 |
| `sleap_aircraft.csv` | Wartime Aircraft Recovery Group Museum, Sleap | 1 | 1 |
| `space_centre_aircraft.csv` | National Space Centre | 3 | 0 |
| `syerston_aircraft.csv` | RAF Syerston Aircraft Display | 9 | 9 |
| `sywell_aircraft.csv` | Sywell Aviation Museum | 7 | 7 |
| `tettenhall_aircraft.csv` | Tettenhall Transport Heritage Centre | 6 | 6 |
| `thinktank_aircraft.csv` | Thinktank Birmingham Science Museum | 2 | 2 |
| `thorpe_camp_aircraft.csv` | Thorpe Camp Visitor Centre | 5 | 5 |
| `tong_paintball_aircraft.csv` | Gazelle XZ318, Tong Paintball | 1 | 1 |
| `tyseley_hunter_aircraft.csv` | Hunter PR.11 WT723, Birmingham Tyseley | 1 | 1 |
| `waddington_gate_aircraft.csv` | RAF Waddington Gate Guardians | 4 | 4 |
| `wainfleet_tower_aircraft.csv` | Wainfleet Control Tower Aircraft Display | 2 | 2 |
| `warkton_aircraft.csv` | Wessex XV726, Kestrel Caravans, Warkton | 1 | 1 |
| `wellesbourne_museum_aircraft.csv` | Wellesbourne Wartime Museum | 4 | 4 |
| `whittington_aircraft.csv` | Puma ZE449, Whittington Barracks, Lichfield | 1 | 1 |
| `wittering_aircraft.csv` | RAF Wittering Heritage Museum | 7 | 7 |
| `xm655_aircraft.csv` | Vulcan XM655, Wellesbourne Mountford | 1 | 1 |
| **total** | 63 sites | **464** | **448 (96.6%)** |

Serial coverage: **448 of 464 rows (96.6%)** carry a `tail_number`. The 16 blanks are
itemised in §4 and are all cases where no identifier is published.

Written with python's `csv` module, `lineterminator="\n"`, UTF-8. Validated for: enum
values (`aircraft_type`, `wing_type`, `military_civilian`, `display_status`,
`role_type`), `wing_type` set for fixed-wing only, `museum_name` matching
`uk_museums.csv` character for character, alias rules (no commas, ≤4 words, ≤34 chars,
dashless forms present), and **no duplicate tail number across any two files** — the
last of these is what caught the Sea Hawk XE368 double-entry.


---

# Research pass: South-East England

# UK — SOUTH-EAST ENGLAND research notes

Assignment: every preserved airframe of every kind in Kent, East Sussex, West Sussex,
Surrey, Hampshire, Isle of Wight, Berkshire, Buckinghamshire, Oxfordshire and Greater
London — **excluding** the RAF Museum London, the Science Museum, IWM London and
IWM Duxford, which other agents hold.

Output directory: `/home/claude/uk/southeast/`
Files: `uk_museums.csv` (66 sites) + 66 `<slug>_aircraft.csv` files + this file.
**317 aircraft rows, 302 with a serial or registration (95%).**

---

## 1. Sources and how much weight each carried

| Source | Weight | What it gave / where it failed |
|---|---|---|
| **`eurodemobbed.org.uk`** county index (`locations.php?country=20&county=<n>`) | **The spine.** Every airframe row below started here. | Walked all 11 county pages for this area programmatically, then fetched all **212 location pages** and parsed them: **1,052 airframes**. Each row carries type, code/markings, status *and a dated last sighting*, plus lat/lon and often a full history tooltip. Sightings run from 2005 to **Aug 2026**, so it doubles as the currency check the brief demands. This is by far the best UK source and nothing else came close. |
| Museum's own website | Wins on "what is here now" | Used for Gatwick Aviation Museum opening arrangements, Kent Battle of Britain Museum, Lashenden, MAPS Rochester, the Trenchard Museum, St George's Chapel Biggin Hill and Brooklands' Aircraft Park. Several were unreachable by machine: Tangmere returns **403 Forbidden**, Solent Sky and FAST returned empty bodies, and `brooklands­museum.com/explore/our-collection/aircraft` and `armyflying.com/explore/aircraft/` are both **404** — their published aircraft indexes are gone. |
| `thunder-and-lightnings.co.uk` | Good for one-off currency checks | Confirmed Sea Hawk WV795 still inside the Dunsfold gate (photo dated 26 Jun 2021). |
| Wikipedia | Leads only, never a fact | Its Brooklands list omits the VC10, the One-Eleven and the whole Aircraft Park; its Kent Battle of Britain Museum list mixes replicas and originals without distinguishing them, and lists a "Gotha G.IV" and "Fokker Dr.I" I could not corroborate. Both were used only to point at things to verify elsewhere. |
| `aviationmuseum.eu`, `airshowspresent.com` | Enthusiast surveys, treated as leads | Gave a much fuller Brooklands list than the museum's own live site; conflicts between the two are recorded in §3. |

**Where eurodemobbed is weakest:** it covers *ex-military* airframes. Civil-only
collections are invisible to it. That is exactly why Brooklands (Concorde, the
One-Eleven, the Viscount, the Merchantman, the Viking, the replicas) needed a
separate pass, and why Solent Sky's civil exhibits are under-recorded here.

---

## 2. Site counts by area

| Area | Sites | Notable |
|---|---|---|
| Kent | 10 | RAF Manston History Museum (22), Kent Battle of Britain Museum, Spitfire & Hurricane Memorial, Brenzett, Lashenden, Shoreham, Royal Engineers Museum, Chatham Dockyard, MAPS Rochester, two roadside monuments |
| Hampshire | 14 | Army Flying Museum (32), Solent Sky (14), FAST (14), Gliding Heritage Centre (10), AAC and RAF gate guards, Fleetlands |
| West/East Sussex | 10 | Tangmere (18), Wings Museum (25), Amberley, Robertsbridge, two paintball sites, campsite Wessex, two ATC airframes |
| Surrey | 5 | Brooklands (25), Gatwick Aviation Museum (14), Dunsfold, Camberley |
| Greater London | 8 | Biggin Hill Heritage Hangar (24), National Army Museum, Battle of Britain Bunker, St George's Chapel, Staples Corner Hunter, Battersea Park Lynx, Greenford Scout, RAF Northolt |
| Oxfordshire | 11 | Aces High gallery, Benson and Brize Norton gate guards, Shrivenham, MOD Bicester, four roadside monuments, Culham paintball |
| Buckinghamshire | 2 | Trenchard Museum RAF Halton (8) + Halton instructional airframes |
| Berkshire | 2 | Museum of Berkshire Aviation, Maidenhead paintball Lynx |
| Isle of Wight | 2 | Wight Aviation Museum, Windmill Campersite Wessex |

Access split: 37 `public`, 18 `restricted` (inside a military or MoD gate), 11 `appointment`.

---

## 3. Corrections, conflicts and judgment calls

**Gatwick Aviation Museum — status established (the brief asked).** It has had a
long history of access disputes with Mole Valley/Reigate & Banstead planning. As of
its own live Visit page it is **open to the public Saturdays and Sundays 10:00–17:00**,
adults £13.50, with weekday and evening visits by arrangement. Recorded as `public`.
Wikipedia and the museum list **Sea Hawk XE364**; eurodemobbed identifies the same
airframe as **WM983 wearing the false serial XE489**, ex-Dutch J-485. I took
eurodemobbed's true identity for `tail_number` and put XE489 in `aliases` — but note
the museum's own placard and Wikipedia both say XE364, a *third* number. **Unresolved:
one of these three is wrong and it needs a look at the airframe.** Likewise the museum
calls XS587 a "Sea Vixen TT.8"; eurodemobbed and the CAA register call it a **D.3**
(G-VIXN). I used D.3 and put the other designations in aliases.

**Brooklands — the museum's own aircraft index is a 404**, so the collection had to be
assembled from the live *Aircraft Park* exhibition page (which names seven airliners
but no registrations), the four surviving `collection-highlights` pages, eurodemobbed's
16 ex-military airframes, and two enthusiast surveys. The two surveys **disagree**:
one lists Lancaster and Jetstream XX499 sections that the other does not, and one
lists a Spitfire IIa P8088/G-CGRM. I recorded only what two independent sources or
eurodemobbed support, and left out the Lancaster section, XX499, the Spitfire, the
TSR-2 EMU, the Avro 504, the Drone, the SE.5a replica, the Demoiselle, the Gull, the
Flea, the Ladybird, the Voisin, the Willow Wren, the Viking Amphibian replica, the
Sopwith Tabloid replica, the Vimy cockpit BAPC.420, Merchantman cockpit G-APEJ and
Viscount cockpit G-AZLP. **That is a deliberate under-count of perhaps 15 rows** and
is the single biggest known gap in this submission — see §6.
VC10 nose **G-ARVM** is recorded here but was for years at RAF Museum Cosford; I have
flagged the doubt in its `description` rather than dropping it.

**Serials that are maintenance serials, not identities.** UK practice is to give a
withdrawn airframe an "M" number. These are in `aliases`, never in `tail_number`
(7154M for WB188, 7712M for WK281, 9006M for XX967, 8140M for XJ571, etc.). I
**deleted** the aliases I had drafted for Halton's XF522 and XF527 because I could not
source their M-numbers and would have been guessing.

**Gate guardians wearing someone else's markings** — recorded per the brief with the
true identity in `tail_number` and the false marking in `aliases`:
XT827 Sioux wears XT231 (Middle Wallop); XP895 Scout wears XP849 (Berkshire Aviation);
WD646 Meteor TT.20 wears WD615 (Manston); E-412 Hunter wears XF368 (Brooklands);
WV332 Hunter nose is ex-Swiss J-4201; ZF578 Lightning F.53 is displayed as XR753;
FX442 Harvard wears N7033; LF751 Hurricane wears BN230; WM983 Sea Hawk wears XE489.

**Full-size replicas.** Recorded, with the word *replica* stated plainly in the
description and no serial in `tail_number`, at: **St George's RAF Chapel Biggin Hill**
(Spitfire as K9998 QJ-K for Geoffrey Wellum; Hurricane as P2921 GZ-L for Peter
Brothers — both glass-fibre, built by a Norfolk yachting firm, installed summer 2010);
**RAF Northolt** (Spitfire Mk I on the A40, commemorating the Polish squadrons); and
the **Battle of Britain Bunker, Uxbridge** (refurbished Spitfire gate guardian — I
could not verify what markings it currently wears, so its aliases are blank).
At **Brooklands** the Vimy NX71MY, Fury K5673, Camel B7270, Bleriot G-LOTI and
Roe I G-ROEI are all stated as replicas in their descriptions. The **Kent Battle of
Britain Museum** has a large fleet of full-size replicas (Spitfire, Bf 109, Defiant
"L7005", Hurricane "N2532", three gate-guardian Hurricanes, a Moth) mostly built for
the 1969 *Battle of Britain* film — **I have deliberately recorded none of them**
because I could not source individual BAPC identities and two untailed rows of the
same type at one site must be distinguishable. See §6.

**Cockpit and nose sections are in scope and are recorded as their own rows**, always
saying so in the description. This area is unusually rich in them: Robertsbridge is
*entirely* nose sections (6), Aces High Steventon is 5 of 6, and Wings Museum,
Manston, Tangmere and Brenzett hold many more.

**Composites and airframes with no identity.** Recorded with a blank `tail_number` and
the reason in the description: the Waco Hadrian at Middle Wallop (wears 243809), the
Bolingbroke and the Tiger Moth at Hawkinge, the Beaufighter cockpit and two Kingcobra
fuselages at Wings, the Grasshopper at the Gliding Heritage Centre, the Helldiver
cockpit, the Ju 88 cockpit at Shoreham. The two anonymous Wings Kingcobra fuselages
are distinguished in description and aliases by their sighting dates.

**Airworthy collections are recorded**, per the brief. Biggin Hill Heritage Hangar
(The Spitfire Company) is `appointment` — hangar tours and Spitfire passenger flights.
Its airframes under restoration or stored off site are marked `under_restoration` /
`in_storage` rather than `on_display`, because a visitor cannot see them.

**Two aircraft the survivors database flags as doubtful** are carried with the doubt
in the description rather than dropped: Lynx XZ727 at Battersea Park Children's Zoo
("identity NOT confirmed") and Jet Provost XN495 at the Wings Museum ("confirm this
is here?").

**Hovercraft are not aircraft.** The Hovercraft Museum at Lee-on-Solent (SR.N5, SR.N6,
BH.7, HD.1, Cushioncraft CC-7) and the Cushioncraft CC-7 at Sandown are excluded.
They appear on eurodemobbed because they carry military serials.

---

## 4. Excluded, and why — named

| Site | Reason |
|---|---|
| **HMS Sultan, Gosport (53 airframes)** | eurodemobbed lists 54 at Gosport. All but the gate guardian are Royal Navy Air Engineering & Survival School ground-training airframes and withdrawn stored helicopters (≈25 Sea Kings, Merlin HM.1s, Lynx, Wildcat ZZ402, Tornado ZA323, Gazelles, EH-101 ZF649) inside the wire of a training establishment with no public access. The **navy agent recorded only the gate guardian Lynx XZ692 and passed the rest to me; I reached the same conclusion and excluded them.** This is the single largest excluded block in the area. |
| **RAF Benson stored Pumas (16)** | Sixteen withdrawn Puma HC.2s parked on the station after the type's 2025 retirement. Withdrawn-in-use aircraft on an operational station, not preserved and not visible. Only the gate-guardian Puma HC.1 ZA937 is recorded. |
| **RAF Odiham stored Chinooks / RAF Brize Norton JADTEU airframes** | Same reason. Only the two Odiham gate guardians and the Brize Dakota KN566 are recorded. |
| **Martin-Baker, Chalgrove (9)** | Ejection-seat test airframes on a closed company airfield: Meteor 7½S WA638/WL419, Hawk XX316, two ex-Danish F-16 noses, plus dumped F-5A, T-38B and F-6 hulks. No public access at all. |
| **White Waltham (41)** | Private owners' airfield and a film-prop store (Tornado ZA355 in USAF marks, Sea King ZB506/ZF116, Black Hawk 80-23476). Nothing is displayed; no visitor access. |
| **Peasemore, Newbury (15) and East Hanney, Oxon (22) — The Gazelle Squadron / Falcon Aviation** | ~35 Gazelle airframes, mostly stored hulks and booms, on two private farm strips. The airworthy Gazelle Squadron display aircraft are visitable only at airshows, not at these addresses. Excluded; passed on as a lead. |
| **Charlwood Yard, Surrey (5)** | A private yard 0.6 miles west of Gatwick Aviation Museum holding Sea Harriers XZ497 and ZE698 and three Sea Kings. Not the museum, not open. Easy to confuse with the museum — flagged so nobody merges them. |
| **Horsham ASL (6), Small Dole (6), Woodmancote (4)** | Commercial helicopter spares yards holding ex-RAN Sea Kings, Pumas and Lynx. Trade premises, not visitable. |
| **"Kent area" Tucano store (12)** | Twelve ex-RAF Short Tucano T.1s in storage at an undisclosed Kent location. No address, no access. |
| **Cowes scrapyard, Isle of Wight** | Phantom FG.1 nose XT863 at Cliftongrade scrapyard (noted Jul 2026). A scrapyard that does not admit visitors. |
| **Airframe Assemblies, Sandown IoW** | Spitfire AA810 and TB382 in a commercial restoration workshop; no public access. |
| **Britten-Norman, Bembridge / Lee-on-Solent (13)** | Islander/Defender airframes for spares recovery and stored company stock at an operating manufacturer. Not preserved, not displayed. |
| **Bramley, Longmoor, Pirbright, Southwick Park, Keogh Barracks, Horsea Island** | Army/MoD battle-damage-repair and ground-instruction hulks, and one Wessex deliberately sunk at the Defence Diving School. Training articles inside ranges, not displays. |
| **Redhill, Goodwood, Headcorn, Thruxton, Popham, Wycombe Air Park, Shoreham, Turweston, Enstone, Kidlington, Denham, Deanland, Lasham (private aircraft)** | Working GA airfields whose eurodemobbed entries are privately owned flying warbirds and light aircraft based there, not exhibits. The *museum* content at Lasham (the Gliding Heritage Centre) **is** recorded; the Jaguar gate guard at Enstone **is** recorded. Boultbee Flight Academy's Spitfires at Goodwood are flying aircraft in commercial operation. |
| **Lavendon (7), Sholing (3), Catford, Golders Green, Kingston, Sutton, Wimbledon, Stockbury, Chailey, Lewes, Uckfield, Ashford, Badger's Mount, Stonegate, Sittingbourne, Woodperry, Great Bookham, Nutfield, Frensham and ~40 other "Private" entries** | Cockpit and nose sections in private houses, gardens, farms and lock-ups that do not admit the public. The brief is explicit: a cockpit in a private house that does not admit the public is not a record. Canberra WJ731 at Golders Green and Hunter E-420 at Walton-on-Thames are both listed "For Sale". |
| **Hovercraft Museum, Lee-on-Solent** | Holds no aircraft (see §3). |
| **Bicester Heritage** | Visited the eurodemobbed entry: the only airframe is a Piper Cub *stored off site*. Bicester Heritage is a motoring/aviation business park of restoration companies with no standing aircraft display. Not a site. |
| **Greenham Common, Upper Heyford, Abingdon (Dalton Barracks), Thorney Island, Dover, Chichester, Old Sarum** | No preserved airframe found in any source. Greenham Common's only eurodemobbed entry is Spitfire NH238, listed "Stored" with **no sighting date at all** — the airframe is a flying Spitfire and is not on show there; excluded. Old Sarum is Wiltshire and not mine. |
| **Portsmouth Historic Dockyard (Sea Harrier ZD611)** | Correctly held by the navy agent as part of the National Museum of the Royal Navy. Not duplicated. |
| **Guildford Paintball (Lynx XZ217)** | Listed "For Sale" in Jan 2022 and not seen since. Cannot stand behind its presence. |

---

## 5. Blank fields left deliberately

- `tail_number` blank on 15 rows: the three replicas at Biggin Hill chapel, Northolt
  and Uxbridge; the Waco Hadrian, Bolingbroke, Tiger Moth composite, Beaufighter
  cockpit, Helldiver cockpit, Ju 88 cockpit, Phoenix drone at the National Army
  Museum, the Reichenberg at Lashenden, the Gliding Heritage Grasshopper, and the two
  anonymous Kingcobra fuselages. Each says in `description` why there is no serial.
- `year_built` is blank on **every** row. eurodemobbed gives first-flight and delivery
  dates in free-text history tooltips, but parsing them into a build year would have
  meant guessing which date the field wants. Blank beats a guess.
- `latitude`/`longitude` are filled from eurodemobbed's own per-location coordinates,
  which are airframe-accurate. The three sites where I supplied a postcode but the
  coordinates are approximate to the site rather than the airframe (St George's Chapel,
  Battle of Britain Bunker) are the only pins I derived rather than copied.
- Some postcodes are the best available for the *site* rather than the exact airframe
  (Ford, Thame, Erith, Gravesend, Hamble, Enstone). They will geocode to the right place.

---

## 6. Needs a human on site — ranked

1. **Kent Battle of Britain Museum, Hawkinge — the replica fleet.** Eight real
   airframes are recorded. The museum also displays a Spitfire replica, a Bf 109
   replica, a Boulton Paul Defiant replica marked L7005, a Hurricane replica marked
   N2532 and **three gate-guardian Hurricanes** in the grounds. Nobody publishes their
   BAPC numbers together. Someone on site (photography is allowed in the grounds after
   your visit) could settle 6–8 rows in ten minutes.
2. **Brooklands Museum — a full walk-round.** The museum's own aircraft index is dead
   and the enthusiast lists disagree by roughly fifteen airframes (§3). Specifically:
   is the Lancaster nose section there? Jetstream XX499? Spitfire IIa P8088/G-CGRM?
   Merchantman cockpit G-APEJ and Viscount cockpit G-AZLP alongside the complete
   G-APEP and G-APIM? And is VC10 nose G-ARVM at Brooklands or still at Cosford?
3. **Gatwick Aviation Museum Sea Hawk — XE364, XE489 or WM983?** Three numbers, three
   sources, one airframe (§3).
4. **RAF Halton is closing.** The station is scheduled to close and the Trenchard
   Museum's future is not stated anywhere I could reach. Typhoon FGR.4 ZJ911 arrived as
   gate guardian only in 2024; Hunter XF527 stands outside; Jet Provost XW303 is a jump
   on the equitation course. **Where do these ten airframes go?** This is the most
   time-sensitive question in the area.
5. **RAF Swanwick Harrier XW917** — last sighting Aug 2016, ten years stale, and the
   only airframe at the site. **Battle of Britain Bunker Spitfire** — confirm what
   markings the replica wears. **Shoreham Aircraft Museum Ju 88 cockpit** — last
   sighting May 2014.

---

## 7. Leads for other agents

- **Wiltshire agent:** Old Sarum is theirs, not mine, and eurodemobbed's Wiltshire page
  is county 58. Boscombe Down Aviation Collection sits there too.
- **Whoever holds RAF Museum London:** RAF Museum airframes are on loan *out* into my
  area and are recorded where a visitor finds them, not at Hendon — Hunter WB188 and
  Swift WK281 at Tangmere, Hurricane LF751 and Spitfire TB752 at the Spitfire &
  Hurricane Memorial Museum, Swift WK198 at Brooklands. Please do not double-record.
- **Whoever holds IWM Duxford:** Hunter F.6A **XG226** is split — the nose is at RAF
  Manston History Museum (recorded here), the rear fuselage is at the East Midlands
  Aeropark. Same for Lynx XZ680 at East Grinstead, whose boom is from XZ608.
- **East of England agent:** Upminster/Damyns Hall (Havering) sits inside the M25 and
  appears on eurodemobbed's *London* page (loc 2691), but is functionally an Essex GA
  strip. I excluded it as private; flagging in case it belongs in an Essex sweep.
- **Anyone doing a "gate guard" sweep:** eurodemobbed's status vocabulary is the key.
  `Preserved, outside` / `Preserved, gate guard` / `Preserved, on base` are all
  displayable; `G.I.`, `Dumped`, `W.f.u.`, `Spares recovery`, `Fire Dump` and
  `Instructional` are not. Filtering on that field is what made 1,052 rows tractable.
- **Anyone doing the whole UK:** the 212 parsed location pages for this area are a
  reusable pattern — `locations.php?country=20&county=<n>` gives the location IDs,
  `locations.php?location=<id>` gives a five-column table plus lat/lon plus a per-
  airframe history tooltip. Note the **old `demobbed.org.uk` domain is dead** but its
  `/images/` path still serves the photographs eurodemobbed links to.
- **Not chased, worth someone's time:** Bentley Priory Museum (Stanmore) may have a
  full-size Hurricane replica outside — Wikipedia does not confirm it and I could not
  verify it. Croydon Airport Visitor Centre and a possible de Havilland Heron there.
  RAF High Wycombe gate guardians (a source exists at wycombeworldonline.co.uk but
  robots.txt blocked it). The Short Scion II under restoration at MAPS Rochester,
  whose identity I could not source.


---

# Research pass: South-West England and Wales

# UK — South-West England and Wales

Assignment area: Cornwall, Devon, Dorset, Somerset (incl. North Somerset and
Bath & NE Somerset), Wiltshire, Gloucestershire (incl. South Gloucestershire),
Bristol, and the whole of Wales. The Fleet Air Arm Museum / Navy Wings,
RNAS Yeovilton and RNAS Culdrose were explicitly out of scope and are not
recorded here. The Helicopter Museum already exists in the database, so it is
delivered as a **top-up file only** and is deliberately absent from
`uk_museums.csv`.

---

## Sources and how much weight each carried

**1. `eurodemobbed.org.uk` — the spine.** Its UK county index
(`locations.php?country=20&county=<n>`) was walked programmatically for
counties 4 (Bristol), 9 (Cornwall), 12 (Devon), 13 (Dorset),
18 (Gloucestershire), 33 (North Somerset), 40 (Scilly Isles), 43 (Somerset),
44 (South Gloucestershire), 53 (Wales) and 58 (Wiltshire). That produced
**177 locations and 954 airframe records**, each with a dated last sighting.
South Gloucestershire and the Scilly Isles county pages are genuinely empty —
South Gloucestershire's sites are filed by EuroDemobbed under Bristol or
Gloucestershire, and the Scillies have no preserved airframe. Sighting dates
in the area ranged from 1997 to August 2026; anything last seen before roughly
2015 was treated as unsafe and is either excluded or flagged in the row's
`description`.

Its one structural limitation is that it is an *ex-military* survivors
database. Every civil airframe in this dataset — Concorde G-BOAF, the SWAM
airliner cockpits, the Bournemouth civil fleet, most of the Helicopter Museum's
Westland 30s and gyroplanes — had to come from elsewhere.

**2. Museums' own structured listings — used in preference to everything else
for "what is here now".**
- The Helicopter Museum publishes a genuinely structured fleet at
  `helimuseum.com/fleet.php` and `reserve.php` with registration, builder,
  construction number, year and a note per airframe. This is the closest thing
  to a Pima-style feed found anywhere in the assignment and it is what the
  top-up file is built on. (Note: `helicoptermuseum.co.uk` redirects to
  `helimuseum.com`; the `.co.uk` host also fails TLS to some clients.)
- `bamhurn.org/exhibits/` — Bournemouth Aviation Museum, one page per exhibit
  with full provenance prose. This is where the civil airframes and their
  construction numbers came from.
- `cornwallaviationhc.co.uk` — read for its aircraft list and instead yielded
  the closure notice (below).
- `airworldmuseum.com`, `aerospacebristol.org`, `southwalesaviationmuseum.com`
  for address/postcode/opening confirmation.

**3. Enthusiast registers** — `cardiffstathan.blogspot.com`'s South Wales
Aviation Museum page, which is a maintained registration-level table and the
only public source for SWAM's civil airframes.

**4. Wikipedia** — leads only, and it proved stale exactly where the brief
warned it would. Its Jet Age Museum article still lists Meteor T.7 **WF784**
and Canberra TT.18 **WK126**, both of which EuroDemobbed places at St Athan
(July 2026 sightings), and Javelin FAW.4 **XA634**, which is at the Midland Air
Museum. Its Helicopter Museum article gives EH101 PP3 as ZH647 while the
museum's own page says ZH657; see the conflicts section.

---

## Corrections and conflicts

**Cornwall Aviation Heritage Centre is closed and is NOT recorded as a site.**
Its own website now carries: *"The Cornwall Aviation Heritage Centre is now
permanently closed due to the termination of its premises lease… Cornwall
Council has terminated CAHC's tenancy and we may never open again."* The
closure was announced for 31 October 2022 when Cornwall Council did not renew
the lease on the Aerohub HAS site. The collection has dispersed, and this
dataset follows the airframes to where they now are:
- Vickers Varsity T.1 **WJ945** → South Wales Aviation Museum
- Vickers VC10 K.3 **ZA148** (nose) → South Wales Aviation Museum
- Harrier GR.3 **XV753** → St Athan (private, not recorded)
- Tornado F.3 **ZH553**, Hawk T.1A **XX240** → MoD Boscombe Down JARTS
  (military, not recorded)
EuroDemobbed still shows six airframes at the old CAHC location with 2023–24
sightings; those are residue on a site with no public access and are excluded.
**A human should establish what is left in the Aerohub HAS site and whether
anything was scrapped.**

**Sikorsky S-55C S-886 vs S-887.** The Helicopter Museum's own reserve list
names S-881 and S-886. EuroDemobbed has S-881 and S-887 at the museum
(March 2026) and S-886 at Hamburger Hill Paintball, Marksbury (April 2017).
An aircraft is in one place, so the dated sightings were followed: **S-881 and
S-887 at the museum, S-886 at Marksbury**, and the conflict is written into
both rows' descriptions. The Marksbury sighting is nine years old and is the
weakest currency claim in this dataset.

**EH101 PP3.** Recorded as **ZH647** (EuroDemobbed and Wikipedia agree); the
museum's fleet page prints ZH657, which is treated as a typographical error.
Civil marks G-EHIL are in `aliases`.

**Super Frelon.** Recorded under French Air Force serial **116** per
EuroDemobbed; the museum quotes only civil marks F-BMHC/F-OCMF and Wikipedia
quotes F-BTRP. Both civil marks are in `aliases`.

**Jet Provost T.5A XW320** carries 9016M in EuroDemobbed's identity field and
9015M in its code field; both are noted in the description.

**Comet 1XB XM823 / G-APAS** at South Wales Aviation Museum is confirmed
present — EuroDemobbed's July 2026 sighting corroborates the September 2025
transfer from the RAF Museum noted in the assignment. It is `in_storage`
(outside, awaiting display), not `on_display`.

**Bournemouth Aviation Museum is open**, contrary to the "closed?" flag in the
assignment: its own site advertises daily opening 10:00–17:00 (16:00 in
winter), £10 adult admission, at Merritown Lane, Hurn, BH23 6BA. Recorded in
full, 30 airframes.

---

## Judgment calls

- **Airworthy privately-owned light aircraft at private strips are excluded.**
  EuroDemobbed's county pages are dominated by them — Dunkeswell (15),
  Eaglescott (11), Eggesford (9), Compton Abbas (13), Henstridge (27),
  Rendcomb (9), Oaksey Park (11), Middlezoy, Netheravon, Saltford, Chirk. These
  are aircraft in active private use on land with no public access; they are
  not preserved airframes a visitor can go and see. Named here so the omission
  is a finding rather than a gap. The one exception made is Meteor T.7 **WL345**
  at Middlezoy, which is a static preserved jet, not a flying club aeroplane.
- **Cockpit and nose sections are recorded as their own rows** with the section
  status stated plainly in `description`. Boscombe Down Aviation Collection is
  overwhelmingly a nose-section collection (roughly 25 of its 48 rows) and is
  recorded that way.
- **Replicas are recorded only where the site displays them as exhibits, and
  always labelled.** Aerospace Bristol's Boxkite, Scout, Babe and the replica
  half of the Bristol Fighter display; Jet Age's Gamecock reproduction, E.28/39
  replica, Hurricane V6799 replica and Horsa cockpit replica; BDAC's
  volunteer-built Lancaster front section and B.E.2b. None carry a real serial
  and none has an invented one.
- **Diving sites are recorded** (National Diving & Activity Centre Tidenham,
  Cromhall Quarry, Vobster Quay). The airframes are submerged but genuinely
  visitable — by divers — and are the reason people dive those quarries.
  `access_type` is `appointment`; `display_status` is `on_display` with the
  submerged condition in `description`.
- **Paintball sites are recorded** (Bristol Activity Centre, Marksbury,
  Thornbury, Trebudannon, Higher Kinnerton, Cowbridge, Radyr). These are exactly
  the "oddities" the brief asks for and all are visitable on a booking.
- **ATC squadron airframes** are `restricted` (inside a cadet HQ compound):
  Frampton Cotterell, Melksham, Bideford, Hawarden, Ammanford, Llanbedr.
- **Gate guardians visible from a public road are `public`** even on a military
  site: RAF St Mawgan's Sea King is `restricted` because it stands inside the
  station perimeter, while MoD Boscombe Down's Lightning T.4, RAF Valley's Hawk
  and MoD Sealand's Tornado are at or outside the gate and are `public`.
- **Historic Helicopters, Chard** is recorded as `appointment`. It is a working
  restoration and heritage-flight operation with nine ex-military helicopters
  and holds open days; EuroDemobbed files it simply as "Private".
- **Cotswold Airport, Kemble** is recorded only for the airframes EuroDemobbed
  marks "Preserved" plus Britannia C.1 XM496, whose preservation society runs
  visitor days. The Buccaneers, Canberra PR.9 G-OMHD and the Mustang on the
  same airfield are privately owned and in storage/active use, and are excluded.
- **`year_built` is almost always blank.** It is populated only for the
  Helicopter Museum, Bournemouth's civil types and Aerospace Bristol, where the
  museum itself publishes a build year. No serial was ever converted to a year.

---

## Excluded, and why — named

| Site | Reason |
|---|---|
| Cornwall Aviation Heritage Centre, Newquay | Permanently closed 31 Oct 2022, lease terminated; collection dispersed |
| Classic Air Force, Newquay | Wound up 2016; no airframes remain under that name |
| Topsham, Exeter (Buccaneer XV359, Jaguar XZ378, Tornado ZA353, Sea Harrier ZD612) | Private industrial-estate compound, explicitly "Private Location", no public access |
| Welshpool-area cockpit collection (9 nose sections incl. Vulcan XM652, Lightning XS923, Buccaneer XT277) | Private collection, no evidence of public admission |
| Newton Abbot Firefly noses; South Molton (Harrier nose XZ138); Gloucester-area nose collection; Cheltenham Scimitar nose XD215; Dursley Vampire cockpit XD452 | Private cockpit collections with no published visiting arrangement |
| MoD Lyneham DCTT (31 Lynx/Gazelle/Apache training airframes) | Inside a live Defence College of Technical Training; only the REME Museum part is public and that is recorded |
| Moreton-in-Marsh Fire Service College (9 airframes) | Fire-training hulks inside a closed training establishment |
| Pembrey Range, Carmarthenshire (Jaguars XX958/XX966, Wessex XR523, Sea King XV372) | Live MoD air weapons range; targets, no access |
| RAF St Athan flightline (42 airframes incl. the Sea Harrier fleet at Horizon Aircraft Services and GJD Services' Pumas) | Commercial maintenance/storage inside the Bro Tathan perimeter; not a visitor site |
| Science Museum store, Wroughton (Dominie NF865, Devon VP975, Gnat XP505, Fa 330) | Reserve store, not open for general visiting; last EuroDemobbed sighting 2013 |
| Dyson HQ, Malmesbury (Lightning F.1A XM173, suspended in the staff café) | Private corporate campus, no public admission |
| Somerton, Somerset (16 Sea Kings, Heli Operations) | Working commercial helicopter storage/overhaul, no public access |
| Portland Heliport (Sea Kings 89+61, 89+64) | Heli Operations training base, not a visitor site |
| Bristol Events Site, Backwell (Arcadia Spectacular — 2 Sea Kings, 1 Lynx) | Stored props on a private events yard |
| Chew Valley (Sea King XZ570, Lynx ZG915) | No evidence of public access at the given coordinates |
| Lizard, Haeleacher Farm (Lynx ZD566) | Private farm; visiting arrangement unknown |
| Callington (Lightning F.6 XR755) | Private site, no public access |
| Trelonk Farm, Truro (Spitfire Vb BL688) | Commercial restoration shop |
| St Mawgan "Spitfire Corner" (Canberra nose WD954) | Stored outside on private ground |
| Larkhill (Phoenix ZJ303) | Royal Artillery Museum storage, no access |
| Salisbury Air Defence Collection (Hurricane cockpit P3554, Lynx nose ZD264) | Last sightings 2007/2017; no current public venue established |
| National Waterfront Museum Swansea; Techniquest Cardiff | Checked as leads; neither holds a real airframe |
| Newquay Airport (Tiger Moths N6985/T6313, Chipmunk WB721 — Vintage Aircraft Factory) | Airworthy aircraft in commercial operation |
| Bournemouth Airport (Draken Europe fleet: 6 Falcon 20, 2 L-159, 13 Squirrel) | Aircraft in active contractor service |
| Caernarfon Airfield fire dump (Whirlwind XD165) | Fire dump wreck, lying on its side, not an exhibit |
| Salisbury Plain (Lynx XZ171, XZ203) | Derelict hulks on a live training area |
| Plympton, New England Quarry (Whirlwind XP395) | Submerged in a quarry with no diving operation established |

---

## Blank fields left deliberately

- `latitude`/`longitude` are populated for **every** site (54 of 54) because
  EuroDemobbed publishes airframe-level coordinates. None was guessed; where
  EuroDemobbed had no coordinate the site was excluded on other grounds anyway.
- `postal_code` is blank for 17 sites — mostly roadside gate guards, farm
  displays and ATC squadrons for which no postcode is published. Coordinates
  are supplied instead and are more precise.
- `website` is blank for everything except the eight sites with a confirmed
  live site of their own.
- `year_built` is blank for 300 of 382 aircraft rows.
- `tail_number` is blank for 11 rows, all replicas or unregistered home-builts
  (Aerospace Bristol's Boxkite/Scout/Bristol Fighter/Babe, Jet Age's
  E.28/39, Horsa cockpit and Typhoon cockpit, BDAC's Lancaster front section
  and B.E.2b, the Helicopter Museum's Hobby Copter and Hilton Teledrone). No
  two untailed rows of the same type share a site.

---

## Needs a human on site — ranked

1. **Cornwall Aviation Heritage Centre residue, Newquay.** What is still inside
   the Aerohub HAS site (Canberra WJ874 G-CDSX, Canberra TT.18 WK124, Jet
   Provost XN494, Jet Provost nose XP642, Pilatus P-2 A-125), who owns it, and
   whether any of it can be seen. Also whether Shackleton AEW.2 **WL795** is
   still standing where the public can see it — it is EuroDemobbed's only
   Shackleton in Cornwall and it is filed as "Private".
2. **Welsh Spitfire Museum, Haverfordwest** (Spitfire LF.VIIIc JG668). Last
   independent sighting September 2021 and no working website found. Confirm
   it is still open at 7 Bridge Street before the record is trusted.
3. **20 (Bideford) Squadron ATC, Lightning F.6 nose XR747.** EuroDemobbed's own
   note says it was "not present outside" at one check. Confirm it is still
   held by the squadron.
4. **Hunter GA.11 WT744 at Braunton** and **Jet Provost T.3A XM358 at Newmead
   Farm, Newbridge on Wye.** Both are recorded `public` on the assumption they
   are roadside displays. Neither has a published street address; confirm they
   can actually be seen from a public place.
5. **Hawarden Airport, Flintshire.** The Su-17s, MiG-27, Tornado F.3 ZE966 and
   Jet Provost XP585 are marked "Preserved, outside" but sit on the Airbus
   Broughton airfield. Recorded `restricted`; establish whether there is any
   public viewing arrangement, and whether the L-29 591771 is still in pieces
   beside a container as EuroDemobbed describes.

Secondary questions: whether Jet Age Museum still holds the Trident 3B nose
**G-AWZU** (Wikipedia says so; deliberately omitted for lack of a current
source); whether Bristol University's Queen's Building Bulldog **FM1223** and
Bristol Vanguard's Lightning **XP745** admit visitors at all (XP745 is recorded
`appointment`, the university Bulldog is omitted).

---

## File and row counts

| file | site | rows | with serial |
|---|---|---|---|
| `20-bideford-squadron-atc_aircraft.csv` | 20 (Bideford) Squadron Air Training Corps | 1 | 1 |
| `2247-hawarden-squadron-atc_aircraft.csv` | 2247 (Hawarden) Squadron Air Training Corps | 1 | 1 |
| `2445-llanbedr-squadron-atc_aircraft.csv` | 2445 (Llanbedr) Squadron Air Training Corps | 1 | 1 |
| `2475-ammanford-squadron-atc_aircraft.csv` | 2475 (Ammanford) Squadron Air Training Corps | 1 | 1 |
| `37-frampton-cotterell-squadron-atc_aircraft.csv` | 37 (Frampton Cotterell) Squadron Air Training Corps | 1 | 1 |
| `aerospace-bristol_aircraft.csv` | Aerospace Bristol | 12 | 8 |
| `airworld-aviation-museum-caernarfon_aircraft.csv` | Airworld Aviation Museum, Caernarfon | 10 | 10 |
| `bogey-knights-devonport_aircraft.csv` | Bogey Knights, Devonport | 1 | 1 |
| `boscombe-down-aviation-collection_aircraft.csv` | Boscombe Down Aviation Collection | 48 | 46 |
| `bournemouth-aviation-museum_aircraft.csv` | Bournemouth Aviation Museum | 30 | 30 |
| `bridgwater-and-taunton-college_aircraft.csv` | Bridgwater and Taunton College | 1 | 1 |
| `bristol-activity-centre-paintball_aircraft.csv` | Bristol Activity Centre Paintball | 1 | 1 |
| `britannia-royal-naval-college-dartmouth_aircraft.csv` | Britannia Royal Naval College Dartmouth | 1 | 1 |
| `cardiff-and-vale-college_aircraft.csv` | Cardiff and Vale College Aerospace Centre | 3 | 3 |
| `carew-cheriton-control-tower_aircraft.csv` | Carew Cheriton Control Tower | 1 | 1 |
| `coleg-cambria-connahs-quay_aircraft.csv` | Coleg Cambria Connah's Quay | 2 | 2 |
| `cornwall-at-war-museum-davidstow_aircraft.csv` | Cornwall At War Museum, Davidstow | 7 | 7 |
| `cotswold-airport-kemble_aircraft.csv` | Cotswold Airport Aircraft Collection, Kemble | 7 | 7 |
| `cowbridge-paintball_aircraft.csv` | Cowbridge Paintball | 1 | 1 |
| `cromhall-quarry-dive-site_aircraft.csv` | Cromhall Quarry Dive Site | 1 | 1 |
| `draken-gate-guard-llangeinor_aircraft.csv` | Draken Gate Guard, Llangeinor | 1 | 1 |
| `gazelle-gate-guardian-taunton_aircraft.csv` | Gazelle Gate Guardian, Taunton | 1 | 1 |
| `gazelle-za804-amesbury_aircraft.csv` | Gazelle HT.3 ZA804, Amesbury | 1 | 1 |
| `hamburger-hill-paintball-marksbury_aircraft.csv` | Hamburger Hill Paintball, Marksbury | 3 | 3 |
| `hawarden-airport-preserved-aircraft_aircraft.csv` | Hawarden Airport Preserved Aircraft | 5 | 5 |
| `helicopter-museum_topup_aircraft.csv` | The Helicopter Museum | 108 | 106 |
| `historic-helicopters-chard_aircraft.csv` | Historic Helicopters, Chard | 9 | 9 |
| `hunter-wt744-braunton_aircraft.csv` | Hunter GA.11 WT744, Braunton | 1 | 1 |
| `jet-age-museum_aircraft.csv` | Jet Age Museum | 15 | 12 |
| `jet-provost-gate-guard-felton_aircraft.csv` | Jet Provost Gate Guard, Felton | 1 | 1 |
| `jet-provost-xm358-newbridge-on-wye_aircraft.csv` | Jet Provost XM358, Newmead Farm Newbridge on Wye | 1 | 1 |
| `leonardo-helicopters-yeovil-gate-guardian_aircraft.csv` | Leonardo Helicopters Yeovil Gate Guardian | 1 | 1 |
| `lightning-xp745-vanguard-bristol_aircraft.csv` | Lightning F.3 XP745, Vanguard Self Storage Bristol | 1 | 1 |
| `lightning-xs936-castle-motors-liskeard_aircraft.csv` | Lightning F.6 XS936, Castle Motors Liskeard | 1 | 1 |
| `lynx-xz250-portland-marina_aircraft.csv` | Lynx HAS.3 XZ250, Portland Marina | 1 | 1 |
| `melksham-squadron-atc_aircraft.csv` | Melksham Squadron Air Training Corps | 1 | 1 |
| `meteor-wl345-middlezoy_aircraft.csv` | Meteor T.7 WL345, Middlezoy Aerodrome | 1 | 1 |
| `mod-boscombe-down-lightning-gate-guardian_aircraft.csv` | MoD Boscombe Down Lightning Gate Guardian | 1 | 1 |
| `mod-sealand-tornado-gate-guardian_aircraft.csv` | MoD Sealand Tornado Gate Guardian | 1 | 1 |
| `national-diving-activity-centre-tidenham_aircraft.csv` | National Diving and Activity Centre, Tidenham | 3 | 3 |
| `on-target-outdoor-paintball-trebudannon_aircraft.csv` | On Target Outdoor Paintball, Trebudannon | 1 | 1 |
| `outpost-paintball-higher-kinnerton_aircraft.csv` | Outpost Paintball Chester, Higher Kinnerton | 1 | 1 |
| `radyr-paintball_aircraft.csv` | Radyr Paintball, Tyla-morris Farm | 1 | 1 |
| `raf-st-mawgan-sea-king-gate-guardian_aircraft.csv` | RAF St Mawgan Sea King Gate Guardian | 1 | 1 |
| `raf-valley-gate-guardian_aircraft.csv` | RAF Valley Gate Guardian | 1 | 1 |
| `reme-museum-lyneham_aircraft.csv` | REME Museum, Lyneham | 3 | 3 |
| `sea-harrier-xz494-wedmore_aircraft.csv` | Sea Harrier XZ494, Castle Farm Campsite Wedmore | 1 | 1 |
| `south-wales-aviation-museum_aircraft.csv` | South Wales Aviation Museum | 77 | 77 |
| `tacla-taid-anglesey-transport-museum_aircraft.csv` | Tacla Taid Anglesey Transport Museum | 1 | 1 |
| `the-tank-museum-bovington_aircraft.csv` | The Tank Museum, Bovington | 2 | 2 |
| `thornbury-paintball_aircraft.csv` | Thornbury Paintball | 1 | 1 |
| `vampire-wz450-vanguard-bath_aircraft.csv` | Vampire T.11 WZ450, Vanguard Self Storage Bath | 1 | 1 |
| `vobster-quay-inland-diving-centre_aircraft.csv` | Vobster Quay Inland Diving Centre | 1 | 1 |
| `welsh-spitfire-museum-haverfordwest_aircraft.csv` | Welsh Spitfire Museum, Haverfordwest | 1 | 1 |
| `yeovil-college_aircraft.csv` | Yeovil College | 1 | 1 |
| **total** | **55 sites** | **382** | **371 (97%)** |

`uk_museums.csv` carries **54 sites** (36 in England, 18 in Wales).
`helicopter-museum_topup_aircraft.csv` is NOT one of them — it targets the
existing database record `The Helicopter Museum` and lists 108 airframes,
every one except the Bell UH-1H 66-16579 already recorded.

Serial coverage overall: **371 of 382 rows (97%)** carry a tail number.

---

## Leads for other agents

- **RAF Museum Cosford / Midlands:** Javelin FAW.4 **XA634** is at the Midland
  Air Museum, not Jet Age as Wikipedia's Jet Age article says.
- **Hampshire agent:** Museum of Army Flying (Middle Wallop) is not in this
  area. Saunders-Roe Skeeter **XM564** is held in store by The Tank Museum,
  Bovington (Dorset) and is recorded here, not at Middle Wallop.
- **Surrey/Sussex agent:** Sea Harrier ZD610 came from Dunsfold Park via
  Bruntingthorpe to Aerospace Bristol in 2015 — Dunsfold's list should not
  still carry it.
- **Leicestershire agent:** Bruntingthorpe no longer holds ZD610 (see above).
- **Merseyside/Cheshire agent:** Chipmunk **WB584** is now a PAX airframe at
  Hooton Park, and Sea Hawk **XE339**'s fuselage is stored there — both are
  filed in Gloucestershire by EuroDemobbed but physically in Cheshire.
- **Whoever takes RNAS Yeovilton:** EuroDemobbed splits Yeovilton into three
  locations — 2520 (station, 31), 8464 (museum, 45) and 8465 (museum store,
  42) — 118 airframes in total. It also lists RNAS Culdrose as location 1348
  with 8 airframes, several of them School of Flight Deck Operations hulks.
- **Wiltshire, if anyone revisits it:** the Air Cadet Grob Viking/Vigilant
  fleet is scattered in storage across Little Rissington (23), an unspecified
  "Wiltshire area" location (16) and St Athan (8). These are stored, not
  displayed, and only the St Athan ones are recorded here (they are inside the
  South Wales Aviation Museum compound).
- **General:** the old `demobbed.org.uk` domain now only serves images; the
  live database is `eurodemobbed.org.uk`. Its location pages carry
  airframe-level latitude/longitude in the header block, which is by far the
  fastest way to fill coordinates for UK gate guards and monuments.
