(() => {
    const {el,link,api,message,external} = Explorer;
    const $ = selector => document.querySelector(selector);
    let targets = [], revision = 0, searchSerial = 0, currentRequest = null, map = null;
    const storageKey = 'aircraft-finder-trips-v1';
    function invalidate() {revision++;currentRequest=null;$('#trip-result').hidden=true;message($('#trip-status'),'');}
    function targetKey(t) {return t.kind === 'airframe' ? `airframe:${t.aircraft_id}` : `model:${t.manufacturer.toLowerCase()}:${t.model.toLowerCase()}`;}
    function targetLabel(t) {return t.label || (t.kind === 'model' ? `${t.manufacturer} ${t.model} · any variant` : `Airframe #${t.aircraft_id}`);}
    function renderTargets() {
        $('#trip-targets').replaceChildren();$('#trip-target-count').textContent=`${targets.length} / 12`;
        targets.forEach((target,index) => {
            const item=el('li'), remove=el('button','Remove','x-button secondary');remove.type='button';remove.setAttribute('aria-label',`Remove ${targetLabel(target)}`);
            remove.onclick=()=>{targets.splice(index,1);invalidate();renderTargets();};item.append(el('span',targetLabel(target)),remove);$('#trip-targets').append(item);
        });
        if (!targets.length) $('#trip-targets').append(el('li','Add an individual airframe or any example of a model.','x-muted'));
    }
    function add(target) {
        if (targets.some(t=>targetKey(t)===targetKey(target))) return message($('#trip-search-status'),'Already on your list.');
        if (targets.length >= 12) return message($('#trip-search-status'),'Choose at most 12 aircraft or models.',true);
        targets.push(target);invalidate();renderTargets();message($('#trip-search-status'),'Added to your aircraft list.');
    }
    function exactTarget(a) {return {kind:'airframe',aircraft_id:a.id,label:`${a.full_designation} · ${a.tail_number || a.aircraft_name || 'Airframe #'+a.id}`};}
    $('#trip-search-form').onsubmit=async e=>{
        e.preventDefault();const q=$('#trip-search').value.trim();if (!q) return;
        const serial=++searchSerial;message($('#trip-search-status'),'Searching…');
        try {
            const data=await api('/api/v1/aircraft/search?'+new URLSearchParams({q,per_page:20}));
            if(serial!==searchSerial)return;$('#trip-search-results').replaceChildren();
            message($('#trip-search-status'),data.total ? `Showing ${data.results.length} of ${data.total} matches. Refine the search for more specific results.`:'No matching aircraft.');
            const shownModels=new Set();
            data.results.forEach(a=>{
                const card=el('article',null,'x-card'), actions=el('div',null,'x-actions');
                card.append(el('h3',`${a.manufacturer} ${a.full_designation}`),el('p',[a.tail_number,a.aircraft_name,a.model_name].filter(Boolean).join(' · ') || `Airframe #${a.id}`,'x-muted'));
                const exact=el('button','This airframe','x-button secondary');exact.type='button';exact.onclick=()=>add(exactTarget(a));actions.append(exact);
                const model={kind:'model',manufacturer:a.manufacturer,model:a.model};
                if(!shownModels.has(targetKey(model))) {
                    shownModels.add(targetKey(model));const any=el('button',`Any ${a.model}`,'x-button');any.type='button';any.onclick=()=>add(model);actions.append(any);
                }
                actions.append(link('History',`/aircraft/${a.id}/history`));card.append(actions);$('#trip-search-results').append(card);
            });
        } catch(error){if(serial===searchSerial)message($('#trip-search-status'),error.message,true);}
    };
    function routeUrl(points) {
        const coord=p=>`${p.latitude},${p.longitude}`;
        const params=new URLSearchParams({api:'1',origin:coord(points[0]),destination:coord(points[points.length-1]),travelmode:'driving'});
        if(points.length>2)params.set('waypoints',points.slice(1,-1).map(coord).join('|'));
        return 'https://www.google.com/maps/dir/?'+params;
    }
    function showPlan(plan) {
        $('#trip-result').hidden=false;
        $('#trip-summary').textContent=`${plan.stops.length} museum stop${plan.stops.length === 1 ? '' : 's'} · ${plan.targets.length-plan.unmatched.length}/${plan.targets.length} aircraft choices covered · ${plan.total_straight_line_miles.toLocaleString()} straight-line miles`;
        if(!map)map=MuseumMap($('#trip-map'), {onTileError(){message($('#trip-tile-status'),'The background map could not load. Your itinerary and directions are still available.',true);}});
        map.map.invalidateSize();map.setMuseums(plan.stops.map(s=>s.museum),{numbered:true});
        const points=[plan.origin,...plan.stops.map(s=>s.museum)];if(plan.round_trip && plan.stops.length)points.push(plan.origin);
        map.setRoute(points.map(p=>[p.latitude,p.longitude]));
        if(!plan.stops.length)map.map.setView([plan.origin.latitude,plan.origin.longitude],7);
        const directions=$('#trip-directions');directions.replaceChildren();
        // At most 3 intermediate waypoints per link, including mobile browsers.
        for(let start=0,part=1;start<points.length-1;start+=4,part++) {
            const chunk=points.slice(start,start+5);
            directions.append(external(points.length<=5?'Open driving directions':`Directions · part ${part}`,routeUrl(chunk)));
        }
        const unmatched=$('#trip-unmatched');unmatched.replaceChildren();unmatched.hidden=!(plan.unmatched.length || plan.no_coordinates.length);
        if(plan.unmatched.length) {
            unmatched.append(el('h3','Still on your list'));
            plan.unmatched.forEach(t=>unmatched.append(el('p',`${t.label}: ${t.reason}`)));
        }
        if(plan.no_coordinates.length) {
            unmatched.append(el('h3','Matching museums without coordinates'));
            plan.no_coordinates.forEach(m=>{const p=el('p');p.append(link(m.name,`/museums/${m.id}`));unmatched.append(p);});
        }
        $('#trip-stops').replaceChildren();
        plan.stops.forEach((stop,index)=>{
            const card=el('article',null,'x-card');card.append(el('h2',`${index+1}. ${stop.museum.name}`),el('p',`${stop.museum.city}, ${stop.museum.country} · ${stop.leg_straight_line_miles} straight-line miles from ${index?'previous stop':'start'}`,'x-muted'));
            const wanted=el('p');stop.target_indexes.forEach(i=>wanted.append(el('span',plan.targets[i].label,'x-tag')));card.append(wanted);
            const aircraftList=el('ul');stop.aircraft.forEach(a=>{const item=el('li');item.append(link(`${a.full_designation} · ${a.tail_number || a.aircraft_name || 'Airframe #'+a.id}`,`/aircraft/${a.id}/history`));aircraftList.append(item);});card.append(aircraftList);
            const actions=el('div',null,'x-actions');actions.append(link('Museum collection',`/museums/${stop.museum.id}`,'x-button secondary'),external('Drive to this stop',routeUrl([points[index],points[index+1]])));
            if(stop.museum.website && /^https?:\/\//i.test(stop.museum.website))actions.append(external('Official museum site',stop.museum.website));card.append(actions);$('#trip-stops').append(card);
        });
        if(plan.round_trip && plan.stops.length)$('#trip-stops').append(el('p',`Return to start: ${plan.return_straight_line_miles} straight-line miles.`,'x-status'));
        message($('#trip-save-status'),'');
        $('#trip-result').scrollIntoView({behavior:'smooth',block:'start'});
    }
    async function build() {
        if(!targets.length)return message($('#trip-status'),'Add at least one aircraft or model.',true);
        const body={origin:{location:$('#trip-origin').value.trim()},targets,radius_miles:Number($('#trip-radius').value),max_stops:Number($('#trip-max-stops').value),round_trip:$('#trip-round').checked};
        const version=++revision;$('#trip-build').disabled=true;$('#trip-result').hidden=true;currentRequest=null;message($('#trip-status'),'Finding museum stops…');
        try {
            const plan=await api('/api/v1/trips/plan',{method:'POST',body:JSON.stringify(body)});
            if(version!==revision)return;
            currentRequest=JSON.parse(JSON.stringify(body));showPlan(plan);message($('#trip-status'),'Plan ready. Review the stops and any unmatched aircraft below.');
        }catch(error){if(version===revision)message($('#trip-status'),error.message,true);}
        finally{$('#trip-build').disabled=false;}
    }
    $('#trip-form').onsubmit=e=>{e.preventDefault();build();};
    $('#trip-form').addEventListener('input',invalidate);
    function readSaved() {
        try {const saved=JSON.parse(localStorage.getItem(storageKey)||'[]');return Array.isArray(saved)?saved.slice(0,10):[];}
        catch {message($('#trip-storage-status'),'Saved trips are unavailable in this browser.',true);return [];}
    }
    function writeSaved(saved) {
        try{localStorage.setItem(storageKey,JSON.stringify(saved));return true;}
        catch{message($('#trip-save-status'),'This browser could not save the trip. Storage may be disabled or full.',true);return false;}
    }
    function renderSaved() {
        const saved=readSaved();$('#trip-saved').replaceChildren();
        if(!saved.length)$('#trip-saved').append(el('p','No saved trips yet.','x-muted'));
        saved.forEach((trip,index)=>{
            if(!trip.request || !Array.isArray(trip.request.targets))return;
            const row=el('div',null,'x-actions'), load=el('button',trip.name || 'Saved trip','x-button secondary'), remove=el('button','Remove','x-button secondary');
            load.type=remove.type='button';
            load.onclick=()=>{
                targets=trip.request.targets.slice(0,12);$('#trip-origin').value=trip.request.origin?.location || '';$('#trip-radius').value=trip.request.radius_miles;$('#trip-max-stops').value=trip.request.max_stops;$('#trip-round').checked=Boolean(trip.request.round_trip);$('#trip-name').value=trip.name;invalidate();renderTargets();if($('#trip-form').reportValidity())build();
            };
            remove.onclick=()=>{saved.splice(index,1);if(writeSaved(saved))renderSaved();};row.append(load,remove);$('#trip-saved').append(row);
        });
    }
    $('#trip-save-form').onsubmit=e=>{
        e.preventDefault();if(!currentRequest)return;
        const name=$('#trip-name').value.trim();if(!name)return message($('#trip-save-status'),'Give your trip a name.',true);
        const saved=readSaved().filter(t=>t.name!==name);saved.unshift({name,request:currentRequest});
        if(writeSaved(saved.slice(0,10))){message($('#trip-save-status'),'Saved on this device. Up to 10 named trips are kept.');renderSaved();}
    };
    renderTargets();renderSaved();
    const initial=new URLSearchParams(location.search), id=initial.get('aircraft_id');
    if(/^\d+$/.test(id||''))api(`/api/v1/aircraft/${id}`).then(data=>add(exactTarget(data.aircraft))).catch(error=>message($('#trip-search-status'),error.message,true));
})();
