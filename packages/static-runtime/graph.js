(function () {
  "use strict";

  const root = document.querySelector("[data-dependency-graph]");
  if (!root) return;

  const svg = document.getElementById("dependency-map");
  const stage = document.getElementById("graph-stage");
  const edgeLayer = svg.querySelector(".graph-edge-layer");
  const nodeLayer = svg.querySelector(".graph-node-layer");
  const status = document.getElementById("graph-status");
  const search = document.getElementById("graph-search");
  const searchResults = document.getElementById("graph-search-results");
  const depthSelect = document.getElementById("graph-depth");
  const orientationButton = document.getElementById("graph-orientation");
  const fitButton = document.getElementById("graph-fit");
  const mapDescription = document.getElementById("graph-map-description");
  const viewer = document.getElementById("graph-viewer");
  const viewerTitle = document.getElementById("graph-viewer-title");
  const viewerSummary = document.getElementById("graph-viewer-summary");
  const viewerContent = document.getElementById("graph-viewer-content");
  const reviewState = document.getElementById("graph-review-state");
  const viewerClose = document.getElementById("graph-viewer-close");
  const svgNamespace = "http://www.w3.org/2000/svg";
  const maxNodes = 54;
  const nodeWidth = 194;
  const nodeHeight = 48;
  const columnGap = 250;
  const rowGap = 72;

  let nodes = new Map();
  let nodesByHref = new Map();
  let incoming = new Map();
  let outgoing = new Map();
  let allEdges = [];
  let focusId = null;
  let orientation = "horizontal";
  let graphBounds = { x: -400, y: -300, width: 800, height: 600 };
  let viewBox = { ...graphBounds };
  let drag = null;

  function normalize(value) {
    return String(value || "")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase();
  }

  function svgElement(name, attributes = {}) {
    const element = document.createElementNS(svgNamespace, name);
    Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, String(value)));
    return element;
  }

  function domainColor(node) {
    const value = node.id.split("/", 1)[0];
    let hash = 0;
    for (const character of value) hash = (hash * 31 + character.charCodeAt(0)) >>> 0;
    const palette = ["#247a62", "#3f6f97", "#8a5d9f", "#a46632", "#597342", "#9b5961", "#397c86"];
    return palette[hash % palette.length];
  }

  function edgeMapAdd(map, id, edge) {
    if (!map.has(id)) map.set(id, []);
    map.get(id).push(edge);
  }

  function preferredNeighbors(edges, direction, centerDomain) {
    return [...edges].sort((first, second) => {
      const firstNode = nodes.get(first[direction]);
      const secondNode = nodes.get(second[direction]);
      const firstSame = firstNode?.id.split("/", 1)[0] === centerDomain ? 0 : 1;
      const secondSame = secondNode?.id.split("/", 1)[0] === centerDomain ? 0 : 1;
      return firstSame - secondSame || firstNode.title.localeCompare(secondNode.title);
    });
  }

  function useMobileLayout() {
    return window.innerWidth <= 720;
  }

  function useVerticalLayout() {
    return orientation === "vertical";
  }

  function collectNeighborhood(centerId, depth) {
    const center = nodes.get(centerId);
    const centerDomain = center.id.split("/", 1)[0];
    const levels = new Map([[centerId, 0]]);
    let beforeFrontier = [centerId];
    let afterFrontier = [centerId];
    let omitted = 0;

    function expand(frontier, edgeMap, direction, level, cap) {
      const candidates = [];
      const seen = new Set();
      for (const id of frontier) {
        for (const edge of preferredNeighbors(edgeMap.get(id) || [], direction, centerDomain)) {
          const candidateId = edge[direction];
          if (levels.has(candidateId) || seen.has(candidateId)) continue;
          seen.add(candidateId);
          candidates.push(candidateId);
        }
      }
      const available = Math.max(0, maxNodes - levels.size);
      const selected = candidates.slice(0, Math.min(cap, available));
      omitted += Math.max(0, candidates.length - selected.length);
      selected.forEach((id) => levels.set(id, level));
      return selected;
    }

    for (let distance = 1; distance <= depth; distance += 1) {
      const beforeCap = distance === 1 ? 10 : distance === 2 ? 10 : 8;
      const afterCap = distance === 1 ? 12 : distance === 2 ? 12 : 10;
      beforeFrontier = expand(beforeFrontier, incoming, "source", -distance, beforeCap);
      afterFrontier = expand(afterFrontier, outgoing, "target", distance, afterCap);
    }

    const visibleEdges = allEdges.filter((edge) => levels.has(edge.source) && levels.has(edge.target));
    return { levels, visibleEdges, omitted };
  }

  function layout(levels) {
    const columns = new Map();
    levels.forEach((level, id) => {
      if (!columns.has(level)) columns.set(level, []);
      columns.get(level).push(nodes.get(id));
    });
    columns.forEach((items) => items.sort((a, b) => a.title.localeCompare(b.title)));

    const positions = new Map();
    if (useVerticalLayout()) {
      const mobile = useMobileLayout();
      let cursorY = 0;
      let minX = 0;
      let maxX = 0;
      let minY = 0;
      let maxY = 0;
      const orderedLevels = [...columns.keys()].sort((a, b) => b - a);
      for (const level of orderedLevels) {
        const items = columns.get(level);
        const columnsInLayer = Math.min(items.length, mobile ? 2 : 5);
        const rows = Math.ceil(items.length / columnsInLayer);
        items.forEach((node, index) => {
          const row = Math.floor(index / columnsInLayer);
          const column = index % columnsInLayer;
          const horizontalGap = mobile ? 216 : 226;
          const x = (column - (columnsInLayer - 1) / 2) * horizontalGap;
          const y = cursorY + row * rowGap;
          positions.set(node.id, { x, y, level });
          minX = Math.min(minX, x - nodeWidth / 2);
          maxX = Math.max(maxX, x + nodeWidth / 2);
          minY = Math.min(minY, y - nodeHeight / 2);
          maxY = Math.max(maxY, y + nodeHeight / 2);
        });
        cursorY += rows * rowGap + (mobile ? 92 : 110);
      }
      graphBounds = {
        x: minX - (mobile ? 28 : 110),
        y: minY - (mobile ? 72 : 110),
        width: Math.max(mobile ? 440 : 720, maxX - minX + (mobile ? 56 : 220)),
        height: Math.max(mobile ? 520 : 620, maxY - minY + (mobile ? 144 : 220)),
      };
      return positions;
    }

    let minX = 0;
    let maxX = 0;
    let minY = 0;
    let maxY = 0;
    columns.forEach((items, level) => {
      const x = level * columnGap;
      const height = (items.length - 1) * rowGap;
      items.forEach((node, index) => {
        const y = index * rowGap - height / 2;
        positions.set(node.id, { x, y, level });
        minX = Math.min(minX, x - nodeWidth / 2);
        maxX = Math.max(maxX, x + nodeWidth / 2);
        minY = Math.min(minY, y - nodeHeight / 2);
        maxY = Math.max(maxY, y + nodeHeight / 2);
      });
    });
    graphBounds = {
      x: minX - 110,
      y: minY - 100,
      width: Math.max(500, maxX - minX + 220),
      height: Math.max(420, maxY - minY + 200),
    };
    return positions;
  }

  function edgePath(source, target) {
    if (useVerticalLayout()) {
      const direction = target.y >= source.y ? 1 : -1;
      const startY = source.y + direction * nodeHeight / 2;
      const endY = target.y - direction * nodeHeight / 2;
      const bend = Math.max(38, Math.abs(endY - startY) * 0.42);
      return `M ${source.x} ${startY} C ${source.x} ${startY + direction * bend}, ${target.x} ${endY - direction * bend}, ${target.x} ${endY}`;
    }
    const startX = source.x + nodeWidth / 2;
    const endX = target.x - nodeWidth / 2;
    const bend = Math.max(45, Math.abs(endX - startX) * 0.42);
    return `M ${startX} ${source.y} C ${startX + bend} ${source.y}, ${endX - bend} ${target.y}, ${endX} ${target.y}`;
  }

  function truncate(value, limit = 29) {
    return value.length <= limit ? value : value.slice(0, limit - 1).trimEnd() + "…";
  }

  function renderNode(node, position) {
    const link = svgElement("a", { href: node.href, "data-node-id": node.id });
    link.classList.add("map-node");
    if (node.id === focusId) link.classList.add("current");
    link.setAttribute("aria-label", node.title);
    const group = svgElement("g", { transform: `translate(${position.x - nodeWidth / 2} ${position.y - nodeHeight / 2})` });
    const body = svgElement("rect", { width: nodeWidth, height: nodeHeight, rx: 8 });
    const accent = svgElement("rect", { width: 6, height: nodeHeight, rx: 3, fill: domainColor(node) });
    const label = svgElement("text", { x: 18, y: 29 });
    label.textContent = truncate(node.title);
    group.append(body, accent, label);
    if (node.dependency_review_count === 0) {
      const marker = svgElement("circle", { cx: nodeWidth - 13, cy: 12, r: 3 });
      marker.classList.add("node-review-marker");
      group.appendChild(marker);
    }
    link.appendChild(group);
    link.addEventListener("click", (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      selectNode(node.id, true);
    });
    return link;
  }

  function setViewBox(next) {
    viewBox = next;
    svg.setAttribute("viewBox", `${next.x} ${next.y} ${next.width} ${next.height}`);
  }

  function fitGraph() {
    setViewBox({ ...graphBounds });
  }

  function setOrientation(next, updateUrl) {
    orientation = next === "vertical" ? "vertical" : "horizontal";
    root.dataset.graphLayout = orientation;
    const destination = orientation === "horizontal" ? "vertical" : "horizontal";
    orientationButton.textContent = destination[0].toUpperCase() + destination.slice(1);
    orientationButton.setAttribute("aria-label", `Switch to ${destination} layout`);
    mapDescription.textContent = orientation === "vertical"
      ? "Dependents appear above the current concept and prerequisites appear below it."
      : "Prerequisites flow from left to right toward concepts they unlock.";
    if (updateUrl) {
      const url = new URL(window.location.href);
      url.searchParams.set("layout", orientation);
      history.replaceState({ ...(history.state || {}), focus: focusId }, "", url);
    }
  }

  function renderGraph() {
    const depth = Number(depthSelect.value || 2);
    const { levels, visibleEdges, omitted } = collectNeighborhood(focusId, depth);
    const positions = layout(levels);
    edgeLayer.replaceChildren();
    nodeLayer.replaceChildren();

    for (const edge of visibleEdges) {
      const path = svgElement("path", {
        d: edgePath(positions.get(edge.source), positions.get(edge.target)),
        "marker-end": "url(#graph-arrow)",
        "data-edge-source": edge.source,
        "data-edge-target": edge.target,
      });
      path.classList.add("map-edge");
      if (!edge.reviewed) path.classList.add("unreviewed");
      if (edge.source === focusId || edge.target === focusId) path.classList.add("current-edge");
      edgeLayer.appendChild(path);
    }
    for (const [id, position] of positions) nodeLayer.appendChild(renderNode(nodes.get(id), position));

    const omittedMessage = omitted ? ` ${omitted} additional neighbors are hidden; refocus a node to continue.` : "";
    const layoutDescription = orientation === "vertical" ? " Dependents are above; prerequisites are below." : " Prerequisites flow left to right.";
    status.textContent = `Showing ${levels.size} concepts and ${visibleEdges.length} prerequisite links around ${nodes.get(focusId).title}.${layoutDescription}${omittedMessage}`;
    status.classList.add("ready");
    fitGraph();
  }

  async function loadViewer(node, shouldOpen) {
    root.classList.toggle("viewer-hidden", !shouldOpen);
    viewer.classList.toggle("open", shouldOpen);
    viewerTitle.textContent = node.title;
    viewerSummary.textContent = node.summary;
    reviewState.textContent = node.dependency_review_count > 0
      ? `Dependencies reviewed ${node.dependency_review_count} time${node.dependency_review_count === 1 ? "" : "s"}.`
      : "Heuristic dependencies · not yet reviewed";
    reviewState.classList.toggle("reviewed", node.dependency_review_count > 0);
    viewerContent.innerHTML = '<div class="loading" role="status">Loading definition…</div>';
    try {
      const response = await fetch(node.fragment);
      if (!response.ok) throw new Error("fragment unavailable");
      const markup = await response.text();
      const documentFragment = new DOMParser().parseFromString(markup, "text/html");
      const content = documentFragment.querySelector(".knowl-content");
      viewerContent.innerHTML = content ? content.outerHTML : markup;
    } catch (error) {
      viewerContent.innerHTML = `<p class="error">Definition could not be loaded. <a href="${node.href}">Open its full page</a>.</p>`;
    }
  }

  function selectNode(id, pushHistory, openViewer = true) {
    if (!nodes.has(id)) return;
    focusId = id;
    renderGraph();
    loadViewer(nodes.get(id), openViewer);
    if (pushHistory) {
      const url = new URL(window.location.href);
      url.searchParams.set("focus", id);
      history.pushState({ focus: id }, "", url);
    }
  }

  function searchMatches(query) {
    const normalized = normalize(query.trim());
    if (!normalized) return [];
    return [...nodes.values()]
      .map((node) => {
        const title = normalize(node.title);
        const id = normalize(node.id);
        let score = 4;
        if (title === normalized) score = 0;
        else if (title.startsWith(normalized)) score = 1;
        else if (title.includes(normalized)) score = 2;
        else if (id.includes(normalized)) score = 3;
        return { node, score };
      })
      .filter((item) => item.score < 4)
      .sort((a, b) => a.score - b.score || a.node.title.localeCompare(b.node.title))
      .slice(0, 8)
      .map((item) => item.node);
  }

  function renderSearchResults() {
    const matches = searchMatches(search.value);
    searchResults.replaceChildren();
    if (!matches.length) {
      searchResults.hidden = true;
      return;
    }
    for (const node of matches) {
      const button = document.createElement("button");
      button.type = "button";
      button.innerHTML = `<strong></strong><small></small>`;
      button.querySelector("strong").textContent = node.title;
      button.querySelector("small").textContent = node.id.split("/", 1)[0].replaceAll("-", " ");
      button.addEventListener("click", () => {
        search.value = node.title;
        searchResults.hidden = true;
        selectNode(node.id, true);
      });
      searchResults.appendChild(button);
    }
    searchResults.hidden = false;
  }

  function zoomAt(event) {
    event.preventDefault();
    const bounds = svg.getBoundingClientRect();
    const scale = event.deltaY < 0 ? 0.86 : 1.16;
    const pointerX = viewBox.x + ((event.clientX - bounds.left) / bounds.width) * viewBox.width;
    const pointerY = viewBox.y + ((event.clientY - bounds.top) / bounds.height) * viewBox.height;
    const width = Math.min(graphBounds.width * 3, Math.max(260, viewBox.width * scale));
    const height = width * (bounds.height / bounds.width);
    const ratioX = (pointerX - viewBox.x) / viewBox.width;
    const ratioY = (pointerY - viewBox.y) / viewBox.height;
    setViewBox({ x: pointerX - ratioX * width, y: pointerY - ratioY * height, width, height });
  }

  function beginDrag(event) {
    if (event.target.closest(".map-node")) return;
    svg.setPointerCapture(event.pointerId);
    drag = { x: event.clientX, y: event.clientY, viewBox: { ...viewBox } };
    svg.classList.add("dragging");
  }

  function moveDrag(event) {
    if (!drag) return;
    const bounds = svg.getBoundingClientRect();
    const dx = ((event.clientX - drag.x) / bounds.width) * drag.viewBox.width;
    const dy = ((event.clientY - drag.y) / bounds.height) * drag.viewBox.height;
    setViewBox({ ...drag.viewBox, x: drag.viewBox.x - dx, y: drag.viewBox.y - dy });
  }

  function endDrag() {
    drag = null;
    svg.classList.remove("dragging");
  }

  async function initialize() {
    try {
      const response = await fetch("/indexes/dependencies.json");
      if (!response.ok) throw new Error("dependency index unavailable");
      const data = await response.json();
      nodes = new Map(data.nodes.filter((node) => node.visibility === "production").map((node) => [node.id, node]));
      nodesByHref = new Map([...nodes.values()].map((node) => [node.href, node]));
      allEdges = data.edges.filter((edge) => nodes.has(edge.source) && nodes.has(edge.target));
      incoming = new Map();
      outgoing = new Map();
      allEdges.forEach((edge) => {
        edgeMapAdd(incoming, edge.target, edge);
        edgeMapAdd(outgoing, edge.source, edge);
      });
      const parameters = new URL(window.location.href).searchParams;
      const requested = parameters.get("focus");
      const requestedLayout = parameters.get("layout");
      setOrientation(
        requestedLayout === "vertical" || requestedLayout === "horizontal"
          ? requestedLayout
          : (useMobileLayout() ? "vertical" : "horizontal"),
        false,
      );
      const initial = nodes.has(requested) ? requested : root.dataset.defaultFocus;
      if (useMobileLayout()) depthSelect.value = "1";
      selectNode(initial, false, window.innerWidth > 760);
    } catch (error) {
      status.textContent = "The dependency graph could not be loaded.";
      status.classList.add("error");
    }
  }

  search.addEventListener("input", renderSearchResults);
  search.addEventListener("keydown", (event) => {
    if (event.key !== "Enter") return;
    const match = searchMatches(search.value)[0];
    if (match) {
      event.preventDefault();
      searchResults.hidden = true;
      selectNode(match.id, true);
    }
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".graph-find")) searchResults.hidden = true;
  });
  depthSelect.addEventListener("change", renderGraph);
  orientationButton.addEventListener("click", () => {
    setOrientation(orientation === "horizontal" ? "vertical" : "horizontal", true);
    renderGraph();
  });
  fitButton.addEventListener("click", fitGraph);
  viewerClose.addEventListener("click", () => {
    root.classList.add("viewer-hidden");
    viewer.classList.remove("open");
  });
  viewer.addEventListener("click", (event) => {
    const link = event.target.closest("a.knowl[href]");
    if (!link || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const node = nodesByHref.get(new URL(link.href).pathname);
    if (!node) return;
    event.preventDefault();
    event.stopPropagation();
    selectNode(node.id, true);
  }, true);
  svg.addEventListener("wheel", zoomAt, { passive: false });
  svg.addEventListener("pointerdown", beginDrag);
  svg.addEventListener("pointermove", moveDrag);
  svg.addEventListener("pointerup", endDrag);
  svg.addEventListener("pointercancel", endDrag);
  window.addEventListener("popstate", (event) => {
    const parameters = new URL(window.location.href).searchParams;
    const requestedLayout = parameters.get("layout");
    if (requestedLayout === "vertical" || requestedLayout === "horizontal") {
      setOrientation(requestedLayout, false);
    }
    const requested = event.state?.focus || parameters.get("focus");
    if (nodes.has(requested)) selectNode(requested, false);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && viewer.classList.contains("open") && window.innerWidth <= 760) {
      root.classList.add("viewer-hidden");
      viewer.classList.remove("open");
    }
  });

  initialize();
}());
