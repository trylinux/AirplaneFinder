/* Actual emulator WebView tests. Requires Playwright and a running debug app.
 * Phases: seed (airplane mode), resume, location, sync (local fixture), deleted.
 * See android/README.md. This driver does not alter connectivity itself.
 */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {_android} = require('playwright');

(async () => {
  const phase = process.argv[2] || 'seed';
  const output = process.env.ANDROID_TEST_OUTPUT || path.resolve('android/build/review');
  fs.mkdirSync(output, {recursive: true});
  const devices = await _android.devices();
  const device = devices.find(d => d.serial() === (process.env.ANDROID_SERIAL || 'emulator-5554'));
  assert(device, 'Expected emulator is not connected');
  try {
    const webview = await device.webView({pkg: 'org.airplanemuseum.finder.debug'});
    const page = await webview.page();
    page.setDefaultTimeout(30000);
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.waitForFunction(() => typeof catalog !== 'undefined' && catalog?.meta?.revision, null, {timeout: 90000});
    async function go(route) {
      await page.evaluate(route => { location.hash = route; }, route);
      await page.waitForFunction(route => location.hash === '#' + route, route);
    }
    if (phase === 'seed') {
      await go('/');
      await page.getByRole('heading', {name:'Dashboard',exact:true}).waitFor();
      assert((await page.evaluate(() => catalog.aircraft.length)) > 100);
      assert.equal(await page.evaluate(() => catalog.meta.catalog_id), 'airplane-repository-seed-v1');
      await page.screenshot({path:path.join(output,'home.png')});
      await go('/aircraft');
      await page.getByRole('heading',{name:'Aircraft',exact:true}).waitFor();
      await page.locator('#search-form input[name=q]').fill('C130');
      await page.locator('#search-form').evaluate(form=>form.requestSubmit());
      await page.waitForFunction(()=>route().searchParams.get('q')==='C130');
      await page.locator('.m-list-item').first().waitFor();
      assert((await page.locator('.m-list-item').count())>0);
      const target=await page.evaluate(()=>{
        const link=catalog.exhibits.find(e=>e.display_status==='on_display'&&
          model.museums.get(e.museum_id)?.country==='United States'&&
          model.museums.get(e.museum_id)?.access_type==='public'&&OfflineCatalog.located(model.museums.get(e.museum_id)));
        return {aircraft:link.aircraft_id,museum:link.museum_id};
      });
      await go('/aircraft/'+target.aircraft);
      await page.locator('[data-add]').click();
      await page.screenshot({path:path.join(output,'aircraft.png')});
      await go('/museums/'+target.museum);
      await page.locator('[data-start]').click();
      await page.locator('#trip-form button[type=submit]').click();
      await page.locator('#save-trip').waitFor();
      await page.locator('#save-trip input').fill('Offline smoke trip');
      await page.locator('#save-trip button').click();
      await page.getByRole('button',{name:/Offline smoke trip ·/}).waitFor();
      fs.writeFileSync(path.join(output,'trip.png'),await device.screenshot());
      await go('/near-me');
      await page.locator('#near-form button[type=submit]').click();
      await page.locator('#near-results .m-list-item').first().waitFor();
      assert.match(await page.locator('#near-results').innerText(), /0\.0 mi/);
      await go('/globe');
      await page.waitForFunction(()=>document.querySelector('#m-globe-loading').style.display==='none');
      await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
      fs.writeFileSync(path.join(output,'globe.png'),await device.screenshot());
      await go('/settings');
      await page.getByRole('heading',{name:'Offline data',exact:true}).waitFor();
      assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
      assert.deepEqual(errors,[]);
      console.log('PASS: airplane-mode catalog, search, details, trip creation/save, Near Me, globe, and narrow layout.');
    } else if(phase === 'location') {
      const {execFileSync}=require('node:child_process');
      const adb=process.env.ADB || 'adb';
      for(const permission of ['ACCESS_COARSE_LOCATION','ACCESS_FINE_LOCATION'])
        execFileSync(adb,['-s',device.serial(),'shell','pm','grant','org.airplanemuseum.finder.debug','android.permission.'+permission]);
      await go('/near-me');
      await page.locator('[data-location]').click();
      execFileSync(adb,['-s',device.serial(),'emu','geo','fix','-86.73806','33.56348']);
      await page.waitForFunction(()=>Math.abs(Number(document.querySelector('[name=latitude]').value)-33.56348)<.001);
      await go('/settings');
      await page.getByRole('heading',{name:'Offline data',exact:true}).waitFor();
      await device.shell('input keyevent 4');
      await page.getByRole('heading',{name:'Near Me',exact:true}).waitFor();
      fs.writeFileSync(path.join(output,'location-device.png'),await device.screenshot());
      console.log('PASS: native location updates and Android back navigation.');
    } else if(phase === 'resume') {
      await go('/trips');
      await page.getByRole('button',{name:/Offline smoke trip ·/}).click();
      await page.getByRole('heading',{name:'Offline smoke trip',exact:true}).waitFor();
      assert((await page.locator('#trip-result .stop').count())>0);
      console.log('PASS: saved itinerary survives process restart and opens offline.');
    } else {
      await go('/settings');
      await page.locator('[data-sync]').click();
      await page.waitForFunction(phase=>catalog.meta.catalog_id==='android-sync-fixture'&&
        catalog.aircraft.length===(phase==='deleted'?0:1),phase,{timeout:60000});
      await go('/trips');
      await page.getByRole('button',{name:/Offline smoke trip ·/}).click();
      await page.locator('#trip-result .sync-error').waitFor();
      if(phase==='sync'){
        await go('/aircraft/1');
        await page.getByRole('heading',{name:'X-1 · TEST-1',exact:true}).waitFor();
        assert.equal(await page.evaluate(()=>window.injected),undefined);
        assert.match(await page.locator('#content').innerText(),/<script>/);
        await go('/facts');
        await page.getByText('Local sync test fact.',{exact:true}).waitFor();
      }
      assert.deepEqual(errors,[]);
      console.log('PASS: '+phase+' snapshot applied; saved itinerary preserved and marked stale; safe content.');
    }
  } finally { await device.close(); }
})().catch(error=>{console.error(error);process.exit(1);});
