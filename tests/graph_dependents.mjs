import {chromium} from 'playwright';
import assert from 'node:assert/strict';
const base=process.env.PREVIEW_URL || 'http://127.0.0.1:8012';
const browser=await chromium.launch({headless:true});
try {
 const page=await browser.newPage();
 const ids=['before2','before','center','after','after2'];
 const graph={nodes:ids.map(id=>({id,title:id,visibility:'production',kind:'Definition',href:`/${id}/`,fragment:`/fragments/${id}/core.html`,domains:[],dependency_review_count:1})),edges:ids.slice(1).map((id,i)=>({source:ids[i],target:id,reviewed:true}))};
 await page.route('**/indexes/dependencies.json',r=>r.fulfill({json:graph}));
 const visible=()=>page.locator('.map-node').evaluateAll(ns=>ns.map(n=>n.dataset.nodeId).sort());
 const expectNodes=async expected=>{await page.waitForFunction(n=>document.querySelectorAll('.map-node').length===n,expected.length);assert.deepEqual(await visible(),expected.sort());};
 await page.goto(`${base}/graph/?focus=center&depth=2`);
 await expectNodes(['before2','before','center']);
 const toggle=page.getByLabel('Show dependents',{exact:true});
 assert.equal(await toggle.isChecked(),false);
 await toggle.check();await expectNodes(ids);
 assert.equal(new URL(page.url()).searchParams.get('dependents'),'show');
 await page.reload();await expectNodes(ids);assert.equal(await toggle.isChecked(),true);
 await toggle.uncheck();await expectNodes(['before2','before','center']);
 await page.goBack();await expectNodes(ids);
 await page.locator('#graph-depth').selectOption('1');await expectNodes(['before','center','after']);
 await toggle.uncheck();await expectNodes(['before','center']);
 console.log('Prerequisite-only default, dependent traversal at two depths, reload and history passed.');
} finally {await browser.close();}
