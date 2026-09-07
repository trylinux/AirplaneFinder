/* Run against serve_fixture.py with Playwright installed, like mobile_views.cjs. */
const assert = require('node:assert/strict');
const {chromium, devices} = require('playwright');

(async () => {
    const browser = await chromium.launch({channel:'chrome', headless:true});
    try {
        for (const mobile of [true, false]) {
            const context = await browser.newContext(mobile ? devices['iPhone 13'] : {viewport:{width:1280,height:900}});
            const page = await context.newPage();
            const errors = [];
            page.on('pageerror', error => errors.push(error.message));
            const base = process.env.TEST_BASE_URL || 'http://127.0.0.1:5057';
            const prefix = mobile ? 'm-' : '';
            // Center a compact group of museums under the globe's initial tilt.
            await page.route('**/api/v1/museums/globe', route => route.fulfill({json:
                Array.from({length:9}, (_, i) => ({id:i+1, name:'Museum ' + (i+1),
                    city:'Test City', country:'United States', latitude:0.25*180/Math.PI + Math.floor(i/3)*0.7,
                    longitude:-90+(i%3)*0.7, aircraft_count:1}))
            }));
            await page.goto(base + '/museums');
            await page.waitForFunction(() => typeof THREE !== 'undefined');
            await page.evaluate(() => {
                const Original = THREE.WebGLRenderer;
                THREE.WebGLRenderer = function(options) {
                    const renderer = new Original(options), render = renderer.render.bind(renderer);
                    renderer.render = function(scene,camera) {window.testGlobe={scene,camera}; render(scene,camera);};
                    return renderer;
                };
            });
            await page.click(mobile ? '[data-view="globe"]' : '[data-tab="tab-discovery"]');
            await page.locator('#' + prefix + 'globe-loading').waitFor({state:'hidden'});
            await page.click('#' + prefix + 'globe-spin-toggle');
            async function marker() {
                return page.evaluate(prefix => {
                    const {scene,camera}=testGlobe;
                    let pin;
                    scene.traverse(o => {if(o.userData.id===1) pin=o;});
                    const p = pin.getWorldPosition(new THREE.Vector3());
                    const a = p.clone().project(camera);
                    const b = p.clone().add(new THREE.Vector3(0,pin.scale.y,0)).project(camera);
                    const rect = document.querySelector('#'+prefix+'globe-canvas').getBoundingClientRect();
                    return {pixels:Math.abs(b.y-a.y)*rect.height/2, opacity:pin.material.opacity,
                        x:rect.left+(a.x+1)*rect.width/2, y:rect.top+(1-a.y)*rect.height/2,
                        z:camera.position.z, near:camera.near, sprite:pin.isSprite};
                }, prefix);
            }
            const initial=await marker();
            assert(initial.sprite);
            assert(Math.abs(initial.pixels-6)<0.1, 'Overview marker should be six CSS pixels');
            await page.evaluate(() => new Promise(resolve => {
                let frames=0; function step(){if(++frames===30) resolve(); else requestAnimationFrame(step);} step();
            }));
            assert(Math.abs((await marker()).pixels-initial.pixels)<0.1, 'Markers must not pulse');
            for(let i=0;i<22;i++) await page.click('#'+prefix+'globe-zoom-in');
            const close=await marker();
            assert(Math.abs(close.z-1.04)<0.0001, 'Buttons should reach the extended zoom limit');
            assert(close.near<close.z-1.004, 'Near plane must not clip close markers');
            assert(Math.abs(close.pixels-initial.pixels)<0.1, 'Close markers must not grow');
            await page.locator('#'+prefix+'globe-wrap').scrollIntoViewIfNeeded();
            await page.screenshot({path:'/private/tmp/airplanefinder-dots-'+(mobile?'mobile':'desktop')+'.png'});
            const tap=await marker();
            if(mobile) {
                // Tap slightly beside a six-pixel dot: retain a forgiving hit area.
                await page.touchscreen.tap(tap.x+7,tap.y+7);
                await page.locator('#m-globe-tooltip.show').waitFor({state:'visible'});
                assert((await page.locator('#m-globe-tooltip').innerText()).includes('Museum 1'));
            } else {
                await page.mouse.click(tap.x,tap.y);
                await page.locator('#museum-modal').waitFor({state:'visible'});
                await page.locator('#museum-modal .modal-close').click();
            }
            await page.click('#'+prefix+'globe-zoom-reset');
            assert.equal((await marker()).z,3.2);
            if(mobile) {
                const rect=await page.locator('#m-globe-canvas').boundingBox();
                const x=rect.x+rect.width/2, y=rect.y+rect.height/2;
                const cdp=await context.newCDPSession(page);
                await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:x-1,y,id:0},{x:x+1,y,id:1}]});
                await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:x-70,y,id:0},{x:x+70,y,id:1}]});
                await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
                await page.waitForFunction(()=>Math.abs(testGlobe.camera.position.z-1.04)<0.0001);
            } else {
                const rect=await page.locator('#globe-canvas').boundingBox();
                await page.mouse.move(rect.x+rect.width/2,rect.y+rect.height/2);
                await page.mouse.wheel(0,-5000);
                await page.waitForFunction(()=>Math.abs(testGlobe.camera.position.z-1.04)<0.0001);
            }
            assert.deepEqual(errors,[]);
            await context.close();
        }
        console.log('PASS: steady six-pixel markers, extended button/pinch/wheel zoom, close-range selection, and reset on mobile and desktop.');
    } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
