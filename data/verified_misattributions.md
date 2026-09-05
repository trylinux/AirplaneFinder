# Verified duplicate / misattributed aircraft — September 2026

Checked the whole live database (850 exhibit links, 835 aircraft) and then
verified each candidate against external airframe registries.

## Headline

**There are no duplicate aircraft records.** Zero cases of two rows
describing one airframe — the `UNIQUE (model, tail_number)` index is doing
its job, and the earlier whitespace cleanup means the dedupe script can now
actually see across records.

**What exists instead is worse and less visible: 12 aircraft records are
each linked to 2–4 museums at once.** One airframe, several museums. That
is physically impossible, and it inflates every museum's apparent
collection. All 12 are low ids (38–69) — all seed data, none from the
California import.

## Verified findings

Seven of the twelve carry a real serial, so each could be traced to a
specific airframe. **Six of the seven are not at any of the museums claimed.**

| Aircraft | id | Claimed by | Actually at | Verdict |
|---|---|---|---|---|
| P-51D 44-74936 | 46 | CAF Arizona, EAA, Duxford, **NMUSAF** | National Museum of the USAF | ✅ one claim correct |
| F-15A 76-0008 | 49 | Hill, NMUSAF | **March Field Air Museum** (on loan from NMUSAF) | ❌ wrong museum |
| C-130H 74-1686 | 38 | Hill, March Field, NMUSAF | **Empire State Aerosciences Museum**, Schenectady NY | ❌ not in database |
| F/A-18A 161749 | 52 | Museum of Flight, Pensacola, Pima | **Flying Leatherneck**, Irvine CA | ❌ not in database |
| C-47A 43-15073 | 58 | CAF Arizona, NMUSAF, Pearl Harbor | **Merville Gun Battery Museum**, Normandy, France | ❌ not in database |
| UH-1H 66-16579 | 61 | Hill, NMUSAF, Pensacola, Pearl Harbor | **The Helicopter Museum**, Weston-super-Mare, UK | ❌ not in database |
| Spitfire Mk.IX MK356 | 66 | Duxford, Musée de l'Air, RAF Museum | **Destroyed in a fatal crash, 25 May 2024** | ❌ aircraft no longer exists |

### The pattern

This is not random. In four cases (F-15A, F/A-18A, C-47A, UH-1H) the museum
genuinely holds an aircraft *of that type* — just a different airframe:

- Hill's F-15 is **77-0090**, not 76-0008.
- Pima's F/A-18A is **163093** (ex-Blue Angels), not 161749.
- CAF Arizona's C-47 is **42-23518** "Old Number 30", not 43-15073.
- Hill's Huey is an HH-1H, **70-02470**, not 66-16579.

So the seed paired real serials with plausible-sounding but wrong museums.
Every serial is real; the *pairings* were invented.

### MK356 deserves its own note

A real and historically significant Spitfire LF Mk.IXe — but it was never in
a museum. It flew with the RAF's Battle of Britain Memorial Flight at RAF
Coningsby, an operational unit, and was **destroyed in a crash on 25 May
2024 that killed the pilot, Sqn Ldr Mark Long**. The record is wrong twice
over: wrong kind of custodian, and the airframe no longer exists. It should
be deleted, not repointed.

## The five without serials

Wright Flyer (63), Curtiss JN-4D (64), Mitsubishi A6M Zero (67),
Messerschmitt Bf 109G (68) and de Havilland Mosquito B.35 (69) are each
linked to 2–3 museums with no tail number. These are *type* records being
shared across museums rather than one record per airframe — exactly the
conflation the Castle seed rework fixed. Each of those museums does hold an
example of the type, so the links aren't wrong so much as under-specified.

Fixing them properly means splitting each into one record per museum, which
needs a serial per airframe to be worth doing. Left alone for now, and
excluded from the fix script.

## Method

1. `GET /api/v1/exhibits` — the flat endpoint built for the admin exhibits
   page — pulled all 850 links in one request.
2. Grouped by normalised tail number, including FY-serial zero-padding so
   `52-008` and `52-0008` compare equal.
3. Grouped by aircraft id to find records with more than one museum link.
4. Verified each serial against aerialvisuals.ca airframe dossiers,
   warbirdregistry.org, the museums' own pages, and aviation-safety.net.

Sources: [aerialvisuals.ca](https://aerialvisuals.ca/AirframeDossier.php?Serial=15385) ·
[warbirdregistry F/A-18 161749](https://www.warbirdregistry.org/jetregistry/f18-161749.html) ·
[warbirdregistry UH-1 66-16579](https://www.warbirdregistry.org/heloregistry/hueyregistry/huey-6616579.html) ·
[March Field F-15](https://www.marchfield.org/f-15-eagle/) ·
[SNAFU Special](https://www.the-snafu-special.com/) ·
[MK356 crash record](https://aviation-safety.net/wikibase/388312)
