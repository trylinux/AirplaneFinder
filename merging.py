"""Transactional catalog merges. Callers commit once, or roll back on error."""
from models import (db, Aircraft, AircraftAlias, AircraftMuseum, AircraftFact,
                    AircraftHistoryEvent, Museum, UserMuseumAssignment)


def _pair(model, keep_id, drop_id):
    if type(drop_id) is not int or drop_id <= 0 or keep_id == drop_id:
        raise ValueError('Choose two different positive record IDs.')
    rows = (model.query.filter(model.id.in_([keep_id, drop_id]))
            .order_by(model.id).with_for_update().all())
    indexed = {row.id: row for row in rows}
    if keep_id not in indexed or drop_id not in indexed:
        raise ValueError('Both records must still exist; refresh the merge plan.')
    return indexed[keep_id], indexed[drop_id]


def _blank(value):
    return value is None or value == ''


def _combine(left, right):
    parts = list(dict.fromkeys(value for value in (left, right) if value))
    result = '\n\n'.join(parts) or None
    if result and len(result.encode('utf-8')) > 65535:
        raise ValueError('Combined notes exceed storage capacity; edit them before merging.')
    return result


def _move_links(links, *, aircraft_id=None, museum_id=None):
    for link in links:
        target_aircraft = aircraft_id if aircraft_id is not None else link.aircraft_id
        target_museum = museum_id if museum_id is not None else link.museum_id
        existing = AircraftMuseum.query.filter_by(
            aircraft_id=target_aircraft, museum_id=target_museum).first()
        if existing:
            if existing.display_status != link.display_status:
                raise ValueError('Exhibit statuses conflict; reconcile them before merging.')
            existing.notes = _combine(existing.notes, link.notes)
            db.session.delete(link)
        else:
            link.aircraft_id, link.museum_id = target_aircraft, target_museum
        db.session.flush()


def merge_aircraft(keep_id, drop_id):
    keep, drop = _pair(Aircraft, keep_id, drop_id)
    for field in ('manufacturer', 'model', 'variant', 'construction_number',
                  'operator_country', 'year_built', 'aircraft_name', 'model_name',
                  'aircraft_type', 'wing_type', 'military_civilian', 'role_type'):
        left, right = getattr(keep, field), getattr(drop, field)
        if not _blank(left) and not _blank(right) and str(left).casefold() != str(right).casefold():
            raise ValueError(f'{field} conflicts; reconcile the records before merging.')

    # Preserve both provenance texts, facts, and unpublished history milestones.
    description = _combine(keep.description, drop.description)
    aliases = list(dict.fromkeys([a.alias for a in keep.aliases] + [a.alias for a in drop.aliases]))
    if drop.tail_number and drop.tail_number != keep.tail_number:
        aliases = list(dict.fromkeys(aliases + [drop.tail_number]))
    fields = {field: getattr(drop, field) for field in (
        'variant', 'construction_number', 'operator_country', 'year_built',
        'aircraft_name', 'model_name', 'wing_type', 'role_type', 'tail_number',
    ) if _blank(getattr(keep, field))}
    _move_links(AircraftMuseum.query.filter_by(aircraft_id=drop_id).all(), aircraft_id=keep_id)
    for model in (AircraftFact, AircraftHistoryEvent):
        model.query.filter_by(aircraft_id=drop_id).update({'aircraft_id': keep_id}, synchronize_session='fetch')
    db.session.delete(drop)
    db.session.flush()  # Release DROP's identity before copying it to KEEP.
    for field, value in fields.items():
        setattr(keep, field, value)
    keep.description = description
    keep.aliases = [AircraftAlias(alias=value) for value in aliases]
    return keep


def merge_museums(keep_id, drop_id, expected_aircraft_ids):
    keep, drop = _pair(Museum, keep_id, drop_id)
    if (not isinstance(expected_aircraft_ids, list)
            or any(type(value) is not int or value <= 0 for value in expected_aircraft_ids)):
        raise ValueError('expected_aircraft_ids must list the reviewed losing collection.')
    links = AircraftMuseum.query.filter_by(museum_id=drop_id).with_for_update().all()
    if {link.aircraft_id for link in links} != set(expected_aircraft_ids):
        raise ValueError('The losing collection changed; refresh the merge plan.')
    if keep.country.casefold() != drop.country.casefold():
        raise ValueError('Museum countries differ; reconcile them before merging.')
    for field in ('postal_code', 'website', 'address', 'state_province'):
        left, right = getattr(keep, field), getattr(drop, field)
        if not _blank(left) and not _blank(right) and left != right:
            raise ValueError(f'{field} conflicts; reconcile the museums before merging.')
        if _blank(left):
            setattr(keep, field, right)
    if not keep.has_coordinates and drop.has_coordinates:
        keep.latitude, keep.longitude = drop.latitude, drop.longitude
    if keep.access_type != drop.access_type:
        raise ValueError('Museum access restrictions differ; reconcile them before merging.')
    _move_links(links, museum_id=keep_id)
    assigned = {a.user_id for a in UserMuseumAssignment.query.filter_by(museum_id=keep_id)}
    for assignment in UserMuseumAssignment.query.filter_by(museum_id=drop_id).all():
        if assignment.user_id in assigned:
            db.session.delete(assignment)
        else:
            assignment.museum_id = keep_id
            assigned.add(assignment.user_id)
    db.session.flush()
    db.session.delete(drop)
    return keep
