(() => {
    const {el,link,api,message,external,directions} = Explorer;
    const status = document.querySelector('#map-status'), results = document.querySelector('#map-results');
    let data = [], filtered = [], pageSize = 30, serial = 0;
    const map = MuseumMap(document.querySelector('#museum-map'), {
        onSelect(museum) {
            results.querySelectorAll('.x-card').forEach(c => c.classList.toggle('selected', c.dataset.id === String(museum.id)));
            const card = results.querySelector(`[data-id="${museum.id}"]`);
            if (card) results.scrollTop = card.offsetTop - results.offsetTop;
        },
        onTileError() { message(document.querySelector('#map-tile-status'), 'The background map could not load. Museum lists and links are still available.', true); }
    });
    function render() {
        results.replaceChildren();
        document.querySelector('#map-result-heading').textContent = `${filtered.length} museums`;
        filtered.slice(0,pageSize).forEach(museum => {
            const card = el('article', null, 'x-card'); card.dataset.id = museum.id;
            card.append(el('h3',museum.name),el('p',`${museum.city}, ${museum.country}`,'x-muted'),el('p',`${museum.aircraft_count} aircraft recorded on display`));
            const actions = el('div',null,'x-actions'), show = el('button','Show on map','x-button secondary'); show.type = 'button';
            show.onclick = () => {map.show(museum); document.querySelector('#museum-map').scrollIntoView({behavior:'smooth',block:'center'});};
            actions.append(show,link('Collection',`/museums/${museum.id}`,'x-button secondary'),external('Directions',directions(museum)));
            card.append(actions); results.append(card);
        });
        if (!filtered.length) results.append(el('p','No museums in this area. Zoom out or show all matches.','x-muted'));
        document.querySelector('#map-more').hidden = filtered.length <= pageSize;
    }
    async function load() {
        const requestId = ++serial; message(status,'Loading museums…');
        try {
            const params = new URLSearchParams({q:document.querySelector('#map-query').value,region:document.querySelector('#map-region').value});
            const response = await api('/api/v1/museums/map?' + params);
            if (requestId !== serial) return;
            data = response.results; filtered = data; pageSize = 30; map.setMuseums(data,{fit:true}); render();
            message(status,`${data.length} mapped museums. Pan or zoom, then choose “Search this area.”`);
            const missing = response.no_coordinates, panel = document.querySelector('#map-unlocated-list'); panel.replaceChildren();
            document.querySelector('#map-unlocated').hidden = !missing.length;
            document.querySelector('#map-unlocated-title').textContent = `${missing.length} matching museums need coordinates`;
            missing.forEach(m => {const p = el('p'); p.append(link(`${m.name} — ${m.city}, ${m.country}`,`/museums/${m.id}`));panel.append(p);});
        } catch(error) {if (requestId === serial) message(status,error.message,true);}
    }
    document.querySelector('#map-search').onsubmit = e => {e.preventDefault();load();};
    document.querySelector('#map-area').onclick = () => {filtered = data.filter(m => map.inBounds(m));pageSize = 30;render();message(status,`${filtered.length} matching museums in the selected area.`);};
    document.querySelector('#map-all').onclick = () => {filtered = data;pageSize = 30;map.setMuseums(data,{fit:true});render();message(status,'Showing all search matches.');};
    document.querySelector('#map-more').onclick = () => {pageSize += 30;render();};
    document.querySelector('#map-locate').onclick = () => {
        if (!navigator.geolocation) return message(status,'Device location is unavailable. Search for a city instead.',true);
        message(status,'Waiting for your location…');
        navigator.geolocation.getCurrentPosition(p => {map.map.setView([p.coords.latitude,p.coords.longitude],10);filtered=data.filter(m=>map.inBounds(m));pageSize=30;render();message(status,'Showing museums near your location.');}, () => message(status,'Location unavailable or permission denied. Search for a city instead.',true), {timeout:10000,maximumAge:60000});
    };
    api('/api/v1/museums/regions').then(regions => regions.forEach(r => {const option=el('option',r.region);option.value=r.region;document.querySelector('#map-region').append(option);})).catch(()=>{});
    load();
})();
