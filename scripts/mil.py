# -*- coding: utf-8 -*-
"""Military serial systems whose SHAPE identifies the operator.

Only shapes unique to one system resolve here. Where several national systems
share a shape the row is refused, because under uq_airframe a wrong country is
worse than no country: it splits one airframe into two records.
"""
import re

# --- shapes that belong to exactly one system -------------------------------
UNIQUE = [
 (re.compile(r"^\d{2}\+\d{2}$"),      "DE", "Bundeswehr NN+NN"),
 (re.compile(r"^MM\d{3,5}$"),         "IT", "Matricola Militare"),
 (re.compile(r"^A\d{1,3}-\d{1,3}$"),  "AU", "RAAF A-series"),
 (re.compile(r"^NZ\d{3,4}$"),         "NZ", "RNZAF serial"),
]

# --- RAF -------------------------------------------------------------------
RAF_2L = re.compile(r"^[A-Z]{2}\d{3}$")
RAF_1L = re.compile(r"^[A-Z]\d{4}$")
# The RAF never used I, Q, U or Y as a serial letter (confusable with 1 and 0),
# so a serial starting with one is some other air arm - Indian Navy IN238,
# IAF Vampire IB427, USAF drone QF420, MiG-21UM U2146.
RAF_NEVER = set("IQUY")
# Air arms with their own serial systems that reuse the RAF shapes. An airframe
# preserved in one of these is far more likely to wear the local serial than an
# RAF one, and no shape rule separates them: India (HAL Ajeet E1046, Bell 47G
# BZ544), Zimbabwe (Canberra R2504), Zambia (Chipmunk AF506), Pakistan,
# Indonesia, Bangladesh, Sri Lanka, Myanmar.
RAF_EXCLUDE_SITES = {"India","Zimbabwe","Zambia","Pakistan","Indonesia",
                     "Bangladesh","Sri Lanka","Myanmar","Nigeria","Ghana","Kenya"}
# Manufacturers the RAF never operated. A British serial on one of these is a
# shape collision, not a fact.
NOT_RAF_MFR = {"mikoyan-gurevich","mikoyan","sukhoi","mil","tupolev","ilyushin",
               "antonov","yakovlev","lavochkin","polikarpov","kamov","pzl",
               "pzl-mielec","pzl-swidnik","wsk mielec","aero","aero vodochody",
               "let","hal","hindustan aeronautics","shenyang","nanchang",
               "chengdu","harbin","xian","casa","iai","embraer","atlas",
               "mitsubishi","kawasaki","fuji","shin meiwa","nurtanio","lipnur",
               # continental WWI makers: the RFC flew a few, but a British
               # serial on one is far more often a shape collision - SPAD XIII
               # S5295 in France was being recorded as RAF
               "spad","nieuport","morane-saulnier","caudron","hanriot","breguet",
               "farman","voisin","salmson","fokker","albatros","pfalz",
               "halberstadt","lvg","rumpler","ansaldo","macchi","aviatik",
               "eurocopter","airbus helicopters","kaman","nakajima","kawanishi",
               "aichi","yokosuka","tachikawa"}
# Makers whose airframes carry British serials. Used to tell an RNAS N-serial
# (N3200 Spitfire) from a US registration of the same shape (N7470, the Boeing
# 747 prototype) - the two are indistinguishable by shape alone.
BRITISH_MFR = {"sopwith","avro","short","short brothers","de havilland","bristol",
  "gloster","supermarine","fairey","vickers","vickers-armstrongs","handley page",
  "armstrong whitworth","blackburn","boulton paul","westland","airspeed","miles",
  "percival","hawker","hawker siddeley","english electric","bac","folland",
  "british aerospace","bae","bae systems","saunders-roe","fairey aviation",
  "gloster aircraft","hunting","hunting percival","auster","slingsby","scottish aviation"}
# Early US Navy bureau numbers ran A#### - the same shape as RAF WWI serials.
# The Curtiss NC-4 (A2294) was being recorded as British.
USN_A_MFR = {"curtiss","boeing","consolidated","vought","martin","douglas",
             "grumman","naval aircraft factory","great lakes","berliner-joyce"}

# --- US fiscal-year serial --------------------------------------------------
# Real USAF/US Army FY serials always carry a four- or five-digit sequence.
# A three-digit suffix means a foreign type-coded system of the same shape:
# Danish 41-401 Spitfire, Saudi/Kuwaiti Lightning 53-412, Turkish C-160 69-022,
# and Australian RAAus ultralight registrations 10-0665 / 19-7589.
FY = re.compile(r"^([0-9]{2})-([0-9]{4,5})$")
FY_SHORT = re.compile(r"^[0-9]{2}-[0-9]{1,3}$")
FY_ALSO = {"Japan":"JP","South Korea":"KR","Taiwan":"TW"}

def _mfr(x): return (x or "").strip().lower()

def from_serial(tail, site_countries=(), manufacturer="", designation=""):
    t=(tail or "").strip().upper()
    if not t: return None, "blank"
    m=_mfr(manufacturer)
    for rx,cc,rule in UNIQUE:
        if rx.match(t): return cc, rule
    # N####, C####, NC###, NX### - a US registration and a British serial share
    # these shapes exactly, so the maker decides. Refusing instead would throw
    # away ~1,900 correct rows in both directions.
    if re.match(r"^C\d{4}$", t) and "United States" not in site_countries:
        # C1347 is a Royal Flying Corps Canada JN-4 serial, not a US registration
        return None, "C#### outside the United States is some other serial system"
    if re.match(r"^[NC]\d{4}$", t) or re.match(r"^N[CXRL]\d{3}$", t):
        if any(sc in ("India","Pakistan","Bangladesh") for sc in site_countries) or m in NOT_RAF_MFR:
            # C1151 and C1586 are Indian Air Force MiG-21 serials, not US
            # registrations, and a continental type is neither
            return None, "N/C-shaped tail on a type or at a site with its own system"
        if m in BRITISH_MFR:
            if "United States" in site_countries:
                # N7471 is a Capital Airlines Viscount - a British maker does
                # not make a US-registered airliner a British serial
                return None, "British maker but US-sited: registration and serial cannot be told apart"
            return "GB", "British serial (maker is a UK airframe builder)"
        return ("US","US registration (maker is not a UK airframe builder)") if m else \
               (None,"N/C-shaped tail with no manufacturer to tell the systems apart")
    if re.match(r"^N\d{1,3}$", t):
        if m in BRITISH_MFR: return "GB", "British serial (maker is a UK airframe builder)"
        return None, "short N-number is also a French and an Indian serial"
    if re.match(r"^AM\d{3}$", t):
        return None, "AM### is an Air Ministry number on a captured airframe"
    if re.match(r"^E\d{4}$", t) and ("gnat" in (designation or "").lower()
                                      or "ajeet" in (designation or "").lower()):
        return "IN", "Indian Air Force Gnat/Ajeet E-series"
    if re.match(r"^[A-Z]0\d{3}$", t):
        return None, "no RAF serial block carries a leading zero"
    if RAF_2L.match(t) or RAF_1L.match(t):
        if t[0] in RAF_NEVER:
            return None, f"the RAF never used {t[0]} as a serial letter"
        if any(s in RAF_EXCLUDE_SITES for s in site_countries):
            return None, "RAF-shaped serial at a site whose own air arm uses the same shape"
        if m in NOT_RAF_MFR:
            return None, f"RAF-shaped serial on a type the RAF never operated ({manufacturer})"
        if RAF_1L.match(t) and m not in BRITISH_MFR:
            # one letter plus four digits collides with the pre-1935 US Navy
            # bureau numbers (A2294, the Curtiss NC-4), with US registrations,
            # and with several other systems. Only a British airframe builder
            # makes it safe.
            return None, "single-letter serial on a type no UK builder made"
        return "GB", "RAF two-letter serial" if RAF_2L.match(t) else "RAF pre-war single-letter serial"
    # Recreational Aviation Australia registrations are NN-NNNN by construction
    # class, the same shape as a US fiscal-year serial
    if re.match(r"^(10|19|24|25|28|32|55)-\d{3,4}$", t) and "Australia" in site_countries:
        return "AU", "RAAus construction-class registration"
    if FY_SHORT.match(t):
        return None, "a US fiscal-year serial never has a suffix under four digits"
    fy=FY.match(t)
    if fy and m in {"mitsubishi","nakajima","kawasaki","aichi","kawanishi","yokosuka"}:
        return None, "fiscal-year shape on a Japanese type"
    if fy:
        for s in site_countries:
            if s in FY_ALSO: return FY_ALSO[s], f"fiscal-year serial at a site in {s}"
        return "US", "USAF/US Army fiscal-year serial"
    return None, "no unique serial system matches"
