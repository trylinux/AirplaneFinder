# Southern Africa excluding South Africa — Zimbabwe, Zambia, Angola

3 sites, 15 airframes, imported September 2026. Greenfield. South Africa was done
separately and is out of scope here; see `data/south_africa/SOUTH_AFRICA_NOTES.md`.

Zimbabwe is essentially a one-place story. Zambia yields one airframe, Angola
two. **Namibia, Botswana, Mozambique, Malawi, Lesotho and Eswatini are documented
negatives** — searched and empty, not skipped.

---

## Sources and their weight

Highest weight went to the operating institution's own pages and to dated
photographs. The single most valuable document was the **National Museums and
Monuments of Zimbabwe regional page for Gweru** — the operator speaking about its
own holdings. Then dated photography: a JetPhotos frame of 10 June 2025 at
Livingstone; an Alamy frame of November 2019 of the Viscount at Gweru; a
photographer's post of July 2023 showing the Gweru Spitfire in person; and a
traveller's account of a 17 March 2025 visit to the Luanda fortress, published
January 2026.

`vickersviscount.net` was treated as a type-specialist register and trusted for
the Viscount's build and service dates. `warbirdregistry.org` supplied the
Spitfire's Rhodesian identity chain. `zimfieldguide.com` and `aeroflight.co.uk`
were used as a paired inventory, with the caveat below. `aviationmuseum.eu` and
`silverhawkauthor` were used strictly for lead generation.

**Aerial Visuals is empty for this region.** Dossier searches on PK355, R2504,
2406, SR48 and 3614 returned either no match or unrelated airframes with
coincidentally similar numbers. It is not a usable source for Rhodesian or
Zimbabwean serials and should not be re-queried next year.

---

## The compilation that proved stale, and exactly how

**aviationmuseum.eu's Gweru page lists thirteen aircraft. Two do not survive
scrutiny.**

Its **Douglas C-47A Dakota, serial 3708**, is absent from both aeroflight and
Zimbabwe Field Guide, which independently list eleven; it does not appear in the
photographic record of the collection; and the Zimbabwe Field Guide text argues
in the present tense that the Air Force of Zimbabwe's Dakota is still parked in
the open at a base, rusting, and *should* be donated to the museum — which is
only coherent if it is not there. `silverhawkauthor` also lists the Dakota at
Gweru, but these two are not independent and neither is corroborated by anyone
who has photographed the hangar. **Dakota 3708 is excluded.**

Its **Bell 205A-1** is real but is a **cabin shell, not an aircraft** — the
photographic caption record is explicit ("Bell AB.205A cabin shell '6082' c/n
4037") while the directory listed it as a complete airframe. It is included as a
row and described honestly.

Separately, aviationmuseum.eu has **no index pages at all** for Namibia,
Botswana, Mozambique, Malawi, Lesotho or Eswatini — those URLs 404 — so it
contributed nothing outside Zimbabwe, Zambia and Angola.

---

## Corrections made, with evidence

**Gweru is two sites, not one, and all fifteen airframes are at the second.**
NMMZ states that "about half a kilometer south of the Military Museum is the Trim
Park Aviation Museum built on the 3,4 hectares of land donated to the Museum by
the City of Gweru… the Double Hangar, which now exhibits various Aircraft,
donated to the Museum by both the Air Force of Zimbabwe and Air Zimbabwe."
Corroborated by aeroflight ("displayed in a large hangar about 400 yards from the
entrance") and by a visitor review ("same ticket gives you entrance up the road
to aviation museum"). OSM carries a museum node named "Aviation Muesum" [sic] on
Bulawayo Road 0.44 km south-southwest of the Military Museum node, matching the
description. **All Zimbabwean airframes are assigned to Trim Park Aviation
Museum.**

The **Zimbabwe Military Museum** on Lobengula Avenue — the parent institution,
ticket point and holder of the Aviation Gallery of aero engines and aviation
history — was researched and confirmed but **holds no airframe**, so it was not
created as a record. A site with no aircraft is not useful in this database. If
the aero-engine gallery is ever judged in scope it should be added then.

**The Bulawayo lead is wrong.** There is no "National Museum of Transport and
Antiquities" in Bulawayo holding aircraft. The NMMZ Western Region page lists only
the Natural History Museum, whose departments are entirely natural-science; the
other Bulawayo museum is the Bulawayo Railway Museum, which is rolling stock. The
"Viscount reportedly at Bulawayo" is the Gweru aircraft, Z-YNA. The two leads
appear to have crossed — the Spitfire genuinely was at Bulawayo decades ago.
**No Bulawayo site is returned.**

**Vampire T.11 wears 4220; its true identity is 2406.** Two inventories carry an
explicit "Displayed ID / Real Identity" column making the distinction, and the
photographic caption record independently reads "Ex RhAF '4220' DH.115 Vampire
T.11 [2406]" with the worn marking in quotes. `tail_number` is 2406; 4220 is in
aliases. This is the one clear repaint case in the collection.

**The Angolan museum's current name is Museu Nacional de História Militar.** The
Angolan Armed Forces' own site and Portuguese Wikipedia use it; English Wikipedia
and the aviation directories use *Museu das Forças Armadas* / Museum of the Armed
Forces, the pre-2013 name. The current local-official form is recorded; the older
Portuguese and English forms should be carried as site aliases when the schema
gains that field.

---

## Derelict-versus-display decisions, named

**Rejected: "Military Aviation Museum of Angola".** aviationmuseum.eu has an
unlinked page under this name listing fourteen aircraft (L-29 I-83, L-39C, SA.342M
H-400, SA.365F H-452, An-30 D2-MBO, An-32A T-250, Cessna 172 I-117, IAR-316B
H-224, MiG-21bis C-369, MiG-23ML, Mi-8MTV H-519, Mi-25 H-224, PC-7, Yak-40K
T-450) on the military side of Luanda airport. **Its own text says "Stored
aircraft"** and it closes with "if you have any picture of this aviation museum,
please share it with us" — the compiler has never seen it. There is no museum
here; this is a stored line-up on a military ramp. An internal tell that the entry
is low-quality: H-224 appears twice, against two different types.

**Rejected: Mirage IIIR2Z tail section, Luanda.** English Wikipedia and
aviationmuseum.eu both describe "downed South African Air Force Puma and Mirage
IIIRZ" wreckage at the fortress. The March 2025 visitor account resolves what it
actually is: **the tail section** of a SAAF Mirage IIIR2Z shot down in July 1979,
mounted on the wall of an indoor hall. A tail section is a relic, not an airframe.
(Note also that the directories' type designation, IIIRZ, is wrong — the
eyewitness reads IIIR2Z.)

**Rejected: SA330 Puma wreck, Luanda.** Same exhibit group, same reasoning, and
unlike the Mirage no eyewitness has described what physically survives.

**Rejected: Canberra T.4 serial 2215, Manyame** — photographed October 1996,
captioned "derelict at Manyame Air Force Base". Derelict, and thirty years stale.

**Rejected: An-26 serial 038, Quelimane, Mozambique** — photographed November
1994, captioned "abandoned debris".

**Rejected: stored airliners at Lusaka Kenneth Kaunda.** A satellite sweep of the
general-aviation and training apron shows several withdrawn airliners parked on
grass. Storage, not display.

**The Bell 205 cabin shell was admitted while the Mirage tail was rejected, and
the line drawn is this:** a helicopter cabin/fuselage shell is the airframe minus
its dynamic components and sits in the collection as an exhibit aircraft; a jet
tail section is a fragment mounted as a war trophy. Reasonable people could draw
it elsewhere; the reasoning is recorded so the call can be reversed cheaply.

---

## Currency, stated plainly

**The honest position on Gweru is that the site is currently alive and the
collection is documented but not individually re-verified.** Evidence the site
operates: the NMMZ page is live and describes the aviation museum in the present
tense; Zimbabwe Field Guide carries a 2026 copyright and describes the eleven
aircraft as complete and displayed; the tourism board lists the museum as open;
visitor reviews from 2018 and 2019 describe guided tours; a photographer posted a
first-hand Spitfire photograph in July 2023.

Per-airframe evidence is weaker, and this is the important caveat: **the
comprehensive photographic set of the collection — every one of the eleven plus
the Bell shell — was shot by a single photographer around 2000–2006 and only
uploaded in 2013–14, which is why it *looks* recent in search results and is
not.** For nine of the twelve Gweru rows the most recent independent confirmation
is roughly twenty years old, mediated by two compilations that assert current
completeness. Only the Spitfire (2023) and the Viscount (2019) have modern
first-hand confirmation.

Livingstone and Luanda are in much better shape — June 2025 and March 2025
respectively.

---

## Satellite work, and what it did and did not settle

Esri World Imagery for the Trim Park site tops out at zoom 17, roughly 1.1 m per
pixel; zoom 18 and 19 return the grey "no imagery" placeholder. At that
resolution the compound is unambiguous — a fenced open plot of roughly the stated
3.4 ha fronting Bulawayo Road, with a large double-bay shed matching NMMZ's
"Double Hangar" — which confirms the *site* and the OSM coordinate. It cannot
resolve individual airframes, and aircraft inside a hangar are invisible from
above in any case, so **satellite did not confirm any Gweru airframe** and no
such claim is made. At Lusaka, imagery is available at zoom 19 (~0.3 m/px) and
was genuinely useful — see the DC-8 question below.

---

## Coordinate provenance and access types

Every coordinate came from OpenStreetMap Nominatim, not from estimation:
Zimbabwe's Gweru aviation site from the museum node on Bulawayo Road; Livingstone
Museum from its museum node; Fortaleza de São Miguel at -8.8076194, 13.2232255,
agreeing with the coordinates on Wikipedia. No coordinate was inferred from a
street address or a map eyeball.

All three sites are `public`. Trim Park: NMMZ operates it as a public museum with
an entrance fee and published hours. Livingstone: Zambia's oldest and largest
museum, published daily hours 09:00–16:30, its own website. Luanda: daily
08:30–17:30 with an admission fee, and the March 2025 account is of a cruise-ship
passenger walking in. **One caveat that did not change the call** — the Angolan
Armed Forces' own news site carries an item headlined to the effect that the
military history museum has restrictions on visits. That page could not be
retrieved (faa.ao failed twice through the proxy). If the restrictions turn out to
be substantive, this site may belong at `appointment`.

---

## Deliberate blanks

**`year_built` is populated on exactly one row**, the Viscount (1956, from a first
flight of 28 March 1956 and a handover of 24 April 1956 in a type-specialist
register). Every other row is blank. In particular **no build year was derived**
for the Spitfire from its 28 March 1951 service-entry date, for the Chipmunk from
its construction-number block, or for either Portuguese T-6 from its
arrival-in-Portugal date. **Rhodesian serials like 1380, 1188, 2406 and 3614 are
four-digit numbers that look like years and are not.**

`tail_number` is blank on the Mignet HM.14 (no inventory records one) and on the
Bell 205 shell (only an unverified painted marking, which sits in aliases).
`postal_code` is blank throughout; none of these three countries uses postal codes
in a way that would populate the field usefully. The Luanda museum has no
verifiable website; a telephone number (+244 222 372 623) exists but there is no
field for it.

---

## Documented negatives — named, so nobody redoes them

**Namibia.** No preserved or displayed aircraft found. The Namibian Air Force
serial register (ab-ix) records fates only as written off, withdrawn, cancelled,
current or unknown — **not one preservation entry**. The National Museum of
Namibia holds no aircraft and two of its three Windhoek sites (Owela, Alte Feste)
were closed and in poor condition as of 2023. Swakopmund, Tsumeb, Eros, Hosea
Kutako and Grootfontein produced nothing. No SAAF Border War relic in Namibia is
displayed.

**Botswana.** Nothing. The Botswana National Museum has no aviation holdings in
any source consulted, and no BDF Air Wing gate guard is documented at
Thebephatshwa or Sir Seretse Khama.

**Mozambique.** Nothing. The Maputo province monument register lists no aircraft
monument; the Museu da Revolução and the Fortaleza de Maputo have no aviation
exhibit. Civil-war MiGs exist but none is documented as displayed. Note that the
**Samora Machel Monument**, which does memorialise an aircraft loss, is at Mbuzini
in **South Africa** and is out of scope on two grounds.

**Malawi, Lesotho and Eswatini.** Nothing in any of the three — no national
museum aviation holding, no air wing display, no monument.

**Zambia beyond Livingstone.** The Lusaka National Museum holds no aircraft. No
Zambia Air Force display was found at Lusaka City Airport or Mumbwa, contrary to
the starting hypothesis, and no preserved Zambian MiG-21 or SF.260 was located.
The Livingstone Chipmunk is the only ZAF airframe in the photographic record with
a display caption.

---

## Ranked open questions

1. **Is the Gweru collection physically intact in 2026?** The highest-value
   follow-up in this package, and nothing on the open web answers it. A visitor
   photo set, or an email to NMMZ Central Region (+263 242 774208). Two decades of
   funding collapse make a per-airframe check worth doing before these twelve rows
   are treated as solid.
2. **Where is MiG-21bis C340?** South Africa returned it to Angola on 17
   September 2017, flown in by an Angolan Il-76 after 26 years at the SAAF Museum
   at Swartkop, having force-landed in Namibia in 1988. Construction number
   N75096900. Its Angolan destination was never reported and no photograph of it
   since has surfaced. If it went to the fortress museum or to a plinth, that is a
   record; if it went to the airport storage line, it is not. **No row created,
   because a record needs a site.**
3. **Is DC-8-62AF 9J-MKK actually displayed at Lusaka?** English Wikipedia's
   preserved-Douglas list says "On static display" at Kenneth Kaunda
   International, ex-Japan Air Lines "Wakasa", last flown 2008 — **with no
   citation**. Zero photographs on JetPhotos; its only dated photograph anywhere is
   28 October 2013 at Lusaka with no display remark. An Esri sweep at 0.3 m/px
   across the KKIA training and general-aviation apron, where a 47-metre
   four-engined DC-8 would be conspicuous, found two rear-engined T-tail jets, two
   twin turboprops and light aircraft — **no DC-8**. That does not cover the whole
   airfield, so this is "not found where I looked", not "proven gone".
4. **Are there Air Force of Zimbabwe gate guards, and where?** A 2022 survey
   article asserts three Vampires and one Canberra serve as gate guards at AFZ
   bases, but names no base and no serial, and no photograph of any of them could
   be found. Manyame and Josiah Tungamirai (Thornhill) are the obvious candidates.
   A single plinthed Vampire at a base gate is a legitimate site record; it just
   cannot be written without a base and an airframe.
5. **Has Trim Park received anything since the eleven?** NMMZ says the aviation
   museum "is slowly taking shape". Zimbabwe Field Guide names AFZ airframes it
   thinks should be donated next — an AB-205 Cheetah, a Dakota, an Alouette III, a
   Reims Cessna 337G Lynx and a Hawk 60. If any transferred after 2016 this
   inventory is short.
6. **Is Tiger Moth SR26 the airframe or the paint?** Two compilations say
   identity; one narrative source implies scheme. Low stakes, but it is the one
   remaining identity that would not be defended hard.
