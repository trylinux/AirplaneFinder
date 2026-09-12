# MEXICO — Museums, Base Collections and Monuments (single pass; all phases)

Database had ZERO records for Mexico. `region` is the literal string `North America` on every
row per the brief's override of the contract's `Europe` default.

Research was done in Spanish throughout. Sources that actually carried this pass are listed in
NOTES; the single most important environmental constraint is that **general web search was
unavailable for this run** (the session's WebSearch quota was already spent, and Bing, DuckDuckGo,
Startpage, Mojeek, Brave, Ecosia and every reachable SearxNG instance returned bot-challenges or
poisoned/irrelevant result sets through this proxy). Everything below therefore rests on
OpenStreetMap/Overpass, Nominatim, the OSM API changeset history, Spanish and English Wikipedia
(full-text `insource:` search + raw wikitext), Wikimedia Commons category and file metadata,
Wikidata, the Historical Marker Database (hmdb.org, reachable only through WebFetch) and a small
number of directly-fetched Mexican pages. This is a good skeleton, not a finished census —
see "Needs a human".

## SITES

### ===================== MUSEUMS =====================

name: Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía
city: Santa Lucía (Zumpango)
state_province: Estado de México
country: Mexico
postal_code: 55755
region: North America
address: Carretera Federal México-Pachuca s/n; interior de la Base Aérea Militar No. 1 / Ciudad Militar Santa Lucía; junto al Aeropuerto Internacional Felipe Ángeles (AIFA)
website: https://www.gob.mx/sedena/acciones-y-programas/atencion-al-publico-museo-militar-de-aviacion-b-a-m-no-1-sta-lucia-edo-mex
access_type: public
latitude: 19.742600
longitude: -98.986700
source: es.wikipedia "Museo Militar de Aviación (México)"; en.wikipedia "Mexican Air Force Museum"; OpenStreetMap way 1073649398 ("Museo Miliar de Aviación", tourism=museum, sic — the OSM name is misspelled); Editorial GEA / Revista Armas "Museo Militar de Aviación" (2022-03-25); México Desconocido "El impresionante museo de la Fuerza Aérea Mexicana" (fetched 2026-09-10, gives free entry and Tue-Sun 09:00-16:00); Obras por Expansión 2022-02-10; Wikimedia Commons Category:Aircraft at the Mexican Air Force Museum
confidence: high — this is the FAM's own national museum, opened 10 February 2022 (FAM's 107th anniversary) in a purpose-built replacement for the hangar display it had kept in the Escuadrón Aéreo 302 hangar from 2000. Reorganisation confirmed: the OLD museum building was demolished/relocated for AIFA construction; the new one was built Oct 2020 – Feb 2022 a few hundred metres from the AIFA landside, next to the Museo del Mamut and the Museo Paleontológico de Santa Lucía Quinamétzin. Free entry, Tue-Sun 09:00-16:00, ~50 aircraft inside and outside. Most recent evidence: OSM survey 2024-2025 and the Wikipedia article as of 2026-09. Individual airframe serials are only sporadically published — see NOTES.

name: Museo del Ejército y Fuerza Aérea Mexicanos (MUEFA) -- Coyoacán
city: Ciudad de México
state_province: Ciudad de México
country: Mexico
postal_code: 04220
region: North America
address: Calzada de Tlalpan 1838; Colonia Churubusco Country Club; Alcaldía Coyoacán
website: https://www.gob.mx/sedena/acciones-y-programas/museo-del-ejercito-y-fuerza-aerea-cd-de-mex
access_type: public
latitude: 
longitude: 
source: es.wikipedia "Museo del Ejército y Fuerza Aérea Mexicanos (Coyoacán)"; SEDENA gob.mx programme page; INAH catalogue number I-0013600100
confidence: medium — museum existence, address, SEDENA ownership and Tue-Sun 10:00-17:00 hours are well documented (opened 13 September 2010 in the 1906 tram substation). It is named in the English Wikipedia T-33 survivor list as one of the places where FAM T-33s are displayed, but NO specific airframe could be tied to it in this pass, so it carries no aircraft rows. Coordinates deliberately blank — I could not find a sourced coordinate and would not guess one.

name: Museo del Ejército y Fuerza Aérea Mexicanos (Bethlemitas) -- Ciudad de México
city: Ciudad de México
state_province: Ciudad de México
country: Mexico
postal_code: 06060
region: North America
address: Calle Filomeno Mata 6 (esq. Tacuba); Ex templo de Betlemitas / Edificio Don Osorio; Centro Histórico; Alcaldía Cuauhtémoc
website: 
access_type: public
latitude: 19.435382
longitude: -99.138988
source: es.wikipedia "Museo del Ejército y Fuerza Aérea Mexicanos (Bethlemitas)"; OpenStreetMap way 526236375; Nominatim confirmation 2026-09-10; INAH I-09-02095 / I-09-00924
confidence: medium-high as a SITE (opened 15 September 1991; Tue-Sat 10:00-18:00; Sun and holidays 10:00-16:00). No airframes: the aviation content is the gallery "La Fuerza Aérea Expedicionaria" — documents, uniforms and models, not aircraft. Recorded because it is one of the Escuadrón 201 commemoration sites the brief asked for.

name: Museo del Ejército y Fuerza Aérea Mexicanos -- Puebla
city: Puebla de Zaragoza
state_province: Puebla
country: Mexico
postal_code: 72000
region: North America
address: Avenida 3 Poniente; Centro Histórico de Puebla
website: https://museospuebla.puebla.gob.mx/museos/item/6-museo-del-ejercito-y-fuerza-aerea
access_type: public
latitude: 19.048410
longitude: -98.207840
source: OpenStreetMap node 4320083590 (museum=military, opening_hours Tu-Fr 10:00-17:00; Sa-Su 10:00-16:00, website tag); Nominatim 2026-09-10; mexicoescultura.com listing
confidence: medium — a real SEDENA military museum with an official state tourism page; no aircraft could be attributed to it in this pass. Included for completeness of the MUEFA network the brief listed.

name: Museo del Ejército y Fuerza Aérea Mexicana (Cuartel Colorado) -- Guadalajara
city: Guadalajara
state_province: Jalisco
country: Mexico
postal_code: 44890
region: North America
address: Calle Valentín Gómez Farías 600 (entre Calzada del Ejército y Riva Palacio); Colonia Reforma
website: 
access_type: public
latitude: 20.669358
longitude: -103.332548
source: OpenStreetMap way 450906329 (operator=SEDENA); El Informador "Por los pasillos del Cuartel Colorado" 2015-07-05 (fetched 2026-09-10 — gives free entry with registration; Tue-Sat 10:00-18:00; Sun and holidays 10:00-16:00; phone 36183974); en.wikipedia "IAI Arava" survivors list
confidence: medium — the IAI Arava 201 on the museum's outdoor plot is confirmed by two independent sources (El Informador feature and the Wikipedia survivor list). Serial not published in either. Most recent hard evidence is the 2015 El Informador piece plus OSM; a 2025-26 status check was not possible.

name: Museo del Concorde -- Ciudad Juárez
city: Ciudad Juárez
state_province: Chihuahua
country: Mexico
postal_code: 32470
region: North America
address: Avenida Antonio J. Bermúdez 2050; Parque Industrial Bermúdez
website: http://www.museodelconcorde.com/
access_type: public
latitude: 
longitude: 
source: es.wikipedia "Museo del Concorde"; en.wikipedia "Museo del Concorde"; El Diario de Juárez 2024-05-22 "Regresa a la frontera Museo del Concorde"
confidence: medium — the collection (over 200 components ex-British Airways acquired 2004 via Dovebid: a Rolls-Royce/Snecma Olympus 593, a Snecma twin intake, the left main landing gear, control columns and seats) is a genuine aerospace museum but contains NO airframe, so it carries zero aircraft rows. English Wikipedia files it under "Defunct museums in Mexico" while simultaneously citing a May 2024 El Diario story headlined "Regresa a la frontera" — i.e. it appears to have reopened/relocated in 2024. Status genuinely unresolved; coordinates blank.

name: Museo Descubre. Centro Interactivo de Ciencia y Tecnología -- Aguascalientes
city: Aguascalientes
state_province: Aguascalientes
country: Mexico
postal_code: 20277
region: North America
address: Avenida San Marcos / Avenida del Parque s/n; Fraccionamiento Jardines de Alejandría
website: 
access_type: public
latitude: 21.856170
longitude: -102.289260
source: es.wikipedia "Museo Descubre" ("exponer aviones antiguos donados por la Fuerza Aérea Mexicana"); OpenStreetMap node 5515611735 (historic=monument "Avion") sitting 33 m from the museum node; Nominatim 2026-09-10
confidence: medium — the museum is unambiguous (opened 20 November 1996; IMAX 4D dome; planetarium). Spanish Wikipedia states plainly that it displays old aircraft donated by the Mexican Air Force, and OSM independently maps an aircraft monument on the forecourt. NEITHER source names a type or serial, so the airframe row is Unidentified. Wikipedia's phrasing is plural ("aviones") — there may be more than one.

name: Museo Francisco Sarabia -- Ciudad Lerdo
city: Ciudad Lerdo
state_province: Durango
country: Mexico
postal_code: 35150
region: North America
address: Boulevard Miguel Alemán / Calle Matamoros; Centro; junto al Parque Avión Sarabia
website: 
access_type: public
latitude: 25.542911
longitude: -103.520936
source: OpenStreetMap way 462665392 (tourism=museum "Museo Francisco Sarabia"), way 733400463 (leisure=park "Avion Sarabia") and node 4580384450 (historic=memorial memorial=statue "Piloto Aviador Francisco Sarabia") — all three within 25 m of each other; Nominatim 2026-09-10; es.wikipedia "Francisco Sarabia Tinoco" and "Conquistador del Cielo"
confidence: medium for the SITE (a municipal museum to Lerdo's most famous son, the record-breaking airline pioneer killed in the Potomac on 7 June 1939, with an adjoining park literally called "Avión Sarabia"). LOW for what airframe is there: the Granville/Miller & DeLackner R6H Q.E.D. "Conquistador del Cielo" (ex-NR14307/NX14307, Mexican registration XB-AKM) is the airframe universally associated with Sarabia and the park name strongly implies an aircraft is displayed, but NEITHER Spanish Wikipedia article states the aircraft's current location and I could not confirm it independently in this pass. See "Needs a human" — this is the single highest-value open question in Mexico.

### ===================== AIR BASES AND SERVICE SCHOOLS =====================

name: Base Aérea Militar No. 4 General Eduardo Aldasoro Suárez -- Cozumel
city: San Miguel de Cozumel
state_province: Quintana Roo
country: Mexico
postal_code: 77600
region: North America
address: Avenida Rafael E. Melgar; frente al acceso de la Base Aérea Militar No. 4 (co-located with Cozumel International Airport)
website: 
access_type: public
latitude: 20.521010
longitude: -86.942830
source: Historical Marker Database markers m101633 (Lockheed T-33; 20°31.261'N 86°56.57'W; erected 2010; photographed 2017-01-15), m101634 (North American T-28A Trojan; 20.52143611 -86.94285556) and the "Tribute to the 201st Squadron of the Mexican Expeditionary Force" marker (20.52110556 -86.94303889); en.wikipedia "List of displayed Lockheed T-33 Shooting Stars" (T-33 4019 at BAM No. 4)
confidence: high for the display line and its position — three dated, photographed, coordinate-bearing markers on the PUBLIC seafront boulevard outside the base gate, not inside the wire, which is why access_type is `public` and not `restricted`. Most recent photographic evidence 2017; the markers were erected in 2010 for the Bicentenario. Note that Escuadrón 201's post-war home base was Cozumel, which is why the 201 tribute stands here.

name: Colegio del Aire / Base Aérea Militar No. 5 -- Zapopan
city: Zapopan
state_province: Jalisco
country: Mexico
postal_code: 45201
region: North America
address: Avenida Base Aérea Militar s/n; La Cañada / Nuevo México; Base Aérea Militar No. 5 "C.P.A. Emilio Carranza Rodríguez"
website: 
access_type: restricted
latitude: 20.754000
longitude: -103.449550
source: es.wikipedia "Base Aérea Militar N.º 5 de Zapopan" (carries the two display photographs with serials in their captions); Wikimedia Commons File:T-33 EMA.JPG and File:DH-100 EMA.JPG (both photographed 2014-08-12, described as "exhibido en el Colegio del Aire"); en.wikipedia "De Havilland Vampire"; OpenStreetMap node/way "Colegio del Aire" amenity=university operator="Universidad del Ejército y Fuerza Aérea"; Nominatim 2026-09-10
confidence: medium-high — two airframes are photographically documented on the Colegio del Aire grounds with legible serials. Access is `restricted`: this is inside an active air base and military academy; the public sees these only on open days (the Espectáculo Aéreo Jalisco and graduation ceremonies). Most recent airframe photograph is 2014.

name: Base Aérea Militar No. 6 de Terán -- Tuxtla Gutiérrez
city: Tuxtla Gutiérrez
state_province: Chiapas
country: Mexico
postal_code: 29020
region: North America
address: Calle 3 Poniente Sur; Terán; antiguo Aeropuerto Nacional Francisco Sarabia (ICAO MMTB); ahora Base Aérea Militar "Gral. Div. P.A. Ángel Hipólito Corzo Molina"
website: 
access_type: restricted
latitude: 16.740180
longitude: -93.172880
source: en.wikipedia "IAI Arava" survivors list (Arava 201 serial 3015 c/n 53 "on display outside the Base Aérea Militar N.º 6 de Terán"); es.wikipedia "Base Aérea Militar N.º 6 de Terán"; Nominatim/OSM aerodrome node 2026-09-10
confidence: medium for the airframe (a single uncited Wikipedia survivor entry, though it carries a specific serial AND construction number, which is the pattern of a real airframe record rather than an invention); high for the base itself. Coordinate given is the aerodrome centroid from OSM, not the airframe's own position — the Wikipedia entry says "outside" the base, so the plinth is probably on the perimeter road. access_type `restricted` pending confirmation of which side of the fence it stands on. NOTE: from 1 March 2026 the FAM renamed its Bases Aéreas Militares to Zonas Aéreas Militares; BAM-6 is now the 15a Zona Aérea Militar.

name: 22a Zona Militar -- Toluca
city: Toluca
state_province: Estado de México
country: Mexico
postal_code: 
region: North America
address: 22a Zona Militar; cerca de Toluca
website: 
access_type: restricted
latitude: 
longitude: 
source: en.wikipedia "IAI Arava" survivors list (Arava 201 serial 3014 c/n 52 "on display near Toluca, at the 22a Military Zone")
confidence: low — one uncited Wikipedia line with a specific serial and c/n. Not corroborated, not in OSM, no coordinate found. Recorded so a later pass does not lose the lead; do not treat the position as established.

### ===================== MONUMENTS AND PUBLIC DISPLAYS =====================

name: Parque Temático Militar -- Zacatecas
city: Zacatecas
state_province: Zacatecas
country: Mexico
postal_code: 98068
region: North America
address: Tiro San Antonio; Zacatecas
website: 
access_type: public
latitude: 22.763020
longitude: -102.559950
source: OpenStreetMap way 633811513 (historic=aircraft "Avión"), way 633811512 (historic=aircraft "Helicóptero"), way 633811514 (historic=memorial "Tanques") and way 633811511 (historic=monument "Bandera de Mexico"), all inside the park polygon named "Parque Temático Militar"; Nominatim 2026-09-10
confidence: medium — a SEDENA-style open-air military theme park with one fixed-wing aircraft, one helicopter, tanks and a monumental flag, all mapped as separate ways (i.e. traced from imagery as physical objects, not points of interest). Neither aircraft is typed or serialled anywhere I could reach, so both rows are Unidentified. Free public park.

name: Parque Tangamanga II military display -- San Luis Potosí
city: San Luis Potosí
state_province: San Luis Potosí
country: Mexico
postal_code: 78140
region: North America
address: Calle Tercera de Adolfo López Mateos; Fraccionamiento Mártires de la Revolución; interior del Parque Tangamanga II
website: 
access_type: public
latitude: 22.184753
longitude: -100.979703
source: OpenStreetMap node 4509439281 (historic=aircraft tourism=attraction aircraft:type=military name="Pilatus PC-7"); adjacent OSM nodes "V.B. MEX-1", "V.B. MOWAG ROLAND", "V.B. HERCULES M-8" and two Humvees (all historic=tank tourism=attraction) within 45 m; Nominatim 2026-09-10
confidence: medium-high that a Pilatus PC-7 is displayed here — the OSM node is explicitly named for the type and sits in a coherent line of five named armoured vehicles, which is the signature of a donated SEDENA display, not a mis-tag. No serial published. PC-7s were the FAM's standard trainer and light attack aircraft (and the type flown by the modern Escuadrón 201), so the identification is intrinsically plausible.

name: Boeing 727 XC-FPA y Super Puma de la Policía Federal -- San Luis Potosí
city: San Luis Potosí
state_province: San Luis Potosí
country: Mexico
postal_code: 78294
region: North America
address: Avenida Los Álamos / Avenida Planetario; Fraccionamiento Garita de Jalisco
website: 
access_type: public
latitude: 22.131045
longitude: -101.007123
source: OpenStreetMap node 6157578853 (historic=aircraft tourism=attraction name="XC-FPA" aircraft:type="B727-264 (Adv.) MSN 22413" operator="Policía Federal" website=https://www.jetphotos.com/info/727-22413) and node 6157578852 (historic=aircraft "AS-322 Super Puma" operator="Policía Federal") 35 m away
confidence: medium-high — the OSM mapper recorded a registration, a full sub-type AND a manufacturer's serial number, and cited a JetPhotos airframe page for it; that is an unusually well-evidenced monument node. Both airframes are ex-Policía Federal (the force was dissolved in 2019 and its aircraft dispersed), displayed in a public open space next to Avenida Planetario. Not visited/verified 2025-26.

name: Douglas DC-3 cine -- San Luis Potosí
city: San Luis Potosí
state_province: San Luis Potosí
country: Mexico
postal_code: 78294
region: North America
address: Avenida Laberinto; Colonia Las Rosas (junto al Museo Laberinto de las Ciencias y las Artes / Parque Tangamanga I)
website: 
access_type: public
latitude: 22.129871
longitude: -100.996191
source: OpenStreetMap node 4741964609 (historic=aircraft tourism=attraction aircraft:type=DC-3 name="DC-3" note="Converted to some kind of cinema"); Nominatim 2026-09-10
confidence: medium — a DC-3 converted into a small cinema and publicly visitable, which the contract explicitly counts as a display record. No registration recorded by the mapper. Sits within an art/science precinct (nearby OSM artworks "Venus", "Eclipse Solar", "Campana Rotaria").

name: Aeroparque Orizaba -- Boeing 727 El Cuatro Vientos
city: Orizaba
state_province: Veracruz
country: Mexico
postal_code: 94300
region: North America
address: Prolongación Norte 2 / Avenida Oriente 39; Colonia Los Naranjos
website: 
access_type: public
latitude: 18.867530
longitude: -97.113230
source: OpenStreetMap node 13541713869 (historic=aircraft) and a coincident way tagged tourism=gallery, both named Boeing 727-200 "El Cuatro Vientos", inside the polygon leisure=park "Aeroparque Orizaba" (way, 7 m away); Nominatim 2026-09-10
confidence: medium-high — a municipal aeropark built around a preserved Boeing 727-200 that has been repurposed as a gallery/exhibition space; two independent OSM objects (the airframe and the gallery use) plus a named park polygon. Registration NOT recorded; the name "El Cuatro Vientos" is the aircraft's display name honouring the 1933 Barberán/Collar Spain-Mexico flight, not a registration. Orizaba's municipal site could not be fetched (404) to date the current state.

name: Parque Centenario de la Fuerza Aérea -- Tuxtla Gutiérrez
city: Tuxtla Gutiérrez
state_province: Chiapas
country: Mexico
postal_code: 29060
region: North America
address: Calle 16a Poniente Norte / Avenida Sauce; Tuxtla Gutiérrez
website: 
access_type: public
latitude: 16.757820
longitude: -93.131900
source: OpenStreetMap node 13514712585 (historic=aircraft "Avión Pilatus PC-7"), node "Monumento al Teniente Piloto Aviador José Espinosa Fuentes" (tourism=artwork, 19 m away) and the park polygon "Parque Centenario de la Fuerza Aérea" (104 m); Nominatim 2026-09-10
confidence: medium-high — a municipal park explicitly dedicated to the FAM centenary (2015), with a Pilatus PC-7 on display beside a monument to Tte. P.A. José Espinosa Fuentes. Espinosa Fuentes is the Escuadrón 201 pilot for whom the national MUMA at Santa Lucía is named; he is commemorated here because Chiapas claims him. This is therefore one of the Escuadrón 201 commemoration sites the brief asked to be found. No serial published.

name: Monumento a la Fuerza Aérea Expedicionaria -- Monterrey
city: Monterrey
state_province: Nuevo León
country: Mexico
postal_code: 64860
region: North America
address: Boulevard Acapulco / Avenida Eugenio Garza Sada; Colonia Las Brisas
website: 
access_type: public
latitude: 25.626100
longitude: -100.276930
source: OpenStreetMap node 13753594081, historic=aircraft, name "Fuerza Aérea Expedicionaria", created 2026-04-22 by mapper "Juan MAS" (5576 changesets) in changeset 181691627; Nominatim reverse geocode 2026-09-10
confidence: low-medium — a named aircraft monument to the Fuerza Aérea Expedicionaria Mexicana (i.e. Escuadrón 201) on a major Monterrey avenue, mapped four months before this pass by an experienced local mapper. The name is specific enough to be trusted as a monument; the airframe type is completely unrecorded, so the row is Unidentified. Given the dedication, a P-47 replica or a T-6/T-28 standing in for one is the likeliest content — but that is a guess and is NOT recorded as fact.

name: Avión Biblioteca -- Utopía Teotongo Iztapalapa
city: Ciudad de México
state_province: Ciudad de México
country: Mexico
postal_code: 09800
region: North America
address: Calle Villa Feliche; Colonia Carlos Hank González; Utopía Teotongo; Alcaldía Iztapalapa
website: 
access_type: public
latitude: 19.329567
longitude: -99.043640
source: OpenStreetMap node 12953068686 (amenity=library, name "Avión Biblioteca"); Nominatim 2026-09-10; Wikimedia Commons Category:Utopía Teotongo - Avión Biblioteca
confidence: medium-high as a site — an airliner fuselage converted into a public lending library inside one of Iztapalapa's "Utopías" (the borough's flagship public-space programme), exactly the "aircraft converted into a public facility and publicly visitable" case the contract says to record. Type and registration NOT established: the Commons category exists but was not enumerable through the API in this pass and no source names the airframe.

name: Monumento C-47 El Mexicano -- Ciudad de México
city: Ciudad de México
state_province: Ciudad de México
country: Mexico
postal_code: 15670
region: North America
address: Avenida Adolfo López Mateos; Colonia Adolfo López Mateos; Alcaldía Venustiano Carranza; junto al Hangar Presidencial del AICM
website: 
access_type: public
latitude: 19.423332
longitude: -99.074524
source: OpenStreetMap node 1445924929, historic=monument, name "C47 - El Mexicano", description "Primer avión presidencial"; the node sits 120 m from the OSM landuse=military polygon "Hangar Presidencial" and 236 m from "Dirección General de Servicios Aéreos CDMX"; Nominatim 2026-09-10
confidence: low-medium AND FLAGGED AS A CONFLICT. Both the Spanish and English Wikipedia articles on the MUMA state that the DC-3 "El Mexicano", Mexico's first presidential aircraft, is displayed AT THE MUSEUM in Santa Lucía. OSM independently maps a monument of the same name and the same description next to the presidential hangar at Mexico City airport. Possible readings: (a) the OSM node is a stale record of where the aircraft stood before the 2020-22 move to Santa Lucía; (b) the airport monument is a separate memorial/marker and the airframe itself is at MUMA; (c) there are two C-47s. I have recorded the airframe row ONCE, at MUMA, and recorded this location as a site with no airframe row, to avoid double-counting the same aircraft. See "Needs a human".

name: Avión monumento -- Town Center Zumpango
city: Zumpango
state_province: Estado de México
country: Mexico
postal_code: 55635
region: North America
address: Calle Lago Sur; Town Center Zumpango
website: 
access_type: public
latitude: 19.790486
longitude: -99.055865
source: OpenStreetMap node 5388458431 (historic=monument, name "Avion"); Nominatim 2026-09-10
confidence: low — an aircraft monument in the open-air retail centre at Zumpango, 12 km from Santa Lucía air base, which makes an ex-FAM donation plausible. Nothing beyond the OSM node; type and serial unknown.

name: Plaza Avión Militar -- Monclova
city: Monclova
state_province: Coahuila
country: Mexico
postal_code: 25700
region: North America
address: Boulevard Ejército Mexicano; Colonia Los Reyes
website: 
access_type: public
latitude: 26.927974
longitude: -101.430933
source: OpenStreetMap node 4193235576 (historic=monument, name "Plaza Avión Militar"); Nominatim 2026-09-10
confidence: low-medium — the name is explicit ("Military Aircraft Plaza") and it stands on Boulevard Ejército Mexicano, the classic location for a donated FAM gate-guard-style monument. Type and serial unknown.

name: Monumento Avioneta de la Fuerza Aérea Mexicana -- Zacatlán
city: Zacatlán
state_province: Puebla
country: Mexico
postal_code: 73316
region: North America
address: Paseo de la Barranca; Zacatlán de las Manzanas
website: 
access_type: public
latitude: 19.931690
longitude: -97.956461
source: OpenStreetMap node 12588064395 (historic=monument, name "Fuerza Aérea Mexicana Avioneta"); adjacent restaurant "La Avioneta" (17 m) named for it; Nominatim 2026-09-10
confidence: low-medium — an explicitly FAM-attributed light aircraft monument on Zacatlán's clifftop promenade, with a neighbouring restaurant named after it (which is good evidence the aircraft is a real local landmark rather than a mis-tag). Type and serial unknown; "avioneta" means a light aircraft, so a Cessna/Bellanca-class trainer or a PT-17 is likelier than a jet.

name: Monumento Helicóptero -- Ciudad Fernández
city: Ciudad Fernández
state_province: San Luis Potosí
country: Mexico
postal_code: 79650
region: North America
address: Avenida Moctezuma; junto a la Unidad Deportiva de Ciudad Fernández
website: 
access_type: public
latitude: 21.947516
longitude: -100.024059
source: OpenStreetMap node 5323225876 (historic=monument, name "Helicóptero"); Nominatim 2026-09-10
confidence: low — a helicopter monument beside the municipal sports ground. No type, no serial. Mexican municipal helicopter monuments are most often ex-FAM/ex-Policía Bell 206/212 or MD 500, but nothing here is established.

name: Parque de la Avioneta -- Ecatepec de Morelos
city: Ecatepec de Morelos
state_province: Estado de México
country: Mexico
postal_code: 55020
region: North America
address: Segunda Cerrada de Allende / Avenida Insurgentes; Ecatepec de Morelos
website: 
access_type: public
latitude: 19.595180
longitude: -99.044770
source: OpenStreetMap way (leisure=park, name "Parque de la Avioneta"); Nominatim 2026-09-10
confidence: low — the park is named for a light aircraft and is 172 m from a street named "Privada Primera Francisco Sarabia", but NO aircraft object is mapped inside it and no other source confirms an airframe is still present. Recorded as a lead, with one Unidentified row, precisely because Mexican park names of this kind usually do commemorate a physically present airframe. Could equally be a name that outlived the aircraft — flagged.

name: Parque La Avioneta -- Tulancingo de Bravo
city: Tulancingo de Bravo
state_province: Hidalgo
country: Mexico
postal_code: 43640
region: North America
address: Avenida Ahuehuetitla; Colonia Ahuehuetitla
website: 
access_type: public
latitude: 20.083320
longitude: -98.417260
source: OpenStreetMap way (leisure=park, name "La avioneta"); Nominatim 2026-09-10
confidence: low — same reasoning and same caveat as Ecatepec above. Tulancingo hosts a significant FAM presence historically, which makes a donated airframe plausible, but no airframe object is mapped.

name: Boeing 737 EI-DNZ -- Instituto Tecnológico de Tijuana
city: Tijuana
state_province: Baja California
country: Mexico
postal_code: 22410
region: North America
address: Avenida Castillo de Chapultepec s/n; Tomás Aquino / Mesa de Otay; Instituto Tecnológico de Tijuana
website: 
access_type: appointment
latitude: 32.531571
longitude: -116.986046
source: OpenStreetMap way 754689811 (historic=aircraft + building=yes) with the Nominatim display name "B737-3TO EI-DNZ"; adjacent OSM objects "Laboratorio de Aeronáutica" (88 m), "Laboratorio de Aeronautica ITT" (115 m, building under construction) and "Taller de Aeronautica" (194 m); Nominatim 2026-09-10
confidence: medium — a complete Boeing 737-300 airframe on the campus of the Instituto Tecnológico de Tijuana, serving its aeronautical engineering laboratory. Registration EI-DNZ is carried in the OSM name, which is a specific, checkable Irish registration rather than a guess. Deliberate retention plus institutional presentation, so it counts; but it is a teaching airframe on a campus, so `appointment` (arrange with the Tec) rather than walk-up `public`.

name: Aeronave en exhibición -- Tecnológico de Monterrey Campus Querétaro
city: Santiago de Querétaro
state_province: Querétaro
country: Mexico
postal_code: 76130
region: North America
address: Avenida Epigmenio González 500; Colonia San Pablo; Tecnológico de Monterrey Campus Querétaro (PrepaTec)
website: 
access_type: appointment
latitude: 20.612728
longitude: -100.407932
source: OpenStreetMap node 12173661003 (historic=aircraft), created 2024-09-12 by mapper "Daniela de la Peña"; Nominatim reverse geocode 2026-09-10 places it on the Tec de Monterrey Querétaro campus among PrepaTec buildings and the Centro de Innovación y Manufactura Avanzada
confidence: low — one untyped OSM node on a private university campus, mapped 2024. Recorded because a single displayed airframe at a school IS a site record per the contract, but nothing about the aircraft is known. `appointment` because campus access is controlled.

## AIRCRAFT

### Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía

Republic|P-47|D|||Thunderbolt|fixed_wing|monoplane|military|fighter||Displayed as an Escuadrón 201 aircraft; the FAEM flew 25 P-47D-30-RA in the Philippines and Formosa in 1945; serial not published by the museum and not recorded here rather than guessed|P47;P-47D;P47D;Thunderbolt|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Douglas|DC-3||||El Mexicano|fixed_wing|monoplane|military|transport||Described by SEDENA and both Wikipedias as Mexico's first presidential aircraft; NOTE an OSM monument of the same name is mapped beside the Hangar Presidencial at Mexico City airport so the physical location of this airframe needs confirmation; registration not published|DC3;C-47;C47;Skytrain;Dakota|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Northrop|F-5|E|4510||Tiger II|fixed_wing|monoplane|military|fighter||Photographed as 4510 in the museum hangar on 2010-05-07 and re-photographed in the new building in 2022; English Wikipedia instead gives FAM-4505 for the museum aircraft — one of the two is wrong or there are two F-5Es; FAM aircraft are frequently repainted|F5;F-5E;F5E;Tiger II;4505;FAM-4505;FAM-4510|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Lockheed|T-33|A|||Shooting Star|fixed_wing|monoplane|military|trainer||The FAM's first T-33 arrived February 1961 and the type served 46 years to July 2007; serial of the museum example not published|T33;T-33A;T33A;Shooting Star|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
de Havilland|DH.100||15|Vampire||fixed_wing|monoplane|military|fighter||Wears the number 15; Mexico bought 15 ex-RCAF Vampire Mk.III in 1961 and retired them in 1967 after six accidents with four complete survivors preserved; the Commons filename calls this one a T.Mk.11 which would make it a two-seat DH.115 instead — the discrepancy is unresolved so the base designation is recorded conservatively|DH100;DH-100;Vampire;Vampire Mk.III;DH.115;Aguacate|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Boeing|PT-17||EPS-6084|Kaydet||fixed_wing|biplane|military|trainer||Serial EPS-6084 from the English Wikipedia Boeing-Stearman survivor list; the FAM operated Stearmans as primary trainers and the Colegio del Aire still flies them|PT17;PT-17;Kaydet;Stearman;Model 75|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Stearman|N2S-3||||Kaydet|fixed_wing|biplane|military|trainer|1939|Commons file metadata gives a delivery date of 8 December 1939; a second Stearman airframe distinct from the PT-17 above; B75N1 model designation|N2S3;N2S-3;B75N1;Kaydet;Stearman|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|US
North American|T-6|G|EAN-796|Texan||fixed_wing|monoplane|military|trainer||Photographed at Santa Lucía on 2010-05-07 wearing EAN-796; a separate Commons image files it as AT-6G|T6;T-6G;T6G;Texan;AT-6;AT6;Harvard;EAN796|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
North American|T-28|A|||Trojan|fixed_wing|monoplane|military|trainer||Displayed at the museum entrance; Mexico acquired 32 T-28A from 1958 and retired them in 1982; serial not published|T28;T-28A;T28A;Trojan|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
TNCA|Serie C|||Microplano||fixed_wing|biplane|military|trainer||Mexican-built at the Talleres Nacionales de Construcciones Aeronáuticas; unequal-span single-bay biplane; one of the museum's signature national exhibits|TNCA Serie C;Serie C;Microplano|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
TNCA|Serie H|||Parasol||fixed_wing|monoplane|military|bomber||Mexican-built high-wing parasol monoplane bomber/reconnaissance testbed; displayed with a TNCA Aztatl six-cylinder engine and an Anáhuac propeller fitted|TNCA Serie H;Serie H;Parasol|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Azcárate|O-E-1|||||fixed_wing|biplane|military|recon||Designed by Gral. Brig. Juan Francisco Azcárate and built at TNCA in 1928; technically a sesquiplane which is recorded here as biplane because the field has no sesquiplane value|Azcarate O-E-1;OE1;O-E-1;Azcárate E-1;sesquiplano|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Pietenpol|Air Camper|||Avión Pinocho||fixed_wing|monoplane|civilian|private|1935|Built in Mexico by Miguel Carrillo Ayala in 1935 and powered by a 201 cubic inch Ford Model A engine|Air Camper;Pinocho;Avion Pinocho|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Aermacchi|AL-60||||LASA-60|fixed_wing|monoplane|military|utility||Built in Mexico as the Lockheed-Azcárate LASA-60; the FAM's standard light utility type of the 1960s|AL60;AL-60;LASA-60;LASA60;Lockheed-Azcárate LASA-60|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
AAMSA|A9B-M||EPA-1|Quail|Naco|fixed_wing|monoplane|military|trainer||Mexican-built development of the CallAir A-9; serial EPA-1 from the English Wikipedia CallAir survivor entry|A9B-M;A9BM;Quail;Naco;CallAir A-9;CallAir A9|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Beechcraft|Musketeer|||||fixed_wing|monoplane|military|trainer||Photographed inside the new museum building on 2022-05-20; serial not visible in the published image|Musketeer;Model 23;Beech 23|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Rockwell|690|A||Turbo Commander||fixed_wing|monoplane|military|transport||Aero 690A Commander in FAM markings; serial not published|690A;Aero Commander 690;Turbo Commander;Aero Commander 500|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Stinson|SR-5|A||Reliant||fixed_wing|monoplane|civilian|commercial_transport||Displayed in Aeronaves de México (later Aeroméxico) colours; this is the museum's civil airline heritage exhibit|SR5;SR-5A;SR5A;Reliant;Aeronaves de Mexico|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Lockheed|L-1329|JetStar 8|3908|JetStar||fixed_wing|monoplane|military|transport||Construction number 5144; former FAM VIP transport; on display at the museum per the English Wikipedia JetStar survivor list and photographed there 2022-05-20|JetStar;L1329;L-1329;c/n 5144;cn 5144|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Beechcraft|UC-45|J|ETL-1320|Expeditor||fixed_wing|monoplane|military|transport||Beechcraft Model 18 family; serial ETL-1320 from the English Wikipedia Model 18 survivor list|UC45;UC-45J;UC45J;Expeditor;C-45;C45;Beech 18;Model 18;ETL1320|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Mitsubishi|MU-2|P|ETE-1357|||fixed_wing|monoplane|military|transport||Serial ETE-1357 from the English Wikipedia MU-2 survivor list which places it at the museum beside AIFA|MU2;MU-2P;MU2P;ETE1357|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Sikorsky|R-6|A|43-45462|Hoverfly II||rotary_wing||military|utility||USAAF serial 43-45462; on static display per the English Wikipedia R-6 survivor list; recorded with operator_country US because it is an ex-USAAF airframe|R6;R-6A;R6A;Hoverfly;Hoverfly II;4345462|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|US
Mil|Mi-26|||||rotary_wing||military|transport||The largest helicopter ever operated by the FAM; serial not published|Mi26;Mi-26;Halo|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
MD Helicopters|MD 500||1138|||rotary_wing||military|utility||Photographed at Santa Lucía on 2010-05-07 as Hughes 369 / MD-500 number 1138|MD500;MD 500;Hughes 369;369;OH-6;Defender|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Eurocopter|AS332|||Super Puma||rotary_wing||military|transport||Visible behind the JetStar in the 2022 museum photograph; serial not readable|AS332;AS-332;Super Puma|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
IAI|Arava|102|3006|||fixed_wing|monoplane|military|transport||Construction number 36; delivered as 2006 and re-serialled 3006 in the 1990s when the whole FAM Arava fleet was renumbered from the 2001-2016 block to 3001-3015|Arava;IAI 102;IAI-102;2006;c/n 36;cn 36|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Convair|CV-580|||||fixed_wing|monoplane|military|transport||Ex-FAM Convair 580; photographed in FAM markings; serial not published (a Commons category exists for FAM Convair 580 number 3907 but it was not tied to this airframe)|CV580;CV-580;Convair 580;Convair 340;Convair 440|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Douglas|DC-6|A||Liftmaster||fixed_wing|monoplane|military|transport||Ex-FAM DC-6A; serial not published|DC6;DC-6A;DC6A;Liftmaster;C-118|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Lockheed|C-130|||Hercules||fixed_wing|monoplane|military|transport||Named in the Editorial GEA description of the outdoor line as the aircraft representing the Plan DN-III-E disaster relief mission; variant and serial not published|C130;C-130;Hercules;C-130K;Hercules C.1|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX
Radioplane|MQM-36|||Shelduck||fixed_wing|monoplane|military|drone||Target drone on display per the English Wikipedia Radioplane BTT article which places it at the museum at AIFA|MQM36;MQM-36;Shelduck;BTT;Basic Training Target|Museo Militar de Aviación Teniente P.A. José Espinoza Fuentes (MUMA) -- Santa Lucía|on_display|MX

### Museo del Ejército y Fuerza Aérea Mexicana (Cuartel Colorado) -- Guadalajara

IAI|Arava|201||||fixed_wing|monoplane|military|transport||On display in the museum grounds; acquired by Mexico from 1973 for troop transport and disaster relief; serial not published in either source|Arava;IAI 201;IAI-201|Museo del Ejército y Fuerza Aérea Mexicana (Cuartel Colorado) -- Guadalajara|on_display|MX

### Museo Descubre. Centro Interactivo de Ciencia y Tecnología -- Aguascalientes

Unidentified|Light aircraft|||||fixed_wing|monoplane|military|other||Spanish Wikipedia states the museum displays old aircraft donated by the Mexican Air Force and OpenStreetMap maps an aircraft monument on the forecourt; neither names a type so no identity is asserted; wing_type recorded as monoplane only because every post-war FAM donation type is one — treat as unconfirmed|Avion Museo Descubre|Museo Descubre. Centro Interactivo de Ciencia y Tecnología -- Aguascalientes|on_display|MX

### Museo Francisco Sarabia -- Ciudad Lerdo

Granville Brothers|R6H|||Q.E.D.|Conquistador del Cielo|fixed_wing|monoplane|civilian|experimental|1934|Granville Miller and De Lackner R6H built 1934 for Jacqueline Cochran for the MacRobertson London-Melbourne race; later NR14307 and NX14307; bought by Francisco Sarabia in 1938 and registered XB-AKM; set the Mexico City-New York record of 10 h 47 min on 24 May 1939 and crashed into the Anacostia at Washington on 7 June 1939 killing Sarabia. PRESENCE AT THIS SITE IS NOT CONFIRMED — the park beside the museum is named Avión Sarabia and this is the airframe associated with him but no source consulted states where the aircraft is today|R6H;R-6H;QED;Q.E.D.;Gee Bee QED;Gee Bee R-6H;NR14307;NX14307;XB-AKM;Conquistador del Cielo|Museo Francisco Sarabia -- Ciudad Lerdo|on_display|MX

### Base Aérea Militar No. 4 General Eduardo Aldasoro Suárez -- Cozumel

Lockheed|T-33|A|4019||Shooting Star|fixed_wing|monoplane|military|trainer||Plinthed on Avenida Rafael E. Melgar outside the base entrance with an interpretive marker erected in 2010; the marker records that the first T-33 reached Mexico in February 1961 and the type served 46 years until July 2007; photographed 2017-01-15|T33;T-33A;T33A;Shooting Star|Base Aérea Militar No. 4 General Eduardo Aldasoro Suárez -- Cozumel|on_display|MX
North American|T-28|A|||Trojan|fixed_wing|monoplane|military|trainer||Plinthed 20 m from the T-33 with its own marker; the marker records that Mexico acquired its first T-28A in 1958 and kept them in service until 1982; serial not on the marker|T28;T-28A;T28A;Trojan|Base Aérea Militar No. 4 General Eduardo Aldasoro Suárez -- Cozumel|on_display|MX

### Colegio del Aire / Base Aérea Militar No. 5 -- Zapopan

Lockheed|T-33|A|JE-047||Shooting Star|fixed_wing|monoplane|military|trainer||Static display on the Colegio del Aire grounds; photographed 2014-08-12; JE is the FAM's jet-trainer serial prefix|T33;T-33A;T33A;Shooting Star;JE047|Colegio del Aire / Base Aérea Militar No. 5 -- Zapopan|on_display|MX
de Havilland|DH.100|F.3||Vampire||fixed_wing|monoplane|military|fighter||Static display on the Colegio del Aire grounds photographed 2014-08-12; one of the four complete survivors of the 15 ex-RCAF Vampire Mk.III bought by Mexico in 1961; nicknamed Aguacate in FAM service; serial not legible in the published image|DH100;DH-100;Vampire;Vampire Mk.III;Mk III;Aguacate|Colegio del Aire / Base Aérea Militar No. 5 -- Zapopan|on_display|MX

### Base Aérea Militar No. 6 de Terán -- Tuxtla Gutiérrez

IAI|Arava|201|3015|||fixed_wing|monoplane|military|transport||Construction number 53; displayed outside the base; from the 3001-3015 re-serialling of the original 2001-2016 FAM Arava block|Arava;IAI 201;IAI-201;c/n 53;cn 53|Base Aérea Militar No. 6 de Terán -- Tuxtla Gutiérrez|on_display|MX

### 22a Zona Militar -- Toluca

IAI|Arava|201|3014|||fixed_wing|monoplane|military|transport||Construction number 52; single uncited Wikipedia survivor entry placing it on display at the 22a Zona Militar near Toluca; position not independently confirmed|Arava;IAI 201;IAI-201;c/n 52;cn 52|22a Zona Militar -- Toluca|on_display|MX

### Parque Temático Militar -- Zacatecas

Unidentified|Fixed-wing aircraft|||||fixed_wing||military|other||Mapped in OpenStreetMap as a traced way named simply Avión inside the Parque Temático Militar alongside tanks and a monumental flag; no type or serial recorded anywhere reachable; wing_type left blank rather than guessed|Avion Parque Tematico Militar Zacatecas|Parque Temático Militar -- Zacatecas|on_display|MX
Unidentified|Helicopter|||||rotary_wing||military|other||Mapped in OpenStreetMap as a traced way named simply Helicóptero 41 m from the fixed-wing aircraft; no type or serial recorded|Helicoptero Parque Tematico Militar Zacatecas|Parque Temático Militar -- Zacatecas|on_display|MX

### Parque Tangamanga II military display -- San Luis Potosí

Pilatus|PC-7|||Turbo Trainer||fixed_wing|monoplane|military|trainer||Displayed in a line with five named armoured vehicles inside Parque Tangamanga II; the PC-7 was the FAM's standard basic trainer and light attack type and equips the modern Escuadrón 201; serial not published|PC7;PC-7;Turbo Trainer|Parque Tangamanga II military display -- San Luis Potosí|on_display|MX

### Boeing 727 XC-FPA y Super Puma de la Policía Federal -- San Luis Potosí

Boeing|727|264 Adv|XC-FPA|||fixed_wing|monoplane|civilian|transport||Manufacturer's serial number 22413 recorded by the OSM mapper together with the registration and a JetPhotos airframe citation; former Policía Federal transport; the Policía Federal was dissolved in 2019 and its fleet dispersed to public display and other agencies|727;B727;Boeing 727-200;727-264;MSN 22413;c/n 22413;XCFPA|Boeing 727 XC-FPA y Super Puma de la Policía Federal -- San Luis Potosí|on_display|MX
Eurocopter|AS332|||Super Puma||rotary_wing||civilian|utility||Former Policía Federal Super Puma displayed 35 m from the Boeing 727; the OSM tag reads AS-322 which is a typo for AS332; registration not recorded|AS332;AS-332;AS 332;Super Puma;AS-322|Boeing 727 XC-FPA y Super Puma de la Policía Federal -- San Luis Potosí|on_display|MX

### Douglas DC-3 cine -- San Luis Potosí

Douglas|DC-3|||||fixed_wing|monoplane|civilian|commercial_transport||Airframe converted into a small cinema and publicly accessible; recorded per the contract rule that an aircraft converted into a public facility and visitable IS a display record; registration not recorded by the mapper|DC3;DC-3;C-47;C47;Dakota|Douglas DC-3 cine -- San Luis Potosí|on_display|MX

### Aeroparque Orizaba -- Boeing 727 El Cuatro Vientos

Boeing|727|200||El Cuatro Vientos||fixed_wing|monoplane|civilian|commercial_transport||Centrepiece of the municipal Aeroparque Orizaba and tagged in OpenStreetMap both as an aircraft and as a gallery i.e. the fuselage is in use as exhibition space; the display name El Cuatro Vientos honours the 1933 Barberán and Collar Seville-Cuba flight and is NOT a registration; registration unknown|727;B727;Boeing 727-200;El Cuatro Vientos|Aeroparque Orizaba -- Boeing 727 El Cuatro Vientos|on_display|MX

### Parque Centenario de la Fuerza Aérea -- Tuxtla Gutiérrez

Pilatus|PC-7|||Turbo Trainer||fixed_wing|monoplane|military|trainer||Displayed beside the monument to Tte. P.A. José Espinosa Fuentes in the park dedicated to the FAM centenary; serial not published|PC7;PC-7;Turbo Trainer|Parque Centenario de la Fuerza Aérea -- Tuxtla Gutiérrez|on_display|MX

### Monumento a la Fuerza Aérea Expedicionaria -- Monterrey

Unidentified|Aircraft|||||fixed_wing||military|other||Named aircraft monument to the Fuerza Aérea Expedicionaria Mexicana on Boulevard Acapulco at Avenida Eugenio Garza Sada; mapped 2026-04-22; no type recorded and none asserted here|Fuerza Aerea Expedicionaria Monterrey|Monumento a la Fuerza Aérea Expedicionaria -- Monterrey|on_display|MX

### Avión Biblioteca -- Utopía Teotongo Iztapalapa

Unidentified|Airliner|||||fixed_wing|monoplane|civilian|commercial_transport||Airliner fuselage converted into a public lending library inside the Utopía Teotongo public-space complex in Iztapalapa; type and registration not established in this pass|Avion Biblioteca;Utopia Teotongo|Avión Biblioteca -- Utopía Teotongo Iztapalapa|on_display|

### Avión monumento -- Town Center Zumpango

Unidentified|Aircraft|||||fixed_wing||military|other||OpenStreetMap historic=monument named simply Avion; 12 km from Santa Lucía air base so an ex-FAM donation is plausible but nothing is established|Avion Zumpango|Avión monumento -- Town Center Zumpango|on_display|

### Plaza Avión Militar -- Monclova

Unidentified|Aircraft|||||fixed_wing||military|other||OpenStreetMap historic=monument named Plaza Avión Militar on Boulevard Ejército Mexicano; type and serial unknown|Plaza Avion Militar Monclova|Plaza Avión Militar -- Monclova|on_display|MX

### Monumento Avioneta de la Fuerza Aérea Mexicana -- Zacatlán

Unidentified|Light aircraft|||||fixed_wing||military|other||OpenStreetMap historic=monument explicitly named Fuerza Aérea Mexicana Avioneta on the Paseo de la Barranca; avioneta implies a light aircraft; type and serial unknown|Avioneta Zacatlan|Monumento Avioneta de la Fuerza Aérea Mexicana -- Zacatlán|on_display|MX

### Monumento Helicóptero -- Ciudad Fernández

Unidentified|Helicopter|||||rotary_wing||military|other||OpenStreetMap historic=monument named Helicóptero beside the municipal sports ground; type and serial unknown|Helicoptero Ciudad Fernandez|Monumento Helicóptero -- Ciudad Fernández|on_display|

### Parque de la Avioneta -- Ecatepec de Morelos

Unidentified|Light aircraft|||||fixed_wing||civilian|other||Park named for a light aircraft; NO airframe object is mapped inside the park and no source confirms an aircraft is still present; this row exists so the lead is not lost and must be verified before it is trusted|Avioneta Ecatepec|Parque de la Avioneta -- Ecatepec de Morelos|on_display|

### Parque La Avioneta -- Tulancingo de Bravo

Unidentified|Light aircraft|||||fixed_wing||civilian|other||Park named for a light aircraft; NO airframe object is mapped inside the park and presence is unverified; recorded as a lead only|Avioneta Tulancingo|Parque La Avioneta -- Tulancingo de Bravo|on_display|

### Boeing 737 EI-DNZ -- Instituto Tecnológico de Tijuana

Boeing|737|3TO|EI-DNZ|||fixed_wing|monoplane|civilian|commercial_transport||Complete airframe on the Instituto Tecnológico de Tijuana campus serving the Laboratorio de Aeronáutica; the registration EI-DNZ is Irish which fits a leasing-company airframe retired to a technical school; former operator not established so operator_country is left blank|737;B737;Boeing 737-300;737-3TO;EIDNZ|Boeing 737 EI-DNZ -- Instituto Tecnológico de Tijuana|on_display|

### Aeronave en exhibición -- Tecnológico de Monterrey Campus Querétaro

Unidentified|Aircraft|||||fixed_wing||civilian|other||Single untyped OpenStreetMap historic=aircraft node on the Tec de Monterrey Querétaro campus mapped in September 2024; nothing further known|Avion Tec Queretaro|Aeronave en exhibición -- Tecnológico de Monterrey Campus Querétaro|on_display|

## NOTES

### Sources and their weight

**What carried this region.** In descending order of value:

1. **OpenStreetMap via Overpass.** The full sweep specified in the brief was run and it worked.
   `overpass-api.de` is blocked by this environment's proxy exactly as warned;
   **`https://maps.mail.ru/osm/tools/overpass/api/interpreter` worked reliably** for every query,
   POSTed from a file with a desktop-Chrome User-Agent and bbox (not area) filters.
   `overpass.kumi.systems` was reachable but slow enough to blow a 2-minute wall clock.
   Two bboxes covering 14.4/-118.5 to 32.8/-86.6 returned 643 elements for
   `historic=aircraft` + `memorial=aircraft` + `memorial:type=aircraft` + `aeroway=gate_guardian`;
   after filtering out the United States with a piecewise border function and Guatemala/Belize
   by hand, **exactly 24 of those 643 are in Mexico**. A second sweep for
   `museum=aerospace`, `memorial=plane`, `artwork_type=aircraft|airplane`,
   `historic=airplane` and `tourism=attraction` + `aircraft:type` over the whole
   country returned **zero additional Mexican objects**. **There is not a single
   `aeroway=gate_guardian` in Mexico in OSM.** That is a real finding: Mexican
   gate guards are essentially unmapped, and this is the largest structural gap.
2. **Nominatim free-text search** (`countrycodes=mx`) was far more productive than
   Overpass regex, which times out on unindexed `name~` over a country this size.
   Searching `avión`, `avioneta`, `parque avión`, `helicóptero monumento`,
   `Parque Temático Militar`, `Museo Fuerza Aérea`, `Colegio del Aire`,
   `monumento aviador` and `avión biblioteca` produced most of the monument list.
3. **Spanish and English Wikipedia** — raw wikitext via `action=raw` and full-text
   `insource:` search via the API. English Wikipedia's per-type *survivors* sections are
   where nearly every Mexican serial in this file came from
   (Sikorsky R-6, Lockheed JetStar, Mitsubishi MU-2, Beechcraft Model 18,
   Boeing-Stearman, Northrop F-5, CallAir A-9, IAI Arava, T-33 displayed list).
4. **Wikimedia Commons** category listings and `extmetadata` — the file *titles* in
   Commons carry serials (`4510 Northrop F-5E...`, `EAN-796 North American T-6...`,
   `1138 Hughes 369...`, `15 De Havilland Vampire...`) and the metadata carries the
   shooting date, which is how the 2010 vs 2022 Santa Lucía photographs were separated.
5. **hmdb.org (Historical Marker Database)** — three Mexican markers at Cozumel with
   surveyed coordinates and dated photographs. hmdb.org is behind Cloudflare and refuses
   `curl` (403), but **WebFetch reaches it**. This is the only source in the pass that
   gave both a serial-bearing interpretive text and a surveyed coordinate.
6. **OSM API changeset history** — used to date and attribute suspicious nodes.
   This is what disqualified the ten Naucalpan "aircraft" (below).

**What did not work, and why it matters.** General web search was unavailable for the whole
pass. WebSearch was exhausted before this task began. Every search engine reachable through
the proxy either bot-challenged (`searx.be`, Startpage, DuckDuckGo lite, Mojeek 403,
Brave 429, Ecosia 403) or returned results that had nothing to do with the query
(Bing repeatedly answered a Spanish query about Escuadrón 201 monuments with German
hotel listings for Aargau and flights to Kefalonia). `sic.cultura.gob.mx`, the Mexican
Secretaría de Cultura's museum registry, loads but renders its per-state lists in
JavaScript. `www.gob.mx` returns 403 to WebFetch. This is the single biggest reason
this file is thinner than Mexico deserves: Spanish-language blog and press coverage of
avión-monumento is abundant and none of it was reachable.

**Compilations that proved stale or wrong.** English Wikipedia's `List of aviation museums`
lists exactly two Mexican entries — Museo del Concorde and the Mexican Air Force Museum —
and misses every other site in this file. English Wikipedia's `Museo del Concorde` article
is categorised as a **defunct** museum while citing a May 2024 El Diario de Juárez article
headlined "Regresa a la frontera Museo del Concorde"; the category and the citation
contradict each other. The `List of displayed Lockheed T-33 Shooting Stars` Mexico section is
a single hand-wave ("various T-33s ... at individual air bases") plus one real entry.

### Corrections made

- **OSM way 1073649398 is named "Museo Miliar de Aviación"** — a typo for *Militar*. Recorded
  under the correct name.
- **OSM node 6157578852 tags the San Luis Potosí helicopter as "AS-322 Super Puma".**
  There is no AS322; the type is the **AS332** Super Puma. Corrected in the row and the
  wrong string preserved in `aliases`.
- **F-5E serial conflict.** English Wikipedia gives **FAM-4505** as the museum's F-5E.
  A Wikimedia Commons photograph taken at Santa Lucía on 2010-05-07 shows **4510**.
  I recorded 4510 (photographic, dated) as `tail_number` and put 4505 in `aliases` with the
  conflict explained in `description`, per the contract's rule that painted/asserted markings
  are not automatically the identity. FAM aircraft are repainted often.
- **Vampire designation.** Mexico bought DH.100 Vampire **Mk.III** (single-seat).
  The Commons file for the museum aircraft is titled *"De Havilland Vampire T.MK.11"*,
  which would be a two-seat **DH.115**. I recorded the base designation DH.100 with a blank
  variant and stated the discrepancy rather than picking one.
- **Azcárate O-E-1 is a sesquiplane.** `wing_type` has no sesquiplane value, so it is
  recorded as `biplane` with the fact stated in `description`.
- **BAM → ZAM.** From **1 March 2026** the Fuerza Aérea Mexicana renamed its
  *Bases Aéreas Militares* to *Zonas Aéreas Militares* and its *Estaciones Aéreas Militares*
  to *Grupos de Bases Aéreas*. BAM-5 Zapopan is now the **10a Zona Aérea Militar**;
  BAM-6 Terán is now the **15a Zona Aérea Militar**. Site names are kept in the familiar
  BAM form (that is what signage, markers and every source still use) with the change noted.
- **"El Mexicano" double location.** Recorded once, at MUMA. See the site block for the
  Mexico City monument and "Needs a human".

### Judgment calls

- **Cozumel is `public`, not `restricted`.** The T-33, the T-28A and the Escuadrón 201
  tribute stand on Avenida Rafael E. Melgar, the seafront boulevard, *outside* the gate of
  BAM-4. The contract says to judge by how a member of the public actually gets in.
- **Colegio del Aire is `restricted`** — the two airframes are inside an active air base
  and academy, visible to the public only on open days.
- **MUMA is `public`** even though it is inside Ciudad Militar Santa Lucía: free entry,
  published hours, an official SEDENA visitor page, and a signposted civilian route from
  AIFA. Spanish Wikipedia notes you need a taxi or private car because public transport
  stops at the civil terminal — an inconvenience, not a gate.
- **Tijuana and Querétaro are `appointment`** — campus airframes at controlled-access
  institutions.
- **Converted airframes recorded as displays**: the San Luis Potosí DC-3 cinema, the
  Orizaba Boeing 727 gallery and the Iztapalapa Avión Biblioteca. All three are deliberate
  retention plus public presentation, which the contract counts.
- **`Unidentified` rows kept rather than dropped.** Eleven airframes are recorded as
  `Unidentified` with a descriptive model. Every one of them sits at a site with independent
  evidence of a physical aircraft; the contract says the correct response is an
  `Unidentified` row, not a missing site.
- **`wing_type` left blank on several `fixed_wing` Unidentified rows.** For an aircraft
  whose type is unknown, "monoplane" would be a guess dressed as data. The one exception
  is Museo Descubre, where the source says "FAM donation", and even there the reasoning
  is written into the description.
- **`operator_country` blanks are deliberate** on the Tijuana 737 (Irish registration,
  prior operator unknown), the Iztapalapa library airliner, the Ciudad Fernández
  helicopter, the Zumpango monument and the two "Avioneta" parks. `US` is used only for
  the Sikorsky R-6A (USAAF 43-45462) and the Stearman N2S-3, both ex-US airframes.
  The P-47D is `MX` because the FAEM operated it, even though it is US-built and wore
  USAAF insignia alongside FAEM markings.

### EXCLUDED, and why

A well-searched zero is a finding. These were considered and rejected:

- **The ten "aircraft" inside Campo Militar No. 1-A, Naucalpan/Lomas de Sotelo, CDMX**
  (OSM nodes 14097695957, 14097696088, 14097696106, 14097696300, 14097696442, 14097696470,
  14103944558, 14103944630, 14103945210 and one more, all c. 19.437–19.449 N, 99.222–99.236 W).
  These were the single largest cluster the Overpass sweep returned in Mexico and they are
  **not display aircraft**. All were created on 2026-08-15 and 2026-08-18 by mapper
  "Juan MAS" in changesets commented *"Lugares faltantes"* with `imagery_used=Bing Maps Aerial`,
  carry no tag but `historic=aircraft`, and an Overpass landuse query confirms they fall inside
  OSM way 176021979 **"Campo Militar 1-A General de División Álvaro Obregón"**, the SEDENA
  garrison and heliport. They are almost certainly parked operational helicopters traced from
  aerial imagery. Operational aircraft are not displays, and the site is closed. Excluded.
- **"Restos de Big Flo" (XB-MNP), Laguna Salada / Highway 5 south of Mexicali**
  (OSM node 6109726276, 32.50124 −115.39674). The Boeing 727-212 Adv deliberately crashed
  for television on 27 April 2012. English Wikipedia states that **satellite imagery taken
  in 2026 shows nothing of the aircraft remains at the site**. A dumped wreck was never a
  display, and it is now gone. Excluded.
- **Douglas DC-3 XB-PXO, Celestún, Yucatán** (OSM way 684071872, 20.97207 −90.28339).
  OSM's own name for it is *"Douglas DC-3 abandonado"*. Abandoned airframe, no evidence of
  deliberate retention or public presentation. Excluded as derelict — but see "Needs a human",
  because a registration this specific is worth a look if it has since been plinthed.
- **"avión", Boulevard Antonio Rocha Cordero, San Luis Potosí** (OSM node,
  22.12632 −101.01517). Tagged `tourism=artwork` + `artwork_type=sculpture` — a sculpture
  of an aircraft, not an airframe. Excluded.
- **Unnamed `historic=aircraft` node at 16.77659 −93.20603, Tuxtla Gutiérrez**
  (OSM node 5210312559, mapped 2017 by "DoubleA", untagged beyond `historic=aircraft`).
  In a residential street grid 5.4 km from BAM-6 with no park, no name and no nearby
  context of any kind. Unverifiable. Excluded, flagged.
- **Unnamed `historic=aircraft` node at Tepic airport** (OSM node 2519455727,
  21.41414 −104.83945, mapped 2013). Sits ~300 m south of the terminal of
  Aeropuerto Internacional de Tepic-Riviera Nayarit beside a private track, inside the
  airport perimeter. Could be a BAM gate guard or could be a stored airframe.
  No name, no type, thirteen years stale. Excluded, flagged.
- **Museo Nacional de Historia (Castillo de Chapultepec)** — named in the brief.
  It is a national history museum in a castle; nothing found associating any airframe
  with it. The Escuadrón 201 material in Chapultepec is the **Tribuna Monumental /
  Monumento a las Águilas Caídas** and the **Mausoleo del Escuadrón 201** (which holds
  the remains of Subtte. P.A. Mario López Portillo and Tte. P.A. José Espinoza Fuentes,
  transferred from the Panteón de Dolores) — memorial architecture and a mausoleum, no aircraft.
  Excluded as a site because there is no airframe; recorded here so it is not re-searched.
- **Museo Histórico Naval, Veracruz** (19.19923 −96.13508) and
  **Museo Histórico Naval de la Ciudad de México** (19.43575 −99.14026) — both confirmed to
  exist via Nominatim, neither could be shown to hold an airframe. Mexican naval aviation
  (Tapachula, La Paz, Veracruz air stations) produced **no** display evidence at all in this
  pass. Excluded, flagged as the largest unworked seam.
- **Museo Tecnológico de la Comisión Federal de Electricidad (MUTEC)**,
  **Papalote Museo del Niño** (CDMX, Monterrey and Cuernavaca) and
  **Centro Cultural Mexiquense**, Toluca — all named in the brief, all confirmed to exist
  in OSM, none with any aircraft evidence found. Excluded.
- **ESIME Ticomán (IPN)** — the Instituto Politécnico Nacional's aeronautical faculty at
  19.50971 −99.13358. It certainly holds instructional airframes, but nothing was
  documented in any reachable source. Excluded, flagged — this is a near-certain miss.
- **Escuadrón 201 place names that are not aircraft**: the Metro Línea 8 station
  "Escuadrón 201" in Iztapalapa (19.36490 −99.10955), the village of Escuadrón 201 in
  Matamoros, Coahuila (25.67493 −103.34834), and the Colonia Escuadrón 201 in Iztapalapa
  (which has a commemorative monument but no aircraft). Named for the squadron; no airframes.
- **Aguascalientes/Zacatlán/etc. peaks, dams and streets called "El Avión" or "Avioneta"** —
  a dozen Nominatim hits that are landforms and road names. Filtered out.
- **The 619 non-Mexican `historic=aircraft` objects** returned by the sweep bboxes
  (southern USA and Guatemala). Filtered by a piecewise US-Mexico border function plus
  manual review of the Guatemala/Belize edge.

### Blank fields, deliberately

- **`tail_number` is blank on 27 of the 43 aircraft rows.** Mexican preserved-aircraft
  serials are simply not published: SEDENA does not publish a collection catalogue, and
  the FAM repaints airframes often. Every serial that appears here has a named source.
  None was inferred from a photograph caption alone unless the caption is the Commons
  file title, which is stated in the description.
- **`year_built` is blank on 41 of 43 rows.** Only the Pietenpol (1935, sourced build date)
  and the Stearman N2S-3 (1939, from a delivery date in the Commons metadata) have one.
  No US fiscal-year serial prefix was converted into a build year.
- **Coordinates are blank** for the MUEFA Coyoacán, Museo del Concorde and 22a Zona Militar
  Toluca sites. In each case the street address is known but no sourced coordinate was
  found, and a geocode of a street name would have produced a plausible-looking wrong number.
- **`postal_code` is blank** where Nominatim did not return one.
- **`website`** is blank except where an official URL was actually seen.

### Needs a human — ranked

1. **The Gee Bee / Granville R6H "Conquistador del Cielo" (XB-AKM).** Where is it?
   The Museo Francisco Sarabia in Ciudad Lerdo, Durango sits beside a park literally named
   *Parque Avión Sarabia* and a statue of the pilot, but no source consulted states the
   aircraft's location, and neither Spanish Wikipedia article on Sarabia or on the aircraft
   says. This is the most historically significant single airframe in Mexico and it is
   currently a blank. **Call:** Museo Francisco Sarabia / Dirección de Cultura, Municipio de
   Lerdo, Durango. One call answers the site's whole aircraft list.
2. **The DC-3/C-47 "El Mexicano".** MUMA at Santa Lucía or the Hangar Presidencial at
   Mexico City airport (OSM node 1445924929, 19.423332 −99.074524)? One phone call to MUMA
   settles a duplicate that will otherwise be imported twice by two different researchers.
   **Call:** MUMA, via the SEDENA visitor page.
3. **A MUMA collection list.** The museum claims **50 aircraft**; this file has 30, most
   without serials. SEDENA's page is 403 to automated fetching. A visitor or a written
   request to the museum would roughly double Mexico's airframe count in one go and put
   serials on most of it. **Call/visit:** Museo Militar de Aviación, BAM No. 1 Santa Lucía,
   Tue–Sun 09:00–16:00, free.
4. **Naval aviation.** The Armada de México's air arm produced **zero** display records in
   this pass. Museo Naval México (Veracruz), the naval air stations at Tapachula, La Paz and
   Veracruz, and the Heroica Escuela Naval Militar at Antón Lizardo are all unworked.
   **Contact:** SEMAR Dirección General de Cultura / Museo Histórico Naval Veracruz,
   Av. Francisco Landero y Coss, Veracruz.
5. **The BAM gate guards.** The brief listed sixteen bases. This pass confirmed displays at
   only **three** (Cozumel BAM-4, Zapopan BAM-5, Terán BAM-6) plus one unconfirmed
   (22a ZM Toluca). Ixtepec, La Paz, Mérida, Puebla, Ciudad Pemex, Hermosillo (BAM-18,
   29.09402 −111.04312 in OSM), Culiacán (BAM-10), Chihuahua, Monterrey, Tampico, Veracruz
   and Campeche are all untouched, and OSM has **no** `aeroway=gate_guardian` anywhere in
   Mexico. A Spanish-language image search on `"gate guard" OR "avión monumento" + <base name>`
   would probably find a dozen more airframes in an afternoon — it just could not be run here.
6. **ESIME Ticomán (IPN), Mexico City** — the national aeronautical engineering faculty.
   Almost certainly holds instructional airframes; nothing documented. **Contact:**
   ESIME Ticomán, Av. Ticomán 600, Col. San José Ticomán, GAM, CDMX.
7. **Type identification for the eleven `Unidentified` rows** — especially the
   Monterrey "Fuerza Aérea Expedicionaria" monument (25.62610 −100.27693, on Blvd Acapulco
   at Garza Sada), the Zacatecas Parque Temático Militar pair, and Museo Descubre's
   FAM donations. All are street-visible; a single photograph closes each one.
8. **Museo del Concorde, Ciudad Juárez** — open or closed, and where?
   English Wikipedia says defunct; El Diario de Juárez of 2024-05-22 says it came back.
   **Call:** museodelconcorde.com; the last published address is
   Av. Antonio J. Bermúdez 2050, Parque Industrial Bermúdez.
9. **Do the Ecatepec and Tulancingo "Avioneta" parks still contain an aircraft?**
   Both parks are named for one; neither has an airframe mapped. Two street-view looks.
10. **Celestún DC-3 XB-PXO** (20.97207 −90.28339) — excluded as abandoned. If Celestún has
    since plinthed it as a beach landmark (a common fate in Yucatán) it becomes a record.
