import json,collections,sys,random
sys.path.insert(0,'/home/claude/pipeline')
from regs import from_registration
from mil import from_serial
a=json.load(open("/home/claude/pipeline/cache_aircraft.json"))
site=json.load(open("/home/claude/pipeline/aircraft_site_country.json"))
plan=[]; audit=[]
for x in a:
    if (x.get("operator_country") or "").strip(): continue
    sc=[c for c,_ in site.get(str(x["id"]),[])]
    cc,rule=from_registration(x.get("tail_number"), sc)
    if not cc:
        cc,rule=from_serial(x.get("tail_number"), sc, x.get("manufacturer"), x.get("full_designation"))
    if not cc: continue
    plan.append({"_id":x["id"],"operator_country":cc})
    audit.append((x["id"],cc,rule,x.get("tail_number"),x.get("manufacturer"),
                  x.get("full_designation"),([c for c,_ in site.get(str(x["id"]),[])] or ["?"])[0]))
json.dump(plan,open("/home/claude/pipeline/country_plan.json","w"))
with open("/home/claude/pipeline/country_audit.tsv","w") as f:
    f.write("id\tcountry\trule\ttail\tmanufacturer\tdesignation\tsite_country\n")
    for r in audit: f.write("\t".join(str(v) for v in r)+"\n")
print("planned:",len(plan))
random.seed(7)
print("\n--- 25 random assignments for review ---")
for r in random.sample(audit,25):
    print(f"  {r[1]}  {r[3]:12s} {str(r[4])[:20]:20s} {str(r[5])[:20]:20s} @{r[6][:16]:16s} [{r[2]}]")
