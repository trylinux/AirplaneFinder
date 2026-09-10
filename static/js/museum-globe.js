/* Shared desktop and mobile museum Discovery view. */

/* ── Data preload ────────────────────────────────────────────────────────
   Everything the globe plots is fetched as soon as the page has loaded and
   pre-baked into flat Float32Arrays during browser idle time — long before
   the Discovery tab is opened. initMuseumGlobe() then only wraps those
   arrays in BufferGeometry, so opening the tab doesn't wait on the network
   or on per-point object construction.
   Border GeoJSON is vendored under /static/data (no third-party CDN). */
var MuseumGlobeData = (function() {
    var R = 1;
    var PIN_R = R * 1.004, COUNTRY_R = R * 1.002, STATE_R = R * 1.003;
    var URLS = {
        pins: '/api/v1/museums/globe',
        countries: '/static/data/world-countries.geo.json?v=1',
        states: '/static/data/us-states.geo.json?v=1'
    };

    function writeXYZ(lat, lon, radius, out, i) {
        var phi = (90 - lat) * Math.PI / 180;
        var theta = (lon + 180) * Math.PI / 180;
        out[i]     = -radius * Math.sin(phi) * Math.cos(theta);
        out[i + 1] =  radius * Math.cos(phi);
        out[i + 2] =  radius * Math.sin(phi) * Math.sin(theta);
    }

    function fetchJSON(url) {
        return fetch(url, {credentials: 'same-origin'}).then(function(r) {
            if (!r.ok) throw new Error(url + ' → HTTP ' + r.status);
            return r.json();
        });
    }

    // Yield to the browser so baking never blocks first paint or input.
    function idle() {
        return new Promise(function(resolve) {
            if (window.requestIdleCallback) window.requestIdleCallback(resolve, {timeout: 1500});
            else setTimeout(resolve, 16);
        });
    }

    function bakePins(museums) {
        var positions = new Float32Array(museums.length * 3);
        museums.forEach(function(m, k) { writeXYZ(m.latitude, m.longitude, PIN_R, positions, k * 3); });
        return {museums: museums, positions: positions};
    }

    // Every ring of every feature becomes line-segment pairs in ONE array,
    // so the whole border layer is a single draw call instead of thousands.
    function bakeBorders(geo, radius) {
        var segments = 0, labels = [];
        var feats = (geo && geo.features) || [];
        var rings = [];
        feats.forEach(function(feat) {
            var g = feat.geometry;
            if (!g) return;
            var polys = g.type === 'Polygon' ? [g.coordinates] :
                        g.type === 'MultiPolygon' ? g.coordinates : [];
            var cx = 0, cy = 0, n = 0;
            polys.forEach(function(poly) {
                poly.forEach(function(ring) {
                    if (ring.length > 1) { rings.push(ring); segments += ring.length - 1; }
                    ring.forEach(function(c) { cx += c[0]; cy += c[1]; n++; });
                });
            });
            var props = feat.properties || {};
            var name = props.name || props.ADMIN || props.NAME || props.name_long || props.STATE_NAME || '';
            if (n && name) labels.push({name: name, lat: cy / n, lon: cx / n});
        });
        var positions = new Float32Array(segments * 6), o = 0;
        rings.forEach(function(ring) {
            for (var k = 0; k < ring.length - 1; k++) {
                writeXYZ(ring[k][1], ring[k][0], radius, positions, o); o += 3;
                writeXYZ(ring[k + 1][1], ring[k + 1][0], radius, positions, o); o += 3;
            }
        });
        return {positions: positions, labels: labels};
    }

    var cache = null;
    function preload() {
        if (cache) return cache;
        cache = {
            pins: fetchJSON(URLS.pins).then(function(m) { return idle().then(function() { return bakePins(m); }); }),
            // Borders are decoration: a failure just means no borders.
            countries: fetchJSON(URLS.countries).then(function(g) {
                return idle().then(function() { return bakeBorders(g, COUNTRY_R); });
            }).catch(function() { return null; }),
            states: fetchJSON(URLS.states).then(function(g) {
                return idle().then(function() { return bakeBorders(g, STATE_R); });
            }).catch(function() { return null; })
        };
        return cache;
    }

    // Kick off as soon as the page has finished its own first-load work.
    if (document.readyState === 'complete') setTimeout(preload, 0);
    else window.addEventListener('load', function() { setTimeout(preload, 0); });

    return {preload: preload, R: R};
})();

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
    var camera = new THREE.PerspectiveCamera(45, W / H, 0.001, 1000);
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
    var surface = new THREE.Mesh(new THREE.SphereGeometry(R * 0.995, 96, 64), surfaceMat);
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

    // Small, steady dots with a dark rim stay legible over borders. Their
    // screen size is fixed below; the larger invisible hit area stays intact.
    var pinCanvas = document.createElement('canvas');
    pinCanvas.width = pinCanvas.height = 32;
    var pinContext = pinCanvas.getContext('2d');
    pinContext.beginPath();
    pinContext.arc(16, 16, 16, 0, Math.PI * 2);
    pinContext.fillStyle = '#071426';
    pinContext.fill();
    pinContext.beginPath();
    pinContext.arc(16, 16, 11, 0, Math.PI * 2);
    pinContext.fillStyle = '#ffffff';
    pinContext.fill();
    var pinMat = new THREE.SpriteMaterial({
        map: new THREE.CanvasTexture(pinCanvas), depthWrite: false
    });
    var activePinMat = pinMat.clone();
    activePinMat.color.setHex(0x38bdf8);
    var activePinId = null;
    var pinTexture = pinMat.map;
    var pinData = [];            // museum records, index-aligned with pinPositions
    var pinPositions = null;     // Float32Array of local xyz, baked in preload
    var pinPoints = null;
    var activePin = new THREE.Sprite(activePinMat);
    activePin.visible = false;
    activePin.renderOrder = 2;
    globeGroup.add(activePin);

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
        sprite.userData.labelScale = sprite.scale.clone();
        sprite.userData.maxPixelHeight = opts.maxPixelHeight || 18;
        return sprite;
    }

    function normCountry(s) {
        return (s || '').toLowerCase().replace(/^the /, '').replace(/\./g, '').trim();
    }

    function addBorders(baked, material, parent) {
        var geom = new THREE.BufferGeometry();
        geom.setAttribute('position', new THREE.BufferAttribute(baked.positions, 3));
        var lines = new THREE.LineSegments(geom, material);
        lines.renderOrder = 1;   // after the translucent surface, so it occludes the far side
        parent.add(lines);
    }

    function addCountries(baked, countryHasMuseum) {
        addBorders(baked, borderMat, globeGroup);
        var keys = Object.keys(countryHasMuseum);
        baked.labels.forEach(function(l) {
            var nc = normCountry(l.name);
            // Loose match: any museum country containing / contained in this name
            var match = countryHasMuseum[nc] || keys.some(function(k) {
                return k && (k.indexOf(nc) >= 0 || nc.indexOf(k) >= 0);
            });
            if (!match) return;
            var sprite = makeLabelSprite(l.name);
            sprite.position.copy(latLonToVec3(l.lat, l.lon, R * 1.004));
            globeGroup.add(sprite);
            labelSprites.push(sprite);
        });
    }

    function addStates(baked) {
        addBorders(baked, stateBorderMat, stateGroup);
        baked.labels.forEach(function(l) {
            var sprite = makeLabelSprite(l.name, {
                fontSize: 36, fontWeight: '500',
                color: '#b8d0f5', worldScale: 0.00045
            });
            sprite.position.copy(latLonToVec3(l.lat, l.lon, R * 1.004));
            stateGroup.add(sprite);
            stateLabelSprites.push(sprite);
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
    var INITIAL_Z = 3.2, MIN_Z = 1.04, MAX_Z = 6;
    var pointers = new Map();
    var press = null, didDrag = false, pinch = null;

    var pickVec = new THREE.Vector3();
    var pickCam = new THREE.Vector3();
    function pickPin(clientX, clientY, radius) {
        if (!pinPositions) return null;
        scene.updateMatrixWorld(true);
        camera.updateMatrixWorld(true);
        var rect = canvas.getBoundingClientRect();
        var m = globeGroup.matrixWorld;
        pickCam.copy(camera.position);
        var best = -1, bestDistance = radius;
        for (var i = 0, n = pinData.length; i < n; i++) {
            pickVec.fromArray(pinPositions, i * 3).applyMatrix4(m);
            // Back-face test: normal · (camera − point) must be positive.
            var dx = pickCam.x - pickVec.x, dy = pickCam.y - pickVec.y, dz = pickCam.z - pickVec.z;
            if (pickVec.x * dx + pickVec.y * dy + pickVec.z * dz <= 0) continue;
            pickVec.project(camera);
            if (pickVec.z < -1 || pickVec.z > 1) continue;
            var x = rect.left + (pickVec.x + 1) * rect.width / 2;
            var y = rect.top + (1 - pickVec.y) * rect.height / 2;
            var distance = Math.hypot(clientX - x, clientY - y);
            if (distance < bestDistance) { best = i; bestDistance = distance; }
        }
        return best < 0 ? null : pinData[best];
    }

    function showPin(m) {
        activePinId = m ? m.id : null;
        activePin.visible = !!m;
        if (m) activePin.position.copy(latLonToVec3(m.latitude, m.longitude, R * 1.004));
        if (!m) { tooltip.classList.remove('show'); return; }
        tooltip.innerHTML =
            '<div class="t-name pin-name">' + escHtml(m.name) + '</div>' +
            '<div class="t-loc pin-loc">' + escHtml([m.city, m.state_province, m.country].filter(Boolean).join(', ')) + '</div>' +
            '<span class="t-count pin-count">' + m.aircraft_count + ' aircraft on display</span>' +
            (options.mobile ? '<a href="/museums/' + m.id + '">View museum &rarr;</a>' : '');
        tooltip.classList.add('show');
    }

    function zoomBy(factor) {
        // Scale altitude above the surface, so close zoom remains gradual.
        camera.position.z = Math.max(MIN_Z, Math.min(MAX_Z, R + (camera.position.z - R) * factor));
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
                if (distance > 0) camera.position.z = Math.max(MIN_Z, Math.min(MAX_Z, R + (pinch.z - R) * pinch.distance / distance));
            } else {
                if (press && Math.hypot(e.clientX - press.x, e.clientY - press.y) > 6) didDrag = true;
                if (didDrag) {
                    var dragSpeed = 0.005 * Math.min(1, (camera.position.z - R) / 2.2);
                    rotY += (e.clientX - previous.x) * dragSpeed;
                    rotX = Math.max(-1.3, Math.min(1.3, rotX + (e.clientY - previous.y) * dragSpeed));
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

    // ── Place pre-baked data (fetched/baked at page load; instant if ready) ──
    var data = MuseumGlobeData.preload();
    var countryHasMuseum = {};
    data.pins.then(function(baked) {
        loadingEl.style.display = 'none';
        pinData = baked.museums;
        pinPositions = baked.positions;
        pinData.forEach(function(m) { countryHasMuseum[normCountry(m.country)] = true; });

        var geom = new THREE.BufferGeometry();
        geom.setAttribute('position', new THREE.BufferAttribute(pinPositions, 3));
        pinPoints = new THREE.Points(geom, new THREE.PointsMaterial({
            size: 6, sizeAttenuation: false,   // six CSS px at every zoom, on the GPU
            map: pinTexture, transparent: true, alphaTest: 0.5, depthWrite: false
        }));
        pinPoints.renderOrder = 1;   // draw after the surface so far-side pins stay hidden
        globeGroup.add(pinPoints);

        return data.countries;
    }).then(function(countries) {
        if (countries) addCountries(countries, countryHasMuseum);
        return data.states;
    }).then(function(states) {
        if (states) addStates(states);
    }).catch(function() {
        if (!pinData.length) loadingEl.textContent = 'Failed to load museum data.';
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
    var markerPosition = new THREE.Vector3();
    function worldUnitsPerPixel(object) {
        object.getWorldPosition(markerPosition).applyMatrix4(camera.matrixWorldInverse);
        return 2 * Math.max(camera.near, -markerPosition.z) * Math.tan(camera.fov * Math.PI / 360) / H;
    }
    function animate() {
        requestAnimationFrame(animate);
        if (!wrap.clientWidth || !wrap.clientHeight || document.hidden) return;
        // Auto-rotate unless paused or dragging
        if (!dragging && !spinPaused && !selected) rotY += 0.00025 * Math.min(1, (camera.position.z - R) / 2.2);

        globeGroup.rotation.y = rotY;
        globeGroup.rotation.x = rotX;

        scene.updateMatrixWorld(true);
        camera.updateMatrixWorld(true);
        // Regular pins are sized by the GPU; only the accented one is scaled here.
        if (activePin.visible) activePin.scale.setScalar(8 * worldUnitsPerPixel(activePin));
        // Labels also stop growing when zoomed in to an individual region.
        labelSprites.concat(stateLabelSprites).forEach(function(label) {
            var baseScale = label.userData.labelScale;
            var limit = label.userData.maxPixelHeight * worldUnitsPerPixel(label);
            label.scale.copy(baseScale).multiplyScalar(Math.min(1, limit / baseScale.y));
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
