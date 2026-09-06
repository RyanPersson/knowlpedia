import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from 'playwright';
const base=process.env.PREVIEW_URL || 'http://127.0.0.1:8012';
const browser=await chromium.launch({headless:true});
try {
 const page=await browser.newPage();
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await mkdir('tmp/feedback-ui',{recursive:true});
 for(const width of [320,390,1440]) {
  await page.setViewportSize({width,height:900});
  await page.goto(base+'/linear-algebra/vector-space/');
  await page.getByRole('button',{name:'Ask Codex about Vector space',exact:true}).click();
  const dialog=page.getByRole('dialog',{name:'Message Codex'});
  assert.ok(await dialog.isVisible());
  assert.equal(await dialog.evaluate(d=>d.scrollWidth>d.clientWidth),false,'Dialog should fit mobile width');
  await page.screenshot({path:`tmp/feedback-ui/dialog-${width}.png`});
  await dialog.getByRole('button',{name:'Close Codex feedback'}).click();
 }
 let release;
 const received=new Promise(resolve=>{release=resolve});
 let heldRoute;
 await page.route('**/__knowlpedia/codex',route=>{heldRoute=route;release()});
 let polls=0;
 await page.route('**/__knowlpedia/codex/late',async route=>{
  polls++;await route.fulfill({json:{status:'completed',response:'Stale vector-space response'}});
 });
 await page.getByRole('button',{name:'Ask Codex about Vector space',exact:true}).click();
 const dialog=page.getByRole('dialog',{name:'Message Codex'});
 await dialog.getByLabel('Your message').fill('Delayed test');
 await dialog.getByLabel('Access key').fill('test-key');
 await dialog.getByRole('button',{name:'Send to Codex'}).click();await received;
 await dialog.getByRole('button',{name:'Close Codex feedback'}).click();
 await page.locator('.core-section a.knowl').filter({hasText:'field'}).first().click();
 await page.getByRole('button',{name:'Ask Codex about Field',exact:true}).click();
 await heldRoute.fulfill({status:202,json:{jobId:'late'}});
 await page.waitForTimeout(200);
 assert.match(await dialog.locator('[data-feedback-context]').textContent(),/algebra-rings\/field/);
 assert.equal(await dialog.locator('[data-feedback-response]').isVisible(),false);
 assert.equal(polls,0,'A response for a closed dialog must not be polled into another knowl');
 assert.deepEqual(errors,[]);
 console.log('Feedback dialog passed at 320/390/1440px; late replies cannot leak into another knowl.');
} finally {await browser.close()}
