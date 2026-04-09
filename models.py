"""SQLAlchemy models."""

import secrets
import hashlib
from math import radians, sin, cos, sqrt, atan2

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
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
    is_admin = db.Column(db.Boolean, default=False)
    is_active_user = db.Column("is_active", db.Boolean, default=True)

    api_keys = db.relationship("ApiKey", back_populates="user", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_active(self):
        return self.is_active_user

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin,
        }


class ApiKey(db.Model):
    __tablename__ = "api_keys"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    key_hash = db.Column(db.String(256), nullable=False)
    label = db.Column(db.String(100), default="default")
    is_active = db.Column(db.Boolean, default=True)
    permissions = db.Column(db.String(50), default="read")  # read, readwrite, admin
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    last_used = db.Column(db.DateTime, nullable=True)

    user = db.relationship("User", back_populates="api_keys")

    @staticmethod
    def hash_key(raw_key):
        return hashlib.sha256(raw_key.encode()).hexdigest()

    @classmethod
    def generate(cls, user_id, label="default", permissions="read"):
        """Create a new API key; returns (ApiKey object, raw_key)."""
        raw_key = "amt_" + secrets.token_hex(24)  # 48-char hex + prefix
        obj = cls(
            user_id=user_id,
            key_hash=cls.hash_key(raw_key),
            label=label,
            permissions=permissions,
        )
        return obj, raw_key

    @classmethod
    def lookup(cls, raw_key):
        """Find an active ApiKey by raw key string."""
        h = cls.hash_key(raw_key)
        return cls.query.filter_by(key_hash=h, is_active=True).first()

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "label": self.label,
            "permissions": self.permissions,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
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
    aircraft_type = db.Column(db.String(20), nullable=False, default="fixed_wing")
    wing_type = db.Column(db.String(20))          # monoplane, biplane, triplane
    military_civilian = db.Column(db.String(10), nullable=False, default="military")
    role_type = db.Column(db.String(30))             # bomber, transport, fighter, etc.
    year_built = db.Column(db.Integer)
    description = db.Column(db.Text)

    museum_links = db.relationship("AircraftMuseum", back_populates="aircraft", lazy="dynamic")
    aliases = db.relationship("AircraftAlias", back_populates="aircraft", cascade="all, delete-orphan", lazy="joined")

    @property
    def full_designation(self):
        """Compute designation in Python — mirrors the MySQL generated column."""
        if self.variant:
            return f"{self.model}-{self.variant}"
        return self.model or ""

    def to_dict(self):
        return {
            "id": self.id,
            "tail_number": self.tail_number,
            "model_name": self.model_name,
            "aircraft_name": self.aircraft_name,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "variant": self.variant,
            "full_designation": self.full_designation,
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
