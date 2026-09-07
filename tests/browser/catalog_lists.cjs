/* Run against serve_fixture.py. Read responses are intercepted to exercise
 * catalogs larger than one API page; the fixture database is never modified. */
const assert = require('node:assert/strict');
const {chromium, devices} = require('playwright');

(async () => {
    const browser = await chromium.launch({channel: 'chrome', headless: true});
    const base = process.env.TEST_BASE_URL || 'http://127.0.0.1:5057';
    const errors = [];
    try {
        const page = await browser.newPage();
        page.on('pageerror', error => errors.push(error.message));
        const quoted = 'Museum "Flight" & Friends\' Collection';
        const aircraft = (await (await page.request.get(base + '/api/v1/aircraft/1')).json()).aircraft;
        const museum = (await (await page.request.get(base + '/api/v1/museums/1')).json()).museum;
        for (const [kind, sample] of [['aircraft', aircraft], ['museums', museum]]) {
            const records = Array.from({length: 101}, (_, i) => ({...sample, id: i + 1,
                ...(kind === 'museums' ? {name: `Museum ${i + 1}`} : {model: `Plane ${i + 1}`, full_designation: `Plane ${i + 1}`})}));
            await page.route(`**/api/v1/${kind}/search?**`, route => {
                const params = new URL(route.request().url()).searchParams;
                const current = Number(params.get('page') || 1);
                const size = Math.min(Number(params.get('per_page') || 20), 100);
                return route.fulfill({json: {results: records.slice((current - 1) * size, current * size), total: records.length, page: current, pages: Math.ceil(records.length / size)}});
            });
            await page.route(`**/api/v1/${kind}/1`, async route => {
                const response = await route.fetch();
                const data = await response.json();
                if (kind === 'museums') data.museum.name = quoted;
                else data.aircraft.aircraft_name = quoted;
                await route.fulfill({response, json: data});
            });
        }
        await page.goto(base + '/admin/aircraft');
        await page.fill('[name="username"]', 'browser-admin');
        await page.fill('[name="password"]', 'browser-test-password');
        await page.click('button[type="submit"]');
        await page.waitForURL('**/admin/aircraft');
        await page.locator('.edit-aircraft-btn[data-id="101"]').waitFor();
        await page.locator('.edit-aircraft-btn[data-id="1"]').click();
        await page.click('#le-toggle-add');
        await page.locator('#le-add-museum option[value="101"]').waitFor({state:'attached'});
        assert.equal(await page.locator('#edit-form [name="aircraft_name"]').inputValue(), quoted);
        await page.goto(base + '/admin/museums');
        await page.locator('.edit-museum-btn[data-id="101"]').waitFor();
        await page.locator('.edit-museum-btn[data-id="1"]').click();
        await page.click('#le-toggle-add');
        await page.locator('#le-add-aircraft option[value="101"]').waitFor({state:'attached'});
        assert.equal(await page.locator('#edit-form [name="name"]').inputValue(), quoted);
        await Promise.all([
            page.waitForResponse(response => response.url().includes('/museums/search?') && response.url().includes('page=2')),
            page.goto(base + '/admin/aircraft/new'),
        ]);
        await page.fill('#museum-search-input', 'Museum 101');
        await page.locator('#museum-dropdown').getByText('Museum 101', {exact: false}).first().waitFor();
        await page.goto(base + '/admin/users');
        await page.locator('#user-museum-assign option[value="101"]').waitFor({state:'attached'});

        // Both home layouts must retain museums even when all distances are unknown.
        for (const mobile of [false, true]) {
            const context = await browser.newContext(mobile ? {...devices['iPhone 13']} : {});
            const home = await context.newPage();
            home.on('pageerror', error => errors.push(error.message));
            await home.route(/\/api\/(?:v1\/)?nearest\?/, route => route.fulfill({json: {
                origin: {location: 'Dayton'}, results: [], no_coordinates: [{museum: {...museum, name: quoted}, aircraft, display_status:'on_display'}]
            }}));
            await home.goto(base + '/');
            await home.fill('#prox-aircraft', 'C-130');
            await home.fill('#prox-location', 'Dayton');
            await home.click(mobile ? '#prox-go' : '#prox-search');
            await home.locator('#prox-results').getByText(quoted, {exact:true}).waitFor();
            assert.equal(await home.evaluate(() => escHtml(0)), '0');
            await context.close();
        }
        assert.deepEqual(errors, [], 'Browser JavaScript errors');
        console.log('PASS: 101-record admin lists and pickers, quoted edit fields, and coordinate-free home search results in desktop/mobile layouts.');
    } finally {
        await browser.close();
    }
})().catch(error => {console.error(error); process.exitCode = 1;});
