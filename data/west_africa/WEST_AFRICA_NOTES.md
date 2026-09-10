# West and Central Africa — Ghana, Mali, Nigeria, Cameroon

7 sites, 13 airframes, imported September 2026. Greenfield.

**Read the coverage warning first — this is a partial pass.** The research run
was cut off by a quota limit roughly halfway through. The countries actually
worked are **Ghana, Mali, Nigeria (partially), Cameroon and Senegal**. The
countries **not reached at all**, whose absence here is a gap and not a negative
result, are:

> Côte d'Ivoire, Burkina Faso, Niger, Guinea, Sierra Leone, Liberia, Togo,
> Benin, Cape Verde, Mauritania, Chad, Central African Republic, Gabon, Republic
> of the Congo, **Democratic Republic of the Congo**, Equatorial Guinea, and São
> Tomé and Príncipe.

The DRC brief in particular — Kinshasa N'Djili, Kisangani, and the work of
separating preserved displays from the region's large derelict population — was
**never started**. Anyone picking this up should start there.

---

## Sources and their weight

The most productive channel was **not an aviation directory**. It was an
OpenStreetMap Overpass sweep of the whole region for `historic=aircraft`,
`memorial=aircraft` and aviation/military museum tags, every hit
reverse-geocoded and then confirmed by pulling satellite tiles and looking at
them. That found the Bamako-Sénou pair, the Aburi helicopter, the KNUST L-29,
the Jos roundabout aircraft, the Ikeja plinth, the Yaoundé pair and the
Dakar-Thiaroye pair — **none of which appear on aviationmuseum.eu at all.**

**Dated photographs were weighted highest.** Three of the four Ghanaian airframes
have their serial or type read directly off a photograph with an EXIF date (2010,
2013, 2022, 2023) rather than copied from a list. Satellite work used Esri World
Imagery's metadata service for per-tile acquisition dates — Bamako-Sénou 12 Jan
2024, Ikeja 13 Dec 2022, Dakar-Thiaroye 6 Mar 2024, Jos 18 May 2021 with a newer
3 Mar 2025 layer — so satellite confirmations here are dated, not vague.

### How aviationmuseum.eu proved stale, specifically

Its pages carry "last page update 05/06-dec-2016". Concretely:

- **Its Africa index does not list Nigeria**, although a Nigeria country page
  exists. The index is out of sync with its own content.
- **Its Mali coordinate is wrong.** It gives the Musée de l'Armée at
  12°38'07.4"N 8°00'52.2"W in Hamdallaye ACI. Satellite imagery for that exact
  point shows **no aircraft** — only a city street. The two Malian display
  aircraft are 12 km away at the air base at Sénou.
- **Its Mali listing contradicts itself**, giving the same serial TZ-367 for both
  the An-2 and the MiG-17F.
- **Its Ghana page misses half the country.** It lists two airframes at Kumasi
  and nothing else; the sweep found two more Ghanaian airframes it does not
  carry — the KNUST L-29 and the Accra Officers Mess MB-326.

Used strictly as a lead list it earned its place. Used as fact it would have
produced a wrong coordinate for Mali and a two-airframe total for Ghana.

---

## Corrections made, with evidence

**The Kumasi helicopter is a Mil Mi-2, not an SA 330 Puma.** Wikimedia Commons
files it under "SA 330 Puma in Ghanaian service". The photograph in that very
category shows a small helicopter with a glazed nose, two turbine intakes above
the cabin and a three-blade rotor — an Mi-2. The Commons category is wrong;
aviationmuseum.eu's Mi-2 is right.

**G706 and G707 are two different MB-326s**, not a transcription variant of one.
Both serials were read off their respective airframes in dated photographs —
G707 at Kumasi (7 September 2013), G706 at the Ghana Air Force Officers Mess in
Accra (29 August 2010).

**The KNUST L-29 Delfin G959 is an entirely new record**, serial read from a
7 July 2022 photograph and re-confirmed by a 1 April 2023 photograph in the same
position.

**The Malian display site is Bamako-Sénou, not Hamdallaye ACI** — relocated on
satellite evidence and identified from OSM as inside Base Aérienne 101 de Sénou,
beside the Foyer de l'Aviateur.

**The Umuahia coordinate** comes from the geotag of a 2015 Commons photograph
taken among the outdoor exhibits (5.5434, 7.48928), not from Wikipedia's
5°32′42″N 7°29′10″E — the two disagree by about 350 m and the photograph is the
better fix on the display area. Stated here rather than silently averaged.

---

## Judgment calls

**The Aburi H-19 is recorded `on_display` despite being wrecked.** It was
deliberately moved from Accra Air Force Base in 1974 to be an exhibit in a public
botanical garden and is still standing where it was put. A Graphic Online report
of 10 May 2024 describes the tail boom, rudder and rotor mast detaching and
cracks in the cockpit and cabin — that is presence evidence, not absence
evidence. This is the opposite of the derelict rule because the placement was
intentional and the setting is a fee-paying public garden. A replacement airframe
has been approved and is waiting at Takoradi Air Force Base for funds to move it.

**The Accra Officers Mess is `restricted`** even though the aircraft is plainly
visible from the street over the wall, because reaching it means entering a
military mess. Bamako-Sénou and the Yaoundé CCAA compound likewise. **Jos would
have been `public`** — a plinth in the middle of a public road roundabout.

**Two confirmed sites were dropped for want of an identifiable airframe.** The
**Airforce Roundabout in Jos** (a twin-engine monoplane on a raised kerbed
roundabout) and the **Airport Road plinth in Ikeja, Lagos** (a single aircraft on
a circular plinth in a walled courtyard beside Murtala Muhammed Airport, with an
OSM node literally named "Aircraft") are both unambiguous plinthed displays in
recent satellite imagery. Neither type is resolvable at available resolution, and
giving them rows would have meant inventing a manufacturer. **The sites are real;
they need one photograph each.**

---

## Excluded, and why — do not re-research these

**Cotonou "Avion sur la plage", Benin.** OSM tags it `tourism=museum,
museum=aviation`, but the linked Commons filename describes it as the *épave* —
the wreck — of an aircraft-restaurant stranded on the beach. A TriStar hull
beached and rotting is exactly the derelict the rules exclude, whatever a mapper
tagged it.

**UTA Flight 772 Memorial, Ténéré, Niger.** A desert memorial built partly from
aluminium including a wing section of the destroyed DC-10. A memorial *to* a
destroyed aircraft, not a preserved airframe.

**Dakar, Camp Lieutenant Amadou Lindor Fall, Senegal — excluded with regret.**
Two aircraft, one small and one substantially larger, sit in a cleared open area
inside this Senegalese Army camp at Thiaroye, confirmed in Google imagery and in
Esri imagery dated 6 March 2024. But they are on bare ground — not plinthed, not
kerbed, not in any arranged display bed — and it could not be established whether
they are a heritage display or stored/instructional airframes. Neither type could
be identified. **This is the strongest single unresolved lead in the whole pass.**

**Nigerian Air Force Museum, Kaduna — could not be substantiated.** The NAF's own
site history page makes no mention of a museum, heritage centre or preserved
aircraft, and searches of Nigerian press around the NAF 60th anniversary returned
airshows and no museum. Nigeria's stored MiG-21 fleet at Makurdi, Kaduna and
Maiduguri was **advertised for sale in 2020**, which makes casual references to
Kaduna MiG-21s "on display" doubly suspect: stored and for-sale is not preserved.
If this museum exists it needs a primary source.

**Abuja Airplane House** — a private villa in Asokoro built in the shape of an
aircraft. A building, not an airframe.

**Banjul, The Gambia** — eight `historic=aircraft` OSM nodes including an Il-62,
several tagged `ruins=yes`. The derelict population at Banjul, and outside the
brief in any case.

**Three Chadian OSM nodes** near N'Djaména, Linia and Ngoura tagged
`historic=aircraft` but carrying only what read as Arabic personal or place names
and no other tags. Almost certainly mis-tagged. Unverified, no rows.

**Searched and nothing confirmable found:** the Kwame Nkrumah memorial aircraft;
preserved presidential aircraft across the region; NAF Makurdi, Takoradi and
Accra base displays; Lagos, Abuja and Kano airport gate guards; and the Musée des
Forces Armées Sénégalaises in Dakar-Plateau (14.66718, -17.44219), which is a
real museum but whose own descriptions name no aircraft.

---

## Deliberate blanks

**`year_built` is blank on every row.** No construction, rollout, first-flight or
delivery date was sourced for any airframe here.

**`tail_number` is blank** on the Kumasi Mi-2 (aviationmuseum.eu's G-661 is
single-sourced and unreadable in the photograph), both Bamako MiGs, the Aburi
H-19, the Yaoundé Fouga and the Umuahia MFI-9B. The Biafran MFI-9B's reported
marking "BB 905" is carried as an alias only: Biafran aircraft wore informal
markings, not national serials.

**Variants are blank** wherever the only support was a single stale directory
line.

**Ghana's postal fields are blank** because what Nominatim returns there
("AK-010-1295", "GD-110-6313") are GhanaPost digital addresses, not postal codes.
The Nigerian codes 930253 and 100282 are reverse-geocodes, not verified.

**The Accra Officers Mess has blank coordinates** — no location was established.

---

## Ranked open questions

1. **Dakar, Camp Lieutenant Amadou Lindor Fall: what are the two aircraft, and
   are they displayed or stored?** One photograph settles it and adds a
   Senegalese site.
2. **The whole of DRC, Congo-Brazzaville, Gabon, CAR, Chad and Equatorial Guinea
   — not started.** This is the largest coverage gap in the African build.
3. **What aircraft is on the Airforce Roundabout in Jos, and what is on the
   plinth on Airport Road in Ikeja?** Two confirmed sites blocked on one
   photograph each.
4. **Does a Nigerian Air Force museum at Kaduna actually exist?** A call to NAF
   Headquarters closes this permanently, in either direction.
5. **Bamako-Sénou: is the swept-wing aircraft a MiG-15 or a MiG-17**, and does
   either reported serial (TZ-372, TZ-367) apply? Mali's December 2024 scrapping
   of its remaining fighters by weight makes a fresh presence check worth doing.
6. **What is the aircraft at 5.655353, -0.182794 on Annie Jiagge Road, Legon,
   Accra?** Confirmed on satellite, unidentified — and possibly, though not
   probably, the G706 mess aircraft.
7. **Re-confirm the five Umuahia airframes individually.** Everything at the
   National War Museum rests on one 2016 compilation plus site-level presence
   evidence from 2022, 2025 and 2026 that names no individual aircraft.
8. **Ghana: has the Aburi H-19 been replaced yet** by the airframe waiting at
   Takoradi?
