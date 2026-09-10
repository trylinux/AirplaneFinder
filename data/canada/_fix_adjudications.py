import csv,os,glob
D='/home/claude/AirplaneFinder/data/canada'; os.chdir(D)
def load(p):
    with open(p,newline='',encoding='utf-8') as f: r=csv.DictReader(f); return r.fieldnames,list(r)
def save(p,h,rows):
    with open(p,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=h,lineterminator='\n'); w.writeheader(); w.writerows(rows)
def drop_row(p,tail,model,note):
    h,rows=load(p)
    k=[r for r in rows if not ((r['tail_number'] or '').strip()==tail and r['model'].strip()==model)]
    assert len(k)<len(rows),(p,tail,model)
    if k: save(p,h,k); print(f'  drop row {model} {tail:8s} from {p:55s} {note}')
    else: os.remove(p); print(f'  drop row {model} {tail:8s} — file now empty, removed {p}')
    return not k

# ---- whole sites recorded twice: keep the richer copy
DROP_SITES=[
 ('19_wing_comox_air_force_museum_aircraft.csv','Comox Air Force Museum and Airpark, 19 Wing Comox','kept the 14-row "Comox Air Force Museum and Heritage Air Park"'),
 ('east__air_force_heritage_park_summerside_aircraft.csv','Air Force Heritage Park, Summerside','kept the bases package copy'),
 ('canadian_harvard_aircraft_association_aircraft.csv','Canadian Harvard Aircraft Association','kept the 13-row Tillsonburg copy'),
 ('college_militaire_royal_de_saint_jean_canuck_aircraft.csv','Collège militaire royal de Saint-Jean Canuck','the Canuck is inside the CFB Saint-Jean / CMR Saint-Jean record'),
 ('miramichi_airport_voodoo_aircraft.csv','Miramichi Airport Voodoo','kept "Former CFB Chatham CF-101 Voodoo, Miramichi", which names the base'),
 ('kf_centre_for_excellence_aircraft.csv','KF Centre for Excellence','kept "KF Centre for Excellence, Kelowna"'),
 ('rcmp_heritage_centre_regina_aircraft.csv','RCMP Heritage Centre','kept "RCMP Heritage Centre, Regina"'),
 ('west__saskatchewan_aviation_museum_aircraft.csv','Saskatchewan Aviation Museum, Saskatoon','kept the 25-row museums copy'),
 ('the_military_museums_calgary_aircraft.csv','The Military Museums','kept the 11-row "The Military Museums, Calgary"'),
 ('royal_military_college_of_canada_kingston_aircraft.csv','Royal Military College of Canada, Kingston','kept "Royal Military College of Canada Aircraft Displays, Kingston"'),
 ('val_d_or_service_culturel_silver_star_aircraft.csv',"Val-d'Or Service Culturel Silver Star",'kept "Val-d\'Or CT-133 Silver Star Monument"'),
 ('rcafa_441_wing_silver_star_barrie_aircraft.csv','RCAFA 441 Wing Silver Star, Barrie','Skaarup records the Silver Star as moved to Base Borden, where it is recorded'),
 ('barrie_paintball_silver_star_angus_aircraft.csv','Barrie Paintball Silver Star, Angus','133581 is recorded with the Canadian Air and Space Conservancy at Edenvale'),
 ('musee_defense_aerienne_bagotville_aircraft.csv',None,'second file for the same Bagotville museum name'),
]
drop_names=set()
for fn,mus,why in DROP_SITES:
    if os.path.exists(fn): os.remove(fn); print(f'  drop site {fn:58s} {why}')
    if mus: drop_names.add(mus)
h,rows=load('ca_museums.csv'); keep=[]; seen=set()
for r in rows:
    if r['name'] in drop_names: print('  drop museum row',r['name']); continue
    if r['name'] in seen: print('  drop duplicate museum row',r['name'],r['city']); continue
    seen.add(r['name']); keep.append(r)
save('ca_museums.csv',h,keep)

# ---- one airframe claimed by two different sites: the specific first-party record wins
drop_row('comox_air_force_museum_aircraft.csv','114115','CT-114','-> Comox Valley Visitor Centre pylon (own site + Wikipedia display list)')
drop_row('4_wing_cold_lake_air_park_aircraft.csv','114083','CT-114','-> Joe Heffner Memorial Park, the serialled claim')
drop_row('8_wing_trenton_gate_guardians_aircraft.csv','116739','CF-116','-> the museum RCAF Memorial Airpark, per its own Sept 2026 collection listing')
drop_row('norwood_tutor_collection_aircraft.csv','114187','CT-114','-> Creston Millennium Park, which has the full taken-on-strength chain')
drop_row('jet_aircraft_museum_aircraft.csv','133648','CT-133','-> Princeton Airport weathervane (town own page + Skaarup)')
drop_row('wdm_moose_jaw_aircraft.csv','114078','CT-114','-> Moose Jaw Visitor Centre, installed 2009')
drop_row('reynolds_alberta_museum_aircraft.csv','134232','CT-134','-> Wetaskiwin Legion pylon (Skaarup)')

# ---- two more sites recorded twice under different names
for fn,mus,why in [
 ('greenwood_military_aviation_museum_aircraft.csv','Greenwood Military Aviation Museum','kept the 14-row "…, 14 Wing Greenwood" copy'),
 ('base_borden_military_museum_aircraft.csv','Base Borden Military Museum','kept the 25-row "…, 16 Wing Borden" copy')]:
    if os.path.exists(fn): os.remove(fn); print(f'  drop site {fn:58s} {why}')
    h,rows=load('ca_museums.csv'); save('ca_museums.csv',h,[r for r in rows if r['name']!=mus]); print('  drop museum row',mus)

# ---- one airframe, two sites. Rule: a dated first-party museum listing beats a
# third-party survey, and a public display beats a restricted instructional airframe.
for p,tail,model,note in [
 ('southport_aerospace_centre_aircraft.csv','134201','CT-134','-> National Air Force Museum (own Sept 2026 listing)'),
 ('cfsate_borden_aircraft.csv','114021','CT-114','-> WDM Moose Jaw; a public display beats a restricted training airframe'),
 ('cfsate_borden_aircraft.csv','114063','CT-114','-> Memorial Military Museum Campbellford, on public display'),
 ('cfsate_borden_aircraft.csv','144614','CC-144','-> Musee de l aviation de Montreal, displayed outdoors 28 July 2026'),
 ('canadian_war_museum_aircraft.csv','P8332','Spitfire','-> Canada Aviation and Space Museum, from its own pages'),
 ('bagotville_musee_defense_aerienne_aircraft.csv','104704','CF-104','-> Musee de l aviation de Montreal (own page, Sept 2026)'),
 ('15_wing_moose_jaw_aircraft.csv','134230','CT-134','-> WDM Moose Jaw; the 15 Wing claim is unconfirmed'),
 ('canadian_air_and_space_conservancy_aircraft.csv','134220','CT-134','-> Memorial Military Museum Campbellford'),
 ('17_wing_winnipeg_air_park_aircraft.csv','114004','CT-114','-> Royal Aviation Museum of Western Canada, a permanent loan'),
 ('cold_lake_air_force_museum_aircraft.csv','133413','CT-133','-> The Military Museums Calgary, outside the Cold War Hangar'),
 ('canadian_harvard_aircraft_association_tillsonburg_aircraft.csv','133263','CT-133','-> Jet Aircraft Museum, the CT-133 operator'),
 ('canadian_harvard_aircraft_association_tillsonburg_aircraft.csv','133441','CT-133','-> Jet Aircraft Museum, the CT-133 operator'),
 ('jet_aircraft_museum_aircraft.csv','133577','CT-133','-> Waterloo Warbirds, which operates C-FRGA'),
 ('canadian_air_land_and_sea_museum_markham_aircraft.csv','133542','CT-133','-> Jet Aircraft Museum, confirmed on its own pages Sept 2026'),
 ('canadian_war_museum_aircraft.csv','100760','CF-100','-> Musee de l aerospatiale du Quebec, from its own site'),
 ('west__the_military_museums_calgary_aircraft.csv','101032','CF-101','-> Alberta Aviation Museum, outdoors beside the hangar'),
 ('16_wing_borden_base_borden_military_museum_aircraft.csv','134222','CT-134','-> Canadian Warplane Heritage (own collection page, Sept 2026)'),
]:
    if os.path.exists(p): drop_row(p,tail,model,note)
    else: print('  MISSING',p)

# HA-1112 C.4K-114: two museums, two different construction numbers, one Spanish serial
h,rows=load('bomber_command_museum_canada_aircraft.csv'); n=0
for r in rows:
    if (r['tail_number'] or '').strip()=='C.4K-114':
        r['tail_number']=''
        al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
        for a in ('C.4K-114','12E-265'):
            if a not in al: al.append(a)
        r['aliases']='; '.join(al)
        r['description']=r['description'].rstrip('. ')+'. Tail left blank because the Canada Aviation and Space Museum records the same Spanish serial on a Buchon of a different construction number; the two attributions conflict and one is wrong.'
        n+=1
assert n; save('bomber_command_museum_canada_aircraft.csv',h,rows); print('  blank C.4K-114 at Nanton (c/n conflict with Ottawa)')

# ---- importer/test-suite conventions
h,rows=load('musee_aerospatiale_quebec_aircraft.csv'); n=0
for r in rows:
    if r['manufacturer'].strip()=='Edelweiss' and not r['model'].strip():
        r['manufacturer'],r['model']='Amateur-built','Edelweiss'; n+=1   # model is required
assert n; save('musee_aerospatiale_quebec_aircraft.csv',h,rows); print('  Edelweiss: name moved from manufacturer to model (model is required)')
h,rows=load('west__the_military_museums_calgary_aircraft.csv'); n=0
for r in rows:
    if r['aircraft_type'].strip()=='drone': r['aircraft_type']='fixed_wing'; r['wing_type']='monoplane'; n+=1
assert n; save('west__the_military_museums_calgary_aircraft.csv',h,rows); print('  Sperwer: aircraft_type drone -> fixed_wing (Q-designated UAVs are aircraft)')
h,rows=load('ottawa_casm_topup_aircraft.csv'); n=0
for r in rows:
    if r['model'].strip()=='HS-2L' and not r['variant'].strip():
        r['model'],r['variant']='HS-2','L'; n+=1
        al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
        for extra in ('HS-2L','HS2L'):
            if extra.lower() not in {x.lower() for x in al}: al.append(extra)
        r['aliases']='; '.join(al)
assert n; save('ottawa_casm_topup_aircraft.csv',h,rows); print('  HS-2L -> HS-2 + L')
