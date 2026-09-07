# World's-largest batch 3 — Duxford, Evergreen, Le Bourget, Monino

Closes out the world's-largest list. Each directory holds the raw research
output (`*_raw.txt`, kept for audit) and the built CSV.

| Museum | id | File | Rows | Tails |
|---|---|---|---|---|
| Imperial War Museum Duxford | 34 | `england/duxford_aircraft.csv` | 114 | 113 (99%) |
| Evergreen Aviation Museum | 49 | `oregon/evergreen_aircraft.csv` | 107 | 94 (87%) |
| Musée de l'Air et de l'Espace | 36 | `france/musee_de_lair_aircraft.csv` | 170 | 42 (24%) |
| Central Air Force Museum, Monino | **new** | `russia/monino_aircraft.csv` | 132 | 105 (79%) |

Monino needs its museum record first — `russia/ru_museums.csv`. Import Russia
last, and museums before aircraft as always.

## Two builder bugs this batch exposed

**Dedupe was keyed on tail alone.** That was fine while every tail was a
globally unique USAF serial. Then Monino arrived with painted bort numbers —
"01" on a MiG-9, a MiG-17, a Tu-4 and an An-14 — and Le Bourget with four
Dassault prototypes all numbered "01", and the dedupe silently threw away 39
real aircraft. It now keys on `(model, tail)`, which is the database's own
unique index. Covered by `tests/test_research_builder.py::TestCrossSliceDedupe`.

**The untailed-duplicate test was too strict.** Monino has two I-16s and two
Po-2s with no published borts. A museum owning two of a type is normal; the
hazard is two rows identical in *every* field. The test now allows rows that
differ in aliases or description.

## Sources and serial coverage

- **Duxford, 99%.** UK serials are exhaustively documented (ukserials, ABPic,
  G-INFO). Note that a large share of Duxford's aircraft are **privately
  owned and airworthy** — The Fighter Collection, Aircraft Restoration
  Company, Historic Aircraft Collection, B-17 *Sally B* — and may be away at
  airshows. Each is tagged `airworthy` in aliases; the G- registration is in
  aliases with the military serial as the tail.
- **Evergreen, 87% — but almost entirely from a registry.** The museum's own
  site publishes almost no serials; nearly every identifier came from
  aerialvisuals.ca's location dossier. That dossier also tracks what *left*
  during the 2014–2018 bankruptcy, which is how the stale Wikipedia entries
  were excluded. The museum has since rebranded as the North American
  Aerospace Museum. Bare FAA numbers from the registry were given their N-
  prefix.
- **Le Bourget, 24% — the honest number.** The museum publishes registrations
  for its airliners and prototypes and inventory numbers ("Inv 57") for its
  pioneers, but no serial for most of the military collection. Inventory
  numbers are in aliases, not the tail column. `in_storage` follows the
  museum's own "Non exposé actuellement" tag — 69 items, including several
  that English Wikipedia still lists as on the tarmac.
- **Monino, 79%.** Painted bort numbers, from `aviamuseum.ru` (the museum's
  volunteer organisation, which publishes a full roster by design bureau with
  hangar locations). Bort numbers are only unique within a type, which the
  `(model, tail)` index accommodates. Where two of one type share a bort
  (both Tu-22Ms are "33") the tails are blank and the bort is in aliases.
  The museum is **confirmed open at Monino** as of August 2026; the
  2016–2018 Patriot Park relocation never happened.

## Corrections from the pre-import audit

Applied at source:

- Duxford **Hurricane R4118 is a Mk I**, not XII (Wikipedia has the same error).
- Duxford's four FAA helicopters (Wessex, Whirlwind, Sea King, Wasp — all
  **HAS** marks) were `search_rescue`. HAS is anti-submarine; now `recon`,
  matching the S-2 Tracker.
- The **AT-16** is a Noorduyn-built Harvard, not North American.
- P-40C is a **Tomahawk**; Warhawk applies from the D onward.
- Spitfire PT462 is a **two-seat T.9** conversion, like PV202.
- Phantoms now use one convention: `F-4` + `M`, with FGR.2 as an alias.
- Monino's Ye-152 is the **Ye-152M** (exhibited as Ye-166); the A does not
  survive. The Yak-141's tail held the type number; its painted bort is 77.
  The Mi-2SKh's "20869" is CCCP-20869 with the prefix dropped.
- Evergreen's Hughes 500C carried **N110035**, which is not a valid US
  registration. It's a character away from the 369D's N11035 — possibly the
  same airframe twice. Tail blanked pending a check.
- Le Bourget's Caudron and Farman families were split as `model="G"` +
  `variant="3"`; a letter alone is not a model. Now `G.3`, `C.635`, `MF.7`,
  `F.60` and so on.

## Uncertain, flagged rather than guessed

- **Monino MiG-25R (02) and MiG-25RB (25)** — the published inventory lists
  only an R and a PD. May be one airframe under two names.
- **Monino's two Mi-24Vs** (46, 44) — the inventory lists one V plus an Mi-25
  export variant. One of these is probably the Mi-25.
- **Monino's two I-16s and three Po-2/U-2s** — kept as the volunteer roster
  lists them, in different hangars, but not independently confirmed.
- **Le Bourget's Atar Volant and Ludion** are wingless VTOL test rigs forced
  into `fixed_wing` / `monoplane` because the schema has nothing better.
- **Duxford Beaufighter JM135** is a composite of four airframes; **Victor
  XH669** is a cockpit section only. Both noted in aliases.

## Known gaps, not researched this pass

- Duxford: HS Trident 2E G-AVFB.
- Monino: Bell P-63, Douglas A-20G, two Li-2s, Aero L-29, Mi-1, the Yak-11/
  12/18/50/52 group, BI-1 replica. The A–M pass excluded Lend-Lease types as
  out of scope; the N–Z pass then confirmed they're there.
- Le Bourget: Dassault Balzac V; the Eurocopter X3 left for Saint-Victoret
  in 2017.

## Cross-museum, verified distinct

SPAD XIII at Duxford (replica) and Le Bourget (original fuselage); Voisin LAS
at Le Bourget and Monino. Different airframes, no shared identifiers.
