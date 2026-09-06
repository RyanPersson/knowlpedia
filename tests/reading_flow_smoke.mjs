import { chromium } from "playwright";
import { readFile } from "node:fs/promises";

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

const fixture = `<!doctype html><html><body>
  <main>
    <article><section class="core-section" data-compact-core="true"><p>GNS begins <a class="knowl" data-knowl="/fragments/core.html" href="/core">the construction</a> such that</p><div class="math-display">x = y</div><p>and continues.</p></section></article>
    <section id="continuous"><div class="knowl-body"><p>Continuous begins <a class="knowl" data-knowl="/fragments/outer.html" href="/continuous">inside</a> and continues.</p><p id="later-paragraph">A later independent paragraph.</p></div></section>
    <p id="prose">Before <a class="knowl" data-knowl="/fragments/outer.html" href="/outer">the concept</a> after.</p>
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

  const core = page.locator(".core-section");
  await core.getByRole("link", { name: "the construction" }).click();
  const corePanel = page.locator(".knowl-panel").first();
  const coreParagraphs = await core.locator(":scope > p").allTextContents();
  if (coreParagraphs.join(" ") !== "GNS begins the construction such that and continues.") throw new Error("Core expansion split prose around its display equation");
  if ((await corePanel.evaluate((el) => el.parentElement?.className)) !== "core-section") throw new Error("Core panel was not inserted after the complete core");
  const coreNestedTrigger = corePanel.getByRole("link", { name: "inside" });
  await coreNestedTrigger.click();
  const coreNested = corePanel.locator(".knowl-panel");
  if ((await coreNested.count()) !== 1) throw new Error("Nested core expansion was not kept inside its owner");
  if ((await coreNested.evaluate((el) => el.parentElement?.className)) !== "knowl-body") throw new Error("Nested core panel left the compact body");
  await page.keyboard.press("Escape");
  await page.keyboard.press("Escape");

  const continuous = page.locator("#continuous");
  await continuous.getByRole("link", { name: "inside" }).click();
  const continuousPanel = continuous.locator(".knowl-panel");
  if ((await continuousPanel.evaluate((el) => el.previousElementSibling?.tagName)) !== "P") throw new Error("Unmarked continuous body used the compact-core boundary");
  if ((await continuousPanel.evaluate((el) => el.nextElementSibling?.id)) !== "later-paragraph") throw new Error("Continuous-document expansion moved to the end of the document");
  await page.keyboard.press("Escape");

  const prose = page.locator("#prose");
  await prose.getByRole("link", { name: "the concept" }).click();
  const outer = page.locator(".knowl-panel").first();
  if ((await prose.textContent()) !== "Before the concept after.") throw new Error("Expansion split the source paragraph");
  if ((await outer.evaluate((el) => el.previousElementSibling?.id)) !== "prose") throw new Error("Panel was not inserted after the paragraph");

  const nestedTrigger = outer.getByRole("link", { name: "inside" });
  await nestedTrigger.click();
  const nested = outer.locator(".knowl-panel");
  if ((await nested.count()) !== 1) throw new Error("Nested panel was not kept inside its owner");
  if ((await nested.evaluate((el) => el.previousElementSibling?.tagName)) !== "P") throw new Error("Nested panel split its paragraph");
  await page.keyboard.press("Escape");
  if ((await page.locator(".knowl-panel").count()) !== 1) throw new Error("Escape did not close the deepest panel");
  if ((await page.evaluate(() => document.activeElement?.textContent)) !== "inside") throw new Error("Escape did not restore focus to the nested trigger");

  await page.locator("#list a.knowl").click();
  const listPanel = page.locator("#list .knowl-panel");
  if ((await listPanel.evaluate((el) => el.parentElement?.tagName)) !== "LI") throw new Error("List panel escaped its list item");
  if ((await page.locator("#list > .knowl-panel").count()) !== 0) throw new Error("List received an invalid direct panel child");

  await page.locator(".index-item a.knowl").click();
  if ((await page.locator(".index-item > .knowl-panel").count()) !== 1) throw new Error("Index panel was not kept in its index item");

  await page.locator("#cell a.knowl").click();
  if ((await page.locator("#cell > .knowl-panel").count()) !== 1) throw new Error("Table cell panel was not kept in its cell");
  if ((await page.locator("table tr > .knowl-panel").count()) !== 0) throw new Error("Table received an invalid direct panel child");
  console.log("Reading flow smoke test passed: paragraph, nested focus/Escape, list, index, and table expansion.");
} finally {
  await browser.close();
}
