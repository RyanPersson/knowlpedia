import assert from 'node:assert/strict';
import { chromium } from 'playwright';
const base = process.env.PREVIEW_URL || 'http://127.0.0.1:8012';
const browser = await chromium.launch({headless: true});
try {
  const page = await browser.newPage({viewport: {width: 1440, height: 960}});
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const data = await (await page.request.get(`${base}/indexes/dependencies.json`)).json();
  const published = data.nodes.filter(node => node.visibility === 'production');
  const catalog = published.filter(node => node.content_source === 'conjectures-catalog');
  assert.ok(catalog.length, 'Run against the composed development preview');
  const organizationalKinds = new Set(['Page', 'Document', 'Section', 'Index']);
  const content = published.filter(node => !organizationalKinds.has(node.kind));
  const defaultCount = content.filter(node => node.content_source !== 'conjectures-catalog').length;
  const count = () => page.locator('#graph-status').textContent();
  const waitCount = n => page.waitForFunction(expected =>
    document.querySelector('#graph-status').textContent.startsWith(`${expected.toLocaleString()} concepts ·`), n);
  await page.goto(`${base}/graph/?view=components`);
  await waitCount(defaultCount);
  assert.equal(await page.getByLabel('Show conjectures catalog').isChecked(), false);
  assert.equal(await page.getByLabel('Show organizational pages').isChecked(), false);
  // Both filters work independently and recompute counts from the remaining nodes.
  for (const [showCatalog, showOrganizational] of [[false,true], [true,true], [true,false], [false,false]]) {
    await page.getByLabel('Show conjectures catalog').setChecked(showCatalog);
    await page.getByLabel('Show organizational pages').setChecked(showOrganizational);
    const expected = published.filter(node => (showCatalog || node.content_source !== 'conjectures-catalog') &&
      (showOrganizational || !organizationalKinds.has(node.kind))).length;
    await waitCount(expected);
    await page.reload();
    await waitCount(expected);
    assert.equal(await page.getByLabel('Show organizational pages').isChecked(), showOrganizational);
  }
  const hiddenCount = await count();
  await page.getByLabel('Show conjectures catalog').check();
  await waitCount(content.length);
  assert.equal(new URL(page.url()).searchParams.get('catalog'), 'show');
  await page.reload();
  await waitCount(content.length);
  assert.equal(await page.getByLabel('Show conjectures catalog').isChecked(), true);
  await page.getByLabel('Show conjectures catalog').uncheck();
  await waitCount(defaultCount);
  assert.equal(await count(), hiddenCount);
  await page.goBack();
  await waitCount(content.length);
  await page.goForward();
  await waitCount(defaultCount);
  // An old deep link into a hidden catalog component must fall back safely.
  await page.goto(`${base}/graph/?view=components&focus=${encodeURIComponent(catalog[0].id)}&cluster=${encodeURIComponent(catalog[0].id)}`);
  await waitCount(defaultCount);
  assert.equal(await page.locator('#graph-status.error').count(), 0);
  await page.locator('.graph-cluster-card').first().click();
  await page.locator('.map-node.current').waitFor();
  const ids = await page.locator('.map-node').evaluateAll(nodes => nodes.map(node => node.dataset.nodeId));
  assert.ok(ids.every(id => !catalog.some(node => node.id === id)));
  assert.ok(ids.every(id => !organizationalKinds.has(published.find(node => node.id === id).kind)));
  await page.getByRole('button', {name: 'All clusters'}).click();
  await page.setViewportSize({width: 390, height: 844});
  await page.screenshot({path: 'tmp/catalog-toggle-mobile.png', fullPage: true});
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
  await page.locator('#graph-view').selectOption('subjects');
  await waitCount(published.length);
  assert.equal(await page.getByLabel('Show organizational pages').isVisible(), false);
  assert.equal(await page.getByLabel('Show conjectures catalog').isVisible(), false);
  assert.deepEqual(errors, []);
  console.log(`Component filters passed: ${defaultCount} mathematical Knowlpedia entries; ${catalog.length} catalog entries toggled, with reload/history/deep-link/mobile checks.`);
} finally { await browser.close(); }
