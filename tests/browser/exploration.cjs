/* Uses serve_fixture.py and its local map tiles; never requests public OSM tiles. */
const assert = require('node:assert/strict');
const {chromium,devices} = require('playwright');
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const base=process.env.TEST_BASE_URL||'http://127.0.0.1:5057';
 const errors=[];let museumId=null,eventId=null,admin=null;
 try {
  const context=await browser.newContext({...devices['iPhone 13']});
  admin=await context.newPage();admin.on('pageerror',e=>errors.push(e.message));
  await admin.goto(base+'/admin/aircraft/1/history');
  await admin.fill('[name="username"]','browser-admin');await admin.fill('[name="password"]','browser-test-password');
  await admin.click('button[type="submit"]');await admin.waitForURL('**/admin/aircraft/1/history');
  await admin.fill('#history-form [name="title"]','A sourced "milestone" <test>');
  await admin.fill('#history-form [name="event_year"]','1980');
  await admin.fill('#history-form [name="source_name"]','Museum archive, page 12');
  await admin.check('#history-form [name="is_approximate"]');
  await admin.uncheck('#history-form [name="is_published"]');
  await admin.click('#history-form [type="submit"]');
  await admin.getByText('Milestone saved.',{exact:true}).waitFor();
  await admin.locator('#history-events').getByText('Draft · hidden from visitors').waitFor();
  eventId=(await (await admin.request.get(base+'/api/v1/aircraft/1/history/manage')).json())[0].id;
  const publicPage=await browser.newPage();publicPage.on('pageerror',e=>errors.push(e.message));
  await publicPage.goto(base+'/aircraft/1/history');
  await publicPage.getByText('No history has been recorded for this airframe yet.').waitFor();
  await admin.locator('#history-events').getByRole('button',{name:'Edit',exact:true}).click();
  await admin.check('#history-form [name="is_published"]');await admin.click('#history-form [type="submit"]');
  await admin.waitForFunction(()=>!document.querySelector('#history-events').textContent.includes('Draft ·'));
  await publicPage.reload();await publicPage.getByText('A sourced "milestone" <test>',{exact:true}).waitFor();
  await publicPage.getByText('Around 1980',{exact:true}).waitFor();
  assert.equal(await publicPage.locator('#history-events test').count(),0,'History text must not become HTML');
  await admin.screenshot({path:'/private/tmp/airplanefinder-history-mobile.png'});
  const created=await admin.evaluate(async()=>Explorer.api('/api/v1/museums',{method:'POST',body:JSON.stringify({name:'Trip Fixture Museum',city:'Test City',country:'United States',region:'North America',latitude:0,longitude:-89.8})}));museumId=created.id;
  await admin.evaluate(async id=>Explorer.api('/api/v1/exhibits',{method:'POST',body:JSON.stringify({museum_id:id,aircraft_id:2,display_status:'on_display'})}),museumId);
  await admin.goto(base+'/map');
  await admin.getByText('2 mapped museums. Pan or zoom, then choose “Search this area.”').waitFor();
  await admin.locator('#museum-map .leaflet-tile-loaded').first().waitFor();
  await admin.locator('#map-results').getByText('Trip Fixture Museum',{exact:true}).waitFor();
  await admin.locator('#map-unlocated').click();await admin.locator('#map-unlocated-list').getByText('Zulu Museum',{exact:false}).waitFor();
  const cluster=admin.locator('#museum-map .x-marker.cluster');
  // At overview both nearby museums collapse to a count rather than overlap.
  for(let i=0;i<5;i++){await admin.locator('#museum-map .leaflet-control-zoom-out').click();await admin.waitForTimeout(350);}
  await cluster.first().waitFor();await cluster.first().click();
  await admin.fill('#map-query','Trip Fixture');await admin.click('#map-search [type="submit"]');
  await admin.getByText('1 mapped museums. Pan or zoom, then choose “Search this area.”').waitFor();
  assert.equal(await admin.locator('#map-results .x-card').count(),1);
  await admin.click('#map-area');await admin.getByText('1 matching museums in the selected area.').waitFor();
  for(const width of [320,390,700]){await admin.setViewportSize({width,height:800});assert(await admin.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Map page overflow');}
  await admin.setViewportSize({width:390,height:844});await admin.screenshot({path:'/private/tmp/airplanefinder-map-mobile.png'});
  await admin.goto(base+'/trips?aircraft_id=1');await admin.locator('#trip-targets').getByText('C-130 · TEST-1',{exact:true}).waitFor();
  await admin.fill('#trip-search','B-17');await admin.click('#trip-search-form [type="submit"]');
  await admin.getByRole('button',{name:'Any B-17',exact:true}).click();
  await admin.fill('#trip-origin','Dayton');await admin.check('#trip-round');
  await admin.click('#trip-build');
  await admin.locator('#trip-summary').filter({hasText:'2 museum stops · 2/2 aircraft choices covered'}).waitFor();
  assert.equal(await admin.locator('#trip-stops article').count(),2);
  assert.deepEqual(await admin.locator('#trip-map .x-marker').allTextContents(),['1','2']);
  assert.equal(await admin.locator('#trip-map .x-marker').first().evaluate(e=>getComputedStyle(e).display),'flex');
  const directions=await admin.locator('#trip-directions a').getAttribute('href');
  assert.equal(new URL(directions).searchParams.get('destination'),'0,-90');
  await admin.fill('#trip-name','Museum weekend');await admin.click('#trip-save-form [type="submit"]');
  await admin.getByText('Saved on this device. Up to 10 named trips are kept.').waitFor();
  await admin.reload();await admin.getByRole('button',{name:'Museum weekend',exact:true}).click();
  await admin.locator('#trip-summary').filter({hasText:'2 museum stops · 2/2 aircraft choices covered'}).waitFor();
  await admin.screenshot({path:'/private/tmp/airplanefinder-trip-mobile.png',fullPage:true});
  await admin.selectOption('#trip-max-stops','1');assert(await admin.locator('#trip-result').isHidden());await admin.click('#trip-build');
  await admin.locator('#trip-unmatched').getByText('Still on your list',{exact:true}).waitFor();
  for(const width of [320,390,700]){await admin.setViewportSize({width,height:800});assert(await admin.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Trip page overflow');}
  await publicPage.goto(base+'/map');await publicPage.locator('#map-results .x-card').first().waitFor();
  await publicPage.screenshot({path:'/private/tmp/airplanefinder-map-desktop.png'});
  await publicPage.goto(base+'/trips?aircraft_id=1');await publicPage.locator('#trip-targets li').filter({hasText:'TEST-1'}).waitFor();
  await publicPage.fill('#trip-origin','Dayton');await publicPage.click('#trip-build');await publicPage.locator('#trip-result').waitFor({state:'visible'});
  await publicPage.screenshot({path:'/private/tmp/airplanefinder-trip-desktop.png',fullPage:true});
  assert.deepEqual(errors,[],'Browser JavaScript errors');
  console.log('PASS: mobile/desktop sourced histories, draft privacy, edit/publish, clustered map and filters, safe text, multi-aircraft itineraries, directions, stop limits, saved trip reloads, and narrow layouts.');
 } catch(error) {
  if(admin){console.error('Browser errors:',errors);console.error('Page:',admin.url());console.error(await admin.locator('body').innerText());await admin.screenshot({path:'/private/tmp/airplanefinder-exploration-failure.png',fullPage:true});}
  throw error;
 } finally {
  if(admin){
   await admin.goto(base+'/trips');
   for(const path of [eventId?`/api/v1/history/${eventId}`:null,museumId?`/api/v1/museums/${museumId}`:null].filter(Boolean)) {
    await admin.evaluate(async path=>Explorer.api(path,{method:'DELETE',body:'{}'}),path).catch(()=>{});
   }
  }
  await browser.close();
 }
})().catch(e=>{console.error(e);process.exitCode=1;});
