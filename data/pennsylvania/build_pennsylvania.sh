#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p data/pennsylvania

python3 scripts/build_from_research.py --in data/pennsylvania/raw/mid_atlantic_air_museum.txt \
  --museum "Mid-Atlantic Air Museum" \
  --out data/pennsylvania/mid_atlantic_air_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_helicopter_museum.txt \
  --museum "American Helicopter Museum & Education Center" \
  --out data/pennsylvania/american_helicopter_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/air_heritage_aviation_museum.txt \
  --museum "Air Heritage Aviation Museum" \
  --out data/pennsylvania/air_heritage_aviation_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/wings_of_freedom_aviation_museum.txt \
  --museum "Harold F. Pitcairn Wings of Freedom Aviation Museum" \
  --out data/pennsylvania/wings_of_freedom_aviation_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/piper_aviation_museum.txt \
  --museum "Piper Aviation Museum" \
  --out data/pennsylvania/piper_aviation_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/golden_age_air_museum.txt \
  --museum "Golden Age Air Museum" \
  --out data/pennsylvania/golden_age_air_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/eagles_mere_air_museum.txt \
  --museum "Eagles Mere Air Museum" \
  --out data/pennsylvania/eagles_mere_air_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/the_franklin_institute.txt \
  --museum "The Franklin Institute" \
  --out data/pennsylvania/the_franklin_institute_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/state_museum_of_pennsylvania.txt \
  --museum "The State Museum of Pennsylvania" \
  --out data/pennsylvania/state_museum_of_pennsylvania_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/klbe_air_museum_latrobe.txt \
  --museum "KLBE Air Museum -- Latrobe" \
  --out data/pennsylvania/klbe_air_museum_latrobe_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/us_army_heritage_and_education_center.txt \
  --museum "U.S. Army Heritage and Education Center -- Carlisle" \
  --out data/pennsylvania/us_army_heritage_and_education_center_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/pennsylvania_national_guard_military_museum.txt \
  --museum "Pennsylvania National Guard Military Museum -- Fort Indiantown Gap" \
  --out data/pennsylvania/pennsylvania_national_guard_military_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/171st_air_refueling_wing_heritage_display.txt \
  --museum "171st Air Refueling Wing Heritage Display -- Pittsburgh" \
  --out data/pennsylvania/171st_air_refueling_wing_heritage_display_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_7293_whitehall.txt \
  --museum "VFW Post 7293 -- Whitehall" \
  --out data/pennsylvania/vfw_post_7293_whitehall_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_8896_richard_j_gross_post_east_berlin.txt \
  --museum "VFW Post 8896 Richard J. Gross Post -- East Berlin" \
  --out data/pennsylvania/vfw_post_8896_richard_j_gross_post_east_berlin_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_813_dubois.txt \
  --museum "VFW Post 813 -- DuBois" \
  --out data/pennsylvania/vfw_post_813_dubois_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_7714_imperial.txt \
  --museum "VFW Post 7714 -- Imperial" \
  --out data/pennsylvania/vfw_post_7714_imperial_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_781_north_huntingdon.txt \
  --museum "VFW Post 781 -- North Huntingdon" \
  --out data/pennsylvania/vfw_post_781_north_huntingdon_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_8168_midland.txt \
  --museum "VFW Post 8168 -- Midland" \
  --out data/pennsylvania/vfw_post_8168_midland_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_8106_new_galilee.txt \
  --museum "VFW Post 8106 -- New Galilee" \
  --out data/pennsylvania/vfw_post_8106_new_galilee_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_92_new_kensington.txt \
  --museum "VFW Post 92 -- New Kensington" \
  --out data/pennsylvania/vfw_post_92_new_kensington_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_6615_white_haven.txt \
  --museum "VFW Post 6615 -- White Haven" \
  --out data/pennsylvania/vfw_post_6615_white_haven_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vfw_post_1568_towanda.txt \
  --museum "VFW Post 1568 -- Towanda" \
  --out data/pennsylvania/vfw_post_1568_towanda_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_460_beaverdale.txt \
  --museum "American Legion Post 460 -- Beaverdale" \
  --out data/pennsylvania/american_legion_post_460_beaverdale_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_506_american_legion_park_carrolltown.txt \
  --museum "American Legion Post 506 American Legion Park -- Carrolltown" \
  --out data/pennsylvania/american_legion_post_506_american_legion_park_carrolltown_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_712_pleasant_hills.txt \
  --museum "American Legion Post 712 -- Pleasant Hills" \
  --out data/pennsylvania/american_legion_post_712_pleasant_hills_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_940_west_brownsville.txt \
  --museum "American Legion Post 940 -- West Brownsville" \
  --out data/pennsylvania/american_legion_post_940_west_brownsville_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_257_stoystown.txt \
  --museum "American Legion Post 257 -- Stoystown" \
  --out data/pennsylvania/american_legion_post_257_stoystown_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_36_jersey_shore.txt \
  --museum "American Legion Post 36 -- Jersey Shore" \
  --out data/pennsylvania/american_legion_post_36_jersey_shore_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_139_milford.txt \
  --museum "American Legion Post 139 -- Milford" \
  --out data/pennsylvania/american_legion_post_139_milford_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/american_legion_post_957_new_berlin.txt \
  --museum "American Legion Post 957 -- New Berlin" \
  --out data/pennsylvania/american_legion_post_957_new_berlin_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vietnam_veterans_of_america_chapter_29_joseph_c_cappella_memorial_park.txt \
  --museum "Vietnam Veterans of America Chapter 29 Joseph C. Cappella Memorial Park -- Port Carbon" \
  --out data/pennsylvania/vietnam_veterans_of_america_chapter_29_joseph_c_cappella_memorial_park_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/vietnam_veterans_of_america_chapter_210_doylestown.txt \
  --museum "Vietnam Veterans of America Chapter 210 -- Doylestown" \
  --out data/pennsylvania/vietnam_veterans_of_america_chapter_210_doylestown_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/veterans_home_association_of_whitemarsh_valley_fort_washington.txt \
  --museum "Veterans Home Association of Whitemarsh Valley -- Fort Washington" \
  --out data/pennsylvania/veterans_home_association_of_whitemarsh_valley_fort_washington_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/memorial_park_new_kensington.txt \
  --museum "Memorial Park -- New Kensington" \
  --out data/pennsylvania/memorial_park_new_kensington_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/lynch_field_park_greensburg.txt \
  --museum "Lynch Field Park -- Greensburg" \
  --out data/pennsylvania/lynch_field_park_greensburg_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/lycoming_county_veterans_memorial_park_williamsport.txt \
  --museum "Lycoming County Veterans Memorial Park -- Williamsport" \
  --out data/pennsylvania/lycoming_county_veterans_memorial_park_williamsport_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/erie_county_memorial_gardens_erie.txt \
  --museum "Erie County Memorial Gardens -- Erie" \
  --out data/pennsylvania/erie_county_memorial_gardens_erie_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/butler_county_airport_gate_display_butler.txt \
  --museum "Butler County Airport gate display -- Butler" \
  --out data/pennsylvania/butler_county_airport_gate_display_butler_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/bradford_regional_airport_display_bradford.txt \
  --museum "Bradford Regional Airport display -- Bradford" \
  --out data/pennsylvania/bradford_regional_airport_display_bradford_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/cabela_s_hamburg_hamburg.txt \
  --museum "Cabela's Hamburg -- Hamburg" \
  --out data/pennsylvania/cabela_s_hamburg_hamburg_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/bass_pro_shops_harrisburg_harrisburg.txt \
  --museum "Bass Pro Shops Harrisburg -- Harrisburg" \
  --out data/pennsylvania/bass_pro_shops_harrisburg_harrisburg_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/the_collegeville_pit_stop_skippack.txt \
  --museum "The Collegeville Pit Stop -- Skippack" \
  --out data/pennsylvania/the_collegeville_pit_stop_skippack_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/901_pub_pottsville.txt \
  --museum "901 Pub -- Pottsville" \
  --out data/pennsylvania/901_pub_pottsville_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/tobyhanna_army_depot_memorial_display_park_tobyhanna.txt \
  --museum "Tobyhanna Army Depot Memorial Display Park -- Tobyhanna" \
  --out data/pennsylvania/tobyhanna_army_depot_memorial_display_park_tobyhanna_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/willow_grove_veterans_memorial_park_willow_grove.txt \
  --museum "Willow Grove Veterans Memorial Park -- Willow Grove" \
  --out data/pennsylvania/willow_grove_veterans_memorial_park_willow_grove_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/nemacolin_pride_and_joy_airplane_hangar_farmington.txt \
  --museum "Nemacolin Pride and Joy Airplane Hangar -- Farmington" \
  --out data/pennsylvania/nemacolin_pride_and_joy_airplane_hangar_farmington_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/naval_support_activity_philadelphia_aircraft_row_philadelphia.txt \
  --museum "Naval Support Activity Philadelphia aircraft row -- Philadelphia" \
  --out data/pennsylvania/naval_support_activity_philadelphia_aircraft_row_philadelphia_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/carlisle_airport_gate_guard_carlisle.txt \
  --museum "Carlisle Airport gate guard -- Carlisle" \
  --out data/pennsylvania/carlisle_airport_gate_guard_carlisle_aircraft.csv
python3 scripts/build_from_research.py --in data/pennsylvania/raw/indiana_county_jimmy_stewart_airport_indiana.txt \
  --museum "Indiana County Jimmy Stewart Airport -- Indiana" \
  --out data/pennsylvania/indiana_county_jimmy_stewart_airport_indiana_aircraft.csv

echo "built: $(ls data/pennsylvania/*_aircraft.csv | wc -l) files, $(cat data/pennsylvania/*_aircraft.csv | grep -cv '^manufacturer,') rows"
