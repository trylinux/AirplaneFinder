"""Apply reviewed site plans through transactional merge APIs.

Defaults to a read-only preview. Use --apply with an explicit --base-url.
No module-import side effects, implicit production target, or DELETE fallback.
"""
import argparse
import json
from pathlib import Path

if __package__:
    from .airplane_api import AirplaneClient, ApiError
else:
    from airplane_api import AirplaneClient, ApiError


def apply_pair(client, plan):
    """Stop on the first failed preservation step. Each API merge is atomic."""
    keep_id, drop_id = plan['keep']['id'], plan['drop']['id']
    if any(type(value) is not int or value <= 0 for value in (keep_id, drop_id)) or keep_id == drop_id:
        raise ValueError('Invalid museum IDs in merge plan.')
    if plan.get('proven') is not True or plan.get('type_only'):
        raise ValueError('The pair needs a reviewed airframe identity match.')
    aircraft_ids = list(plan['delete_aircraft']) + [row['aircraft_id'] for row in plan['relink_links']]
    aircraft_ids += [row[field] for row in plan['matched'] for field in ('drop_aircraft', 'keep_aircraft')]
    if any(type(value) is not int or value <= 0 for value in aircraft_ids):
        raise ValueError('Invalid aircraft IDs in merge plan.')
    expected = set(plan['delete_aircraft']) | {row['aircraft_id'] for row in plan['relink_links']}
    matches = {row['drop_aircraft']: row['keep_aircraft'] for row in plan['matched']}
    if (set(matches) != set(plan['delete_aircraft']) or len(matches) != len(plan['matched'])
            or set(matches) & set(matches.values())):
        raise ValueError('Ambiguous aircraft matches; review the plan.')
    current = client.get_museum(drop_id)
    actual = {row['id'] for row in current['aircraft']}
    if actual != expected:
        raise ValueError('Collection changed since the plan; regenerate and review it.')
    for losing_id, surviving_id in matches.items():
        client.post(f'/api/v1/aircraft/{surviving_id}/merge', json={'drop_id': losing_id})
    client.post(f'/api/v1/museums/{keep_id}/merge', json={
        'drop_id': drop_id,
        # Aircraft merges preserve the losing museum's links under KEEP IDs.
        'expected_aircraft_ids': sorted({matches.get(value, value) for value in expected}),
    })


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=Path(__file__).resolve().parents[1] / 'data/_research/merge_plan.json')
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('drop_ids', nargs='*', type=int)
    args = parser.parse_args(argv)
    if args.apply and not args.all and not args.drop_ids:
        parser.error('--apply needs explicit losing museum IDs or --all')
    try:
        plans = json.loads(args.plan.read_text())
        client = AirplaneClient(base_url=args.base_url)
        for plan in plans:
            if not plan.get('proven') or (args.drop_ids and plan['drop']['id'] not in args.drop_ids):
                continue
            print(f"{plan['drop']['id']} -> {plan['keep']['id']}")
            if args.apply and not args.dry_run:
                apply_pair(client, plan)
        return 0
    except (OSError, ValueError, KeyError, TypeError, ApiError) as exc:
        print(f'Merge stopped: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
