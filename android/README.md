# Aircraft Finder for Android

An offline Android companion to the public website. The app uses the website's
mobile CSS, icons, typography, and Three.js globe in a bundled WebView. Kotlin
owns the Room database, Android location permissions, saved trips, and WorkManager
updates. The Android source belongs in this public repository; signing keys,
credentials, `local.properties`, and build outputs do not.

## Features

- Aircraft/museum search, sorting, museum country filtering, detail pages, type
  descriptions, published histories and facts from the local catalog.
- Offline museum globe using the website's bundled country/state boundaries.
- Near Me using device location or entered coordinates; restricted museums are
  excluded by default and can be explicitly included.
- Offline trip planning for specific airframes or any variant of a model,
  up to 12 targets and eight museum stops. Uses the website's coverage-first,
  nearest-neighbor rules and straight-line distance estimates.
- Named itineraries persist independently of catalog replacement and can be
  reopened without making a server request. Older itineraries are labeled.
- Automatic refresh on foreground entry and approximately every 12 hours in
  the background, subject to Android scheduling/network constraints. Manual
  refresh is available in Data & updates. Failed downloads retain local data.
- Online catalog editing opens the existing authenticated website in the user's
  browser. There are no embedded credentials and no queued offline writes.

Street maps, address/postal-code geocoding, and new road directions require an
online service. The app's offline route sketch is explicitly not a road map.
It does not bulk-download public OpenStreetMap tiles. GPS can work without
connectivity, but availability and time to first fix depend on the device.

## Build and run

Open this `android/` directory as a project in Android Studio. The checked-in
Gradle wrapper uses Gradle 9.6.0 and Android Gradle Plugin 9.4.1. Install Android
SDK platform 37; the app targets 36 and supports Android 8/API 26 onward. Use a
compatible JDK (the installed Studio JDK 25 was used for development).

```sh
cd android
./gradlew :app:assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am start -n org.airplanemuseum.finder.debug/org.airplanemuseum.finder.MainActivity
```

`ANDROID_HOME` or an untracked `local.properties` must identify the SDK. On the
development Mac, the SDK is `/Users/zach/Library/Android/sdk`. Debug builds use
`org.airplanemuseum.finder.debug`; release builds use `org.airplanemuseum.finder`.
The package ID is provisional until the first store release.

Release builds are unsigned; configure signing outside source control. Before a
store release, complete a real-device/accessibility test pass, replace the
research seed with a production snapshot, and provide the app-store privacy and
data-safety information appropriate to the final distribution.

## Catalog provenance and production rollout

**The current bundled seed is historical repository research, not a reconciled
copy of the live website.** Its manifest and the app display this distinction.
It includes repository CSV aircraft/museums and seeded type descriptions. It
does not invent missing facts/history or infer ambiguous museum links. It may
include records that later live cleanup merged or corrected.

`scripts/build_android_seed.py` builds this development seed deterministically
from sorted source files (generation timestamp and resulting revision change).
It reports aircraft rows for which it could not resolve a museum unambiguously.
The seed has a separate catalog namespace so saved itineraries cannot silently
resolve its IDs against unrelated production IDs.

To prepare authoritative offline data, deploy the backend changes and run on the
server using its existing database configuration:

```sh
.venv/bin/flask --app app publish-offline-catalog
```

This reads all public catalog tables in one repeatable-read transaction on
MySQL/MariaDB. It excludes user accounts, API keys, private history/type drafts,
and inactive facts. Set `OFFLINE_CATALOG_DIR` to a writable persistent directory;
the default is `instance/offline-catalog/`. No database migration is required.

Run the publisher after catalog maintenance or from the server's scheduler.
Publication is explicit: HTTP clients never cause an expensive export. Each
snapshot is immutable, and the manifest is atomically replaced only after the
new snapshot is present. Keep old snapshots available for in-flight downloads;
retention cleanup is an operator task.

The server exposes:

- `GET /api/v1/offline/manifest`: schema, catalog namespace, generation time,
  revision, compressed/uncompressed sizes, entity counts, and download path.
- `GET /api/v1/offline/snapshots/<sha256>.json.gz`: immutable, public-only data.

Until deployed and published, the existing website may return 404/503. The app
reports that state and keeps the bundled catalog. No production deployment or
publication is performed by building the Android project.

Before releasing, copy the published directory locally and replace the seed:

```sh
.venv/bin/python scripts/bundle_android_catalog.py /path/to/published-offline-catalog
```

The app verifies checksum, byte counts, schema, uniqueness, public flags, and
references before applying a replacement in one Room transaction. Deleted server
records disappear during replacement; saved itineraries retain their own data.
The v1 format limits downloads to 16 MiB compressed and 64 MiB uncompressed.
Checksums detect corruption; HTTPS authenticates the server. This is a full
snapshot protocol, not a timestamp-based incremental feed.

## Tests

Backend publication, privacy, deletion, ETag, and type-resolution checks:

```sh
python -m pytest tests/test_offline_catalog.py tests/test_android_planner.py
```

The planner parity checks need Node on PATH, or `NODE_BINARY` set to its path.
Android instrumentation tests run on a connected emulator/device:

```sh
cd android
./gradlew :app:connectedDebugAndroidTest
```

The local sync fixture uses SQLite and temporary files; it never accesses the
production database:

```sh
python tests/browser/serve_android_fixture.py
cd android
./gradlew -PcatalogBaseUrl=http://10.0.2.2:5058 :app:assembleDebug
```

Only debug builds permit cleartext to that exact emulator fixture host. Release
builds always use `https://airplane.museum`, regardless of that Gradle property.
The fixture is intended only for local tests; it includes a mutation route for
testing catalog deletion propagation.

The WebView smoke driver uses Playwright's Android support with a running debug
app on `emulator-5554` (override with `ANDROID_SERIAL`). Run from the repository
root with Playwright available to Node:

```sh
node tests/browser/android_offline.cjs seed
# Force-stop and reopen the app, keeping airplane mode enabled:
node tests/browser/android_offline.cjs resume
# Restore connectivity; this phase grants location permission on the emulator
# and injects test GPS coordinates. ADB must be on PATH or set in ADB:
node tests/browser/android_offline.cjs location
```

For update testing, install the fixture-configured build without clearing its
data, start the fixture server, and run the `sync` phase. POST to
`http://127.0.0.1:5058/__test__/delete-aircraft`, then run `deleted`. These phases
verify replacement/deletion, inert HTML-like catalog content, and preservation
of the trip created by `seed`. Restore the default production-URL build after
testing. Screenshots are written under the ignored `android/build/review/`.

### Development validation (2026-11-04)

- Full Python suite: 87,877 passed; focused export/planner parity checks: 7 passed.
- Debug APK built; Android lint: zero errors, five warnings (tooling/style and
  the deliberate use of JavaScript in the bundled WebView).
- Four instrumented tests passed on the API 36 Pixel 8 emulator, including
  bundled snapshot validation, corruption rejection, atomic replacement, and
  independent saved-trip persistence.
- Emulator UI checks passed for airplane-mode cold start, search/details,
  saved trips across restart, globe, Near Me, GPS, Android back, reconnect sync,
  deletion propagation, and safe rendering of catalog text.

Physical-device, accessibility, and store-release validation remain outstanding.

## Security and maintenance boundaries

Bundled scripts run only at `https://appassets.androidplatform.net`. File/content
access and mixed content are disabled; the CSP rejects external scripts, frames,
and objects. The native message interface checks the exact origin and main frame
and exposes named operations rather than filesystem or SQL access. All external
websites open in the user's browser, outside the privileged WebView. Network
updates cannot supply executable app code or redirect downloads to another host.

Public catalog data is stored in app-private Room storage. No account database,
administrator token, or signing secret is bundled. Location is requested only
when the user chooses it; opening external directions intentionally sends that
destination to the selected service. App backups are disabled in this first
version, so uninstalling the app removes saved trips.

The shared website assets are copied by `prepareSharedAssets` at build time;
edit their originals under `static/`. Android-only rendering and planner logic
live in `app/src/main/assets/`. Changes to selection/identity/access rules should
add parity cases against the Flask implementation. See `THIRD_PARTY.md` for
bundled asset licenses.
