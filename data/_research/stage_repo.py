import csv,glob,io,os,sys,json,collections
sys.path.insert(0,'/home/claude/pipeline')
from pipe import slugify, HDR_A, HDR_M
TOPUP={"smithsonian_national_air_and_space_museum":("Smithsonian National Air and Space Museum","District of Columbia"),
 "air_mobility_command_museum":("Air Mobility Command Museum","Delaware"),
 "barksdale_global_power_museum":("Barksdale Global Power Museum","Louisiana"),
 "air_zoo":("Air Zoo","Michigan")}
ABBR={"Connecticut":"ct","Rhode Island":"ri","Massachusetts":"ma","New Hampshire":"nh","Vermont":"vt","Maine":"me",
"New Jersey":"nj","Maryland":"md","West Virginia":"wv","Delaware":"de","District of Columbia":"dc",
"North Carolina":"nc","South Carolina":"sc","Tennessee":"tn","Kentucky":"ky","Mississippi":"ms","Louisiana":"la",
"Illinois":"il","Indiana":"in","Michigan":"mi","Minnesota":"mn","Iowa":"ia","North Dakota":"nd","South Dakota":"sd",
"Montana":"mt","Wyoming":"wy","Alaska":"ak"}
OUT="/home/claude/repo_stage/data"
bystate=collections.defaultdict(lambda: {"m":[], "a":[]})
for r in ["r1_newengland","r2_midatlantic","r3_carolinas","r4_midsouth","r5_greatlakes","r6_uppermidwest","r7_rockies"]:
    d=f"/home/claude/{r}/raw"
    info={}
    for row in csv.DictReader(open(d+"/museums.csv")):
        info[slugify(row["name"])]=(row["name"], row["state_province"], row)
    for f in sorted(glob.glob(d+"/*.txt")):
        slug=os.path.basename(f)[:-4]
        if slug in info: name,state,mrow=info[slug]
        elif slug in TOPUP: name,state=TOPUP[slug]; mrow=None
        else: print("UNKNOWN SITE",r,slug); continue
        rows=[l.rstrip("\n").split("|") for l in open(f) if l.strip()]
        bystate[state]["a"].append((slug,name,rows))
        if mrow: bystate[state]["m"].append(mrow)
for state,v in bystate.items():
    sl=state.lower().replace(" ","_"); ab=ABBR[state]
    dd=os.path.join(OUT,sl); os.makedirs(dd,exist_ok=True)
    if v["m"]:
        with open(os.path.join(dd,f"{ab}_museums.csv"),"w",newline="") as fh:
            w=csv.DictWriter(fh,fieldnames=HDR_M,lineterminator="\n"); w.writeheader()
            for m in v["m"]: w.writerow({k:m[k] for k in HDR_M})
    for slug,name,rows in v["a"]:
        with open(os.path.join(dd,f"{slug}_aircraft.csv"),"w",newline="") as fh:
            w=csv.writer(fh,lineterminator="\n")
            w.writerow(HDR_A[:13]+["museum_name","display_status"])
            for q in rows: w.writerow(q[:13]+[name]+[q[13]])
    print(f"{sl}: {len(v['m'])} new sites, {len(v['a'])} files, {sum(len(x[2]) for x in v['a'])} rows")
