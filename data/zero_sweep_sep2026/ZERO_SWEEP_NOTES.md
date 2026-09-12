# The zero-record sweep — 70 countries and territories, 10 September 2026

Every sovereign state and notable territory holding **no record at all** was
identified by diffing a 223-entry reference list against the live database, then
checked — deliberately — **in its own language**, because English Wikipedia is
systematically thin on small countries and a native-language article on an air
force, a national museum or a capital city routinely names an airframe that
appears nowhere in English.

Seven fetch passes (Sonnet) grouped by language; all deconfliction, adjudication
and assembly done separately (Opus). The fetch passes were told to report
uncertainty rather than resolve it, and they did — which is what made the
adjudication worth doing.

## Result

**10 new countries and territories · 11 sites · 20 airframes.**
Database country count went **153 → 163**.

| Country | Site | Airframes |
|---|---|---|
| Solomon Islands | Vilu Military Museum, Guadalcanal | 7 |
| Falkland Islands | Falkland Islands Museum and National Trust, Stanley | 3 |
| Benin | two Cotonou airframes | 2 |
| Lesotho | LDF Air Wing display, Maseru | 2 |
| Guam | Arc Light Memorial, Andersen AFB | 1 |
| Curaçao | Curaçao Museum, Willemstad | 1 |
| Palestine | Al-Sairafi 707 restaurant, Wadi al-Badhan | 1 |
| Aruba | Queen Beatrix International Airport | 1 |
| Guinea | Conakry air base | 1 |
| South Sudan | Wau | 1 |

**The best find is the Vilu Military Museum** on Guadalcanal — an open-air museum
founded in 1975 by Fred Kona, abandoned during the civil unrest and later
reclaimed by his family, holding seven recovered Guadalcanal-campaign airframes
including **F4F-4 BuNo 12068**, **J2F-5 Duck BuNo 00791** and the nose section of
**G4M1 "Betty" #1570** wearing tail code 377.

## Two corrections the fetch passes got wrong, and I caught

**1. Guam's B-52D 56-0586 was scrapped, and every published list still shows it.**
The fetch pass recorded it in good faith from three Wikipedia and Commons
sources, all of which say the complete aircraft stands at the Arc Light Memorial.
It does not. Guam's climate corroded it beyond saving and it was cut up from
about **2014**; the **vertical tail was preserved on a plinth** alongside a B-52H
tail, the memorial was redesigned around a **B-52D silhouette laid out on the
ground**, and further sections went to Andersen's Heritage Hall in the passenger
terminal. An earlier B-52D at the same site, 55-0100, was scrapped in 1983 for
the same reason. **The record now says tail section only.** Source: Vintage
Aviation News.

**2. The Falkland Islands are not a zero.** The fetch pass concluded they were,
having found that every known Pucará survivor is accounted for in a UK museum —
which is true, and is the wrong question. The **Falkland Islands Museum and
National Trust** in Stanley holds three airframes. The **Phantom FGR.2 XV409**
nose section is double-sourced: Thunder & Lightnings' survivors register and
aviationmuseum.eu agree that it stood as the Mount Pleasant terminal gate guard
from January 2003, was condemned for structural corrosion in late 2011, was cut
up in January 2012, and that **its nose was kept for the museum**. A Lynx HMA.8
and a Sea King HAR.3 are also held, but on aviationmuseum.eu alone — so, per this
project's standing rule that it is a lead list and never a fact, **their serials
are recorded in the description and `tail_number` is left blank** until a second
source or a dated photograph confirms them.

## Adjudications

**Grenada — Pearls Airport An-26 and An-2R: EXCLUDED.** These are the two aircraft
seized in the 1983 invasion, they are a named stop on tourist itineraries, and
they have their own TripAdvisor listing — which is exactly the profile that makes
this a hard call. It fails anyway, and the **Grenada Airports Authority's own
history page is what decides it**: it records "remnants of Cuban and Soviet
aircraft still visible on site" and describes the site as used "for drag racing,
livestock grazing, and as a shortcut for local transportation." No retention, no
signage, no maintenance, no visitor provision. This is the mirror image of
Sólheimasandur, where the landowners closed vehicle access, built a paid car park
and ran a shuttle. **Survival by neglect is not presentation.**

**Suriname — the SLM Flight 764 memorial: EXCLUDED.** Four engine cowlings
recovered from Suriname's worst air disaster, mounted on columns with victim
plaques at Rusthof cemetery. That is a memorial built *from* debris, not a
retained airframe — the same class as the UTA 772 memorial at Ténéré, which this
project already excluded.

**Aruba — an unnamed OSM node: INCLUDED, with the uncertainty stated.** A bare
`historic=aircraft` node reverse-geocodes to inside Queen Beatrix International
Airport, whose wartime name was Dakota Field. No name, no type, no photograph,
nothing in any other source. It is recorded as `Unidentified` because an
airframe-level node inside an international airport is a far stronger prior than
the unnamed node in open country this project rejected at Playa Grande Ixcán —
but the description says plainly that one untyped node is the whole of the
evidence.

**Storage is not display, again.** Excluded on the project's own rule, all coded
`std` (stored) rather than `pre` (preserved) by spottingmode: Burundi's Bujumbura
DC-3, Mi-8 and Caravelle group; Equatorial Guinea's Bata Mi-26; the Comoros
Mi-8MT and Mi-14PZh at Moroni; and the five-airframe group at Bangui M'Poko,
which reads as a grounded air force rather than a display. **South Sudan's Juba
aircraft dump** was investigated specifically and excluded as derelict.

**Pacific wrecks.** Million Dollar Point (Vanuatu) is a dumping ground.
Chuuk Lagoon (Micronesia) is underwater and in situ. Guadeloupe's four "ULM
Caraïbes" OSM nodes are tagged `artwork_type=sculpture` and are not airframes —
re-verified this pass, having been excluded once before. Timor-Leste's Douglas
A-26 reported "parked" at Dili in the 1980s has no evidence of deliberate display.

## Where the zeros are real, and where they are not

**This distinction is the point of the exercise.** A well-searched zero is a
finding and stops the country being re-researched every year. An unsearched zero
recorded as a finding is worse than useless.

**Genuine, well-searched zeros — with the queries logged in the dossiers:**
San Marino · Andorra · Monaco · Liechtenstein · Vatican City · Kosovo · Bhutan ·
Maldives · Panama · Guyana · Haiti · Bermuda · Bahamas · Martinique · Réunion ·
Mauritius · Seychelles · Eswatini · Cape Verde · Gambia · Liberia · Mauritania ·
Sierra Leone · Togo · Western Sahara · Vanuatu · Fiji · New Caledonia ·
French Polynesia · Marshall Islands · Micronesia · Kiribati ·
Northern Mariana Islands · Samoa · American Samoa · Tonga · Cook Islands ·
Tuvalu · Nauru · Palau · Timor-Leste · Guadeloupe

Two worth singling out. **Panama's zero was re-tested and holds** — the earlier
pass could not reach OSM at all, so this one ran Overpass on all three mirrors
(`area["ISO3166-1"="PA"]`, zero elements) and added Spanish-language extracts on
the Fuerza Aérea Panameña and SENAN. And **Réunion**, which was the strongest
prior in its whole brief — France plinths retired aircraft routinely — was
searched to the Musée de Villèle, Base Aérienne 181 and the Commons categories,
and has nothing.

**NOT well-searched — do not read these as absence:**

- **Gibraltar.** The single strongest remaining candidate anywhere in this sweep.
  RAF Gibraltar at North Front has a long history and the Spanish-language
  sources were never reached.
- **Macau.** Portuguese and Cantonese — its two highest-value languages — were
  never reached. The 1948 Miss Macao hijacking aircraft crashed into the sea and
  was never recovered, so that lead is closed; the museums are not.
- **Greenland.** The **Narsarsuaq museum**, at the wartime Bluie West One airbase,
  **closed in April 2026** when the settlement's airport was downgraded to a
  heliport — and no source found says what it held or where that went. An open
  lead, not a zero.
- **Jersey**, **Faroe Islands** — native-language editions barely queried.
- **Burundi, Central African Republic, Comoros, Equatorial Guinea** — the only
  source reached was spottingmode, and only its `std` entries.
- **Solomon Islands beyond Vilu** (Betikama, Honiara) and **Kiribati/Betio**,
  where recovered Japanese guns are confirmed but aircraft are not.
- Several Caribbean islands — Dominica, St Kitts, St Lucia, St Vincent, Antigua,
  Cayman, US Virgin Islands — got an OSM check only.

## The constraint that shaped this sweep

**The Wikimedia APIs were throttled hard on this environment's shared egress** —
30 to 120 seconds between successful calls, across all Wikimedia projects
including Wikidata and Commons. Every fetch pass hit it and several spent most of
their budget waiting. That is why the native-language coverage is uneven and why
the "not well-searched" list above is as long as it is.

**For the next pass**: sleep 3–5 seconds between calls from the start, back off to
60 s on the first 429, and **prefer `action=query&prop=extracts&titles=<exact
title>` over `list=search`** — one targeted extract on an article title you can
predict is worth ten searches you never get to run.

OSM Overpass was also largely unavailable: all three mirrors timed out for the
entire Pacific pass, and returned zero elements across ten African countries and
across the European microstates. **`overpass-api.de` remains blocked by the
container proxy**; `maps.mail.ru` and `overpass.private.coffee` both answered for
Aruba and Panama.

## What is left

1. **Gibraltar, Macau, Greenland, Jersey and the Faroes** — a second pass in
   Spanish, Portuguese, Cantonese, Danish and Faroese. Gibraltar first.
2. **The Narsarsuaq museum's collection** — where did it go in April 2026?
3. **Corroborate the Falklands Lynx XZ725 and Sea King XZ593.** One dated
   photograph moves both serials from the description into `tail_number`.
4. **Palestine**: the Al-Sairafi 707's status since 2023 is unconfirmed, and the
   brief this pass worked from described *two* 707s under different owners at a
   neighbouring location — every source found describes one aircraft at Wadi
   al-Badhan. Worth resolving whether there was an earlier, separate pair.
5. **Re-verify the four single-source African rows** — Conakry's MiG-17F 715
   (2018), Cotonou's TriStar 9L-LFB (2016), Cotonou's TY-AAM (2025, type
   unresolved — spottingmode gives it only as "Petrel") and Wau's An-26 ST-APO
   (2018). All are `restricted` and none has confirmed public presentation.
