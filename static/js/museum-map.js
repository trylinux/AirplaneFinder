/* Leaflet map shared by museum discovery and trip suggestions. */
window.MuseumMap = function(container, {onSelect = () => {}, onMove = () => {}, onTileError = () => {}} = {}) {
    const {el, link} = Explorer;
    const map = L.map(container, {worldCopyJump:true, maxZoom:19, minZoom:2}).setView([25,0], 2);
    const tiles = L.tileLayer(container.dataset.tileUrl, {maxZoom:19, attribution:container.dataset.attribution}).addTo(map);
    tiles.on('tileerror', onTileError);
    const layer = L.layerGroup().addTo(map), path = L.layerGroup().addTo(map), road = L.layerGroup().addTo(map);
    let museums = [], numbered = false, selected = null;
    // Keep consecutive points on the same side of the date line so a trip
    // across it draws as one short line, not a lap around the world.
    function unwrap(points) {
        const adjusted = [points[0].slice()];
        for (const p of points.slice(1)) {
            const previous = adjusted[adjusted.length-1][1];
            adjusted.push([p[0], p[1]+360*Math.round((previous-p[1])/360)]);
        }
        return adjusted;
    }
    function point(museum) {
        const lon = museum.longitude + 360 * Math.round((map.getCenter().lng - museum.longitude) / 360);
        return [museum.latitude, lon];
    }
    function inBounds(museum, bounds = map.getBounds()) { return bounds.contains(point(museum)); }
    function popup(museum) {
        const content = el('div');
        content.append(el('h3', museum.name), el('p', `${museum.city}, ${museum.country}`));
        if (museum.aircraft_count != null) content.append(el('p', `${museum.aircraft_count} aircraft recorded on display`));
        content.append(link('View museum collection →', `/museums/${museum.id}`));
        return content;
    }
    function render() {
        layer.clearLayers();
        const groups = new Map();
        museums.forEach((museum, index) => {
            if (!inBounds(museum, map.getBounds().pad(.2))) return;
            const projected = map.project(point(museum), map.getZoom());
            // Fixed world-pixel cells prevent clusters jumping when the map pans.
            const key = numbered ? String(index) : `${Math.floor(projected.x / 48)}:${Math.floor(projected.y / 48)}`;
            if (!groups.has(key)) groups.set(key, []);
            groups.get(key).push({museum,index});
        });
        for (const entries of groups.values()) {
            const cluster = entries.length > 1, museum = entries[0].museum;
            const position = cluster ? [entries.reduce((s,e)=>s+point(e.museum)[0],0)/entries.length, entries.reduce((s,e)=>s+point(e.museum)[1],0)/entries.length] : point(museum);
            const size = cluster || numbered ? 34 : 18;
            const marker = L.marker(position, {title:cluster ? `${entries.length} museums` : museum.name,
                icon:L.divIcon({className:'x-marker' + (cluster ? ' cluster' : ''), html:cluster ? String(entries.length) : numbered ? String(entries[0].index + 1) : '', iconSize:[size,size], iconAnchor:[size/2,size/2]})}).addTo(layer);
            if (cluster) {
                marker.on('click', () => {
                    const bounds = L.latLngBounds(entries.map(e => point(e.museum)));
                    if (map.getZoom() < 19) map.fitBounds(bounds, {padding:[40,40], maxZoom:map.getZoom()+3});
                    else {
                        const content = el('div'); content.append(el('h3','Museums at this location'));
                        entries.forEach(e => content.append(link(e.museum.name, `/museums/${e.museum.id}`), el('br')));
                        marker.bindPopup(content).openPopup();
                    }
                });
            } else {
                marker.bindPopup(popup(museum));
                marker.on('click', () => { selected = museum.id; onSelect(museum); });
                if (selected === museum.id) marker.openPopup();
            }
        }
    }
    map.on('moveend', () => {render(); onMove();});
    const observer = new ResizeObserver(() => map.invalidateSize()); observer.observe(container);
    return {
        map,
        setMuseums(items, options = {}) {
            museums = items; numbered = Boolean(options.numbered); selected = null;
            if (options.fit && items.length) {
                // Unwrap around the first museum so trips across the date line stay compact.
                const base = items[0].longitude;
                map.fitBounds(items.map(m => [m.latitude, m.longitude + 360 * Math.round((base - m.longitude) / 360)]), {padding:[30,30], maxZoom:12});
            }
            render();
        },
        show(museum) {selected = museum.id; map.setView(point(museum), Math.max(map.getZoom(), 14)); render();},
        inBounds,
        setRoute(points) {
            path.clearLayers(); road.clearLayers();
            if (points.length < 2) return;
            const adjusted = unwrap(points);
            L.polyline(adjusted, {color:'#2563eb', weight:3, dashArray:'7 8'}).addTo(path);
            const startsAtMuseum = museums.some(m => Math.abs(m.latitude - points[0][0]) < .00001 && Math.abs(m.longitude - points[0][1]) < .00001);
            L.circleMarker(adjusted[0], {radius:startsAtMuseum ? 22 : 7, color:startsAtMuseum ? '#16a34a' : '#fff', fillColor:'#16a34a', fillOpacity:startsAtMuseum ? .2 : 1, weight:2}).bindTooltip('Starting point').addTo(path);
            map.fitBounds(adjusted, {padding:[35,35], maxZoom:12});
        },
        /* Draw a drivable route (one array of [lat,lon] per leg) on top of the
           straight-line guide. The dashed line stays underneath, faded, so
           the visit order is still legible where roads loop back. */
        setRoadRoute(legs) {
            road.clearLayers();
            if (!legs || !legs.length) { path.eachLayer(l => l.setStyle && l.setStyle({opacity:1})); return; }
            path.eachLayer(l => l.setStyle && l.options.dashArray && l.setStyle({opacity:.35}));
            const all = [];
            legs.forEach((leg, index) => {
                if (!leg.points || leg.points.length < 2) return;
                const adjusted = unwrap(leg.points);
                L.polyline(adjusted, {color:'#0f172a', weight:7, opacity:.55}).addTo(road);   // casing
                L.polyline(adjusted, {color:'#f59e0b', weight:4, opacity:.95}).bindTooltip(`Leg ${index+1}`, {sticky:true}).addTo(road);
                all.push(...adjusted);
            });
            if (all.length) map.fitBounds(all, {padding:[35,35], maxZoom:12});
        },
        destroy() {observer.disconnect(); map.remove();}
    };
};
