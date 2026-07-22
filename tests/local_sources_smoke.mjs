import { chromium } from "playwright";

const baseUrl = process.env.PREVIEW_URL || "http://127.0.0.1:8012";
const browser = await chromium.launch({ headless: true });

try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const response = await page.goto(`${baseUrl}/conjectures/formal-conjectures-corpus/`);
  if (!response?.ok()) throw new Error("The local conjecture corpus index did not load");
  if ((await page.locator("body").getAttribute("data-knowl-preload")) !== "visible") {
    throw new Error("The large corpus index is not using visible lazy preloading");
  }

  const corpusTriggers = page.locator('a.knowl[data-knowl^="/fragments/conjectures/"]');
  if ((await corpusTriggers.count()) !== 1170) {
    throw new Error(`Expected 1,170 corpus knowl triggers, found ${await corpusTriggers.count()}`);
  }
  if ((await page.locator("template[data-knowl-fragment]").count()) !== 0) {
    throw new Error("The corpus index eagerly embedded knowl templates");
  }

  await page.locator("#section.arxiv > summary").click();
  const curlingTrigger = page.getByRole("link", { name: "The Curling Number Conjecture", exact: true });
  await curlingTrigger.click();
  await page.waitForFunction(() =>
    document.querySelector('.knowl-panel [data-knowl-id="conjectures/generated/arxiv/0912-2382/curlingnumberconjecture/arxiv-0912-2382-curling-number-conjecture"]')
  );

  await page.setViewportSize({ width: 390, height: 844 });
  const indexOverflows = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth
  );
  if (indexOverflows) throw new Error("The corpus index overflows at a mobile viewport");

  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(`${baseUrl}/conjectures/hilbert-smith-p-adic/`);
  await page.getByRole("link", { name: "locally compact group", exact: true }).first().click();
  const outer = page.locator('.knowl-panel [data-knowl-id="topology/locally-compact-group"]');
  await outer.waitFor();
  await outer.getByRole("link", { name: "locally compact", exact: true }).click();
  await page.locator('.knowl-panel [data-knowl-id="topology/locally-compact-space"]').waitFor();
  if ((await page.locator(".knowl-panel").count()) !== 2) {
    throw new Error("A catalog page could not open nested knowls from knowlpedia-content");
  }
  await page.keyboard.press("Escape");
  if ((await page.locator(".knowl-panel").count()) !== 1) {
    throw new Error("Escape did not close only the nested cross-repository knowl");
  }

  await page.setViewportSize({ width: 390, height: 844 });
  const curatedOverflows = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth
  );
  if (curatedOverflows) throw new Error("The curated conjecture page overflows at a mobile viewport");
} finally {
  await browser.close();
}
