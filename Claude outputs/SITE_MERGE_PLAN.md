# Duplicate site records — merge plan

Every museum record was checked against every other within 300 m and in the
same country. **Nothing here has been executed** — see "Running it" at the end.

| class | pairs | what it means |
|---|---|---|
| **proven** | 51 | both records hold the same airframe, identified by tail number or construction number. No research needed. |
| type-only | 22 | both hold the same type with no serial on either side. One aircraft twice, or two of a type at co-located sites. |
| neighbours | 215 | share no airframe. Mostly legitimate: a gate guardian outside a museum's fence, two collections on one airfield. |

Executing the proven set deletes **96 duplicate aircraft rows**, relinks
**21 aircraft** to the surviving site and removes **51 museum records**.

Before anything is deleted, every field the survivor is missing is folded in
from its duplicate — tail number, construction number, operator country,
year built, aliases, and the longer description. The merge loses nothing.

## The 51 proven duplicates

`keep` is chosen by airframe count first, then by which record is more
completely filled in. `del` counts duplicate aircraft rows removed; `move`
counts aircraft unique to the losing site that are relinked instead.

| m | keep | drop | del | move | proof |
|---|---|---|---|---|---|
| 0 | **Addis Ababa Bole International Airpo** `791` (1) | Ethiopian Airlines DC-3 Display -- A `6094` (1) | 1 | 0 | C-47A ET-AIA |
| 0 | **Aero Beach** `805` (15) | Aero Beach Entebbe `6107` (10) | 8 | 2 | 707-436 5X-CAU; AS-202-18A1 AF-104 |
| 0 | **Aéroport de Kinshasa-N'Dolo** `1789` (1) | Kinshasa N'Dolo Dakota `6219` (1) | 1 | 0 | C-47A 9Q-CTR |
| 0 | **São Tomé Super Constellations** `6223` (2) | Asas d'Avião `1796` (2) | 2 | 0 | L-1049H CF-NAL; L-1049H CF-NAM |
| 0 | **N'Djamena Broussard Display** `6215` (1) | Base Aérienne Adji Kosseï `1788` (1) | 1 | 0 | MH.1521M TT-KAB |
| 0 | **Base Aérienne de Ouagadougou** `1799` (1) | Ouagadougou MiG-17 Monument `6211` (1) | 1 | 0 | MiG-17F BF8401 |
| 0 | **Pointe-Noire Air Base Displays** `6216` (2) | Base Aérienne de Pointe-Noire `1795` (2) | 1 | 1 | MiG-15UTI 102 |
| 0 | **Cite des Sciences a Tunis** `841` (3) | Cite des Sciences a Tunis Aircraft D `6077` (3) | 1 | 2 | 91D Y31001 |
| 0 | **Egyptian National Military Museum --** `6033` (6) | Egyptian National Military Museum `817` (6) | 6 | 0 | MiG-17F 2481; MiG-21F-13 5908 |
| 0 | **Guluf Airline Restaurant Ilyushin Il** `6096` (1) | Guluf Airline Restaurant `803` (1) | 1 | 0 | Il-18V EX-011 |
| 0 | **Hawulti Museum Aircraft Park -- Meke** `6091` (4) | Tigray Martyrs' Memorial Monument `794` (4) | 4 | 0 | 421 ST-PRC; Mi-24A 1621 |
| 0 | **Houmt Souk T-6 Display -- Djerba** `6080` (1) | Houmt Souk T-6 Display `843` (1) | 1 | 0 | T-6G TS-APF |
| 0 | **Hurghada Air Base MiG-21 Gate Guard** `6041` (1) | Hurghada MiG-21 Monument `822` (1) | 1 | 0 | MiG-21PFS 8047 |
| 0 | **Ismailia Air Base Preserved Aircraft** `6043` (2) | Ismailia MiG-17 Monument `824` (1) | 1 | 0 | MiG-17F 2034 |
| 0 | **Khartoum Air Base MiG-21 Gate Guard** `6087` (1) | Khartoum MiG-21 Monument `838` (1) | 1 | 0 | MiG-21M 344 |
| 0 | **Parc de la Vallée de la N'Sele** `1791` (3) | Kingankati Airliner Display `6221` (3) | 3 | 0 | 727-22C 9Q-CGB; 737-298C 9Q-CNK |
| 0 | **Massawa An-12 Roadside Display** `790` (1) | Massawa Antonov An-12 Display `6090` (1) | 1 | 0 | An-12BP CCCP-11815 |
| 0 | **Meknes Air Base Preserved Aircraft** `6072` (3) | Meknes Air Base Displays `835` (3) | 3 | 0 | F-5A 97108; F-5A 69119 |
| 0 | **Moi Air Base** `799` (1) | Moi Air Base Provost Gate Guard -- E `6105` (1) | 1 | 0 | Provost T.1 969 |
| 0 | **Moi Forces Academy Bulldog Display -** `6099` (1) | Moi Forces Academy Lanet `800` (1) | 1 | 0 | Bulldog-127 711 |
| 0 | **Musee de l Armee Populaire de Libera** `809` (1) | Musée de l'Armée de Libération Popul `6055` (1) | 1 | 0 | Mirage F1EH 167 |
| 0 | **Musee Royal Air Maroc** `836` (5) | Musée Royal Air Maroc -- Casablanca `6071` (5) | 2 | 3 | L-749A CN-CCN; SV.4C CN-TUJ |
| 0 | **Rabat-Sale Air Base Preserved Aircra** `6074` (2) | Rabat-Sale Air Base Dornier Display `837` (1) | 1 | 0 | Do 28D-2 CNA-NQ |
| 0 | **Shackleton MR.3 -- Vereeniging Road ** `6153` (1) | Vic's Viking Garage Shackleton `698` (1) | 1 | 0 | Shackleton MR.3 1723 |
| 0 | **Sousse Military Display -- Saab 91 a** `6078` (2) | Sousse Military Aircraft Display `846` (2) | 1 | 1 | 91D Y31006 |
| 0 | **Sudan Military Museum** `839` (4) | Sudan Military Museum -- Khartoum `6086` (4) | 3 | 1 | Mi-2 ST-SAC; MiG-21US 300 |
| 1 | **Amhara People's Martyrs' Memorial Mo** `793` (3) | Bahir Dar Air Base Preserved Aircraf `6092` (3) | 3 | 0 | MiG-21UM 1005; MiG-23BN 1277 |
| 1 | **Asmara Expo Park Aircraft Display** `6089` (3) | Asmara Expo Park `789` (3) | 2 | 1 | 727-25F 5Y-BMW; C-47A ET-AJH |
| 1 | **Niamey Air Base Dornier Display** `6210` (1) | Base Aérienne 101 de Niamey `1804` (1) | 1 | 0 | Do 28D-2 5U-MBA |
| 1 | **Base Aérienne 210 de Bobo-Dioulasso** `1798` (1) | Bobo-Dioulasso SF.260 Display `6212` (1) | 1 | 0 | SF.260WL BF8423 |
| 1 | **Libreville Air Base Displays** `6217` (2) | Base Aérienne de Libreville `1793` (2) | 2 | 0 | EMB-110P TR-KNC; MH.1521M TR-KAB |
| 1 | **Centre d'Information Territorial Cha** `6054` (2) | Centre d Information Territorial Cha `806` (1) | 1 | 0 | MiG-17 FR-77 |
| 1 | **Kitengela Boeing 720 Restaurant** `6098` (1) | Club 034 Kitengela `796` (1) | 1 | 0 | 720-047B 5Y-BBX |
| 1 | **Marrakech Air Base Preserved Aircraf** `6073` (3) | Ecole Royale de l Air Marrakech C-11 `833` (1) | 1 | 0 | C-119G 862 |
| 1 | **Helwan MiG-21 Monument** `6046` (1) | Helwan MiG-21 Gate Guard `821` (1) | 1 | 0 | MiG-21F-13 5617 |
| 1 | **Musée central de l'Armée -- Alger** `6052` (1) | Musee Central de l Armee `808` (1) | 1 | 0 | MiG-17 2523 |
| 1 | **Musee Militaire National du Palais d** `6076` (4) | Musee Militaire National Palais de l `845` (4) | 3 | 1 | F-5E Y92517; F-86F Y91602 |
| 1 | **Tobruk Museum Lady Be Good Remains** `6122` (1) | Tobruk Museum `832` (1) | 1 | 0 | B-24D 41-24301 |
| 3 | **AFB Waterkloof Gate Guards** `667` (4) | Air Force Base Waterkloof Gate Guard `6132` (3) | 3 | 0 | Buccaneer S.50 412; Canberra T.4 459 |
| 4 | **Air Force Base Bloemspruit Gate Guar** `6135` (1) | AFB Bloemspruit Gate Guard `664` (1) | 1 | 0 | Impala Mk I 461 |
| 9 | **Nigerian Air Force Displays -- Jos** `6189` (2) | Air Force Roundabout Jos `1805` (1) | 1 | 0 | L-29 NAF420 |
| 19 | **Sci-Bono Discovery Centre** `688` (2) | Sci-Bono Discovery Centre -- Johanne `6128` (1) | 1 | 0 | Cheetah E 826 |
| 25 | **Zimbabwe Military Museum** `6165` (13) | Trim Park Aviation Museum `850` (12) | 7 | 5 | Hunter FGA.9 1188; Provost T.52 3614 |
| 28 | **Air Force Base Hoedspruit Airframes** `6136` (2) | Aerotel Hoedspruit `668` (2) | 1 | 1 | 737-277 ZS-BIL |
| 40 | **Impala Gate Guard -- Kempton Park** `6149` (1) | Laerskool Impala Gate Guard `678` (1) | 1 | 0 | Impala Mk I 494 |
| 40 | **Mirage III Plinth -- Bonaero Park** `6152` (1) | Sir Pierre van Ryneveld High School  `689` (1) | 1 | 0 | Mirage III CZ 807 |
| 45 | **Air Force Base Langebaanweg Gate Gua** `6134` (3) | AFB Langebaanweg Heritage Displays `666` (3) | 1 | 2 | Impala Mk I 576 |
| 62 | **Djibouti Air Base Gate Guards** `6097` (6) | Base Aerienne 188 Djibouti `788` (6) | 6 | 0 | AD-4N 125741; D18S F-BEHI |
| 123 | **Museu Nacional de Historia Militar** `848` (2) | Fortaleza de São Miguel Harvards `6178` (2) | 1 | 1 | T-6G 1685 |
| 137 | **Queens Fort Military Museum -- Bloem** `6129` (3) | Queen's Fort Military Museum `684` (3) | 3 | 0 | Impala Mk I 591; Impala Mk II 1032 |
| 161 | **Thaba Tshwane Military Displays -- P** `6138` (2) | SA Air Force Headquarters Aircraft D `685` (2) | 2 | 0 | Impala Mk I 524; Mirage F1CZ 202 |

## The 22 type-only matches — one decision each

| m | record A | record B | country |
|---|---|---|---|
| 0 | Sikorsky H-19 Display -- Aburi `6203` (1) | Aburi Botanical Gardens `852` (1) | Ghana |
| 0 | Beni Suef Air Base Su-7 Gate Guard `6042` (1) | Beni Suef Su-7 Monument `812` (1) | Egypt |
| 0 | Bilbays Air Base Preserved Trainers `6050` (2) | Bilbeis Air Force Academy Display `813` (2) | Egypt |
| 0 | Cameroon Civil Aviation Authority Headqu `851` (1) | Yaoundé Fouga Magister Memorial `6214` (1) | Cameroon |
| 0 | Escuela de Suboficiales FAC Displays, Ma `1234` (2) | Comando Aéreo de Mantenimiento CAMAN Dis `1235` (1) | Colombia |
| 0 | Conservatoire d'Aéronefs CANOPEE, Châtea `2291` (49) | Conservatoire CANOPEE Châteaudun `2273` (38) | France |
| 0 | Luxor Airport Road Aircraft Monuments `6048` (4) | Luxor Military Aircraft Display `828` (3) | Egypt |
| 0 | Lycee Ibn Khaldoun T-6 Display -- Mtorre `6079` (1) | Lycee Ibn Khaldoun Aircraft Display `844` (1) | Tunisia |
| 0 | Mersa Matruh Air Base Su-17 Gate Guard `6044` (1) | Mersa Matruh Su-17 Monument `830` (1) | Egypt |
| 0 | Minya Air Base L-29 Gate Guard `6045` (1) | Minya L-29 Monument `831` (1) | Egypt |
| 0 | Stanley's Haven Piper Navajo Playground  `6106` (1) | Stanley's Haven `801` (1) | Kenya |
| 1 | Franceville Fouga Magister Display `6218` (1) | Monument Fouga Magister de Mvengue `1794` (1) | Gabon |
| 4 | Bao tang Lich su Quan su Viet Nam (Vietn `6246` (12) | Vietnam Military History Museum `637` (10) | Vietnam |
| 5 | Eagle 150B Display -- Kuala Lumpur `6282` (2) | National Museum of Malaysia `517` (1) | Malaysia |
| 11 | Independence Palace `650` (2) | Dinh Doc Lap (Independence Palace) Aircr `6251` (2) | Vietnam |
| 12 | War Remnants Museum `647` (6) | Bao tang Chung tich Chien tranh (War Rem `6249` (5) | Vietnam |
| 25 | Vietnam People's Air Force Museum `636` (28) | Bao tang Phong khong - Khong quan (Vietn `6245` (16) | Vietnam |
| 30 | B-52 Victory Museum `638` (3) | Bao tang Chien thang B52 (B-52 Victory M `6247` (2) | Vietnam |
| 47 | Ta Con Airfield Historic Site (Khe Sanh  `642` (4) | Khe Sanh Combat Base / San bay Ta Con `6255` (3) | Vietnam |
| 271 | National Aviation Museum of the Royal Th `561` (114) | Royal Thai Air Force Academy Aviation Pa `577` (8) | Thailand |
| 281 | Bao tang Chien thang B52 (B-52 Victory M `6247` (2) | Huu Tiep Lake B-52 Wreck Site `639` (1) | Vietnam |
| 286 | B-52 Victory Museum `638` (3) | Huu Tiep Lake B-52 Wreck Site `639` (1) | Vietnam |

## Running it

```bash
AIRPLANE_KEY=amt_... python3 scripts/apply_merge.py            # all 51 proven pairs
AIRPLANE_KEY=amt_... python3 scripts/apply_merge.py 6107 6094  # just these drop ids
```

The script is resumable — it records each completed pair in `merged_pairs.txt`
and skips it on a re-run — and it writes every call it makes to
`merge_actions.log`. It deletes a museum record only after that site's
aircraft have all been either merged away or successfully relinked; if any
step of a pair fails, the museum record is left alone.

`data/_research/rollback_site_merge.json` holds the complete pre-merge state
of all 213 aircraft, 51 museums and 213 links involved. `scripts/restore_merge.py`
replays it if a merge turns out to be wrong.
