# JAPAN — Museums and Major Institutional Collections (phase 1 of 2)

Japan had exactly ONE record in the database. This pass covers museums, memorial museums,
service public-relations museums, corporate archives, university/technical-college teaching
collections and the two JAXA public centres. Base gate guards, base perimeter displays and
free-standing monuments are deliberately EXCLUDED — a parallel agent is doing those.

`region` is the literal string `Asia` on every row (database enum override for this brief).

All research was done in Japanese. The two sources that carried this country are named in
NOTES; English-language coverage was used only as a cross-check and was repeatedly wrong.

## SITES

name: Gifu-Kakamigahara Air and Space Museum
city: Kakamigahara
state_province: Gifu
country: Japan
postal_code: 504-0924
region: Asia
address: 5-1 Shimogiri-cho / 岐阜県各務原市下切町5丁目1番地
website: https://www.sorahaku.net/
access_type: public
latitude: 35.388083
longitude: 136.862472
source: ja.wikipedia "岐阜かかみがはら航空宇宙博物館" (full 展示機種 list with per-airframe serials; coordinates from the article infobox; read 2026-09); 用廃機ハンターが行く！ (wrecks.hatenablog.com) site article and three-part display inventory last revised 2026; Gifu Prefecture PDF "岐阜県内の登録博物館・指定施設一覧" (令和7年10月1日現在); 横山晋太郎「航空機を後世に遺す」グランプリ出版 2018 cited throughout the wiki article for acquisition histories
confidence: high — the largest real-airframe collection in Japan (41 real airframes plus 15 full-scale models as of 2024); the ja.wikipedia list is unusually well sourced and carries a serial for nearly every airframe; a new annexe ("Space Box") opened 2024-10-12 and SLIM/SORA-Q replicas entered the permanent display 2026-02-21; most recent evidence 2026

name: Tokorozawa Aviation Museum
city: Tokorozawa
state_province: Saitama
country: Japan
postal_code: 359-0042
region: Asia
address: 1-13 Namiki / 所沢航空記念公園内
website: https://tam-web.jsf.or.jp/
access_type: public
latitude: 35.799037
longitude: 139.471806
source: ja.wikipedia "所沢航空発祥記念館"; 用廃機ハンターが行く！ site article revised 2025-12-12 (20th revision) which carries the serial of every indoor airframe and every stored airframe plus the closure notice; Saitama Prefecture procurement notice for the renewal basic-design commission
confidence: high on content and identity; MEDIUM on current access — the museum has been CLOSED for a major rebuild since 2025-09-01 and is scheduled to reopen end of March 2027. Several airframes (H-19C 40001; V-44A 50002; UH-1B 41547) were scheduled for scrapping as part of that work. The outdoor YS-11A at Kokukoen station and the C-46D in the park remain publicly visible throughout. Evidence dated 2025-12.

name: JASDF Hamamatsu Air Park
city: Hamamatsu
state_province: Shizuoka
country: Japan
postal_code: 432-8851
region: Asia
address: Nishiyama-cho muban-chi / 航空自衛隊浜松基地 浜松広報館（エアーパーク）
website: https://www.mod.go.jp/asdf/airpark/
access_type: public
latitude: 34.748639
longitude: 137.712083
source: ja.wikipedia "浜松広報館" (per-airframe serial list; infobox coordinates); 用廃機ハンターが行く！ two-part site article (outdoor / indoor) 2022-08-04 and the Zero feature article revised 2025-02 which documents the 2024 relocation of the A6M5a
confidence: high — the JASDF's own public museum; free-standing public building outside the flightline with its own car park so access is public not restricted; a 2021 refit ADDED two airframes and REMOVED eight, so pre-2021 lists are stale; the A6M5a moved from the hangar ceiling to the second floor of the adjacent 資料展示館 during 2024

name: Misawa Aviation and Science Museum
city: Misawa
state_province: Aomori
country: Japan
postal_code: 033-0022
region: Asia
address: 158 Kitayama Oaza-Misawa / 青森県三沢市大字三沢字北山158番地
website: https://www.kokukagaku.jp/
access_type: public
latitude: 40.708250
longitude: 141.390361
source: ja.wikipedia "青森県立三沢航空科学館"; 用廃機ハンターが行く！ site article (14th revision 2022-08-17) which supplies every outdoor serial and the provenance of the T-33A; Aomori Prefecture operating-report PDFs cited there
confidence: high — prefectural museum; the outdoor 三沢市大空ひろば park is free and separately accessible from the paid indoor hall; a 2020-21 refit removed the Tachikawa Ki-54 (to Tachihi Holdings) the S-51 and the A6M2 replica and added the HondaJet demonstrator; evidence 2022 with 2025 cross-checks

name: Yushukan -- Yasukuni Shrine
city: Chiyoda
state_province: Tokyo
country: Japan
postal_code: 102-8246
region: Asia
address: 3-1-1 Kudankita / 靖國神社 遊就館
website: https://www.yasukuni.or.jp/yusyukan/
access_type: public
latitude: 35.695100
longitude: 139.743700
source: 用廃機ハンターが行く！ "【東京都】靖國神社遊就館の展示機" revised 2024-12-31; ja.wikipedia "遊就館"; the same blog's nationwide Zero and non-Zero wartime-survivor feature articles (revised 2025-02 and 2026-04)
confidence: high — three internationally significant airframes; the entrance hall holding the A6M5 can be entered free of charge; the Suisei and Ohka are behind the JPY 1000 ticket. Note the Ki-115 Tsurugi named in the brief is NOT here — see NOTES.

name: Kawaguchiko Motor Museum and Fighter Plane Museum
city: Narusawa
state_province: Yamanashi
country: Japan
postal_code: 401-0320
region: Asia
address: Fuji-Sakura Kogen / 山梨県南都留郡鳴沢村富士桜高原内
website: http://www.car-airmuseum.com/
access_type: appointment
latitude: 35.453700
longitude: 138.741000
source: 用廃機ハンターが行く！ "【山梨県】河口湖自動車博物館・飛行舘" revised 2026-03-09 (7th revision) with per-airframe manufacturer serials and backyard inventory; the same author's Zero feature article; Jウイング誌 2021年8月号別冊「全国保存機・展示機ガイド2021」 which the same author wrote and later corrected
confidence: high on content — this is the private Harada collection and it opens to the public for ONE MONTH A YEAR (1-31 August), so access is recorded as `appointment`; opening dates hours and photography rules are re-announced each year and must be checked before travel; the display layout and which airframes are out of the backyard changes every season so any airframe list is a snapshot (this one is 2019-2021 with 2026 review)

name: Kure Maritime Museum -- Yamato Museum
city: Kure
state_province: Hiroshima
country: Japan
postal_code: 737-0029
region: Asia
address: 5-20 Takara-machi / 呉市海事歴史科学館
website: https://yamato-museum.com/
access_type: public
latitude: 34.241200
longitude: 132.555800
source: 用廃機ハンターが行く！ "【広島県】呉市海事歴史科学館「大和ミュージアム」のゼロ戦ほか" revised 2026-04-09 (4th revision); ja.wikipedia "大和ミュージアム"; Kure City press releases of 2026-01-27 and 2026-04-02 cited there
confidence: high and very current — the museum was CLOSED for renewal works until 2026-04-22 and REOPENED 2026-04-23. The Zuiun full-scale replica displayed alongside the works site 2026-01-27 to 2026-04-05 was dismantled 2026-04-08/09 and is in store; the Zero-observation-seaplane replica was at the temporary "Yamato Museum Satellite" which closed on reopening. Only the A6M6 is a confirmed permanent airframe.

name: Chiran Peace Museum for Kamikaze Pilots
city: Minamikyushu
state_province: Kagoshima
country: Japan
postal_code: 897-0302
region: Asia
address: 17881 Kori Chiran-cho / 知覧特攻平和会館
website: http://www.chiran-tokkou.jp/
access_type: public
latitude: 31.363600
longitude: 130.434300
source: 用廃機ハンターが行く！ "【鹿児島県】知覧特攻平和会館の展示機" revised 2026-04-29 (4th revision incl. a 2026-04-27 site visit); 知覧特攻平和会館文化財調査報告書(1) 「陸軍四式戦闘機「疾風（1446号機）」保存状態調査報告書 I」令和4年3月; the same blog's wartime-survivor feature
confidence: high — evidence includes an author visit in April 2026. The Ki-61 Hien named in older sources LEFT in 2015 and is now at Kakamigahara; the T-6G left in 2006. Most of the indoor hall is no-photography which is why serials are thin.

name: JMSDF Kanoya Air Base Museum
city: Kanoya
state_province: Kagoshima
country: Japan
postal_code: 893-0064
region: Asia
address: 3-11-2 Nishihara / 海上自衛隊鹿屋航空基地史料館
website: https://www.mod.go.jp/msdf/kanoya/toukatu/HPzairyou/1-8siryoukann/1-8siryoukann.html
access_type: public
latitude: 31.380833
longitude: 130.836917
source: 用廃機ハンターが行く！ "【鹿児島県】海自 鹿屋航空基地史料館" revised 2026-07-09 (7th revision incl. a 2026-04-25 visit) which supplies a serial for all 18 airframes; ja.wikipedia "鹿屋航空基地史料館" (coordinates postal code and type list); 「零戦、かく戦かえり！」零戦搭乗員会編 文春ネスコ 2004 pp.553-565 for the Zero restoration
confidence: high and current to April 2026. The display area sits OUTSIDE the main gate so access is public and free; several outdoor airframes are visible even when the hall is shut. Condition is deteriorating badly — the author expects typhoon/corrosion losses. A U-36A (9206) was ferried in after its 2025-03-10 retirement and shown in a hangar at the 2025 and 2026 air memorial events; it is expected to become an exhibit but that is NOT yet confirmed, so it is not recorded here.

name: Tachiarai Peace Memorial Museum
city: Chikuzen
state_province: Fukuoka
country: Japan
postal_code: 838-0814
region: Asia
address: 2561-1 Takata / 筑前町立大刀洗平和記念館
website: http://tachiarai-heiwa.jp/
access_type: public
latitude: 33.412300
longitude: 130.619600
source: 用廃機ハンターが行く！ "【福岡県】大刀洗平和記念館と駅前のT-33A" revised 2023-11-17 (7th revision); the same author's Zero feature (Mitsubishi c/n 3148 provenance); ja.wikipedia "筑前町立大刀洗平和記念館"
confidence: high — the only A6M3 Type 32 on display anywhere in Japan; photography of the Zero the Ki-27 and the Shinden was opened up in July 2022. The T-33A is across the road at the old Tachiarai station and is recorded here because the museum grew out of that building; it is visible 24/7.

name: Museum of Aeronautical Sciences -- Narita
city: Shibayama
state_province: Chiba
country: Japan
postal_code: 289-1608
region: Asia
address: 111-3 Iwayama Shibayama-machi Sanbu-gun
website: https://www.aeromuseum.or.jp/
access_type: public
latitude: 35.740300
longitude: 140.397800
source: 用廃機ハンターが行く！ "【千葉県】航空科学博物館" revised 2025-06-18 (7th revision) which lists all 19 outdoor airframes with registrations AND explicitly corrects three registrations that ja.wikipedia gets wrong; ja.wikipedia "航空科学博物館"
confidence: high — the ONLY aviation museum in Japan registered as a 登録博物館 under the Museum Act. Civil aircraft only; no military types. Three ja.wikipedia registrations (JA5073 JA3009 N25MB) are wrong and are corrected in the rows below — see NOTES.

name: Ishikawa Aviation Plaza
city: Komatsu
state_province: Ishikawa
country: Japan
postal_code: 923-0995
region: Asia
address: 92 Ataka-shinmachi Hei / 石川県小松市安宅新町丙92番地
website: https://www.pref.ishikawa.lg.jp/aviation/
access_type: public
latitude: 36.404444
longitude: 136.410611
source: 用廃機ハンターが行く！ "【石川県】石川県立航空プラザ" revised 2022-05-27 (5th revision) with a serial for every airframe; ja.wikipedia "石川県立航空プラザ"; Komatsu City machizukuri foundation facility page
confidence: high on the airframe list (2021-2022 evidence with 2026 cross-check); free admission; the only aviation museum on the Sea of Japan coast. The TH-55J (61324) was returned to the JGSDF and scrapped in March 2019 for asbestos and is NOT recorded. The ex-government B747 VIP cabin was announced as a display only to June 2022 and its current status is unconfirmed.

name: Aichi Museum of Flight
city: Toyoyama
state_province: Aichi
country: Japan
postal_code: 480-0202
region: Asia
address: Oaza Toyoba (inside Prefectural Nagoya Airport)
website: https://aichi-mof.com/
access_type: public
latitude: 35.247611
longitude: 136.924694
source: 用廃機ハンターが行く！ "【愛知県】あいち航空ミュージアム" revised 2026-03-05 (17th revision) with registrations and acquisition histories; ja.wikipedia "あいち航空ミュージアム"; Aichi Prefecture governor's press conference material 2025-02-05 and the FY2022 budget line for the T-4 installation
confidence: high on content; MEDIUM on current access — the museum is scheduled to be CLOSED from June 2026 to about January 2027 for the installation of Mitsubishi SpaceJet airframe 10, and the specialist source expects at least one MH2000 the EH-101 and possibly one or two light aircraft to be REMOVED in that refit. Anything recorded here should be re-verified after the reopening.

name: Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba
city: Chikusei
state_province: Ibaraki
country: Japan
postal_code: 308-0811
region: Asia
address: The Hirosawa City / ザ・ヒロサワ・シティ内「ユメノバ」
website: https://www.thehirosawacity.jp/
access_type: public
latitude: 36.292300
longitude: 140.018500
source: 用廃機ハンターが行く！ "【茨城県】筑西市 ザ・ヒロサワ・シティの"ユメノバ"" revised 2025-04-24 (16th revision) plus the 2025-04-25 short bulletin on the helicopter moves; National Museum of Nature and Science press releases 579133.pdf and 584358.pdf; the same blog's Zero and YS-11 features
confidence: high and current to April 2025 — this is where the National Museum of Nature and Science's aircraft collection actually went. It opened 2024-02-11 after repeated delays. Aircraft are spread over THREE buildings inside the park (Kahaku-Hirosawa Air Museum; Glider and Model Aircraft Hall; Cactus Garden greenhouse) and were re-shuffled in April 2025. Admission JPY 2500.

name: Mitsubishi Heavy Industries Oe Clock Tower Aviation Archive
city: Nagoya
state_province: Aichi
country: Japan
postal_code: 455-0024
region: Asia
address: 2-15 Oe-cho Minato-ku / 三菱重工業株式会社 大江工場旧事務本館
website: https://www.mhi.com/jp/expertise/museum/nagoya/index.html
access_type: appointment
latitude: 
longitude: 
source: 用廃機ハンターが行く！ "【愛知県】三菱重工 大江時計台航空史料室" revised 2025-10-12; the same author's Zero and wartime-survivor features
confidence: high — opened 2020-01-31 in the old Oe works headquarters after the Komaki-Minami works archive closed in May 2017. Free but ADVANCE ONLINE BOOKING IS COMPULSORY and visits run in fixed two-hour slots Wed/Thu/Fri 09:00-17:00; photography is banned everywhere except the entrance hall. Coordinates deliberately blank — no surveyed position found.

name: Kokukan boon
city: Toyoyama
state_province: Aichi
country: Japan
postal_code: 
region: Asia
address: 120-1 Aza-Shinmei Oaza-Aoyama / 神明公園内
website: https://www.town.toyoyama.lg.jp/
access_type: public
latitude: 
longitude: 
source: 用廃機ハンターが行く！ "【愛知県】豊山町 航空館boon" revised 2022-11-23 which reconstructs the whole registration history of JA8626 and documents a dating error on the town's own website
confidence: medium-high — small free municipal museum opened 2005-04-01 holding the residue of the old Nagoya Airport Aerospace Hall (closed 2004-10-31). Only three airframes. Evidence 2022.

name: Shidenkai Exhibition Hall
city: Ainan
state_province: Ehime
country: Japan
postal_code: 798-4110
region: Asia
address: 5688 Misho Hirajo / 南レク馬瀬山公園 紫電改展示館
website: 
access_type: public
latitude: 32.950200
longitude: 132.549300
source: 用廃機ハンターが行く！ "【愛媛県】紫電改展示館" revised 2025-01-13 (4th revision) and the companion post "紫電改展示館改装計画" 2023-06-14; Nankai Broadcasting web news 2023-06-13
confidence: medium — the airframe and the site are certain and admission is free; the ACCESS is the risk. Ehime Prefecture is replacing the building: construction was to start in FY2025 with completion and opening during FY2026 and the specialist source expects a closed period for the move that had not been scheduled as of January 2025. Verify before travel. Note the published address is inconsistent across sources — three variants circulate and one misprints 御荘 as 御苑.

name: Bansei Tokko Peace Museum
city: Minamisatsuma
state_province: Kagoshima
country: Japan
postal_code: 897-1123
region: Asia
address: 1955-3 Kaseda-Takahashi / 南さつま市立万世特攻平和祈念館
website: https://bansei-tokkou.jp/
access_type: public
latitude: 31.437300
longitude: 130.295400
source: 用廃機ハンターが行く！ "【鹿児島県】万世特攻平和祈念館の零式水上偵察機" 2022-10-10; ja.wikipedia "南さつま市立万世特攻平和祈念館"
confidence: high — one airframe; recovered 1992 and certified 重要航空遺産 by the Japan Aeronautic Association in 2011. Ground floor photography allowed; the second floor is not. The museum's claim to hold "the only surviving example" is not correct — see NOTES.

name: Mitsu Seiki -- Tsubasa no Hiroba
city: Awaji
state_province: Hyogo
country: Japan
postal_code: 656-1522
region: Asia
address: 301 Shimokawai / ミツ精機株式会社 本社・多賀工場
website: http://www.mitsu.co.jp/
access_type: public
latitude: 34.458600
longitude: 134.860100
source: 用廃機ハンターが行く！ "【兵庫県】ミツ精機（株）「翼の広場」の展示機" revised 2022-10-17 with a serial for all seven airframes
confidence: high — a precision-engineering company's corporate display park; free walk-in on company working days 08:00-17:00 Mon-Fri only; parties of 10+ must book. Recorded as `public` because an individual can simply turn up. The specialist source rates the outdoor preservation standard as the best in Japan. This is the largest aircraft display in western Japan.

name: Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion
city: Arakawa
state_province: Tokyo
country: Japan
postal_code: 
region: Asia
address: Arakawa Campus / 東京都立産業技術高等専門学校 荒川キャンパス 科学技術展示館
website: https://www.metro-cit.ac.jp/community/pavilion.html
access_type: appointment
latitude: 
longitude: 
source: Official college page (2026 open-day calendar; the 2009-05-18 Japan Aeronautic Association 重要航空遺産 certification "戦後航空再開時の国産航空機群" naming six specific items); 用廃機ハンターが行く！ bulletin 2025-12-02 recording the 2025 changes and the annual open-day posts for 2025 and 2026; the same blog's F-86D national list
confidence: high on identity and on the certified items; MEDIUM on the full airframe count. Around 15 airframes; the specialist source counts nine civil-registered fixed-wing among them. Admission is free but the hall opens on only EIGHT named weekdays a year (2026: 15 Apr / 18 May / 1 Jun / 18 Sep / 14 Oct / 1 Dec / 17 Dec / 25 Mar) 10:00-15:00 — hence `appointment`. Groups of 10+ must give notice.

name: Tsukuba Space Center -- Space Dome
city: Tsukuba
state_province: Ibaraki
country: Japan
postal_code: 305-8505
region: Asia
address: 2-1-1 Sengen / JAXA 筑波宇宙センター
website: https://www.jaxa.jp/about/centers/tksc/
access_type: public
latitude: 36.065778
longitude: 140.129806
source: ja.wikipedia "筑波宇宙センター" (Space Dome floor area; the H-II test vehicle becoming a permanent outdoor exhibit)
confidence: medium — the site free entry and the H-II launch vehicle are certain; the individual spacecraft in the Space Dome are a mixture of full-scale models and flight spares and JAXA does not publish an item-level inventory with identifiers so only the securely attested items are recorded below and every other field is blank

name: JAXA Sagamihara Campus -- Space Science Exploration Field Center
city: Sagamihara
state_province: Kanagawa
country: Japan
postal_code: 252-5210
region: Asia
address: 3-1-1 Yonodai Chuo-ku / 宇宙科学研究所 宇宙科学探査交流棟
website: https://www.isas.jaxa.jp/
access_type: public
latitude: 35.558333
longitude: 139.395278
source: ja.wikipedia "JAXA相模原キャンパス" — the 交流棟 opened February 2018 and took over the old lobby display; an M-V full-scale airframe model and an M-3SII full-size model stand outdoors
confidence: medium — free public exhibition building; the outdoor M-V and M-3SII are certain and unambiguous; the indoor probe exhibits are full-scale models and engineering hardware without published identifiers so they are not recorded individually

name: Yokaren Peace Memorial Museum
city: Ami
state_province: Ibaraki
country: Japan
postal_code: 300-0302
region: Asia
address: 5-1 Mawatari / 阿見町予科練平和記念館
website: https://www.yokaren-heiwa.jp/
access_type: public
latitude: 36.045583
longitude: 140.223472
source: ja.wikipedia "予科練平和記念館"; 用廃機ハンターが行く！ Zero feature (revised 2025-02) which gives the replica's commissioning detail — Ami Town FY2015 budget JPY 37.07 million placed with 広洋社 of Mito
confidence: high on the site; the single airframe is a full-scale REPLICA and is flagged as such. It is rolled out of its shelter only on fine Sundays and public holidays.

name: Tsukuba Naval Air Group Memorial Museum
city: Kasama
state_province: Ibaraki
country: Japan
postal_code: 
region: Asia
address: 筑波海軍航空隊記念館
website: https://p-ibaraki.com/
access_type: public
latitude: 
longitude: 
source: 用廃機ハンターが行く！ Zero feature revised 2025-02 which tracks the airframe from Misawa (until 2020-11-08) to a fuselage-only display at Tomobe station to the museum's exhibition store from 2022-06-25; ja.wikipedia "筑波海軍航空隊記念館"
confidence: medium-high — the site is certain; the only aircraft is the ex-Misawa full-scale A6M2 REPLICA built for the film 「聯合艦隊司令長官 山本五十六」. Viewing conditions can be restricted so check before travel.

name: Daikeien -- Ichikawa
city: Ichikawa
state_province: Chiba
country: Japan
postal_code: 
region: Asia
address: 大慶園
website: http://www.daikeien.jp/index01.html
access_type: public
latitude: 
longitude: 
source: 用廃機ハンターが行く！ "【千葉県】大慶園の機体" via the national directory entry 2026-05-05 and the F-104J/DJ national list revised 2021-06 (serials 76-8697 and 46-8571)
confidence: medium — an amusement arcade and go-kart park holding about seven airframes' worth of material as eye-catchers rather than as a museum display. It is recorded because the airframes are deliberately retained and publicly visible; the specialist source is explicit that it is NOT a museum. It is internationally known for holding the nose of the only F-15 ever lost in a mid-air engagement.

name: Hijiri Museum -- Ikusaka
city: Ikusaka
state_province: Nagano
country: Japan
postal_code: 
region: Asia
address: 聖博物館
website: 
access_type: public
latitude: 
longitude: 
source: 用廃機ハンターが行く！ national F-86D list revised 2026-03-05 (94-8146; noted as a 無償貸付機) and the F-104J/DJ national list revised 2021-06 (46-8608)
confidence: medium — a small municipal museum with two JASDF jets outdoors. Both are on free loan from the JASDF. The airframes are SHEETED OVER and inaccessible from roughly mid-November to April each year because of snow.

name: sora Kasai -- Uzurano Airfield Site
city: Kasai
state_province: Hyogo
country: Japan
postal_code: 
region: Asia
address: 2274-11 Uzurano-cho / 加西市地域活性化拠点施設「soraかさい」
website: https://sorakasai.com/
access_type: public
latitude: 
longitude: 
source: 用廃機ハンターが行く！ "【兵庫県】soraかさいの実物大模型と近隣のSNJ" revised 2023-05-19 with a 2023-04-02 site visit
confidence: high — opened 2022-04-18 on the site of the IJN Uzurano airfield. The two aircraft inside are full-scale REPLICAS and are flagged as such; the one real airframe is the ex-JMSDF SNJ-5 in a restored open revetment about 800 m north-west of the building (34.8950N approx.) which was rescued from Kanoya in 2019 after typhoon damage.

## AIRCRAFT

### Gifu-Kakamigahara Air and Space Museum

Kawasaki|KV-107|IIA-4|51804|Sea Knight||rotary_wing||military|transport||Outdoor display; ex-JGSDF transport helicopter; repainted on a five-to-ten-year cycle like all four outdoor airframes|KV107; V-107; JG-1804|Gifu-Kakamigahara Air and Space Museum|on_display|JP
NAMC|YS-11|A-213|JA8731|||fixed_wing|monoplane|civilian|commercial_transport||Outdoor display; ex-Air Nippon; flown into Gifu air base and towed to the museum along the 1.2 km access road built for the purpose|YS11; YS-11A-500R|Gifu-Kakamigahara Air and Space Museum|on_display|JP
ShinMaywa|US-1|A|9078|||fixed_wing|monoplane|military|search_rescue||Outdoor display; ex-JMSDF rescue flying boat; flew from Iwakuni to Gifu on 1995-12-12 routed over 24 schools in Kakamigahara so pupils could watch|US1; US-1A|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|P-2|J|4782|Neptune||fixed_wing|monoplane|military|recon||Outdoor display; ex-JMSDF; retired 1994-05-22 and flown from Kanoya to Gifu on the 26th; parked on the air base until the museum opened|P2J; P-2J; Kawasaki P-2J|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Wright|Flyer||||Wright Flyer|fixed_wing|biplane|civilian|experimental||Full-scale replica of the 1903 machine; indoor display|Wright Flyer I|Gifu-Kakamigahara Air and Space Museum|on_display|
Grade|Monoplane|||||fixed_wing|monoplane|civilian|experimental||Faithful reconstruction built by the volunteer グラーデ復元の会; indoor display|Grade Eindecker|Gifu-Kakamigahara Air and Space Museum|on_display|
Kawasaki|Salmson 2|A2|1001|Otsu-shiki Ichi-gata Teisatsuki||fixed_wing|biplane|military|recon||Faithful reconstruction built by Kawasaki Heavy Industries of the Japanese-built Salmson 2A2 army reconnaissance biplane; certified 近代化産業遺産 by METI|Salmson 2A2; 乙式一型偵察機; Otsu-shiki 1-gata|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Mitsubishi|A6M|1|三菱201|12-shi Kanjo Sentoki||fixed_wing|monoplane|military|fighter||Full-scale replica of the A6M1 Zero prototype built for the museum; displayed from the 2018 reopening|A6M1; 十二試艦上戦闘機; 12-shi carrier fighter|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|Ki-61|II Kai|川崎6117|Hien||fixed_wing|monoplane|military|fighter||The world's only surviving Ki-61-II Kai; displayed 1986-2015 at Chiran then restored by Kawasaki at Gifu in 2015 deliberately left unpainted to show construction technique; certified 重要航空遺産 and 近代化産業遺産; a national roundel is projected onto the airframe|Ki61; Ki-61-II-Kai; 三式戦闘機二型; Type 3 Fighter; Tony; c/n 6117|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|KAL-1||JA3074|||fixed_wing|monoplane|civilian|utility||Indoor display; Kawasaki liaison aircraft prototype; on display since 2014|KAL1; KAL-1|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|KAT-1||JA3084|||fixed_wing|monoplane|civilian|trainer||Indoor display since 2003; airframe number 1 of the two KAT-1 built; parts of the second airframe JA3100 were used in its restoration|KAT1; KAT-1|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Lockheed|T-33|A|61-5221|Shooting Star||fixed_wing|monoplane|military|trainer||Special Air Development and Test Wing configuration; retired at Iruma and earmarked for return to the USA under the MDAP agreement then re-loaned by the USA; dismantled at Iruma and rebuilt by the JASDF 2nd Depot at Gifu|T33; T-33A; T-33A Kai|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Lockheed|F-104|J|36-8515|Starfighter||fixed_wing|monoplane|military|fighter||Indoor display; Mitsubishi-built under licence; one of only three F-104J/DJ in Japan on routine indoor public display|F104; F-104J; Eiko; Mitsubishi F-104J|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Saab|91|B|TX-7101|Safir||fixed_wing|monoplane|military|test||High-lift research aircraft converted from a Saab 91B Safir and designated X1G1B; certified 重要航空遺産|Saab Safir; X1G; X1G1B; 91B Kai|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Fuji|T-1|B|05-5810|Hatsutaka||fixed_wing|monoplane|military|trainer||Special Air Development and Test Wing configuration wearing the ADTW 50th anniversary scheme; on display since 2007|T1; T-1B|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Nihon University|N-62||JA3251|Eaglet||fixed_wing|monoplane|civilian|experimental||Restored to airworthy condition by the Japan Aviation Academy and flown from the academy strip in Yamanashi to Gifu air base on 1998-11-08 before entering the museum|N62; N-62 Eaglet; Nihon-Itochu N-62|Gifu-Kakamigahara Air and Space Museum|on_display|JP
ShinMaywa|UF-XS||オ-991|||fixed_wing|monoplane|military|test||Experimental flying boat that proved the US-1 hull; had been condemned to be scrapped and returned to the JMSDF and was reprieved at the last moment; dismantled for transport then rebuilt by ShinMaywa; certified 重要航空遺産|UFXS; UF-XS|Gifu-Kakamigahara Air and Space Museum|on_display|JP
NAL|Flying Test Bed|||||fixed_wing|monoplane|civilian|experimental||VTOL test rig using JR100F lift-jet engines; transferred free of charge from the National Museum of Nature and Science and restored by Fuji Heavy Industries|VTOL Flying Test Bed; JR100F testbed; 航技研フライングテストベッド|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Fuji|FA-200||JA3263|Aero Subaru||fixed_wing|monoplane|civilian|experimental||FA-200 modified as a STOL research aircraft|FA200; FA-200 Kai|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Fuji|T-3||11-5547|||fixed_wing|monoplane|military|trainer||Indoor display since 2008|T3; T-3|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Mitsubishi|T-2||19-5173|||fixed_wing|monoplane|military|trainer||Blue Impulse markings; indoor display since 2001|T2; T-2; Blue Impulse|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Mitsubishi|T-2|CCV|29-5103|||fixed_wing|monoplane|military|test||Control-configured-vehicle research aircraft; indoor display since 2014|T2 CCV; T-2CCV|Gifu-Kakamigahara Air and Space Museum|on_display|JP
McDonnell Douglas|F-4|EJ|07-8431|Phantom II||fixed_wing|monoplane|military|fighter||F-4EJ Kai standard; Mitsubishi-built under licence; added to the indoor display in 2023|F4; F-4EJ; F-4EJ Kai; Phantom|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|Asuka||8501|||fixed_wing|monoplane|civilian|experimental||Quiet STOL research aircraft; the airframe around which the whole museum was conceived — Kakamigahara secured it in 1989 and the loan was agreed in August 1991; certified 重要航空遺産 and 航空宇宙技術遺産|Asuka; 飛鳥; NAL Asuka; QSTOL|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Nihon University|N-70||||Cygnus|fixed_wing|monoplane|civilian|private||Motor glider|N70; N-70 Cygnus|Gifu-Kakamigahara Air and Space Museum|on_display|
Nihon University|HYPER CHick|||KoToNo Limited||fixed_wing|monoplane|civilian|experimental|1992|Human-powered aircraft; span 25.9 m length 8.2 m height 3.3 m weight 37.0 kg; set the first Japanese women's human-powered flight record of 119.045 m at Fujikawa gliding field on 1992-07-05; damaged at the 16th Birdman Rally and repaired; skin repaired again during the 2017 closure|HYPER CHick KoToNo Limited|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|BK117|P5|JQ0003|||rotary_wing||civilian|test||Advanced flight-safety technology demonstrator; on display since 2001|BK117; BK117P5|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|BK117|A|6001|||rotary_wing||military|test||Acquisition Technology and Logistics Agency trials helicopter; added 2023; used for rear-seat and cockpit sitting experience|BK117; BK117A|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|OH-1|||Ninja||rotary_wing||military|recon||Full-scale mock-up|OH1; OH-1|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|KH-4||JA7110|||rotary_wing||civilian|utility||Bell 47G3B-KH4 built by Kawasaki|Bell 47G3B-KH4; KH4; KH-4|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|KHR-1||2500|||rotary_wing||civilian|experimental||Rigid-rotor research helicopter; most of the airframe other than the rotor system had been lost so it was rebuilt around another KH-4; on display since 2004|KHR1; KHR-1|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Hughes|OH-6|J|JG1058|Cayuse||rotary_wing||military|test||Kawasaki KA370 new-rotor-system flight-test aircraft; after the trials it was restored to standard OH-6 configuration as JGSDF 31058 and displayed as such from 1996; returned to its trials configuration for display in 2004|OH6; OH-6J Kai; KA370; 31058|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Kawasaki|K-RACER|X1|JX0169|||rotary_wing||civilian|drone||Kawasaki VTOL unmanned aircraft; 5 m rotor 1.9 m height powered by a Kawasaki Ninja H2R motorcycle engine|K-RACER-X1; KRACER|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Hagiwara|H-23|BA-2|JA2023|||fixed_wing|monoplane|civilian|private||In the reserve store; never publicly displayed; shown occasionally on the booked そらはく資料特別公開 tours|H23; H-23BA-2|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Hagiwara|H-23|C-2|JA2077|||fixed_wing|monoplane|civilian|private||In the reserve store; glider|H23; H-23C-2|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Mita|3|Kai 1|JA2080|||fixed_wing|monoplane|civilian|private||In the reserve store; two-seat advanced glider|Mita 3; 三田式3改1型|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Mita|3|Kai 1|JA2176|||fixed_wing|monoplane|civilian|private||In the reserve store; two-seat advanced glider|Mita 3; 三田式3改1型|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Takatori|SH-16|S|JA2102|||fixed_wing|monoplane|civilian|private||In the reserve store; ex-Kyoto University gliding club|SH16; SH-16S|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Kawasaki|KAT-1||JA3100|||fixed_wing|monoplane|civilian|trainer||Airframe number 2 of the two built; displayed at Tokyo Metropolitan University of Science and Technology then taken by Kakamigahara City; condition too poor to display so it has stayed in the store and donated parts to the restoration of JA3084|KAT1; KAT-1|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Fuji|T-1|B|85-5801|Hatsutaka||fixed_wing|monoplane|military|trainer||Prototype airframe 801; converted from T1F2 82-5801 to T-1B 85-5801; displayed outdoors at Ashiya air base then in the museum store from 2001|T1; T-1B; T1F2; 82-5801|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Fuji|KM-2||6255|||fixed_wing|monoplane|military|trainer||Ex-JMSDF 201 Training Squadron at Ozuki; later a teaching airframe at Tokyo Metropolitan College of Aeronautical Engineering; now in the museum store|KM2; KM-2|Gifu-Kakamigahara Air and Space Museum|in_storage|JP
Nissan|Pencil Rocket|||||missile_rocket||civilian|sounding||Replica of the 1955 Pencil Rocket|Pencil Rocket; ペンシルロケット|Gifu-Kakamigahara Air and Space Museum|on_display|JP
OKB-1|Sputnik|1|||Sputnik 1|spacecraft||civilian|space||Replica|Sputnik-1; PS-1|Gifu-Kakamigahara Air and Space Museum|on_display|
NASDA|Ryusei|||りゅうせい||spacecraft||civilian|space||Replica displayed inside an H-II launcher fairing alongside Myojo|Ryusei; VEP; りゅうせい|Gifu-Kakamigahara Air and Space Museum|on_display|JP
NASDA|Myojo|||みょうじょう||spacecraft||civilian|space||Replica displayed inside an H-II launcher fairing alongside Ryusei|Myojo; OREX; みょうじょう|Gifu-Kakamigahara Air and Space Museum|on_display|JP
JAXA|Hayabusa2|||はやぶさ2||spacecraft||civilian|space||Replica|Hayabusa2; はやぶさ2|Gifu-Kakamigahara Air and Space Museum|on_display|JP
JAXA|SLIM|||||spacecraft||civilian|space||Replica shown in the landed attitude on a simulated lunar surface; first shown in the FY2024 special exhibition and permanent from 2026-02-21|SLIM; Smart Lander for Investigating Moon|Gifu-Kakamigahara Air and Space Museum|on_display|JP
JAXA|SORA-Q|||||spacecraft||civilian|space||Replica lunar excursion vehicle; permanent from 2026-02-21|SORA-Q; LEV-2|Gifu-Kakamigahara Air and Space Museum|on_display|JP
NASDA|OICETS|||Kirari||spacecraft||civilian|space||Optical inter-orbit communications engineering test satellite; described as a replica but incorporating some genuine flight hardware|Kirari; OICETS; きらり|Gifu-Kakamigahara Air and Space Museum|on_display|JP
NASDA|COMETS|||Kakehashi||spacecraft||civilian|space||The genuine thermal-test article used during development — not a replica|Kakehashi; COMETS; かけはし|Gifu-Kakamigahara Air and Space Museum|on_display|JP
University of Tokyo|Nano-JASMINE|||||spacecraft||civilian|space||Engineering model|Nano-JASMINE|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Tokyo Institute of Technology|CUTE|I|||CUTE-I|spacecraft||civilian|space||CubeSat|CUTE-I; CUTE-1|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Nagoya University|ChubuSat|2|||ChubuSat-2|spacecraft||civilian|space||Replica microsatellite|ChubuSat-2|Gifu-Kakamigahara Air and Space Museum|on_display|JP
Wakayama University|UNIFORM|2|||UNIFORM2|spacecraft||civilian|space||Built as a manufacturing-training article for the UNIFORM microsatellite programme; UNIFORM1 was the flight article|UNIFORM2; UNIFORM-2|Gifu-Kakamigahara Air and Space Museum|on_display|JP
JAXA|Kibo|||JEM||spacecraft||civilian|space||Full-scale model of the Japanese Experiment Module|Kibo; JEM; きぼう|Gifu-Kakamigahara Air and Space Museum|on_display|JP
JAXA|MINERVA|||||spacecraft||civilian|space||Replicas of the MINERVA-1A MINERVA-2A and MINERVA-II2 asteroid rovers|MINERVA; ミネルバ|Gifu-Kakamigahara Air and Space Museum|on_display|JP
DLR|MASCOT|||||spacecraft||civilian|space||Replica of the German asteroid lander carried by Hayabusa2|MASCOT|Gifu-Kakamigahara Air and Space Museum|on_display|DE
NASA|Mars Exploration Rover|||||spacecraft||civilian|space||Replica; previously exhibited in the United States pavilion at Expo 2005 Aichi|MER; Mars Exploration Rover|Gifu-Kakamigahara Air and Space Museum|on_display|US
NASA|Curiosity|||||spacecraft||civilian|space||Replica; previously exhibited in the United States pavilion at Expo 2005 Aichi|Curiosity; MSL|Gifu-Kakamigahara Air and Space Museum|on_display|US
Energia|Soyuz|||||spacecraft||civilian|space||Soviet-made reproduction of a Soyuz re-entry capsule; owned by the Tsukuba Space Center and on display here since June 2025|Soyuz descent module; ソユーズ帰還カプセル|Gifu-Kakamigahara Air and Space Museum|on_display|SU
Energia|Bion|9|||Bion 9|spacecraft||civilian|space||Owned by the Tsukuba Space Center and on display here since June 2025|Bion-9; ビオン9号|Gifu-Kakamigahara Air and Space Museum|on_display|SU

### Tokorozawa Aviation Museum

NAMC|YS-11|A|JA8732|||fixed_wing|monoplane|civilian|commercial_transport||Outdoor display in front of Kokukoen station; repainted 2010 and mid-2017; the blue upper surfaces were badly flaked when inspected on 2025-04-06|YS11; YS-11A|Tokorozawa Aviation Museum|on_display|JP
Curtiss|C-46|D|91-1143|Commando||fixed_wing|monoplane|military|transport||Outdoor display in front of the museum building; actually converted from a C-46A to an EC-46 electronic-warfare aircraft and restored to transport configuration when displayed in March 1980 by removing two ventral radomes — the single black radome on the nose upper decking survives and unnatural panel lines mark the removed ones; it never flew in D configuration; managed by Tokorozawa City not by the museum which is why the museum's own outdoor-display page does not mention it; repainted January 2011 late January 2015 and about December 2019|C46; C-46D; EC-46; C-46 ECM|Tokorozawa Aviation Museum|on_display|JP
Fuji|T-1|B|25-5856|Hatsutaka||fixed_wing|monoplane|military|trainer||Indoor display; JASDF free-loan airframe; wears the 5th Technical School (Komaki) fin marking; one of only two places in Japan where a T-1 can be viewed from above|T1; T-1B|Tokorozawa Aviation Museum|on_display|JP
North American|T-6|G|52-0099|Texan||fixed_wing|monoplane|military|trainer||Indoor display; ex-JASDF but NOT a JASDF free-loan airframe and its route into the collection is not documented|T6; T-6G; Harvard|Tokorozawa Aviation Museum|on_display|JP
Kawasaki|KAL-2||20001|||fixed_wing|monoplane|military|utility||Indoor display; ex-JGSDF and the only KAL-2 on display anywhere; recorded at Kisarazu camp about 1982; originally olive drab and repainted in a light scheme for display because too many of the founding exhibits were dark-coloured JGSDF machines|KAL2; KAL-2|Tokorozawa Aviation Museum|on_display|JP
Stinson|L-5|E||Sentinel||fixed_wing|monoplane|military|utility||Indoor display; ex-JGSDF and the only one on display in Japan; the fin carries 535025 which is an L-5G serial — the true type is an L-5E and the true serial is not known; treat the painted marking as false|L5; L-5E; Sentinel; 535025|Tokorozawa Aviation Museum|on_display|JP
Piper|L-21|B|12032|Super Cub||fixed_wing|monoplane|military|utility||Indoor display suspended from the ceiling; the only ex-JGSDF example on display in Japan; civil type designation PA-18-135|L21; L-21B; PA-18-135; Super Cub|Tokorozawa Aviation Museum|on_display|JP
Beechcraft|T-34|A|60508|Mentor||fixed_wing|monoplane|military|trainer||Indoor display; ex-JGSDF; originally olive drab and repainted orange for display which is far from its service appearance|T34; T-34A; Mentor|Tokorozawa Aviation Museum|on_display|JP
Sikorsky|H-19|C|40001|Chickasaw||rotary_wing||military|utility||Indoor display; ex-JGSDF and the only intact example in Japan; a public notice issued at the end of 2020 scheduled it for scrapping and the renewal plan confirms disposal — treat its survival past 2025 as unverified|H19; H-19C; S-55; Chickasaw|Tokorozawa Aviation Museum|on_display|JP
Hughes|OH-6|J|31065|Cayuse||rotary_wing||military|recon||Indoor display; ex-JGSDF; repainted in a light scheme for display rather than its service olive drab|OH6; OH-6J; Cayuse|Tokorozawa Aviation Museum|on_display|JP
Vertol|V-44|A|50002|||rotary_wing||military|transport||Indoor display; the second of only two acquired by the JGSDF and the only one on display; a public notice issued at the end of 2020 scheduled it for scrapping in the 2025 rebuild|V44; V-44A; H-21B; Piasecki H-21|Tokorozawa Aviation Museum|on_display|JP
Nieuport|81|E2|||Nieuport 81E2|fixed_wing|biplane|military|trainer||Only the nose frame and engine of the genuine airframe survive; displayed beside a full replica of the same type|Nieuport 81E2; Nieuport 81|Tokorozawa Aviation Museum|on_display|JP
Nakajima|Ki-11|Type 91|c/n 237|Type 91 Fighter||fixed_wing|monoplane|military|fighter|1933|Fuselage only of manufacturer's number 237 built January 1933; the only surviving Type 91 fighter in the world; certified 重要航空遺産 by the Japan Aeronautic Association and 近代化産業遺産 by METI in FY2008; the airframe was bought privately during the war and kept untouched|Type 91 Fighter; 九一式戦闘機; Nakajima NC; c/n 237|Tokorozawa Aviation Museum|on_display|JP
Kirigamine|K-14||JA0148|Hato||fixed_wing|monoplane|civilian|private||Primary glider; indoor display|K14; K-14; 霧ヶ峰式はとK-14型|Tokorozawa Aviation Museum|on_display|JP
Cessna|T310|P|JA5170|||fixed_wing|monoplane|civilian|private||Indoor display with the right wing removed for cockpit access and structural demonstration; the museum's only indoor civil fixed-wing aircraft|T310; Cessna T310P|Tokorozawa Aviation Museum|on_display|JP
Kawasaki|C-1||68-1019|||fixed_wing|monoplane|military|transport|1976|Nose section only about 3.7 m long 3.1 m wide 4.5 m high; accepted 1976 and retired about 2023-10-30 with 17880 flying hours; separated from the fuselage at Iruma on 2025-12-11 and delivered to the museum in the early hours of 2025-12-12; the remaining fuselage was scrapped at Iruma on 2026-01-27|C1; C-1|Tokorozawa Aviation Museum|on_display|JP
Rinji Gunyo Kikyu Kenkyukai|Kaishiki|1|||Kaishiki No.1|fixed_wing|biplane|military|experimental||Full-scale replica suspended in the entrance hall; the type was based on the 1910 Henri Farman biplane not on the Wright Flyer|Kaishiki No.1; 会式一号機; 臨時軍用気球研究会式一号機|Tokorozawa Aviation Museum|on_display|JP
Nieuport|81|E2|||Nieuport 81E2|fixed_wing|biplane|military|trainer||Full-scale replica displayed beside the genuine nose frame of the same type|Nieuport 81E2 replica|Tokorozawa Aviation Museum|on_display|JP
North American|F-86|D|84-8102|Sabre Dog||fixed_wing|monoplane|military|fighter||In the reserve hangar; supplied to the JASDF by the USA and later a 1st Technical School instructional airframe; recorded at Kisarazu camp about 1980; NOT listed on the JASDF free-loan register so it was obtained by another route; displayed without a nose number at first and carried 102 by 2015; confirmed present at the October 2024 hangar opening; disposal is thought likely in the 2025 rebuild; one of only two Japanese survivors with the alternative cooling-air intake shape|F86D; F-86D; Sabre Dog|Tokorozawa Aviation Museum|in_storage|JP
Kawasaki|Bell 47|D-1|30003|||rotary_wing||military|trainer||In the reserve hangar; ex-JGSDF H-13E; the fin is painted ST-5 with the earlier serial JG-0003 showing faintly beneath|Bell 47D-1; H-13E; ST-5; JG-0003|Tokorozawa Aviation Museum|in_storage|JP
Kawasaki|KV-107|II-4|51734|||rotary_wing||military|transport||In the reserve hangar; ex-JGSDF; has never been publicly displayed at the museum|V-107A; KV107; KV-107II-4|Tokorozawa Aviation Museum|in_storage|JP
Mil|Mi-8|PA|JA9549|Hip||rotary_wing||civilian|transport||In the reserve hangar; ex-Aero Asahi and the only Mi-8 ever operated in Japan; displayed in the hall for some years after the museum opened; a 2024 laser survey found it is taller than the hangar door and the staff cannot work out how it was got in or how to get it out|Mi8; Mi-8PA; Hip|Tokorozawa Aviation Museum|in_storage|JP
Piper|J-3|C-65|JA3925|Cub||fixed_wing|monoplane|civilian|private||In the reserve hangar; float-equipped|J3; J-3C-65; Piper Cub|Tokorozawa Aviation Museum|in_storage|JP
Cessna|170|B|JA3052|||fixed_wing|monoplane|civilian|private||In the reserve hangar with wings and engine removed|Cessna 170B|Tokorozawa Aviation Museum|in_storage|JP
Schleicher|ASW 15|B|JA2150|||fixed_wing|monoplane|civilian|private||In the reserve hangar; ex-Tohoku University gliding club|ASW15; ASW 15B|Tokorozawa Aviation Museum|in_storage|JP
Nihon University|Sakuzo|IV|||Sakuzo IV|fixed_wing|monoplane|civilian|experimental||Human-powered aircraft built by Nihon University; in the reserve hangar|Sakuzo IV; 作蔵IV|Tokorozawa Aviation Museum|in_storage|JP

### JASDF Hamamatsu Air Park

Curtiss|C-46|D|91-1138|Commando||fixed_wing|monoplane|military|transport||Outdoor display; Flight Check Squadron markings|C46; C-46D|JASDF Hamamatsu Air Park|on_display|JP
North American|F-86|F|02-7966|Sabre||fixed_wing|monoplane|military|fighter||Outdoor display in Blue Impulse markings; Mitsubishi-built under licence|F86; F-86F; Sabre; Blue Impulse|JASDF Hamamatsu Air Park|on_display|JP
Lockheed|F-104|J|76-8698|Starfighter||fixed_wing|monoplane|military|fighter||Outdoor display in UF-104J unmanned target configuration; Mitsubishi-built under licence|F104; F-104J; UF-104J; Eiko|JASDF Hamamatsu Air Park|on_display|JP
Piasecki|H-21|B|02-4756|Workhorse||rotary_wing||military|transport||Outdoor display|H21; H-21B; Workhorse; Vertol 44|JASDF Hamamatsu Air Park|on_display|JP
Western Electric|MIM-14|Nike J||Nike Hercules||missile_rocket||military|surface_to_air||Outdoor display; Japanese-assembled Nike J surface-to-air missile|Nike J; MIM-14; Nike Hercules; ナイキJ|JASDF Hamamatsu Air Park|on_display|JP
Mitsubishi|A6M|52a|三菱4685|Zero||fixed_wing|monoplane|military|fighter||Shot down over Guam July 1944 and found at Agana in April 1963; airlifted to Gifu in January 1964 and restored there; the first Zero restored in postwar Japan and generally regarded as the least accurate of the surviving restorations; hung in flying attitude in the display hangar from the 1999 opening and moved during 2024 to the second floor of the adjacent archive building where it now sits on its undercarriage|A6M5a; 零式艦上戦闘機52型甲; Zeke; c/n 4685|JASDF Hamamatsu Air Park|on_display|JP
Beechcraft|B-65||03-3094|Queen Air||fixed_wing|monoplane|military|utility||Indoor display; withdrawn from public view in the 2021 refit|B65; B-65; Queen Air; LR-1|JASDF Hamamatsu Air Park|in_storage|JP
Mitsubishi|F-1||90-8225|||fixed_wing|monoplane|military|ground_attack||Indoor display as a sectioned cutaway airframe|F1; F-1|JASDF Hamamatsu Air Park|on_display|JP
Mitsubishi|F-1||90-8227|||fixed_wing|monoplane|military|ground_attack||Indoor display|F1; F-1|JASDF Hamamatsu Air Park|on_display|JP
Mitsubishi|F-2||63-8501|||fixed_wing|monoplane|military|fighter||Full-scale mock-up of the first aircraft; painted and displayed indoors; the matching F-2B nose mock-up is at Ishikawa Aviation Plaza|F2; F-2; XF-2|JASDF Hamamatsu Air Park|on_display|JP
North American|F-86|D|84-8104|Sabre Dog||fixed_wing|monoplane|military|fighter||Indoor display; a 1st Technical School instructional airframe by the end of FY1973; no fin unit marking has ever been recorded on it|F86D; F-86D; Sabre Dog|JASDF Hamamatsu Air Park|on_display|JP
North American|F-86|F|02-7960|Sabre||fixed_wing|monoplane|military|fighter||Indoor display in Blue Impulse markings; Mitsubishi-built; note that the airframe at Kawaguchiko painted as 02-7960 is really 02-7962 — this is the genuine 960|F86; F-86F; Sabre; Blue Impulse|JASDF Hamamatsu Air Park|on_display|JP
Lockheed|F-104|J|76-8693|Starfighter||fixed_wing|monoplane|military|fighter||Indoor display; Mitsubishi-built under licence; one of only three F-104J/DJ in Japan on routine indoor public display|F104; F-104J; Eiko|JASDF Hamamatsu Air Park|on_display|JP
McDonnell Douglas|F-4|EJ|17-8440|Phantom II||fixed_wing|monoplane|military|fighter||F-4EJ Kai standard; the last F-4EJ built and the last F-4 Phantom built anywhere in the world; Mitsubishi-built under licence|F4; F-4EJ; F-4EJ Kai; Phantom|JASDF Hamamatsu Air Park|on_display|JP
Sikorsky|H-19|C|91-4709|Chickasaw||rotary_wing||military|search_rescue||Indoor display; withdrawn from public view in the 2021 refit|H19; H-19C; S-55|JASDF Hamamatsu Air Park|in_storage|JP
Kawasaki|KV-107|II|24-4832|||rotary_wing||military|search_rescue||Indoor display|KV107; V-107; KV-107II|JASDF Hamamatsu Air Park|on_display|JP
Mitsubishi|MU-2|S|13-3209|||fixed_wing|monoplane|military|search_rescue||Indoor display|MU2; MU-2S|JASDF Hamamatsu Air Park|on_display|JP
Sikorsky|S-62|J|53-4774|||rotary_wing||military|search_rescue||Indoor display; withdrawn from public view in the 2021 refit|S62; S-62J|JASDF Hamamatsu Air Park|in_storage|JP
Fuji|T-1|A|15-5825|Hatsutaka||fixed_wing|monoplane|military|trainer||Indoor display; withdrawn from public view in the 2021 refit|T1; T-1A|JASDF Hamamatsu Air Park|in_storage|JP
Mitsubishi|T-2||59-5111|||fixed_wing|monoplane|military|trainer||Indoor display in Blue Impulse markings|T2; T-2; Blue Impulse|JASDF Hamamatsu Air Park|on_display|JP
Fuji|T-3||91-5517|||fixed_wing|monoplane|military|trainer||Indoor display|T3; T-3|JASDF Hamamatsu Air Park|on_display|JP
Kawasaki|T-4||66-5745|||fixed_wing|monoplane|military|trainer||Indoor display in Blue Impulse markings|T4; T-4; Blue Impulse|JASDF Hamamatsu Air Park|on_display|JP
North American|T-6|F|52-0010|Texan||fixed_wing|monoplane|military|trainer||Indoor display; withdrawn from public view in the 2021 refit|T6; T-6F; Texan; SNJ|JASDF Hamamatsu Air Park|in_storage|JP
North American|T-28|B|63-0581|Trojan||fixed_wing|monoplane|military|trainer||Indoor display; withdrawn from public view in the 2021 refit|T28; T-28B; Trojan|JASDF Hamamatsu Air Park|in_storage|JP
Lockheed|T-33|A|71-5239|Shooting Star||fixed_wing|monoplane|military|trainer||Indoor display; withdrawn from public view in the 2021 refit|T33; T-33A; Shooting Star|JASDF Hamamatsu Air Park|in_storage|JP
Beechcraft|T-34|A|51-0382|Mentor||fixed_wing|monoplane|military|trainer||Indoor display; Fuji-built under licence|T34; T-34A; Mentor|JASDF Hamamatsu Air Park|on_display|JP
de Havilland|DH.100|T.55|63-5571|Vampire||fixed_wing|monoplane|military|trainer||Indoor display; withdrawn from public view in the 2021 refit; two-seat Vampire trainer|DH100; Vampire; Vampire T.55|JASDF Hamamatsu Air Park|in_storage|JP
Ansaldo|SVA|9|13146|||fixed_wing|biplane|military|recon||Indoor display; Italian biplane of the type flown on the 1920 Rome-Tokyo flight|SVA9; Ansaldo SVA 9|JASDF Hamamatsu Air Park|on_display|IT

### Misawa Aviation and Science Museum

Mitsubishi|F-1||00-8247|||fixed_wing|monoplane|military|ground_attack||Outdoor in the Ozora Hiroba free park; JASDF free-loan airframe; wears the 3rd Squadron warrior badge and the special retirement scheme; Misawa is the only place in Japan where an F-1 an early-production T-2 and a late-production T-2 stand together|F1; F-1|Misawa Aviation and Science Museum|on_display|JP
McDonnell Douglas|F-4|EJ|57-8375|Phantom II||fixed_wing|monoplane|military|fighter||F-4EJ Kai standard; JASDF free-loan airframe; 8th Squadron black panther badge; delivered 2009-01-29 and repainted between 2021-09-09 and 2021-12-10 for JPY 2035000 with about 80 per cent of the stencilling reinstated|F4; F-4EJ; F-4EJ Kai; Phantom|Misawa Aviation and Science Museum|on_display|JP
Lockheed|F-104|J|76-8699|Starfighter||fixed_wing|monoplane|military|fighter||JASDF free-loan airframe; 207th Squadron markings and the anti-salt-corrosion finish specific to the Okinawa-based aircraft; cockpit opened to visitors|F104; F-104J; Eiko|Misawa Aviation and Science Museum|on_display|JP
Mitsubishi|T-2||59-5105|||fixed_wing|monoplane|military|trainer||JASDF free-loan airframe; a rare early-production T-2; moved from a display site inside Misawa air base where it had been given F-1 camouflage; repainted into early 4th Air Wing markings for museum display|T2; T-2|Misawa Aviation and Science Museum|on_display|JP
Mitsubishi|T-2||29-5177|||fixed_wing|monoplane|military|trainer||JASDF free-loan airframe; late-production; Blue Impulse markings and badly faded when inspected in 2021|T2; T-2; Blue Impulse|Misawa Aviation and Science Museum|on_display|JP
Fuji|T-3||91-5516|||fixed_wing|monoplane|military|trainer||JASDF free-loan airframe; 11th Flying Training Wing (Shizuhama) markings; cockpit opened to visitors|T3; T-3|Misawa Aviation and Science Museum|on_display|JP
Lockheed|T-33|A|81-5344|Shooting Star||fixed_wing|monoplane|military|trainer||Northern Air Defence Force support flight markings in blue; retired from the JASDF and RETURNED TO THE USAF in 2002 then loaned free of charge by the US military to Misawa City so the airframe is legally American not Japanese; on display since July 2005|T33; T-33A; Shooting Star|Misawa Aviation and Science Museum|on_display|US
Mitsubishi|LR-1||22009|||fixed_wing|monoplane|military|recon||Ex-JGSDF; cabin opened to visitors; badly faded|LR1; LR-1; MU-2|Misawa Aviation and Science Museum|on_display|JP
Hughes|OH-6|D|31270|Cayuse||rotary_wing||military|recon||Ex-JGSDF; the second airframe of this type displayed here; a viewing platform surrounds the nose|OH6; OH-6D; Cayuse|Misawa Aviation and Science Museum|on_display|JP
General Dynamics|F-16|A|78-0021|Fighting Falcon||fixed_wing|monoplane|military|fighter||On loan from the USAF; the only F-16A on permanent public display in Japan|F16; F-16A; Fighting Falcon; Viper|Misawa Aviation and Science Museum|on_display|US
Lockheed|P-3|UP-3A|150526|Orion||fixed_wing|monoplane|military|utility||Bureau Number 150526; on loan from the US Seventh Fleet; cabin opened to visitors; believed to be the only UP-3A on display anywhere in the world; often listed as UP-3C in later sources|P3; UP-3A; Orion; BuNo 150526|Misawa Aviation and Science Museum|on_display|US
NAMC|YS-11||JA8776|||fixed_wing|monoplane|civilian|commercial_transport||Indoor display with the cabin open; ex-Japan Air Commuter; the only YS-11 in Japan preserved in Toa Domestic Airlines colours|YS11; YS-11|Misawa Aviation and Science Museum|on_display|JP
Honda|HondaJet||N420HA|||fixed_wing|monoplane|civilian|private||Construction number P001; the HondaJet technology demonstrator; on display from the April 2021 reopening|HondaJet; HA-420; c/n P001|Misawa Aviation and Science Museum|on_display|US
Bellanca|Model J|Skyrocket||Miss Veedol||fixed_wing|monoplane|civilian|private||Full-scale replica of the aircraft flown by Pangborn and Herndon on the first non-stop trans-Pacific flight from Sabishiro Beach in 1931; the museum's centrepiece|Miss Veedol; Bellanca Skyrocket; ミス・ビードル号|Misawa Aviation and Science Museum|on_display|US
Tokyo Imperial University|Koken-ki|||Koken-ki||fixed_wing|monoplane|civilian|experimental||Full-scale replica of the 1938 long-range record aircraft|Koken-ki; 航研機|Misawa Aviation and Science Museum|on_display|JP
Narahara|Type 2|||Narahara No.2||fixed_wing|biplane|civilian|experimental||Full-scale replica of the 1911 machine|奈良原式2号機; Narahara No.2|Misawa Aviation and Science Museum|on_display|JP
Shirato|Asahi|||Shirato Asahi-go||fixed_wing|biplane|civilian|experimental||Full-scale replica|白戸式旭号; Shirato Asahi|Misawa Aviation and Science Museum|on_display|JP
Wright|Flyer||||Wright Flyer|fixed_wing|biplane|civilian|experimental||Full-scale replica|Wright Flyer I|Misawa Aviation and Science Museum|on_display|
Unidentified|HAYABUSA Kai|||||fixed_wing|biplane|civilian|private||Primary training glider; rebuilt from a shoulder-and-high-wing biplane layout into a shoulder-and-low-wing biplane so it no longer matches the photograph on its own interpretation board|HAYABUSA Kai; プライマリーグライダーHAYABUSA改|Misawa Aviation and Science Museum|on_display|JP
JAXA|Hayabusa2|||はやぶさ2||spacecraft||civilian|space||Full-scale model; added in the April 2021 reopening|Hayabusa2; はやぶさ2|Misawa Aviation and Science Museum|on_display|JP
Nihon University|CHicK|2000|||CHicK-2000|fixed_wing|monoplane|civilian|experimental||Human-powered aircraft|CHicK-2000|Misawa Aviation and Science Museum|on_display|JP

### Yushukan -- Yasukuni Shrine

Mitsubishi|A6M|52|三菱4240|Zero||fixed_wing|monoplane|military|fighter||Recovered at Rabaul and restored by the Kawaguchiko Motor Museum with Mitsubishi Heavy Industries assistance; primarily Mitsubishi manufacturer's number 4240 with some parts from 4241 so it is a composite; presented to Yasukuni Shrine in 2002 and displayed in the ground-floor entrance hall which can be entered without paying admission|A6M5; 零式艦上戦闘機52型; Zeke; c/n 4240; c/n 4241|Yushukan -- Yasukuni Shrine|on_display|JP
Yokosuka|D4Y|1|||Suisei|fixed_wing|monoplane|military|bomber||Rebuilt from three airframes found on Yap by Nobuhiko Endo in 1972-73 and brought to Japan in 1980 with Nippon Television's help; restored in 75 days; a composite airframe; designed under Masao Yamana of the Naval Air Technical Arsenal|D4Y; D4Y1; Suisei; 彗星11型; Judy|Yushukan -- Yasukuni Shrine|on_display|JP
Yokosuka|MXY-7|11|||Ohka|fixed_wing|monoplane|military|air_to_surface||Full-scale replica suspended above the Suisei in the main hall|MXY7; MXY-7; Ohka; 桜花11型; Baka|Yushukan -- Yasukuni Shrine|on_display|JP

### Kawaguchiko Motor Museum and Fighter Plane Museum

Curtiss|C-46|D|61-1127|Commando||fixed_wing|monoplane|military|transport||Outdoor beside the car park; hoardings rather than a fence in front of it in 2019 suggesting repainting was planned|C46; C-46D|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Lockheed|F-104|DJ|26-5007|Starfighter||fixed_wing|monoplane|military|trainer||JASDF free-loan airframe displayed on the roof of the museum entrance; the only intact two-seat Starfighter in Japan; the centre of the fin was painted yellow when inspected in 2019|F104; F-104DJ; Eiko|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
North American|F-86|F|02-7970|Sabre||fixed_wing|monoplane|military|fighter||Fuselage only displayed on a container beside the flight hall; in 2019 the wings were in the backyard|F86; F-86F; Sabre|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Nakajima|A6M|21|中島91518|Zero||fixed_wing|monoplane|military|fighter||Nakajima-built manufacturer's number 91518; recovered from Yap in the Caroline Islands in 1983 and restored here; the only Zero in Japan finished in the early grey-white scheme; displayed with wingtips folded|A6M2; 零式艦上戦闘機21型; Zeke; c/n 91518|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Nakajima|A6M|21|中島92717|Zero||fixed_wing|monoplane|military|fighter||Nakajima-built manufacturer's number 92717; displayed with the skin left off to reveal the internal structure|A6M2; 零式艦上戦闘機21型; Zeke; c/n 92717|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Nakajima|A6M|52|中島1493|Zero||fixed_wing|monoplane|military|fighter||Nakajima-built manufacturer's number 1493; recovered from Yap in the Caroline Islands and restored here; displayed wearing the tail marking 豹187|A6M5; 零式艦上戦闘機52型; Zeke; c/n 1493; 豹187|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Nakajima|Ki-43|I||Hayabusa||fixed_wing|monoplane|military|fighter||Restoration begun on display in 2013 as a fuselage only; wings had been rebuilt by 2019 and in 2021 it was suspended above the Ki-43-II|Ki43; Ki-43-I; Hayabusa; Oscar; 一式戦闘機一型|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Nakajima|Ki-43|II||Hayabusa||fixed_wing|monoplane|military|fighter||Long-running in-house restoration; shown in bare metal in August 2021|Ki43; Ki-43-II; Hayabusa; Oscar; 一式戦闘機二型|Kawaguchiko Motor Museum and Fighter Plane Museum|under_restoration|JP
Mitsubishi|G4M|22|12017|Hamaki||fixed_wing|monoplane|military|bomber||Fuselage only of airframe 12017 coded 龍41; restored a little further each year|G4M; G4M2; Betty; 一式陸上攻撃機22型; 龍41; c/n 12017|Kawaguchiko Motor Museum and Fighter Plane Museum|under_restoration|JP
Yokosuka|MXY-7|11|||Ohka|fixed_wing|monoplane|military|air_to_surface||Full-scale replica|MXY7; Ohka; 桜花|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Yokosuka|K5Y|||Akatombo||fixed_wing|biplane|military|trainer||Type 93 intermediate trainer displayed in bare metal with a red tail rather than the well-known overall orange; marked カー753|K5Y; Type 93 Intermediate Trainer; Willow; 93式中間練習機; カー753|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
Nakajima|C6N|||Saiun||fixed_wing|monoplane|military|recon||Fuselage only; listed in the specialist survey of the collection|C6N; Saiun; Myrt; 彩雲|Kawaguchiko Motor Museum and Fighter Plane Museum|under_restoration|JP
Pitts|S-2|A|JA4130|Special||fixed_wing|biplane|civilian|private||Suspended from the roof of the flight hall|Pitts S-2A; S2A; Pitts Special|Kawaguchiko Motor Museum and Fighter Plane Museum|on_display|JP
North American|F-86|F|02-7962|Sabre||fixed_wing|monoplane|military|fighter||In the backyard; painted in Blue Impulse markings and lettered 02-7960 which is FALSE — the real 02-7960 is at Hamamatsu Air Park; 962 flew with Blue Impulse around 1970-73 then went to 6 Squadron at Tsuiki and retired in standard markings|F86; F-86F; Sabre; 02-7960|Kawaguchiko Motor Museum and Fighter Plane Museum|in_storage|JP
Lockheed|T-33|A|51-5639|Shooting Star||fixed_wing|monoplane|military|trainer||In the backyard; the rear fuselage is a reproduction — the original rear fuselage and the broken fin have been seen separately on the site; the nose numbers are not the correct size|T33; T-33A|Kawaguchiko Motor Museum and Fighter Plane Museum|in_storage|JP
North American|T-6|G|52-0098|Texan||fixed_wing|monoplane|military|trainer||In the backyard; if the fuselage number 098 is correct this is the aircraft loaned by the Defence Agency to the Ishibashi Cultural Centre in Kurume on 1965-06-17 as the sea-rescue machine Matsukaze-go and displayed in its funfair until that closed on 1977-07-03; how and when it reached Kawaguchiko is unknown; present in the backyard by 2008-08-31|T6; T-6G; Texan; Matsukaze-go|Kawaguchiko Motor Museum and Fighter Plane Museum|in_storage|JP
Sikorsky|H-19|C|40012|Chickasaw||rotary_wing||military|utility||Nose section only in the backyard|H19; H-19C; S-55|Kawaguchiko Motor Museum and Fighter Plane Museum|in_storage|JP
Grumman|S2F|1|4111|Tracker||fixed_wing|monoplane|military|recon||Nose section only in the backyard; Bureau Number 136660 and manufacturer's number 569 read from the data plate; ex-JMSDF withdrawn 1975 and registered N218AK in 1978 for use as an Alaskan water bomber but never exported; a faint 11 survives on the right side of the nose|S2F-1; S-2 Tracker; BuNo 136660; c/n 569; N218AK|Kawaguchiko Motor Museum and Fighter Plane Museum|in_storage|JP

### Kure Maritime Museum -- Yamato Museum

Nakajima|A6M|62|中島82729|Zero||fixed_wing|monoplane|military|fighter||Nakajima-built manufacturer's number 82729; force-landed on Lake Biwa in August 1945 with engine trouble and raised in 1978; displayed at the Arashiyama Museum in Kyoto until it closed in 1991 then at the Shirahama Gyoen hot-spring inn Zero Park in Wakayama until that closed on 2002-03-13; bought by Kure City with a Donryu engine for about JPY 300 million and re-restored; the only A6M6 Type 62 in Japan; the re-restoration is widely criticised as poorly researched; it wears the marking 210-118/B|A6M6; 零式艦上戦闘機62型; Zeke; c/n 82729; 210-118|Kure Maritime Museum -- Yamato Museum|on_display|JP
Aichi|E16A|1|634-02|Zuiun||fixed_wing|monoplane|military|recon||Full-scale replica built about 2017; toured Fuji-Q Highland Yomiuriland and Hakkeijima before disappearing from view; unveiled beside the museum during the rebuild on 2026-01-27 and shown until 2026-04-05 then dismantled on 8-9 April and put into the museum's store; no future display date has been announced|E16A; Zuiun; Paul; 瑞雲; 634-02|Kure Maritime Museum -- Yamato Museum|in_storage|JP
Mitsubishi|F1M|2|||Zero Kanshi|fixed_wing|biplane|military|recon||Full-scale replica built for the rebuild period; the lower two thirds of the main float were never built so it sits on the floor simulating a waterborne attitude; displayed at the temporary Yamato Museum Satellite in Kure which closed when the main museum reopened on 2026-04-23; its future was unannounced as of April 2026|F1M2; Pete; 零式観測機|Kure Maritime Museum -- Yamato Museum|in_storage|JP

### Chiran Peace Museum for Kamikaze Pilots

Nakajima|Ki-84|Ia|1446|Hayate||fixed_wing|monoplane|military|fighter||The only surviving Ki-84 in the world; recovered by US forces in the Philippines in 1945 restored to flying condition by Planes of Fame and given to Japan in 1973; held successively by Fuji Heavy Industries at Utsunomiya the Arashiyama Museum in Kyoto and Shirahama in Wakayama before Chiran Town bought it; now owned by Minamikyushu City; certified 重要航空遺産 on 2023-02-14; photography is forbidden; the long-standing story that its wing spar was cut is refuted by the museum's own 2022 conservation survey which found no evidence of any cut outside the designed break points|Ki84; Ki-84-Ia; Hayate; Frank; 四式戦闘機一型甲; c/n 1446|Chiran Peace Museum for Kamikaze Pilots|on_display|JP
Mitsubishi|A6M|52c|||Zero|fixed_wing|monoplane|military|fighter||Forward half of the airframe only; ditched in May 1945 after engine failure and raised from off Tenouchi harbour Shimo-Koshikijima on 1980-06-12; the rear fuselage tore off on ditching and was lost; deliberately NOT restored and shown in as-recovered condition; the only exhibit inside the hall that may be photographed|A6M5c; 零式艦上戦闘機52型丙; Zeke|Chiran Peace Museum for Kamikaze Pilots|on_display|JP
Fuji|T-3||81-5502|||fixed_wing|monoplane|military|trainer||Outdoor and photographable at any time; JASDF free-loan airframe; withdrawn at Hofu-Kita in 2005 and installed in May 2005 replacing T-6G 52-0120; originally in standard colours and later painted overall silver retaining only the roundels the serial and the fin unit badge|T3; T-3|Chiran Peace Museum for Kamikaze Pilots|on_display|JP
Nakajima|Ki-43|IIIa||Hayabusa||fixed_wing|monoplane|military|fighter||Full-scale model used in the 2007 film 俺は君のためにこそ死ににいく; displayed as a diorama in the indoor relics room after the Hien was returned|Ki43; Ki-43-III; Hayabusa; Oscar; 一式戦闘機三型甲|Chiran Peace Museum for Kamikaze Pilots|on_display|JP
Nakajima|Ki-43|||Hayabusa||fixed_wing|monoplane|military|fighter||Nine-tenths scale model used in the 2007 film 俺は君のためにこそ死ににいく; displayed outdoors|Ki43; Hayabusa; Oscar; 一式戦闘機|Chiran Peace Museum for Kamikaze Pilots|on_display|JP
Nakajima|Ki-27|||Type 97 Fighter||fixed_wing|monoplane|military|fighter||Full-scale replica placed since about July 2020 in a surviving open revetment about 2.6 km west of the museum at 31.3600N 130.4070E; freely visible from the road across the tea fields|Ki27; Ki-27; Nate; 九七式戦闘機|Chiran Peace Museum for Kamikaze Pilots|on_display|JP

### JMSDF Kanoya Air Base Museum

Kawanishi|H8K|2|T-31|Nishiki Daitei||fixed_wing|monoplane|military|recon||The only surviving Kawanishi H8K in the world; returned by the United States and displayed at the Museum of Maritime Science in Harumi Tokyo before moving here in April 2004; kept outdoors in a typhoon belt with volcanic ashfall from Sakurajima and the specialist source judges it to be far more deteriorated than it looks|H8K2; Emily; 二式大型飛行艇; 二式大艇; T-31|JMSDF Kanoya Air Base Museum|on_display|JP
Beechcraft|B-65||6714|Queen Air||fixed_wing|monoplane|military|utility||Outdoor; used as a trainer at Tokushima; the rudder and the left aileron were already missing in March 2020|B65; B-65; Queen Air|JMSDF Kanoya Air Base Museum|on_display|JP
Fuji|KM-2||6263|||fixed_wing|monoplane|military|trainer||Outdoor; used as a trainer at Ozuki|KM2; KM-2|JMSDF Kanoya Air Base Museum|on_display|JP
Lockheed|P-2|V-7|4618|Neptune||fixed_wing|monoplane|military|recon||Outdoor; the only P2V-7 left in Japan; heavily faded and corroding by 2026|P2V-7; P2V7; Neptune|JMSDF Kanoya Air Base Museum|on_display|JP
Kawasaki|P-2|J|4771|Neptune||fixed_wing|monoplane|military|recon||Outdoor on a slope nose-high; 83 were built by Kawasaki and none was lost in service; last repainted about 2007 and badly faded by 2026|P2J; P-2J|JMSDF Kanoya Air Base Museum|on_display|JP
Kawasaki|P-2|J|4783|Neptune||fixed_wing|monoplane|military|recon||Outdoor; the last P-2J built; badly faded by 2026|P2J; P-2J|JMSDF Kanoya Air Base Museum|on_display|JP
Douglas|R4D|6Q|9023|Skytrain||fixed_wing|monoplane|military|electronic_warfare||Outdoor; the US Navy electronic-training version of the C-47B with a nose radome and a ventral radome; the only R4D-6Q left in Japan and the only DC-3 family aircraft anywhere in Japan displayed in electronic-warfare configuration — the ex-EC-46 airframes at Iruma and Tokorozawa had their radomes removed|R4D-6Q; R4D6Q; C-47J; EC-47J; Skytrain; Dakota|JMSDF Kanoya Air Base Museum|on_display|JP
Grumman|S2F|1|4131|Tracker||fixed_wing|monoplane|military|recon||Outdoor; only two complete examples survive in Japan — this and the one at JMSDF Tokushima|S2F-1; S-2 Tracker|JMSDF Kanoya Air Base Museum|on_display|JP
Beechcraft|JRB|4|6434|Expeditor||fixed_wing|monoplane|military|utility||Outdoor; one of three left in Japan the others being at JMSDF Shimofusa and a golf range in Maizuru|JRB-4; JRB4; SNB; Expeditor; Beech 18|JMSDF Kanoya Air Base Museum|on_display|JP
Beechcraft|T-34|A|9012|Mentor||fixed_wing|monoplane|military|trainer||Outdoor; installed about 2004 in place of 9006; only two ex-JMSDF T-34A survive in Japan — this and the one at Ozuki|T34; T-34A; Mentor|JMSDF Kanoya Air Base Museum|on_display|JP
ShinMaywa|US-1|A|9076|||fixed_wing|monoplane|military|search_rescue||Outdoor; built as a US-1 and later re-engined to US-1A standard; the rudder and left flap were missing in 2008 and have since been faired over with sheet metal to restore the outline|US1; US-1A|JMSDF Kanoya Air Base Museum|on_display|JP
Bell|47|G-2A|8753|Sioux||rotary_wing||military|trainer||Outdoor; the only ex-JMSDF Bell 47G-2A in Japan|Bell 47G-2A; H-13|JMSDF Kanoya Air Base Museum|on_display|JP
Kawasaki|KV-107|IIA-3|8608|||rotary_wing||military|utility||Outdoor; served with 111 Squadron at Shimofusa on mine countermeasures; faded by 2026|V-107A; KV107; KV-107IIA-3|JMSDF Kanoya Air Base Museum|on_display|JP
Sikorsky|HSS-2|A|8074|Sea King||rotary_wing||military|recon||Outdoor; the only HSS-2A left in Japan; no HSS-2 survives and four HSS-2B do|HSS2A; HSS-2A; SH-3; Sea King; S-61|JMSDF Kanoya Air Base Museum|on_display|JP
Hughes|OH-6|J|8763|Cayuse||rotary_wing||military|trainer||Outdoor; the only surviving JMSDF helicopter trainer of the OH-6 family — no JMSDF OH-6D or OH-6DA survives|OH6; OH-6J; Cayuse|JMSDF Kanoya Air Base Museum|on_display|JP
Kawasaki|P-2|J|4770|Neptune||fixed_wing|monoplane|military|recon||Nose section only displayed inside the hall|P2J; P-2J|JMSDF Kanoya Air Base Museum|on_display|JP
Sikorsky|S-61|AH|8941|Sea King||rotary_wing||military|search_rescue||Forward fuselage only displayed inside the hall with the tail cut off behind the cabin|S61; S-61AH; HSS-2B; Sea King|JMSDF Kanoya Air Base Museum|on_display|JP
Mitsubishi|A6M|52|||Zero|fixed_wing|monoplane|military|fighter||Displayed on the second floor and photographable; a COMPOSITE built in 1992 from an A6M2 Type 21 raised in Kinko Bay and an A6M5c Type 52c raised off Fukiagehama and completed as a Type 52; the cockpit can be viewed; the restoration is described by Sukenari Hirayama in 零戦かく戦かえり 文春ネスコ 2004 pp.553-565|A6M5; 零式艦上戦闘機52型; Zeke|JMSDF Kanoya Air Base Museum|on_display|JP

### Tachiarai Peace Memorial Museum

Nakajima|Ki-27|||Type 97 Fighter||fixed_wing|monoplane|military|fighter||Recovered from Hakata Bay and displayed essentially as raised but set in a three-point attitude; photography was forbidden until 2022-07-30 when the museum reviewed its rules after allowing the Zero and the Shinden to be photographed; no airframe number|Ki27; Ki-27; Nate; 九七式戦闘機|Tachiarai Peace Memorial Museum|on_display|JP
Mitsubishi|A6M|32|三菱3148|Zero||fixed_wing|monoplane|military|fighter||Mitsubishi-built manufacturer's number 3148; found on Saipan in December 1979 and imported by the Fukuoka Aerospace Association in October 1982 and restored; displayed at Nagoya Komaki airport until that exhibition hall closed in October 2004 then stored at the Onrakukan in Asakura until moving here on 2009-10-03; the only clipped-wing A6M3 Type 32 on display in Japan; wears the marking Y2-128|A6M3; 零式艦上戦闘機32型; Hamp; Zeke 32; c/n 3148; Y2-128|Tachiarai Peace Memorial Museum|on_display|JP
Mitsubishi|MH2000|A|JA003M|||rotary_wing||civilian|utility||Outdoor display; the fifth MH2000 built and the third production MH2000A of only seven of the family completed; flown until September 2004 then bought by Chikuzen Town in March 2005 and stored with the Zero at the Onrakukan in Asakura until the museum opened|MH2000; MH-2000A|Tachiarai Peace Memorial Museum|on_display|JP
Kyushu|J7W|1|||Shinden|fixed_wing|monoplane|military|fighter||Full-scale model built for the 2023 film ゴジラ-1.0 and bought for about JPY 22 million including dismantling transport and re-erection; public from 2022-07-06; the only surviving real J7W1 is a fuselage in the Smithsonian collection and is not assembled so this is the only place the canard layout can be seen in three dimensions|J7W; J7W1; Shinden; 震電|Tachiarai Peace Memorial Museum|on_display|JP
Lockheed|T-33|A|71-5293|Shooting Star||fixed_wing|monoplane|military|trainer||JASDF free-loan airframe standing in front of the old Tachiarai station building across the road from the museum at 33.4137N 130.6192E; visible 24 hours a day; the serial painted on the left canopy frame had worn away and was unreadable in 2021|T33; T-33A|Tachiarai Peace Memorial Museum|on_display|JP

### Museum of Aeronautical Sciences -- Narita

NAMC|YS-11||JA8611|||fixed_wing|monoplane|civilian|commercial_transport||Outdoor; the YS-11 prototype; cabin open to visitors|YS11; YS-11|Museum of Aeronautical Sciences -- Narita|on_display|JP
Mitsubishi|MU-2|B|JA8628|||fixed_wing|monoplane|civilian|private||Outdoor; former Mitsubishi Heavy Industries company aircraft|MU2; MU-2B|Museum of Aeronautical Sciences -- Narita|on_display|JP
Fuji|FA-200|160|JA3848|Aero Subaru||fixed_wing|monoplane|civilian|private||Outdoor|FA200; FA-200-160; Aero Subaru|Museum of Aeronautical Sciences -- Narita|on_display|JP
Fuji|FA-300||JA5258|||fixed_wing|monoplane|civilian|private||Outdoor; the FA-300 prototype; also marketed as the Rockwell Commander 700|FA300; FA-300; Fuji Model 700; Commander 700|Museum of Aeronautical Sciences -- Narita|on_display|JP
American Aviation|AA-1|Yankee|JA3613|||fixed_wing|monoplane|civilian|private||Outdoor|AA1; AA-1 Yankee|Museum of Aeronautical Sciences -- Narita|on_display|JP
Aero Commander|680|E|JA5074|||fixed_wing|monoplane|civilian|private||Outdoor; former Asia Air Survey company aircraft; ja.wikipedia gives JA5073 which is WRONG — the airframe is JA5074|Aero Commander 680E; 680E; JA5073|Museum of Aeronautical Sciences -- Narita|on_display|JP
Cessna|195||JA3007|||fixed_wing|monoplane|civilian|private||Outdoor; the former Asahi Shimbun aircraft Asakaze; ja.wikipedia gives JA3009 which is WRONG — the airframe is JA3007|Cessna 195; Asakaze; 朝風; JA3009|Museum of Aeronautical Sciences -- Narita|on_display|JP
Cessna|172|P|JA3944|Skyhawk||fixed_wing|monoplane|civilian|private||Outdoor|Cessna 172P; Skyhawk|Museum of Aeronautical Sciences -- Narita|on_display|JP
Cessna|411|A|JA5151|||fixed_wing|monoplane|civilian|private||Outdoor; former Chunichi Shimbun aircraft Ootaka|Cessna 411A; Ootaka; おおたか|Museum of Aeronautical Sciences -- Narita|on_display|JP
Cessna|421|B|JA5238|Golden Eagle||fixed_wing|monoplane|civilian|private||Outdoor; former Mainichi Shimbun aircraft Kinsei II|Cessna 421B; Golden Eagle; Kinsei II; 金星II|Museum of Aeronautical Sciences -- Narita|on_display|JP
Beechcraft|E33||JA3440|Bonanza||fixed_wing|monoplane|civilian|trainer||Outdoor; former Civil Aviation College trainer|Beech E33; Bonanza|Museum of Aeronautical Sciences -- Narita|on_display|JP
Beechcraft|56TC||JA5159|Turbo Baron||fixed_wing|monoplane|civilian|private||Outdoor; former Mainichi Shimbun aircraft Myojo|Beech 56TC; Turbo Baron; Myojo; 明星|Museum of Aeronautical Sciences -- Narita|on_display|JP
Boeing|747|212B|N642NW|||fixed_wing|monoplane|civilian|commercial_transport||Nose section only — the so-called Section 41; displayed outdoors|B747; 747-212B; Section 41; Jumbo|Museum of Aeronautical Sciences -- Narita|on_display|US
Gates Learjet|25|B|N67HB|||fixed_wing|monoplane|civilian|private||Outdoor; donated by Narita Airport Biso in December 2008; ja.wikipedia gives N25MB which is WRONG — the airframe is N67HB|Learjet 25B; N25MB|Museum of Aeronautical Sciences -- Narita|on_display|US
Aerospatiale|SA330|F|JA9512|Puma||rotary_wing||civilian|search_rescue||Outdoor; former Tokyo Fire Department Yurikamome|SA330F; Puma; Yurikamome; ゆりかもめ|Museum of Aeronautical Sciences -- Narita|on_display|JP
Kamov|Ka-26|D|JA7990|Hoodlum||rotary_wing||civilian|utility||Outdoor; coaxial-rotor helicopter and a genuine rarity in Japan|Ka26; Ka-26D; Hoodlum|Museum of Aeronautical Sciences -- Narita|on_display|JP
Sikorsky|S-62|A|JA9156|||rotary_wing||civilian|search_rescue||Outdoor; former Japan Coast Guard aircraft|S62; S-62A|Museum of Aeronautical Sciences -- Narita|on_display|JP
Hughes|369|HS|JA9298|||rotary_wing||civilian|utility||Outdoor; former Shin Nihon Helicopter company aircraft|Hughes 369HS; 500; MD500|Museum of Aeronautical Sciences -- Narita|on_display|JP
Robinson|R22|Beta|JA7758|||rotary_wing||civilian|private||Outdoor; former Honda Airways aircraft|R22; R22 Beta|Museum of Aeronautical Sciences -- Narita|on_display|JP
Kawasaki|369|HS|JA9115|||rotary_wing||civilian|search_rescue||Kawasaki-built Hughes 369HS construction number 6615; a permanent exhibit around 2010 and now in store and brought out for events; registration cancelled 1993-07-08; the left side is skinned open as a cutaway and the main rotor blades are cut short; only two 369HS were operated by the Japan Coast Guard — this and JA9113|Kawasaki-Hughes 369HS; c/n 6615|Museum of Aeronautical Sciences -- Narita|in_storage|JP

### Ishikawa Aviation Plaza

Fuji|KM-2||6288|||fixed_wing|monoplane|military|trainer||Outdoor; ex-JMSDF trainer; moved outside about 2010 to make room for indoor play equipment|KM2; KM-2|Ishikawa Aviation Plaza|on_display|JP
Sikorsky|HSS-2|B|8101|Sea King||rotary_wing||military|recon||Outdoor; ex-JMSDF; the tail rotor has been removed|HSS2B; HSS-2B; SH-3; Sea King; S-61|Ishikawa Aviation Plaza|on_display|JP
Lockheed|F-104|J|46-8539|Starfighter||fixed_wing|monoplane|military|fighter||Indoor; JASDF free-loan airframe; Mitsubishi-built; one of only three F-104J/DJ in Japan on routine indoor public display|F104; F-104J; Eiko|Ishikawa Aviation Plaza|on_display|JP
Mitsubishi|T-2||99-5163|||fixed_wing|monoplane|military|trainer||Indoor; JASDF free-loan airframe; retained its Blue Impulse scheme after leaving the team and flew for some years with the Gifu ADTW fin badge; the badge was painted out and position number 6 applied for display; Kakamigahara had also wanted this airframe|T2; T-2; Blue Impulse|Ishikawa Aviation Plaza|on_display|JP
Fuji|T-3||11-5538|||fixed_wing|monoplane|military|trainer||Indoor; JASDF free-loan airframe; delivered 2008-10-28 with wings and tailplane removed and reassembled on site — the fitters left their names and the date 2008-10-29 inside the left main-gear door|T3; T-3|Ishikawa Aviation Plaza|on_display|JP
Lockheed|T-33|A|71-5321|Shooting Star||fixed_wing|monoplane|military|trainer||Indoor; JASDF free-loan airframe; retired at Iruma; displayed with 303 Squadron markings on the right and 306 Squadron on the left at the insistence of a former 6th Air Wing commander; carried an unexplained ventral radome while based at Gifu between about 1980 and 1988 of which almost no photographs exist|T33; T-33A|Ishikawa Aviation Plaza|on_display|JP
Hughes|OH-6|J|31093|Cayuse||rotary_wing||military|recon||Indoor; ex-JGSDF observation helicopter|OH6; OH-6J; Cayuse|Ishikawa Aviation Plaza|on_display|JP
Dornier|Do 28|A-1|JA5115|||fixed_wing|monoplane|civilian|utility||Indoor; restored at JGSDF Tachikawa camp and displayed there before moving here|Do28; Do 28A-1; Skyservant|Ishikawa Aviation Plaza|on_display|JP
Beechcraft|E33||JA3442|Bonanza||fixed_wing|monoplane|civilian|private||Indoor|Beech E33; Bonanza|Ishikawa Aviation Plaza|on_display|JP
Pilatus|PC-6|B2-H2|JA8221|Turbo Porter||fixed_wing|monoplane|civilian|utility||Indoor; used on the Japanese Antarctic Research Expedition; the display area is very poorly lit|PC6; PC-6; Turbo Porter|Ishikawa Aviation Plaza|on_display|JP
Pitts|S-2|B|JA11AR|Special||fixed_wing|biplane|civilian|private||Indoor in the entrance hall; former Aerok Aerobatic Team aircraft|Pitts S-2B; S2B; Pitts Special|Ishikawa Aviation Plaza|on_display|JP
Bell|47|G-2|JA7316|Sioux||rotary_wing||civilian|utility||Indoor; pushed into a corner of the hall when inspected in 2018|Bell 47G-2; H-13|Ishikawa Aviation Plaza|on_display|JP
Mitsubishi|F-2|B||||fixed_wing|monoplane|military|fighter||Nose-section mock-up built during (X)F-2 development; displayed with an ASM-2 mock-up and a fuel tank; the matching F-2A full mock-up is at Hamamatsu Air Park|F2; F-2B mockup|Ishikawa Aviation Plaza|on_display|JP
Mitsubishi|X-2||004|Shinshin||fixed_wing|monoplane|military|test|2007|Radio-controlled scale model built by Mitsubishi in March 2007 as the fifth-phase high-manoeuvrability flight-control research prototype and used for aerodynamic evaluation ahead of the X-2; airframe 004 per the tail data plate|X2; ATD-X; Shinshin; 高運動飛行制御システム|Ishikawa Aviation Plaza|on_display|JP
Nihon University|Zephyrus|Beta|||Zephyrus Beta|fixed_wing|monoplane|civilian|experimental|1997|Human-powered aircraft suspended from the ceiling; set the then Japanese women's distance record of 1004 m on 1997-11-16|Zephyrus Beta; ゼフィルス・ベータ|Ishikawa Aviation Plaza|on_display|JP
Evans|VP-1||||Volksplane|fixed_wing|monoplane|civilian|private||Homebuilt aircraft on indoor display|VP1; VP-1; Volksplane|Ishikawa Aviation Plaza|on_display|

### Aichi Museum of Flight

NAMC|YS-11|P|52-1152|||fixed_wing|monoplane|military|transport||JASDF free-loan airframe; flew a farewell display at the Miho air base festival on 2017-05-28 and ferried to Komaki the next day for withdrawal; the museum centrepiece|YS11; YS-11P|Aichi Museum of Flight|on_display|JP
Mitsubishi|MU-2||JA8737|||fixed_wing|monoplane|civilian|private||Construction number MU-2-501; registered 1969-08-09 and cancelled 2012-12-12 and a Mitsubishi Heavy Industries company aircraft throughout; built as an MU-2-30 and converted to -35 then -36; belly-landed at Hachinohe on 1998-07-15; displayed at the Komaki-Minami works archive until that closed in May 2017|MU2; MU-2; c/n MU-2-501|Aichi Museum of Flight|on_display|JP
Mitsubishi|MU-300||JA8248|Diamond||fixed_wing|monoplane|civilian|private||The first aircraft ever certificated under the then-new FAA rules; sales were poor and the type and production rights went to Beechcraft; later adopted by the JASDF as the T-400|MU300; MU-300; Diamond; Beechjet 400; T-400|Aichi Museum of Flight|on_display|JP
Mitsubishi|MH2000|A|JA002M|||rotary_wing||civilian|utility||One of only seven MH2000 built|MH2000; MH-2000A|Aichi Museum of Flight|on_display|JP
Mitsubishi|MH2000|A|JA21ME|MuPAL-epsilon||rotary_wing||civilian|test||The JAXA research helicopter MuPAL-ε; an MH2000A rebuilt internally; distinctive instrumentation boom|MH2000; MH-2000A; MuPAL-e; MuPAL-epsilon|Aichi Museum of Flight|on_display|JP
AgustaWestland|EH101||JA01MP|Merlin||rotary_wing||civilian|utility||Former Tokyo Metropolitan Police Department aircraft; on display since 2019-02-22; the only civil-registered EH101 in Japan|EH101; EH-101; AW101; Merlin|Aichi Museum of Flight|on_display|JP
Robinson|R22|Beta|JA7787|||rotary_wing||civilian|private||Registered 1990-02-26 and destroyed on 1991-09-25 after striking a windsock at an off-airport landing site; registration cancelled 1991-10-08; later displayed at the Mitsubishi Minato Mirai Technology Museum and at Seco International at Nagoya airport before coming here; announced as a new exhibit on 2021-10-10|R22; R22 Beta|Aichi Museum of Flight|on_display|JP
Rockwell|Commander 112||JA3783|||fixed_wing|monoplane|civilian|private||Displayed outdoors at the museum car park entrance|Commander 112; Rockwell 112|Aichi Museum of Flight|on_display|JP
Nagoya Municipal Industrial High School|80-shiki Meishiko Flyer||JR1968|||fixed_wing|monoplane|civilian|experimental|2017|Built by the aircraft club of Nagoya Municipal Industrial High School after Chuhachi Ninomiya's Tamamushi-gata flying machine; made a hop of about 70 m at Karasu airfield in Tsu on 2017-01-28|八〇式名市工フライヤー; Meishiko Flyer|Aichi Museum of Flight|on_display|JP
Kawasaki|T-4||26-5805|||fixed_wing|monoplane|military|trainer||Blue Impulse markings; withdrawn from use in 2019; road-hauled in dismantled form on 2022-10-11 and formally unveiled on 2022-11-26 for the 150th anniversary of Aichi Prefecture; the installation cost JPY 84798000 in the FY2022 prefectural budget; the first Blue Impulse T-4 displayed at a civilian museum|T4; T-4; Blue Impulse|Aichi Museum of Flight|on_display|JP
Mitsubishi|A6M|52|||Zero|fixed_wing|monoplane|military|fighter||Full-scale replica built by Baba Body of Saga Prefecture and used in the films 人間の翼 君を忘れない and 永遠の０; briefly displayed at Misawa in 2010; installed here about March 2019 to replace the genuine Mitsubishi c/n 4708 which was returned to Mitsubishi|A6M5; 零式艦上戦闘機五二型|Aichi Museum of Flight|on_display|JP

### Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba

Nakajima|A6M|21|中島31870|Zero||fixed_wing|monoplane|military|fighter||Two-seat reconnaissance conversion assembled at Rabaul in 1944 from several airframes with Nakajima manufacturer's number 31870 as the main component; shot down off Lambert on New Britain on 1945-01-09; recovered in 1973 restored and bought by a Nihon University professor who gave it to the National Museum of Nature and Science; displayed at Ueno until July 2020 re-restored in 2020 and delivered here on 2021-03-18; the rear seat is a plank about 30 cm across and the reconnaissance aperture in the belly is about 10 cm across and is displayed closed|A6M2; 零式艦上戦闘機21型; Zeke; c/n 31870|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
NAMC|YS-11||JA8610|||fixed_wing|monoplane|civilian|commercial_transport||The first production YS-11; stored in a Haneda hangar after retirement and road-hauled to Chikusei overnight on 27-28 March 2020; reassembly stalled when the museum ran out of money during the pandemic and was completed after a crowdfunding appeal raised JPY 27938610 from 994 backers by 2021-11-06; completion ceremony 2021-12-11|YS11; YS-11|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Sikorsky|S-58||JA7201|Choctaw||rotary_wing||civilian|utility||Used by the third to sixth Japanese Antarctic Research Expeditions and the machine that rescued the dogs Taro and Jiro; transferred from the Maritime Safety Agency to the National Museum of Nature and Science in 1973 and stored until moved here in the early hours of 2021-03-03|S58; S-58; H-34; Choctaw|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Kawasaki|Bell 47|G-2|JA7313|Sioux||rotary_wing||civilian|utility||Construction number 218; registration cancelled 1978-03-11; a teaching airframe at Nakanihon Air Service College then given to the Helicopter History Preservation Society; road-hauled here about 2023-11-27 and moved from the Helicopter and Solar Car Hall into the air museum about 2025-04-14; the JA7313 radio callsign survives on the instrument panel|Bell 47G-2; c/n 218|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Kawasaki|369|HS|JA9204|||rotary_wing||civilian|utility||Construction number 6647; registration cancelled 1992-12-15; a teaching airframe at Nakanihon Air Service College then given to the Helicopter History Preservation Society; road-hauled here about 2023-11-27 and moved into the air museum about 2025-04-14; the right arm of the Y-shaped tail fin is not fitted|Kawasaki-Hughes 369HS; c/n 6647|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Kirigamine|Taka 7||JA2001|||fixed_wing|monoplane|civilian|private||Held by the National Museum of Nature and Science; the first glider ever entered on the Japanese civil register|霧ヶ峰式鷹7号; Taka 7|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Nihon University|Stork|B|||Stork B|fixed_wing|monoplane|civilian|experimental|1976|Human-powered aircraft built as a Nihon University graduation project; set what was then the world endurance record of 4 minutes 43 seconds on 1976-12-31|Stork B|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Fuji|FA-200|180|JA3673|Aero Subaru||fixed_wing|monoplane|civilian|private||Construction number FA200-225; registration cancelled 1992-11-27; the fuselage is cut behind the cabin and the left wing and main gear are detached and laid alongside|FA200; FA-200-180; Aero Subaru; c/n FA200-225|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Nihon Hikoki|NP-100||JQ2001|||fixed_wing|monoplane|civilian|experimental||Motor glider; development abandoned in 1978 and the airframe passed through two private collectors before returning to Nihon Hikoki and being stored at the Sugita works from 2001; Kakamigahara had negotiated for it and lost it when the first collector died; first shown to the public here about 45 years after the programme ended|NP100; NP-100; NP-100A|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Grumman|G-1159||JA8431|Gulfstream II||fixed_wing|monoplane|civilian|private||Construction number 141; registration cancelled 2020-04-08; about twenty years with the Civil Aviation Bureau then with Diamond Air Service; forward fuselage only; the Diamond Air Service titles on the upper fuselage have been repainted Hirosawa Air; no data plate was found but JA8431 is taped to the instrument panel; the cut and the scrapping of the rest were done by Econecol|G1159; Gulfstream II; GII; c/n 141|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Cessna|150|C|JA3187|||fixed_wing|monoplane|civilian|private||Construction number 15059783; registration cancelled 2014-04-18; at Propeller Cafe at Chofu in 2014 and outdoors on the Hirosawa City site from about 2015; now inside the Cactus Garden greenhouse|Cessna 150C; c/n 15059783|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Cessna|172||JA3107|Skyhawk||fixed_wing|monoplane|civilian|private||Construction number 29151; registration cancelled 1992-03-13; the first Cessna 172 imported into Japan; a teaching airframe at Osaka Aviation College around 2010 and outdoors on the Hirosawa City site from about 2015; now inside the Cactus Garden greenhouse|Cessna 172; c/n 29151|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Slingsby|T59|D|JA2140|Kestrel||fixed_wing|monoplane|civilian|private||Construction number 1773; registration cancelled 2010-06-30; inside the Cactus Garden greenhouse|T59D; Slingsby Kestrel; c/n 1773|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Slingsby|T59|A|JA2135|Kestrel||fixed_wing|monoplane|civilian|private||Construction number 1722; registration cancelled 2010-06-30; in the Glider and Model Aircraft Hall|T59A; Slingsby Kestrel; c/n 1722|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP
Nihon Hikoki|B4|PC-11AF|JA2276|||fixed_wing|monoplane|civilian|private||Construction number 1003; registration cancelled 2010-06-30; all-metal glider licence-built by Nihon Hikoki; in the Glider and Model Aircraft Hall|Pilatus B4; B4-PC11AF; c/n 1003|Kahaku-Hirosawa Air Museum -- The Hirosawa City Yumenoba|on_display|JP

### Mitsubishi Heavy Industries Oe Clock Tower Aviation Archive

Mitsubishi|A6M|52a|三菱4708|Zero||fixed_wing|monoplane|military|fighter||Mitsubishi-built manufacturer's number 4708; recovered from Yap by the Kawaguchiko Motor Museum in 1983 and given to Mitsubishi who restored it; shown under restricted access at the Komaki-Minami works archive then lent to the Aichi Museum of Flight from its opening on 2017-11-30 until 2019-04-08 and returned; on public display here since 2020-01-31; photography is forbidden|A6M5a; 零式艦上戦闘機52型甲; Zeke; c/n 4708|Mitsubishi Heavy Industries Oe Clock Tower Aviation Archive|on_display|JP
Mitsubishi|J8M|1|||Shusui|fixed_wing|monoplane|military|fighter||Restored airframe; part of the fuselage was dug up during expansion work at the Nihon Hikoki Sugita works in Kanazawa-ku Yokohama in June 1961; displayed at JASDF Gifu air base from 1963 and transferred to Mitsubishi in 1997; restoration completed December 2001 and shown at the Komaki-Minami works archive; moved here 2020-01-31; photography is forbidden|J8M; J8M1; Shusui; 秋水; Ki-200|Mitsubishi Heavy Industries Oe Clock Tower Aviation Archive|on_display|JP

### Kokukan boon

Mitsubishi|MU-2|A|JA8626|||fixed_wing|monoplane|civilian|private||Construction number MU-2-003 and the third MU-2 built; registered 1964-09-29 first flown about February 1965 and cancelled 1975-07-14; displayed on the roof of Nagoya Airport from 1975 and inside the airport Aerospace Hall from 1985-07-20 until it closed 2004-10-31; here since the museum opened 2005-04-01; Toyoyama Town's own website dates the airframe 1963 which is wrong — it flew in early 1965|MU2; MU-2A; c/n MU-2-003|Kokukan boon|on_display|JP
Kawasaki|369|HS|JA9053|||rotary_wing||civilian|utility||Construction number 6608 built 1970-09-30 per the cabin data plate; registered 1970-10-13 and cancelled 1985-12-24; the Chunichi Shimbun aircraft Akizuru|Kawasaki-Hughes 369HS; c/n 6608; Akizuru; あきづる|Kokukan boon|on_display|JP

### Shidenkai Exhibition Hall

Kawanishi|N1K|2-J|||Shiden-Kai|fixed_wing|monoplane|military|fighter||Found in November 1978 at about 40 m depth in Kura Bay off Shirohama in Minamiuwa District and raised on 1979-07-14; believed to be one of the six aircraft that failed to return from the action of 1945-07-24; the only Shiden-Kai on display in Japan and the only significant aircraft exhibit in Shikoku; free admission|N1K2-J; N1K2J; Shiden-Kai; George; 紫電改21型|Shidenkai Exhibition Hall|on_display|JP

### Bansei Tokko Peace Museum

Aichi|E13A|1|九飛41116|Zuiun||fixed_wing|monoplane|military|recon||Manufacturer's number Kyu-Hi 41116; ran out of fuel returning from a night reconnaissance towards Okinawa on 1945-06-04 and ditched with all three crew escaping; raised on 1992-08-22 from about 5 m of water some 600 m off Fukiagehama; certified 重要航空遺産 by the Japan Aeronautic Association in 2011; displayed lying as it was found on the seabed with a walkway added over the fin about April 2021|E13A; E13A1; Jake; 零式水上偵察機; 零三座水偵; c/n 41116|Bansei Tokko Peace Museum|on_display|JP

### Mitsu Seiki -- Tsubasa no Hiroba

Mitsubishi|F-1||70-8207|||fixed_wing|monoplane|military|ground_attack||Outdoor; JASDF free-loan airframe; 6 Squadron (Tsuiki) markings; preservation standard rated the best of any outdoor display in Japan|F1; F-1|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP
Fuji|T-1|B|35-5862|Hatsutaka||fixed_wing|monoplane|military|trainer||Outdoor; JASDF free-loan airframe; 5th Technical School (Komaki) fin badge|T1; T-1B|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP
Fuji|T-3||01-5533|||fixed_wing|monoplane|military|trainer||Indoor; JASDF free-loan airframe; wears the Gifu ADTW badge|T3; T-3|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP
Hughes|OH-6|D|31122|Cayuse||rotary_wing||military|recon||Indoor; ex-JGSDF; excellent condition|OH6; OH-6D; Cayuse|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP
Bell|UH-1|H|41669|Iroquois||rotary_wing||military|utility||Outdoor; ex-JGSDF; Fuji-built under licence|UH1; UH-1H; Iroquois; Huey|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP
Kawasaki|KV-107|IIA-4|51816|||rotary_wing||military|transport||Outdoor; ex-JGSDF; described by the specialist source as the best-kept outdoor airframe in Japan|V-107A; KV107; KV-107IIA-4|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP
Mitsubishi|LR-1||22004|||fixed_wing|monoplane|military|recon||Outdoor; ex-JGSDF; the ventral and aft-cabin reconnaissance camera bays can be examined closely|LR1; LR-1; MU-2|Mitsu Seiki -- Tsubasa no Hiroba|on_display|JP

### Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion

North American|F-86|D|84-8117|Sabre Dog||fixed_wing|monoplane|military|fighter||JASDF free-loan airframe held indoors; retains its original service stencilling which makes it a reference airframe — a model manufacturer is recorded as having come to survey it; 105 Squadron shachihoko fin badge with a badly faded blue band; the detached rocket pack carries 117 in red on its side; the radar dish was turned towards the visitor walkway in 2024|F86D; F-86D; Sabre Dog|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP
Toyo Koku|TT-10||JA3026|||fixed_wing|monoplane|civilian|trainer||Named in the 2009-05-18 Japan Aeronautic Association 重要航空遺産 certification 戦後航空再開時の国産航空機群; the right wing was under a tarpaulin in December 2025 apparently against a roof leak|TT10; TT-10|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP
Toyo Koku|FD-25|B|JA3092|Defender||fixed_wing|monoplane|civilian|ground_attack||Manufacturer's number 2; named in the 2009 重要航空遺産 certification; the right wing was under a tarpaulin in December 2025|FD25; FD-25B; Fletcher Defender; c/n 2|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP
Toyo Koku|FD-25|A||Defender||fixed_wing|monoplane|civilian|trainer||Named in the 2009 重要航空遺産 certification as a light attack and training aircraft|FD25; FD-25A; Fletcher Defender|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP
Yomiuri|Y-1||JA7009|||rotary_wing||civilian|utility||Named in the 2009 重要航空遺産 certification|Y1; Y-1; 読売Y-1|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP
Jiyu Koku Kenkyujo|JHX-3|||||rotary_wing||civilian|experimental||Named in the 2009 重要航空遺産 certification|JHX3; JHX-3|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP
Auster|J/5G||JA3029|Cirrus Autocar||fixed_wing|monoplane|civilian|private||Displayed with the wings removed from 2021 to 2023 and re-winged and moved by December 2025 into the space vacated by the Beechcraft 58|J5G; Auster J/5G; Cirrus Autocar|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|GB
Piper|PA-22|135|JA3036|Tri-Pacer||fixed_wing|monoplane|civilian|private||Indoor display|PA22; PA-22-135; Tri-Pacer|Tokyo Metropolitan College of Industrial Technology -- Science and Technology Pavilion|on_display|JP

### Hijiri Museum -- Ikusaka

North American|F-86|D|94-8146|Sabre Dog||fixed_wing|monoplane|military|fighter||JASDF free-loan airframe displayed outdoors; sheeted over and inaccessible from about mid-November each year until roughly April because of snow|F86D; F-86D; Sabre Dog|Hijiri Museum -- Ikusaka|on_display|JP
Lockheed|F-104|J|46-8608|Starfighter||fixed_wing|monoplane|military|fighter||Displayed outdoors; Mitsubishi-built under licence; sheeted over through the winter|F104; F-104J; Eiko|Hijiri Museum -- Ikusaka|on_display|JP

### sora Kasai -- Uzurano Airfield Site

North American|SNJ|5|6180|Texan||fixed_wing|monoplane|military|trainer||The only real airframe on the site; ex-JMSDF and displayed at the Kanoya museum until damaged around the tail and tailwheel by a typhoon about 2017; rescued rather than scrapped and moved to a restored open revetment about 800 m north-west of the sora Kasai building in September 2019; lent by 1st Air Group to the Kasai City Defence Association; still yellow in December 2019 and repainted into a wartime IJN green scheme before the spring 2020 opening; wears ツ-7 which was the marking of an actual Tsukuba air group N1K1 Shiden and NOT of this airframe|SNJ-5; SNJ5; T-6; Texan; Harvard; ツ-7|sora Kasai -- Uzurano Airfield Site|on_display|JP
Kawanishi|N1K|2-J|||Shiden-Kai|fixed_wing|monoplane|military|fighter||Full-scale replica built by Koyosha of Mito; first displayed in the Kasai City disaster-stores warehouse and moved into sora Kasai when it opened on 2022-04-18|N1K2-J; Shiden-Kai; George; 紫電改|sora Kasai -- Uzurano Airfield Site|on_display|JP
Nakajima|B5N|1|||Type 97 Carrier Attack Bomber|fixed_wing|monoplane|military|bomber||Full-scale replica built new for the 2022-04-18 opening by Koyosha of Mito for JPY 19 million; suspended from the ceiling so the cockpit and detail cannot be inspected; built to represent a Hikari 3-engined B5N1 converted to a trainer and NOT the B5N2 of Pearl Harbor and Midway|B5N; B5N1; Kate; 九七式艦上攻撃機|sora Kasai -- Uzurano Airfield Site|on_display|JP

### Yokaren Peace Memorial Museum

Mitsubishi|A6M|21|A60-05|Zero||fixed_wing|monoplane|military|fighter|2015|Full-scale replica commissioned by Ami Town in its FY2015 budget for JPY 37070000 from Koyosha of Mito; the fin marking A60-05 is invented and stands for the town's 60th anniversary and the museum's 5th; rolled out of its shelter on fine Sundays and public holidays only|A6M2; 零式艦上戦闘機21型; A60-05|Yokaren Peace Memorial Museum|on_display|JP

### Tsukuba Naval Air Group Memorial Museum

Mitsubishi|A6M|21|||Zero|fixed_wing|monoplane|military|fighter||Full-scale replica built for the film 聯合艦隊司令長官 山本五十六; displayed at Misawa until 2020-11-08 then given to this museum; the fuselage alone was shown at the Tomoa community centre by Tomobe station from mid-November 2020 and moved to the museum in spring 2022; on public display in an exhibition store near the underground command post since 2022-06-25|A6M2; 零式艦上戦闘機21型|Tsukuba Naval Air Group Memorial Museum|on_display|JP

### Daikeien -- Ichikawa

McDonnell Douglas|F-15|J|||Eagle|fixed_wing|monoplane|military|fighter||Nose section only; internationally known as the only F-15 nose anywhere from an airframe destroyed in an air-to-air engagement; displayed outdoors as an eye-catcher|F15; F-15J; Eagle|Daikeien -- Ichikawa|on_display|JP
Lockheed|F-104|J|76-8697|Starfighter||fixed_wing|monoplane|military|fighter||Displayed outdoors in pieces — nose fuselage and tail separately; Mitsubishi-built under licence|F104; F-104J; Eiko|Daikeien -- Ichikawa|on_display|JP
Lockheed|F-104|J|46-8571|Starfighter||fixed_wing|monoplane|military|fighter||Displayed outdoors as nose and fuselage sections; Mitsubishi-built under licence|F104; F-104J; Eiko|Daikeien -- Ichikawa|on_display|JP
Bell|47|G||||rotary_wing||civilian|utility||Displayed outdoors as an eye-catcher|Bell 47G|Daikeien -- Ichikawa|on_display|
Robinson|R22|||||rotary_wing||civilian|private||Displayed inside the amusement building|R22|Daikeien -- Ichikawa|on_display|

### Tsukuba Space Center -- Space Dome

NASDA|H-II|||H-II launch vehicle||missile_rocket||civilian|launch_vehicle||Test vehicle about 50 m long displayed horizontally outdoors near the main entrance; first shown at the special open day of 2007-04-21 and now a permanent exhibit|H-II; H2 rocket; H-IIロケット|Tsukuba Space Center -- Space Dome|on_display|JP

### JAXA Sagamihara Campus -- Space Science Exploration Field Center

ISAS|M-V|||M-V launch vehicle||missile_rocket||civilian|launch_vehicle||Full-scale airframe model displayed outdoors beside the M-3SII|M-V; MV rocket; M-Vロケット|JAXA Sagamihara Campus -- Space Science Exploration Field Center|on_display|JP
ISAS|M-3S|II||M-3SII launch vehicle||missile_rocket||civilian|launch_vehicle||Full-scale model displayed outdoors beside the M-V|M-3SII; M3SII; M-3SIIロケット|JAXA Sagamihara Campus -- Space Science Exploration Field Center|on_display|JP

## NOTES

### Sources and their weight

**What carried this country: 用廃機ハンターが行く！ (wrecks.hatenablog.com).** A single Japanese
enthusiast (id:Unikun) has been maintaining a per-site and per-type census of Japanese
withdrawn-from-use and preserved airframes since 2019, with a dated edit history on every post
(most of the site articles used here are on their 4th to 20th revision, several revised in 2026),
explicit site-visit dates, coordinates to four decimal places, and — critically — a habit of
publishing corrections against his own earlier work and against Wikipedia and against the
Jウイング 全国保存機・展示機ガイド supplement that he himself wrote. He is a named contributor to
that commercial guide, which makes his corrections to it first-party. This is the closest thing
Japan has to the Polish per-type lists. It is the source of nearly every serial in this file.
Its weaknesses are stated in his own posts: he does not systematically research civil light
aircraft registrations, he does not visit sites annually, and photography bans at several
museums mean he cannot confirm what he cannot see.

**Japanese Wikipedia**, second and independent. ja.wikipedia carries per-airframe serials in the
museum articles for Kakamigahara, Hamamatsu and Aichi that are as good as the blog's and in the
Kakamigahara case better (the storage-hangar inventory with registrations and the 展示が計画されて
いた機体 list are unique to it). Coordinates and postal codes throughout came from ja.wikipedia
infoboxes. BUT: ja.wikipedia is measurably wrong on civil registrations at the Museum of
Aeronautical Sciences — see Corrections. It also has NO systematic 保存機 sections for the JASDF
types (F-86F, F-104J, F-4EJ, T-2, T-33A, T-1, C-46, P-2J) that the brief expected: I searched
ja.wikipedia for those and they do not exist. The brief's model of "per-type preserved lists on
ja.wikipedia" is correct for the Zero (零式艦上戦闘機 has a 日本国内の保存施設 section) and YS-11
(静態保存機 section) and nothing else. The equivalent function is served by the blog's per-type
articles instead, which ARE systematic — F-86F, F-86D, F-104J/DJ, T-33A, T-1A/B, T-2, T-3, T-6,
T-34A, C-46, L-19, LR-1, KM-2, B-65, JRB-4, S2F-1, SNJ, HSS-2/S-61, AH-1S, CH-47J.

**Official sites**, used for access rules and opening calendars only: mod.go.jp/asdf/airpark,
mod.go.jp/msdf/kanoya, metro-cit.ac.jp (which supplies the 2009 重要航空遺産 certification text
naming six specific airframes), sorahaku.net, aichi-mof.com, pref.ishikawa.lg.jp.

**Primary/print sources cited through the above and worth a human's time**: 横山晋太郎「航空機を後世
に遺す」グランプリ出版 2018 (the Kakamigahara acquisition history, cited page-by-page in the wiki
article); 知覧特攻平和会館文化財調査報告書(1)「陸軍四式戦闘機「疾風（1446号機）」保存状態調査報告書 I」
2022年3月 (settles the Ki-84 wing-spar question); 零戦搭乗員会編「零戦、かく戦かえり！」文春ネスコ 2004
pp.553-565 (the Kanoya Zero restoration, by the man who did it).

**Not used:** aviationmuseum.eu and silverhawkauthor.com have thin and stale Japan coverage and
were not relied on for anything. Grokipedia was not used.

### Corrections made

- **Museum of Aeronautical Sciences, three registrations.** ja.wikipedia gives the Aero Commander
  680E as **JA5073** — it is **JA5074**. It gives the Cessna 195 as **JA3009** — it is **JA3007**.
  It gives the Learjet 25B as **N25MB** — it is **N67HB**. All three corrections are the specialist
  source's, made against the airframes in front of him, and all three are recorded in the rows
  with the false value carried in `aliases` so a later researcher hitting the wiki figure lands on
  the right airframe.
- **Kawaguchiko F-86F painted 02-7960.** The airframe in the Kawaguchiko backyard wears Blue
  Impulse markings and the serial **02-7960**. It is really **02-7962**. 962 flew with Blue Impulse
  around 1970-73, then went to 6 Sqn at Tsuiki, and retired in standard colours. The genuine
  02-7960 is on indoor display at Hamamatsu Air Park. Recorded as 02-7962 with the false marking
  in `aliases`.
- **Tokorozawa L-5.** The fin carries **535025**, which is an **L-5G** serial. The airframe is an
  **L-5E** and its true serial is not established. `tail_number` left BLANK and the painted marking
  put in `aliases` — this is the contract's "painted markings are frequently not the airframe's
  identity" case.
- **Tokorozawa C-46D 91-1143.** Widely published as "EC-46D". There was no EC-46D: the ECM
  conversion was designated simply "C-46 ECM型". The airframe is a C-46A converted to EC-46 and
  reconverted to transport configuration for display in 1980, and never flew as a D. Recorded as
  C-46 + D (the designation it now wears and is catalogued under) with the whole history in the
  description.
- **Misawa T-33A 81-5344 is American, not Japanese.** Retired from the JASDF, returned to the USAF
  in 2002, then loaned by the US military to Misawa City. `operator_country` = **US**, not JP. The
  same applies to the F-16A, the UP-3A (BuNo 150526) and the HondaJet demonstrator N420HA at that
  site, and to the Boeing 747 nose and the Learjet at Narita.
- **Misawa UP-3A vs UP-3C.** ja.wikipedia and the museum's own newer signage say **UP-3C**; the
  specialist source who has photographed it says **UP-3A**, BuNo 150526, and states it is the only
  UP-3A on display in the world. Recorded as UP-3A with the BuNo, which is the identity that will
  survive a re-designation dispute. Flagged for a human below.
- **Kanoya "SNJ-5" is not there any more.** ja.wikipedia's 屋外展示機 section still lists an SNJ-5
  under 過去の展示物 but many secondary lists still carry it as current. It was moved in September
  2019 to the Uzurano airfield revetment at Kasai, Hyogo, where it is recorded in this file under
  sora Kasai as 6180.
- **Bansei's "only surviving E13A" claim is wrong.** A second (incomplete — fuselage and left wing
  only) Zero-type three-seat reconnaissance seaplane exists; it was displayed at Gifu air base for
  years and moved about March 2021 to the Fuyo Museum in Buzen, Fukuoka. Not recorded as a site
  because the Fuyo Museum's access status is unresolved (see Needs a human).
- **The Yushukan does NOT hold a Ki-115 Tsurugi.** The brief lists one there. The only Ki-115 in
  Japan is at the **National Museum of Nature and Science Tsukuba Research Materials Centre**,
  disassembled into engine/fuselage/wings, NOT on public display since a brief 1985 showing at
  Kawaguchiko, shown only at the annual store open day and with photography forbidden. It is
  therefore NOT recorded as a display and NOT counted. The Yushukan's third airframe is an Ohka
  replica.
- **The National Museum of Nature and Science at Ueno no longer displays its aircraft.** The brief
  expected a Zero and a YS-11 there. The Zero (Nakajima c/n 31870) left Ueno in July 2020 and the
  first production YS-11 (JA8610) left Haneda storage in March 2020; both, plus the Antarctic S-58
  JA7201 and the glider JA2001, are now at the Kahaku-Hirosawa Air Museum at Chikusei, Ibaraki,
  which is a joint operation between the national museum and Hirosawa Shoji. Recorded there.
  Ueno itself is NOT a site record.
- **Chiran no longer holds the Hien.** Ki-61-II Kai c/n 6117 was at Chiran 1986 to August 2015 and
  is now at Kakamigahara. Many English pages still place it at Chiran.
- **Aichi Museum of Flight no longer holds a real Zero.** Mitsubishi c/n 4708 was there
  2017-11-30 to 2019-04-08 and is now at the Oe Clock Tower archive. What is at Aichi now is the
  Baba Body film replica.

### Judgment calls

- **Replicas and full-scale models are recorded, and every one says so in its description.**
  Japan's preserved-aircraft landscape is unusually replica-heavy — several are film props
  (Shinden at Tachiarai from ゴジラ-1.0; two Hayabusa at Chiran and the A6M2 at Tsukuba from
  Japanese features; the Shiden-Kai and B5N at sora Kasai purpose-built) and they are the
  headline exhibits at the sites that hold them. Excluding them would misrepresent those sites.
- **Composites are called out explicitly** because the brief is right that it matters: the Kanoya
  A6M5 is an A6M2 and an A6M5c welded into a "Type 52"; the Yushukan A6M5 is mostly c/n 4240 with
  parts of 4241; the Yushukan Suisei is three Yap airframes; the Kakamigahara KHR-1 is a rotor
  system rebuilt into a different KH-4 airframe.
- **Nose sections and partial airframes are recorded as records** (Boeing 747 Section 41 and the
  Gulfstream II forward fuselage; the C-1 nose at Tokorozawa; the P-2J nose and S-61 forward
  fuselage at Kanoya; the F-15J nose at Daikeien; the Chiran A6M5c forward half; the Kawaguchiko
  S2F-1 and H-19C noses). Each says what survives.
- **`display_status` for in-store airframes.** Tokorozawa's reserve hangar and Kakamigahara's
  reserve store hold airframes that are shown only on booked or occasional open days. Those are
  `in_storage`, not `on_display`, even though the public can sometimes see them. Hamamatsu's eight
  airframes withdrawn from view in the 2021 refit are likewise `in_storage` — they are still on
  the base but no longer part of the public display.
- **`access_type` reasoning.** `public` for Hamamatsu and Kanoya even though both sit on military
  bases, because both are purpose-built public buildings with their own free car parks reached
  without passing a gate guard (Kanoya's display area is outside the main gate entirely).
  `public` for Mitsu Seiki even though it is a private factory, because an individual can walk in
  on any working day without booking. `appointment` for Kawaguchiko (open one month a year),
  Tokyo Metropolitan College (eight named weekdays a year) and the Oe archive (compulsory advance
  online booking with fixed time slots). Daikeien is `public` — it is an arcade, not a museum, but
  the airframes are deliberately retained and freely visible.
- **`operator_country` blanks.** Left blank for airframes that never had a single national
  operator: the Wright Flyer and Grade replicas, homebuilts, the Evans VP-1, the Bell 47G and R22
  at Daikeien, the Sputnik replica. The Auster J/5G at the Tokyo college is `GB` (British-built and
  British-registered before import); the SVA 9 at Hamamatsu is `IT`; the Soyuz capsule reproduction
  and Bion 9 are `SU`.
- **Sites deliberately named with a ` -- <city>` suffix** where the bare name would collide:
  Yushukan, Museum of Aeronautical Sciences, Kure Maritime Museum, Daikeien, Hijiri Museum,
  sora Kasai, and the Kahaku-Hirosawa/Hirosawa City compound.

### EXCLUDED, and why — a well-searched zero

**Bases and monuments — out of scope for phase 1, being done in parallel:** Hyakuri Yuhien
(8 airframes: F-1, F-4EJ Kai, F-86D, F-86F, F-104J, RF-4E 901 — the only RF-4E left in Japan,
T-2 Blue Impulse, T-33A; visitable by applying at the gate Mon/Wed/Fri 13:00-15:00, Japanese
nationals only); Iruma Shubudai Memorial Hall (Ohka 11, F-1 70-8201 the first F-1, V-107A
74-4844, and the genuine 1910 Henri Farman); JASDF Ashiya, Tsuiki, Komaki, Miho, Hofu-Kita,
Kumagaya, Komatsu, Gifu; JGSDF Kisarazu, Kasumigaura, Narashino, Matsudo, Tachikawa, Asaka
(Rikkun Land), Sendai; JMSDF Shimofusa, Tokushima, Ozuki, Ominato; USAF Yokota and Misawa;
USMC Iwakuni. Each of these has published airframe-level lists on the same specialist blog and
they should go to the other agent, not be duplicated here.

**Considered and rejected as sites:**
- **National Museum of Nature and Science, Ueno.** No aircraft on display — the collection moved
  to Chikusei. Not a record.
- **Miraikan (National Museum of Emerging Science and Innovation), Odaiba.** Named in the brief.
  No preserved aircraft or spacecraft airframes; its space content is models and media. Not a
  record.
- **National Museum of Nature and Science Tsukuba Research Materials Centre.** Holds the Ki-115
  Tsurugi (the only one in Japan) but it is disassembled, not publicly displayed, shown once a
  year at a store open day, and photography is banned. Fails the "deliberate retention PLUS
  public presentation" test. Named here so nobody re-researches it.
- **Old Car Center Kudan, Fukushima.** Held 15 airframes (B-65, F-86F, three F-104J/DJ, L-19E,
  RF-4EJ nose, KM-2, T-2 nose, T-6, T-33A, UH-1B, OH-6J, KH-4, TH-55J). **ALL REMOVED in March
  2025.** Zero airframes remain. Do not re-research.
- **Minobu-cho private collection, Yamanashi.** F-86F, F-104J, T-2, T-6, T-33A, OH-6J, V-107A at
  a private house. Not open to the public in any form. Excluded.
- **Fuyo Museum, Buzen, Fukuoka.** Holds the second E13A (fuselage and left wing). Held a limited
  Thursdays-only opening in summer 2023; its website had gone by late 2022 and its current status
  is unresolved. Excluded pending a phone call — see below.
- **Ruriki Onsen "Zero Fighter Institute", Kyoto.** Its famous "Zero" was a JASDF **T-6G
  (52-0101)** in Zero-style green paint. Transferred to a private owner in Hyogo by August 2024
  and no longer publicly visible. Excluded, and named here because it is the single most common
  "Zero" misidentification in Japan.
- **Iwakuni air base A6M2 replica.** Inside the base and off the public route since the runway
  moved offshore. Excluded.
- **DOREMI COLLECTION MUSEUM, Asakuchi, Okayama** (opened 2024-04-29; a 1/1 Ki-61 replica plus a
  genuine bare-frame fuselage bought at auction from an Australian collector; booked time slots,
  from JPY 1100). A legitimate site — NOT excluded on merit, only deferred: I could not get an
  airframe-level confirmation of the genuine fuselage's provenance. See Needs a human.
- **Fully commercial "aircraft as furniture" sites** — Cessnas on shop roofs, a DH.114 on a dry
  cleaner's roof in Fuchu, a Convair 240 beside Route 25 in Suzuka, a Beech D18S at a beer garden
  in Yorii, a Cessna 340 by Route 16 at Yokota. These are single-airframe monument records, not
  museums, and belong to the monuments pass. The specialist blog's 【まとめ】民間機の展示機・教材機
  (fixed-wing, rotary-wing and glider editions, last surveyed 2024-2026) is a complete national
  gazetteer of them with registrations and coordinates and is the right starting point.

**Aircraft excluded at recorded sites:** Kakamigahara's 過去に屋内展示された機体 list (YURI-I human
-powered helicopter, OH-6J 31081 returned to the JGSDF in 2024, SS-2 JA2114, Mita 3 JA2091,
FA-200-180 JA3483 now a teaching airframe at Gifu Technical High School, BK117 prototype 2
returned to Kawasaki 2014, L-13 JA2235, Bo-dai B-5 glider returned 2011, K-14 glider, CHicK-GRX
paper aeroplane, Miracle Vehicle mock-up, AS 332 JA6669 nose, Kenzan replica nose, HOPE test
article) — all withdrawn or returned, several before 2016. Tokorozawa's disposals (KH-4 JA30213
scrapped 2021-02-19, TH-55J 61328 and UH-1B 41560 scrapped March 2020, UH-1B 41547 returned and
scrapped in the 2025 rebuild, Cessna 150L N1794Q, FA-200-180 JA3751, Fokker D.VII and SPAD S.XIII
and Wright Flyer replicas all gone by October 2024). Misawa's disposals (Tachikawa Ki-54 to
Tachihi Holdings 2020-11-08 — see below; Sikorsky S-51-1A JA7014 returned March 2021; DC-9 nose;
Pitts S-1C N122EZ). Narita's Cessna 175A JA3136 (removed between March 2024 and February 2025).
Ishikawa's TH-55J 61324 (returned and scrapped March 2019 for asbestos).

### Blank fields, deliberately

- **`year_built` is blank on almost every row.** JASDF serials are 2-2-3 with the first two digits
  being the Japanese fiscal year of the CONTRACT, and I have not converted a single one into a
  build year. IJN/IJA manufacturer's numbers do not encode dates. The only `year_built` values in
  this file come from a sourced build, first-flight or commissioning date (the Type 91 fighter
  c/n 237 built January 1933; the X-2 scale model built March 2007; the human-powered aircraft
  records; the Ami Town replica commissioned FY2015; the Aichi high-school flyer flown 2017; the
  Nihon University Stork B 1976; the C-1 68-1019 accepted 1976).
- **`tail_number` blank on the wartime Japanese airframes that genuinely have no recovered
  manufacturer's number** — the Tachiarai Ki-27, the Chiran A6M5c, the Kanoya A6M5 composite, the
  Shidenkai, the Yushukan Suisei, the Kawaguchiko Ki-43s and C6N. Where a manufacturer's number IS
  established it is in `tail_number` in the Japanese form (三菱4240, 中島91518, 川崎6117, 九飛41116)
  because that IS the airframe's identity, per the brief.
- **Coordinates blank** for the Oe archive, Kokukan boon, the Tokyo college, Hijiri Museum,
  sora Kasai, the Tsukuba Naval Air Group museum and Daikeien. No surveyed position was found for
  these and I will not invent one. Every other site has a figure taken from either a ja.wikipedia
  infobox or the specialist source's own GPS reading.
- **Postal codes blank** where no source gave one. Several are recoverable from the sites'
  official pages by a human with five minutes.
- **`operator_country` blank** as set out in Judgment calls.

### Needs a human — ranked

1. **Aichi Museum of Flight will reopen around January 2027 with a changed collection.** The
   installation of Mitsubishi SpaceJet airframe 10 requires floor space and the specialist source
   expects at least one MH2000, the EH-101 and possibly one or two light aircraft to go. Re-verify
   the whole site after reopening, and add the SpaceJet when it is installed.
   https://aichi-mof.com/ — Aichi Prefecture governor's office publishes the schedule.
2. **Tokorozawa reopens end of March 2027.** H-19C 40001, V-44A 50002 and UH-1B 41547 were all
   scheduled for scrapping. Confirm which survived, confirm whether F-86D 84-8102 and Mi-8PA
   JA9549 survived the rebuild, and confirm the C-1 nose 68-1019 is on public display.
   https://tam-web.jsf.or.jp/
3. **Shidenkai Exhibition Hall is being rebuilt** with completion targeted during FY2026 and a
   move period that had not been scheduled as of January 2025. One call to the 南レク管理事務所 or
   Ainan Town office settles whether the airframe is currently viewable and what the new site's
   address and coordinates will be. Note the published address exists in three variants and one
   misprints 御荘 as 御苑.
4. **Kanoya: is U-36A 9206 now an exhibit?** It was ferried to Kanoya after its 2025-03-10
   retirement and displayed in a hangar at the April 2025 and April 2026 air memorial events. If it
   has gone onto the outdoor line it is a new record and a genuinely rare type. Kanoya Air Base
   public affairs: https://www.mod.go.jp/msdf/kanoya/ — one call also settles the current condition
   of the H8K2, which the same source expects to be lost to corrosion or typhoon damage.
5. **Kure: where did the Zuiun and the F1M2 replicas go?** Both were built for the closure period,
   both were struck immediately before the 2026-04-23 reopening, and Kure City has published no
   future plan for either. Kure City 文化振興課 / yamato-museum.com.
6. **Misawa UP-3A vs UP-3C.** The museum's own signage and ja.wikipedia say UP-3C; the airframe
   evidence says UP-3A, BuNo 150526. One look at the data plate settles it.
   https://www.kokukagaku.jp/ tel via the museum.
7. **Tachikawa Ki-54 (the Lake Towada aircraft).** Left Misawa 2020-11-08 for Tachihi Holdings in
   Tachikawa, Tokyo, and is in a warehouse on their site. It was opened to the public for a few
   days in 2021 and 2022. If Tachihi has established any regular access this becomes a site record
   for a genuinely unique airframe — the best-preserved Japanese wartime aircraft in existence
   thanks to fresh-water immersion.
8. **Fuyo Museum, Buzen, Fukuoka** (豊前市赤熊1341-4). Holds the second E13A. Held a Thursdays-only
   limited opening June-August 2023; its website had disappeared by late 2022. Establish whether it
   is open and on what terms.
9. **DOREMI COLLECTION MUSEUM, Asakuchi, Okayama.** Opened 2024-04-29 with a 1/1 Ki-61 replica and
   reportedly a genuine Ki-61 fuselage frame bought at auction from an Australian collector.
   Confirm whether the genuine frame is displayed and what its provenance is; if so this is a
   significant new site.
10. **Tokyo Metropolitan College of Industrial Technology, full airframe list.** About 15 airframes;
    I have eight. The college publishes only the six 重要航空遺産 items. Visit on one of the eight
    2026 open days, or ask 管理課会計係施設担当 on 03-3801-2144.
11. **Tsukuba Space Center and JAXA Sagamihara item-level inventories.** Both hold substantial
    spacecraft collections (Kibo module, Kounotori, Kiku series, Daichi, Kaguya, Hayabusa,
    Hayabusa2 at Sagamihara) but neither publishes which items are flight spares, engineering
    models or display mock-ups, and none carries a public identifier. A researcher who can get an
    exhibit list from JAXA広報 would turn one thin site record each into perhaps 30 rows.
12. **Phase 2 lead list, ready to work.** The specialist blog's 【まとめ】 series is a complete
    national gazetteer with registrations and coordinates and is the single highest-yield remaining
    target: 民間機の展示機・教材科（固定翼機編 / 回転翼機編 / グライダー編）, 海上保安庁使用機,
    消防ヘリ, 警察ヘリ, お役所仕事の用廃機, plus the per-prefecture categories. It also carries
    annual 国内の用廃機動向 posts for 2020 through 2026 which are a moves-and-scrappings changelog —
    the fastest possible currency check for anything recorded here.
13. **Aviation schools and universities not worked in this pass**, each with 4-16 teaching
    airframes and each already surveyed by the same source: 中日本航空専門学校 (Gifu, 16 fixed-wing
    confirmed 2024-01), 国際航空専門学校 (Tokorozawa, ~10 fixed + 4 rotary), 大阪航空専門学校 (10
    fixed-wing), 崇城大学 (Kumamoto, 6), 日本文理大学 (Oita, 4), 日本航空学園 山梨/石川能登 campuses
    (including 4 YS-11 at Noto), 帝京大学宇都宮, 静岡理工科大学航空資料館, 奈良工業高等専門学校,
    成田国際航空専門学校. All are `appointment` sites — most open only at the annual autumn campus
    festival.
