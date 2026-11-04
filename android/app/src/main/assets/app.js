/* Offline UI. Styles and globe are copied from the website at build time. */
'use strict';
const $ = selector => document.querySelector(selector);
const escHtml = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
window.escHtml = escHtml;
const pretty = value => String(value || '—').replace(/_/g,' ').replace(/\b\w/g,c=>c.toUpperCase());
const label = a => [a.full_designation || a.model, a.tail_number || a.aircraft_name].filter(Boolean).join(' · ');
const place = m => [m.city,m.state_province,m.country].filter(Boolean).join(', ');
const safeUrl = value => { try { const u=new URL(value);return ['https:','http:'].includes(u.protocol)&&!u.username&&!u.password ? u.href:null; }catch{return null;} };
const source = (url,name='Source') => safeUrl(url) ? `<a href="${escHtml(safeUrl(url))}">${escHtml(name)} <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></a>`:'';
const head = (title, subtitle, icon) => `<div class="m-page-header"><h1><i class="fa-solid fa-${icon}" aria-hidden="true"></i> ${escHtml(title)}</h1><p class="m-subtitle">${escHtml(subtitle)}</p></div>`;
const empty = text => `<p class="muted">${escHtml(text)}</p>`;
const card = (title,body) => `<section class="m-card"><h2>${escHtml(title)}</h2>${body}</section>`;
const pill = text => `<span class="pill">${escHtml(text)}</span>`;
const fmt = number => Number(number).toLocaleString();
const pending = new Map(); let serial=0, model, catalog, globe, status={}, targets=[], currentTrip=null;
const draft = {latitude:'',longitude:'',radius:500,stops:5,round:false};
function native(action, extra={}) {
  return new Promise((resolve,reject)=>{
    if(!window.AircraftNative)return reject(Error('Android integration is unavailable.'));
    const id=String(++serial), timer=setTimeout(()=>{pending.delete(id);reject(Error('The operation timed out.'));},35000);
    pending.set(id,{resolve,reject,timer});
    AircraftNative.postMessage(JSON.stringify({id,action,...extra}));
  });
}
if(window.AircraftNative) AircraftNative.onmessage=event=>{
  const message=JSON.parse(event.data), item=pending.get(message.id);if(!item)return;
  clearTimeout(item.timer);pending.delete(message.id);
  if(message.result.error && !Object.hasOwn(message.result,'revision'))item.reject(Error(message.result.error));else item.resolve(message.result);
};
let noticeTimer;
function notice(message) { $('#notice').textContent=message;$('#notice').hidden=false;clearTimeout(noticeTimer);noticeTimer=setTimeout(()=>$('#notice').hidden=true,6500); }
function route() {
  try { return new URL((location.hash.slice(1)||'/'),location.origin); }catch {return new URL('/',location.origin);}
}
function navigate(path) {location.hash=path;}
function aircraftCard(a, extra='') {
  return `<a class="m-list-item" href="#/aircraft/${a.id}"><div class="m-list-title">${escHtml(a.full_designation || a.model)} ${a.tail_number?pill(a.tail_number):''}</div><div class="m-list-meta">${escHtml([a.manufacturer,a.model_name,a.aircraft_name].filter(Boolean).join(' · '))}</div>${extra}</a>`;
}
function museumCard(m,extra='') {
  return `<a class="m-list-item" href="#/museums/${m.id}"><div class="m-list-title">${escHtml(m.name)}</div><div class="m-list-meta">${escHtml(place(m))}${m.access_type!=='public'?pill(pretty(m.access_type)):''}</div>${extra}</a>`;
}
function searchForm(q,placeholder,filters='') {
  return `<form id="search-form"><div class="m-search"><input name="q" aria-label="Search" value="${escHtml(q)}" placeholder="${escHtml(placeholder)}"><button aria-label="Search"><i class="fa-solid fa-magnifying-glass"></i></button></div>${filters}</form>`;
}
function options(values,selected,all) {return `<option value="">${escHtml(all)}</option>`+values.map(v=>`<option value="${escHtml(v)}" ${v===selected?'selected':''}>${escHtml(v)}</option>`).join('');}
function bindSearch(path) {$('#search-form').onsubmit=e=>{e.preventDefault();navigate(path+'?'+new URLSearchParams(new FormData(e.target)));};}
function paged(rows,render,params) {
  const pages=Math.max(1,Math.ceil(rows.length/30)), page=Math.max(1,Math.min(pages,Number(params.get('page'))||1));
  return (rows.slice((page-1)*30,page*30).map(row=>render(row)).join('')||empty('No matching records in this offline copy.'))+
    `<div class="pager"><button data-page="${page-1}" ${page===1?'disabled':''}>Previous</button><span>${page} / ${pages}</span><button data-page="${page+1}" ${page===pages?'disabled':''}>Next</button></div>`;
}
function dashboard() {
  $('#content').innerHTML=head('Dashboard','Find historic aircraft and the museums that display them.','gauge-high')+
    `<span class="offline-badge"><i class="fa-solid fa-circle-check"></i> Catalog available offline</span>
    <div class="m-stats"><a class="m-stat" href="#/aircraft"><div class="m-stat-icon"><i class="fa-solid fa-jet-fighter"></i></div><div><div class="m-stat-num">${fmt(catalog.aircraft.length)}</div><div class="m-stat-label">Aircraft</div></div></a>
    <a class="m-stat" href="#/museums"><div class="m-stat-icon"><i class="fa-solid fa-building-columns"></i></div><div><div class="m-stat-num">${fmt(catalog.museums.length)}</div><div class="m-stat-label">Museums</div></div></a>
    <a class="m-stat m-stat-wide" href="#/globe"><div class="m-stat-icon"><i class="fa-solid fa-globe"></i></div><div><div class="m-stat-num">${new Set(catalog.museums.map(m=>m.country)).size}</div><div class="m-stat-label">Countries · Explore the globe</div></div></a></div>`+
    card('Quick search',searchForm('','Aircraft, model, alias, or tail number'))+
    card('Explore nearby',`<p>Find public museums using your location, or choose coordinates without a connection.</p><div class="actions"><a class="m-btn" href="#/near-me"><i class="fa-solid fa-location-dot"></i> Near Me</a><a class="m-btn secondary" href="#/trips"><i class="fa-solid fa-route"></i> Plan a trip</a></div>`)+
    card('Your offline copy',`<p class="muted">${escHtml(catalog.meta.source)}</p><p class="muted">Generated ${escHtml(new Date(catalog.meta.generated_at).toLocaleDateString())}. Museum access and displays can change; check before visiting.</p><div class="actions"><a class="m-btn secondary" href="#/settings">Data & updates</a></div>`);
  bindSearch('/aircraft');
}
function directory(kind,params) {
  const isAircraft=kind==='aircraft',q=params.get('q')||'',country=params.get('country')||'',sort=params.get('sort')||'name';
  let rows=isAircraft?model.searchAircraft(q):model.searchMuseums(q);
  if(country)rows=rows.filter(m=>m.country===country);
  rows.sort((a,b)=>String(sort==='manufacturer'?a.manufacturer:sort==='tail'?a.tail_number:isAircraft?(a.full_designation||a.model):a.name).localeCompare(String(sort==='manufacturer'?b.manufacturer:sort==='tail'?b.tail_number:isAircraft?(b.full_designation||b.model):b.name),undefined,{numeric:true})||a.id-b.id);
  const sortOptions=isAircraft?['name','manufacturer','tail']:['name'];
  const filters=`<div class="filters">${!isAircraft?`<label>Country<select name="country">${options([...new Set(catalog.museums.map(m=>m.country))].sort(),country,'All countries')}</select></label>`:''}<label>Sort<select name="sort">${sortOptions.map(v=>`<option value="${v}" ${sort===v?'selected':''}>${pretty(v)}</option>`).join('')}</select></label></div>`;
  $('#content').innerHTML=head(isAircraft?'Aircraft':'Museums',`${fmt(rows.length)} records in your offline catalog.`,isAircraft?'jet-fighter':'building-columns')+
    (!isAircraft?'<div class="actions"><a class="m-btn secondary" href="#/globe"><i class="fa-solid fa-globe"></i> Discovery globe</a></div>':'')+
    card('Search & filter',searchForm(q,isAircraft?'Model, name, alias, tail #':'Museum, city, or country',filters))+card('Directory',paged(rows,isAircraft?aircraftCard:museumCard,params));
  bindSearch('/'+kind);
}
function specs(row,fields) {return '<dl class="specs">'+fields.filter(([key])=>row[key]!=null&&row[key]!=='').map(([key,title])=>`<div><dt>${escHtml(title)}</dt><dd>${escHtml(pretty(row[key]))}</dd></div>`).join('')+'</dl>';}
function aircraftDetail(id) {
  const a=model.aircraft.get(id);if(!a)return missing();
  const type=model.types.get(a.type_id),links=catalog.exhibits.filter(e=>e.aircraft_id===id),history=catalog.history.filter(h=>h.aircraft_id===id);
  $('#content').innerHTML=`<a class="d-back" href="#/aircraft">← Back to aircraft</a>`+head(label(a),[a.manufacturer,a.model_name,a.aircraft_name].filter(Boolean).join(' · '),'jet-fighter')+
    `<div class="actions"><button class="m-btn" data-add="${id}"><i class="fa-solid fa-plus"></i> Add to trip</button><a class="m-btn secondary" href="https://airplane.museum/admin/aircraft">Edit online</a></div>`+
    card('Airframe details',specs(a,[['manufacturer','Manufacturer'],['model','Model'],['variant','Variant'],['tail_number','Registration'],['construction_number','Construction number'],['operator_country','Operator'],['year_built','Year built'],['aircraft_type','Type'],['role_type','Role']]))+
    (type?card('About the '+(type.designation||type.display_name),`<p class="prose">${escHtml(type.description)}</p><div class="actions">${source(type.source_url,type.source_name||'Source')}${source(type.wikipedia_url,'Wikipedia')}</div>`+specs(type,[['first_flight_year','First flight'],['number_built','Number built'],['crew','Crew'],['engines','Powerplant'],['max_speed_kmh','Max speed (km/h)'],['range_km','Range (km)']])):'')+
    (a.description?card('About this airframe',`<p class="prose">${escHtml(a.description)}</p>`):'')+
    card('Museum locations',links.map(e=>museumCard(model.museums.get(e.museum_id),`<div>${pill(pretty(e.display_status))}</div>`)).join('')||empty('No museum location recorded in this copy.'))+
    (a.aliases?.length?card('Also known as',a.aliases.map(pill).join('')):'')+
    card('History',history.sort((x,y)=>(x.event_year||0)-(y.event_year||0)||x.id-y.id).map(h=>`<div class="stop"><h3>${escHtml(h.event_year||'Date unknown')} · ${escHtml(h.title)}</h3><p class="prose">${escHtml(h.description)}</p>${source(h.source_url,h.source_name||'Source')}</div>`).join('')||empty('No published milestones in this copy.'));
}
function museumDetail(id) {
  const m=model.museums.get(id);if(!m)return missing();
  const links=catalog.exhibits.filter(e=>e.museum_id===id);
  $('#content').innerHTML=`<a class="d-back" href="#/museums">← Back to museums</a>`+head(m.name,place(m),'building-columns')+
    card('Visiting',`<p>${pill(pretty(m.access_type||'public'))}</p><p>${escHtml(m.address||'Address not recorded.')}</p><p class="muted">Confirm opening times and visitor access before traveling.</p><div class="actions">${source(m.website,'Museum website')}${OfflineCatalog.located(m)?source(`https://www.google.com/maps/dir/?api=1&destination=${m.latitude},${m.longitude}`,'Directions online'):''}</div>${OfflineCatalog.located(m)?`<button class="m-btn secondary" data-start="${id}">Start a trip here</button>`:''}`)+
    card(`Collection · ${links.length}`,links.map(e=>aircraftCard(model.aircraft.get(e.aircraft_id),pill(pretty(e.display_status)))).join('')||empty('No aircraft recorded in this copy.'));
}
function originFields() {return `<div class="filters"><label>Latitude<input class="m-input" name="latitude" type="number" min="-90" max="90" step="any" required value="${escHtml(draft.latitude)}"></label><label>Longitude<input class="m-input" name="longitude" type="number" min="-180" max="180" step="any" required value="${escHtml(draft.longitude)}"></label></div><div class="actions"><button type="button" class="m-btn secondary" data-location="1"><i class="fa-solid fa-location-crosshairs"></i> Use my location</button><a class="m-btn secondary" href="#/museums">Choose a museum</a></div><p class="muted">Location can work offline. New city/postal-code lookup requires the website.</p>`;}
function readOrigin(form) {const values=new FormData(form);if(values.get('latitude')===''||values.get('longitude')==='')throw Error('Enter both coordinates.');draft.latitude=Number(values.get('latitude'));draft.longitude=Number(values.get('longitude'));return {latitude:draft.latitude,longitude:draft.longitude};}
function nearMe() {
  $('#content').innerHTML=head('Near Me','Find museums from your offline catalog.','location-dot')+card('Starting location',`<form id="near-form">${originFields()}<label><input name="restricted" type="checkbox"> Include restricted sites</label><button class="m-btn" type="submit">Find nearby museums</button></form>`)+`<section class="m-card" id="near-results" aria-live="polite">${empty('Choose your location to see distances.')}</section>`;
  $('#near-form').onsubmit=e=>{e.preventDefault();try {const results=model.nearest(readOrigin(e.target),{includeRestricted:e.target.elements.restricted.checked});$('#near-results').innerHTML=results.slice(0,50).map(r=>museumCard(r.museum,pill(r.miles.toFixed(1)+' mi'))).join('')||empty('No located museums in this copy.');}catch(error){notice(error.message);}};
}
function facts() {
  const rows=catalog.facts;
  $('#content').innerHTML=head('Facts',rows.length?'Published aviation facts, available offline.':'Type notes from your bundled catalog. Published facts arrive with a website snapshot.','lightbulb')+
    (rows.length?rows.map(f=>card('Did you know?',`<p class="prose">${escHtml(f.fact)}</p><div class="actions">${source(f.source_url)}${f.aircraft_id?`<a href="#/aircraft/${f.aircraft_id}">View aircraft</a>`:''}</div>`)).join(''):
      catalog.types.slice(0,15).map(t=>card(t.display_name,`<p>${escHtml((t.description||'').split('\n\n')[0])}</p><div class="actions">${source(t.wikipedia_url||t.source_url)}</div>`)).join(''));
}
function tripTargets() {return targets.map((t,i)=>`<div class="target"><span>${escHtml(t.label)}</span><button data-remove="${i}" aria-label="Remove ${escHtml(t.label)}">×</button></div>`).join('')||empty('Find an aircraft below or add one from its detail page.');}
async function trips() {
  $('#content').innerHTML=head('Trip Planner','Choose aircraft, find museums, and save an itinerary offline.','route')+
    card('Aircraft to see',`<div id="targets">${tripTargets()}</div><form id="trip-search" class="m-search"><input name="q" aria-label="Find aircraft for trip" placeholder="Search aircraft or model"><button aria-label="Search aircraft"><i class="fa-solid fa-search"></i></button></form><div id="trip-matches"></div>`)+
    card('Plan your visit',`<form id="trip-form">${originFields()}<div class="filters"><label>Radius (miles)<input name="radius" type="number" min="1" max="5000" value="${draft.radius}" required></label><label>Maximum stops<input name="stops" type="number" min="1" max="8" value="${draft.stops}" required></label></div><label><input name="round" type="checkbox" ${draft.round?'checked':''}> Return to start</label><button class="m-btn" type="submit">Build offline itinerary</button></form>`)+
    `<div id="trip-result"></div>`+card('Saved trips','<div id="saved-trips">Loading…</div>');
  $('#trip-search').onsubmit=e=>{e.preventDefault();const rows=model.searchAircraft(new FormData(e.target).get('q')).slice(0,8);$('#trip-matches').innerHTML=rows.map(a=>`<div class="m-list-item"><div class="m-list-title">${escHtml(label(a))}</div><div class="actions"><button class="m-btn secondary" data-add="${a.id}">This airframe</button><button class="m-btn secondary" data-model="${a.id}">Any ${escHtml(a.model)}</button></div></div>`).join('')||empty('No matches.');};
  $('#trip-form').onsubmit=e=>{e.preventDefault();try {
    const origin=readOrigin(e.target),form=new FormData(e.target);draft.radius=Number(form.get('radius'));draft.stops=Number(form.get('stops'));draft.round=form.has('round');
    currentTrip=model.plan({origin,targets,max_stops:draft.stops,radius_miles:draft.radius,round_trip:draft.round});renderTrip(currentTrip);
  }catch(error){notice(error.message);}};
  if(currentTrip)renderTrip(currentTrip);
  await savedTrips();
}
function sketch(trip) {
  const points=[trip.origin,...trip.stops.map(s=>s.museum),...(trip.round_trip?[trip.origin]:[])];
  const lats=points.map(p=>p.latitude),lons=points.map(p=>p.longitude),a=Math.min(...lats),b=Math.max(...lats),c=Math.min(...lons),d=Math.max(...lons);
  const xy=points.map(p=>[20+(p.longitude-c)/(d-c||1)*280,145-(p.latitude-a)/(b-a||1)*120]);
  return `<svg class="trip-map" viewBox="0 0 320 170" role="img" aria-label="Straight-line itinerary sketch, not a road map"><polyline points="${xy.map(p=>p.join(',')).join(' ')}" fill="none" stroke="#3b82f6" stroke-width="2"/>${xy.map(([x,y],i)=>`<circle cx="${x}" cy="${y}" r="5" fill="#06b6d4"/><text x="${x+7}" y="${y-7}">${i===0?'Start':trip.round_trip&&i===xy.length-1?'':i}</text>`).join('')}</svg>`;
}
function renderTrip(trip) {
  const stale=trip.catalog_id!==catalog.meta.catalog_id||trip.revision!==catalog.meta.revision;
  $('#trip-result').innerHTML=card(trip.name||'Your itinerary',
    (stale?'<p class="sync-error">Saved using an older catalog. This itinerary is preserved; verify current museum access and displays.</p>':'')+
    `<p><strong>${trip.stops.length} stops · ${fmt(trip.total_straight_line_miles)} mi</strong></p><p class="muted">Straight-line estimate, not driving distance. Street maps and road directions open online.</p>`+
    (trip.stops.length?sketch(trip):empty('No eligible museums matched within this radius.'))+
    trip.stops.map((s,i)=>`<div class="stop"><h3>${i+1}. ${escHtml(s.museum.name)}</h3><p class="muted">${escHtml(place(s.museum))} · ${s.leg_straight_line_miles} mi from previous stop</p><p>${escHtml(s.aircraft.map(label).join(', '))}</p>${source(`https://www.google.com/maps/dir/?api=1&destination=${s.museum.latitude},${s.museum.longitude}`,'Driving directions online')}</div>`).join('')+
    (trip.unmatched||[]).map(m=>`<p class="muted">${escHtml(m.label)}: ${escHtml(m.reason)}</p>`).join('')+
    (trip.stops.length?`<form id="save-trip" class="m-search"><input name="name" aria-label="Trip name" placeholder="Name this trip" maxlength="100" required value="${escHtml(trip.name||'')}"><button>Save</button></form>`:''));
  if($('#save-trip'))$('#save-trip').onsubmit=async e=>{e.preventDefault();try {await native('saveTrip',{trip:{...trip,name:new FormData(e.target).get('name').trim()}});notice('Trip saved on this device.');await savedTrips();}catch(error){notice(error.message);}};
}
async function savedTrips() {
  try {const result=await native('trips');if(!$('#saved-trips'))return;
    $('#saved-trips').innerHTML=result.trips.map((t,i)=>`<div class="target"><button class="m-btn secondary" data-load-trip="${i}">${escHtml(t.name)} · ${t.stops.length} stops</button><button data-delete-trip="${escHtml(t.id)}" aria-label="Delete ${escHtml(t.name)}"><i class="fa-solid fa-trash"></i></button></div>`).join('')||empty('No saved trips yet.');
    $('#saved-trips').querySelectorAll('[data-load-trip]').forEach(button=>button.onclick=()=>{currentTrip=result.trips[Number(button.dataset.loadTrip)];renderTrip(currentTrip);$('#trip-result').scrollIntoView({behavior:'smooth'});});
  }catch(error){if($('#saved-trips'))$('#saved-trips').textContent=error.message;}
}
function settings() {
  $('#content').innerHTML=head('Offline data','Your catalog stays available when the network disappears.','cloud-arrow-down')+
    card('Catalog on this device',`<p>${escHtml(catalog.meta.source)}</p><p class="muted">Generated ${escHtml(new Date(catalog.meta.generated_at).toLocaleString())}</p><p>${fmt(catalog.aircraft.length)} aircraft · ${fmt(catalog.museums.length)} museums</p><div id="sync-status" aria-live="polite"></div><div class="actions"><button class="m-btn" data-sync="1">Update now</button></div><p class="muted">Updates run when connected, subject to Android battery and background limits. Failed updates retain your previous catalog and saved trips.</p>`)+
    card('Online editing',`<p>Sign in on the website to edit catalog records. Offline edits are not queued.</p><div class="actions"><a class="m-btn secondary" href="https://airplane.museum/admin">Open management website</a></div>`)+
    card('About',`<p>Aircraft Finder ${escHtml('0.1.0')}</p><p class="muted">The same mobile styling and globe as airplane.museum. Catalog text is stored on this device; location is requested only when you choose it. Saved trips stay on this device.</p><p>${source('https://airplane.museum','Visit website')}</p>`);
  updateStatus();
}
function updateStatus() {
  if(!$('#sync-status'))return;
  $('#sync-status').innerHTML=(status.running?'<p class="offline-badge">Downloading and checking an update…</p>':'')+
    (status.last_checked?`<p class="muted">Last checked ${escHtml(new Date(status.last_checked).toLocaleString())}</p>`:'<p class="muted">No successful server check yet.</p>')+
    (status.error?`<p class="sync-error">${escHtml(status.error)}</p>`:'');
}
function missing() {$('#content').innerHTML=head('Record unavailable','This record is not in the current offline copy.','circle-info')+'<a class="m-btn" href="#/">Back to dashboard</a>';}
async function render() {
  if(!catalog)return;const {pathname,searchParams}=route(),parts=pathname.split('/').filter(Boolean);
  $('#content').hidden=pathname==='/globe';$('#globe-page').hidden=pathname!=='/globe';
  document.querySelectorAll('[data-tab]').forEach(tab=>{const active=tab.dataset.tab===(parts[0]==='globe'?'museums':parts[0]||'home');tab.classList.toggle('active',active);if(active)tab.setAttribute('aria-current','page');else tab.removeAttribute('aria-current');});
  window.scrollTo(0,0);
  if(pathname==='/')dashboard();
  else if(['aircraft','museums'].includes(parts[0]))parts[1]?(parts[0]==='aircraft'?aircraftDetail:museumDetail)(Number(parts[1])):directory(parts[0],searchParams);
  else if(pathname==='/near-me')nearMe();
  else if(pathname==='/facts')facts();
  else if(pathname==='/trips')await trips();
  else if(pathname==='/settings')settings();
  else if(pathname==='/globe') {if(!globe)globe=initMuseumGlobe({prefix:'m-',mobile:true});globe?.resize();}
  else missing();
}
document.addEventListener('click',async event=>{
  const button=event.target.closest('button'),anchor=event.target.closest('a');
  if(anchor && /^\/museums\/\d+$/.test(anchor.getAttribute('href')||'')) {event.preventDefault();navigate(anchor.getAttribute('href'));return;}
  if(!button)return;
  try {
    if(button.dataset.page){const u=route();u.searchParams.set('page',button.dataset.page);navigate(u.pathname+u.search);}
    if(button.dataset.add||button.dataset.model){
      const a=model.aircraft.get(Number(button.dataset.add||button.dataset.model));
      const target=button.dataset.model?{kind:'model',manufacturer:a.manufacturer,model:a.model,label:`${a.manufacturer} ${a.model} · any variant`}:{kind:'airframe',aircraft_id:a.id,label:label(a)};
      const key=t=>t.kind==='model'?t.manufacturer+'|'+t.model:String(t.aircraft_id);
      if(targets.some(t=>key(t)===key(target)))return notice('Already in your trip.');
      if(targets.length>=12)return notice('A trip can include up to 12 targets.');
      targets.push(target);currentTrip=null;if($('#targets'))$('#targets').innerHTML=tripTargets();if($('#trip-result'))$('#trip-result').innerHTML='';notice('Added to your trip.');
    }
    if(button.dataset.remove!==undefined){targets.splice(Number(button.dataset.remove),1);currentTrip=null;$('#targets').innerHTML=tripTargets();$('#trip-result').innerHTML='';}
    if(button.dataset.start){const m=model.museums.get(Number(button.dataset.start));draft.latitude=m.latitude;draft.longitude=m.longitude;navigate('/trips');}
    if(button.dataset.location){button.disabled=true;const point=await native('location');draft.latitude=point.latitude;draft.longitude=point.longitude;document.querySelectorAll('[name="latitude"]').forEach(e=>e.value=point.latitude);document.querySelectorAll('[name="longitude"]').forEach(e=>e.value=point.longitude);notice('Location updated.');}
    if(button.dataset.sync){await native('sync');notice('Update queued. Android will run it when a network is available.');await poll();}
    if(button.dataset.deleteTrip){await native('deleteTrip',{tripId:button.dataset.deleteTrip});await savedTrips();}
  } catch(error){notice(error.message);}finally{button.disabled=false;}
});
async function loadCatalog(){const response=await fetch('/api/catalog');if(!response.ok)throw Error('Could not open the local catalog.');catalog=await response.json();model=OfflineCatalog.create(catalog);}
async function poll(){try {
  status=await native('status');
  if(status.revision&&catalog&&status.revision!==catalog.meta.revision){
    // The shared globe caches its points. Reload the whole local view so maps,
    // details and search all use one revision, preserving the current itinerary.
    sessionStorage.setItem('offlineUiState',JSON.stringify({catalog_id:catalog.meta.catalog_id,targets,draft,currentTrip}));
    location.reload();return;
  }
  updateStatus();
}catch{/* Local browsing remains usable when background status is unavailable. */}}
window.addEventListener('hashchange',()=>render().catch(e=>notice(e.message)));
loadCatalog().then(()=>{
  try {
    const saved=JSON.parse(sessionStorage.getItem('offlineUiState')||'null');
    sessionStorage.removeItem('offlineUiState');
    if(saved){
      Object.assign(draft,saved.draft);currentTrip=saved.currentTrip;
      targets=saved.catalog_id===catalog.meta.catalog_id?saved.targets.filter(t=>t.kind==='model'||model.aircraft.has(t.aircraft_id)):[];
      notice('Catalog updated. Your saved trips are unchanged.');
    }
  }catch{/* A corrupt transient UI draft must not prevent opening the catalog. */}
  return render();
}).then(()=>poll()).catch(error=>{$('#content').innerHTML=card('Could not open the catalog',`<p>${escHtml(error.message)}</p><p>Close and reopen the app. Your existing data is retained.</p>`);});
setInterval(poll,5000);
