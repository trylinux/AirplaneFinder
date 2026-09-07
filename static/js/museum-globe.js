/* Shared desktop and mobile museum Discovery view. */
function initMuseumGlobe(options) {
    var prefix = options.prefix || "";
    var wrap = document.getElementById(prefix + 'globe-wrap');
    var canvas = document.getElementById(prefix + 'globe-canvas');
    var tooltip = document.getElementById(prefix + 'globe-tooltip');
    var loadingEl = document.getElementById(prefix + 'globe-loading');

    if (typeof THREE === 'undefined') {
        loadingEl.textContent = 'Could not load the globe. Please reload or use the directory.';
        return null;
    }
    var W = wrap.clientWidth, H = wrap.clientHeight;

    // Scene, camera, renderer
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(45, W / H, 0.1, 1000);
    camera.position.z = 3.2;

    var renderer;
    try {
        renderer = new THREE.WebGLRenderer({canvas: canvas, antialias: true, alpha: true});
    } catch (error) {
        loadingEl.textContent = 'Your browser could not start the globe. Use the directory to browse museums.';
        return null;
    }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setSize(W, H, false);
    renderer.setClearColor(0x000000, 0);

    // ── Globe group (rotates as a whole) ──
    var globeGroup = new THREE.Group();
    scene.add(globeGroup);

    var R = 1;

    // Solid semi-transparent sphere (so pins on the far side are occluded)
    var surfaceMat = new THREE.MeshBasicMaterial({
        color: 0x0a1b3a, transparent: true, opacity: 0.92
    });
    var surface = new THREE.Mesh(new THREE.SphereGeometry(R * 0.995, 48, 32), surfaceMat);
    globeGroup.add(surface);

    // Wireframe overlay — latitude/longitude grid in dim blue
    var wireMat = new THREE.LineBasicMaterial({
        color: 0x3a6bd8, transparent: true, opacity: 0.35
    });
    var wire = new THREE.LineSegments(
        new THREE.WireframeGeometry(new THREE.SphereGeometry(R, 24, 18)),
        wireMat
    );
    globeGroup.add(wire);

    // Brighter outline (rim glow)
    var rimMat = new THREE.LineBasicMaterial({
        color: 0x6ba7ff, transparent: true, opacity: 0.55
    });
    var equator = new THREE.LineLoop(
        new THREE.BufferGeometry().setFromPoints(
            Array.from({length: 128}, function(_, i) {
                var a = (i / 128) * Math.PI * 2;
                return new THREE.Vector3(Math.cos(a) * R, 0, Math.sin(a) * R);
            })
        ),
        rimMat
    );
    globeGroup.add(equator);

    // ── lat/lon → xyz ──
    function latLonToVec3(lat, lon, radius) {
        var phi = (90 - lat) * Math.PI / 180;
        var theta = (lon + 180) * Math.PI / 180;
        return new THREE.Vector3(
            -radius * Math.sin(phi) * Math.cos(theta),
             radius * Math.cos(phi),
             radius * Math.sin(phi) * Math.sin(theta)
        );
    }

    // Shared pin geometry / material
    var pinGeom = new THREE.SphereGeometry(0.012, 10, 10);
    var pinMat = new THREE.MeshBasicMaterial({
        color: 0xffffff, transparent: true, opacity: 0.95
    });
    var pins = [];

    // Country borders + labels
    var borderMat = new THREE.LineBasicMaterial({
        color: 0x6fa3e8, transparent: true, opacity: 0.55
    });
    var stateBorderMat = new THREE.LineBasicMaterial({
        color: 0x8fb8e8, transparent: true, opacity: 0.45
    });
    var labelSprites = [];
    var stateLabelSprites = [];
    var stateGroup = new THREE.Group();
    stateGroup.visible = false;
    globeGroup.add(stateGroup);

    function makeLabelSprite(text, opts) {
        opts = opts || {};
        var fontSize = opts.fontSize || 54;
        var fontWeight = opts.fontWeight || '600';
        var color = opts.color || '#dbe7ff';
        var worldScale = opts.worldScale || 0.00065; // world units per canvas pixel
        var font = fontWeight + ' ' + fontSize + 'px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif';

        // Measure the text so the canvas never crops long labels
        var meas = document.createElement('canvas').getContext('2d');
        meas.font = font;
        var textW = Math.ceil(meas.measureText(text).width);
        var padX = 30, padY = 20;
        var w = textW + padX * 2;
        var h = fontSize + padY * 2;

        var canvas = document.createElement('canvas');
        canvas.width = w; canvas.height = h;
        var ctx = canvas.getContext('2d');
        ctx.font = font;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.shadowColor = 'rgba(0,0,0,0.9)';
        ctx.shadowBlur = 10;
        ctx.fillStyle = 'rgba(0,0,0,0.75)';
        ctx.fillText(text, w/2, h/2);
        ctx.shadowBlur = 0;
        ctx.fillStyle = color;
        ctx.fillText(text, w/2, h/2);

        var tex = new THREE.CanvasTexture(canvas);
        tex.needsUpdate = true;
        var mat = new THREE.SpriteMaterial({
            map: tex, transparent: true, depthTest: false, depthWrite: false
        });
        var sprite = new THREE.Sprite(mat);
        sprite.scale.set(w * worldScale, h * worldScale, 1);
        return sprite;
    }

    function normCountry(s) {
        return (s || '').toLowerCase().replace(/^the /, '').replace(/\./g, '').trim();
    }

    function addCountriesGeoJSON(geo, countryHasMuseum) {
        var feats = geo.features || [];
        feats.forEach(function(feat) {
            var props = feat.properties || {};
            var cname = props.name || props.ADMIN || props.NAME || props.name_long || '';
            var g = feat.geometry;
            if (!g) return;
            var polys = g.type === 'Polygon' ? [g.coordinates] :
                        g.type === 'MultiPolygon' ? g.coordinates : [];
            var all = [];
            polys.forEach(function(poly) {
                poly.forEach(function(ring) {
                    var pts = ring.map(function(c) {
                        all.push(c);
                        return latLonToVec3(c[1], c[0], R * 1.002);
                    });
                    if (pts.length > 1) {
                        var bg = new THREE.BufferGeometry().setFromPoints(pts);
                        globeGroup.add(new THREE.Line(bg, borderMat));
                    }
                });
            });

            // Label if this country has at least one museum
            var nc = normCountry(cname);
            var match = countryHasMuseum[nc];
            if (!match) {
                // Loose match: check if any museum country contains / is contained in this name
                for (var k in countryHasMuseum) {
                    if (k && (k.indexOf(nc) >= 0 || nc.indexOf(k) >= 0)) { match = true; break; }
                }
            }
            if (match && all.length) {
                var cx = 0, cy = 0;
                all.forEach(function(c) { cx += c[0]; cy += c[1]; });
                cx /= all.length; cy /= all.length;
                var sprite = makeLabelSprite(cname);
                sprite.position.copy(latLonToVec3(cy, cx, R * 1.035));
                globeGroup.add(sprite);
                labelSprites.push(sprite);
            }
        });
    }

    function addStatesGeoJSON(geo) {
        var feats = geo.features || [];
        feats.forEach(function(feat) {
            var props = feat.properties || {};
            var sname = props.name || props.NAME || props.STATE_NAME || '';
            var g = feat.geometry;
            if (!g) return;
            var polys = g.type === 'Polygon' ? [g.coordinates] :
                        g.type === 'MultiPolygon' ? g.coordinates : [];
            var all = [];
            polys.forEach(function(poly) {
                poly.forEach(function(ring) {
                    var pts = ring.map(function(c) {
                        all.push(c);
                        return latLonToVec3(c[1], c[0], R * 1.003);
                    });
                    if (pts.length > 1) {
                        var bg = new THREE.BufferGeometry().setFromPoints(pts);
                        stateGroup.add(new THREE.Line(bg, stateBorderMat));
                    }
                });
            });
            if (all.length && sname) {
                var cx = 0, cy = 0;
                all.forEach(function(c) { cx += c[0]; cy += c[1]; });
                cx /= all.length; cy /= all.length;
                var sprite = makeLabelSprite(sname, {
                    fontSize: 36, fontWeight: '500',
                    color: '#b8d0f5', worldScale: 0.00045
                });
                sprite.position.copy(latLonToVec3(cy, cx, R * 1.04));
                stateGroup.add(sprite);
                stateLabelSprites.push(sprite);
            }
        });
    }

    // Pick in screen pixels so small pins remain tappable at every zoom level.
    // Reject the far side of the sphere before measuring the touch target.
    var raycaster = new THREE.Raycaster();
    var occluder = new THREE.Sphere(new THREE.Vector3(), R * 0.995);
    var pointer = null;
    var selected = null;
    var dragging = false;
    var spinPaused = false;
    var rotY = 0, rotX = 0.25;
    var INITIAL_Z = 3.2, MIN_Z = 1.35, MAX_Z = 6;
    var pointers = new Map();
    var press = null, didDrag = false, pinch = null;

    function pickPin(clientX, clientY, radius) {
        scene.updateMatrixWorld(true);
        camera.updateMatrixWorld(true);
        var rect = canvas.getBoundingClientRect();
        var best = null, bestDistance = radius;
        pins.forEach(function(pin) {
            var world = pin.getWorldPosition(new THREE.Vector3());
            var direction = world.clone().sub(camera.position).normalize();
            raycaster.set(camera.position, direction);
            var surfaceHit = raycaster.ray.intersectSphere(occluder, new THREE.Vector3());
            if (surfaceHit && camera.position.distanceTo(surfaceHit) < camera.position.distanceTo(world) - 0.02) return;
            var projected = world.clone().project(camera);
            if (projected.z < -1 || projected.z > 1) return;
            var x = rect.left + (projected.x + 1) * rect.width / 2;
            var y = rect.top + (1 - projected.y) * rect.height / 2;
            var distance = Math.hypot(clientX - x, clientY - y);
            if (distance < bestDistance) { best = pin.userData; bestDistance = distance; }
        });
        return best;
    }

    function showPin(m) {
        if (!m) { tooltip.classList.remove('show'); return; }
        tooltip.innerHTML =
            '<div class="t-name pin-name">' + escHtml(m.name) + '</div>' +
            '<div class="t-loc pin-loc">' + escHtml([m.city, m.state_province, m.country].filter(Boolean).join(', ')) + '</div>' +
            '<span class="t-count pin-count">' + m.aircraft_count + ' aircraft on display</span>' +
            (options.mobile ? '<a href="/museums/' + m.id + '">View museum &rarr;</a>' : '');
        tooltip.classList.add('show');
    }

    function zoomBy(factor) {
        camera.position.z = Math.max(MIN_Z, Math.min(MAX_Z, camera.position.z * factor));
    }
    document.getElementById(prefix + 'globe-zoom-in').addEventListener('click', function() { zoomBy(0.8); });
    document.getElementById(prefix + 'globe-zoom-out').addEventListener('click', function() { zoomBy(1.25); });
    document.getElementById(prefix + 'globe-zoom-reset').addEventListener('click', function() { camera.position.z = INITIAL_Z; });
    var spinBtn = document.getElementById(prefix + 'globe-spin-toggle');
    spinBtn.addEventListener('click', function() {
        spinPaused = !spinPaused;
        spinBtn.innerHTML = spinPaused ? '<i class="fa-solid fa-play"></i>' : '<i class="fa-solid fa-pause"></i>';
        spinBtn.setAttribute('aria-label', spinPaused ? 'Resume rotation' : 'Pause rotation');
        spinBtn.classList.toggle('paused', spinPaused);
    });

    function pointerDistance() {
        var points = Array.from(pointers.values());
        return Math.hypot(points[0].x - points[1].x, points[0].y - points[1].y);
    }
    canvas.addEventListener('pointerdown', function(e) {
        if (e.button !== 0) return;
        pointers.set(e.pointerId, {x: e.clientX, y: e.clientY});
        dragging = true;
        pointer = null;
        selected = null;
        showPin(null);
        if (pointers.size === 1) {
            press = {x: e.clientX, y: e.clientY};
            didDrag = false;
        } else {
            didDrag = true;
            pinch = {distance: pointerDistance(), z: camera.position.z};
        }
        canvas.setPointerCapture(e.pointerId);
    });
    canvas.addEventListener('pointermove', function(e) {
        var previous = pointers.get(e.pointerId);
        if (previous) {
            pointers.set(e.pointerId, {x: e.clientX, y: e.clientY});
            if (pointers.size > 1 && pinch) {
                var distance = pointerDistance();
                if (distance > 0) camera.position.z = Math.max(MIN_Z, Math.min(MAX_Z, pinch.z * pinch.distance / distance));
            } else {
                if (press && Math.hypot(e.clientX - press.x, e.clientY - press.y) > 6) didDrag = true;
                if (didDrag) {
                    rotY += (e.clientX - previous.x) * 0.005;
                    rotX = Math.max(-1.3, Math.min(1.3, rotX + (e.clientY - previous.y) * 0.005));
                }
            }
        } else if (e.pointerType === 'mouse') {
            pointer = {x: e.clientX, y: e.clientY};
            if (!options.mobile) {
                var rect = canvas.getBoundingClientRect();
                tooltip.style.left = (e.clientX - rect.left) + 'px';
                tooltip.style.top = (e.clientY - rect.top) + 'px';
            }
        }
    });
    function releasePointer(e) {
        if (!pointers.has(e.pointerId)) return;
        var tapped = e.type === 'pointerup' && !didDrag && pointers.size === 1 && press &&
            Math.hypot(e.clientX - press.x, e.clientY - press.y) <= 6;
        pointers.delete(e.pointerId);
        dragging = pointers.size > 0;
        pinch = null;
        if (canvas.hasPointerCapture(e.pointerId)) canvas.releasePointerCapture(e.pointerId);
        if (tapped) {
            var m = pickPin(e.clientX, e.clientY, e.pointerType === 'mouse' ? 12 : 24);
            if (options.mobile) { selected = m; showPin(m); }
            else if (m) options.onSelect(m.id);
        }
    }
    canvas.addEventListener('pointerup', releasePointer);
    canvas.addEventListener('pointercancel', releasePointer);
    canvas.addEventListener('lostpointercapture', releasePointer);
    canvas.addEventListener('pointerleave', function() {
        pointer = null;
        if (!selected) showPin(null);
    });
    canvas.addEventListener('wheel', function(e) {
        e.preventDefault();
        zoomBy(Math.exp(e.deltaY * (e.ctrlKey ? 0.015 : 0.0015)));
    }, {passive: false});

    // ── Fetch museums and place pins, then fetch country geometry ──
    $.getJSON('/api/v1/museums/globe', function(museums) {
        loadingEl.style.display = 'none';
        var countryHasMuseum = {};
        museums.forEach(function(m) {
            var pos = latLonToVec3(m.latitude, m.longitude, R * 1.01);
            var pin = new THREE.Mesh(pinGeom, pinMat.clone());
            pin.position.copy(pos);
            pin.userData = m;
            globeGroup.add(pin);
            pins.push(pin);
            countryHasMuseum[normCountry(m.country)] = true;
        });

        // Country borders + labels (lightweight world GeoJSON via jsDelivr)
        $.getJSON('https://cdn.jsdelivr.net/gh/johan/world.geo.json@master/countries.geo.json')
            .done(function(geo) { addCountriesGeoJSON(geo, countryHasMuseum); })
            .fail(function() { /* silently skip borders if CDN blocked */ });

        // US state borders + labels (loaded lazily; shown when zoomed in)
        $.getJSON('https://cdn.jsdelivr.net/gh/PublicaMundi/MappingAPI@master/data/geojson/us-states.json')
            .done(function(geo) { addStatesGeoJSON(geo); })
            .fail(function() { /* silently skip states if CDN blocked */ });
    }).fail(function() {
        loadingEl.textContent = 'Failed to load museum data.';
    });

    // ── Resize handler ──
    function onResize() {
        if (!wrap.clientWidth || !wrap.clientHeight) return;
        W = wrap.clientWidth; H = wrap.clientHeight;
        camera.aspect = W / H;
        camera.updateProjectionMatrix();
        renderer.setSize(W, H, false);
    }
    window.addEventListener('resize', onResize);
    var resizeObserver = new ResizeObserver(onResize);
    resizeObserver.observe(wrap);

    // ── Animation loop ──
    var clock = new THREE.Clock();
    function animate() {
        requestAnimationFrame(animate);
        if (!wrap.clientWidth || !wrap.clientHeight || document.hidden) return;
        var t = clock.getElapsedTime();

        // Auto-rotate unless paused or dragging
        if (!dragging && !spinPaused && !selected) rotY += 0.00025;

        globeGroup.rotation.y = rotY;
        globeGroup.rotation.x = rotX;

        // Throb pins: scale oscillates between .85 and 1.6, opacity 0.6 → 1
        var throb = 0.85 + Math.sin(t * 2.6) * 0.4;
        var opac  = 0.65 + Math.sin(t * 2.6) * 0.35;
        pins.forEach(function(p) {
            p.scale.setScalar(throb);
            p.material.opacity = opac;
        });

        // Zoom-based detail: show state lines/labels only when close
        var z = camera.position.z;
        var stateDetailOn = z < 2.4;
        stateGroup.visible = stateDetailOn;

        // Fade country labels on the far side of the globe
        var camDir = new THREE.Vector3();
        camera.getWorldPosition(camDir).normalize();
        var worldPos = new THREE.Vector3();
        if (labelSprites.length) {
            // Also fade country labels out when zoomed in so state labels can shine
            var countryZoomFade = Math.max(0, Math.min(1, (z - 2.0) / 0.6));
            labelSprites.forEach(function(s) {
                s.getWorldPosition(worldPos);
                var facing = worldPos.clone().normalize().dot(camDir);
                var o = Math.max(0, Math.min(1, (facing - 0.15) * 2.2)) * countryZoomFade;
                s.material.opacity = o;
                s.visible = o > 0.02;
            });
        }
        if (stateDetailOn && stateLabelSprites.length) {
            var stateFade = Math.max(0, Math.min(1, (2.4 - z) / 0.5));
            stateLabelSprites.forEach(function(s) {
                s.getWorldPosition(worldPos);
                var facing = worldPos.clone().normalize().dot(camDir);
                var o = Math.max(0, Math.min(1, (facing - 0.15) * 2.2)) * stateFade;
                s.material.opacity = o;
                s.visible = o > 0.02;
            });
        }

        if (pointer && !dragging && !selected) {
            var hovered = pickPin(pointer.x, pointer.y, 12);
            showPin(hovered);
            canvas.style.cursor = hovered ? 'pointer' : 'grab';
        }

        renderer.render(scene, camera);
    }
    animate();
    return {resize: onResize};
}
