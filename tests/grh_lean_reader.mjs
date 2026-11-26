import assert from "node:assert/strict";
import { chromium } from "playwright";

const base = process.env.PREVIEW_URL || "http://127.0.0.1:8015";
const browser = await chromium.launch({headless: true, executablePath: process.env.PLAYWRIGHT_CHROME_PATH});
try {
  for (const width of [1280, 390]) {
    const page = await browser.newPage({viewport: {width, height: 850}});
    await page.goto(base + "/grh-lean/", {waitUntil: "domcontentloaded"});
    assert.match(await page.locator("h1").innerText(), /Riemann hypothesis and Dirichlet GRH/);
    await page.locator('main a.knowl[href="/grh-lean/zero-criterion/"]').first().click();
    const criterion = page.locator(".knowl-panel").last();
    await criterion.getByRole("button", {name: "Proof", exact: true}).click();
    await criterion.locator('a.knowl[href="/grh-lean/remainder-transform/"]').first().click();
    await page.locator(".knowl-panel").last().locator('a.knowl[href="/complex-analysis/residue/"]').first().click();
    await page.waitForFunction(() => Array.from(document.querySelectorAll(".knowl-panel"))
      .filter(panel => panel.innerText.trim()).length >= 3);

    await page.goto(base + "/grh-lean/declarations/#source=New.Reduction.MainInequality:87");
    const panel = page.locator("#lean-focus");
    await panel.getByRole("heading", {name: "New.star_inequality", exact: true}).waitFor();
    await panel.getByRole("link", {name: "Comparing the upper and lower covolume bounds"}).waitFor();
    const proofs = panel.locator("summary").filter({hasText: "Proof in the authors’ comments"});
    await proofs.first().click();
    await panel.locator("ol li").first().waitFor();
    const deps = panel.locator("summary").filter({hasText: /^(Direct dependencies|Named source references)/});
    await deps.first().click();
    const child = panel.locator(".lean-children > details").first();
    await child.locator(":scope > summary").click();
    await child.locator(".lean-meta").first().waitFor();

    await page.getByRole("searchbox", {name: "Find a declaration or module"}).fill("integral_forms_long");
    await page.locator('#lean-results a').filter({hasText:"New.Data.integral_forms_long"}).first().click();
    await panel.getByRole("heading", {name: "New.Data.integral_forms_long", exact: true}).waitFor();
    const term = panel.locator(".lean-code .lean-term").first();
    await term.click();
    await panel.locator(".lean-inline .lean-meta").first().waitFor();
    const dimensions = await page.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
    assert.ok(dimensions[0] <= dimensions[1]+1, "Page overflows the viewport");
    await page.close();
  }
  console.log("Recursive mathematical and formal disclosures passed at desktop and phone widths.");
} finally {
  await browser.close();
}
