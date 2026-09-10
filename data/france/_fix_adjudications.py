import csv,os,glob
D='/home/claude/AirplaneFinder/data/france'; os.chdir(D)
def load(p):
    with open(p,newline='',encoding='utf-8') as f: r=csv.DictReader(f); return r.fieldnames,list(r)
def save(p,h,rows):
    with open(p,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=h,lineterminator='\n'); w.writeheader(); w.writerows(rows)

# ---- duplicate SITES: (file to delete, museum row to delete, why)
DROP_SITES=[
 ('lycee-flora-tristan_aircraft.csv','Lycée Flora Tristan Camblanes Super Étendard',
  'same Super Etendard 12 as Aerocampus Aquitaine, Latresne (adjacent commune, same 33360); kept the richer 3-row campus record'),
 ('gendarmerie-rochefort-alize_aircraft.csv','Alizé Gate Guard, École de Gendarmerie de Rochefort',
  'same Alize 8 on the same roundabout as "Alize du Rond-Point de l\'Avion, Rochefort"'),
 ('northwest__canopee_chateaudun_aircraft.csv','CANOPEE Châteaudun',
  'duplicate of "Conservatoire d\'Aeronefs CANOPEE, Chateaudun"'),
 ('chan_nimes_aircraft.csv','Conservatoire Historique de l\'Aéronautique Navale, Nîmes',
  'duplicate of the same conservatoire recorded as "..., Nimes-Garons"'),
 ('saint-raphael-etendard_aircraft.csv','Étendard IV Monument, Saint-Raphaël',
  'Etendard IV M 29 moved to the SDIS station at Frejus in June 2022; ARDHAN still lists the old seafront site'),
 ('lycee_briand_houilles_aircraft.csv','Lycée Aristide Briand Houilles Instructional Airframes','duplicate site'),
 ('lycee_jully_saint_avold_aircraft.csv','Lycée Charles Jully Saint-Avold Instructional Airframes','duplicate site'),
 ('lycee_frederic_mistral_nimes_aircraft.csv','Lycée Frédéric Mistral Super Étendard, Nîmes','duplicate site'),
 ('lycee_jean_zay_jarny_aircraft.csv','Lycée Jean Zay Jarny Instructional Airframes','duplicate site'),
 ('lycee_corbiere_morlaix_aircraft.csv','Lycée Tristan Corbière Morlaix Instructional Airframes','duplicate site'),
 ('lycee_val_de_lys_aircraft.csv','Lycée Val de Lys Estaires Instructional Airframes','duplicate site'),
 ('melun_villaroche_aircraft.csv',None,'duplicate of the northwest package\'s richer 29-row Melun-Villaroche file'),
]
drop_names=set()
for fn,mus,why in DROP_SITES:
    if os.path.exists(fn): os.remove(fn); print(f'  drop site file {fn:52s} {why}')
    if mus: drop_names.add(mus)
h,rows=load('fr_museums.csv'); keep=[]; seen=set()
for r in rows:
    if r['name'] in drop_names: print('  drop museum row',r['name']); continue
    if r['name'] in seen: print('  drop duplicate museum row',r['name'],r['city']); continue
    seen.add(r['name']); keep.append(r)
save('fr_museums.csv',h,keep)

def drop_row(p,tail,model,note):
    h,rows=load(p)
    k=[r for r in rows if not ((r['tail_number'] or '').strip()==tail and r['model'].strip()==model)]
    assert len(k)<len(rows),(p,tail); save(p,h,k); print(f'  drop row {model} {tail:6s} from {p} — {note}')
def blank_row(p,tail,model,variant,note):
    h,rows=load(p); n=0
    for r in rows:
        if (r['tail_number'] or '').strip()==tail and r['model'].strip()==model and r['variant'].strip()==variant:
            r['tail_number']=''
            al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
            if tail not in al: al.append(tail)
            r['aliases']='; '.join(al)
            r['description']=(r['description'].rstrip('. ')+'. '+note).strip(); n+=1
    assert n,(p,tail,model,variant); save(p,h,rows); print(f'  blank {model} {variant} {tail} in {p}')

drop_row('ban-lann-bihoue_aircraft.csv','29','F-8',
         'ARDHAN lists Crusader 29 at both Landivisiau and Lann-Bihoue; kept at Landivisiau, the Crusader base')
drop_row('montelimar_meac_aircraft.csv','233','Mirage III',
         'museum-owned but craned onto the Villeperdrix roundabout; recorded at the monument, where a visitor sees it')
blank_row('lyon_corbas_clement_ader_aircraft.csv','02','Mirage III','R',
          'Tail left blank because the short French number 02 is shared with the Mirage IIIA 02 displayed at ISAE-SUPAERO and the database keys aircraft on model plus tail.')
blank_row('lyon_corbas_clement_ader_aircraft.csv','001','Mirage III','E',
          'Tail left blank because the museum also holds Mirage IIIB 001 and the database keys aircraft on model plus tail.')

drop_row('caea_bordeaux_merignac_aircraft.csv','06','Étendard IV',
         'ARDHAN lists 06 twice; Ailes Anciennes Toulouse has the full provenance chain (recovered at Rochefort, displayed at Vannes, inherited by AAT)')
drop_row('grenier_aviation_aircraft.csv','F-WJDT','RL-21',
         'the Leduc RL-21 is a monument historique in the Espace Air Passion collection at Angers-Marce')

# --- test-suite conventions
h,rows=load('lebourget_topup_aircraft.csv'); n=0
for r in rows:
    if r['model'].strip()=='F-105' and r['variant'].strip()=='G':
        r['role_type']='electronic_warfare'; n+=1
assert n; save('lebourget_topup_aircraft.csv',h,rows); print('  F-105G -> electronic_warfare (Wild Weasel)')
h,rows=load('ban-hyeres_aircraft.csv'); n=0
for r in rows:
    al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
    keep=[a for a in al if 'HAS.2' not in a]
    if len(keep)!=len(al):
        r['aliases']='; '.join(keep)
        if not r['variant'].strip(): r['variant']='HAS.2'   # the mark belongs in variant, not aliases
        n+=1
assert n; save('ban-hyeres_aircraft.csv',h,rows); print('  Lynx HAS.2: mark moved from aliases to the variant field (the alias prose filter reads HAS as a verb)')

# --- collisions with records already live in the database
def blank_tail(p,tail,model,note):
    h,rows=load(p); n=0
    for r in rows:
        if (r['tail_number'] or '').strip()==tail and r['model'].strip()==model:
            r['tail_number']=''
            al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
            if tail not in al: al.append(tail)
            r['aliases']='; '.join(al)
            r['description']=(r['description'].rstrip('. ')+'. '+note).strip(); n+=1
    assert n,(p,tail,model); save(p,h,rows); print(f'  blank {model} {tail} in {p}')
blank_tail('celag_grenoble_le_versoud_aircraft.csv','FR41','H-21',
  'Tail left blank because FR41 is already recorded on the H-21C at The Helicopter Museum, Weston-super-Mare, taken from that museum own fleet list; the CELAG attribution rests on a third-party inventory and a site last updated in 2019, so the two need reconciling on the ground.')
blank_tail('montelimar_meac_aircraft.csv','235','Mirage F1',
  'Tail left blank because the number 235 is already held in this database by a South African Mirage F1AZ and the database keys aircraft on model plus tail.')
blank_tail('memorial_caen_aircraft.csv','45','MiG-21',
  'Tail left blank because the two-digit bort number 45 is not unique and is already held by a Soviet-operated MiG-21 recorded elsewhere.')
