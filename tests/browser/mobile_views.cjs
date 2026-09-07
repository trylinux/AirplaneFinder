/* Start serve_fixture.py, then run with Node and Playwright installed:
 * NODE_PATH=/path/to/node_modules node tests/browser/mobile_views.cjs
 * Uses an isolated Chrome profile. No production data or account required.
 */
const assert = require('node:assert/strict');
const {chromium, devices} = require('playwright');

(async () => {
    const browser = await chromium.launch({channel: 'chrome', headless: true});
    const errors = [];
    try {
        const context = await browser.newContext({...devices['iPhone 13'], defaultBrowserType: undefined});
        const page = await context.newPage();
        page.setDefaultTimeout(15000);
        page.on('pageerror', error => errors.push(error.message));
        const base = process.env.TEST_BASE_URL || 'http://127.0.0.1:5057';
        async function visible(selector, text) {
            await page.locator(selector).filter({hasText: text}).first().waitFor({state: 'visible'});
        }
        async function noOverflow() {
            assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'Page overflows horizontally');
        }
        await page.goto(base + '/museums');
        await visible('#m-results', 'Alpha Aviation Museum');
        await page.selectOption('#m-sort', 'name');
        await page.selectOption('#m-sort-dir', 'desc');
        await page.waitForFunction(() => document.querySelector('#m-results .m-list-title')?.textContent.includes('Zulu'));
        await page.selectOption('#m-region', 'Europe');
        await visible('#m-results', 'Zulu Museum');
        assert.equal(await page.locator('#m-results .m-list-item').count(), 1);
        await page.selectOption('#m-region', '');
        await page.fill('#m-q', 'Alpha');
        await page.click('#m-go');
        await visible('#m-results', 'Alpha Aviation Museum');
        await page.click('#m-results .m-list-item');
        await visible('#m-detail-body', 'Hercules');
        await visible('#m-detail-body', 'Test Airframe');
        assert(!(await page.locator('#m-detail-body').innerText()).includes('B-17'), 'Stored aircraft leaked into public collection');
        await page.click('a[href="/aircraft/1"]');
        await visible('#m-detail-body', 'C-130');
        await page.click('a[href="/museums/1"]');
        await visible('#m-detail-body', 'Alpha Aviation Museum');
        await noOverflow();

        // Repeat the same search after expanding a collection: each new card must load.
        await page.goto(base + '/near-me');
        await page.fill('#loc-input', 'Dayton');
        for (let i = 0; i < 2; i++) {
            await page.click('#btn-search');
            await visible('.m-museum-head', 'Alpha Aviation Museum');
            await page.click('.m-museum-head');
            await visible('.m-aircraft-list', 'C-130');
        }
        await page.setViewportSize({width: 320, height: 700});
        await noOverflow();
        await page.screenshot({path: '/private/tmp/airplanefinder-near-me.png'});

        await page.goto(base + '/aircraft');
        await visible('#ac-results', 'C-130');
        await page.selectOption('#ac-sort', 'full_designation');
        await page.selectOption('#ac-sort-dir', 'desc');
        await page.waitForFunction(() => document.querySelector('#ac-results .m-list-title')?.textContent.includes('C-130'));
        await page.click('[data-q="B-17"]');
        await visible('#ac-results', 'B-17');
        assert.equal(await page.locator('#ac-results .m-list-item').count(), 1);
        await noOverflow();

        await page.goto(base + '/museums');
        await page.fill('#m-prox-location', 'Dayton');
        await page.selectOption('#m-prox-region', 'Europe');
        await page.click('#m-prox-go');
        await visible('#m-prox-results', 'Zulu Museum');
        await visible('#m-prox-results', 'distance unavailable');
        await page.waitForFunction(() => typeof THREE !== 'undefined');
        // Observe the actual rendered scene to locate a pin and measure gestures.
        await page.evaluate(() => {
            const Original = THREE.WebGLRenderer;
            THREE.WebGLRenderer = function(options) {
                const renderer = new Original(options);
                const render = renderer.render.bind(renderer);
                renderer.render = function(scene, camera) { window.testGlobe = {scene, camera}; render(scene, camera); };
                return renderer;
            };
        });
        await page.click('[data-view="globe"]');
        await page.locator('#m-globe-loading').waitFor({state: 'hidden'});
        await page.waitForFunction(() => window.testGlobe);
        await page.click('#m-globe-spin-toggle');
        await page.click('#m-globe-zoom-in');
        assert(await page.evaluate(() => testGlobe.camera.position.z < 3.2));
        await page.click('#m-globe-zoom-reset');
        assert.equal(await page.evaluate(() => testGlobe.camera.position.z), 3.2);
        const point = await page.evaluate(() => {
            let pin;
            testGlobe.scene.traverse(o => {if (o.userData.id === 1) pin = o;});
            const v = pin.getWorldPosition(new THREE.Vector3()).project(testGlobe.camera);
            const r = document.querySelector('#m-globe-canvas').getBoundingClientRect();
            return {x: r.left + (v.x + 1) * r.width / 2, y: r.top + (1 - v.y) * r.height / 2};
        });
        await page.touchscreen.tap(point.x, point.y);
        await visible('#m-globe-tooltip', 'Alpha Aviation Museum');
        await page.locator('#m-globe-tooltip a').click();
        await visible('#m-detail-body', 'Hercules');

        await page.goBack();
        await page.click('[data-view="globe"]');
        await page.locator('#m-globe-loading').waitFor({state: 'hidden'});
        const cdp = await context.newCDPSession(page);
        const rect = await page.locator('#m-globe-canvas').boundingBox();
        const cx = rect.x + rect.width / 2, cy = rect.y + rect.height / 2;
        await cdp.send('Input.dispatchTouchEvent', {type:'touchStart', touchPoints:[{x:cx-25,y:cy,id:0},{x:cx+25,y:cy,id:1}]});
        await cdp.send('Input.dispatchTouchEvent', {type:'touchMove', touchPoints:[{x:cx-55,y:cy,id:0},{x:cx+55,y:cy,id:1}]});
        await cdp.send('Input.dispatchTouchEvent', {type:'touchEnd', touchPoints:[]});
        assert.equal(await page.locator('#m-globe-tooltip.show').count(), 0, 'Pinch selected a museum');
        await cdp.send('Input.dispatchTouchEvent', {type:'touchStart', touchPoints:[{x:cx,y:cy,id:0}]});
        await cdp.send('Input.dispatchTouchEvent', {type:'touchMove', touchPoints:[{x:cx+60,y:cy+20,id:0}]});
        await cdp.send('Input.dispatchTouchEvent', {type:'touchEnd', touchPoints:[]});
        assert.equal(await page.locator('#m-globe-tooltip.show').count(), 0, 'Drag selected a museum');
        await page.click('[data-view="list"]');
        await page.setViewportSize({width: 700, height: 320});
        await page.click('[data-view="globe"]');
        await noOverflow();
        await page.screenshot({path:'/private/tmp/airplanefinder-globe.png'});

        await page.setViewportSize({width:320, height:700});
        await page.goto(base + '/admin/museums');
        await page.fill('[name="username"]', 'browser-admin');
        await page.fill('[name="password"]', 'browser-test-password');
        await page.click('button[type="submit"]');
        await page.waitForURL('**/admin/museums');
        await visible('#admin-museum-results', 'Alpha Aviation Museum');
        assert(await page.locator('.app-main').evaluate(el => el.clientWidth >= innerWidth - 2), 'Management content squeezed beside the topbar');
        await noOverflow();
        await page.locator('.edit-museum-btn[data-id="1"]').click();
        await page.locator('#edit-modal').waitFor({state:'visible'});
        await page.waitForFunction(() => getComputedStyle(document.querySelector('#edit-modal')).opacity === '1');
        await page.fill('#edit-form [name="address"]', '2 Museum Way');
        await page.screenshot({path:'/private/tmp/airplanefinder-mobile-edit.png'});
        assert(await page.locator('.modal-content').evaluate(el => el.scrollWidth <= el.clientWidth), 'Museum editor overflows horizontally');
        await page.click('#edit-form button[type="submit"]');
        await page.waitForFunction(() => document.querySelector('#edit-msg')?.textContent.includes('Saved'));
        assert.equal((await (await page.request.get(base + '/api/v1/museums/1')).json()).museum.address, '2 Museum Way');
        await page.goto(base + '/admin/museums/new');
        await visible('h2', 'Add New Museum');
        await noOverflow();

        const desktop = await browser.newPage({viewport:{width:1280,height:900}});
        desktop.on('pageerror', error => errors.push(error.message));
        await desktop.goto(base + '/museums/1');
        await desktop.locator('#museum-modal').waitFor({state:'visible'});
        assert((await desktop.locator('#museum-modal-body').innerText()).includes('Hercules'));
        await desktop.goto(base + '/aircraft/1');
        await desktop.locator('#aircraft-modal').waitFor({state:'visible'});
        await desktop.goto(base + '/museums');
        await desktop.click('[data-tab="tab-discovery"]');
        await desktop.locator('#globe-loading').waitFor({state:'hidden'});
        assert.deepEqual(errors, [], 'Browser JavaScript errors');
        console.log('PASS: mobile sorting, filtering, museum/aircraft links, visible collections, repeated Near Me searches, narrow layouts, globe touch gestures, orientation changes, mobile management login/edit/save, and desktop detail/globe views.');
    } finally {
        await browser.close();
    }
})().catch(error => {console.error(error); process.exitCode = 1;});
