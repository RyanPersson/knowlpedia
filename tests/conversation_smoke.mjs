import assert from 'node:assert/strict';
import {readFile, mkdir} from 'node:fs/promises';
import {chromium} from 'playwright';
const base=process.env.PREVIEW_URL || 'http://127.0.0.1:8012';
const token=(await readFile('.preview-server/codex-access-token','utf8')).trim();
const browser=await chromium.launch({headless:true});
try {
 const page=await browser.newPage();
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const unauthorized=await page.request.get(base+'/__knowlpedia/conversation');
 assert.equal(unauthorized.status(),401);
 await page.addInitScript(token=>localStorage.setItem('knowl-codex-access-key',token),token);
 await mkdir('tmp/conversation-ui',{recursive:true});
 for(const width of [320,390,1440]) {
  await page.setViewportSize({width,height:1000});
  await page.goto(base+'/conversation/');
  await page.waitForFunction(()=>document.getElementById('history').textContent.includes('poincare disk'));
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
  await page.screenshot({path:`tmp/conversation-ui/page-${width}.png`});
 }
 let payload;
 await page.route('**/__knowlpedia/codex',async route=>{
  payload=route.request().postDataJSON();
  await route.fulfill({status:202,json:{jobId:'conversation-test'}});
 });
 await page.route('**/__knowlpedia/codex/conversation-test',route=>route.fulfill({json:{status:'completed',response:'Test reply'}}));
 await page.getByLabel('Your message').fill('General conversation test');
 await page.getByRole('button',{name:'Send to Codex',exact:true}).click();
 await page.waitForFunction(()=>document.getElementById('status').textContent==='Codex replied.');
 assert.equal(payload.knowlId,''); assert.equal(payload.intent,'auto'); assert.equal(payload.conversation,true);
 assert.equal(await page.locator('#intent').count(),0);
 // Theme follows the shared preference and supports toggling.
 await page.evaluate(()=>localStorage.setItem('knowl-theme','dark'));
 await page.reload();
 assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 await page.getByRole('button',{name:'Use light theme'}).click();
 assert.equal(await page.evaluate(()=>localStorage.getItem('knowl-theme')),'light');
 assert.deepEqual(errors,[]);
 console.log('Conversation history, authentication, mobile layouts, direct send payload, automatic intent, and shared dark-mode preference passed.');
} finally {await browser.close();}
