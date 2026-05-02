#!/usr/bin/env python3
"""Smoke-test the API. Hits ``/api/v1/stats`` and reports counts.

Designed to be called from cron / monit / a healthcheck timer. Exits 0 on
success and non-zero on any failure, with a single-line summary on stdout
that's friendly to ``logger`` or whatever else is listening.

Usage
-----
    python3 scripts/health_check.py
    AIRPLANE_BASE_URL=https://airplane.museum python3 scripts/health_check.py

    # Useful in cron — e.g. a 1-minute check that pings a status URL
    # if the API stops responding.
    * * * * *  python3 /opt/AirplaneFinder/scripts/health_check.py \\
                  || curl -s https://status-collector.example.com/airplane-down

Exit codes
    0  — API responded with a stats payload
    1  — API responded but the payload looks wrong
    2  — request failed entirely (network, 5xx, etc.)
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from airplane_api import AirplaneClient, ApiError  # noqa: E402


REQUIRED_KEYS = ("aircraft_count", "museum_count", "link_count", "country_count")


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base-url",
                   help="API base URL (overrides $AIRPLANE_BASE_URL)")
    p.add_argument("--timeout", type=float, default=10.0,
                   help="Seconds to wait for /stats (default: 10)")
    p.add_argument("--quiet", "-q", action="store_true",
                   help="Suppress success output; print only on failure")
    args = p.parse_args()

    client = AirplaneClient(base_url=args.base_url, timeout=args.timeout)
    started = time.monotonic()
    try:
        stats = client.stats()
    except ApiError as e:
        print(f"FAIL: API error {e.status} from {client.base_url} — {e.payload}")
        sys.exit(2)
    except Exception as e:
        # Network-level failure: name resolution, refused connection, timeout.
        print(f"FAIL: could not reach {client.base_url} — {type(e).__name__}: {e}")
        sys.exit(2)

    elapsed_ms = (time.monotonic() - started) * 1000

    missing = [k for k in REQUIRED_KEYS if k not in stats]
    if missing:
        print(f"FAIL: stats payload missing keys: {missing}")
        sys.exit(1)

    if not args.quiet:
        print(
            f"OK ({elapsed_ms:.0f} ms)  "
            f"aircraft={stats['aircraft_count']}  "
            f"museums={stats['museum_count']}  "
            f"exhibits={stats['link_count']}  "
            f"countries={stats['country_count']}"
        )
    sys.exit(0)


if __name__ == "__main__":
    main()
