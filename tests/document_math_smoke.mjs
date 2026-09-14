import assert from "node:assert/strict";
import { dirname, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";
import katex from "katex";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const base = process.env.PREVIEW_URL || "http://127.0.0.1:8015";
const escape = (text) => text.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
const long = Array.from({ length: 12 }, (_, i) => `a_{${i + 1}}`).join("+") + "=0";
const math = (id, tex, display = false) => `<${display ? "div" : "span"} id="${id}" class="math-${display ? "display" : "inline"} math-mathjax" data-document-math="true">${escape(display ? `\\[${tex}\\]` : `\\(${tex}\\)`)}</${display ? "div" : "span"}>`;
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const errors = [];
  const failures = [];
  page.on("pageerror", (error) => errors.push(error.message));
  page.on("response", (response) => { if (response.status() >= 400) failures.push(response.url()); });
  // Use generic formulas and local runtime files, without a private paper.
  await page.route((url) => ["/assets/knowl.css", "/assets/document-math.js"].includes(url.pathname), async (route) => {
    const name = new URL(route.request().url()).pathname.split("/").pop();
    await route.fulfill({ path: resolve(root, "packages/static-runtime", name), contentType: name.endsWith("css") ? "text/css" : "text/javascript" });
  });
  await page.route((url) => url.pathname.startsWith("/assets/mathjax/"), async (route) => {
    const directory = resolve(root, "node_modules/mathjax/es5");
    const path = resolve(directory, new URL(route.request().url()).pathname.slice("/assets/mathjax/".length));
    assert(path.startsWith(directory + sep));
    await route.fulfill({ path, contentType: path.endsWith(".woff") ? "font/woff" : "text/javascript" });
  });
  const fixture = `<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="/assets/knowl.css"><link rel="stylesheet" href="/assets/katex.min.css">
<style>::-webkit-scrollbar{width:6px;height:6px}::-webkit-scrollbar-thumb{background:#aaa}
/* Native MathML metrics can be wider than the visible typeset formula. */
#accessible-term mjx-assistive-mml math{font-size:4em}</style>
<script>window.MathJax={startup:{typeset:false}};</script><script defer src="/assets/mathjax/tex-chtml.js"></script><script defer src="/assets/document-math.js"></script></head>
<body><main class="page-shell document-markdown-shell"><article class="document-markdown"><section class="core-section">
<p>Short terms ${math("letter", "k")}, ${math("subscript", "\\beta_k")}, ${math("short-inline", "F_\\eta(c)=d(\\eta)")} and ${math("delimiters", "\\left(f(x)\\right)")}.</p>
${math("short-display", "8\\beta_0^2\\kappa_0d_0\\le1", true)}
${math("tag-display", "x+y=z\\tag{1}", true)}
<p style="text-align:right">${math("accessible-term", "a+b=c")}</p>
<p>A longer inline expression: ${math("long-inline", long)}.</p>
${math("long-display", long, true)}
${math("long-tag-display", `${long}\\tag{2}`, true)}
<div id="inserted-knowl"></div></section></article></main></body></html>`;
  await page.route("**/document-math-fixture/", (route) => route.fulfill({ contentType: "text/html", body: fixture }));
  await page.goto(`${base}/document-math-fixture/`);
  await page.waitForFunction(() => !!window.KnowlpediaDocumentMath);
  await page.evaluate(async () => {
    await window.KnowlpediaDocumentMath.ready;
    await window.KnowlpediaDocumentMath.typesetAll();
    await document.fonts.ready;
  });

  async function check(id, scrolls) {
    await page.waitForFunction(({ id, scrolls }) => document.getElementById(id).classList.contains("math-overflow-x") === scrolls, { id, scrolls });
    const result = await page.locator(`#${id}`).evaluate((node) => {
      const style = getComputedStyle(node);
      node.scrollLeft = 0;
      const math = node.querySelector("mjx-math, .katex-html");
      const left = math.getBoundingClientRect().left - node.getBoundingClientRect().left;
      node.scrollLeft = node.scrollWidth;
      return { x: style.overflowX, y: style.overflowY, offset: node.scrollLeft, left };
    });
    assert.equal(result.x, scrolls ? "auto" : "visible", id);
    assert.equal(result.y, scrolls ? "hidden" : "visible", id);
    if (scrolls) {
      assert(result.offset > 0, `${id} remains horizontally scrollable`);
      assert(result.left >= -1, `${id} starts with its left edge visible`);
    } else assert.equal(result.offset, 0, `${id} is not a scroll container`);
  }
  for (const id of ["letter", "subscript", "short-inline", "delimiters", "short-display", "tag-display", "accessible-term"]) await check(id, false);
  for (const id of ["long-inline", "long-display", "long-tag-display"]) await check(id, true);
  assert.equal(await page.locator("#accessible-term mjx-assistive-mml math").textContent(), "a+b=c", "The accessible MathML copy is preserved");
  assert.equal(await page.locator(".math-mathjax mjx-container").evaluateAll((nodes) => nodes.every((node) => getComputedStyle(node).overflowX === "visible" && getComputedStyle(node).overflowY === "visible")), true, "MathJax does not create nested scrollbars");

  const inserted = `<aside class="knowl-panel"><div class="knowl-content"><div class="knowl-body"><p>A nested term <span id="nested-short" class="math-inline math-katex">${katex.renderToString("f(x)=y")}</span>.</p><div id="nested-long" class="math-display math-katex">${katex.renderToString(long, { displayMode: true })}</div></div></div></aside>`;
  await page.locator("#inserted-knowl").evaluate((node, html) => { node.innerHTML = html; }, inserted);
  await page.evaluate(() => document.fonts.ready);
  await check("nested-short", false);
  await check("nested-long", true);
  await page.setViewportSize({ width: 1000, height: 900 });
  for (const id of ["long-inline", "long-display", "long-tag-display", "nested-long"]) await check(id, false);
  await page.setViewportSize({ width: 390, height: 844 });
  for (const id of ["long-inline", "long-display", "long-tag-display", "nested-long"]) await check(id, true);
  await page.locator("#short-inline").evaluate((node) => { node.style.fontSize = "100px"; });
  await check("short-inline", true);
  await page.locator("#short-inline").evaluate((node) => { node.style.fontSize = ""; });
  await check("short-inline", false);
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), true, "Mobile page stays within the viewport");
  assert.deepEqual(errors, []);
  assert.deepEqual(failures, []);
  console.log("Document math smoke passed: fitting formulas have no scrollbars; wide formulas scroll; resize, font changes and inserted knowls update correctly.");
} finally {
  await browser.close();
}
