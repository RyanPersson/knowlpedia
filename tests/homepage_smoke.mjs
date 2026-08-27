import { chromium } from "playwright";
import { existsSync } from "node:fs";

const baseUrl = process.env.PREVIEW_URL || "http://127.0.0.1:8012";
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH || (existsSync(macChrome) ? macChrome : undefined);
const browser = await chromium.launch({ headless: true, executablePath });

async function hasHorizontalOverflow(page) {
  return page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
}

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  await page.goto(`${baseUrl}/`);

  const heading = page.getByRole("heading", { level: 1 });
  if ((await heading.textContent()) !== "Start with one idea. Follow it anywhere.") {
    throw new Error("Homepage orientation heading is missing");
  }
  if ((await page.locator("body").textContent()).includes("Imported Knowlpedia Content")) {
    throw new Error("Legacy imported-content copy returned to the homepage");
  }
  if ((await page.locator(".subject-card").count()) !== 8) {
    throw new Error("Homepage does not show the eight featured subject gateways");
  }
  if ((await page.locator(".dependency-node").count()) !== 5) {
    throw new Error("Homepage dependency preview is incomplete");
  }
  if (await hasHorizontalOverflow(page)) throw new Error("Desktop homepage overflows horizontally");

  await page.getByRole("button", { name: /Search concepts/ }).click();
  const search = page.getByRole("searchbox", { name: "Search by name, alias, or description" });
  await search.fill("Hilbert space");
  if ((await page.locator(".search-result").first().locator("strong").textContent()) !== "Hilbert space") {
    throw new Error("Homepage search does not rank an exact concept first");
  }
  await search.press("Escape");

  const libraryHref = await page.getByRole("link", { name: "Library", exact: true }).getAttribute("href");
  if (libraryHref !== "/library/") throw new Error("Global navigation does not point to the complete library");

  await page.setViewportSize({ width: 390, height: 844 });
  if (await hasHorizontalOverflow(page)) throw new Error("Mobile homepage overflows horizontally");
  const cardBoxes = await page.locator(".subject-card").evaluateAll((cards) =>
    cards.slice(0, 2).map((card) => {
      const box = card.getBoundingClientRect();
      return { left: box.left, top: box.top };
    })
  );
  if (Math.abs(cardBoxes[0].left - cardBoxes[1].left) > 1 || cardBoxes[1].top <= cardBoxes[0].top) {
    throw new Error("Narrow mobile subject cards are not arranged in one readable column");
  }
  const searchHeight = await page.locator(".home-hero .hero-search").evaluate(
    (button) => button.getBoundingClientRect().height
  );
  if (searchHeight < 44) throw new Error("Mobile homepage search target is too small");

  await page.goto(`${baseUrl}/library/`);
  if (!(await page.getByRole("heading", { name: "The Knowlpedia library" }).isVisible())) {
    throw new Error("Complete library route is unavailable");
  }
  if (!(await page.locator(".index-section").first().isVisible())) {
    throw new Error("Complete library does not contain its subject index");
  }

  console.log("Homepage smoke test passed: orientation copy, search, library navigation, graph preview, and responsive layout.");
} finally {
  await browser.close();
}
