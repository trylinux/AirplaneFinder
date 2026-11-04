"""Build a clearly labeled repository-data seed; never connects to production.

For a release, replace this seed with a published production snapshot using
scripts/bundle_android_catalog.py. Repository CSVs are historical research
inputs, not a verified export of the deployed catalog.
"""
import csv
import json
import math
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from catalog_identity import join_designation, identity_keys
from models import type_match_key
from offline_catalog import KINDS, publish_snapshot, resolve_types
from validation import safe_http_url


def build():
    payload = {kind: [] for kind in KINDS}
    files = []
    for path in sorted((ROOT / 'data').rglob('*.csv')):
        if '_research' in path.parts or 'raw' in path.parts:
            continue
        with path.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames and (set(('name', 'city', 'country')) <= set(reader.fieldnames)
                                      or set(('manufacturer', 'model')) <= set(reader.fieldnames)):
                files.append((path, list(reader)))
    by_name, by_file, unique_museums = defaultdict(list), defaultdict(dict), {}
    for path, rows in files:
        for row in rows:
            if not row.get('name') or not row.get('country'):
                continue
            key = tuple((row.get(k) or '').strip().casefold() for k in ('name', 'city', 'country'))
            if key not in unique_museums:
                museum = {k: (row.get(k) or '').strip() or None for k in
                          ('name', 'city', 'state_province', 'country', 'region', 'address', 'postal_code', 'website')}
                museum['id'] = len(payload['museums']) + 1
                museum['access_type'] = row.get('access_type') or 'public'
                museum['website'] = safe_http_url(museum['website'])
                for axis, bound in [('latitude', 90), ('longitude', 180)]:
                    try:
                        value = float(row.get(axis) or '')
                        museum[axis] = value if math.isfinite(value) and abs(value) <= bound else None
                    except ValueError:
                        museum[axis] = None
                payload['museums'].append(museum)
                unique_museums[key] = museum
                by_name[key[0]].append(museum)
            by_file[path.parent][key[0]] = unique_museums[key]
    identity, exhibits, ambiguous = {}, {}, 0
    for path, rows in files:
        for row in rows:
            if not row.get('manufacturer') or not row.get('model'):
                continue
            name = (row.get('museum_name') or '').strip().casefold()
            museum = by_file[path.parent].get(name)
            if not museum and len(by_name[name]) == 1:
                museum = by_name[name][0]
            keys = identity_keys(row)
            # A serial-free type at one museum does not identify an airframe elsewhere.
            if not keys:
                keys = {('unmarked', str(path), name, row['manufacturer'], row['model'], row.get('variant', ''))}
            existing = sorted({identity[k] for k in keys if k in identity})
            if existing:
                aircraft_id = existing[0]
            else:
                aircraft = {k: (row.get(k) or '').strip() or None for k in
                            ('manufacturer', 'model', 'variant', 'tail_number', 'construction_number', 'operator_country',
                             'model_name', 'aircraft_name', 'aircraft_type', 'wing_type', 'military_civilian', 'role_type', 'description')}
                aircraft_id = aircraft['id'] = len(payload['aircraft']) + 1
                aircraft['full_designation'] = join_designation(aircraft['model'], aircraft['variant'])
                aircraft['aliases'] = [v.strip() for v in (row.get('aliases') or '').split(';') if v.strip()]
                try:
                    aircraft['year_built'] = int(row.get('year_built') or '')
                except ValueError:
                    aircraft['year_built'] = None
                payload['aircraft'].append(aircraft)
            for key in keys:
                identity.setdefault(key, aircraft_id)
            if museum:
                pair = (aircraft_id, museum['id'])
                if pair not in exhibits:
                    exhibits[pair] = {'id': len(exhibits) + 1, 'aircraft_id': aircraft_id,
                                      'museum_id': museum['id'], 'display_status': row.get('display_status') or 'on_display',
                                      'notes': 'Bundled repository research; confirm current display and visitor access.'}
            else:
                ambiguous += 1
    payload['exhibits'] = list(exhibits.values())
    seen_types = set()
    for name in ('seed_top25.json', 'seed_next50.json', 'batch_families_01.json'):
        for row in json.loads((ROOT / 'data/aircraft_types' / name).read_text()):
            if not row.get('model') or row.get('is_published') is False:
                continue
            key = (row['model'], row.get('variant'), row.get('manufacturer_scope'))
            if key in seen_types:
                continue
            seen_types.add(key)
            row.update(id=len(payload['types']) + 1, is_published=True,
                       match_key=type_match_key(row['model'], row.get('variant')),
                       designation=join_designation(row['model'], row.get('variant')))
            row['aliases'] = []
            for field in ('source_url', 'wikipedia_url'):
                row[field] = safe_http_url(row.get(field))
            payload['types'].append(row)
    resolve_types(payload['aircraft'], payload['types'])
    destination = ROOT / 'android/app/src/main/assets/seed'
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        manifest = publish_snapshot(payload, temporary, catalog_id='airplane-repository-seed-v1',
                                    source='Bundled repository research — not a live website export')
        shutil.copyfile(Path(temporary) / f"{manifest['revision']}.json.gz", destination / 'catalog.snapshot')
        shutil.copyfile(Path(temporary) / 'manifest.json', destination / 'manifest.json')
    print(json.dumps({'counts': manifest['counts'], 'bytes': manifest['byte_size'],
                      'aircraft_rows_without_unambiguous_museum': ambiguous}, indent=2))


if __name__ == '__main__':
    build()
