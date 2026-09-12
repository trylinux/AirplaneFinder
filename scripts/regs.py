# -*- coding: utf-8 -*-
"""Civil registration prefixes -> ISO 3166-1 alpha-2.

ICAO allocates these nationality marks uniquely, so a well-formed registration
identifies its country of registry with no further evidence. That is exactly
what operator_country records: the marks the airframe wears.
"""
import re
# prefix (before the dash) -> country
DASHED = {
 "G":"GB","D":"DE","F":"FR","I":"IT","EC":"ES","CS":"PT","PH":"NL","OO":"BE",
 "LX":"LU","HB":"CH","OE":"AT","SE":"SE","LN":"NO","OY":"DK","OH":"FI","TF":"IS",
 "EI":"IE","EJ":"IE","SP":"PL","OK":"CZ","OM":"SK","HA":"HU","YR":"RO","LZ":"BG",
 "SX":"GR","TC":"TR","9A":"HR","S5":"SI","Z3":"MK","T7":"SM","LY":"LT","YL":"LV",
 "ES":"EE","ER":"MD","UR":"UA","EW":"BY","RA":"RU","RF":"RU","4K":"AZ","EK":"AM",
 "4L":"GE","UN":"KZ","EX":"KG","EY":"TJ","EZ":"TM","UK":"UZ","JU":"MN",
 "VH":"AU","ZK":"NZ","ZS":"ZA","ZT":"ZA","ZU":"ZA","5Y":"KE","5H":"TZ","5X":"UG",
 "9J":"ZM","Z":"ZW","ZM":"NZ","CCCP":"RU","DDR":"DE","DM":"DE","P4":"AW","A2":"BW","V5":"NA","7Q":"MW","C9":"MZ","5R":"MG","3B":"MU",
 "TU":"CI","TY":"BJ","TT":"TD","TR":"GA","TN":"CG","9Q":"CD","TJ":"CM","5N":"NG",
 "9G":"GH","TZ":"ML","XT":"BF","5U":"NE","6V":"SN","C5":"GM","9L":"SL","A6":"AE",
 "A7":"QA","A9C":"BH","A4O":"OM","9K":"KW","JY":"JO","OD":"LB","SU":"EG","ST":"SD",
 "7T":"DZ","TS":"TN","5A":"LY","CN":"MA","ET":"ET","4X":"IL","EP":"IR","YI":"IQ",
 "YK":"SY","AP":"PK","VT":"IN","4R":"LK","S2":"BD","9N":"NP","XY":"MM","XU":"KH",
 "RDPL":"LA","HS":"TH","9M":"MY","9V":"SG","V8":"BN","PK":"ID","RP":"PH","B":"CN",
 "JA":"JP","HL":"KR","P":"KP","XA":"MX","XB":"MX","XC":"MX","TG":"GT","YS":"SV",
 "HR":"HN","YN":"NI","TI":"CR","HP":"PA","CU":"CU","HI":"DO","HH":"HT","6Y":"JM",
 "9Y":"TT","8P":"BB","V2":"AG","J6":"LC","J8":"VC","VP-B":"BM","C6":"BS","VQ-T":"TC",
 "CC":"CL","LV":"AR","LQ":"AR","CX":"UY","ZP":"PY","CP":"BO","OB":"PE","HC":"EC",
 "HK":"CO","YV":"VE","8R":"GY","PZ":"SR","PP":"BR","PT":"BR","PR":"BR","PU":"BR",
 "PS":"BR","C-F":"CA","C-G":"CA","C-I":"CA","CF":"CA","9H":"MT","5B":"CY",
 "3A":"MC","9V":"SG","A3":"TO","DQ":"FJ","5W":"WS","C2":"NR","T2":"TV","P2":"PG",
 "H4":"SB","YJ":"VU","F-O":"FR","VP-C":"KY","2":"GG",
}
RE_DASHED = re.compile(r"^([A-Z0-9]{1,4})-([A-Z0-9]{2,5})$")
# Countries whose civil registrations legitimately carry a NUMERIC suffix.
# Everywhere else the suffix is letters, and a numeric one means the string is
# a military serial wearing a registration-shaped mask - RAAF A72-176 read as
# Qatar, Indonesian TT-0411 read as Chad, RAAF A20-627 read as Botswana.
NUMERIC_OK = {"RA","RF","CCCP","HK","CU","TG","YV","LV","CC","OB","CP","ZP","CX"}
# Military serial systems that are not registrations at all.
RE_RAAF = re.compile(r"^A\d{1,3}-\d{1,3}$")          # RAAF A72-176, A20-627
NOT_A_REG = {"OK-GLI"}                                # Buran orbiter designation
RE_N      = re.compile(r"^N[0-9][0-9A-Z]{0,4}$")          # US civil, bare N-number
RE_JA     = re.compile(r"^JA[0-9][0-9A-Z]{2,3}$")         # Japan, no dash
RE_B      = re.compile(r"^B-[0-9]{3,5}$")                 # China/Taiwan/HK - AMBIGUOUS
def from_registration(tail, site_countries=()):
    """Return (cc, rule) for an unambiguous civil registration, else (None, why)."""
    t = (tail or "").strip().upper()
    if not t: return None, "blank"
    if re.match(r"^N\d{1,4}$", t):
        # N556, N248, N949, N4172: a bare N-number is a US registration and is
        # also an RNAS/RAF, a French and an Indian serial. Settled downstream
        # by the manufacturer, not here.
        return None, "bare N-number is a US registration and also a British serial"
    if RE_N.match(t): return "US", "N-number"
    if RE_JA.match(t): return "JP", "JA-number"
    if t.startswith("B-"):
        # B- is shared by mainland China, Taiwan, Hong Kong and Macau. Only the
        # Hong Kong block is separable by shape: B-H / B-K / B-L plus letters.
        if re.match(r"^B-[HKL][A-Z]{2}$", t): return "HK", "B-H/K/L Hong Kong registration"
        return None, "B- prefix is shared by China, Taiwan, Hong Kong and Macau"
    if t in NOT_A_REG: return None, "a type designation, not a registration"
    if RE_RAAF.match(t): return "AU", "RAAF A-series serial"
    m = RE_DASHED.match(t)
    if not m: return None, "not a civil registration"
    p, suf = m.group(1), m.group(2)
    # EXACT prefix match only. Matching a prefix-of-the-prefix turned every
    # Soviet CCCP- registration into a Chilean CC- one (135 rows), P4- Aruba
    # into P- North Korea, and the Spanish code G1-AD into a UK G- registration.
    # Before 1929 Canada and Australia used blocks of the common British mark.
    # The UK reissued G-CAxx from about 2005, so the site decides: a 1920s
    # Canadian airframe is in Canada, a modern G-CAMM is not.
    if p == "G" and len(t) == 6:
        if t[2:4] in ("CA","CY") and "Canada" in site_countries:
            return "CA", "G-C Canadian Empire-era mark"
        if t[2:4] == "AU" and "Australia" in site_countries:
            return "AU", "G-AU Australian Empire-era mark"
    if p in DASHED:
        if not suf.isalpha() and p not in NUMERIC_OK:
            return None, f"{p}- with a numeric suffix is a military serial, not a registration"
        return DASHED[p], f"{p}- registration"
    # C-FABC / C-GABC arrive as prefix "C"
    if p == "C" and len(t) == 6 and t[2] in "FGI": return "CA", "C-F/G registration"
    return None, f"unrecognised prefix {p}"
