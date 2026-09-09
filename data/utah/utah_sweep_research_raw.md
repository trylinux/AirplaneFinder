I have enough to deliver. Writing up now.

## 1. SITE RECORDS

`name|city|state_province|country|postal_code|region|address|website|access_type|latitude|longitude`

```
Hill Aerospace Museum|Roy|Utah|United States|84056|North America|7961 Cottonwood Street Building 1955 Hill Air Force Base|https://www.aerospaceutah.org/|public|41.161828|-112.020664
Hill Air Force Base Memorial Park|Ogden|Utah|United States|84056|North America||https://www.hill.af.mil/|restricted|41.116019|-111.981939
Utah National Guard Headquarters Draper|Draper|Utah|United States|84020|North America|12953 South Minuteman Drive|https://guard.utah.gov/|public|40.516667|-111.890533
VFW Post 5560 Memorial Vernal|Vernal|Utah|United States|84078|North America|||public|40.456033|-109.526314
Camp Williams Utah National Guard|Bluffdale|Utah|United States||North America||https://guard.utah.gov/camp-williams/|restricted|40.433672|-111.928511
Northrop Grumman Rocket Garden Promontory|Corinne|Utah|United States|84307|North America|9160 Utah State Route 83|https://www.northropgrumman.com/|public|41.658921|-112.440841
```

**Coordinate provenance:** all six are Aerial Visuals *mapped airframe positions* except the Rocket Garden (GPS fix published by a 2024 field photographer) and Draper (a Waymarking GPS reading taken at the airframe, N 40° 31.000 W 111° 53.432, which agrees with the Aerial Visuals position to ~4 m). None are geocoded addresses. Camp Williams address and ZIP left blank — I did not verify them and will not guess.

---

## 2. AIRFRAME LINES

`manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status`

### HILL AEROSPACE MUSEUM — ⚠️ FULL ROSTER (75 rows), NOT a delta

This is the museum's own complete current collection page, scraped page-by-page (75 aircraft detail pages, each with a specs block). **Diff this against your 76.** The museum publishes exactly 75; Wikipedia's "80+/90+" figure is not supported by the museum's own list.

```
Douglas|A-1|H|135247|Skyraider||fixed_wing|monoplane|military|ground_attack||CORRECTION: museum prints serial 52-0247 and type A-1E; the Aerial Visuals dossier identifies the airframe as an AD-6/A-1H BuNo 135247 c/n 9891 displayed as an A-1E in false markings USAF 120247; the museum number appears to be a garbling of that marking; acquired from Davis-Monthan in 2001 and recorded present after 2023|A1H; AD-6; AD6; A-1E; A1E; BuNo 135247; c/n 9891; 120247|on_display
Fairchild Republic|A-10|A|73-1666|Thunderbolt II||fixed_wing|monoplane|military|ground_attack|1975|Serial checks against the A-10A FY73 pre-production block 73-1664/1673; museum states delivery to the USAF in June 1975; USAF Heritage Program loan|A10A; Warthog|on_display
Douglas|A-26|B|44-35617|Invader||fixed_wing|monoplane|military|bomber||Serial checks against the A-26B FY44 block; converted post-war by On Mark Engineering as a Marketeer executive transport and civil-registered N600WB before museum acquisition|A26B; B-26; B26; On Mark Marketeer; c/n 28896; N600WB|on_display
Ling-Temco-Vought|YA-7|F|70-1039|Corsair II||fixed_wing|monoplane|military|ground_attack||Serial falls in the A-7D FY70 block and matches one of only two YA-7F Strikefighter prototype conversions|YA7F; A-7D; A7D; Strikefighter|on_display
Rockwell|B-1|B|83-0070|Lancer||fixed_wing|monoplane|military|bomber||Serial checks against the B-1B FY83 block 83-0065/0071|B1B; c/n 7|on_display
Boeing|B-17|G|44-83663|Flying Fortress||fixed_wing|monoplane|military|bomber|1945|Museum states manufactured 1945; serial checks against the B-17G-90-DL Douglas Long Beach block matching the museum's own block designation; served the Brazilian Air Force fifteen years as FAB 5400 then civil N47780; acquired by John Lindquist 1987 and donated after restoration into 493rd Bomb Group markings|B17G; B-17G-90-DL; FAB 5400; N47780; c/n 32304|on_display
Consolidated|B-24|D|41-23908|Liberator||fixed_wing|monoplane|military|bomber||Serial checks against the B-24D FY41 block|B24D; c/n 393|on_display
North American|B-25|J|44-86772|Mitchell||fixed_wing|monoplane|military|bomber|1945|Museum states manufactured 1945 and first accepted by the USAF in June 1945 then immediately stored; serial checks against the B-25J FY44 block|B25J; c/n 108-47526; N2888G|on_display
Boeing|B-29|||Superfortress|Straight Flush|fixed_wing|monoplane|military|bomber||CORRECTION: the museum specs block prints 52-10862 which is its own C-45H Expeditor's serial; airplanes-online and a dated Vintage Aviation News report of 28 July 2025 both give 44-86408 which checks against the B-29-55-MO Martin Omaha block and matches the museum's own B-29-55-MO designation; painted to represent the Hiroshima weather reconnaissance aircraft Straight Flush; outboard wing sections removed for restoration inside the Hadley Gallery as of July 2025|B29; B-29-55-MO; 52-10862|under_restoration
Boeing|B-52|G|58-0191|Stratofortress|Bearing Arms|fixed_wing|monoplane|military|bomber|1959|Museum states built by Boeing at Wichita and delivered to the USAF in October 1959; serial checks against the B-52G FY58 block|B52G; c/n 464259|on_display
de Havilland Canada|C-7|B|63-9757|Caribou||fixed_wing|monoplane|military|transport||Serial checks against the C-7A/DHC-4 FY63 block; Aerial Visuals records the airframe as a C-7A while the museum displays it as a C-7B|C7B; C-7A; C7A; DHC-4; DHC4|on_display
Douglas|C-47|B|43-49281|Skytrain||fixed_wing|monoplane|military|transport|1944|Museum states manufactured 1944; serial checks against the C-47B FY43 block and construction number 15097 is consistent with Oklahoma City production|C47B; Dakota; c/n 15097; N143Z|on_display
Douglas|C-54|G|45-0502|Skymaster||fixed_wing|monoplane|military|transport||Serial checks against the C-54G FY45 block; later carried Haitian registration HH-JMA|C54G; C-54G-1-DO; c/n 35955; HH-JMA|on_display
Fairchild|C-119|G|22107|Flying Boxcar||fixed_wing|monoplane|military|transport||Tail number is the Royal Canadian Air Force serial not a construction number; struck off RCAF charge 22 August 1967 then Hawkins and Powers Aviation as N966S; registration cancelled 20 March 2013; displayed in false USAF markings 52-2107; USAF Museum loan|C119G; c/n 10738; N966S; 52-2107|on_display
Douglas|C-124|C|53-0050|Globemaster II||fixed_wing|monoplane|military|transport||Serial checks against the C-124C FY53 block 53-0001/0052|C124C; Old Shaky; c/n 44345|on_display
Lockheed|NC-130|B|57-0526|Hercules||fixed_wing|monoplane|military|transport||Serial checks against the C-130B FY57 block 57-0525/0529; museum displays it as an NC-130B and Aerial Visuals as a C-130B|NC130B; C-130B; C130B|on_display
Convair|VC-131||55-0300|Samaritan||fixed_wing|monoplane|military|transport||Museum prints 55-300; serial checks against the C-131D FY55 block 55-0291/0301; Aerial Visuals records it as a C-131D later civil N8440H|VC131; C-131D; C131D; c/n 340-233; N8440H|on_display
Boeing|KC-135|E|57-1510|Stratotanker||fixed_wing|monoplane|military|tanker||Serial checks against the KC-135A FY57 block; the E model is the re-engined conversion|KC135E; c/n 17581|on_display
Lockheed|C-140|B|62-4201|JetStar||fixed_wing|monoplane|military|transport||Serial checks against the C-140B FY62 block 62-4197/4201; Aerial Visuals records it as a VC-140B; museum describes it as a presidential transport|C140B; VC-140B; VC140B; c/n 1329-5045|on_display
General Atomics|MQ-1|B|03-33116|Predator||fixed_wing|monoplane|military|drone||Q designation denotes an unmanned aircraft; serial consistent with the FY03 MQ-1 series|MQ1B; RQ-1; RQ1|on_display
Wright Brothers|Flyer||||1903 Wright Flyer|fixed_wing|biplane|civilian|experimental||Full scale reproduction of the 1903 Wright Flyer; museum records no serial and credits Orville and Wilbur Wright; on loan from the US Air Force Heritage Program|Wright Flyer; 1903 Flyer|on_display
Burgess|Model B||||Burgess-Wright Flyer|fixed_wing|biplane|civilian|trainer||Replica of the Burgess-Wright Model B built under Wright licence; the museum specs block prints 69115 which is not a recognised Burgess identity and is not carried as a serial|Burgess-Wright; Model F Flyer; 69115|on_display
Curtiss|JN-4|D|SC5002|Jenny||fixed_wing|biplane|military|trainer||Aerial Visuals gives Signal Corps serial SC5002 with construction number 5002 and civil registration N5001; the museum prints 5002 alone; museum text states the airframe was originally built by the Springfield Airplane Company under Curtiss licence|JN4D; JN-4; JN4; c/n 5002; N5001; 5002|on_display
McDonnell Douglas|F-4|C|63-7424|Phantom II||fixed_wing|monoplane|military|fighter|1964|Museum states it rolled off the production line in 1964 and crash-landed in Missouri two days after USAF acceptance; first airframe through the Hill F-4 Crash Damage Repair Program; displayed since 1989; serial checks against the F-4C FY63 block|F4C; c/n 0366|on_display
McDonnell Douglas|F-4|D|66-8711|Phantom II||fixed_wing|monoplane|military|fighter||Serial checks against the F-4D FY66 block|F4D; c/n 2483|on_display
McDonnell Douglas|RF-4|C|66-0469|Phantom II||fixed_wing|monoplane|military|recon|1967|Museum states it rolled off the production line in 1967; serial checks against the RF-4C FY66 block|RF4C; c/n 2632|on_display
Northrop|F-5|E|73-1640|Tiger II||fixed_wing|monoplane|military|fighter||Museum prints 73-01640; the FY73 F-5E allocations are not contiguous and I could not confirm this serial against a published block so it is carried exactly as printed; the Aerial Visuals record for the same number is internally garbled and adds nothing|F5E; 73-01640|on_display
McDonnell Douglas|F-15|A|77-0090|Eagle||fixed_wing|monoplane|military|fighter|1978|Museum states it rolled off the assembly line in 1978 which differs from the FY prefix as expected; serial checks against the F-15A-19-MC FY77 block; served in the Netherlands and the United States|F15A; c/n 371|on_display
General Dynamics|F-16|A|79-0388|Fighting Falcon||fixed_wing|monoplane|military|fighter||Block 10B; serial checks against the F-16A FY79 block|F16A; c/n 61-173|on_display
General Dynamics|F-16|A|79-0402|Fighting Falcon|Little Precious|fixed_wing|monoplane|military|fighter||Block 10B; serial checks against the F-16A FY79 block; Aerial Visuals places this airframe at the Hill AFB west side display rather than inside the museum so which side of the fence it stands on should be confirmed on site|F16A; c/n 61-187|on_display
General Dynamics|F-16|A|81-0678|Fighting Falcon||fixed_wing|monoplane|military|fighter||Displayed in USAF Thunderbirds markings; serial checks against the F-16A FY81 block|F16A; Thunderbird|on_display
Mikoyan-Gurevich|MiG-21|F-13||Fishbed||fixed_wing|monoplane|military|fighter||Museum prints 585 in the serial field which is a marking or construction number rather than a verified serial and is not carried as an identity; acquired and placed on display July 1993|MiG21; MiG-21F; Fishbed-C; 585|on_display
Lockheed Martin|F-22|A|91-4002|Raptor||fixed_wing|monoplane|military|fighter||Serial checks against the F-22 EMD block 91-4001/4009; absent from the Aerial Visuals Hill dossier so presence rests on the museum's own current collection page alone|F22A|on_display
Lockheed|P-38|J|42-67638|Lightning||fixed_wing|monoplane|military|fighter|1943|Museum states manufactured 1943 and assigned to the 54th Fighter Squadron 343rd Fighter Group 11th Air Force on Attu in the Aleutians; serial checks against the P-38J-10-LO FY42 block|P38J|on_display
Curtiss|P-40|N||Warhawk||fixed_wing|monoplane|military|fighter||Aerial Visuals records this airframe as a P-40N replica; the museum prints 42-105270 which is therefore treated as a representation and deliberately not carried as an identity|P40N; P-40N-5-CU; 42-105270|on_display
Republic|P-47|D|44-32798|Thunderbolt||fixed_wing|monoplane|military|fighter|1944|Museum states manufactured 1944 and Aerial Visuals records USAAF acceptance on 12 November 1944; donated to Peru in 1949 as Fuerza Aerea del Peru 450 then civil N987R; at Hill by 2003; has worn false markings 420473|P47D; FAP 450; N987R; c/n 3759; 420473|on_display
North American|P-51|D|44-13371|Mustang||fixed_wing|monoplane|military|fighter||Serial checks against the P-51D-5-NA FY44 block; Aerial Visuals holds no serial for the Hill Mustang so the number rests on the museum's own page alone|P51D|on_display
Lockheed|T-33|A|52-9535|Shooting Star||fixed_wing|monoplane|military|trainer||CORRECTION: exhibited and captioned by the museum as an F-80A with serial 44-84999; an Aerial Visuals dossier carrying a dated photographer log of 26 May 2015 identifies the airframe as a T-33A-1-LO serial 52-9535 marked as P-80A 44-84999; 52-9535 checks against the T-33A FY52 block and 44-84999 against the P-80A FY44 block so both are individually plausible and only the dated photo log separates them|T33A; F-80A; F80A; P-80A; P80A; Shooting Star; 44-84999|on_display
Republic|F-84|F|51-1640|Thunderstreak||fixed_wing|monoplane|military|fighter|1954|Museum states manufactured 1954; serial checks against the F-84F FY51 block beginning 51-1640|F84F|on_display
Republic|F-84|G|52-3242|Thunderjet||fixed_wing|monoplane|military|fighter|1953|Museum states manufactured 1953; serial checks against the F-84G FY52 block|F84G; N5036K|on_display
North American|F-86|F|52-4978|Sabre||fixed_wing|monoplane|military|fighter|1953|Museum states manufactured 1953 and acquired in 2004; a dated photographer log of 26 May 2015 records 52-4978 on site; serial checks against the F-86F-30-NA FY52 block; the Aerial Visuals headline FAAC-123 is a later foreign air force number within the same dossier not a competing identity; NMUSAF loan|F86F; F-86F-30-NA; FAAC-123|on_display
Northrop|F-89|H|54-0322|Scorpion||fixed_wing|monoplane|military|fighter||Serial checks against the F-89H FY54 block which begins at 54-0322|F89H|on_display
North American|F-100|A|52-5777|Super Sabre||fixed_wing|monoplane|military|fighter|1954|Museum states manufactured 1954; serial checks against the F-100A FY52 block|F100A; c/n 192-22; N1453|on_display
McDonnell|F-101|B|57-0252|Voodoo||fixed_wing|monoplane|military|fighter|1959|Museum states it rolled off the assembly line in 1959; serial checks against the F-101B FY57 block|F101B; c/n 430|on_display
Convair|F-102|A|57-0833|Delta Dagger||fixed_wing|monoplane|military|fighter|1958|Museum states manufactured 1958; serial checks against the F-102A-90-CO FY57 block|F102A; Deuce; c/n 8-10-799|on_display
Lockheed|F-104|A|56-0753|Starfighter||fixed_wing|monoplane|military|fighter|1957|Museum states manufactured 1957 and Aerial Visuals records USAF acceptance 22 August 1957; serial checks against the F-104A-10-LO FY56 block; previously displayed at Arkansas National Guard HQ Robinson AAF and moved to Hill after June 2007|F104A; c/n 183-1041|on_display
Republic|F-105|D|59-1743|Thunderchief||fixed_wing|monoplane|military|ground_attack|1960|Museum states manufactured 1960 and service in the United States and Thailand; serial checks against the F-105D FY59 block|F105D; Thud; c/n D055|on_display
Republic|F-105|G|62-4440|Thunderchief||fixed_wing|monoplane|military|electronic_warfare||Wild Weasel conversion; serial checks against the F-105F FY62 block 62-4412/4447 from which G models were converted|F105G; Wild Weasel; F-105F; F105F; c/n F029|on_display
General Dynamics|F-111|E|68-0020|Aardvark||fixed_wing|monoplane|military|bomber|1969|Museum states manufactured 1969; serial checks against the F-111E FY68 block|F111E; Aardvark|on_display
Lockheed|F-117|A|82-0799|Nighthawk||fixed_wing|monoplane|military|ground_attack||Museum prints 82-799; serial checks against the F-117A FY82 block 82-0799/0806; all operational Nighthawks were A models so the variant is recorded as A; the museum has published a restoration video series on this airframe|F117A; F117; Nighthawk; 82-799|on_display
Convair|F-106|A|58-0774|Delta Dart||fixed_wing|monoplane|military|fighter|1959|Museum states manufactured 1959 and that the airframe went to AMARC then Illinois for conversion to a QF-106 target drone; serial checks against the F-106A-100-CO FY58 block; the Aerial Visuals headline AD146 is the drone conversion number not a serial|F106A; QF-106A; QF106A; c/n 8-24-105; AD146|on_display
PZL-Mielec|Lim-5|||MiG-17F||fixed_wing|monoplane|military|fighter||Aerial Visuals identifies this as a Polish WSK-Mielec built Lim-5 serial 406 construction number 1C 04-06; the museum prints 1C0406 in the serial field which is the construction number not a serial; displayed as a Soviet MiG-17F|MiG17F; MiG-17; MiG17; Lim5; Fresco-C; c/n 1C 04-06; 406; 1C0406|on_display
Bell|HH-1|H|70-2470|Iroquois||rotary_wing||military|search_rescue||Museum prints 70-02470; serial checks against the HH-1H FY70 block; delivered to the 1550th Aircrew Training and Test Wing at Hill in 1973|HH1H; UH-1; UH1; Huey; 70-02470|on_display
Sikorsky|CH-3|E|65-12790|Jolly Green Giant||rotary_wing||military|search_rescue|1966|Museum states manufactured 1966 and service in Southeast Asia; serial checks against the CH-3C/E FY65 block|CH3E; S-61R; S61R|on_display
Bell|TH-13|T|67-17053|Sioux||rotary_wing||military|trainer||Serial checks against the TH-13T FY67 block; Aerial Visuals additionally holds a separate Hill TH-13T record with construction number 3760 and registration N62233 which may be the same machine or a second airframe|TH13T; Model 47; H-13; H13; N62233|on_display
Piasecki|CH-21|C|56-2142|Workhorse||rotary_wing||military|transport||Serial checks against the H-21B/C FY56 block; Aerial Visuals records it as a CH-21B while the museum displays it as a CH-21C-VL|CH21C; H-21; H21; Shawnee; CH-21B; CH21B|on_display
Kaman|HH-43|B|62-4561|Huskie||rotary_wing||military|search_rescue|1963|Museum states manufactured 1963 and service in Japan Oklahoma and finally Hill; serial checks against the HH-43B/F FY62 block; Aerial Visuals records it as an HH-43F|HH43B; HH-43F; HH43F; H-43; H43|on_display
Sikorsky|MH-53|M|68-10369|Pave Low IV||rotary_wing||military|search_rescue||Serial checks against the HH-53/CH-53C FY68 block which ends at 68-10369|MH53M; Pave Low; HH-53; HH53; S-65|on_display
Cessna|O-2|A|68-10853|Super Skymaster||fixed_wing|monoplane|military|recon||Serial consistent with the O-2A FY68 series; Aerial Visuals records it as a GO-2A ground instructional conversion|O2A; Model 337; GO-2A; GO2A|on_display
Lockheed|U-2|C|56-6716|Dragon Lady||fixed_wing|monoplane|military|recon||Serial checks against the U-2 FY56 block; Aerial Visuals records the airframe as a U-2A while the museum displays it as a U-2C|U2C; U-2A; U2A; Article 383|on_display
North American Rockwell|OV-10|A|67-14675|Bronco||fixed_wing|monoplane|military|recon|1968|Museum states manufactured 1968 and assignment to Da Nang Air Base South Vietnam the following year; serial checks against the OV-10A FY67 block|OV10A; c/n 321-083|on_display
Martin|RB-57|A|52-1492|Canberra||fixed_wing|monoplane|military|recon|1955|Museum states manufactured 1955 and service with the 7499th Support Group on Operation Heart Throb; serial checks against the B-57A/RB-57A FY52 block; licence-built English Electric Canberra|RB57A; B-57; B57; English Electric Canberra; c/n 075|on_display
Lockheed|SR-71|C|61-7981|Blackbird||fixed_wing|monoplane|military|recon||The sole SR-71C; a composite airframe reassembled from the forward fuselage of a static test article and the wing and rear fuselage of YF-12A 60-6934; NMUSAF loan; confirmed on site by a dated photographer log of 26 May 2015|SR71C; SR-71; SR71; c/n 2000; 60-6934|on_display
North American|AT-6|A|||Texan||fixed_wing|monoplane|military|trainer||Composite airframe assembled by a restoration firm for the Aerospace Heritage Foundation of Utah from parts acquired from several sources; the museum specs block prints 039 which is not a USAAF serial and is not carried as an identity|AT6A; T-6; T6; Harvard; SNJ; 039|on_display
Vultee|BT-13|B|42-90406|Valiant||fixed_wing|monoplane|military|trainer||Serial checks against the BT-13B FY42 block|BT13B; Vibrator; SNV|on_display
Boeing-Stearman|PT-17|||Kaydet||fixed_wing|biplane|military|trainer||Serial 41-25284 checks against the PT-17 FY41 block and the Aerial Visuals construction number 75-2773 is consistent with it; later civil N264HC|PT17; Model 75; Stearman; c/n 75-2773; N264HC|on_display
North American|T-28|B|137749|Trojan||fixed_wing|monoplane|military|trainer||Tail number is a US Navy BuNo which checks against the T-28B BuNo range|T28B; BuNo 137749|on_display
Convair|T-29|C|52-1119|Flying Classroom||fixed_wing|monoplane|military|trainer||Serial checks against the T-29C FY52 block; Aerial Visuals tags this airframe USN which is inconsistent with the USAF-only T-29C programme and is treated as a database error|T29C; C-131; C131; Samaritan; c/n 240-358|on_display
Lockheed|T-33|A|51-9271|Shooting Star||fixed_wing|monoplane|military|trainer|1953|Museum states original delivery to the USAF in 1953; serial checks against the T-33A FY51 block; later civil N1452; described by the museum as its first aircraft|T33A; c/n 580-7055; N1452|on_display
Cessna|T-37|A|57-2259|Tweet||fixed_wing|monoplane|military|trainer||Museum labels it simply T-37; the serial checks against the T-37A FY57 block so the A model is recorded; Aerial Visuals mislabels this same serial as an A-37 Dragonfly|T37A; T-37; Tweety Bird; A-37; A37|on_display
Northrop|T-38|A|61-0824|Talon||fixed_wing|monoplane|military|trainer||Serial checks against the T-38A FY61 block; Aerial Visuals records it as a GT-38A ground instructional conversion|T38A; GT-38A; GT38A|on_display
Beech|C-45|H|52-10862|Expeditor||fixed_wing|monoplane|military|transport||Serial checks against the C-45H FY52 block 52-10539/10904 and the construction number AF-792 is consistent; later civil N87688; this is the serial the museum's own B-29 page mistakenly reproduces|C45H; Model 18; Twin Beech; c/n AF-792; N87688|on_display
Cessna|U-3|A|57-5869|Blue Canoe||fixed_wing|monoplane|military|utility||Museum prints 57-05869; serial consistent with the U-3A FY57 series|U3A; Model 310; L-27; L27|on_display
Piper|L-4|J|45-4655|Grasshopper||fixed_wing|monoplane|military|utility|1945|Museum states manufactured 1945 and service with the 15th Air Force at Bari Italy; serial checks against the L-4J FY45 block|L4J; J-3 Cub; J3 Cub; Cub|on_display
Ryan|L-17|||Navion||fixed_wing|monoplane|military|utility||The museum specs block prints NAV-4-1300 which is a Ryan Navion construction number rather than a serial so no tail number is carried; Ryan built the L-17B and L-17C so one of those is the likely variant but neither is confirmed|L17; Navion; NAV-4-1300; L-17B; L17B; L-17C; L17C|on_display
```

### HILL AIR FORCE BASE MEMORIAL PARK (on-base displays) — NEW SITE

```
Republic|F-105|D|62-4347|Thunderchief||fixed_wing|monoplane|military|ground_attack||Serial checks against the F-105D FY62 block; last flown 3 October 1983 and mounted on a pylon 25 February 1984 during the 419th TFW Thud Out ceremonies as a monument to all USAF personnel lost flying the Thunderchief; holds the type record of 6730.5 flying hours|F105D; Thud; c/n D546|on_display
General Dynamics|F-16|A|78-0065|Fighting Falcon||fixed_wing|monoplane|military|fighter||Block 5; serial checks against the F-16A FY78 block; served the 4th and 421st TFS of the 388th TFW then the 466th of the 419th and finally 419 MXS as a maintenance trainer|F16A; c/n 61-61; HL; HI|on_display
General Dynamics|F-16|C|83-1126|Fighting Falcon||fixed_wing|monoplane|military|fighter||Block 25A; serial checks against the F-16C FY83 block; grounded at Hill in 2006 after depot found an engine bay burn-through and preserved rather than sent to AMARC; placed on display 23 April 2012 which corroborates a 388th Fighter Wing article of 26 April 2012 announcing an F-16 static display added to Hill Memorial Park|F16C; c/n 5C-9; LF; WA; MO|on_display
Lockheed|WC-130|B|62-3493|Hercules||fixed_wing|monoplane|military|recon||Serial checks against the C-130B FY62 block 62-3487/3496; built as a WC-130B weather reconnaissance aircraft|WC130B; C-130B; C130B; c/n 3707|on_display
Lockheed|QT-33|A|156077|Shooting Star||fixed_wing|monoplane|military|drone||Tail number is the US Navy BuNo; built as a T-33A-1-LO and taken on USAF charge as 52-9171 which checks against the T-33A FY52 block before Navy conversion to a QT-33A drone; Aerial Visuals logs it on site in 2013 and 2019|QT33A; T-33A; T33A; BuNo 156077; 52-9171; c/n 580-7225|on_display
```

### UTAH NATIONAL GUARD HEADQUARTERS DRAPER — NEW SITE

```
North American|F-86|F|||Sabre||fixed_wing|monoplane|military|fighter||Composite airframe restored from parts of several F-86E and F models and carrying no data plate so no serial is recorded; restoration credited largely to M/Sgt William Parker of the Utah Air National Guard; previously displayed on a pole at Sellersburg-Clark County Airport Indiana in US Navy FJ-3 Fury markings as Navy 6049; now pole-mounted in the Utah National Guard compound at Draper in clear view from Interstate 15 without entering security and marked 49-1273 as a dedication to a Utah Air National Guard Sabre lost in Lambs Canyon Utah|F86F; F-86E; F86E; FJ-3 Fury; FJ3; 49-1273; 91273; 12769; FU-769; Navy 6049|on_display
```

### VFW POST 5560 MEMORIAL VERNAL — NEW SITE

```
Bell|AH-1|F|78-23110|Cobra||rotary_wing||military|ground_attack||Serial checks against the AH-1S/F FY78 block 78-23046/23128; Aerial Visuals places the airframe at VFW Post 5560 Vernal and an independent photographer log dated 30 September 2014 records an AH-1F memorial at Vernal in fantastic condition with M197 cannon and TOW pylons alongside other US Army memorials; the serial itself rests on Aerial Visuals alone|AH1F; AH-1S; AH1S; Cobra; HueyCobra|on_display
```

### CAMP WILLIAMS — NEW SITE

```
Bell|UH-1|||Iroquois||rotary_wing||military|utility||Aerial Visuals gives serial 66-0546 attributed to the USAF with a photograph dated 28 May 2012 at Camp Williams Bluffdale; 66-0546 does not fall in the USAF UH-1F FY66 block 66-1211/1236 and is far more consistent with a US Army UH-1D or UH-1H so the attribution is doubtful and no tail number is carried; the variant could not be established|UH1; Huey; 66-0546|on_display
```

### NORTHROP GRUMMAN ROCKET GARDEN PROMONTORY — NEW SITE

```
Thiokol|Space Shuttle SRB||||Space Shuttle Solid Rocket Booster|missile_rocket||civilian|launch_vehicle||Full length solid rocket booster displayed horizontally and the largest item in the garden; the Promontory plant produced the Shuttle SRB motors; attested independently by Roadside America and by a dated 2024 field photography report|SRB; RSRM; Redesigned Solid Rocket Motor|on_display
Thiokol|Minuteman|||Minuteman||missile_rocket||military|ballistic||Three-stage land-based intercontinental ballistic missile; attested independently by Roadside America and by a dated 2024 field photography report|LGM-30; LGM30; Minuteman ICBM|on_display
Thiokol|Trident|||Trident||missile_rocket||military|ballistic||Submarine launched ballistic missile; attested by a dated 2024 field photography report and by the Box Elder County Museum rocket garden guide|UGM-96; UGM-133|on_display
Thiokol|Peacekeeper|||Peacekeeper||missile_rocket||military|ballistic||Named in the Box Elder County Museum rocket garden guide published January 2026|LGM-118; LGM118; MX|on_display
Thiokol|Star 30|BP|||Star 30BP motor|missile_rocket||civilian|launch_vehicle||Apogee kick motor used on satellites in geosynchronous orbit; named in the Box Elder County Museum rocket garden guide published January 2026|Star30BP; Star-30BP|on_display
```

### Already-recorded sites: **nothing to add**

- **Western Sky Aviation Warbird Museum** — Wikipedia's list and the museum's own fleet page both reduce to your existing 13. The fleet page's "MiG-15 UTI" and "MiG-15bis Chinese variant" are the SBLim-2 N15UT and Shenyang J-2 you already hold; "MiG-17 Polish-built 1959" is Lim-5 N509. Aerial Visuals adds one identity note only: the J-2 is PLAAF **03274**, c/r **N115M**. The T-33 and P-51 the fleet page mentions are described by the museum itself as visitors that require calling ahead — excluded as not resident.
- **Historic Wendover Airfield Museum** — nothing beyond your 3. Wikipedia's extra item is an aluminium *scale model* B-24H by Guillermo Rojas Bazan, not an airframe. Aerial Visuals holds a separate Wendover Airport record for two ex-RCAF Canadair Silver Star 3s (21129/NX84TB, 21456/N333MJ) but flags them "may be based here" — based aircraft, not museum displays.
- **Utah Military Museum at Historic Fort Douglas** — nothing beyond your 3; Aerial Visuals' Fort Douglas dossier lists exactly those three.
- **CAF Utah Wing Museum** — nothing addable. See open question 3.

---

## 3. NOTES

### Sources and their weight

- **Hill's own site was the backbone but had to be scraped page-by-page.** The category page carries no serials; each of the 75 aircraft has a detail page with a specs block that does. I fetched all 75. **Currency: strong** — the site references Fly-by Fridays events in August 2026.
- **Aerial Visuals' `Locator.php` accepts a `Region` POST** and returns a full Utah location index with per-location dossiers. This is what produced every new site in this package. Its per-airframe dossiers carry dated photographer logs, which is the only real currency evidence available for Utah's monuments.
- **Aerial Visuals' aggregate counts are worthless.** It claims "250+ aircraft" for Hill and "30+" for Western Sky. Both are wrong by a factor of three or more — it is counting every airframe ever associated with a location, including departed ones. Its *per-airframe* dossiers are good; its *counts* are not. Use accordingly.
- Aerial Visuals' `AirframeDossier.php` returns fatal PHP errors on some requests but works reliably via `curl` with a browser UA; `WebFetch` on a bare dossier URL failed where curl succeeded.
- **Everything Aerial Visuals flags "NEED HELP" is its own admission of doubt, not a record.** I did not create rows from any of them.

### Corrections made, with evidence

1. **Hill's B-29 serial is wrong on the museum's own page.** It prints `52-10862`, which is the serial of the museum's *own Beech C-45H* (confirmed: the C-45H page prints the same number, and Aerial Visuals gives C-45H 52-10862 c/n AF-792 N87688, which checks against the C-45H FY52 block 52-10539/10904 — the B-29 has no FY52 block at all). True identity **44-86408 "Straight Flush"**, given independently by airplanes-online and by a Vintage Aviation News article dated 28 July 2025, and consistent with the museum's own "B-29-55-MO" block designation. That article also establishes it is **under restoration with outboard wings removed** — so its display_status is wrong if you have it as on_display.
2. **Hill's "F-80A 44-84999" is a T-33A wearing false markings.** Aerial Visuals dossier 10229 carries a photographer log dated 26 May 2015 reading "Lockheed T-33A-1-LO s/n 52-9535 USAF Marked as P-80A 44-84999." Both numbers are block-valid, which is exactly why this one has propagated.
3. **Hill's "A-1E 52-0247" does not exist as an identity.** The airframe is AD-6/A-1H **BuNo 135247** c/n 9891, displayed as an A-1E in false markings "USAF 120247". The museum's 52-0247 looks like a garbling of the marking 120247.
4. **Hill's C-119G "22107" is NOT a construction number** — my initial suspicion, and it was wrong. It is the genuine **RCAF serial**; c/n is 10738 and the civil registration was N966S. It wears *false* USAF markings 52-2107. Worth flagging because the correct-looking "52-2107" is the trap here, not 22107.
5. **Hill's P-40N is recorded by Aerial Visuals as a replica.** I did not carry the museum's 42-105270 into `tail_number`.
6. **Hill's MiG-17F is a Polish PZL/WSK-Mielec Lim-5**, and the "1C0406" in its serial field is the construction number (1C 04-06); the serial is 406. Same failure mode as Castle Air Museum's c/n-in-serial-field problem.
7. **Hill's AT-6A "039", Burgess-Wright "69115", L-17 "NAV-4-1300" and MiG-21F "585" are all non-serials** (composite with no identity, unrecognised number, Ryan Navion c/n, and a marking respectively). All four left blank in `tail_number` with the printed value preserved bare in `aliases`.
8. **AH-1 70-16042 collision resolved.** Aerial Visuals lists it at *both* Fort Douglas and "Utah Army National Guard, Salt Lake City". The airframe dossier makes the ARNG entry the *former* location and Fort Douglas current. Your existing Fort Douglas record is correct; I did not create a duplicate.
9. **The "Bountiful F-86A 49-1273" and the "Draper F-86F" are the same airplane.** Aerial Visuals holds two records; dossier 154058 shows the Draper machine is a composite with no data plate *marked* 49-1273 as a memorial dedication. Dossier 16183 is the ghost that marking generated. One site record, no serial.

### Judgment calls

- **Hill's roster is exactly 75, not 90+.** I am returning the museum's own published list in full, as asked. Since your DB holds 76, the diff should surface roughly one extra record — check first for a **C-130E 64-0569** and an **RF-84F 51-17046**, both of which Aerial Visuals associates with Hill but which are absent from the museum's current collection page (see open question 2).
- Hill's `year_built` is populated for 30 of 75, every one from an explicit museum statement of manufacture, roll-out, delivery or acceptance. **No FY prefix was ever used as a year.** Note that where both exist they usually differ (F-15A: FY77, built 1978; A-10A: FY73, delivered 1975; F-104A: FY56, accepted 1957) — exactly the pattern the rule exists to protect.
- The Draper F-86 is `public` despite standing inside a Guard compound: the Waymarking entry states explicitly that it is pole-mounted and visible from I-15 with "no need to get into the security to see the display."
- Hill Memorial Park is `restricted` — it is inside the Hill AFB fence line.
- The Rocket Garden is `public` (free, unfenced, outside the controlled area) per the factory-tours listing, which also gives daily 9–5.
- Camp Williams UH-1 is recorded with **no tail number** despite Aerial Visuals offering one, because 66-0546 fails the USAF UH-1F block check that AV's own "USAF" attribution implies. Presence is sound; identity is not.

### Excluded, and why

- **Southern Utah Air Museum, Washington UT — CLOSED.** Confirmed by Yelp ("CLOSED") and aviationmuseum.eu. It held a B-52G 59-2579, C-97G 52-2656, T-29C 53-3477, T-37A 57-2269, F-106B 59-0164, KA-3B 147657, C-118A 53-3275, WC-130E 64-0553, T-33 51-6557 and T-38A 64-13179. **Where those ten airframes went is unresolved and is the single biggest open item in Utah.** Do not create this site.
- **Green River Launch Complex** — abandoned; launch pads, blockhouse and raceways only, no displayed vehicles.
- **Riverton Veterans Park UH-1** — a 2018 news hit that is **Riverton, Wyoming**, not Utah.
- **HMdb F-4D 64-965** — Canton, **Texas**. **emsvf.org RF-4C 67-0438** — Meridian, **Mississippi**. **National War Memorial Registry F-86** — Greenville, **South Carolina**. Three separate false positives from state-agnostic searches.
- **Bountiful Veterans Park** — its own website describes granite name walls and no aircraft. The AV "F-86 in Bountiful" lead is the Draper airframe's marking, resolved above.
- **Beaver T-33 49-0902** — AV flags it "there *may* be a T-33 displayed in Beaver"; no venue, no coordinates, no sighting newer than a 2010 compilation. Serial is block-valid but that is all.
- **Wellington American Legion Post 44 T-38** — AV "NEED HELP", empty dossier, no corroboration.
- **Salt Lake City ANG F-105B and F-86A** — AV "NEED HELP", no map reference, and the F-86A number is the Draper marking again.
- **Utah State University Logan** (CT-39A 62-4464, HH-52A 1377) and **Utah Technical College / SLCC** (Piper U-11A BuNo 149052, Bell 206 71-20739 and 68-16793, CT-39A 62-4498, Jet Provost XN506) — ground-instructional airframes in aviation-maintenance programmes, not displays, and with no currency evidence past a 2010 compilation. Excluded on both grounds.
- **Based / operational aircraft, not displays:** Ogden Municipal (three Vampires, two Jet Provosts, OV-1D N10VD), Heber Valley/Worldwide Warbirds (Otter, PV-2 Harpoon, L-29, Yak-50, CJ-6s), SLC International (Harvard, Jet Provost, L-39), Bountiful Skypark, Brigham City Municipal, Provo (two Mustangs), Spanish Fork (Whirlwind XR483), SLC Municipal 2 (Venom J-1730), Wendover Airport (two Canadair Silver Stars).
- **Delle "Bomb Range" F-4s** — range targets on the Utah Test and Training Range, not displays.
- **Rocket garden items I would not write:** Roadside America alone names Patriot, Maverick, Minotaur, Antares and an Atlas. Patriot and Maverick are Raytheon weapons even though Northrop/Thiokol built motors for them, so `manufacturer` is genuinely ambiguous, and no second source names any of the five. Per your rule I am returning a note instead of rows. The garden reportedly holds "nearly 40" items; I am giving you the 5 I can defend and telling you the other ~35 are unenumerated in any source I found.
- **CAF Utah Wing TBM Avenger** — the wing's site advertises a TBM giving rides. It is an operating ride aircraft, and I could not confirm a registration or that it is Utah Wing-assigned rather than visiting. See open question 3.

### Deliberate blanks

- `tail_number` blank at Hill for: Wright Flyer, Burgess-Wright, MiG-21F, P-40N, AT-6A, L-17. Blank for the Draper F-86 (no data plate) and the Camp Williams UH-1 (failed block check).
- `variant` blank for the B-29 (plain B-29, block suffix is not a variant designator), the VC-131, the Lim-5, the Camp Williams UH-1 and all rocket-garden entries.
- `year_built` blank for 45 of the 75 Hill airframes and for **every** airframe at the five new sites — no construction, roll-out, first-flight, delivery or acceptance date was sourced for any of them.
- Camp Williams `address` and `postal_code`, and Hill Memorial Park `address`, and the Vernal `address` — unverified, left blank rather than guessed.

### Needs a human on site — ranked

1. **Where did the Southern Utah Air Museum's ten airframes go?** A B-52G, a C-97G, an F-106B and a KA-3B do not evaporate. Last listed phone **(435) 669-7768**. One call could either create a site or close ten questions.
2. **Hill Aerospace Museum, (801) 825-5817.** Four questions in one call: (a) confirm the B-29 is 44-86408 and that the website's 52-10862 is the C-45H's number; (b) confirm the "F-80A" is really T-33A 52-9535; (c) confirm the A-1 is BuNo 135247; (d) is the C-130E 64-0569 and/or RF-84F 51-17046 (a cockpit section reportedly restored by Utah State University for Hill) on the property? That last one probably explains your 76-vs-75 gap.
3. **CAF Utah Wing, (435) 709-7269.** Registration of the TBM Avenger, whether it is wing-assigned, and the registration of the T-6 you hold with no serial. Wikipedia was last updated May 2026 and still lists only two aircraft, which does not match the wing's own site.
4. **VFW Post 5560, Vernal.** Post 5560 does **not appear** in the current Utah VFW state directory (District 6 now lists only Price 2379, Fort Duchesne 4519 and Moab 10900). The Cobra was photographed in Vernal in September 2014, but the post's 2026 status and the airframe's custody are both unverified. This is my least-confident site record.
5. **Hill AFB public affairs.** Confirm the five Memorial Park airframes are all still standing, and identify the **F-4 at the Roy Gate** referenced in the 388th FW's own April 2012 article — Aerial Visuals holds four Hill-associated Phantoms not on the museum list (F-4C 64-0664, NRF-4C 65-0905, F-4E 68-0304, F-4E 68-0476) and one of them is likely it.
6. **Dugway Proving Ground.** Aerial Visuals places **B-29A 42-94052** there — ex-RAF Washington B.1 WF444, and the serial checks against the B-29A-25-BN block. If that is a survivor rather than a range hulk it is nationally significant. Almost certainly inaccessible; worth one email.
7. **Northrop Grumman Promontory, (435) 471-3500.** Ask for the garden's signage list. That converts ~35 unenumerated items into rows.

### Currency summary, stated plainly

| Site | Best currency evidence | Age |
|---|---|---|
| Hill Aerospace Museum | own site, Aug 2026 events; B-29 article Jul 2025 | current |
| Hill AFB Memorial Park | 388th FW article Apr 2012 + AV logs 2013/2019 | 7–14 yrs |
| Utah NG HQ Draper | Waymarking entry, undated visit logs | unknown |
| VFW 5560 Vernal | photographer log 30 Sep 2014 | 12 yrs |
| Camp Williams | photograph 28 May 2012 | 14 yrs |
| Rocket Garden | Box Elder County guide, Jan 2026 | current |

Only Hill and the Rocket Garden meet a strict "open in 2026" test on evidence. The other four rest on last-known-good sightings between 2012 and 2014, and I would not claim more than that.