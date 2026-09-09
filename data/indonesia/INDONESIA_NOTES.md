# Indonesia — research notes

Output: `/home/claude/seasia/indonesia/`
`id_museums.csv` (63 sites) + 62 `<site_slug>_aircraft.csv` files (155 airframes).

Sweep covered Java (DKI Jakarta, Jawa Barat, Jawa Tengah, DI Yogyakarta, Jawa Timur, Banten
searched but nothing found), Sumatra (Aceh, Sumatera Barat, Riau, Sumatera Selatan, Lampung,
Bangka Belitung), Sulawesi (Selatan, Tenggara, Tengah), Kalimantan (Barat, Selatan), Bali,
Papua. Java is where almost everything is; the outer islands are essentially a Skyhawk-and-
MiG-17 monument map.

---

## 1. Sources used, and how they behaved

**Authoritative / primary**

- `museumdirgantaramandala.id` — the air force museum's own site. Has a "Koleksi Pesawat"
  section but it is a *narrative* page, not an inventory: it names about 13 types and gives
  exactly one serial (Cureng TJ-62, which is contradicted below). Useless as a checklist.
- `tni-au.mil.id`, `tni.mil.id`, `koopsud1.tni-au.mil.id`, `lanud-*.tni-au.mil.id`,
  `aau.ac.id` — the TNI-AU newsroom is the single most productive source for *monuments*:
  it reports every monument unveiling and every "karya bakti" cleaning detail, which is also
  the best currency evidence available (a 2025 cleaning report proves the airframe is still
  there). **It very rarely publishes serials.** Roughly two thirds of the monument records
  here have a confirmed type, location and date but no serial, because the TNI-AU release
  did not carry one. Those `tail_number` fields are deliberately blank.
- Local government sites (`malangkota.go.id`, `sumenepkab.go.id`, `subang.go.id`,
  `disporapar.malangkota.go.id`, `portal.tasikmalayakota.go.id`, `uns.ac.id`,
  `setda.bogorkab.go.id`, `disparekraf.bogorkab.go.id`) — reliable on location and date,
  never on serials.

**Enthusiast / survey**

- `aviationmuseum.eu` — carries a serial-by-serial survey list of Museum Pusat TNI AU
  Dirgantara Mandala. This is the only detailed serial list for that museum anywhere and it
  is clearly walk-round derived (it includes obscure items like the Grunau Baby, the Star-Lite
  PK-SLX and *two* Lim-5P airframes). Used as the primary serial authority for that museum.
- `aviahistoria.com` ("Aviation History of Indonesia") — the single best Indonesian source
  found. One article per preserved airframe, with photographs, serial and provenance. It
  supplied essentially the whole Satriamandala inventory, and corrected two serials. Its
  "museum" category is only ~22 posts, so its coverage is deep but narrow.
- `pacificwrecks.com` — good on the Japanese and WWII-era airframes at the air force museum
  and on their Babo/Biak recovery provenance. Source of the P-51 correction below.

**Compilations (leads only, treated as one source where they share ancestry)**

- `id.wikipedia.org` — `Museum Pusat TNI AU Dirgantara Mandala`, `Daftar monumen A-4 Skyhawk`,
  `A-4 Skyhawk dalam TNI Angkatan Udara`, `Museum Satria Mandala`, `Museum Loka Jala Crana`.
  Error-prone on serials (see §2) and, in the case of `Daftar monumen A-4 Skyhawk`, the
  **current article is a truncated remnant**: it now lists only four Indonesian airframes.
- `p2k.stekom.ac.id` — a mirror of Indonesian Wikipedia. It preserves an **older and much
  fuller** version of `Daftar monumen A-4 Skyhawk` (18 Indonesian entries against the live
  article's 4). Treated as the *same source* as id.wikipedia for independence purposes, but
  used as the lead list for the Skyhawk diaspora because the live article has lost the data.
  Every serial taken only from that mirror is flagged in its row `description`.
- `detik.com` (`8 Pesawat "Terparkir" di Jatim`), `jelajah-nesia.blogspot.com`
  (`Monumen Pesawat Legendaris Di Jawa Timur`), `travelingyuk.com`,
  `finnsbeachclub.com` — listicles, useful purely for discovering sites. Each one was
  re-checked against a second source before a site was created; two were dropped (§5).
- `aerialvisuals.ca` — **unusable for Indonesia.** The country browse URL returns a PHP fatal
  error and no Indonesian airframes could be pulled from it. Not used.
- Grokipedia was not used.

**Search language.** English coverage is near-worthless here. Everything productive came from
Indonesian queries: `monumen pesawat`, `museum dirgantara`, `koleksi pesawat`, `tugu pesawat`,
`lanud`, `monumen pesawat + <province>`, `pesawat dijadikan monumen`.

---

## 2. Corrections made, with evidence

1. **P-51D at the air force museum, Yogyakarta.** Recorded as `F-361`, not `F-338`.
   Pacific Wrecks states plainly: airframe F-361, "Displayed as F-338". id.wikipedia lists
   it as "P-338" (also a mangled prefix — the AURI Mustang prefix is `F-`, not `P-`).
   `tail_number = F-361`; `F-338`, `F338`, `P-338` are in `aliases`; the split is explained
   in `description`. This is exactly the painted-markings-are-not-identity trap.

2. **A-4E at the air force museum.** Recorded as `TT-0407`. Two independent sources give
   TT-0407 (the aviationmuseum.eu survey; the id.wikipedia article *A-4 Skyhawk dalam TNI
   Angkatan Udara*). The id.wikipedia *museum* article and the p2k mirror of the monument
   list both say TT-0440. Went with TT-0407, noted the conflict in the row.

3. **TA-4J `TL-0419`, Tebet, Jakarta.** The p2k mirror lists this airframe as
   "TT-0419, TA-4I, Lanud Pekanbaru". aviahistoria.com has a dedicated 2025 article with
   photographs placing `TL-0419`, a TA-4J, at the Monumen Swa Bhuana Paksa opposite Tebet
   Eco Park, Jakarta, unveiled 2023 — and explains the provenance (ex-US Navy stock bought
   1999, SDLM by Safe Air Ltd in New Zealand, Skadron Udara 11). The dedicated article wins.
   Both the letter prefix (`TL-` for the 1999 batch, not `TT-`) and the location were wrong
   in the compilation. No Skyhawk is recorded at Lanud Pekanbaru as a result.

4. **Cureng TJ-62.** The museum's own website in Yogyakarta captions its Cureng "TJ-62";
   so does aviahistoria.com for the Satriamandala aircraft. aviahistoria explains why: the
   two museums **swapped** their Cureng replicas — Jakarta's damaged example went to
   Yogyakarta for restoration and Yogyakarta's better one stayed in Jakarta. Since an
   airframe can only be in one place, `TJ-62` is assigned to Satriamandala (the source that
   actually documents the swap) and the Yogyakarta Cureng is recorded with a blank
   `tail_number`. Both are replicas — the originals were destroyed in the Dutch military
   actions of 1947-49 — and both rows say so.

5. **Fokker F.27 at the air force museum:** `A-2707` (aviationmuseum.eu survey) rather than
   id.wikipedia's `T-2707`. Same airframe; prefix disputed; noted in the row.

6. **PBY-5A Catalina:** `PB-505` (survey) rather than id.wikipedia's `PB-501`. Pacific Wrecks
   adds the provenance — ex-BuNo 46539, obtained from Bruce Fenstermaker in 1991 in exchange
   for a Babo salvage permit — which is in the description.

7. **F-86 Sabre TS-8609.** detik.com places it on the Blitar alun-alun; the TNI-AU release
   places it at Museum PETA, "east of the Soeprijadi statue", unveiled 31 December 2022.
   Recorded at Museum PETA (official source, and it names the exact spot).

8. **A-4 `TT-0431`.** Recorded at Lanud Iswahjudi per the id.wikipedia A-4-in-service article.
   The p2k mirror of the monument list puts TT-0431 at the air force hospital dr. Dody
   Sardjoto in Makassar. Rather than duplicate the airframe, TT-0431 is at Iswahjudi and the
   Makassar hospital row has a **blank** tail number with the conflict written into it.

9. **Museum Angkut's "presidential Boeing 737-200"** is a purpose-built walk-through
   mock-up, not an airframe. Recorded, flagged as a mock-up in `description`, not silently
   as real. The Bell 47 "Si Walet" at the same museum *is* a real 1958 helicopter (gift to
   Sukarno, 1960).

10. **Talang Betutu MiG-19, Palembang** rests on a single 2008 local-history blog and has
    not been re-confirmed since. It is in the CSV, but the row says currency is uncertain.
    Same treatment for the Gedung Juang Sabre in Pekanbaru: a 2020 news item said the Riau
    provincial government had been asked to move it *again*, into the Lanud Roesmin Nurjadin
    compound, and I could not confirm whether that happened.

---

## 3. Judgment calls

**Replicas and mock-ups**, all flagged in `description`, never as real:
Cureng K5Y1 (both museums), Wiweko WEL-1 "RI-X", Dakota "RI-001 Seulawah" at Blang Padang,
Boeing 737-200 presidential mock-up at Museum Angkut, and the Ilyushin Il-28 at Sawotratap,
Sidoarjo — Kompas reported in November 2024 that this "monument" was being *fabricated* in
Sidoarjo, i.e. it is a newly built replica, not an ex-AURI Beagle.

**Composite / stand-in identity.** Two airframes are displayed as something they are not:
- The Dakota at the air force museum wears `VT-CLA`, the Indian-registered Dakota shot down
  over Ngoto on 29 July 1947 killing Adisutjipto, Abdulrachman Saleh and Adisumarmo. The
  original's wreck site is at Ngoto; the displayed aircraft is a stand-in. `tail_number`
  blank, `VT-CLA` in aliases.
- The "Seulawah" at Satriamandala is an ex-Garuda DC-3 registered `PK-GDZ` standing in for
  RI-001, which has disappeared. `tail_number = PK-GDZ`, `RI-001` in aliases.

**The Stearman PT-13D at the air force museum** wears "TAL-OA", which is not a TNI-AU serial
(it is probably an airline/owner marking from its American life — Pacific Wrecks records it
as acquired from the Mid-Atlantic Air Museum in 1991). `tail_number` blank, marking in aliases.

**The Gannets.** Two ex-ALRI Fairey Gannets survive, one at Satriamandala in Jakarta and one
at Loka Jala Crana in Surabaya. The Jakarta aircraft is captioned "AS 00", which reads as a
display marking rather than a serial, so both rows have blank tail numbers and the aliases
carry the marking. They are recorded as two distinct airframes, one per site.

**access_type reasoning** (judged by how a member of the public actually gets in, not who
owns the land):
- `public` — walk-up or normal ticketed: the air force museum in Yogyakarta (a military
  museum, but sold as a tourist attraction with its own ticketing), Satriamandala, Museum
  Transportasi TMII, Museum Angkut, Museum PETA, and **every roadside/park/town-square
  monument**, including the Taman Dirgantara at Lanud Supadio — the TNI-AU explicitly opened
  it as a public open space ("Supadio Weekend Happiness", 2025) and that is how visitors get in.
- `appointment` — Loka Jala Crana (inside the naval academy at Bumimoro; visits are arranged,
  usually as groups) and the Unsurya campus display.
- `restricted` — anything behind a working military gate with no public route: Lanud Halim,
  Iswahjudi, Abdulrachman Saleh, Sultan Iskandar Muda, Bun Yamin, Hanandjoeddin, Sultan
  Hasanuddin, Roesmin Nurjadin, Palu, Makopsau II, the AAU campus, the Kalijati museum
  (inside Lanud Suryadarma — it is a real museum but you do not walk up to it), Depohar 30,
  the air force hospital at Makassar, and Pusdiklat Migas Cepu (an industrial training
  campus). Bali's Nyang Nyang villa 737 and the Ngurah Rai bypass 737 are marked `restricted`
  because both sit on fenced private land — visible, but not enterable.

**Bali abandoned airframes.** Four are recorded (Nyang Nyang clifftop villa 737, the Ngurah
Rai bypass 737, the DC-10 on the G88 Kerobokan roofline, the ex-Batavia Air 737-200 PK-YTW
outside Krisna Funtasticland at Lovina). These are commercial/decorative installations rather
than museum pieces, but the spec explicitly wants resorts and restaurants with a real
airframe, and all four are permanently sited and publicly known. A fifth reported airframe —
a 737 in a field in Jembrana, West Bali — and a "Lion Air fuselage" whose whereabouts the
source itself says nobody knows, were **not** recorded (§5).

**Wreck-derived monuments are records.** The F-16A `TS-1643` at Lanud Roesmin Nurjadin is the
rebuilt remains of the aircraft destroyed by fire on take-off at Halim in April 2015; the
Hawk 200 at Aneuk Galong was struck off charge after airframe cracking near Pekanbaru. Both
are `on_display` with the circumstances in `description`.

**Operational aircraft excluded.** Nothing in these files is a flying airframe. Aircraft seen
at open-base events (F-16s and Hawks at the Lanud Roesmin Nurjadin open base, the 22
helicopters at Penerbad Expo 2025 in Semarang) are in-service aircraft and were excluded.

---

## 4. Fields left deliberately blank, and why

- **`tail_number` on ~60 % of monument rows.** The TNI-AU and local-government announcements
  that document these monuments essentially never publish the serial. Guessing from the type
  and the known TNI-AU block (`A-` fighter, `M-` bomber, `T-` transport, `H-` helicopter,
  `TS-`/`TT-`/`TL-`/`LM-`/`LD-`/`LK-` trainers and later fighters) would have been easy and
  wrong. Left blank.
- **`year_built` on all but four rows.** Indonesian sources quote *service* years constantly
  ("served 1973-1981", "1960-1969") and construction years almost never. A serial was never
  converted into a year. The four populated are: N-250 PK-XNG (1995, first flight, well
  documented), Bell 47 "Si Walet" (1958, stated by the museum), Nomad P-806 (1974, stated),
  Nomad P-830 (1982, stated).
- **`postal_code`** on all but three sites — Indonesian sources almost never give one for a
  monument or a base.
- **`website`** on all monument rows — they have none.
- **Serials for the Kalijati museum's 21 aircraft.** indonesia.travel names five types
  (Piper J-3 Cub, Grumman G-21 Goose, Lockheed Lodestar, PZL Gelatik, Cessna 172) plus the
  A-4E; no serial for any of them, and no published inventory exists. Five type-only rows
  plus the Skyhawk are recorded; the remaining ~15 aircraft are undocumented (§6).

**Coordinates.** Only one is properly sourced: the air force museum at Yogyakarta,
`-7.7900, 110.4156`, from the coordinates on the English Wikipedia article
(7°47′24″S 110°24′56″E). **Every other coordinate in `id_museums.csv` is an approximate
position for the named landmark, town or air base, not a surveyed airframe position**, and
should be treated as accurate to roughly a few hundred metres up to a couple of kilometres
for the vaguer entries (Tulang Bawang, Gadut, Aneuk Galong, Palu, Sengkang, Talang Betutu,
Kendari, and the two Bali private-land 737s are the weakest). They are given to 4 decimals
because the schema asks for 4 decimals, not because they are surveyed to 4 decimals. Anyone
importing should re-pin these from satellite imagery before treating them as authoritative.

---

## 5. Excluded — do not re-research

- **Parung aircraft boneyard, Kampung Jampang, Kemang, Bogor.** Real and well documented by
  aviahistoria.com (2022): ex-Sriwijaya 737-800s PK-CMI/PK-CMT/PK-CMK, Lion 737-400 PK-LIT,
  Sky Angkor A320 XU-706, Aviastar BAe 146 PK-BRI, Cessna 172 PK-NIR, an F28 and an NC-212,
  on a 1-ha site leased 2019-2024. **Excluded because it is a scrapping/parting-out yard, not
  a display**, and the lease reportedly ran out in 2024, so the inventory is almost certainly
  gone. If the DB ever wants boneyards, this is the record to build from.
- **Bukit Pelangi "Monumen Pesawat Terbang", Sangatta, Kutai Timur.** Only evidence is an
  Instagram place tag. No type, no news coverage, no confirmation it exists. Not recorded.
- **Derelict airliner, Jl. Candi Penataran, Manyaran, Semarang.** One listicle mention, no
  type, no registration, no date. Not recorded.
- **Lanud Silas Papare, Jayapura.** Antara reported in 2024 that the base was *building* a
  monument showing the TNI-AU's role in Papua; nothing confirms an airframe was installed or
  which type. Not recorded — this is the biggest single gap (§6).
- **Ex-Phuket Air airliner, Waru, Sidoarjo.** detikJatim lists it, but it is an abandoned
  hulk on a former soda-factory site with no type, no registration and no display intent.
  Not recorded.
- **737 in a field in Jembrana, West Bali**, and the **"Lion Air fuselage"** whose location
  the source itself says is unknown. Not recorded.
- **Museum Rumah Sejarah Kalijati, Subang.** The Dutch-surrender house museum. It is a
  separate registered museum from the Amerta Dirgantara Mandala aircraft museum on the same
  base, and it has **no aircraft**. Recorded neither as a duplicate nor as a site.
- **Monumen Perjuangan TNI AU / Museum Monumen Ngoto, Bantul.** Commemorates the VT-CLA
  shoot-down of 29 July 1947. No airframe on site — the Dakota that represents VT-CLA is at
  the air force museum. Not a site record.
- **Monumen Jogja Kembali, Monumen Pancasila Sakti, Patung Dirgantara (Pancoran).** Sculpture
  monuments with no airframe.
- **Open-base and expo aircraft** (Lanud Roesmin Nurjadin open base; Penerbad Expo 2025,
  Semarang) — in-service aircraft, not displays.

---

## 6. Open questions, ranked

1. **Museum Amerta Dirgantara Mandala, Lanud Suryadarma, Kalijati (Subang).** The Association
   of Indonesian Museums says it holds **21 aircraft**; I could document 6. This is the
   largest single hole in the Indonesian dataset — a 1917 Dutch hangar full of unlisted
   airframes including a Grumman Goose and a Lockheed Lodestar, both rare. **One phone call
   closes it.** The museum is run by the Penerangan (information) unit of Lanud Suryadarma;
   contact via Lanud R. Suryadarma, Kalijati, Subang 41271, or through the Dinas Penerangan
   TNI AU (Dispenau) at Mabesau, Cilangkap, Jakarta. Ask for the *daftar koleksi pesawat*
   with registrasi.
2. **Serials for the whole monument population.** Roughly 40 airframes here have a confirmed
   type and place but no serial. **Dispenau is again the single contact that would close
   dozens at once** — every one of these monuments was handed over by the TNI-AU and the
   handover documents carry the serial. `pen@tni-au.mil.id` / Dinas Penerangan Angkatan Udara,
   Mabes TNI AU Cilangkap, Jakarta Timur.
3. **Museum Pusat TNI AU Dirgantara Mandala — reconciling the two serial lists.** The
   aviationmuseum.eu survey and id.wikipedia disagree on at least seven airframes
   (Catalina, F.27, HU-16 variant, Bell 204B, Super Puma, Cessna 401/402, A-4). One walk-round
   with a camera settles all of them. Museum contact: +62 877-1029-7780,
   museumdirgantaramandala@gmail.com.
4. **Does the museum have one Ki-79 or two?** Pacific Wrecks says the Mansyu Ki-79 moved from
   Satriamandala to Yogyakarta; aviahistoria photographed a Ki-79 marked "01" at Satriamandala
   in 2022; id.wikipedia lists a Ki-79 replica at Yogyakarta. Recorded once, at Satriamandala.
   If there are in fact two, the Yogyakarta one is missing from these files.
5. **The A-4 Skyhawk diaspora.** 32 airframes were dispersed from Skadron Udara 11 Makassar;
   19 are placed here. malangkota.go.id also named Aceh, Kendari, Cepu, Kalijati, Lampung,
   Majalengka, Sengkang, Iswahjudi and Depohar 30 (all captured) but also "kota-kota besar
   lainnya". At least a dozen Skyhawk monuments are unlocated. A restored
   `Daftar monumen A-4 Skyhawk` on id.wikipedia would fix most of this — the data existed and
   has been deleted from the live article; it survives only in the p2k mirror.
6. **Papua and Maluku are effectively empty.** Nothing confirmed at Jayapura, Biak, Merauke,
   Timika or Ambon. Biak in particular is a former WWII field with a large wreck population
   and a real chance of preserved airframes.
7. **Sumatra north and west.** No monument confirmed at Lanud Soewondo (Medan), Lanud Maimun
   Saleh (Sabang), Padang, Jambi, Bengkulu or Natuna. The Aceh Hawk 200 and the Palembang
   Sabre suggest the pattern exists; the reporting does not.
8. **Museum Transportasi TMII** has an "Anjungan Udara" pavilion; only the DC-9 PK-GNT and the
   NBo-105 HR-1525 could be identified. kemenhub.go.id also describes a "Touver TG 24"
   trainer, New Zealand-built 1969, used at PLP Curug from 1971 — almost certainly a garbled
   **AESL/Victa Airtourer**, but that identification is a guess and no row was written for it.
   The museum reopened after a revitalisation and its current inventory is undocumented online.
9. **Museum Loka Jala Crana, Surabaya.** Only the Gannet is confirmed. Indonesian sources say
   "pesawat, helikopter" plural. Contact via Akademi TNI AL, Bumimoro, Surabaya.
10. **Monumen Pesawat TNI AL, Kendari** — confirmed by an Antara photo feature as a
    Skuadron Udara 800 maritime patrol aircraft donated to the city, but no type or serial is
    published. Given every other TNI-AL civic donation in this dataset is a GAF Nomad, it is
    very likely a Nomad — but that is inference, so the site is recorded **with no aircraft
    row**. Same for nothing else: it is the only site here without an aircraft file.
11. **The Fokker F.27 "Ampuh" at Halim (unveiled 29 May 2025)** and the **SA 330 Puma at
    Simpang Sentul, Bogor (July 2025)** are both very recent and both had their serials
    withheld in every release. Puspenerbal/Dispenau would have them.

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
