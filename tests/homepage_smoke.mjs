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

  if ((await page.getByRole("heading", { level: 1 }).textContent()) !== "Knowlpedia") {
    throw new Error("Homepage entry heading is missing");
  }
  if ((await page.locator("body").textContent()).includes("Imported Knowlpedia Content")) {
    throw new Error("Legacy imported-content copy returned to the homepage");
  }
  if ((await page.locator(".start-actions > a").count()) !== 2) {
    throw new Error("Homepage does not expose graph and library entry points");
  }
  if ((await page.locator(".start-subjects li").count()) < 20) {
    throw new Error("Homepage subject directory is unexpectedly incomplete");
  }
  if (await hasHorizontalOverflow(page)) throw new Error("Desktop homepage overflows horizontally");

  await page.getByRole("button", { name: /Search the mathematical library/ }).click();
  const search = page.getByRole("searchbox", { name: "Search by name, alias, or description" });
  await search.fill("Hilbert space");
  if ((await page.locator(".search-result").first().locator("strong").textContent()) !== "Hilbert space") {
    throw new Error("Homepage search does not rank an exact concept first");
  }
  await search.press("Escape");

  const graphHref = await page.getByRole("link", { name: /Dependency graph/ }).getAttribute("href");
  const indexHref = await page.getByRole("link", { name: /Complete index/ }).getAttribute("href");
  if (graphHref !== "/graph/" || indexHref !== "/index/") {
    throw new Error("Homepage entry points target the wrong routes");
  }
  const desktopActionHeights = await page.locator(".start-actions > a").evaluateAll((items) =>
    items.map((item) => item.getBoundingClientRect().height)
  );
  if (desktopActionHeights.some((height) => height > 52)) {
    throw new Error("Homepage entry actions have expanded into oversized cards");
  }
  const desktopHeadingSize = await page.getByRole("heading", { level: 1 }).evaluate((heading) =>
    Number.parseFloat(getComputedStyle(heading).fontSize)
  );
  if (desktopHeadingSize > 32) throw new Error("Desktop homepage heading is oversized");
  if ((await page.locator(".start-subjects").evaluate((section) => section.getBoundingClientRect().top)) > 650) {
    throw new Error("Homepage subjects do not begin in the first desktop viewport");
  }

  await page.setViewportSize({ width: 390, height: 844 });
  if (await hasHorizontalOverflow(page)) throw new Error("Mobile homepage overflows horizontally");
  const actionBoxes = await page.locator(".start-actions > a").evaluateAll((items) =>
    items.map((item) => {
      const box = item.getBoundingClientRect();
      return { left: box.left, top: box.top };
    })
  );
  if (Math.abs(actionBoxes[0].top - actionBoxes[1].top) > 1 || actionBoxes[1].left <= actionBoxes[0].left) {
    throw new Error("Mobile entry actions are not compact and side by side");
  }
  if ((await page.locator(".start-search").evaluate((button) => button.getBoundingClientRect().height)) < 44) {
    throw new Error("Mobile homepage search target is too small");
  }

  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto(`${baseUrl}/index/`);
  if (!(await page.getByRole("heading", { name: /Browse all .* knowls by subject/ }).isVisible())) {
    throw new Error("Complete index route is unavailable");
  }
  if ((await page.locator(".index-hero .hero-search").count()) !== 0) {
    throw new Error("Index page repeats the global concept search control");
  }
  if (!(await page.locator("#search-open").isVisible())) {
    throw new Error("Index page removed the requested header search control");
  }
  if ((await page.locator(".library-breadcrumb, .index-intro, .index-hero .kind").count()) !== 0) {
    throw new Error("Index page restored redundant identity or browse copy");
  }
  if (!(await page.locator(".index-section").first().isVisible())) {
    throw new Error("Complete index does not contain its subject directory");
  }

  const indexText = await page.locator("main").textContent();
  if (!indexText.includes("Mathematical knowledge, connected") || !indexText.includes("Open a definition without losing your place")) {
    throw new Error("Index orientation copy is missing");
  }
  if (indexText.includes("production knowls")) throw new Error("Reader-facing index exposes build-profile terminology");
  for (const subject of ["knowlification", "posts", "search"]) {
    if ((await page.locator(`#subject-${subject}`).count()) !== 0) throw new Error(`Meta subject ${subject} leaked into the index`);
  }

  await page.locator("#subject-filter").fill("differential");
  const visibleSubjectNames = await page.locator(".index-section:visible > summary > span:first-child").allTextContents();
  if (!visibleSubjectNames.length || visibleSubjectNames.some((name) => !name.toLowerCase().includes("differential"))) {
    throw new Error("Subject filter does not restrict the index by subject name");
  }

  const desktopSearchWidth = await page.locator("#search-open").evaluate((button) => button.getBoundingClientRect().width);
  const desktopIconSize = await page.locator("#search-open .header-action-icon").evaluate((icon) => Number.parseFloat(getComputedStyle(icon).fontSize));
  if (desktopSearchWidth < 160 || desktopIconSize < 18) throw new Error("Desktop header search control is too cramped");

  await page.setViewportSize({ width: 390, height: 844 });
  if (await hasHorizontalOverflow(page)) throw new Error("Mobile index header overflows horizontally");
  const mobileSearchWidth = await page.locator("#search-open").evaluate((button) => button.getBoundingClientRect().width);
  const mobileIconSize = await page.locator("#theme-toggle .header-action-icon").evaluate((icon) => Number.parseFloat(getComputedStyle(icon).fontSize));
  if (mobileSearchWidth < 58 || mobileIconSize < 19) throw new Error("Mobile header controls are too small");

  console.log("Homepage smoke test passed: search, graph/index entry points, subject filter, and responsive layout.");
} finally {
  await browser.close();
}
