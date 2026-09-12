import csv,glob,json,re,collections,unicodedata,sys
sys.path.insert(0,'/home/claude/pipeline')
from fam2 import base, norm_mfr, load
from overrides import MOVE, REPLACE

# ---------- curated table ----------
TAB={}
for f in sorted(glob.glob("/home/claude/pipeline/curate/out*.tsv")):
    for i,l in enumerate(open(f,encoding="utf-8")):
        if i==0: continue
        p=l.rstrip("\n").split("\t")
        if len(p)!=7: continue
        fam,mfr,canon,aka,vr,conf,note=[x.strip() for x in p]
        canon="" if canon.upper()=="NONE" else canon
        akas=[x.strip() for x in aka.split(";") if x.strip()]
        rules={}
        for r in vr.split(";"):
            if "=" in r:
                k,v=r.split("=",1); rules[k.strip()]=v.strip()
        TAB[(mfr,fam)]=dict(canon=canon,aka=akas,rules=rules,conf=conf,note=note)

def famkey(x):
    b=base(x.get("model"))
    m=(x.get("model") or "").strip()
    return (norm_mfr(x.get("manufacturer")), b if b else m)

# ---------- name variants ----------
def deaccent(s): return unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode()
CAMEL=re.compile(r"(?<=[a-z])(?=[A-Z])")
SOLID={"superfortress":"Super Fortress","flyingfortress":"Flying Fortress",
       "thunderstreak":"Thunder Streak","thunderflash":"Thunder Flash",
       "thunderjet":"Thunder Jet","thunderchief":"Thunder Chief",
       "warhawk":"War Hawk","starfighter":"Star Fighter","skyhawk":"Sky Hawk",
       "skytrain":"Sky Train","skyraider":"Sky Raider","skymaster":"Sky Master",
       "superfortress ":"Super Fortress","supersabre":"Super Sabre",
       "seaking":"Sea King","seasprite":"Sea Sprite","seahawk":"Sea Hawk",
       "seastallion":"Sea Stallion","tomcat":"Tom Cat","hellcat":"Hell Cat",
       "wildcat":"Wild Cat","bearcat":"Bear Cat","kittyhawk":"Kitty Hawk",
       "blackhawk":"Black Hawk","greyhound":"Grey Hound","boxcar":"Box Car"}
TWO_WORDS=re.compile(r"^[A-Za-z]+ [A-Za-z]+$")
def variants(name):
    """Spelling forms of one name that a plain substring search would otherwise
    miss. Search is a plain LIKE %q%, so 'super fortress' does not match
    'Superfortress' and vice versa."""
    out={name}
    d=deaccent(name)
    if d!=name: out.add(d)
    for n in list(out):
        s=CAMEL.sub(" ",n)                       # SeaCobra -> Sea Cobra
        if s!=n: out.add(s)
        # only split a plain two-word name back into a solid form; doing it to
        # "Combat Talon II" or "Hercules C.3" just makes unreadable noise
        if TWO_WORDS.match(n): out.add(n.replace(" ",""))
    for n in list(out):
        k=n.lower().replace(" ","")
        if k in SOLID: out.add(SOLID[k])
    return {x for x in out if x and len(x)>2}

DESIG=re.compile(r"^([A-Za-z]{1,4})-(\d{1,3}[A-Za-z]{0,3})$")
def dashless(model,variant):
    out=set()
    for src in (model or "", (model or "")+("-"+variant if variant else "")):
        m=DESIG.match(src)
        if m: out.add(m.group(1)+m.group(2))
    return out

TAILY=re.compile(r"^(N\d|[0-9]{2,3}-[0-9]{3,5}$|[0-9]{4,6}$|BuNo|c/n)", re.I)
def looks_like_identity(v):
    return bool(TAILY.match(v.strip()))

def main():
    a=load()
    plan=[]; stats=collections.Counter()
    for x in a:
        k=famkey(x)
        t=TAB.get(k)
        cur_mn=(x.get("model_name") or "").strip()
        cur_al=[s.strip() for s in (x.get("aliases") or []) if s.strip()]
        new_mn=cur_mn; move_to_aircraft_name=None
        approved=set()
        if t:
            approved={t["canon"]}|set(t["aka"])|set(t["rules"].values())
            approved={s for s in approved if s}
            want=t["rules"].get((x.get("model") or "").strip()) or t["canon"]
            if not cur_mn and want:
                new_mn=want; stats["filled_blank"]+=1
            elif cur_mn and want and x["id"] in MOVE:
                new_mn=want; move_to_aircraft_name=MOVE[x["id"]]; stats["moved_named"]+=1
            elif cur_mn and want and x["id"] in REPLACE:
                new_mn=want; stats["replaced"]+=1
            elif cur_mn and want and cur_mn not in approved:
                # an off-list value: an individual aircraft name, a serial, or a
                # manufacturer-prefixed string. Move it aside only when it is rare
                # in its family, so a real name the curator missed is not lost.
                if looks_like_identity(cur_mn):
                    new_mn=want; move_to_aircraft_name=cur_mn; stats["moved_identity"]+=1
                elif cur_mn.lower().startswith(tuple(
                        s.lower() for s in [(x.get("manufacturer") or "").strip()] if s)):
                    # "North American Mitchell" is a redundant restatement, not an
                    # airframe's name - replace it and keep the old string only as
                    # a search alias
                    new_mn=want; stats["replaced_mfr_prefixed"]+=1
                else:
                    stats["offlist_kept"]+=1
        # aliases: everything searchable for this airframe
        names=set(approved)|({cur_mn} if cur_mn else set())|({new_mn} if new_mn else set())
        add=set()
        for n in names: add|=variants(n)
        add|=dashless(x.get("model"), x.get("variant"))
        have={s.lower() for s in cur_al}
        newal=cur_al+[s for s in sorted(add) if s.lower() not in have and not _dupe(s,have)]
        body={}
        if new_mn!=cur_mn: body["model_name"]=new_mn
        if move_to_aircraft_name and not (x.get("aircraft_name") or "").strip():
            body["aircraft_name"]=move_to_aircraft_name
        if len(newal)!=len(cur_al): body["aliases"]=newal
        if body:
            body["_id"]=x["id"]; plan.append(body)
    print("planned changes:",len(plan),dict(stats))
    json.dump(plan,open("/home/claude/pipeline/name_plan.json","w"))

def _dupe(s,have):
    have.add(s.lower()); return False

if __name__=="__main__": main()
