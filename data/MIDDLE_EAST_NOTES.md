# Middle East — imported 10 September 2026

**305 new sites · 824 airframes · 12 countries.** With the Gulf states and Egypt
already in, the region now stands at **340 sites**. Turkey, Israel, Iran, Jordan,
Cyprus, Syria, Iraq, Lebanon, Qatar, Bahrain and Yemen were all greenfield; the
UAE was a top-up against three existing records.

| Country | Sites | Airframes | Directory |
|---|---|---|---|
| Turkey | 166 | 430 | `data/turkey/` |
| Israel | 42 | 209 | `data/israel/` |
| Iran | 40 | 93 | `data/iran/` |
| Jordan | 24 | 27 | `data/jordan/` |
| Cyprus | 9 | 12 | `data/cyprus/` |
| UAE (top-up) | 8 new + 2 rows onto an existing site | 15 | `data/uae/` |
| Syria | 6 | 17 | `data/syria/` |
| Iraq | 3 | 4 | `data/iraq/` |
| Qatar | 3 | 5 | `data/qatar/` |
| Yemen | 2 | 2 | `data/yemen/` |
| Lebanon | 1 | 9 | `data/lebanon/` |
| Bahrain | 1 | 1 | `data/bahrain/` |

Each country directory holds `<cc>_museums.csv`, one `*_aircraft.csv` per site,
and the raw research output kept for audit. **Turkey and Israel between them are
two-thirds of the region.**

---

## The import had to work around the rate limit

`bulk_import` is capped at 200 calls/hour and this package is 306 aircraft files.
Repo files are still **one per museum**, as the methodology and
`tests/test_flagship_topup_files.py` require — but the import ran from **twelve
concatenated per-country batches**, 24 calls in total. Every batch was dry-run
clean before any was applied, which is what makes the reduced atomicity
acceptable: the risk of a per-country batch is that one bad row rejects a whole
country, and a clean dry run removes it. Anyone re-importing should do the same
rather than firing 306 calls at a 200/hour ceiling.

---

## Sources: what actually worked

**`spottingmode.com/wro` carried this region**, as it has carried Africa and
Asia. Its value is the status vocabulary — `pre` (preserved) against `std`,
`dum`, `dlt` and `i/a` — plus per-location coordinates, construction numbers and
dated "last noted" fields. **Every coordinate in the Turkish monument package is
a spottingmode per-location fix copied unchanged to six decimal places**, made on
satellite imagery against the airframe itself. Not one is a geocoded address and
not one was generated. It is also live: contributors were editing it on
8 September 2026, the day before this work, and a contributor walked Cyprus on
3 October 2025. **Reach it with `curl --ciphers "DEFAULT:@SECLEVEL=0"`** — its
TLS handshake fails modern OpenSSL. It still is not in `METHODOLOGY.md`.

**Esri World Imagery's `identify` endpoint** returns per-tile acquisition dates,
which turns "is it still there?" into a dated answer instead of a shrug. It is
what confirmed the Al Ain and Al Minhad Hawks (Sep–Oct 2025), the Al Dhafra
Mirage 2000 (Mar 2025), the Doha Whirlwind and Hunter (May 2025), and a good part
of the Turkish monument population.

**`aviationmuseum.eu` is worse than a lead list here.** Its Cyprus page states
flatly "We haven't found any aviation museum, or museum with aircraft in Cyprus"
— against which this package returns **nine Cypriot sites**. Its UAE page lists
one entry and **places Sharjah in Bahrain**. It contributed nothing to any of the
six passes.

**Turkish-language search is the biggest untapped lever in the region.** Every
`anıt uçak` / `teşhir uçağı` query run from this environment returned US-weighted
noise, yet the two Turkish news pages that were reachable each resolved something
material. The Niğde Phantom — added on a local newspaper reference alone in
October 2025 — is the shape of what a Turkish-locale pass would add.

---

## Two claims that did not survive, and one that did

**Israel's IAF Museum at Hatzerim is real and is as big as advertised** — it is
the anchor of the Israeli package and the reason Israel returns 209 airframes
from 42 sites.

**There is no aviation museum at Al Udeid, Qatar.** Despite the type of base it
is, no preserved airframe could be evidenced there at all.

**The UAE's three existing records were not thin by accident, but they were
under-described.** The top-up found eight further sites and fifteen airframes —
the biggest single miss being **Higher Colleges of Technology Dubai Men's
College** with five airframes, a larger group than the Abu Dhabi campus already
recorded. See the UAE conflict note below, which is the most important data-quality
finding in this package.

---

## The Al Mahatta identity conflict — unresolved, deliberately

`Al Mahatta Museum` already held seven airframes from an earlier session. The
research pass returned the same seven, **with different identities on five of
them**, on the grounds that the museum displays aircraft in other aircraft's
markings:

| Already in the database | This pass claims |
|---|---|
| C-47A `42-92452` | `N688EA`, painted G-AMZZ |
| Anson C.19 `TX183` | `G-BSMF`, painted G-AKVW |
| DH.114 `XR443` | `VH-NJP`, painted G-ANFE |
| DH.106 `XK655` | Comet 2 `G-AMXA` |
| DH.104 `G-ARDE` | same |
| Auster J/1 `G-AJRE` | same |
| VC10 K.3 `ZA149` | same |

**No row was imported for Al Mahatta.** Importing would have created seven
duplicate airframes, and overwriting would have replaced one session's sourcing
with another's on a single source's say-so. The disagreement is recorded here
instead and needs one adjudication pass. The same applies to the Emirates
National Auto Museum TriStar `TT-DWE`, already present and not re-imported. Only
**CERT Complex, HCT Abu Dhabi** took genuine top-up rows — an AB 206B3 and a
PA-28, both new airframes alongside the MB-326KD already recorded.

---

## Collisions resolved

**Three Turkish sites were recorded twice**, once by the museums pass and once by
the monuments pass, under different names but **identical coordinates**. The
institution name was kept in each case and the monument-style name dropped:
Gökmen Uzay ve Havacılık Eğitim Merkezi (not "Bursa Altınova Phantom Monument"),
Kayseri Bilim Merkezi (not "…Phantom Display"), and UçakPark Havacılık Bilim
Merkezi (not "Çayırova A340 Display") — the last inherited its coordinate from
the dropped record, which had one where the keeper did not.

**One serial-namespace collision.** The MiG-15 at Aden Airport, Yemen, wears
`03`; Monino's MiG-15UTI is also `03`, and `UNIQUE (model, tail_number)` cannot
tell them apart. The Yemeni airframe was imported with a **blank tail_number**,
the number preserved in its aliases and the reason written into its description.
This is the same failure that forced a blank on SAAF Mirage F1CZ 207 against a
French Mirage F1C-200 207, and it will keep recurring — Israeli, Iranian and
Turkish serials are all short and drawn from independent national sequences.
**The fix is a key with something national in it, not blanking real serials one
at a time.**

---

## Judgment calls worth knowing about

**The Nicosia Trident is excluded.** Cyprus Airways Trident 2E `5B-DAB` is still
physically on the apron and was seen there on 3 October 2025 — but it is coded
derelict, described as "slowly disintegrating on the apron" with no maintenance,
and sits inside the UN buffer zone enterable only by special permission. It fails
both halves of *deliberate retention plus public presentation*. **Live
complication:** on 19 February 2026 a bicommunal project to turn the airport into
a museum was reported. If that is built and the Trident stabilised, this row
should be created — a plan is not a display.

**The Umm Al Quwain Il-76 is excluded because it no longer exists.** It was
dismantled and scrapped from May 2022 to clear the Siniyah Island bridge
approach. No "Dream Park" airframe could be evidenced at Umm Al Quwain either;
the emirate has nothing as of 2026.

**Dive Bahrain's 747 is excluded.** Deliberately sunk in 2019 as a ticketed
underwater park — about as deliberate and public as retention gets — but by
November 2020 Bahraini MPs found "parts of the jumbo airplane scattered across
the seabed". A broken-up airframe dispersed across a seabed is a reef, not a
preserved aircraft. One correction regardless: the press called it a 747-400. It
is a **747-236B**, c/n 22442, ex-British Airways.

**Turkey's base air parks are one site each, not one site per airframe.**
Splitting Etimesgut, Akıncı, Çiğli or Gaziemir into eight or ten sites apiece
would have produced a site list that stops reading as a museum database. Each
aircraft's own coordinate is in its description where it differs from the site
fix. Airframes plainly outside the wire as separate public monuments *were* split
out — İncirlik's road F-104, Batman's boulevard T-33, Çorlu's Önerler F-104,
Konya's two NF-5s and A300, Merzifon's Sofular F-5, Akhisar's second F-104,
Dalaman's town T-33.

**Northern Cyprus sites are filed `country = Cyprus`** with the de facto
administration stated in each description — a database-consistency choice, not a
political one. The two Sovereign Base Area sites raise the mirror-image question
and were filed the same way, with `state_province = Akrotiri Sovereign Base
Area`.

---

## Deliberate blanks

**`year_built` is blank on all 824 rows.** Not one build, rollout, first-flight
or delivery date was sourced anywhere in the region. This matters more here than
usual because so many of these serials *look* like years: Turkish Air Force
serials carry US fiscal-year prefixes (63-12718, 67-0395, 74-6862) and
Lockheed/Canadair construction-derived numbers (7164, 8321, 9145); Iranian
serials are 3-DDDD. **None is a year and none was treated as one.** One row
arrived with the serial written into the `year_built` column — Hava Lojistik
Komutanlığı CF-104 62-810 — and was corrected before import.

**Roughly 30 Turkish rows carry a deliberately blank `tail_number`**, in three
kinds, each stated in its own description: no contributor has ever linked an
identity; the airframe wears a serial demonstrably not its own (Bandırma 6-186,
Of 78-135, Hendek 4-733, Kütahya's second Bellanca); or a single specialist
source proposes an identity no second channel confirms (Çardak, Arslanbey, Muş,
Akıncı's fourth F-104). In every case of the third kind the candidate serial is
named in the description and carried in aliases, so it is recoverable the moment
a second source appears.

**Postal codes are blank across nearly the whole region.** Nominatim returned one
for only a handful of Turkish points and none was guessed.

---

## Ranked open items

1. **Adjudicate Al Mahatta.** Seven airframes, five contested identities, two
   sessions disagreeing. Until it is settled the museum's records are wrong in
   one direction or the other.
2. **A Turkish-locale search pass.** The single biggest coverage lever left in
   the region — municipal installations from 2020–26 that no English-language
   channel has caught up with.
3. **Ten F-104 sites the International F-104 Society names that spottingmode does
   not carry, with no coordinates**: 62-12239 Eskişehir; 6653 Balıkesir 191 Filo;
   8128 Diyarbakır; 8116 Çardak; 8168 Arslanbey; **104751 in Trabzon city centre
   since 10 March 2018**; **104756 at Çayağzı west of Riva since mid-2011**;
   104796 Muş; 104891 Diyarbakır gate; 9175 Eskişehir. Each needs one coordinate
   to become a row; the Trabzon and Riva pair are the most likely genuinely
   separate monuments missed.
4. **What is "Ankara – Museum" (spottingmode 7615)?** Nine airframes, categorised
   as an aviation museum, at 39.90156 32.77208 in Üniversiteler, Çankaya, updated
   March 2025 with photographs. It is not the Etimesgut museum, not the THK
   museum and not the Air Force Museum. Six OSM `historic=aircraft` nodes sit
   within 50 m.
5. **The Syrian Air Force Museum at Aleppo (Nayrab).** Its post-war state is the
   single least certain thing in this package — see `data/syria/`.
6. **Kütahya Aircraft Park access type.** Eight airframes in a landscaped park;
   marked `restricted` on the assumption it sits inside the Hava Er Eğitim Tugayı
   compound. That assumption is unverified and is the access call most worth
   checking.
7. **The Kayseri site groupings.** Twelve locations collapsed into three sites
   named geographically because the institutions could not be confirmed. If the
   Erenköy compound is the 2nci Hava İkmal Bakım Merkezi and the Köşk group is
   Erciyes Üniversitesi, both names should be corrected.
8. **Aliağa F-4E 67-0395** — imagery at the recorded point shows groundworks and
   no aircraft. Either the coordinate is off by 100 m or it moved during a
   seafront redevelopment.
9. **The Bahrain Bo 105 at Sakhir** is the weakest row in the region: one
   contributor report of 15 October 2025, an approximate coordinate the source
   itself flags, and nothing at the point on February 2025 imagery.
10. **Turkish vocational high schools.** Only four campus sites made it in, and
    the Meslek Lisesi pattern — a school with a real airframe in the yard — is
    certainly more common than that.
