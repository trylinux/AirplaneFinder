# Phase 5 — Pennsylvania identity-gap resolution pass
Written 10 Sep 2026. Four sites. This file ADDS identities to phase1_museums_raw.md; it
does not re-list sites. Site lines are unchanged from phase 1 and are not repeated except
where a coordinate is improved (see §3).

---

## 1. American Helicopter Museum & Education Center — West Chester

### The break in the case
The FAA owner-name search really does return only ONE airframe (verified again this pass,
with a browser user-agent — the plain fetch is 403ed by Akamai):

    Nametxt=AMERICAN+HELICOPTER+MUSEUM  ->  1 of 1
    N5H | s/n 3 | BELL 47B | AMERICAN HELICOPTER MUSEUM AND EDUCATION CENTER | WEST CHESTER PA
    (N-number record: MFR Year 1946; Status Valid; cert issued 13 Jan 1997)

Variants tried and rejected: "AMERICAN HELICOPTER MUSEUM & EDUCATION CENTER" (the ampersand
is an unsupported character and the form errors), "AMERICAN HELICOPTER MUSEUM INC" (subsumed
by the above prefix search). So the FAA is a dead end here — AHMEC's airframes are almost all
ex-military or deregistered civil, and the museum genuinely publishes nothing.

**The tool that broke it open was the Aerial Visuals LOCATION dossier, not the airframe seed
search:** https://aerialvisuals.ca/LocationDossier.php?Serial=3592 lists 24 airframes with
identities, seven of them individually satellite-mapped to sub-arcsecond coordinates on the
museum apron. That is rung 4, so every identity below is corroborated where I could and
flagged where I could not. Corroborating rungs used: Wikipedia per-type survivor lists (rung 7),
ABPic photo caption (rung 6), Vertical Magazine feature (rung 6), aviationmuseum.eu type list
(rung 8, used ONLY to confirm a type is present, never for an identity).

### AIRCRAFT — American Helicopter Museum & Education Center
Field choices (model/variant split, aircraft_type, role_type) are kept identical to the
phase-1 lines so the two files merge without duplicate rows. Only tail_number, year_built,
aliases and description change on existing rows; new rows are marked NEW in §1.2.

Bell|47|B|N5H|||rotary_wing||civilian|utility|1946|Third of forty-three Bell 47Bs built; used as a company demonstrator; FAA registry confirms BELL 47B c/n 3 registered to American Helicopter Museum and Education Center with MFR Year 1946; registration status Valid at 10 Sep 2026|c/n 3|on_display
Bell|47|D-1||Sioux|H-13D|rotary_wing||military|utility||Displayed indoors in MASH configuration with litter panniers; Aerial Visuals lists an OH-13D at this site but publishes no serial for it; serial deliberately blank|H-13D; OH-13D; MASH helicopter|on_display
Bell|47|H-1|N8010E|||rotary_wing||civilian|private||Executive and charter variant of the Model 47; Aerial Visuals gives c/n 1355 and registration N8010E; N8010E is no longer live on the FAA registry — it now shows only as a Textron reservation — so this is a cancelled registration carried as the airframe identity|c/n 1355|on_display
Bell|47|J-2A|N8523F|Ranger||rotary_wing||civilian|private||Aerial Visuals gives c/n 3317 and registration N8523F; not present on the live FAA registry so the registration is cancelled; this airframe does not appear in the museum's own online gallery so presence needs a 2025-26 confirmation|c/n 3317; Bell 47J-2A|on_display
Bell|204|TH-1L|157817|Iroquois|Huey|rotary_wing||military|trainer||US Navy training Huey; BuNo 157817 from the Aerial Visuals location dossier; Vertical Magazine independently describes a US Navy UH-1L/TH-1L trainer at the museum|BuNo 157817; TH-1L; Huey|on_display
Bell|206||||JetRanger|rotary_wing||civilian|utility||Listed by the museum and by Aerial Visuals as a Bell Jet Ranger; no serial or registration published by any source; deliberately blank|JetRanger; Bell 206A|on_display
Bell|AH-1|F|68-15138||Cobra|rotary_wing||military|ground_attack||Displayed outdoors; serial 68-15138 from the Aerial Visuals airframe dossier for this location; 68-15138 falls in the FY68 AH-1G production block later converted to AH-1F so the serial block-checks|68-15138; Bell 209; Cobra|on_display
Bell-Boeing|V-22|||Osprey||rotary_wing||military|transport||Aerial Visuals gives BuNo 163913; Vertical Magazine independently describes the museum's Osprey as the THIRD prototype on permanent loan from the National Museum of the Marine Corps and 163913 is the third of the six full-scale-development airframes 163911-163916 — the two agree|BuNo 163913; XV-22; YV-22A; Osprey; tiltrotor|on_display
Boeing|360||N360BV|||rotary_wing||civilian|experimental||One-off all-composite tandem-rotor technology demonstrator built at Boeing Vertol Philadelphia; sole example; ABPic photo caption gives N360BV c/n 001 at the American Helicopter Museum; Aerial Visuals maps it on the apron but mislabels the type as CH-46X|c/n 001; Boeing Model 360; Boeing Vertol 360|on_display
Boeing|CH-47|HH-47|||CSAR-X mockup|rotary_wing||military|search_rescue||Full-size mockup built for the USAF CSAR-X competition; a mockup not an airframe so it has no serial|HH-47 CSAR-X mockup|on_display
Boeing Vertol|CH-46|E|157667|Sea Knight|Frog|rotary_wing||military|transport||The museum states this was the last aircraft delivered from Boeing Vertol Plant 2 near Philadelphia International Airport; Aerial Visuals carries BuNo 157667 in its UNCONFIRMED list for this site so the BuNo is provisional and the museum's own claim is unverified|BuNo 157667; Boeing Vertol 107; Frog|on_display
Kaman|HH-2|D|149031|Seasprite|K-20|rotary_wing||military|search_rescue||Displayed outdoors and satellite-mapped by Aerial Visuals at 39.99232 -75.57915; BuNo 149031 c/n 35; note Vertical Magazine calls the museum's Seasprite an SH-2F which conflicts with the HH-2D designation — the BuNo is the reliable half|BuNo 149031; c/n 35; Kaman K-20; Seasprite|on_display
Hughes|269|A|67-15412|Osage|TH-55A|rotary_wing||military|trainer||Primary US Army rotary trainer to 1988; the museum calls this airframe Stubby and says it was acquired in 1998; serial 67-15412 from the Aerial Visuals location dossier|67-15412; TH-55A; Osage; Stubby|on_display
Hughes|369|OH-6A|65-12916|Cayuse||rotary_wing||military|recon||Serial 65-12916 from the Aerial Visuals location dossier; falls in the FY65 OH-6A block; a SECOND OH-6A 67-16112 / N62575 in NOTAR configuration appears in Aerial Visuals' unconfirmed list for this site and may be a separate airframe|65-12916; OH-6A; Cayuse; Loach|on_display
Hughes|500|D|81-23655|Little Bird|MH-6J|rotary_wing||military|utility||Displayed indoors; Aerial Visuals gives 81-23655 and calls it MH-6C; the museum and Vertical Magazine call it an AH-6J/MH-6J flown by the 160th SOAR; the serial is the reliable half|81-23655; MD 530F; MH-6C; MH-6J; Little Bird|on_display
Gyrodyne|QH-50|C|001190|DASH||rotary_wing||military|drone||US Navy Drone Anti-Submarine Helicopter; Aerial Visuals carries s/n 001190 c/n DS-1190 in its UNCONFIRMED list for this site so the serial is provisional; Vertical Magazine describes a 1964 QH-50C with torpedoes on display|BuNo 001190; c/n DS-1190; DSN-3; DASH|on_display
Piasecki|CH-21|C|55-4140|Shawnee||rotary_wing||military|transport||Satellite-mapped by Aerial Visuals at 39.99218 -75.57942; s/n 55-4140 c/n C.94; the museum's own gallery does not list an H-21 at all but Vertical Magazine confirms a Piasecki H-21 is on the floor|55-4140; c/n C.94; H-21; Shawnee; Flying Banana|on_display
Piasecki|H-21|B|FR09|Work Horse||rotary_wing||military|transport||Aerial Visuals lists a SECOND Piasecki H-21 at this site — ex-French Army Aviation Legere de l'Armee de Terre FR09 c/n B.155; no other source shows two H-21s here so this is low confidence and may be a duplicate dossier for 55-4140|FR09; c/n B.155; H-21B; Work Horse|on_display
Piasecki|HUP|2|128479|Retriever||rotary_wing||military|utility||Displayed indoors; BuNo 128479 given independently by the Aerial Visuals location dossier and by the Wikipedia HUP Retriever survivor list; this CONFIRMS it is a different airframe from HUP-2 BuNo 128517 at Wings of Freedom Horsham — phase 1 open question 11 is closed|BuNo 128479; UH-25B; PV-14; HUP-2; Retriever|on_display
Piasecki|VZ-8|P|58-5510|Airgeep||rotary_wing||military|experimental||US Army ducted-fan flying jeep; s/n 58-5510 from the Aerial Visuals location dossier; not listed in the museum's own online gallery but aviationmuseum.eu independently lists a VZ-8P Aerial Jeep here|58-5510; VZ-8P; Airgeep; Aerial Jeep|on_display
Hiller|OH-23|G|62-3759|Raven||rotary_wing||military|utility||s/n 62-3759 from the Aerial Visuals location dossier; aviationmuseum.eu independently lists an OH-23G Raven here; Aerial Visuals separately reports a UH-12D at the site which is the same basic type and may be the same airframe|62-3759; UH-12; Raven|on_display
Sikorsky|S-61|HH-3|151556|Sea King||rotary_wing||military|search_rescue||Displayed outdoors and satellite-mapped by Aerial Visuals at 39.99225 -75.57923; BuNo 151556 c/n 61-292; the museum's own current gallery does not show it but the mapped fix plus Vertical Magazine's description of an HH-3A confirm presence|BuNo 151556; c/n 61-292; HH-3A; Sea King; Jolly Green|on_display
Sikorsky|S-62|HH-52|1383||Sea Guardian|rotary_wing||military|search_rescue||Displayed outdoors and satellite-mapped by Aerial Visuals at 39.99217 -75.57930; US Coast Guard s/n 1383 c/n 62-064; distinct from the HH-52A c/n 1394 owned by the Mid-Atlantic Air Museum at Reading|USCG 1383; c/n 62-064; HH-52A; Sea Guard|on_display
Sikorsky|S-51||9603|Dragonfly|H-5|rotary_wing||military|utility||Ex-Royal Canadian Air Force 9603 c/n 5130 per the Aerial Visuals location dossier; aviationmuseum.eu independently lists both an S-51 Dragonfly and an H-5G here which are almost certainly this one airframe|RCAF 9603; c/n 5130; H-5G; Dragonfly|on_display
Sikorsky|HO5S|1|130136|||rotary_wing||military|utility||US Marine Corps BuNo 130136 c/n 52-094 per the Aerial Visuals location dossier; the civil equivalent is the Sikorsky S-52; aviationmuseum.eu independently lists an HO5S-1 here|BuNo 130136; c/n 52-094; S-52|on_display
Sikorsky|R-6|A|N75610|Hoverfly II||rotary_wing||military|utility||Built by Nash-Kelvinator under licence; registration N75610 from the Aerial Visuals location dossier; N75610 has since been REASSIGNED by the FAA to a Powrachute 914 Custom in Texas so this is a cancelled registration and not a live identity; the museum describes it as its oldest airframe and it is under restoration|N75610; R-6A; Nash-Kelvinator; Hoverfly II|under_restoration
Sud-Ouest|SO.1221||57-6106|Djinn|YHO-1|rotary_wing||military|utility||French tip-jet helicopter evaluated by the US Army as the YHO-1; s/n 57-6106 from the Aerial Visuals location dossier which also carries the French serial FR75; aviationmuseum.eu independently lists an SO.1221S Djinn here|57-6106; FR75; YHO-1; Djinn|on_display
Brantly|B-2|B|N2294U|||rotary_wing||civilian|private||c/n 467 registration N2294U per the Aerial Visuals location dossier; not on the live FAA registry so the registration is cancelled; aviationmuseum.eu independently lists a Brantly B-2B here|c/n 467; B-2B|on_display
Enstrom|F-28|A||||rotary_wing||civilian|private||The museum states this is the second production aircraft used for certification then modified for a 1967 US Army training helicopter competition; no serial or registration published by any source; deliberately blank|F-28A|on_display
Piasecki|HRP|2||Rescuer||rotary_wing||military|search_rescue||Listed on the museum's own Aircraft Under Restoration page and by aviationmuseum.eu; Wikipedia states two surviving HRP Rescuers are IN STORAGE at this museum but publishes no BuNos; no source anywhere gives a BuNo so this is deliberately blank|HRP-2; HRP-1; Rescuer; Flying Banana|under_restoration
Piasecki|XHJP|1||||rotary_wing||military|utility||Listed on the museum's own Aircraft Under Restoration page and by aviationmuseum.eu; XHJP-1 was the HUP prototype and only two or three were built; Wikipedia's HUP survivor list records no surviving XHJP-1 at all so the identity is unresolvable from open sources|XHJP-1|under_restoration
Sikorsky|H-19|S-55||Chickasaw||rotary_wing||military|utility||Listed on the museum's own Aircraft Under Restoration page; does not appear in the Aerial Visuals location dossier or in the aviationmuseum.eu type list so both presence and identity need confirmation|S-55; H-19; Chickasaw|under_restoration
Sikorsky|HOS|1||||rotary_wing||military|utility||helis.com news items describe a US Coast Guard HOS-1 restored over eight years and unveiled at this museum; no serial published; possibly the same airframe as the R-6A above since HOS-1 is the Navy designation of the R-6A — treat as ONE airframe until separated|HOS-1; R-6|under_restoration
Bensen|B-7|W||Hydro-Gyroglider||rotary_wing||civilian|experimental||Tandem trainer used to teach over 600 pilots to fly gyrocopters; no serial published by any source|B-7W|on_display
Bensen|B-8|M||Gyrocopter||rotary_wing||civilian|experimental||Homebuilt gyrocopter; aviationmuseum.eu reports TWO B-8M examples here; no serials published by any source|B-8M|on_display
McCulloch|J-2|||Gyroplane||rotary_wing||civilian|private||No serial or registration published; note the Mid-Atlantic Air Museum at Reading separately owns McCulloch J-2 c/n 032 N4322G which is a DIFFERENT airframe|J-2 gyroplane|on_display
Galaxie|XRG-65|||Glaticopter||rotary_wing||civilian|experimental||One-off helicopter built by Edward Glatfelter of Newtown Square Pennsylvania; no serial|XRG-65 Glaticopter; Glatfelter|on_display
Parsons|Super Mac|II||||rotary_wing||civilian|experimental||EAA Best New Rotorcraft Design 1995; homebuilt gyrocopter; no serial|Super Mac II; Parsons Sport Autogyro|on_display
Air Command|Commander Sport|||||rotary_wing||civilian|experimental||Homebuilt gyrocopter; aviationmuseum.eu identifies it as an Air Command 447 Commander Sport; no serial|Air Command 447; Commander Sport|on_display
AeroVelo|Atlas|||||rotary_wing||civilian|experimental||Human-powered helicopter; first to hover for sixty seconds and reach three metres; AHS Sikorsky Prize winner; no serial|Atlas|on_display
Kitty Hawk|Flyer|||||rotary_wing||civilian|experimental||Electric multirotor personal air vehicle; no serial|Kitty Hawk Flyer|on_display
Leonardo|AW139|||Mockup||rotary_wing||civilian|transport||Cabin mockup modified to demonstrate state-of-the-art interiors; a mockup not an airframe|AW139 mockup|on_display

### 1.2 NEW rows this pass — airframes phase 1 did not have at all
These come from the Aerial Visuals location dossier corroborated by the aviationmuseum.eu
type list. Presence is good; identities vary in confidence (see §1.3).

Bell|47|J-2A|N8523F  — NEW
Bell|47|H-1|N8010E   — NEW
Brantly|B-2|B|N2294U — NEW
Hiller|OH-23|G|62-3759 — NEW
Piasecki|CH-21|C|55-4140 — NEW
Piasecki|H-21|B|FR09 — NEW (doubtful, see §1.3)
Piasecki|VZ-8|P|58-5510 — NEW
Sikorsky|S-51||9603 — NEW
Sikorsky|HO5S|1|130136 — NEW
Sikorsky|R-6|A|N75610 — NEW
Sud-Ouest|SO.1221||57-6106 — NEW

### 1.3 Confidence register for every AHMEC identity resolved

| Manufacturer | Model | Variant | Identity resolved | Source (rung) | Confidence |
|---|---|---|---|---|---|
| Bell | 47 | B | N5H c/n 3, built 1946 | FAA owner+N-number search (2) | CERTAIN |
| Piasecki | HUP | 2 | BuNo 128479 | Aerial Visuals location dossier (4) + Wikipedia HUP survivor list (7) — independent | HIGH |
| Bell-Boeing | V-22 | — | BuNo 163913 | Aerial Visuals (4) + Vertical Mag "third prototype" (6); FSD block 163911-916 agrees | HIGH |
| Boeing | 360 | — | N360BV c/n 001 | ABPic caption naming the museum (6) + Aerial Visuals (4) | HIGH |
| Sikorsky | S-62 | HH-52 | USCG 1383 c/n 62-064 | Aerial Visuals, satellite-mapped on apron (4) | HIGH |
| Sikorsky | S-61 | HH-3 | BuNo 151556 c/n 61-292 | Aerial Visuals, satellite-mapped (4) | HIGH |
| Kaman | HH-2 | D | BuNo 149031 c/n 35 | Aerial Visuals, satellite-mapped (4) | HIGH |
| Piasecki | CH-21 | C | 55-4140 c/n C.94 | Aerial Visuals, satellite-mapped (4) | HIGH |
| Bell | AH-1 | F | 68-15138 | Aerial Visuals airframe dossier (4); FY68 block checks | MEDIUM-HIGH |
| Bell | 204 | TH-1L | BuNo 157817 | Aerial Visuals (4) | MEDIUM |
| Hughes | 269 | A | 67-15412 | Aerial Visuals (4) | MEDIUM |
| Hughes | 369 | OH-6A | 65-12916 | Aerial Visuals (4) | MEDIUM |
| Hughes | 500 | D | 81-23655 | Aerial Visuals (4); designation disputed MH-6C vs MH-6J | MEDIUM |
| Piasecki | VZ-8 | P | 58-5510 | Aerial Visuals (4); type presence corroborated by aviationmuseum.eu (8) | MEDIUM |
| Sikorsky | HO5S | 1 | BuNo 130136 c/n 52-094 | Aerial Visuals (4); type corroborated (8) | MEDIUM |
| Sikorsky | S-51 | — | RCAF 9603 c/n 5130 | Aerial Visuals (4); type corroborated (8) | MEDIUM |
| Sud-Ouest | SO.1221 | — | 57-6106 (FR75) | Aerial Visuals (4); type corroborated (8) | MEDIUM |
| Hiller | OH-23 | G | 62-3759 | Aerial Visuals (4); type corroborated (8) | MEDIUM |
| Bell | 47 | H-1 | N8010E c/n 1355 | Aerial Visuals (4); registration cancelled — FAA now shows a Textron reservation | MEDIUM |
| Bell | 47 | J-2A | N8523F c/n 3317 | Aerial Visuals (4); registration cancelled; not in museum gallery | LOW-MEDIUM |
| Brantly | B-2 | B | N2294U c/n 467 | Aerial Visuals (4); registration cancelled; type corroborated (8) | MEDIUM |
| Sikorsky | R-6 | A | N75610 | Aerial Visuals (4); N75610 REASSIGNED to a Texas Powrachute so cancelled | LOW-MEDIUM |
| Boeing Vertol | CH-46 | E | BuNo 157667 | Aerial Visuals UNCONFIRMED list (4) | LOW |
| Gyrodyne | QH-50 | C | BuNo 001190 c/n DS-1190 | Aerial Visuals UNCONFIRMED list (4) | LOW |
| Hughes | 369 | OH-6A NOTAR | 67-16112 / N62575 | Aerial Visuals UNCONFIRMED list (4); may be a second OH-6A or a duplicate | LOW |
| Piasecki | H-21 | B | FR09 c/n B.155 | Aerial Visuals (4) only; no second source shows two H-21s here | LOW |

**Deliberately blank — nothing sourceable exists:** Bell 47D-1/OH-13D, Bell 206 JetRanger,
Enstrom F-28A, Piasecki HRP-2, Piasecki XHJP-1, Sikorsky H-19/S-55, Sikorsky HOS-1, Bensen
B-7W, Bensen B-8M (x2), McCulloch J-2, Galaxie XRG-65, Parsons Super Mac II, Air Command 447,
AeroVelo Atlas, Kitty Hawk Flyer, Leonardo AW139 mockup, Boeing HH-47 mockup, Pitcairn PCA-1A,
Sikorsky VS-300 replica, Sikorsky XR-4 cockpit, Princeton Air Cycle / Gem X-2 Air Scooter,
Rotorway Scorpion, Rotorway Scorpion Too, Robinson R-22, Bolkow Bo-105C, Sikorsky S-76,
Bell 30-1-A. **A blank is the correct answer for these — do not re-research them.**

### 1.4 Additional AHMEC airframes reported but NOT yet given phase-1 rows
Aerial Visuals and aviationmuseum.eu both report these types at the site; neither publishes an
identity and the museum's own gallery is silent. They are listed here so a later pass knows they
exist, but I have NOT written pipe rows for them because presence is single-sourced:
Pitcairn PCA-1A, Sikorsky VS-300 (cockpit section, replica), Sikorsky XR-4 (cockpit section),
Sikorsky S-76 Spirit (ex-SARA testbed, donated by Sikorsky per helis.com news), Robinson R-22,
Bolkow Bo-105C, Princeton Gem X-2 Air Scooter, Rotorway Scorpion, Rotorway Scorpion Too,
Bell 30-1-A, Sikorsky R-5.

### 1.5 One airframe has LEFT
Aerial Visuals records **Sikorsky UH-34D Seahorse BuNo 148768 c/n 58-1319** as
"once based, stored or displayed here but moved on". The Vertical Magazine feature still
describes a UH-34D donated by the National Air and Space Museum as being on the floor. These
conflict. The museum's own current online gallery does not list a UH-34D. **Do not record it
until someone confirms it in person** — the AV "moved on" flag is the more recently maintained
of the two.

---

## 2. The Franklin Institute — Philadelphia

### What changed

**(a) The gallery is gone, and nothing aviation replaced it.** fi.edu's own Franklin Air Show
page now reads "WE ARE CLEARING THE RUNWAY... flying off into the sunset as we make room for a
sunnier experience... cleared for departure on January 5, 2026." The museum's current
"Exhibits and Experiences" index as of 10 Sep 2026 lists Wondrous Space, Body Odyssey, Hamilton
Collections Gallery, Your Brain, SportsZone, Sir Isaac's Loft, Amazing Machine, Brick Play Space,
the Benjamin Franklin National Memorial, the Holt & Miller Observatory, Fels Planetarium, and
STAR WARS: The Experience opening February 2027. **There is no aviation gallery and no aircraft
named anywhere in the current exhibit index.** PhillyVoice reports the closure is part of a
consolidation to six "core" exhibits.

**(b) Wright Model B — still in the building, location not yet announced.** A Franklin Institute
representative told PhillyVoice the 1911 Wright Model B "will be relocated to a new spot in the
building." No source published this pass names the new spot. Treat as **on_display, location
within the building unstated** — it is the institution's signature artifact and the museum has
committed publicly to keeping it out. The December 2024 Philadelphia Inquirer story about the
Bergdoll family's ownership challenge is still the live provenance issue; nothing has been
reported as resolved.

**(c) T-33 — the serial is RIGHT and the museum's own "TO-2" gloss is WRONG. RESOLVED.**
- 53-6038 falls inside **53-5919/6152 = Lockheed T-33A-5-LO** (Joe Baugher 1953 USAF serials,
  crouze.com mirror, fetched this pass). The serial block-checks cleanly as a USAF T-33A.
- The Franklin Institute's own exhibit page dates the airframe to **1948** and its catalogue
  number is **66-1**. A 1948 build date is incompatible with an FY53 serial, and the FY53 serial
  is incompatible with the TO-2 designation (TO-2 was the US Navy designation applied to T-33s
  in 1949-50, renamed TV-2 in 1950; those carry BuNos, never USAF FY serials).
- The independent February 2025 aviationhistorymuseums.com visit report records the aircraft as
  **"Lockheed T-33 (53-6038), 1953"** with no Navy claim at all.
- **Conclusion: the airframe is a Lockheed T-33A-5-LO, USAF serial 53-6038.** The museum's
  "1948" and "TO-2/TV-2" labels are exhibit-copy error and should be recorded as such, not as
  aliases implying a Navy identity. I have removed TO-2/TV-2 from the alias field below.
- **Fate: unknown.** No source says where the cockpit went after 5 Jan 2026. It was a walk-in
  cockpit on the second floor; the PhillyVoice piece says it is "unclear what the museum will do
  with the rest of the pieces." Record as in_storage until someone reports otherwise.

**(d) Budd BB-1 Pioneer — CONFIRMED still outdoors.** The museum's own live page fi.edu/en/
budd-bb1-pioneer-aircraft states it stands "in front of the museum" at the **20th Street main
entrance**, where it has been since 1935, removed only three times (1969, and Sept 2016 to
1 Dec 2017 for conservation — cleaning, polishing, mesh netting, crack patching). The
February 2025 visit report independently records it "on display in front of the new museum
building, where it has been ever since." **It is outdoors, free to view without admission, and
is now the only aircraft the Franklin Institute definitely still presents to the public.**
Wikipedia gives first flight 1931 and notes fabric and lower wing were removed in 1935 — so the
displayed object is a partially stripped airframe. No registration is published by any source;
leave tail_number blank.

### AIRCRAFT — The Franklin Institute (replacement rows)

Wright|Model B|||Bergdoll Flyer||fixed_wing|biplane|civilian|private|1911|Bought new by Grover Cleveland Bergdoll who was taught by Orville Wright; confiscated by the US government in 1921; installed in the Franklin Institute in 1934; museum catalogue number 2885; the Franklin Air Show gallery closed 5 January 2026 and the museum states the aircraft is being relocated to a new spot inside the building — the new location has not been announced as of September 2026|FI Cat 2885; Bergdoll Flyer; Wright B|on_display
Lockheed|T-33|A|53-6038|Shooting Star||fixed_wing|monoplane|military|trainer||Serial 53-6038 block-checks as a Lockheed T-33A-5-LO in the FY53 range 53-5919/6152 per Joe Baugher; the museum's own exhibit copy dating it 1948 and calling it an ex-Navy TO-2 is ERROR — TO-2s carry Navy BuNos not USAF fiscal-year serials; museum catalogue number 66-1; the gallery closed 5 January 2026 and the aircraft's onward fate is unreported|FI Cat 66-1; 53-6038|in_storage
Budd|BB-1|||Pioneer||fixed_wing|biplane|civilian|experimental|1931|First US all-stainless-steel aircraft; shotwelded biplane flying boat with a 210 hp Kinner C-5; first flown 1931 from the Budd factory field; donated 1935 and mounted outside the 20th Street entrance ever since with fabric and lower wing removed; conserved September 2016 to 1 December 2017; confirmed outdoors on the museum's own live page in September 2026|Budd Pioneer; BB1|on_display

**year_built change:** the T-33's year_built is now BLANK, not 1953. Phase 1 populated 1953 from
the fiscal-year prefix, which the brief forbids. No acceptance date was found this pass.

---

## 3. Allegheny Arms & Armor Museum — Smethport. STILL UNRESOLVED — recommend EXCLUDE

### What I established
- **Both airframes are individually satellite-mapped** by the Aerial Visuals location dossier
  (https://aerialvisuals.ca/LocationDossier.php?Serial=3583):
  - Grumman A-6A Intruder, BuNo **147867** — 41 50 32.34 N 78 26 29.82 W (41.842317, -78.441617)
  - Sikorsky CH-34A, s/n **57-1698** USAF, c/n **58-0842**, c/r **N94485** —
    41 50 32.04 N 78 26 30.61 W (41.842233, -78.441836)
  - Main museum building marker: 41 50 33.04 N 78 26 28.66 W (41.842511, -78.441294) — this is a
    better site coordinate than the blank in the phase-1 site line.
- **Provenance of the A-6 established:** the Aerial Visuals airframe dossier (Serial=15765)
  records BuNo 147867 as ex-USN, then the **Intrepid Sea-Air-Space Museum, New York**, then
  **moved to Smethport in October 1997**.
- **A third airframe has already left:** Bell AH-1F Cobra **69-16442** is in the AV "moved on"
  list for this site. So the site does lose airframes and the AV dossier does track departures —
  which makes its silence on the other two mildly reassuring but not evidence.
- **FAA on N94485: DEREGISTERED.** The live registry returns only "N94485 is Deregistered" with
  no owner record. Consistent with a static display; tells us nothing about location.
- **No 2023-2026 evidence of any kind was found.** The best dated primary source remains
  William Maloney's photo essay from **June 2010**, which describes both the A-6 and the
  Sikorsky as "in very poor shape" (bee's nest in the helicopter). RoadsideAmerica's newest
  visitor comment is **2017**; an earlier one from 2006 already reported "the actual museum part
  was closed" while the outdoor grounds remained walkable. McKean County local news searches,
  Smethport borough and Route 6 Alliance tourism pages, and visitPA all return nothing on this
  museum — the borough's own attraction listing does not mention it.

### Verdict
**Presence in 2025-26 cannot be substantiated from open sources.** The airframes were there in
2010 and probably in 2017; the indoor museum has been shut since at least 2006; and the only
mapped fixes come from a directory that does not date its map entries. Under the brief's
stale-data discipline this fails the "is it still there in 2025-26?" test.

**Recommendation: EXCLUDE the site from the database for now**, and carry it as a named open
question so nobody re-researches it from scratch. If a later pass wants to close it, the two
identities above are correct and ready — only currency is missing. **One 2026 satellite look at
41.8423 N 78.4416 W, or one phone call to McKean County / Smethport Borough (borough office,
smethportpa.org), would settle it.** Note also that both airframes were described as badly
deteriorated in 2010, so even if present they may now qualify as "scrap/derelict hulks", which
the brief excludes on its own terms.

Corrected coordinates if a later pass does record the site:
Allegheny Arms and Armor Museum -- Smethport|Smethport|Pennsylvania|United States|16749|North America|US Route 6||public|41.842511|-78.441294
(coordinate = Aerial Visuals' main-museum marker; access_type "public" reflects a walk-the-grounds
roadside display, NOT a functioning museum.)

---

## 4. Mid-Atlantic Air Museum — Reading. ALL FIVE VERIFIED MUSEUM-OWNED. Nothing to flag.

FAA owner-name search on **"MID ATLANTIC AIR MUSEUM"** (the hyphenated spelling returns ZERO —
the registry stores it without the hyphen; this is the trap that made the earlier pass unable to
confirm) returns 50+ aircraft on page 1 alone. Each of the five was then confirmed individually
on its N-number record, all registered to **11 MUSEUM DR, READING, PENNSYLVANIA 19605** — the
museum's own address. Registration status **Valid** on all five at 10 Sep 2026.

| Recorded as | FAA record | Owner name on record | Verdict |
|---|---|---|---|
| B-25J N9456Z | NORTH AMERICAN **TB-25N**, s/n **44-29939**, cert issued 20 May 1982, expires 30 Apr 2030, A/W date 19 Sep 1961 | MID ATLANTIC AIR MUSEUM INC, 11 Museum Dr, Reading PA 19605 | **CONFIRMED museum-owned and resident** |
| R4D-6 N229GB | DOUGLAS **DC3C 1830-94**, s/n **26874**, cert issued 13 Jul 1981, expires 31 Oct 2027 | MID ATLANTIC AIR MUSEUM INC | **CONFIRMED** |
| C-119F N175ML | FAIRCHILD **C-119**, s/n **131677**, MFR Year **1953**, cert issued 6 Mar 1995, expires 31 Oct 2029 | MID ATLANTIC AIR MUSEUM | **CONFIRMED** |
| P2V-7 N45309 | LOCKHEED **SP-2H**, s/n **7180**, cert issued 18 Nov 1983, expires 31 Oct 2028 | MID ATLANTIC AIR MUSEUM | **CONFIRMED** |
| TBM-3 N109K | GRUMMAN **TBM-3**, s/n **53638**, MFR Year **1945**, cert issued 30 Jan 2004, expires 30 Apr 2029 | MID ATLANTIC AIR MUSEUM | **CONFIRMED** |

**No visiting warbirds among them. Nothing to flag.** Registrations held 22-45 years each,
which is itself strong evidence of residency rather than a visiting aircraft.

### Corrections these lookups force on the phase-1 MAAM rows
1. **N9456Z is a TB-25N, s/n 44-29939** — a post-war conversion of a B-25J. Record
   `North American|B-25|J|44-29939` with `TB-25N` in aliases, or `model B-25 / variant J`
   with the description noting the FAA carries it as TB-25N. Do NOT put "N9456Z" in
   tail_number if the military serial 44-29939 is available — the brief prefers the military
   serial and puts the N-number in aliases. Same logic for the others below.
2. **N175ML year_built = 1953** (FAA MFR Year — a legitimate year_built source per the brief).
   s/n 131677 is the USAF/USN serial, i.e. **C-119F/R4Q-2 BuNo 131677**, not a construction number.
3. **N109K year_built = 1945** (FAA MFR Year). s/n 53638 is the Grumman/Eastern construction
   number, not a BuNo.
4. **N45309 s/n 7180** is the Lockheed c/n; the FAA model is **SP-2H**, the post-1962
   designation of the P2V-7. Both designations are correct; SP-2H is the later one.
5. **N229GB s/n 26874** is the Douglas c/n; FAA type is DC3C, i.e. a civilianised C-47/R4D.

### Bonus: 45 further MAAM-owned airframes surfaced by the same search
The owner search returned far more than the five asked about. Page 1 (of 2) is reproduced here
because it anchors most of the museum's collection with construction numbers, and a later pass
should mine it rather than repeat the search. **Note the FAA pagination parameter does not work —
`&PageNo=2` returns page 1 again — so page 2 was NOT retrieved this pass.**

N109K/53638 GRUMMAN TBM-3 · N119EC/T40-308 FAIRCHILD M-62A · N12RR/1 ROMANO BUSHBY ·
N1394/1394 SIKORSKY HH-52A · N14742/101 KELLETT KD-1A · N15252/A-572 AERONCA C-3 ·
N15792/1006 HEATH AVIATION LNB-4 · N15J/55-1 MIDGET MUSTANG MC-4 · N15K/1062 BIRD A-T ·
N16470/001 SWEET-ROGER ARROW SPORT-S · N174HM/HM-174 MERKEL J4B-2 · N175ML/131677 FAIRCHILD C-119 ·
N1841/1 FLYING FLEA HM162 · N19139/2987 FAIRCHILD 24G · N214N/1-058 CAMAIR 480 ·
N22443/2034 AUSTER 5J1 · N229GB/26874 DOUGLAS DC3C · N234/1-070 CAMAIR 480 · N243/1-077 CAMAIR 480 ·
N24554/88-12281 NORTH AMERICAN SNJ-4 · N25546/823 REARWIN 8135 · N26475/28 MEYERS OTW ·
N285SN/0723 SONEX · N30031/01 ZUCK PLANE-MOBILE · N303JV/001 KR-2 · N333JA/24339 VANS RV-6A ·
N338VA/01 DONS EAGLE · N3430H/4055 ERCOUPE 415-G · N34781/237 CULVER LCA · N3601Z/22-7489 PIPER PA-22-150 ·
N3925M/HO-155 FAIRCHILD(HOWARD) M-62C(PT-23A) · N39563/F5664TA AERONCA 65-TAC · N404H/BA-590 BEECH G18S ·
N41793/5855 CESSNA T-50 · N4259T/324 BABY ACE D · N4322G/032 McCULLOCH J-2 ·
N433V/1-1933 PIETENPOL AIRCAMPER · N44718/2782 NAVAL AIRCRAFT FACTORY N3N-3 · N4487K/NAV-4-1487 TEMCO D-16 ·
N450A/14141 MARTIN 404 · N45309/7180 LOCKHEED SP-2H · N46922/145712 SIKORSKY S-58 ·
N47021/L-5531 TAYLORCRAFT DCO-65 · N472MA/472 BD-5B · N47608/058B-5442 AERONCA O-58B ·
N484SM/275 MITCHELL WING A-10D · N49049/1582 RYAN PT-22 · N4991C/JT1/89 TAYLOR MONOPLANE ·
N50024/6143AE FAIRCHILD M-62A · N50084/53-7720 PIPER L-21B

Two of these matter to other sites: **N1394 HH-52A c/n 1394** is MAAM's, NOT the American
Helicopter Museum's HH-52A (USCG 1383 c/n 62-064) — two different Sea Guards in Pennsylvania.
**N4322G McCulloch J-2 c/n 032** is MAAM's, distinct from the AHMEC J-2.

---

## NOTES

### Method notes worth carrying forward
1. **The FAA owner-name search 403s a plain curl.** Send a desktop browser User-Agent and it
   returns 200. WebFetch also fails on it — it renders the empty form and reports "unsupported
   characters". Use `curl -A "<chrome UA>"` with `+` for spaces and NEVER an ampersand in the name.
2. **`&PageNo=N` on the FAA name-result URL is ignored.** Page 2 of a >50-row owner search must
   be reached another way (POST, or narrow the name string). MAAM page 2 was not retrieved.
3. **Match the registry's punctuation, not the museum's.** "MID-ATLANTIC AIR MUSEUM" → zero rows.
   "MID ATLANTIC AIR MUSEUM" → 50+. This single hyphen was the whole blocker.
4. **Aerial Visuals LOCATION dossiers are far higher-yield than seed searches for museums.**
   `LocationDossier.php?Serial=<id>` lists every airframe at a site with c/n, serial and
   registration, plus satellite-fixed coordinates for the mapped ones, plus separate
   "unconfirmed" and "moved on" buckets. AHMEC = 3592, Allegheny Arms Smethport = 3583.
   Find the id by web-searching "aerialvisuals location dossier <museum name>".
5. helis.com and rotorspot.nl were both **unreachable** this pass — helis.com is behind a
   Cloudflare JS challenge (403 to curl, and WebFetch only sees its news column, not the
   per-airframe register). rotorspot.nl did not surface in any search. Both remain untried
   avenues for AHMEC.

### What was NOT reached
- **helis.com and rotorspot.nl per-airframe registers for AHMEC** (Cloudflare / not found).
  These are the most likely sources to raise the LOW/MEDIUM confidence AHMEC identities.
- **AHMEC's own press kit or collection PDF** — no such document was located; the site is a Wix
  build with no downloadable collection list.
- **MAAM FAA owner-search page 2** (pagination broken) — roughly 10-20 further airframes.
- **Any 2023-26 evidence for Smethport.** Nothing exists in text sources; this needs imagery or
  a phone call.
- **The Franklin Institute T-33's post-January-2026 whereabouts** — unreported everywhere.
- **The Wright Model B's new in-building location** — unannounced as of September 2026.

### Open questions ranked
1. **Is anything still standing at 41.8423 N 78.4416 W in Smethport?** One satellite look closes
   the whole site. Until then, EXCLUDE. (Also settles whether the two airframes are now hulks.)
2. **Where did the Franklin Institute T-33 53-6038 go?** One call to The Franklin Institute,
   **(215) 448-1200**, would also close the Wright Model B's new location — two answers, one call.
3. **Does AHMEC have one H-21 or two?** Aerial Visuals says two (55-4140 and French FR09);
   everyone else says one. One call to the American Helicopter Museum, **(610) 436-9600**, would
   settle this AND the CH-46E BuNo AND the UH-34D question AND the HRP-2/XHJP-1 BuNos —
   **this is the single highest-value phone call in the state.**
4. **Is the AHMEC "HOS-1" the same airframe as the R-6A N75610?** HOS-1 is the Navy designation
   of the R-6A. Probably one airframe double-counted; same call closes it.
5. **Is AHMEC's UH-34D BuNo 148768 present or gone?** Aerial Visuals says gone; Vertical
   Magazine says present. Same call.
6. **MAAM owner-search page 2** — needs a working pagination method.
