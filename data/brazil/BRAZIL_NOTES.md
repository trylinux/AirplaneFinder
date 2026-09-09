# BRAZIL — Pass 1 (public civilian museums + discovery sweep) — NOTES

Status: final for this pass (search engines were unavailable for most of it — see §1; a follow-up sweep with working search is recommended, §7/§8).
Build script: `_build_brazil_p1.py` (+ `_extra_sites.py` for sites added later). Re-run it to regenerate the CSVs.

## 1. Sources and their weight

| Source | Weight | Notes |
|---|---|---|
| Museum's own pages (MUSAL "Aeronaves do Acervo" article titles, Panambi museum posts, MuseusBr/IBRAM cadastro entries) | High for "is it here / is the museum open" | fab.mil.br and marinha.mil.br are behind a Cloudflare challenge in this environment; MUSAL page titles were harvested from search-engine indexes (one page per airframe, e.g. "MIRAGE 2000 - DASSAULT-BRÉGUET F-2000C", "SIKORSKY S-61 (SH-3) SEA KING", "BELL 47G-2 (H-13H)"). MuseusBr (cadastro.museus.gov.br) gave status (Aberto/Fechado), address, CEP and hours for every museum. |
| Aviação em Floripa blog, "Uma visita ao Ninho das Velhas Águias" (visit 23 Aug 2022) | High (currency + serials) | 55-airframe MUSAL walk-round with serials as painted. |
| AeroEntusiasta forum "Aviões Preservados pelo Brasil", compilation updated 9 Feb 2026 (fetched directly) | High (currency) | Lists MUSAL jets/transports (AT-26 4462/4499/4525/4634, C-130 2453/2476, KC-130 2462, F-103 4904/4913, F-2000 4948, P-47 4120/4184, UP-16 7037, VC-96 2116, L-188 PP-VJM) and the full Panambi list. |
| aerialvisuals.ca Location Dossier 4149 (MUSAL) + 95 airframe dossiers; Location Dossiers for Bebedouro (6503), Catavento (16214) etc. | Medium (identity, c/n, ex-serials, coordinates) | Undated for most entries; used for identities, not currency. |
| en/pt Wikipedia MUSAL inventory (Sept 2012 site survey) | Medium | Backbone for the pre-2012 collection; "not displayed Sept 2012" items carried as in_storage unless seen later. |
| Wikimedia Commons categories (MUSAL 2012 photos; MAB 2019/2023 photos) | Medium | Photo evidence of presence. |
| Pass 2 / Pass 3 notes (this project) | High | Their "Leads for other agents" sections were folded in; sites they recorded were NOT duplicated. |
| Grokipedia | not used | |

Search engines (WebSearch budget, Google, Bing, DDG) were unavailable for most of this pass; discovery relied on the AeroEntusiasta compilation, MuseusBr registry search, Wikipedia API search, aerialvisuals Locator directory (17 Brazilian regions) and Commons.

## 2. Sites recorded (Pass 1)

| File | Site | Rows | With tail |
|---|---|---|---|
| museu-aeroespacial-rio_aircraft.csv | Museu Aeroespacial (MUSAL), Rio de Janeiro RJ | 119 | 101 |
| museu-eduardo-andre-matarazzo-bebedouro_aircraft.csv | Museu de Armas, Veículos e Máquinas Eduardo André Matarazzo, Bebedouro SP | 18 | 10 |
| museu-catavento-sao-paulo_aircraft.csv | Museu Catavento, São Paulo SP | 1 | 1 |
| museu-militar-brasileiro-panambi_aircraft.csv | Museu Militar Brasileiro (ACMMB), Panambi RS | 18 | 13 |
| museu-do-expedicionario-curitiba_aircraft.csv | Museu do Expedicionário, Curitiba PR | 1 | 0 |
| museu-asas-de-um-sonho-itu_aircraft.csv | Museu Asas de um Sonho, Itu SP (replicas only) | 4 | 0 |
| museu-epcar-guaramiranga_aircraft.csv | Museu EPCAR Turma 73/AFA/76, Guaramiranga CE | 4 | 3 |
| museu-de-cabangu-santos-dumont_aircraft.csv | Museu de Cabangu, Santos Dumont MG | 1 | 0 |
| espaco-cultural-da-marinha-rio_aircraft.csv | Espaço Cultural da Marinha, Rio de Janeiro RJ | 2 | 1 |
| sitio-do-carrocao-dc-3-tatui_aircraft.csv | Sítio do Carroção DC-3, Tatuí SP | 1 | 1 |
| **Total** | **10 sites** | **169** | **130 (77%)** |

MUSAL serial coverage by slice: A–F 55 rows/44 tails, G–M 30/26, N–Z 34/31 (rows without tails are the 1920s-40s airframes wearing period markings, the gliders/ultralight and the H-13H).

## 3. Corrections / identity notes

- **MUSAL Albatross**: painted 6529 but aerialvisuals identifies the airframe as 6534 (c/n G-037, ex 49-0079) — tail 6534, 6529 alias.
- **MUSAL P-47D 4184**: ex 45-49151 (Virginia ANG), painted 420339 "B4"; Wikipedia's 2012 table gives the painted USAAF number as the identity.
- **MUSAL Xavante 4462**: Pass 2 blanked the EEAR Guaratinguetá Xavante painted 4462; MUSAL's 4462 is c/n 71-001-244, the first Brazilian-built Xavante, and is kept as the genuine one. Wikipedia's 2012 survey says the airframe then painted 4462 was really 4525 — both are now listed at MUSAL (2026 compilation), so both rows exist.
- **MUSAL Bell 206**: painted 8571 (2022); aerialvisuals gives 8591 for c/n 1382 — tail 8571, 8591 alias.
- **MUSAL T-28**: displayed as Navy N-703; true history T-28A 50-0202 → Hamilton T-28R-1 Nomair N9104Z → Navy N-703 → FAB 0862.
- **MUSAL DC-3 PP-AVJ**: painted as Aerovias Brasil; probably ex-FAB C-47A 2024 / N4946F (arrived 1996) — flagged "probably".
- **Bebedouro Meteor**: Wikipedia says one Meteor "of 1954" but Ogden and historiadafab list both 4409 and 4442 there — see below.
- **Panambi R-35A 6002**: the 2026 compilation lists 6002 both at Panambi and as a fuselage in a Porto Alegre scrapyard; one is wrong. Kept at Panambi (museum has a dedicated Learjet post).
- **Panambi AT-26 "4616"**: the same number is quoted for the Paulo Bento monument, which Pass 3 recorded with tail 4616. Tail blanked here, 4616 as alias (one is a painted number).
- **MUSAL Meteor F.8 4460**: not a museum composite — it was assembled by PAe-SP from spares and flew as 4399 then 4460 as the 1º GAvCa target tug until its delivery flight to MUSAL on 22 Apr 1974 (historiadafab.rudnei.cunha.nom.br). 4399 added as alias.
- **Bebedouro Meteors**: historiadafab's F-8 fate list confirms both 4409 and 4442 'preservado Bebedouro'; two rows with tails.
- **Guaramiranga Xavante "4570"**: number also claimed at Recife and Porto Velho; tail blank as in Pass 2.

## 4. Judgment calls

- **Replicas**: MUSAL's 14-bis (1973) and Demoiselle replicas recorded and flagged "a replica". The Itu museum currently shows only replicas (14-bis, Demoiselle, Blériot XI, DSL "São Paulo"); recorded and flagged so the site exists in the database, because the ex-TAM originals are announced to follow.
- **Wrecks as exhibits** (Panambi AMX 5656, T-25 1939): recorded, described as wreckage.
- **Fuselages** (Panambi C-115 2369, second C-95): recorded with "fuselage" in description/alias.
- **display_status**: "in_storage" used for MUSAL airframes last confirmed only in the 2012 "not displayed" list or only by the aerialvisuals/2026 compilation without a visitor sighting (B-17 5408, PT-26 0310, T-6 1617, L-42 3225, H-13J 8510, C-119 2305, C-82 2202, PV-1, C-47 2015, C-95 2150, UH-1H 8683, AT-26 4499/4525, P-47 4120, T-22 0811). MUSAL has ~150 airframes in total per FAB, so a reserve collection is certain.
- **Museu do Expedicionário P-47**: sits on the plaza outside the museum (a plaza monument by form) but is the museum's signature exhibit and was in this pass's assignment; recorded here, so Pass 3 should not add it.
- **Access**: `public` everywhere except Sítio do Carroção (`appointment` — a school/holiday camp, entry only with booked groups). MUSAL is inside the Campo dos Afonsos base perimeter but has its own public entrance and free admission. Museu EPCAR Guaramiranga is a private paid museum in a hotel garden, open daily.
- **Espaço Cultural da Marinha AF-1**: only the aerialvisuals Locator reports a Skyhawk beside the Sea King; recorded with blank tail and `in_storage` so it is not advertised as viewable until confirmed.
- **Cabangu**: only the T-23 recorded; its 14-bis/Demoiselle replicas are noted, not recorded.

## 5. Excluded (do not re-research without new evidence)

- **Museu Asas de um Sonho / Museu TAM, São Carlos** — closed since 29 Jan 2016; ~100 airframes still in the São Carlos hangar (AT-26 4566, F-103 4908, P-47D 4109 "B2", UP-16 7034, VU-93 2128, Constellation PP-PDD, Bf 109, Spitfire, Corsair, MiG-21, Jahu S.55 etc.). Not visitable. Ten of them (Bf 109, Fokker T-22, AT-6D, T-27, T-25, C-95, AH-2 Sabre helicopter…) were trucked to Campo de Marte in 2025 for the **Museu Aeroespacial Paulista (MAPA)**, activated 3 July 2026 with only a 200 m² Hangar 01 for meetings; public opening announced for 2027. Neither site recorded.
- **Museu da Aeronáutica (Fundação Santos-Dumont), São Paulo** — closed 2000 (Oca, Ibirapuera), collection moved to Cotia then dispersed (Jahu to Museu TAM 2007; relics to NUBAST Santos). No public site.
- **Museu Varig / Fundação Ruben Berta, Porto Alegre** — no airframe on public display; the "Varig Vive" 727 PP-VLD at Nova Petrópolis is a construction site (Pass 3 exclusion).
- **Museu Aeroespacial "Entre Nuvens e Estrelas", Universidade Tuiuti do Paraná, Curitiba** — MuseusBr status "Fechado"; collection is models/relics only. (The UTP campus Xavante 4631 is a Pass 3 record.)
- **MUSAL Dornier Do 24ATT** — photographed at MUSAL in the 2000s; returned to Dornier and flying again (RP-C2403). Not present.
- **MUSAL C-45M "491 FACh"** and **C-47A 43-15495 "TC-21"** — aerialvisuals dossiers point to MUSAL but are Chilean/Argentine airframes with no Brazilian evidence; not recorded.
- **MUSAL F-5E cockpit simulator, Boeing 727 Varig simulator, Embraer 190 VC-2 (operational visitor)** — not airframes.
- **Museu de Tecnologia de São Paulo** (Taboão da Serra) — closed 2011; its DC-3 is the Catavento aircraft.
- **Casa de Cultura Aeroespacial, Alcântara MA** — replica Sonda 4 only.
- **"Manaus Air Museum" Meteor T.7 4308** (Ogden survivors list / historiadafab "preservado Manaus/AM") — no such museum could be found; Pass 2 found nothing at Base Aérea de Manaus. Unverified, not recorded.
- **Ogden's MUSAL Meteors T.7 4300 (ex WS142) and "T.8 4453"** — not in the 2012 survey or the 2022 visit; not recorded (possible reserve-hangar items — see §7).
- **Museu Aeroterrestre (Brigada Pára-quedista), Vila Militar Rio** — MuseusBr "Aberto", but its C-47 is Pass 2's brigada-paraquedista-deodoro record; not duplicated.
- Pass 2 recorded: Museu da Aviação Naval (SPA), Memorial Aeroespacial Brasileiro (SJC), CLBI/CCEIT Parnamirim — not duplicated. Pass 3 recorded the ULBRA Xavante, Garibaldi and Tijucas 'Posto do Avião' airframes, Jardim Secreto do Capitão (Gramado), Univali Piçarras, Universidade Tuiuti Xavante and the Cascavel airport 737 — not duplicated.
- **Beto Carrero World, Hopi Hari, MCT-PUCRS, Museu Militar do Comando Militar do Sul, Museu Histórico e Militar de Bauru, Museu Militar Conde de Linhares, Museu Santos Dumont (Petrópolis), Estação Ciência** — no evidence of a real airframe found (Wikipedia/MuseusBr checks); not recorded.

## 6. Blank fields, deliberately

- Tails blank where only painted early-era markings exist (MUSAL Stearman "K132", Jungmann "FAB 07", Fledgling "K-263", Tiger Moth "105", Fw 44 "N-161", Widgeon "FAB 14", Waco CJC/CSO/RNF, Nieuport "N2102"); the markings are aliases.
- Bebedouro: only the eight aerialvisuals-documented airliners/bomber have identities; the fighters/light aircraft are described from the Wikipedia/UNESP summary.
- Panambi: 737 identities from the 2026 compilation (PP-SFJ, N393US); the museum itself publishes none.
- Coordinates: MUSAL (aerialvisuals site C, hangar apron), Bebedouro, Catavento (aerialvisuals), Panambi (Wikipedia infobox) — museum position, not individual airframes. Blank for Curitiba and Itu.

## 7. Needs a human on site (ranked)

0. A repeat sweep with a working search engine: this pass could not run the state-by-state Portuguese keyword searches the brief asks for (WebSearch budget exhausted after the MUSAL phase; Google/Bing/DDG blocked from the sandbox). Discovery therefore leaned on the AeroEntusiasta compilation (already mined by Pass 3), MuseusBr and aerialvisuals. Museums possibly missed: aeroclube museums, university displays (UFMG CEA, UnB), any post-2024 private collection openings.
1. MUSAL reserve hangar: which of the in_storage rows are actually on view now (B-17 5408, C-82 2202, C-119 2305, PV-1, C-47 2015, second/third Xavantes, P-47 4120, C-130M 2476)?
2. Bebedouro: confirm both Meteors and read the T-33, T-6 and Invader serials; confirm the museum is still open after the 2006 flood damage and whether all 17-19 airframes survive.
3. Itu: which ex-TAM originals (if any) have joined the replicas since Aug 2024?
4. Museu do Expedicionário P-47: read the data plate/serial (three different identities quoted).
5. Panambi: confirm the two 737 registrations and the three H-1H serials.

## 8. Leads for other agents / follow-up sweep

- **Pass 3 (monuments)**: aerialvisuals Locator entries not in Pass 3's files — Campinas, Campo dos Amarais airfield: Grumman G-64/SA-16A Albatross FAB 6535 (c/n G-038, 49-0080) as PP-ZAT, based/parked there (film-prop paint 2009; -22.8626,-47.1064); São Bernardo do Campo (Cidade da Criança) DC-3 PP-ANN (c/n 1992, ex NC18116) at -23.6872,-46.5575, aerialvisuals says on site since 1970 — park status unknown; Olinda AESO campus DC-3-277C PT-BFU (c/n 2248) -8.0052,-34.8753; Olinda F-80C 4215 (ex 49-0622) -8.0621,-34.9041 (Pass 3 recorded the Sport Recife jet as AT-33 4315 — this is a second, separate Olinda location per aerialvisuals 8097); Tatuí airfield Vampire T.35 PP-XUI (ex RAAF A79-645) — possibly airworthy/private, -23.3313,-47.8794; Recife Espaço Ciência (Olinda) Xavante — site unreachable, unverified; Campinas Parque Taquaral BT-15 PP-GRK — unverified.
- **Pass 2**: MUSAL-adjacent Army/FAB sites already in Pass 2. Ogden lists Meteor T.7 4300 at MUSAL — if a base-side hangar tour is ever possible, look for it.
- **Future Pass 1 (2027)**: Museu Aeroespacial Paulista (MAPA), PAMA-SP/Campo de Marte, São Paulo — 80 aircraft planned (40 ex-Museu TAM incl. Bf 109G-4, Spitfire IX, F4U-1 Corsair; 40 FAB). Re-check opening in 2027 and move the São Carlos/MAPA airframes then.

## 9. File / row-count table

See §2. Totals: 10 sites, 169 aircraft rows, 130 with tail numbers (77%). Build output: `python3 _build_brazil_p1.py`.


---

# BRAZIL — Pass 2: military base collections — research notes

Output directory: `/home/claude/sa/brazil_p2/`. Museums file `br_museums.csv` (43 sites), 43 `<slug>_aircraft.csv`
files (143 rows, 122 with tail numbers). Scope: FAB, Navy and Army sites (bases, wings, schools, depots, HQs,
CINDACTAs, launch centres, museums that sit inside a military fence). Civilian museums and town monuments are
NOT recorded here — they are listed under "Leads for other agents" at the end.

## Sources and weight

| Source | Weight | Comment |
|---|---|---|
| AeroEntusiasta forum, "Aviões Preservados pelo Brasil" — state-by-state compilation posted 14 Jan 2026, updated 9 Feb 2026 (forum.aeroentusiasta.com.br t=27215, pages 180+) | **High (currency)** | The single best currency source found. Spotter-community list with serials and exact locations. Used as the backbone. Its author flags doubtful serials with ???? / XXXX; I did the same (blank). |
| Same forum thread, individual dated posts 2009-2025 (installation news, dated photos) | High for the airframe/date concerned | e.g. F-5E 4882 trucked to Canoas Nov 2016; EC-95B 2307 inaugurated 16 Aug 2019; A-1A 5542 inaugurated 9 Nov 2017; A-1A 5538 seen at DECEA 4 Nov 2024; F-5B 4802 geolocated at CAE 6 Dec 2024. |
| Aviação em Floripa blog, "Santa Cruz: uma Base Aérea com muitas histórias — Parte 2" (May 2025, photos M. Lobo da Silva) | **High** | Full inventory of the seven BASC aircraft with identities (incl. the Impala Mk.1 story); also "Revisitando o Museu da Aviação Naval" (Nov 2023) and "Asas eternas — aeronaves da FAB preservadas em SC" (Dec 2020). |
| Gaceta Aeronáutica, "Preservados Aviación Naval Brasileña" parts 1 & 2 (Jan 2025) | High | Complete list of the Museu da Aviação Naval park with serials/c-ns and of the three base displays at BAeNSPA. |
| ABRAPAC / L. C. Saraiva, "Aeronaves preservadas e estocadas no Brasil" PDF dated 12 Nov 2019 (aeromuseu.com.br) | Medium — **stale by 6+ years** | Comprehensive but 2019. Where a 2019 entry is absent from the 2026 compilation I recorded it with an explicit "not in Feb 2026 list, presence needs confirmation" caveat (C-47 2032 Belém; C-47 2075 EEAR; AT-26 4575 and T-6 1478 Cumbica; F-5E 4880 PAMA-SP; EPCAR T-23/T-6/AT-33/H-1H). Several of its serials are typos (F-8 "4494" Salvador; F-103 "4916" for the Gama plaza) — corrected from other sources. |
| aviagraphers.net "Brazilian aircraft monuments" | Low-medium (undated photos, ~2010s) | Used for unit markings and a few identities; contradicted on Porto Velho serial. |
| Wikipedia survivor lists (Meteor, P-47, A-26, B-17) | Lead only | Meteor list contains internal contradictions for Canoas (4433 vs 4448) and a typo for Salvador (4004). |
| aerialvisuals.ca | Low (many timeouts) | Used only to pull ex-identities for B-25J 5133 (44-30245), B-26 5156 (44-35586), SB-17G 5402 (44-85583), F-80C 4225 (49-0827), CA-10 6552 (BuNo 46643). |
| Poder Aéreo, Aeroflap, Cavok, Correio Braziliense articles | Medium, dated | BARF deactivation (July 2024); Anápolis 2024 Portões Abertos comments (Mirage III 4910, Mirage 2000 4940); PAMA-SP Mirage 4927 inauguration (Apr 2012); Mirage 2000 fleet fate. |
| fab.mil.br / www2.fab.mil.br (AFA per-aircraft pages) | High for identity, but pages are behind Cloudflare and could not be fetched; used only via search-result titles ("F-103E FAB 4925 - AFA", "H1-H FAB 8702 - AFA", "T-21 FAB 0710", "TZ-13 Blaník FAB 8010", "G-19 Ipanema FAB 0152", etc.). |

Web search budget was exhausted about two-thirds of the way through; the remaining verification was done by
direct fetches of known URLs. Google Maps/Flickr could not be reached.

## Corrections made (with evidence)

- **Santa Cruz "Xavante 4458"** is an ex-SAAF Atlas Impala Mk.1, never in FAB service, wearing a fictitious serial from the Meteor block (Aviação em Floripa, May 2025). Same applies to the Impalas painted 4456 (Colégio Militar do Recife), 4457 (Vinhedo), 4459 (Volta Redonda), 4460 (Porto Velho) and 4461 (Brasília). Recorded with blank tail, marking in aliases.
- **Santa Cruz P-47** is 42-26757 (wartime A5, FAB 4107) painted as 44-19660 C5 (FAB 4118). Recorded tail 4107, false markings in aliases.
- **Santa Cruz Xavante serial** given as 4450 in ABRAPAC 2019 and 4458 in the 2025/2026 sources; 2019 also listed P-47 "419660" as a second airframe — that is the painted USAAF serial of the same P-47, not a second aircraft. Only seven aircraft exist at BASC (confirmed May 2025).
- **Florianópolis "SH-1D 8535"** is UH-1H 8697 restored in 1970s SAR colours (Aviação em Floripa, Dec 2020). Recorded tail 8697, 8535 as alias.
- **PAMA-SP**: F-5B 4803 removed from the entrance plinth in 2012 in favour of Mirage 4927; 4803 stayed inside PAMA-SP/COMGAP and by 2018 wore "Ayrton Senna" titles. Recorded at PAMA-SP (2026 list), not COMGAP.
- **C-95 2190** listed at Base Aérea do Recife in 2019 is at CENIPA Brasília in 2026 — recorded at CENIPA only.
- **C-115 2353** stored at Base Aérea de Manaus in 2019 is at the Army's Comando Militar da Amazônia in 2026 — recorded at CMA.
- **AT-26 4535** was inside CINDACTA III in 2019; it is now the gate guard of the former BARF (2026 list; Poder Aéreo July 2024 gate photo).
- **Anápolis gate Mirage**: Cavok's Nov 2010 inauguration piece says 4926, but 4926 went to the Gama plaza in Aug 2011 and the FAB's own Flickr caption plus both compilations give 4915 for the BR-414 gate. Recorded 4915.
- **Salvador Meteor** recorded 4404 (2026 list); "4494" (ABRAPAC) and "4004" (Wikipedia) are typos.
- **Base Aérea do Recife** was deactivated 11/24 July 2024; monuments passed to CINDACTA III. Site named accordingly and access left `restricted`.

## Judgment calls

- **Access type**: every site inside a military gate is `restricted`, even where the airframe is visible from the road (Galeão C-91, Fortaleza F-80, Salvador Meteor, Recife B-17, Anápolis Mirage). Museu da Aviação Naval (free entry, published hours, inside BAeNSPA), Memorial Aeroespacial Brasileiro (inside DCTA), CLBI visitor centre and the DECEA plaza at Santos Dumont are `public`.
- **Museums inside the fence** (Museu da Aviação Naval, Memorial Aeroespacial Brasileiro, CLBI/CCEIT) are recorded here per the brief; **coordinator: check pass 1 for duplicates** of these three.
- **Coordinates** are base/site-level (Wikipedia base coordinates), never airframe-level; blank where no coordinate was found. Address fields are the base's public street address where known.
- **Nose sections**: Mirage III "4930" nose at BAAN and AF-1 N-1014 cockpit at the naval museum are recorded and flagged in description; the KC-137 2404 fin at Galeão and F-5/AMX fins used as monuments at Santa Cruz are NOT recorded (not airframes).
- **Hangar-kept aircraft** at the AFA (T-21 0710, T-6 in EDA colours, two T-27 hung in the EDA hangar) recorded as `in_storage`; Mirage 4922 at BABR (`armazenado`) and Bell 47 PP-HUF (restoration) likewise.
- **Duplicate painted serials**: where the same 4-digit serial is claimed at two sites and I could not tell which is genuine, the tail is blank and the painted number is an alias: 4462 (EEAR vs MUSAL), 4570 (Recife interior vs Museu EPCAR Guaramiranga vs Porto Velho 2019). VU-93 2118 (II COMAR) is kept with tail because only the 2019 list put it at MUSAL.
- **A-29 at Boa Vista**: compilation serial "5525" is an AMX serial; tail left blank.
- **Porto Velho Xavante**: four sources, four serials (4460 Impala per Aviação em Floripa; 4478 aviagraphers; 4570 ABRAPAC; 4578 AeroEntusiasta). Tail blank, 4460 and 4578 as aliases.
- **EEAR "A-1B 5650"** may be a mock-up (ABRAPAC 2019); recorded with that flag rather than excluded, because the 2026 compilation lists it as an aircraft.
- **CLBI rockets** (Sonda I, Nike-Apache) recorded although the source is ambiguous about original vs replica; flagged.
- **Model field** uses FAB designations (F-103, F-8, AT-26, AT-33, TF-33, C-115, C-95, VU-93, P-16, P-15, CA-10, H-1, H-13, H-50, F-2000, T-25, TZ-13, G-19) with manufacturer designations in aliases, consistently.

## Excluded, and why

- **Casa de Cultura Aeroespacial, Alcântara (CLA)** — displays a full-size *replica* Sonda 4 plus models; no real rocket found. Not recorded.
- **CIAvEx / Base de Aviação de Taubaté** — has a "Museu de Aviação do Exército" of models, uniforms and documents; no preserved airframe could be confirmed. Not recorded (open question below).
- **Escola Naval, CIAAN** — no preserved airframe found in any source.
- **CIAAR Lagoa Santa** — no preserved airframe found.
- **Base Aérea dos Afonsos / UNIFA** — nothing beyond MUSAL (pass 1). ABRAPAC 2019 "AT-26 4604 at CEMAL on a pedestal" and "EMB-121 Xingu at the FAB school on Ilha do Governador" could not be confirmed and are not recorded.
- **Base Aérea de Manaus** — C-115 2367 "at the base" in 2019 is absent in 2026; C-105 2360 (aviagraphers) is an operational aircraft. Nothing recorded.
- **T-27 1345 Canoas** — seen dismantled at the Vila dos Sargentos in Nov 2024 "to become a monument"; intent, not arrival. Not recorded.
- **F-5EM 4856, 4871, 4850 at PAMA-SP** (2022) — in transit/storage pending MUSAL; not recorded.
- **KC-137 2404** (Galeão) — vertical fin only.
- **Mirage 2000 4948** — at MUSAL (pass 1). The nine Mirage 2000 sold to PROCOR (2019) are gone.
- **B-17 5408** — MUSAL, stored (pass 1).
- **Fortaleza AT-26 "4460"** (ABRAPAC 2019, no location) — unlocated; not recorded.
- **Mirage 2000B at Brasília** is recorded but with blank tail (see open questions).

## Deliberately blank fields

- `year_built` everywhere (no sourced build dates).
- `postal_code` everywhere (CEPs not verified).
- `tail_number` blank on 21 rows: AFA unidentified airframes (T-6 ×2, T-27 ×3, A-1, T-25, H-1H), EEAR Xavante and H-1H, Recife interior Xavante, Colégio Militar Recife Impala, Santa Cruz Impala, Porto Velho Impala, Boa Vista A-29, Brasília Mirage 2000B, PAMA-LS C-95 and T-25, MAB AMX prototype, CLBI rockets.
- `latitude/longitude` blank on 17 sites.

## Needs a human on site (ranked)

1. **Academia da Força Aérea** — read the serials of the un-identified line aircraft (T-6, T-27, A-1, second T-25, second H-1H) and the EDA hangar aircraft; confirm 4925/4413/4328/4883 still in the line after the Oct 2023 storm (only operational T-27s were reported damaged).
2. **Base Aérea de Natal** — confirm the nine aircraft (esp. B-25J 5133 and the fourth Xavante 4622) and whether a formal "Memorial" exists with visiting arrangements.
3. **Base Aérea de Brasília** — identify the Mirage 2000B on display (4932 or 4933?) and whether Mirage III 4922 is viewable.
4. **Canoas gate Meteor** — 4433 or 4448?
5. **Porto Velho / Recife interior / EEAR Xavantes** — read the painted serials and look for c/n plates.
6. **EEAR "A-1B 5650"** — real airframe or mock-up?
7. **Belém C-47 2032, EEAR C-47 2075, Cumbica AT-26 4575 and T-6 1478, PAMA-SP F-5E 4880, EPCAR T-23/T-6/AT-33/H-1H/Meteor 4406** — 2019-only entries; still there?
8. **CIAvEx Taubaté** — is there any airframe (HA-1, UH-1, Pantera) on a plinth?
9. **CLBI** — are the Sonda I and Nike-Apache real rounds?

## File / row-count table

| File | Rows | With tail |
|---|---|---|
| br_museums.csv | 43 sites | — |
| base-aerea-santa-cruz_aircraft.csv | 7 | 6 |
| base-aerea-galeao_aircraft.csv | 1 | 1 |
| cae-ilha-do-governador_aircraft.csv | 1 | 1 |
| decea-santos-dumont_aircraft.csv | 1 | 1 |
| cgcfn-ilha-das-cobras_aircraft.csv | 1 | 1 |
| brigada-paraquedista-deodoro_aircraft.csv | 2 | 2 |
| museu-aviacao-naval-spa_aircraft.csv | 11 | 11 |
| baensp-displays_aircraft.csv | 3 | 3 |
| aman-resende_aircraft.csv | 1 | 1 |
| base-aerea-anapolis_aircraft.csv | 5 | 5 |
| base-aerea-brasilia_aircraft.csv | 3 | 2 |
| cenipa-brasilia_aircraft.csv | 3 | 3 |
| comdabra-brasilia_aircraft.csv | 1 | 1 |
| base-aerea-canoas_aircraft.csv | 4 | 4 |
| base-aerea-santa-maria_aircraft.csv | 2 | 2 |
| base-aerea-florianopolis_aircraft.csv | 1 | 1 |
| base-aerea-campo-grande_aircraft.csv | 1 | 1 |
| cindacta-iv-manaus_aircraft.csv | 1 | 1 |
| cma-manaus_aircraft.csv | 1 | 1 |
| base-aerea-belem_aircraft.csv | 2 | 2 |
| base-aerea-boa-vista_aircraft.csv | 1 | 0 |
| base-aerea-porto-velho_aircraft.csv | 1 | 0 |
| cpbv-cachimbo_aircraft.csv | 1 | 1 |
| base-aerea-natal_aircraft.csv | 9 | 9 |
| base-aerea-recife-cindacta-iii_aircraft.csv | 4 | 3 |
| comar-ii-recife_aircraft.csv | 3 | 3 |
| hospital-aeronautica-recife_aircraft.csv | 1 | 1 |
| colegio-militar-recife_aircraft.csv | 1 | 0 |
| base-aerea-fortaleza_aircraft.csv | 2 | 2 |
| base-aerea-salvador_aircraft.csv | 2 | 2 |
| dtcea-fernando-de-noronha_aircraft.csv | 1 | 1 |
| clbi-barreira-do-inferno_aircraft.csv | 3 | 1 |
| afa-pirassununga_aircraft.csv | 20 | 12 |
| eear-guaratingueta_aircraft.csv | 9 | 7 |
| epcar-barbacena_aircraft.csv | 6 | 6 |
| pama-lagoa-santa_aircraft.csv | 3 | 1 |
| pama-sao-paulo_aircraft.csv | 4 | 4 |
| comgap-sao-paulo_aircraft.csv | 1 | 1 |
| base-aerea-sao-paulo-cumbica_aircraft.csv | 3 | 3 |
| dcta-sao-jose-dos-campos_aircraft.csv | 4 | 4 |
| memorial-aeroespacial-brasileiro_aircraft.csv | 9 | 8 |
| cindacta-ii-curitiba_aircraft.csv | 2 | 2 |
| colegio-militar-curitiba_aircraft.csv | 1 | 1 |
| **Total** | **143** | **122 (85%)** |

## Leads for other agents (outside pass-2 scope)

All from the AeroEntusiasta Feb 2026 compilation unless noted; FAB serials as listed there.

**Pass 1 / museums (possible overlaps with this pass):** Museu da Aviação Naval (São Pedro da Aldeia), Memorial Aeroespacial Brasileiro (São José dos Campos) and CLBI/CCEIT (Parnamirim) are recorded HERE — dedupe. MUSAL holds Mirage 2000 4948, F-103 4904 & 4913, AT-26 4462/4499/4525/4634, C-130 2453/2476, KC-130 2462, P-47 4120 & 4184, UP-16 7037, VC-96 2116, Electra PP-VJM, VU-93 2118 (2019). Museu EPCAR Turma 73 (Hotel Vale das Nuvens, Guaramiranga/CE — private, paid): A-1A 5524, AT-26 4570, H-1H 8684, T-25 1961. Museu Militar Brasileiro, Panambi/RS: A-1B 5656 wreck, AT-26 4616, C-115 2368 & 2369 (fuselage), C-95 ×2, H-1H 8654 + two more, P-95A 7052, R-35A 6002, T-25 1875/1926/1939, 727 PR-TTP, 737s PP-SFJ & N393US, PA-23 PT-ATW. Museu Asas de um Sonho (São Carlos) closed — AT-26 4566, F-103 4908, P-47 4109 "B2", UP-16 7034, VU-93 2128 to go to the new Museu Aeroespacial Paulista (MAPA) per Aviação em Floripa 2025. Museu do Expedicionário, Curitiba: P-47D 45-49485 painted "A4". Museu de Armas, Bebedouro: Meteors 4409/4442, A-26 "5176", TF-33, T-6s etc. Museu Catavento SP: DC-3 PT-KUB. Museu Casa de Cabangu (Santos Dumont/MG): T-23.

**Pass 3 / monuments — FAB airframes on plazas/roads etc.:**
- RJ: A-1M 5530 Praça do Avião, Estrada do Galeão, Ilha do Governador (replaced a mock-up, 2020); AT-26 4459 Memorial dos Expedicionários and 4470 Praça Antônio Pedro da Costa, Volta Redonda (both ex-SAAF Impala Mk.1 with fictitious serials per Aviação em Floripa); C-130E 2451, 2456 and C-130H 2463 at Gamela Eco Resort, Cantagalo; 727 PP-BLR Ipiabas/Barra do Piraí; SH-3D N-3009 and AF-1 N-1006 (Navy) on the Lagoa de Araruama waterfront, São Pedro da Aldeia (inaugurated 2023 / Aug 2020).
- DF: F-103 4914 and AT-26 4475 Clube da Aeronáutica; F-103 4924 Clube SO/SGT; F-103 4926 Praça do Avião, Gama (Aug 2011); A-1A 5522 ENAJUM/STM garage (geolocated Nov 2024); 767 PT-TAC Taguatinga; 737 PP-SNA Planaltina.
- GO: F-103 4919 Praça Americano do Brasil, Anápolis; F-5EM 4836 Praça Ten. Diomar Meneses, Jataí; 737 PP-SPH Urutaí; E120 PP-ISF Simolândia.
- MG: F-5EM 4874 Praça do Avião, Carandaí (21 Nov 2022, first modernised F-5 preserved); C-95 2176 Espera Feliz; T-6 1261 Paraguaçu; UH-14 N-7070 (Navy) Praça do Soldado, Itajubá; 737s PP-SMC Contagem, PP-SMA Lagoa Santa, PP-SMB Nanuque, PR-MTG Caratinga; DC-8 PR-SKM etc. Poços de Caldas; E120 PR-OAN Monte Verde.
- SP: AT-26 4457 Vinhedo (Impala, false serial), 4491 Americana, 4495 Boracéia, 4560 Vila Galvão/Guarulhos, 4586 Pompéia, 4596 + C-115 2352 Aeródromo Broa/Itirapina, 4624 Itápolis, 4632 São José do Rio Preto, unidentified AT-26 Praça Fernando Arruda Botelho São Carlos; AT-33 4350 Dumont, AT-33 (serial ?) Assis airport; F-103 4929 Araras; C-95 2187 Bauru; C-115 2362 Auto Posto Bambina, Araraquara (ex-Brigada Paraquedista Deodoro); C-95 2132 Embraer main gate SJC; EMB-110 PP-ZDF Parque Santos Dumont SJC (restored 2018); T-27 1374 (Jardim América), T-25 1837 (Praça Ninho das Águias), T-25 1932 (praça) and T-6 1647 (Praça do Castelinho), all Pirassununga town; T-6 1235 Clube Náutico Guarapiranga SP; C-97 2014 Chalé Cantos das Águas, Igaratá; A-1 5521 Flyjet Blumenau (SC); P-16 7015 Laranjal Paulista; Phenom PP-XOH Botucatu; numerous airliners (see compilation).
- PR: F-8 4452 & F-5E 4879 are CINDACTA II (recorded here); AT-26A 4631 Universidade Tuiuti, 4472 Maringá; A-318 PR-ONO Morretes; VC-96 2115 Parque das Cataratas, Foz do Iguaçu; U-42 2948/2992 Toledo; Paranavaí E721 ZP-BLY.
- RS: F-8 4439 Praça do Avião Canoas; AT-26 4508 ULBRA Canoas, 4510 V COMAR rotunda/Praça FAB Canoas (30 Sep 2010), 4517 Mata (Dec 2018), 4526 Rio Grande, 4567 RSC-287 portal Santa Maria, 4615 Cachoeira do Sul airport, 4616 Paulo Bento; H-1H 8701 Av. Fernando Ferrari rotunda Santa Maria (removed for repaint Jul 2023, to be reinstalled); A-1B 5655 UFSM engineering hangar; T-6 1259 Erechim; Canela "Mundo Gelado" (C-130E 2459, C-130H 2478, two P-3AM, C-97, A-1, Bell 222 — dismantled); Porto Alegre scrapyard Rua Amynthas Jacques de Morais 50B (A-1A 5503/5529/5541/5544, A-29A 5725, F-5F 4806, P-95 7056/7060, R-35 6002, V-35 2716, H-1H — fuselages); DC-3 PP-ANU Porto Alegre; PP-VBT Garibaldi; 727 PP-VLD Nova Petrópolis.
- SC: T-6 1458 Brusque, 1287 Rio Negrinho; T-25 1841 Gaspar, 1854 Tubarão (May 2021); AT-26 4533 Aeroclube de SC São José (Sep 2017, c/n 75072315); SH-3 N-3012 (Navy) Univali Balneário Piçarras (Aug 2024) — an A-4 Skyhawk added 2026 per Sociedade Militar; YS-11 PP-CTI Tijucas.
- NE/N: AT-26 4587 Camocim, 4460 Fortaleza (unlocated), 4635 Triunfo, 4469 Florânia, 4514 Parelhas, 4639 Mossoró airport, 4493 Av. João Alencar Boa Vista, unidentified AT-26 Porto Nacional/TO; T-27 1381 Umirim; AT-33 4315 Sport Club do Recife; F-80C 4215 was also reported at Sport Recife (2019) — same site, check which serial; EU-93 painted "2011" Posto Marrone Recife; F-103 4931 Praça Orugan, Salvador; F-103 4909 Sorriso airport (MT); T-6 1415 Praça Cel Av Chaves Filho outside Base Aérea de Campo Grande; DC-3s Alta Floresta, Canarana, Carajás; 737s Presidente Figueiredo; VU-93 Faculdade AGES Lagarto/SE; Yak-40, MiGs etc. per compilation.

**Other countries:** none found.


---

# BRAZIL — Pass 3: monuments and off-base displays — NOTES

Output directory: `/home/claude/sa/brazil_p3/`
Museums file: `br_museums.csv` (121 site records). Aircraft: one `<slug>_aircraft.csv` per site (121 files, 141 rows).
Research date: 9 Sep 2026.

## 1. Sources and their weight

| Source | Date | Weight | Notes |
|---|---|---|---|
| **AeroFórum (forum.aeroentusiasta.com.br) thread "Aviões Preservados pelo Brasil", post of 14 Jan 2026 "primeiro compilado das aeronaves preservadas/monumentos", updated 09 Feb 2026, plus follow-ups to 5 Sep 2026** | 2026 | **Primary currency source.** A state-by-state compilation by the enthusiasts who also maintain the AeroEntusiasta "Série Preservados" blog. It gives serial/registration + venue for ~300 airframes (museums, bases, monuments, scrapyards). Treated as "reported present Feb 2026". Entries that are scrapyards, private farms, dismantled storage or fuselage dealers were excluded (see §4). | Saved locally as scratch; forum pages 0–300. |
| **ABRAPAC "Aeronaves preservadas e estocadas no Brasil"** (aeromuseu.com.br/preservadas_estocadas.pdf) | 12 Nov 2019 | Lead list with serials and c/ns; **stale by 6 years** — several entries have since moved (C-115 2352 Araraquara→Broa; Xavante Americana Praça Tiradentes→Parque Ecológico; Goiânia Meteor gone; 737 PP-SMA Vespasiano→Lagoa Santa). Used for serials/c/ns and cross-checked against 2026. |
| Monolito Nimbus (monolitonimbus.com.br) per-type pages (AT-26, T-6, T-27, Meteor, DC-3, Bandeirante) | 2016–18 | Location detail (square names, dates of installation, some coordinates). Stale for currency. |
| aviacaoemfloripa.com.br "Asas eternas" (Dec 2020) and AeroJota "aviões da FAB preservados em SC" (7 Aug 2025) | 2020/2025 | Authoritative for the six Santa Catarina FAB monuments incl. c/ns. |
| News (Aeroin, AeroJota, Cavok, Força Aérea, Aeroflap, Poder Aéreo, NSC, Maringá Post, prefeitura sites) | 2020–2026 | Dated installation/restoration events: Salvador Meteor (Jan 2025), Jataí F-5 (Jun 2023), Carandaí F-5 (Nov 2022), Itajubá UH-14 (Sep 2024), Pedras Grandes AMX (Sep 2026), Balneário Piçarras A-4 (Apr 2026), Gramado park (Jun–Aug 2026), Maringá Xavante fall/restoration (Aug 2026), Brusque T-6 (Aug 2025), Canarana DC-3 (Jun 2025), Alta Floresta DC-3 (Dec 2022), Bauru C-95 (Nov 2023), São Pedro da Aldeia A-4 (Aug 2020) and SH-3 (Aug 2023), Ilha do Governador A-1M (Apr 2020), Taguatinga 767 (Sep 2025), Mata Xavante (Dec 2018), Santa Maria H-1H (Jul 2023). |
| Photo sites: JetPhotos FAB4404 (5 Apr 2025), airplane-pictures.net FAB4931 (2 Nov 2025); Tripadvisor (Canoas Meteor May 2023, Guarulhos Xavante Jul 2025); Wanderlog (Gama Mirage coordinates, 767 Google reviews) | 2023–25 | Dated presence evidence. airhistory.net and abpic returned nothing usable (Cloudflare / no FAB entries). |
| Wikipedia "List of surviving Gloster Meteors" | — | Stale: still lists Goiânia 4411 (removed after vandalism; now at MUSAL per Monolito Nimbus). |

**Tooling caveat:** the shared web-search budget was exhausted about a third of the way through the verification phase and the fetch proxy then rate-limited hard, so roughly half the rows rest on the Feb-2026 AeroFórum compilation + ABRAPAC 2019 concordance rather than on an independent 2024-26 photo. Each description states which evidence it rests on.

## 2. Scope decisions

Included: aircraft on plinths/praças/roundabouts, airport forecourts, aero clubs, schools/universities, clubs, hotels/pousadas/resorts, restaurants/bars, fuel stations, shopping centres, theme/eco parks, factory gate guards visible from the street, derelict-but-landmark airliners that the public visits (Itacoatiara C-46, Taguatinga 767, Foz "Sucatinha").
Excluded: anything inside a military fence (Pass 2), civilian museums (Pass 1) — both listed in §7 as leads; scrapyards, dealers' yards, private farms with no access, training fuselages inside companies, projects not yet open.

## 3. Corrections and conflicts (with evidence)

- **Salvador Meteor** — serial is **FAB 4404** (JetPhotos 2025, Wikipedia list, 2026 compilation). AeroJota/aeroin headlines say "4004", which is not a valid FAB Meteor serial (F.8s were 44xx). 4004 kept in aliases.
- **Gama Mirage** — **4926** (Poder Aéreo 2010 inauguration article; 2026 compilation). ABRAPAC 2019 said 4916, which both ABRAPAC and 2026 place at COMDABRA; treated as an ABRAPAC error.
- **Sport Club do Recife jet** — ABRAPAC: F-80C 4215; 2026 compilation: AT-33A 4315. Recorded as AT-33A 4315 with 4215/F-80C in aliases. Needs a look (single- vs two-seat).
- **Araraquara / Itirapina Buffalos** — ABRAPAC 2019: C-115 2352 at the Araraquara fuel station; 2026: 2362 at Araraquara (Auto Posto Bambina) and 2352 at the Broa aerodrome. Followed 2026. (ABRAPAC had 2362 at the Deodoro Army brigade in Rio — it may have been released.)
- **Parelhas Xavante** — 4514 (2026) vs 4614 (ABRAPAC). Recorded 4514, alias 4614.
- **Paulo Bento vs Panambi "4616"** — 4616 (c/n 80170413) was inaugurated at Paulo Bento on 12 Oct 2005 (forum 2009, ABRAPAC). The 2026 compilation lists 4616 at both Paulo Bento and the Museu Militar Brasileiro, Panambi. Kept at Paulo Bento; the Panambi one (museum, Pass 1) must carry a false or misread serial — flagged for Pass 1.
- **False serials (recorded blank tail, marking in aliases):** Vinhedo "4457"; Clube de Aeronáutica de Brasília "4536" (real 4536 crashed Fortaleza 25 Nov 1987; possibly 4475); Rio Grande "4526" (composite airframe); Pedras Grandes AMX painted "5522" is really **5541** (recorded 5541); Posto Marrone HS-125 "2011"; Luís Eduardo Magalhães Learjet "PR-DMF" (real PT-LBW per compilation, recorded PT-LBW); Tefé PA-28 "PI-CAO"; Chapada Navion "??-MKK"; Toledo Regente 2948/2992 (paint removed).
- **Ilha do Governador** — a fibreglass AMX replica stood 1999–2020; since 14 Apr 2020 the real **A-1M 5530** is on the pylon. The 2026 compilation also lists "A1 FAB (0000 MOCK-UP) Praça do Avião" — that is the old replica entry; not recorded.
- **Alta Floresta DC-3** — PT-KVA (ABRAPAC, Monolito) vs PP-KVA (2026 typo?). Recorded PT-KVA.
- **Pacatuba DC-3** — PT-KZF (Monolito, 2026) vs PT-KYW (ABRAPAC). Recorded PT-KZF.
- **Regente Feijó Bandeirante** — PT-SCD (ABRAPAC) vs PP-SCD (2026). Recorded PP-SCD, alias PT-SCD.

## 4. Excluded (do not re-research without new evidence)

Removed / gone:
- Goiânia Praça do Avião Meteor **4411** — removed after vandalism, sent to MUSAL; only a 14-bis replica remains (Sagres Online; Monolito Nimbus).
- Fortaleza airport DC-3 PT-AOB — sold to Germany 2017 (Agência Brasil).
- Belo Horizonte Shopping Del Rey T-6 1552 and Meteor — removed years ago (Monolito Nimbus comments).
- Camocim: the real Xavante may have moved to the airport in 2023 — recorded at the praça with a caveat rather than excluded.

Not publicly accessible / private storage / scrapyards (all from the 2026 compilation unless noted):
- Manaus DC-8 PR-SKI "Aero River" — owner's private space, no access (Portal Amazônia 2021). Manaus Rico EMB-120s PP-ISG/PT-WGE on the company farm. Presidente Figueiredo 737s PP-VMM/PP-RLA on a private BR-174 property, not visible from the road (AeroEntusiasta 2020).
- Planaltina DF 737 PP-SNA at Haras Rancho Tokarski (private). Brasília "Pan Am Experience" F100 PR-OAF — venue nature unknown, no evidence of public display.
- Urutaí GO 737 PP-SPH — private fazenda; a restaurant conversion was only announced Jan 2026.
- Araraquara "Rancho do Piloto" 737s PP-SFI/PP-SMW (private ranch). Dom Pedrito RS 727 PR-TTB (private property). Itapejara d'Oeste PR Helisul farm (737 PP-SMH, 733 fuselage, two DC-3 fuselages, Learjet PT-LMS). Nova Odessa Ambipar 737 PP-SMR / PP-SMZ cockpit (corporate training). Porto Alegre Flight school 737 PP-VMH (training; 2026 says now Guaíba — location unknown). Poços de Caldas DC-8 PR-SKM + Lider bizjets on a vacant lot. Bernardino de Campos 737 PP-VME (tail only). Campinas 727s PP-JUB (scrapyard) and PR-LGC (festival dance-floor at Fazenda Invernada, not a permanent display). Fernandópolis/São Carlos "Sucatas Bim" EMB-120s. Porto Alegre Rua Amynthas Jacques de Morais fuselages (A-1A 5503/5529/5541-now-Pedras-Grandes/5544, A-29A 5725, F-5F 4806, P-95 7056/7060, R-35 6002, V-35 2716, H-1H) — a dealer's yard. Ribeirão Preto Yak-40 S9-BAP and Passaredo EMB-120s (airport apron). Caucaia and Maracanaú "Sucata Aeroporto" 727 PR-AIB / 737 PT-MTF (scrapyards). Recife airport A300 PR-STN (stored). Tefé/Manaus etc. as noted.
- Nova Petrópolis Boulevard Varig Vive 727 PP-VLD — on site since Dec 2021 but the complex is under construction and not open (varigvive.com.br lists the inauguration for 2035).
- Blumenau AMX (FAB 5521 per compilation) — privately owned by the aero-club president, being repainted for erection in front of the Quero-Quero airport (NSC Dec 2024). Not yet a display; re-check.
- Pomerode Aero Hotel Bonanza A36 — inside a hangar; no evidence of public display.
- Macapá "Parque Residência" Bandeirante PT-FDL — only a forum question (Aug 2026); unverified.
- Tabatinga AM DC-3 HC-ALD at the airport (cinema room, 2011) — not in the 2026 compilation; unverified.
- Olinda PE AESO campus DC-3 PT-BFU; Recife Espaço Ciência Xavante; Aquiraz CE Bell 47J PT-HAI; João Pessoa Aeroclube da Paraíba 2888; Tatuí Sítio do Carroção DC-3 PT-KYX; São Bernardo do Campo Cidade da Criança DC-3 PP-ANN; Campinas Parque Taquaral BT-15 PP-GRK; Mococa PP-VBN (airworthy, hangared) — all absent from the 2026 compilation and last reported 2016-19; **not recorded**, listed here for a follow-up sweep.
- São Luís motel Bandeirante — unidentified, motel.

## 5. Judgment calls

- **Derelicts recorded as sites**: Itacoatiara C-46 PP-NMH (stripped hulk but a documented attraction, g1 2025), Taguatinga 767 (fenced landmark, cleaned Sep 2025), Foz do Iguaçu VC-96 2115 ("Sucatinha", beside the park entrance). Descriptions say so.
- **Gramado "Jardim Secreto do Capitão"** (opened 2026, ~40 aircraft) is a ticketed theme park, not a museum by name; recorded here with the 10 airframes I could identify (2 Hercules with serials; others type-only, one placeholder AMX row although three are reported). Pass 1 should not duplicate it; a collection list from the park is the top serial gap.
- **Balneário Piçarras**: SH-3 N-3012 (in place since Aug 2024) and AF-1 N-1012 (assembled from 23 Apr 2026, completion expected ~Sep 2026) recorded on one site as on_display — the A-4 is physically on site; if it is still fenced off, flip to under_restoration.
- **Maringá Xavante 4472** recorded `under_restoration` (blown down 2026; restoration started 22 Aug 2026).
- **Composite/false-serial Xavantes**: tail left blank where the painted serial is known to be false (Vinhedo, Brasília club, Rio Grande).
- **Access**: `appointment` for members' clubs (Sport Recife, Clube de Aeronáutica, Clube SO/SGT, Guarapiranga), guest-only pousadas/resorts (Monte Verde, Campos do Jordão, Igaratá, Cantagalo, Divino de São Lourenço), the Cascavel private airport museum (booked visits), university hangar (UFSM), UNICEP and AGES campuses, and the Barreira do Inferno visitor centre. `public` for university open campuses (ULBRA, Tuiuti), factory gate guards viewable from the road (Embraer SJC and Botucatu).
- **Base-adjacent squares** recorded as public monuments because they stand outside the gate on public roads: Salvador Praça do Avião, Gama Praça do Avião (in front of III FAE HQ), Anápolis BR-414 Mirage 4915, Campo Grande Praça Chaves Filho T-6 1415, Santa Maria RSC-287 Xavante 4567, Canoas V COMAR roundabout 4510. If Pass 2 finds any of these inside the perimeter, delete here.
- Navy AF-1 recorded with model `AF-1` (Brazilian designation), aliases A-4/A-4KU. FAB local designations used throughout (F-8, F-103, AT-26, C-95, C-115, U-42, U-93/VU-93, C-97, VC-96, H-1H as `UH-1`+`H`).

## 6. Blank fields, deliberately

- Coordinates given only for Gama (Wanderlog) and Pirassununga T-27 (Monolito Nimbus, airframe position); all others blank — never guessed.
- `year_built` only for Canarana DC-3 (1944), Pirassununga T-27 1374 (first flight 1985), Santa Maria H-1H (1967).
- Tails blank on 20 rows: false/covered serials (Porto Nacional, Vinhedo, Brasília club Xavante, Rio Grande, Posto Marrone, Lagarto, Toledo, Chapada, Tefé), unread serials (Assis AT-33, São Carlos praça, Genesis Park 737, Gramado ×8).
- CEPs only where a source gave them (Gama, Guarulhos, Canoas).

## 7. Leads for other agents

**Pass 1 (civilian museums):** Museu EPCAR Guaramiranga/CE (A-1A 5524, AT-26 4570, H-1H 8684, T-25 1961; museuepcarguaramiranga.com.br); Museu Militar Brasileiro, Panambi/RS (A-1B 5656 wreck, AT-26 "4616"?, 727 PR-TTP arrived Sep 2025, 737s N393US & PP-SFJ, C-115 2368/2369, two C-95, H-1H 8654 + two more, PA-23 PT-ATW, P-95A 7052, R-35A 6002, T-25 1875/1926/1939); Museu Casa de Cabangu, Santos Dumont/MG (T-23 Uirapuru); Museu Catavento, São Paulo (DC-3 PT-KUB); Museu do Expedicionário, Curitiba (P-47D "A4", quoted 4171 by 2026 / 226756 by ABRAPAC); Museu Eduardo Matarazzo, Bebedouro (Meteors 4409/4442, T-6s incl. 1339 etc.); Museu TAM/Asas de um Sonho, São Carlos (status?); Memorial Aeroespacial Brasileiro, SJC; Museu da Aviação de Manaus (Meteor T.7 4308); Umirim municipal aviation museum (Nov 2021) next to the T-27; Museu Oceanográfico Univali (its indoor exhibits); Cascavel Aeroporto Executivo "museu" recorded here (single 737) — merge if Pass 1 has it.

**Pass 2 (military bases and institutions):** Fernando de Noronha DTCEA-FN AT-26 4488 (internal praça); Recife: COMAR II (AT-26 4466, AT-33 4322, VU-93 2118), Hospital da Aeronáutica AT-26 4548 (restored 2023), CINDACTA III (AT-26 4535 now at BARF gate, VU-93 2121), Colégio Militar do Recife AT-26 4456, BARF B-17 5402 gate, PARF; Natal BANT (AT-26 4487/4577/4584/4622, B-25J 5133, B-26B 5156, C-95 2191, H-50 8772, T-25 1960); Fortaleza BAFZ (C-95 2175, F-80 4225 gate) and "AT-26 4460 Fortaleza" (location unknown); Belém BABE (C-47 2032, CA-10 6552); Cachimbo AT-26A 4630; Manaus CINDACTA IV gate AT-26 4518, CMA C-115 2353; Boa Vista BABV A-29B 5525; Porto Velho BAPV AT-26 4578; Brasília: CENIPA (AT-26 4507, C-95 2190, SH-3B N-3017), COMDABRA Mirage 4916, BABR (Mirage 4922 "30 anos", VU-93 2127), ENAJUM/STM garage A-1A 5522; Anápolis BAAN (Mirage 4910 interior, 4901 Vila dos Sargentos, 4930 nose at GDA); Campo Grande BACG C-115 2370; Lagoa Santa PAMA-LS (T-6 1378, C-95, T-25); Barbacena EPCAR (T-23 0965, T-6 1223, AT-33 4342, AT-26 4611, H-1H 8695, Meteor 4406); Resende AMAN Meteor 4401 (off the approach road — check whether public); Rio: MUSAL is Pass 1; Galeão BAGL (C-91 2502 gate, KC-137 2404 fin), CAE Ilha do Governador F-5B 4802, 26º BIPqdt C-119 2304, Brigada Pára-quedista/Deodoro C-47 2017 (PP-AKA) & C-115 2362(?), DECEA Santos Dumont A-1A 5538 (praça in front of DECEA HQ, seen Nov 2024 — may be publicly visible), CFN command A-1A(?) "N-1016" (naval AF-1?), Santa Cruz BASC (A-1A 5514, AT-26 4458/4450, F-5B 4805, Meteor 4430/4441, P-16E 7032, P-47D 4107 "C5", TF-33 4348, A-1 monument Nov 2020); Canoas BACO (Meteor 4433/4448 gate, AT-33 4336, F-5E 4882, T-27 1345 Vila dos Sargentos, C-95 2307); Santa Maria BASM (A-1A 5542, AT-26 4519); Florianópolis BAFL UH-1H 8535/8697; Curitiba CINDACTA II (Meteor 4452, F-5E 4879), Colégio Militar de Curitiba A-1A 5528; Guaratinguetá EEAR (A-1B 5650 gate, AT-26 4462, C-95 2136, EU-93 2119, F-103D 4906, H-1H, H-13 8515, T-25 1846, C-47 2075); Pirassununga AFA (T-6, T-23 1737, T-25 1870/1967, T-27, Meteor 4413, AT-33 4328, Mirage 4925, F-5E 4883, A-1, C-115 2351, AT-26 4598, UH-1H 8702, T-24 Fouga monument 2021, TZ-13, Ipanema, T-21); Guarulhos BASP (T-6 1478 restored 2024, AT-26 4585/4575, Salão Histórico Dec 2024); São Paulo PAMA-SP (Mirage 4927, F-5B 4803 "Ayrton Senna", UP-16 7021, F-5E 4880), COMGAP A-1A 5515; SJC DCTA/CTA (T-27 1300, IC-95B 2328, AT-26 4478, IPEV Xavante 4467 monument Dec 2024, MAB collection); Gavião Peixoto Embraer (A-29 5700, PT-ZTF, PP-XOJ).

## 8. Needs a human on site (ranked)

1. Jardim Secreto do Capitão, Gramado — full inventory with serials (~40 airframes; only 2 serials known).
2. Camocim — is the Xavante 4587 still on Praça Pinto Martins or at the airport?
3. Sport Club do Recife — F-80C 4215 or AT-33A 4315?
4. Pirassununga T-25 1932 — which square? and Florânia 4469 condition.
5. Read serials: São Carlos praça Xavante, Assis AT-33, Toledo Regente, Porto Nacional Xavante, Lagarto HS-125, Tefé PA-28, Chapada Navion, Genesis Park 737/727 no.2, Balneário Piçarras A-4 completion.
6. Santa Maria H-1H 8701 — back on the roundabout after the 2023 repaint?
7. Praia do Avião ATR-42 PR-MPN near Manaus — where exactly, and is it visitable?
8. Ipiabas 727, Santo Antônio do Leverger 727, Carolina 727, Morretes A318 — are the venues open?

## 9. File / row-count table

| Region | Sites | Aircraft rows | Rows with tail |
|---|---|---|---|
| Norte (AM, PA, TO, RR) | 7 | 7 | 5 |
| Nordeste (AL, BA, CE, PE, RN, MA, SE) | 19 | 20 | 17 |
| Centro-Oeste (DF, GO, MS, MT) | 14 | 15 | 14 |
| Sudeste (MG, ES, RJ, SP) | 45 | 53 | 50 |
| Sul (PR, SC, RS) | 36 | 46 | 35 |
| **Total** | **121** | **141** | **121 (86%)** |

Figures computed from the written CSVs.
