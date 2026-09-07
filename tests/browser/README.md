# Mobile and desktop browser checks

These checks use an isolated SQLite database and a temporary Chrome profile.
They exercise museum and aircraft searches, sorting, public collection visibility,
repeated Near Me searches, globe gestures, narrow layouts, desktop detail links,
and mobile management login and museum editing with CSRF enabled.

Install the application's Python requirements and a Node.js Playwright package.
Google Chrome must be installed (`channel: 'chrome'`). For a temporary Node install:

```sh
npm install --prefix /tmp/airplanefinder-browser-tests playwright
```

Start the fixture server from the repository root:

```sh
.venv/bin/python tests/browser/serve_fixture.py
```

Then run the browser checks in another terminal:

```sh
NODE_PATH=/tmp/airplanefinder-browser-tests/node_modules node tests/browser/mobile_views.cjs
NODE_PATH=/tmp/airplanefinder-browser-tests/node_modules node tests/browser/globe_markers.cjs
NODE_PATH=/tmp/airplanefinder-browser-tests/node_modules node tests/browser/catalog_lists.cjs
```

The globe check verifies steady marker size at overview and close zoom, button/wheel/pinch zoom limits, and selection on both mobile and desktop.

The catalog check verifies admin lists and pickers beyond 100 records, quoted names in edit fields, and home search results when all matching museums lack coordinates. Its larger read responses are intercepted without changing the fixture database.

Stop the fixture server when finished. Its data is discarded on exit.
Screenshots are written to `/private/tmp/airplanefinder-*.png`.
The server binds only to `127.0.0.1:5057` and never uses the configured database.
Public CDN access is required, as it is for the app's jQuery, Three.js, and maps.
