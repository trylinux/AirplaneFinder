"""Copy a locally published production snapshot into the Android seed assets."""
import argparse
import gzip
import hashlib
import json
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot_directory', type=Path)
    args = parser.parse_args()
    manifest = json.loads((args.snapshot_directory / 'manifest.json').read_text())
    revision = manifest['revision']
    if len(revision) != 64 or any(c not in '0123456789abcdef' for c in revision):
        raise ValueError('Invalid revision')
    source = args.snapshot_directory / f'{revision}.json.gz'
    packed = source.read_bytes()
    if hashlib.sha256(packed).hexdigest() != manifest['sha256']:
        raise ValueError('Checksum mismatch')
    document = json.loads(gzip.decompress(packed))
    if document['schema_version'] != 1 or document['catalog_id'] != manifest['catalog_id']:
        raise ValueError('Unsupported snapshot')
    destination = Path(__file__).resolve().parents[1] / 'android/app/src/main/assets/seed'
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination / 'catalog.snapshot')
    shutil.copyfile(args.snapshot_directory / 'manifest.json', destination / 'manifest.json')
    print(f'Bundled {manifest["catalog_id"]}: {manifest["counts"]}')


if __name__ == '__main__':
    main()
