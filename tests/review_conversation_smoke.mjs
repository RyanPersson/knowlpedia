import assert from 'node:assert/strict';
import {chromium} from 'playwright';
const base=process.env.PREVIEW_URL || 'http://127.0.0.1:8012';
const browser=await chromium.launch({headless:true});
try {
 const context=await browser.newContext();
 // All model requests are intercepted: opening/testing the UI sends no model turn.
 let payload=null, sends=0;
 await context.addInitScript(()=>localStorage.setItem('knowl-codex-access-key','browser-test-only'));
 await context.route('**/__knowlpedia/conversation',r=>r.fulfill({json:{messages:[],active:false}}));
 await context.route('**/__knowlpedia/codex',async r=>{sends++;payload=r.request().postDataJSON();await r.fulfill({status:202,json:{jobId:'diff-test'}});});
 await context.route('**/__knowlpedia/codex/diff-test',r=>r.fulfill({json:{status:'completed'}}));
 const page=await context.newPage();
 await page.goto(base+'/review/dependency-structure/');
 const frame=page.frameLocator('#review-frame');
 await frame.locator('#message-diff').waitFor();
 const popupPromise=context.waitForEvent('page');
 await frame.getByRole('link',{name:'Message about this diff'}).click();
 const conversation=await popupPromise;
 await conversation.waitForLoadState();
 await conversation.waitForFunction(()=>document.getElementById('diff-description').textContent.includes('→'));
 assert.equal(sends,0);
 const url=new URL(conversation.url());
 assert.ok(url.searchParams.get('reviewHash').length===64);
 assert.equal(await conversation.locator('#knowl').inputValue(),url.searchParams.get('knowlId'));
 assert.equal(await conversation.locator('#knowl').getAttribute('readonly'),'');
 for(const width of [390,1440]) {
  await conversation.setViewportSize({width,height:1000});
  assert.equal(await conversation.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
  await conversation.screenshot({path:`tmp/review-conversation-${width}.png`});
 }
 await conversation.getByLabel('Your message').fill('Why was this hypothesis added?');
 await conversation.getByRole('button',{name:'Send to Codex',exact:true}).click();
 await conversation.waitForFunction(()=>document.getElementById('status').textContent==='Codex replied.');
 assert.equal(sends,1);
 assert.equal(payload.reviewContext,url.searchParams.get('reviewContext'));
 assert.equal(payload.reviewHash,url.searchParams.get('reviewHash'));
 const snapshot=await (await conversation.request.get(base+payload.reviewContext)).json();
 assert.equal(payload.knowlId,snapshot.comparison.knowl_id);
 assert.ok(snapshot.comparison.baseline_ref.length===40);
 assert.ok(snapshot.comparison.proposed_ref.length===40);
 assert.ok(snapshot.comparison.unified_diff.includes('@@'));
 await conversation.getByRole('button',{name:'Remove diff context'}).click();
 await conversation.getByLabel('Your message').fill('An unrelated question');
 await conversation.getByRole('button',{name:'Send to Codex',exact:true}).click();
 await conversation.waitForFunction(()=>document.getElementById('status').textContent==='Codex replied.');
 assert.equal(payload.reviewContext,undefined);
 assert.equal(payload.reviewHash,undefined);
 console.log('Review button opens conversation, attaches exact versions, sends only on submit, and removes context; desktop/mobile passed. No model turn submitted.');
} finally {await browser.close();}
