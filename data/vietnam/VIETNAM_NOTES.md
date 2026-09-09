# Vietnam — research notes for airplane.museum

Scope of this pass: 20 sites, 105 aircraft/missile records, swept north to south
(Hanoi → Hai Phong → Dien Bien/Quang Tri → Da Nang → Hue → Nha Trang → Ho Chi Minh City
→ Mekong Delta). Everything below is what a future researcher needs in order not to
repeat the same work or the same mistakes.

---

## 1. Administrative names — read this before touching `state_province`

Vietnam's province merger took effect **1 July 2025**: 63 provinces became 34, and the
district (`quận`/`huyện`) tier was abolished in favour of a two-tier province → ward/commune
structure. Every `state_province` and every address in `vn_museums.csv` uses the
**post-merger** names, verified against OpenStreetMap/Nominatim reverse data, which has
already been updated:

| Old | Now used here |
|---|---|
| Bình Phước (Đồng Xoài, Phước Long) | **Đồng Nai** |
| Bà Rịa–Vũng Tàu, Bình Dương | **Hồ Chí Minh** |
| Thừa Thiên Huế | **Huế** (centrally-governed city) |
| Quảng Trị + Quảng Bình | **Quảng Trị** |
| Quảng Nam + Đà Nẵng | **Đà Nẵng** |
| Hải Dương + Hải Phòng | **Hải Phòng** |
| Bến Tre, Trà Vinh + Vĩnh Long | **Vĩnh Long** |
| Ninh Thuận + Khánh Hòa | **Khánh Hòa** |

Ward names also changed. Examples that will not match older directories: the Air Force
Museum is now in **phường Phương Liệt, Hà Nội** (not "quận Thanh Xuân"); the Military
History Museum is in **phường Xuân Phương** (built as "Tây Mỗ/Đại Mỗ, quận Nam Từ Liêm");
the War Remnants Museum is in **phường Xuân Hòa** (not "Quận 3"); Ta Con is in
**xã Khe Sanh, Quảng Trị** (not "huyện Hướng Hóa"). Anyone re-checking these sites against
a pre-2025 guidebook will think they have moved. They have not.

Local-language names of the sites (English names are used in the CSV):

- Vietnam People's Air Force Museum — *Bảo tàng Phòng không – Không quân*
- Vietnam Military History Museum — *Bảo tàng Lịch sử Quân sự Việt Nam*
- B-52 Victory Museum — *Bảo tàng Chiến thắng B-52*
- Huu Tiep Lake B-52 Wreck Site — *Hồ Hữu Tiệp* ("hồ máy bay B-52")
- Vietnam Aviation Museum — *Bảo tàng Hàng không* (Cục Hàng không Việt Nam)
- Vietnam Naval Museum — *Bảo tàng Hải quân*
- Ta Con Airfield — *Di tích sân bay Tà Cơn* (Khe Sanh Combat Base)
- Military Zone 5 Museum — *Bảo tàng Quân khu 5*
- Hue History Museum — *Bảo tàng Lịch sử thành phố Huế* (ex *Bảo tàng Lịch sử Thừa Thiên Huế*)
- Air Force Officers' School Museum — *Bảo tàng Không quân Nha Trang / Trường Sĩ quan Không quân*
- Southern Air Force Museum — *Bảo tàng Không quân phía Nam* (older listings: "Tan Son Nhut Air Force Museum")
- War Remnants Museum — *Bảo tàng Chứng tích Chiến tranh*
- Ho Chi Minh City Museum — *Bảo tàng Thành phố Hồ Chí Minh* (Dinh Gia Long)
- Ho Chi Minh Campaign Museum — *Bảo tàng Chiến dịch Hồ Chí Minh*
- Independence Palace — *Dinh Độc Lập* / Reunification Palace
- Cu Chi Tunnels (Ben Duoc) — *Khu di tích lịch sử Địa đạo Củ Chi – Bến Dược*
- Vinh Long Provincial Museum — *Bảo tàng Vĩnh Long*
- Dong Nai Provincial Museum — *Bảo tàng Đồng Nai*
- Binh Phuoc Provincial Museum — *Bảo tàng tỉnh Bình Phước*
- Road 14 – Phuoc Long Campaign Museum — *Bảo tàng Chiến dịch Đường 14 – Phước Long*

---

## 2. The Military History Museum move — resolved

**The move is real and complete.** The new *Bảo tàng Lịch sử Quân sự Việt Nam* at
Km 6+500 Đại lộ Thăng Long, phường Xuân Phương, Hà Nội opened **1 November 2024**,
free until December 2024, ticketed at 40,000 VND from **12 April 2025**. Closed Mondays
and Fridays. 38.6 ha site, 64,000 m² main building, 45 m Victory Tower.

What went to the new site (confirmed):

- **MiG-21 4324** — national treasure, suspended on cables in the main lobby
- **MiG-21 5121** — national treasure (Phạm Tuân's B-52 kill, 27 Dec 1972)
- **T-54B 843** — national treasure (tank, not in the aircraft CSV)
- **MiG-17 2047**, **Su-22**, PT-76 "555", 85 mm and 57 mm guns on the left
  (Vietnamese equipment) side
- **A-37, F-5E, CH-47, C-130**, M48 Patton, M107 175 mm SP gun and captured armour
  on the right (French/US equipment) side
- An **An-26** and a **B-52 wreckage** display are also present

What happened to the old site: on **26 December 2024** the Ministry of National Defence
merged the entire premises of the old museum at **28A Điện Biên Phủ, phường Ba Đình**
into the **Imperial Citadel of Thăng Long (Hoàng thành Thăng Long)** heritage complex.
The old site therefore no longer exists as a museum and **no site record is created for it**.

**Open question (ranked #1 below):** the old site's 2,000 m² outdoor yard contained the
famous heaped monument of French and American aircraft wreckage. I could not establish
from any 2025–26 source whether that wreckage pile moved to Xuân Phương, was absorbed
into the Hoàng thành Thăng Long display, or was dispersed. No record was created for it
anywhere, deliberately — a guess would have put an airframe in two places.

---

## 3. Sources used, and how each failed

**Good, and used as primary evidence**

- **Wikimedia Commons / Flickr album by "kitmasterbloke" (Steve Knight), 2 April 2025** —
  the single best currency evidence for the Hanoi Air Force Museum. File names carry the
  numbers read off the airframes; EXIF/album geotag 20.999387, 105.829216 is the museum.
  Caveat: the timestamp and GPS are identical across the whole album (album-level metadata,
  not per-frame), so they establish *which museum* but not *which day each airframe was seen*.
- **oldjets.net "War Remnants museums IndoChina"** — a genuine January–February 2025 visit
  with dated captions. Failure mode: the author's own **section headings are wrong**. His
  first block is headed "Air Force Museum – Saigon" but its opening sentence describes the
  War Remnants Museum; the aircraft in it (MiG-21 4326, Mi-8, Mi-24A 7403, F-5 7579,
  U-17, A-37, UH-1) are the **Southern Air Force Museum** collection, corroborated
  independently by Vietnamese press. His later "War remnants museums – Saigon" block
  (CH-47 086, F-5 69170, A-37B 70-1285, A-1H 139674, U-17B 71-1448, UH-1H 69-15753) is the
  real War Remnants Museum. He also reuses the same C-130 identity (5-0532 / ex-56-476)
  for both Củ Chi and Khe Sanh, which cannot both be true.
- **Vietnamese press, April 2025** (Thanh Niên 02/04/2025, VnExpress "Nơi lưu giữ tiêm kích
  ném bom Tân Sơn Nhất") — photographed, numbered coverage of the Southern Air Force Museum.
- **vi.wikipedia.org** — the Zone 5 Military Museum article has by far the best sourced
  outdoor inventory of any Vietnamese museum article (per-item capture histories).
- **vtcnews.vn**, **media.qdnd.vn**, **hanoibylocals.com** — new Military History Museum
  outdoor inventory.
- **VnExpress "Những 'ngựa thồ' trưng bày ở sân bay Tà Cơn" (May 2026)** — the most recent
  survey of Ta Con; this is where the C-119 arrival is documented.
- **caa.gov.vn** (Civil Aviation Authority of Vietnam) — for the Aviation Museum at Gia Lâm.
- **OpenStreetMap / Nominatim** — coordinates and current ward names.

**Stale or actively contaminated — do not trust without a second source**

- **aviationmuseum.eu is contaminated across its Vietnamese pages.** The serial block
  `0475 / 5020 / 7579 / 2011 / 6058` appears verbatim on its **Hanoi Air Force Museum**,
  **Da Nang Air Base Museum** and (partly) **Tan Son Nhut** pages. Its "Vietnam Air Force
  Museum" blog page is a **union of its older Hanoi and Tan Son Nhut pages** — that is why
  0475, 4326, 7579 and 764 appear there. Its Da Nang page is demonstrably wrong: an actual
  2025 visit to the Zone 5 Museum found MiG-21 5114/5127, UH-1 69-15130, A-37 10793 and
  O-1 042 — no overlap at all with aviationmuseum's Da Nang list. **Its per-site Vietnamese
  serial lists should be treated as lead generation only.** Its Đồng Nai, Bình Phước,
  Nha Trang and Naval Museum lists do *not* overlap the contaminated block and were used,
  flagged as single-sourced.
- **en.wikipedia.org** museum articles list types but almost never serials, and the
  Vietnam Military History Museum article still describes the pre-move collection
  (UH-1H, A-1E, A-1H, T-34, M113) without saying which items went to Xuân Phương.
- **Grokipedia** appeared in search results for the Military History Museum. Not used.

---

## 4. Every correction made, with the evidence

1. **aviationmuseum.eu's Hanoi Air Force Museum list is a merge of two museums.**
   Corrected by splitting it: 0372 UH-1H, 0475 A-37B, 4326 MiG-21PF, 7403 Mi-24A,
   7812 Mi-8, 764 U-17B and 7579 F-5 belong to the **Southern Air Force Museum**
   (87 Thăng Long, HCMC), corroborated by two 2025 Vietnamese press pieces with photographs
   and by aviationmuseum's own older, separate "Tan Son Nhut AF Museum" page.
2. **MiG-21 4326 is in Ho Chi Minh City, not Hanoi.** The April 2025 Hanoi photo album
   contains only MiG-21s 5020 and "5121"; Thanh Niên and VnExpress both photograph 4326
   at the Southern Air Force Museum.
3. **Il-14 VN-C482 and An-2 670C are at the Vietnam Aviation Museum, Gia Lâm** (119 Nguyễn
   Sơn, phường Bồ Đề), per the Civil Aviation Authority's own pages. A 2012 Commons photo
   of C-482 is filed under "Aircraft at the Vietnamese Air Force Museum" — that appears to
   be a Commons mis-categorisation; the Aviation Museum opened on 15 January 2006, before
   the photo. Separately, oldjets attributes C-482 to the *Military History* Museum; that
   is a third attribution and is not followed. Il-14 VN-C482 was trucked to the National
   Exhibition Centre in **August 2025** for the "80 năm hành trình Độc lập – Tự do – Hạnh
   phúc" exhibition; that was a temporary loan and the record keeps it at Gia Lâm.
4. **Independence Palace's F-5E is not Nguyễn Thành Trung's aircraft.** The palace's own
   site (dinhdoclap.gov.vn) calls it a *hiện vật đồng dạng* — an equivalent example of the
   type he flew on 8 April 1975. Vietnamese TV coverage that calls it "the F-5E that bombed
   the palace" is wrong. `tail_number` blank; the visible 01638 is an alias.
5. **The A-37 that bombed Tân Sơn Nhất is claimed by two museums.** VnExpress (April 2025)
   places **A-37B 0475**, flown by Từ Đễ of the Quyết Thắng squadron, at the Southern Air
   Force Museum; VOV (2025) states an A-37 of the same squadron is at the Air Defence–Air
   Force Museum in Hanoi. The squadron used five captured A-37s, so both can be true.
   0475 is recorded in HCMC only; the Hanoi A-37 is recorded untailed.
6. **C-130 identity 5-0532 cannot serve both Củ Chi and Ta Con.** Ta Con's aircraft is
   marked **532** in 2026 reporting, so the displayed marking is recorded there as an alias;
   Củ Chi's C-130 is recorded with no number at all.
7. **The Ta Con C-119 is new.** It was moved from Đồng Nai to Ta Con in **early 2026** after
   a 4 billion VND restoration funded by Ho Chi Minh City, and is described as the only
   substantially complete C-119 left in Vietnam. Any Đồng Nai-province list that still shows
   a C-119 is now out of date.
8. **"5832" at the Military History Museum is a Su-22, not a MiG-21.** A February 2025
   through-the-fence report calls it a MiG-21; VPAF Su-22s are numbered in the 58xx block
   (the Hanoi Air Force Museum's two are 5821 and 5831), and the museum's own outdoor
   inventory lists a Su-22 and no second MiG-21 outdoors. Recorded as Su-22, number as alias.
9. **Bà Rịa–Vũng Tàu Museum has no aircraft** — checked its own exhibition description;
   all three floors are indoor galleries. Excluded (see §6).

---

## 5. Judgment calls

**Painted markings vs identity.** Vietnamese displays repaint freely, and the same number
turns up at two museums more than once. Where two sites are photographed wearing the same
number I left `tail_number` blank at the weaker-sourced site and put the number in `aliases`:

| Number | Sites claiming it | Resolution |
|---|---|---|
| **7579** (F-5) | Hanoi Air Force Museum (Commons photo 2/4/2025) and Southern Air Force Museum (two Vietnamese press pieces, 2025) | Tail recorded at HCMC; Hanoi's F-5 left untailed, alias 7579 |
| **764** (U-17) | Hanoi (Commons photo) and Southern AF Museum (aviationmuseum) | **Both** left untailed, alias 764 |
| **5121** (MiG-21) | Hanoi Air Force Museum (Commons photo, placard "shot down a B-52 27/12/72") and Vietnam Military History Museum (national treasure) | Tail recorded at the Military History Museum, whose claim rests on the 2012 national-treasure designation; the Air Force Museum aircraft left untailed with the marking as an alias |
| **2011 / 2047** (MiG-17) | 2047 is firmly the Military History Museum's; 2011 appears on both a MiG-17 and a Shenyang J-5 in compiled listings | Hanoi Air Force Museum MiG-17 left untailed |

**Wreckage counts as a record.** Per the spec, four wreck records are included and are
described as wreckage, not complete airframes: the B-52 in Huu Tiep lake (in situ, national
relic, restored 2021–22 and reopened December 2022), the B-52 remains at the B-52 Victory
Museum and at the Military History Museum, the F-4 forward fuselage and the O-1 and Ryan
Firebee remains at the Hanoi Air Force Museum, and the F-4 wreck at the Ho Chi Minh Campaign
Museum. The Củ Chi UH-1 is a hulk and is described as such.

**Composites and restorations flagged, not asserted as original.** Binh Phuoc's A-37B 71-822
was rebuilt to shape by the A42 aircraft repair plant after the original structure had
corroded away — parts of it are reconstruction. The War Remnants Museum's own signage notes
that several of its aircraft wear US Air Force markings although they were VNAF machines,
repainted for display; that is recorded in the CH-47 and F-5 descriptions.

**Missiles included, guns and radars not.** SA-2/S-75, AA-1 Alkali, AA-2 Atoll and the P-15
Termit are recorded as `missile_rocket`. The extensive radar park at the Hanoi Air Force
Museum (SNR-75 Fan Song, P-12, P-15, P-35, PRV-11, PC-7, RCP-7) and the anti-aircraft gun
lines (37 mm 61-K, 57 mm S-60, 100 mm KS-19, ZPU-1/2/4, 90 mm M2) have **no valid
`aircraft_type`** in the schema, so they are deliberately omitted rather than forced into
`other`. The same applies to tanks (T-54B 843, PT-76 555, M48, M41, M113), the BLU-82
Daisy Cutter at the War Remnants Museum and Zone 5, and the M107. If the schema later gains
a ground-equipment type, these are the sites to revisit first.

**`access_type` choices.**
- `restricted` — **Air Force Officers' School Museum, Nha Trang**: the aircraft park is
  inside the Trường Sĩ quan Không quân perimeter. Casual walk-up entry is not how a member
  of the public gets in.
- `appointment` — **Vietnam Aviation Museum, Gia Lâm**: the CAAV describes it as open to
  visitors, but it sits inside the Civil Aviation Authority compound at 119 Nguyễn Sơn and
  has no published public opening hours or ticket. Arrange ahead.
- everything else `public`, including the two military-run museums in Hanoi (the Air Force
  Museum charges 20,000 VND at a public gate; the B-52 Victory Museum is free) and Ta Con
  (40,000 VND adult / 20,000 child, daily 08:00–17:00).

**Deliberately blank fields.**
- `year_built` is blank on **every** row. Not one site publishes a construction, roll-out or
  delivery date, and every number available is a serial or a display number. No exceptions
  were manufactured from serial blocks.
- `variant` is blank where sources disagree: the Ho Chi Minh Campaign Museum F-5 (Vietnamese
  sources say F-5E, photographic listings say F-5A), the Hanoi Air Force Museum MiG-17,
  the B-52s (D vs G disputed at all three sites).
- `postal_code` is blank where Nominatim returned no code or returned an obvious
  non-postal value (the Zone 5 Museum's "02363" is a telephone area code and was discarded).
- `website` is blank for the military-run museums; the Air Force Museum's only public
  presence is a Facebook page, which is not a website.

**Coordinates.** Most are OSM/Nominatim point matches on the named museum, to 4 dp.
Four are weaker and should be tightened from satellite imagery before anyone maps an
individual airframe:
- **Hue History Museum** — street-level point on Điện Biên Phủ, phường Thuận Hóa, not a
  building match.
- **Binh Phuoc Provincial Museum** — Đồng Xoài ward centroid.
- **Road 14 – Phuoc Long Campaign Museum** — Phước Long ward centroid.
- **Vietnam People's Air Force Museum** — the CSV uses the OSM point for the museum entrance
  (20.9995, 105.8292); the April 2025 photo album geotag is 20.9994, 105.8292, i.e. the same
  spot, which is a useful cross-check that the museum has not moved off Bạch Mai airfield.

---

## 6. Excluded — do not re-research these

- **Vietnam Military History Museum, old site, 28A Điện Biên Phủ** — merged into Hoàng thành
  Thăng Long on 26 Dec 2024; no longer a museum. Task instruction was to record the current
  location only, and that is what was done.
- **Bà Rịa–Vũng Tàu Museum, 4 Trần Phú, Vũng Tàu** — 2,855 m² of purely indoor galleries
  across three floors; no outdoor hardware. Checked against the museum's own exhibition
  description.
- **Southern Women's Museum (Bảo tàng Phụ nữ Nam Bộ), HCMC** — appeared in the seed list.
  No evidence of any airframe found in any source consulted. Excluded, not confirmed absent.
- **Da Nang Museum (Bảo tàng Đà Nẵng)** — relocated to 42 Bạch Đằng and reopened in 2025.
  Its new home is a restored French-era administrative building on the riverfront with no
  outdoor hardware yard. The military hardware people remember in Đà Nẵng is at the
  **Zone 5 Museum**, which is a separate institution and is recorded. Excluded.
- **Vịnh Mốc tunnels and Quảng Trị Citadel** — no aircraft found; the aircraft in that
  province are at Ta Con.
- **Cambodian sites** in the oldjets source (Siem Reap War Museum, J-6 30-950, Mi-8 XU-814)
  — out of country scope, noted here so the next person recognises them.
- **Aviationmuseum.eu "National Vietnam War Museum"** — despite the name this is
  "The Bunker" in Orlando, Florida. Not a Vietnamese site.

---

## 7. Open questions, ranked

1. **What happened to the aircraft-wreckage monument at 28A Điện Biên Phủ?** The single
   biggest unresolved item. One visit or one email would settle whether the heaped French
   and American wreckage moved to Xuân Phương, stayed with the Hoàng thành Thăng Long
   complex, or was dispersed — and would also confirm whether the old site's UH-1H, A-1E
   and A-1H made the move (English Wikipedia still lists them without saying where they are).
   Contact: **Bảo tàng Lịch sử Quân sự Việt Nam**, Km 6+500 Đại lộ Thăng Long, phường
   Xuân Phương, Hà Nội — director Đại tá Lê Vũ Huy. The same contact would close #2, #3
   and #4 below.
2. **Confirm the Military History Museum's outdoor numbers.** No dated photograph with
   readable numbers was found for the new site's A-37, F-5E, CH-47, C-130, An-26 or Su-22.
   Four `tail_number` fields there are blank purely for lack of a photograph.
3. **Resolve the 7579 / 764 / 5121 duplications.** These need a photograph of the placard,
   not of the airframe. The Hanoi Air Force Museum (*Bảo tàng Phòng không – Không quân*,
   173C Trường Chinh, phường Phương Liệt, Hà Nội) and the **Bảo tàng Không quân phía Nam**,
   87 Thăng Long, phường Tân Sơn Nhất, HCMC (free entry, Tue–Thu + weekends) both hold the
   contested numbers; one visit to each closes three records.
4. **Does the Hanoi Air Force Museum still hold the Soyuz-37 descent capsule?** Older visitor
   accounts describe a space capsule associated with Phạm Tuân's 1980 flight. I could not
   date any sighting after 2015 and could not establish whether it is the flown descent
   module or a training article, so **no record was created**. If it is there, it is a
   `spacecraft` record and probably the most significant object in the museum after the MiGs.
5. **The Grumman F8F-1B "G1510" at Dong Nai Provincial Museum.** Single-sourced
   (aviationmuseum.eu, with a photograph). If real it is a first Indochina War survivor of
   real significance and the marking should be matchable to a US Navy BuNo or a French
   Armée de l'Air serial. Contact: **Bảo tàng Đồng Nai**, đường Nguyễn Ái Quốc, phường
   Tân Triều, Đồng Nai — Mon–Fri 07:30–11:00 / 13:00–17:00.
6. **Vinh Long's F-5 in Imperial Iranian Air Force markings.** Photographed January 2025.
   If those markings are original rather than a display fantasy, this airframe came from
   the pre-1975 IIAF transfer batch and should be identifiable in Iranian F-5 records.
   Contact: **Bảo tàng Vĩnh Long**, đường Hùng Vương, phường Long Châu, Vĩnh Long.
7. **Military-region and provincial museums not yet swept.** Bảo tàng Quân khu 1 (Thái
   Nguyên), Quân khu 2, Quân khu 3, Quân khu 4 (Vinh), Quân khu 7 (HCMC — administratively
   the parent of the Ho Chi Minh Campaign Museum), Quân khu 9 (Cần Thơ). Several of these
   are known to have outdoor hardware yards; none could be confirmed to hold an airframe
   within this pass. Quân khu 9 in particular sits in Ninh Kiều, Cần Thơ and is the obvious
   next target in the delta.
8. **Điện Biên Phủ.** The Bảo tàng Chiến thắng lịch sử Điện Biên Phủ (đường Võ Nguyên Giáp,
   phường Điện Biên Phủ, 21.3807, 103.0152) and the battlefield sites around Mường Thanh
   are known to hold French aircraft wreckage from 1954, but no specific airframe could be
   confirmed. **No site record was created.** This is the largest remaining geographic gap.
9. **Gate guards and plinth airframes.** This pass found no verifiable single-airframe
   monument outside a museum — no confirmed gate guard at Nội Bài, Tân Sơn Nhất, Biên Hòa,
   Phù Cát, Phan Rang or Đà Nẵng, and no confirmed roundabout or park MiG. Vietnam almost
   certainly has them (the Hàm Rồng bridge memorial in Thanh Hóa and the Học viện Phòng
   không – Không quân at Sơn Tây are the strongest leads). English- and Vietnamese-language
   web search for `tượng đài máy bay` and `máy bay trưng bày` returned museum coverage only.
   This is the weakest part of the pass and the clearest instruction for the next one:
   **the plinths are there, they are just not written up online.** Provincial newspaper
   photo galleries (báo tỉnh) are the likeliest source.
10. **Nội Bài / Tân Sơn Nhất preserved airliners.** Nothing found. Vietnam Airlines has no
    known preserved-airframe programme; the only civil airframes located are the Il-14 and
    An-2 at the Gia Lâm Aviation Museum.

---

## 8. Practical notes for a visit

- **Bảo tàng Phòng không – Không quân**, Hanoi: 20,000 VND, roughly 08:00–11:00 and
  13:00–16:00, closed Friday. 73 large outdoor objects on 15,000 m²; the indoor hall holds
  over 3,000 items and 62,000 catalogued artefacts.
- **Bảo tàng Lịch sử Quân sự Việt Nam**: 40,000 VND, closed Monday and Friday, 08:00–11:30
  and 13:00–16:30. Free for under-16s, over-80s, veterans and serving personnel.
- **B-52 Victory Museum**: free, Tue–Thu and weekends, 08:00–11:30 / 13:00–16:30.
- **Bảo tàng Không quân phía Nam**: free, weekdays 07:00–16:00; the indoor building is often
  locked without notice, the aircraft yard is not.
- **Ta Con**: 40,000 VND adult, 20,000 child, daily 08:00–17:00. Everything is outdoors and
  the airframes are corroding fast; photograph numbers now.
- **Zone 5 Museum, Đà Nẵng**: free for Vietnamese nationals, 60,000 VND for foreigners plus
  10,000 VND camera fee, closed Monday.

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
