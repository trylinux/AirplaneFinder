"""Seed the database with sample museums, aircraft, zip codes, and a default admin user."""

from app import app
from models import db, User, ApiKey, Museum, Aircraft, AircraftAlias, AircraftMuseum, ZipCode, UserMuseumAssignment, UserCountryAssignment

MUSEUMS = [
    # ── North America ──
    {
        "name": "National Museum of the United States Air Force",
        "city": "Dayton", "state_province": "Ohio", "country": "United States",
        "postal_code": "45433", "region": "North America",
        "address": "1100 Spaatz St, Wright-Patterson AFB, OH 45433",
        "website": "https://www.nationalmuseum.af.mil",
        "latitude": 39.7811, "longitude": -84.1107,
    },
    {
        "name": "Smithsonian National Air and Space Museum",
        "city": "Washington", "state_province": "DC", "country": "United States",
        "postal_code": "20560", "region": "North America",
        "address": "655 Jefferson Dr SW, Washington, DC 20560",
        "website": "https://airandspace.si.edu",
        "latitude": 38.8882, "longitude": -77.0199,
    },
    {
        "name": "Steven F. Udvar-Hazy Center",
        "city": "Chantilly", "state_province": "Virginia", "country": "United States",
        "postal_code": "20151", "region": "North America",
        "address": "14390 Air and Space Museum Pkwy, Chantilly, VA 20151",
        "website": "https://airandspace.si.edu/udvar-hazy-center",
        "latitude": 38.9114, "longitude": -77.4440,
    },
    {
        "name": "Pima Air & Space Museum",
        "city": "Tucson", "state_province": "Arizona", "country": "United States",
        "postal_code": "85756", "region": "North America",
        "address": "6000 E Valencia Rd, Tucson, AZ 85756",
        "website": "https://pimaair.org",
        "latitude": 32.1710, "longitude": -110.8684,
    },
    {
        "name": "Museum of Flight",
        "city": "Seattle", "state_province": "Washington", "country": "United States",
        "postal_code": "98108", "region": "North America",
        "address": "9404 E Marginal Way S, Seattle, WA 98108",
        "website": "https://www.museumofflight.org",
        "latitude": 47.5180, "longitude": -122.2964,
    },
    {
        "name": "Intrepid Sea, Air & Space Museum",
        "city": "New York", "state_province": "New York", "country": "United States",
        "postal_code": "10036", "region": "North America",
        "address": "Pier 86, W 46th St, New York, NY 10036",
        "website": "https://www.intrepidmuseum.org",
        "latitude": 40.7645, "longitude": -73.9997,
    },
    {
        "name": "National Naval Aviation Museum",
        "city": "Pensacola", "state_province": "Florida", "country": "United States",
        "postal_code": "32508", "region": "North America",
        "address": "1750 Radford Blvd, NAS Pensacola, FL 32508",
        "website": "https://www.navalaviationmuseum.org",
        "latitude": 30.3524, "longitude": -87.2920,
    },
    {
        "name": "March Field Air Museum",
        "city": "Riverside", "state_province": "California", "country": "United States",
        "postal_code": "92518", "region": "North America",
        "address": "22550 Van Buren Blvd, Riverside, CA 92518",
        "website": "https://www.marchfield.org",
        "latitude": 33.8803, "longitude": -117.2590,
    },
    {
        "name": "Hill Aerospace Museum",
        "city": "Roy", "state_province": "Utah", "country": "United States",
        "postal_code": "84056", "region": "North America",
        "address": "7961 Wardleigh Rd, Hill AFB, UT 84056",
        "website": "https://www.hill.af.mil/About/Fact-Sheets/Display/Article/397316/hill-aerospace-museum/",
        "latitude": 41.1188, "longitude": -111.9632,
    },
    {
        "name": "Commemorative Air Force Airbase Arizona",
        "city": "Mesa", "state_province": "Arizona", "country": "United States",
        "postal_code": "85215", "region": "North America",
        "address": "2017 N Greenfield Rd, Mesa, AZ 85215",
        "website": "https://www.azcaf.org",
        "latitude": 33.4607, "longitude": -111.7273,
    },
    {
        "name": "EAA Aviation Museum",
        "city": "Oshkosh", "state_province": "Wisconsin", "country": "United States",
        "postal_code": "54902", "region": "North America",
        "address": "3000 Poberezny Rd, Oshkosh, WI 54902",
        "website": "https://www.eaa.org/eaa-museum",
        "latitude": 43.9831, "longitude": -88.5570,
    },
    {
        "name": "Pacific Aviation Museum Pearl Harbor",
        "city": "Honolulu", "state_province": "Hawaii", "country": "United States",
        "postal_code": "96818", "region": "North America",
        "address": "319 Lexington Blvd, Honolulu, HI 96818",
        "website": "https://www.pearlharboraviationmuseum.org",
        "latitude": 21.3547, "longitude": -157.9581,
    },
    {
        "name": "Canada Aviation and Space Museum",
        "city": "Ottawa", "state_province": "Ontario", "country": "Canada",
        "postal_code": "K1A 0M8", "region": "North America",
        "address": "11 Aviation Pkwy, Ottawa, ON K1K 2X5",
        "website": "https://ingeniumcanada.org/aviation",
        "latitude": 45.4576, "longitude": -75.6440,
    },

    # ── Europe ──
    {
        "name": "Royal Air Force Museum London",
        "city": "London", "state_province": "England", "country": "United Kingdom",
        "postal_code": "NW9 5LL", "region": "Europe",
        "address": "Grahame Park Way, London NW9 5LL",
        "website": "https://www.rafmuseum.org.uk",
        "latitude": 51.5953, "longitude": -0.2376,
    },
    {
        "name": "Imperial War Museum Duxford",
        "city": "Duxford", "state_province": "Cambridgeshire", "country": "United Kingdom",
        "postal_code": "CB22 4QR", "region": "Europe",
        "address": "Duxford Airfield, Cambridgeshire CB22 4QR",
        "website": "https://www.iwm.org.uk/visits/iwm-duxford",
        "latitude": 52.0907, "longitude": 0.1319,
    },
    {
        "name": "Deutsches Museum Flugwerft Schleissheim",
        "city": "Oberschleissheim", "state_province": "Bavaria", "country": "Germany",
        "postal_code": "85764", "region": "Europe",
        "address": "Effnerstr. 18, 85764 Oberschleissheim",
        "website": "https://www.deutsches-museum.de/flugwerft",
        "latitude": 48.2394, "longitude": 11.5614,
    },
    {
        "name": "Musee de l'Air et de l'Espace",
        "city": "Le Bourget", "state_province": "Ile-de-France", "country": "France",
        "postal_code": "93350", "region": "Europe",
        "address": "Aeroport de Paris-Le Bourget, 93350 Le Bourget",
        "website": "https://www.museeairespace.fr",
        "latitude": 48.9469, "longitude": 2.4386,
    },

    # ── Asia-Pacific ──
    {
        "name": "JASDF Hamamatsu Air Park",
        "city": "Hamamatsu", "state_province": "Shizuoka", "country": "Japan",
        "postal_code": "432-8001", "region": "Asia-Pacific",
        "website": "https://www.mod.go.jp/asdf/airpark/",
        "latitude": 34.7505, "longitude": 137.7036,
    },

    # ── Oceania ──
    {
        "name": "Australian War Memorial",
        "city": "Canberra", "state_province": "ACT", "country": "Australia",
        "postal_code": "2612", "region": "Oceania",
        "address": "Treloar Cres, Campbell ACT 2612",
        "website": "https://www.awm.gov.au",
        "latitude": -35.2809, "longitude": 149.1486,
    },
]

AIRCRAFT = [
    # model_name  = type's common name (Hercules, Mustang, Cobra)
    # aircraft_name = individual airframe name (Bockscar, Enola Gay, Daisy Duke)

    # C-130 variants (idx 0-3)
    {"manufacturer": "Lockheed", "model": "C-130", "variant": "A", "tail_number": "57-0457", "model_name": "Hercules", "aircraft_name": None, "year_built": 1957, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "Early model Hercules tactical transport."},
    {"manufacturer": "Lockheed", "model": "C-130", "variant": "E", "tail_number": "62-1787", "model_name": "Hercules", "aircraft_name": None, "year_built": 1962, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "Extended range Hercules with upgraded engines."},
    {"manufacturer": "Lockheed Martin", "model": "C-130", "variant": "H", "tail_number": "74-1686", "model_name": "Hercules", "aircraft_name": None, "year_built": 1974, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "Most widely produced Hercules variant."},
    {"manufacturer": "Lockheed Martin", "model": "C-130", "variant": "J", "tail_number": "99-1431", "model_name": "Super Hercules", "aircraft_name": None, "year_built": 1999, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "Latest Hercules variant with glass cockpit and Rolls-Royce AE 2100D3 engines."},

    # Bombers (idx 4-9)
    {"manufacturer": "Boeing", "model": "B-17", "variant": "G", "tail_number": "44-83624", "model_name": "Flying Fortress", "aircraft_name": "Shoo Shoo Baby", "year_built": 1944, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "WWII heavy bomber, restored to original condition."},
    {"manufacturer": "Boeing", "model": "B-29", "variant": None, "tail_number": "44-27297", "model_name": "Superfortress", "aircraft_name": "Bockscar", "year_built": 1944, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "Dropped the Fat Man atomic bomb on Nagasaki on August 9, 1945."},
    {"manufacturer": "Boeing", "model": "B-29", "variant": None, "tail_number": "44-86292", "model_name": "Superfortress", "aircraft_name": "Enola Gay", "year_built": 1944, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "Dropped the first atomic bomb on Hiroshima on August 6, 1945."},
    {"manufacturer": "Convair", "model": "B-36", "variant": "J", "tail_number": "52-2220", "model_name": "Peacemaker", "aircraft_name": None, "year_built": 1952, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "Largest mass-produced piston-engined aircraft ever built."},
    {"manufacturer": "Boeing", "model": "B-52", "variant": "D", "tail_number": "56-0612", "model_name": "Stratofortress", "aircraft_name": None, "year_built": 1956, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "Long-range strategic bomber used from the 1950s to present."},
    {"manufacturer": "Northrop Grumman", "model": "B-2", "variant": "A", "tail_number": "82-1066", "model_name": "Spirit", "aircraft_name": "Spirit of Kitty Hawk", "year_built": 1993, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "Stealth strategic bomber with flying-wing design."},

    # Fighters (idx 10-18)
    {"manufacturer": "North American", "model": "P-51", "variant": "D", "tail_number": "44-74936", "model_name": "Mustang", "aircraft_name": None, "year_built": 1944, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Iconic WWII fighter that helped win air superiority over Europe."},
    {"manufacturer": "Lockheed", "model": "P-38", "variant": "L", "tail_number": "44-53236", "model_name": "Lightning", "aircraft_name": None, "year_built": 1944, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Distinctive twin-boom WWII fighter."},
    {"manufacturer": "Grumman", "model": "F-14", "variant": "A", "tail_number": "160694", "model_name": "Tomcat", "aircraft_name": None, "year_built": 1976, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Variable-sweep wing fleet defense fighter."},
    {"manufacturer": "McDonnell Douglas", "model": "F-15", "variant": "A", "tail_number": "76-0008", "model_name": "Eagle", "aircraft_name": None, "year_built": 1976, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Air superiority fighter with unmatched combat record."},
    {"manufacturer": "General Dynamics", "model": "F-16", "variant": "A", "tail_number": "75-0745", "model_name": "Fighting Falcon", "aircraft_name": None, "year_built": 1978, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "First production Block 1 Fighting Falcon."},
    {"manufacturer": "Lockheed Martin", "model": "F-16", "variant": "C", "tail_number": "84-1301", "model_name": "Fighting Falcon", "aircraft_name": None, "year_built": 1984, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Block 25 F-16C with improved radar."},
    {"manufacturer": "McDonnell Douglas", "model": "F/A-18", "variant": "A", "tail_number": "161749", "model_name": "Hornet", "aircraft_name": None, "year_built": 1983, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Multi-role carrier-based strike fighter."},
    {"manufacturer": "Lockheed Martin", "model": "F-22", "variant": "A", "tail_number": "91-4003", "model_name": "Raptor", "aircraft_name": None, "year_built": 2003, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Fifth-generation stealth air superiority fighter."},
    {"manufacturer": "Lockheed", "model": "F-117", "variant": "A", "tail_number": "79-10781", "model_name": "Nighthawk", "aircraft_name": None, "year_built": 1981, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "ground_attack", "description": "First operational stealth attack aircraft."},

    # Reconnaissance / Special (idx 19-21)
    {"manufacturer": "Lockheed", "model": "SR-71", "variant": "A", "tail_number": "61-7972", "model_name": "Blackbird", "aircraft_name": None, "year_built": 1966, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "recon", "description": "World's fastest air-breathing manned aircraft, cruising above Mach 3."},
    {"manufacturer": "Lockheed", "model": "SR-71", "variant": "A", "tail_number": "61-7976", "model_name": "Blackbird", "aircraft_name": None, "year_built": 1966, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "recon", "description": "SR-71 that set the transcontinental speed record."},
    {"manufacturer": "Lockheed", "model": "U-2", "variant": "C", "tail_number": "56-6680", "model_name": "Dragon Lady", "aircraft_name": None, "year_built": 1956, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "recon", "description": "High-altitude reconnaissance aircraft."},

    # Transports / Cargo (idx 22-24)
    {"manufacturer": "Douglas", "model": "C-47", "variant": "A", "tail_number": "43-15073", "model_name": "Skytrain", "aircraft_name": None, "year_built": 1943, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "Military version of DC-3, workhorse of WWII."},
    {"manufacturer": "Boeing", "model": "C-17", "variant": "A", "tail_number": "87-0025", "model_name": "Globemaster III", "aircraft_name": None, "year_built": 1993, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "Strategic and tactical airlifter."},
    {"manufacturer": "Lockheed", "model": "C-5", "variant": "A", "tail_number": "69-0014", "model_name": "Galaxy", "aircraft_name": None, "year_built": 1969, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "transport", "description": "One of the largest military transport aircraft in the world."},

    # Helicopters (idx 25-26)
    {"manufacturer": "Bell", "model": "UH-1", "variant": "H", "tail_number": "66-16579", "model_name": "Huey", "aircraft_name": None, "year_built": 1966, "aircraft_type": "rotary_wing", "wing_type": None, "military_civilian": "military", "role_type": "transport", "description": "Iconic Vietnam-era helicopter."},
    {"manufacturer": "Sikorsky", "model": "UH-60", "variant": "A", "tail_number": "79-23298", "model_name": "Black Hawk", "aircraft_name": None, "year_built": 1979, "aircraft_type": "rotary_wing", "wing_type": None, "military_civilian": "military", "role_type": "transport", "description": "Medium-lift utility helicopter."},

    # Early Aviation (idx 27-28)
    {"manufacturer": "Wright Brothers", "model": "Wright Flyer", "variant": None, "tail_number": None, "model_name": "Flyer", "aircraft_name": None, "year_built": 1903, "aircraft_type": "fixed_wing", "wing_type": "biplane", "military_civilian": "civilian", "role_type": "experimental", "description": "The first successful heavier-than-air powered aircraft."},
    {"manufacturer": "Curtiss", "model": "JN-4", "variant": "D", "tail_number": None, "model_name": "Jenny", "aircraft_name": None, "year_built": 1917, "aircraft_type": "fixed_wing", "wing_type": "biplane", "military_civilian": "military", "role_type": "transport", "description": "Primary trainer of WWI, later a famous barnstorming aircraft."},

    # International aircraft (idx 29-34)
    {"manufacturer": "Avro", "model": "Lancaster", "variant": "B.X", "tail_number": "KB726", "model_name": "Lancaster", "aircraft_name": None, "year_built": 1945, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "WWII heavy bomber used by the RAF and RCAF."},
    {"manufacturer": "Supermarine", "model": "Spitfire", "variant": "Mk.IX", "tail_number": "MK356", "model_name": "Spitfire", "aircraft_name": None, "year_built": 1944, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Iconic British WWII fighter."},
    {"manufacturer": "Mitsubishi", "model": "A6M", "variant": "Zero", "tail_number": None, "model_name": "Zero", "aircraft_name": None, "year_built": 1940, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Imperial Japanese Navy fighter, dominant in the early Pacific War."},
    {"manufacturer": "Messerschmitt", "model": "Bf 109", "variant": "G", "tail_number": None, "model_name": None, "aircraft_name": None, "year_built": 1943, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "fighter", "description": "Most-produced fighter aircraft of WWII."},
    {"manufacturer": "de Havilland", "model": "Mosquito", "variant": "B.35", "tail_number": None, "model_name": "Mosquito", "aircraft_name": "Wooden Wonder", "year_built": 1945, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "military", "role_type": "bomber", "description": "British multi-role combat aircraft built primarily of wood."},
    {"manufacturer": "Concorde", "model": "Concorde", "variant": None, "tail_number": "G-BOAA", "model_name": "Concorde", "aircraft_name": None, "year_built": 1974, "aircraft_type": "fixed_wing", "wing_type": "monoplane", "military_civilian": "civilian", "role_type": "commercial_transport", "description": "Supersonic passenger airliner."},
]

# Museum-aircraft associations (museum_index, aircraft_index, status)
LINKS = [
    # National Museum USAF (0)
    (0, 5, "on_display"),      # Bockscar
    (0, 7, "on_display"),      # B-36J Peacemaker
    (0, 2, "on_display"),      # C-130H
    (0, 10, "on_display"),     # P-51D
    (0, 13, "on_display"),     # F-15A
    (0, 18, "on_display"),     # F-117A
    (0, 8, "on_display"),      # B-52D
    (0, 14, "on_display"),     # F-16A
    (0, 22, "on_display"),     # C-47A
    (0, 17, "on_display"),     # F-22A
    (0, 21, "on_display"),     # U-2C
    (0, 0, "on_display"),      # C-130A
    (0, 25, "on_display"),     # UH-1H

    # Smithsonian NASM (1)
    (1, 27, "on_display"),     # Wright Flyer
    (1, 28, "on_display"),     # JN-4D Jenny

    # Udvar-Hazy (2)
    (2, 6, "on_display"),      # Enola Gay
    (2, 19, "on_display"),     # SR-71A 61-7972
    (2, 12, "on_display"),     # F-14A
    (2, 23, "on_display"),     # C-5A
    (2, 9, "on_display"),      # B-2A
    (2, 34, "on_display"),     # Concorde

    # Pima (3)
    (3, 1, "on_display"),      # C-130E
    (3, 8, "on_display"),      # B-52D
    (3, 11, "on_display"),     # P-38L
    (3, 16, "on_display"),     # F/A-18A
    (3, 15, "on_display"),     # F-16C

    # Museum of Flight Seattle (4)
    (4, 20, "on_display"),     # SR-71A 61-7976
    (4, 4, "on_display"),      # B-17G
    (4, 12, "on_display"),     # F-14A
    (4, 16, "on_display"),     # F/A-18A
    (4, 34, "on_display"),     # Concorde

    # Intrepid NYC (5)
    (5, 3, "on_display"),      # C-130J
    (5, 12, "on_display"),     # F-14A
    (5, 14, "on_display"),     # F-16A

    # National Naval Aviation Museum (6)
    (6, 12, "on_display"),     # F-14A
    (6, 16, "on_display"),     # F/A-18A
    (6, 25, "on_display"),     # UH-1H

    # March Field (7)
    (7, 8, "on_display"),      # B-52D
    (7, 2, "on_display"),      # C-130H
    (7, 19, "on_display"),     # SR-71A

    # Hill Aerospace (8)
    (8, 14, "on_display"),     # F-16A
    (8, 13, "on_display"),     # F-15A
    (8, 2, "on_display"),      # C-130H
    (8, 25, "on_display"),     # UH-1H

    # CAF Mesa (9)
    (9, 10, "on_display"),     # P-51D
    (9, 4, "on_display"),      # B-17G
    (9, 22, "on_display"),     # C-47A

    # EAA Oshkosh (10)
    (10, 27, "on_display"),    # Wright Flyer (replica)
    (10, 10, "on_display"),    # P-51D
    (10, 28, "on_display"),    # JN-4D

    # Pacific Aviation Museum (11)
    (11, 22, "on_display"),    # C-47A
    (11, 25, "on_display"),    # UH-1H
    (11, 31, "on_display"),    # A6M Zero

    # Canada Aviation Museum (12)
    (12, 29, "on_display"),    # Lancaster
    (12, 33, "on_display"),    # Mosquito

    # RAF Museum London (13)
    (13, 30, "on_display"),    # Spitfire
    (13, 32, "on_display"),    # Bf 109
    (13, 33, "on_display"),    # Mosquito

    # IWM Duxford (14)
    (14, 30, "on_display"),    # Spitfire
    (14, 10, "on_display"),    # P-51D
    (14, 4, "on_display"),     # B-17G
    (14, 34, "on_display"),    # Concorde

    # Deutsches Museum (15)
    (15, 32, "on_display"),    # Bf 109

    # Musee de l'Air Paris (16)
    (16, 34, "on_display"),    # Concorde
    (16, 30, "on_display"),    # Spitfire

    # JASDF Hamamatsu (17)
    (17, 31, "on_display"),    # A6M Zero

    # Australian War Memorial (18)
    (18, 31, "on_display"),    # A6M Zero
]

# Aircraft aliases: (aircraft_index, [aliases])
# These allow finding aircraft by common alternate names or no-hyphen variants
ALIASES = [
    (0, ["C130A", "C130", "Hercules"]),
    (1, ["C130E", "C130", "Hercules"]),
    (2, ["C130H", "C130", "Hercules"]),
    (3, ["C130J", "C130", "Hercules", "Super Hercules", "Super Herc"]),
    (4, ["B17G", "B17", "Flying Fortress"]),
    (5, ["B29", "Superfortress", "Super Fortress"]),
    (6, ["B29", "Superfortress", "Super Fortress"]),
    (7, ["B36J", "B36", "Peacemaker"]),
    (8, ["B52D", "B52", "Stratofortress", "BUFF"]),
    (9, ["B2A", "B2", "Stealth Bomber", "Spirit"]),
    (10, ["P51D", "P51", "Mustang"]),
    (11, ["P38L", "P38", "Lightning"]),
    (12, ["F14A", "F14", "Tomcat"]),
    (13, ["F15A", "F15", "Eagle"]),
    (14, ["F16A", "F16", "Falcon", "Viper", "Fighting Falcon"]),
    (15, ["F16C", "F16", "Falcon", "Viper", "Fighting Falcon"]),
    (16, ["FA18A", "FA18", "F18", "Hornet"]),
    (17, ["F22A", "F22", "Raptor"]),
    (18, ["F117A", "F117", "Nighthawk", "Stealth Fighter"]),
    (19, ["SR71A", "SR71", "Blackbird", "Habu"]),
    (20, ["SR71A", "SR71", "Blackbird", "Habu"]),
    (21, ["U2C", "U2", "Dragon Lady"]),
    (22, ["C47A", "C47", "Skytrain", "Dakota", "DC3", "DC-3", "Gooney Bird"]),
    (23, ["C17A", "C17", "Globemaster"]),
    (24, ["C5A", "C5", "Galaxy"]),
    (25, ["UH1H", "UH1", "Huey", "Iroquois"]),
    (26, ["UH60A", "UH60", "Black Hawk", "Blackhawk"]),
    (27, ["Wright Flyer", "Flyer", "Kitty Hawk"]),
    (28, ["JN4D", "JN4", "Jenny"]),
    (29, ["Lancaster", "Lanc", "Avro Lancaster"]),
    (30, ["Spitfire", "Spit", "Supermarine Spitfire"]),
    (31, ["A6M", "Zero", "Zeke", "Mitsubishi Zero"]),
    (32, ["Bf109", "Bf109G", "Me109", "Me-109", "Messerschmitt 109"]),
    (33, ["Mosquito", "Mossie", "de Havilland Mosquito"]),
    (34, ["Concorde", "SST"]),
]

# Geocoding cache seed — just the museum cities so proximity search
# works out-of-the-box even without pgeocode/geopy installed.
# All other lookups are resolved on-the-fly by geocoder.py and cached
# in this same table automatically.
ZIP_CODES = [
    # US museum cities
    ("20151", "Chantilly", "Virginia", "United States", 38.8943, -77.4311),
    ("45433", "Dayton", "Ohio", "United States", 39.7589, -84.1916),
    ("32501", "Pensacola", "Florida", "United States", 30.4213, -87.2169),
    ("85215", "Mesa", "Arizona", "United States", 33.4607, -111.7273),
    ("96818", "Honolulu", "Hawaii", "United States", 21.3547, -157.9581),
    ("84056", "Roy", "Utah", "United States", 41.1616, -112.0263),
    ("54901", "Oshkosh", "Wisconsin", "United States", 44.0247, -88.5426),
    ("85756", "Tucson", "Arizona", "United States", 32.1715, -110.8673),
    ("92518", "Riverside", "California", "United States", 33.9806, -117.3755),
    ("98101", "Seattle", "Washington", "United States", 47.6062, -122.3321),
    ("97201", "Portland", "Oregon", "United States", 45.5051, -122.6750),
    ("80201", "Denver", "Colorado", "United States", 39.7392, -104.9903),
    # International museum cities
    ("K1A0M8", "Ottawa", "Ontario", "Canada", 45.4215, -75.6972),
    ("CB224QR", "Duxford", "Cambridgeshire", "United Kingdom", 52.0907, 0.1319),
    ("SW1A1AA", "London", "England", "United Kingdom", 51.5014, -0.1419),
    ("75001", "Paris", "Ile-de-France", "France", 48.8606, 2.3376),
    ("80331", "Munich", "Bavaria", "Germany", 48.1351, 11.5820),
    ("100-0001", "Tokyo", "Tokyo", "Japan", 35.6762, 139.6503),
    ("2600", "Canberra", "ACT", "Australia", -35.2809, 149.1300),
    ("2000", "Sydney", "NSW", "Australia", -33.8688, 151.2093),
]


DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "admin"  # Change this in production!


def seed():
    with app.app_context():
        db.create_all()

        # Clear existing data (order matters for FK constraints)
        AircraftMuseum.query.delete()
        AircraftAlias.query.delete()
        Aircraft.query.delete()
        Museum.query.delete()
        ZipCode.query.delete()
        ApiKey.query.delete()
        UserMuseumAssignment.query.delete()
        UserCountryAssignment.query.delete()
        User.query.delete()
        db.session.commit()

        # ── Create default admin user ──
        admin = User(username=DEFAULT_ADMIN_USERNAME, email="admin@example.com", role="admin")
        admin.set_password(DEFAULT_ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.flush()

        # Generate a default admin API key so scripts can use it right away
        api_key_obj, raw_key = ApiKey.generate(admin.id, label="seed-admin-key", permissions="admin")
        db.session.add(api_key_obj)
        db.session.flush()

        # ── Create sample users with different roles ──
        # Manager: assigned to US museums
        mgr_us = User(username="manager_us", email="manager_us@example.com", role="manager")
        mgr_us.set_password("manager123")
        db.session.add(mgr_us)
        db.session.flush()
        db.session.add(UserCountryAssignment(user_id=mgr_us.id, country="United States"))
        mgr_us_key, mgr_us_raw = ApiKey.generate(mgr_us.id, label="auto", permissions="readwrite")
        db.session.add(mgr_us_key)

        # Manager: assigned to UK museums
        mgr_uk = User(username="manager_uk", email="manager_uk@example.com", role="manager")
        mgr_uk.set_password("manager123")
        db.session.add(mgr_uk)
        db.session.flush()
        db.session.add(UserCountryAssignment(user_id=mgr_uk.id, country="United Kingdom"))
        mgr_uk_key, mgr_uk_raw = ApiKey.generate(mgr_uk.id, label="auto", permissions="readwrite")
        db.session.add(mgr_uk_key)

        # Viewer: read-only access
        viewer = User(username="viewer", email="viewer@example.com", role="viewer")
        viewer.set_password("viewer123")
        db.session.add(viewer)
        db.session.flush()
        viewer_key, viewer_raw = ApiKey.generate(viewer.id, label="auto", permissions="read")
        db.session.add(viewer_key)

        # ── Insert museums ──
        museum_objs = []
        for m in MUSEUMS:
            obj = Museum(**m)
            db.session.add(obj)
            museum_objs.append(obj)
        db.session.flush()

        # ── Assign US manager to first 3 US museums specifically ──
        for i in range(min(3, len(museum_objs))):
            if museum_objs[i].country == "United States":
                db.session.add(UserMuseumAssignment(user_id=mgr_us.id, museum_id=museum_objs[i].id))
        db.session.flush()

        # ── Insert aircraft ──
        aircraft_objs = []
        for a in AIRCRAFT:
            obj = Aircraft(**a)
            db.session.add(obj)
            aircraft_objs.append(obj)
        db.session.flush()

        # ── Insert aircraft aliases ──
        alias_count = 0
        for aircraft_idx, alias_list in ALIASES:
            for alias_str in alias_list:
                obj = AircraftAlias(aircraft_id=aircraft_objs[aircraft_idx].id, alias=alias_str)
                db.session.add(obj)
                alias_count += 1
        db.session.flush()

        # ── Insert exhibit links ──
        for museum_idx, aircraft_idx, status in LINKS:
            link = AircraftMuseum(
                museum_id=museum_objs[museum_idx].id,
                aircraft_id=aircraft_objs[aircraft_idx].id,
                display_status=status,
            )
            db.session.add(link)

        # ── Insert geocoding entries ──
        for zc in ZIP_CODES:
            obj = ZipCode(
                zip_code=zc[0], city=zc[1], state=zc[2],
                country=zc[3], latitude=zc[4], longitude=zc[5],
            )
            db.session.add(obj)

        db.session.commit()

        # Count stats
        countries = set(m["country"] for m in MUSEUMS)

        print("=" * 60)
        print("  Database seeded successfully!")
        print("=" * 60)
        print(f"  Museums:   {len(museum_objs)} ({len(countries)} countries)")
        print(f"  Aircraft:  {len(aircraft_objs)}")
        print(f"  Aliases:   {alias_count}")
        print(f"  Exhibits:  {len(LINKS)}")
        print(f"  Geocoding: {len(ZIP_CODES)} cache entries (museum cities)")
        print(f"  Users:     4 (1 admin, 2 managers, 1 viewer)")
        print()
        print("  Default admin login:")
        print(f"    Username: {DEFAULT_ADMIN_USERNAME}")
        print(f"    Password: {DEFAULT_ADMIN_PASSWORD}")
        print()
        print("  Sample users:")
        print("    manager_us / manager123  (manager, US museums)")
        print("    manager_uk / manager123  (manager, UK museums)")
        print("    viewer     / viewer123   (viewer, read-only)")
        print()
        print("  Default admin API key (save this!):")
        print(f"    {raw_key}")
        print()
        print("  Change all passwords after first login!")
        print("=" * 60)


if __name__ == "__main__":
    seed()
