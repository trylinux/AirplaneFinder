#!/usr/bin/env python3
"""Find and merge duplicate aircraft rows.

Two aircraft rows are *suspected duplicates* when:
  - they share the same (manufacturer, model, variant), case-insensitive
    and whitespace-trimmed, AND
  - the group has more than one row.

That's intentionally broad — the script REPORTS suspects, it doesn't
auto-delete. A curator inspects the report and decides whether two
rows really are the same airframe (e.g. a curator double-entered a
plane) or distinct airframes of the same type that just happen to share
metadata (e.g. four physical F-14As, each at a different museum).

Usage
-----
Report (default — no DB writes):
    python3 scripts/dedupe_aircraft.py
    python3 scripts/dedupe_aircraft.py --json     # machine-readable
    python3 scripts/dedupe_aircraft.py --min 3    # only groups of 3+

Merge two rows (re-point KEEP's links/aliases, delete DROP):
    python3 scripts/dedupe_aircraft.py --merge KEEP_ID DROP_ID
    python3 scripts/dedupe_aircraft.py --merge 12 47 --yes   # skip prompt

Merge semantics
---------------
  - Every AircraftMuseum link pointing at DROP is re-pointed at KEEP.
    If KEEP is already linked to that museum, DROP's link is deleted
    (the unique (aircraft_id, museum_id) index forbids the conflict).
  - Every AircraftAlias attached to DROP is re-pointed at KEEP, with
    deduplication so KEEP doesn't end up with two identical alias rows.
  - DROP's Aircraft row is then deleted. ON DELETE CASCADE handles any
    remaining cleanup.
  - Everything happens inside one transaction. A failure rolls back.

Exit codes
    0  — report ran or merge committed
    1  — no duplicates found (in report mode), or merge declined
    2  — bad arguments / row not found
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

# Run as a top-level script: sys.path needs the repo root so `from app
# import app, db` resolves to the Flask app, not (e.g.) the stdlib.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app, db  # noqa: E402
from models import Aircraft, AircraftAlias, AircraftMuseum, Museum  # noqa: E402


# ─────────────────────────────────────────────────────────────────────
# Grouping — what counts as a duplicate suspect
# ─────────────────────────────────────────────────────────────────────

def _norm(s):
    """Case-insensitive trim, treating None and '' the same."""
    if s is None:
        return ""
    return s.strip().lower()


def find_duplicate_groups(min_size=2):
    """Return list of (key, [Aircraft rows]) for every group of size >= min_size.

    Key is the (manufacturer, model, variant) tuple — normalized, but
    returned in canonical form (the first row's values).
    """
    groups = defaultdict(list)
    for ac in Aircraft.query.order_by(Aircraft.id).all():
        key = (_norm(ac.manufacturer), _norm(ac.model), _norm(ac.variant))
        groups[key].append(ac)
    return [
        (members[0], members)
        for key, members in sorted(groups.items())
        if len(members) >= min_size
    ]


# ─────────────────────────────────────────────────────────────────────
# Report mode
# ─────────────────────────────────────────────────────────────────────

def _museum_names_for(aircraft_id):
    """Names of museums this aircraft is linked to, sorted for stable output."""
    return sorted(
        m.name for m in db.session.query(Museum.name)
        .join(AircraftMuseum, AircraftMuseum.museum_id == Museum.id)
        .filter(AircraftMuseum.aircraft_id == aircraft_id)
        .all()
    )


def _row_summary(ac):
    """Compact dict describing one Aircraft row for the report."""
    return {
        "id": ac.id,
        "tail_number": ac.tail_number,
        "aircraft_name": ac.aircraft_name,
        "year_built": ac.year_built,
        "museums": _museum_names_for(ac.id),
    }


def _print_text_report(groups):
    print("=" * 70)
    print(f"  Duplicate-suspect aircraft groups: {len(groups)}")
    print("=" * 70)
    if not groups:
        print("  (none — every (manufacturer, model, variant) is unique)")
        return
    for canonical, members in groups:
        header = " ".join(filter(None, [
            canonical.manufacturer, canonical.model, canonical.variant or ""
        ])).strip()
        print()
        print(f"  ── {header} — {len(members)} rows ──")
        for ac in members:
            row = _row_summary(ac)
            tail = row["tail_number"] or "(no tail)"
            name = f' "{row["aircraft_name"]}"' if row["aircraft_name"] else ""
            yr = f" [{row['year_built']}]" if row["year_built"] else ""
            museums = ", ".join(row["museums"]) or "(unlinked)"
            print(f"    id={row['id']:>4}  {tail:<14}{name}{yr}")
            print(f"             at: {museums}")
        # Suggest a keep target: row with the most informative metadata.
        ranked = sorted(
            members,
            key=lambda a: (
                bool(a.tail_number),
                bool(a.aircraft_name),
                bool(a.year_built),
                len(_museum_names_for(a.id)),
                -a.id,  # tiebreak: lower id wins (older row)
            ),
            reverse=True,
        )
        print(f"    suggest: keep id={ranked[0].id}, "
              f"merge candidates: {[a.id for a in ranked[1:]]}")
    print()
    print("  Next step (per group):")
    print("    python3 scripts/dedupe_aircraft.py --merge <KEEP_ID> <DROP_ID>")


def _print_json_report(groups):
    out = []
    for canonical, members in groups:
        out.append({
            "manufacturer": canonical.manufacturer,
            "model": canonical.model,
            "variant": canonical.variant,
            "rows": [_row_summary(ac) for ac in members],
        })
    print(json.dumps(out, indent=2, default=str))


# ─────────────────────────────────────────────────────────────────────
# Merge mode
# ─────────────────────────────────────────────────────────────────────

def merge(keep_id, drop_id, assume_yes=False):
    """Re-point DROP's links/aliases onto KEEP, then delete DROP.

    Returns (links_moved, links_dropped, aliases_moved, aliases_dropped).
    Raises ValueError on bad input. Wraps the work in a transaction so a
    failure rolls everything back.
    """
    if keep_id == drop_id:
        raise ValueError("KEEP and DROP cannot be the same id")

    keep = Aircraft.query.get(keep_id)
    drop = Aircraft.query.get(drop_id)
    if not keep:
        raise ValueError(f"keep_id={keep_id} not found")
    if not drop:
        raise ValueError(f"drop_id={drop_id} not found")

    # Show the operator what's about to happen so they can bail.
    keep_museums = _museum_names_for(keep_id)
    drop_museums = _museum_names_for(drop_id)
    keep_aliases = [a.alias for a in keep.aliases]
    drop_aliases = [a.alias for a in drop.aliases]

    print("─" * 70)
    print(f"  KEEP id={keep.id}:  {keep.manufacturer} {keep.model} "
          f"{keep.variant or ''}  tail={keep.tail_number or '(none)'}")
    print(f"    museums: {', '.join(keep_museums) or '(none)'}")
    print(f"    aliases: {', '.join(keep_aliases) or '(none)'}")
    print(f"  DROP id={drop.id}:  {drop.manufacturer} {drop.model} "
          f"{drop.variant or ''}  tail={drop.tail_number or '(none)'}")
    print(f"    museums: {', '.join(drop_museums) or '(none)'}")
    print(f"    aliases: {', '.join(drop_aliases) or '(none)'}")
    print()
    print(f"  Will: re-point DROP's links/aliases onto KEEP, delete DROP.")
    print(f"  This is irreversible (no soft-delete).")

    if not assume_yes:
        ans = input("  Proceed? [y/N]: ").strip().lower()
        if ans not in ("y", "yes"):
            print("  Aborted.")
            return None

    # We use bulk SQL UPDATEs/DELETEs here rather than touching the ORM
    # relationships. The Aircraft.aliases relationship has
    # cascade="all, delete-orphan", which would helpfully (but
    # incorrectly) delete the moved aliases when we eventually
    # session.delete(drop) — the in-memory collection still has them.
    # Going through the SQL layer sidesteps that entirely.

    # ── Links: re-point what we can, delete the rest ──
    keep_museum_ids = {
        mid for (mid,) in db.session.query(AircraftMuseum.museum_id)
        .filter_by(aircraft_id=keep.id).all()
    }
    # Duplicate links (DROP linked to a museum KEEP is already linked to)
    # have to be deleted before the re-point, otherwise the
    # (aircraft_id, museum_id) UNIQUE index trips.
    links_dropped = db.session.execute(
        AircraftMuseum.__table__.delete().where(
            AircraftMuseum.aircraft_id == drop.id,
            AircraftMuseum.museum_id.in_(keep_museum_ids) if keep_museum_ids else False,
        )
    ).rowcount if keep_museum_ids else 0
    links_moved = db.session.execute(
        AircraftMuseum.__table__.update()
        .where(AircraftMuseum.aircraft_id == drop.id)
        .values(aircraft_id=keep.id)
    ).rowcount

    # ── Aliases: re-point unique ones, delete duplicates ──
    keep_alias_set = {
        a for (a,) in db.session.query(AircraftAlias.alias)
        .filter_by(aircraft_id=keep.id).all()
    }
    aliases_dropped = db.session.execute(
        AircraftAlias.__table__.delete().where(
            AircraftAlias.aircraft_id == drop.id,
            AircraftAlias.alias.in_(keep_alias_set) if keep_alias_set else False,
        )
    ).rowcount if keep_alias_set else 0
    aliases_moved = db.session.execute(
        AircraftAlias.__table__.update()
        .where(AircraftAlias.aircraft_id == drop.id)
        .values(aircraft_id=keep.id)
    ).rowcount

    # ── Delete DROP. By now it owns no links or aliases, so cascade has
    # nothing left to do. Expire identity-map state so SA doesn't try to
    # re-process drop.aliases / drop.museum_links from a stale snapshot. ──
    db.session.expire(drop)
    db.session.delete(drop)
    db.session.commit()

    print(f"  Done. links moved={links_moved}, links dropped (already on "
          f"KEEP)={links_dropped}, aliases moved={aliases_moved}, "
          f"aliases dropped={aliases_dropped}.")
    return (links_moved, links_dropped, aliases_moved, aliases_dropped)


# ─────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(
        description="Find/merge duplicate aircraft rows.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  Report duplicates:\n"
            "    %(prog)s\n"
            "    %(prog)s --json\n"
            "  Merge (re-point links/aliases from DROP to KEEP, delete DROP):\n"
            "    %(prog)s --merge KEEP_ID DROP_ID\n"
            "    %(prog)s --merge 12 47 --yes\n"
        ),
    )
    p.add_argument("--json", action="store_true",
                   help="emit JSON instead of formatted text (report mode)")
    p.add_argument("--min", type=int, default=2, metavar="N",
                   help="only report groups with N or more rows (default 2)")
    p.add_argument("--merge", nargs=2, type=int, metavar=("KEEP_ID", "DROP_ID"),
                   help="merge DROP_ID into KEEP_ID")
    p.add_argument("--yes", action="store_true",
                   help="skip the confirmation prompt during merge")
    args = p.parse_args()

    with app.app_context():
        if args.merge:
            keep_id, drop_id = args.merge
            try:
                result = merge(keep_id, drop_id, assume_yes=args.yes)
            except ValueError as e:
                print(f"error: {e}", file=sys.stderr)
                return 2
            return 0 if result is not None else 1

        groups = find_duplicate_groups(min_size=args.min)
        if args.json:
            _print_json_report(groups)
        else:
            _print_text_report(groups)
        return 0 if groups else 1


if __name__ == "__main__":
    sys.exit(main())
