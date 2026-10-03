/* A visual view of catalogue records, never a second mathematical data source. */
(function () {
  "use strict";
  const root = document.querySelector("[data-finite-groups]");
  if (!root) return;
  const $ = id => document.getElementById(`fg-${id}`);
  const regionNames = { cyclic: "Cyclic", alternating: "Alternating", classical: "Classical Lie type", exceptional: "Exceptional Lie type", sporadic: "Sporadic", familiar: "Familiar finite groups" };
  const regions = Object.keys(regionNames);
  const clusterNames = { mathieu: "Mathieu groups", leech: "Leech-related groups", monster: "Monster-related groups", pariah: "Pariahs" };
  const simpleRoles = new Set(["simple-family", "sporadic", "tits"]);
  const el = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text != null) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  const metadata = obj => obj.properties.finite_group;
  const humanize = value => String(value).replaceAll("-", " ");
  const href = id => `/${id.split("/").map(encodeURIComponent).join("/")}/`;
  const link = (id, label) => { const node = el("a", label); node.href = href(id); return node; };
  const groupedDecimal = value => value.replace(/\B(?=(\d{3})+(?!\d))/g, ",");

  function math(tex, block = false) {
    const node = el("span", tex, block ? "fg-math-display" : "fg-math");
    if (window.katex) window.katex.render(tex, node, { throwOnError: false, trust: false, strict: "ignore", displayMode: block });
    return node;
  }

  function prose(value, tag = "p", className = "") {
    const text = String(value);
    const node = el(tag, null, className);
    const delimiters = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|\$([^$\n]+?)\$/g;
    let cursor = 0;
    for (const match of text.matchAll(delimiters)) {
      node.append(document.createTextNode(text.slice(cursor, match.index)), math(match[1] || match[2] || match[3] || match[4], Boolean(match[1] || match[2])));
      cursor = match.index + match[0].length;
    }
    node.append(document.createTextNode(text.slice(cursor)));
    return node;
  }

  function compactOrder(decimal) {
    if (decimal.length <= 12) return { label: groupedDecimal(decimal), tex: decimal.replace(/\B(?=(\d{3})+(?!\d))/g, "\\,"), approximate: false };
    // Decimal strings and integer arithmetic preserve the actual ordering of huge groups.
    let leading = BigInt(decimal.slice(0, 3));
    if (decimal[3] >= "5") leading += 1n;
    let exponent = decimal.length - 1;
    if (leading === 1000n) { leading = 100n; exponent += 1; }
    const digits = String(leading);
    const mantissa = `${digits[0]}.${digits.slice(1)}`;
    return { label: `approximately ${mantissa} × 10^${exponent}`, tex: `${mantissa}\\times10^{${exponent}}`, approximate: true };
  }

  function compareOrder(left, right) {
    const a = metadata(left).order_decimal, b = metadata(right).order_decimal;
    if (a == null && b == null) return left.name.localeCompare(right.name);
    if (a == null) return 1;
    if (b == null) return -1;
    const x = BigInt(a), y = BigInt(b);
    return x < y ? -1 : x > y ? 1 : left.name.localeCompare(right.name);
  }

  function comparePresentation(left, right) {
    const a = metadata(left).display_order ?? Infinity;
    const b = metadata(right).display_order ?? Infinity;
    return (a < b ? -1 : a > b ? 1 : 0) || left.name.localeCompare(right.name, undefined, { numeric: true });
  }

  async function start() {
    const response = await fetch(root.dataset.catalogUrl);
    if (!response.ok) throw new Error(`Data request failed (${response.status})`);
    const data = await response.json();
    const allObjects = new Map(data.objects.map(obj => [obj.id, obj]));
    const objects = data.objects.filter(obj => obj.properties?.finite_group);
    if (!objects.length) throw new Error("No finite-group records are available yet.");
    const byId = new Map(objects.map(obj => [obj.id, obj]));
    const relationships = new Map(data.relationships.map(record => [record.id, record]));
    const searchText = new Map(objects.map(obj => [obj.id, `${obj.name} ${obj.id} ${obj.notation} ${obj.family} ${JSON.stringify(obj.parameters)} ${JSON.stringify(metadata(obj))} order ${metadata(obj).order_decimal || ""}`.toLowerCase()]));
    const state = { layout: "classification", section: "all", query: "", sporadic: "cluster", selected: null };
    const dialog = $("detail");
    let visible = [];
    let renderTimer;
    let restoring = false;

    function writeUrl() {
      if (restoring) return;
      const url = new URL(location.href);
      for (const [key, value] of Object.entries({ layout: state.layout === "all" ? "all" : null, region: state.section === "all" ? null : state.section, q: state.query || null, sporadic: state.sporadic === "order" ? "order" : null, group: state.selected })) {
        if (value) url.searchParams.set(key, value);
        else url.searchParams.delete(key);
      }
      history.replaceState(null, "", url);
    }

    function tile(obj) {
      const fg = metadata(obj);
      const button = el("button", null, "fg-tile fg-region");
      button.type = "button";
      button.dataset.groupId = obj.id;
      button.dataset.region = fg.section;
      button.dataset.role = fg.table_role;
      button.setAttribute("aria-haspopup", "dialog");
      button.setAttribute("aria-expanded", String(state.selected === obj.id));
      button.setAttribute("aria-controls", "fg-detail");
      const role = obj.status === "family" ? "Family" : fg.table_role === "tits" ? "Tits group" : "Individual group";
      button.setAttribute("aria-label", `${obj.name}. ${role}. ${fg.parameter_summary}. Open details.`);
      const top = el("span", null, "fg-tile-top");
      top.append(el("span", role), el("span", fg.rank_label || (fg.table_role === "sporadic" ? "Sporadic" : "")));
      const symbol = el("span", null, "fg-tile-symbol");
      symbol.append(math(obj.notation));
      const name = el("span", obj.name, "fg-tile-name");
      const domain = prose(fg.parameter_summary, "span", "fg-tile-domain");
      const order = el("span", null, "fg-tile-order");
      if (fg.order_decimal) {
        const compact = compactOrder(fg.order_decimal);
        order.append(math(`\\lvert G\\rvert ${compact.approximate ? "\\approx" : "="}${compact.tex}`));
        order.setAttribute("aria-label", `Order ${compact.label}`);
        order.title = `Exact order: ${groupedDecimal(fg.order_decimal)}`;
      } else if (fg.order_tex.length <= 32 && !/\\(?:prod|sum|frac)/.test(fg.order_tex)) {
        order.append(math(`\\lvert G\\rvert=${fg.order_tex}`));
      } else {
        order.textContent = "Order: see formula →";
      }
      button.append(top, symbol, name, domain, order);
      button.addEventListener("click", () => openDetails(obj.id));
      return button;
    }

    function section(key, records, title = regionNames[key], columns = null) {
      if (!records.length) return null;
      const node = el("section", null, "fg-section fg-region");
      node.dataset.region = key;
      const heading = el("div", null, "fg-section-heading");
      const label = el("h2", title);
      label.id = `fg-section-${key}`;
      node.setAttribute("aria-labelledby", label.id);
      heading.append(label, el("span", `${records.length} ${records.length === 1 ? "entry" : "entries"}`, "fg-section-count"));
      const grid = el("div", null, "fg-grid");
      if (columns) grid.dataset.columns = String(columns);
      for (const obj of records) { grid.append(tile(obj)); visible.push(obj); }
      node.append(heading, grid);
      return node;
    }

    function renderClassification(records) {
      const board = $("board");
      const families = records.filter(obj => metadata(obj).table_role === "simple-family").sort(comparePresentation);
      const foundations = el("div", null, "fg-foundations");
      for (const key of ["cyclic", "alternating"]) {
        const node = section(key, families.filter(obj => metadata(obj).section === key));
        if (node) foundations.append(node);
      }
      if (foundations.childElementCount) board.append(foundations);
      const classical = section("classical", families.filter(obj => metadata(obj).section === "classical"));
      if (classical) board.append(classical);
      const exceptional = section("exceptional", families.filter(obj => metadata(obj).section === "exceptional"), regionNames.exceptional, 5);
      if (exceptional) board.append(exceptional);
      for (const obj of records.filter(obj => metadata(obj).table_role === "tits")) {
        const boundary = el("section", null, "fg-boundary fg-region fg-section");
        boundary.dataset.region = "exceptional";
        boundary.setAttribute("aria-label", "The Tits group: a separate boundary case");
        boundary.append(tile(obj)); visible.push(obj);
        const explanation = el("div");
        explanation.append(el("h3", "A separate boundary case"), prose(metadata(obj).construction_summary), el("p", "The Tits group is shown separately from the sporadic groups."));
        boundary.append(explanation);
        board.append(boundary);
      }
      const sporadics = records.filter(obj => metadata(obj).table_role === "sporadic");
      if (sporadics.length) {
        const area = el("section", null, "fg-section fg-region");
        area.dataset.region = "sporadic";
        const heading = el("div", null, "fg-sporadic-heading");
        const intro = el("div");
        intro.append(el("h2", "The sporadic groups"), el("p", "ATLAS display groups organize the exceptions. These labels do not assert direct subgroup containment."));
        const sortControl = el("div");
        const label = el("label", "Arrange the sporadics");
        label.htmlFor = "fg-sporadic-order";
        const select = el("select"); select.id = "fg-sporadic-order";
        for (const [value, text] of [["cluster", "ATLAS grouping"], ["order", "Increasing order"]]) { const option = el("option", text); option.value = value; select.append(option); }
        select.value = state.sporadic;
        select.addEventListener("change", event => { state.sporadic = event.target.value; render(); $("sporadic-order")?.focus(); });
        sortControl.append(label, select); heading.append(intro, sortControl); area.append(heading);
        if (state.sporadic === "order") {
          const grid = el("div", null, "fg-grid");
          for (const obj of [...sporadics].sort(compareOrder)) { grid.append(tile(obj)); visible.push(obj); }
          area.append(grid);
        } else {
          for (const [key, title] of [...Object.entries(clusterNames), ["unassigned", "Other recorded sporadics"]]) {
            const members = sporadics.filter(obj => key === "unassigned" ? !clusterNames[metadata(obj).sporadic_cluster] : metadata(obj).sporadic_cluster === key).sort(compareOrder);
            if (!members.length) continue;
            const cluster = el("section", null, "fg-cluster"); cluster.dataset.cluster = key;
            const label = el("div", null, "fg-section-heading");
            label.append(el("h3", title), el("span", `${members.length} ${members.length === 1 ? "group" : "groups"}`, "fg-section-count"));
            const grid = el("div", null, "fg-grid");
            for (const obj of members) { grid.append(tile(obj)); visible.push(obj); }
            cluster.append(label, grid); area.append(cluster);
          }
        }
        board.append(area);
      }
      if (!state.query && state.section === "all") {
        const familiar = objects.filter(obj => !simpleRoles.has(metadata(obj).table_role));
        if (familiar.length) {
          const invitation = el("div", null, "fg-familiar-invitation");
          invitation.append(el("p", `${familiar.length} more entries cover familiar families and individual examples. Simplicity is recorded separately for each one.`));
          const button = el("button", "Browse all groups"); button.type = "button";
          button.addEventListener("click", () => { state.layout = "all"; render(); $("all").focus(); });
          invitation.append(button); board.append(invitation);
        }
      }
    }

    function renderAll(records) {
      const board = $("board");
      const legend = el("div", null, "fg-legend"); legend.setAttribute("aria-label", "Tile colors");
      for (const key of regions.filter(key => records.some(obj => metadata(obj).section === key))) {
        const item = el("span", null, "fg-region"); item.dataset.region = key; item.append(el("i"), document.createTextNode(regionNames[key])); legend.append(item);
      }
      board.append(legend);
      const families = records.filter(obj => obj.status === "family").sort((a, b) => regions.indexOf(metadata(a).section) - regions.indexOf(metadata(b).section) || comparePresentation(a, b));
      const individuals = records.filter(obj => obj.status !== "family").sort(compareOrder);
      const orderDescription = individuals.some(obj => !metadata(obj).order_decimal) ? "Known exact orders increase from small to large; entries without a fixed order follow. Equal orders need not mean isomorphic groups." : "Arranged by exact order, from small to large. Equal orders need not mean isomorphic groups.";
      for (const [title, intro, members] of [["Families", "Each tile stands for the full stated parameter range. Families are not numerically ranked by order.", families], ["Individual groups", orderDescription, individuals]]) {
        if (!members.length) continue;
        const area = el("section", null, "fg-section");
        area.dataset.collection = title.toLowerCase();
        const heading = el("div", null, "fg-section-heading");
        heading.append(el("h2", title), el("span", `${members.length} entries`, "fg-section-count"));
        const grid = el("div", null, "fg-all-grid");
        for (const obj of members) { grid.append(tile(obj)); visible.push(obj); }
        area.append(heading, el("p", intro, "fg-section-intro"), grid); board.append(area);
      }
    }

    function render() {
      clearTimeout(renderTimer);
      visible = [];
      const tokens = state.query.toLowerCase().trim().split(/\s+/).filter(Boolean);
      const queryMatches = obj => tokens.every(token => searchText.get(obj.id).includes(token) || searchText.get(obj.id).includes(token.replaceAll(",", "")));
      const records = objects.filter(obj => (state.layout === "all" || simpleRoles.has(metadata(obj).table_role)) && (state.section === "all" || metadata(obj).section === state.section) && queryMatches(obj));
      $("classification").setAttribute("aria-pressed", String(state.layout === "classification"));
      $("all").setAttribute("aria-pressed", String(state.layout === "all"));
      $("region").value = state.section;
      $("view-description").textContent = state.layout === "classification" ? "Simple families first, then the sporadic exceptions." : "Families side by side; individual groups in order of size.";
      $("results").textContent = `${records.length} ${records.length === 1 ? "entry" : "entries"} shown${state.query ? ` for “${state.query}”` : ""}. Select a tile to explore.`;
      $("reset").hidden = !state.query && state.section === "all";
      $("board").replaceChildren();
      if (records.length) {
        if (state.layout === "classification") renderClassification(records); else renderAll(records);
      } else {
        const empty = el("section", null, "fg-empty");
        empty.append(el("h2", "No matching entries in this view"), el("p", "Try a shorter name, a mathematical symbol, or a different region."));
        if (state.layout === "classification") {
          const button = el("button", "Search all groups", "fg-text-button"); button.type = "button";
          button.addEventListener("click", () => { state.layout = "all"; render(); }); empty.append(button);
        }
        $("board").append(empty);
      }
      writeUrl();
    }

    function detailSection(title, content) {
      const section = el("section"); section.append(el("h3", title), content); return section;
    }

    function openDetails(id, updateUrl = true) {
      if (!byId.has(id)) return;
      state.selected = id;
      const obj = byId.get(id), fg = metadata(obj);
      const body = $("detail-body"); body.replaceChildren();
      body.className = "fg-region"; body.dataset.region = fg.section;
      body.append(el("p", regionNames[fg.section], "fg-detail-region"));
      const symbol = el("div", null, "fg-detail-symbol"); symbol.append(math(obj.notation)); body.append(symbol);
      const title = el("h2", obj.name); title.id = "fg-detail-title"; body.append(title);
      const badges = el("div", null, "fg-detail-badges");
      badges.append(el("span", obj.status === "family" ? "Constrained family" : "Individual group"));
      badges.append(el("span", fg.simple === true ? "Simple" : fg.simple === false ? "Not simple" : "Simplicity depends on parameters"));
      if (fg.table_role === "tits") badges.append(el("span", "Tits boundary case"));
      if (fg.sporadic_cluster) badges.append(el("span", clusterNames[fg.sporadic_cluster]));
      body.append(badges, prose(fg.construction_summary, "p", "fg-detail-intro"));
      const order = el("div", null, "fg-detail-order"); order.append(math(`\\lvert G\\rvert=${fg.order_tex}`, true));
      if (fg.order_decimal) order.append(el("p", `Exact order: ${groupedDecimal(fg.order_decimal)}`, "fg-exact-order"));
      body.append(detailSection("Order", order));
      body.append(detailSection(obj.status === "family" ? "Parameter range" : "The specified group", prose(fg.parameter_summary)));
      body.append(detailSection("Simplicity", prose(fg.simple_condition)));
      if (obj.constraints.length) {
        const list = el("ul"); for (const condition of obj.constraints) list.append(prose(condition, "li"));
        body.append(detailSection("Conditions and conventions", list));
      }
      const links = el("nav", null, "fg-detail-links"); links.setAttribute("aria-label", "Explore this group");
      const definition = link(obj.knowl, "Read the definition"); definition.className = "fg-primary-link";
      const explore = el("a", "Explore its homomorphisms");
      explore.href = `/catalog/explorer/?${new URLSearchParams({ source: id, target: id, operation: "aut", category: "finite-groups" })}`;
      const permalink = el("a", "Link to this tile");
      const url = new URL(location.href); url.searchParams.set("group", id); permalink.href = url.href;
      links.append(definition, explore, permalink); body.append(links);
      const relationIds = new Set([...(data.indexes.relationships_from[id] || []), ...(data.indexes.relationships_to[id] || [])]);
      if (relationIds.size) {
        const connections = el("div");
        for (const relationId of [...relationIds].slice(0, 8)) {
          const relation = relationships.get(relationId);
          const row = el("article", null, "fg-detail-relation");
          const other = allObjects.get(relation.source === id ? relation.target : relation.source);
          row.append(link(other.knowl, other.name), el("p", humanize(relation.kind)), prose(relation.statement));
          if (relation.conditions.length) row.append(prose(`Conditions: ${relation.conditions.join(" ")}`));
          row.append(link(relation.knowl, "Read this relationship")); connections.append(row);
        }
        if (relationIds.size > 8) connections.append(el("p", `Showing 8 of ${relationIds.size} recorded relationships. Follow the catalogue explorer for the full neighborhood.`));
        body.append(detailSection("Recorded connections", connections));
      }
      const index = visible.findIndex(item => item.id === id);
      $("detail-position").textContent = index >= 0 ? `${index + 1} of ${visible.length} visible entries` : "Selected catalogue entry";
      $("previous").disabled = index <= 0;
      $("next").disabled = index < 0 || index >= visible.length - 1;
      root.querySelectorAll(".fg-tile").forEach(button => button.setAttribute("aria-expanded", String(button.dataset.groupId === id)));
      if (!dialog.open) dialog.showModal();
      dialog.scrollTop = 0;
      if (updateUrl) writeUrl();
    }

    function moveSelection(direction) {
      const index = visible.findIndex(obj => obj.id === state.selected);
      const next = visible[index + direction];
      if (index >= 0 && next) openDetails(next.id);
    }

    function readUrl() {
      restoring = true;
      const query = new URLSearchParams(location.search);
      state.layout = query.get("layout") === "all" ? "all" : "classification";
      state.section = regions.includes(query.get("region")) ? query.get("region") : "all";
      if (state.section === "familiar") state.layout = "all";
      state.query = query.get("q") || "";
      state.sporadic = query.get("sporadic") === "order" ? "order" : "cluster";
      state.selected = byId.has(query.get("group")) ? query.get("group") : null;
      $("search").value = state.query;
      render();
      if (state.selected) openDetails(state.selected, false);
      else if (dialog.open) dialog.close();
      restoring = false;
    }

    $("classification").addEventListener("click", () => { state.layout = "classification"; if (state.section === "familiar") state.section = "all"; render(); });
    $("all").addEventListener("click", () => { state.layout = "all"; render(); });
    $("search").addEventListener("input", event => { state.query = event.target.value; clearTimeout(renderTimer); renderTimer = setTimeout(render, 100); });
    $("region").addEventListener("change", event => { state.section = event.target.value; if (state.section === "familiar") state.layout = "all"; render(); });
    $("reset").addEventListener("click", () => { state.query = ""; state.section = "all"; $("search").value = ""; render(); $("search").focus(); });
    $("board").addEventListener("keydown", event => {
      const current = event.target.closest(".fg-tile");
      if (!current || !["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Home", "End"].includes(event.key)) return;
      const buttons = [...$("board").querySelectorAll(".fg-tile")];
      const index = buttons.indexOf(current);
      let target;
      if (event.key === "Home") target = buttons[0];
      else if (event.key === "End") target = buttons.at(-1);
      else if (event.key === "ArrowLeft") target = buttons[index - 1];
      else if (event.key === "ArrowRight") target = buttons[index + 1];
      else {
        const box = current.getBoundingClientRect();
        const x = box.left + box.width / 2, y = box.top + box.height / 2;
        const direction = event.key === "ArrowDown" ? 1 : -1;
        const candidates = buttons.filter(button => button !== current).map(button => {
          const rect = button.getBoundingClientRect();
          return { button, dx: Math.abs(rect.left + rect.width / 2 - x), dy: (rect.top + rect.height / 2 - y) * direction };
        }).filter(candidate => candidate.dy > 8).sort((a, b) => a.dy - b.dy || a.dx - b.dx);
        if (candidates.length) {
          const nearestRow = candidates.filter(candidate => candidate.dy < candidates[0].dy + 8);
          target = nearestRow.sort((a, b) => a.dx - b.dx)[0].button;
        }
      }
      event.preventDefault();
      target?.focus();
    });
    $("close").addEventListener("click", () => dialog.close());
    $("previous").addEventListener("click", () => moveSelection(-1));
    $("next").addEventListener("click", () => moveSelection(1));
    dialog.addEventListener("keydown", event => {
      if (event.key === "ArrowLeft") { event.preventDefault(); moveSelection(-1); }
      if (event.key === "ArrowRight") { event.preventDefault(); moveSelection(1); }
    });
    dialog.addEventListener("click", event => { if (event.target === dialog) { const box = dialog.getBoundingClientRect(); if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close(); } });
    dialog.addEventListener("close", () => {
      const selected = state.selected; state.selected = null;
      root.querySelectorAll(".fg-tile").forEach(button => {
        button.setAttribute("aria-expanded", "false");
        if (button.dataset.groupId === selected) button.focus();
      });
      writeUrl();
    });
    window.addEventListener("popstate", readUrl);
    readUrl();
    $("loaded").hidden = false;
    const count = role => objects.filter(obj => metadata(obj).table_role === role).length;
    $("status").textContent = `${count("simple-family")} simple families · ${count("sporadic")} sporadic groups · ${count("tits")} Tits group · ${objects.length} catalogue entries in all.`;
    root.dataset.finiteGroupsReady = "true";
  }

  start().catch(error => {
    $("status").textContent = `The table could not load: ${error.message}. The definitions remain available in the finite-group catalogue.`;
    $("status").setAttribute("role", "alert");
    console.error(error);
  });
}());
