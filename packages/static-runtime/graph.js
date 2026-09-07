/* Shared, deterministic graph operations; also exercised directly by Node tests. */
const GraphModel = (() => {
  function rank(ids, edges) {
    const degree = new Map([...ids].sort().map(id => [id, 0]));
    const next = new Map([...degree.keys()].map(id => [id, new Set()]));
    for (const {source, target} of edges) {
      if (!degree.has(source) || !degree.has(target) || next.get(source).has(target)) continue;
      next.get(source).add(target);
      degree.set(target, degree.get(target) + 1);
    }
    const queue = [...degree.keys()].filter(id => degree.get(id) === 0);
    const levels = new Map(queue.map(id => [id, 0]));
    for (let i = 0; i < queue.length; i++) {
      const id = queue[i];
      for (const target of next.get(id)) {
        levels.set(target, Math.max(levels.get(target) || 0, levels.get(id) + 1));
        degree.set(target, degree.get(target) - 1);
        if (degree.get(target) === 0) queue.push(target);
      }
    }
    if (queue.length !== degree.size) throw new Error("The dependency index contains a cycle. Rebuild it after correcting the prerequisite metadata.");
    return levels;
  }

  function clusters(nodes, edges, mode) {
    const groups = new Map();
    if (mode === "subjects") {
      for (const node of nodes.values()) {
        const key = node.id.split("/")[0];
        if (!groups.has(key)) groups.set(key, new Set());
        groups.get(key).add(node.id);
      }
    } else {
      const neighbors = new Map([...nodes.keys()].map(id => [id, []]));
      for (const {source, target} of edges) {
        neighbors.get(source).push(target);
        neighbors.get(target).push(source);
      }
      const seen = new Set();
      for (const id of [...nodes.keys()].sort()) {
        if (seen.has(id)) continue;
        const members = new Set([id]);
        seen.add(id);
        const queue = [id];
        for (let i = 0; i < queue.length; i++) {
          for (const neighbor of neighbors.get(queue[i])) {
            if (seen.has(neighbor)) continue;
            seen.add(neighbor); members.add(neighbor); queue.push(neighbor);
          }
        }
        groups.set(id, members);
      }
    }
    const result = [...groups].map(([id, members]) => ({
      id, members,
      title: mode === "subjects" ? id.replaceAll("-", " ") : members.size === 1 ? nodes.get(id).title : `Component containing ${nodes.get(id).title}`,
      edges: 0,
    }));
    const owner = new Map();
    result.forEach(group => group.members.forEach(id => owner.set(id, group)));
    edges.forEach(edge => { if (owner.get(edge.source) === owner.get(edge.target)) owner.get(edge.source).edges++; });
    return result.sort((a, b) => b.members.size - a.members.size || a.title.localeCompare(b.title));
  }
  return {rank, clusters};
})();
if (typeof module !== "undefined") module.exports = GraphModel;

(function () {
  "use strict";

  if (typeof document === "undefined") return;
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
  const showDependents = document.getElementById("graph-show-dependents");
  const reviewFilter = document.getElementById("graph-review-filter");
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
  const viewSelect = document.getElementById("graph-view");
  const clusterPanel = document.getElementById("graph-clusters");
  const catalogControl = document.getElementById("graph-catalog-control");
  const showCatalog = document.getElementById("graph-show-catalog");
  const organizationalControl = document.getElementById("graph-organizational-control");
  const showOrganizational = document.getElementById("graph-show-organizational");
  const organizationalKinds = new Set(["page", "document", "section", "index"]);
  let graphData = null;
  const clusterBack = document.getElementById("graph-cluster-back");
  const controls = [...root.querySelectorAll(".graph-toolbar input, .graph-toolbar select, .graph-toolbar button, .graph-zoom button")];
  controls.forEach(control => { control.disabled = true; });
  const maxNodes = 600;
  const nodeWidth = 176;
  const nodeHeight = 56;
  const columnGap = 216;
  const rowGap = 80;

  let nodes = new Map();
  let nodesByHref = new Map();
  let incoming = new Map();
  let outgoing = new Map();
  let allEdges = [];
  let focusId = null;
  let orientation = "horizontal";
  let reviewMode = "all";
  let graphBounds = { x: -400, y: -300, width: 800, height: 600 };
  let viewBox = { ...graphBounds };
  let drag = null;
  let mode = "neighborhood";
  let clusterId = null;
  let clusterGroups = [];
  let viewerRequest = 0;
  let initialFocus = null;

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
    const nodeBudget = Math.min(maxNodes, 42 + 12 * Math.max(0, depth - 3));
    const center = nodes.get(centerId);
    const centerDomain = center.id.split("/", 1)[0];
    const levels = new Map([[centerId, 0]]);
    let beforeFrontier = [centerId];
    let afterFrontier = [centerId];
    const visibleGraphEdges = reviewMode === "reviewed"
      ? allEdges.filter((edge) => edge.reviewed)
      : allEdges;
    const visibleIncoming = new Map();
    const visibleOutgoing = new Map();
    visibleGraphEdges.forEach((edge) => {
      edgeMapAdd(visibleIncoming, edge.target, edge);
      edgeMapAdd(visibleOutgoing, edge.source, edge);
    });
    const hidden = new Set();
    const activeCluster = clusterGroups.find(group => group.id === clusterId);
    const allowed = activeCluster?.members;

    function expand(frontier, edgeMap, direction, level, cap) {
      const candidates = [];
      const seen = new Set();
      for (const id of frontier) {
        for (const edge of preferredNeighbors(edgeMap.get(id) || [], direction, centerDomain)) {
          const candidateId = edge[direction];
          if (levels.has(candidateId) || seen.has(candidateId)) continue;
          if (allowed && !allowed.has(candidateId)) { hidden.add(candidateId); continue; }
          seen.add(candidateId);
          candidates.push(candidateId);
        }
      }
      const available = Math.max(0, nodeBudget - levels.size);
      const selected = candidates.slice(0, Math.min(cap, available));
      candidates.slice(selected.length).forEach(id => hidden.add(id));
      selected.forEach((id) => levels.set(id, level));
      return selected;
    }

    for (let distance = 1; distance <= depth; distance += 1) {
      const beforeCap = useMobileLayout() ? 3 : distance === 1 ? 6 : 5;
      const afterCap = useMobileLayout() ? 3 : distance === 1 ? 7 : 6;
      beforeFrontier = expand(beforeFrontier, visibleIncoming, "source", -distance, beforeCap);
      if (showDependents.checked) afterFrontier = expand(afterFrontier, visibleOutgoing, "target", distance, afterCap);
    }

    const visibleEdges = visibleGraphEdges.filter((edge) => levels.has(edge.source) && levels.has(edge.target));
    const orderedLevels = GraphModel.rank(levels.keys(), visibleEdges);
    const centerLevel = orderedLevels.get(centerId);
    orderedLevels.forEach((level, id) => orderedLevels.set(id, level - centerLevel));
    levels.forEach((_, id) => hidden.delete(id));
    return { levels: orderedLevels, visibleEdges, omitted: hidden.size, cluster: activeCluster };
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
          const horizontalGap = mobile ? 200 : 210;
          const x = (column - (columnsInLayer - 1) / 2) * horizontalGap;
          const y = cursorY + row * rowGap;
          positions.set(node.id, { x, y, level });
          minX = Math.min(minX, x - nodeWidth / 2);
          maxX = Math.max(maxX, x + nodeWidth / 2);
          minY = Math.min(minY, y - nodeHeight / 2);
          maxY = Math.max(maxY, y + nodeHeight / 2);
        });
        cursorY += rows * rowGap + (mobile ? 36 : 80);
      }
      graphBounds = {
        x: minX - (mobile ? 28 : 110),
        y: minY - (mobile ? 28 : 80),
        width: Math.max(mobile ? 440 : 720, maxX - minX + (mobile ? 56 : 220)),
        height: Math.max(mobile ? 520 : 620, maxY - minY + (mobile ? 56 : 160)),
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
      x: minX - 24,
      y: minY - 100,
      width: Math.max(400, maxX - minX + 48),
      height: Math.max(420, maxY - minY + 200),
    };
    return positions;
  }

  function edgePath(source, target, positions, edgeIndex) {
    const vertical = useVerticalLayout();
    const start = vertical ? {x: source.x, y: source.y - nodeHeight / 2}
      : {x: source.x + nodeWidth / 2, y: source.y};
    const end = vertical ? {x: target.x, y: target.y + nodeHeight / 2}
      : {x: target.x - nodeWidth / 2, y: target.y};
    const bend = Math.max(24, Math.abs(vertical ? end.y - start.y : end.x - start.x) * 0.42);
    const c1 = vertical ? {x: start.x, y: start.y - bend} : {x: start.x + bend, y: start.y};
    const c2 = vertical ? {x: end.x, y: end.y + bend} : {x: end.x - bend, y: end.y};
    const obstacles = [...positions.values()].filter(p => p !== source && p !== target);
    // A shortcut edge may skip ranks, and wrapped vertical layers may contain
    // intervening cards. Keep these edges out of the card bodies and labels.
    let blocked = false;
    for (let step = 1; step < 40 && !blocked; step++) {
      const t = step / 40, u = 1 - t;
      const x = u**3 * start.x + 3*u*u*t*c1.x + 3*u*t*t*c2.x + t**3*end.x;
      const y = u**3 * start.y + 3*u*u*t*c1.y + 3*u*t*t*c2.y + t**3*end.y;
      blocked = obstacles.some(p => Math.abs(x-p.x) < nodeWidth/2+4 && Math.abs(y-p.y) < nodeHeight/2+4);
    }
    if (!blocked) return `M ${start.x} ${start.y} C ${c1.x} ${c1.y}, ${c2.x} ${c2.y}, ${end.x} ${end.y}`;
    const laneOffset = 22 + (edgeIndex % 4) * 12;
    if (vertical) {
      const lane = Math.max(...[...positions.values()].map(p => p.x + nodeWidth/2)) + laneOffset;
      graphBounds.width = Math.max(graphBounds.width, lane + 20 - graphBounds.x);
      return `M ${start.x} ${start.y} V ${start.y-12} H ${lane} V ${end.y+12} H ${end.x} V ${end.y}`;
    }
    const lane = Math.min(...[...positions.values()].map(p => p.y - nodeHeight/2)) - laneOffset;
    const bottom = graphBounds.y + graphBounds.height;
    graphBounds.y = Math.min(graphBounds.y, lane - 20);
    graphBounds.height = bottom - graphBounds.y;
    return `M ${start.x} ${start.y} H ${start.x+16} V ${lane} H ${end.x-16} V ${end.y} H ${end.x}`;
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
    const title = svgElement("title");
    title.textContent = `${node.title} — ${node.id.split("/")[0].replaceAll("-", " ")}`;
    const label = svgElement("text", { x: 14, y: 24 });
    const words = node.title.split(/\s+/);
    let first = "";
    while (words.length && (first + " " + words[0]).trim().length <= 19) first = (first + " " + words.shift()).trim();
    if (!first) first = words.shift() || "";
    const line1 = svgElement("tspan", {x: 14, y: words.length ? 23 : 33});
    line1.textContent = truncate(first, 19);
    label.appendChild(line1);
    if (words.length) {
      const line2 = svgElement("tspan", {x: 14, y: 41});
      line2.textContent = truncate(words.join(" "), 19);
      label.appendChild(line2);
    }
    link.appendChild(title);
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
    const bounds = svg.getBoundingClientRect();
    if (!bounds.width || !bounds.height) return;
    const ratio = bounds.width / bounds.height;
    const width = Math.max(graphBounds.width, graphBounds.height * ratio);
    const height = width / ratio;
    setViewBox({ x: graphBounds.x + (graphBounds.width - width) / 2,
      y: graphBounds.y + (graphBounds.height - height) / 2, width, height });
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

  function setReviewMode(next, updateUrl) {
    reviewMode = next === "reviewed" ? "reviewed" : "all";
    if (reviewFilter) {
      if (reviewFilter.type === "checkbox") reviewFilter.checked = reviewMode === "reviewed";
      else reviewFilter.value = reviewMode;
    }
    if (updateUrl) {
      const url = new URL(window.location.href);
      if (reviewMode === "reviewed") url.searchParams.set("review", "reviewed");
      else url.searchParams.delete("review");
      history.pushState({ ...(history.state || {}), focus: focusId, review: reviewMode }, "", url);
    }
  }

  function renderGraph() {
    if (!nodes.has(focusId)) return;
    const depth = Number(depthSelect.value || 2);
    if (mode !== "neighborhood" && !clusterId) { renderClusters(); return; }
    clusterPanel.hidden = true;
    showDependents.disabled = depthSelect.disabled = orientationButton.disabled = fitButton.disabled = false;
    svg.removeAttribute("hidden");
    clusterBack.hidden = mode === "neighborhood";
    const { levels, visibleEdges, omitted, cluster } = collectNeighborhood(focusId, depth);
    const positions = layout(levels);
    edgeLayer.replaceChildren();
    nodeLayer.replaceChildren();

    for (const [edgeIndex, edge] of visibleEdges.entries()) {
      const path = svgElement("path", {
        d: edgePath(positions.get(edge.source), positions.get(edge.target), positions, edgeIndex),
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
    const reviewedEdges = visibleEdges.filter((edge) => edge.reviewed).length;
    const unreviewedEdges = visibleEdges.length - reviewedEdges;
    const reviewDescription = reviewMode === "reviewed"
      ? ` Reviewed-only mode hides ${allEdges.filter((edge) => !edge.reviewed && levels.has(edge.source) && levels.has(edge.target)).length} unreviewed links.`
      : "";
    const emptyDescription = reviewMode === "reviewed" && levels.size === 1
      ? " No reviewed prerequisite links connect to this concept yet."
      : "";
    status.textContent = `${cluster ? `${cluster.title}: ${cluster.members.size} concepts in this cluster. ` : ""}Showing ${levels.size} concepts around ${nodes.get(focusId).title}: ${reviewedEdges} reviewed and ${unreviewedEdges} unreviewed prerequisite links.${reviewDescription}${emptyDescription}${layoutDescription}${omittedMessage}`;
    status.classList.add("ready");
    fitGraph();
  }

  async function loadViewer(node, shouldOpen) {
    const request = ++viewerRequest;
    root.classList.toggle("viewer-hidden", !shouldOpen);
    viewer.classList.toggle("open", shouldOpen);
    viewer.inert = !shouldOpen;
    viewerTitle.textContent = node.title;
    viewerSummary.textContent = node.summary;
    reviewState.textContent = node.dependency_review_count > 0
      ? `This prerequisite list has ${node.dependency_review_count} review${node.dependency_review_count === 1 ? "" : "s"}. Neighboring lists may be unreviewed.`
      : node.dependency_heuristic === "semantic-cycle-repair-v1"
        ? "Cycle repairs applied · full dependency review pending"
        : "Prerequisite suggestions · not yet reviewed";
    reviewState.classList.toggle("reviewed", node.dependency_review_count > 0);
    viewerContent.innerHTML = '<div class="loading" role="status">Loading definition…</div>';
    try {
      const response = await fetch(node.fragment);
      if (!response.ok) throw new Error("fragment unavailable");
      const markup = await response.text();
      if (request !== viewerRequest) return;
      const documentFragment = new DOMParser().parseFromString(markup, "text/html");
      const content = documentFragment.querySelector(".knowl-content");
      viewerContent.innerHTML = content ? content.outerHTML : markup;
    } catch (error) {
      if (request !== viewerRequest) return;
      viewerContent.innerHTML = `<p class="error">Definition could not be loaded. <a href="${node.href}">Open its full page</a>.</p>`;
    }
  }

  function selectNode(id, pushHistory, openViewer = true) {
    if (!nodes.has(id)) return;
    focusId = id;
    if (mode !== "neighborhood") {
      const group = clusterGroups.find(group => group.members.has(id));
      clusterId = group?.id || null;
    }
    renderGraph();
    loadViewer(nodes.get(id), openViewer);
    if (pushHistory) writeUrl(true);
  }

  function writeUrl(push = false) {
    const url = new URL(location.href);
    url.searchParams.set("focus", focusId);
    url.searchParams.set("layout", orientation);
    url.searchParams.set("depth", depthSelect.value);
    url.searchParams.set("view", mode);
    if (showDependents.checked) url.searchParams.set("dependents", "show");
    else url.searchParams.delete("dependents");
    if (reviewMode === "reviewed") url.searchParams.set("review", "reviewed");
    else url.searchParams.delete("review");
    if (showOrganizational.checked) url.searchParams.set("organizational", "show");
    else url.searchParams.delete("organizational");
    if (showCatalog.checked) url.searchParams.set("catalog", "show");
    else url.searchParams.delete("catalog");
    if (clusterId) url.searchParams.set("cluster", clusterId);
    else url.searchParams.delete("cluster");
    history[push ? "pushState" : "replaceState"]({}, "", url);
  }

  function renderClusters() {
    clusterPanel.replaceChildren();
    showDependents.disabled = depthSelect.disabled = orientationButton.disabled = fitButton.disabled = true;
    clusterPanel.hidden = false;
    svg.setAttribute("hidden", "");
    clusterBack.hidden = true;
    root.classList.add("viewer-hidden");
    viewer.classList.remove("open");
    viewer.inert = true;
    const heading = document.createElement("h1");
    heading.textContent = mode === "subjects" ? "Explore by subject" : "Connected components";
    const description = document.createElement("p");
    description.textContent = mode === "subjects"
      ? "Browse concepts by their canonical subject. Open a cluster to explore its prerequisite graph."
      : "Each component contains concepts connected by prerequisite links, ignoring direction for grouping. Isolated concepts form their own components.";
    const grid = document.createElement("div");
    grid.className = "graph-cluster-grid";
    for (const group of clusterGroups) {
      const button = document.createElement("button");
      button.className = "graph-cluster-card";
      button.type = "button";
      const title = document.createElement("strong");
      title.textContent = group.title;
      const count = document.createElement("span");
      count.textContent = `${group.members.size.toLocaleString()} concept${group.members.size === 1 ? "" : "s"} · ${group.edges.toLocaleString()} link${group.edges === 1 ? "" : "s"}`;
      button.append(title, count);
      button.addEventListener("click", () => {
        clusterId = group.id;
        const id = group.members.has(focusId) ? focusId : [...group.members].sort((a, b) =>
          (outgoing.get(b)?.length || 0) - (outgoing.get(a)?.length || 0) || a.localeCompare(b))[0];
        selectNode(id, true, !useMobileLayout());
      });
      grid.appendChild(button);
    }
    clusterPanel.append(heading, description, grid);
    status.textContent = `${nodes.size.toLocaleString()} concepts · ${clusterGroups.length.toLocaleString()} ${mode === "subjects" ? "subject clusters" : "connected components"} · acyclic prerequisite graph`;
  }

  function setMode(value) {
    mode = ["subjects", "components"].includes(value) ? value : "neighborhood";
    root.dataset.graphView = mode;
    viewSelect.value = mode;
    catalogControl.hidden = mode !== "components" || !graphData.nodes.some(node => node.content_source === "conjectures-catalog");
    organizationalControl.hidden = mode !== "components";
    const hideOrganizational = mode === "components" && !showOrganizational.checked;
    const hideCatalog = mode === "components" && !showCatalog.checked;
    nodes = new Map(graphData.nodes.filter(node => node.visibility === "production" &&
      !(hideCatalog && node.content_source === "conjectures-catalog") &&
      !(hideOrganizational && organizationalKinds.has((node.kind || "").toLowerCase()))).map(node => [node.id, node]));
    nodesByHref = new Map([...nodes.values()].map(node => [node.href, node]));
    allEdges = graphData.edges.filter(edge => nodes.has(edge.source) && nodes.has(edge.target));
    incoming = new Map(); outgoing = new Map();
    allEdges.forEach(edge => { edgeMapAdd(incoming, edge.target, edge); edgeMapAdd(outgoing, edge.source, edge); });
    initialFocus = nodes.has(root.dataset.defaultFocus) ? root.dataset.defaultFocus : nodes.keys().next().value;
    if (!nodes.has(focusId)) focusId = initialFocus;
    searchResults.hidden = true;
    clusterGroups = mode === "neighborhood" ? [] : GraphModel.clusters(nodes, reviewMode === "reviewed" ? allEdges.filter(edge => edge.reviewed) : allEdges, mode);
  }

  function restoreUrl() {
    const parameters = new URL(location.href).searchParams;
    const requestedLayout = parameters.get("layout");
    setOrientation(["vertical", "horizontal"].includes(requestedLayout) ? requestedLayout : (useMobileLayout() ? "vertical" : "horizontal"), false);
    depthSelect.value = [...depthSelect.options].some(option => option.value === parameters.get("depth")) ? parameters.get("depth") : "1";
    setReviewMode(parameters.get("review"), false);
    showDependents.checked = parameters.get("dependents") === "show";
    showCatalog.checked = parameters.get("catalog") === "show";
    showOrganizational.checked = parameters.get("organizational") === "show";
    setMode(parameters.get("view"));
    clusterId = clusterGroups.some(group => group.id === parameters.get("cluster")) ? parameters.get("cluster") : null;
    const requested = parameters.get("focus");
    focusId = nodes.has(requested) ? requested : initialFocus;
    if (clusterId && !clusterGroups.find(group => group.id === clusterId).members.has(focusId)) {
      focusId = [...clusterGroups.find(group => group.id === clusterId).members][0];
    }
    if (mode !== "neighborhood" && !clusterId) renderClusters();
    else selectNode(focusId, false, !useMobileLayout());
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
      searchResults.hidden = !search.value.trim();
      if (search.value.trim()) {
        const message = document.createElement("p");
        message.textContent = "No concepts found. Try another name.";
        searchResults.appendChild(message);
      }
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

  function svgPoint(clientX, clientY) {
    return new DOMPoint(clientX, clientY).matrixTransform(svg.getScreenCTM().inverse());
  }

  function zoom(scale, point = {x: viewBox.x + viewBox.width / 2, y: viewBox.y + viewBox.height / 2}) {
    const width = Math.min(graphBounds.width * 5, Math.max(240, viewBox.width * scale));
    const factor = width / viewBox.width;
    setViewBox({x: point.x - (point.x - viewBox.x) * factor,
      y: point.y - (point.y - viewBox.y) * factor, width, height: viewBox.height * factor});
  }

  function zoomAt(event) {
    event.preventDefault();
    zoom(event.deltaY < 0 ? 0.86 : 1.16, svgPoint(event.clientX, event.clientY));
  }

  function beginDrag(event) {
    if (event.button !== 0 || event.target.closest(".map-node")) return;
    svg.setPointerCapture(event.pointerId);
    drag = { point: svgPoint(event.clientX, event.clientY), viewBox: { ...viewBox }, inverse: svg.getScreenCTM().inverse() };
    svg.classList.add("dragging");
  }

  function moveDrag(event) {
    if (!drag) return;
    const point = new DOMPoint(event.clientX, event.clientY).matrixTransform(drag.inverse);
    setViewBox({ ...drag.viewBox, x: drag.viewBox.x - (point.x - drag.point.x), y: drag.viewBox.y - (point.y - drag.point.y) });
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
      graphData = data;
      setMode("neighborhood");
      const ranks = GraphModel.rank(nodes.keys(), allEdges);
      const height = Math.max(1, ...ranks.values());
      depthSelect.replaceChildren(...Array.from({length: height}, (_, index) => {
        const depth = index + 1;
        return new Option(`${depth} ${depth === 1 ? "step" : "steps"}`, String(depth));
      }));
      if (!nodes.size) throw new Error("No published concepts are available.");
      controls.forEach(control => { control.disabled = false; });
      initialFocus = nodes.has(root.dataset.defaultFocus) ? root.dataset.defaultFocus : nodes.keys().next().value;
      restoreUrl();
    } catch (error) {
      status.textContent = `The dependency graph could not be loaded. ${error.message}`;
      status.classList.add("error");
      controls.forEach(control => { control.disabled = true; });
    }
  }

  search.addEventListener("input", renderSearchResults);
  search.addEventListener("keydown", (event) => {
    if (event.key === "Escape") { searchResults.hidden = true; return; }
    if (event.key === "ArrowDown" && !searchResults.hidden) {
      event.preventDefault(); searchResults.querySelector("button")?.focus(); return;
    }
    if (event.key !== "Enter") return;
    const match = searchMatches(search.value)[0];
    if (match) {
      event.preventDefault();
      searchResults.hidden = true;
      selectNode(match.id, true);
    }
  });
  searchResults.addEventListener("keydown", event => {
    const buttons = [...searchResults.querySelectorAll("button")];
    const index = buttons.indexOf(document.activeElement);
    if (event.key === "Escape") { searchResults.hidden = true; search.focus(); }
    if (["ArrowDown", "ArrowUp"].includes(event.key)) {
      event.preventDefault(); buttons[(index + (event.key === "ArrowDown" ? 1 : buttons.length - 1)) % buttons.length]?.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (!event.target.closest(".graph-find")) searchResults.hidden = true;
  });
  showDependents.addEventListener("change", () => { renderGraph(); writeUrl(true); });
  depthSelect.addEventListener("change", () => { renderGraph(); writeUrl(true); });
  viewSelect.addEventListener("change", () => {
    setMode(viewSelect.value); clusterId = null;
    if (mode === "neighborhood") selectNode(focusId, false, !useMobileLayout());
    else renderClusters();
    writeUrl(true);
  });
  for (const filter of [showCatalog, showOrganizational]) filter.addEventListener("change", () => {
    setMode(mode);
    clusterId = null;
    renderClusters();
    writeUrl(true);
  });
  clusterBack.addEventListener("click", () => { clusterId = null; renderClusters(); writeUrl(true); });
  document.getElementById("graph-zoom-in").addEventListener("click", () => zoom(0.8));
  document.getElementById("graph-zoom-out").addEventListener("click", () => zoom(1.25));
  if (reviewFilter) {
    reviewFilter.addEventListener("change", () => {
      const next = reviewFilter.type === "checkbox"
        ? (reviewFilter.checked ? "reviewed" : "all")
        : reviewFilter.value;
      setReviewMode(next, false);
      setMode(mode);
      if (clusterId) clusterId = clusterGroups.find(group => group.members.has(focusId))?.id || null;
      renderGraph();
      writeUrl(true);
    });
  }
  orientationButton.addEventListener("click", () => {
    setOrientation(orientation === "horizontal" ? "vertical" : "horizontal", true);
    renderGraph();
  });
  fitButton.addEventListener("click", fitGraph);
  viewerClose.addEventListener("click", () => {
    root.classList.add("viewer-hidden");
    viewer.classList.remove("open");
    viewer.inert = true;
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
  svg.addEventListener("keydown", event => {
    if (event.target !== svg) return;
    const moves = {ArrowLeft: [-1,0], ArrowRight: [1,0], ArrowUp: [0,-1], ArrowDown: [0,1]};
    if (moves[event.key]) {
      event.preventDefault(); const [x,y] = moves[event.key];
      setViewBox({...viewBox, x:viewBox.x+x*viewBox.width*0.12, y:viewBox.y+y*viewBox.height*0.12});
    } else if (["+", "=", "-", "Home"].includes(event.key)) {
      event.preventDefault();
      if (event.key === "Home") fitGraph(); else zoom(event.key === "-" ? 1.25 : 0.8);
    }
  });
  svg.addEventListener("wheel", zoomAt, { passive: false });
  svg.addEventListener("pointerdown", beginDrag);
  svg.addEventListener("pointermove", moveDrag);
  svg.addEventListener("pointerup", endDrag);
  svg.addEventListener("pointercancel", endDrag);
  window.addEventListener("popstate", restoreUrl);
  new ResizeObserver(() => { if (!svg.hasAttribute("hidden")) fitGraph(); }).observe(stage);
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && viewer.classList.contains("open") && useMobileLayout()) {
      root.classList.add("viewer-hidden");
      viewer.classList.remove("open");
    viewer.inert = true;
    }
  });

  initialize();
}());
