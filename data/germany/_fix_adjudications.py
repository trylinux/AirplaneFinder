import csv,os,glob
D='/home/claude/AirplaneFinder/data/germany'; os.chdir(D)
def load(p):
    with open(p,newline='',encoding='utf-8') as f: r=csv.DictReader(f); return r.fieldnames,list(r)
def save(p,h,rows):
    with open(p,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=h,lineterminator='\n'); w.writeheader(); w.writerows(rows)
def drop(p,tail,note):
    h,rows=load(p); keep=[r for r in rows if (r['tail_number'] or '').strip().lower()!=tail.lower()]
    assert len(keep)<len(rows),(p,tail); save(p,h,keep); print(f'  drop {tail:8s} {p:44s} {note}')
def blank(p,tail,note):
    h,rows=load(p); n=0
    for r in rows:
        if (r['tail_number'] or '').strip().lower()==tail.lower():
            r['tail_number']=''
            al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
            if f'Wnr {tail}'.lower() not in {x.lower() for x in al}: al.append(f'Wnr {tail}')
            r['aliases']='; '.join(al); r['description']=(r['description'].rstrip('. ')+'. '+note).strip(); n+=1
    assert n,(p,tail); save(p,h,rows); print(f'  blank {tail} {p}')
G=[f for f in glob.glob('*_aircraft.csv') if 'gatow' in f][0]
for t,n in [('313','-> Rothenburg (loan, museum site 2026)'),('JB+110','-> Uetersen (stayed 1995)'),
            ('D-9539','-> Altenburg-Nobitz'),('99+01','-> Rothenburg (loan from MHM Dresden)'),
            ('99+41','-> Altenburg-Nobitz'),('29+14','-> Eschbach (F-104 Society 2025)')]:
    drop(G,t,n)
LS=[f for f in glob.glob('*_aircraft.csv') if 'luftraum' in f.lower()][0]
drop(LS,'D-EAZO','-> Grossenhain flying collection')
GH=[f for f in glob.glob('*_aircraft.csv') if 'grossenhain' in f.lower() or 'großenhain' in f.lower()][0]
drop(GH,'21+55','-> Hassfurt Starfighter-Denkmal (F-104 Society 2025)')
RE=[f for f in glob.glob('*_aircraft.csv') if 'rechlin' in f.lower() and '120076' in open(f,encoding='utf-8').read()][0]
blank(RE,'120076','Tail left blank because Werknummer 120076 is the original He 162 in the Deutsches Technikmuseum Berlin; this airframe is a rebuild incorporating about 40 percent original parts.')

# --- D-AQUI: the real one (Wnr 130714) is Lufthansa's at Hangar One; Sinsheim's
# CASA 352L merely wears the marks, like Speyer's, which the researcher already flagged.
SI=[f for f in glob.glob('*_aircraft.csv') if 'sinsheim' in f.lower()][0]
h,rows=load(SI); n=0
for r in rows:
    if r['tail_number']=='D-AQUI':
        r['tail_number']=''
        al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
        if 'D-AQUI' not in al: al.append('D-AQUI')
        r['aliases']='; '.join(al)
        r['description']=r['description'].rstrip('. ')+'. The marks D-AQUI are a Lufthansa-colours repaint; the real D-AQUI (Werknummer 130714) is the Lufthansa Traditionsflug aircraft at Hangar One, Frankfurt.'
        n+=1
assert n; save(SI,h,rows); print('  blank D-AQUI  '+SI+' (false marking)')

# --- Ju 52 model/variant spelling, country-wide
n=0
for p in glob.glob('*_aircraft.csv'):
    h,rows=load(p); ch=False
    for r in rows:
        m,v=r['model'].strip(),r['variant'].strip()
        if m=='Ju 52/3m' and not v: r['model'],r['variant']='Ju 52','3m'; ch=True; n+=1
        elif m=='Ju 52' and v.startswith('/'): r['variant']=v.lstrip('/'); ch=True; n+=1
        else: continue
        al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
        for extra in ('Ju 52/3m','Ju52'):
            if extra.lower() not in {x.lower() for x in al}: al.append(extra)
        r['aliases']='; '.join(al)
    if ch: save(p,h,rows)
print(f'  normalised {n} Ju 52 model/variant spellings')

# --- importer/test hygiene
for p in glob.glob('*_aircraft.csv'):
    h,rows=load(p); ch=False
    for r in rows:
        if r['model'].strip()=='UH-1D' and not r['variant'].strip():
            r['model'],r['variant']='UH-1','D'; ch=True
            al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
            for extra in ('UH-1D','UH1D'):
                if extra.lower() not in {x.lower() for x in al}: al.append(extra)
            r['aliases']='; '.join(al)
        if r['manufacturer'].strip()=='Unknown':
            r['manufacturer']='Unidentified'; ch=True
    if ch: save(p,h,rows); print('  hygiene fixes in',p)

# --- two-digit Soviet bort numbers collide with Russian records already in the
# database; the (model, tail_number) key cannot hold both. Blank the German tail
# and keep the bort as an alias - the same workaround used for SAAF Mirage 207.
for fn,tail in [('sinsheim_aircraft.csv','03'),
                ('interessenverein_luftfahrt_neuenkirchen_aircraft.csv','07'),
                ('rechlin_laerz_luftfahrtmuseum_aircraft.csv','07')]:
    h,rows=load(fn); n=0
    for r in rows:
        if (r['tail_number'] or '').strip()==tail and r['model'].strip() in ('An-2','Su-7','MiG-17'):
            r['tail_number']=''
            al=[a.strip() for a in r['aliases'].split(';') if a.strip()]
            for extra in (f'bort {tail}',):
                if extra.lower() not in {x.lower() for x in al}: al.append(extra)
            r['aliases']='; '.join(al)
            r['description']=r['description'].rstrip('. ')+f'. Tail left blank in this database because the two-digit bort number {tail} is not unique - it collides with a Soviet-operated airframe of the same type already recorded elsewhere.'
            n+=1
    assert n,(fn,tail); save(fn,h,rows); print(f'  blank bort {tail} {fn}')
