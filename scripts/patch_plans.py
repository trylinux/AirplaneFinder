"""Narrow, explicit application of reviewed catalog plans; never execute plan text."""
import argparse
import json
from pathlib import Path

if __package__:
    from .airplane_api import AirplaneClient, ApiError
else:
    from airplane_api import AirplaneClient, ApiError


def patch_body(entry, allowed):
    if not isinstance(entry, dict) or type(entry.get('_id')) is not int or entry['_id'] <= 0:
        raise ValueError('Each plan entry needs a positive integer _id.')
    body = {key: value for key, value in entry.items() if not key.startswith('_')}
    if not body or set(body) - set(allowed):
        raise ValueError(f'Plan may only change: {", ".join(sorted(allowed))}.')
    for key, value in body.items():
        if key == 'aliases':
            if not isinstance(value, list) or any(not isinstance(alias, str) for alias in value):
                raise ValueError('aliases must be an array of text.')
        elif value is not None and not isinstance(value, str):
            raise ValueError(f'{key} must be text or null.')
    return body


def main(allowed, argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    try:
        entries = json.loads(args.plan.read_text())
        if not isinstance(entries, list):
            raise ValueError('Plan must be an array of objects.')
        # Validate the whole plan before making even one write.
        patches = [(entry['_id'], patch_body(entry, allowed)) for entry in entries]
        if not args.apply or args.dry_run:
            print(f'{len(patches)} reviewed changes; preview only. Use --apply to write.')
            return 0
        client = AirplaneClient(base_url=args.base_url)
        for aircraft_id, body in patches:
            current = client.get_aircraft(aircraft_id)['aircraft']
            if all(current.get(key) == value for key, value in body.items()):
                continue
            client.patch(f'/api/v1/aircraft/{aircraft_id}', json=body)
            print(f'Applied aircraft {aircraft_id}: {", ".join(body)}')
        return 0
    except (OSError, ValueError, KeyError, TypeError, ApiError) as exc:
        print(f'Plan stopped: {exc}')
        return 1
