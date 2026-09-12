import json,os,sys,time,urllib.request,threading,queue
KEY=os.environ["AIRPLANE_KEY"]; HOST="https://airplane.museum"
plan=json.load(open("/home/claude/pipeline/country_plan.json"))
DONE="/home/claude/pipeline/applied_country_ids.txt"
done=set()
if os.path.exists(DONE): done={int(l) for l in open(DONE) if l.strip()}
todo=[p for p in plan if p["_id"] not in done]
print("todo",len(todo),"already done",len(done),flush=True)
lock=threading.Lock(); fh=open(DONE,"a"); n=[0]; err=[0]
q=queue.Queue()
for p in todo: q.put(p)
def patch(p):
    body={k:v for k,v in p.items() if k!="_id"}
    r=urllib.request.Request(f"{HOST}/api/v1/aircraft/{p['_id']}",data=json.dumps(body).encode(),
      headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"},method="PATCH")
    for a in range(4):
        try:
            urllib.request.urlopen(r,timeout=60).read(); return None
        except urllib.error.HTTPError as e:
            b=e.read().decode()[:160]
            if e.code in (429,500,502,503,504) and a<3: time.sleep(5*(a+1)); continue
            return f"{p['_id']} HTTP {e.code} {b}"
        except Exception as e:
            if a<3: time.sleep(3); continue
            return f"{p['_id']} {e}"
def worker():
    while True:
        try: p=q.get_nowait()
        except queue.Empty: return
        e=patch(p)
        with lock:
            if e: err[0]+=1; print("ERR",e,flush=True)
            else: fh.write(f"{p['_id']}\n")
            n[0]+=1
            if n[0]%500==0: fh.flush(); print(f"  {n[0]}/{len(todo)} errors={err[0]}",flush=True)
        q.task_done()
ts=[threading.Thread(target=worker,daemon=True) for _ in range(2)]
[t.start() for t in ts]; [t.join() for t in ts]
fh.flush(); fh.close()
print("DONE",n[0],"errors",err[0],flush=True)
