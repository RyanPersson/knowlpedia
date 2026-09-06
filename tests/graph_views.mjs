import { chromium } from 'playwright';
import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';

const base = process.env.PREVIEW_URL || 'http://127.0.0.1:8016';
const screenshots = path.resolve(process.env.SCREENSHOT_DIR || 'tmp/graph-screenshots');
await mkdir(screenshots, {recursive:true});
const browser = await chromium.launch({headless:true, executablePath:process.env.PLAYWRIGHT_CHROME_PATH || undefined});
const errors = [];
async function ready(page) {
  await page.locator('.map-node.current').waitFor();
  await page.waitForFunction(() => document.querySelector('#graph-status').textContent.includes('Showing'));
}
async function forwardEdges(page) {
  const wrong = await page.evaluate(() => {
    const vertical = document.querySelector('[data-dependency-graph]').dataset.graphLayout === 'vertical';
    const positions = new Map([...document.querySelectorAll('.map-node')].map(n => {
      const b=n.getBoundingClientRect();return [n.dataset.nodeId,{x:b.x+b.width/2,y:b.y+b.height/2}];
    }));
    return [...document.querySelectorAll('.map-edge')].filter(e => {
      const a=positions.get(e.dataset.edgeSource),b=positions.get(e.dataset.edgeTarget);
      return vertical ? a.y <= b.y : a.x >= b.x;
    }).map(e => [e.dataset.edgeSource,e.dataset.edgeTarget]);
  });
  assert.deepEqual(wrong, [], 'Every rendered prerequisite edge must advance in the chosen direction');
}
async function screenshot(page,name) {await page.screenshot({path:path.join(screenshots,`${name}.png`)});}
try {
  const page = await browser.newPage({viewport:{width:1440,height:960}});
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(`${base}/graph/`);await ready(page);await forwardEdges(page);
  await screenshot(page,'desktop-neighborhood');
  const initialBox = await page.locator('#dependency-map').getAttribute('viewBox');
  await page.locator('#dependency-map').focus();await page.keyboard.press('ArrowRight');
  assert.notEqual(await page.locator('#dependency-map').getAttribute('viewBox'),initialBox);
  await page.keyboard.press('Home');
  assert.equal(await page.locator('#dependency-map').getAttribute('viewBox'),initialBox);
  // Every depth respects DAG order, even when a shorter path skips levels.
  for(const depth of ['2','3','1']) {
    await page.locator('#graph-depth').selectOption(depth);await forwardEdges(page);
    assert.equal(new URL(page.url()).searchParams.get('depth'),depth);
  }
  const beforeZoom = await page.locator('#dependency-map').getAttribute('viewBox');
  await page.getByRole('button',{name:'Zoom in',exact:true}).click();
  assert.notEqual(await page.locator('#dependency-map').getAttribute('viewBox'),beforeZoom);
  await page.getByRole('button',{name:'Fit',exact:true}).click();
  assert.equal(await page.locator('#dependency-map').getAttribute('viewBox'),beforeZoom);
  await page.getByRole('button',{name:'Switch to vertical layout'}).click();
  await forwardEdges(page);await screenshot(page,'desktop-vertical');
  await page.getByRole('button',{name:'Switch to horizontal layout'}).click();

  for (const mode of ['subjects','components']) {
    await page.locator('#graph-view').selectOption(mode);
    await page.locator('.graph-cluster-card').first().waitFor();
    assert.equal(await page.locator('#dependency-map').isVisible(),false);
    assert.equal(await page.locator('#graph-fit').isDisabled(),true);
    await screenshot(page,mode);
    const card = mode === 'subjects' ? page.locator('.graph-cluster-card').filter({hasText:'linear algebra'}) : page.locator('.graph-cluster-card').first();
    await card.click();await ready(page);await forwardEdges(page);
    assert.ok(new URL(page.url()).searchParams.get('cluster'));
    await screenshot(page,`${mode}-detail`);
    const selected = await page.locator('.map-node.current').getAttribute('data-node-id');
    await page.reload();await ready(page);
    assert.equal(await page.locator('.map-node.current').getAttribute('data-node-id'),selected);
    await page.getByRole('button',{name:'All clusters'}).click();
    await page.locator('.graph-cluster-card').first().waitFor();
    await page.goBack();await ready(page);
    await page.goForward();await page.locator('.graph-cluster-card').first().waitFor();
  }
  await page.locator('#graph-view').selectOption('neighborhood');await ready(page);
  await page.getByLabel('Find a concept').fill('no-such-concept-98652');
  await page.getByText('No concepts found. Try another name.').waitFor();
  await page.getByLabel('Find a concept').fill('Hilbert space');
  await page.getByLabel('Find a concept').press('ArrowDown');
  assert.equal(await page.locator('#graph-search-results button').first().evaluate(n => n === document.activeElement),true);
  await page.keyboard.press('Enter');await ready(page);
  assert.equal(await page.locator('#graph-viewer-title').textContent(),'Hilbert space');

  // A late fragment response must not replace the currently selected knowl.
  let release, markStarted, markFinished;
  const gate = new Promise(resolve => {release=resolve;});
  const started = new Promise(resolve => {markStarted=resolve;});
  const finished = new Promise(resolve => {markFinished=resolve;});
  await page.route('**/fragments/linear-algebra/vector-space/core.html', async route => {
    markStarted();await gate;
    await route.fulfill({contentType:'text/html',body:'<div class="knowl-content">STALE_VECTOR_FRAGMENT</div>'});
    markFinished();
  });
  await page.getByLabel('Find a concept').fill('Vector space');
  await page.getByLabel('Find a concept').press('Enter');await started;
  await page.getByLabel('Find a concept').fill('Hilbert space');
  await page.getByLabel('Find a concept').press('Enter');
  await page.locator('#graph-viewer-content .knowl-content').waitFor();
  release();await finished;
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  assert.doesNotMatch(await page.locator('#graph-viewer-content').textContent(),/STALE_VECTOR_FRAGMENT/);
  await page.getByRole('button',{name:'Use dark theme'}).click();
  await screenshot(page,'dark-neighborhood');
  await page.getByRole('button',{name:'Use light theme'}).click();

  // Returning to a URL with no focus/layout must restore the initial defaults.
  const historyPage=await browser.newPage();
  await historyPage.goto(`${base}/graph/`);await ready(historyPage);
  const initial = await historyPage.locator('.map-node.current').getAttribute('data-node-id');
  await historyPage.locator('.map-node:not(.current)').first().click();
  await historyPage.goBack();await ready(historyPage);
  assert.equal(await historyPage.locator('.map-node.current').getAttribute('data-node-id'),initial);
  await historyPage.close();

  for(const width of [390,720,768]) {
    const mobile=await browser.newPage({viewport:{width,height:844}});
    mobile.on('pageerror',e=>errors.push(e.message));
    await mobile.goto(`${base}/graph/`);await ready(mobile);await forwardEdges(mobile);
    assert.equal(await mobile.evaluate(()=>document.documentElement.scrollWidth <= innerWidth),true,'No page-level horizontal overflow');
    await screenshot(mobile,`responsive-${width}`);
    if(width===390) {
      const visibleLabelSize = await mobile.locator('.map-node text').first().evaluate(n => parseFloat(getComputedStyle(n).fontSize) * n.getScreenCTM().a);
      assert.ok(visibleLabelSize >= 11.5, `Mobile labels too small: ${visibleLabelSize}`);
      await mobile.locator('.map-node.current').click();
      await mobile.locator('#graph-viewer.open').waitFor();
      await screenshot(mobile,'mobile-viewer');
      await mobile.getByRole('button',{name:'Close knowl viewer'}).click();
      assert.equal(await mobile.locator('#graph-viewer').evaluate(n=>n.inert),true);
      await mobile.locator('#graph-view').selectOption('subjects');
      await mobile.locator('.graph-cluster-card').first().waitFor();await screenshot(mobile,'mobile-subjects');
    }
    await mobile.close();
  }
  // Reject cyclic and empty indices visibly, including self edges.
  for (const [name,data] of [
    ['cycle',{nodes:[{id:'a',title:'A',visibility:'production',href:'/a/'}],edges:[{source:'a',target:'a'}]}],
    ['empty',{nodes:[],edges:[]}],
  ]) {
    const errorPage=await browser.newPage();
    await errorPage.route('**/indexes/dependencies.json',route=>route.fulfill({json:data}));
    await errorPage.goto(`${base}/graph/`);
    await errorPage.locator('#graph-status.error').waitFor();
    assert.equal(await errorPage.locator('.map-node').count(),0);
    assert.match(await errorPage.locator('#graph-status').textContent(), name==='cycle'? /cycle/:/No published/);
    await errorPage.close();
  }
  assert.deepEqual(errors,[],'No browser runtime errors');
  console.log(`Graph views passed: DAG direction, all depths, clusters, URL history, zoom, keyboard search, responsive views, empty/cyclic errors. Screenshots: ${screenshots}`);
} finally { await browser.close(); }
