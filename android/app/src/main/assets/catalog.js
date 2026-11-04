(function (root) {
  'use strict';
  const text = value => String(value || '').toLocaleLowerCase();
  const compact = value => text(value).replace(/[^a-z0-9]/g, '');
  const located = m => typeof m.latitude === 'number' && typeof m.longitude === 'number' &&
    Number.isFinite(m.latitude) && Number.isFinite(m.longitude) && Math.abs(m.latitude) <= 90 && Math.abs(m.longitude) <= 180;
  function distance(a, b) {
    const rad = Math.PI / 180, lat = (b.latitude - a.latitude) * rad, lon = (b.longitude - a.longitude) * rad;
    const h = Math.sin(lat / 2) ** 2 + Math.cos(a.latitude * rad) * Math.cos(b.latitude * rad) * Math.sin(lon / 2) ** 2;
    return 3958.8 * 2 * Math.asin(Math.sqrt(Math.min(1, Math.max(0, h))));
  }
  function create(data) {
    const aircraft = new Map(data.aircraft.map(a => [a.id, a]));
    const museums = new Map(data.museums.map(m => [m.id, m]));
    const types = new Map(data.types.map(t => [t.id, t]));
    const aircraftText = new Map(data.aircraft.map(a => [a.id, text([a.manufacturer, a.model, a.variant, a.full_designation, a.tail_number, a.construction_number, a.model_name, a.aircraft_name, ...(a.aliases || [])].join(' '))]));
    function searchAircraft(query) {
      const q = text(query).trim(), c = compact(query);
      return data.aircraft.filter(a => !q || aircraftText.get(a.id).includes(q) ||
        (c && compact(a.full_designation || a.model).includes(c)));
    }
    function searchMuseums(query) {
      const q = text(query).trim();
      return data.museums.filter(m => text([m.name,m.city,m.state_province,m.country].join(' ')).includes(q));
    }
    function nearest(origin, {query='', includeRestricted=false}={}) {
      if (!located(origin)) throw Error('Enter valid latitude and longitude.');
      return searchMuseums(query).filter(m => located(m) && (includeRestricted || m.access_type !== 'restricted'))
        .map(m => ({museum:m, miles:distance(origin,m)})).sort((a,b) => a.miles-b.miles || a.museum.id-b.museum.id);
    }
    function plan({origin, targets, max_stops=5, radius_miles=500, round_trip=false}) {
      if (!located(origin)) throw Error('Choose a starting location or enter valid coordinates.');
      if (!Array.isArray(targets) || !targets.length || targets.length>12) throw Error('Choose between 1 and 12 aircraft or models.');
      if (!Number.isInteger(max_stops) || max_stops<1 || max_stops>8) throw Error('Choose between 1 and 8 stops.');
      if (!Number.isFinite(radius_miles) || radius_miles<1 || radius_miles>5000) throw Error('Radius must be between 1 and 5,000 miles.');
      const unique = [...new Map(targets.map(t => [t.kind==='airframe' ? 'a'+t.aircraft_id : 'm'+text(t.manufacturer)+'|'+text(t.model),t])).values()];
      const matches = unique.map(t => {
        if (t.kind==='airframe') {
          if (!aircraft.has(t.aircraft_id)) throw Error('An aircraft was removed from this catalog. Select it again.');
          return new Set([t.aircraft_id]);
        }
        if (t.kind!=='model') throw Error('Invalid target.');
        return new Set(data.aircraft.filter(a=>text(a.manufacturer)===text(t.manufacturer)&&text(a.model)===text(t.model)).map(a=>a.id));
      });
      const candidates = new Map();
      const reasons = matches.map(ids=>!ids.size?'No matching aircraft in the catalog.':'No recorded on-display exhibit.');
      matches.forEach((ids,i)=>{
        const links=data.exhibits.filter(e=>ids.has(e.aircraft_id)&&e.display_status==='on_display'&&museums.get(e.museum_id)?.access_type!=='restricted');
        if(links.length) reasons[i]=links.every(e=>!located(museums.get(e.museum_id)))?'Matching museums have no coordinates.':'No located match within the search radius.';
        links.forEach(e=>{
          const m=museums.get(e.museum_id);
          if(!m || !located(m) || distance(origin,m)>radius_miles)return;
          reasons[i]='Not included within your stop limit.';
          if(!candidates.has(m.id))candidates.set(m.id,{museum:m,targets:new Set(),aircraft:new Map()});
          candidates.get(m.id).targets.add(i);candidates.get(m.id).aircraft.set(e.aircraft_id,aircraft.get(e.aircraft_id));
        });
      });
      let remaining=new Set(matches.map((_,i)=>i)),selected=[],point=origin;
      while(selected.length<max_stops) {
        const count=c=>[...c.targets].filter(i=>remaining.has(i)).length;
        const choices=[...candidates.values()].filter(c=>count(c)).sort((a,b)=>count(b)-count(a)||distance(point,a.museum)-distance(point,b.museum)||a.museum.id-b.museum.id);
        if(!choices.length)break;
        const chosen=choices[0];selected.push(chosen);chosen.targets.forEach(i=>remaining.delete(i));point=chosen.museum;
      }
      point=origin;let total=0;const stops=[];
      while(selected.length) {
        selected.sort((a,b)=>distance(point,a.museum)-distance(point,b.museum)||a.museum.id-b.museum.id);
        const chosen=selected.shift(), miles=distance(point,chosen.museum);total+=miles;
        stops.push({museum:chosen.museum,aircraft:[...chosen.aircraft.values()],target_indexes:[...chosen.targets],leg_straight_line_miles:Math.round(miles*10)/10});point=chosen.museum;
      }
      if(round_trip && stops.length)total+=distance(point,origin);
      return {origin,targets:unique,stops,radius_miles,max_stops,round_trip,total_straight_line_miles:Math.round(total*10)/10,
        unmatched:[...remaining].map(i=>({label:unique[i].label,reason:reasons[i]})),catalog_id:data.meta.catalog_id,revision:data.meta.revision};
    }
    return {data,aircraft,museums,types,searchAircraft,searchMuseums,nearest,plan};
  }
  root.OfflineCatalog = {create,distance,located};
  if(typeof module!=='undefined')module.exports=root.OfflineCatalog;
})(globalThis);
