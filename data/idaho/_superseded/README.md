Superseded. `id_parks_aircraft.csv` held all three Idaho park monuments in
one file, which breaks the one-file-per-museum rule in METHODOLOGY.md (and
is caught by tests/test_flagship_topup_files.py). Its rows now live in
carl_miller_park_aircraft.csv, lakeview_park_aircraft.csv and
malad_city_park_aircraft.csv, unchanged.

Kept only because this shell cannot delete files on the host. Safe to remove.
