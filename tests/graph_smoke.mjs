import { chromium } from "playwright";
import { existsSync } from "node:fs";

const baseUrl = process.env.PREVIEW_URL || "http://127.0.0.1:8012";
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const executablePath = process.env.PLAYWRIGHT_CHROME_PATH || (existsSync(macChrome) ? macChrome : undefined);
const browser = await chromium.launch({ headless: true, executablePath });

async function nodeCenter(locator) {
  return locator.evaluate((node) => {
    const box = node.getBoundingClientRect();
    return { x: box.left + box.width / 2, y: box.top + box.height / 2 };
  });
}

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 960 } });
  await page.goto(`${baseUrl}/graph/`);
  await page.locator(".map-node").first().waitFor();
  await page.locator("#graph-viewer-content .knowl-content").waitFor();

  const reviewFilter = page.locator("#graph-review-filter");
  await reviewFilter.waitFor();
  // A completed corpus may have no unreviewed edges. Exercise filtering on
  // a deterministic three-node graph, then resume checks on the real index.
  const mixedFocus = "algebra-rings/ring";
  await page.route("**/indexes/dependencies.json", async route => {
    const response = await route.fetch();
    const data = await response.json();
    const ids = new Set([mixedFocus, "algebra-rings/unital-ring", "algebra-rings/commutative-ring"]);
    data.nodes = data.nodes.filter(node => ids.has(node.id));
    data.edges = [
      {source: mixedFocus, target: "algebra-rings/unital-ring", reviewed: true},
      {source: mixedFocus, target: "algebra-rings/commutative-ring", reviewed: false},
    ];
    await route.fulfill({response, json: data});
  });
  await page.goto(`${baseUrl}/graph/?focus=${encodeURIComponent(mixedFocus)}`);
  await page.locator(".map-node.current").waitFor();
  const unreviewedEdges = await page.locator(".map-edge.unreviewed").count();
  if (!unreviewedEdges) throw new Error("The test neighborhood has no displayed unreviewed edges");
  await reviewFilter.check();
  if (new URL(page.url()).searchParams.get("review") !== "reviewed") throw new Error("Reviewed-only filter is not reflected in the URL");
  // A node may remain reachable through a reviewed path after its unreviewed
  // edge disappears. Filtering need not reduce the number of visible nodes.
  if (await page.locator(".map-edge.unreviewed").count()) throw new Error("Reviewed-only mode retained unreviewed edges");
  if (!(await page.locator(".map-edge").count())) throw new Error("Reviewed-only mode lost the reviewed links");
  if (!(await page.locator(`.map-node.current[data-node-id="${mixedFocus}"]`).count())) throw new Error("Reviewed-only mode lost the focused node");
  if (!/reviewed-only mode hides/i.test(await page.locator("#graph-status").textContent())) throw new Error("Reviewed-only empty/filter state is not explained");
  await page.goBack();
  await page.waitForFunction(() => !new URL(location.href).searchParams.has("review"));
  if (await reviewFilter.isChecked()) throw new Error("Back navigation did not restore all-edge mode");
  await page.goForward();
  await page.waitForFunction(() => new URL(location.href).searchParams.get("review") === "reviewed");
  if (!(await reviewFilter.isChecked())) throw new Error("Forward navigation did not restore reviewed-only mode");
  await page.unroute("**/indexes/dependencies.json");
  await page.goto(`${baseUrl}/graph/`);
  await page.locator(".map-node.current").waitFor();

  const nodeCount = await page.locator(".map-node").count();
  if (nodeCount < 2 || nodeCount > 84) throw new Error(`Focused graph has an invalid node count: ${nodeCount}`);
  if (!(await page.locator(".map-node.current").isVisible())) throw new Error("Current concept is not highlighted");
  if ((await page.locator(".map-edge").count()) < 1) throw new Error("Dependency edges are missing");
  if (!(await page.locator("#graph-viewer").isVisible())) throw new Error("Desktop knowl viewer is not visible");
  if ((await page.locator("[data-dependency-graph]").getAttribute("data-graph-layout")) !== "horizontal") {
    throw new Error("Desktop graph does not start in horizontal layout");
  }

  await page.getByRole("button", { name: "Switch to vertical layout" }).click();
  await page.waitForFunction(() => document.querySelector("[data-dependency-graph]")?.dataset.graphLayout === "vertical");
  if (new URL(page.url()).searchParams.get("layout") !== "vertical") {
    throw new Error("Vertical graph orientation is not reflected in the URL");
  }
  const currentId = await page.locator(".map-node.current").getAttribute("data-node-id");
  const incomingEdge = page.locator(`.map-edge[data-edge-target="${currentId}"]`).first();
  const outgoingEdge = page.locator(`.map-edge[data-edge-source="${currentId}"]`).first();
  const prerequisiteId = await incomingEdge.getAttribute("data-edge-source");
  const dependentId = await outgoingEdge.getAttribute("data-edge-target");
  if (!prerequisiteId || !dependentId) throw new Error("Default graph focus cannot verify both vertical directions");
  const currentCenter = await nodeCenter(page.locator(`.map-node[data-node-id="${currentId}"]`));
  const prerequisiteCenter = await nodeCenter(page.locator(`.map-node[data-node-id="${prerequisiteId}"]`));
  const dependentCenter = await nodeCenter(page.locator(`.map-node[data-node-id="${dependentId}"]`));
  if (prerequisiteCenter.y <= currentCenter.y || dependentCenter.y >= currentCenter.y) {
    throw new Error("Vertical graph must put prerequisites below and dependents above the current concept");
  }

  await page.locator(`.map-node[data-node-id="${prerequisiteId}"]`).click();
  await page.waitForFunction(() => new URL(location.href).searchParams.has("focus"));
  if (!(await page.locator("#graph-viewer-title").textContent())) throw new Error("Node selection did not update the viewer");

  await page.getByLabel("Find a concept").fill("Hilbert space");
  const result = page.locator("#graph-search-results button").first();
  await result.waitFor();
  if ((await result.locator("strong").textContent()) !== "Hilbert space") {
    throw new Error("Graph search does not rank the exact concept first");
  }
  await result.click();
  if ((await page.locator("#graph-viewer-title").textContent()) !== "Hilbert space") {
    throw new Error("Graph search did not focus the selected concept");
  }

  const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await mobile.goto(`${baseUrl}/graph/`);
  await mobile.locator(".map-node").first().waitFor();
  if ((await mobile.locator("[data-dependency-graph]").getAttribute("data-graph-layout")) !== "vertical") {
    throw new Error("Mobile graph does not start in vertical layout");
  }
  if (!(await mobile.getByRole("button", { name: "Switch to horizontal layout" }).isVisible())) {
    throw new Error("Mobile graph orientation control is unavailable");
  }
  if (await mobile.locator("#graph-viewer").evaluate((viewer) => viewer.classList.contains("open"))) {
    throw new Error("Mobile knowl sheet opens before a node is selected");
  }
  await mobile.locator(".map-node").first().click();
  await mobile.locator("#graph-viewer.open").waitFor();
  await mobile.locator("#graph-viewer-content .knowl-content").waitFor();
  await mobile.getByRole("button", { name: "Close knowl viewer" }).click();
  if (await mobile.locator("#graph-viewer").evaluate((viewer) => viewer.classList.contains("open"))) {
    throw new Error("Mobile knowl sheet did not close");
  }
  await mobile.close();

  console.log("Graph smoke test passed: focused neighborhood, search, selection, desktop viewer, and mobile sheet.");
} finally {
  await browser.close();
}
