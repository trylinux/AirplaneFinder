"""Geocoding helper — resolves zip/postal codes and city names to (lat, lon).

Uses a layered approach:
  1. Database cache (zip_codes table) — instant, no network
  2. pgeocode — offline postal code data for 80+ countries
  3. geopy/Nominatim — online fallback for city names and addresses

Successful lookups from layers 2-3 are cached in the database for
future use so the same query never hits external services twice.
"""

import math
import logging

log = logging.getLogger(__name__)

# ── Lazy-load optional libraries ──────────────────────────────

_pgeocode_nominatims = {}  # country_code → pgeocode.Nominatim instance

def _pgeocode_lookup(postal_code, country_hint="us"):
    """Look up a postal code using pgeocode (offline data).

    Returns (lat, lon) or (None, None).
    """
    try:
        import pgeocode  # noqa: delayed import
    except ImportError:
        return None, None

    country_hint = country_hint.lower()
    if country_hint not in _pgeocode_nominatims:
        try:
            _pgeocode_nominatims[country_hint] = pgeocode.Nominatim(country_hint)
        except Exception:
            return None, None

    nomi = _pgeocode_nominatims[country_hint]
    try:
        result = nomi.query_postal_code(postal_code)
        if result is not None and not math.isnan(result.latitude):
            return float(result.latitude), float(result.longitude)
    except Exception as exc:
        log.debug("pgeocode error for %s/%s: %s", postal_code, country_hint, exc)

    return None, None


def _geopy_lookup(query_str):
    """Geocode a free-form string using geopy + OpenStreetMap Nominatim.

    Returns (lat, lon) or (None, None).
    """
    try:
        from geopy.geocoders import Nominatim as GeopyNominatim  # noqa: delayed import
    except ImportError:
        return None, None

    try:
        geolocator = GeopyNominatim(user_agent="aircraft-finder", timeout=5)
        location = geolocator.geocode(query_str)
        if location:
            return float(location.latitude), float(location.longitude)
    except Exception as exc:
        log.debug("geopy error for %r: %s", query_str, exc)

    return None, None


# ── Country code mapping (common names → ISO 2-letter) ───────

_COUNTRY_CODES = {
    "united states": "us", "usa": "us", "us": "us",
    "canada": "ca",
    "united kingdom": "gb", "uk": "gb",
    "germany": "de", "deutschland": "de",
    "france": "fr",
    "japan": "jp",
    "australia": "au",
    "italy": "it", "italia": "it",
    "spain": "es", "espana": "es",
    "netherlands": "nl",
    "belgium": "be",
    "austria": "at",
    "switzerland": "ch",
    "sweden": "se",
    "norway": "no",
    "denmark": "dk",
    "finland": "fi",
    "poland": "pl",
    "czech republic": "cz", "czechia": "cz",
    "portugal": "pt",
    "brazil": "br",
    "mexico": "mx",
    "india": "in",
    "china": "cn",
    "south korea": "kr", "korea": "kr",
    "new zealand": "nz",
    "ireland": "ie",
    "israel": "il",
    "turkey": "tr",
    "south africa": "za",
    "argentina": "ar",
    "russia": "ru",
    "singapore": "sg",
    "thailand": "th",
    "philippines": "ph",
    "taiwan": "tw",
    "greece": "gr",
    "romania": "ro",
    "hungary": "hu",
    "croatia": "hr",
}


def _guess_country_code(location_str):
    """Try to guess the ISO country code from the input.

    Returns a two-letter code (default "us").
    """
    lower = location_str.lower()
    for name, code in _COUNTRY_CODES.items():
        if name in lower:
            return code
    return "us"


# ── Main resolver ─────────────────────────────────────────────

def resolve_location(location_str, db=None, ZipCode=None):
    """Resolve a location string to (lat, lon).

    Tries in order:
      1. Database cache
      2. pgeocode (offline postal codes)
      3. geopy Nominatim (online, free-form)

    Caches successful results from 2-3 back into the database.

    Args:
        location_str: zip code, postal code, city name, or "city, state" format
        db: SQLAlchemy db instance (for caching)
        ZipCode: the ZipCode model class (for cache reads/writes)

    Returns:
        (lat, lon) tuple of floats, or (None, None) if unresolvable.
    """
    location_str = location_str.strip()
    if not location_str:
        return None, None

    # ── Layer 1: Database cache ──

    if ZipCode is not None:
        # Exact postal code match
        z = ZipCode.query.get(location_str)
        if z:
            return float(z.latitude), float(z.longitude)

        # City name match
        z = ZipCode.query.filter(ZipCode.city.ilike(location_str)).first()
        if z:
            return float(z.latitude), float(z.longitude)

        # "city, state/country" format
        if "," in location_str:
            from sqlalchemy import or_
            parts = [p.strip() for p in location_str.split(",")]
            z = ZipCode.query.filter(
                ZipCode.city.ilike(parts[0]),
                or_(
                    ZipCode.state.ilike(f"%{parts[1]}%"),
                    ZipCode.country.ilike(f"%{parts[1]}%"),
                )
            ).first()
            if z:
                return float(z.latitude), float(z.longitude)

    # ── Layer 2: pgeocode (offline postal codes) ──

    country_code = _guess_country_code(location_str)

    # Extract the postal code portion (handle "city, state ZIP" patterns)
    postal_candidate = location_str.split(",")[0].strip() if "," not in location_str else location_str.split()[-1].strip()

    # For pure numeric input, assume postal code
    clean_input = location_str.replace(" ", "").replace("-", "")
    is_likely_postal = (
        clean_input.isdigit() or                       # US: 92591
        (len(clean_input) <= 10 and clean_input.isalnum())  # UK: SW1A1AA, CA: K1A0M8
    )

    if is_likely_postal:
        # Try the raw input as a postal code
        lat, lon = _pgeocode_lookup(location_str, country_code)
        if lat is not None:
            _cache_result(location_str, lat, lon, country_code, db, ZipCode)
            return lat, lon

        # Also try common country codes if US didn't match
        if country_code == "us":
            for alt_code in ["ca", "gb", "de", "fr", "au", "jp"]:
                lat, lon = _pgeocode_lookup(location_str, alt_code)
                if lat is not None:
                    _cache_result(location_str, lat, lon, alt_code, db, ZipCode)
                    return lat, lon

    # ── Layer 3: geopy Nominatim (online, free-form) ──

    lat, lon = _geopy_lookup(location_str)
    if lat is not None:
        _cache_result(location_str, lat, lon, country_code, db, ZipCode)
        return lat, lon

    return None, None


def _cache_result(key, lat, lon, country_code, db, ZipCode):
    """Cache a geocoding result in the zip_codes table."""
    if db is None or ZipCode is None:
        return
    try:
        # Don't overwrite existing entries
        existing = ZipCode.query.get(key)
        if existing:
            return
        country_name = {v: k for k, v in _COUNTRY_CODES.items()}.get(country_code, country_code).title()
        entry = ZipCode(
            zip_code=key,
            city=key,  # best guess; will be refined on future queries
            state="",
            country=country_name,
            latitude=lat,
            longitude=lon,
        )
        db.session.add(entry)
        db.session.commit()
    except Exception:
        db.session.rollback()  # don't let cache failures break the request
