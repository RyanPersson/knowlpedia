import assert from "node:assert/strict";
import { readFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { chromium } from "playwright";

const site = path.resolve(process.env.KNOWLPEDIA_SITE_DIR || "public-imported");
const artifacts = path.resolve("tmp/catalog-content-smoke");
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".woff": "font/woff" };
await mkdir(artifacts, { recursive: true });
const data = JSON.parse(await readFile(path.join(site, "indexes/catalog.json"), "utf8"));
const objectIds = ["lg-sl-2-c", "la-heisenberg-1-r", "j-herm-3-o", "scalar-split-o", "field-qp", "field-f2-laurent"];
const pages = ["catalog", "catalog/created-knowls", ...objectIds.map(id => {
  const obj = data.objects.find(object => object.id === id);
  assert.ok(obj, `Missing representative object ${id}`);
  return obj.knowl;
}), "catalog/arithmetic/adeles-q", "catalog/arithmetic/ideles-q", "catalog/relationships/compact-freudenthal-magic-square", "catalog/relationships/vinberg-magic-square-construction", "knowlification/orders-and-fractional-ideals-index", "algebra-rings/order-in-algebra", "algebra-rings/maximal-order", "algebra-rings/fraction-field", "algebra-commutative/fractional-ideal", "algebra-commutative/dedekind-domain"];
const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROME_PATH });
try {
  const context = await browser.newContext();
  const failures = [];
  await context.route("**/*", async route => {
    const url = new URL(route.request().url());
    if (url.hostname !== "knowlpedia.test") return route.abort();
    const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "");
    const filename = path.resolve(site, relative, ...(url.pathname.endsWith("/") ? ["index.html"] : []));
    if (!filename.startsWith(site + path.sep)) return route.abort();
    try {
      await route.fulfill({ body: await readFile(filename), contentType: types[path.extname(filename)] || "application/octet-stream" });
    } catch {
      failures.push(url.pathname);
      await route.fulfill({ status: 404, body: "Not found" });
    }
  });
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  for (const width of [390, 1440]) {
    await page.setViewportSize({ width, height: width === 1440 ? 1000 : 844 });
    for (const id of pages) {
      await page.goto(`https://knowlpedia.test/${id}/`);
      await page.evaluate(() => document.fonts.ready);
      assert.equal(await page.locator("h1").count(), 1, `Missing page title: ${id}`);
      await page.locator("details.knowl-section").evaluateAll(sections => sections.forEach(section => { section.open = true; }));
      assert.equal(await page.locator(".math-render-error, .katex-error, .missing-knowl").count(), 0, `Rendering error: ${id}`);
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
      assert.equal(overflow, false, `Page overflow at ${width}px: ${id}`);
      if (["catalog/arithmetic/adeles-q", "catalog/arithmetic/ideles-q"].includes(id)) {
        assert.ok(await page.locator(".core-section .math-display .katex").count() > 0, `Restricted-product formula must render on ${id}`);
        const rawMath = await page.locator(".core-section").evaluate(node => {
          const walker = document.createTreeWalker(node, NodeFilter.SHOW_TEXT);
          const outsideMath = [];
          while (walker.nextNode()) {
            if (!walker.currentNode.parentElement.closest(".math-inline, .math-display, annotation, .katex")) outsideMath.push(walker.currentNode.textContent);
          }
          return outsideMath.join("");
        });
        assert.doesNotMatch(rawMath, /\\(?:\[|\]|\(|\)|mathbb|mathcal|prod)/, `Raw TeX leaked into prose on ${id}`);
      }
      if (id.includes("vinberg")) {
        assert.ok(await page.locator(".math-display").count() > 0, "Vinberg construction must render its displayed formula");
        const displayStates = await page.locator(".math-display").evaluateAll(nodes => nodes.map(node => ({
          overflowing: node.scrollWidth > node.clientWidth + 1,
          overflowX: getComputedStyle(node).overflowX,
        })));
        assert.ok(displayStates.every(state => !state.overflowing || ["auto", "scroll"].includes(state.overflowX)), `Vinberg long displays must scroll within the page at ${width}px`);
      }
      if (["catalog", "catalog/arithmetic/adeles-q", "catalog/arithmetic/ideles-q", "catalog/relationships/vinberg-magic-square-construction", "algebra-rings/order-in-algebra", "knowlification/orders-and-fractional-ideals-index"].includes(id)) {
        await page.screenshot({ path: path.join(artifacts, `${id.replaceAll("/", "-")}-${width}.png`), fullPage: true });
      }
    }
  }
  // A newly added definition remains usable inside the ordinary inline knowl flow.
  await page.goto("https://knowlpedia.test/knowlification/orders-and-fractional-ideals-index/");
  await page.locator('a.knowl[href="/algebra-rings/order-in-algebra/"]').first().click();
  await page.locator(".knowl-panel .knowl-content").waitFor();
  assert.match(await page.locator(".knowl-panel .knowl-content").first().textContent(), /order|algebra/i);
  assert.equal(await page.locator(".knowl-panel .missing-knowl, .knowl-panel .katex-error").count(), 0);
  assert.deepEqual(errors, [], "Browser errors");
  assert.deepEqual(failures, [], "Missing site resources");
  console.log(`Catalogue content smoke passed: ${pages.length} pages at 390px and 1440px, mathematical rendering, Vinberg overflow containment, and inline order definition.`);
} finally {
  await browser.close();
}
