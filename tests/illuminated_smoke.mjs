import assert from "node:assert/strict";
import { mkdirSync, existsSync } from "node:fs";
import { chromium } from "playwright";

const baseUrl = process.env.PREVIEW_URL || "http://127.0.0.1:8001";
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH || (existsSync(macChrome) ? macChrome : undefined);
const browser = await chromium.launch({ headless: true, executablePath });

function contrast(a, b) {
  const luminance = (color) => color.match(/[\d.]+/g).slice(0, 3).map(Number)
    .map((v) => v / 255).map((v) => v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4)
    .reduce((sum, v, i) => sum + v * [0.2126, 0.7152, 0.0722][i], 0);
  const x = luminance(a), y = luminance(b);
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
}

async function verifyReading(page, label) {
  const metrics = await page.evaluate(() => {
    const style = getComputedStyle(document.documentElement);
    const color = (variable) => {
      const swatch = document.createElement("span");
      swatch.style.color = style.getPropertyValue(variable);
      document.body.append(swatch);
      const result = getComputedStyle(swatch).color;
      swatch.remove();
      return result;
    };
    return {
      overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      colors: Object.fromEntries(["--ink", "--muted", "--quiet", "--link", "--accent-strong", "--canvas", "--surface-subtle"].map((key) => [key, color(key)])),
      math: document.querySelectorAll(".katex").length,
    };
  });
  assert.equal(metrics.overflow, false, `${label}: page overflows horizontally`);
  assert.ok(metrics.math > 0, `${label}: mathematical typesetting is absent`);
  for (const text of ["--ink", "--muted", "--quiet", "--link", "--accent-strong"]) {
    for (const background of ["--canvas", "--surface-subtle"]) {
      assert.ok(contrast(metrics.colors[text], metrics.colors[background]) >= 4.5,
        `${label}: ${text} on ${background} does not meet 4.5:1 contrast`);
    }
  }
}

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 } });
  const errors = [];
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(`${baseUrl}/illuminated/`);
  assert.equal(await page.locator("html").getAttribute("data-palette"), "vellum");
  const choices = page.getByRole("radiogroup", { name: "Illuminated edition" });

  for (const [palette, signatureTheme] of [["vellum", "light"], ["lapis", "dark"], ["black-hours", "dark"]]) {
    await choices.locator(`[data-palette-value="${palette}"]`).click();
    assert.equal(await page.locator("html").getAttribute("data-manuscript"), palette);
    assert.equal(await page.locator("html").getAttribute("data-theme"), signatureTheme);
    assert.equal(await choices.locator('[aria-checked="true"]').count(), 1);
    await page.reload();
    assert.equal(await page.locator("html").getAttribute("data-palette"), palette);

    for (const theme of ["light", "dark"]) {
      if (await page.locator("html").getAttribute("data-theme") !== theme) await page.locator("#theme-toggle").click();
      await verifyReading(page, `${palette}/${theme}/desktop`);
      const trigger = page.locator("#specimen-i").getByRole("link", { name: "binary operation", exact: true });
      await trigger.click();
      const panel = page.locator("#specimen-i > .core-section > .knowl-panel").first();
      await panel.waitFor({ state: "visible" });
      await panel.locator(".knowl-body a.knowl").first().click();
      await panel.locator(".knowl-panel").waitFor({ state: "visible" });
      await page.setViewportSize({ width: 390, height: 844 });
      await verifyReading(page, `${palette}/${theme}/mobile-expanded`);
      await page.keyboard.press("Escape");
      assert.equal(await panel.locator(".knowl-panel").count(), 0);
      await page.keyboard.press("Escape");
      assert.equal(await page.locator("#specimen-i .knowl-panel").count(), 0);
      await page.setViewportSize({ width: 1440, height: 1100 });
    }

    if (await page.locator("html").getAttribute("data-theme") !== signatureTheme) await page.locator("#theme-toggle").click();
    if (process.env.SCREENSHOT_DIR) {
      mkdirSync(process.env.SCREENSHOT_DIR, { recursive: true });
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.screenshot({ path: `${process.env.SCREENSHOT_DIR}/${palette}.png` });
    }
    await page.locator("#specimen-i .edition-read-link").click();
    assert.equal(await page.locator("html").getAttribute("data-palette"), palette, "Edition did not follow the reader to a real page");
    await verifyReading(page, `${palette}/standalone`);
    await page.goto(`${baseUrl}/illuminated/`);
  }

  await choices.locator('[data-palette-value="vellum"]').click();
  await choices.locator('[data-palette-value="vellum"]').press("ArrowRight");
  assert.equal(await page.locator("html").getAttribute("data-palette"), "lapis", "Radio arrow navigation failed");
  await page.locator("#theme-toggle").click();
  await page.reload();
  assert.equal(await page.locator("html").getAttribute("data-theme"), "light", "URL overrides the chosen reading mode after reload");
  await page.emulateMedia({ media: "print" });
  assert.equal(await choices.isVisible(), false, "Edition picker is printed");
  assert.equal(await page.locator("body").evaluate((element) => getComputedStyle(element).backgroundColor), "rgb(255, 255, 255)");
  assert.deepEqual(errors, []);

  const restricted = await browser.newPage();
  await restricted.addInitScript(() => {
    Object.defineProperty(Storage.prototype, "getItem", { value() { throw new Error("Storage unavailable"); } });
    Object.defineProperty(Storage.prototype, "setItem", { value() { throw new Error("Storage unavailable"); } });
  });
  await restricted.goto(`${baseUrl}/illuminated/?palette=lapis&theme=dark`);
  assert.equal(await restricted.locator("html").getAttribute("data-manuscript"), "lapis");
  for (const expected of ["light", "dark"]) {
    await restricted.locator("#theme-toggle").click();
    assert.equal(await restricted.locator("html").getAttribute("data-theme"), expected);
  }
  await restricted.reload();
  assert.equal(await restricted.locator("html").getAttribute("data-theme"), "dark");
  console.log("Illuminated smoke passed: three editions in both modes, text contrast, nested knowls, mobile overflow, persistence, keyboard controls, print, and unavailable storage.");
} finally {
  await browser.close();
}
