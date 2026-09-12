# Duplicate airframes revealed by the operator_country backfill

Setting the operator country made **27 pairs** collide on
`uq_airframe (full_designation, tail_number, operator_country)`. A collision
here is not an error — it means two rows describe the same airframe and one
of them already carried a country code. Nothing was overwritten: the second
row simply kept its blank country, so both are still in the database.

Each pair needs a decision: merge the better-sourced row's detail into one
record and delete the other, or establish that they really are two airframes.

| keep? | id | designation | tail | site | vs id | site |
|---|---|---|---|---|---|---|
|  | 10708 | Cessna 421 | ST-PRC | Tigray Martyrs' Memorial Monument | 37832 | Hawulti Museum Aircraft Park -- Mekell |
|  | 10666 | Boeing 707-436 | 5X-CAU | Aero Beach | 37564 | Aero Beach Entebbe |
|  | 10694 | Boeing 720-047B | 5Y-BBX | Club 034 Kitengela | 37880 | Kitengela Boeing 720 Restaurant |
|  | 10686 | Boeing 727-25F | 5Y-BMW | Asmara Expo Park | 37601 | Asmara Expo Park Aircraft Display |
|  | 14131 | Boeing 727-22C | 9Q-CGB | Parc de la Vallée de la N'Sele | 37876 | Kingankati Airliner Display |
|  | 9928 | Boeing 737-277 | ZS-BIL | Aerotel Hoedspruit | 37581 | Air Force Base Hoedspruit Airframes |
|  | 14132 | Boeing 737-298C | 9Q-CNK | Parc de la Vallée de la N'Sele | 37877 | Kingankati Airliner Display |
|  | 10700 | Antonov An-12BP | CCCP-11815 | Massawa An-12 Roadside Display | 37951 | Massawa Antonov An-12 Display |
|  | 10805 | Consolidated B-24D | 41-24301 | Tobruk Museum | 38304 | Tobruk Museum Lady Be Good Remains |
|  | 10664 | Douglas C-47A | ET-AIA | Addis Ababa Bole International Airport | 37793 | Ethiopian Airlines DC-3 Display -- Add |
|  | 10685 | Douglas C-47A | ET-AJH | Asmara Expo Park | 37600 | Asmara Expo Park Aircraft Display |
|  | 14121 | Douglas C-47A | 9Q-CTR | Aéroport de Kinshasa-N'Dolo | 37879 | Kinshasa N'Dolo Dakota |
|  | 10693 | Beech D18S | F-BEHI | Base Aerienne 188 Djibouti | 37772 | Djibouti Air Base Gate Guards |
|  | 14140 | Dornier Do 28D-2 | 5U-MBA | Base Aérienne 101 de Niamey | 38079 | Niamey Air Base Dornier Display |
|  | 14126 | Embraer EMB-110P | TR-KNC | Base Aérienne de Libreville | 37902 | Libreville Air Base Displays |
|  | 14133 | Lockheed L-1011-500 | 9Q-CHC | Parc de la Vallée de la N'Sele | 37878 | Kingankati Airliner Display |
|  | 14122 | Lockheed L-1049H | CF-NAL | Asas d'Avião | 38180 | São Tomé Super Constellations |
|  | 14123 | Lockheed L-1049H | CF-NAM | Asas d'Avião | 38181 | São Tomé Super Constellations |
|  | 10793 | Lockheed L-749A | CN-CCN | Musee Royal Air Maroc | 37995 | Musée Royal Air Maroc -- Casablanca |
|  | 14124 | Max Holste MH.1521M | TT-KAB | Base Aérienne Adji Kosseï | 38072 | N'Djamena Broussard Display |
|  | 14125 | Max Holste MH.1521M | TR-KAB | Base Aérienne de Libreville | 37901 | Libreville Air Base Displays |
|  | 10802 | PZL-Swidnik Mi-2 | ST-SAC | Sudan Military Museum | 38279 | Sudan Military Museum -- Khartoum |
|  | 10668 | Mil Mi-26T | RA-06019 | Aero Beach | 37565 | Aero Beach Entebbe |
|  | 10680 | Piper PA-23-250 | 5X-UVS | Aero Beach | 37572 | Aero Beach Entebbe |
|  | 10797 | Stampe et Vertongen SV.4C | CN-TUJ | Musee Royal Air Maroc | 37996 | Musée Royal Air Maroc -- Casablanca |
|  | 10767 | North American T-6G | TS-APF | Houmt Souk T-6 Display | 37837 | Houmt Souk T-6 Display -- Djerba |
|  | 10821 | Vickers Viscount-748D | Z-YNA | Trim Park Aviation Museum | 38354 | Zimbabwe Military Museum |
