Research complete: **7 sites, 299 airframe records** for a state that had zero. Files at `/tmp/claude-0/-home-claude/e1494fa4-ac19-515f-af28-953c0b47c409/scratchpad/al/` (`sites.txt`, `aam.txt`, `smof.txt`, `rest.txt`), all field-validated (14 fields, wing_type discipline enforced).

---

# 1. SITE RECORDS

`name|city|state_province|country|postal_code|region|address|website|access_type|latitude|longitude`

```
US Army Aviation Museum|Fort Rucker|Alabama|United States|36362|North America|6000 Novosel Street Building 6000|https://www.armyaviationmuseum.org/|restricted|31.32417|-85.71306
Southern Museum of Flight|Birmingham|Alabama|United States|35206|North America|4343 73rd Street North|https://southernmuseumofflight.org/|public|33.56348|-86.73806
USS Alabama Battleship Memorial Park|Mobile|Alabama|United States|36602|North America|2703 Battleship Parkway|https://www.ussalabama.com/|public|30.68192|-88.01437
US Space and Rocket Center|Huntsville|Alabama|United States|35805|North America|1 Tranquility Base|https://www.rocketcenter.com/|public|34.71136|-86.65461
Tuskegee Airmen National Historic Site|Tuskegee|Alabama|United States|36083|North America|1616 Chappie James Avenue|https://www.nps.gov/tuai/|public|32.45917|-85.68000
US Veterans Memorial Museum|Huntsville|Alabama|United States|35801|North America|2060 Airport Road SW|https://www.memorialmuseum.org/|public|34.69207|-86.58623
Alabama Aviation College at Ozark|Ozark|Alabama|United States|36360|North America|3405 South US Highway 231|https://escc.edu/|appointment|31.43103|-85.62299
```

**Coordinate provenance:** AAM — Wikipedia's coordinate, which I reverse-geocoded and it landed *on a mapped airframe* ("Grumman OV-1B Mohawk, Andrews Avenue"), the best class of fix. SMoF, Battleship Park, USSRC, USVMM, ESCC — Nominatim returned the named POI itself, not just the street. Tuskegee — Wikipedia site coordinate; Nominatim matched only the street (32.4579/-85.6850), so this one is the weakest.

**The Fort Rucker naming question — the brief's premise needs correcting.** The brief says "renamed Fort Novosel in 2023 and renamed again in 2025." Correct, but the 2025 change went *back* to **Fort Rucker**, redesignated 11 June 2025 — now honouring Capt. Edward W. Rucker, a WWI aviator, rather than the Confederate Col. Edmund Rucker of 1942–2023. **The current name is Fort Rucker.** The installation's own site has moved to `home.army.mil/rucker/` — though that page's body text still reads "Fort Novosel, AL 36362," and the street is still Novosel Street. I used "Fort Rucker" as the city.

**Access type — the Army Aviation Museum is `restricted`, and this is a real judgment, not a formality.** Its own visit page: *"The Army Aviation Museum is located on a military installation. Gate access may require additional identification… All visitors to Fort Rucker, ages 16 and older, must have a photo ID"* and *"YOUR ID MUST BE REAL ID COMPLIANT OR HAVE A SECOND FORM OF ID."* Vehicle operators must produce licence, registration and proof of insurance; overseas visitors must clear the Provost Marshal in advance. That is a controlled military gate, so `restricted` — unlike Pearl Harbor Aviation Museum, there is no public shuttle bypassing the checkpoint. Admission itself is free. Visitor Center for gate assistance: **(334) 255-0797**; museum **(334) 598-2508**.

ESCC Ozark is `appointment`: it is a working maintenance-training campus, not a visitor attraction.

---

# 2. AIRFRAMES

`manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status`

## US Army Aviation Museum — 161 rows

```
Boeing Vertol|Model 347||65-7992||Winged Chinook|rotary_wing||military|experimental||One-off compound research conversion of a CH-47A; displayed in the outdoor airpark|BV-347;Model 347;Winged Chinook|on_display
Bell|AH-1|S|68-17109|Cobra||rotary_wing||military|ground_attack||Outdoor airpark|AH1S;HueyCobra|on_display
Lockheed|AP-2|E|131485|Neptune|Crazy Cat|fixed_wing|monoplane|military|electronic_warfare||Army SIGINT Neptune of the Crazy Cat program; museum page prints the serial as 61-31485 which is a mangled Navy BuNo; corrected to BuNo 131485 on Aerial Visuals c/n 5366 and JetPhotos|AP2E;P-2;P2V;BuNo 131485;c/n 5366|on_display
Beechcraft|C-12|C|73-22250|Huron||fixed_wing|monoplane|military|transport||Outdoor airpark|C12C;King Air 200|on_display
Sikorsky|CH-54|A|68-18438|Tarhe||rotary_wing||military|transport||Museum page calls it a CH-54B; Aerial Visuals records 68-18438 as a CH-54A c/n 64-040 and silverhawkauthor agrees; recorded as CH-54A|CH54A;S-64;Skycrane;c/n 64-040|on_display
Beechcraft|JU-21|H|70-15888|Ute||fixed_wing|monoplane|military|utility||Outdoor airpark|JU21H;U-21;King Air|on_display
North American|L-17|B|48-1046|Navion||fixed_wing|monoplane|military|utility||Outdoor airpark|L17B;Ryan Navion|on_display
Bell|OH-58|C|68-16734|Kiowa||rotary_wing||military|recon||Outdoor airpark; silverhawkauthor gives this airframe as 70-16734 - unresolved conflict|OH58C;Jet Ranger|on_display
Grumman|OV-1|B|62-5860|Mohawk||fixed_wing|monoplane|military|recon||Outdoor airpark; museum prints 62-05860|OV1B;AO-1|on_display
Cessna|T-37|A|56-3466|Tweet||fixed_wing|monoplane|military|trainer||Outdoor airpark|T37A;Tweety Bird|on_display
North American|T-39|A|61-0685|Sabreliner||fixed_wing|monoplane|military|transport||Outdoor airpark|T39A|on_display
Cessna|U-3|A|57-5863|Blue Canoe||fixed_wing|monoplane|military|utility||Outdoor airpark; formerly L-27A|U3A;L-27A;Cessna 310|on_display
Beechcraft|U-8|G|58-1359|Seminole||fixed_wing|monoplane|military|utility||Outdoor airpark; formerly L-23|U8G;L-23;Twin Bonanza|on_display
de Havilland Canada|YC-7|A|57-3080|Caribou||fixed_wing|monoplane|military|transport||Outdoor airpark|YC7A;C-7;DHC-4|on_display
Aero Commander|YU-9|A|52-6219|||fixed_wing|monoplane|military|utility||Outdoor airpark; formerly YL-26|YU9A;YL-26;Aero Commander 520|on_display
Nieuport|28|C.1|17-6531|||fixed_wing|biplane|military|fighter||Main gallery; museum lists it as 28C-1 and silverhawkauthor identifies the type as Nieuport 28C.1; the quoted serial 17-6531 does not fit a known US Army sequence and is doubted|Nieuport 28;28C1|on_display
Bell|AH-1|F|76-22600|Cobra||rotary_wing||military|ground_attack||Main gallery|AH1F|on_display
Bell|AH-1|G|66-15246|HueyCobra||rotary_wing||military|ground_attack||Main gallery|AH1G|on_display
Royal Aircraft Factory|B.E.2|c|1780|||fixed_wing|biplane|military|recon||Reproduction; main gallery|BE2C;BE-2C|on_display
Bleriot|XI|||||fixed_wing|monoplane|civilian|other||Reproduction; main gallery|Bleriot 11|on_display
Piasecki|CH-21|C|56-2040|Shawnee||rotary_wing||military|transport||Main gallery|CH21C;H-21;Flying Banana|on_display
Sikorsky|CH-37|B|55-0644|Mojave||rotary_wing||military|transport||Main gallery|CH37B;H-37;S-56|on_display
Boeing Vertol|CH-47|A|60-3451|Chinook||rotary_wing||military|transport||Main gallery|CH47A|on_display
Sikorsky|H-19|C|51-14272|Chickasaw||rotary_wing||military|transport||Main gallery|H19C;S-55|on_display
Hiller|H-23|A|51-3975|Raven||rotary_wing||military|trainer||Main gallery|H23A;UH-12;OH-23A|on_display
Piasecki|H-25|A|51-16616|Army Mule||rotary_wing||military|transport||Main gallery|H25A;HUP|on_display
Curtiss|JN-4|D|18-2780|Jenny||fixed_wing|biplane|military|trainer||Main gallery|JN4D|on_display
Cessna|L-19|A|50-1327|Bird Dog||fixed_wing|monoplane|military|recon||Main gallery|L19A;O-1;Cessna 305|on_display
Piper|L-4|A|42-15174|Grasshopper||fixed_wing|monoplane|military|recon||Main gallery|L4A;J-3 Cub|on_display
Lockheed|YAH-56|A|66-8830|Cheyenne||rotary_wing||military|ground_attack||Main gallery; compound attack helicopter prototype|YAH56A;AH-56|on_display
General Atomics|MQ-1|C|107|Warrior Alpha||fixed_wing|monoplane|military|drone||Main gallery; the quoted number 107 is also given for the museum RQ-5A Hunter and may be a manufacturer article number rather than a serial|MQ1C;Warrior Alpha;Gray Eagle|on_display
Bell|OH-13|C|48-845|Sioux||rotary_wing||military|recon||Main gallery|OH13C;Bell 47|on_display
Bell|OH-58|A|71-20468|Kiowa||rotary_wing||military|recon||Main gallery|OH58A|on_display
Bell|OH-58|D|92-00581|Kiowa Warrior||rotary_wing||military|recon||Main gallery|OH58D|on_display
Hughes|OH-6|A|68-17340|Cayuse||rotary_wing||military|recon||Main gallery|OH6A;Loach;Model 369|on_display
Radioplane|OQ-3|||||fixed_wing|monoplane|military|drone||Main gallery target drone|OQ3|on_display
Sikorsky|R-4|B|43-46592|Hoverfly||rotary_wing||military|utility||Main gallery; the Army first helicopter type|R4B;VS-316|on_display
Sikorsky|R-5|A|43-46645|Dragonfly||rotary_wing||military|utility||Main gallery; silverhawkauthor calls this airframe an R-5D|R5A;H-5;S-48|on_display
Boeing Sikorsky|RAH-66||95-00001|Comanche||rotary_wing||military|recon||Main gallery; second of two prototypes built|RAH66;Comanche|on_display
AeroVironment|RQ-11||||Raven|fixed_wing|monoplane|military|drone||Main gallery hand-launched UAS|RQ11|on_display
Honeywell|RQ-16||0507205|T-Hawk||fixed_wing||military|drone||Main gallery ducted-fan micro UAS; wing_type left blank as it is a ducted-fan lift design with no conventional wing|RQ16;T-Hawk;MAV|on_display
IAI|RQ-5|A|107|Hunter||fixed_wing|monoplane|military|drone||Main gallery; built by IAI with TRW; the quoted number 107 duplicates the museum MQ-1C entry and is doubted as a serial|RQ5A;Hunter|on_display
Alliant Techsystems|RQ-6|A|116|Outrider||fixed_wing|monoplane|military|drone||Main gallery|RQ6A;Outrider|on_display
AAI|RQ-7|A|2045|Shadow 200||fixed_wing|monoplane|military|drone||Main gallery|RQ7A;Shadow|on_display
Royal Aircraft Factory|S.E.5|a|18-0012|||fixed_wing|biplane|military|fighter||Reproduction; main gallery|SE5a;SE-5A|on_display
Hughes|TH-55|A|67-16795|Osage||rotary_wing||military|trainer||Main gallery|TH55A;Model 269|on_display
de Havilland Canada|U-1|A|57-6135|Otter||fixed_wing|monoplane|military|transport||Main gallery|U1A;DHC-3|on_display
Bell|UH-1|M|66-15156|Iroquois||rotary_wing||military|utility||Main gallery; silverhawkauthor lists this airframe as QUH-1M|UH1M;Huey|on_display
Bell|UH-1|V|70-16393|Iroquois||rotary_wing||military|search_rescue||Main gallery aeromedical Huey|UH1V;Huey|on_display
Sikorsky|UH-60|L|90-26288|Black Hawk||rotary_wing||military|utility||Main gallery; Direct Action Penetrator configuration|UH60L;DAP;Blackhawk|on_display
Wright|Model B|||||fixed_wing|biplane|civilian|other||Replica; main gallery|Wright B Flyer|on_display
Lockheed|XMQM-105||||Aquila|fixed_wing|monoplane|military|drone||Main gallery|XMQM105;Aquila|on_display
Hiller|YH-32||55-4965|Hornet||rotary_wing||military|utility||Main gallery ramjet-tipped rotor helicopter|YH32;HJ-1;Hornet|on_display
de Havilland Canada|YU-6|A|51-6263|Beaver||fixed_wing|monoplane|military|utility||Main gallery; museum lists as YL-20/YU-6A; silverhawkauthor gives 51-16263 - unresolved conflict|YU6A;YL-20;L-20;DHC-2|on_display
Bell|YUH-1|D|60-6030|Iroquois||rotary_wing||military|utility||Main gallery; museum lists as YUH-1D/H|YUH1D;Huey|on_display
Doak|VZ-4|DA|56-9642|||fixed_wing|monoplane|military|experimental||Sole VZ-4 built; transferred from the US Army Transportation Museum Fort Eustis in August 2024 and now in the galleries - this transfer is confirmed by Wikipedia and resolves the older listings that place it in Virginia|VZ4;Doak 16;VZ-4DA|on_display
Sopwith|F.1||||Camel|fixed_wing|biplane|military|fighter||Reproduction; Training Support Facility open-house display|Sopwith Camel;F1|on_display
Sikorsky|H-5|G|48-558|Dragonfly||rotary_wing||military|search_rescue||Training Support Facility open-house display|H5G;S-51|on_display
Bell|H-13|E|51-14193|Sioux||rotary_wing||military|utility||Training Support Facility open-house display|H13E;Bell 47|on_display
Hiller|H-23|B|51-16142|Raven||rotary_wing||military|trainer||Training Support Facility open-house display|H23B;UH-12|on_display
Sikorsky|H-19|D|55-3221|Chickasaw||rotary_wing||military|transport||Training Support Facility open-house display|H19D;S-55|on_display
Sikorsky|H-34|C|54-2874|Choctaw||rotary_wing||military|transport||Training Support Facility open-house display|H34C;S-58|on_display
Kaman|HOK|1|138101|Huskie||rotary_wing||military|utility||Museum page prints the serial as 61-38101 which is a mangled Navy BuNo; corrected to BuNo 138101 which the Wikipedia HH-43 survivor list places at this museum and which falls in the HOK-1 block; redesignated OH-43D; formerly displayed at the National Naval Aviation Museum Pensacola circa 1986-2001|HOK1;OH-43D;HH-43;Huskie;BuNo 138101|on_display
Stinson|L-1|A|40-3141|Vigilant||fixed_wing|monoplane|military|recon||Training Support Facility open-house display|L1A;O-49|on_display
Taylorcraft|L-2|A|42-35872|Grasshopper||fixed_wing|monoplane|military|recon||Training Support Facility open-house display|L2A;O-57|on_display
Cessna|L-19|A|51-4943|Bird Dog||fixed_wing|monoplane|military|recon||Training Support Facility open-house display|L19A;O-1|on_display
Boeing|PT-17||41-7121|Kaydet||fixed_wing|biplane|military|trainer||Training Support Facility open-house display; Stearman Model 75|PT17;Stearman;Model 75|on_display
Sikorsky|R-6|A|43-45473|Hoverfly II||rotary_wing||military|utility||Training Support Facility open-house display|R6A;S-49|on_display
Bell|207||N73927|Sioux Scout||rotary_wing||military|experimental||Training Support Facility evolutionary series; gunship testbed that led to the Cobra|Bell 207;Sioux Scout|on_display
Bell|209|||||rotary_wing||military|experimental||Training Support Facility evolutionary series; Cobra prototype; museum quotes 20001 which is the construction number not a serial|Bell 209;c/n 20001;AH-1 prototype|on_display
Bell|AH-1|G|71-15090|Cobra||rotary_wing||military|ground_attack||Training Support Facility evolutionary series|AH1G|on_display
Bell|AH-1|S|70-16072|Cobra||rotary_wing||military|ground_attack||Training Support Facility evolutionary series|AH1S|on_display
Bell|AH-1|F|67-15524|Cobra||rotary_wing||military|ground_attack||Training Support Facility evolutionary series|AH1F|on_display
Bell|AH-1|J|72-2504|SeaCobra||rotary_wing||military|ground_attack||Training Support Facility evolutionary series; the AH-1J was a Navy and export type normally carrying a BuNo so this USAF-style serial is doubted|AH1J;SeaCobra|on_display
Bell|TAH-1|S|70-15979|Cobra||rotary_wing||military|trainer||Training Support Facility evolutionary series; museum lists as N/TAH-1S|TAH1S;NTAH-1S|on_display
Bell|OH-4|A|62-4201|||rotary_wing||military|recon||Training Support Facility evolutionary series; LOH competitor; museum lists as OH-4A and silverhawkauthor as YOH-4A|OH4A;YOH-4A;Bell 206|on_display
Bell|OH-58|A|68-16687|Kiowa||rotary_wing||military|recon||Training Support Facility evolutionary series|OH58A|on_display
Bell|OH-58|C|71-20634|Kiowa||rotary_wing||military|recon||Training Support Facility evolutionary series|OH58C|on_display
Bell|OH-58|D|92-00597|Kiowa Warrior||rotary_wing||military|recon||Training Support Facility evolutionary series; museum prints 92-000597|OH58D|on_display
Bell|OH-58|F|93-00960|Kiowa Warrior||rotary_wing||military|recon||Training Support Facility evolutionary series|OH58F|on_display
Bell|XH-40||55-4459|||rotary_wing||military|experimental||Training Support Facility evolutionary series; Huey prototype|XH40;HU-1 prototype|on_display
Bell|UH-1|A|59-1695|Iroquois||rotary_wing||military|utility||Training Support Facility evolutionary series|UH1A;Huey|on_display
Bell|UH-1|B|62-1884|Iroquois||rotary_wing||military|utility||Training Support Facility evolutionary series; silverhawkauthor gives 61-1884 - unresolved conflict|UH1B;Huey|on_display
Bell|UH-1|B|62-12554|Iroquois||rotary_wing||military|utility||Training Support Facility evolutionary series|UH1B;Huey|on_display
Bell|UH-1|H|68-16404|Iroquois||rotary_wing||military|utility||Training Support Facility evolutionary series|UH1H;Huey|on_display
Bell|UH-1|M|65-9446|Iroquois||rotary_wing||military|ground_attack||Training Support Facility evolutionary series|UH1M;Huey|on_display
Bell|UH-1|V|70-16387|Iroquois||rotary_wing||military|search_rescue||Training Support Facility evolutionary series|UH1V;Huey|on_display
Lockheed|CL-475||N6940C|||rotary_wing||civilian|experimental||Training Support Facility experimental hall; rigid-rotor research helicopter|CL475|on_display
North American|F-51|D|44-72990|Mustang||fixed_wing|monoplane|military|fighter||Training Support Facility experimental hall; serial falls inside the P-51D-25-NA block 44-72027 to 44-73044|F51D;P-51D|on_display
Boeing Sikorsky|RAH-66||94-0327|Comanche||rotary_wing||military|recon||Training Support Facility experimental hall; first of two prototypes|RAH66;Comanche|on_display
Ryan|VZ-3|RY|56-6941|Vertiplane||fixed_wing|monoplane|military|experimental||Training Support Facility experimental hall|VZ3RY;Ryan 92|on_display
Sikorsky|XH-39||49-2890|||rotary_wing||military|experimental||Training Support Facility experimental hall|XH39;S-59|on_display
Lockheed|XH-51|A|61-51262|||rotary_wing||military|experimental||Training Support Facility experimental hall|XH51A|on_display
Lockheed|XH-51|A|61-51263|||rotary_wing||military|experimental||Training Support Facility experimental hall; the compound winged and jet-augmented conversion|XH51A;XH-51A Compound|on_display
Sikorsky|XH-59|A|73-21942|||rotary_wing||military|experimental||Training Support Facility experimental hall; Advancing Blade Concept demonstrator|XH59A;ABC;S-69|on_display
McDonnell|XV-1||53-4016|||rotary_wing||military|experimental||Training Support Facility experimental hall; convertiplane|XV1|on_display
Lockheed|YAH-56|A|66-8832|Cheyenne||rotary_wing||military|ground_attack||Training Support Facility experimental hall|YAH56A;AH-56|on_display
Bell|YAH-63|A|74-22247|||rotary_wing||military|ground_attack||Training Support Facility experimental hall; losing AAH competitor to the YAH-64|YAH63A;Bell 409|on_display
Hughes|YAH-64|A|74-22249|Apache||rotary_wing||military|ground_attack||Training Support Facility experimental hall; AAH prototype|YAH64A;Apache|on_display
Sikorsky|YH-18|A|49-2888|||rotary_wing||military|experimental||Training Support Facility experimental hall|YH18A;S-52|on_display
Cessna|YH-41||56-4244|Seneca||rotary_wing||military|utility||Training Support Facility experimental hall; Cessna CH-1 Skyhook|YH41;CH-1;Skyhook|on_display
Fairchild Hiller|YOH-5|A|62-4206|||rotary_wing||military|recon||Training Support Facility experimental hall; LOH competitor|YOH5A;FH-1100|on_display
Hughes|YOH-6|A|62-4213|Cayuse||rotary_wing||military|recon||Training Support Facility experimental hall; LOH competitor; Castle Air Museum has published this serial for its HH-43B which is an error - the airframe is here|YOH6A;Model 369|on_display
Sikorsky|YUH-60|A|73-21651|Black Hawk||rotary_wing||military|utility||Training Support Facility experimental hall; UTTAS prototype|YUH60A;Blackhawk|on_display
Boeing Vertol|YUH-61|A|73-21656|||rotary_wing||military|utility||Training Support Facility experimental hall; losing UTTAS competitor|YUH61A;Boeing Vertol 179|on_display
Sikorsky|Raider X||23-2500|||rotary_wing||military|experimental||Training Support Facility experimental hall; FARA competitive prototype 1; the FARA programme was cancelled in February 2024 and the museum lists the airframe as on display - arrival is sourced only to the museum own collection page|Raider X;FARA CP-1;S-97 derivative|on_display
Bell|360||23-2501|Invictus||rotary_wing||military|experimental||Training Support Facility experimental hall; FARA competitive prototype 2; arrival is sourced only to the museum own collection page|Bell 360;Invictus;FARA CP-2|on_display
Sikorsky Boeing|SB-1||N100FV|Defiant||rotary_wing||military|experimental||Training Support Facility experimental hall; JMR-TD compound demonstrator donated to the museum as reported by TWZ in November 2024|SB1;SB>1 Defiant;Defiant|on_display
Interstate|L-6|A|43-2560|Grasshopper||fixed_wing|monoplane|military|recon||Storage|L6A;Cadet;S-1B|in_storage
Convair|L-13|A|46-159|||fixed_wing|monoplane|military|utility||Storage|L13A;Stinson L-13|in_storage
Piper|L-18|C|52-2536|Super Cub||fixed_wing|monoplane|military|trainer||Storage|L18C;PA-18|in_storage
Piper|L-21|A|51-15782|Super Cub||fixed_wing|monoplane|military|recon||Storage|L21A;PA-18|in_storage
Cessna|LC-126|C|51-6998|||fixed_wing|monoplane|military|utility||Storage|LC126C;Cessna 195|in_storage
Beechcraft|RC-12|D|80-23376|Huron||fixed_wing|monoplane|military|electronic_warfare||Storage|RC12D;Guardrail;King Air|in_storage
Beechcraft|RU-8|D|56-3712|Seminole||fixed_wing|monoplane|military|electronic_warfare||Storage|RU8D;L-23;Twin Bonanza|in_storage
North American|T-28|B|53-7747|Trojan||fixed_wing|monoplane|military|trainer||Storage; the T-28B was a Navy type normally carrying a BuNo so this USAF-style serial is doubted|T28B;Trojan|in_storage
Beechcraft|T-34|C|160464|Turbo Mentor||fixed_wing|monoplane|military|trainer||Storage; museum page prints 16-0464 which is the Navy BuNo 160464 with a spurious hyphen; 160464 falls inside the T-34C block|T34C;Turbo Mentor;BuNo 160464|in_storage
Beechcraft|T-42|A|65-12697|Cochise||fixed_wing|monoplane|military|trainer||Storage|T42A;Baron 95-B55|in_storage
Cessna|T-41|B|67-15161|Mescalero||fixed_wing|monoplane|military|trainer||Storage|T41B;Cessna 172|in_storage
Helio|YL-24||52-2540|Courier||fixed_wing|monoplane|military|utility||Storage|YL24;Courier|in_storage
Grumman|YOV-1|A|57-6539|Mohawk||fixed_wing|monoplane|military|recon||Storage|YOV1A;YAO-1|in_storage
Boeing|CH-47|D|87-0108|Chinook||rotary_wing||military|transport||Storage|CH47D|in_storage
Del Mar|DHT-1|A|002|Whirlymite||rotary_wing||military|experimental||Storage; one-man helicopter|DHT1A;Whirlymite|in_storage
Sikorsky|EH-60|A|85-24474|Black Hawk||rotary_wing||military|electronic_warfare||Storage|EH60A;Quick Fix;Blackhawk|in_storage
Bell|H-13|B|48-827|Sioux||rotary_wing||military|utility||Storage|H13B;Bell 47|in_storage
Sikorsky|H-34|A|53-4526|Choctaw||rotary_wing||military|transport||Storage|H34A;S-58;CH-34A|in_storage
Sikorsky|MH-60|K|91-26373|Black Hawk||rotary_wing||military|utility||Storage; special operations variant|MH60K;Blackhawk|in_storage
Hiller|OH-23|F|62-12508|Raven||rotary_wing||military|utility||Storage|OH23F;UH-12|in_storage
Bell|UH-1|B|60-3553|Iroquois||rotary_wing||military|utility||Storage|UH1B;Huey|in_storage
Bell|UH-1|H|68-15595|Iroquois||rotary_wing||military|utility||Storage|UH1H;Huey|in_storage
Radioplane|OQ-19||||Basic Training Target|fixed_wing|monoplane|military|drone||Storage; museum lists as OQ-19B/D|OQ19;BTT;KD2R|in_storage
Northrop|MQM-57|B|||Falconer|fixed_wing|monoplane|military|drone||Storage; museum lists as SD-1|MQM57B;SD-1;Falconer|in_storage
Windecker|YE-5|A|N4196G|Eagle||fixed_wing|monoplane|military|test||Storage; composite-airframe research aircraft|YE5A;Windecker Eagle|in_storage
Ryan|XV-5|B|62-4506|Vertifan||fixed_wing|monoplane|military|experimental||Storage; museum prints 62-04506|XV5B;Vertifan|in_storage
Brantly|YHO-3|BR|58-1496|||rotary_wing||military|recon||Training Support Facility non-public storage|YHO3BR;Brantly B-2|in_storage
McCulloch|YH-30||52-5837|||rotary_wing||military|experimental||Training Support Facility non-public storage; silverhawkauthor gives 52-583 - unresolved conflict|YH30;MC-4C|in_storage
American Helicopter|XH-26||50-1840|Jet Jeep||rotary_wing||military|experimental||Training Support Facility non-public storage|XH26;Jet Jeep|in_storage
Stinson|L-5|G|45-34985|Sentinel||fixed_wing|monoplane|military|recon||Training Support Facility non-public storage|L5G;Sentinel|in_storage
Hiller|YH-32||55-4963|Hornet||rotary_wing||military|utility||Training Support Facility non-public storage|YH32;HJ-1|in_storage
Hiller|XROE|1|4004|Rotorcycle||rotary_wing||military|utility||Training Support Facility non-public storage|XROE1;Rotorcycle|in_storage
Curtiss-Wright|VZ-7|AP|58-5508|Flying Jeep||rotary_wing||military|experimental||Training Support Facility non-public storage|VZ7AP;Flying Jeep|in_storage
Aeronca|L-16|A|47-924|Champion||fixed_wing|monoplane|military|recon||Training Support Facility non-public storage|L16A;Champ;7BCM|in_storage
Stinson|L-5||42-99103|Sentinel||fixed_wing|monoplane|military|recon||Training Support Facility non-public storage; silverhawkauthor identifies this airframe as an L-5B|L5;Sentinel|in_storage
Piper|L-4|B|43-515|Grasshopper||fixed_wing|monoplane|military|recon||Training Support Facility non-public storage|L4B;J-3 Cub|in_storage
Bell|TH-13|T|67-17024|Sioux||rotary_wing||military|trainer||Training Support Facility non-public storage|TH13T;Bell 47G-3B|in_storage
Lockheed|X-26|B|67-15345|||fixed_wing|monoplane|military|test||Training Support Facility non-public storage; Quiet Thruster quiet-aircraft research glider|X26B;QT-2;Quiet One|in_storage
Boeing|YL-15|A|47-429|Scout||fixed_wing|monoplane|military|recon||Training Support Facility non-public storage|YL15A;Scout|in_storage
Cessna|L-19|A|51-12349|Bird Dog||fixed_wing|monoplane|military|recon||Training Support Facility non-public storage|L19A;O-1|in_storage
Hughes|OH-6|A|65-12917|Cayuse||rotary_wing||military|recon||Training Support Facility non-public storage; silverhawkauthor records this airframe as the NOTAR testbed|OH6A;NOTAR;Model 369|in_storage
Hughes|TH-55|A|67-16966|Osage||rotary_wing||military|trainer||Training Support Facility non-public storage; silverhawkauthor gives 67-16963 - unresolved conflict|TH55A;Model 269|in_storage
Firestone|XR-9|B|46-001|||rotary_wing||military|experimental||Training Support Facility non-public storage|XR9B;Firestone 45|in_storage
Boeing|A160||A015|Hummingbird||rotary_wing||military|drone||Training Support Facility non-public storage|A160;Hummingbird|in_storage
General Atomics|MQ-1|C|0700114|Gray Eagle||fixed_wing|monoplane|military|drone||Training Support Facility non-public storage|MQ1C;Gray Eagle|in_storage
IAI|MQ-5|B|||Hunter|fixed_wing|monoplane|military|drone||Training Support Facility non-public storage; museum lists as MQ-5B U-Wing|MQ5B;Hunter;U-Wing|in_storage
Bell|TH-67||00-67446|Creek||rotary_wing||military|trainer||Training Support Facility non-public storage; the quoted serial format does not match Army TH-67 practice and is doubted|TH67;Creek;Bell 206B-3|in_storage
Boeing|AH-64|D|00-05198|Apache Longbow||rotary_wing||military|ground_attack||In maintenance|AH64D;Apache Longbow|under_restoration
Boeing|P-12|E||||fixed_wing|biplane|military|fighter||Replica; in maintenance|P12E;Boeing 100|under_restoration
Laister-Kauffman|TG-4|A|43-53083|Yankee Doodle 2||fixed_wing|monoplane|military|trainer||Training glider; in maintenance|TG4A;LK-10A|under_restoration
Sikorsky|S-72||N740|RSRA||rotary_wing||military|test||Rotor Systems Research Aircraft; in maintenance; the museum also lists an S-67 with the same numbers which appears to be a duplicate of this entry|S72;RSRA;c/n 545|under_restoration
Cessna|O-2|A|67-21414|Skymaster||fixed_wing|monoplane|military|recon||In maintenance|O2A;Cessna 337|under_restoration
Boeing Vertol|ACH-47|A|64-13149|Chinook|Easy Money|rotary_wing||military|ground_attack||Guns-A-Go-Go armed Chinook and the sole survivor of four; museum page prints 64-131149 with a duplicated digit; corrected to 64-13149 c/n B121 on Aerial Visuals and the serial falls inside the FY64 CH-47A block|ACH47A;Guns-A-Go-Go;Easy Money;c/n B121|under_restoration
```

## Southern Museum of Flight — 96 rows

```
Lockheed|A-12||60-6937|Oxcart||fixed_wing|monoplane|military|recon||CIA Oxcart article 131; first A-12 deployed to Kadena for Operation Black Shield and flew the first A-12 combat mission on 22 May 1967 the final Black Shield mission on 8 May 1968 and the last A-12 flight on 21 June 1968; moved here from Lockheed Skunk Works Palmdale in February 2000; 345.75 hours in 177 missions|A12;Article 131;Blackbird;Oxcart|on_display
Convair|TF-102|A|56-2352|Delta Dagger||fixed_wing|monoplane|military|trainer||Serial confirmed on Aerial Visuals as TF-102A-41-CO|TF102A;F-102|on_display
General Dynamics|F-111|A|67-0069|Aardvark||fixed_wing|monoplane|military|bomber||Serial confirmed on Aerial Visuals as F-111A c/n A1-114|F111A;Aardvark;c/n A1-114|on_display
Grumman|F-14|A|162600|Tomcat||fixed_wing|monoplane|military|fighter||Serial confirmed on Aerial Visuals as F-14A-135-GR c/n 522|F14A;Tomcat;c/n 522|on_display
Grumman|F-14|A|162608|Tomcat||fixed_wing|monoplane|military|fighter||Serial confirmed on Aerial Visuals as F-14A-135-GR|F14A;Tomcat|on_display
Lockheed|F-104|C|56-0929|Starfighter||fixed_wing|monoplane|military|fighter|||F104C;Starfighter|on_display
LTV|A-7|E|159278|Corsair II||fixed_wing|monoplane|military|ground_attack||Serial confirmed on Aerial Visuals as A-7E-15-CV c/n E-349|A7E;Corsair II;c/n E-349|on_display
McDonnell|F-101|B|56-0273|Voodoo||fixed_wing|monoplane|military|fighter|||F101B;Voodoo|on_display
McDonnell|RF-4|C|63-7745|Phantom II||fixed_wing|monoplane|military|recon||Formerly displayed in the Alabama Air National Guard air park at Birmingham; silverhawkauthor lists it at both places which is a duplication|RF4C;Phantom|on_display
McDonnell|F-4|N|152996|Phantom II||fixed_wing|monoplane|military|fighter|||F4N;Phantom|on_display
Mikoyan-Gurevich|MiG-15|||||fixed_wing|monoplane|military|fighter||Korean War Jets exhibit; silverhawkauthor quotes 2057 which is a construction or bort number rather than a serial so tail_number is left blank|MiG15;Fagot;2057|on_display
Mikoyan-Gurevich|MiG-21|UM||Mongol B||fixed_wing|monoplane|military|trainer|||MiG21UM;Mongol|on_display
North American|F-86|F||Sabre||fixed_wing|monoplane|military|fighter||silverhawkauthor quotes 12910 which is an incomplete serial so tail_number is left blank|F86F;Sabre;12910|on_display
North American|F-86|D|52-4243|Sabre Dog||fixed_wing|monoplane|military|fighter|||F86D;Sabre Dog|on_display
North American|F-100|C|54-1753|Super Sabre||fixed_wing|monoplane|military|fighter|||F100C;Super Sabre;Hun|on_display
Republic|F-84|F|51-9404|Thunderstreak||fixed_wing|monoplane|military|ground_attack|||F84F;Thunderstreak|on_display
Republic|RF-84|F|52-7409|Thunderflash||fixed_wing|monoplane|military|recon||Formerly displayed in the Alabama Air National Guard air park at Birmingham; silverhawkauthor calls it an F-84F Thunderstreak in one place which is wrong for the RF-84F photo variant|RF84F;Thunderflash|on_display
Republic|F-105|F|63-8365|Thunderchief||fixed_wing|monoplane|military|ground_attack||Serial confirmed on Aerial Visuals as F-105F-1-RE c/n F142|F105F;Thunderchief;Thud;c/n F142|on_display
Republic|F-84|F|51-1487|Thunderstreak||fixed_wing|monoplane|military|ground_attack||Unrestored project airframe; silverhawkauthor labels it RF-84F-15-RE which conflicts with the F-84F designation it also gives|F84F;Thunderstreak|under_restoration
North American|B-25|C|41-12634|Mitchell||fixed_wing|monoplane|military|bomber||Recovered from Lake Murray South Carolina in September 2005 after a 1943 training crash and conserved here as a wreck exhibit|B25C;Mitchell;Lake Murray B-25|on_display
North American|TB-25|N|44-30635|Mitchell||fixed_wing|monoplane|military|trainer|||TB25N;B-25;Mitchell|on_display
Douglas|R4D|6Q|50814|Skytrooper||fixed_wing|monoplane|military|transport||Carried the US registration N48211 which the FAA cancelled on 13 December 2012 with the Southern Museum of Flight Foundation as last owner; the FAA record gives the airframe serial as 50814 which is the Navy BuNo|R4D6Q;C-47;N48211;BuNo 50814|on_display
Douglas|A-26|C|44-35724|Invader||fixed_wing|monoplane|military|bomber||Museum and Wikipedia list the type as B-26 Invader which is the post-1948 redesignation|A26C;B-26;Invader|on_display
Beechcraft|A45||N14VY|Mentor||fixed_wing|monoplane|military|trainer||silverhawkauthor calls this a Beechcraft C-45 Expeditor which is wrong; the FAA record for N14VY gives Beech A45 c/n BG-74 which is the Model 45 Mentor family not the Twin Beech; registration cancelled 6 March 2017 with the museum foundation as last owner|A45;T-34;Mentor;c/n BG-74;N14VY|on_display
Cessna|T-37|B|56-3555|Tweet||fixed_wing|monoplane|military|trainer|||T37B;Tweet|on_display
North American|T-6|G|N12CC|Texan||fixed_wing|monoplane|military|trainer|1950|silverhawkauthor gives the serial as 16866 which is the FAA airframe serial not a USAF serial - a museum-page construction-number error; registration cancelled 11 October 2012 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|T6G;AT-6;Texan;c/n 16866;N12CC|on_display
North American|T-28|C|140659|Trojan||fixed_wing|monoplane|military|trainer|||T28C;Trojan|on_display
Northrop|T-38|A|62-3723|Talon||fixed_wing|monoplane|military|trainer|||T38A;Talon|on_display
North American|T-39|D|151338|Sabreliner||fixed_wing|monoplane|military|trainer|||T39D;Sabreliner|on_display
North American|T-2|C|159165|Buckeye||fixed_wing|monoplane|military|trainer|||T2C;Buckeye|on_display
Douglas|TA-4|J|158465|Skyhawk||fixed_wing|monoplane|military|trainer|||TA4J;Skyhawk|on_display
Lockheed|T-33|A|57-0602|Shooting Star||fixed_wing|monoplane|military|trainer||First of two T-33A examples|T33A;Shooting Star;T-Bird|on_display
Lockheed|T-33|A||Shooting Star||fixed_wing|monoplane|military|trainer||Second of two T-33A examples; no serial published by any source consulted|T33A;Shooting Star;T-Bird|on_display
Grumman|TS-2|A|136560|Tracker||fixed_wing|monoplane|military|other||Carried US registration N91368 which the FAA cancelled on 24 November 2014 with the museum foundation as last owner; the FAA record gives the type as S2F-1 TS-2A and the airframe serial as 136560 which is the Navy BuNo|TS2A;S2F-1;Tracker;N91368;BuNo 136560|on_display
Cessna|M337|B|N849AF|Super Skymaster||fixed_wing|monoplane|military|recon|1968|The military O-2A equivalent; silverhawkauthor lists this once as an O-2A and once as a Cessna 337B which is the same single airframe double-counted; registration cancelled 31 October 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|M337B;O-2A;Cessna 337;N849AF;c/n 337M0214|on_display
Bell|UH-1|D|66-16086|Iroquois||rotary_wing||military|utility|||UH1D;Huey|on_display
Bell|UH-1|H|66-16873|Iroquois||rotary_wing||military|utility|||UH1H;Huey|on_display
Hughes|OH-6|A|67-16243|Cayuse||rotary_wing||military|recon||silverhawkauthor lists this serial simultaneously at the museum the Birmingham ANG air park and Birmingham municipal airport which is one airframe recorded three times|OH6A;Loach|on_display
Hughes|OH-6|A|67-16087|Cayuse||rotary_wing||military|recon|||OH6A;Loach|on_display
Sikorsky|CH-54|B|69-18464|Tarhe||rotary_wing||military|transport||Serial confirmed on Aerial Visuals as CH-54B c/n 64-071|CH54B;Skycrane;S-64;c/n 64-071|on_display
Sikorsky|CH-54|B|69-18479|Tarhe||rotary_wing||military|transport||silverhawkauthor calls this a CH-54A in one entry and a CH-54B in another and also lists it at the ANG air park and the municipal airport - one airframe recorded three times|CH54B;Skycrane;S-64|on_display
Mil|Mi-25|||Hind||rotary_wing||military|ground_attack||Libyan Mi-25 recovered from Chad in Operation Mount Hope III in 1988; received by the museum in April 2012|Mi25;Mi-24;Hind;Operation Mount Hope III|on_display
Antonov|An-2|||Colt||fixed_wing|biplane|military|transport||Received by the museum in April 2012|An2;Colt|on_display
Aero Vodochody|L-39|C|N82497|Albatros||fixed_wing|monoplane|military|trainer||Registration cancelled 29 October 2013 with the museum foundation as last owner|L39C;Albatros;N82497;c/n 430405|on_display
Mississippi State University|XV-11|A|65-13070|Marvel||fixed_wing|monoplane|military|experimental|||XV11A;Marvel|on_display
Aero Commander|680||N131JG|||fixed_wing|monoplane|civilian|private|1957|Registration cancelled 18 July 2017 with the museum foundation as last owner; year from the FAA YEAR MFR field|Aero Commander 680;N131JG;c/n 680-515-185|on_display
Aeronca|11AC||N9180E|Chief||fixed_wing|monoplane|civilian|private|1946|Registration cancelled 27 June 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|Aeronca 11AC;Chief;N9180E;c/n 11AC-813|on_display
Aeronca|15AC||N1065H|Sedan||fixed_wing|monoplane|civilian|private|1948|On floats; registration cancelled 28 February 2017 with the museum foundation as last owner; year from the FAA YEAR MFR field|Aeronca 15AC;Sedan;N1065H;c/n 15AC-83|on_display
Aeronca|K||N17799|||fixed_wing|monoplane|civilian|private||Registration cancelled 13 April 2017 with the museum foundation as last owner|Aeronca K;N17799;c/n K-66|on_display
Alexander|Eaglerock||N5914|Long-Wing||fixed_wing|biplane|civilian|private||Registration cancelled 16 February 2018 with the Southern Museum of Flight as last owner; silverhawkauthor renders the marking as NC5914|Eaglerock;Long Wing Eaglerock;N5914;NC5914;c/n 557|on_display
Beagle|B.206||N15JP|||fixed_wing|monoplane|civilian|private|||Beagle 206;N15JP|on_display
Beechcraft|2000||N214JB|Starship||fixed_wing|monoplane|civilian|private||FAA shows N214JB as deregistered|Starship;Beech 2000;N214JB|on_display
Boeing|PT-17|||Kaydet||fixed_wing|biplane|military|trainer||Tuskegee Airmen exhibit; Stearman Model 75|PT17;Stearman;Model 75|on_display
Cessna|310|A|N3051D|||fixed_wing|monoplane|civilian|private|1956|Registration cancelled 7 April 2017 with the museum foundation as last owner; year from the FAA YEAR MFR field|Cessna 310A;N3051D;c/n 35251|on_display
Culver|LCA||N41712|Cadet||fixed_wing|monoplane|civilian|private||Registration cancelled 19 May 2015 with the museum foundation as last owner|Culver LCA;Cadet;N41712;c/n 419|on_display
Fairchild|PT-19|||Cornell||fixed_wing|monoplane|military|trainer||Tuskegee Airmen exhibit|PT19;Cornell;M-62|on_display
Fokker|D.VII||N904AC|||fixed_wing|biplane|military|fighter||Replica; registration cancelled 1 June 2017 with the museum foundation as last owner|Fokker DVII;N904AC|on_display
Folland|Gnat|||||fixed_wing|monoplane|military|trainer|||Gnat|on_display
Forney|F-1||N7574C|Ercoupe||fixed_wing|monoplane|civilian|private|1959|Registration cancelled 18 November 2014 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Forney F-1;Ercoupe 415;N7574C;c/n 5691|on_display
Great Lakes|2T-1|A-2||||fixed_wing|biplane|civilian|private|||Great Lakes 2T-1A-2|on_display
Mooney|M-18|L|N370A|Mite||fixed_wing|monoplane|civilian|private|1949|Registration cancelled 23 January 2018 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Mooney M-18;Mite;N370A;c/n 31|on_display
Piper|PA-28|140||Cherokee Cruiser||fixed_wing|monoplane|civilian|private|||PA28-140;Cherokee|on_display
Republic|RC-3||N6537K|Seabee||fixed_wing|monoplane|civilian|private|1947|Registration cancelled 30 April 2013 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|RC-3;Seabee;N6537K;c/n 803|on_display
Stinson|SR-5|||Junior||fixed_wing|monoplane|civilian|private|||Stinson SR-5;Junior|on_display
Stinson|10|A|N31553|Voyager||fixed_wing|monoplane|civilian|private|1941|silverhawkauthor gives the registration as N7802 which is in fact the FAA airframe serial number 7802; the registration was N31553 cancelled 27 September 2012 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Stinson 10A;Voyager;N31553;c/n 7802|on_display
Vultee|BT-13|B||Valiant||fixed_wing|monoplane|military|trainer||Tuskegee Airmen exhibit; silverhawkauthor quotes 762 which is not a valid BT-13 serial so tail_number is left blank|BT13B;Valiant;Vibrator|on_display
Bede|BD-4||N56BT|||fixed_wing|monoplane|civilian|experimental||FAA shows N56BT as no longer registered to the museum|BD-4;N56BT|on_display
Bede|BD-5|B|N51CJ|||fixed_wing|monoplane|civilian|experimental|1990|Registration cancelled 17 January 2018 with the museum foundation as last owner; year from the FAA YEAR MFR field|BD-5B;N51CJ;c/n 2185|on_display
Bensen|B-8|M|N4470|Gyrocopter||rotary_wing||civilian|experimental|1970|Registration cancelled 9 July 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|B-8M;Bensen;N4470;c/n 210|on_display
Brantley|Starduster|1|N111JB|||fixed_wing|biplane|civilian|experimental||Registration cancelled 22 February 2017 with the museum foundation as last owner|Starduster-1;N111JB;c/n JB-01|on_display
Brothers|RW 152||N3306|||fixed_wing|monoplane|civilian|experimental|1987|silverhawkauthor renders the builder as Brothers Michael which is the FAA registrant name Michael Brothers; registration cancelled 30 April 2013 with the museum foundation as last owner; the FAA record for this cancellation is under N232TC not N3306|RW 152;N232TC;c/n 3306|on_display
Bushby|Mustang|II|N7XL|||fixed_wing|monoplane|civilian|experimental|1983|Registration cancelled 11 May 2015 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Mustang II;Bushby;N7XL;c/n M-II-707|on_display
Curtiss|Model D|||Pusher|fixed_wing|biplane|civilian|experimental||1912 replica|Curtiss D;Curtiss Pusher|on_display
Frierson|VariEze||N101EZ|||fixed_wing|monoplane|civilian|experimental|1978|Rutan VariEze built by Frierson; registration cancelled 9 August 2016 with the museum foundation as last owner; year from the FAA YEAR MFR field|VariEze;Vari-Eze;N101EZ;c/n 1182|on_display
Harrison|Mini-Mac||N75GH|||fixed_wing|monoplane|civilian|experimental|1974|Registration cancelled 19 November 2014 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Mini Mac;N75GH;c/n 3|on_display
Heath|Super Parasol|||||fixed_wing|monoplane|civilian|private||1927 aircraft|Heath Parasol;Super Parasol|on_display
Holland|SPT FY||N1099|||fixed_wing|monoplane|civilian|experimental||Registration cancelled 8 November 2013 with the museum foundation as last owner; FAA registrant L C Holland|Holland/Isaac SPT FY;N1099;c/n 1049|on_display
Huff-Daland|Duster|||||fixed_wing|biplane|civilian|other||Crop duster; silverhawkauthor gives the marking as NX2953|Huff-Daland;Duster;NX2953|on_display
Laister-Kauffman|LK-10|A|N56588|||fixed_wing|monoplane|civilian|trainer||Military designation TG-4A; registration cancelled 28 February 2017 with the museum foundation as last owner|LK-10A;TG-4A;N56588;c/n 71|on_display
Macaro|Sonerai|II|N64RD|||fixed_wing|monoplane|civilian|experimental||Registration cancelled 20 September 2013 with the museum foundation as last owner; FAA registrant Raymond J Macaro|Sonerai II;N64RD;c/n 4464|on_display
Mitchell|B-10|||Buzzard||fixed_wing|monoplane|civilian|private||Ultralight|B-10;Buzzard|on_display
Reznor|Monerai|S|N5587X|||fixed_wing|monoplane|civilian|experimental|1981|Sailplane; registration cancelled 22 April 2013 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Monerai-S;N5587X;c/n 0045|on_display
Pazmany|PL-4|A|N43NP|||fixed_wing|monoplane|civilian|experimental||Registration cancelled 4 June 2013 with the museum foundation as last owner; FAA registrant Norman Ellis Ponder Jr|PL-4A;N43NP;c/n 424-18-3854|on_display
Piel|Emeraude|CP-30|N54144|||fixed_wing|monoplane|civilian|private|1970|Registration cancelled 23 October 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|Emeraude;CP-30;N54144;c/n 1048|on_display
Piper|J-3|||Cub|fixed_wing|monoplane|civilian|private||Unrestored project|J-3;Cub|under_restoration
Hayes|Pitts|S-1C|N14RH|Special||fixed_wing|biplane|civilian|experimental|1977|Registration cancelled 11 January 2018 with the museum foundation as last owner; year from the FAA YEAR MFR field|Pitts S-1C;Special;N14RH;c/n RMH1|on_display
Hill|KR-1||N20501|||fixed_wing|monoplane|civilian|experimental|1983|Rand Robinson KR-1 built by Ray L Hill; registration cancelled 18 September 2012 with the museum foundation as last owner; year from the FAA YEAR MFR field|KR-1;Rand Robinson;N20501;c/n 2667|on_display
Rochester|Davis|DA-2A|N1517C|||fixed_wing|monoplane|civilian|experimental|1971|Registration cancelled 17 December 2014 with the museum foundation as last owner; year from the FAA YEAR MFR field|Davis DA-2A;N1517C;c/n 37|on_display
Ross|Sea Bird|1|N667RR|||fixed_wing|monoplane|civilian|experimental|1999|Registration cancelled 30 May 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|Sea Bird 1;Seabird;N667RR;c/n 001|on_display
Rotec|Rally|||||fixed_wing|monoplane|civilian|private||Ultralight|Rotec Rally|on_display
RotorWay|Exec|4||||rotary_wing||civilian|experimental|||Rotorway Exec;Exec 4|on_display
Rutan|VariViggen|||||fixed_wing|monoplane|civilian|experimental|||Vari-Viggen;VariViggen|on_display
Campbell|Glasair|II FT|N612WC|||fixed_wing|monoplane|civilian|experimental|1995|Stoddard-Hamilton Glasair II FT built by Julian W Campbell; registration cancelled 10 April 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|Glasair II;Glassaire II F-T;N612WC;c/n 4243572040|on_display
Pruett|Pusher||N1496|||fixed_wing|monoplane|civilian|experimental|1967|Not listed by any directory consulted; found only in the FAA deregistration file - cancelled 8 February 2018 with the Southern Museum of Flight as last owner; year from the FAA YEAR MFR field|Pruett Pusher;N1496;c/n JP-2|on_display
Cumulus|2F||N203JS|||fixed_wing|monoplane|civilian|experimental|1951|Glider; registration cancelled 16 July 2013 with the museum foundation as last owner; year from the FAA YEAR MFR field|Cumulus 2F;N203JS;c/n 02|on_display
Wright|Flyer|||||fixed_wing|biplane|civilian|other||1903 Flyer replica|Wright Flyer;1903 Flyer|on_display
```

## USS Alabama Battleship Memorial Park — 29 rows

```
Vought|OS2U|3|5951|Kingfisher||fixed_wing|monoplane|military|recon||Park page prints the identity as BU0951 which is not a valid OS2U BuNo; 5951 falls inside the OS2U-3 block 5913-6042 and is recorded here as the most probable reading - NEEDS ON-SITE CONFIRMATION|OS2U3;Kingfisher;BU0951|on_display
North American|P-51|D|44-74216|Mustang|Red Tail|fixed_wing|monoplane|military|fighter||Park page prints the serial as 4474216; USAF-owned loan; painted in Tuskegee Airmen red-tail markings which the park describes as representative rather than an actual Tuskegee aircraft|P51D;Mustang;Red Tail|on_display
North American|B-25|J|44-31004|Mitchell||fixed_wing|monoplane|military|bomber||Park page prints the identity as 20NC44310004 which is garbled; silverhawkauthor gives TB-25J 44-31004 and that reading is adopted|B25J;TB-25J;Mitchell|on_display
Douglas|C-47|D|44-76326|Skytrain||fixed_wing|monoplane|military|transport||Park page prints the serial as 4076326 which is a transcription error; silverhawkauthor gives VC-47D 44-76326 and that reading is adopted; USAF-owned loan|C47D;VC-47D;Skytrain;Dakota|on_display
Boeing|E75||N43320|Kaydet||fixed_wing|biplane|civilian|trainer||Stearman Model 75; FAA registry shows N43320 c/n 75-8413 currently registered to the USS Alabama Battleship Foundation Inc of Mobile which is strong current presence evidence|E75;PT-17;Stearman;Model 75;N43320;c/n 75-8413|on_display
Grumman|G-21|A|N48550|Goose||fixed_wing|monoplane|civilian|transport|1939|Park page lists it as Grumman Goose Mk. II; FAA registry shows N48550 c/n 1061 currently registered to the USS Alabama Battleship Foundation Inc of Mobile; year from the FAA YEAR MFR field|G21A;Goose;JRF;N48550;c/n 1061|on_display
North American|F-86|L|51-2993|Sabre||fixed_wing|monoplane|military|fighter||Park page prints 512993|F86L;Sabre|on_display
Piasecki|CH-21|D|51-5859|Workhorse||rotary_wing||military|transport||Park page prints 515859 and calls it a CH-21D; silverhawkauthor calls it a CH-21B and gives 51-15859; the five-digit and six-digit readings cannot both be right - NEEDS ON-SITE CONFIRMATION|CH21D;CH-21B;H-21;Workhorse;Flying Banana|on_display
Grumman|F9F|5P|126275|Panther||fixed_wing|monoplane|military|recon||Park page gives F9F-5P; 126275 falls inside the F9F-5P photo-reconnaissance block so the park reading is preferred over silverhawkauthor which calls it an F9F-2P|F9F5P;Panther|on_display
Douglas|AD-4|N||Skyraider||fixed_wing|monoplane|military|ground_attack||No BuNo published by the park; silverhawkauthor gives 126956 which is unconfirmed so tail_number is left blank|AD4N;A-1;Skyraider;Spad;126956|on_display
Douglas|A-4|C|147787|Skyhawk||fixed_wing|monoplane|military|ground_attack||147787 falls inside the A-4C block; silverhawkauthor splits this into an A-4C 147767 and an A-4L 147787 but the park lists only one Skyhawk|A4C;A-4L;Skyhawk;Scooter|on_display
McDonnell|F-4|C|63-7487|Phantom II||fixed_wing|monoplane|military|fighter||Park page prints 637487; removed from the park entrance for restoration as reported in early February 2026 so it is not currently on public display|F4C;Phantom|under_restoration
Republic|F-105|B|54-0102|Thunderchief||fixed_wing|monoplane|military|ground_attack||Park page prints 540102 and the block designation as F-105B-IRE which is a typo for F-105B-1-RE; 54-0102 falls inside the small F-105B block 54-0100 to 54-0111|F105B;Thunderchief;Thud|on_display
Vought|RF-8|A|145645|Crusader||fixed_wing|monoplane|military|recon||Park page gives RF-8A 145645 which falls inside the RF-8A block; silverhawkauthor gives RF-8G 146898 which is a different real airframe - the park page is preferred as the site authority but the conflict is unresolved|RF8A;RF-8G;Crusader|on_display
Grumman|A-6||151626|Intruder||fixed_wing|monoplane|military|ground_attack||Park page gives the type simply as A-6; silverhawkauthor identifies it as a KA-6D tanker conversion|A6;KA-6D;Intruder|on_display
Mikoyan-Gurevich|MiG-17|A||Fresco||fixed_wing|monoplane|military|fighter||Wears the bort number Red 87 which is not a serial; park-owned|MiG17A;Fresco;Red 87|on_display
Boeing|B-52|D|55-0071|Stratofortress||fixed_wing|monoplane|military|bomber||Park page prints 55071; 55-0071 falls inside the B-52D block; USAF-owned loan|B52D;Stratofortress;BUFF|on_display
Lockheed|A-12||60-6938|Oxcart||fixed_wing|monoplane|military|recon||CIA Oxcart article 132; park page prints 606938; one of two A-12s in Alabama the other being 60-6937 at the Southern Museum of Flight|A12;Article 132;Blackbird;Oxcart|on_display
General Dynamics|F-16|A|79-0334|Fighting Falcon||fixed_wing|monoplane|military|fighter||Park page lists it as F-16A GF denoting a permanently grounded ground-instructional airframe and publishes no serial; 79-0334 comes from silverhawkauthor alone and falls inside the F-16A block - single-source|F16A;GF-16A;Viper;Fighting Falcon|on_display
McDonnell Douglas|F-15|A|75-0045|Eagle||fixed_wing|monoplane|military|fighter||Park page prints 75045 and gives the type as F-15A; silverhawkauthor calls it an F-15C which is wrong - 75-0045 is inside the F-15A block|F15A;Eagle|on_display
Bell|VH-1|N|158551|Iroquois|Army One|rotary_wing||military|transport||Presidential fleet HMX-1 helicopter used by Presidents Nixon Ford Carter Reagan and George H W Bush; recently restored and described by the park as one of the newest additions|VH1N;UH-1N;Huey;Army One;Bell 212|on_display
McDonnell Douglas|F/A-18|A|162417|Hornet|Snake 407|fixed_wing|monoplane|military|fighter||162417 falls inside the F/A-18A block|FA18A;F-18;Hornet|on_display
Northrop|YF-17|A|72-01570|Cobra||fixed_wing|monoplane|military|fighter||Park page prints 201570 and labels it prototype 1002 meaning the second of two airframes built; the correct serial is USAF 72-01570 not a Navy BuNo as silverhawkauthor states|YF17A;YF-17;Cobra;F-18 prototype|on_display
Grumman|F-14|A||Tomcat||fixed_wing|monoplane|military|fighter||No BuNo published by the park; silverhawkauthor gives 161611 which falls inside the F-14A block but is single-source so tail_number is left blank|F14A;Tomcat;161611|on_display
Kaman|SH-2|F||Seasprite||rotary_wing||military|search_rescue||Park page renders the type as HS-2F which is a typo for SH-2F; silverhawkauthor gives BuNo 150181 which is unconfirmed so tail_number is left blank|SH2F;Seasprite;150181|on_display
Grumman|HU-16|E|2129|Albatross||fixed_wing|monoplane|military|search_rescue||US Coast Guard serial 2129|HU16E;Albatross;USCG 2129|on_display
Sikorsky|HH-52|A|1378|Sea Guard||rotary_wing||military|search_rescue||US Coast Guard serial 1378|HH52A;Sea Guardian;S-62;USCG 1378|on_display
Sikorsky|HO4S|||Chickasaw||rotary_wing||military|search_rescue||On loan from the National Naval Aviation Museum Pensacola per the park ownership column; silverhawkauthor gives HO-4S UH-19D 55-5239 which mixes a Navy type with a USAF serial so tail_number is left blank|HO4S;H-19;S-55;Chickasaw|on_display
Chrysler|Redstone|||||missile_rocket||military|ballistic||Park page lists it as Chrysler SRBM with serial unknown|Redstone;SRBM;PGM-11|on_display
```

## US Space and Rocket Center — 5 rows

```
Lockheed|A-12||60-6930|Oxcart||fixed_wing|monoplane|military|recon||CIA Oxcart article 127 and the seventh of the A-12 series; first flew 1963; 258 flights and about 500 flight hours; dedicated at the Rocket Center on 1 February 1991 and repainted in 2017; on loan from the National Museum of the United States Air Force|A12;Article 127;Blackbird;Oxcart|on_display
North American Rockwell|Apollo|CM|CM-113||Casper|spacecraft||civilian|space||Flown Apollo 16 command module which orbited the Moon 64 times in April 1972; a genuine flight article|Apollo 16;Casper;CM-113;Command Module|on_display
Boeing|Saturn V|SA-500D|||Saturn V Dynamic Test Vehicle|missile_rocket||civilian|launch_vehicle||Ground dynamic test article not a flight article; displayed horizontally in the Davidson Center for Space Exploration; the stages were built by Boeing North American Aviation and Douglas|SA-500D;Saturn V;Dynamic Test Vehicle|on_display
Chrysler|Saturn I|SA-D5|||Saturn I Block II Dynamic Test Vehicle|missile_rocket||civilian|launch_vehicle||Vertical dynamic test vehicle and a long-standing Huntsville landmark; a test article not a flight article|SA-D5;Saturn I;Block II|on_display
Rockwell|Space Shuttle||||Pathfinder|spacecraft||civilian|space||Steel and wood simulator built for handling and facility fit checks; not a flight article and not an orbiter|Pathfinder;OV-098;Space Shuttle simulator|on_display
```

## Tuskegee Airmen National Historic Site — 3 rows

```
Boeing|PT-17||||Kaydet|fixed_wing|biplane|military|trainer||Original restored primary trainer displayed in Hangar 1 and described in a March 2023 visit report as in especially pristine condition; no serial or registration published by the National Park Service or by any source consulted|PT17;Stearman;Model 75|on_display
Piper|J-3||||Cub|fixed_wing|monoplane|civilian|trainer||Original restored Civilian Pilot Training Program aircraft displayed in Hangar 1; a March 2023 visit report calls it a Piper C-2 Cub while the National Park Service page calls it a J3 Piper Cub; no serial or registration published|J-3;J3;Cub;Piper Cub|on_display
North American|P-51|D|||Mustang|fixed_wing|monoplane|military|fighter||Full-scale replica displayed in Hangar 2 in red-tail markings; not an original airframe and carries no genuine serial|P51D;Mustang;Red Tail;replica|on_display
```

## US Veterans Memorial Museum, Huntsville — 4 rows

```
Bell|OH-58|A|69-16303|Kiowa||rotary_wing||military|recon||FAA registry shows N303VM airframe serial 69-16303 currently registered to the US Veterans Memorial Museum of Huntsville which is strong current presence evidence; a June 2024 published visit also records an OH-58 Kiowa on display|OH58A;Kiowa;N303VM;Jet Ranger|on_display
Bell|AH-1||||Cobra|rotary_wing||military|ground_attack||Recorded on display in a June 2024 published visit; no serial published and the variant is not stated so variant is left blank|AH1;Cobra;HueyCobra|on_display
Bell|H-13|D|||Sioux|rotary_wing||military|utility||Recorded on display in a June 2024 published visit and presented as the type used in the MASH film and television series; no serial published|H13D;Bell 47;Sioux|on_display
Waco|CG-4|A|||Hadrian|fixed_wing|monoplane|military|transport||Assault glider recorded as undergoing restoration in a June 2024 published visit; no serial published|CG4A;Hadrian;Waco glider|under_restoration
```

## Alabama Aviation College at Ozark — 1 row

```
Bell|AH-1||||Cobra|rotary_wing||military|ground_attack||Restored by Alabama Aviation Center students and placed on display on the Ozark campus as reported by the Dothan Eagle in November 2015; the campus also receives ex-Army airframes for maintenance instruction which are training assets rather than exhibits; no serial published and the variant is not stated|AH1;Cobra;HueyCobra|on_display
```

---

# 3. NOTES

## Currency evidence, site by site — and how old it is

| Site | Open in 2026? | Evidence | Age |
|---|---|---|---|
| Army Aviation Museum | Yes | Foundation site live with hours/admission; installation page live at the new `/rucker/` path | Current |
| Southern Museum of Flight | Yes | Own site: Tue–Sat 9–4, adult $10, child $8, military $5; no closure notice | Fetched Sept 2026 |
| Battleship Memorial Park | Yes | Own aircraft page live; a Feb 2026 news item about the park's Phantom | Feb 2026 |
| US Space & Rocket Center | Yes | Own per-aircraft pages live | Current |
| Tuskegee Airmen NHS | Yes | NPS page, last updated 20 May 2025 | ~16 months |
| US Veterans Memorial Museum | Yes | FAA registration *currently valid* in the museum's name + June 2024 published visit | Reg. current; display ~2 yrs |
| Alabama Aviation College Ozark | Yes (campus) | Campus live; the Cobra display report is Nov 2015 | **~11 years — weakest** |

**The strongest currency finding of the whole sweep** is that the Army Aviation Museum's own collection page is genuinely current, not a legacy document. Three independent 2024–25 events are reflected in it: the **Doak VZ-4DA 56-9642** transfer from Fort Eustis in **August 2024** (confirmed by Wikipedia); the **SB>1 Defiant** donation reported by TWZ in **November 2024**; and the two **FARA competitive prototypes** from a programme cancelled in February 2024. Its section structure (Airpark / Main Gallery / three TSF groups / Storage / Maintenance) totals ~177 entries, consistent with the "more than 160 aircraft" claim — i.e. it is a full inventory, not a highlights list. **I treated it as authoritative on presence and built the museum's 161 rows from it.**

## Which compilations proved stale, and exactly how

**silverhawkauthor's Fort Rucker page is at least twenty years out of date.** It lists the **Boeing Vertol XCH-62A 73-22012** as present. That airframe was **scrapped at Fort Rucker in 2005**, with parts sent to the Helicopter Museum at Weston-super-Mare in 2008. That single check dates the whole page. It also carries ~190 entries against the museum's ~177, with visible internal duplication: `UH-1C 0-22099` and `UH-1B 62-2099` are one aircraft (the `0-` prefix is the over-ten-years-old marking, not a serial); `GUH-1D 63-12972` and `UH-1H 63-12972` are one aircraft; `NAH-1G 66-15248` and `AH-1S 66-15248` are one aircraft; `Lockheed H-59 73-21942` and `Sikorsky XH-59 73-21942` are one aircraft under two wrong manufacturers. It also gives `XV-6A Kestrel 64-18264` **and** `AV-8A Harrier 64-18264` as two aircraft — 64-18264 is in the XV-6A Kestrel block, so the AV-8A entry is spurious. And it assigns `Lockheed CL-475` the serial 56-4320, which is the museum's VCH-34A. **I did not import a single Fort Rucker row from it.** I used it only as a cross-check that flushed out real conflicts, which I have flagged in individual `description` fields.

**silverhawkauthor's Birmingham page double- and triple-counts.** Its "Aircraft at Other Birmingham Locations" section re-lists OH-6A 67-16243, RF-4C 63-7745, RF-84F 52-7409 and CH-54 69-18479 at the Alabama ANG air park and/or Birmingham municipal airport *while also listing them at the museum*. These are single airframes that moved from the ANG air park into the museum's outdoor park; the compilation kept both entries. I recorded each once, at the museum, and said so in the row.

**silverhawkauthor's Mobile page substantially over-lists.** It gives an F6F-3 Hellcat, an SBD-3 Dauntless, an F4U-7 Corsair, an SH-60B Seahawk, a CH-3C, an F-100D, an EA-3B, a second Skyhawk, two Hueys and a BQM-74C that **do not appear on the park's own current aircraft table**. The park's table is a structured inventory with a per-aircraft owner column (Park / USAF / USN / USG / Pensacola loan) — it reads as a maintained record, not a highlights page. I built Mobile from the park's table (29 airframes) and excluded the extras.

**Wikipedia's Southern Museum of Flight list is explicitly "Selected aircraft on display" and carries no serials at all.** Useful only for type-level confirmation (it is where the Mi-24's true identity as an **Mi-25 captured in Operation Mount Hope III** comes from, and the April 2012 arrival date for the Mi-25 and An-2).

**Grokipedia was not used at any point.**

## The FAA registry did the heavy lifting at Birmingham

This was the single most productive move. I pulled the FAA's full releasable-aircraft database (`ReleasableAircraft.zip`, ~73 MB, data updated each federal working day) and searched `MASTER.txt` and `DEREG.txt` for Alabama registrants.

`DEREG.txt` returned **43 airframes deregistered with a Southern Museum of Flight entity as last owner**, cancellations spread 2012–2018 — the classic signature of a museum retiring flying registrations on static exhibits. That gives independent presence evidence, plus a construction number and a legitimate `YEAR MFR` for each, and it caught four errors silverhawkauthor had propagated:

- **N14VY is a Beech A45, c/n BG-74 — a Model 45 Mentor, not a "C-45 Expeditor."** silverhawkauthor's Twin Beech identification is simply wrong.
- **The T-6G's "serial 16866" is the FAA airframe serial (a construction number), not a USAF serial.** This is the museum-page failure mode the methodology warns about, caught red-handed. `tail_number` is the registration N12CC; 16866 went to aliases.
- **N849AF is one aircraft, not two.** silverhawkauthor lists an "O-2A N849AF" and a "Cessna 337B N849AF" separately; the FAA record is a single Cessna M337B c/n 337M0214, 1968.
- **The Stinson 10A's "N7802" is its construction number, not its registration.** The registration was N31553.

It also surfaced a **Pruett Pusher N1496, c/n JP-2, 1967**, cancelled Feb 2018 with the museum as last owner — an airframe no directory I consulted lists at all.

`MASTER.txt` gave two *currently valid* registrations that are excellent presence evidence:
- **N43320**, Boeing E75 Stearman c/n 75-8413, and **N48550**, Grumman G-21A Goose c/n 1061 (1939) — both registered to **USS Alabama Battleship Foundation Inc, Mobile**. These match the park's otherwise-unidentified "Boeing-Stearman Model 75" and "Grumman Goose Mk. II" and give the Goose a sourced `year_built`.
- **N303VM**, Bell OH-58A serial 69-16303, registered to **US Veterans Memorial Museum, Huntsville** — which is how I found that site at all.

`year_built` is populated on **26 rows only**, every one of them from an FAA `YEAR MFR` field. **No `year_built` was ever inferred from a fiscal-year serial prefix.** Every other row is deliberately blank.

## Corrections made, with evidence

**A pattern discovered at Fort Rucker: the museum prints Navy BuNos with a spurious leading "6" and a hyphen.** Three instances, each independently confirmed:

1. **AP-2E "61-31485" → BuNo 131485.** Confirmed by Aerial Visuals (Lockheed AP-2E, s/n 131485 USN, c/n 5366) and a JetPhotos image captioned 131485. Type recorded `electronic_warfare` — it is a Crazy Cat SIGINT aircraft, not a patrol bomber.
2. **"HH-43 61-38101" → Kaman HOK-1/OH-43D BuNo 138101.** The Wikipedia HH-43 survivor list places BuNo 138101 at this museum by name, notes it was at the National Naval Aviation Museum Pensacola c.1986–2001, and records that it was repainted from Marine to Army colours. 138101 sits at the head of the HOK-1 BuNo block. The type is also corrected — it is an HOK-1, not an HH-43.
3. **T-34C "16-0464" → BuNo 160464**, which falls inside the T-34C block. Same mangling, one digit differently placed.

Other corrections:

- **ACH-47A "Easy Money" "64-131149" → 64-13149.** The museum page has a duplicated digit. Aerial Visuals gives ACH-47A s/n 64-13149, c/n B121, and the serial falls inside the FY64 CH-47A block 64-13106/13173. This is the sole survivor of the four Guns-A-Go-Go gunships and worth getting right.
- **CH-54 68-18438 is a CH-54A, not the CH-54B the museum page states.** Aerial Visuals: CH-54A, c/n 64-040. silverhawkauthor independently agrees on the A.
- **Battleship Park's F-15 is an F-15A, not the F-15C silverhawkauthor calls it.** The park says F-15A and 75-0045 falls inside the F-15A block. The park is right.
- **Battleship Park's YF-17 carries USAF serial 72-01570, not a Navy BuNo.** The park prints "201570" and labels it "1002" (second airframe); silverhawkauthor renders it as "BuNo 72-1570", conflating the two systems. The two YF-17 prototypes were 72-01569 and 72-01570.
- **Battleship Park's serials are printed without hyphens and are unreliable as typed:** `4474216` → 44-74216, `4076326` → 44-76326, `637487` → 63-7487, `540102` → 54-0102, `55071` → 55-0071, `606938` → 60-6938, `75045` → 75-0045, `512993` → 51-2993, and `20NC44310004` → 44-31004 (garbled beyond simple de-hyphenation).
- **The three Alabama A-12s are all correctly distinguished.** Alabama holds two of the thirteen A-12s outdoors plus a third indoors, which is genuinely unusual and easy to conflate: **60-6930 / Article 127** at Huntsville (NMUSAF loan, dedicated 1 Feb 1991, repainted 2017), **60-6937 / Article 131** at Birmingham (arrived Feb 2000 from Palmdale; flew the first and last Black Shield missions), **60-6938 / Article 132** at Mobile. Confirmed against blackbirds.net's location table and habu.org's per-airframe page for 6937. Note the USSRC's own page says "Article 127" but publishes no tail number — the serial comes from the survivor tables.
- **F-105G note, for the vocabulary check:** Alabama has no F-105G. Birmingham's F-105F 63-8365 is recorded `ground_attack`, which is correct for the two-seat F; the `electronic_warfare` convention applies only to the G Wild Weasel conversion.

## Judgment calls

- **Fort Rucker display status mapping.** The museum's TSF (Training Support Facility) groups are labelled "ON DISPLAY" by the museum but sit in a facility open only on open-house days. I honoured the museum's own label (`on_display`) for the Open House, Evolutionary and Experimental series; used `in_storage` for the sections the museum itself marks "NOT ON DISPLAY – STORAGE" and "TSF Not Public"; and `under_restoration` for the "In Maintenance" section. Each TSF row says which group it is in, so a later pass can re-cut this if the site is treated as two records. **Note one conflict:** the museum lists HOK-1 138101 under TSF open-house display while Wikipedia says storage; I went with the museum.
- **Helicopters all have blank `wing_type`,** as required — this matters enormously here, since roughly two-thirds of the Fort Rucker collection is rotary.
- **One deliberate blank `wing_type` on a fixed_wing row:** the Honeywell RQ-16 T-Hawk. It is Q-designated so it is `fixed_wing` per the rule, but it is a ducted-fan lift vehicle with no wing at all — monoplane would be a fabrication. Flagged in its description so a later pass doesn't read it as an oversight.
- **Replicas and reproductions are recorded, and every one is flagged as such in `description`:** at Fort Rucker the B.E.2c, Blériot XI, S.E.5a, Sopwith F.1 Camel, Wright Model B and P-12E; at Birmingham the Fokker D.VII, Curtiss Model D and 1903 Wright Flyer; at Tuskegee the P-51D.
- **USSRC scope.** The brief said aircraft and flight-article spacecraft, not models. I included the A-12 and the Apollo 16 command module **CM-113 "Casper"** (a genuine flown flight article), plus the two Saturn dynamic test vehicles and Pathfinder — each labelled in `description` as a **test article or simulator, not a flight article**, so the distinction survives. I **excluded** the museum's rocket and missile park (V-2, Redstone, Jupiter, Juno II, Nike, MIM-23 Hawk, Honest John, Corporal, Patriot), the engine collection (F-1, J-2, SSME, NERVA), the Skylab engineering mock-up and the Apollo 12 Mobile Quarantine Facility. The MQF and Skylab mock-up are borderline and could be argued in; the rocket park is a large, separate, well-defined job.
- **The Mobile Kingfisher BuNo is my one genuinely uncomfortable call.** The park prints "BU0951", which is not a valid OS2U BuNo. 5951 sits inside the OS2U-3 block 5913–6042 and is the obvious reading of a dropped leading digit — but it is *my inference*, not a source. I recorded it with "NEEDS ON-SITE CONFIRMATION" in the description. If you would rather not carry an inferred serial at all, blank this one field; nothing else depends on it.

## Excluded, and why

- **Ryder's Replica Fighter Museum, Guntersville** — **defunct.** Four FAA registrations (Halberstadt D.IV replica N1388J, Fokker Dr.I replica N1917X, Fokker D.IV N4200S, DH.5 replica N950JS, plus a PA-46) all cancelled between 1997 and 2002. Named here so nobody researches it again.
- **Warbird South Flying Museum, Rainbow City** — holds **N982Z**, a *currently registered, airworthy* 1943 Douglas DC-3C, c/n 12947. Facebook presence only, no evidence of a public display facility. Operational aircraft are not displays. Recorded here as a lead rather than a row.
- **"Saving Our Flying Heritage Through A Flying Museum", Harvest** — Cessna 310D N6992T, cancelled 2019. Nothing else found. Lead only.
- **Red Tail Scholarship Foundation, Tuskegee** — holds **eight** currently registered aircraft (six PA-28s, two PA-31Ps). These are operational flight-training aircraft supporting a scholarship programme at Moton Field, **not** exhibits, and must not be confused with the NPS site's three display aircraft. Explicitly excluded.
- **N49VZ Zorn ASOB** — silverhawkauthor places it at the Southern Museum of Flight, but the FAA shows it currently registered to a private individual in Mobile. Either a loan since returned or a stale entry. Excluded pending evidence.
- **N2VE, a VariEze registered to "Alabama Space and Rocket Center Museum" and cancelled 2015** — no current evidence it is displayed. Excluded; worth one question to USSRC.
- **N30131 (Raven S-60 hot-air balloon, cancelled 2012), N555X (Piper PA-19 c/n 18-2136, cancelled 2004) and N74US (Piccard AX-6 balloon, cancelled 1985)**, all registered to the Army Aviation Museum. None appears on the museum's current inventory. Excluded. The two balloons may relate to the "Balloon Gondola" and "Balloon Envelope c. 1917" storage entries.
- **The Fort Rucker balloon gondola and 1917 balloon envelope** — excluded because I found **no sourced manufacturer**, and manufacturer is required. This is the only place the manufacturer rule cost me rows.
- **Three Fort Rucker storage entries excluded as unresolvable:** "YAO-3(G) 57-6535" (no such designation exists; possibly a Mohawk prototype, but I will not guess); "H-1, SN LWL-H-2"; and "Lockheed Test Bed 006" (manufacturer known, model not). Also the **"S-67 Rotary Systems/Compound SN:545/740"** entry, which duplicates the S-72 RSRA's own numbers — I recorded the S-72 once and noted the apparent duplication. The real Sikorsky S-67 Blackhawk was destroyed in a 1974 crash.
- **Maxwell AFB Air Park, Dannelly Field ANG, Birmingham ANG air park, and the Fort Rucker non-museum displays** — deferred to the base pass as instructed.
- **Southern Heritage Air Museum** — appeared in searches; it is in Tallulah, **Louisiana**. Not Alabama.
- **Wiregrass Museum of Art, Dothan** — the only "Wiregrass" museum in the region. It is an art museum with no aircraft. The brief's "Wiregrass" lead resolves to the Wiregrass *region*, whose aviation content is the Army Aviation Museum and the Ozark college campus, both captured.
- **Anniston** — swept, nothing found. The Berman Museum holds arms and armour, no aircraft.

## Leads for the base and monument pass

From skytamer's Alabama index (old, but a useful target list) and the FAA sweep:

- **Alabama ANG air park, Birmingham** — historically UH-1, OH-6A 67-16243, RF-4C 63-7745, RF-84F 52-7409, CH-54 69-18479. **Caution: those four serials are now at the Southern Museum of Flight in my package.** Verify on site before creating rows, or you will duplicate airframes.
- **Birmingham International Airport** — UH-1 63-08502, OH-58 71-21288.
- **Maxwell AFB Air Park + Gunter Annex**, Montgomery. **USAF Enlisted Heritage Hall** at Gunter is a genuine museum (not a gate guard) but appears to hold essentially no airframes — worth one check rather than a full pass.
- **Dannelly Field ANG**, Montgomery.
- **VFW Post 4850 static display, Jasper.**
- **City static displays**: Lineville, Mobile, Monroeville, Montgomery, Ozark, Selma, Tuscaloosa.
- **Charles E. Bailey Sr. Sportplex / Veterans Memorial Park, Alexander City.**
- **Florala State Park**; **Stewart Flying Service, Middleton Field, Evergreen.**
- Skytamer also lists **Aviation Challenge** and **US Space Camp**, Huntsville, as separate from USSRC — likely the same campus, but worth confirming they are not distinct display sites.

## Open questions, ranked, with phone numbers

1. **US Army Aviation Museum — (334) 598-2508.** One call closes the most: (a) confirm the FARA prototypes **Raider X 23-2500** and **Bell 360 Invictus 23-2501** have physically arrived — presence rests solely on the museum's own page and the programme was cancelled before either was finished; (b) resolve **UH-1B 60-3554**, which the museum's page lists in *both* the TSF Evolutionary series and Storage — one airframe, two places, on a single page; (c) confirm the doubted serials **AH-1J 72-2504** and **T-28B 53-7747** (both Navy types carrying USAF-style serials) and **TH-67 00-67446** (wrong serial shape for the type); (d) confirm the **Nieuport 28C.1 "17-6531"**; (e) ask whether the RQ-5A Hunter and MQ-1C really both carry "107".
2. **USS Alabama Battleship Memorial Park — 1.800.GANGWAY.** (a) The **OS2U Kingfisher BuNo** — is it 5951? (b) **CH-21: 51-5859 or 51-15859, and B or D?** (c) Is the Crusader an **RF-8A 145645** (park) or **RF-8G 146898** (silverhawkauthor)? (d) The **F-14A** and **SH-2F** BuNos, which the park does not publish. (e) Where is **F-4C 63-7487** being restored, and when does it return? (f) Confirm the F6F Hellcat, SBD Dauntless, F4U-7 Corsair, SH-60B, CH-3C and F-100D that silverhawkauthor lists are genuinely gone — if any remain, my Mobile list is six rows short.
3. **Southern Museum of Flight — (205) 833-8226.** Serials for the second **T-33A**, the **MiG-15**, the **F-86F**, the **BT-13B** and the **PT-17/PT-19** in the Tuskegee exhibit — five blanks a single visit would fill. Also confirm the **Barber Motorsports Park** relocation is still an expansion rather than a move; as of 2023 the museum said it was keeping the 73rd Street campus, and a move would invalidate this site record wholesale.
4. **Alabama Aviation College at Ozark.** My only source for the AH-1 display is a **November 2015** newspaper report — eleven years old and by far the weakest currency evidence in this package. Confirm the Cobra is still displayed, get its serial and variant, and establish whether any of the ex-Army airframes the campus received are exhibits rather than teaching hulks.
5. **Tuskegee Airmen NHS — (334) 727-1247.** Serials/registrations for the PT-17 and the Cub, and settle whether the Cub is a J-3 (NPS) or a C-2 (the 2023 visit report).
6. **US Veterans Memorial Museum, Huntsville.** Serials for the AH-1, the H-13D and the CG-4A, and the AH-1 variant. Their website returned a server error throughout this session; the FAA registration and a June 2024 published visit carried the site.