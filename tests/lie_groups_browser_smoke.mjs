import assert from "node:assert/strict";
import { chromium } from "playwright";
import { execFileSync } from "node:child_process";
import { readFileSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const artifacts = path.join(repo, "tmp/lie-groups-layouts");
mkdirSync(artifacts, { recursive: true });
const label = process.env.LAYOUT_LABEL || "actual";
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".svg": "image/svg+xml" };
const shell = execFileSync("python3", ["-c", `
import sys
sys.path.insert(0, 'packages/compiler')
from lie_groups_html import render_lie_groups_table
def shell(title, body, **kwargs):
    return '<!doctype html><html data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="/assets/knowl.css"><link rel="stylesheet" href="/assets/katex.min.css"><script defer src="/assets/lie-groups.js"></script></head><body>'+body+'</body></html>'
print(render_lie_groups_table(shell, None))
`], { cwd: repo, encoding: "utf8" });
const fixtureObject = (id, compact, complex, cell) => ({
  id, name: `Synthetic ${id}`, notation: `X_{${id}}`, family: "synthetic-family", status: "family", kind: "lie-group", knowl: `test/${id}`,
  parameters: { n: "n" }, dimensions: { real: "2n", ...(complex ? { complex: "n" } : {}) }, constraints: ["n >= 1"],
  category_ids: ["real-lie-groups", ...(complex ? ["complex-lie-groups"] : [])],
  properties: { ...(compact == null ? {} : { compact }), connected: true, lie_group: { section: "classical", form: complex ? "complex" : "real", parameter_summary: "Synthetic parameter n >= 1.", construction_summary: "A layout fixture; no mathematical classification is asserted.", global_form_summary: "The fixture records one specified group convention.", ...(cell ? { classification_cells: [{ series: "A", form: cell, notation: `X_{${id}}`, dimension_tex: "r(r+2)", dimension_field: complex ? "complex" : "real", parameter_summary: "Synthetic rank r >= 1.", specialization: "The displayed slice uses n = r+1.", global_form: "The selected fixture global group." }] } : {}) } },
});
const fixture = { objects: [fixtureObject("compact", true, false, "compact"), fixtureObject("split", "n = 1", false, "split"), fixtureObject("complex", false, true, "complex"), fixtureObject("unknown", null, false, null)], relationships: [] };

async function routeShell(page, data) {
  await page.route("https://lie.test/**", async route => {
    const pathname = new URL(route.request().url()).pathname;
    if (pathname === "/indexes/catalog.json") return route.fulfill({ json: data });
    if (pathname === "/catalog/lie-groups/table/") return route.fulfill({ contentType: "text/html", body: shell });
    let filename;
    if (["/assets/lie-groups.js", "/assets/lie-groups.css", "/assets/knowl.css"].includes(pathname)) filename = path.join(repo, "packages/static-runtime", path.basename(pathname));
    else if (["/assets/katex.min.js", "/assets/katex.min.css"].includes(pathname)) filename = path.join(repo, "node_modules/katex/dist", path.basename(pathname));
    else if (pathname.startsWith("/assets/fonts/")) filename = path.join(repo, "node_modules/katex/dist/fonts", path.basename(pathname));
    if (filename) return route.fulfill({ contentType: types[path.extname(filename)], body: readFileSync(filename) });
    return route.fulfill({ status: 404, body: "Not required by this test" });
  });
}
async function noOverflow(page, message) {
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), false, message);
  assert.equal(await page.locator(".katex-error").count(), 0, `${message}: mathematical rendering`);
}
async function screenshotLayouts(page) {
  const measurements = [];
  for (const width of [1440, 390]) {
    await page.setViewportSize({ width, height: width === 1440 ? 1100 : 844 });
    for (const layout of ["classification", "all"]) {
      await page.locator(`#lg-${layout}`).click();
      await page.evaluate(() => document.fonts.ready);
      await noOverflow(page, `${layout} layout fits ${width}px`);
      await page.screenshot({ path: path.join(artifacts, `${label}-${layout}-${width}.png`), fullPage: true });
      await page.screenshot({ path: path.join(artifacts, `${label}-${layout}-${width}-viewport.png`) });
      measurements.push(await page.evaluate(({ width, layout }) => ({ width, layout, pageHeight: document.documentElement.scrollHeight, firstTileTop: document.querySelector(".lg-tile:not([hidden])")?.getBoundingClientRect().top, visibleTiles: [...document.querySelectorAll(".lg-tile")].filter(node => node.getClientRects().length).length }), { width, layout }));
    }
  }
  writeFileSync(path.join(artifacts, `${label}-measurements.json`), JSON.stringify(measurements, null, 2) + "\n");
}
async function verifyDetail(page, obj, cell = null) {
  await page.locator("#lg-detail[open]").waitFor();
  assert.equal(await page.locator("#lg-detail-title").textContent(), obj.name);
  assert.equal(await page.locator(".lg-primary-link").getAttribute("href"), `/${obj.knowl}/`);
  assert.equal(await page.locator("#lg-detail .katex-error").count(), 0, `Math in ${obj.id}`);
  assert.equal(await page.locator("#lg-detail").evaluate(node => node.scrollWidth > node.clientWidth + 1), false, `Detail fits for ${obj.id}`);
  assert.match(await page.locator("#lg-detail-body").textContent(), /Global group/);
  if (cell) {
    assert.match(await page.locator("#lg-detail-body").textContent(), /This table selection/);
    assert.match(await page.locator("#lg-detail-body").textContent(), /Properties of the owning entry/);
    assert.ok((await page.locator("#lg-detail-body").textContent()).includes(cell.global_form));
    assert.equal(new URL(page.url()).searchParams.get("cell"), `${cell.series}:${cell.form}`);
    const scalar = cell.dimension_field === "complex" ? "C" : "R";
    assert.ok((await page.locator(".lg-slice annotation").allTextContents()).includes(`\\dim_{\\mathbb ${scalar}}=${cell.dimension_tex}`), `The slice uses ${cell.dimension_field} dimension for ${obj.id}`);
  }
  if ((obj.id === "lg-so-identity-p-q-r" && cell?.series === "D") || (obj.id === "lg-su-n" && cell)) {
    await page.screenshot({ path: path.join(artifacts, `${label}-detail-${obj.id}-${page.viewportSize().width}.png`) });
    if (obj.id === "lg-su-n") {
      const examples = page.locator('.lg-connections[data-context="family-examples"]');
      assert.ok(await examples.locator(".lg-detail-relation").count() > 0, "SU family details expose its recorded low-rank examples");
      await examples.locator(".lg-detail-relation").first().scrollIntoViewIfNeeded();
      await page.screenshot({ path: path.join(artifacts, `${label}-low-rank-su-${page.viewportSize().width}.png`) });
    }
  }
  if (obj.id === "lg-psl-n-c" && !cell) {
    const lorentz = page.locator('.lg-connections[data-context="family-examples"] .lg-detail-relation[data-category="real-lie-groups"]');
    assert.equal(await lorentz.count(), 1, "The PSL(2,C)/Lorentz example keeps its real Lie-group category");
    await lorentz.scrollIntoViewIfNeeded();
    await page.screenshot({ path: path.join(artifacts, `${label}-real-category-map-${page.viewportSize().width}.png`) });
  }
  await page.keyboard.press("Escape");
}

const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROME_PATH });
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 } });
  const errors = []; page.on("pageerror", error => errors.push(error.message));
  await routeShell(page, fixture);
  await page.goto("https://lie.test/catalog/lie-groups/table/");
  await page.locator('[data-lie-groups-ready="true"]').waitFor();
  assert.equal(await page.locator(".lg-tile").count(), 3);
  await page.locator('.lg-tile[data-entry-key="A:compact"]').focus();
  await page.keyboard.press("ArrowRight"); await page.keyboard.press("Enter");
  await verifyDetail(page, fixture.objects[1], fixture.objects[1].properties.lie_group.classification_cells[0]);
  assert.equal(await page.locator('.lg-tile[data-entry-key="A:split"]').evaluate(node => node === document.activeElement), true);
  await page.locator("#lg-filters summary").click();
  for (const [filter, id] of [["unknown", "unknown"], ["parameter", "split"], ["no", "complex"], ["yes", "compact"]]) {
    await page.locator("#lg-compact").selectOption(filter);
    assert.equal(await page.locator(".lg-tile").count(), 1);
    assert.equal(await page.locator(".lg-tile").getAttribute("data-group-id"), id);
  }
  await page.locator("#lg-classification").click();
  assert.equal(await page.locator("#lg-compact").inputValue(), "all", "Full-family filters must not leak into the selected rank slices");
  assert.equal(await page.locator(".lg-tile").count(), 3);
  await page.locator("#lg-field").selectOption("complex");
  assert.equal(await page.locator(".lg-tile").count(), 1);
  await page.reload(); await page.locator('[data-lie-groups-ready="true"]').waitFor();
  assert.equal(await page.locator("#lg-field").inputValue(), "complex");
  assert.equal(await page.locator("#lg-all").getAttribute("aria-pressed"), "true");
  await page.locator("#lg-reset").click();
  await page.locator("#lg-search").fill("unknown"); await page.waitForFunction(() => document.querySelectorAll(".lg-tile").length === 1);
  await page.locator(".lg-tile").click(); await verifyDetail(page, fixture.objects[3]);
  assert.deepEqual(errors, []); await page.close();

  if (process.env.PREVIEW_URL || process.env.KNOWLPEDIA_SITE_DIR || process.env.CATALOG_DATA_PATH) {
    const actual = await browser.newPage({ viewport: { width: 1440, height: 1100 } });
    const actualErrors = []; actual.on("pageerror", error => actualErrors.push(error.message));
    const base = process.env.PREVIEW_URL?.replace(/\/$/, "") || "https://lie.test";
    let data;
    if (!process.env.PREVIEW_URL && process.env.KNOWLPEDIA_SITE_DIR) {
      const site = path.resolve(process.env.KNOWLPEDIA_SITE_DIR);
      data = JSON.parse(readFileSync(path.join(site, "indexes/catalog.json"), "utf8"));
      await actual.route("https://lie.test/**", async route => {
        const pathname = decodeURIComponent(new URL(route.request().url()).pathname);
        const filename = path.resolve(site, pathname.replace(/^\/+/, ""), ...(pathname.endsWith("/") ? ["index.html"] : []));
        if (!filename.startsWith(site + path.sep) || !existsSync(filename)) return route.fulfill({ status: 404, body: "Not found" });
        return route.fulfill({ body: readFileSync(filename), contentType: types[path.extname(filename)] || "application/octet-stream" });
      });
    } else if (!process.env.PREVIEW_URL) { data = JSON.parse(readFileSync(process.env.CATALOG_DATA_PATH, "utf8")); await routeShell(actual, data); }
    await actual.goto(`${base}/catalog/lie-groups/table/`);
    await actual.locator('[data-lie-groups-ready="true"]').waitFor();
    data ||= await actual.evaluate(async () => (await fetch("/indexes/catalog.json")).json());
    const groups = data.objects.filter(obj => obj.properties?.lie_group);
    const cells = groups.flatMap(obj => (obj.properties.lie_group.classification_cells || []).map(cell => ({ obj, cell })));
    assert.equal(groups.length, 180); assert.equal(cells.length, 27);
    assert.equal(await actual.locator(".lg-matrix-row").count(), 9);
    assert.equal(await actual.locator(".lg-tile").count(), cells.length);
    await screenshotLayouts(actual);
    await actual.locator("#lg-classification").click();
    await actual.locator("#lg-search").fill("Type A");
    await actual.waitForFunction(() => document.querySelectorAll(".lg-tile").length === 3);
    assert.deepEqual(await actual.locator(".lg-tile").evaluateAll(nodes => [...new Set(nodes.map(node => node.dataset.series))]), ["A"]);
    await actual.locator("#lg-reset").click();
    const dCell = cells.find(entry => entry.cell.series === "D" && entry.cell.form === "split");
    await actual.goto(`${base}/catalog/lie-groups/table/?${new URLSearchParams({ group: dCell.obj.id, cell: "D:split" })}`);
    await actual.locator('[data-lie-groups-ready="true"]').waitFor();
    assert.equal(await actual.locator("#lg-series").inputValue(), "D", "A direct cell link selects its phone series");
    await actual.keyboard.press("Escape");
    assert.equal(await actual.locator('.lg-tile[data-entry-key="D:split"]').evaluate(node => node === document.activeElement), true, "Closing a phone cell permalink restores focus to its visible tile");
    for (const width of [1440, 390]) {
      await actual.setViewportSize({ width, height: width === 1440 ? 1100 : 844 });
      await actual.locator("#lg-classification").click();
      for (const { obj, cell } of cells) {
        if (width === 390) await actual.locator("#lg-series").selectOption(cell.series);
        await actual.locator(`.lg-tile[data-entry-key="${cell.series}:${cell.form}"]`).click();
        await verifyDetail(actual, obj, cell);
      }
      await actual.locator("#lg-all").click();
      const seen = new Set();
      for (;;) {
        const ids = await actual.locator(".lg-tile").evaluateAll(nodes => nodes.map(node => node.dataset.groupId));
        for (const id of ids) {
          assert.ok(!seen.has(id), `Each catalogue entry appears once: ${id}`); seen.add(id);
          const obj = groups.find(group => group.id === id);
          await actual.locator(`.lg-tile[data-group-id="${id}"]`).click();
          const expectedKinds = data.relationships.filter(relation => relation.source === id || relation.target === id).map(relation => relation.kind).sort();
          assert.deepEqual(await actual.locator('.lg-connections[data-context="direct"] .lg-detail-relation').evaluateAll(nodes => nodes.map(node => node.dataset.kind).sort()), expectedKinds, `All typed relationships retained for ${id}`);
          const displayedRelations = await actual.locator(".lg-detail-relation").evaluateAll(nodes => nodes.map(node => ({ id: node.dataset.relationId, kind: node.dataset.kind, category: node.dataset.category, categoryLabel: node.querySelector(".lg-relation-category").textContent })));
          for (const row of displayedRelations) {
            const sourceRelation = data.relationships.find(relation => relation.id === row.id);
            assert.equal(row.kind, sourceRelation.kind); assert.equal(row.category, sourceRelation.category_id || "");
            assert.equal(row.categoryLabel, sourceRelation.category_id ? (data.categories?.find(category => category.id === sourceRelation.category_id)?.name || sourceRelation.category_id.replaceAll("-", " ")) : "No morphism category asserted");
          }
          await verifyDetail(actual, obj);
        }
        await noOverflow(actual, `Catalogue page fits ${width}px`);
        if (await actual.locator("#lg-page-next").isDisabled()) break;
        await actual.locator("#lg-page-next").click();
      }
      assert.equal(seen.size, groups.length);
    }
    await actual.locator("#lg-classification").click();
    await actual.locator("#lg-search").fill("Heisenberg"); await actual.locator(".lg-empty").waitFor();
    await actual.getByRole("button", { name: "Search all groups" }).click();
    assert.ok(await actual.locator(".lg-tile").count() > 0);
    await actual.locator("#lg-reset").click();
    await actual.locator("#lg-classification").click();
    await actual.setViewportSize({ width: 1440, height: 1100 });
    await actual.evaluate(() => { document.documentElement.dataset.theme = "dark"; });
    await actual.screenshot({ path: path.join(artifacts, `${label}-classification-dark.png`) });
    await actual.evaluate(() => { document.documentElement.dataset.theme = "light"; });
    if (process.env.PREVIEW_URL || process.env.KNOWLPEDIA_SITE_DIR) {
      const readers = ["catalog", "catalog/created-knowls", "catalog/lie-groups-table-guide", "catalog/lie-groups-index", "lie-groups/classification-simple-lie-algebras", "lie-groups/compact-symplectic-group", ...["lg-sl-n-r", "lg-spin-n-r", "lg-spin-n-c", "lg-so-identity-p-q-r", "lg-so-p-q-r", "lg-e6-split", "lg-e8-complex", "lg-heisenberg-n-c"].map(id => groups.find(obj => obj.id === id)?.knowl).filter(Boolean)];
      for (const width of [390, 1440]) {
        await actual.setViewportSize({ width, height: width === 1440 ? 1100 : 844 });
        for (const id of readers) {
          await actual.goto(`${base}/${id}/`); await actual.evaluate(() => document.fonts.ready);
          assert.equal(await actual.locator("h1").count(), 1, `Reader exists: ${id}`);
          await actual.locator("details.knowl-section").evaluateAll(nodes => nodes.forEach(node => { node.open = true; }));
          assert.equal(await actual.locator(".katex-error, .math-render-error, .missing-knowl").count(), 0, `Reader math/links: ${id}`);
          await noOverflow(actual, `Reader ${id} fits ${width}px`);
          if (id === "catalog/lie-groups-table-guide") await actual.screenshot({ path: path.join(artifacts, `${label}-guide-${width}.png`), fullPage: true });
        }
      }
    }
    assert.deepEqual(actualErrors, []);
    writeFileSync(path.join(artifacts, `${label}-checks.json`), JSON.stringify({ catalogueEntries: groups.length, classificationCells: cells.length, widths: [1440, 390], allDetailsOpenedAtBothWidths: true, exactRelationshipKindsRetained: true, noPageOverflow: true, noKatexErrors: true, noJavaScriptErrors: true, readerPagesChecked: Boolean(process.env.PREVIEW_URL || process.env.KNOWLPEDIA_SITE_DIR) }, null, 2) + "\n");
    await actual.close();
  }
  console.log("Lie-group table passed: two layouts, slice/full-family distinction, all entries and cells, typed relationships, dimensions, filters, URL state, keyboard details, phone containment, and screenshots.");
} finally { await browser.close(); }
