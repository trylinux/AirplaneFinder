import json,os,sys,time
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from pipe import get
CA="/home/claude/pipeline/cache_aircraft.json"; CM="/home/claude/pipeline/cache_museums.json"
def pull(ep):
    j=get(f"/{ep}/search?per_page=100&page=1"); out=list(j["results"]); n=j["pages"]
    for p in range(2,n+1):
        for attempt in range(4):
            try: out+=get(f"/{ep}/search?per_page=100&page={p}")["results"]; break
            except Exception as e: time.sleep(2)
        if p%20==0: print(ep,p,n,flush=True)
    return out
if __name__=="__main__":
    a=pull("aircraft"); json.dump(a,open(CA,"w")); print("aircraft",len(a))
    m=pull("museums");  json.dump(m,open(CM,"w")); print("museums",len(m))
