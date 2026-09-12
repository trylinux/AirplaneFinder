import json,collections,re,unicodedata

def norm_mfr(m):
    m=(m or "").strip().lower()
    m=unicodedata.normalize("NFKD",m).encode("ascii","ignore").decode()
    m=re.sub(r"[^a-z0-9 ]"," ",m); m=re.sub(r"\s+"," ",m).strip()
    for a,b in [("mcdonnell douglas","mcdonnell"),("lockheed martin","lockheed"),
                ("north american aviation","north american"),("bell helicopter","bell"),
                ("bell textron","bell"),("douglas aircraft","douglas"),
                ("mikojan guriewicz","mikoyan"),("mikoyan gurevich","mikoyan"),
                ("suchoj","sukhoi"),("aero vodochody","aero"),("de havilland canada","dhc"),
                ("hawker aircraft","hawker"),("gloster aircraft","gloster"),
                ("vickers supermarine","supermarine"),("ling temco vought","vought"),
                ("ltv","vought"),("pzl swidnik","pzl"),("wsk pzl mielec","pzl"),
                ("pzl mielec","pzl"),("wsk mielec","pzl"),("beechcraft","beech"),
                ("aerospatiale","aerospatiale"),("british aerospace","bae"),
                ("general dynamics","general dynamics")]:
        if m==a or m.startswith(a+" "): m=b+m[len(a):]
    return m

# US modifier prefixes that may precede the basic mission letter.
MODS=set("XYZJNGCRTVKMEDSAHLPQUFWO")
# National / designer prefixes that are NOT modifiers - never strip these.
KEEP={"CF","CT","CL","CC","CP","CH-1","DC","DHC","DH","SNC","SNJ","SNB","GC","FC",
      "TS","YS","MB","BO","CG","CM","CA","HT","PC","SF","MD","AT-26","PT-26"}
DESIG=re.compile(r"^([A-Za-z]{1,3})-(\d{1,3})$")
# Soviet/Russian and other designer prefixes are part of the type name, not a
# US mission modifier - An-2 is not an "N-2", Yak-40 is not a "K-40".
DESIGNER={"MIG","SU","TU","YAK","IL","AN","MI","KA","LA","BE","PZL","LET","IAR",
          "HA","SM","MS","MH","FW","BF","DO","JU","HE","AR","BU","SG","RF","ME"}

def base(model):
    """Return the base designation (basic mission + number) for a US-style
    designation, or None when the model is not one or when its prefix is a
    national/designer prefix rather than a mission modifier."""
    m=(model or "").strip()
    x=DESIG.match(m)
    if not x: return None
    p,num=x.group(1).upper(),x.group(2)
    if p in KEEP or p in DESIGNER: return None
    if len(p)==1: return p+"-"+num
    if not all(c in MODS for c in p): return None
    return p[-1]+"-"+num

def load(path="/home/claude/pipeline/cache_aircraft.json"):
    return json.load(open(path))
