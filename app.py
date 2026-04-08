"""Flask application – Aircraft Museum Tracker.

Features:
  - Flask-Login session auth for the web admin panel
  - Bearer-token (API key) auth for the JSON REST API
  - Full CRUD on aircraft, museums, and exhibit links
  - Public read-only search + proximity endpoints
  - International museum support (optional coordinates)
"""

from datetime import datetime, timezone
from functools import wraps

from flask import (
    Flask, render_template, request, jsonify,
    redirect, url_for, flash, abort,
)
from flask_login import (
    LoginManager, login_user, logout_user,
    login_required, current_user,
)
from sqlalchemy import or_, func

from models import (
    db, User, ApiKey,
    Museum, Aircraft, AircraftAlias, AircraftMuseum, ZipCode, haversine,
)
from geocoder import resolve_location
from config import Config


# ══════════════════════════════════════════════
# App factory
# ══════════════════════════════════════════════

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "login_page"
    login_manager.login_message_category = "warning"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


app = create_app()


# ══════════════════════════════════════════════
# API-key authentication decorator
# ══════════════════════════════════════════════

def _get_api_user():
    """Return (User, ApiKey) from the Authorization header, or (None, None)."""
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        raw_key = auth[7:].strip()
        api_key = ApiKey.lookup(raw_key)
        if api_key:
            api_key.last_used = datetime.now(timezone.utc)
            db.session.commit()
            return api_key.user, api_key
    return None, None


def api_auth_required(min_permission="read"):
    """Decorator: require a valid API key with at least *min_permission*.

    Permission levels: read < readwrite < admin
    Also accepts a logged-in web session as a fallback.
    """
    levels = {"read": 0, "readwrite": 1, "admin": 2}

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user, api_key = _get_api_user()

            # Fallback: logged-in web session counts as admin
            if user is None and current_user.is_authenticated:
                user = current_user
                perm_level = 2  # web sessions are admin
            elif api_key:
                perm_level = levels.get(api_key.permissions, 0)
            else:
                return jsonify({"error": "Authentication required. Supply 'Authorization: Bearer <api_key>' header."}), 401

            if perm_level < levels.get(min_permission, 0):
                return jsonify({"error": f"Insufficient permissions. Requires '{min_permission}'."}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator


# ══════════════════════════════════════════════
# Web page routes (public)
# ══════════════════════════════════════════════

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/aircraft")
def aircraft_page():
    return render_template("aircraft.html")


@app.route("/museums")
def museums_page():
    return render_template("museums.html")


# ══════════════════════════════════════════════
# Auth: login / logout / register
# ══════════════════════════════════════════════

@app.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("admin_page"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password) and user.is_active:
            login_user(user, remember=True)
            next_url = request.args.get("next") or url_for("admin_page")
            return redirect(next_url)

        flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("admin_page"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip() or None
        password = request.form.get("password", "")
        password2 = request.form.get("password2", "")

        if not username or not password:
            flash("Username and password are required.", "error")
        elif password != password2:
            flash("Passwords do not match.", "error")
        elif User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
        else:
            # First user is automatically admin
            is_first = User.query.count() == 0
            user = User(username=username, email=email, is_admin=is_first)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Account created!" + (" You are the first user, so you have admin rights." if is_first else ""), "success")
            return redirect(url_for("admin_page"))

    return render_template("register.html")


# ══════════════════════════════════════════════
# Admin panel (session-protected)
# ══════════════════════════════════════════════

@app.route("/admin")
@login_required
def admin_page():
    return render_template("admin.html")


@app.route("/admin/api-keys")
@login_required
def api_keys_page():
    return render_template("api_keys.html")


# ══════════════════════════════════════════════
# API: Public read-only (no auth needed)
# ══════════════════════════════════════════════

def _build_aircraft_filter(q):
    """Build an OR filter that matches aircraft by model, name, tail, manufacturer, or alias."""
    like = f"%{q}%"
    # Subquery: aircraft IDs that match via aliases
    alias_ids = db.session.query(AircraftAlias.aircraft_id).filter(
        AircraftAlias.alias.ilike(like)
    ).subquery()
    return or_(
        Aircraft.tail_number.ilike(like),
        Aircraft.model_name.ilike(like),
        Aircraft.aircraft_name.ilike(like),
        Aircraft.model.ilike(like),
        Aircraft.variant.ilike(like),
        db.func.concat(Aircraft.model, db.func.ifnull(db.func.concat('-', Aircraft.variant), '')).ilike(like),
        Aircraft.manufacturer.ilike(like),
        Aircraft.id.in_(alias_ids),
    )


@app.route("/api/v1/aircraft/search")
def api_aircraft_search():
    """Search aircraft by tail number, model, variant, name, manufacturer, or alias."""
    q = request.args.get("q", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)

    query = Aircraft.query
    if q:
        query = query.filter(_build_aircraft_filter(q))
    query = query.order_by(Aircraft.model, Aircraft.variant, Aircraft.model_name)
    p = query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({"results": [a.to_dict() for a in p.items], "total": p.total, "page": p.page, "pages": p.pages})


@app.route("/api/v1/aircraft/<int:aircraft_id>")
def api_aircraft_detail(aircraft_id):
    """Get a single aircraft with its museum locations."""
    aircraft = Aircraft.query.get_or_404(aircraft_id)
    links = AircraftMuseum.query.filter_by(aircraft_id=aircraft_id).all()
    museums = [{**lnk.museum.to_dict(), "display_status": lnk.display_status, "notes": lnk.notes} for lnk in links]
    return jsonify({"aircraft": aircraft.to_dict(), "museums": museums})


@app.route("/api/v1/museums/search")
def api_museum_search():
    """Search museums by name, city, state/province, country, or region."""
    q = request.args.get("q", "").strip()
    region = request.args.get("region", "").strip()
    country = request.args.get("country", "").strip()
    state = request.args.get("state", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)

    query = Museum.query
    if q:
        like = f"%{q}%"
        query = query.filter(or_(
            Museum.name.ilike(like),
            Museum.city.ilike(like),
            Museum.state_province.ilike(like),
            Museum.country.ilike(like),
        ))
    if region:
        query = query.filter(Museum.region == region)
    if country:
        query = query.filter(Museum.country.ilike(country))
    if state:
        query = query.filter(Museum.state_province.ilike(state))
    query = query.order_by(Museum.name)
    p = query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({"results": [m.to_dict() for m in p.items], "total": p.total, "page": p.page, "pages": p.pages})


@app.route("/api/v1/museums/<int:museum_id>")
def api_museum_detail(museum_id):
    """Get a single museum with its aircraft collection."""
    museum = Museum.query.get_or_404(museum_id)
    links = AircraftMuseum.query.filter_by(museum_id=museum_id).all()
    aircraft_list = [{**lnk.aircraft.to_dict(), "display_status": lnk.display_status, "notes": lnk.notes} for lnk in links]
    return jsonify({"museum": museum.to_dict(), "aircraft": aircraft_list})


@app.route("/api/v1/museums/regions")
def api_museum_regions():
    """List all regions with museum counts."""
    rows = db.session.query(Museum.region, func.count(Museum.id)).group_by(Museum.region).all()
    return jsonify([{"region": r, "count": c} for r, c in rows])


@app.route("/api/v1/museums/countries")
def api_museum_countries():
    """List all countries with museum counts."""
    rows = db.session.query(Museum.country, func.count(Museum.id)).group_by(Museum.country).all()
    return jsonify([{"country": c, "count": n} for c, n in rows])


@app.route("/api/v1/nearest")
def api_nearest_museum():
    """Find nearest museum(s) with a specific aircraft to a location.

    The 'aircraft' param can match model, name, tail, manufacturer, or alias.
    Optionally filter by 'museum' name as well.
    Only museums with known coordinates are included in distance results.
    Museums without coordinates are listed separately.
    """
    aircraft_query = request.args.get("aircraft", "").strip()
    museum_query = request.args.get("museum", "").strip()
    location = request.args.get("location", "").strip()
    limit = min(request.args.get("limit", 5, type=int), 25)

    if not aircraft_query or not location:
        return jsonify({"error": "Both 'aircraft' and 'location' parameters are required."}), 400

    lat, lon = _resolve_location(location)
    if lat is None:
        return jsonify({"error": f"Could not resolve location: {location}"}), 404

    matching = Aircraft.query.filter(_build_aircraft_filter(aircraft_query)).all()
    if not matching:
        return jsonify({"error": f"No aircraft matching '{aircraft_query}' found."}), 404

    links_query = AircraftMuseum.query.filter(AircraftMuseum.aircraft_id.in_([a.id for a in matching]))

    # Optional museum name filter
    if museum_query:
        museum_like = f"%{museum_query}%"
        museum_ids = [m.id for m in Museum.query.filter(Museum.name.ilike(museum_like)).all()]
        if not museum_ids:
            return jsonify({"error": f"No museums matching '{museum_query}' found."}), 404
        links_query = links_query.filter(AircraftMuseum.museum_id.in_(museum_ids))

    links = links_query.all()
    if not links:
        return jsonify({"error": f"No museums found displaying aircraft matching '{aircraft_query}'."}), 404

    results = []
    no_coords = []
    for lnk in links:
        museum = lnk.museum
        if museum.has_coordinates:
            dist = haversine(lat, lon, float(museum.latitude), float(museum.longitude))
            results.append({
                "distance_miles": round(dist, 1),
                "museum": museum.to_dict(),
                "aircraft": lnk.aircraft.to_dict(),
                "display_status": lnk.display_status,
            })
        else:
            no_coords.append({
                "museum": museum.to_dict(),
                "aircraft": lnk.aircraft.to_dict(),
                "display_status": lnk.display_status,
                "note": "Distance unavailable — museum coordinates not on file.",
            })

    results.sort(key=lambda x: x["distance_miles"])
    response = {
        "origin": {"location": location, "latitude": lat, "longitude": lon},
        "results": results[:limit],
    }
    if no_coords:
        response["no_coordinates"] = no_coords
    return jsonify(response)


@app.route("/api/v1/museums/nearby")
def api_nearby_museums():
    """Find museums nearest to a given location.

    Parameters:
        location (required) — zip/postal code or city name.
        region   (optional) — filter by museum region.
        limit    (optional) — max results (default 10, max 50).
    """
    location = request.args.get("location", "").strip()
    region = request.args.get("region", "").strip()
    limit = min(request.args.get("limit", 10, type=int), 50)

    if not location:
        return jsonify({"error": "The 'location' parameter is required."}), 400

    lat, lon = _resolve_location(location)
    if lat is None:
        return jsonify({"error": f"Could not resolve location: {location}"}), 404

    query = Museum.query
    if region:
        query = query.filter(Museum.region == region)

    museums = query.all()

    results = []
    no_coords = []
    for m in museums:
        if m.has_coordinates:
            dist = haversine(lat, lon, float(m.latitude), float(m.longitude))
            results.append({"distance_miles": round(dist, 1), "museum": m.to_dict()})
        else:
            no_coords.append({"museum": m.to_dict(), "note": "Distance unavailable — coordinates not on file."})

    results.sort(key=lambda x: x["distance_miles"])
    response = {
        "origin": {"location": location, "latitude": lat, "longitude": lon},
        "results": results[:limit],
    }
    if no_coords:
        response["no_coordinates"] = no_coords
    return jsonify(response)


@app.route("/api/v1/stats")
def api_stats():
    """Dashboard statistics."""
    return jsonify({
        "aircraft_count": Aircraft.query.count(),
        "museum_count": Museum.query.count(),
        "link_count": AircraftMuseum.query.count(),
        "country_count": db.session.query(func.count(func.distinct(Museum.country))).scalar(),
    })


# ── Backward-compat aliases (old /api/ routes) ──

@app.route("/api/aircraft/search")
def aircraft_search_compat():
    return api_aircraft_search()

@app.route("/api/aircraft/<int:aircraft_id>")
def aircraft_detail_compat(aircraft_id):
    return api_aircraft_detail(aircraft_id)

@app.route("/api/museums/search")
def museum_search_compat():
    return api_museum_search()

@app.route("/api/museums/<int:museum_id>")
def museum_detail_compat(museum_id):
    return api_museum_detail(museum_id)

@app.route("/api/museums/regions")
def museum_regions_compat():
    return api_museum_regions()

@app.route("/api/nearest")
def nearest_compat():
    return api_nearest_museum()

@app.route("/api/museums/nearby")
def nearby_museums_compat():
    return api_nearby_museums()

@app.route("/api/stats")
def stats_compat():
    return api_stats()


# ══════════════════════════════════════════════
# API: Authenticated CRUD (requires API key or session)
# ══════════════════════════════════════════════

# ── Aircraft CRUD ──

@app.route("/api/v1/aircraft", methods=["POST"])
@api_auth_required("readwrite")
def api_create_aircraft():
    """Create a new aircraft record.

    Optional: pass ``museum_id`` and ``display_status`` to automatically
    link the aircraft to a museum on creation.
    """
    data = request.get_json() or {}
    required = ["manufacturer", "model"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    aircraft = Aircraft(
        tail_number=data.get("tail_number"),
        model_name=data.get("model_name"),
        aircraft_name=data.get("aircraft_name"),
        manufacturer=data["manufacturer"],
        model=data["model"],
        variant=data.get("variant"),
        aircraft_type=data.get("aircraft_type", "fixed_wing"),
        wing_type=data.get("wing_type") or None,
        military_civilian=data.get("military_civilian", "military"),
        year_built=data.get("year_built"),
        description=data.get("description"),
    )
    db.session.add(aircraft)
    db.session.flush()

    # Add aliases if provided
    for alias_str in data.get("aliases", []):
        alias_str = alias_str.strip()
        if alias_str:
            db.session.add(AircraftAlias(aircraft_id=aircraft.id, alias=alias_str))

    # Optionally link to a museum right away
    museum_id = data.get("museum_id")
    if museum_id:
        museum = Museum.query.get(museum_id)
        if museum:
            link = AircraftMuseum(
                aircraft_id=aircraft.id,
                museum_id=museum.id,
                display_status=data.get("display_status", "on_display"),
            )
            db.session.add(link)

    db.session.commit()
    return jsonify(aircraft.to_dict()), 201


@app.route("/api/v1/aircraft/<int:aircraft_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_aircraft(aircraft_id):
    """Update an existing aircraft record. Include 'aliases' array to replace all aliases."""
    aircraft = Aircraft.query.get_or_404(aircraft_id)
    data = request.get_json() or {}
    for field in ["tail_number", "model_name", "aircraft_name",
                   "manufacturer", "model", "variant",
                   "aircraft_type", "wing_type", "military_civilian",
                   "year_built", "description"]:
        if field in data:
            val = data[field] if data[field] else None  # treat empty string as None
            setattr(aircraft, field, val)
    # Replace aliases if provided
    if "aliases" in data:
        AircraftAlias.query.filter_by(aircraft_id=aircraft_id).delete()
        for alias_str in data["aliases"]:
            alias_str = alias_str.strip()
            if alias_str:
                db.session.add(AircraftAlias(aircraft_id=aircraft_id, alias=alias_str))
    db.session.commit()
    return jsonify(aircraft.to_dict())


@app.route("/api/v1/aircraft/<int:aircraft_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_aircraft(aircraft_id):
    """Delete an aircraft record (admin only)."""
    aircraft = Aircraft.query.get_or_404(aircraft_id)
    db.session.delete(aircraft)
    db.session.commit()
    return jsonify({"deleted": True, "id": aircraft_id})


# ── Museum CRUD ──

@app.route("/api/v1/museums", methods=["POST"])
@api_auth_required("readwrite")
def api_create_museum():
    """Create a new museum record.

    Required: name, city, country, region.
    Optional: state_province, postal_code, address, website, latitude, longitude.
    """
    data = request.get_json() or {}
    required = ["name", "city", "country", "region"]
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

    museum = Museum(
        name=data["name"],
        city=data["city"],
        state_province=data.get("state_province"),
        country=data["country"],
        postal_code=data.get("postal_code"),
        region=data["region"],
        address=data.get("address"),
        website=data.get("website"),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
    )
    db.session.add(museum)
    db.session.commit()
    return jsonify(museum.to_dict()), 201


@app.route("/api/v1/museums/<int:museum_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_museum(museum_id):
    """Update an existing museum record."""
    museum = Museum.query.get_or_404(museum_id)
    data = request.get_json() or {}
    for field in ["name", "city", "state_province", "country", "postal_code", "region",
                   "address", "website", "latitude", "longitude"]:
        if field in data:
            setattr(museum, field, data[field])
    db.session.commit()
    return jsonify(museum.to_dict())


@app.route("/api/v1/museums/<int:museum_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_museum(museum_id):
    """Delete a museum record (admin only)."""
    museum = Museum.query.get_or_404(museum_id)
    db.session.delete(museum)
    db.session.commit()
    return jsonify({"deleted": True, "id": museum_id})


# ── Exhibit links ──

@app.route("/api/v1/exhibits", methods=["POST"])
@api_auth_required("readwrite")
def api_create_exhibit():
    """Link an aircraft to a museum."""
    data = request.get_json() or {}
    if not data.get("aircraft_id") or not data.get("museum_id"):
        return jsonify({"error": "Both 'aircraft_id' and 'museum_id' are required."}), 400

    Aircraft.query.get_or_404(data["aircraft_id"])
    Museum.query.get_or_404(data["museum_id"])

    link = AircraftMuseum(
        aircraft_id=data["aircraft_id"],
        museum_id=data["museum_id"],
        display_status=data.get("display_status", "on_display"),
        notes=data.get("notes"),
    )
    db.session.add(link)
    db.session.commit()
    return jsonify(link.to_dict()), 201


@app.route("/api/v1/exhibits/<int:link_id>", methods=["PUT", "PATCH"])
@api_auth_required("readwrite")
def api_update_exhibit(link_id):
    """Update an exhibit link (status, notes)."""
    link = AircraftMuseum.query.get_or_404(link_id)
    data = request.get_json() or {}
    for field in ["display_status", "notes"]:
        if field in data:
            setattr(link, field, data[field])
    db.session.commit()
    return jsonify(link.to_dict())


@app.route("/api/v1/exhibits/<int:link_id>", methods=["DELETE"])
@api_auth_required("admin")
def api_delete_exhibit(link_id):
    """Remove an exhibit link (admin only)."""
    link = AircraftMuseum.query.get_or_404(link_id)
    db.session.delete(link)
    db.session.commit()
    return jsonify({"deleted": True, "id": link_id})


# ── Backward-compat write aliases ──

@app.route("/api/aircraft", methods=["POST"])
@api_auth_required("readwrite")
def create_aircraft_compat():
    return api_create_aircraft()

@app.route("/api/aircraft/<int:aid>", methods=["PUT"])
@api_auth_required("readwrite")
def update_aircraft_compat(aid):
    return api_update_aircraft(aid)

@app.route("/api/aircraft/<int:aid>", methods=["DELETE"])
@api_auth_required("admin")
def delete_aircraft_compat(aid):
    return api_delete_aircraft(aid)

@app.route("/api/museums", methods=["POST"])
@api_auth_required("readwrite")
def create_museum_compat():
    return api_create_museum()

@app.route("/api/museums/<int:mid>", methods=["PUT"])
@api_auth_required("readwrite")
def update_museum_compat(mid):
    return api_update_museum(mid)

@app.route("/api/museums/<int:mid>", methods=["DELETE"])
@api_auth_required("admin")
def delete_museum_compat(mid):
    return api_delete_museum(mid)

@app.route("/api/aircraft_museum", methods=["POST"])
@api_auth_required("readwrite")
def link_compat():
    return api_create_exhibit()

@app.route("/api/aircraft_museum/<int:lid>", methods=["DELETE"])
@api_auth_required("admin")
def unlink_compat(lid):
    return api_delete_exhibit(lid)


# ══════════════════════════════════════════════
# API: Key management (session-auth only)
# ══════════════════════════════════════════════

@app.route("/api/v1/keys", methods=["GET"])
@login_required
def api_list_keys():
    """List current user's API keys."""
    keys = ApiKey.query.filter_by(user_id=current_user.id).all()
    return jsonify([k.to_dict() for k in keys])


@app.route("/api/v1/keys", methods=["POST"])
@login_required
def api_create_key():
    """Generate a new API key for the current user."""
    data = request.get_json() or {}
    label = data.get("label", "default")
    permissions = data.get("permissions", "read")
    if permissions not in ("read", "readwrite", "admin"):
        return jsonify({"error": "permissions must be 'read', 'readwrite', or 'admin'."}), 400
    if permissions == "admin" and not current_user.is_admin:
        return jsonify({"error": "Only admins can create admin-level keys."}), 403

    api_key, raw_key = ApiKey.generate(current_user.id, label=label, permissions=permissions)
    db.session.add(api_key)
    db.session.commit()
    return jsonify({"key": raw_key, "id": api_key.id, "label": label, "permissions": permissions}), 201


@app.route("/api/v1/keys/<int:key_id>", methods=["DELETE"])
@login_required
def api_revoke_key(key_id):
    """Revoke (deactivate) an API key."""
    api_key = ApiKey.query.get_or_404(key_id)
    if api_key.user_id != current_user.id and not current_user.is_admin:
        abort(403)
    api_key.is_active = False
    db.session.commit()
    return jsonify({"revoked": True, "id": key_id})


# ══════════════════════════════════════════════
# API documentation page
# ══════════════════════════════════════════════

@app.route("/api/v1/docs")
def api_docs():
    return render_template("api_docs.html")


# ══════════════════════════════════════════════
# Helper
# ══════════════════════════════════════════════

def _resolve_location(location_str):
    """Return (lat, lon) for a zip/postal code or city name.

    Delegates to the geocoder module which tries, in order:
      1. Database cache (zip_codes table)
      2. pgeocode — offline postal-code data for 80+ countries
      3. geopy/Nominatim — online fallback for city names & addresses

    Successful external lookups are cached in the DB automatically.
    """
    return resolve_location(location_str, db=db, ZipCode=ZipCode)


if __name__ == "__main__":
    app.run(
        host=Config.SERVER_HOST,
        port=Config.SERVER_PORT,
        debug=Config.SERVER_DEBUG,
    )
