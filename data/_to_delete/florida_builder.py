import csv, os, re
DIGITS="0123456789"
def join_designation(model, variant):
    model=(model or "").strip(); variant=(variant or "").strip()
    if not variant: return model
    if variant[0] in DIGITS: return f"{model}-{variant}"
    if model and model[-1] in DIGITS: return f"{model}{variant}"
    return f"{model} {variant}"
DESIG1=re.compile(r'^([A-Za-z]{1,4})-(\d{1,3}[A-Za-z]{0,3})$')
def dashless(s):
    m=DESIG1.match((s or "").strip())
    if not m: return None
    v=m.group(1)+m.group(2)
    return v if v!=s.strip() else None
HDR=["manufacturer","model","variant","tail_number","model_name","aircraft_name","aircraft_type",
     "wing_type","military_civilian","role_type","year_built","description","aliases","museum_name","display_status"]
IN=["manufacturer","model","variant","tail_number","model_name","aircraft_name","aircraft_type",
    "wing_type","military_civilian","role_type","year_built","description","aliases","display_status"]
def build(path, museum, lines):
    rows=[]
    for ln in lines:
        ln=ln.strip()
        if not ln or ln.startswith("#"): continue
        p=[x.strip() for x in ln.split("|")]
        assert len(p)==14, f"{path}: {len(p)} fields\n  {ln[:150]}"
        r=dict(zip(IN,p))
        assert r["manufacturer"], f"{path}: blank manufacturer\n  {ln[:150]}"
        assert "," not in r["description"] and "," not in r["aliases"], f"{path}: comma\n  {ln[:150]}"
        if r["aircraft_type"]!="fixed_wing": r["wing_type"]=""
        al=[a.strip() for a in r["aliases"].split(";") if a.strip()]
        low={a.lower() for a in al}
        for src in [r["model"], join_designation(r["model"],r["variant"])]+list(al):
            d=dashless(src or "")
            if d and d.lower() not in low: al.append(d); low.add(d.lower())
        r["aliases"]="; ".join(al); r["museum_name"]=museum
        rows.append(r)
    with open(path,"w",newline="",encoding="utf-8") as fh:
        w=csv.DictWriter(fh,fieldnames=HDR,lineterminator="\n"); w.writeheader()
        for r in rows: w.writerow({k:r.get(k,"") for k in HDR})
    print(f"  {os.path.basename(path):44s} {len(rows):3d} rows  {sum(1 for r in rows if r['tail_number']):3d} tails")
    return rows
