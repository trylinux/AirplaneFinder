# Resolved airframe conflicts — batch 3

## 1. Douglas A-4M 158430 (c/n 14252)
VERDICT: B
CONFIDENCE: high
EVIDENCE: SilverHawkAuthor's Tennessee survivor list carries the entry verbatim as
"Douglas A-4M Skyhawk (BuNo. 158430), Sequatchie County Veterans Memorial Park"
(https://www.silverhawkauthor.com/post/warplane-survivors-usa-tennessee). The Tennessee Magazine
feature on the Dunlap park independently describes "an A4 Skyhawk" on the grounds alongside a
Jeep and an M59 (https://www.tnmagazine.org/monumental-service/). Overpass (overpass.private.coffee,
queried 12 Sep 2026) returns three historic=aircraft nodes within 1500 m of the Dunlap coordinates
(9991960880 / 9991960881 "UH-1" / 9991960882) and ZERO aircraft nodes within 1500 m of the
D'Iberville coordinates 30.4321,-88.9002. No source consulted places any aircraft at
Veterans Memorial Park, D'Iberville MS. The A-row description is a verbatim paste of the B-row text.
ACTION: delete id 26248, keep 26200

## 2. Vought A-7D 69-6241 (c/n D-071)
VERDICT: A
CONFIDENCE: high
EVIDENCE: Wikipedia's List of surviving LTV A-7 Corsair IIs gives 69-6241 as
"Brooke County Veterans Memorial Park, Weirton, West Virginia" and lists no A-7 at
Burlington Township, New Jersey
(https://en.wikipedia.org/wiki/List_of_surviving_LTV_A-7_Corsair_IIs).
The pasted description's own Aerial Visuals fix, 40.390672 -80.594217, is byte-for-byte the
Weirton site coordinate; the Burlington Township row carries that same Weirton coordinate in its
text while sitting at 40.067522 -74.827031. Self-refuting paste.
ACTION: delete id 25621, keep 25669

## 3. Bell AH-1F 67-15805 (c/n 20469)
VERDICT: B
CONFIDENCE: high
EVIDENCE: Aerial Visuals airframe dossier for s/n 67-15805 US, c/n 20469
(https://www.aerialvisuals.ca/AirframeDossier.php?Serial=7370, read 12 Sep 2026) gives
Latest Owner or Location = "American Legion Post 42, Charlotte, Michigan", with an
August 2007 transfer to that post recorded in the history. The c/n given is confirmed by the
AV AH-1 index (67-15781 = c/n 20445, +24 = 20469). Overpass found no aircraft node within
1500 m of either Michigan site, so OSM is silent rather than contradictory. The Mount Clemens
Post 4 row is a paste onto a similarly-numbered Legion post.
ACTION: delete id 26815, keep 26795

## 4. Lockheed C-130E 63-7877 (c/n 3948)
VERDICT: FALSE-COLLISION
CONFIDENCE: high
EVIDENCE: Joe Baugher, USAF serials 1963 (https://www.joebaugher.com/usaf_serials/1963.html):
"7877 (MSN 382-3948) ... 8/09: 182nd Airlift Wing Unit, Peoria, IL for static display.
Now displayed in air park at Illinois ANG base, Peoria, Illinois."
Baugher, 1962 (https://www.joebaugher.com/usaf_serials/1962.html):
"1862 (MSN 382-3826) ... Put on display at Scott Field Heritage Airpark at Scott AFB, IL
May 21, 2009." Two different airframes: c/n 382-3948 belongs to 63-7877 at Peoria; the Scott
Field aircraft is 62-1862, c/n 382-3826. The Scott Field record simply carries the wrong c/n.
ACTION: keep both; correct c/n on id 26668 from 3948 to 382-3826 (or blank it), and set
c/n 382-3948 on id 26675

## 5. Republic F-105D 60-0455 (c/n D143)
VERDICT: B
CONFIDENCE: high
EVIDENCE: Wikipedia, List of surviving Republic F-105 Thunderchiefs
(https://en.wikipedia.org/wiki/List_of_surviving_Republic_F-105_Thunderchiefs):
60-0455 at "Veteran's Memorial Park, Dixon, Illinois. (Moved from Jackson, Mississippi in 2009
and restored to Vietnam era camouflage markings.)" The only other Illinois F-105 listed is
61-0099 at Sugar Grove; no F-105 is recorded at Oglesby. The Oglesby row repeats the Dixon
row's text word for word, including its claim about "an OpenStreetMap node at this fix".
ACTION: delete id 26713, keep 26694

## 6. Republic F-84F 51-9444 (c/n unknown)
VERDICT: FALSE-COLLISION
CONFIDENCE: high
EVIDENCE: The two rows share no identity — Seminole Valley Park holds 51-9444, Hancock Field
holds a machine recorded as 46-600. The only shared field is the literal placeholder string
`unknown` in the c/n column of id 24421 (matched against a NULL c/n on id 27143). The Hancock
Field description is itself a different airframe's history (20th FG / Massachusetts ANG 101st FS /
127th PTG / 3750th TTW, ex-Lackland). Note the same id 24421 collides identically in conflict 7
against a third, different serial (51-1662) — proof the key is a placeholder, not an airframe.
ACTION: keep both; null the c/n on id 24421 (replace the literal `unknown` with NULL)

## 7. Republic F-84F 51-1662 (c/n unknown)
VERDICT: FALSE-COLLISION
CONFIDENCE: high
EVIDENCE: Same mechanism as conflict 6 and the same B record (id 24421, c/n literal `unknown`,
tail 46-600). Mayville's aircraft is 51-1662 per the NMUSAF July 2015 loan register cited on the
row; Hancock Field's is a different serial entirely. One record cannot be two serials, so the
collision is on the placeholder string.
ACTION: keep both; null the c/n on id 24421 (same fix as conflict 6)

## 8. FMA IA-50B T-129 (c/n 22)
VERDICT: FALSE-COLLISION
CONFIDENCE: high
EVIDENCE: The two rows are different type series with independent construction-number sequences:
FMA/DINFIA IA-50 Guaraní II (A: T-129) and FMA IA-35 Huanquero (B: A-320, explicitly "IA-35 c/n 22"
in its own description). aeron-aves.blogspot.com catalogues IA-50 airframes by their own c/n run
(c/n 26 at Diamante, c/n 29 as LV-LAI at Aeroclub Paraná), confirming the IA-50 sequence is
separate from the IA-35 sequence. c/n 22 in an IA-50 series and c/n 22 in an IA-35 series are
two different aeroplanes.
ACTION: keep both; qualify the c/n fields by type (or null one) so IA-50 c/n 22 and IA-35 c/n 22
no longer key together. Do not delete either record.

## 9. Fairchild PT-26 N4732G (c/n 10846)
VERDICT: FALSE-COLLISION
CONFIDENCE: high
EVIDENCE: Different type series entirely — a Fairchild M-62/PT-26 Cornell trainer at the CAF
National Airbase versus a Fairchild C-119/R4Q twin-boom transport at the Don F. Pratt Memorial
Museum (its own description records serial 131679 as a USN R4Q-2 BuNo and already flags a
variant/serial conflict). Construction numbers are unique only within a series; PT-26 c/n 10846
and C-119 c/n 10846 are unrelated.
ACTION: keep both; null or type-qualify the c/n on one side (the PT-26 record 6951 has no
independently sourced c/n — null it there)

## 10. Grumman S-2 c/n 325C
VERDICT: BOTH
CONFIDENCE: high
EVIDENCE: aeron-aves (Aeronaves Preservadas en Argentina), post of 15 May 2023:
"S-2 Turbo Tracker en Espora BACE 06May23. 0703/2-AS-24, (S-2E) nº/construcción 325C, ex US Navy
como BuAer 153569" — c/n 325C is the Espora gate guard, photographed 6 May 2023.
Same blog, post of 19 Apr 2019, "Tracker Santa Romana": "Grumman S2F-3S Tracker, reg 0703/2-AS-24
(c/n 325C), **representado**. Aeronave original 0862/2-AS-29 ... Ingresado a la Argentina como
fuente de repuesto" — i.e. the Santa Romana machine merely *represents* 2-AS-24; it is really
0862/2-AS-29, imported as a spares source
(https://aeron-aves.blogspot.com/search?q=325C, read 12 Sep 2026).
Two real airframes; the identity 0703/2-AS-24 c/n 325C belongs to Espora.
ACTION: keep both; on id 11524 blank c/n 325C and demote tail 2-AS-24 to a "painted as" note,
recording the true identity 0862/2-AS-29. Keep id 11343 as 0703 c/n 325C.

## 11. Lockheed T-33A 53-6132 (c/n 580-9753)
VERDICT: B
CONFIDENCE: high
EVIDENCE: Aerial Visuals airframe dossier for s/n 53-6132 USAF, c/n 580-9753
(https://www.aerialvisuals.ca/AirframeDossier.php?Serial=14377, read 12 Sep 2026) gives
Latest Owner or Location = "Sequatchie County Veterans Memorial Park, Dunlap, Tennessee",
transferred there by May 2019. Overpass returns two unnamed historic=aircraft nodes plus a UH-1
node at the Dunlap coordinates and zero aircraft nodes at D'Iberville — consistent with the
A-4M and the T-33 both standing at Dunlap. Same paste pattern as conflicts 1 and 12.
ACTION: delete id 26247, keep 26199

## 12. Douglas TA-4J 159795 (c/n 14494)
VERDICT: B
CONFIDENCE: high
EVIDENCE: Aerial Visuals airframe dossier for TA-4J 159795 USN, c/n 14494
(https://aerialvisuals.ca/AirframeDossier.php?Serial=31718, read 12 Sep 2026) gives Latest Owner
or Location = "Veterans Memorial Park of Collegedale, off Apison Pike, Collegedale, Tennessee",
on loan there by 2015. D'Iberville has no aircraft in OSM and none in any source consulted.
Note that D'Iberville is paired here with Collegedale while conflicts 1 and 11 pair it with
Dunlap — a single site cannot have supplied three pasted airframes from two different Tennessee
parks, which confirms D'Iberville as the spurious destination in all three.
ACTION: delete id 26245, keep 26190

## 13. Bell UH-1H-BF c/n 10080 (67-18577)
VERDICT: BOTH
CONFIDENCE: low
EVIDENCE: Both airplane.museum rows trace to one source, aeron-aves.blogspot.com, which itself
publishes two mutually exclusive posts under the same identity:
- 19 Apr 2019, "UH Santa Romana (II)": "Bell UH-1H-BF, reg H-(?), (c/n 10080), N° serie 67-18577.
  Recibido como repuesto, (AMQ), (MNA). Se encuentra preservado en la estancia Santa Romana,
  con registro falso H-19. Fotografias 13Abr19."
- 12 Mar 2023, "Bell UH en la IMPA": "Bell UH-1H-BF, (c/n 10080) Fuerza Aerea Argentina.
  Nro de Serie 67-18577. Material didactico en la Escuela Tecnica Nº7 Taller Regional Quilmes.
  Fotografias 12Nov22."
(https://aeron-aves.blogspot.com/search?q=10080, read 12 Sep 2026)
A photographed Huey demonstrably stands at each site (Apr 2019 and Nov 2022 respectively), so
neither record should be deleted. The identity is the duplicated element, and the Santa Romana
post is the weaker of the two: it records the registration as "H-(?)" wearing a false H-19, i.e.
the c/n was inferred rather than read. amilarg.com.ar, the other Argentine reference, is blocked
by the egress proxy from here and could not be consulted.
ACTION: keep both; blank c/n 10080 / serial 67-18577 on id 11530 (Santa Romana) and retain them
on id 11325 (Quilmes). Flag id 11530 for a photographic data-plate re-check.

## 14. Bell UH-1H 67-17562 (c/n 9760)
VERDICT: B
CONFIDENCE: high
EVIDENCE: Aerial Visuals airframe dossier for s/n 67-17562 US, c/n 9760
(https://www.aerialvisuals.ca/AirframeDossier.php?Serial=72288, read 12 Sep 2026) gives
Latest Owner or Location = "American Legion Post 423, Orland, Indiana", with photographs dated
23 July 2017 at that location and a full US Army history (3/17 Cav Di An 1968, 142nd Trans Co
1971, ARADMAC Corpus Christi, Fort Rucker 1972). The c/n matches the AV index exactly
(67-17562 = c/n 9760). Charlotte Post 42 legitimately holds AH-1F 67-15805 (conflict 3) but not
this Huey; the blank-tailed Charlotte row is a paste onto a similarly-numbered Legion post.
ACTION: delete id 26794, keep 26768

## 15. Bell UH-1H 73-21687 (c/n unknown)
VERDICT: FALSE-COLLISION
CONFIDENCE: high
EVIDENCE: The two rows are different types at different serials — a UH-1H Huey, 73-21687, at the
McVille Dam veterans memorial in North Dakota, and a Cobra recorded as 70-16087 at American Legion
Post 285, Parkersburg, Iowa. Their only shared field is the literal placeholder `unknown` in the
c/n column of id 27160 (against a NULL c/n on id 27179); the B description states outright that
"no construction number [was] recorded by any source consulted". Nothing links the two airframes.
ACTION: keep both; null the c/n on id 27160 (replace the literal `unknown` with NULL)

---

## Counts
- A: 1 (conflict 2)
- B: 6 (conflicts 1, 3, 5, 11, 12, 14)
- BOTH: 2 (conflicts 10, 13)
- NEITHER: 0
- FALSE-COLLISION: 6 (conflicts 4, 6, 7, 8, 9, 15)
- UNRESOLVED: 0
