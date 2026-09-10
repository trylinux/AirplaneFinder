# New South Wales and the Australian Capital Territory — research notes

Output: `/home/claude/anz/nsw_act/`

- `nsw_act_museums.csv` — 24 sites (all NSW; no new ACT site was created, see §6)
- 24 `<site_slug>_aircraft.csv` files — 241 airframes
- `awm_topup_aircraft.csv` — 40 airframes added to the pre-existing
  `Australian War Memorial` record (the Mitsubishi A6M Zero already in the database
  is deliberately **not** repeated)

Total 281 aircraft rows across 25 aircraft CSVs.

Research window: September 2026. Every ADF airframe was checked against
ADF-Serials before being placed.

---

## 1. Sources used, and how they behaved

**Primary / authoritative**

- **ADF-Serials (`adf-serials.com.au`)** — the backbone of this survey. Its
  per-serial pages carry a disposition narrative that usually ends with a current
  location, and it is the only source that reliably distinguishes near-identical
  serials. It was used to build the whole gate-guard and plinth sweep: the RAAF
  Series 2 and 3 type pages (`2a77` Meteor, `2a79` Vampire, `2a84a/b` Canberra,
  `2a85` Winjeel, `2a89` Neptune, `2a92` Jindivik, `2a94` Sabre, `2a65` Dakota,
  `3a1` Sioux, `3a2` Iroquois, `3a3` Mirage, `3a4` Caribou, `3a7` Macchi,
  `3a8` F-111, `3a9` Orion, `3a15` Chinook, `3a17` Kiowa, `3a18` Nomad,
  `3a20` Boeing 707, `3a21` Hornet, `3a22` Squirrel, `3a23` PC-9,
  `2a97` Hercules) and the RAN pages (`n1` Firefly, `n2` Dakota, `n3` Gannet,
  `n4` Sea Venom, `n7` Wessex, `n8` Scout, `n12` Tracker, `n13` Skyhawk,
  `n16` Sea King, `n24` Seahawk) were downloaded and every record containing a
  NSW/ACT place name plus a disposition verb was read. This is what produced
  Forbes, Corowa, Wingham, Mulwala, Moree, Nyngan, Woolgoolga, Holsworthy,
  Singleton, the Nowra bridge Iroquois and the Wagga pole Vampire — none of
  which appear on any museum list.
  Its weakness is currency: many entries end at a 2012–2019 sighting.
- **Museum websites** — `hars.org.au`, `aviationmuseum.com.au` (Temora),
  `fighterworld.com.au`, `ehham.org.au` (Evans Head),
  `camdenmuseumofaviation.com.au`, `narromineaviationmuseum.org.au`,
  `awm.gov.au` gallery pages. Australian museums publish *type* lists readily and
  *serial* lists almost never. HARS's own "flying aircraft" and "static aircraft"
  pages name 15 and 16 types respectively with exactly one registration between
  them (VH-OJA). Temora's collection page names 14 types and no serials at all.
  They were therefore used for **currency** (is this type still here?) and the
  serials came from elsewhere.
- **`airforce.gov.au`** — the RAAF Wagga Heritage Centre "Display Aircraft" page
  is blocked to automated fetching (robots and an HTTP/2 reset), so the Wagga
  inventory below is reconstructed from ADF-Serials plus a 2014 walk-round.

**Survey / enthusiast**

- **`aviationmuseum.eu`** — the only source with serial-by-serial inventories for
  HARS, the Fleet Air Arm Museum, Camden, Narromine, the Powerhouse, HARS Parkes
  and RAAF Wagga. Its inventories are two-column HTML tables, and the two columns
  are **not always aligned** (see §2). It is also demonstrably stale in places and
  contains cross-page contamination (§2).
- **Aviation Spotters Online** — a November 2017 walk-round of the Fleet Air Arm
  Museum with serials; used to corroborate the FAAM list.
- **Vintage Aviation News** — the September 2023 "Big Things in Store" report from
  the AWM's Treloar Technology Centre (the single most useful currency evidence
  for the AWM), the July 2019 Temora gift announcement, the January 2026 RAAF
  heritage fleet review, the February 2026 arrival of Orion A9-752 at Evans Head.
- **ABC News (31 July 2025)** for the return of Lancaster W4783 to the Memorial.
- Wikipedia and `grubby-fingers-aircraft-illustration.com` were treated as leads
  only; both proved wrong on serials (§2).

---

## 2. Corrections made, with evidence

1. **Meteor at Fighter World is A77-875, not A77-851.** `fighterworld.com.au`
   labels its Meteor "A77-851". ADF-Serials shows A77-851 was converted to a U.21A
   and struck off in 1964, with only its cockpit surviving at the South Australian
   Aviation Museum, while **A77-875** went from RSTT Wagga to Williamtown for
   display in April 1966 and is the airframe Fighter World restored — in the
   markings of **A77-881**, the 77 Squadron display aircraft. Recorded as A77-875
   with `A77-881` in aliases.
2. **Temora's Meteor is VZ467, not A77-851.** Same clash. VH-MBX is ex-RAF VZ467,
   "Winston", the last F.8 in RAF service, painted as A77-851. `tail_number`
   VZ467, false serial `A77-851` in aliases, both facts in `description`.
3. **The AWM's Wessex is N7-216, not N7-226.** `aviationmuseum.eu` lists
   "Westland Wessex N7-226 (WA226)" in AWM storage. ADF-Serials: N7-226 is *on
   display at the Fleet Air Arm Museum*; N7-216 went from the Australian National
   Maritime Museum to the AWM in 2019, replaced at the Maritime Museum by Seahawk
   N24-006. Both aircraft are now recorded, in the right places.
4. **Sea Fury WG630 and MiG-15UTI "607" are at HARS, not the FAAM.** They appear
   on both `aviationmuseum.eu` pages. HARS's own static-aircraft page lists a Sea
   Fury, a MiG-15, a MiG-17 and a MiG-21; and Vintage Aviation News / Warbirds
   Online document the Sea Fury WG630 refurbishment *at HARS*. Placed at HARS,
   removed from the FAAM file. (The AWM's Sea Fury is a different airframe,
   VX730.)
5. **Firefly WJ109 is at the FAAM, not in AWM storage.** ADF-Serials: Nowra gate
   guard 1965–72, restored by volunteers from 1973, displayed as 207/K then 238/K.
   Removed from the AWM list.
6. **The AWM's Pfalz is a D.XII, 2600/18.** `aviationmuseum.eu` says "Pfalz D.XIII
   2600/13". The September 2023 Treloar open-day report gives D.XII 2600/18.
7. **The AWM's S.E.5a is recorded as A2-4**, per the same Treloar report;
   `aviationmuseum.eu` gives the RAF identity D6950. Both are carried (A2-4 as
   `tail_number`, D6950 as an alias) and the conflict is stated in `description`.
8. **Catalina VH-ASA belongs to the Powerhouse Museum, not HARS.** It is
   Sir Patrick Gordon Taylor's *Frigate Bird II*. The HARS survey row
   "Boeing PB2B-2 Catalina VH-ASA" is a duplication error and that row was
   **dropped** from the HARS file rather than given a fabricated identity.
9. **The `aviationmuseum.eu` HARS table is misaligned in rows 13–18.** Its
   registration column runs `– / VH-KFL / A20-99 / (VH-EAD) A85-435 /
   A94-901 / A7-030` against types `Clancy Skybaby / CA-3 Wirraway /
   CA-25 Winjeel / CA-27 Sabre / CA-28 Ceres / CA-30 (MB-326H)`. Type-consistency
   fixes four of them (A85-435 = Winjeel, A94-901 = Sabre, A7-030 = Macchi) but
   leaves the Wirraway, Skybaby and Ceres unresolved — and the same page's own
   photo caption calls the HARS Wirraway "CA-16 A20-458", while ADF-Serials puts
   A20-99 at Mildura. **The Wirraway, Skybaby and Ceres rows therefore carry no
   `tail_number`.** VH-KFL is left unassigned. Blank beats a guess.
10. **Vampire A79-822 is no longer at Fighter World.** `aviationmuseum.eu` lists
    it there; ADF-Serials records severe fuselage-pod deterioration noted in
    November 2010, after which it was dismantled and sent to the RAAF Amberley
    Aviation Heritage Centre. Excluded from the Fighter World file.
11. **Vampire A79-642 is at Temora, not Camden.** It was at Camden until August
    2000, then acquired by Temora to support A79-617. Moved. Cockpit A79-648 is
    explicitly *not* at Camden (ADF-Serials calls that report an error) and is
    excluded.
12. **Winjeel A85-364 (the CA-22 prototype) is at RAAF Wagga, not the FAAM.**
    Relocated to the RAAF Base Wagga Aviation Heritage Centre in 2020.
13. **Meteor A77-878 left the FAAM in February 2018** for RAAF Amberley. It is
    kept in the FAAM file only as a `in_storage` row flagged in `description` as
    departed — see §5 for why it was not silently deleted.
14. **The 2014 RAAF Wagga gate-guard list is out of date.** Of its five aircraft,
    Winjeel **A85-403** went to RAAF Base Townsville and Sabre **A94-982** went to
    Point Cook in September 2018; its intended replacement A94-910 was gifted to
    ANAM Moorabbin in May 2018. So there is probably **no Sabre at Wagga now** —
    the Wagga file contains no Sabre. Added since 2014: Mirage A3-51 (September
    2018), Macchi A7-004 as gate guard (November 2018), Winjeel A85-364 (2020),
    plus F-111C A8-142 (June 2012) which the 2014 article said was not yet public.
15. **Hudson serial.** Wikipedia gives Temora's Hudson as A16-211 and its
    Spitfire VIII as A58-602. The 2019 gift schedule and the survey inventories
    both give **A16-112** and **A58-758**; those are used, with the conflict noted
    in the row.

---

## 3. Judgment calls

- **Airworthy collections are recorded.** HARS's flying fleet (Connie VH-EAG,
  Catalina A24-362, Neptune A89-273, Orion A9-753, Caribou A4-210, the Dakotas,
  Southern Cross replica) and Temora's flying fleet are museum-owned or
  Commonwealth-owned collection aircraft on public display, and are marked
  `on_display` with the airworthy status in `description`.
- **Temora's ownership split.** Eleven aircraft were gifted to the Commonwealth on
  1 July 2019 but stayed at Temora on public display. The **January 2026 RAAF
  heritage fleet review** then withdrew eight types: Vampire, Meteor, A-37,
  Ryan STM-S2 and Canberra **returned to the museum**; Hudson, both Spitfires,
  Boomerang, Wirraway and Tiger Moth **continue flying at Temora**; the Sabre, the
  CT-4A and the RE8 were listed for "consideration for static display at approved
  heritage institutions". Nothing moved to the RAAF Museum at Point Cook from
  Temora — Point Cook's five continuing aircraft (Mustang, Harvard, Winjeel, Tiger
  Moth, Sopwith Pup) were already there. Sabre A94-983 is recorded at Temora,
  where ADF-Serials last places it, with the pending decision stated in the row.
- **Replicas** are recorded with the replica status in `description` and never in
  aliases: Fighter World's Fokker Dr.I, Sopwith Camel, Spitfire Mk VIII (as
  A58-429/QY-V) and Mk IX and its Bf 109; the FAAM's Sopwith Pup N5182 and
  Hargrave box kite; HARS's Southern Cross VH-USU; Narromine's Wright Model A.
- **Access types.** `public` for the aerodrome museums, the RAAF Wagga heritage
  centre (it sits in the original 1940 guardhouse *outside* the wire, free
  admission, Sat–Thu) and the roadside/RSL monuments. `restricted` for HMAS
  Albatross gate guards, Holsworthy Barracks, the Army Infantry Museum inside
  Lone Pine Barracks, and the **Camden Museum of Aviation**, whose own website
  states it is "currently closed to the public" with "no plans to re-open".
  Fighter World is on Medowie Road at the Williamtown base boundary and is
  reached without a base pass — `public`.
- **Section-only airframes were recorded when they are the museum's exhibit**
  (Camden's Lincoln, Beaufighter and Canberra cockpits; the FAAM's FB-111A and
  Tracker forward fuselages; HARS's 707-338C forward fuselage; the AWM's C-130H
  flight deck; Fighter World's Mirage A3-97 cockpit; Evans Head's Canberra WJ678
  cockpit). Mere tail fins and rudders were **not** — see §5.
- **Two sites for HARS.** Albion Park and Parkes are separate places with separate
  opening hours and separate inventories, so they are separate site records.
- **HMAS Albatross was split from the Fleet Air Arm Museum.** The museum is a
  public building reached from Albatross Road; the Seahawk N24-009 and Squirrel
  N22-018 gate guards are inside the naval air station. Different access, two
  records.

---

## 4. Fields deliberately left blank

- **Coordinates.** Given only for sites where a mapped position is defensible:
  the aerodrome reference points for Shellharbour, Parkes, Temora, Nowra
  (HMAS Albatross), Narromine and Evans Head, and the street addresses of the
  Powerhouse and the Australian National Maritime Museum. **Every pole, plinth and
  RSL site is blank** — the sources say "a park in Wagga Wagga" or "outside the
  RSL" and a town-centre coordinate would be a guess about where the airframe
  actually stands. Fighter World, RAAF Wagga, Camden, Singleton, Broken Hill and
  Holsworthy are also blank for the same reason: the site is inside a large
  campus and no source pinned the building.
- **`year_built`** is blank on **every row**. No construction, roll-out,
  first-flight or delivery date was sourced for any of these airframes;
  ADF-Serials publishes *delivery to the RAAF* dates, which is not the same thing,
  and RAAF A-serials are emphatically not years.
- **`tail_number`** blank where the identity is contested or unpublished: HARS's
  Wirraway, Clancy Skybaby and CA-28 Ceres (§2.9); the AWM's Tachikawa Ki-54;
  Fighter World's four replicas, Stearman, CT-4B and Bloodhound; Temora's O-1G
  Bird Dog (the survey gives "4606/53125", two numbers that were not reconciled);
  Evans Head's Caribou, MiG-15, Anson, Nomad and Drifter; Narromine's Corben
  Super Ace; the FAAM's Hargrave kite and Skycraft Scout; the Powerhouse's
  Bleriot XI, Skycraft Scout and Eagle XP-1; Camden's Falcon glider, Gere Sport
  and Gray monoplane; HARS Parkes's Firefly cockpit.
- **`aircraft_name`** used only where a name is genuinely borne:
  *G for George*, *City of Canberra*, *Connie*, *Southern Cross*, *Frigate Bird II*,
  *Shark 07*, *Worimi*.

---

## 5. Sites and airframes excluded, and why

- **Australian Aviation Museum, Bankstown — permanently closed.** Its Wikipedia
  article states "The Museum is now closed permanently." No site record was
  created. Its dispersal is traceable in the data: Canberra A84-502 and Vampire
  A79-665 went to HARS, and its Nomad went to Evans Head. **Mirage A3-44** was
  loaned there, allocated to the Benalla Aviation Museum in February 2019 and was
  "still sitting in the open at Bankstown" as of 31 October 2019 — current
  location unknown, so it is in no file. The Vampire **XA167** (displayed as
  A79-643) that stood on a plinth at the de Havilland/Boeing Bankstown factory was
  donated to the Bankstown museum on the factory's sale; also untraced.
- **Tail fins and other fragments are not airframes.** Excluded: Mirage
  **A3-116**'s tail outside the 331 Squadron (City of Coffs Harbour) Australian
  Air Force Cadets building; Mirage **A3-90**'s tail fin outside Fighter World;
  F-111G **A8-514**'s fin and rudder outside HQ Joint Operations Command at
  Bungendore NSW (the rest of the airframe was buried at a landfill near Ipswich
  in 2011). Each is noted here rather than invented as a site.
- **Private restorations and hangared warbirds** — excluded per the spec: Bell 47
  **A1-397** under restoration in a Bankstown hangar; Bell 47 **A1-405** under
  restoration by a private owner at Albury; Boomerangs **A46-73**, **A46-90** and
  **A46-128** in private restoration in NSW; Vampire fuselages **A79-175** and
  **A79-733** stored at Parkes for a private owner (not the HARS annexe);
  Vampire **A79-807** on loan to the Clyde North group at Wagga; Macchi
  **A7-025** at Pay's Air Services, Scone. Hawker Hunter VH-FRH, Nord 1002 VH-OFS
  and AT-6D VH-XAN appear in HARS airshow photo captions but are visiting
  privately-owned warbirds, not HARS collection aircraft.
- **Sabre A94-970 — "In 2025 move to Scone NSW"** (ADF-Serials). No public site at
  Scone was confirmed, so no record was created. This is a live lead (§7).
- **Sabre A94-965** — last reported on a property at West Hoxton, Sydney, with no
  confirmed sighting. **Sabre A94-902** — forward fuselage removed from Wagga in
  2010, "current location unknown". Both excluded.
- **Wessex N7-212**, sold in 2015 to a paintball park at Badgery Creek NSW, and
  **Wessex N7-219**, main fuselage at the Dubbo Military Museum as of 2003, and
  **Neptune A89-279**, which left Dubbo Military Museum by road for Mudgee in
  July 2013 — none could be confirmed as current, and the Dubbo Military Museum's
  present status could not be established. All excluded, all listed in §7.
- **Australian Army Flying Museum, Oakey** — Queensland, out of area, as
  instructed.
- **Meteor A77-878** is retained as a row in the FAAM file marked `in_storage`
  with a `description` stating it left for RAAF Amberley in February 2018. It is
  flagged here because a Queensland worker will legitimately claim it; if this
  survey's row and theirs collide, **theirs is right** and this row should be
  dropped.

---

## 6. The ACT

The only ACT site in this survey is the **Australian War Memorial**, which already
exists in the database and is handled through `awm_topup_aircraft.csv`. The sweep
for other Canberra airframes found nothing that qualifies:

- **RAAF Base Fairbairn / Canberra Airport** — no preserved airframe found in the
  ADF-Serials sweep; Fairbairn appears only as a former operating base.
- **RMC Duntroon and ADFA** — Macchi **A7-060** was an ADFA training aid from
  February 1993, went to storage at Wagga and was **scrapped in mid-2014**;
  Iroquois A2-490 was displayed at an ADFA open day in 2003 but is now the
  Holsworthy gate guard. No permanent ACT display airframe was found at either.
- The F-111G fin at **HQJOC Bungendore** is in NSW and is a fragment (§5).
- The Memorial's off-site holdings at the **Treloar Technology Centre / Mitchell
  annexe** are not a separate visitable site; they are recorded as
  `in_storage` rows against the Memorial, which is what the spec asks for.

The prompt's "Australian Aviation Heritage?" in Canberra could not be matched to
any real institution and is treated as a non-lead.

---

## 7. Open questions, ranked

1. **What is actually on display at the AWM now?** The Memorial's galleries
   reopened in 2026 after a six-year rebuild and it has not published a current
   aircraft list. The `display_status` split in `awm_topup_aircraft.csv` uses the
   Memorial's own live gallery pages where they name an aircraft (Anzac Hall:
   Lancaster, F/A-18A, Chinook; Aircraft Hall: Deperdussin, Albatros D.Va, S.E.5a,
   Anson cockpit, Zero, Sea Fury, Mustang, MiG-15) and otherwise falls back to the
   September 2023 Treloar inventory, marking those `in_storage`. Several marquee
   aircraft (Me 262, Me 163, Bf 109, Kittyhawk, Beaufort, Pfalz, DH.9, Bronco,
   RF-111C) are almost certainly back on display and are currently recorded as
   stored. **A single walk-round or a published gallery list would fix ten rows.**
2. **Which Sabre, if any, is at RAAF Base Wagga in 2026?** A94-982 left in 2018
   and its replacement A94-910 was diverted to Moorabbin. The Wagga file has no
   Sabre. Needs a current photograph of the base entrance.
3. **Sabre A94-970 at Scone.** ADF-Serials records a 2025 move to Scone NSW with
   no recipient named. Scone Aerodrome hosts Pay's Air Service; if the Sabre is on
   public display there, that is a missing site.
4. **A18-306 is claimed by two museums** — Evans Head (via the Bankstown museum,
   trailer-mounted) and the RFDS Broken Hill Visitor Experience (donated from
   Wagga in June 2018). Both rows exist; the Evans Head row has **no serial** and
   the conflict is stated in both. One of the two is a different Nomad.
5. **Evans Head's Kiowa.** The museum says it acquired A17-018 in August 2017;
   ADF-Serials shows A17-018 sold at a Grays auction in March 2019. The serial on
   the museum's airframe needs checking.
6. **HARS's Wirraway, Ceres, Skybaby and the loose registration VH-KFL.**
   Four unknowns in one misaligned table (§2.9). One HARS visit resolves all four.
7. **Is HARS's Iskra "816" at Albion Park or Parkes?** It appears in both survey
   inventories. Recorded at Parkes only.
8. **Dubbo Military Museum** — does it still exist, and does it still hold Wessex
   N7-219? Two aircraft have left it since 2003 and no current web presence was
   established. Potentially a missing site.
9. **Powerhouse Museum display state.** The Ultimo site is closed for renewal and
   Powerhouse advertises a "regional display" of the Catalina; some of the ten
   aircraft may be at the Castle Hill store, which would be a second site.
10. **Fleet Air Arm Museum A-4G identity.** The 2017 walk-round says the Skyhawk
    displayed as 882 is N13-154903; ADF-Serials makes it N13-154906 (really
    ex-USN A-4B BuNo 142874). N13-154906 is used.
11. **Coordinates for the fourteen sites left blank** (§4) — each needs a
    satellite fix on the actual airframe.
12. **Wessex N7-212 at the Badgery Creek paintball park** — a genuine airframe at
    a commercial site, last evidence 2015. If still there it is a site record.
