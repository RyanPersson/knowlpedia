import { chromium } from "playwright";
import { existsSync } from "node:fs";

const baseUrl = process.env.PREVIEW_URL || "http://127.0.0.1:8012";
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH || (existsSync(macChrome) ? macChrome : undefined);
const browser = await chromium.launch({ headless: true, executablePath });

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
  const closeHeight = await panel.getByRole("button", { name: "Close", exact: true }).first().evaluate(
    (button) => button.getBoundingClientRect().height
  );
  if (closeHeight < 44) throw new Error("Mobile close target is smaller than 44 pixels");

  console.log("Runtime smoke test passed: search, nested sections, focus, Escape, and mobile layout.");
} finally {
  await browser.close();
}
