# South America — build-out overview (September 2026)

First South American data in the database. Eleven packages, one directory
per country (`data/brazil` … `data/bolivia`, with Guyana/Suriname/French
Guiana together in `data/guianas`). Each directory has its own
`<COUNTRY>_NOTES.md` with a coordinator summary on top of the raw research
notes; read those before touching a country.

| Country | Sites | Airframes | Tailed | Notes |
|---|---|---|---|---|
| Brazil | 173 | 450 | 82% | three passes; MUSAL 119 rows; Museu TAM closed, MAPA (Campo de Marte) opens 2027 |
| Argentina | 149 | 387 | 91% | two passes; MNA Morón 63, MUAN Bahía Blanca 31; ~80 plaza monuments |
| Chile | 32 | 184 | 79% | MNAE 123 rows from its own PDFs; regional monument sweep incomplete |
| Colombia | 24 | 102 | 69% | Tocancipá move audited (T-33 2033 stayed at CATAM); city sweep incomplete |
| Peru | 22 | 67 | 81% | collection is inside Las Palmas (restricted); Parque del Aire is the public part |
| Venezuela | 12 | 68 | 74% | Maracay 45 rows; pre-2019 evidence flagged row by row |
| Ecuador | 20 | 66 | 94% | FAE Quito 23 rows; ~15 more T-33 monuments unlocated |
| Uruguay | 8 | 60 | 90% | Meregalli museum is at Base Aérea I, Ruta 101 (moved 2013-15) |
| Bolivia | 13 | 36 | 92% | El Alto museum serials rest on a 2016 list |
| Paraguay | 4 | 9 | 44% | thin — interior never swept |
| Guianas | 1 | 1 | — | Ariane 5 mock-up at Kourou; Guyana and Suriname searched empty |
| **Total** | **458** | **1,430** | **84%** | |

## Things every later pass should know

- **Serial systems collide across countries.** The `(model, tail_number)`
  unique key treats FAB 4201, FACh 750, FAU 256 and FAP 256 as the same
  namespace. Two genuine Chilean Bo 105 "C-19"s could not both be imported
  with a tail; the older one carries the number in aliases only. Expect more
  of this as Europe and Asia fill in — it is a schema limitation, not a data
  error, and blanking the tail is the agreed workaround for now.
- **The bulk-import endpoint is limited to 200 calls per hour per source
  IP.** A 458-file import needed a resumable runner that records each file as
  it lands. Never re-run a file that already imported: rows without a tail
  duplicate silently.
- **Coordinates are mostly town centroids.** 280 of 458 sites were geocoded
  by Nominatim from city + province; the per-country `*_geocode_log.csv`
  says which. Pinning the airframe positions from satellite imagery is the
  single most valuable follow-up for the map.
- **Research ran without web search for the second half of every agent.**
  The big museum collections were built from the museums' own pages, PDFs
  and REST feeds and are solid; the small-town monument sweeps are only as
  complete as the national compilations (ABRAPAC 2019 + AeroEntusiasta 2026
  for Brazil; Gaceta Aeronáutica censuses + the Roll Out / Aeronaves
  Preservadas blogs for Argentina; tallyho.cl for Chile; FAC/FAE press for
  Colombia/Ecuador). Each country's notes rank what a browser-enabled rerun
  should look at first.
