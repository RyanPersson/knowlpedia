import { chromium } from "playwright";
import { existsSync } from "node:fs";

const baseUrl = process.env.PREVIEW_URL || "http://127.0.0.1:8012";
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH || (existsSync(macChrome) ? macChrome : undefined);
const browser = await chromium.launch({ headless: true, executablePath });

async function assertSectionMatchesOwner(section) {
  const colors = await section.evaluate((element) => {
    const owner = element.closest(".knowl-panel");
    return {
      section: getComputedStyle(element).backgroundColor,
      owner: owner ? getComputedStyle(owner).backgroundColor : null,
    };
  });
  if (colors.section !== colors.owner) {
    throw new Error(
      `Inline section background ${colors.section} does not match its owning knowl ${colors.owner}`
    );
  }
}

async function assertTrunkAlternation(page, firstPanel, secondPanel, theme) {
  const activeTheme = await page.locator("html").getAttribute("data-theme");
  if (activeTheme !== theme) await page.locator("#theme-toggle").click();
  const colors = {
    page: await page.locator("body").evaluate((element) => getComputedStyle(element).backgroundColor),
    first: await firstPanel.evaluate((element) => getComputedStyle(element).backgroundColor),
    second: await secondPanel.evaluate((element) => getComputedStyle(element).backgroundColor),
  };
  if (colors.page === colors.first) {
    throw new Error(`${theme} theme repeats the page background on the first embedded knowl`);
  }
  if (colors.second !== colors.page) {
    throw new Error(
      `${theme} theme nested knowl ${colors.second} does not continue the page trunk color ${colors.page}`
    );
  }
  return colors;
}

function contrastRatio(first, second) {
  const channels = (color) => color.match(/[\d.]+/g).slice(0, 3).map(Number);
  const luminance = (color) => {
    const linear = channels(color).map((value) => {
      const normalized = value / 255;
      return normalized <= 0.04045 ? normalized / 12.92 : ((normalized + 0.055) / 1.055) ** 2.4;
    });
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2];
  };
  const a = luminance(first);
  const b = luminance(second);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}

try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  await page.goto(`${baseUrl}/algebraic-geometry-foundations/g-torsor-on-a-site/`);

  await page.getByRole("button", { name: /Search/ }).click();
  const search = page.getByRole("searchbox", { name: "Search by name, alias, or description" });
  await search.fill("etale topology");
  const firstResult = page.locator(".search-result").first();
  if ((await firstResult.locator("strong").textContent()) !== "Étale topology") {
    throw new Error("Search did not rank Étale topology first");
  }
  await search.press("Escape");
  if ((await page.evaluate(() => document.activeElement?.id)) !== "search-open") {
    throw new Error("Closing search did not restore focus to its trigger");
  }

  await page.getByRole("link", { name: "schemes", exact: true }).click();
  const panel = page.locator(".knowl-panel");
  await panel.getByRole("button", { name: "Examples", exact: true }).click();
  await page.waitForFunction(() =>
    document.querySelector(".knowl-inline-section")?.textContent?.includes("Every affine scheme")
  );
  await assertSectionMatchesOwner(panel.locator(".knowl-inline-section"));

  await panel.getByRole("link", { name: "affine scheme", exact: true }).click();
  if ((await page.locator(".knowl-panel").count()) !== 2) {
    throw new Error("Nested knowl did not open inside its parent");
  }
  await page.keyboard.press("Escape");
  if ((await page.locator(".knowl-panel").count()) !== 1) {
    throw new Error("Escape did not close only the deepest knowl");
  }

  await page.setViewportSize({ width: 390, height: 844 });
  const overflows = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  if (overflows) throw new Error("The knowl page overflows at a mobile viewport");
  const closeHeight = await panel.getByRole("button", { name: /Collapse Scheme/i }).first().evaluate(
    (button) => button.getBoundingClientRect().height
  );
  if (closeHeight < 44) throw new Error("Mobile close target is smaller than 44 pixels");
  const pageLinkBox = await panel.getByRole("link", { name: /Open Scheme as a full page/i }).first().evaluate(
    (link) => ({ width: link.getBoundingClientRect().width, height: link.getBoundingClientRect().height })
  );
  if (pageLinkBox.width < 44 || pageLinkBox.height < 44) {
    throw new Error("Mobile full-page target is smaller than 44 pixels");
  }

  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(`${baseUrl}/shared-foundations/real-numbers/`);
  await page.getByRole("link", { name: "rational numbers", exact: true }).first().click();
  const rationalPanel = page.locator(".knowl-panel").first();
  await rationalPanel.getByRole("button", { name: "Remarks", exact: true }).click();
  await assertSectionMatchesOwner(
    rationalPanel.locator(":scope > .knowl-content > .knowl-section-slot > .knowl-inline-section")
  );

  await rationalPanel.getByRole("link", { name: "real numbers", exact: true }).click();
  const nestedRealPanel = rationalPanel.locator(".knowl-panel").first();
  await nestedRealPanel.getByRole("button", { name: "Examples", exact: true }).click();
  await assertSectionMatchesOwner(
    nestedRealPanel.locator(":scope > .knowl-content > .knowl-section-slot > .knowl-inline-section")
  );

  const testingTrigger = page.getByRole("button", { name: "Testing" });
  await testingTrigger.click();
  const testingPanel = page.getByRole("dialog", { name: "Test site styles" });
  const paletteOptions = testingPanel.locator(".palette-option");
  if ((await paletteOptions.count()) !== 5) throw new Error("Testing panel does not expose all five palettes");

  const palettes = ["current", "original", "washi", "sumi", "aizome"];
  const signatures = { light: new Set(), dark: new Set() };
  for (const palette of palettes) {
    await testingPanel.locator(`[data-palette-value="${palette}"]`).click();
    if ((await page.locator("html").getAttribute("data-palette")) !== palette) {
      throw new Error(`Palette button did not apply ${palette}`);
    }
    for (const theme of ["light", "dark"]) {
      const colors = await assertTrunkAlternation(page, rationalPanel, nestedRealPanel, theme);
      signatures[theme].add(`${colors.page}|${colors.first}`);
      const contrast = contrastRatio(colors.page, colors.first);
      const minimumContrast = theme === "light" ? 1.06 : 1.12;
      if (!["current", "original"].includes(palette) && contrast < minimumContrast) {
        throw new Error(`${palette} ${theme} backgrounds do not have enough visual separation`);
      }
      if (!["current", "original"].includes(palette) && theme === "light" && contrast > 1.13) {
        throw new Error(`${palette} light backgrounds have more separation than the experimental target`);
      }
      await assertSectionMatchesOwner(
        rationalPanel.locator(":scope > .knowl-content > .knowl-section-slot > .knowl-inline-section")
      );
      await assertSectionMatchesOwner(
        nestedRealPanel.locator(":scope > .knowl-content > .knowl-section-slot > .knowl-inline-section")
      );
    }
  }
  if (signatures.light.size !== palettes.length || signatures.dark.size !== palettes.length) {
    throw new Error("The palette choices do not produce five distinct light and dark background pairs");
  }

  await testingPanel.locator('[data-palette-value="washi"]').click();
  await page.keyboard.press("Escape");
  if (await testingPanel.isVisible()) throw new Error("Escape did not close the testing panel");
  if ((await page.evaluate(() => document.activeElement?.id)) !== "testing-open") {
    throw new Error("Closing the testing panel did not restore focus to its trigger");
  }
  await page.reload();
  if ((await page.locator("html").getAttribute("data-palette")) !== "washi") {
    throw new Error("The selected palette did not persist across a reload");
  }

  console.log("Runtime smoke test passed: search, five persistent light/dark palettes, contrasting trunk backgrounds, nested sections, matching section backgrounds, focus, Escape, and mobile layout.");
} finally {
  await browser.close();
}
