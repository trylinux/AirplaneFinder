"""SQLAlchemy models."""

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
    role = db.Column(db.String(20), nullable=False, default="viewer")  # admin, manager, viewer
    is_active_user = db.Column("is_active", db.Boolean, default=True)
    last_login = db.Column(db.DateTime, nullable=True)
    last_login_ip = db.Column(db.String(45), nullable=True)     # IPv4 or IPv6
    last_logout = db.Column(db.DateTime, nullable=True)
    contribution_count = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Default lazy loading; the only site that walks user.api_keys is
    # User.to_dict. Everywhere else queries ApiKey directly via its own model.
    api_keys = db.relationship("ApiKey", back_populates="user")
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
        return self.role == "admin"

    @property
    def is_manager(self):
        return self.role in ("admin", "manager")

    def assigned_museum_ids(self):
        """Return set of museum IDs this user is assigned to."""
        return {a.museum_id for a in self.museum_assignments}

    def assigned_countries(self):
        """Return set of country names this user is assigned to."""
        return {a.country for a in self.country_assignments}

    def can_access_museum(self, museum):
        """Check if user can access a specific museum (admin=all, others=assigned)."""
        if self.is_admin:
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
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    museum_id = db.Column(db.Integer, db.ForeignKey("museums.id"), nullable=False)

    user = db.relationship("User", back_populates="museum_assignments")
    museum = db.relationship("Museum")


class UserCountryAssignment(db.Model):
    __tablename__ = "user_country_assignments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    user = db.relationship("User", back_populates="country_assignments")


class ApiKey(db.Model):
    __tablename__ = "api_keys"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
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
    latitude = db.Column(db.Numeric(10, 7))               # nullable
    longitude = db.Column(db.Numeric(10, 7))              # nullable

    aircraft_links = db.relationship("AircraftMuseum", back_populates="museum", lazy="dynamic")

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
            "latitude": float(self.latitude) if self.latitude is not None else None,
            "longitude": float(self.longitude) if self.longitude is not None else None,
        }


class Aircraft(db.Model):
    __tablename__ = "aircraft"

    id = db.Column(db.Integer, primary_key=True)
    tail_number = db.Column(db.String(20))
    model_name = db.Column(db.String(200))       # type common name: "Cobra", "Hercules"
    aircraft_name = db.Column(db.String(200))     # individual name: "Daisy Duke", "Bockscar"
    manufacturer = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    variant = db.Column(db.String(50))
    # MySQL-side STORED generated column (see schema.sql). Declared via Computed
    # so SQLAlchemy excludes it from INSERT/UPDATE but lets queries reference it
    # in filters — letting searches hit idx_full_desig instead of computing
    # CONCAT(...) on every row.
    full_designation = db.Column(
        db.String(100),
        Computed("CONCAT(model, IFNULL(CONCAT('-', variant), ''))", persisted=True),
    )
    aircraft_type = db.Column(db.String(20), nullable=False, default="fixed_wing")
    wing_type = db.Column(db.String(20))          # monoplane, biplane, triplane
    military_civilian = db.Column(db.String(10), nullable=False, default="military")
    role_type = db.Column(db.String(30))             # bomber, transport, fighter, etc.
    year_built = db.Column(db.Integer)
    description = db.Column(db.Text)

    museum_links = db.relationship("AircraftMuseum", back_populates="aircraft", lazy="dynamic")
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
            # Fall back to in-Python computation for unflushed instances where
            # the DB-generated value hasn't been loaded yet.
            "full_designation": self.full_designation or (
                f"{self.model}-{self.variant}" if self.variant else (self.model or "")
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
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id"), nullable=False)
    alias = db.Column(db.String(200), nullable=False)

    aircraft = db.relationship("Aircraft", back_populates="aliases")


class AircraftMuseum(db.Model):
    __tablename__ = "aircraft_museum"

    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id"), nullable=False)
    museum_id = db.Column(db.Integer, db.ForeignKey("museums.id"), nullable=False)
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
    template_id = db.Column(db.Integer, db.ForeignKey("aircraft_templates.id"), nullable=False)
    alias = db.Column(db.String(200), nullable=False)

    template = db.relationship("AircraftTemplate", back_populates="aliases")


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
