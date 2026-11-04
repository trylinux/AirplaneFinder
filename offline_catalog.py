"""Publish immutable, public-only catalog snapshots for offline clients.

Generate explicitly with the CLI; HTTP reads never perform full catalog scans.
Keep old content-addressed files until no clients can be downloading them.
"""
import gzip
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from flask import abort, jsonify, send_file
from sqlalchemy.orm import Session, selectinload

from models import (db, Aircraft, Museum, AircraftMuseum, AircraftType,
                    AircraftFact, AircraftHistoryEvent, type_match_key,
                    manufacturer_matches)

SCHEMA_VERSION = 1
KINDS = ('aircraft', 'museums', 'exhibits', 'types', 'facts', 'history')


def resolve_types(aircraft, types):
    """Resolve once during export, using the same ranking as AircraftType."""
    index = {}
    for item in types:
        index.setdefault(item['match_key'], []).append((item, None))
        for alias in item.get('aliases', []):
            index.setdefault(alias['match_key'], []).append((item, alias))
    for row in aircraft:
        keys = list(dict.fromkeys([type_match_key(row['model'], row.get('variant')),
                                  type_match_key(row['model'])]))
        candidates = []
        for position, key in enumerate(keys):
            for item, alias in index.get(key, []):
                if not manufacturer_matches(item.get('manufacturer_scope'), row['manufacturer']):
                    continue
                if alias and not manufacturer_matches(alias.get('manufacturer_scope'), row['manufacturer']):
                    continue
                scope = (alias or item).get('manufacturer_scope')
                candidates.append(((position, int(alias is not None), int(not scope), item['id']), item['id']))
        row['type_id'] = min(candidates)[1] if candidates else None


def database_snapshot():
    """One repeatable-read transaction, with no account or unpublished data."""
    isolation = 'REPEATABLE READ' if db.engine.dialect.name in ('mysql', 'mariadb') else 'SERIALIZABLE'
    with db.engine.connect().execution_options(isolation_level=isolation) as connection:
        with connection.begin(), Session(bind=connection) as session:
            payload = {
                'aircraft': [a.to_dict() for a in session.query(Aircraft).options(selectinload(Aircraft.aliases)).order_by(Aircraft.id)],
                'museums': [m.to_dict() for m in session.query(Museum).order_by(Museum.id)],
                'exhibits': [{key: getattr(e, key) for key in ('id', 'aircraft_id', 'museum_id', 'display_status', 'notes')}
                             for e in session.query(AircraftMuseum).order_by(AircraftMuseum.id)],
                'types': [t.to_dict() for t in session.query(AircraftType).options(selectinload(AircraftType.aliases))
                          .filter_by(is_published=True).order_by(AircraftType.id)],
                'facts': [{'id': f.id, 'aircraft_id': f.aircraft_id, 'fact': f.fact,
                           'source_url': f.to_dict()['source_url']}
                          for f in session.query(AircraftFact).filter_by(is_active=True).order_by(AircraftFact.id)],
                'history': [h.to_dict() for h in session.query(AircraftHistoryEvent)
                            .filter_by(is_published=True).order_by(AircraftHistoryEvent.id)],
            }
    resolve_types(payload['aircraft'], payload['types'])
    return payload


def publish_snapshot(payload, directory, *, catalog_id='airplane.museum', source='Published website catalog'):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    document = {'schema_version': SCHEMA_VERSION, 'catalog_id': catalog_id,
                'generated_at': datetime.now(timezone.utc).isoformat(), 'source': source,
                **{kind: payload[kind] for kind in KINDS}}
    raw = json.dumps(document, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    packed = gzip.compress(raw, mtime=0)
    if len(raw) > 64 * 1024 * 1024 or len(packed) > 16 * 1024 * 1024:
        raise ValueError('Snapshot exceeds the v1 mobile client size limits.')
    revision = hashlib.sha256(packed).hexdigest()
    manifest = {key: document[key] for key in ('schema_version', 'catalog_id', 'generated_at', 'source')}
    manifest.update(revision=revision, sha256=revision, byte_size=len(packed), uncompressed_size=len(raw),
                    counts={kind: len(payload[kind]) for kind in KINDS},
                    download_path=f'/api/v1/offline/snapshots/{revision}.json.gz')
    def atomic_write(name, content):
        descriptor, temporary = tempfile.mkstemp(dir=directory)
        try:
            with os.fdopen(descriptor, 'wb') as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, directory / name)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    atomic_write(f'{revision}.json.gz', packed)
    atomic_write('manifest.json', json.dumps(manifest, indent=2).encode())
    return manifest


def register_offline(app):
    def directory():
        return Path(app.config['OFFLINE_CATALOG_DIR'])

    @app.get('/api/v1/offline/manifest')
    def offline_manifest():
        path = directory() / 'manifest.json'
        if not path.is_file():
            return jsonify(error='Offline catalog has not been published yet.'), 503
        return send_file(path, mimetype='application/json', conditional=True, max_age=300)

    @app.get('/api/v1/offline/snapshots/<revision>.json.gz')
    def offline_snapshot(revision):
        if not re.fullmatch(r'[0-9a-f]{64}', revision):
            abort(404)
        path = directory() / f'{revision}.json.gz'
        if not path.is_file():
            abort(404)
        return send_file(path, mimetype='application/gzip', conditional=True, max_age=31536000,
                         etag=revision)

    @app.cli.command('publish-offline-catalog')
    def publish_command():
        """Publish a consistent public snapshot after catalog maintenance."""
        manifest = publish_snapshot(database_snapshot(), directory())
        print(json.dumps(manifest, indent=2))
