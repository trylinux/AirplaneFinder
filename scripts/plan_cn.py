import json,re,collections
# A separator is REQUIRED: without it the bare "cn" form swallowed the de-spaced
# registration aliases the name pass created - "CNCCG" read as c/n "CCG".
CN=re.compile(r"^(?:c/n|cn|msn|s/n|w\.?nr\.?|werknummer|constructor'?s? number)[\s:.]+([A-Za-z0-9][\w/.\-]{0,24})$", re.I)
a=json.load(open("/home/claude/pipeline/cache_aircraft.json"))
plan=[]; skip=[]
for x in a:
    if (x.get("construction_number") or "").strip(): continue
    al=[s for s in (x.get("aliases") or [])]
    keep=[]; got=[]
    for s in al:
        m=CN.match(s.strip())
        if m: got.append(m.group(1))
        else: keep.append(s)
    if not got: continue
    if len(set(got))>1:
        skip.append((x["id"],got,x.get("manufacturer"),x.get("full_designation"))); continue
    plan.append({"_id":x["id"],"construction_number":got[0],"aliases":keep})
json.dump(plan,open("/home/claude/pipeline/cn_plan.json","w"))
with open("/home/claude/pipeline/cn_skipped.tsv","w") as f:
    f.write("id\tcandidates\tmanufacturer\tdesignation\n")
    for r in skip: f.write(f"{r[0]}\t{'; '.join(r[1])}\t{r[2]}\t{r[3]}\n")
print("planned:",len(plan),"  skipped (conflicting c/n):",len(skip))
