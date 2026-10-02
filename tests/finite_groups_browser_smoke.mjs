import assert from "node:assert/strict";
import { chromium } from "playwright";
import { execFileSync } from "node:child_process";
import { readFileSync, existsSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const artifacts = path.join(repo, "tmp/finite-groups-layouts");
mkdirSync(artifacts, { recursive: true });
const known = (id, name, order, section = "sporadic", cluster = "monster") => ({
  id, name, notation: `X_{${id.split("-").at(-1)}}`, kind: "finite-group", family: "synthetic-test-group", status: "defined",
  parameters: {}, constraints: [], knowl: `test/${id}`, properties: { finite_group: {
    table_role: section === "sporadic" ? "sporadic" : "example", section, order_tex: order, order_decimal: order,
    simple: section === "sporadic", simple_condition: "A synthetic fixture statement for the browser test.",
    parameter_summary: "One specified group.", construction_summary: "Synthetic fixture; no mathematical classification is asserted.",
    ...(cluster ? { sporadic_cluster: cluster } : {}),
  } },
});
const family = (id, name, notation, section, domain, order) => ({
  id, name, notation, kind: "finite-group", family: "test-family", status: "family", parameters: { n: "n" },
  constraints: [domain], knowl: `test/${id}`, properties: { finite_group: {
    table_role: section === "familiar" ? "family" : "simple-family", section, order_tex: order, order_decimal: null,
    simple: section !== "familiar" ? true : null, simple_condition: "Simplicity is subject to the fixture parameter conditions.",
    parameter_summary: domain, construction_summary: "A test family used to exercise layout and constraints.", rank_label: "parameter n",
    ...(id.startsWith("fg-classical-") ? { display_order: 7 - Number(id.split("-").at(-1)) } : {}),
  } },
});
const fixture = {
  schema_version: 1,
  objects: [
    family("fg-prime", "Prime cyclic groups", "C_p", "cyclic", "p is a prime.", "p"),
    family("fg-alternating", "Alternating groups", "A_n", "alternating", "n is an integer with n ≥ 5.", "n!/2"),
    ...Array.from({ length: 6 }, (_, i) => family(`fg-classical-${i + 1}`, `Classical fixture ${i + 1}`, `A_{${i + 1}}(q)`, "classical", "q is a prime power; the stated low-rank exclusions apply.", "q^{n(n-1)/2}\\prod_{j=2}^n(q^j-1)/\\gcd(n,q-1)")),
    ...Array.from({ length: 10 }, (_, i) => family(`fg-exceptional-${i + 1}`, `Exceptional fixture ${i + 1}`, `${i < 5 ? "E" : "{}^2F"}_{${i + 1}}(q)`, "exceptional", "q is a prime power in the stated parameter range.", "q^{120}\\prod_{d\\in D}(q^d-1)")),
    { ...known("fg-tits", "Tits fixture", "17971200", "exceptional", null), properties: { finite_group: { ...known("fg-tits", "", "17971200", "exceptional", null).properties.finite_group, table_role: "tits", simple: true } } },
    ...Array.from({ length: 24 }, (_, i) => known(`fg-sporadic-${i + 1}`, `Sporadic fixture ${i + 1}`, String((i + 2) * (i + 2) * 1234567), "sporadic", ["mathieu", "leech", "monster", "pariah"][Math.floor(i / 6)])),
    known("fg-large-a", "Z earlier huge fixture", "9007199254740992", "sporadic", "monster"),
    known("fg-large-b", "A later huge fixture", "9007199254740993", "sporadic", "monster"),
    known("fg-unclustered", "Unassigned-cluster fixture", "199999999999999999999", "sporadic", null),
    family("fg-cyclic", "All cyclic groups", "C_n", "familiar", "n is a positive integer.", "n"),
    family("fg-dihedral", "Dihedral groups", "D_{2n}", "familiar", "n is an integer with n ≥ 3.", "2n"),
    known("fg-trivial", "Trivial group", "1", "familiar", null),
    known("fg-small", "Small example", "8", "familiar", null),
  ],
  relationships: [], indexes: { relationships_from: {}, relationships_to: {} },
};

const shell = execFileSync("python3", ["-c", `
import sys
sys.path.insert(0, 'packages/compiler')
from finite_groups_html import render_finite_groups_table
def shell(title, body, **kwargs):
    return '<!doctype html><html data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="/assets/knowl.css"><link rel="stylesheet" href="/assets/katex.min.css"><script defer src="/assets/finite-groups.js"></script></head><body>'+body+'</body></html>'
print(render_finite_groups_table(shell, None))
`], { cwd: repo, encoding: "utf8" });
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".svg": "image/svg+xml" };

async function fixtureRoutes(page, records) {
  await page.route("https://finite.test/**", async route => {
    const pathname = new URL(route.request().url()).pathname;
    if (pathname === "/indexes/catalog.json") return route.fulfill({ json: records });
    if (pathname === "/catalog/finite-groups/table/") return route.fulfill({ contentType: "text/html", body: shell });
    let filename;
    if (["/assets/finite-groups.js", "/assets/finite-groups.css", "/assets/knowl.css"].includes(pathname)) filename = path.join(repo, "packages/static-runtime", path.basename(pathname));
    else if (["/assets/katex.min.js", "/assets/katex.min.css"].includes(pathname)) filename = path.join(repo, "node_modules/katex/dist", path.basename(pathname));
    else if (pathname.startsWith("/assets/fonts/")) filename = path.join(repo, "node_modules/katex/dist/fonts", path.basename(pathname));
    if (filename) return route.fulfill({ contentType: types[path.extname(filename)], body: readFileSync(filename) });
    return route.fulfill({ status: 404, body: "Not needed by this test" });
  });
}

async function screenshotLayouts(page, prefix) {
  for (const width of [1440, 390]) {
    await page.setViewportSize({ width, height: width === 1440 ? 1100 : 844 });
    for (const layout of ["classification", "all"]) {
      await page.locator(`#fg-${layout}`).click();
      await page.evaluate(() => document.fonts.ready);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), false, `${layout} layout must fit ${width}px`);
      await page.screenshot({ path: path.join(artifacts, `${prefix}-${layout}-${width}.png`), fullPage: true });
      await page.screenshot({ path: path.join(artifacts, `${prefix}-${layout}-${width}-viewport.png`) });
    }
  }
}

async function screenshotSporadics(page, prefix) {
  await page.locator("#fg-classification").click();
  await page.locator("#fg-region").selectOption("sporadic");
  for (const width of [1440, 390]) {
    await page.setViewportSize({ width, height: width === 1440 ? 1100 : 844 });
    for (const arrangement of ["cluster", "order"]) {
      await page.locator("#fg-sporadic-order").selectOption(arrangement);
      await page.screenshot({ path: path.join(artifacts, `${prefix}-sporadics-${arrangement}-${width}.png`), fullPage: true });
    }
  }
  await page.locator("#fg-reset").click();
}

const browser = await chromium.launch({ headless: true, executablePath: process.env.PLAYWRIGHT_CHROME_PATH });
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 } });
  const errors = []; page.on("pageerror", error => errors.push(error.message));
  await fixtureRoutes(page, fixture);
  await page.goto("https://finite.test/catalog/finite-groups/table/");
  await page.locator('[data-finite-groups-ready="true"]').waitFor();
  assert.equal(await page.evaluate(() => document.characterSet), "UTF-8");
  assert.doesNotMatch(await page.locator("#fg-status").textContent(), /Â|â€|�/);
  assert.equal(await page.locator('.fg-tile[data-role="simple-family"]').count(), 18);
  assert.equal(await page.locator('.fg-tile[data-role="sporadic"]').count(), 27, "An optional missing cluster must not drop a record");
  assert.equal(await page.locator('.fg-cluster .fg-tile[data-role="tits"]').count(), 0);
  assert.equal(await page.locator('.fg-boundary .fg-tile[data-role="tits"]').count(), 1);
  assert.equal(await page.locator('.fg-tile[data-region="classical"]').first().getAttribute("data-group-id"), "fg-classical-6", "Authored presentation order wins over alphabetical order");
  await page.locator('.fg-tile[data-group-id="fg-prime"]').focus();
  await page.keyboard.press("ArrowRight");
  assert.equal(await page.locator('.fg-tile[data-group-id="fg-alternating"]').evaluate(node => node === document.activeElement), true);
  await page.keyboard.press("End");
  assert.equal(await page.locator('.fg-tile[data-group-id="fg-unclustered"]').evaluate(node => node === document.activeElement), true);
  await page.keyboard.press("Home");
  assert.equal(await page.locator('.fg-tile[data-group-id="fg-prime"]').evaluate(node => node === document.activeElement), true);
  await page.locator("#fg-sporadic-order").selectOption("order");
  const ordered = await page.locator('.fg-tile[data-role="sporadic"]').evaluateAll(nodes => nodes.map(node => node.dataset.groupId));
  assert.ok(ordered.indexOf("fg-large-a") < ordered.indexOf("fg-large-b"), "Huge orders must not round to a Number tie");
  await page.locator("#fg-sporadic-order").selectOption("cluster");
  await screenshotLayouts(page, process.env.FIXTURE_LAYOUT_LABEL || "fixture-current");
  assert.equal(await page.locator('[data-collection="families"] .fg-tile[data-role="example"]').count(), 0);
  assert.equal(await page.locator('[data-collection="individual groups"] .fg-tile').first().getAttribute("data-group-id"), "fg-trivial");
  await page.locator("#fg-search").fill("9,007,199,254,740,993");
  await page.waitForFunction(() => document.querySelectorAll(".fg-tile").length === 1);
  await page.locator('.fg-tile[data-group-id="fg-large-b"]').click();
  await page.locator("#fg-detail[open]").waitFor();
  assert.match(await page.locator(".fg-exact-order").textContent(), /9,007,199,254,740,993/);
  assert.equal(await page.locator(".fg-detail a.fg-primary-link").getAttribute("href"), "/test/fg-large-b/");
  assert.match(await page.locator('.fg-detail a[href^="/catalog/explorer/"]').getAttribute("href"), /category=finite-groups/);
  assert.equal(new URL(page.url()).searchParams.get("group"), "fg-large-b");
  await page.keyboard.press("Escape");
  assert.equal(await page.locator('.fg-tile[data-group-id="fg-large-b"]').evaluate(node => node === document.activeElement), true);
  await page.locator("#fg-reset").click();
  await page.locator("#fg-region").selectOption("familiar");
  assert.equal(await page.locator("#fg-all").getAttribute("aria-pressed"), "true");
  assert.equal(await page.locator('.fg-tile:not([data-region="familiar"])').count(), 0);
  await page.locator('.fg-tile[data-group-id="fg-trivial"]').focus();
  await page.keyboard.press("Enter");
  assert.match(await page.locator(".fg-detail-badges").textContent(), /Not simple/);
  await page.keyboard.press("ArrowRight");
  assert.equal(await page.locator("#fg-detail-title").textContent(), "Small example");
  await page.keyboard.press("Escape");
  await page.locator("#fg-reset").click();
  await page.locator("#fg-classification").click();
  await page.locator("#fg-search").fill("dihedral");
  await page.locator(".fg-empty").waitFor();
  await page.getByRole("button", { name: "Search all groups" }).click();
  assert.equal(await page.locator('.fg-tile[data-group-id="fg-dihedral"]').count(), 1);
  assert.deepEqual(errors, []);
  await page.close();

  if (process.env.PREVIEW_URL || process.env.CATALOG_DATA_PATH || process.env.KNOWLPEDIA_SITE_DIR) {
    const actual = await browser.newPage({ viewport: { width: 1440, height: 1100 } });
    const actualErrors = []; actual.on("pageerror", error => actualErrors.push(error.message));
    let base = process.env.PREVIEW_URL?.replace(/\/$/, "") || "https://finite.test";
    let actualData;
    if (!process.env.PREVIEW_URL && process.env.KNOWLPEDIA_SITE_DIR) {
      const site = path.resolve(process.env.KNOWLPEDIA_SITE_DIR);
      actualData = JSON.parse(readFileSync(path.join(site, "indexes/catalog.json"), "utf8"));
      await actual.route("https://finite.test/**", async route => {
        const pathname = decodeURIComponent(new URL(route.request().url()).pathname);
        const filename = path.resolve(site, pathname.replace(/^\/+/, ""), ...(pathname.endsWith("/") ? ["index.html"] : []));
        if (!filename.startsWith(site + path.sep) || !existsSync(filename)) return route.fulfill({ status: 404, body: "Not found" });
        return route.fulfill({ body: readFileSync(filename), contentType: types[path.extname(filename)] || "application/octet-stream" });
      });
    } else if (!process.env.PREVIEW_URL) {
      actualData = JSON.parse(readFileSync(process.env.CATALOG_DATA_PATH, "utf8"));
      await fixtureRoutes(actual, actualData);
    }
    await actual.goto(`${base}/catalog/finite-groups/table/`);
    await actual.locator('[data-finite-groups-ready="true"]').waitFor();
    assert.equal(await actual.evaluate(() => document.characterSet), "UTF-8");
    assert.doesNotMatch(await actual.locator("#fg-status").textContent(), /Â|â€|�/);
    assert.doesNotMatch(await actual.locator("#fg-search").getAttribute("placeholder"), /Â|â€|�/);
    actualData ||= await actual.evaluate(async () => (await fetch("/indexes/catalog.json")).json());
    const finite = actualData.objects.filter(obj => obj.properties?.finite_group);
    assert.equal(await actual.locator('.fg-tile[data-role="simple-family"]').count(), 18);
    assert.equal(await actual.locator('.fg-tile[data-role="sporadic"]').count(), 26);
    assert.equal(await actual.locator('.fg-tile[data-role="tits"]').count(), 1);
    await screenshotLayouts(actual, process.env.LAYOUT_LABEL || "actual");
    assert.equal(await actual.locator(".fg-tile").count(), finite.length);
    for (const obj of finite) {
      await actual.locator(`.fg-tile[data-group-id="${obj.id}"]`).click();
      await actual.locator("#fg-detail[open]").waitFor();
      assert.equal(await actual.locator("#fg-detail-title").textContent(), obj.name);
      assert.equal(await actual.locator("#fg-detail .katex-error").count(), 0, `Mathematics in ${obj.id}`);
      const formulas = await actual.locator(".fg-detail-order .fg-math-display").evaluateAll(nodes => nodes.map(node => {
        const content = node.querySelector(".katex-html");
        node.scrollLeft = 0;
        const left = content.getBoundingClientRect().left - node.getBoundingClientRect().left;
        const wide = node.scrollWidth > node.clientWidth + 1;
        node.scrollLeft = node.scrollWidth;
        const scrollable = node.scrollLeft > 0;
        node.scrollLeft = 0;
        return { left, wide, scrollable };
      }));
      assert.ok(formulas.every(formula => formula.left >= -1 && (!formula.wide || formula.scrollable)), `Long order formulas must start visibly and scroll in ${obj.id}`);
      assert.equal(await actual.locator(".fg-primary-link").getAttribute("href"), `/${obj.knowl}/`);
      assert.equal(await actual.evaluate(() => document.getElementById("fg-detail").scrollWidth > document.getElementById("fg-detail").clientWidth + 1), false, `Detail overflow for ${obj.id}`);
      await actual.keyboard.press("Escape");
    }
    await screenshotSporadics(actual, process.env.LAYOUT_LABEL || "actual");
    await actual.evaluate(() => { document.documentElement.dataset.theme = "dark"; });
    await actual.locator("#fg-classification").click();
    await actual.setViewportSize({ width: 1440, height: 1100 });
    await actual.screenshot({ path: path.join(artifacts, `${process.env.LAYOUT_LABEL || "actual"}-classification-dark.png`) });
    if (process.env.PREVIEW_URL || process.env.KNOWLPEDIA_SITE_DIR) {
      const readerIds = ["catalog/finite-groups", "algebra-groups/classification-finite-simple-groups", "catalog/finite-groups/sporadic/monster", "catalog/finite-groups/sporadic/m24", "catalog/finite-groups/sporadic/fi22", "catalog/finite-groups/sporadic/baby-monster",
        finite.find(obj => obj.id === "fg-psl-n-q").knowl,
        finite.find(obj => obj.properties.finite_group.table_role === "tits").knowl,
        finite.find(obj => obj.id === "fg-cyclic-p").knowl,
        ...["psu-n-q", "finite-orthogonal-derived-group", "omega-odd-n-q", "steinberg-fixed-point-group", "sz-q", "ree-g2-q", "triality-d4-q"].map(id => `catalog/finite-groups/lie-type/${id}`)];
      for (const width of [390, 1440]) {
        await actual.setViewportSize({ width, height: width === 1440 ? 1100 : 844 });
        for (const id of readerIds) {
          await actual.goto(`${base}/${id}/`);
          await actual.evaluate(() => document.fonts.ready);
          assert.equal(await actual.locator("h1").count(), 1, `Reader page ${id}`);
          await actual.locator("details.knowl-section").evaluateAll(nodes => nodes.forEach(node => { node.open = true; }));
          assert.equal(await actual.locator(".katex-error, .math-render-error, .missing-knowl").count(), 0, `Reader math/links in ${id}`);
          assert.equal(await actual.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), false, `Reader overflow at ${width}px in ${id}`);
          const longFormulas = await actual.locator(".math-display").evaluateAll(nodes => nodes.map(node => ({ wide: node.scrollWidth > node.clientWidth + 1, overflow: getComputedStyle(node).overflowX })));
          assert.ok(longFormulas.every(node => !node.wide || ["auto", "scroll"].includes(node.overflow)), `Scrollable reader formulas in ${id}`);
          if (id.includes("/sporadic/")) await actual.screenshot({ path: path.join(artifacts, `${process.env.LAYOUT_LABEL || "actual"}-reader-${id.split("/").at(-1)}-${width}.png`), fullPage: true });
        }
      }
    }
    assert.deepEqual(actualErrors, []);
    await actual.close();
  }
  console.log("Finite-group table passed: both layouts, exact large-order sorting, cluster/Tits separation, search and filters, keyboard details, domains, mobile containment, and screenshots.");
} finally { await browser.close(); }
