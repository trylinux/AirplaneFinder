# Nebraska

26 museums, 104 aircraft. The state previously held one record — the Strategic
Air Command & Aerospace Museum at Ashland, with a single SR-71 attached.

## Sources and their weight

The **SAC & Aerospace Museum publishes a per-aircraft exhibit page carrying the
serial verbatim**, and it supplied most of the acceptance and delivery dates
used for `year_built`. That is the strongest single source in this pass;
Baugher and Aerial Visuals were used to corroborate rather than to originate.

For everything else, **Aerial Visuals' Nebraska locator and its per-site
dossiers** did the work — they carry mapped display coordinates, which is why
almost every monument here has a fix rather than a centroid. Overpass was
unreachable through the proxy during the sweep.

**silverhawkauthor's Nebraska page** was used only to generate leads, and three
of its entries are demonstrably wrong (see exclusions).

## A cross-agent collision, resolved

The **F-105D 61-0069** turned up twice: once as a SAC Museum aircraft
"displayed off-site on a pylon along I-80", and once as an apparently separate
Ashland-area site four miles from the museum. Same airframe. It is recorded
once, under the museum, with the pylon location in its aliases. Had it gone in
twice the `(model, tail_number)` unique key would have caught it — but only
after one file had already imported.

## Corrections made

- **The pre-existing SR-71A 61-7964 row had the manufacturer as "Lockheed
  Martin"** — the aircraft was built by Lockheed, two decades before the merger.
  Corrected in place, with its service history and 1966 first-flight date added.
- **Only one P-59 survives at Minden**, 44-22656. silverhawkauthor lists a
  second, 44-22639, which is not among the six surviving Airacomets anywhere.
- **There is no F-100 at Fairbury** — locals confirmed it to Aerial Visuals;
  only the T-33 is there.
- **The EC-135A at Offutt is 61-0287**, not the 61-0582 silverhawkauthor gives.
- **The Nebraska National Guard Museum is at Seward**, not Lincoln, and holds no
  aircraft; the Guard-associated Huey is at Seward Municipal Airport about a
  mile and a half away, recorded as its own site.
- **The Aurora F-100F is a QF-100F drone conversion**, drone number QF418, and
  its USAF serial is not established — recorded with a blank tail and
  `role_type: drone` rather than the unverifiable serial one source offers.

## Judgment calls

**The B-36J is a complete aircraft**, not a nose section — worth stating because
most surviving B-36s are not.

**Three SAC Museum airframes are in the Durham Restoration Gallery** as of
September 2025 — the Vulcan, the T-29A and the HU-16B — and are recorded
`under_restoration`. The **F-117A 85-0831 left that gallery for Hangar A on
25 August 2025** after a five-year restoration, and is recorded `on_display`;
its finish is an applied vinyl wrap rather than paint. The **TB-25N 44-28738 is
a fuselage only** and is `in_storage`.

**Four SAC items are recorded but flagged**: the AGM-86B, X-38, Vela satellite
and the Apollo boilerplate appear on Wikipedia sourced to older museum URLs but
are absent from the museum's current exhibition index. CSM-009 likewise has no
live exhibit page. They are recorded because the source lineage is the museum
itself, with the doubt in each row's aliases.

**Offutt's three airframes are recorded at one site.** The B-17F sits on the
south side of the base rather than at Zorinsky Air Park; that is noted in its
aliases rather than split into a second record, since access is identical.

**Harold Warp Pioneer Village is a general pioneer museum**, but its aircraft
are genuine and significant — an original 1910 Curtiss Pusher flown by Charles
Hamilton on the first New York-Philadelphia round trip, a P-59B Airacomet, and
an HNS-1 Hoverfly. Only the Wright Flyer is a replica.

## Excluded, and why

- **Nebraska National Guard Museum, Seward** — no aircraft. Note its former
  domain nengm.org has expired; use the ne.ng.mil page.
- **Duncan Aviation's pole-mounted Learjet 35, Lincoln** — a corporate monument
  with no serial and no mapped coordinate. Worth adding if either surfaces.
- **An Arrow Sport reportedly suspended in the Lincoln Airport terminal** — one
  stale source.
- **Nebraska Army National Guard AASF, Grand Island (AH-1F 68-15108)** — single
  stale source, not in the Aerial Visuals index.
- **Alliance Municipal Airport C-45H 52-10965** — privately owned and
  operational, not a display.
- **Millard Airport Lim-6R N17JL** — moved out of state to Reno.
- **Offutt's Le May Aero Club T-41s** and the **Omaha Police OH-58As** —
  operational aircraft.
- **Columbus Municipal Airport** — an Aerial Visuals location with no confirmed
  airframes.
- **Kearney, Stuhr Museum (Grand Island), the Durham Museum (Omaha), Fremont,
  and about fifteen other towns** — no displayed airframes found. North Platte
  hosts the CAF Airpower History Tour, which visits rather than resides.
- **No Commemorative Air Force unit is based in Nebraska.**
- **AH-1S 78-23108 and UH-1 69-15330** — formerly at the Lincoln ANG park, since
  moved on.
- **SAC Museum departures**: C-133B 59-0536 (to the AMC Museum, Dover, in 2000)
  and UH-13J 57-2729, the Eisenhower presidential helicopter, which returned to
  the Smithsonian in 2004 and is still listed at Ashland by stale sources. The
  C-124A that one list places there is at Dover and never was at Ashland.

## Blank fields, deliberately

`year_built` comes from museum-stated acceptance, delivery or first-flight
dates. It is blank on every monument, on the Offutt statics, and on the SAC
Museum's TB-29, U-2C, RB-45C, B-25N, both MiGs, the MQ-1C, the B-1A and all
missiles and spacecraft. No fiscal-year prefix was converted to a year anywhere.

**Beatrice Municipal Airport has no postal code.** OSM's reverse geocode
returned a Missouri ZIP for that point, which is plainly a data error, and no
authoritative value was found — so it is blank rather than guessed. Every other
Nebraska postal code here was reverse-geocoded from the display coordinate.

Tails are blank on the Aurora QF-100F, and on the Pioneer Village Curtiss
Pusher, Heath Parasol, Weedhopper, KR-2, Pitcairn autogiro, Bensen Gyro-Glider
and Wright Flyer replica.

## Needs a human on site

- **Offutt AFB** — the three identities are solid but no public source confirms
  them after 2023, and the base is restricted. The 55th Wing history office
  would settle it.
- **The MiG-23's identity.** Wikipedia's survivor list says German Air Force
  20+15; the museum says construction number 0390324630, marked Red 338 in East
  German service. Almost certainly one ex-NVA airframe, but nothing ties the two
  numbers together in print.
- **The Lincoln ANG F-86** — Aerial Visuals says F-86D 53-0831, another source
  says F-86L 52-3760. Recorded once with the conflict in aliases.
- **The four flagged SAC space and missile items** above.
- **Two Pioneer Village registrations** where the museum's own account and
  Aerial Visuals disagree — the JN-4D (NC1350 vs N782) and the Stinson SM-8A
  (NC907W vs NC903W).
- **The Grand Island Guard Cobra** and the **Duncan Learjet**, either to record
  or to strike.
