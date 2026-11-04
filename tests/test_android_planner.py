"""Contract checks: Android's offline planner must agree with the website."""
import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest


@pytest.mark.parametrize('round_trip,max_stops,radius', [(False, 5, 500), (True, 1, 500), (True, 8, 1)])
def test_offline_stop_selection_matches_server(client, make_aircraft, make_museum, make_link,
                                             round_trip, max_stops, radius):
    from offline_catalog import database_snapshot
    node = os.environ.get('NODE_BINARY') or shutil.which('node')
    if not node:
        pytest.skip('Set NODE_BINARY to run the Android JavaScript parity tests.')
    a, b = make_aircraft(model='X', tail_number='ONE'), make_aircraft(model='Y', tail_number='TWO')
    for index, access in enumerate(('restricted', 'public', 'appointment')):
        museum = make_museum(name=f'Site {index}', latitude=index * .1, longitude=0, access_type=access)
        make_link(a, museum)
        if index == 2:
            make_link(b, museum)
    payload = {'origin': {'latitude': 0, 'longitude': 0}, 'round_trip': round_trip,
               'max_stops': max_stops, 'radius_miles': radius,
               'targets': [{'kind': 'airframe', 'aircraft_id': a.id}, {'kind': 'airframe', 'aircraft_id': b.id}]}
    expected = client.post('/api/v1/trips/plan', json=payload).json
    data = {**database_snapshot(), 'meta': {'catalog_id': 'test', 'revision': '1'}}
    module = Path(__file__).resolve().parents[1] / 'android/app/src/main/assets/catalog.js'
    program = "const lib=require(process.argv[1]);let s='';process.stdin.on('data',c=>s+=c);process.stdin.on('end',()=>{const x=JSON.parse(s);process.stdout.write(JSON.stringify(lib.create(x.data).plan(x.request)));});"
    result = subprocess.run([node, '-e', program, str(module)], input=json.dumps({'data': data, 'request': payload}),
                            text=True, capture_output=True, check=True)
    actual = json.loads(result.stdout)
    assert [s['museum']['id'] for s in actual['stops']] == [s['museum']['id'] for s in expected['stops']]
    assert actual['total_straight_line_miles'] == pytest.approx(expected['total_straight_line_miles'], abs=.1)
    assert len(actual['unmatched']) == len(expected['unmatched'])
