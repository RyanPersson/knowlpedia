import { chromium } from "playwright";
import { readFile } from "node:fs/promises";
import assert from "node:assert/strict";

const runtime = await readFile(new URL("../packages/static-runtime/knowl.js", import.meta.url), "utf8");
const base = "http://knowlpedia.test";
const fragments = {
  "/fragments/core.html": '<div class="knowl-content" data-knowl-title="Core"><div class="knowl-body" data-compact-core="true"><p>Core begins <a class="knowl" data-knowl="/fragments/inner.html" href="/inner">inside</a> such that</p><div class="math-display">x = y</div><p>and continues.</p></div></div>',
  "/fragments/outer.html": '<div class="knowl-content" data-knowl-title="Outer"><p>Outer begins <a class="knowl" data-knowl="/fragments/inner.html" href="/inner">inside</a> and continues.</p></div>',
  "/fragments/inner.html": '<div class="knowl-content" data-knowl-title="Inner"><p>Inner definition.</p></div>',
  "/fragments/list.html": '<div class="knowl-content" data-knowl-title="List"><p>List definition.</p></div>',
  "/fragments/index.html": '<div class="knowl-content" data-knowl-title="Index"><p>Index definition.</p></div>',
  "/fragments/table.html": '<div class="knowl-content" data-knowl-title="Table"><p>Table definition.</p></div>'
};

const fixture = `<!doctype html><html><head><meta charset="utf-8"></head><body>
  <main>
    <article><section class="core-section" data-compact-core="true"><p>GNS begins <a class="knowl" data-knowl="/fragments/core.html" href="/core">the construction</a> such that</p><div class="math-display">x = y</div><p>and continues.</p></section></article>
    <section id="continuous"><div class="knowl-body"><p>Continuous begins <a class="knowl" data-knowl="/fragments/outer.html" href="/continuous">inside</a> and continues.</p><p id="later-paragraph">A later independent paragraph.</p></div></section>
    <p id="prose">Before <a class="knowl" data-knowl="/fragments/outer.html" href="/outer">the concept</a> after.</p>
    <section id="formatted"><p id="formatted-prose">Before <strong id="emphasis">bold <em>start <a class="knowl" data-knowl="/fragments/inner.html" href="/inner">first</a> middle <a class="knowl" data-knowl="/fragments/inner.html" href="/inner">second</a> end</em> bold tail</strong> <span class="math-inline">x²</span> then <a class="knowl" data-knowl="/fragments/inner.html" href="/inner">third</a>.</p></section>
    <ul id="list"><li>List item: <a class="knowl" data-knowl="/fragments/list.html" href="/list">expand this</a> and continue.</li></ul>
    <ol><li class="index-item"><a class="knowl index-knowl" data-knowl="/fragments/index.html" href="/index">Index entry</a></li></ol>
    <table><tbody><tr><td id="cell">Cell: <a class="knowl" data-knowl="/fragments/table.html" href="/table">expand</a> remains valid.</td></tr></tbody></table>
  </main>
</body></html>`;

const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROME_PATH });
try {
  const page = await browser.newPage();
  await page.route(`${base}/**/*`, async (route) => {
    const path = new URL(route.request().url()).pathname;
    if (path === "/fixture/") return route.fulfill({ body: fixture, contentType: "text/html" });
    if (fragments[path]) return route.fulfill({ body: fragments[path], contentType: "text/html" });
    return route.fulfill({ status: 404, body: "Not found" });
  });
  await page.goto(`${base}/fixture/`);
  await page.addScriptTag({ content: runtime });
  await page.locator("a.knowl").evaluateAll((links) => links.forEach((link) => link.setAttribute("aria-expanded", "false")));

  const core = page.locator(".core-section");
  await core.getByRole("link", { name: "the construction" }).click();
  const corePanel = page.locator(".knowl-panel").first();
  const coreParagraphs = await core.locator(":scope > p").allTextContents();
  assert.deepEqual(coreParagraphs, ["GNS begins the construction", " such that", "and continues."]);
  assert.equal(await corePanel.evaluate((el) => el.nextElementSibling?.textContent), " such that", "Compact core must resume immediately below the definition");
  assert.equal(await corePanel.evaluate((el) => el.nextElementSibling?.nextElementSibling?.className), "math-display", "Display equation must retain its position after the resumed prose");
  const coreNestedTrigger = corePanel.getByRole("link", { name: "inside" });
  await coreNestedTrigger.click();
  const coreNested = corePanel.locator(".knowl-panel");
  if ((await coreNested.count()) !== 1) throw new Error("Nested core expansion was not kept inside its owner");
  if ((await coreNested.evaluate((el) => el.parentElement?.className)) !== "knowl-body") throw new Error("Nested core panel left the compact body");
  assert.equal(await coreNested.evaluate((el) => el.nextElementSibling?.textContent), " such that");
  await page.keyboard.press("Escape");
  await page.keyboard.press("Escape");

  const continuous = page.locator("#continuous");
  await continuous.getByRole("link", { name: "inside" }).click();
  const continuousPanel = continuous.locator(".knowl-panel");
  if ((await continuousPanel.evaluate((el) => el.previousElementSibling?.tagName)) !== "P") throw new Error("Unmarked continuous body used the compact-core boundary");
  assert.equal(await continuousPanel.evaluate((el) => el.nextElementSibling?.textContent), " and continues.");
  assert.equal(await continuousPanel.evaluate((el) => el.nextElementSibling?.nextElementSibling?.id), "later-paragraph");
  await page.keyboard.press("Escape");

  const prose = page.locator("#prose");
  await prose.getByRole("link", { name: "the concept" }).click();
  const outer = page.locator(".knowl-panel").first();
  assert.equal(await prose.textContent(), "Before the concept");
  assert.equal(await outer.evaluate((el) => el.previousElementSibling?.id), "prose");
  assert.equal(await outer.evaluate((el) => el.nextElementSibling?.textContent), " after.");
  assert.equal(await page.locator("p .knowl-panel").count(), 0, "Panels must not create invalid paragraph markup");

  const nestedTrigger = outer.getByRole("link", { name: "inside" });
  await nestedTrigger.click();
  const nested = outer.locator(".knowl-panel");
  if ((await nested.count()) !== 1) throw new Error("Nested panel was not kept inside its owner");
  assert.equal(await nested.evaluate((el) => el.previousElementSibling?.textContent), "Outer begins inside");
  assert.equal(await nested.evaluate((el) => el.nextElementSibling?.textContent), " and continues.");
  await page.keyboard.press("Escape");
  if ((await page.locator(".knowl-panel").count()) !== 1) throw new Error("Escape did not close the deepest panel");
  if ((await page.evaluate(() => document.activeElement?.textContent)) !== "inside") throw new Error("Escape did not restore focus to the nested trigger");
  assert.equal(await outer.locator("p").textContent(), "Outer begins inside and continues.");
  await page.keyboard.press("Escape");
  assert.equal(await prose.textContent(), "Before the concept after.", "Closing must rejoin the sentence");

  const formatted = page.locator("#formatted");
  const originalMarkup = await formatted.innerHTML();
  await formatted.evaluate((element) => {
    window.originalMath = element.querySelector(".math-inline");
    window.originalThird = element.querySelectorAll("a.knowl")[2];
    window.thirdClicks = 0;
    window.originalThird.addEventListener("click", () => window.thirdClicks++);
  });
  const orders = [["first", "second", "third"], ["third", "second", "first"], ["second", "first", "third"]];
  for (const openOrder of orders) {
    for (const closeOrder of orders) {
      for (const name of openOrder) await formatted.getByRole("link", { name, exact: true }).click();
      assert.equal(await formatted.locator(".knowl-panel").count(), 3);
      assert.equal(await page.locator("#emphasis").count(), 1, "Splitting must not duplicate IDs");
      assert.deepEqual(await formatted.locator(":scope > p").allTextContents(), ["Before bold start first", " middle second", " end bold tail x² then third", "."]);
      for (const name of closeOrder) await formatted.getByRole("link", { name, exact: true }).click();
      assert.equal(await formatted.innerHTML(), originalMarkup, "Any closing order must restore the original formatted paragraph");
    }
  }
  assert.equal(await formatted.evaluate((element) => element.querySelector(".math-inline") === window.originalMath), true);
  assert.equal(await formatted.evaluate((element) => element.querySelectorAll("a.knowl")[2] === window.originalThird), true);
  assert.equal(await page.evaluate(() => window.thirdClicks), 18, "Moved links retain their listeners");

  // Closing a parent with an open descendant restores only the outer prose.
  await prose.getByRole("link", { name: "the concept" }).click();
  await page.locator(".knowl-panel").getByRole("link", { name: "inside" }).click();
  await prose.getByRole("link", { name: "the concept" }).click();
  assert.equal(await page.locator(".knowl-panel").count(), 0);
  assert.equal(await prose.textContent(), "Before the concept after.");

  await page.locator("#list a.knowl").click();
  const listPanel = page.locator("#list .knowl-panel");
  if ((await listPanel.evaluate((el) => el.parentElement?.tagName)) !== "LI") throw new Error("List panel escaped its list item");
  assert.equal(await listPanel.evaluate((el) => el.nextSibling?.textContent), " and continue.");
  if ((await page.locator("#list > .knowl-panel").count()) !== 0) throw new Error("List received an invalid direct panel child");

  await page.locator(".index-item a.knowl").click();
  if ((await page.locator(".index-item > .knowl-panel").count()) !== 1) throw new Error("Index panel was not kept in its index item");

  await page.locator("#cell a.knowl").click();
  if ((await page.locator("#cell > .knowl-panel").count()) !== 1) throw new Error("Table cell panel was not kept in its cell");
  assert.equal(await page.locator("#cell > .knowl-panel").evaluate((el) => el.nextSibling?.textContent), " remains valid.");
  if ((await page.locator("table tr > .knowl-panel").count()) !== 0) throw new Error("Table received an invalid direct panel child");
  console.log("Reading flow smoke test passed: inline prose/core/nested/list/cell expansion, arbitrary closing order, formatting/math/node preservation, focus/Escape, and index placement.");
} finally {
  await browser.close();
}
