import json,os,sys,time,threading,queue,urllib.request
sys.path.insert(0,'/home/claude/pipeline')
KEY=os.environ["AIRPLANE_KEY"]; HOST="https://airplane.museum/api/v1"
def get(u):
    r=urllib.request.Request(HOST+u,headers={"Authorization":f"Bearer {KEY}"})
    for a in range(5):
        try: return json.load(urllib.request.urlopen(r,timeout=90))
        except Exception as e:
            if a<4: time.sleep(2*(a+1)); continue
            raise
mus=json.load(open("cache_museums.json"))
out={}; lock=threading.Lock(); q=queue.Queue()
for m in mus: q.put(m)
n=[0]
def w():
    while True:
        try: m=q.get_nowait()
        except queue.Empty: return
        try:
            for a in (get(f"/museums/{m['id']}").get("aircraft") or []):
                with lock: out.setdefault(a["id"],[]).append((m["country"],m["id"]))
        except Exception as e:
            with lock: print("fail",m["id"],e,flush=True)
        with lock:
            n[0]+=1
            if n[0]%500==0: print(f"  {n[0]}/{len(mus)}",flush=True)
ts=[threading.Thread(target=w,daemon=True) for _ in range(8)]
for t in ts: t.start()
for t in ts: t.join()
json.dump({str(k):v for k,v in out.items()},open("aircraft_site_country.json","w"))
print("mapped",len(out),"aircraft")
