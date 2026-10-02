import assert from "node:assert/strict";
import { chromium } from "playwright";
import { existsSync, readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH || (existsSync(macChrome) ? macChrome : undefined);
const browser = await chromium.launch({ headless: true, executablePath });
const proof = { status: "proved-in-text", method: "Elementary calculation.", references: [], lean: null };
const category = id => ({ id, name: id, knowl: `test/${id}`, scalar: id.endsWith("c") ? "C" : "R", object_axioms: ["A structure."], morphism_axioms: ["Preserve that structure."], unit_policy: "not applicable", regularity: "linear" });
const object = (id, name, category_ids, extra = {}) => ({ id, name, notation: id === "a" ? "\\mathbb C" : "\\mathbb R", kind: "algebra", family: "example", parameters: { field: id === "a" ? "C" : "R" }, dimensions: { real: id === "a" ? 2 : 1 }, category_ids, constraints: [], properties: {}, status: "defined", references: [], knowl: `test/${id}`, ...extra });
const fixture = {
  schema_version: 1,
  objects: [object("a", "A complex object", ["vectors-r", "vectors-c"]), object("b", "B real object", ["vectors-r"]), object("c", "C group", ["groups"]), object("d", "D symbolic family", ["vectors-r"], { status: "family", dimensions: { real: "n" }, constraints: ["n >= 1"] })],
  categories: [category("vectors-r"), category("vectors-c"), category("groups")],
  views: [
    { id: "a@vectors-r", object_id: "a", category_id: "vectors-r", scalar: "R" },
    { id: "a@vectors-c", object_id: "a", category_id: "vectors-c", scalar: "C" },
    { id: "a-twisted", object_id: "a", category_id: "vectors-c", scalar: "C", description: "Conjugated scalar action", constraints: ["Use the conjugated action."] },
    { id: "b@vectors-r", object_id: "b", category_id: "vectors-r", scalar: "R" },
    { id: "c@groups", object_id: "c", category_id: "groups", scalar: null },
    { id: "d@vectors-r", object_id: "d", category_id: "vectors-r", scalar: "R" },
  ],
  relationships: [
    { id: "construction", source: "a", target: "b", kind: "scalar-restriction", category_id: null, statement: "A recorded construction, not a map.", knowl: "test/construction", conditions: ["Chosen structure."], evidence: proof },
    { id: "embedding", source: "b", target: "a", kind: "embedding", category_id: "vectors-r", statement: "A recorded real linear embedding.", knowl: "test/embedding", conditions: [], evidence: proof },
    { id: "two-input", source: "c", target: "b", kind: "construction", category_id: null, parameters: { other_input_id: "a" }, statement: "A two-input construction.", knowl: "test/two-input", conditions: [], evidence: proof },
  ],
  morphism_spaces: [
    { id: "real-aut", source_view: "a@vectors-r", target_view: "a@vectors-r", operation: "aut", coverage: "complete", result_object_ids: ["b"], description: "The real automorphism group is $\\mathrm{GL}_2(\\mathbb R)$.", conditions: [], knowl: "test/real-aut", evidence: proof },
    { id: "complex-aut", source_view: "a@vectors-c", target_view: "a@vectors-c", operation: "aut", coverage: "partial", description: "Recorded complex automorphisms.", conditions: [], knowl: "test/complex-aut", evidence: proof },
    { id: "twisted-end", source_view: "a-twisted", target_view: "a-twisted", operation: "end", description: "Maps of the conjugated structure.", conditions: [], knowl: "test/twisted-end", evidence: proof },
    { id: "real-hom", source_view: "a@vectors-r", target_view: "b@vectors-r", operation: "hom", coverage: "complete", description: "A recorded Hom description. <img src=x onerror=alert(1)>", conditions: [], knowl: "test/real-hom", evidence: proof },
  ],
  indexes: { views_by_object: {}, morphisms_by_source: {}, morphism_lookup: {}, relationships_from: {}, relationships_to: {}, construction_inputs: {} },
};
const push = (dict, key, value) => (dict[key] ||= []).push(value);
for (const view of fixture.views) push(fixture.indexes.views_by_object, view.object_id, view.id);
for (const relation of fixture.relationships) {
  push(fixture.indexes.relationships_from, relation.source, relation.id);
  push(fixture.indexes.relationships_to, relation.target, relation.id);
  if (relation.parameters?.other_input_id) push(fixture.indexes.construction_inputs, relation.parameters.other_input_id, relation.id);
}
for (const space of fixture.morphism_spaces) {
  push(fixture.indexes.morphisms_by_source, space.source_view, space.id);
  const bySource = fixture.indexes.morphism_lookup[space.source_view] ||= {};
  const byTarget = bySource[space.target_view] ||= {};
  push(byTarget, space.operation, space.id);
}

// Exercise the actual generated shell without requiring a persistent test server.
const shell = execFileSync("python3", ["-c", `
import sys
sys.path.insert(0, 'packages/compiler')
from catalog_html import render_catalog_explorer
def shell(title, body, **kwargs):
    return '<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="/assets/knowl.css"><script defer src="/assets/catalog.js"></script></head><body>'+body+'</body></html>'
print(render_catalog_explorer(shell, None))
`], { cwd: repo, encoding: "utf8" });

async function installStaticFixture(page, records) {
  await page.route("https://catalog.test/**", async route => {
    const url = new URL(route.request().url());
    if (url.pathname === "/indexes/catalog.json") return route.fulfill({ json: records });
    if (url.pathname === "/catalog/explorer/") return route.fulfill({ contentType: "text/html", body: shell });
    if (["/assets/catalog.js", "/assets/catalog.css", "/assets/knowl.css", "/assets/katex.min.js"].includes(url.pathname)) {
      const filename = url.pathname.split("/").at(-1);
      const source = filename === "katex.min.js" ? path.join(repo, "node_modules/katex/dist", filename) : path.join(repo, "packages/static-runtime", filename);
      return route.fulfill({ contentType: filename.endsWith(".js") ? "text/javascript" : "text/css", body: readFileSync(source) });
    }
    return route.fulfill({ status: 404, body: "Not needed by this test" });
  });
}

try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  await installStaticFixture(page, fixture);
  await page.goto("https://catalog.test/catalog/explorer/?source=a&target=a&operation=aut&category=vectors-r");
  await page.locator('[data-catalog-ready="true"]').waitFor();
  assert.match(await page.locator("#catalog-coverage").textContent(), /Complete description/);
  assert.equal(await page.locator("#catalog-target").isDisabled(), true);
  assert.equal(await page.locator("#catalog-morphisms .katex").count(), 1);
  assert.equal(await page.locator('#catalog-morphisms a[href="/test/b/"]').count(), 1);
  await page.locator("#catalog-category").selectOption("vectors-c");
  assert.match(await page.locator("#catalog-coverage").textContent(), /Partial/);
  assert.equal(await page.locator("#catalog-morphisms [data-record-id=real-aut]").count(), 0);
  await page.locator("#catalog-operation").selectOption("end");
  assert.match(await page.locator("#catalog-morphisms").textContent(), /does not mean that it is empty/);
  await page.locator("#catalog-source-view").selectOption("a-twisted");
  assert.equal(await page.locator("#catalog-target-view").inputValue(), "a-twisted");
  assert.match(await page.locator("#catalog-source-view-info").textContent(), /conjugated action/);
  assert.match(await page.locator("#catalog-coverage").textContent(), /Completeness not specified/);
  assert.match(await page.locator("#catalog-morphisms").textContent(), /conjugated structure/);
  await page.locator("#catalog-operation").selectOption("hom");
  await page.locator("#catalog-target").selectOption("b");
  assert.equal(await page.locator("#catalog-category").inputValue(), "vectors-r");
  assert.match(await page.locator("#catalog-morphisms").textContent(), /recorded Hom description/);
  assert.equal(await page.locator("#catalog-morphisms img").count(), 0, "Record text must not inject HTML");
  assert.equal(await page.locator(".catalog-edge.construction").count(), 2);
  assert.equal(await page.locator(".catalog-edge:not(.construction)").count(), 1);
  assert.match(await page.locator('[data-relationship-id="two-input"] .catalog-relation-title').textContent(), /C group \+ A complex object/);
  assert.equal(new URL(page.url()).searchParams.get("target"), "b");
  await page.locator("#catalog-source-search").fill("C group");
  assert.match(await page.locator("#catalog-source-matches").textContent(), /1 matching object/);
  await page.locator("#catalog-source").selectOption("c");
  assert.equal(await page.locator("#catalog-category").isDisabled(), true);
  assert.match(await page.locator("#catalog-category-info").textContent(), /no common category recorded/);
  assert.match(await page.locator("#catalog-morphisms").textContent(), /same category/);
  await page.locator("#catalog-source-search").fill("");
  await page.locator("#catalog-source").selectOption("d");
  assert.match(await page.locator("#catalog-source-card").textContent(), /Symbolic family/);
  assert.match(await page.locator("#catalog-source-card").textContent(), /n >= 1/);
  await page.setViewportSize({ width: 390, height: 844 });
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), false, "Mobile layout must not overflow horizontally");
  assert.deepEqual(errors, []);
  await page.close();

  if (process.env.PREVIEW_URL || process.env.CATALOG_DATA_PATH || process.env.KNOWLPEDIA_SITE_DIR) {
    const actual = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    const actualErrors = [];
    actual.on("pageerror", error => actualErrors.push(error.message));
    let actualData;
    let base = process.env.PREVIEW_URL?.replace(/\/$/, "") || "https://catalog.test";
    if (process.env.KNOWLPEDIA_SITE_DIR && !process.env.PREVIEW_URL) {
      const site = path.resolve(process.env.KNOWLPEDIA_SITE_DIR);
      actualData = JSON.parse(readFileSync(path.join(site, "indexes/catalog.json"), "utf8"));
      const types = { ".html": "text/html", ".json": "application/json", ".js": "text/javascript", ".css": "text/css", ".woff2": "font/woff2", ".woff": "font/woff", ".svg": "image/svg+xml" };
      await actual.route("https://catalog.test/**", async route => {
        const url = new URL(route.request().url());
        const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "");
        const filename = path.resolve(site, relative, ...(url.pathname.endsWith("/") ? ["index.html"] : []));
        if (!filename.startsWith(site + path.sep)) return route.abort();
        try {
          return route.fulfill({ body: readFileSync(filename), contentType: types[path.extname(filename)] || "application/octet-stream" });
        } catch { return route.fulfill({ status: 404, body: "Not found" }); }
      });
    } else if (!process.env.PREVIEW_URL) {
      actualData = JSON.parse(readFileSync(process.env.CATALOG_DATA_PATH, "utf8"));
      await installStaticFixture(actual, actualData);
    }
    await actual.goto(`${base}/catalog/explorer/`);
    await actual.locator('[data-catalog-ready="true"]').waitFor();
    actualData ||= await actual.evaluate(async () => (await fetch("/indexes/catalog.json")).json());
    const count = await actual.locator("#catalog-source option").count();
    assert.ok(count > 100, `Expected a substantial actual catalogue, got ${count} objects`);
    assert.equal(await actual.locator("#catalog-source-card .katex-error").count(), 0);
    assert.ok(await actual.locator("#catalog-source-card a").count() > 0);
    for (const record of actualData.morphism_spaces) {
      const source = actualData.views.find(view => view.id === record.source_view);
      const target = actualData.views.find(view => view.id === record.target_view);
      const params = new URLSearchParams({ source: source.object_id, target: target.object_id, source_view: source.id, target_view: target.id, category: source.category_id, operation: record.operation });
      await actual.goto(`${base}/catalog/explorer/?${params}`);
      await actual.locator('[data-catalog-ready="true"]').waitFor();
      assert.equal(await actual.locator(`[data-record-id="${record.id}"]`).count(), 1, `Actual record ${record.id} should be reachable by its declared views`);
      assert.equal(await actual.locator("#catalog-morphisms .katex-error").count(), 0, `Actual record ${record.id} should render its mathematics`);
      for (const resultId of record.result_object_ids || []) {
        const result = actualData.objects.find(object => object.id === resultId);
        const href = `/${result.knowl.split("/").map(encodeURIComponent).join("/")}/`;
        assert.ok(await actual.locator(`[data-record-id="${record.id}"] a[href="${href}"]`).count() > 0, `Actual record ${record.id} should link its result object ${resultId}`);
      }
    }
    await actual.goto(`${base}/catalog/explorer/`);
    await actual.locator('[data-catalog-ready="true"]').waitFor();
    if (process.env.CATALOG_SCREENSHOT) await actual.screenshot({ path: process.env.CATALOG_SCREENSHOT, fullPage: true });
    await actual.setViewportSize({ width: 390, height: 844 });
    assert.equal(await actual.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), false);
    assert.deepEqual(actualErrors, []);
    await actual.close();
  }
  console.log("Catalogue browser smoke passed: category and structure switching, sparse queries, coverage, End/Aut identity, construction arrows, escaping, search, family constraints, and mobile layout.");
} finally {
  await browser.close();
}
