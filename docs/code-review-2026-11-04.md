# AirplaneFinder code and security review — 2026-11-04

Reviewed the repository at `5884b2b` and implemented the fixes described below
in the working tree. No production data, deployments, or historical research
records were changed. This is a source review with local regression testing,
not a penetration test or an OWASP certification.

## Scope and architecture

The application is a Flask/MySQL catalog with public search, museum and airframe
detail pages, a shared aircraft-type library, maps, histories, and trip planning.
Flask-Login sessions and hashed Bearer API keys protect editing. Managers have
museum/country scopes; aircraft administrators manage shared catalog records;
administrators also manage accounts. Jinja, desktop/mobile JavaScript, SQL
migrations, import/export tools, research planners, maintenance scripts, tests,
configuration, and recent Git history were included in the review.

There is no application LLM client, model execution, RAG store, or autonomous
agent runtime. AI-assisted research and scripts that apply generated plans are
the relevant prompt-injection boundary. Catalog text and research documents
must remain data, even when they contain instructions addressed to an agent.

## Findings and fixes

Priorities reflect the consequences and required access in this application,
not a formal CVSS calculation. All entries in this table were addressed locally.

| Priority | Finding and consequence | Implemented correction |
| --- | --- | --- |
| P1 | The first public registration became an administrator. An outsider could claim a fresh deployment. | Public registration always creates a viewer. Initial administration requires the documented local bootstrap. Registration also initializes session timestamps. |
| P1 | Aircraft-type search combined a filtered query with a broader union, exposing unpublished records. Other draft reads did not consistently require an editor. | Apply publication restrictions to the combined search predicate. Draft access requires an editor, with a readwrite/admin key when using Bearer authentication. Explicit invalid credentials do not fall back to a session. Private/Bearer responses use `no-store`. |
| P1 | Merge tooling could delete a losing record after partial transfer, dropping facts, histories, notes, assignments, or fields. | Shared transactional merge services preserve related data, reject conflicting fields, and check the reviewed losing museum collection. New authorized merge endpoints commit once per operation. The remote script stops on failure and has no client-side DELETE fallback. |
| P1 | Stored website/source values could use active URL schemes, and several management error messages interpolated server text into HTML. | Central HTTP(S) URL validation rejects credentials, controls, malformed ports, and unsafe schemes. Render/serialization guards cover legacy URLs. Error strings are escaped before HTML insertion. |
| P2 | Password changes left existing session and remember cookies usable. Logout used a state-changing GET. | Login identities include a password-hash fingerprint, invalidating old cookies when passwords change. Logout is POST with CSRF-protected forms. |
| P2 | API shapes, lengths, booleans, numbers, and enums were inconsistently checked. Malformed values could cause 500s or unintended publication; DB errors could disclose SQL/details. | Shared schema-based text checks, bounded aliases/integers, finite decimal validation, strict flags, and endpoint validators. Sanitized 400/409 responses and rollback on rejected writes. Duplicate exhibit links return 409. |
| P2 | Alternate API-key creation routes could bypass their individual quotas and applied different expiry rules. | Both routes share an account quota and one label/expiry validator. Expiry is a bounded positive integer. |
| P2 | Public/proximity APIs lacked consistent consumption limits; legacy aliases could evade an endpoint limit. | Configurable API limits and a shared proximity/geocoding limit. A shared production limiter backend remains a deployment requirement. |
| P2 | Provider payloads could trigger parsing errors or excessive polyline decoding; geocoding wildcard queries could match unrelated cached places. Long cache keys exceeded the production column. | Bounded route response/polyline parsing and safe provider failures, literal location matching, bounded query text, and hashed long-query cache keys. |
| P2 | Maintenance plans could include arbitrary extra fields, malformed IDs, or structured values. Several appliers duplicated hardcoded paths and applied by default. | A shared plan validator enforces positive IDs, allowed fields, and scalar/list shapes. Names, construction-number, country, and merge runners preview by default and require explicit targets for writes. Manufacturer/variant appliers validate plans and return failure on conflicts. |
| P2 | Import filtering used an older identity rule and could discard distinct variants/operators. Aircraft exports omitted construction numbers and operator countries. | Shared designation/identity helpers preserve those distinctions and recognize usable construction numbers. Export both identity fields. Merge planning excludes placeholder construction numbers and checks manufacturer/operator context. |
| P2 | Exported catalog strings could become spreadsheet formulas. | Default CSV output prefixes potentially active strings with an apostrophe. JSON and explicit `--raw-csv` preserve machine-interchange text; documentation explains the tradeoff. |
| P2 | Dependencies had published advisories; development defaults exposed debug mode and a broad bind address. Local secret configuration was not actually ignored. | Upgrade Flask to 3.1.3 and cryptography to 50.0.0, disable debug by default, bind localhost, reject missing/default production secrets, and ignore `web.config`. |
| P2 | User-controlled text could forge additional log lines; Bearer writes were attributed to anonymous. | Escape control characters in log formatting and record the effective API user. Login IP uses the peer address rather than trusting arbitrary forwarded headers. |
| P2 | Trip selection could recommend restricted museums despite visitor-access rules. | Exclude restricted museums from trip candidates; existing discoverability and explicit proximity opt-in remain. |

Other correctness changes include clamping haversine floating-point input,
grouping all selected museum columns for stricter SQL compatibility, and
mirroring the existing SQL airframe/exhibit uniqueness rules in ORM metadata.
These do not replace production migrations or solve MySQL nullable-key races.

## OWASP coverage

The mappings below use the [Web Top 10 2025](https://top10.owasp.org/2025/0x00_2025-Introduction/),
[API Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/), and
[LLM Top 10 2026 published source](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/README.md).
Labels are shortened. The LLM project repository identifies its 2026 release
as published on August 4, 2026. A category marked absent means no corresponding
runtime was found; it does not certify external research agents or tools.

### Web

| Category | Repository assessment |
| --- | --- |
| A01 — Authorization | Fixed registration escalation and draft disclosure. Existing role, assignment, object ownership, and key permission tests pass. New merge operations require catalog administrators. |
| A02 — Configuration | Safer bind/debug defaults and secret guard; actual TLS/proxy/worker configuration remains unverified. CSP still permits inline scripts/styles used throughout the templates. |
| A03 — Dependencies | Upgraded affected runtime packages; resolved dependency audit reports no known advisories. Transitive pinning, hashes, and automated recurring audit are follow-up work. |
| A04 — Crypto | Existing password/API-key hashing retained; password changes revoke cookies. Production transport and secret handling cannot be established from local tests. |
| A05 — Injection | Fixed URL/HTML/CSV/log injection paths. SQLAlchemy predicates bind values; inspected dynamic SQL was not an exposed user-controlled SQL execution interface. No application eval/exec path for catalog text was found. |
| A06 — Design | Replaced destructive multi-request merge behavior with atomic server operations. Conflicting data requires reconciliation; whole batches are not atomic. |
| A07 — Authentication | Existing lockouts and CSRF tests pass. Closed cookie revocation, GET logout, and key quota inconsistencies. |
| A08 — Integrity | Plan field allowlists, shared identity rules, preserved merge relations, and corrected export fields reduce accidental or generated-data corruption. Semantic research accuracy still requires evidence review. |
| A09 — Auditability | Improved actor attribution and log formatting. Central collection, retention, and alerts are operational work. |
| A10 — Error paths | Invalid inputs and provider responses fail predictably; write errors roll back and suppress database details. Load and database outage behavior need deployment testing. |

### API

| Category | Repository assessment |
| --- | --- |
| API1 — Record access | Museum scopes, key ownership, and editor/admin boundaries exercised; public catalog reads are intentional. |
| API2 — Credentials | Bearer/session distinction, invalid-token behavior, expiry, cookie revocation, and shared key quota checked. |
| API3 — Field access | Write handlers select fields explicitly; publish flags now require booleans. Draft fields no longer leak through search. |
| API4 — Resource budgets | Added shared limits; existing body/row/stop bounds retained; upstream response parsing bounded. Some complete-list endpoints remain costly as the catalog grows. |
| API5 — Operation access | Administrative operations remain role-gated; merge operations use the same catalog-admin boundary. |
| API6 — Automated abuse | Signup/login/key/bulk/proximity flows have controls. Multi-worker quotas and provider billing caps need production configuration. |
| API7 — Outbound targets | Runtime routing uses a fixed HTTPS provider; catalog source URLs are links, not arbitrary server fetch targets. Operator-run research downloaders still require trusted target selection. |
| API8 — Deployment | Safer defaults and JSON API errors implemented. Proxy trust, database privileges, and actual secure headers require deployment inspection. |
| API9 — Inventory | Reviewed route aliases, read/write documentation, migration instructions, and maintenance scripts. No machine-readable OpenAPI inventory exists. |
| API10 — Provider data | Route measurements, geometry, shapes, and payload size are validated. External geocoder/provider availability remains an integration dependency. |

### LLM and prompt injection

| Category | Repository assessment |
| --- | --- |
| LLM01 — Injected instructions | No model runtime in the app. External pages, CSV cells, descriptions, and research notes can carry indirect instructions to a researching agent. Plans now accept data only within allowed write fields. |
| LLM02 — Secret disclosure | No prompt/model channel exists in the server. Research tools must not include API credentials or private configuration in model context or generated artifacts. |
| LLM03 — Agent authority | No autonomous tool loop found. Maintenance scripts are the meaningful write capability: explicit destinations, preview defaults for the revised runners, narrow fields, and stop-on-error reduce consequences. |
| LLM04 — Dependencies | No model/plugin dependency chain in the app. Python dependency findings were fixed; externally operated agents are outside this repository. |
| LLM05 — Poisoned data | CSV/research data can contain plausible but false identifiers, aliases, or locations. Mechanical checks cannot prove historical truth. Provenance and human adjudication remain necessary. |
| LLM06 — Consumption | No inference billing or token loop. API/provider request budgets address the equivalent runtime concern. |
| LLM07 — False claims | Existing data-rule tests check consistency, not real-world holdings. Do not treat generated narratives or duplicate proposals as verified evidence. |
| LLM08 — Hidden context | No system prompt or hidden model context in the application. External assistants must keep credentials and privileged instructions out of retrieved content. |
| LLM09 — Retrieval stores | No embeddings/vector store or retrieval permission system found. Not applicable to the current app. |
| LLM10 — Output sinks | Treat generated output as untrusted catalog data: validate shapes/URLs, escape HTML and CSV, and forbid extra mutation fields. Regression tests include instruction-like text and script markup. |

The prompt-injection test demonstrates that instruction-like text remains escaped
content in the application. It does **not** demonstrate that an LLM cannot be
persuaded by that text. No regex filter can supply that guarantee. Research
agents should use read-only access while gathering evidence, produce reviewable
plans, and apply only authorized changes through the bounded interfaces. Never
execute commands or follow credential/permission requests embedded in a source.

## Cross-check of prior work

Git history was used to identify earlier feature promises and compare them with
the current implementation and tests. This does not attribute every commit to
Codex or prove that every historical production data edit was correct.

| Earlier work | Cross-check and result |
| --- | --- |
| `699cdf6` site merge preservation | Existing field preservation was insufficient for related records and partial failures. Replaced with transactional merges; tests cover history, facts, notes, assignments, zero coordinates, stale plans, and conflict rollback. |
| `08de200`, `1110c87` type aliases/library | Existing alias/scope/data checks pass; found and fixed the publication-filter bypass. |
| Construction-number/operator/variant cleanup | Found stale import-filter and export assumptions; fixed those and strengthened merge-candidate checks. Historical country/name decisions still require source adjudication. |
| Globe draw-call and marker changes | Browser tests still expected sprites after the renderer moved to `THREE.Points`. Updated assertions to actual point geometry, stable size, zoom, selection, and reset. |
| Mobile/detail-page changes | Browser tests expected an obsolete detail modal. Updated navigation assertions and checked visible collections, narrow layouts, login/edit/save, sorting, filters, and gestures. |
| Pagination/list work | Browser coverage verifies 101-record admin lists and pickers, quoted edit values, and coordinate-free search results. |
| Exploration/routing/history | Browser coverage passes for draft history privacy, publishing, maps, itineraries, directions, saved trips, and stop limits. Provider error handling and restricted-site selection were strengthened. |
| Previous security audit | Existing auth/scope/key/CSRF regressions rerun. The test fixture held Flask's login cache across requests; fixed its lifecycle so separate test clients no longer inherit another client's cached identity. |
| Manufacturer/variant apply scripts | Added common field validation and nonzero exits on failures/conflicts. Their existing explicit `--dry-run` contract is retained; they do not share the new preview-by-default contract. |
| Deployment/migration documentation | Corrected migration coverage and the claim of atomic MySQL DDL. Existing migrations are not automatically applied by this review. |

The two access tests formerly skipped when geocoding was unavailable now seed a
local postal-code fixture. They exercise the behavior deterministically without
a network lookup.

## Reuse and redundancy

Implemented small shared components where duplicated logic caused divergence:

- `validation.py`: URL safety, ORM text limits, and alias shape/size checks.
- `catalog_identity.py`: designation formatting, construction placeholders, and
  identity keys shared by server/model/filter code.
- `merging.py`: relation-preserving transactions shared by HTTP and local dedupe.
- `scripts/patch_plans.py`: replaces three near-identical hardcoded apply loops
  and supplies field validation to manufacturer/variant tools.
- `scripts/csv_safety.py`: shared spreadsheet output protection.
- Shared API-key options and catalog-validation decorators in `app.py`.

Further restructuring should be separate, behavior-preserving work: move route
families into blueprints and make `create_app()` register them; centralize
repeated desktop/mobile escape, enum, and form behavior; consolidate legacy
script HTTP clients and snapshot paths. A wholesale rewrite during security
fixes would make regression review harder.

## Validation evidence

Validation used Python 3.14 in an isolated temporary environment and SQLite
fixtures. Browser checks used local fixture data and installed Chrome.

- Baseline: 87,815 passed, two skipped. The count is dominated by parametrized
  data checks; it is not 87,815 independent security scenarios.
- Full pytest run: **87,868 passed, zero skipped**, 301 warnings, in 50.50 seconds.
  Warnings include existing SQLAlchemy legacy API usage. A subsequent remote
  merge integration check exposed an expected-collection ID mismatch after
  aircraft links were preserved; corrected it and reran all eight merge tests,
  which passed. That check also rejects plan IDs containing path fragments
  before any request is made.
- All four browser suites passed: `exploration.cjs`, `mobile_views.cjs`,
  `globe_markers.cjs`, and `catalog_lists.cjs`.
- `pip-audit` after upgrades: no known vulnerabilities in the audited resolved
  runtime/production requirements. This is an advisory lookup, not proof of
  dependency safety.
- `pip check`, shell syntax checks, and `git diff --check` passed.
- Bandit: 15 remaining findings, none high severity. These comprise the guarded
  development secret marker; fixed/operator-selected URL fetches; a localhost
  alias string mistaken for a bind; nonsecurity sampling randomness; and two
  exception-handling patterns. The legacy retry script's broad catch should be
  replaced during client consolidation. These findings were not blanket-suppressed.

New focused coverage is in `tests/test_review_regressions.py` and
`tests/test_safe_merges.py`. Browser assertions were corrected to current
behavior; those changes should be reviewed alongside the feature code rather
than interpreted as a newly discovered UI failure.

## Remaining work and deployment notes

1. **Production configuration:** install the updated production requirements,
   use a strong secret, keep debug off, terminate HTTPS at a trusted proxy, and
   configure shared rate-limit storage plus its driver. The in-memory default
   cannot enforce a global multi-worker quota. Apply provider billing limits,
   log retention, and alerts. Actual deployment settings were not available.
2. **MySQL integration:** run migrations and integration/concurrency tests against
   supported MySQL/MariaDB before deployment. SQLite does not establish row-lock,
   collation, nullable uniqueness, or DDL behavior. Check for historical
   duplicates before applying unique constraints; do not silently delete them.
3. **Compatibility:** deploying the new cookie identity logs out old sessions.
   Logout clients must POST with CSRF. Deploy merge endpoints before their CLI;
   merge clients must handle 409 and refresh partially applied plans. CSV exports
   now escape potentially active cells; use JSON or explicit raw CSV for lossless
   machine workflows. Exports are not relational database backups.
4. **Catalog scale:** add versioned pagination to remaining complete-list APIs,
   query budgets, and load tests without breaking existing CLI consumers. API
   rate limiting bounds frequency, not the cost of one full-catalog query.
5. **Supply chain/browser policy:** add reproducible transitive dependency locks,
   recurring audits, and a staged CSP nonce migration. Current inline template
   scripts mean that simply removing `unsafe-inline` would break the UI.
6. **Research integrity:** re-snapshot and review stale plans before applying;
   alias writes replace arrays. Plan validation prevents extra fields, not false
   but well-formed data. Historical live holdings, previous merge outcomes, and
   source claims were not independently verified against museums or production.
7. **Maintenance debt:** retire or migrate older one-off scripts with historical
   workspace/host assumptions. The revised principal runners are safer, but this
   review does not make every legacy operator script preview-only.

No production migration, import, merge, credential rotation, commit, or deployment
was performed as part of this review.
