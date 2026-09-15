"""SQLAlchemy models."""

import re
import secrets
import hashlib
from datetime import datetime, timezone
from math import radians, sin, cos, sqrt, atan2

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Computed
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# ──────────────────────────────────────────────
# Auth models
# ──────────────────────────────────────────────

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200))
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="viewer")  # admin, aircraft_admin, manager, viewer
    is_active_user = db.Column("is_active", db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    last_login_ip = db.Column(db.String(45), nullable=True)     # IPv4 or IPv6
    last_logout = db.Column(db.DateTime, nullable=True)
    contribution_count = db.Column(db.Integer, default=0, nullable=False)
    # Failed-login tracking: incremented on each bad attempt against this
    # username, reset to zero on any successful login. When it crosses the
    # configured threshold, locked_until is set and the account refuses
    # logins until that timestamp passes.
    failed_login_count = db.Column(db.Integer, default=0, nullable=False)
    locked_until = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Default lazy loading; the only site that walks user.api_keys is
    # User.to_dict. Everywhere else queries ApiKey directly via its own model.
    api_keys = db.relationship("ApiKey", back_populates="user", cascade="all, delete-orphan")
    # Default ("select") lazy loading: these were previously lazy="joined", which
    # meant every User query — including the Flask-Login load_user() call on each
    # session request — joined both assignment tables even when unused. Callers
    # that DO need them (admin list views) should use selectinload() explicitly.
    museum_assignments = db.relationship("UserMuseumAssignment", back_populates="user", cascade="all, delete-orphan")
    country_assignments = db.relationship("UserCountryAssignment", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_active(self):
        return self.is_active_user

    @property
    def is_admin(self):
        """Strict 'admin' role check. Use this for user-management gates —
        only true admins should be able to create/edit/delete users."""
        return self.role == "admin"

    @property
    def is_aircraft_admin(self):
        """Strict 'aircraft_admin' role check. The role gets full CRUD over
        aircraft/museums/exhibits/templates, but cannot manage users."""
        return self.role == "aircraft_admin"

    @property
    def is_data_admin(self):
        """True if the user can perform admin-level data operations
        (deletes, etc.) on aircraft, museums, exhibits, or templates.

        Use this — not is_admin — to gate data-delete endpoints, so that
        the new aircraft_admin role gets the same data privileges without
        also unlocking user management."""
        return self.role in ("admin", "aircraft_admin")

    @property
    def is_manager(self):
        """True if the user can create/update data. Includes admin and
        aircraft_admin since both have at least the manager-level write
        privileges as a subset of theirs."""
        return self.role in ("admin", "aircraft_admin", "manager")

    def assigned_museum_ids(self):
        """Return set of museum IDs this user is assigned to."""
        return {a.museum_id for a in self.museum_assignments}

    def assigned_countries(self):
        """Return set of country names this user is assigned to."""
        return {a.country for a in self.country_assignments}

    @property
    def is_locked(self):
        """True if a lockout window is currently active for this account."""
        if self.locked_until is None:
            return False
        # locked_until may be naive (MySQL TIMESTAMP); treat naive as UTC.
        lu = self.locked_until
        if lu.tzinfo is None:
            lu = lu.replace(tzinfo=timezone.utc)
        return datetime.now(timezone.utc) < lu

    def lockout_seconds_remaining(self):
        """Seconds until the lockout expires, or 0 if not locked."""
        if not self.is_locked:
            return 0
        lu = self.locked_until
        if lu.tzinfo is None:
            lu = lu.replace(tzinfo=timezone.utc)
        return max(0, int((lu - datetime.now(timezone.utc)).total_seconds()))

    def register_failed_login(self, max_attempts, lockout_seconds):
        """Bump failed_login_count; if at threshold, lock for lockout_seconds.

        Caller must commit. Returns True if the failure caused a fresh lock.
        """
        from datetime import timedelta
        self.failed_login_count = (self.failed_login_count or 0) + 1
        if self.failed_login_count >= max_attempts:
            self.locked_until = datetime.now(timezone.utc) + timedelta(seconds=lockout_seconds)
            return True
        return False

    def reset_failed_logins(self):
        """Wipe lockout state. Call on any successful login. Caller commits."""
        self.failed_login_count = 0
        self.locked_until = None

    def can_access_museum(self, museum):
        """Data admins access every museum; other roles require an assignment."""
        if self.is_data_admin:
            return True
        museum_ids = self.assigned_museum_ids()
        countries = self.assigned_countries()
        if not museum_ids and not countries:
            return False
        if museum_ids and museum.id in museum_ids:
            return True
        if countries and museum.country in countries:
            return True
        return False

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "is_admin": self.is_admin,
            "is_active": self.is_active,
            "last_login": self.last_login.isoformat() if self.last_login else None,
            "last_login_ip": self.last_login_ip,
            "last_logout": self.last_logout.isoformat() if self.last_logout else None,
            "contribution_count": self.contribution_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "assigned_museums": [a.museum_id for a in self.museum_assignments],
            "assigned_countries": [a.country for a in self.country_assignments],
            "api_keys": [k.to_dict() for k in self.api_keys if k.is_active],
        }


class UserMuseumAssignment(db.Model):
    __tablename__ = "user_museum_assignments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    museum_id = db.Column(db.Integer, db.ForeignKey("museums.id", ondelete="CASCADE"), nullable=False)

    user = db.relationship("User", back_populates="museum_assignments")
    museum = db.relationship("Museum")


class UserCountryAssignment(db.Model):
    __tablename__ = "user_country_assignments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    user = db.relationship("User", back_populates="country_assignments")


class ApiKey(db.Model):
    __tablename__ = "api_keys"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    key_hash = db.Column(db.String(256), nullable=False)
    key_prefix = db.Column(db.String(16), nullable=True)   # first 12 chars for identification
    label = db.Column(db.String(100), default="default")
    is_active = db.Column(db.Boolean, default=True)
    permissions = db.Column(db.String(50), default="read")  # read, readwrite, admin
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    expires_at = db.Column(db.DateTime, nullable=True)        # NULL = never expires
    last_used = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="api_keys")

    @staticmethod
    def hash_key(raw_key):
        return hashlib.sha256(raw_key.encode()).hexdigest()

    @classmethod
    def generate(cls, user_id, label="default", permissions="read", expires_at=None):
        """Create a new API key; returns (ApiKey object, raw_key)."""
        raw_key = "amt_" + secrets.token_hex(24)  # 48-char hex + prefix
        obj = cls(
            user_id=user_id,
            key_hash=cls.hash_key(raw_key),
            key_prefix=raw_key[:12],              # store "amt_XXXXXXXX" for display
            label=label,
            permissions=permissions,
            expires_at=expires_at,
        )
        return obj, raw_key

    @property
    def is_expired(self):
        """True if the key has an expiry date that has passed."""
        if self.expires_at is None:
            return False
        exp = self.expires_at if self.expires_at.tzinfo else self.expires_at.replace(tzinfo=timezone.utc)
        return datetime.now(timezone.utc) > exp

    @classmethod
    def lookup(cls, raw_key):
        """Find an active, non-expired ApiKey by raw key string."""
        h = cls.hash_key(raw_key)
        key = cls.query.filter_by(key_hash=h, is_active=True).first()
        if key and key.is_expired:
            return None
        return key

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "key_prefix": (self.key_prefix or "amt_????") + "…",
            "label": self.label,
            "permissions": self.permissions,
            "is_active": self.is_active,
            "is_expired": self.is_expired,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "last_used": self.last_used.isoformat() if self.last_used else None,
        }


# ──────────────────────────────────────────────
# Domain models
# ──────────────────────────────────────────────

class Museum(db.Model):
    __tablename__ = "museums"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state_province = db.Column(db.String(100))          # state, province, county, etc.
    country = db.Column(db.String(100), nullable=False, default="United States")
    postal_code = db.Column(db.String(20))               # optional
    region = db.Column(db.String(50), nullable=False)     # North America, Europe, etc.
    address = db.Column(db.String(300))
    website = db.Column(db.String(300))
    # Visitor access. 'public' = walk in; 'appointment' = call ahead or
    # open-house only; 'restricted' = base access / escort / DoD ID.
    # Proximity search hides 'restricted' unless explicitly asked for it,
    # mirroring how display_status hides aircraft a visitor can't see.
    access_type = db.Column(db.String(20), nullable=False,
                            default="public", server_default="public")
    latitude = db.Column(db.Numeric(10, 7))               # nullable
    longitude = db.Column(db.Numeric(10, 7))              # nullable

    # cascade + passive_deletes: when a Museum is deleted, MySQL's ON DELETE
    # CASCADE on aircraft_museum.museum_id handles the link cleanup. Telling
    # SQLAlchemy to skip its own NULL-the-FK behavior avoids an IntegrityError
    # (the aircraft_museum FK columns are NOT NULL) and avoids a redundant
    # round-trip to bulk-delete the rows itself.
    aircraft_links = db.relationship(
        "AircraftMuseum",
        back_populates="museum",
        lazy="dynamic",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    @property
    def has_coordinates(self):
        return self.latitude is not None and self.longitude is not None

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "state_province": self.state_province,
            "country": self.country,
            "postal_code": self.postal_code,
            "region": self.region,
            "address": self.address,
            "website": self.website,
            "access_type": self.access_type or "public",
            "latitude": float(self.latitude) if self.latitude is not None else None,
            "longitude": float(self.longitude) if self.longitude is not None else None,
        }


# ── Designation joining ───────────────────────────────────────────────
#
# ``full_designation`` used to be CONCAT(model, '-', variant), which produced
# "SR-71-A" and "F-4-C". Aviation writes those "SR-71A" and "F-4C". The join
# depends on what sits either side of the seam; a sweep of the catalogue put
# every pair the database holds into one of three buckets:
#
#   model ends in a digit, variant starts with a letter  (2,673 rows)
#       -> no separator:  SR-71 + A      = SR-71A
#                         UH-1  + H      = UH-1H
#   variant starts with a digit                            (418 rows)
#       -> a dash:        747   + 100    = 747-100
#                         FJ    + 1      = FJ-1
#                         PA-28 + 180    = PA-28-180
#   anything else (both sides alphabetic)                  (241 rows)
#       -> a space:       Vampire + T.35 = Vampire T.35
#                         Titan   + II   = Titan II
#
# The one knowingly-wrong case is a proper-name model with a numeric variant
# ("Mercure" + "100" renders "Mercure-100", not "Mercure 100"). Telling those
# apart from Navy short designators (FJ-1, R4D-6S, ZPG-2) needs judgement the
# expression cannot make, and the Navy forms are far more numerous.
#
# SQL mirrors of this function live in schema.sql (MySQL) and
# tests/conftest.py (SQLite). All three must agree — test_designation.py
# checks the Python one against the SQLite one on real pairs.

_DIGITS = "0123456789"


def join_designation(model, variant):
    """Join a model and variant the way the generated column does."""
    model = (model or "").strip()
    variant = (variant or "").strip()
    if not variant:
        return model
    if variant[0] in _DIGITS:
        return f"{model}-{variant}"
    if model and model[-1] in _DIGITS:
        return f"{model}{variant}"
    return f"{model} {variant}"


# Kept next to join_designation() so the two are edited together. Mirrored in
# schema.sql; changing either means writing a migration (see
# migrate_full_designation.sql).
_FULL_DESIGNATION_SQL = (
    "CONCAT(model, CASE"
    "  WHEN variant IS NULL OR variant = '' THEN ''"
    "  WHEN LOCATE(LEFT(variant, 1), '0123456789') > 0 THEN CONCAT('-', variant)"
    "  WHEN LOCATE(RIGHT(model, 1), '0123456789') > 0 THEN variant"
    "  ELSE CONCAT(' ', variant)"
    " END)"
)


class Aircraft(db.Model):
    __tablename__ = "aircraft"

    id = db.Column(db.Integer, primary_key=True)
    tail_number = db.Column(db.String(20))
    model_name = db.Column(db.String(200))       # type common name: "Cobra", "Hercules"
    aircraft_name = db.Column(db.String(200))     # individual name: "Daisy Duke", "Bockscar"
    manufacturer = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    variant = db.Column(db.String(50))
    # Manufacturer's construction number / msn. Not part of any unique key --
    # see the note on uq_airframe in schema.sql.
    construction_number = db.Column(db.String(50))
    # ISO 3166-1 alpha-2 of the operator whose marks the airframe wears, not
    # the country it sits in today. Part of uq_airframe.
    operator_country = db.Column(db.String(2))
    # MySQL-side STORED generated column (see schema.sql). Declared via Computed
    # so SQLAlchemy excludes it from INSERT/UPDATE but lets queries reference it
    # in filters — letting searches hit idx_full_desig instead of computing
    # CONCAT(...) on every row.
    full_designation = db.Column(
        db.String(100),
        Computed(_FULL_DESIGNATION_SQL, persisted=True),
    )
    aircraft_type = db.Column(db.String(20), nullable=False, default="fixed_wing")
    wing_type = db.Column(db.String(20))          # monoplane, biplane, triplane
    military_civilian = db.Column(db.String(10), nullable=False, default="military")
    role_type = db.Column(db.String(30))             # bomber, transport, fighter, etc.
    year_built = db.Column(db.Integer)
    description = db.Column(db.Text)

    # See note on Museum.aircraft_links — same reason. Without these, deleting
    # an Aircraft that's listed at any museum raises IntegrityError because
    # SQLAlchemy tries to UPDATE aircraft_museum.aircraft_id = NULL.
    museum_links = db.relationship(
        "AircraftMuseum",
        back_populates="aircraft",
        lazy="dynamic",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    aliases = db.relationship("AircraftAlias", back_populates="aircraft", cascade="all, delete-orphan", lazy="joined")

    # Note: full_designation is declared above as a generated column. Loaded
    # instances have it populated by the database; unflushed new instances see
    # None, which is acceptable since callers serialize only after commit.

    def to_dict(self):
        return {
            "id": self.id,
            "tail_number": self.tail_number,
            "model_name": self.model_name,
            "aircraft_name": self.aircraft_name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "variant": self.variant,
            "construction_number": self.construction_number,
            "operator_country": self.operator_country,
            # Fall back to in-Python computation for unflushed instances where
            # the DB-generated value hasn't been loaded yet.
            "full_designation": self.full_designation or join_designation(
                self.model, self.variant
            ),
            "aircraft_type": self.aircraft_type,
            "wing_type": self.wing_type,
            "military_civilian": self.military_civilian,
            "role_type": self.role_type,
            "year_built": self.year_built,
            "description": self.description,
            "aliases": [a.alias for a in self.aliases],
        }


class AircraftAlias(db.Model):
    __tablename__ = "aircraft_aliases"

    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id", ondelete="CASCADE"), nullable=False)
    alias = db.Column(db.String(200), nullable=False)

    aircraft = db.relationship("Aircraft", back_populates="aliases")


class AircraftMuseum(db.Model):
    __tablename__ = "aircraft_museum"

    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id", ondelete="CASCADE"), nullable=False)
    museum_id = db.Column(db.Integer, db.ForeignKey("museums.id", ondelete="CASCADE"), nullable=False)
    display_status = db.Column(db.String(20), default="on_display")
    notes = db.Column(db.Text)

    aircraft = db.relationship("Aircraft", back_populates="museum_links")
    museum = db.relationship("Museum", back_populates="aircraft_links")

    def to_dict(self):
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "museum_id": self.museum_id,
            "display_status": self.display_status,
            "notes": self.notes,
            "aircraft": self.aircraft.to_dict(),
            "museum": self.museum.to_dict(),
        }


class AircraftTemplate(db.Model):
    """Reusable 'type info' record. An admin picks one when creating a new
    Aircraft to pre-fill the type-level fields; per-airframe fields
    (tail_number, aircraft_name, year_built) are never on the template.
    """
    __tablename__ = "aircraft_templates"

    id = db.Column(db.Integer, primary_key=True)
    # Short label shown in the picker, e.g. "C-130H Hercules".
    name = db.Column(db.String(200), nullable=False, unique=True)
    manufacturer = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    variant = db.Column(db.String(50))
    model_name = db.Column(db.String(200))
    aircraft_type = db.Column(db.String(20), nullable=False, default="fixed_wing")
    wing_type = db.Column(db.String(20))
    military_civilian = db.Column(db.String(10), nullable=False, default="military")
    role_type = db.Column(db.String(30))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    aliases = db.relationship(
        "AircraftTemplateAlias",
        back_populates="template",
        cascade="all, delete-orphan",
        lazy="joined",
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "variant": self.variant,
            "model_name": self.model_name,
            "aircraft_type": self.aircraft_type,
            "wing_type": self.wing_type,
            "military_civilian": self.military_civilian,
            "role_type": self.role_type,
            "description": self.description,
            "aliases": [a.alias for a in self.aliases],
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class AircraftTemplateAlias(db.Model):
    __tablename__ = "aircraft_template_aliases"

    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey("aircraft_templates.id", ondelete="CASCADE"), nullable=False)
    alias = db.Column(db.String(200), nullable=False)

    template = db.relationship("AircraftTemplate", back_populates="aliases")


# ──────────────────────────────────────────────
# Aircraft types (shared, inherited type information)
# ──────────────────────────────────────────────

# Everything that isn't a letter or a digit is noise for matching purposes:
# sources write "MiG-21", "MIG 21" and "Mig21" for the same aeroplane.
_TYPE_KEY_NOISE = re.compile(r"[^A-Z0-9]+")


def type_match_key(model, variant=None):
    """Normalized join key used to attach an Aircraft to an AircraftType.

    Deliberately NOT manufacturer-scoped. A licence-built airframe is still
    the same type: Fuji built 89 of the UH-1s in this database, Kawasaki 36
    of the T-33s, HAL 38 of the MiG-21s, and all of them want the Bell /
    Lockheed / Mikoyan-Gurevich write-up. 791 of 4,877 designations in the
    collection carry more than one manufacturer spelling, so putting
    manufacturer in the key would fragment the very thing this table exists
    to share.

    Punctuation and case are dropped, so ("F-4", "C") and ("F-4C", None)
    both produce "F4C" — which is correct, they are the same aircraft, and
    the importer has recorded it both ways.

    Returns None for an empty model, which callers treat as "no match".
    """
    joined = f"{(model or '').strip()}{(variant or '').strip()}".upper()
    return _TYPE_KEY_NOISE.sub("", joined) or None


def manufacturer_matches(scope, manufacturer):
    """Does an airframe's manufacturer satisfy a type's manufacturer_scope?

    Deliberately loose at the edges: the same company is written several ways
    in this collection ("Bell" / "Bell Helicopter", "North American" /
    "North American Aviation"), so a scope matches when either normalized
    string starts with the other. That admits "Bell Helicopter" for scope
    "Bell" while still refusing "Pitts" for scope "Grumman", which is the
    only distinction this guard exists to make.

    An empty scope matches everything -- that is the unscoped default. An
    empty manufacturer against a non-empty scope does NOT match: an airframe
    with no recorded builder cannot be shown to be the right one.
    """
    scope_key = _TYPE_KEY_NOISE.sub("", (scope or "").upper())
    if not scope_key:
        return True
    mfr_key = _TYPE_KEY_NOISE.sub("", (manufacturer or "").upper())
    if not mfr_key:
        return False
    return mfr_key.startswith(scope_key) or scope_key.startswith(mfr_key)


class AircraftType(db.Model):
    """Type-level information shared by every airframe of a designation.

    This is the answer to "what IS a T-33A", written once and inherited by
    all 372 of them, as opposed to Aircraft.description which is the answer
    to "what is the story of THIS airframe" and stays per-record.

    Resolution is two-tier and happens at render time rather than through a
    foreign key on Aircraft (see resolve_for()): an exact model+variant type
    wins, and a base model-only type catches everything else. That means a
    newly imported F-104G inherits the F-104 write-up the moment it lands,
    with no backfill step and nothing to drift out of sync.
    """
    __tablename__ = "aircraft_types"

    id = db.Column(db.Integer, primary_key=True)

    # The designation this type describes. variant NULL = the base type,
    # which is the fallback for every variant without its own record.
    model = db.Column(db.String(50), nullable=False)
    variant = db.Column(db.String(50))
    # Normalized model+variant. Maintained by the application (not a
    # generated column) because the test suite runs on SQLite and the
    # normalization is easier to read in Python. Unique: one write-up per
    # designation.
    match_key = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), nullable=False, unique=True)
    # Normally NULL, and normally that is right: a designation identifies a
    # type regardless of who bent the metal, which is what lets a Fuji UH-1H
    # inherit Bell's write-up. But a few designation STRINGS are reused by
    # unrelated aircraft -- "S-2" is 52 Grumman Trackers, 10 Pitts biplanes
    # and 3 Ayres cropdusters; "47", "737" and "T-38" have the same problem.
    # Setting this restricts the type to airframes whose manufacturer
    # matches, and a scoped type NEVER applies to an airframe it does not
    # match. See manufacturer_matches().
    #
    # Empty string, not NULL, is "unscoped". That is not fussiness: the
    # uniqueness rule is (match_key, manufacturer_scope), and MySQL counts
    # every NULL as distinct in a UNIQUE index -- so a nullable column would
    # happily accept two unscoped F-104 write-ups and leave the page picking
    # between them arbitrarily, which is the one thing this table must never
    # do. With '' the key bites: one unscoped record per designation, plus
    # one per distinct scope, so a Grumman S-2 and a Pitts S-2 can coexist.
    manufacturer_scope = db.Column(db.String(100), nullable=False, default="",
                                   server_default="")

    __table_args__ = (
        db.UniqueConstraint("match_key", "manufacturer_scope",
                            name="uq_type_match"),
    )

    # Alternate designations that reach this same write-up. See
    # AircraftTypeAlias -- the T-6 record answers to AT-6 and SNJ through
    # these, without 45 near-duplicate write-ups existing to say so.
    aliases = db.relationship("AircraftTypeAlias", back_populates="aircraft_type_record",
                              cascade="all, delete-orphan", lazy="selectin")

    # Display metadata. manufacturer here is the ORIGINAL designer, shown as
    # provenance; an individual airframe keeps its own builder, so a Fuji
    # UH-1H still reads "Fuji" in its own spec table.
    display_name = db.Column(db.String(200), nullable=False)   # "Lockheed T-33A Shooting Star"
    manufacturer = db.Column(db.String(100))
    model_name = db.Column(db.String(200))                     # "Shooting Star"
    also_built_by = db.Column(db.String(300))                  # "Kawasaki, Canadair"
    origin_country = db.Column(db.String(2))                   # ISO 3166-1 alpha-2

    description = db.Column(db.Text, nullable=False)

    aircraft_type = db.Column(db.String(20), nullable=False, default="fixed_wing")
    role_type = db.Column(db.String(30))
    wing_type = db.Column(db.String(20))
    military_civilian = db.Column(db.String(10), nullable=False, default="military")

    first_flight_year = db.Column(db.Integer)
    introduced_year = db.Column(db.Integer)
    retired_year = db.Column(db.Integer)
    number_built = db.Column(db.Integer)
    # Which variant the figures below describe. A base type covers every
    # variant but its numbers cannot: a T-33A and a T-33SF are not the
    # same aeroplane on paper. Naming the basis is the honest way to
    # publish one spec block for a whole family.
    spec_basis = db.Column(db.String(100))
    crew = db.Column(db.String(60))
    engines = db.Column(db.String(200))
    length_m = db.Column(db.Numeric(6, 2))
    wingspan_m = db.Column(db.Numeric(6, 2))
    height_m = db.Column(db.Numeric(6, 2))
    max_speed_kmh = db.Column(db.Integer)
    range_km = db.Column(db.Integer)
    ceiling_m = db.Column(db.Integer)

    source_name = db.Column(db.String(300))
    source_url = db.Column(db.String(1000))
    wikipedia_url = db.Column(db.String(1000))

    # Unpublished types are editable in admin but never reach a public page.
    is_published = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    @property
    def designation(self):
        """The designation as aviation writes it — same rule as Aircraft."""
        return join_designation(self.model, self.variant)

    @property
    def is_base_type(self):
        return not (self.variant or "").strip()

    def sync_key(self):
        """Recompute match_key from model/variant, and normalize the scope.

        Both halves of the uniqueness rule are set here so no caller can
        leave a NULL scope behind and quietly defeat the unique key.
        """
        self.match_key = type_match_key(self.model, self.variant)
        self.manufacturer_scope = (self.manufacturer_scope or "").strip()
        return self.match_key

    @classmethod
    def resolve_for(cls, model, variant=None, manufacturer=None, published_only=True):
        """Return the best type for a designation, or None.

        Priority, highest first:
          1. exact model+variant, scoped to this manufacturer
          2. exact model+variant, unscoped
          3. exact model+variant reached through an ALIAS (scoped, then not)
          4. base model, scoped to this manufacturer
          5. base model, unscoped
          6. base model reached through an ALIAS (scoped, then not)

        Two rules shape that order. A more specific designation always
        beats a less specific one, because an F-104G write-up is a better
        answer than the F-104 one. And at the same specificity a real
        record beats an alias, so writing an actual "Su-17" type later
        quietly supersedes the alias pointing Su-17 at the Su-22 without
        anyone having to delete it.

        A type whose manufacturer_scope does not match is excluded outright
        rather than demoted -- that is the whole point of scoping it, and
        without the exclusion a Pitts S-2 would still fall through to the
        Grumman write-up. An alias carries its own scope for the same
        reason (alias "204" means a Bell, not any airframe spelled 204),
        AND the type it points at must still admit the manufacturer: an
        alias is a second door into a type, never a way around its scope.

        Two indexed IN() queries over at most two keys each, so the page
        still costs a pair of cheap lookups.
        """
        best = cls._resolve_candidates(model, variant, manufacturer,
                                       published_only)
        if not best:
            return None
        return min(best, key=lambda triple: triple[0])[1]

    @classmethod
    def _resolve_candidates(cls, model, variant=None, manufacturer=None,
                            published_only=True):
        """Every type that could answer for this designation, as
        (rank, type, alias_or_None). Shared by resolve_for() and
        resolve_detail_for() so the ranking rule lives in exactly one
        place."""
        keys = []
        exact = type_match_key(model, variant)
        base = type_match_key(model, None)
        if exact:
            keys.append(exact)
        if base and base not in keys:
            keys.append(base)
        if not keys:
            return []

        q = cls.query.filter(cls.match_key.in_(keys))
        if published_only:
            q = q.filter(cls.is_published.is_(True))

        # (key position, alias?, unscoped?) -- lower sorts better.
        candidates = []
        for t in q.all():
            if not manufacturer_matches(t.manufacturer_scope, manufacturer):
                continue
            candidates.append(((keys.index(t.match_key), 0,
                                0 if t.manufacturer_scope else 1), t, None))

        aq = (AircraftTypeAlias.query
              .filter(AircraftTypeAlias.match_key.in_(keys))
              .join(cls, AircraftTypeAlias.type_id == cls.id))
        if published_only:
            aq = aq.filter(cls.is_published.is_(True))
        for a in aq.all():
            if not manufacturer_matches(a.manufacturer_scope, manufacturer):
                continue
            target = a.aircraft_type_record
            if target is None:
                continue
            if not manufacturer_matches(target.manufacturer_scope, manufacturer):
                continue
            candidates.append(((keys.index(a.match_key), 1,
                                0 if a.manufacturer_scope else 1), target, a))

        return candidates

    @classmethod
    def resolve_detail_for(cls, model, variant=None, manufacturer=None,
                           published_only=True):
        """resolve_for, plus HOW it matched: (type, alias_or_None).

        The admin preview and the API's /resolve need to say "this landed
        on the T-6 write-up *through the AT-6 alias*", which is the one
        thing a bare type object cannot tell you -- and the thing an editor
        most needs to see before trusting the match.
        """
        best = cls._resolve_candidates(model, variant, manufacturer,
                                       published_only)
        if not best:
            return None, None
        _rank, t, alias = min(best, key=lambda triple: triple[0])
        return t, alias

    def to_dict(self):
        def _num(v):
            return float(v) if v is not None else None
        return {
            "id": self.id,
            "slug": self.slug,
            "model": self.model,
            "variant": self.variant,
            "designation": self.designation,
            "match_key": self.match_key,
            "is_base_type": self.is_base_type,
            "manufacturer_scope": self.manufacturer_scope or None,
            "aliases": [a.to_dict() for a in sorted(self.aliases, key=lambda a: a.designation)],
            "display_name": self.display_name,
            "manufacturer": self.manufacturer,
            "model_name": self.model_name,
            "also_built_by": self.also_built_by,
            "origin_country": self.origin_country,
            "description": self.description,
            "aircraft_type": self.aircraft_type,
            "role_type": self.role_type,
            "wing_type": self.wing_type,
            "military_civilian": self.military_civilian,
            "first_flight_year": self.first_flight_year,
            "introduced_year": self.introduced_year,
            "retired_year": self.retired_year,
            "number_built": self.number_built,
            "spec_basis": self.spec_basis,
            "crew": self.crew,
            "engines": self.engines,
            "length_m": _num(self.length_m),
            "wingspan_m": _num(self.wingspan_m),
            "height_m": _num(self.height_m),
            "max_speed_kmh": self.max_speed_kmh,
            "range_km": self.range_km,
            "ceiling_m": self.ceiling_m,
            "source_name": self.source_name,
            "source_url": self.source_url,
            "wikipedia_url": self.wikipedia_url,
            "is_published": bool(self.is_published),
        }



class AircraftTypeAlias(db.Model):
    """An alternate designation that resolves to an existing AircraftType.

    The same aeroplane is catalogued under several names, and the catalogue
    records whichever one is painted on the airframe: 129 Texans are "T-6",
    but the Navy's are "SNJ" and the trainer command's are "AT-6"; a
    Canadair-built F-104 is a "CF-104"; a licence-built MiG-15 in Poland is
    a "Lim-2". Those are not different aircraft, so they should not want
    different write-ups -- but they are different designation STRINGS, so
    match_key cannot see through them.

    An alias is simply a second match_key pointing at a type. It changes no
    aircraft record and adds no text; it widens what one write-up answers
    to. That is far cheaper than the alternative: 45 aliases reach ~850
    airframes that 45 newly researched type records would otherwise have to
    cover one by one.

    It carries its own manufacturer_scope for the same reason a type does.
    Alias "204" for the Bell UH-1 is a bare number that would otherwise
    match any airframe spelled 204, so it is scoped to Bell; the alias is
    excluded outright for anyone else rather than demoted.
    """

    __tablename__ = "aircraft_type_aliases"

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("aircraft_types.id", ondelete="CASCADE"),
                        nullable=False)

    # The alternate designation as written ("AT-6", "CF-104", "Lim-2").
    # Stored whole rather than split into model/variant: an alias only ever
    # needs to produce a match_key, and the split would be a second place
    # for the join rule to drift from Aircraft's.
    designation = db.Column(db.String(100), nullable=False)
    match_key = db.Column(db.String(120), nullable=False)
    # '' not NULL, for the same reason as AircraftType.manufacturer_scope:
    # MySQL counts NULLs as distinct in a UNIQUE index, which would let two
    # unscoped aliases for one designation point at two different types and
    # leave the page choosing arbitrarily.
    manufacturer_scope = db.Column(db.String(100), nullable=False, default="",
                                   server_default="")

    aircraft_type_record = db.relationship("AircraftType", back_populates="aliases")

    __table_args__ = (
        db.UniqueConstraint("match_key", "manufacturer_scope",
                            name="uq_type_alias_match"),
    )

    def sync_key(self):
        self.designation = (self.designation or "").strip()
        self.match_key = type_match_key(self.designation)
        self.manufacturer_scope = (self.manufacturer_scope or "").strip()
        return self.match_key

    def to_dict(self):
        return {
            "id": self.id,
            "designation": self.designation,
            "match_key": self.match_key,
            "manufacturer_scope": self.manufacturer_scope or None,
        }


class AircraftFact(db.Model):
    """A piece of aviation trivia, optionally tied to a specific aircraft.

    ``aircraft_id`` is nullable on purpose. Most facts are general ("the
    SR-71 leaked fuel on the ground until friction heat sealed the tanks"),
    but one attached to an airframe can also surface on that aircraft's
    detail page. ON DELETE SET NULL rather than CASCADE: deleting an
    aircraft record shouldn't silently destroy the writing about it.
    """

    __tablename__ = "aircraft_facts"

    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.Text, nullable=False)
    source_url = db.Column(db.String(500))
    aircraft_id = db.Column(
        db.Integer,
        db.ForeignKey("aircraft.id", ondelete="SET NULL"),
        nullable=True,
    )
    # Hide a fact without deleting it — useful when something is disputed
    # but you don't want to lose the text.
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    aircraft = db.relationship("Aircraft", backref="facts")

    def to_dict(self):
        return {
            "id": self.id,
            "fact": self.fact,
            "source_url": self.source_url,
            "aircraft_id": self.aircraft_id,
            "aircraft": self.aircraft.to_dict() if self.aircraft else None,
            "is_active": bool(self.is_active),
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class AircraftHistoryEvent(db.Model):
    """Sourced milestones tied to a stable airframe ID, independent of its registration."""
    __tablename__ = "aircraft_history_events"

    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type = db.Column(db.String(30), nullable=False, default="other")
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    event_year = db.Column(db.Integer)
    event_month = db.Column(db.Integer)
    event_day = db.Column(db.Integer)
    is_approximate = db.Column(db.Boolean, nullable=False, default=False)
    operator = db.Column(db.String(200))
    location = db.Column(db.String(200))
    registration = db.Column(db.String(80))
    source_name = db.Column(db.String(300))
    source_url = db.Column(db.String(1000))
    is_published = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="SET NULL"))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        fields = ("id", "aircraft_id", "event_type", "title", "description", "event_year",
                  "event_month", "event_day", "is_approximate", "operator", "location",
                  "registration", "source_name", "source_url", "is_published")
        result = {field: getattr(self, field) for field in fields}
        result["updated_at"] = self.updated_at.isoformat() if self.updated_at else None
        return result


class ZipCode(db.Model):
    __tablename__ = "zip_codes"

    zip_code = db.Column(db.String(20), primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False, default="United States")
    latitude = db.Column(db.Numeric(10, 7), nullable=False)
    longitude = db.Column(db.Numeric(10, 7), nullable=False)


def haversine(lat1, lon1, lat2, lon2):
    """Calculate distance in miles between two lat/lon points."""
    R = 3958.8  # Earth radius in miles
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))
