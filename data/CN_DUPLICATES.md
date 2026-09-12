# Duplicate airframes revealed by the construction-number recovery

Moving construction numbers out of `aliases` into their own column made
**89 pairs** collide. `_find_aircraft_duplicate` treats a match on
manufacturer plus construction number as the same airframe *even when the
tail numbers differ* — which is exactly when a tail-based check misses a
duplicate. Nothing was overwritten; both rows of every pair are still live.

| c/n | id | designation | tail | site | vs id | tail | site |
|---|---|---|---|---|---|---|---|
| A10-307 | 26217 | Fairchild Republic A-10A | — | Don F. Pratt Memorial Museum A | 26125 | 78-0687 | Don F. Pratt Memorial Museum |
| 14284 | 26718 | Douglas A-4J | — | Memorial Park -- Oglesby | 26698 | 158479 | Veterans Memorial Park -- Dixo |
| 14284 | 26801 | Douglas A-4J | — | Veterans Memorial Park of Delt | 26698 | 158479 | Veterans Memorial Park -- Dixo |
| 14252 | 26248 | Douglas A-4M | — | Veterans Memorial Park -- D'Ib | 26200 | 158430 | Sequatchie County Veterans Mem |
| I-151 | 26716 | Grumman A-6E | — | Memorial Park -- Oglesby | 26696 | 152603 | Veterans Memorial Park -- Dixo |
| I-151 | 26769 | Grumman A-6E | — | Wayne County Indiana Veterans  | 26696 | 152603 | Veterans Memorial Park -- Dixo |
| D-071 | 25669 | Vought A-7D | — | Brooke County Veterans Memoria | 25621 | 69-6241 | Veterans Memorial Park -- Burl |
| 20063 | 25670 | Bell AH-1F | — | Brooke County Veterans Memoria | 25622 | 66-15307 | Veterans Memorial Park -- Burl |
| 20306 | 26244 | Bell AH-1F | — | Veterans Memorial Park -- D'Ib | 26189 | 67-15642 | Veterans Memorial Park of Coll |
| 20469 | 26815 | Bell AH-1F | — | American Legion Post 4 -- Moun | 26795 | 67-15805 | American Legion Post 42 -- Cha |
| 20900 | 27122 | Bell AH-1F | — | McLeod County Veterans Memoria | 27109 | 70-15956 | Veterans Memorial Park -- Brec |
| 21034 | 26218 | Bell AH-1S | — | Don F. Pratt Memorial Museum A | 26126 | 70-16090 | Don F. Pratt Memorial Museum |
| 20210 | 27188 | Bell AH-1S | — | South Dakota Veterans Park --  | 27164 | 67-15546 | Veterans Park -- Ryan |
| 1006 | 26216 | Lockheed AH-56A | — | Don F. Pratt Memorial Museum A | 26123 | 66-8831 | Don F. Pratt Memorial Museum |
| 3341701 | 33372 | Antonov An-12BP | — | Fergana House of Officers An-1 | 32748 | — | Fergana House of Officers An-1 |
| 111347315 | 12212 | Antonov An-2 | — | Patriot Park Museum Complex | 34240 | — | An-2 Monument -- Одинцовский г |
| 84-03 | 33379 | Antonov An-26 | — | Yangikurgan An-26 Monument | 32755 | — | Yangikurgan An-26 Monument |
| 2101 | 12198 | Antonov An-26KPA | — | Patriot Park Museum Complex | 34182 | RA-26642 | Одинцовский городской округ Ai |
| 10846 | 26222 | Fairchild C-119F | — | Don F. Pratt Memorial Museum A | 26124 | 131679 | Don F. Pratt Memorial Museum |
| 3948 | 26675 | Lockheed C-130E | 63-7877 | Illinois Air National Guard 18 | 26668 | 62-1862 | Scott Field Heritage Air Park |
| 19666 | 27318 | Douglas C-47A | — | Museum of Alaska Transportatio | 24868 | 43-15200 | Museum of Aviation -- Robins A |
| 16693 | 6947 | Douglas C-47B | 43-49942 | CAF National Airbase | 6927 | 44-77109 | CAF Highland Lakes Squadron |
| D143 | 26713 | Republic F-105D | — | Memorial Park -- Oglesby | 26694 | 60-0455 | Veterans Memorial Park -- Dixo |
| 0349 | 27174 | McDonnell F-4C | — | American Legion Post 4 -- Hill | 27167 | 63-7417 | American Legion Post 4655 -- C |
| unknown | 26994 | Republic F-84F | 52-6418 | 133rd Air Control Squadron --  | 24421 | 46-600 | Hancock Field Air National Gua |
| unknown | 27143 | Republic F-84F | 51-9444 | Seminole Valley Park -- Cedar  | 24421 | 46-600 | Hancock Field Air National Gua |
| unknown | 27148 | Republic F-84F | 51-1735 | Correctionville Veterans Displ | 24421 | 46-600 | Hancock Field Air National Gua |
| unknown | 27150 | Republic F-84F | 51-1818 | Fairfield Municipal Airport Di | 24421 | 46-600 | Hancock Field Air National Gua |
| unknown | 27178 | Republic F-84F | 51-1662 | Mayville Veterans Display -- M | 24421 | 46-600 | Hancock Field Air National Gua |
| 191-658 | 11535 | North American F-86F | C-113 | Museo Interfuerzas Estancia Sa | 11398 | C-111 | Escuela de Aviación Militar Có |
| 11 | 26469 | General Dynamics FB-111A | 68-0239 | K. I. Sawyer Heritage Air Muse | 26472 | 68-0239 | K. I. Sawyer Heritage Air Muse |
| 1 | 24302 | Grumman G-63 | NX41858 | Cradle of Aviation Museum | 25705 | N55RG | Sullenberger Aviation Museum |
| 2014 | 25804 | Boeing Vertol H-46HH-46D | 150941 | Eastern Carolina Aviation Heri | 25802 | 150941 | Eastern Carolina Aviation Heri |
| 22 | 11543 | FMA IA-50B | T-129 | Museo Interfuerzas Estancia Sa | 11445 | A-320 | II Brigada Aérea Paraná Histor |
| 0101 | 32591 | Ilyushin Il-86 | CCCP-86000 | Державний музей авіації Україн | 34192 | RA-10300 | Быково Aircraft Monuments |
| 5235001414208 | 12192 | Kamov Ka-27PL | — | Patriot Park Museum Complex | 34212 | — | Одинцовский городской округ Ai |
| 3538054602126 | 12182 | Kamov Ka-50 | — | Patriot Park Museum Complex | 34382 | — | Ka-50 Monument -- Одинцовский  |
| 3532434216904 | 12199 | Mil Mi-24P | 27 | Patriot Park Museum Complex | 34183 | 27 Yellow | Одинцовский городской округ Ai |
| 3532422421276 | 12177 | Mil Mi-24V | — | Patriot Park Museum Complex | 37309 | — | Mi-24 Monument -- Одинцовский  |
| 4249 | 12178 | Mil Mi-8T | 10 | Patriot Park Museum Complex | 34209 | 10 Yellow | Одинцовский городской округ Ai |
| 0390206625 | 11661 | Mikoyan-Gurevich MiG-23ML | 125 | Central Air Force Museum | 34848 | 125 Light Blue | Monino Aircraft Monuments |
| 61912538152 | 12715 | Mikoyan-Gurevich MiG-27 | 51 | Technical Museum of Vadim Zado | 12619 | — | Battle Glory of the Urals Muse |
| 2960509182 | 12209 | Mikoyan-Gurevich MiG-29-9-12 | — | Patriot Park Museum Complex | 34177 | — | Одинцовский городской округ Ai |
| 10846 | 6951 | Fairchild PT-26 | N4732G | CAF National Airbase | 26124 | 131679 | Don F. Pratt Memorial Museum |
| 11828 | 26136 | Douglas R4D-5 | 17096 | Don F. Pratt Memorial Museum | 26134 | 17096 | Don F. Pratt Memorial Museum |
| 11828 | 26223 | Douglas R4D-5 | — | Don F. Pratt Memorial Museum A | 26134 | 17096 | Don F. Pratt Memorial Museum |
| 2828 | 26280 | McDonnell Douglas RF-4C | — | East Mississippi Veterans Memo | 26251 | 67-0438 | Veterans Memorial Park -- D'Ib |
| unknown | 27152 | Republic RF-84F | 51-1948 | Harlan Municipal Airport Displ | 24421 | 46-600 | Hancock Field Air National Gua |
| 325C | 11524 | Grumman S-2G | 2-AS-24 | Museo Interfuerzas Estancia Sa | 11343 | 0703 | Base Aeronaval Comandante Espo |
| 001 | 26491 | Baker Special | — | Wurtsmith Air Museum | 26480 | N3203 | Wurtsmith Air Museum |
| 0115305 | 11799 | Sukhoi Su-24MR | 26 | Central Museum of the Armed Fo | 37273 | 37 Red | Medyn Aircraft Monuments |
| 25508601008 | 12175 | Sukhoi Su-25T | 11 | Patriot Park Museum Complex | 33973 | 11 White | Su-25 Monument -- Одинцовский  |
| 36911027514 | 12203 | Sukhoi Su-27 | — | Patriot Park Museum Complex | 33977 | — | Su-27 Monument -- Одинцовский  |
| 96310422069 | 12204 | Sukhoi Su-27UB | — | Patriot Park Museum Complex | 34211 | — | Одинцовский городской округ Ai |
| JT-66 | 29543 | Fuji T-1B | 35-5870 | Sakitama Garden -- Nihon Kokuk | 29007 | 35-5867 | JASDF Kisarazu Sub-Base -- 1st |
| 580-9753 | 26247 | Lockheed T-33A | — | Veterans Memorial Park -- D'Ib | 26199 | 53-6132 | Sequatchie County Veterans Mem |
| 580-7225 | 27102 | Lockheed T-33A | 52-9171 | American Legion Post 87 -- Ale | 10656 | 156077 | Hill Air Force Base Memorial P |
| 580-9721 | 27187 | Lockheed T-33A | — | South Dakota Veterans Park --  | 27163 | 53-6100 | Veterans Park -- Ryan |
| 580-1145 | 31091 | Lockheed T-33A | — | Wyoming National Guard Museum  | 27246 | 56-3661 | Wyoming National Guard Museum |
| 14494 | 26245 | Douglas TA-4J | — | Veterans Memorial Park -- D'Ib | 26190 | 159795 | Veterans Memorial Park of Coll |
| 504504 | 12275 | Tupolev Tu-128UT | 15 | Museum of the 514th Aircraft R | 34017 | 15 Blue | Tu-128 Monument -- Rzhev |
| 63527 | 32762 | Tupolev Tu-134B-3 | — | Gelediz Tu-134 Restaurant | 31921 | — | Gelediz Tu-134 Restaurant |
| 0032 | 26220 | Bell UH-1A | — | Don F. Pratt Memorial Museum A | 26128 | 58-2091 | Don F. Pratt Memorial Museum |
| 1090 | 23210 | Bell UH-1B | 966 | Forsvarets flysamling Gardermo | 24230 | 52-7833 | Harold F. Pitcairn Wings of Fr |
| 0032 | 26219 | Bell UH-1B | — | Don F. Pratt Memorial Museum A | 26128 | 58-2091 | Don F. Pratt Memorial Museum |
| 0926 | 27110 | Bell UH-1B | 63-8701 | Veterans Memorial Park -- Brec | 27125 | — | Veterans Memorial Park Iwo Jim |
| 10080 | 11530 | Bell UH-1H | — | Museo Interfuerzas Estancia Sa | 11325 | — | Área Material Quilmes Escuela  |
| 5803 | 25678 | Bell UH-1H | — | Vietnam Veterans Memorial -- T | 25671 | 66-16109 | Marion County Vietnam Veterans |
| 11109 | 26249 | Bell UH-1H | — | Veterans Memorial Park -- D'Ib | 26234 | 68-16450 | Jeffersontown Veterans Memoria |
| 9760 | 26794 | Bell UH-1H | — | American Legion Post 42 -- Cha | 26768 | 67-17562 | American Legion Post 423 -- Or |
| 9760 | 26814 | Bell UH-1H | — | American Legion Post 4 -- Moun | 26768 | 67-17562 | American Legion Post 423 -- Or |
| 4711 | 27161 | Bell UH-1H | — | Veterans Park -- Ryan | 27132 | 65-9667 | Sleepy Eye Veterans Park -- Sl |
| unknown | 27179 | Bell UH-1H | 73-21687 | McVille Dam Veterans Memorial  | 27160 | 70-16087 | American Legion Post 285 -- Pa |
| 11948 | 31094 | Bell UH-1H | — | VFW Post 9439 -- Casper | 27253 | 69-15660 | VFW Post 9439 -- Casper |
| 11109 | 26246 | Bell UH-1M | — | Veterans Memorial Park -- D'Ib | 26234 | 68-16450 | Jeffersontown Veterans Memoria |
| 0970603 | 11664 | Yakovlev Yak-28PP | 45 | Central Air Force Museum | 34850 | 45 Light Blue | Monino Aircraft Monuments |
| 1971105 | 11665 | Yakovlev Yak-28PP | 53 | Central Air Force Museum | 34851 | 53 Light Blue | Monino Aircraft Monuments |
| 1971002 | 11666 | Yakovlev Yak-28PP | 43 | Central Air Force Museum | 34852 | 43 Light Blue | Monino Aircraft Monuments |
| 2930105 | 11663 | Yakovlev Yak-28U | 63 | Central Air Force Museum | 34849 | 63 Blue | Monino Aircraft Monuments |
| 7977861706107 | 12365 | Yakovlev Yak-38 | 71 | Saratov State Museum of Milita | 34105 | 71 Yellow | Yak-38 Monument -- Saratov |
| 9711152 | 32757 | Yakovlev Yak-40 | — | Ashtarak Yak-40 | 31916 | — | Ashtarak Yak-40 |
| 9610147 | 32760 | Yakovlev Yak-40 | — | Sevan Yak-40 | 31919 | — | Sevan Yak-40 |
| 9611246 | 32866 | Yakovlev Yak-40 | — | Rustavi Yak-40 | 32091 | — | Rustavi Yak-40 |
| 9910404 | 32924 | Yakovlev Yak-40 | — | Osh City Park Yak-40 | 32161 | — | Osh City Park Yak-40 |
| 9030413 | 33021 | Yakovlev Yak-40 | — | Dushanbe Yak-40 Monument | 32323 | — | Dushanbe Yak-40 Monument |
| 9520441 | 33022 | Yakovlev Yak-40 | — | Tajik Technical University Yak | 32324 | — | Tajik Technical University Yak |
| 9040514 | 33368 | Yakovlev Yak-40 | — | Chimgan Mekhnat Recreation Bas | 32744 | — | Chimgan Mekhnat Recreation Bas |
| 9110216 | 33370 | Yakovlev Yak-40 | — | Dustabad Park of Culture Yak-4 | 32746 | — | Dustabad Park of Culture Yak-4 |
| 9341731 | 33374 | Yakovlev Yak-40 | — | Karshi Children's Playground Y | 32750 | — | Karshi Children's Playground Y |
