#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p data/new_york

python3 scripts/build_from_research.py --in data/new_york/raw/intrepid_topup.txt \
  --museum "Intrepid Sea, Air & Space Museum" \
  --out data/new_york/intrepid_topup_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/empire_state_aerosciences_topup.txt \
  --museum "Empire State Aerosciences Museum" \
  --out data/new_york/empire_state_aerosciences_topup_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/cradle_of_aviation_museum.txt \
  --museum "Cradle of Aviation Museum" \
  --out data/new_york/cradle_of_aviation_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_airpower_museum.txt \
  --museum "American Airpower Museum" \
  --out data/new_york/american_airpower_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/old_rhinebeck_aerodrome.txt \
  --museum "Old Rhinebeck Aerodrome" \
  --out data/new_york/old_rhinebeck_aerodrome_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/grumman_memorial_park_calverton.txt \
  --museum "Grumman Memorial Park -- Calverton" \
  --out data/new_york/grumman_memorial_park_calverton_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/historic_aircraft_restoration_project_brooklyn.txt \
  --museum "Historic Aircraft Restoration Project -- Brooklyn" \
  --out data/new_york/historic_aircraft_restoration_project_brooklyn_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/new_york_hall_of_science_rocket_park.txt \
  --museum "New York Hall of Science Rocket Park -- Queens" \
  --out data/new_york/new_york_hall_of_science_rocket_park_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/glenn_h_curtiss_museum.txt \
  --museum "Glenn H. Curtiss Museum" \
  --out data/new_york/glenn_h_curtiss_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/national_warplane_museum.txt \
  --museum "National Warplane Museum" \
  --out data/new_york/national_warplane_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/national_soaring_museum.txt \
  --museum "National Soaring Museum" \
  --out data/new_york/national_soaring_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/wings_of_eagles_discovery_center.txt \
  --museum "Wings of Eagles Discovery Center" \
  --out data/new_york/wings_of_eagles_discovery_center_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/niagara_aerospace_museum.txt \
  --museum "Niagara Aerospace Museum" \
  --out data/new_york/niagara_aerospace_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/buffalo_and_erie_county_naval_military_park.txt \
  --museum "Buffalo and Erie County Naval & Military Park" \
  --out data/new_york/buffalo_and_erie_county_naval_military_park_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/greater_rochester_international_airport.txt \
  --museum "Frederick Douglass Greater Rochester International Airport" \
  --out data/new_york/greater_rochester_international_airport_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/history_center_in_tompkins_county.txt \
  --museum "The History Center in Tompkins County" \
  --out data/new_york/history_center_in_tompkins_county_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/dart_airport_aviation_museum.txt \
  --museum "Dart Airport Aviation Museum" \
  --out data/new_york/dart_airport_aviation_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/plattsburgh_air_force_base_museum.txt \
  --museum "Plattsburgh Air Force Base Museum" \
  --out data/new_york/plattsburgh_air_force_base_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/griffiss_b52_memorial_rome.txt \
  --museum "Griffiss Air Park B-52 Memorial -- Rome" \
  --out data/new_york/griffiss_b52_memorial_rome_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/sampson_wwii_navy_veterans_memorial_museum.txt \
  --museum "Sampson World War II Navy Veterans Memorial Museum -- Romulus" \
  --out data/new_york/sampson_wwii_navy_veterans_memorial_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/oriskany_museum_trinkaus_park.txt \
  --museum "The Oriskany Museum at Trinkaus Park -- Oriskany" \
  --out data/new_york/oriskany_museum_trinkaus_park_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/moriarty_memorial_air_park_niagara_falls_ars.txt \
  --museum "Col. John Moriarty Memorial Air Park -- Niagara Falls Air Reserve Station" \
  --out data/new_york/moriarty_memorial_air_park_niagara_falls_ars_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/hancock_field_ang_base_air_park.txt \
  --museum "Hancock Field Air National Guard Base Air Park" \
  --out data/new_york/hancock_field_ang_base_air_park_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/stratton_air_national_guard_base.txt \
  --museum "Stratton Air National Guard Base" \
  --out data/new_york/stratton_air_national_guard_base_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/ny_national_guard_joint_force_hq_latham.txt \
  --museum "New York National Guard Joint Force Headquarters -- Latham" \
  --out data/new_york/ny_national_guard_joint_force_hq_latham_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/stewart_air_national_guard_base.txt \
  --museum "Stewart Air National Guard Base" \
  --out data/new_york/stewart_air_national_guard_base_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/francis_s_gabreski_air_national_guard_base.txt \
  --museum "Francis S. Gabreski Air National Guard Base" \
  --out data/new_york/francis_s_gabreski_air_national_guard_base_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/eastern_air_defense_sector_rome.txt \
  --museum "Eastern Air Defense Sector -- Rome" \
  --out data/new_york/eastern_air_defense_sector_rome_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_374_arcade.txt \
  --museum "VFW Post 374 -- Arcade" \
  --out data/new_york/vfw_post_374_arcade_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_1470_bath.txt \
  --museum "VFW Post 1470 -- Bath" \
  --out data/new_york/vfw_post_1470_bath_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_939_moira.txt \
  --museum "American Legion Post 939 -- Moira" \
  --out data/new_york/american_legion_post_939_moira_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/walter_m_kenney_park_town_of_tonawanda.txt \
  --museum "Walter M. Kenney Park -- Town of Tonawanda" \
  --out data/new_york/walter_m_kenney_park_town_of_tonawanda_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_1279_campbell.txt \
  --museum "American Legion Post 1279 -- Campbell" \
  --out data/new_york/american_legion_post_1279_campbell_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_34_shortsville.txt \
  --museum "American Legion Post 34 -- Shortsville" \
  --out data/new_york/american_legion_post_34_shortsville_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/putnam_county_veterans_memorial_park_carmel.txt \
  --museum "Putnam County Veterans Memorial Park -- Carmel" \
  --out data/new_york/putnam_county_veterans_memorial_park_carmel_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_2721_cuba.txt \
  --museum "VFW Post 2721 -- Cuba" \
  --out data/new_york/vfw_post_2721_cuba_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_894_armed_forces_tribute_deruyter.txt \
  --museum "American Legion Post 894 Armed Forces Tribute -- DeRuyter" \
  --out data/new_york/american_legion_post_894_armed_forces_tribute_deruyter_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_362_east_aurora.txt \
  --museum "American Legion Post 362 -- East Aurora" \
  --out data/new_york/american_legion_post_362_east_aurora_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_880_eden.txt \
  --museum "American Legion Post 880 -- Eden" \
  --out data/new_york/american_legion_post_880_eden_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_9487_franklinville.txt \
  --museum "VFW Post 9487 -- Franklinville" \
  --out data/new_york/vfw_post_9487_franklinville_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_409_gowanda.txt \
  --museum "American Legion Post 409 -- Gowanda" \
  --out data/new_york/american_legion_post_409_gowanda_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_1419_hamburg.txt \
  --museum "VFW Post 1419 -- Hamburg" \
  --out data/new_york/vfw_post_1419_hamburg_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/alexander_corners_veterans_and_pearl_harbor_memorial_henderson.txt \
  --museum "Alexander Corners Veterans and Pearl Harbor Memorial -- Henderson" \
  --out data/new_york/alexander_corners_veterans_and_pearl_harbor_memorial_henderson_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_1434_hinsdale.txt \
  --museum "American Legion Post 1434 -- Hinsdale" \
  --out data/new_york/american_legion_post_1434_hinsdale_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/fulton_county_airport_johnstown.txt \
  --museum "Fulton County Airport -- Johnstown" \
  --out data/new_york/fulton_county_airport_johnstown_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/marine_corps_league_detachment_754_farney_hall_lowville.txt \
  --museum "Marine Corps League Detachment 754 Farney Hall -- Lowville" \
  --out data/new_york/marine_corps_league_detachment_754_farney_hall_lowville_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_5092_lyons.txt \
  --museum "VFW Post 5092 -- Lyons" \
  --out data/new_york/vfw_post_5092_lyons_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_79_massena.txt \
  --museum "American Legion Post 79 -- Massena" \
  --out data/new_york/american_legion_post_79_massena_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/amvets_post_4_massena_center.txt \
  --museum "AMVETS Post 4 -- Massena Center" \
  --out data/new_york/amvets_post_4_massena_center_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_369_mexico.txt \
  --museum "VFW Post 369 -- Mexico" \
  --out data/new_york/vfw_post_369_mexico_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/crane_park_monroe.txt \
  --museum "Crane Park -- Monroe" \
  --out data/new_york/crane_park_monroe_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/77_water_street_rooftop_new_york.txt \
  --museum "77 Water Street Rooftop -- New York" \
  --out data/new_york/77_water_street_rooftop_new_york_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/museum_of_modern_art_new_york.txt \
  --museum "Museum of Modern Art -- New York" \
  --out data/new_york/museum_of_modern_art_new_york_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/town_of_wheatfield_highway_department_wheatfield.txt \
  --museum "Town of Wheatfield Highway Department -- Wheatfield" \
  --out data/new_york/town_of_wheatfield_highway_department_wheatfield_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_601_parish.txt \
  --museum "American Legion Post 601 -- Parish" \
  --out data/new_york/american_legion_post_601_parish_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_8495_freedom_hill_memorial_perinton.txt \
  --museum "American Legion Post 8495 Freedom Hill Memorial -- Perinton" \
  --out data/new_york/american_legion_post_8495_freedom_hill_memorial_perinton_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_1757_sackets_harbor.txt \
  --museum "American Legion Post 1757 -- Sackets Harbor" \
  --out data/new_york/american_legion_post_1757_sackets_harbor_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_8259_stittville.txt \
  --museum "VFW Post 8259 -- Stittville" \
  --out data/new_york/vfw_post_8259_stittville_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_915_central_square.txt \
  --museum "American Legion Post 915 -- Central Square" \
  --out data/new_york/american_legion_post_915_central_square_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/veterans_park_remembering_vietnam_monument_city_of_tonawanda.txt \
  --museum "Veterans Park Remembering Vietnam Monument -- City of Tonawanda" \
  --out data/new_york/veterans_park_remembering_vietnam_monument_city_of_tonawanda_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/american_legion_post_1376_new_hartford.txt \
  --museum "American Legion Post 1376 -- New Hartford" \
  --out data/new_york/american_legion_post_1376_new_hartford_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_6433_waterloo.txt \
  --museum "VFW Post 6433 -- Waterloo" \
  --out data/new_york/vfw_post_6433_waterloo_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/westchester_county_airport_white_plains.txt \
  --museum "Westchester County Airport -- White Plains" \
  --out data/new_york/westchester_county_airport_white_plains_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/william_krieger_memorial_park_woodridge.txt \
  --museum "William Krieger Memorial Park -- Woodridge" \
  --out data/new_york/william_krieger_memorial_park_woodridge_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/twa_hotel_queens.txt \
  --museum "TWA Hotel -- Queens" \
  --out data/new_york/twa_hotel_queens_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vaughn_college_of_aeronautics_and_technology_east_elmhurst.txt \
  --museum "Vaughn College of Aeronautics and Technology -- East Elmhurst" \
  --out data/new_york/vaughn_college_of_aeronautics_and_technology_east_elmhurst_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/aviation_high_school_long_island_city.txt \
  --museum "Aviation High School -- Long Island City" \
  --out data/new_york/aviation_high_school_long_island_city_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/wilson_technological_center_aviation_program_east_farmingdale.txt \
  --museum "Wilson Technological Center Aviation Program -- East Farmingdale" \
  --out data/new_york/wilson_technological_center_aviation_program_east_farmingdale_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/hartland_veterans_memorial_hartland.txt \
  --museum "Hartland Veterans Memorial -- Hartland" \
  --out data/new_york/hartland_veterans_memorial_hartland_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/arnot_mall_horseheads.txt \
  --museum "Arnot Mall -- Horseheads" \
  --out data/new_york/arnot_mall_horseheads_aircraft.csv
python3 scripts/build_from_research.py --in data/new_york/raw/vfw_post_8265_eden.txt \
  --museum "VFW Post 8265 -- Eden" \
  --out data/new_york/vfw_post_8265_eden_aircraft.csv

echo "built: $(ls data/new_york/*aircraft.csv | wc -l) files, $(cat data/new_york/*aircraft.csv | grep -cv '^manufacturer,') rows"
