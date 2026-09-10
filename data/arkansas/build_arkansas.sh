#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p data/arkansas

python3 scripts/build_from_research.py --in data/arkansas/raw/arkansas_air_and_military_museum.txt \
  --museum "Arkansas Air & Military Museum" \
  --out data/arkansas/arkansas_air_and_military_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/jacksonville_museum_of_military_history.txt \
  --museum "Jacksonville Museum of Military History" \
  --out data/arkansas/jacksonville_museum_of_military_history_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/wings_of_honor_museum.txt \
  --museum "Wings of Honor Museum" \
  --out data/arkansas/wings_of_honor_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/aviation_cadet_museum.txt \
  --museum "Aviation Cadet Museum -- Silver Wings Field" \
  --out data/arkansas/aviation_cadet_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/little_rock_afb_heritage_park.txt \
  --museum "Little Rock Air Force Base Heritage Park" \
  --out data/arkansas/little_rock_afb_heritage_park_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/little_rock_afb_main_gate.txt \
  --museum "Little Rock Air Force Base Main Gate" \
  --out data/arkansas/little_rock_afb_main_gate_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/jacksonville_lrafb_joint_education_center.txt \
  --museum "Jacksonville-Little Rock AFB Joint Education Center" \
  --out data/arkansas/jacksonville_lrafb_joint_education_center_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/189th_airlift_wing_base_operations.txt \
  --museum "189th Airlift Wing Base Operations -- Little Rock AFB" \
  --out data/arkansas/189th_airlift_wing_base_operations_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/arkansas_national_guard_museum_camp_robinson.txt \
  --museum "Arkansas National Guard Museum -- Camp Robinson" \
  --out data/arkansas/arkansas_national_guard_museum_camp_robinson_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/188th_wing_static_display_collection.txt \
  --museum "188th Wing Static Display Collection -- Fort Smith Regional Airport" \
  --out data/arkansas/188th_wing_static_display_collection_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/fort_chaffee_vietnam_veterans_museum.txt \
  --museum "Fort Chaffee Vietnam Veterans Museum -- Chaffee Crossing" \
  --out data/arkansas/fort_chaffee_vietnam_veterans_museum_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/vfw_post_5225_west_memphis.txt \
  --museum "VFW Post 5225 -- West Memphis" \
  --out data/arkansas/vfw_post_5225_west_memphis_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/vietnam_veterans_memorial_rogers.txt \
  --museum "Vietnam Veterans Memorial -- Rogers Executive Airport" \
  --out data/arkansas/vietnam_veterans_memorial_rogers_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/cross_county_veterans_memorial_wynne.txt \
  --museum "Cross County Veterans Memorial -- Wynne" \
  --out data/arkansas/cross_county_veterans_memorial_wynne_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/veterans_memorial_park_holiday_island.txt \
  --museum "Veterans Memorial Park -- Holiday Island" \
  --out data/arkansas/veterans_memorial_park_holiday_island_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/american_legion_post_41_helena.txt \
  --museum "American Legion Post 41 -- Helena-West Helena" \
  --out data/arkansas/american_legion_post_41_helena_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/kindley_park_gravette.txt \
  --museum "Kindley Park -- Gravette" \
  --out data/arkansas/kindley_park_gravette_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/vfw_post_1341_bull_shoals.txt \
  --museum "VFW Post 1341 -- Bull Shoals" \
  --out data/arkansas/vfw_post_1341_bull_shoals_aircraft.csv
python3 scripts/build_from_research.py --in data/arkansas/raw/vfw_post_9095_little_rock.txt \
  --museum "VFW Post 9095 -- Little Rock" \
  --out data/arkansas/vfw_post_9095_little_rock_aircraft.csv

echo "built: $(ls data/arkansas/*_aircraft.csv | wc -l) files, $(cat data/arkansas/*_aircraft.csv | grep -cv '^manufacturer,') rows"
