#!/usr/bin/env python3
"""Find the nearest museums displaying a given aircraft.

Hits ``/api/v1/nearest`` — public endpoint, no auth needed.

Usage
-----
    python3 scripts/find_nearest.py "C-130" "Dayton, OH"
    python3 scripts/find_nearest.py "B-29" "10001" --limit 10
    python3 scripts/find_nearest.py "F-16" "London" --museum "Imperial"
    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/find_nearest.py ...

Exit codes
    0  — at least one matching museum found
    1  — no matches (location resolved, but nothing nearby)
    2  — request failed (location couldn't be geocoded, etc.)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("aircraft",
                   help="Aircraft model, alias, or tail number (e.g. 'C-130')")
    p.add_argument("location",
                   help="ZIP/postal code or 'City, State'")
    p.add_argument("--museum", default="",
                   help="Optional museum-name filter")
    p.add_argument("--limit", "-n", type=int, default=5)
    p.add_argument("--base-url")
    args = p.parse_args()

    client = AirplaneClient(base_url=args.base_url)
    try:
        data = client.find_nearest(
            aircraft=args.aircraft, location=args.location,
            museum=args.museum, limit=args.limit,
        )
    except ApiError as e:
        # 404 from /nearest typically means we couldn't geocode the location
        # or no aircraft matched the query — surface the server's message.
        print(f"request failed: {e}", file=sys.stderr)
        sys.exit(2)

    results = data.get("results") or []
    origin = data.get("origin") or {}
    if not results:
        print(f"No matches found for {args.aircraft!r} near {args.location!r}.",
              file=sys.stderr)
        sys.exit(1)

    print(f"Origin: {origin.get('location')} "
          f"({origin.get('latitude')}, {origin.get('longitude')})")
    print()
    print(f"  {'#':>2}  {'distance':>10}  museum  /  aircraft")
    print(f"  {'-'*2}  {'-'*10}  {'-'*52}")
    for i, r in enumerate(results, start=1):
        dist = f"{r['distance_miles']} mi"
        mu, ac = r["museum"], r["aircraft"]
        loc = ", ".join(filter(None, [mu.get("city"), mu.get("country")]))
        line1 = f"  {i:>2}  {dist:>10}  {mu['name']}  ({loc})"
        line2 = f"  {' '*16}  {ac.get('full_designation') or ac.get('model')}" \
                f"{' — ' + r['display_status'] if r.get('display_status') else ''}"
        print(line1)
        print(line2)


if __name__ == "__main__":
    main()
