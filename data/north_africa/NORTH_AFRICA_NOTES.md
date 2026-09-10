# North Africa — Egypt, Tunisia, Algeria, Morocco, Libya, Sudan

42 sites, 100 airframes, imported September 2026. Greenfield: nothing from any
of these countries was in the database.

Egypt dominates — 21 of the 42 sites — and most of them are **single-airframe
roadside monuments**, not museums. That is the real shape of North African
aviation preservation: a national air force museum plus a long tail of MiGs and
Sukhois on plinths at town entrances, war memorials and roundabouts.

---

## Sources and their weight

**aviationmuseum.eu was the seed, as instructed, and it is a lead list and
nothing more.** Its pages carry "last page update" dates as old as December
2016, its Africa index links only Egypt, Tunisia and Sudan out of these six
countries, and where it does speak it is frequently wrong about type. It was
used to generate site names and candidate serials; every one was then checked
against something else.

The channel that actually produced this package was **an OpenStreetMap Overpass
sweep for `historic=aircraft` and `memorial=aircraft` across all six countries,
reverse-geocoded and then verified by pulling satellite tiles for each hit and
looking at them.** Most of the Egyptian monument population is invisible to
every aviation directory and visible on OSM and imagery. Dated photographs
(ABPic, airhistory.net, jetphotos) were weighted highest wherever they existed;
Esri World Imagery's per-tile acquisition dates were used to date satellite
confirmations rather than treating imagery as undated.

**Transliteration is a real problem in this region.** The same site appears as
Almaza / Al-Maza / El Maza, Bilbeis / Bilbays / Belbeis, Mersa Matruh / Marsa
Matrouh. Sites are recorded under the most common English form; other spellings
belong in a site-alias field the schema does not yet have.

---

## Country by country

**Egypt** is the only country in the region with a substantial curated
collection — the Egyptian Air Force Museum at Almaza. The National Military
Museum at the Citadel and the 6th of October Panorama both hold aircraft as part
of broader military displays. Everything else is monuments: MiG-17s, MiG-21s,
Su-7s, Su-20s and Su-17s on plinths from Alexandria to Hurghada, plus base gate
guards at Helwan, Inshas, Cairo West and the Air Force Academy at Bilbeis.

**Tunisia** yielded seven sites, and the interesting finding is that most are
*not* military: a science centre, a lycée, and two town displays. The Musée
Militaire National at the Palais de la Rose in Manouba is the anchor.

**Algeria** yielded five, centred on the Musée Central de l'Armée in Algiers and
the martyrs' memorial museums. Note that the Musée de l'Armée Populaire de
Libération Sahraouie is at Rabuni **in the Sahrawi refugee camps near Tindouf**
— it is filed under Algeria because that is where it physically stands, which is
the database's rule (record where an aircraft is, not who owns it), but the
institution is Sahrawi, not Algerian.

**Morocco** yielded five, all `restricted`: the Royal Air Maroc museum at the
former Anfa airport and four air base displays. The Musée Royal Air Maroc is
recorded `restricted` rather than `public` because access is by arrangement
through the airline, not walk-up.

**Libya is one site.** The Tobruk Museum, `restricted`. This is the expected
result: what existed was largely destroyed or dispersed after 2011, and nothing
verifiable survives in the public record. Treat Libya as effectively
unrecoverable from open sources rather than as unsearched.

**Sudan is three sites** and all of them are provisional. The civil war since
April 2023 has been fought across Khartoum and Omdurman, the Sudan Military
Museum is in Khartoum North, and Wadi Seidna air base has been a front line.
These three rows record what was there before the war; **none has been confirmed
since 2023.**

---

## Judgment calls

**Monuments are records.** Twelve Egyptian sites are a single aircraft on a
plinth at a town entrance or roundabout. That is exactly the class of site the
methodology says must not be dismissed, and they are the majority of what
survives in this region.

**Access type judged by how a visitor actually gets in.** The Egyptian Air Force
Museum is `public` — normal ticketed admission, despite sitting on Almaza air
base. Every roadside monument is `public`. Base gate guards at Helwan, Inshas,
Cairo West, Bilbeis, Gafsa, Meknes, Marrakech, Kenitra, Rabat-Salé and Blida are
`restricted` — inside controlled military gates, not visible from a public road.
The Luxor Military Aircraft Display is `restricted` (airside/military side) while
the Luxor MiG-17 Monument 2 km away is `public`; they are two separate records
because they are two separate places.

**Coordinates are satellite fixes or mapped features, never town centroids.**
Where no fix could be made, the coordinate is blank. Wadi Seidna is the one
coarse coordinate in the set (15.81, 32.51 — an airfield reference point, not a
fix on an airframe) and it is flagged here rather than presented as precise.

---

## Deliberate blanks

**`year_built` is blank on all 100 rows.** No construction, rollout, first-flight
or delivery date was sourced for any airframe in this region. Soviet-bloc
construction numbers were not converted into years.

**Serials are blank on most monument rows.** Egyptian, Tunisian, Algerian and
Moroccan monument airframes are typically repainted in a squadron scheme with no
legible serial, and satellite imagery cannot read one. Blank is the honest
answer; where a directory offered a serial that could not be corroborated, it was
left out of `tail_number` and the doubt noted in the description.

**Postal codes are blank except where a source stated one** (Cairo 11636 and
11811, Port Said 42512, Manouba 2087, Algiers 16000, Casablanca 20200, Khartoum
North 13311). No North African postal code was guessed or reverse-geocoded.

---

## Excluded, and why — do not re-research these

**Port Said Military Museum** was researched and confirmed to exist, but **no
individual airframe could be named**, so no site record was created. A site with
no aircraft is not useful in this database. If someone photographs its aircraft
the site is worth adding.

**Operational and stored aircraft** across all six countries. Egypt in
particular has large stored MiG-21 and F-4 populations that circulate in lists as
"preserved"; stored is not displayed.

**Libya beyond Tobruk.** Aircraft that existed at Tripoli and Benghazi before
2011 are not recorded because none could be confirmed to survive. Named as an
absence rather than omitted silently.

---

## Ranked open questions

1. **Has anything at the Sudan Military Museum, the Khartoum MiG-21 monument or
   Wadi Seidna survived the war since April 2023?** All three rows predate the
   fighting. This is the least certain group in the package by a wide margin.
2. **A full serial pass on the Egyptian Air Force Museum.** The collection is
   the largest in North Africa and most of its airframes are recorded without a
   serial. One visit with a camera would transform the Egyptian data.
3. **Are the Egyptian monument airframes still on their plinths?** Twelve of
   them rest on OSM plus satellite. Satellite confirms an aircraft shape on a
   plinth; it cannot confirm the type or the serial.
4. **What is at Port Said?** See exclusions.
5. **Libya.** Everything. If any Libyan collection survives, nothing in the open
   record says so.
6. **Morocco's Musée Royal Air Maroc access.** Recorded `restricted` on the
   basis that access is arranged through the airline; if it now admits walk-up
   visitors it should be `public`.
