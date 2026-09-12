#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p data/georgia

python3 scripts/build_from_research.py --in data/georgia/raw/robins_topup.txt \
  --museum "Museum of Aviation -- Robins Air Force Base" \
  --out data/georgia/robins_topup_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/national_museum_of_the_mighty_eighth_air_force.txt \
  --museum "National Museum of the Mighty Eighth Air Force" \
  --out data/georgia/national_museum_of_the_mighty_eighth_air_force_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/delta_flight_museum.txt \
  --museum "Delta Flight Museum" \
  --out data/georgia/delta_flight_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/georgia_veterans_memorial_state_park_cordele.txt \
  --museum "Georgia Veterans Memorial State Park -- Cordele" \
  --out data/georgia/georgia_veterans_memorial_state_park_cordele_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/the_national_infantry_museum.txt \
  --museum "The National Infantry Museum" \
  --out data/georgia/the_national_infantry_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/commemorative_air_force_airbase_georgia.txt \
  --museum "Commemorative Air Force Airbase Georgia" \
  --out data/georgia/commemorative_air_force_airbase_georgia_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/army_aviation_heritage_foundation_and_flying_museum.txt \
  --museum "Army Aviation Heritage Foundation and Flying Museum" \
  --out data/georgia/army_aviation_heritage_foundation_and_flying_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/the_museum_of_flight_dallas.txt \
  --museum "The Museum of Flight -- Dallas" \
  --out data/georgia/the_museum_of_flight_dallas_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/the_museum_of_flight_rome.txt \
  --museum "The Museum of Flight -- Rome" \
  --out data/georgia/the_museum_of_flight_rome_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/griffin_b_bell_aerospace_technology_center_south_georgia_technical_col.txt \
  --museum "Griffin B. Bell Aerospace Technology Center -- South Georgia Technical College" \
  --out data/georgia/griffin_b_bell_aerospace_technology_center_south_georgia_technical_col_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/tellus_science_museum.txt \
  --museum "Tellus Science Museum" \
  --out data/georgia/tellus_science_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/57th_fighter_group_restaurant_atlanta.txt \
  --museum "57th Fighter Group Restaurant -- Atlanta" \
  --out data/georgia/57th_fighter_group_restaurant_atlanta_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/flying_cowboy_steakhouse_douglas.txt \
  --museum "Flying Cowboy Steakhouse -- Douglas" \
  --out data/georgia/flying_cowboy_steakhouse_douglas_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/zacks_mini_warehousing_locust_grove.txt \
  --museum "Zacks Mini Warehousing -- Locust Grove" \
  --out data/georgia/zacks_mini_warehousing_locust_grove_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/aviation_history_and_technology_center.txt \
  --museum "Aviation History & Technology Center" \
  --out data/georgia/aviation_history_and_technology_center_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/burger_king_locust_grove.txt \
  --museum "Burger King -- Locust Grove" \
  --out data/georgia/burger_king_locust_grove_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/president_george_w_bush_air_park_moody_air_force_base.txt \
  --museum "President George W. Bush Air Park -- Moody Air Force Base" \
  --out data/georgia/president_george_w_bush_air_park_moody_air_force_base_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/116th_air_control_wing_heritage_display_robins_air_force_base.txt \
  --museum "116th Air Control Wing Heritage Display -- Robins Air Force Base" \
  --out data/georgia/116th_air_control_wing_heritage_display_robins_air_force_base_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/dobbins_air_reserve_base_marietta.txt \
  --museum "Dobbins Air Reserve Base -- Marietta" \
  --out data/georgia/dobbins_air_reserve_base_marietta_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/georgia_air_national_guard_224th_joint_communications_support_squadron.txt \
  --museum "Georgia Air National Guard 224th Joint Communications Support Squadron -- Brunswick" \
  --out data/georgia/georgia_air_national_guard_224th_joint_communications_support_squadron_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/savannah_air_national_guard_base_garden_city.txt \
  --museum "Savannah Air National Guard Base -- Garden City" \
  --out data/georgia/savannah_air_national_guard_base_garden_city_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/memorial_park_alma.txt \
  --museum "Memorial Park -- Alma" \
  --out data/georgia/memorial_park_alma_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/vfw_post_2872_athens.txt \
  --museum "VFW Post 2872 -- Athens" \
  --out data/georgia/vfw_post_2872_athens_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/american_legion_post_201_alpharetta.txt \
  --museum "American Legion Post 201 -- Alpharetta" \
  --out data/georgia/american_legion_post_201_alpharetta_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/american_legion_post_77_conyers.txt \
  --museum "American Legion Post 77 -- Conyers" \
  --out data/georgia/american_legion_post_77_conyers_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/walk_of_heroes_veterans_war_memorial_conyers.txt \
  --museum "Walk of Heroes Veterans War Memorial -- Conyers" \
  --out data/georgia/walk_of_heroes_veterans_war_memorial_conyers_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/cobb_county_youth_museum_marietta.txt \
  --museum "Cobb County Youth Museum -- Marietta" \
  --out data/georgia/cobb_county_youth_museum_marietta_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/falcon_field_veterans_memorial_park_peachtree_city.txt \
  --museum "Falcon Field Veterans Memorial Park -- Peachtree City" \
  --out data/georgia/falcon_field_veterans_memorial_park_peachtree_city_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/helton_howland_memorial_park_tallapoosa.txt \
  --museum "Helton Howland Memorial Park -- Tallapoosa" \
  --out data/georgia/helton_howland_memorial_park_tallapoosa_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/american_legion_post_127_buford.txt \
  --museum "American Legion Post 127 -- Buford" \
  --out data/georgia/american_legion_post_127_buford_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/vfw_post_8433_cairo.txt \
  --museum "VFW Post 8433 -- Cairo" \
  --out data/georgia/vfw_post_8433_cairo_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/vfw_post_8433_davis_park_cairo.txt \
  --museum "VFW Post 8433 Davis Park -- Cairo" \
  --out data/georgia/vfw_post_8433_davis_park_cairo_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/holland_watson_veterans_memorial_park_chickamauga.txt \
  --museum "Holland-Watson Veterans Memorial Park -- Chickamauga" \
  --out data/georgia/holland_watson_veterans_memorial_park_chickamauga_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/american_legion_post_157_donalsonville.txt \
  --museum "American Legion Post 157 -- Donalsonville" \
  --out data/georgia/american_legion_post_157_donalsonville_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/hunter_memorial_park_douglasville.txt \
  --museum "Hunter Memorial Park -- Douglasville" \
  --out data/georgia/hunter_memorial_park_douglasville_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/vfw_post_8076_hartwell.txt \
  --museum "VFW Post 8076 -- Hartwell" \
  --out data/georgia/vfw_post_8076_hartwell_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/american_legion_post_123_lexington.txt \
  --museum "American Legion Post 123 -- Lexington" \
  --out data/georgia/american_legion_post_123_lexington_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/georgia_national_guard_academy_macon.txt \
  --museum "Georgia National Guard Academy -- Macon" \
  --out data/georgia/georgia_national_guard_academy_macon_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/vfw_post_6605_warner_robins.txt \
  --museum "VFW Post 6605 -- Warner Robins" \
  --out data/georgia/vfw_post_6605_warner_robins_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/warner_robins_city_hall_warner_robins.txt \
  --museum "Warner Robins City Hall -- Warner Robins" \
  --out data/georgia/warner_robins_city_hall_warner_robins_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/donnie_cochran_memorial_savannah_state_university.txt \
  --museum "Donnie Cochran Memorial -- Savannah State University" \
  --out data/georgia/donnie_cochran_memorial_savannah_state_university_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/american_legion_post_120_waynesboro.txt \
  --museum "American Legion Post 120 -- Waynesboro" \
  --out data/georgia/american_legion_post_120_waynesboro_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/masonic_lodge_197_willacoochee.txt \
  --museum "Masonic Lodge 197 -- Willacoochee" \
  --out data/georgia/masonic_lodge_197_willacoochee_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/veterans_memorial_park_williamson.txt \
  --museum "Veterans Memorial Park -- Williamson" \
  --out data/georgia/veterans_memorial_park_williamson_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/griffin_spalding_county_airport_griffin.txt \
  --museum "Griffin-Spalding County Airport -- Griffin" \
  --out data/georgia/griffin_spalding_county_airport_griffin_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/barrow_county_airport_winder.txt \
  --museum "Barrow County Airport -- Winder" \
  --out data/georgia/barrow_county_airport_winder_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/fannin_county_veterans_memorial_park_blue_ridge.txt \
  --museum "Fannin County Veterans Memorial Park -- Blue Ridge" \
  --out data/georgia/fannin_county_veterans_memorial_park_blue_ridge_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/bleckley_county_school_cochran.txt \
  --museum "Bleckley County School -- Cochran" \
  --out data/georgia/bleckley_county_school_cochran_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/sam_s_burger_deli_rooftop_armuchee.txt \
  --museum "Sam's Burger Deli rooftop -- Armuchee" \
  --out data/georgia/sam_s_burger_deli_rooftop_armuchee_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/douglas_municipal_airport_douglas.txt \
  --museum "Douglas Municipal Airport -- Douglas" \
  --out data/georgia/douglas_municipal_airport_douglas_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/byron_roadside_t_33_display_byron.txt \
  --museum "Byron Roadside T-33 Display -- Byron" \
  --out data/georgia/byron_roadside_t_33_display_byron_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/webb_military_museum_savannah.txt \
  --museum "Webb Military Museum -- Savannah" \
  --out data/georgia/webb_military_museum_savannah_aircraft.csv
python3 scripts/build_from_research.py --in data/georgia/raw/6th_cavalry_museum_fort_oglethorpe.txt \
  --museum "6th Cavalry Museum -- Fort Oglethorpe" \
  --out data/georgia/6th_cavalry_museum_fort_oglethorpe_aircraft.csv

echo "built: $(ls data/georgia/*aircraft.csv | wc -l) files, $(cat data/georgia/*aircraft.csv | grep -cv '^manufacturer,') rows"
