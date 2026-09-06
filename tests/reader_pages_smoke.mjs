import assert from "node:assert/strict";
import { readFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { chromium } from "playwright";

// Run against a completed build without starting a preview service.
const site = path.resolve(process.env.KNOWLPEDIA_SITE_DIR || "public-imported");
const artifacts = path.resolve("tmp/reader-pages-smoke");
await mkdir(artifacts, { recursive: true });
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css",
  ".json": "application/json", ".svg": "image/svg+xml", ".woff2": "font/woff2" };
const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROME_PATH });
try {
  const context = await browser.newContext();
  await context.route("**/*", async (route) => {
    const url = new URL(route.request().url());
    if (url.hostname !== "knowlpedia.test") return route.abort();
    const relative = decodeURIComponent(url.pathname).replace(/^\/+/, "");
    const filename = path.resolve(site, relative, ...(url.pathname.endsWith("/") ? ["index.html"] : []));
    if (!filename.startsWith(site + path.sep)) return route.abort();
    try {
      await route.fulfill({ body: await readFile(filename), contentType: types[path.extname(filename)] || "application/octet-stream" });
    } catch {
      await route.fulfill({ status: 404, body: "Not found" });
    }
  });
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", (error) => errors.push(error.message));
  for (const width of [320, 390, 1440]) {
    await page.setViewportSize({ width, height: width === 1440 ? 1000 : 844 });
    for (const id of ["operator-algebras/gns-construction", "algebra-category-theory/group-object",
      "complex-analysis/subharmonic-function", "complex-analysis/quaternionic-plurisubharmonic-function"]) {
      await page.goto(`http://knowlpedia.test/${id}/`);
      await page.evaluate(() => document.fonts.ready);
      assert.equal(await page.locator("h1").count(), 1, `Missing page: ${id}`);
      assert.equal(await page.locator(".core-heading").count(), 0, `Repeated definition label: ${id}`);
      await page.locator("details.knowl-section").evaluateAll((sections) => sections.forEach((section) => { section.open = true; }));
      assert.equal(await page.locator(".math-render-error, .katex-error, .missing-knowl").count(), 0, `Rendering error: ${id}`);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `Page overflow: ${width}px ${id}`);
      if (id.endsWith("group-object")) {
        const overflow = await page.locator(".core-section .math-display").evaluateAll((formulas) =>
          formulas.some((formula) => formula.scrollWidth > formula.clientWidth + 1));
        assert.equal(overflow, false, `Group-object axioms require sideways scrolling at ${width}px`);
      }
      if (id.endsWith("gns-construction") && width === 390) {
        const coreTop = await page.locator(".core-section").evaluate((element) => element.getBoundingClientRect().top);
        assert.ok(coreTop < 320, `Definition begins too far down the mobile page: ${coreTop}`);
        console.log(`390px GNS definition begins at ${Math.round(coreTop)}px`);
        const trigger = page.locator(".core-section a.knowl").filter({ hasText: "positive linear functional" }).first();
        const paragraph = trigger.locator("xpath=ancestor::p[1]");
        const before = await paragraph.textContent();
        await trigger.click();
        await page.locator(".knowl-panel .knowl-content").waitFor();
        assert.equal(await paragraph.textContent(), before, "Expanded prerequisite interrupts its sentence");
        assert.equal(await page.locator(".core-section").evaluate((core) => {
          const panel = core.querySelector(".knowl-panel");
          return panel && core.lastElementChild === panel;
        }), true, "Expansion separates definition prose from its displayed equation");
      }
      await page.screenshot({ path: path.join(artifacts, `${id.split("/").pop()}-${width}.png`), fullPage: true });
    }
  }

  await page.goto("http://knowlpedia.test/graph/?focus=algebra-rings/ring");
  await page.locator("#graph-viewer-content .knowl-content").waitFor();
  assert.match(await page.locator("#graph-review-state").textContent(), /This prerequisite list has 1 review/);
  assert.match(await page.locator("#graph-status").textContent(), /reviewed and \d+ unreviewed/);
  const graph = JSON.parse(await readFile(path.join(site, "indexes/dependencies.json"), "utf8"));
  const ring = "algebra-rings/ring";
  for (const specialization of ["unital-ring", "commutative-ring"]) {
    const id = `algebra-rings/${specialization}`;
    assert.ok(graph.edges.some((edge) => edge.source === ring && edge.target === id && edge.reviewed));
    assert.ok(!graph.edges.some((edge) => edge.source === id && edge.target === ring));
  }
  await page.screenshot({ path: path.join(artifacts, "ring-graph.png") });
  assert.deepEqual(errors, [], "Browser errors");
  console.log("Reader pages passed at 320px, 390px, and 1440px; reviewed ring dependencies passed.");
} finally {
  await browser.close();
}
