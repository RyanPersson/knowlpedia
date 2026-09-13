import assert from "node:assert/strict";
import { chromium } from "playwright";

const base = process.env.PREVIEW_URL || "http://127.0.0.1:8015";
const browser = await chromium.launch({ headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  await page.goto(`${base}/`);
  await page.locator("#docs-open").click();
  await page.getByRole("heading", { name: "Understanding Knowlpedia", exact: true }).waitFor();
  await page.locator('.docs-nav a[href="/docs/source-format/"]').click();
  await page.getByRole("heading", { name: "Source format", exact: true }).waitFor();
  await page.locator("#library-open").click();
  await page.getByRole("heading", { name: "Your library", exact: true }).waitFor();
  await page.getByRole("link", { name: "A place to keep reading", exact: true }).click();
  await page.locator('a.knowl[href="/algebra-groups/group/"]').first().click();
  const group = page.locator('.knowl-panel [data-knowl-id="algebra-groups/group"]').first();
  await group.waitFor();
  const nested = group.locator('a.knowl[data-knowl]').first();
  await nested.click();
  await page.waitForFunction(() => document.querySelectorAll('.knowl-panel').length === 2);
  await page.keyboard.press("Escape");
  assert.equal(await page.locator('.knowl-panel').count(), 1);
  await page.screenshot({ path: "tmp/private-library-desktop.png", fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: "tmp/private-library-mobile.png", fullPage: true });
  for (const path of ["/docs/", "/docs/source-format/", "/docs/private-reading/", "/library/"]) {
    await page.goto(`${base}${path}`);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${path} overflows on mobile`);
  }
  for (const width of [320, 390, 720]) {
    await page.setViewportSize({ width, height: 844 });
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `Header overflows at ${width}px`);
    await page.locator("#testing-open").click();
    const bounds = await page.evaluate(() => ({
      headerBottom: document.querySelector(".site-header").getBoundingClientRect().bottom,
      panelTop: document.querySelector("#testing-panel").getBoundingClientRect().top,
    }));
    assert.ok(bounds.panelTop >= bounds.headerBottom, `Testing panel covers header at ${width}px`);
    await page.locator("#testing-close").click();
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(`${base}/docs/`);
  await page.screenshot({ path: "tmp/codebase-docs-mobile.png", fullPage: true });
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.screenshot({ path: "tmp/codebase-docs-desktop.png", fullPage: true });
  assert.deepEqual(errors, []);
  console.log("Docs navigation, private library, nested expansion, and mobile layout passed.");
} finally {
  await browser.close();
}
