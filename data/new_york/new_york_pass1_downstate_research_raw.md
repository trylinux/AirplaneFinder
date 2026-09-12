# NEW YORK — PASS 1: DOWNSTATE (NYC / Long Island / Hudson Valley) + ESAM top-up
Research date: 10 September 2026. Compiled per /home/claude/newyork/BRIEF.md.

---

## 1. SITES

name|city|state_province|country|postal_code|region|address|website|access_type|latitude|longitude
Intrepid Sea<<>>, Air & Space Museum|New York|New York|United States|10036|North America|Pier 86 W 46th St & 12th Ave|https://intrepidmuseum.org|public|40.764600|-74.000100
Cradle of Aviation Museum|Garden City|New York|United States|11530|North America|Charles Lindbergh Blvd|https://www.cradleofaviation.org|public|40.728864|-73.596825
American Airpower Museum|Farmingdale|New York|United States|11735|North America|1230 New Highway Republic Airport|https://www.americanairpowermuseum.com|public|40.729100|-73.415700
Old Rhinebeck Aerodrome|Red Hook|New York|United States|12571|North America|9 Norton Road|https://oldrhinebeck.org|public|41.971500|-73.863200
Empire State Aerosciences Museum|Glenville|New York|United States|12302|North America|250 Rudy Chase Drive|https://www.esam.org|public|42.859960|-73.932079
Grumman Memorial Park -- Calverton|Calverton|New York|United States|11933|North America|NY-25 Middle Country Road at Grumman Boulevard|https://grummanmemorialpark.org|public|40.924700|-72.765400
Historic Aircraft Restoration Project -- Brooklyn|Brooklyn|New York|United States|11234|North America|Hangar B Floyd Bennett Field Gateway National Recreation Area|https://www.nps.gov/gate|public|40.589300|-73.889600
New York Hall of Science Rocket Park -- Queens|Corona|New York|United States|11368|North America|47-01 111th Street Flushing Meadows-Corona Park|https://nysci.org|public|40.736500|-73.852000
Bayport Aerodrome Society|Bayport|New York|United States|11705|North America|Bayport Aerodrome 20 Vitre Avenue|https://www.bayportaerodromesociety.com|public|40.748400|-73.053000

**NOTE ON THE INTREPID SITE LINE.** The database already holds this museum as id 25 under the exact
name `Intrepid Sea, Air & Space Museum`. That name contains a comma, which the unquoted pipe/CSV
contract forbids. I have written it above with a `<<>>` placeholder where the comma belongs — the
importer MUST match the EXISTING row by id 25 and must NOT create a new site. Same for
`Empire State Aerosciences Museum` (id 268), which is already correct and comma-free.

**Coordinate provenance:** Cradle = Aerial Visuals mapped fix on museum building (site E of
LocationDossier 3177). ESAM = coordinates embedded in the museum's own Google Maps link on esam.org.
All others = geocoded street address or airport/park reference point; Intrepid = Pier 86 berth.

---

## 2. AIRCRAFT

### Intrepid Sea, Air & Space Museum
(top-up of existing id 25. **DELETE the existing bogus row Lockheed Martin C-130J 99-1431** —
that airframe was destroyed 25 Jan 2001 and has never been at Pier 86.)

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Lockheed|A-12||60-6925||Blackbird|fixed_wing|monoplane|military|recon||First production A-12 built for the CIA Oxcart programme; article number 122; on the flight deck since 2012 and confirmed present on the museum's 2025 exhibition pages|Oxcart; Article 122; c/n 122|on_display
Rockwell|Space Shuttle|OV-101||Orbiter|Enterprise|spacecraft||civilian|space||Approach-and-landing-test orbiter; never flew in space; housed in the Space Shuttle Pavilion on the flight deck since 2012; museum's own 2025-26 pages list it as a permanent exhibition|OV-101; Constitution|on_display
BAC-Aerospatiale|Concorde|102|G-BOAD||Alpha Delta|fixed_wing|monoplane|civilian|commercial_transport|1976|British Airways Concorde 210; holds the New York-London airliner speed record of 2h 52m 59s set 7 Feb 1996; displayed on Pier 86 alongside the ship; returned to the pier after 2023-24 restoration|c/n 210; Alpha Delta|on_display
Grumman|F-14|D|157986||Tomcat|fixed_wing|monoplane|military|fighter||Seventh F-14 built and the F-14D Super Tomcat development airframe; BuNo falls in the 157980-157991 prototype block; long-term flight-deck exhibit|c/n 7; P-1; Super Tomcat|on_display
Grumman|A-6|F|162185||Intruder|fixed_wing|monoplane|military|ground_attack||One of the five A-6F Intruder II prototypes 162183-162187; sister airframe 162184 is at the Cradle of Aviation; sometimes captioned A-6E in older directories|c/n I-678; A-6E; Intruder II|on_display
Grumman|E-1|B|147212||Tracer|fixed_wing|monoplane|military|recon||BuNo checks against the WF-2/E-1B block 147211-147240; wears AU-773; flight deck|c/n 11; WF-2; AU-773; Willy Fudd|on_display
Grumman|F-11|A|141824||Tiger|fixed_wing|monoplane|military|fighter||Ex-Blue Angels; painted as Blue Angel number 5; aviamagazine.com gives 141884 which falls outside the F11F-1 block 141728-141868 and is rejected here|F11F-1; Blue Angel 5|on_display
Grumman|F-9|J|141117||Cougar|fixed_wing|monoplane|military|fighter||F9F-8 Cougar wearing E-210; Blue Angels connection reported; F-9J was the 1962 redesignation of the F9F-8|F9F-8; F-9J; E-210|on_display
Grumman|TBM|3E|53842||Avenger|fixed_wing|monoplane|military|bomber||General Motors-built; BuNo 53842 falls in the TBM-3E block 53050-53949; aviamagazine.com lists TBM-1 24803 instead — that BuNo is a TBM-1C and conflicts with the type the museum itself states|c/n 3904|on_display
Goodyear|FG-1|D|92013||Corsair|fixed_wing|monoplane|military|fighter||Goodyear-built Corsair on loan from the National Naval Aviation Museum; arrived Oct 2024; unveiled 21 March 2025 as centrepiece of a new 10500 sq ft hangar-deck exhibition; painted for Alfred Lerch of VF-10 flying from Intrepid|F4U; Bent-Wing Bird|on_display
Douglas|XBT2D|1|09102||Skyraider|fixed_wing|monoplane|military|ground_attack||Douglas XBT2D-1 Skyraider prototype; BuNo falls in the 09085-09109 prototype block; wears AJ-501; aviamagazine.com prints 109102 with a stray leading digit|c/n 1930; XAD-1; AD-1; AJ-501|on_display
Douglas|A-4|B|142833||Skyhawk|fixed_wing|monoplane|military|ground_attack||Museum states this airframe served aboard Intrepid 1966-1969; wears AK-512|c/n 11895; A4D-2; AK-512; Scooter|on_display
Douglas|F-6|A|134836||Skyray|fixed_wing|monoplane|military|fighter||Construction number 10430; delivered to the US Navy 1956; served aboard Intrepid; struck off charge 5 Dec 1961; at New England Air Museum 1984-2021; barged to Pier 86 and placed on the flight deck 27 July 2021|F4D-1; c/n 10430|on_display
Douglas|F3H|2N|146739||Demon|fixed_wing|monoplane|military|fighter||BuNo checks against the F3H-2N block 146709-146740; wears AF-105|c/n 78; F-3C; AF-105|on_display
McDonnell Douglas|F-4|N|150628||Phantom II|fixed_wing|monoplane|military|fighter||US Marine Corps airframe; Wikipedia's F-4 survivors list records it at Intrepid in VMFA-323 markings; museum caption ties it to Operation Eagle Claw 1980; wears NK-101|c/n 286|on_display
North American|FJ|3|135868||Fury|fixed_wing|monoplane|military|fighter||BuNo checks against the FJ-3 block 135774-136162; wears AF-203; captioned FJ-2/-3 by the museum|c/n 194-95; F-1C; AF-203|on_display
Vought|F-8|K|145550||Crusader|fixed_wing|monoplane|military|fighter||F8U-1 rebuilt as F-8K; BuNo falls in the 145546-145562 block; wears AK-102|AK-102|on_display
General Dynamics|F-16|A|79-0403||Fighting Falcon|fixed_wing|monoplane|military|fighter||FY79 block 79-0288/79-0409 confirms the F-16A; museum states it flew in Operation Desert Storm|c/n 61-188|on_display
McDonnell Douglas|AV-8|C|159232||Harrier|fixed_wing|monoplane|military|ground_attack||US Marine Corps AV-8A upgraded to AV-8C; BuNo in the 158384-159378 Harrier block; wears NM-601|c/n 712141; NM-601; Hawker Siddeley Harrier|on_display
Israel Aircraft Industries|Kfir|C2|999734||F-21A Lion|fixed_wing|monoplane|military|fighter||Ex-Israeli Kfir C.2 leased to the US Navy/Marine Corps as an F-21A aggressor; the 999xxx number is the US inventory number carried by the leased Kfirs; true Israeli serial not established|F-21A; Lion|on_display
Dassault|Etendard|IVM|60||Etendard|fixed_wing|monoplane|military|ground_attack||French Navy Etendard IVM number 60; some sources caption it Super Etendard — the airframe is the earlier IVM|Etendard IVM|on_display
Mikoyan-Gurevich|MiG-21|PFM|4105||Fishbed|fixed_wing|monoplane|military|fighter||Ex-Polish Air Force; construction number 94A4105 gives the airframe number 4105; displayed in North Vietnamese markings|c/n 94A4105; Fishbed|on_display
PZL-Mielec|Lim-5||0327||MiG-17F Fresco|fixed_wing|monoplane|military|fighter||Polish-built MiG-17F; displayed in North Vietnamese camouflage; serial 0327 is reported by silverhawkauthor and is not independently confirmed — treat as provisional|MiG-17F; Fresco C; Lim-5|on_display
Aermacchi|MB-339|PAN|MM54439||Frecce Tricolori|fixed_wing|monoplane|military|trainer||Italian Air Force display aircraft in Frecce Tricolori colours; carries display number 7|c/n 6598; MM54439|on_display
Beechcraft|T-34|A|N34Z||Mentor|fixed_wing|monoplane|military|trainer||Civil-registered Mentor displayed on the flight deck|c/n G-283|on_display
Northrop|T-38||N913NA||Talon|fixed_wing|monoplane|civilian|trainer||Ex-NASA astronaut-proficiency Talon in NASA markings|N913NA|on_display
Bell|UH-1|A|59-1621||Iroquois|rotary_wing||military|utility||US Army; FY59 UH-1A|c/n 80; Huey; HU-1A|on_display
Bell|AH-1|J|159218||SeaCobra|rotary_wing||military|ground_attack||US Marine Corps; BuNo in the AH-1J block 159210-159228; museum states it flew to Pier 86 under its own power|c/n 26058; Sea Cobra; 704|on_display
Piasecki|HUP|2|128519||Retriever|rotary_wing||military|utility||Painted to represent a helicopter once based aboard Intrepid; wears HU-69; aviamagazine.com gives 128518 — one digit apart and unresolved; both fall in the HUP-2 block 128507-128582|HU-69|on_display
Sikorsky|HO4S|3G|1308||Chickasaw|rotary_wing||military|search_rescue||US Coast Guard; captioned H-19 Chickasaw by the museum; USCG number 1308|c/n 55-729; H-19; HO4S-3G; 95|on_display
Sikorsky|HH-52|A|1429||Seaguard|rotary_wing||military|search_rescue||US Coast Guard HH-52A number 1429|c/n 62117; S-62; Sea Guard|on_display
RSC Energia|Soyuz|TMA-6||Descent Module||spacecraft||civilian|space|2005|Flown Soyuz TMA-6 descent module; docked with the International Space Station in 2005; displayed in the Space Shuttle Pavilion|Soyuz TMA-6|on_display
NASA|Mercury|Replica|||Aurora 7|spacecraft||civilian|space||REPLICA of Scott Carpenter's Mercury capsule Aurora 7 — flagged as a replica; the flown Aurora 7 is at the Museum of Science and Industry Chicago|Aurora 7; Mercury-Atlas 7|on_display

### Cradle of Aviation Museum
(~75 airframes claimed by the museum; the list below is what I can substantiate. Serials
re-anchored against the Aerial Visuals location dossier because aviationmuseum.eu's table for
this museum is column-shifted by one row over a long stretch — see NOTES.)

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Grumman|F-14|D|164603||Tomcat|fixed_wing|monoplane|military|fighter||The last US Navy F-14 to fly — Felix 101 of VF-31 — flown to Calverton 4 Oct 2006; restoration completed and unveiled at the museum in 2023; displayed outside the building|Felix 101; NK-101; Felix One|on_display
Grumman|F-14|A|157982||Tomcat|fixed_wing|monoplane|military|fighter||Third F-14 built; R&D airframe; Hangar 2 Jet Gallery; Aerial Visuals maps it inside Hangar 2|YF-14A; c/n 3|on_display
Grumman|F-14|A|160899||Tomcat|fixed_wing|monoplane|military|fighter||Hangar 2 Jet Gallery; several directories describe this as a cockpit/forward-fuselage section only — presence confirmed but completeness not|c/n 160899|on_display
Grumman|A-6|F|162184||Intruder|fixed_wing|monoplane|military|ground_attack||A-6F Intruder II prototype; one of the five-airframe block 162183-162187; sister 162185 is at the Intrepid; Hangar 2 Jet Gallery|Intruder II; A6-F|on_display
Grumman|E-2|C|160012||Hawkeye|fixed_wing|monoplane|military|recon||Outdoor display; Aerial Visuals fixes it at 40.728461 -73.598664; wears AD|c/n 160012; AD|on_display
Grumman|F-9|H|130763||Cougar|fixed_wing|monoplane|military|fighter||F9F-7/8 Cougar; wears R-126; Jet Age Gallery; museum captions it F9F-7|F9F-7; F9F-8; R-126|on_display
Grumman|F-11|A|141832||Tiger|fixed_wing|monoplane|military|fighter||Visitor Center Atrium; BuNo checks against the F11F-1 block 141728-141868; wears 5|F11F-1|on_display
Grumman|F6F|5K|94263||Hellcat|fixed_wing|monoplane|military|fighter||World War Two Gallery; displayed with wings folded; wears 77|c/n A-12015; F6F-5|on_display
Grumman|F4F|3|12297||Wildcat|fixed_wing|monoplane|military|fighter||World War Two Gallery; wears 4|c/n 5957|on_display
Grumman|F3F|2|||Flying Barrel|fixed_wing|biplane|military|fighter||REPRODUCTION F3F-2 in Golden Age Gallery; Aerial Visuals explicitly flags it as a replica; wears 0968 and 6-F-1 as painted markings|F3F-2; 0968; 6-F-1|on_display
Grumman|TBM|3E|91586||Avenger|fixed_wing|monoplane|military|bomber||World War Two Gallery; carried civil registration N9433Z before preservation; wears 113|c/n 4491; N9433Z; TBM-3E|on_display
Grumman|G-21|A|||Goose|fixed_wing|monoplane|civilian|utility||Golden Age Gallery; Aerial Visuals records it as a JRF-1 Goose; museum captions it G-21 Goose; registration reported as NC169134 by aviationmuseum.eu whose table is shifted — not carried here|JRF-1; OA-13; Goose|on_display
Grumman|G-63||NX41858||Kitten I|fixed_wing|monoplane|civilian|private||Jet Age Gallery; the sole Grumman G-63 Kitten I|c/n 1|on_display
Grumman|OV-1|B|59-2633||Mohawk|fixed_wing|monoplane|military|recon||Aerial Visuals records the airframe as a JOV-1B Mohawk serial 59-2633; aviationmuseum.eu prints 0-12994 which is a buzz-number style rendering and is not carried here|JOV-1B; AV-1B; Mohawk|on_display
Fairchild Republic|A-10|A|76-0535||Thunderbolt II|fixed_wing|monoplane|military|ground_attack||Hangar 2 Jet Gallery; FY76 A-10A block; wears NF|Warthog; NF|on_display
Fairchild Republic|A-10|A|77-0252||Thunderbolt II|fixed_wing|monoplane|military|ground_attack||Cockpit/forward fuselage section only inside the main museum|c/n A10-177; Warthog|on_display
Fairchild Republic|T-46|A|||Eaglet|fixed_wing|monoplane|military|trainer||T-46A flight demonstrator in the Jet Age Gallery; the Long Island-built next-generation trainer cancelled in 1986|Eaglet; NGT|on_display
Republic|P-47|N|44-89444||Thunderbolt|fixed_wing|monoplane|military|fighter||World War Two Gallery; Farmingdale-built; Aerial Visuals gives 44-89444 for the P-47N and 45-59504 for the F-84B; aviationmuseum.eu transposes these two|Jug; Thunderbolt|on_display
Republic|F-84|B|45-59504||Thunderjet|fixed_wing|monoplane|military|fighter||Jet Age Gallery; museum captions it P-84B; FY45 block 45-59482/45-59573 confirms the F-84B|P-84B; Thunderjet|on_display
Republic|F-84|F|51-9480||Thunderstreak|fixed_wing|monoplane|military|ground_attack||Outdoor display per Aerial Visuals; NOTE Wikipedia's American Airpower Museum article also claims 51-9480 — an aircraft is in exactly one place and the mapped Aerial Visuals fix at Garden City is the stronger evidence|Thunderstreak|on_display
Republic|F-105|B|57-5783||Thunderchief|fixed_wing|monoplane|military|ground_attack||Jet Age Gallery; Wikipedia's F-105 survivor list places 57-5783 at the Cradle; Aerial Visuals flagged it as unconfirmed after a 2008 visit but the museum's own current gallery page carries a dedicated F-105B exhibit entry|c/n B20; Thud; Thunderchief|on_display
Republic|F-105|D|||Thunderchief|fixed_wing|monoplane|military|ground_attack||Cockpit section only; wears 631; serial not established|Thud; 631|on_display
Republic|RC-3||N6461K||Seabee|fixed_wing|monoplane|civilian|private||Jet Age Gallery; Aerial Visuals lists it among airframes it could not confirm on-site but the museum's own current gallery page lists the Seabee|c/n 0712; Seabee|on_display
Republic|JB-2|||Loon||fixed_wing|monoplane|military|cruise||American copy of the Fieseler Fi 103 V-1 built by Republic at Farmingdale; World War One/Jet Age display; aviationmuseum.eu's serial 44-89444 for this item is a column shift and belongs to the P-47N|Loon; V-1; Fieseler Fi 103|on_display
Curtiss|JN-4|A|1187||Jenny|fixed_wing|biplane|military|trainer||World War One Gallery; the museum links its Jenny to Charles Lindbergh's barnstorming era|Jenny; JN-4|on_display
Thomas-Morse|S-4|C|38934||Scout|fixed_wing|biplane|military|trainer||World War One Gallery; Aerial Visuals gives serial 38934 and civil registration N1115; aviationmuseum.eu prints 45-15574 for this aircraft which is in fact the WACO CG-4A serial|N1115; Tommy; S4C|on_display
Waco|CG-4|A|45-15574||Hadrian|fixed_wing|monoplane|military|transport||Assault glider; Aerial Visuals gives 45-15574|Hadrian; glider|on_display
Breese|Penguin||33622|||fixed_wing|monoplane|military|trainer||Non-flying World War One ground taxi trainer; World War One Gallery|Penguin|on_display
Sperry|Aerial Torpedo|||Curtiss-Sperry||fixed_wing|biplane|military|cruise||Curtiss-Sperry Aerial Torpedo — the 1918 Long Island-built flying bomb; World War One Gallery; aviationmuseum.eu's AS.22-328 is unverified and not carried|Curtiss-Sperry Flying Bomb|on_display
Sperry|M-1|||Messenger||fixed_wing|biplane|military|utility||REPRODUCTION 1922 Sperry Messenger in the Visitor Center Atrium; Aerial Visuals flags it as a replica|Messenger; Verville-Sperry|on_display
Ryan|NYP|||Spirit of St. Louis||fixed_wing|monoplane|civilian|private||REPRODUCTION Spirit of St. Louis in the Golden Age Gallery; the museum also holds a Ryan B-1 Brougham sister ship; sources disagree on which is displayed — verify on site|Spirit of St. Louis; Ryan B-1 Brougham|on_display
Savoia-Marchetti|S-56|B|N349N||amphibian|fixed_wing|biplane|civilian|private||Aerial Visuals gives c/n 12 and registration N349N; aviationmuseum.eu shifts this registration onto the Ryan NYP|c/n 12; SM.56|on_display
Bleriot|XI||||Bleriot|fixed_wing|monoplane|civilian|private|1909|Hempstead Plains Gallery; the museum dates it 1909|Type XI|on_display
Wright|EX|||Vin Fiz||fixed_wing|biplane|civilian|private||REPRODUCTION of the Wright EX Vin Fiz flown by Cal Rodgers on the first transcontinental flight in 1911; Hempstead Plains Gallery|Vin Fiz|on_display
Curtiss|Golden Flyer||||Golden Flyer|fixed_wing|biplane|civilian|private||REPRODUCTION Curtiss Golden Flyer No. 1; Hempstead Plains Gallery; Aerial Visuals lists it as a Herring-Curtiss 1 replica|Herring-Curtiss 1; Golden Flyer No. 1|on_display
Langley|Aerodrome|5|||Aerodrome Number 5|fixed_wing|monoplane|civilian|experimental||REPRODUCTION of Samuel Langley's 1896 steam-powered Aerodrome Number 5; Dream of Wings Gallery|Aerodrome No. 5|on_display
Lilienthal|Normal-Segelapparat||||glider|fixed_wing|monoplane|civilian|experimental||REPRODUCTION Lilienthal hang glider; Dream of Wings Gallery|Lilienthal glider|on_display
Brunner Winkle|Bird|A|||Bird|fixed_wing|biplane|civilian|private||Golden Age Gallery; Aerial Visuals notes a Brunner-Winkle Bird c/n 1067 registration N787Y as having left the collection — the museum's current gallery page still lists a Brunner Winkle Bird so a second airframe is present or the departure note is stale|Bird A|on_display
Peel|Z-1|||Glider Boat||fixed_wing|monoplane|civilian|experimental||Peel Z-1 Glider Boat; Golden Age Gallery|Z-1 Glider Boat|on_display
Commonwealth|185||N92972||Skyranger|fixed_wing|monoplane|civilian|private||Jet Age Gallery; Aerial Visuals gives c/n 1705 and registration N92972; aviationmuseum.eu shifts N92972 onto a Piper Cherokee cockpit|c/n 1705; Rearwin Skyranger|on_display
Gyrodyne|XRON|1|04014||Rotorcycle|rotary_wing||military|utility||Visitor Center Atrium; Gyrodyne of St James Long Island built the one-man Rotorcycle|Rotorcycle; XRON-1|on_display
Gyrodyne|QH-50|C|||DASH|rotary_wing||military|drone||Drone Anti-Submarine Helicopter built at St James Long Island; Jet Age Gallery; Aerial Visuals lists s/n DS-1235 as unconfirmed so the serial is left blank|DASH; QH-50C|on_display
Gyrodyne|GCA-2|C|N6594K||Gyrodyne|rotary_wing||civilian|experimental||Jet Age Gallery; Aerial Visuals gives c/n 1002 and registration N6594K; aviationmuseum.eu prints N659AK which does not resolve in the FAA registry|c/n 1002; Model 2C|on_display
Convair|340||N24AT||Convair|fixed_wing|monoplane|civilian|commercial_transport||Cockpit/flight-deck section; Aerial Visuals records it as a CV-440 ex-Luftwaffe 12+01 c/n 340-148|c/n 340-148; CV-440; 12+01|on_display
Boeing|707|458||El Al||fixed_wing|monoplane|civilian|commercial_transport||Flight-deck section only; ex-El Al 4X-ATA; Hangar 2 Jet Gallery|c/n 18070; 4X-ATA|on_display
Douglas|C-47|B|||Skytrain|fixed_wing|monoplane|military|transport||Cockpit/forward fuselage section only; serial not established|Dakota; Gooney Bird|on_display
Cessna|172||||Skyhawk|fixed_wing|monoplane|civilian|private||Cockpit section used as a hands-on exhibit|Skyhawk|on_display
Piper|PA-28|140|||Cherokee|fixed_wing|monoplane|civilian|private||Cockpit section; the registration N92972 attached to this item by aviationmuseum.eu belongs to the Commonwealth Skyranger|Cherokee|on_display
Cassutt|Special||||racer|fixed_wing|monoplane|civilian|private||Contemporary Aviation Gallery; Formula One air racer|Cassutt IIIM|on_display
Grumman|G-164|||Ag-Cat||fixed_wing|biplane|civilian|other||Grumman agricultural biplane; reported in the collection by aviationmuseum.eu only — presence not independently confirmed|Ag-Cat|on_display
Klemin|K-1||N69097|||fixed_wing|monoplane|civilian|experimental||Aerial Visuals records a Klemin K-1 c/n 1 registration N69097; aviationmuseum.eu shifts N69097 onto an Aircraft Engineering Company Ace|c/n 1; Ace|on_display
Fleet|Fawn|II|N614M|||fixed_wing|biplane|civilian|trainer||Aerial Visuals gives Consolidated-Fleet Fawn II c/n 190 registration N614M; museum captions the Golden Age display Fleet 2|c/n 190; Fleet 2|on_display
Grumman|Lunar Module|LM-13|||Lunar Module 13|spacecraft||civilian|space||Unflown Apollo Lunar Module built at Bethpage; assigned to the cancelled Apollo 18/19; the centrepiece of the Exploring Space gallery; on loan from the Smithsonian|LM-13; Apollo LM|on_display
Rockwell|Command Module|002|||Apollo Command Module 002|spacecraft||civilian|space||Apollo boilerplate/test Command Module 002 in the Exploring Space gallery|CM-002; Apollo CM|on_display

### American Airpower Museum
(Republic Field Farmingdale. **What I counted:** the static gate/hangar airframes that cannot fly
plus the airworthy warbirds the museum itself lists on its own Collections > Flying Aircraft page as
its collection and which live in the hangar between shows. **What I excluded:** privately-owned
warbirds merely based at Republic Field, and the P-47D NX1345B which crashed in the Hudson on
27 May 2016 — see NOTES.)

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
General Dynamics|F-111|A|67-0047||Aardvark|fixed_wing|monoplane|military|bomber||Static gate display; FY67 F-111A block 67-0032/67-0120; wears ST; named on the museum's own current Static Aircraft page|Aardvark; ST|on_display
Republic|F-105|D|62-4361||Thunderchief|fixed_wing|monoplane|military|ground_attack||Static display; FY62 F-105D block 62-4234/62-4411; wears RU; named on the museum's own current Static Aircraft page|Thud; RU|on_display
Republic|F-84|E|49-2348||Thunderjet|fixed_wing|monoplane|military|ground_attack||Static display; FY49 F-84E block 49-2022/49-2437; named on the museum's own current Static Aircraft page|Thunderjet|on_display
Republic|RF-84|F|53-7595||Thunderflash|fixed_wing|monoplane|military|recon||Static display; FY53 RF-84F block; Farmingdale-built|Thunderflash|on_display
Fairchild Republic|A-10|A|80-0247||Thunderbolt II|fixed_wing|monoplane|military|ground_attack||Cockpit/forward fuselage section; FY80 A-10A block 80-0140/80-0276; the A-10 was designed and first built at this field|Warthog|on_display
Northrop Grumman|EA-6|B|162938||Prowler|electronic_warfare|monoplane|military|electronic_warfare||BuNo checks against the EA-6B block 162934-162939; wears NJ-906|Prowler; NJ-906|on_display
North American|P-51|D|44-14151||Mustang|fixed_wing|monoplane|military|fighter||REPLICA Mustang displayed as 44-14151; flagged as a replica by aviationmuseum.eu|Mustang|on_display
Mikoyan-Gurevich|MiG-21|UM|||Mongol|fixed_wing|monoplane|military|trainer||Cockpit section only; wears 18|Mongol; 18|on_display
Douglas|C-47|B|N15SJ||Skytrain|fixed_wing|monoplane|military|transport||Museum's airworthy Dakota; carries USAAF serial 44-76717 and D-Day invasion stripes as D8-Z; the museum states it flew on D-Day and sells flight experiences in it; currently registered to AMERICAN AIRPOWER MUSEUM INC in the FAA registry as a DC3C c/n 33049|44-76717; D8-Z; Dakota IV; c/n 33049|on_display
Consolidated|PBY|6A|N7057C||Catalina|fixed_wing|monoplane|military|search_rescue||Registered to AMERICAN AIRPOWER MUSEUM in the current FAA registry as a Consolidated Vultee 28-5ACF c/n 64072|Catalina; 28-5ACF; c/n 64072|on_display
Aero Vodochody|L-39|C|N29VP||Albatros|fixed_wing|monoplane|military|trainer||Registered to AMERICAN AIRPOWER MUSEUM INC in the current FAA registry; c/n 031623|Albatros; c/n 031623|on_display
North American|SNJ|5|N26862||Texan|fixed_wing|monoplane|military|trainer||Registered to AMERICAN AIRPOWER MUSEUM in the current FAA registry as an AT-6D c/n 90699; wears 02|AT-6D; Texan; c/n 90699|on_display
Cessna|337|B|N888B||Super Skymaster|fixed_wing|monoplane|civilian|utility||Registered to AMERICAN AIRPOWER MUSEUM in the current FAA registry; c/n 3370586; displayed in the hangar|Super Skymaster; O-2|on_display
Beechcraft|D-45||N4028E||Mentor|fixed_wing|monoplane|military|trainer||Registered to AMERICAN AIRPOWER MUSEUM in the current FAA registry; c/n BG-292|T-34; Mentor; c/n BG-292|on_display
Piper|PA-32|260|N3411W||Cherokee Six|fixed_wing|monoplane|civilian|private||Registered to AMERICAN AIRPOWER MUSEUM in the current FAA registry; c/n 32-272; jump/utility aircraft rather than an exhibit — record only if the importer wants non-exhibit museum-owned aircraft|Cherokee Six|on_display
Curtiss|P-40|M|NX1232N||Warhawk|fixed_wing|monoplane|military|fighter||Airworthy; listed by the museum on its own current Flying Aircraft page; wears 00|Warhawk; Kittyhawk III|on_display
Grumman|TBM|3E|N9586Z||Avenger|fixed_wing|monoplane|military|bomber||Airworthy; listed by the museum on its own current Flying Aircraft page; carries BuNo 85886 and wears SL-401|85886; SL-401|on_display
North American|B-25|J|NL2825B||Mitchell|fixed_wing|monoplane|military|bomber||Airworthy; listed by the museum on its own current Flying Aircraft page; carries 02168|Mitchell; RB-25|on_display
North American|P-51|D|N51HR||Mustang|fixed_wing|monoplane|military|fighter||Airworthy; listed by the museum on its own current Flying Aircraft page; carries USAAF serial 44-63542|Mustang; 44-63542|on_display
North American|T-28|D|||Nomad|fixed_wing|monoplane|military|trainer||Airworthy AT-28D-5 Nomad listed by the museum on its own current Flying Aircraft page; reported on loan; registration not established|AT-28D; Trojan; Nomad|on_display
Waco|UPF|7|N32006|||fixed_wing|biplane|civilian|trainer||Reported in the collection by aviationmuseum.eu; not on the museum's current Flying Aircraft page — presence in 2025-26 unconfirmed|UPF-7|on_display

### Old Rhinebeck Aerodrome
(All 85 aircraft the museum publishes on its own current collection pages. The Aerodrome presents
its whole collection in the museum buildings and the airshow hangars; visitors walk through the
hangars on any open day, so the airworthy airshow fleet is a public display and is recorded, with
`display_status` following the museum's own label: Static Exhibit and Active -> on_display;
Under Restoration -> under_restoration; In Storage -> in_storage. Every reproduction is flagged in
`description`. N-numbers come from the FAA owner-name search on RHINEBECK AERODROME MUSEUM and are
assigned only where the type/constructor match is unambiguous.)

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Aeromarine|39|B||||fixed_wing|biplane|military|trainer|1917|ORIGINAL airframe; museum lists it as in storage|Aeromarine 39B|in_storage
Aeromarine-Klemm|L-26|A|N320N|||fixed_wing|monoplane|civilian|private|1929|ORIGINAL airframe; static exhibit; FAA c/n 2-59|c/n 2-59|on_display
Aeronca|65|TAC|N36967|Defender||fixed_wing|monoplane|civilian|private|1941|ORIGINAL airframe; under restoration; FAA c/n C2711TA|Defender; c/n C2711TA|under_restoration
Aeronca|C-3||N17447|||fixed_wing|monoplane|civilian|private|1936|ORIGINAL airframe; static exhibit; FAA c/n A-754|c/n A-754|on_display
Aeronca|7|AC|N8111N|Champion||fixed_wing|monoplane|civilian|private|1946|ORIGINAL airframe; flown in the airshow; FAA c/n 7AC-3712|Champ; c/n 7AC-3712|on_display
Albatros|D|Va|N12156|||fixed_wing|biplane|military|fighter||REPRODUCTION built by Cole Palen; under restoration; painted in the 2015 colours of Eduard Ritter von Schleich; FAA c/n 17-D-7517|c/n 17-D-7517|under_restoration
Albree|Pigeon-Fraser||||Pursuit|fixed_wing|monoplane|military|fighter|1917|ORIGINAL airframe; only three were built; static exhibit|Pigeon Fraser Pursuit|on_display
American Eagle|A-129||N513H|||fixed_wing|biplane|civilian|private|1929|ORIGINAL airframe; static exhibit; FAA c/n 534|c/n 534|on_display
Ansaldo|A|1||Balilla||fixed_wing|biplane|military|fighter||REPRODUCTION; static exhibit|Balilla; A.1|on_display
Arup|S-2||||flying wing|fixed_wing|monoplane|civilian|experimental|1933|REPRODUCTION of the 1933 Arup S-2 lifting-body aircraft|Arup S-2|on_display
Avro|504|K|N4929|||fixed_wing|biplane|military|trainer||REPRODUCTION built by Cole Palen; under restoration; the museum auctioned surplus Avro 504K artifacts in early 2025; FAA c/n HAC1|c/n HAC1|under_restoration
Brunner Winkle|Bird|CK||||fixed_wing|biplane|civilian|private|1931|ORIGINAL airframe; static exhibit|Bird Model CK|on_display
Bleriot|XI||N60094|||fixed_wing|monoplane|civilian|private|1909|ORIGINAL 1909 airframe with its original Anzani engine; believed the second-oldest airworthy aeroplane in the world; under restoration; FAA c/n 56|c/n 56|under_restoration
Bleriot|XI|||Cross Country||fixed_wing|monoplane|civilian|private|1911|ORIGINAL airframe; the long-span Cross Country variant; static exhibit|Type XI Cross Country|on_display
Boeing|N2S|5||Stearman||fixed_wing|biplane|military|trainer|1943|ORIGINAL airframe; flown in the airshow|Kaydet; PT-17; Stearman|on_display
Bristol|F.2|B||Brisfit||fixed_wing|biplane|military|fighter||REPRODUCTION; flown in the airshow|Brisfit; F2B Fighter|on_display
Burgess-Collier|Flying Boat||||flying boat|fixed_wing|biplane|civilian|private|1913|ORIGINAL airframe; museum lists it as in storage but visible to visitors|Burgess-Collier|in_storage
Caudron|G|III|N3943P|||fixed_wing|biplane|military|recon||REPRODUCTION built by Cole Palen; static exhibit; FAA c/n 1914-2|G.3; c/n 1914-2|on_display
Chanute|Glider||||hang glider|fixed_wing|biplane|civilian|experimental|1896|REPRODUCTION of an Octave Chanute glider; static exhibit|Chanute glider|on_display
Curtiss|Fledgling||N271Y|||fixed_wing|biplane|civilian|trainer|1929|ORIGINAL airframe; in storage; FAA c/n B-52|c/n B-52|in_storage
Curtiss|JN-4|H|N3918|Jenny||fixed_wing|biplane|military|trainer|1917|ORIGINAL airframe; Navy trainer variant; flown in the airshow; FAA c/n 3919|Jenny; c/n 3919|on_display
Curtiss|Pusher|Model A||||fixed_wing|biplane|civilian|experimental|1909|REPRODUCTION; the museum lists it as on loan — confirm whether it is on loan to or from Old Rhinebeck before publishing|Curtiss Model A|on_display
Curtiss|Pusher|Model D||||fixed_wing|biplane|civilian|experimental|1911|REPRODUCTION; flown in the airshow; two Curtiss pushers are FAA-registered to the museum as N4124A c/n 2 and N68014 c/n 1976 but which belongs to Model A and which to Model D is not established|N4124A; N68014|on_display
Curtiss-Wright|CW-1|Junior|N605EB|||fixed_wing|monoplane|civilian|private|1931|ORIGINAL airframe; static exhibit; FAA c/n 1025|Junior; c/n 1025|on_display
Davis|D1|W||||fixed_wing|monoplane|civilian|private|1933|ORIGINAL airframe; flown in the airshow; one of two Davis machines in the collection|Davis D1-W|on_display
Davis|D1|W||||fixed_wing|monoplane|civilian|private|1929|ORIGINAL airframe; under restoration; the FAA registers a Davis V-3 c/n 115 as N532K to the museum — the V-3 designation does not match either D1-W so the registration is left unassigned|N532K; Davis V-3|under_restoration
De Havilland|DH.82||||Tiger Moth|fixed_wing|biplane|military|trainer|1934|ORIGINAL airframe; under restoration|Tiger Moth|under_restoration
Santos-Dumont|Demoiselle||||Demoiselle|fixed_wing|monoplane|civilian|private|1909|REPRODUCTION of the Santos-Dumont Demoiselle; static exhibit|Demoiselle; No. 20|on_display
Deperdussin|Racer||||Monocoque Racer|fixed_wing|monoplane|civilian|experimental|1913|REPRODUCTION of the 1913 Deperdussin monocoque racer; static exhibit|Deperdussin Monocoque|on_display
Dickson|Primary Glider||||glider|fixed_wing|monoplane|civilian|experimental|1930|REPRODUCTION; designed in England by Roger Dickson; static exhibit|Dickson glider|on_display
Etrich|Taube|Model F|N567JD|||fixed_wing|monoplane|civilian|private|1912|REPRODUCTION; flown in the airshow; fitted with a De Havilland Gipsy Major in place of the original Daimler; FAA c/n 015|Taube; c/n 015|on_display
Fairchild|24|H|N19129|||fixed_wing|monoplane|civilian|private|1937|ORIGINAL airframe; static exhibit; FAA c/n 3224|c/n 3224|on_display
Fleet|Finch|16-B|N24197|||fixed_wing|biplane|military|trainer|1942|ORIGINAL airframe; in storage; FAA c/n 303|c/n 303|in_storage
Fleet|Finch|16-B|N666J|||fixed_wing|biplane|military|trainer|1942|ORIGINAL airframe; under restoration; FAA c/n 350|c/n 350|under_restoration
Fleet|Model 1||||Fleet|fixed_wing|biplane|civilian|trainer|1930|ORIGINAL airframe; flown in the airshow|Fleet 1|on_display
Fokker|D|VI|N1649|||fixed_wing|biplane|military|fighter||REPRODUCTION built by Charles Brady; flown in the airshow; FAA c/n 1649|c/n 1649|on_display
Fokker|D|VII|N70814|||fixed_wing|biplane|military|fighter||REPRODUCTION built by James Palen; flown in the airshow; FAA c/n 1918-1989|c/n 1918-1989|on_display
Fokker|Dr.I||N220TP||triplane|fixed_wing|triplane|military|fighter||REPRODUCTION; museum lists this example as on loan; FAA registers a Palmer/Wilgus Fokker F1 c/n F1-103 as N220TP|Dr.1; Triplane; c/n F1-103|on_display
Fokker|Dr.I||N3221||triplane|fixed_wing|triplane|military|fighter||REPRODUCTION; static exhibit; FAA c/n 322|Dr.1; Triplane; c/n 322|on_display
Fokker|Dr.I||||triplane|fixed_wing|triplane|military|fighter||REPRODUCTION built by Cole Palen in the mid-1960s with a Le Rhone 9J; flown in the airshow|Dr.1; Triplane|on_display
Fokker|E|I|||Eindecker|fixed_wing|monoplane|military|fighter||REPRODUCTION; static exhibit|Eindecker; E.I|on_display
Great Lakes|2T-1||N304Y|||fixed_wing|biplane|civilian|private|1931|REPRODUCTION; flown in the airshow; FAA c/n 191|c/n 191|on_display
Great Lakes|2T-1|E|||Modified|fixed_wing|biplane|civilian|private|1931|ORIGINAL airframe modified with a Warner engine; flown in the airshow|2T-1E|on_display
Great Lakes|2T-1|MS||||fixed_wing|biplane|civilian|private|1931|ORIGINAL airframe with a Menasco Pirate; static exhibit|2T-1MS|on_display
Hanriot|||||Hanriot|fixed_wing|monoplane|civilian|private|1910|REPRODUCTION; under restoration; fitted with a 1939 Franklin in place of the original ENV|Hanriot monoplane|under_restoration
Heath|Parasol|LNA-40||||fixed_wing|monoplane|civilian|private|1932|ORIGINAL airframe; static exhibit|Heath Parasol|on_display
Monocoupe|113||||Monocoupe|fixed_wing|monoplane|civilian|private|1929|ORIGINAL airframe; under restoration|Monocoupe 113|under_restoration
Monocoupe|90||||Monocoupe|fixed_wing|monoplane|civilian|private|1931|ORIGINAL airframe; static exhibit; the museum owns two FAA-registered Monocoupe 90s N116V c/n 625 and N429N c/n 618 — which is the 90 and which the 90-J is not established|N116V; N429N|on_display
Monocoupe|90|J|||Monocoupe|fixed_wing|monoplane|civilian|private|1931|ORIGINAL airframe with a Warner Scarab Jr; in storage|Monocoupe 90-J|in_storage
Morane-Saulnier|A|I|N1379M|||fixed_wing|monoplane|military|fighter|1917|ORIGINAL airframe; static exhibit; FAA c/n 417|MS.A-1; c/n 417|on_display
Morane-Saulnier|MS.130||N7MS|||fixed_wing|monoplane|military|trainer|1927|ORIGINAL airframe; static exhibit; FAA c/n 001|MS 130 ET2; c/n 001|on_display
Morane-Saulnier|N||N5356J|Bullet||fixed_wing|monoplane|military|fighter||REPRODUCTION built by Cole Palen; static exhibit; FAA c/n 1915-84|Bullet; c/n 1915-84|on_display
New Standard|D-25||N176H|||fixed_wing|biplane|civilian|transport|1929|ORIGINAL airframe; the barnstorming ride aircraft flown at every airshow; FAA c/n 138|c/n 138|on_display
New Standard|D-25||N19157|||fixed_wing|biplane|civilian|transport|1929|ORIGINAL airframe; under restoration; FAA c/n 162J; a third D-25 N31K c/n 150 is also registered to the museum and is not on the published collection list|c/n 162J|under_restoration
Nicholas-Beazley|NB-8|G|N576Y|||fixed_wing|monoplane|civilian|private|1931|ORIGINAL airframe; static exhibit; FAA c/n K-18|c/n K-18|on_display
Nieuport|10||||Nieuport|fixed_wing|biplane|military|recon|1915|ORIGINAL airframe; static exhibit|Nieuport 10|on_display
Nieuport|11||||Bebe|fixed_wing|biplane|military|fighter|1915|REPRODUCTION; under restoration|Bebe; Nieuport 11|under_restoration
Nieuport|17||||Nieuport|fixed_wing|biplane|military|fighter|1916|REPRODUCTION; museum lists it as on loan|Nieuport 17|on_display
Nieuport|2|N|||Nieuport|fixed_wing|monoplane|civilian|private|1911|REPRODUCTION; static exhibit; the FAA registers a Nieuport 83E c/n 680 as N680CP to the museum which does not match any published collection entry|Nieuport 2N; N680CP|on_display
Passat|Ornithopter||||ornithopter|fixed_wing|monoplane|civilian|experimental|1910|REPRODUCTION; static exhibit|Passat Ornithopter|on_display
Pietenpol|Air Camper||||Air Camper|fixed_wing|monoplane|civilian|private|1928|REPRODUCTION homebuilt; in storage|Aircamper|in_storage
Piper|J-3||||Cub|fixed_wing|monoplane|civilian|private|1941|ORIGINAL airframe; flown in the airshow|Cub|on_display
Pitcairn|PA-6||||Mailwing|fixed_wing|biplane|civilian|transport|1929|ORIGINAL airframe; static exhibit|Mailwing|on_display
Porterfield|CP-65||N37709|Collegiate||fixed_wing|monoplane|civilian|private|1941|ORIGINAL airframe; static exhibit; FAA c/n 938|Collegiate; c/n 938|on_display
Royal Aircraft Factory|F.E.8||N17501|||fixed_wing|biplane|military|fighter|1915|REPRODUCTION built by Cole Palen; museum lists it as on loan; FAA c/n 300|FE8; c/n 300|on_display
Royal Aircraft Factory|S.E.5|a||||fixed_wing|biplane|military|fighter|1917|REPRODUCTION; under restoration|SE5a|under_restoration
Ryan|NYP||N211XC||Spirit of St. Louis|fixed_wing|monoplane|civilian|private||REPRODUCTION of Lindbergh's Spirit of St. Louis; first test flight December 2015; added to the airshow 2016; FAA c/n 30|Spirit of St. Louis; c/n 30|on_display
Short|S.29||N4275|||fixed_wing|biplane|civilian|experimental|1910|REPRODUCTION built by Cole Palen and Jim Cole in 1971 with a 60 hp ENV V-8; static exhibit; FAA c/n 2|Short S-29; c/n 2|on_display
Siemens-Schuckert|D|III|||Siemens|fixed_wing|biplane|military|fighter|1918|REPRODUCTION; static exhibit|SSW D.III|on_display
Sopwith|1 1/2 Strutter||||Strutter|fixed_wing|biplane|military|recon|1916|REPRODUCTION; under restoration|1.5 Strutter; Sopwith Strutter|under_restoration
Sopwith|Camel||N7157Q|||fixed_wing|biplane|military|fighter|1917|REPRODUCTION built by James Palen; flown in the airshow; FAA c/n 1990|c/n 1990|on_display
Sopwith|Dolphin||N47166|||fixed_wing|biplane|military|fighter|1917|REPRODUCTION built by Cole Palen — the first known airworthy Dolphin reproduction attempted; powered by a vintage Hispano-Suiza V-8; under restoration; FAA c/n 1533|c/n 1533|under_restoration
Sopwith|Pup||N5139|||fixed_wing|biplane|military|fighter|1916|REPRODUCTION; the museum lists it as active but Wikipedia states Cole Palen's 1967 Pup is now at the Owls Head Transportation Museum — a second airframe or a stale Wikipedia claim; FAA registers a Sopwith Scout c/n 83213 as N5139 to the museum|c/n 83213|on_display
SPAD|VII||N8096L|||fixed_wing|biplane|military|fighter|1917|REPRODUCTION built by Carl Swanson; flown in the airshow; FAA c/n 1999|SPAD S.VII; c/n 1999|on_display
Spartan|C-3||N285M|||fixed_wing|biplane|civilian|private|1929|ORIGINAL airframe; static exhibit; FAA c/n 120|C3-165; c/n 120|on_display
Stinson|SM-1|B|N1517|Detroiter||fixed_wing|monoplane|civilian|transport|1927|ORIGINAL airframe; flown in the airshow; FAA c/n M-267|Detroiter; c/n M-267|on_display
Taylor|E-2||||Cub|fixed_wing|monoplane|civilian|private|1934|ORIGINAL airframe; flown in the airshow|E-2 Cub|on_display
Taylor|J-2||N17834||Cub|fixed_wing|monoplane|civilian|private|1936|ORIGINAL airframe; flown in the airshow; FAA lists it as a Piper J-2 c/n 1269|J-2 Cub; c/n 1269|on_display
Thomas|Pusher|Model E|N4720G|||fixed_wing|biplane|civilian|experimental|1912|ORIGINAL airframe restored by Cole Palen; static exhibit; FAA c/n 2|Thomas Model E; c/n 2|on_display
Thomas-Morse|S-4|B||Scout||fixed_wing|biplane|military|trainer|1918|ORIGINAL airframe; static exhibit|Tommy; S4B|on_display
Voisin||||Voisin||fixed_wing|biplane|civilian|private|1908|Museum calls it ORIGINAL; the FAA registers a Renik-built Voisin c/n 1 as N38933 to the museum which implies a reproduction — conflict unresolved|N38933; c/n 1|on_display
Waco|10||||Waco 10|fixed_wing|biplane|civilian|private|1927|ORIGINAL airframe; static exhibit|Waco 10; GXE|on_display
Wright|EX|||Vin Fiz||fixed_wing|biplane|civilian|private|1911|REPRODUCTION of the Wright EX Vin Fiz; static exhibit|Vin Fiz|on_display
Wright|Flyer||||Wright Flyer|fixed_wing|biplane|civilian|experimental|1903|REPRODUCTION of the 1903 Wright Flyer; static exhibit|1903 Flyer|on_display
Wright|Glider||||Wright Glider|fixed_wing|biplane|civilian|experimental|1902|REPRODUCTION of the 1902 Wright glider; static exhibit|1902 glider|on_display
Piccard|AX3M||N7132|||lighter_than_air||civilian|private||Hot-air balloon registered to RHINEBECK AERODROME MUSEUM in the current FAA registry as c/n 23; not on the museum's published aircraft collection list — confirm before publishing|c/n 23; balloon|on_display

### Empire State Aerosciences Museum
(top-up of existing id 268. **EXCLUDED as already recorded and genuinely present:**
Lockheed YMC-130H 74-1686.)

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Convair|F-102|A|56-1219||Delta Dagger|fixed_wing|monoplane|military|fighter||Agneta Airpark; FY56 F-102A block 56-0956/56-1544|Deuce; Delta Dagger|on_display
McDonnell|F-101|F|59-0413||Voodoo|fixed_wing|monoplane|military|fighter||Agneta Airpark; FY59 F-101B block 59-0391/59-0483; the F-101F is the dual-control F-101B|Voodoo; F-101B|on_display
McDonnell Douglas|F-4|D|65-0626||Phantom II|fixed_wing|monoplane|military|fighter||Agneta Airpark; FY65 F-4D block 65-0580/65-0801|Phantom|on_display
Republic|F-84|F|51-1620||Thunderstreak|fixed_wing|monoplane|military|ground_attack||Agneta Airpark; FY51 F-84F block 51-1346/51-1786|Thunderstreak|on_display
Republic|F-105|G|62-4444||Thunderchief|fixed_wing|monoplane|military|electronic_warfare||Agneta Airpark; FY62 F-105F block 62-4412/62-4447 from which the G Wild Weasels were converted; Wikipedia's F-105 survivor list places 62-4444 at ESAM|Thud; Wild Weasel|on_display
Fairchild Republic|A-10|A|75-0263||Thunderbolt II|fixed_wing|monoplane|military|ground_attack||Agneta Airpark; FY75 A-10A block 75-0258/75-0309; wears 263|Warthog|on_display
Northrop|F-5|E|162307||Tiger II|fixed_wing|monoplane|military|fighter||Agneta Airpark; ex-US Navy adversary aircraft; wears 06; the BuNo is reported by silverhawkauthor only and is not independently confirmed|Tiger II|on_display
Grumman|F-14|A|160411||Tomcat|fixed_wing|monoplane|military|fighter||Agneta Airpark; BuNo checks against the F-14A block 160379-160414; wears 201|Tomcat|on_display
Grumman|A-6|E|152935||Intruder|fixed_wing|monoplane|military|ground_attack||Agneta Airpark; built as an A-6A in the 152583-152954 block and rebuilt as an A-6E; wears 501 in VA-176 markings|Intruder; 501|on_display
Grumman|S-2|A|133264||Tracker|fixed_wing|monoplane|military|recon||Agneta Airpark; TS-2A trainer conversion; wears AF-405 in USS Intrepid markings; silverhawkauthor prints the truncated 3264 on its ESAM page and the full 133264 on its Intrepid page|TS-2A; S2F; AF-405|on_display
North American|RA-5|C|156621||Vigilante|fixed_wing|monoplane|military|recon||Agneta Airpark; BuNo checks against the RA-5C block 156608-156643; wears 614 in RVAH-5 markings|Vigilante; 614|on_display
North American|T-2|C|156730||Buckeye|fixed_wing|monoplane|military|trainer||Agneta Airpark; BuNo checks against the T-2C block 156693-156733; wears 802|Buckeye|on_display
LTV|A-7|E|160613||Corsair II|fixed_wing|monoplane|military|ground_attack||Agneta Airpark; BuNo checks against the A-7E block 160537-160618; wears 306 in VA-46 Clansmen markings|Corsair II; SLUF; 306|on_display
Douglas|A-4|F|155009||Skyhawk|fixed_wing|monoplane|military|ground_attack||Agneta Airpark; BuNo checks against the A-4F block 154970-155069; wears AF-05 in VFC-12 markings|Scooter; AF-05|on_display
Douglas|F3D|2T|127074||Skyknight|fixed_wing|monoplane|military|fighter||Agneta Airpark; BuNo falls in the F3D-2 block 124595-127086; displayed in USMC VMF(N)-513 Korean War colours|F-10; Skyknight; Whale|on_display
Douglas|C-47|A|43-12061||Skytrain|fixed_wing|monoplane|military|transport||Agneta Airpark; the serial is reported by silverhawkauthor only and does not sit cleanly in a published C-47A block — treat as unverified|Dakota; Gooney Bird|on_display
Supermarine|Scimitar|F1|XD220|||fixed_wing|monoplane|military|fighter||Agneta Airpark; Royal Navy Scimitar; wears 608; one of very few Scimitars outside the UK|608; Scimitar F.1|on_display
Mikoyan-Gurevich|MiG-15||624||Fagot|fixed_wing|monoplane|military|fighter||Agneta Airpark; airframe number 624; formerly reported at the Intrepid before ESAM acquired several ex-Intrepid airframes|Fagot|on_display
Mikoyan-Gurevich|MiG-17|F|605||Fresco|fixed_wing|monoplane|military|fighter||Agneta Airpark; ex-Polish Air Force; airframe number 605|Fresco C; Lim-5|on_display
Mikoyan-Gurevich|MiG-21|MF|2406||Fishbed|fixed_wing|monoplane|military|fighter||Agneta Airpark; ex-Polish Air Force; airframe number 2406|Fishbed J|on_display
Bell|UH-1|M|65-9435||Iroquois|rotary_wing||military|utility||FY65 UH-1C block 65-9416/65-9587 from which UH-1M gunships were converted; wears 513 and the name Proud Mary|Huey; Proud Mary; 513|on_display
Bell|UH-1|||15623|Iroquois|rotary_wing||military|utility||A second Huey reported by silverhawkauthor with the bare number 15623 which is probably the tail-number portion of a FY-prefixed serial — serial not established so left in aliases only|15623; Huey|on_display
Hughes|OH-6|A|68-17343||Cayuse|rotary_wing||military|recon||FY68 OH-6A block 68-17145/68-17360; displayed in USMC markings|Loach; Cayuse|on_display
Folland|Gnat|F1|||Gnat|fixed_wing|monoplane|military|fighter||Serial not established|Gnat FM Mk 1|on_display
Lockheed|10|E|||Electra|fixed_wing|monoplane|civilian|commercial_transport||Fuselage section only|Electra 10E|on_display
Heath|Super Parasol||N598K|||fixed_wing|monoplane|civilian|private||Indoor gallery; c/n 39|c/n 39|on_display
Mooney|M-18|LA|N4089|Mite||fixed_wing|monoplane|civilian|private|1952|Indoor gallery; c/n 128|Mite; c/n 128|on_display
Stits|Skycoupe||N3834|||fixed_wing|monoplane|civilian|private||Indoor gallery|Stitts Skycoupe|on_display
Schweizer|RP-1||N8482U|||fixed_wing|monoplane|civilian|research||Ex-NASA research glider|NASA glider|on_display
Nieuport|||||Scout|fixed_wing|biplane|military|fighter||REPRODUCTION Nieuport scout; indoor gallery|Nieuport Scout|on_display
Huntington|Chum||||Chum|fixed_wing|monoplane|civilian|experimental||Experimental homebuilt; indoor gallery|Huntington Chum|on_display

### Grumman Memorial Park -- Calverton

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Grumman|F-14|A|160902||Tomcat|fixed_wing|monoplane|military|fighter||Mounted outdoors at the entrance to the former Naval Weapons Industrial Reserve Plant Calverton where every F-14 was flight-tested; BuNo checks against the F-14A block 160887-160930; wears 134; the airframe has weathered badly and press coverage has repeatedly called for restoration|Tomcat; 134|on_display
Grumman|A-6|E|164384||Intruder|fixed_wing|monoplane|military|ground_attack||Outdoor display beside the F-14; wears AA-505; BuNo sits at the top of the final A-6E block|Intruder; AA-505|on_display

### Historic Aircraft Restoration Project -- Brooklyn
(Hangar B Floyd Bennett Field; open to the public Tuesday Thursday and Saturday 09:00-16:00 per an
August 2024 report; group tours on 718-338-3799. All airframes are National Park Service property
restored by HARP volunteers under the NPS Volunteers-In-Parks programme and are presented in a
walk-through hangar.)

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Consolidated|PBY|5A|N4582T||Catalina|fixed_wing|monoplane|military|search_rescue||Hangar B; confirmed present in an August 2024 press report|Catalina|on_display
Douglas|C-47|B|44-76457||Skytrain|fixed_wing|monoplane|military|transport||Hangar B; confirmed present in an August 2024 press report|Dakota; Gooney Bird|on_display
Douglas|A-4|B|142829||Skyhawk|fixed_wing|monoplane|military|ground_attack||Hangar B; A4D-2; wears AB-500; confirmed present in an August 2024 press report|A4D-2; AB-500; Scooter|on_display
Grumman|HU-16|E|7216||Albatross|fixed_wing|monoplane|military|search_rescue||Hangar B; US Coast Guard number 7216; confirmed present in an August 2024 press report|Albatross|on_display
Grumman|JRF|5|N644R||Goose|fixed_wing|monoplane|military|utility||Hangar B; confirmed present in an August 2024 press report|Goose; G-21|on_display
Lockheed|SP-2|E|131542||Neptune|fixed_wing|monoplane|military|recon||Hangar B; wears 210; confirmed present in an August 2024 press report as an SP2H/SP-2E|P2V; Neptune; 210|on_display
Sikorsky|HH-3|F|1434||Pelican|rotary_wing||military|search_rescue||Hangar B; US Coast Guard number 1434; confirmed present in an August 2024 press report|Pelican; Jolly Green|on_display
Beechcraft|SNB|5|90536||Expeditor|fixed_wing|monoplane|military|transport||Hangar B; wears 119; confirmed present in an August 2024 press report|Expeditor; C-45; Twin Beech|on_display
Fairchild|PT-26|B|N1321V||Cornell|fixed_wing|monoplane|military|trainer||Hangar B; confirmed present in an August 2024 press report|Cornell II; M-62|on_display
Lockheed|Vega|5C|NR105W||Winnie Mae|fixed_wing|monoplane|civilian|private||FULL-SCALE REPLICA of Wiley Post's Winnie Mae which departed Floyd Bennett Field on his 1933 solo round-the-world flight; the original is in the Smithsonian|Winnie Mae|on_display
Wright|Flyer||||Wright Flyer|fixed_wing|biplane|civilian|experimental||REPLICA 1903 Wright Flyer; confirmed present in an August 2024 press report|1903 Flyer|on_display
Boeing|PT-13||||Kaydet|fixed_wing|biplane|military|trainer||Stearman Kaydet reported present in an August 2024 press report; serial not established|Stearman; Kaydet|on_display
North American|SNJ||||Texan|fixed_wing|monoplane|military|trainer||SNJ/AT-6 trainer reported present in an August 2024 press report; serial not established|AT-6; Texan|on_display
Boeing|C-97||||Stratofreighter|fixed_wing|monoplane|military|transport||A USAF C-97 is reported present in an August 2024 press report; almost certainly a fuselage or cockpit section given the hangar footprint; serial not established — verify|Stratofreighter; KC-97|on_display

### New York Hall of Science Rocket Park -- Queens

manufacturer|model|variant|tail_number|model_name|aircraft_name|aircraft_type|wing_type|military_civilian|role_type|year_built|description|aliases|display_status
Martin|Titan|II||Titan II GLV||missile_rocket||military|launch_vehicle|1961|Erected for the 1964-65 New York World's Fair; stands 110 ft with a Gemini capsule mock-up on top; built for the Air Force in 1961 and never flown; fully restored in 2001 and re-erected 2003|Titan II; Gemini-Titan|on_display
Convair|Atlas|D||Atlas||missile_rocket||military|launch_vehicle|1961|Erected for the 1964-65 New York World's Fair; built for the Air Force in 1961 and never flown; fully restored in 2001 and re-erected 2003; an HMdb marker records the display|Mercury-Atlas; SM-65|on_display
McDonnell|Mercury|Capsule|||Mercury spacecraft|spacecraft||civilian|space||Rocket Park; the museum states this capsule orbited the Earth; visitors may sit inside; identity of the specific spacecraft not established — verify before publishing as a flown article|Mercury capsule|on_display
McDonnell|Gemini|Capsule|||Gemini spacecraft|spacecraft||civilian|space||MOCK-UP Gemini two-man capsule mounted atop the Titan II|Gemini capsule|on_display
North American|X-15||||X-15|fixed_wing|monoplane|military|test||FULL-SCALE MODEL of the X-15 rocket research aircraft; not a flown airframe|X-15 model|on_display
Boeing|Saturn V|S-IC||boattail||missile_rocket||civilian|launch_vehicle||Saturn V boattail/propulsion section displayed in Rocket Park|Saturn V; S-IC|on_display

### Bayport Aerodrome Society
Hangars open to the public every Sunday 10:00-16:00 April through November. The society's museum
hangar holds artifacts; the antique aircraft in the hangars are **member-owned and airworthy** and
the society publishes no inventory. **No airframe rows are offered.** See NOTES.

---

## 3. NOTES

### 3.1 Sources used and their weight
- **Museum's own current pages (rung 1):** oldrhinebeck.org/collections-list/ (all 9 pages scraped
  10 Sep 2026 — gives type, year, original/reproduction and display status for all 85 aircraft; the
  single best primary source in this pass); cradleofaviation.org galleries + virtual-museum pages;
  americanairpowermuseum.com Collections > Flying Aircraft and Static Aircraft; intrepidmuseum.org
  exhibitions and 2024-25 press releases; esam.org (site structure only — ESAM publishes no
  inventory and its map is an image).
- **FAA owner-name registry (rung 2):** the single highest-yield tool again. Working queries and
  their yields — `RHINEBECK` → 50 aircraft registered to RHINEBECK AERODROME MUSEUM (`OLD RHINEBECK`
  and `OLD RHINEBECK AERODROME` both return nothing); `AMERICAN AIRPOWER MUSEUM` → 7 aircraft;
  `CRADLE` / `CRADLE OF AVIATION` → 1 only (a Lancair 320 N3075W, a donated homebuilt, not a gallery
  exhibit); `EMPIRE STATE AEROSCIENCES`, `AEROSCIENCES`, `BAYPORT AERODROME`, `NEW YORK HALL OF
  SCIENCE`, `VANDERBILT MUSEUM`, `HUDSON VALLEY AIR`, `WARWICK VALLEY` → all nil.
  **Mechanical note for the next pass:** the GET form
  `registry.faa.gov/AircraftInquiry/Search/NameResult?Nametxt=<name>` now 302s to
  "Name has unsupported characters" for every input. You must GET
  `/AircraftInquiry/Search/NameInquiry`, scrape `__RequestVerificationToken`, and POST it back to
  `/AircraftInquiry/Search/NameResult` with fields `nametxt` and `sort_option=1`. A working shell
  script is left at /tmp/faa.sh.
- **Joe Baugher production blocks (rung 3):** used to block-check every USAF/USN serial recorded.
  All recorded serials pass except the two flagged below.
- **Aerial Visuals (rung 4):** LocationDossier.php?Serial=3177 (Cradle of Aviation) supplied mapped
  coordinates and the serial/type pairings used to correct aviationmuseum.eu. Their airframe search
  is JavaScript-driven and cannot be scraped server-side.
- **Wikipedia survivor lists (rung 7):** F-4 and F-105 survivor lists used to cross-check Intrepid
  and ESAM.
- **aviationmuseum.eu and silverhawkauthor (LEAD LISTS ONLY, rung 8):** used only to generate
  candidate rows, then re-anchored. Column shifts found and corrected are itemised below.

### 3.2 Corrections made, with evidence
1. **Intrepid C-130J 99-1431 (existing id 25 row) is bogus and must be DELETED.** That airframe was
   written off 25 Jan 2001 and Intrepid has never displayed a C-130J.
2. **aviationmuseum.eu's Cradle of Aviation table is column-shifted by one row** across the middle
   of the alphabet. Confirmed shifts corrected here against the Aerial Visuals dossier:
   51-9480 belongs to the F-84F not the Rearwin Skyranger; 44-89444 belongs to the P-47N not the
   JB-2; 45-59504 belongs to the F-84B not the P-47N; N6461K belongs to the Seabee not the P-84B;
   N349N belongs to the Savoia-Marchetti not the Ryan NYP; N1115 belongs to the Thomas-Morse not the
   Sperry Messenger; 45-15574 belongs to the WACO CG-4A not the Thomas-Morse; N92972 belongs to the
   Commonwealth Skyranger not the Piper Cherokee cockpit; N69097 belongs to the Klemin K-1 not the
   Ace. **Every serial that source supplies for this museum must be treated as unusable on its own.**
3. **Intrepid Grumman Tiger: aviamagazine.com's BuNo 141884 fails the production block check** —
   F11F-1 BuNos run 141728-141868. silverhawkauthor's 141824 falls inside the block and is used.
4. **Intrepid Skyraider: aviamagazine.com prints 109102**; the Douglas XBT2D-1 prototype block is
   09085-09109, so the leading 1 is a typo. Recorded as 09102.
5. **Intrepid Avenger:** aviamagazine.com says TBM-1 BuNo 24803 (a TBM-1C number); the museum and
   Wikipedia both say TBM-3E, and 53842 sits in the TBM-3E block 53050-53949. Recorded 53842 and
   flagged.
6. **Intrepid A-6 is an A-6F not an A-6E.** BuNo 162185 is one of the five A-6F Intruder II
   prototypes 162183-162187; its sister 162184 is at the Cradle of Aviation. Both museums' captions
   and most directories say A-6E for the Intrepid airframe.
7. **Intrepid Douglas F4D-1/F-6A Skyray 134836 is a 2021 arrival**, not a legacy exhibit: barged
   from the New England Air Museum and placed on the flight deck 27 July 2021. Older directories
   omit it; older ones that list "F-6 134836" are right for the wrong reason.
8. **silverhawkauthor's Intrepid page is a historical accumulation, not a current inventory.** It
   lists at least ten airframes that are now at ESAM (F3D-2T 127074, RA-5C 156621, TS-2A 133264,
   MiG-15 624, Scimitar XD220) or that left decades ago (SP-2E 131542 and HU-16E 7216, which are
   in fact at HARP Brooklyn; H-21C; XA3D-1; YA-6A; two F-84Fs; F6F-5; SB2C-3; YF-17; S.E.5a; S-55D;
   CH-34C; OH-13S; AH-1F/G). Only airframes corroborated by Wikipedia's current article or by a
   2021-2025 museum/press source are recorded above.

### 3.3 Source conflicts left open
- **Republic F-84F 51-9480 is claimed by two museums.** Aerial Visuals maps it as an outdoor display
  at the Cradle of Aviation; Wikipedia's American Airpower Museum article lists it at Farmingdale.
  An aircraft is in exactly one place. I have recorded it at the **Cradle** because Aerial Visuals
  has a mapped coordinate fix and AAM's own current Static Aircraft page does not name an F-84F.
  One phone call to AAM on **631-293-6398** would settle this and several other AAM questions.
- **Intrepid Piasecki HUP-2: 128518 (aviamagazine) vs 128519 (silverhawkauthor).** Both fall inside
  the HUP-2 block 128507-128582. Recorded 128519; flagged.
- **Old Rhinebeck Sopwith Pup.** The museum lists a Pup as Active; Wikipedia says Cole Palen's 1967
  Pup went to the Owls Head Transportation Museum in Maine. Either a second airframe exists or the
  Wikipedia claim is stale.
- **Old Rhinebeck Voisin.** The museum calls it Original; the FAA registers N38933 to the museum as
  a Renik-built Voisin, which reads as a modern construction.
- **Cradle Ryan NYP.** The museum's Golden Age gallery page says "Spirit of St. Louis"; its history
  page says it holds a Ryan Brougham sister ship of the Spirit. Aerial Visuals lists neither but
  does list a Savoia-Marchetti S-56B registered N349N. Verify on site which is displayed.

### 3.4 Judgment calls
- **Old Rhinebeck: I recorded all 85 published collection aircraft**, including the airworthy
  airshow fleet. Reasoning: the Aerodrome's admission ticket walks the visitor through the hangars
  where the flying machines live, the museum publishes them as one collection with display statuses,
  and the brief's exclusion is for "airworthy private warbirds merely based at a field" — these are
  museum-owned and museum-exhibited. Aircraft the museum labels **On Loan** (Curtiss Pusher Model A,
  one Fokker Dr.I, Nieuport 17, F.E.8) are recorded as on_display but the direction of the loan is
  not stated by the museum and should be confirmed.
- **American Airpower Museum:** I counted (a) the static jets that cannot fly, (b) the seven aircraft
  currently registered to the museum in the FAA registry, and (c) the airworthy warbirds the museum
  itself publishes on its Flying Aircraft page. I did **not** count warbirds that appear only in
  aviationmuseum.eu's table with third-party registrations (Beech D18S x2, Beech B95, Cessna U-3A,
  Fouga Magister N224PS, Lockheed T-33A N43856, Stinson 108-2 N348C, SNJ-4 N9523C) — those look like
  visiting or privately-based aircraft, not the museum's collection.
- **Bayport Aerodrome Society: recorded as a site with no airframe rows.** The hangars are open to
  the public on Sundays April-November, but every aircraft in them is a member-owned airworthy
  antique and the society publishes no inventory. The site line is worth keeping so a later pass can
  fill it; a phone/email enquiry to info@bayportaerodromesociety.org is the way in.
- **Rocket Park mock-ups.** The Gemini capsule on the Titan and the X-15 are models, and I have said
  so in `description` rather than dropping them, because they are the reason people go. The Mercury
  capsule is described by the museum as having orbited — I have not been able to identify which
  spacecraft it is and have flagged it rather than assert a flown article.
- **ESAM is in Schenectady County, not downstate.** It is in this pass only because the task assigned
  it. Whoever runs the upstate pass should not re-research it.

### 3.5 Deliberately blank fields
- `year_built` is blank on almost every military airframe: a fiscal-year prefix is not a build year
  and I found no sourced construction/delivery dates. It is populated only where the museum states a
  design/build year (Old Rhinebeck publishes a Year for each aircraft) or where a delivery year is
  documented (Concorde G-BOAD 1976; Mooney Mite 1952; Titan II and Atlas 1961).
- `postal_code` is given only where the museum publishes a full street address.
- `wing_type` blank for all rotary_wing, spacecraft, missile_rocket and lighter_than_air rows.
- Serials left blank rather than guessed: Intrepid Kfir true Israeli serial; Cradle F-105D cockpit,
  C-47B cockpit, JB-2, Sperry Aerial Torpedo, G-21 Goose, Ag-Cat, Bleriot, Vin Fiz, Golden Flyer,
  Langley, Lilienthal, Peel, Cassutt, Cessna 172, PA-28; ESAM Folland Gnat, Lockheed 10E, Nieuport
  replica, Huntington Chum, second UH-1; HARP Stearman, SNJ and C-97; most Old Rhinebeck airframes
  not FAA-registered to the museum.

### 3.6 EXCLUDED — do not re-research
- **Lockheed Martin C-130J 99-1431 at the Intrepid** — bogus seed data; delete the existing row.
- **Republic P-47D NX1345B / 44-90447 "Jacky's Revenge" at the American Airpower Museum** — crashed
  into the Hudson River 27 May 2016 killing the pilot. Still listed by Wikipedia and
  aviationmuseum.eu. Not there.
- **Grumman S-2E 151664** — Aerial Visuals records it as having left the Cradle of Aviation;
  aviationmuseum.eu places it at HARP Brooklyn but the August 2024 HARP press inventory does not
  mention it. Location unresolved; recorded at neither.
- **Brunner-Winkle A Bird N787Y c/n 1067** — Aerial Visuals records it as gone from the Cradle.
- **Historic Aircraft Restoration Museum (FAA owner name)** — this is in Creve Coeur Missouri and is
  a different organisation from Brooklyn's Historic Aircraft Restoration Project. Its 19 FAA-
  registered aircraft are NOT in New York. Do not import them.
- **American Airpower Heritage Flying Museum** — the FAA owner-name search on "AMERICAN AIRPOWER"
  returns ~50 aircraft under this name; that is the Commemorative Air Force in Texas, not
  Farmingdale. Only rows reading exactly AMERICAN AIRPOWER MUSEUM / MUSEUM INC are Long Island.
- **Aviation Career & Technical Education High School, Long Island City** — holds training airframes
  but they are instructional equipment behind a school gate, not a public presentation.
- **Vaughn College, East Elmhurst** — aeronautics college; donated its historic aviation mural to the
  Cradle of Aviation in March 2025; no publicly-presented airframe found.
- **Stewart Air National Guard Base, Newburgh** — no gate guard or air park found in any source.
- **Francis S. Gabreski ANGB, Westhampton Beach** — no static display found in any source; if one
  exists it is behind the gate and would be `restricted`.
- **Camp Smith, Cortlandt Manor** — no aircraft display found.
- **Wurtsboro, Stormville, Randall (Middletown) and Warwick airports** — all active general-aviation
  or gliding fields; no preserved display found. The FAA owner-name search on STORMVILLE returns one
  operational Piper PA-22.
- **New Jersey and Connecticut border sites** — out of scope per the task.

### 3.7 Open questions, ranked
1. **Cradle of Aviation, 516-572-4111.** One call closes four things at once: (a) is the F-105B
   57-5783 and the B-25 still on site — Aerial Visuals has had an open query since 2008;
   (b) which Ryan is displayed, the NYP reproduction or the B-1 Brougham; (c) does the F-84F carry
   51-9480; (d) a full current airframe list with serials, since the museum claims ~75 and I can
   only substantiate ~53.
2. **American Airpower Museum, 631-293-6398.** Confirm the F-84F 51-9480 claim, the Waco UPF-7, the
   AT-28D's registration and loan status, and which of the aviationmuseum.eu warbirds are the
   museum's own.
3. **Empire State Aerosciences Museum, 518-377-2191.** ESAM publishes no serials at all. Every serial
   above except the F-105G and the YMC-130H rests on a single lead-list source. Ask for the airpark
   placard list; specifically confirm the C-47A 43-12061, the F-5E BuNo 162307 and the second UH-1.
4. **HARP Brooklyn, 718-338-3799.** Confirm the C-97 (type and whether it is a complete airframe),
   the Stearman and SNJ serials, and whether the S-2E 151664 is there.
5. **Old Rhinebeck Aerodrome, 845-752-3200.** Ask them to reconcile the 50 FAA registrations against
   the 85-item published collection — specifically the third New Standard D-25 N31K, the Nieuport
   83E N680CP, the Gazelle HO-2 N6551, the Ormand Parasol N5719, the Piccard balloon N7132, and
   which Monocoupe is the 90-J.
6. **New York Hall of Science, 718-699-0005.** Identify the Mercury capsule — flown article or
   boilerplate.
7. **Bayport Aerodrome Society, info@bayportaerodromesociety.org.** Ask for the current hangar list
   and which aircraft are society-owned rather than member-owned.

### 3.8 What was NOT reached in this pass
- No systematic county-by-county sweep of American Legion / VFW post displays in the fourteen
  downstate counties. Generic web search returned nothing for Nassau, Suffolk, Westchester,
  Rockland, Putnam, Dutchess, Orange, Sullivan or Ulster, and HMdb could not be queried by aircraft
  type. **The right tool for the next pass is HMdb county result pages**
  (`hmdb.org/results.asp?Search=County&County=<X>+County&State=New+York`) read one county at a time,
  plus satellite/Street View sweeps of post addresses from the American Legion Department of New York
  "Posts by County" PDF at nylegion.net. I judged that too large to complete inside this pass and
  have left it explicitly undone rather than return a thin guess.
- Staten Island (Richmond County) and the Bronx produced no candidate site from any source.
- The Vanderbilt Museum in Centerport was checked and produced no aircraft; the FAA owner-name search
  on VANDERBILT returns only unrelated owners.
