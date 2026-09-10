# France — coordinator summary

Imported live 10 September 2026. Four research passes: the major museums (plus
a diff of Le Bourget); Armée de l'Air / Aéronavale / ALAT base displays; the
northern and western régions; the southern and eastern régions. The per-pass
research notes follow this summary unchanged; where they disagree with this
section, this section is what was imported.

France already held `Musee de l'Air et de l'Espace` with **170 aircraft** — the
one big European collection that was already thorough — and the single C-47 at
`Musee de la Batterie de Merville`. Neither was re-created; Le Bourget got a
**20-row top-up** covering airframes the live list was missing, including six
Dugny reserve and restoration aircraft the museum acknowledges in its 2024
Rapport d'activités.

**Files:** `fr_museums.csv` (113 new sites) and 114 `*_aircraft.csv` files, one per
site. `musee_de_lair_aircraft.csv` is the pre-existing Le Bourget file and was
left untouched.

**Rows:** 1139 aircraft · 731 with tail numbers (64%) ·
1080 on_display / 15 in_storage / 44 under_restoration.

**Sites by région:** Provence-Alpes-Côte d'Azur 15, Occitanie 14, Nouvelle-Aquitaine 14, Île-de-France 11, Bretagne 10, Grand Est 10, Auvergne-Rhône-Alpes 9, Normandie 9, Hauts-de-France 7, Pays de la Loire 5, Centre-Val de Loire 5, Bourgogne-Franche-Comté 4.
**Access:** 57 public · 19 appointment · 37 restricted.

**Largest collections:** Espace Air Passion 164, Ailes Anciennes Toulouse 71, Musée de l'Épopée de l'Industrie et de l'Aéronautique 65, Musée européen de l'Aviation de Chasse 65, Conservatoire d'Aéronefs CANOPEE, Châteaudun 49, Musée du Château de Savigny-lès-Beaune 46, Musée de l'Aviation Clément Ader 46, Musée de l'Aéronautique Navale 43, Conservatoire CANOPEE Châteaudun 38, Aeroscopia 36.

**Coordinates:** every site has one. 12 were fixed by the researchers; the
rest were geocoded by the coordinator, level recorded per site in
`fr_geocode_log.csv` — 33 from the street address, 66 from the code
postal, 2 city-level.

## The finding that matters most: aerosteles.net is not a preserved-aircraft source

Both monument agents were pointed at `aerosteles.net` as their spine. Between
them they pulled the complete national index, cut it to their départements —
**2,489 entries in the north and west, 1,472 in the south and east** — and read
every entry that named an aircraft type. It produced **one** site record, and
that one only because it mentioned a municipal museum's inauguration.

aerosteles.net is a database of *memorials*: crash stelae, plaques, propellers
on pillars, names carved in stone. It is excellent at that and almost useless
for "where can I go and see an aircraft". **Do not spend another pass on it.**
The sources that actually produced French airframes were:

- **ARDHAN's `Aéronefs préservés de l'Aéronautique navale, par lieux`**
  (Claude Morin, February and August 2025 editions) — the naval heritage
  association's own by-location census, dated, with serials and condition. It
  carried the entire Aéronavale half of the work plus all ten lycées that hold
  real airframes.
- **`foxalphazoulou.overblog.com`**, current to September 2026 — the only
  genuinely current source for Armée de l'Air base displays.
- **`kosmonavtika.com`'s "Où sont-ils ?" registers** — per-site pages carrying
  a last-updated date, several reading 2026.
- **Nicolas Pillet's survivor registers**, a per-airframe Mirage IV disposal
  list on the Delta Reflex forum, and first-party feeds at Ailes Anciennes
  Toulouse (91 per-aircraft pages), Montélimar (59 datasheets), CAEA (a live
  WordPress REST feed), Lyon-Corbas and CANOPEE Châteaudun.

Two source failures shaped the result and should be fixed on any re-run:
**airhistory.net returned 403 through this environment's proxy on every
request**, so the "[Off-Airport] France" listing — the one taxonomy that maps
exactly onto roadside airframes — went unused; and `pyperpote.tonsite.biz/pfa/`,
a dedicated French gate-guard database, is down with a fatal error while
web.archive.org is blocked here. **The roadside plinth population is therefore
the thinnest part of this package**, and French Wikipedia, unlike English,
carries no per-type survivor lists to fall back on.

## Cross-pass adjudications (one airframe, one place)

Twelve sites came back recorded twice under different names, and the duplicates
were merged rather than imported: CANOPEE Châteaudun, Melun-Villaroche, the
Conservatoire Historique de l'Aéronautique Navale at Nîmes-Garons, and six
lycées were each held by two agents. `_fix_adjudications.py` reproduces every
decision. The substantive ones:

- **Étendard IV M 29** — ARDHAN still lists it on the Saint-Raphaël seafront;
  it moved to the SDIS fire station at Fréjus in June 2022 and stands there
  beside a Flamant. Recorded at Fréjus.
- **Alizé 8** came back as both a gendarmerie gate guard and a roundabout
  monument at Rochefort. It is one aircraft on one plinth on the rond-point
  Albert-Bignon; recorded once, as public.
- **Super Étendard 12** was placed at both the Lycée Flora Tristan
  (Camblanes-et-Meynac) and Aérocampus Aquitaine (Latresne) — adjacent communes
  sharing postcode 33360. Kept at Aérocampus, the aeronautical campus, with the
  richer record.
- **Crusader 29** is listed by ARDHAN at both Landivisiau and Lann-Bihoué. Kept
  at Landivisiau, the Crusader base; the conflict is unresolved and needs a
  person on either base.
- **Mirage IIIB 233** is owned by the Montélimar museum but was craned onto the
  Villeperdrix roundabout. Recorded at the monument, where a visitor sees it.
- **Étendard IV M 06** and the **Leduc RL-21 F-WJDT** were each claimed twice;
  kept at Ailes Anciennes Toulouse and Espace Air Passion respectively, on the
  strength of full provenance chains against bare inventory lines.

## Short French serials and the (model, tail) key

French military serials are often one to three digits, so they collide readily.
Five rows were imported with a **blank tail and the number kept as an alias**
because the number was already taken: Mirage IIIR **02** (shared with the
Mirage IIIA 02 at ISAE-SUPAERO), Mirage IIIE **001** (shared with the museum's
own Mirage IIIB 001), Mirage F1CT **235** (shared with a South African F1AZ),
MiG-21R **45** (a Soviet bort number), and H-21C **FR41** at CELAG Grenoble,
where the same serial is recorded on the H-21 at The Helicopter Museum from
that museum's own fleet list — those two attributions need reconciling on the
ground.

## Live-database correction made during this pass

The database carried a Mirage III with tail **10** in the Bundeswehr
procurement office's study collection at Langemarck-Kaserne. Its own
description reads "coded 10-RD" — a squadron code, not a serial. The tail was
blanked live and the reasoning written into the record; 10 belongs to the
Mirage IIIA pre-production airframe on the ISAE-SUPAERO campus.

## Coordinator corrections applied before import

- 125 dashless designation aliases added.
- `Unknown` manufacturer placeholders replaced with `Unidentified`.
- F-105G role corrected to `electronic_warfare` (the Wild Weasel convention the
  test suite enforces).
- The alias `Lynx HAS.2` moved into the variant field — the alias prose filter
  reads `HAS` as a verb, so any British HAS./HAR. mark fails as an alias.

**Validation:** every row passed `_validate_aircraft_row` and the alias suite;
zero museum-name collisions against the 2,234 museums then live; a combined dry
run of all 1139 rows returned `created: 1139, linked: 1139, errors: []`; after
import all 114 per-site live counts equal the file counts, and all 115 French
sites carry coordinates.

## A process note for the next country

The consolidation script that merges the per-agent packages into `data/<country>/`
rebuilds the directory from the raw agent output. Twice it wiped work done
downstream of it — the geocoded coordinates, and (the first time) the
pre-existing `musee_de_lair_aircraft.csv`, which had to be restored from git.
The second wipe happened *after* the museums were live, so 101 sites were
imported with blank coordinates and had to be PATCHed afterwards. The script
now preserves named files and carries existing coordinates forward. **Geocode
after the last consolidation run, not before.**

## What is still open

- **The roadside plinth sweep needs redoing with airhistory.net reachable.**
  This is the single biggest gap and it is a tooling problem, not a research one.
- **Corsica returned nothing** — 27 aerosteles entries, all crash memorials, and
  no survivor register lists a Corsican location. Needs someone on the island.
- **Mas Palégry (Perpignan)** dispersed nine aircraft at an Osenat auction on
  1 June 2019 and is still on Wikipedia; **Vraux** closed on 29 September 2024
  including a Short Stirling fuselage. Neither destination is known.
- **BA 116 Luxeuil and BA 701 Salon-de-Provence** produced no site at all —
  implausible for a fighter base and the home of the Patrouille de France.
- **ALAT produced nothing** (Phalsbourg, Étain, Pau, Le Luc, Montauban). The
  Malcros *Aéronefs de l'ALAT* PDF series at museehelico-alat.com is the obvious
  next source.
- **Savigny-lès-Beaune's ~80 outdoor aircraft have 7 known serials**, and ARDHAN
  flags doubt over the collection's future.

---

# Research pass: the major museums and the Le Bourget diff

# France — major aviation museums, plus a Le Bourget diff

Output directory: `/home/claude/fr/museums/`
Assignment: France's major aviation museums, plus a diff of the Musée de l'Air
et de l'Espace at Le Bourget. Monuments, plinth aircraft and base gate guards
are **not** in this pass — leads found along the way are listed at the end.

---

## 1. Le Bourget diff

`lebourget_topup_aircraft.csv`, museum_name `Musee de l'Air et de l'Espace`
(the DB spelling), **20 rows**, 7 with a serial. The diff yielded results, so
the file was written.

The 169 lines in `/home/claude/fr/lebourget_live.txt` were subtracted from the
current collection reconstructed from:

| Source | Weight | What it gave |
|---|---|---|
| Museum's own **2024 Rapport d'activités** (PDF on museeairespace.fr) | Highest — official and dated | The Réserve Grands Formats contents at Dugny: A-26 Invader, Potez 25, Farman 190, Lockheed Constellation; Caravelle F-RAFG under restoration |
| **AAMA Le Bourget** (the museum's own volunteer association) | High | Vautour IIB 634 and B-26B 44-34773 "à l'abri dans les réserves du Musée de l'Air à Dugny" |
| French Wikipedia `Musée de l'Air et de l'Espace` | Lead only | Massia-Biot glider, La France and Santos-Dumont gondolas, Pou-du-ciel, MS.317, Diamant A, F-104, F-105 |
| English Wikipedia `Musée de l'air et de l'espace` | Lead only | Balzac V, DC-3 cockpit, Caravelle forward fuselage, Zeppelin LZ 113 gondola, Voisin 10 CA2 |
| `master194.com` walkaround (March 2026) and `bdd.deltareflex.com` (dated photo) | Currency evidence | Confirmed F-104G **22+40** and F-105G **63-8300** are physically at Le Bourget |

### Deliberate exclusions from the diff
- **Eurocopter X3** — English Wikipedia still lists it; French Wikipedia records
  that it left in early 2017 for the Musée de l'Aviation at Saint-Victoret.
  Not recorded at Le Bourget. Lead for whoever takes Saint-Victoret.
- **Lockheed P-38 Lightning** — only wreck fragments of Saint-Exupéry's aircraft,
  recovered near the île de Riou. Fragments, not an airframe or a section.
- **L'Oiseau Blanc main landing gear** — a component, not an airframe.
- **V-2 rocket engine** — an engine.
- Scale satellite models (Spoutnik 1, Vostok 1, Lunokhod 1, SPOT-1, Arabsat,
  Molnyia 1A), the 1/6 Montgolfier model and the Solar Impulse model.
- **Second S3 missile** — Wikipedia says the museum holds two; the live list has
  one. I could not tell which of the two the existing row is, so no second row.
- **Morane-Saulnier Type H** and **Sud-Est SE.3110** — mentioned by French
  Wikipedia but too close to the already-recorded Type G and SE.3101 to add
  without risking a duplicate.
- **Boeing 707 "Château de Maintenon"** — the 2024 report names a 707 under
  restoration; the live list already carries a 707 (F-BHSL) and the museum owns
  only one, so no row.
- **Mirage F1 reassembled after transfer from Rochefort** (2024 report) — the
  live list has two Mirage F1 (207 and a CR). Cannot tell if this is a third.
- 2007 European Heritage Days reports of the Dugny reserves (Caudron C.366,
  CR.714R, B-17, Lysander, Fouga CM.175 Zéphyr, DC-7C F-ZBCA, Sopwith 1½
  Strutter, Avro Lancaster, SNCASE Baroudeur, DFS 230) — **nineteen years stale**
  and not corroborated by any 2024-26 source. Left out entirely rather than
  guessed at. This is the biggest known gap in the diff.

### Judgment calls in the diff
- **Jaguar A04** added: the museum and avionslegendaires state four Jaguars are
  held (A1, A04, A91, E3); only three are in the live list. The existing
  untailed `Jaguar A` row could be A1 or A04 — the description says so.
- **Douglas DC-3 cockpit** and **Caravelle forward fuselage** recorded as
  section-only rows, distinguishable from the complete C-47A and the complete
  Caravelle 12 F-GCVL already recorded.
- **Lockheed Constellation** recorded with a blank tail: the museum's 2024 report
  names the type but not the sub-type or registration.
- The **Émouchet SA-104** and the **EA-41 rocket** are both in the museum per
  French Wikipedia but I could not establish a manufacturer I could stand behind
  (SA-104 is variously credited, EA-41 to Barré/DEFA/LRBA), so both were dropped
  rather than invented. Two known misses.

---

## 2. New museum sites

`fr_museums.csv` — **19 sites**, one row each, all `country=France`,
`region=Europe`, `state_province` = région. Postal codes filled everywhere.
Coordinates only where a source gave them (7 of 19); the rest are blank rather
than guessed, as instructed.

Le Bourget and Merville are **not** in the museums file.

| File | Site | Rows | With serial |
|---|---|---:|---:|
| `espace_air_passion_aircraft.csv` | Espace Air Passion, Angers-Marcé | 164 | 107 |
| `ailes_anciennes_toulouse_aircraft.csv` | Ailes Anciennes Toulouse, Blagnac | 71 | 29 |
| `montelimar_meac_aircraft.csv` | Musée européen de l'Aviation de Chasse | 66 | 50 |
| `chateau_savigny_aircraft.csv` | Château de Savigny-lès-Beaune | 46 | 7 |
| `lyon_corbas_clement_ader_aircraft.csv` | Musée de l'Aviation Clément Ader | 46 | 31 |
| `anaman_rochefort_aircraft.csv` | Musée de l'Aéronautique Navale | 43 | 42 |
| `canopee_chateaudun_aircraft.csv` | Conservatoire CANOPEE Châteaudun | 38 | 0 |
| `aeroscopia_aircraft.csv` | Aeroscopia, Blagnac | 36 | 23 |
| `caea_bordeaux_merignac_aircraft.csv` | Conservatoire de l'Air et de l'Espace d'Aquitaine | 29 | 19 |
| `salis_la_ferte_alais_aircraft.csv` | Musée Volant Jean-Baptiste Salis | 28 | 1 |
| `melun_villaroche_aircraft.csv` | Musée de l'Aviation de Melun-Villaroche | 24 | 16 |
| `dax_alat_aircraft.csv` | Musée de l'ALAT et de l'Hélicoptère, Dax | 23 | 5 |
| `mapica_la_baule_aircraft.csv` | Musée Aéronautique Presqu'île Côte d'Amour | 15 | 0 |
| `morbihan_aero_musee_aircraft.csv` | Morbihan Aéro Musée, Monterblanc | 13 | 2 |
| `cite_de_lespace_aircraft.csv` | Cité de l'espace, Toulouse | 8 | 0 |
| `biscarrosse_hydraviation_aircraft.csv` | Musée de l'Hydraviation | 5 | 0 |
| `musee_safran_reau_aircraft.csv` | Musée Aéronautique et Spatial Safran | 4 | 0 |
| `hangar_y_aircraft.csv` | Hangar Y, Meudon | 1 | 0 |
| `normandie_niemen_les_andelys_aircraft.csv` | Mémorial Normandie-Niémen | 1 | 0 |
| `lebourget_topup_aircraft.csv` | (top-up, existing DB site) | 20 | 7 |
| **Total** | | **681** | **339 (50%)** |

---

## 3. Sources and how much each proved worth

**Structured feed found (gold standard).** Two sites publish machine-readable
per-airframe pages:
- `aatlse.org/appareils-sitemap.xml` → 91 French-language per-aircraft pages for
  Ailes Anciennes Toulouse, each with a "Notre appareil" paragraph giving
  provenance and usually a serial. This is what makes the AAT and Aeroscopia
  files trustworthy.
- `meacmtl.com/fiches-avions/` → 59 datasheets for Montélimar with a
  "Provenance de l'appareil exposé" section carrying the serial, unit codes and
  arrival date for nearly every airframe. Hence 50 of 66 Montélimar rows carry a
  serial. (Their WordPress REST API exposes no aircraft post type, so the pages
  were scraped; about a third of them rate-limited on the first pass and had to
  be re-fetched.)
- `caea.fr/wp-json/wp/v2/avions` **is** a working REST feed (100 items on page 1),
  each aircraft split into "L'appareil du CAEA" / historique / gallery posts.
  Very rich provenance prose, serials for nine airframes.
- `museeaviationlyon.fr/le-musee/` publishes a plain "NOS APPAREILS ACTUELS"
  list of 46 aircraft **with serials**, explicitly flagged "liste non exhaustive".

**The single most valuable source in this pass** was
`aeronavale.org` (ARDHAN), *"I – Aéronefs de l'Aéronautique Navale préservés,
par lieux"*, **dated February 2025** — a PDF listing every preserved French naval
airframe by location with serial numbers and condition notes. It supplied the
whole Rochefort inventory (42 of 43 rows carry a serial), and corrected or
completed Savigny, Dax, Vannes, Melun-Villaroche, Aeroscopia, AAT, Montélimar,
Lyon-Corbas and CAEA. Its condition notes ("épave", "en stockage", "en instance
de cession") were used to set `display_status` honestly.

**Sites that proved stale or unusable:**
- `anaman.fr` — Cloudflare error 523, origin down, no Wayback snapshot of the
  aircraft page. The entire Rochefort file therefore rests on ARDHAN + French
  Wikipedia rather than on the museum's own pages.
- `musee-aviation-angers.fr` — a Wix site: the collection pages render client-side
  and contain no aircraft text in the HTML. Espace Air Passion, the second largest
  collection in France, has **no scrapeable first-party inventory**.
- `chateau-savigny.com` — publishes only "près de 100 avions de chasse … dont 4
  avions de la Patrouille de France, 11 MIG et 17 Dassault". No list, no serials.
- French Wikipedia's museum articles are type lists without serials almost
  everywhere; used as leads only.
- The 2013 avionslegendaires reportage on Savigny is thirteen years old and is
  the only per-type inventory that exists for that site.

---

## 4. Corrections made, with evidence

- **Aeroscopia vs. Ailes Anciennes Toulouse are two separate sites.** They share
  an address block on rue Roger Béteille at Blagnac and AAT owns roughly 27 of
  the aircraft displayed *inside* Aeroscopia. Following "record where an aircraft
  is, not who owns it", AAT-owned aircraft that the association's own pages say
  are "exposé dans Aeroscopia" are in the Aeroscopia file; the rest are in the
  AAT file. Each row says who owns it.
- **Aeroscopia Crusader = n°19, Alouette II Marine = n°05** (ARDHAN Feb 2025).
  My first pass had both untailed.
- **AAT H-21 = FR 106**, and the **Alizé n°5 is under full restoration**, not on
  display (ARDHAN Feb 2025).
- **Montélimar Ouragan is 214, not 251.** Separately, the **AAT Ouragan wears
  "251" and Patrouille de France colours but is really n°215** — the association
  says so explicitly. Both recorded with the true serial and the false marking
  noted in `description`, per the aliases rule.
- **Montélimar Mirage IIIEX** is a rebuild of Mirage IIIE **n°467**, not a new
  airframe; the museum says so. Recorded as one aircraft, variant EX.
- **Montélimar "Fiat G.91 T1" is really a Dornier-built G.91 T3** repainted in
  Italian T1 colours in 2007 — the museum says so on its own datasheet.
- **Montélimar F-84F wears the false code "BA-02"** from its 1972 conversion into
  a ground decoy representing a Mirage V; real serial 52-7175.
- **Montélimar has a second Crusader**: the forward fuselage of F8-A BuAer
  **149210** presented as a diorama (ARDHAN). Added.
- **Lyon-Corbas Nord 1101**: museum says n°123, ARDHAN says n°125. Museum wins for
  "what is here now"; the conflict is recorded in the row's description.
- **Lyon-Corbas holds a Nord 2200 fin only** (n°01) — added as a section row.
- **MAPICA is at La Baule-Escoublac, not Saint-Nazaire.** The brief called it the
  "Musée Aéronautique Presqu'île Côte d'Amour, Saint-Nazaire"; the association's
  own address and the tourist office both place it on the La Baule-Escoublac
  aerodrome (44500). Recorded there.
- **"Espace Aéro Lyon" and the "Musée de l'Aviation Clément Ader" are the same
  site.** EALC = Espaces Aéro Lyon-Corbas, the association that runs the Clément
  Ader museum on Corbas aerodrome. One site record, not two.
- **"Aérocentre / Musée de Châteaudun" = CANOPEE**, the Conservatoire d'Aéronefs
  Non Opérationnels Préservés Et Exposés on the former air base 279,
  2 route d'Orléans, 28200 Châteaudun; free visits Saturday afternoons.
- **The Normandie-Niémen memorial at Les Andelys is real** and has a Mirage F1
  mounted in front of it (49.24515, 1.40653). The regiment's *Hall
  Normandie-Niémen* is a gallery inside Le Bourget, not a separate museum — the
  brief's phrasing conflates the two.

---

## 5. Judgment calls

- **Replicas and reproductions are recorded, and said so in `description`,
  never in `aliases`**: the Aeroscopia Blériot XI and Morane Type G, the CAEA
  SPAD VII (a 1989 display reproduction built for a reception at Dakar, which the
  association itself does not call a faithful replica), the Hangar Y *La France*,
  the Lyon-Corbas Zipfel and Demoiselle, the Le Bourget Potez 25, and the
  Biscarrosse Donnet-Lévêque.
- **Sections and cockpits recorded as such**: Le Bourget DC-3 cockpit, Caravelle
  nose, Voisin 10 CA2 airframe structure, three airship gondolas; Rochefort
  Étendard IVP n°115 (rear section, missile-damaged over Bosnia) and Super
  Étendard n°17 (instructional airframe); Montélimar DC-7C nose and Mirage G8-02
  centre fuselage; Savigny Noratlas fuselage; Lyon-Corbas Concorde test section
  and Nord 2200 fin; Biscarrosse Latécoère 631 wing section and cabin, and the
  original Canard Fabre float.
- **Cité de l'espace**: rockets and spacecraft recorded as `missile_rocket` /
  `spacecraft` with `role_type` `launch_vehicle` / `space`, and every full-scale
  model flagged as such in `description`. Only two items there are real hardware:
  the Mir engineering model and the Europa **Coralie** second stage (restored by
  Ailes Anciennes Toulouse, transferred December 2017). The Soyuz capsule's status
  (flown descent module vs. training article) is not stated and is flagged.
  The James Webb mirrors in the gardens are components and were excluded.
- **Access types.** `appointment` for Lyon-Corbas (guided visits only, no free
  visit), CAEA (inside base aérienne 106), MAPICA and Musée Safran. `public`
  everywhere else including CANOPEE (free Saturday afternoons) and AAT (open
  Saturdays 10:00-17:30).
- **Airworthy aircraft** are recorded where a visitor would find them on the
  ground: the AJBS fleet at Cerny - La Ferté-Alais, the Montélimar OV-10 Bronco
  F-AZKM (damaged in a forced landing at Leszno in June 2026 — condition flagged),
  the CAEA Stampe.
- **Espace Air Passion registrations.** The only per-airframe inventory I could
  find is a third-party one on `aviationmuseum.eu` presenting registrations and
  types as two parallel columns. The columns are self-consistent for most of the
  list (gliders get F-C…, amateur-built get F-P…) but six registrations appear
  twice against different types, which means the pairing slips somewhere.
  **Every duplicated registration, and every registration whose format contradicts
  its type, was blanked** rather than attached to a possibly wrong airframe; the
  description of each affected row says so. 107 of 164 rows keep a registration.
  This whole file should be treated as the weakest in the set.
- **Untailed duplicates.** Where a site holds several examples of one type with no
  serials (six Wassmer Javelot, three SG 38, four Mignet HM.8 at Angers), each
  extra row carries a distinguishing `aircraft_name` so no two untailed rows of a
  type are identical.

## 6. Exclusions, named

- **Château de Saumur** — verified and excluded. Saumur's military museum is the
  Musée des Blindés (armour). Neither the château nor the Musée des Blindés holds
  an aircraft. No record written.
- **Musée Costes et Bellonte** — could not be verified as an existing site with an
  airframe. Costes and Bellonte's Breguet 19 *Point d'Interrogation* is at Le
  Bourget and already recorded there. No record written.
- **"Musée de la Résistance et de l'Aviation" sites** — no single institution of
  that name could be pinned down; several Resistance museums hold aircraft relics
  rather than airframes. Nothing written; left as a lead.
- **"Musée de l'Air annexes"** — the only current MAE annexe holding aircraft is
  the Dugny reserve, which is covered inside the Le Bourget top-up as `in_storage`
  rows rather than as a separate site. The Hangar Y at Meudon was the museum's
  home from 1921 but is now independent and holds one reproduction airship.
- **Musée Aéronautique de Cornouaille, Plobannalec** — closed in 2022; ARDHAN
  records its Alouette II going to the MAE and its HSS wrecks demolished. Not
  recorded.
- **Musée de Brienne-le-Château** — former museum; its Neptune 147563 (MAE loan)
  is described as increasingly degraded outdoors with an uncertain future. Not
  recorded; needs a human.
- **Melun-Villaroche airworthy aircraft.** The third-party list for Melun also
  contains DH.82 F-AZDH, TBM Avenger F-AZJA, T-6 F-AZEF, Po-2 F-AZPO and Yak-11
  F-AZOK. These are airworthy collection aircraft whose home base I could not
  confirm as Melun, and recording them there would create false conflicts with
  La Ferté-Alais. **Excluded, deliberately.**
- **aerosteles.net**: not used in this pass and no entries were assessed or
  rejected from it. The monument sweep, and therefore the aerosteles filtering,
  belongs to the agents holding monuments and gate guards.

## 7. Blank fields left deliberately

- `latitude` / `longitude` blank for 12 of 19 sites — no sourced coordinate.
  Every one of those has a correct five-digit code postal instead.
- `website` blank for the Les Andelys memorial only.
- `year_built` blank on all but ~15 rows: only filled where a build or delivery
  date was explicitly sourced.
- `tail_number` blank on 342 rows, overwhelmingly at CANOPEE, MAPICA, Savigny,
  Salis and Dax, where the institution publishes types but not serials.

---

## 8. Needs a human on site — ranked

1. **The Dugny reserve inventory.** The 2024 activity report names about a dozen
   aircraft in the new Réserve Grands Formats; the last full public listing of the
   Dugny reserves is from 2007. Roughly ten to fifteen airframes (Caudron C.366,
   CR.714R, B-17, Lysander, Fouga Zéphyr, DC-7C F-ZBCA, Sopwith 1½ Strutter,
   Lancaster nose, Baroudeur, DFS 230) are unaccounted for. The reserves open to
   the public roughly once a year at the Journées du Patrimoine.
2. **Espace Air Passion registration pairing.** 164 airframes, no first-party
   inventory, and six known-bad registration pairings. A visitor with the placards
   would fix the largest single file in this pass.
3. **Château de Savigny-lès-Beaune serials.** About 90 aircraft outdoors, only
   seven serials known (all naval, from ARDHAN). ARDHAN also records "incertitudes
   sur l'avenir de la collection depuis 2022" — is the collection still complete
   and still there?
4. **Étendard IV M n°06 is listed at two sites.** ARDHAN puts it at both Ailes
   Anciennes Toulouse and the CAEA at Bordeaux-Mérignac. One is wrong. Both rows
   carry the warning.
5. **Rochefort transfers in progress.** ARDHAN records Étendard IVM n°01 awaiting
   transfer to Albert, Lynx n°04 to Lyon-Corbas, and the PBY Catalina to
   Biscarrosse. All three are recorded at Rochefort with the caveat in the
   description; they may already have moved.

Runners-up: is the A400M MSN001 still on Aeroscopia's south apron, or did the
Transall replace it? Is the Cessna 337 inside Aeroscopia or on loan to the lycée
Saint-Exupéry next door? Which of Montélimar's four Fouga is which? Did the
Montélimar Bronco F-AZKM survive its June 2026 accident in Poland?

---

## 9. Leads for other agents

**Monuments and plinth aircraft noticed in passing (not recorded here):**
- **Mirage F1 in front of the Normandie-Niémen memorial, Les Andelys (27700)** —
  I did record this one, as the brief named it; if the monument agent also has it,
  de-duplicate in my favour or theirs, but not both.
- **Matra R.422 SAM**, formerly a "pot de fleur" at the entrance to Nîmes-Courbessac
  air base — now at Montélimar, so the base no longer has it.
- **Alouette II n°152** was a gate display at base aérienne 200 Apt-Saint-Christol
  until 1998 — now at Montélimar.
- **Rallye n°85 on a plinth in front of the Musée de l'Aviation at Saint-Victoret**
  (ARDHAN) — a plinth aircraft at a museum entrance.
- **Étendard IV M n°05** stands at the entrance to the Rochefort museum access road,
  effectively a gate guard; recorded in the museum file.

**Museums and collections in scope for someone else:**
- **Musée de l'Aviation, Saint-Victoret (13)** — holds the **Eurocopter X3** that
  left Le Bourget in 2017, plus HSS-1 n°944, Rallye n°85, Super Frelon n°188.
  Wikipedia coordinates 43.420107, 5.2350786.
- **Musée Delta, Athis-Mons (91)** — 48.7162379, 2.3714161. Not covered here.
- **Musée de l'Épopée de l'Industrie et de l'Aéronautique, Albert (80)** — C-47
  n°720, Alouette III n°160, Lynx n°03, Zéphyr n°24 (restoration finished July
  2024, ex-Rochefort), and Étendard IVM n°01 expected.
- **Musée Aéronautique d'Orange / Les Amis de la 5e Escadre (84)** — Alizé n°55,
  Crusader n°8, Étendard IVM n°37, Étendard IVP n°153, Super Frelon n°186,
  Zéphyr n°12, all outdoors.
- **Conservatoire Historique de l'Aéronautique Navale (CHAN), Nîmes (30)** —
  Alizé n°48 and Atlantic 1 n°31, the latter restored in 2024 and displayed near
  the entrance to the old BAN Nîmes-Garons.
- **Musée Castel-Mauboussin, Cuers (83)** — Rallye n°68, Castel 301 n°1057,
  Caudron 800 n°288, Nord 2000 n°48.
- **CELAG, Grenoble-Le Versoud (38)** — Alouette II n°488.
- **Musée d'Aviation du Berry, Touchay (18)** — Étendard IV n°41, very poor
  condition, apparently not to be restored.
- **Musée Nostalgic Aéro Passion, Sain-Yan (71)** — Étendard n°36 on deposit from
  Lyon-Corbas.
- **Les Ailes de la Mer, Bayonne (64)** — Super Étendard n°14 and a Crusader F8-A/J,
  cockpit sections only.
- **Association Héritage Avions Morane-Saulnier, Tarbes (65)** — Rallye MS 880 n°66.
- **Musée de la Marine, Paris** — Super Étendard n°18 cockpit, believed in reserve
  and not displayed.
- **Musée Airborne, Sainte-Mère-Église (50)** — C-47 n°25.
- **Aérothèque, Blagnac (31)**; **L'Envol des Pionniers, Toulouse (31)** — holds the
  Ailes Anciennes **Salmson 2A2 replica**, formally handed over in 2019.
- **Espace Patrimonial Rozanoff, base aérienne 118 Mont-de-Marsan (40)**;
  **Musée aéronautique de la base aérienne 709, Cognac-Châteaubernard (16)**;
  **Musée de la base aérienne 112, Reims (51)** — all `restricted`, inside gates.
- **Musée des débuts de l'aviation, Douzy (08)**; **Musée des frères Caudron, Rue (80)**;
  **Musée aéronautique du Berry, Touchay (18)**; **Musée de l'aéronautique locale de
  Bétheny (51)**; **Maison Chevanne, Bellegarde-en-Marche (23)**;
  **D-Day Wings Museum, Caen-Carpiquet (14)**; **Musée du terrain d'aviation militaire,
  Condé-Vraux (51)**; **Musée de l'Aviation Mas Palègry, Perpignan (66)**;
  **Musée des parachutistes, Pau (64)**; **Musée du débarquement Utah Beach (50)**;
  **Mémorial de Caen (14)**; **Musée des Arts et Métiers, Paris** — all on the French
  Wikipedia list of aviation museums, none covered in this pass.

**Out of scope, noted as instructed:** **Musée de l'Espace, Kourou (Guyane)** —
overseas département, out of scope for metropolitan France.

**Useful tooling note for whoever comes next:** `aeronavale.org` publishes a
second PDF, *"II – Aéronefs de l'A.N. préservés par types et numéros"*, which
cross-indexes the same population by type and serial. Between the two, every
preserved French naval airframe in the country can be located and serialled.


---

# Research pass: Armée de l'Air, Aéronavale and ALAT displays

# FR_BASES — French military aviation displays (Armée de l'Air et de l'Espace, Aéronavale, ALAT)

Output directory: `/home/claude/fr/bases/`
Museums file: `fr_museums.csv` (39 sites) · 39 per-site aircraft files · 186 aircraft rows · 177 with serials (95%).

---

## 1. Sources and how much weight each carried

| Rung | Source | What it gave, and how much I trust it |
|---|---|---|
| 1 | **ARDHAN, *Aéronefs préservés de l'Aéronautique navale — Listing I, par lieux*, Claude Morin, edition of August 2025** (PDF, `aeronavale.org`) | The single best source in this assignment. It is the Aéronavale's own heritage association inventory, revised continuously, organised by location, and it explicitly separates museums, state establishments, BAN "pots de fleurs", schools and private owners. Every naval row here comes from it. A copy of the extracted text is saved beside the CSVs as `_src_ardhan_lieux_aout2025.txt`. |
| 2 | **`canopeechateaudun.fr` own aircraft page** | CANOPEE publishes its own 49-airframe list with serials and unit codes. Museum-published, so it wins on "what is here now". |
| 2 | **`epr118.fr` (Espace Patrimonial Rozanoff, BA 118) own "Exposition statique" page** | Gives the *types* on outdoor display and the visiting rules, address and published GPS, but no serials. |
| 2 | **`poleaeronautiqueavord.fr` own photo albums** | The album folder names are per-aircraft (`mirage-iiib-214`, `jaguar-a-n-22`, `xingu-n-70`…), which is effectively a serialised collection list. |
| 3 | **`foxalphazoulou.overblog.com`** — a French preservation blog with a monthly "Infos patrimoine" column, current to **September 2026** | The most *current* source found for base displays. It supplied Rochefort's new Mirage 2000C stèle (2026), Nancy-Ochey's Mirage 2000D 652 (1 June 2026), the Bordeaux-Mérignac Fouga coming off its plinth (20 April 2026), the CHAN Nîmes-Garons move, Saint-Dizier's Jaguar A148, and the Captieux range aircraft. Its 2015 Noratlas survivor census is the source for the Noratlas rows. Blog, so rung 3 — but the only source that is genuinely 2026-current. |
| 3 | **Delta Reflex forum, "Liste des Mirages IV" (post by *BEN*, 15 December 2023)** | A per-airframe disposal list for all 62 Mirage IVA/IVP. This resolved almost every Mirage IV base display in France, and corrected two errors (below). |
| 3 | **fr.wikipedia `Dassault Mirage III` survivor list** | ~98 entries, well referenced but of mixed vintage. Used only for airframes it calls **exposé / préservé**; I refused every entry it calls **stocké** (see §4). |
| 4 | **`aviationmuseum.eu`** | Gave the BA 118 serial set. Demonstrably unreliable on detail: its Avord list is badly garbled (it lists "Mirage 2000N 63/12-YK", "Fouga A151", "Xingu A22" where the association's own albums say Mirage 2000N 339, Jaguar A22, Xingu 70, Mystère IVA 63) and it calls the BA 118 Mirage IIIE 572 a "Mirage 5E". I used it only where nothing better existed, and said so in each `description`. |

**Sources that did not work.** `traditions-air.fr` turned out to be a unit-heraldry and press-release site, not a display inventory — its only relevant page (PAF aircraft) is about which aircraft the team *flew*, not what is preserved. `alat.fr`'s "Stèles et lieux de mémoire" page renders its content client-side and returned only navigation. `airhistory.net` is behind Cloudflare and returned 403 to every request. `aerosteles.net`'s complete-list page timed out repeatedly and the site's own front page says it was last updated **12 August 2022**; in any case it is the monument agent's spine, not mine. `pyperpote.tonsite.biz/pfa/` — a dedicated French "pots de fleurs" gate-guard database — is **down with a WordPress fatal error**, and `web.archive.org` is blocked by this environment's egress policy, so the archived 2023 snapshot could not be read. That is the biggest single gap in this pass and the first thing a follow-up should retry.

---

## 2. Corrections made, with the evidence

- **BA 118 Mont-de-Marsan, "Mirage IV n°7".** aviationmuseum.eu lists a whole Mirage IV. The Delta Reflex disposal list records n°7 (F-THAF) as having been rebuilt into Mirage IVP prototype 01 and its **cabin only** as being at the Mont-de-Marsan base museum. Recorded as a cockpit section, and **Mirage IVA n°43 (F-THBP) added** as the complete airframe displayed at BA 118.
- **BA 118, "Mirage 5E n°572 / 4-BR".** Serial 572 and an EC 4 code are a Mirage IIIE, and EPR's own static-exhibition page names a restored **Mirage IIIE**. Recorded as Mirage III E; discrepancy noted in the row.
- **Pôle Aéronautique d'Avord.** aviationmuseum.eu's list was discarded wholesale in favour of the association's own album names plus the Fondation du Patrimoine appeal page. Result: Alouette II 341, Xingu 70, Jaguar A22, Mirage 2000N 339, Mirage F1CT 260, Mirage IIIB 214, Mirage IIIE 489, Mystère IVA 63, Alpha Jet E43, CAC Systèmes Fox drone.
- **Mirage IIIB n°214** is in **two** sources at two places. fr.wikipedia resolves it: it stood at the **entrance of BA 702 Avord** and was **moved off base to the Pôle Aéronautique in August 2025**. Recorded once, at the Pôle.
- **BA 133 Nancy-Ochey Mirage IIIE.** fr.wikipedia lists 469, 498, 500 and 608 as "stored at Nancy-Ochey". foxalphazoulou's 2026 report names **n°498, freshly repainted**, as the one standing beside the new Mirage 2000D stèle. Only 498 recorded.
- **CANOPEE Mirage IV n°1** looked suspect (Le Bourget holds n°9). The Delta Reflex list confirms it: n°1, the first production airframe, later re-registered F-THAP, went to **Musée CANOPEE Châteaudun**. Kept.
- **BA 106 Bordeaux-Mérignac** — foxalphazoulou calls it "Base Aérienne 204". Every official source (defense.gouv.fr, fr.wikipedia) says **BA 106**. Recorded as BA 106 with the discrepancy in the Fouga's `description`.

---

## 3. Judgment calls

- **Access.** Every airframe inside a military perimeter is `restricted`, including base "musées des traditions" that need clearance. `appointment` is used for three sites that publish a booking route and a price or opening hours: **CANOPEE Châteaudun** (12 €, book a visit), **Espace Patrimonial Rozanoff BA 118** (free, Wed/Thu, but you press a call button at a gate inside the base perimeter and names must be sent 48–72 h ahead), **Musée de la BA 102 Dijon-Longvic** (opens only for heritage days and air shows; ID required), and the **Pôle Aéronautique d'Avord**. `public` is used for exactly three: the **Alizé on the roundabout outside the former BAN Rochefort** (now the Gendarmerie school), the **Étendard IV on the Saint-Raphaël seafront**, and the **CHAN enclosure at Nîmes-Garons**, which foxalphazoulou reports in 2026 as arranged so that both the Atlantic and the Alizé are visible from the **D42**.
- **Sections.** Fins, noses and cockpits are recorded and said so plainly in `description`: Crusader 31 and Atlantic 55 and Crusader 5 fins (Landivisiau, Lann-Bihoué), Neptune 569 and Nord 262 cockpits (Lann-Bihoué ETAN), Super Étendard 50, 59, 69, 39 cockpits, Mirage IV 22 fin and Mirage IVP 7 cabin, Noratlas 28 nose, Jaguar A cockpit at Évreux, Mirage III cockpit at Dijon.
- **Replicas and mock-ups** are recorded with the word in `description`, never in `aliases`: the BA 118 **Yak-9D mock-up** and **Nieuport 17 replica**, and the Dijon **Mirage 2000 "Cristal"** cutaway (a real full-size instructional structure with a Plexiglas skin, not a fibreglass shell).
- **Instructional airframes count.** The EPPE deck-handling school airframes at Hyères (two Rafale M prototypes, four Super Étendards, an Alouette III), the EFSOAA airframes at Rochefort and the ten lycée airframes are all recorded — the brief asks for technical-school instructional airframes explicitly.
- **Fire-section hulks do not count.** Mirage IIIE 462 (SSIS BA 120 Cazaux), Mirage IIIE 516 (SSIS BA 709 Cognac), Mirage IVA 44 (Cazaux fire school), Mirage IIIE 426 (ESIS BA 115 Orange) and Super Étendard 61 at Landivisiau are training carcasses, not displays. **Super Étendard 61 is the one exception I did record**, because ARDHAN lists it within the Landivisiau preserved group; the others are excluded and named here.
- **Airframes leaving.** Jaguar A148 at Saint-Dizier is recorded as on display but flagged as intended for the National Museum of the USAF. Mirage IVP 55 at Saint-Dizier is `in_storage` (for the Mémorial de Gaulle at Colombey). Fouga 60 at Mérignac is `under_restoration` (off its plinth since 20 April 2026, due back).

---

## 4. Excluded, and why — named

**Aerosteles.** I rejected **zero** aerosteles entries as plaques-without-aircraft, for a reason worth stating plainly: I never got a usable list out of the site. Its "Liste complète" page timed out on every attempt through this environment's proxy, and its own front page declares a last update of **12 August 2022**. The monument agent owns that spine; nothing here depends on it.

**Reported present but refused for lack of standing evidence:**

- **Every fr.wikipedia Mirage III entry marked *stocké*** — 403 and 483 at Colmar-Meyenheim, 404 at Cognac, 412 at Tours, 425 at Ambérieu, 440 at Cuers, 469/500/608 at Nancy-Ochey, 471 and 496 at Cambrai, 476/484/494/524/547 at Châteaudun, 495/508 at Orange, 497/555/574 at Rochefort, 502 at Doullens, 519 at Captieux (this one *is* recorded — foxalphazoulou 2026 puts it at the range entrance), 590 at Floirac. "Stored" is not "on display", several of those bases have since closed, and Châteaudun's storage park was largely scrapped in February 2021. Roughly **20 airframes** dropped on this rule.
- **BA 279 Châteaudun's Nord 262 storage line** (n°43, 45, 46, 51, 52, 53, 63, 69, 70, 71, 73, 75, 79, 100). ARDHAN says they appear to have been **scrapped in 2021**. Excluded.
- **CELAE Cuers.** ARDHAN: "aucun appareil n'est préservé" — Étendard IVM 11 and 13, Lynx 275/620/803 all awaiting destruction; Super Frelon 04 already destroyed. Excluded.
- **AIA Cuers scrapping queue** — Atlantique 2 n°1, 7, 8; Lynx 813; Super Étendard 28, 47, 48, 68. Excluded (only the three *displayed* airframes recorded).
- **Base navale de Brest / Penfeld, Super Frelon n°134.** ARDHAN says it was removed in early 2024 and its future is uncertain. Excluded.
- **BAN Lann-Bihoué disposal queue** — Atlantic n°7 (scrapped 2023), Nord 262 n°28 and 62 (wrecks), Xingu n°30 and 47. Excluded.
- **Institut Amaury de Lagrange, Morbecque (59)** — ARDHAN says Alouette III n°262 is *prévue* (planned), not delivered. Excluded.
- **Lycée R. & N. de Rothschild, Saint-Maximin (60)** — MS.760 n°40 went back to the Musée de l'Air in 2020. Excluded.
- **BA 116 Luxeuil.** Both known displays have gone: **Mirage IIIE n°571** was dismantled on the base in 2026 by Ailes Anciennes Haute-Savoie, and **Mystère 20SNA n°483 (339-JI)** has been handed to EALC Lyon-Corbas. I found no evidence of a surviving display, so **no Luxeuil site was created**. This is almost certainly wrong — see §6.
- **BA 117 Paris, Mirage IIIE n°529.** fr.wikipedia says it stood at the entrance, was moved to Châteaudun during the Balard construction and was "to return in 2014". No evidence it did. Excluded, flagged.
- **École du Service de Santé des Armées, Lyon-Bron, Mirage IIIE n°567.** One stale source only, and the ESSA at Bron closed in 2011. Excluded, flagged as a lead.
- **SPAD VII n°3270** rebuilt at Saint-Dizier — being finished for the American Heritage Museum in the USA. Excluded.
- **P-38 Lightning full-size mock-up** at Saint-Dizier — not an airframe, and destined for the Maison du Petit Prince. Excluded, noted.
- **Alpha Jet fin monument at the entrance to Cazaux village** (inaugurated 28 August 2023, on public land). A fin on its own, and off base — passed to the monuments agent.
- **Thalès Brest, Super Étendard n°35 on a plinth**, and **Dassault Argenteuil, Mirage IIIE n°570 at the factory gate**, and **stèle Dassault Bordeaux, Mirage IVP n°56** — industrial sites, not bases. Leads.

---

## 5. Blank fields left deliberately

- **Coordinates are blank on 37 of 39 sites.** Only two are filled, both from a figure the site itself publishes: BA 118 EPR (43.905806, −0.498303, from epr118.fr) and the Pôle Aéronautique d'Avord (47.0356638, 2.6534963, from Berry Province). A base's map pin is not the airframe's position and I would not have been recording where the visitor should stand, so blank is honest.
- **Postal code blank on one site** — Lycée Frédéric Mistral, Nîmes. Nîmes has both 30000 and 30900 and I could not confirm which.
- **`year_built` is blank on all 186 rows.** No sourced build or delivery date was found for a single airframe; the only near miss is the Nancy-Ochey Mirage 2000D 652, which foxalphazoulou says "sorti d'usine en 1996" — a factory-release year for the type's delivery, which I judged too loose to file as `year_built`.
- **Nine rows carry no serial**: the CANOPEE F-84F (CANOPEE does not publish one), the BA 118 Nieuport 17 replica, the Évreux Transall C-160NG and Jaguar A cockpit, the Lann-Bihoué Nord 262 cockpit, the Avord CAC Fox drone, and three at Dijon (Mirage IIIC, Mirage 2000 Cristal, Mirage III cockpit). Each says so in `description`.
- **`variant` left blank** on French Navy Alouette IIIs, Lynx and HSS-1s. The sub-variant is not stated by ARDHAN and guessing SA 316B vs SA 319B or Mk.2(FN) vs Mk.4(FN) from a bare number would be invention.

---

## 6. Needs a human on site — ranked

1. **BA 116 Luxeuil-Saint-Sauveur.** I created no site at all, on the strength of two removals. A base with a fighter wing almost certainly has a gate guard. Someone should walk the entrance and the traditions area.
2. **BA 701 Salon-de-Provence, and the Patrouille de France heritage.** Nothing found beyond unit history. The École de l'Air, the PAF and the Groupement École 312 between them must hold retired Fouga Magisters, Alpha Jets and a Mystère IVA, and none of it is on the open web in a form I could stand behind. This is the largest named gap in the assignment.
3. **BA 115 Orange — is the "musée de la base aérienne 115" the same thing as the Musée Aéronautique d'Orange (Les Amis de la 5e Escadre)?** fr.wikipedia attributes Mirage 5F n°38 to a base museum and Mirage F1C 103, F1CT 238, Mirage IIIR 231, Alizé 55, Crusader 8, Étendard IVM 37, Étendard IVP 153, Super Frelon 186 and Zéphyr 12 to the association. If they are one organisation on one site, my BA 115 record and the museums agent's record will collide. **This is the single most likely duplicate in the whole set.**
4. **Évreux's Transall C-160NG and Jaguar A cockpit need serials**, and the Breguet 765 Sahara n°501 needs a note on whether the association's restoration is now visitable — it has been running since 1997.
5. **BAN Landivisiau vs BAN Lann-Bihoué: Crusader n°29.** ARDHAN lists the same aircraft at both bases. I recorded it twice with the conflict spelled out in both rows rather than silently picking one, because I have no basis to choose. **One of these two rows must be deleted before import** — an aircraft is in exactly one place. Same question, smaller stakes, for Super Étendard n°18: ARDHAN puts a whole airframe at Landivisiau and a cockpit at the Musée de la Marine in Paris.

Also unresolved but lower value: whether Noratlas n°208 "à Toulouse-Balma" is on the DGA Techniques Aéronautiques site (Balma is where DGA-TA sits, so it probably is, but I would not file it on that inference); whether the BA 117 Paris Mirage IIIE came back; and whether the BA 943 Mont-Agel and BA 901 Drachenbronn Mirage IIIs, both from a single stale Wikipedia line, are still standing.

---

## 7. Coverage against the assignment's base list

**Recorded (19 Armée de l'Air / joint sites):** BA 102 Dijon-Longvic, BA 105 Évreux, BA 106 Bordeaux-Mérignac, BA 110 Creil, BA 113 Saint-Dizier, BA 115 Orange, BA 118 Mont-de-Marsan, BA 120 Cazaux, BA 123 Orléans-Bricy, BA 125 Istres, BA 133 Nancy-Ochey, BA 279 Châteaudun (CANOPEE), BA 702 Avord, BA 721 Rochefort, BA 722 Saintes (EETAAE), BA 901 Drachenbronn, BA 943 Mont-Agel, ex-BA 101 Francazal, CTPE Captieux. Plus Pôle Aéronautique d'Avord (off base).

**Aéronavale (9 sites):** Hyères (base + EPPE + ETAN), Landivisiau, Lann-Bihoué (base + ETAN), Lanvéoc-Poulmic, École navale, École des Fusiliers Marins Lorient, AIA Cuers-Pierrefeu, ex-BAN Rochefort (Gendarmerie school), ex-BAN Fréjus-Saint-Raphaël, plus CHAN at the former BAN Nîmes-Garons. Toulon itself yielded nothing — ARDHAN records no preserved airframe at the naval base, only at Cuers and Hyères.

**Technical schools (10 lycée sites + EFSOAA + EETAAE 722).** All ten lycées in ARDHAN's section 5 handled: nine recorded, Morbecque excluded as not yet delivered, Saint-Maximin excluded as returned to the MAE. ARDHAN itself flags this list as "demanderait à être actualisée" and says it has no photographs of these aircraft — so all ten are single-sourced and should be treated as the weakest block in the set.

**DGA:** DGA Techniques Aéronautiques Toulouse/Balma (Super Étendard 01, Étendard IV 26) and CTPE Captieux. **DGA-EV / CEV Istres and Brétigny produced nothing** — CEV Brétigny closed with BA 217 in 2012 and I found no trace of what happened to its airframes.

**Not recorded, nothing found:** BA 103 Cambrai, BA 107 Villacoublay, BA 112 Reims, BA 116 Luxeuil, BA 117 Paris, BA 126 Solenzara, BA 128 Metz-Frescaty, BA 132 Colmar, BA 136 Toul-Rosières, BA 217 Brétigny, BA 705 Tours, BA 709 Cognac, BA 726 Nîmes-Garons (only the CHAN enclosure), BA 942 Lyon-Mont Verdun, BA 701 Salon-de-Provence. For the closed ones the answer to "what happened to the gate guards" is, as far as this pass could establish: **Metz-Frescaty's Noratlas n°41 and Cambrai-Épinoy's Noratlas n°172 fuselage are both listed as gone** (foxalphazoulou's "disparus"), and Châteaudun's whole storage park was scrapped in February 2021 apart from what CANOPEE saved. Nothing was found on Colmar, Toul-Rosières, Reims or Brétigny.

**ALAT produced nothing at all.** No display was substantiated at Phalsbourg, Étain-Rouvres, Pau, Dax, Le Luc, Montauban or Villacoublay. `alat.fr`'s stèles page would not render, the Musée de l'ALAT at Dax is a civilian-access museum belonging to another agent, and the Malcros *Aéronefs de l'ALAT* PDF series (hosted at `museehelico-alat.com`) is the obvious next source — it is a per-airframe fate register by type, in about twenty volumes, and a follow-up pass should mine the Alouette II, Alouette III, Gazelle and Puma volumes for "pot de fleur" entries. **ALAT is the biggest unworked area in this assignment.**

**Gendarmerie and Sécurité Civile.** The only thing found is the Alizé at the gate of the Gendarmerie school at Rochefort (recorded). Nothing was substantiated at the Sécurité Civile base at Nîmes-Garons or at any Gendarmerie air unit.

---

## 8. Leads for other agents

**Museums / collections agent**
- **Musée Aéronautique d'Orange, Les Amis de la 5e Escadre** — Alizé 55, Crusader 8, Étendard IVM 37, Étendard IVP 153, Super Frelon 186, Zéphyr 12, Mirage IIIR 231, Mirage F1C 103, Mirage F1CT 238, all outdoors. **Check against my BA 115 record first (§6.3).**
- **Musée de la base aérienne 112 et de l'aéronautique locale**, Bétheny (former BA 112 Reims).
- **Musée de l'ALAT et de l'Hélicoptère, Dax** — Alouette II 162, HSS-1 143, Lynx 276, Super Frelon 163, Alouette III 302, plus Alouette III 306 ex-Sécurité Civile.
- **Musée des Parachutistes, Pau** — Noratlas n°161 plus parts of n°186.
- **Conservatoire de l'Air et de l'Espace d'Aquitaine (CAEA), Mérignac** — Alizé 50, Étendard IVM 06 and 40, Crusader 32, HSS 149, JRB-4 4, SNJ 7 and 81 (81 is the ex-Lann-Bihoué gate guard), Super Étendard 33, Super Frelon 165, Mirage IIIB 204, Mirage IIIE 454 and 560, Mirage F1BQ 16, Mirage F1EQ6/27, Noratlas 188, Jaguar E23, Mirage IV A03 cabin, Mirage IVP 56.
- **EALC / Musée Clément Ader, Lyon-Corbas** — Alizé 47, Étendard IVM 34, MS.760 31, N.1101 125, N.2200 01 fin, N.262 60, Super Étendard 71, plus Mystère 20SNA n°483 arriving from Luxeuil in 2026.
- **Morbihan Aéro Musée, Monterblanc** — as of an August 2026 visit: H-34A 58705, Noratlas 160, Transall C-160R R202 (64-GB), T-33A 53091, MS.733 45, Pitts S-1D F-PYXA, DFS SG-38, Fouga CM.170 n°143, Caudron C-800 F-CAHF, Mauboussin 129 n°191, Étendard IVM 14, F-4C 64-0922 fuselage. Hangar No. 2 is a listed monument.
- **Musée de l'Épopée de l'Industrie et de l'Aéronautique, Albert** — has taken Étendard IV n°01 (June 2025) and Zéphyr n°24 (2024) from ANAMAN Rochefort; also Mirage F1C 20, Mirage IIIE 449 and 515, Mirage IVP 25, C-47 720, Alouette III 160, Noratlas 54/97/125/184/189.
- **ANAMAN Rochefort** (Musée de l'Aéronautique Navale) — the full holding is in `_src_ardhan_lieux_aout2025.txt`, including which airframes have left and which are due to leave (Lynx 03 to Albert, Lynx 04 to EALC, the Catalina to Biscarrosse).
- **Musée européen de l'Aviation de Chasse, Montélimar** — has gained Mirage IIIT n°01 from BA 721 Rochefort (November 2024) and Microjet 200B n°03 F-WDMT; still expecting Super Étendard n°15 from Hyères.

**Monuments agent**
- Alpha Jet fin, entrance to Cazaux village (La Teste-de-Buch), inaugurated 28 August 2023, public land.
- Super Étendard n°35 on a plinth outside Thalès, Brest.
- Mirage IIIE n°570 at the gate of Dassault Aviation, Argenteuil.
- Mirage IVP n°56 on a Dassault stèle at Bordeaux.
- Mirage IIIE n°504 note: mine, at BA 943 — but the Roquebrune display may be visible from the public road; worth a check.
- Noratlas on plinths at Tarbes (n°111), Pamiers (n°196), Les Mureaux (n°202), Toulouse-Balma (n°208), Aulnay-sous-Bois (n°50, UNP 93 clubhouse), Merville-Calonne (n°129, EPAG).
- Mirage IIIE n°243 on a roundabout at Saint-Amand-Montrond; n°233 on the N7 roundabout at Montélimar; n°84 on an N7 roundabout at Orange; n°514 at Rennes Saint-Jacques airport; n°521 at Montceau-les-Mines; n°550 at Cannes-Mandelieu; n°578 at Beynes; n°579 at Bitche; n°616 at Le Havre-Octeville; n°02 at ISAE-Supaéro Toulouse.
- Mirage F1C n°101 on a pylon at Les Andelys (Eure) since 2008; F1C n°85 at the aéroclub vauclusien, Avignon.
- Zéphyr n°29 (in fact Fouga n°517) on a plinth at the entrance to the Morlaix airport zone; Zéphyr n°18 on a plinth beside the A7 at Portes-lès-Valence.
- Étendard IVM n°3 in a park at Paray-Vieille-Poste.
- HSS-1 n°177 converted into holiday accommodation at a campsite in Saint-Michel-Chef-Chef (44).
- Alouette II on a roundabout at Marignane; AS 350 Écureuil on the roof of the restaurant "Chez Barbara" at Censeau (39).
- Breguet 763 Provence n°6 at the Aéroclub de Chaubuisson, Fontenay-Trésigny — present since 1968, the club issued an appeal for help in June 2026.

**Overseas / out of scope found in passing:** Alouette III n°303 with Air Formation at Tahiti-Faa'a.

---

## 9. Files and row counts

| file | rows | with serial |
|---|---|---|
| `aia-cuers-pierrefeu_aircraft.csv` | 3 | 3 |
| `ba102-dijon-longvic_aircraft.csv` | 4 | 1 |
| `ba105-evreux_aircraft.csv` | 6 | 4 |
| `ba106-bordeaux-merignac_aircraft.csv` | 2 | 2 |
| `ba110-creil_aircraft.csv` | 2 | 2 |
| `ba113-saint-dizier_aircraft.csv` | 4 | 4 |
| `ba115-orange_aircraft.csv` | 2 | 2 |
| `ba118-mont-de-marsan_aircraft.csv` | 17 | 16 |
| `ba120-cazaux_aircraft.csv` | 1 | 1 |
| `ba123-orleans-bricy_aircraft.csv` | 1 | 1 |
| `ba125-istres_aircraft.csv` | 1 | 1 |
| `ba133-nancy-ochey_aircraft.csv` | 2 | 2 |
| `ba702-avord_aircraft.csv` | 1 | 1 |
| `ba721-rochefort_aircraft.csv` | 9 | 9 |
| `ba901-drachenbronn_aircraft.csv` | 1 | 1 |
| `ba943-roquebrune_aircraft.csv` | 1 | 1 |
| `ban-hyeres_aircraft.csv` | 15 | 15 |
| `ban-landivisiau_aircraft.csv` | 11 | 11 |
| `ban-lann-bihoue_aircraft.csv` | 8 | 7 |
| `ban-lanveoc-poulmic_aircraft.csv` | 11 | 11 |
| `canopee-chateaudun_aircraft.csv` | 49 | 48 |
| `chan-nimes-garons_aircraft.csv` | 2 | 2 |
| `ctpe-captieux_aircraft.csv` | 2 | 2 |
| `dga-toulouse_aircraft.csv` | 2 | 2 |
| `ecole-fusiliers-marins-lorient_aircraft.csv` | 2 | 2 |
| `ecole-navale_aircraft.csv` | 1 | 1 |
| `eetaa722-saintes_aircraft.csv` | 2 | 2 |
| `francazal-noratlas_aircraft.csv` | 1 | 1 |
| `gendarmerie-rochefort-alize_aircraft.csv` | 1 | 1 |
| `lycee-alexandre-denis-cerny_aircraft.csv` | 1 | 1 |
| `lycee-aristide-briand-houilles_aircraft.csv` | 2 | 2 |
| `lycee-charles-jully-saint-avold_aircraft.csv` | 1 | 1 |
| `lycee-flora-tristan_aircraft.csv` | 1 | 1 |
| `lycee-frederic-mistral-nimes_aircraft.csv` | 1 | 1 |
| `lycee-jean-zay-jarny_aircraft.csv` | 1 | 1 |
| `lycee-tristan-corbiere-morlaix_aircraft.csv` | 2 | 2 |
| `lycee-val-de-lys-estaires_aircraft.csv` | 2 | 2 |
| `pole-aeronautique-avord_aircraft.csv` | 10 | 9 |
| `saint-raphael-etendard_aircraft.csv` | 1 | 1 |
| **39 files** | **186** | **177** (95%) |

`fr_museums.csv` — 39 sites: 3 `public`, 4 `appointment`, 32 `restricted`.

Working files kept for provenance: `_build.py`, `_data_*.py` (the generators, so every row can be traced to the statement that produced it) and `_src_ardhan_lieux_aout2025.txt` (extracted text of the ARDHAN PDF, in case that PDF is replaced).


---

# Research pass: the northern and western régions

# FR_NORTHWEST — Hauts-de-France, Normandie, Île-de-France, Bretagne, Pays de la Loire, Centre-Val de Loire, Grand Est

Output directory: `/home/claude/fr/northwest/`
Museums file: `fr_museums.csv` — 35 sites.
Aircraft files: 35, one per site — 227 rows, 197 with a serial or registration (87 %).

38 départements screened: 02 08 10 14 18 22 27 28 29 35 36 37 41 44 45 49 50 51 52 53
54 55 56 57 59 60 61 62 67 68 72 75 76 77 78 80 85 88 91 92 93 94 95.

---

## 1. Sources and how much weight each carried

| Source | Weight | What it gave, and how it failed |
|---|---|---|
| **`aeronavale.org` (ARDHAN), "Aéronefs de l'Aéronautique navale préservés par lieux", February 2025** | **Highest.** Dated, signed, revised annually, and explicit about doubt ("à confirmer", "devrait être cédé") | The single best source in this sweep. It is the only source that gave me the lycée and école-technique airframes the assignment asked for (Estaires, Houilles, Morlaix, Jarny, Saint-Avold), the Morlaix airport plinth Fouga, the Thales Brest Super Étendard, and the Saint-Michel-Chef-Chef campsite helicopter. It also corrected two other lists (see §3). |
| **Museums' own collection pages** | High, and wins on "what is here now" | CANOPEE Châteaudun publishes a full current aircraft list; used verbatim in preference to third-party lists. Musée-EIA (Albert) and the Warluis museum publish no machine-readable inventory. |
| **`aviationmuseum.eu`** | Medium-high for breadth, medium for currency | Its per-museum tables (serial column paired with a type column) were the backbone of the museum sweep and gave the France index that Wikipedia's `Liste des musées aéronautiques` only partly duplicates. Undated, and demonstrably stale in places — it still lists the closed Cornouailles, Condé-Vraux, BA 112 and Normandy Tank museums as if current, and lists a Mercure and a Caravelle at Musée Delta that no longer exist there. |
| **`aerosteles.net`** | **Low for this task.** See §2 | Thorough, well photographed, and almost entirely about crash memorials. |
| **French Wikipedia per-type articles** (Mirage III, Jaguar, Fouga Magister, Nord 2501, Étendard) | Low | The French Wikipedia type articles do **not** carry survivor lists in the way the English ones often do. Mirage III, Jaguar and Fouga Magister each yielded zero usable French locations. Only `Nord 2501` had a survivors paragraph, and it produced exactly one record in my area — Noratlas n°202 at ArianeGroup Les Mureaux. |
| **`airhistory.net`** | Not usable in this session | Every request, including via the proxy with a browser user-agent, returned HTTP 403. Its "[Off-Airport]" taxonomy is exactly right for the monument sweep and remains the largest untapped source for whoever picks this up. |
| **POP / Plateforme Ouverte du Patrimoine (`pop.culture.gouv.fr`)** | Promising, barely used | Surfaced the Les Mureaux Noratlas as a protected Palissy object. A systematic Palissy query for `avion` would probably find every legally protected airframe in France in one pass. |

---

## 2. aerosteles.net: how hard the filter had to be

I pulled the complete `liste-fr` index (4 151 entries nationally), parsed it by commune INSEE code, and cut it to my 38 départements: **2 489 entries**. I then keyword-screened all 2 489 titles for aircraft types, "socle", "musée", "gardien", "cellule", "fuselage" and similar, which surfaced **328 candidates**, and read the plausible ones.

**Records produced from aerosteles: zero.**

- Roughly **2 160 of the 2 489** were rejected on the title alone — named individuals, crews, "maison natale de", cemetery graves, airfield plaques, record-flight markers.
- Of the **328 keyword hits, at least 300 are crash stelae**: the single largest category in the seven régions is "Lancaster <serial>" — a roadside stele at a bomber crash site, with no airframe. Grand Est, Centre-Val de Loire and Île-de-France are saturated with them.
- The handful that genuinely name a preserved airframe were all already accounted for:
  - `merville_dakota` — the Merville battery C-47, **already in the database**.
  - `mae-legende`, `mae-legende2`, `mae-legende3` (Dugny) — inside Le Bourget, **excluded**.
  - `fauville-transall` (BA 105 Évreux), `moeslains-rafale` and `stdizier-jaguar` (BA 113) — **Armée de l'Air base displays, excluded by assignment**.
- Two entries I chased individually and rejected on the evidence:
  - **`damery-noratlas` (Damery, 51)** — the title reads "Noratlas N°69" and looks like a preserved airframe. The entry page shows a **stele only**, at the edge of the Bois de Saint-Marc, for the loss of Nord 2501 n°69 (F-RAQH) of ET 1/62 on 19 October 1971. Rejected.
  - **`vaudrecourt-mirage` (52)**, **`stmaurice-f100` (88)**, **`valdajol-mirage4` (88)**, **`ochey-mirage3` (54)** — all crash or unit memorials, no airframe.

So: **2 489 entries screened, 328 read, 0 site records.** aerosteles is the right spine for *finding* French aviation memorials and completely the wrong spine for finding *airframes*. That is the finding, and it is worth recording so nobody repeats the sweep.

---

## 3. Corrections made, with the evidence

1. **CANOPEE Châteaudun — 49 rows, not 63.** aviationmuseum.eu lists 63 airframes. CANOPEE's own current site (`canopeechateaudun.fr/aeronefs_`, © 2026) lists 46 entries. I used the museum's own list plus nothing, per the methodology's "the museum's own site wins for what is here now". The 17 in the third-party list but not the museum's — Mirage IIIE 429/513/534, Mirage IIIB-RV 277, Mirage IIIR 303, Mirage IIIRD 367, MD 312 n°218, MD 315 n°124, Mystère IVA n°59, Super-Mystère n°59, Sikorsky H-34A SKY479, Jaguar A A43 and A154, Nord 262 and others — are **not recorded**. They may have been scrapped, moved, or simply omitted from the museum's page. Flagged in §6.
2. **CANOPEE: "486" is a Fouga, not a Tucano — corrected the other way round.** aviationmuseum lists n°486 as a Fouga CM.170; the museum's own page also files 486 under Fouga CM.170 with the note "ex 312-TX". I followed the museum. (My initial reading, that 486 must be a second EMB-312 because French Tucanos are serialled in the 450–530 band, is the plausible alternative and is left here as a doubt.)
3. **CANOPEE T-33A: 51-6524, not 18658.** The museum gives 51-6524 / 314-YG; aviationmuseum gives 18658 / 314-YG. Museum wins.
4. **CANOPEE F-100: an F-100A n°53-1580 / FW-580, not an F-100D 56-3380 / FW-380.** Museum wins.
5. **Musée Delta is much smaller than published lists suggest.** The 2013 avionslegendaires report records the collection being broken up for a road and tram line: the Mercure and the Caravelle went for scrap or were dispersed (fr.wikipedia says the Mercure was dismantled and shipped to the Netherlands; the Caravelle F-BVPZ became an airport fire-training hulk). **Neither is recorded at Musée Delta.** What is recorded is what aviationmuseum's current table and the museum's own address show: Concorde 02 F-WTSA, Mirage IIIB-RV 245, Mirage IIIE 530, Mirage IIIRD 352, an Aviasud Sirocco and a Visair 1. Address corrected to 40 avenue Jean-Pierre Bénard (not 1 avenue Bernard Lathière, which several directories still carry).
6. **Étendard IV M n°01 is at Rochefort, not Albert.** aviationmuseum puts an Étendard IV M "01" in the Albert collection. ARDHAN (Feb 2025) puts n°01 outdoors at Rochefort "en instance de cession au Musée d'Albert" — pending transfer, not transferred. An aircraft is in exactly one place, so it is **not** in the Albert file. Re-check after 2026.
7. **Albert gained an Alouette III.** ARDHAN records Alouette III n°160 at the Albert museum; no third-party list had it. Added.
8. **Albert's C-47 and Lynx and Zéphyr provenance.** ARDHAN identifies the Albert C-47 as ex-Aéronavale n°720 painted in June 1944 US colours; aviationmuseum gives the marks 42-108979 / H2-K / 282. Recorded with 42-108979 in `tail_number` and `720` in aliases, with the provenance in the description.
9. **Musée des Frères Caudron, Rue (80) — excluded, no airframe.** Its Wikipedia entry and the Baie de Somme tourist board both describe models, trophies, bronzes and documents, not an aircraft. It is a Caudron *memorial* museum. Named here so the omission is deliberate, not a gap.

---

## 4. Excluded, and why — every one named

**Excluded by assignment** (owned by other agents): Le Bourget, Espace Air Passion Angers, Musée Aéronautique Presqu'île Côte d'Amour, Morbihan Aéro Musée Vannes, Hangar Y Meudon, Musée Safran Réau, La Ferté-Alais, Normandie-Niémen Les Andelys, Musée de la Batterie de Merville, and all Armée de l'Air / Aéronavale / ALAT base displays.

Base-display airframes I found and deliberately did **not** record, so they are on the record as seen:
BA 105 Évreux Transall; BA 113 Saint-Dizier Rafale and Jaguar monuments; BAN Landivisiau (Crusader 29/31, Étendard 15/52, Super Étendard 18/23/30/61, Zéphyr 30); BAN Lann-Bihoué (Alizé 86, C-47 87, Crusader 29, Neptune 567); BAN Lanvéoc-Poulmic (Alouette III 161/245/444/314, CAP 10 108/111/120, HSS 129, Lynx 270, Rallye 64, Super Frelon 162); École navale Brest Super Étendard n°57 (sits on the Lanvéoc-Poulmic naval air station); École des Fusiliers Marins Lorient (HSS 144, Super Frelon 148).

**Closed — excluded with the closure evidence:**

| Site | Why excluded |
|---|---|
| **Musée Aéronautique de Cornouaille, Plobannalec (29)** | Closed since 2022 (ARDHAN, Feb 2025, explicitly: "Ce musée a fermé en 2022"). Its Alouette II n°809 was a Musée de l'Air loan and may return to Le Bourget; the HSS n°135, 640, 641 were wrecks marked for demolition. Nothing to visit. |
| **Musée du Terrain d'Aviation de Condé-Vraux 1939-1945, Vraux (51)** | Permanently closed 29 September 2024. Held a Broussard 164/2-HE, a Jaguar A A17 nose, a Stirling fuselage LK142 and a DFS 320 frame. **Where those four went is an open question** — worth a follow-up, they are real airframes. |
| **Musée de la Base Aérienne 112, Reims (51)** | Closed. Held RF-84F 37577/33-CK and Vautour 2N 347/30-FB. Disposition unknown. |
| **Normandy Tank Museum, Catz (50)** | Closed 2017 and the collection auctioned. Held a Stearman F-AZNT and a Poullin PJ-5A. |
| **Musée de Brienne-le-Château (10)** | Listed by ARDHAN as *ex*-museum; its Neptune n°147563 (a Musée de l'Air loan) was progressively deteriorating outdoors and may have been recovered. Not recorded. |

**Excluded on substance:**

| Site / airframe | Why |
|---|---|
| Musée des Frères Caudron, Rue (80) | Models and archives only, no airframe (see §3.9). |
| Aero Vintage Academy and Mémorial Flight, Cerny / La Ferté-Alais (91) | Both sit on the La Ferté-Alais aerodrome, which the assignment excludes. Their collections (Stearmans, a P-51D, a T-28A Fennec, and Mémorial Flight's WWI fleet) are substantial and should not be lost — see Leads. |
| Lycée R. & N. de Rothschild, Saint-Maximin (60) | Its MS 760 n°40 went back to the Musée de l'Air in 2020. Nothing there now. |
| Institut Amaury de Lagrange, Morbecque (59) | ARDHAN says Alouette III n°262 is "prévue" — planned, not delivered. No evidence of presence, so no record. |
| Fort de l'OTAN / Fort Lefebvre (Mirage IIIE 403/13-QB) | It is at Belfort (90), Bourgogne-Franche-Comté — out of my area. Handed on as a lead. |
| Le Plessis-Belleville (60) MS 733 n°46, Compiègne-Margny (60) MS 317 n°351, Poses/Val-de-Reuil (27) MS 317 n°258, Rouen (76) MS 733 n°128, Rennes (35) MS 733 n°200, Pontivy (56) MS 733 n°61, Chavenay-Villepreux (78) Stampe n°1073, Lunéville (54) Stampe n°595, Haguenau (67) Stampe n°691, Orbigny (37) Stampe n°262 and n°1091, Étampes-Mondésir (91) Rallye n°83, Signy-Signets (77) Alouette II n°163 / Alouette III n°358 and n°280 | Privately owned airworthy or stored aircraft at aerodromes, with no public collection to visit. The app answers "where can I go and see this"; a hangared private aeroplane is not an answer. Named so the decision is auditable. |
| Caen-Carpiquet (14) MS 733 n°190 (F-AZAF) | ARDHAN calls it an "épave" — a wreck. No public access, no record. |
| Musée de la Marine, Paris — Super Étendard n°18 cockpit | ARDHAN: "non exposé, vraisemblablement dans les réserves". Not visitable; not recorded. |
| Dassault Seclin (59) Mirage III NG prototype | fr.wikipedia says it is *stored* on the factory car park. No public access and no confirmation of presence; a lead, not a record. |
| Payen Pa-100 at Musée Delta | A 1:1 mock-up, not an airframe. Not recorded. |

---

## 5. Judgment calls

- **Replicas are recorded, and the description says so in the first clause.** Four rows are replicas or reconstructions: the Nieuport 17 at Thiepval, the Hawker Typhoon JP656 at the Mémorial de Caen, the Horsa PF800 at Mémorial Pegasus, and the Sommer 1910 biplane at Douzy. Each is the reason a visitor goes to that room, and each is flagged. The Payen Pa-100 mock-up at Musée Delta and the 1:4 Sommer models at Douzy are *not* recorded — a scale model is not an airframe.
- **Sections are recorded and labelled.** Cockpit/nose/fuselage-only rows: B-24D 41-30188 and B-25D and the second Typhoon and the Corsair tail at the D-Day Wings Museum; C-47B N2-123 cockpit, also D-Day Wings; the Dead Man's Corner C-47 fuselage and Waco cockpit; the Mémorial Pegasus Horsa wreck; the Boeing 727 and Mercure forward fuselages at Albert; the Émeraude and HM-14 fuselages at the Grenier de l'Aviation; the An-2 fuselage at MM Park; the Super Étendard n°69 cockpit at Houilles.
- **Missiles are in scope and recorded**: the V-1, the piloted Fi 103R Reichenberg n°126 and the V-2 at La Coupole; the V-1 at Melun-Villaroche. `aircraft_type` = `missile_rocket`, `role_type` = `cruise` or `ballistic`, `wing_type` blank.
- **Access types.** Lycée airframes are `appointment` — they exist for teaching, are inside a school, and are not on a public road. CANOPEE is `appointment` (guided tours Wednesdays and Saturdays) even though the collection sits on the former BA 279; the ARDHAN census is explicit that CANOPEE is a separate Armée de l'Air *conservatoire*, not a base gate display, which is why it is included at all. Concorde F-BVFF is `public`: Heritage Concorde states it is "not currently open to the public, but can be viewed externally", and the brief treats a guardian visible from outside as public. ArianeGroup Les Mureaux and Thales Brest are `restricted` — real airframes on private industrial ground.
- **Two untailed rows of the same type at one site** — only case is the D-Day Wings Typhoon pair (composite JP843 and a bare cockpit), and the second is distinguished in its description.
- **`year_built` is blank on all 227 rows.** No source in this sweep gave a sourced build or delivery date, and a French airframe number is not a year.
- **`latitude`/`longitude` are blank on all 35 sites.** The only coordinates I could have used were Google-Maps embed centres scraped from third-party pages, which point at a town or an airport rather than at an airframe. Postal codes are filled on all 35. A correct code postal beats a guessed pin.

---

## 6. Needs a human on site — ranked

1. **CANOPEE Châteaudun: are the 17 airframes on the third-party list but absent from the museum's own page still there?** Mirage IIIE 429 / 513 / 534, Mirage IIIB-RV 277, Mirage IIIR 303, Mirage IIIRD 367, MD 312 n°218, MD 315 n°124, Mystère IVA n°59, Super-Mystère n°59, Sikorsky H-34A, Jaguar A A43 and A154, F-84F 52-9117, Nord 262. This is the single biggest number in play in the whole area — 17 aircraft, one visit.
2. **Where did the Vraux collection go when the museum closed on 29 September 2024?** A Short Stirling fuselage (LK142) is a genuinely rare object; so is a Jaguar A nose. Also the BA 112 Reims RF-84F and Vautour.
3. **Musée de l'Épopée de l'Industrie et de l'Aéronautique, Albert — verify the full 65-row list on the ground.** It is the largest collection in the seven régions and it has no published inventory of its own; my list is a third-party table plus ARDHAN corrections. Specific questions: is Étendard IV M n°01 there yet? Is MS 733 n°173 the museum's or the Albert Vintage Aircraft association's? What is the airframe the source calls "Vickers Blériot 22" (F-PCVB), which I left out because I could not identify it?
4. **Camping du Haut Village, Saint-Michel-Chef-Chef (44): identify the two fixed-wing airframes.** The site advertises "Avion SKYLANDER" and "Avion GRUMMAN" as accommodation alongside the Sikorsky. I recorded only the helicopter, because ARDHAN gives its identity (HSS-1 n°177) and I will not guess a type from a marketing name.
5. **Musée de l'Aviation de Warluis (60): confirm the collection and get serials.** The museum website returned an empty response throughout this session; the eight rows rest entirely on one undated third-party table.

Secondary: does the Mémorial de Caen still display the MiG-21R n°45 (the Cold War gallery has been reworked)? Is the Étendard IV M n°3 "exposé dans un parc" at Paray-Vieille-Poste (91, next to Orly) still there, and is it a Musée Delta outstation or a municipal monument?

---

## 7. File and row counts

| File | Site | Aircraft | With serial |
|---|---|---|---|
| `albert_epopee_aircraft.csv` | Musée de l'Épopée de l'Industrie et de l'Aéronautique | 65 | 61 |
| `canopee_chateaudun_aircraft.csv` | CANOPEE Châteaudun | 49 | 48 |
| `melun_villaroche_aircraft.csv` | Musée de l'Aviation de Melun-Villaroche | 29 | 22 |
| `dday_wings_aircraft.csv` | D-Day Wings Museum | 13 | 7 |
| `grenier_aviation_aircraft.csv` | Le Grenier de l'Aviation | 12 | 10 |
| `warluis_aircraft.csv` | Musée de l'Aviation de Warluis | 8 | 8 |
| `musee_delta_aircraft.csv` | Musée Delta | 6 | 5 |
| `arts_et_metiers_aircraft.csv` | Musée des Arts et Métiers | 4 | 1 |
| `abri_hatten_aircraft.csv` | Musée de l'Abri de Hatten | 3 | 3 |
| `airborne_museum_aircraft.csv` | Airborne Museum | 3 | 3 |
| `la_coupole_aircraft.csv` | La Coupole | 3 | 1 |
| `mm_park_aircraft.csv` | MM Park France | 3 | 3 |
| `dday_experience_aircraft.csv` | D-Day Experience - Dead Man's Corner Museum | 2 | 1 |
| `lycee_briand_houilles_aircraft.csv` | Lycée Aristide Briand Houilles Instructional Airframes | 2 | 2 |
| `lycee_corbiere_morlaix_aircraft.csv` | Lycée Tristan Corbière Morlaix Instructional Airframes | 2 | 2 |
| `lycee_val_de_lys_aircraft.csv` | Lycée Val de Lys Estaires Instructional Airframes | 2 | 2 |
| `memorial_caen_aircraft.csv` | Mémorial de Caen | 2 | 2 |
| `memorial_pegasus_aircraft.csv` | Mémorial Pegasus | 2 | 1 |
| `betheny_aeronautique_aircraft.csv` | Musée de l'Aéronautique Locale de Bétheny | 1 | 1 |
| `camping_haut_village_aircraft.csv` | Camping du Haut Village Aircraft, Saint-Michel-Chef-Chef | 1 | 1 |
| `concorde_fbvff_cdg_aircraft.csv` | Concorde F-BVFF, Paris-Charles de Gaulle | 1 | 1 |
| `douzy_sommer_aircraft.csv` | Musée des Débuts de l'Aviation Roger Sommer | 1 | 0 |
| `fismes_france40_aircraft.csv` | Musée France 40 Véhicules | 1 | 1 |
| `historial_vendee_aircraft.csv` | Historial de la Vendée | 1 | 1 |
| `lycee_jean_zay_jarny_aircraft.csv` | Lycée Jean Zay Jarny Instructional Airframes | 1 | 1 |
| `lycee_jully_saint_avold_aircraft.csv` | Lycée Charles Jully Saint-Avold Instructional Airframes | 1 | 1 |
| `meaux_grande_guerre_aircraft.csv` | Musée de la Grande Guerre du Pays de Meaux | 1 | 1 |
| `morlaix_fouga_monument_aircraft.csv` | Fouga Magister Monument, Morlaix Airport | 1 | 1 |
| `noratlas_les_mureaux_aircraft.csv` | Noratlas Monument, ArianeGroup Les Mureaux | 1 | 1 |
| `overlord_museum_aircraft.csv` | Overlord Museum | 1 | 1 |
| `potez_36_albert_aircraft.csv` | Potez 36 Monument, Gare d'Albert | 1 | 0 |
| `saint_cyr_coetquidan_aircraft.csv` | Musée de l'Officier, Académie Militaire de Saint-Cyr Coëtquidan | 1 | 1 |
| `thales_brest_super_etendard_aircraft.csv` | Super Étendard Monument, Thales Brest | 1 | 1 |
| `thiepval_historial_aircraft.csv` | Historial de la Grande Guerre - Musée de Thiepval | 1 | 1 |
| `utah_beach_aircraft.csv` | Musée du Débarquement Utah Beach | 1 | 1 |
| **Total** | **35 sites** | **227** | **197 (87 %)** |

Also written: `build_museums.py`, `acbuild.py`, `b_albert.py`, `b_canopee.py`, `b_rest1.py`, `b_rest2.py`, `b_rest3.py` — the generators, kept so the CSVs are reproducible.

---

## 8. Leads for other agents

**For whoever owns La Ferté-Alais (91):** two further collections share the aerodrome and are not the Amicale Jean-Baptiste Salis.
- *Aero Vintage Academy*, 91590 Cerny: Boeing PT-13D (N43SV/796), PT-17 (F-HIZI/55), Stearman PT-17 (N66557/533), NAF N3N-3 (N44877/707), P-51D (F-HTFM, ex NZ2427/23), T-6 (F-HLEA/55), T-28A Fennec (N14113, 17206/TL-206), Piper J-3 (NC91944), Travelair 4000 (NC4418).
- *Mémorial Flight*, aérodrome de Cerny-La Ferté-Alais: Blériot XI BL297, Stearman PT-13D 41-17601/64, FFVS J22 10/E, Fokker D.VII 4400, Fokker Dr.I 489/17, LVG C.VI 9041/18, Morane AI 1567/7, Polikarpov I-153 n°9, RAF S.E.2f 2560, S.E.5a C.1096/3, Sopwith 1½ Strutter 3214, SPAD XIII n°5.
- ARDHAN also puts Étendard IV M n°3 and n°9 with the Salis association, n°3 "exposé dans un parc" at Paray-Vieille-Poste near Orly, and MS 502 n°320 (F-AZCP) and Nord 1101 n°67 (F-GMCY) at La Ferté-Alais.

**For Bourgogne-Franche-Comté:** *Fort de l'OTAN / Fort Lefebvre*, Fort du Salbert, 90000 Belfort (`ouvrage-g.com`) — Mirage IIIE n°403 coded 13-QB. Not on the standard museum lists.

**For Nouvelle-Aquitaine / Occitanie / PACA:** ARDHAN's February 2025 census is a ready-made inventory for the naval airframes at Rochefort ANAMAN (~45 aircraft), the CAEA Bordeaux-Mérignac, the CHAN Nîmes, Ailes Anciennes Toulouse, Musée d'Orange, the Musée Castel-Mauboussin at Cuers, and Les Ailes de la Mer at Bayonne. It is at `aeronavale.org/wp-content/uploads/2025/04/1-Aeronefs-preserves-de-lA.N.-par-lieux-fevrier-2025.pdf` and it is dated and honest about doubt. Use it.

**Lycée airframes elsewhere in France** (ARDHAN, Feb 2025), same pattern as the five I recorded: Lycée Flora Tristan, Cenon/Camblanes (33) — Super Étendard n°12; Lycée Frédéric Mistral, Nîmes (30) — Super Étendard n°39 cockpit; Lycée Alexandre Denis, Cerny (91) — Super Étendard n°32; ECAUT Viuz-en-Sallaz (74) — Noratlas n°146, used as the school chapel since 1989.

**Other Noratlas monuments outside my area:** n°111 at the Quartier Soult, Tarbes (65); n°105 airworthy at Marseille-Provence with Noratlas de Provence, listed as a monument historique since 2006; n°191 and n°201 with Ailes Anciennes Toulouse.

**Method note for the rest of France:** `airhistory.net` was 403 throughout this session. If another agent can reach it, its "[Off-Airport]" browse is the tool that will actually enumerate the plinth population — the source I most wanted and could not use. Second choice: a Palissy query on `pop.culture.gouv.fr` for protected aircraft objects.

**Out-of-scope leads found:** none in the overseas départements.


---

# Research pass: the southern and eastern régions

# France — Southern & Eastern régions: monuments, small museums, oddities

Scope: Nouvelle-Aquitaine, Occitanie, Auvergne-Rhône-Alpes,
Provence-Alpes-Côte d'Azur, Bourgogne-Franche-Comté, Corse.

WORK IN PROGRESS — see bottom for final tables.

## The aerosteles.net sweep (done first, as the brief directs)

Method: pulled `https://www.aerosteles.net/liste-fr` (the complete French
index, 4,151 entries), parsed it by commune INSEE code, and selected every
entry whose commune lies in one of my 51 départements: **1,472 in-scope
entries**. Then fetched **1,458** of those 1,472 individual `stelefr-*`
pages (14 failed repeatedly — listed below) and text-scanned every one for
airframe-presence language (`socle`, `est exposé`, `préservé`, `gate guard`,
`avion gardien`, `le fuselage est`, `réplique`, `maquette`, `musée`, …).

**Result: 1,471 of the 1,472 in-scope aerosteles entries were rejected as
memorial stèles, plaques, crash-site markers or name-plaques with no
airframe.** The single entry that survived is `stelefr-stvictoret-musee`
(Saint-Victoret, 13) — and even that is only aerosteles recording the
*inauguration* of a municipal aviation museum, not an airframe of its own.

Representative rejects that look like airframes from the title but are not
(each individually read):
- `montauban-gazelle` / `caylus-gazelle` "Gazelle n° 4200" — crew memorial.
- `lons-noratlas`, `premian-n2501`, `blond-2501`, `tarbes-noratlas`,
  `saverdun-n2501`, `perillos-noratlas` "Noratlas n° NN" — all accident
  memorials to the crew of that Noratlas; no airframe.
- `stemaxime-flamant` "MD 312 Flamant n° 299" — two plaques and two crosses
  at a mountain crash site.
- `argeles-broussard`, `quenza-broussard`, `ancelle-broussard` — crash stèles.
- the whole `mdm-*` set (23 entries, Mimizan) — a "Mur du Souvenir", i.e. a
  wall of plaques for BA 118 / CEAM losses.
- `latestedebuch-mir4n5`, `latestedebuch-mir4n40`, `luxey-mirage4`,
  `pelussin-f1`, `laroque-paf`, `cros-lynx`, `stmicheldeuzet-vautour` — crash
  memorials for Mirage IV / Mirage F1 / Fouga / Mirage 2000N / Vautour.
- `cornebarrieu-noratlas` — a Noratlas **propeller** on a pillar (explicitly
  excluded by the brief), and it has since been moved.
- `pierrefeu-lancair` — the aircraft engraved on the stèle is, in the site's
  own words, "une licence artistique du graveur".

Conclusion recorded for the other agents: **aerosteles.net is a memorial
database, not a preserved-airframe database.** In these six régions it
yielded exactly one usable lead. All the actual plinth airframes below were
found through other channels.

The 14 pages that would not load (server 403/timeout after three retries;
their list-page titles were all person- or crash-shaped, so the loss is
unlikely to hide an airframe): cervione-340bg, parcader-statue1,
luxey-mirage4, aurieres-combegrasse, pau-neuneu, pau_5rhc, bron-mouillard,
challesleseaux-aerodrome, montauban-rsa, hyeres-aviation, orange-goumin,
vivonne-mosquito, champlay-b17, stmartindutertre-phare.


---

## Sources, and how much each was worth

| source | weight | what it gave / how it failed |
|---|---|---|
| **aerosteles.net** | near zero for airframes | 1,472 in-scope entries fetched and read; **1,471 rejected as plaques with no aircraft** (see section above). One usable lead. |
| **ARDHAN, *Aéronefs de l'Aéronautique navale préservés par lieux*, February 2025** (PDF at aeronavale.org) | very high | The single best French source found. Dated, location-organised, honest about doubts. Gave Saint-Victoret, Orange, Cuers, CELAG, Tarbes, Bayonne, Saint-Yan, Niort, the Rochefort Alizé, the Fréjus Étendard and the lycée airframes. |
| **kosmonavtika.com ("Où sont-ils ?", Nicolas Pillet)** | very high | Per-type survivor tables with photographs and a "dernière mise à jour" date on each site page — the best currency evidence available without a site visit. Supaéro pages updated 9 March 2026; Saix 10 July 2026; Aérocampus 23 January 2025. Museum-biased: it under-reports roadside airframes. |
| **French Wikipedia per-type "Appareils préservés"** | high as leads | Nord 2501, Caravelle, Mirage III, Mirage F1 lists were rich and mostly accurate; every entry used here was re-checked against a second source. |
| **The site's own page** (musee-a5e.com, musee-aviation-saint-victoret.fr, aeroretro.fr, ailes-anciennes74.com, ecaut.com, lesurplus.fr, noratlas-de-provence.com) | decisive for "what is here now" | Used in preference to every list when they disagreed. |
| **Local press and municipal sites** | decisive for monuments | ville-frejus.fr, ville-rochefort.fr, L'Hebdo 17, zoomdici.fr, France 3 Côte d'Azur. These are what proved the Fréjus Étendard had moved and the Loudes Fouga had come back. |
| **airhistory.net** | unusable | Cloudflare-blocked from this environment on every attempt, including the collection and off-airport listings. A human with a browser should re-run the "[Off-Airport] France" sweep — it is the one taxonomy that maps exactly onto roadside airframes and I could not read it. |
| **aviationmuseum.eu** | medium, stale | Gave the only itemised CELAG inventory found (14 helicopters, page dated 16 January 2016). Its France index is broken and lists one museum. |

## Corrections made, with the evidence

- **Étendard IV-M n°29, Fréjus — moved.** ARDHAN (February 2025) still puts it "en front de mer près de l'ancienne BAN, état dégradé". The Ville de Fréjus's own news item records it being craned off the Base Nature on **16 June 2022** and taken to the SDIS Var fire station on the rue des Batteries, where a Dassault MD 315 Flamant already stood. Recorded at the fire station, with a second airframe found in the process.
- **Musée de l'Aviation du Mas Palégry, Perpignan (66) — gone.** Still listed on French Wikipedia's *Liste de musées aéronautiques*. The Charles Noetinger collection (MS.733 Alcyon, Fouga Magister, a dismantled but complete Vampire, an RF-84F Thunderflash, an MH.1521 Broussard, a Caudron C.800, a Wassmer Bijave, a Mignet-Boyer Pou-du-Ciel prototype and a Mystère IVA cockpit) was **dispersed at auction by Osenat on 1 June 2019**. Excluded. Where those nine airframes went is the single biggest open lead in these six régions.
- **Super Étendard Modernisé n°12 — two addresses.** ARDHAN puts it at the Lycée Flora Tristan, Camblanes-et-Meynac; Pillet puts it at Aérocampus Aquitaine, Latresne — neighbouring communes. ARDHAN itself says its lycée list "demanderait à être actualisée" and has no photographs of those aircraft, while Pillet has a dated photograph from January 2025. Recorded at **Aérocampus**, with the conflict stated in the row's description.
- **Le Surplus, Portes-lès-Valence — two airframes, one source each.** The shop's own *Avions* page (2025) names only the Fouga CM.175 Zéphyr n°18. Pillet's Mirage 5 register has a photographed page for a Mirage 5BR n°07 at Portes-lès-Valence. Both recorded, the Mirage flagged as needing a look.
- **Noratlas n°78, Uchaud (30) — scrapped** about 2023 after lying in pieces since the 1990s. Not recorded; noted here so the next researcher does not chase it.
- **CELAG's Sikorsky H-34/HSS — sold.** The 2016 aviationmuseum.eu inventory lists H-34A "SA177/F"; ARDHAN records that CELAG sold the H-34/HSS to a private owner in the Puy-de-Dôme in 2022 (and that it was resold in 2023 to a campsite owner at Saint-Michel-Chef-Chef in the Loire-Atlantique, who turned it into holiday accommodation). Dropped from the CELAG file. **That campsite helicopter is a live lead for the Pays de la Loire agent.**
- **caea.info is dead.** The Conservatoire de l'Air et de l'Espace d'Aquitaine's old domain now resolves to a domain-auction parking page; its content has moved to caea.fr / c-aea.fr. Relevant to whoever owns Mérignac.

## Judgment calls

- **Where the boundary with the "bases" agent was drawn.** Excluded: anything standing inside an active Armée de l'Air et de l'Espace, Aéronavale or ALAT installation, plus the state technical and training establishments that behave like one — AIA Cuers (Super Étendard n°16, Crusader n°37, Lynx n°264), CELAE Cuers, EPPE and ETAN Hyères, EFSOAA/BA 721 Rochefort, EETAA 722 Saintes, DGA Toulouse, BA 115 Orange's own museum, BA 118's Espace Rozanoff, and the École des Pupilles de l'Air at Montbonnot-Saint-Martin (Mirage IIIR n°349). **Included** where the unit is an *army* one and the aircraft stands at the gate as decoration: the Noratlas at the Quartier Soult in Tarbes (35e RAP), at the 1er RCP in Pamiers and at the Camp de Caylus. These three are the likeliest points of overlap with another agent.
- **ANAMAN / Musée de l'Aéronautique navale, Rochefort (17) is NOT in these files.** It sits in Nouvelle-Aquitaine and is not on my exclusion list by name, but it occupies the Dodin and Saint-Trojan hangars on BA 721 Rochefort, so it falls under "any Armée de l'Air / Aéronavale / ALAT base display". It holds roughly forty airframes (Alizé, Alouette II and III, Aquilon n°53, Broussard, Caudron C.800, C-47, Crusader n°11, D.520 n°650, Étendard IV M and P, H-21, HSS, Jaguar M 05, Lynx, MD 312, MS.733, MS.760, Navajo, Neptune, N.262, PBY Catalina, Rallye, SNB-5, Stampe, Super Étendard, Super Frelon, T-6, Zéphyr). **If no other agent has claimed it, it is the largest single gap in Nouvelle-Aquitaine and someone must take it.**
- **Airworthy collections were included** when the aircraft live in a hangar a visitor can arrange to see: AéroRétro at Saint-Rambert-d'Albon, Le Noratlas de Provence at Marseille-Provence, the Escadrille du Souvenir at Niort. `display_status` is still the visitor's view, so aircraft the association itself describes as under restoration are `under_restoration`.
- **Replicas are recorded but said so in `description`**: the Henri Fabre *Canard* at Saint-Victoret and the Santos-Dumont *Demoiselle* at AéroRétro are reproductions, not original airframes.
- **Sections only, said so in `description`**: the CL-215 cabin n°1029 at Saint-Victoret, the Super Étendard n°14 and Crusader cockpits at Bayonne, the Super Étendard n°39 cockpit at the Lycée Frédéric Mistral, Nîmes.
- **`access_type`.** `public` for anything on a road, roundabout, seafront or open school forecourt; `appointment` for association hangars with published visiting arrangements (AéroRétro, CELAG, CHAN-Nîmes, Castel-Mauboussin, Noratlas de Provence, Caravelle Guyane, Aérocampus); `restricted` for the ISAE-SUPAERO campus and the two army sites at Pamiers and Caylus.
- **`latitude`/`longitude` left blank almost everywhere.** Only three sites have a published coordinate I trust: Saint-Victoret (from aerosteles), Rochefort's rond-point Albert-Bignon (from the town's own equipment register) and Le Versoud (from aviationmuseum.eu). Everywhere else a correct code postal is the better record; no pin was guessed.
- **`year_built` is blank on every row but one line of prose.** Not one of these sources publishes a build date I could stand behind; serial numbers were never promoted into that field.

## Blank fields left deliberately

- **31 of 136 aircraft rows have no `tail_number`** (77% serial coverage). The gaps are concentrated in exactly the places you would expect: roadside Fouga Magisters (Loudes, Saint-Dalmas-de-Tende, Salon-de-Provence, Saint-Victoret) whose owners are councils that never published a serial; the Saint-Victoret helicopter hall, where the museum writes type histories rather than airframe histories; and the AéroRétro restoration shop. In every case the row's `description` says the serial was not published rather than leaving the reader guessing.
- The Alouette III at the Musée Aéronautique d'Orange appears in the museum's own aircraft index but has no page and no serial anywhere.
- The Eurocopter X3 at Saint-Victoret is a one-off demonstrator; a registration is widely quoted but I could not confirm it from the museum or a registry, so the field is blank.

## Excluded, and why — by name

| site | why |
|---|---|
| Musée de l'Aviation du Mas Palégry, Perpignan (66) | Collection auctioned off 1 June 2019; museum gone. |
| Musée Air Mémorial Creusois / Maison Chevanne, Bellegarde-en-Marche (23) | Models, photographs and 400 aviator biographies. **No airframe.** |
| Aérothèque, Blagnac (31) | Archive and models; its aircraft went to Aeroscopia. **No airframe of its own.** |
| Musée de l'Automobiliste, Mougins (06) | Listed with a Blériot XI (G-BLXI) on a page last updated in 2009; the museum has since changed hands and I could not confirm any airframe. Not recordable. |
| Musée de l'Aéronautique navale (ANAMAN), Rochefort (17) | On BA 721 — see the judgment call above. **~40 airframes; needs an owner.** |
| AIA Cuers (83), CELAE Cuers, EPPE Hyères, ETAN Hyères, BAN Hyères "pots de fleurs" | State military-industrial and naval-base sites, no public access. |
| EFSOAA / BA 721 Rochefort (17); EETAA 722 Saintes (17); DGA Toulouse (31) | Military training and procurement establishments. |
| Musée de la BA 115, Orange (84); Espace Patrimonial Rozanoff, BA 118 Mont-de-Marsan (40); Musée de la BA 709 Cognac (17); BA 126 Solenzara (2A) | Air-base displays. |
| École des Pupilles de l'Air 749, Montbonnot-Saint-Martin (38) — Mirage IIIR n°349 | Armée de l'Air school. |
| Crusader F8E(FN) n°34, Lons-le-Saunier (39) | In a closed hangar on the aerodrome, possibly sold to the USA; not visitable. |
| Nord 1002 n°90, Montélimar-Ancône (26) | Dismantled in a private hangar. |
| Étendard IV M n°60, Espalion (12); MS.733 n°189, Montpellier (34); Stampe n°531, Issoire (63); Stampe n°1030, Cannes-Mandelieu (06); Rallye n°86, Ceyzériat (01); Rallye n°87, Montluçon-Domérat (03) | Privately owned single aircraft with no public access and no published visiting arrangement. Listed here as leads. |
| Noratlas n°78, Uchaud (30) | Scrapped c. 2023. |
| Musée mémorial des parachutistes, Lons/Pau (64) | Its Noratlas connection is a memorial stele to the crew of Noratlas n°49, not an airframe. |
| All aircraft at Aeroscopia, Ailes Anciennes Toulouse, MEAC Montélimar, Savigny-lès-Beaune, Biscarrosse, CAEA Mérignac, Musée de l'ALAT Dax, Lyon-Corbas, Cité de l'espace | Assigned to other agents. The one exception is the **Mirage IIIB n°233 on the Montélimar roundabout**, which belongs to MEAC but stands a kilometre from it on the RN7 and is recorded here as its own site. |

## Corsica — a documented blank

Corse produced **no records at all**, and that is a finding rather than an omission. Twenty-seven aerosteles entries fall in Corse-du-Sud and Haute-Corse; every one is a crash or crew memorial (the Caravelle Ajaccio-Nice, the DC-9 Inex-Adria at Petreto-Bicchisano, Broussard n°272 at Quenza, the Mirage 2000 stele at Bonifacio, Tracker T3 at Calenzana). Nicolas Pillet's survivor registers list not one Corsican location for any French jet type; ARDHAN's February 2025 census lists none; the Caravelle and Noratlas survivor lists list none. The only military aviation site on the island is **BA 126 Ventiseri-Solenzara**, which is excluded. If an airframe is preserved on Corsica it is at an aeroclub (Ghisonaccia-Alzitone, Propriano, Corte) and is not on the open web; it needs a person on the ground.

## Ranked "needs a human on site"

1. **Where did the nine Mas Palégry aircraft go after the 1 June 2019 Osenat sale?** Nine real airframes, including an RF-84F and a complete Vampire, vanished from the record in one afternoon. The auction catalogue (Osenat lot list 98668) names buyers' lots and is the thread to pull.
2. **Does anyone own ANAMAN Rochefort?** Forty airframes, and my exclusion rule is the only reason they are not in this file.
3. **Is the Mirage 5BR n°07 still at Le Surplus, Portes-lès-Valence?** The shop's own 2025 page names only the Zéphyr. Two minutes from the A7.
4. **Serials for the four unmarked roadside Fouga Magisters** (Loudes, Saint-Dalmas-de-Tende, Salon-de-Provence, Saint-Victoret). All four are reachable and the number is usually stencilled on the fin or the nose leg.
5. **Corsica**, as above — one visit to Ghisonaccia and Propriano would settle it.
6. **The three extra aircraft kosmonavtika puts at the Musée Aéronautique d'Orange** that the museum's own index does not list: Jaguar E n°7, Mirage F1CR n°636, Mirage 2000N n°349. Either recent arrivals the association has not put on the website, or errors. I followed the museum and left them out.
7. **Mirage 5 n°10 at "Orange", not the museum.** Pillet's Mirage 5 register has a separate photographed page for it. It is somewhere in or around Orange and I could not place it — possibly a second roundabout, possibly the BA 115 gate.
8. **CELAG, Le Versoud.** The whole thirteen-aircraft file rests on a 2016 inventory plus ARDHAN's 2025 confirmation of one airframe. The association reorganised for lack of money and its own site has not been updated since 2019. Someone should go on a Saturday afternoon and count.

## Leads for other agents

- **ANAMAN / Musée de l'Aéronautique navale, Rochefort (17)** — see above. Nouvelle-Aquitaine or "bases", but somebody.
- **Sikorsky H-34 painted as HSS-1 n°177** — sold by CELAG in 2022, resold in 2023 to a campsite owner at **Saint-Michel-Chef-Chef (44)** and converted into "hébergement insolite". A Pays de la Loire record.
- **Caravelle VI-N F-BYCY (c/n 233) at Xertigny (88)**, in Denis Duchêne's private collection, converted to bed-and-breakfast rooms — Grand Est.
- **Noratlas n°202 at the ArianeGroup site, Les Mureaux (78)** — Île-de-France.
- **Noratlas n°160**, fully restored at Morbihan Aéro Musée, Vannes-Meucon (56) — Bretagne.
- **Étendard IV M n°01** left Rochefort for the Musée de l'Épopée de l'Industrie et de l'Aéronautique at **Albert (80)** in 2025; **Lynx n°03 and Zéphyr n°24** went the same way — Hauts-de-France, and the Albert list needs updating for all three.
- **Étendard IV M n°3, parc Gaston Jankiewicz, Paray-Vieille-Poste (91)** — a town park with a fighter in it. Île-de-France.
- **Mirage F1C n°101 on a pylon at Les Andelys (27)** since 2008 — Normandie.
- **`caea.info` is dead**; CAEA content is now at caea.fr and c-aea.fr. Whoever has Mérignac needs the new domain.
- **airhistory.net is Cloudflare-blocked from this environment.** Whoever can reach it should run the "[Off-Airport] France" listing; it is the one source that would systematically catch the roadside airframes that neither aerosteles nor Pillet records.
- **Overseas départements** (out of scope, noted as the brief asks): ARDHAN records Alouette III n°303 with Air Formation at **Tahiti-Faa'a**, and a Nord 262 fleet formerly at Châteaudun. Nothing else surfaced.

## File and row counts

| file | rows | with serial |
|---|---|---|
| `aerocampus_aquitaine_latresne_aircraft.csv` | 3 | 3 |
| `aeroretro_saint_rambert_dalbon_aircraft.csv` | 17 | 11 |
| `ailes_anciennes_haute_savoie_aircraft.csv` | 3 | 3 |
| `alize_rond_point_avion_rochefort_aircraft.csv` | 1 | 1 |
| `caravelle_guyane_avignon_aircraft.csv` | 1 | 1 |
| `celag_grenoble_le_versoud_aircraft.csv` | 13 | 13 |
| `chan_nimes_aircraft.csv` | 2 | 2 |
| `chapelle_noratlas_ecaut_viuz_en_sallaz_aircraft.csv` | 1 | 1 |
| `collection_castel_mauboussin_cuers_aircraft.csv` | 4 | 4 |
| `escadrille_du_souvenir_niort_aircraft.csv` | 4 | 4 |
| `etendard_flamant_caserne_batteries_frejus_aircraft.csv` | 2 | 1 |
| `fouga_magister_monument_loudes_aircraft.csv` | 1 | 0 |
| `fouga_magister_monument_salon_de_provence_aircraft.csv` | 1 | 0 |
| `fouga_magister_saint_dalmas_de_tende_aircraft.csv` | 1 | 0 |
| `heritage_avions_morane_saulnier_tarbes_aircraft.csv` | 1 | 1 |
| `isae_supaero_mirage_iii_toulouse_aircraft.csv` | 2 | 2 |
| `le_surplus_portes_les_valence_aircraft.csv` | 2 | 2 |
| `les_ailes_de_la_mer_bayonne_aircraft.csv` | 2 | 1 |
| `lycee_frederic_mistral_nimes_aircraft.csv` | 1 | 1 |
| `mirage_f1_gate_guard_avignon_aircraft.csv` | 1 | 1 |
| `mirage_iii_chateau_pas_de_loup_saix_aircraft.csv` | 1 | 1 |
| `mirage_iii_monument_montceau_les_mines_aircraft.csv` | 1 | 1 |
| `mirage_iii_monument_montelimar_aircraft.csv` | 1 | 1 |
| `mirage_iii_monument_orange_aircraft.csv` | 1 | 1 |
| `musee_aeronautique_orange_aircraft.csv` | 34 | 33 |
| `musee_aviation_saint_victoret_aircraft.csv` | 29 | 11 |
| `natura_lodge_cessna_barjac_aircraft.csv` | 1 | 0 |
| `noratlas_1er_rcp_pamiers_aircraft.csv` | 1 | 1 |
| `noratlas_camp_de_caylus_aircraft.csv` | 1 | 1 |
| `noratlas_de_provence_marseille_aircraft.csv` | 1 | 1 |
| `noratlas_quartier_soult_tarbes_aircraft.csv` | 1 | 1 |
| `nostalgic_aero_saint_yan_aircraft.csv` | 1 | 1 |
| **total (32 aircraft files)** | **136** | **105 (77%)** |

Serial coverage: **105 of 136 aircraft rows carry a tail number (77%)**.
Sites: **32**, in one museums file (`fr_museums.csv`) plus 32 per-site aircraft
files. By région: Provence-Alpes-Côte d'Azur 10, Occitanie 9,
Auvergne-Rhône-Alpes 7, Nouvelle-Aquitaine 4, Bourgogne-Franche-Comté 2,
Corse 0.
