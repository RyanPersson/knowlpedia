/* Presentation of shared catalogue data; no independent mathematical records. */
(function () {
  "use strict";
  const root = document.querySelector("[data-lie-groups]");
  if (!root) return;
  const $ = id => document.getElementById(`lg-${id}`);
  const sections = { classical: "Classical", exceptional: "Exceptional", abelian: "Abelian", nilpotent: "Nilpotent", geometric: "Geometric", product: "Products" };
  const seriesOrder = ["A", "B", "C", "D", "G2", "F4", "E6", "E7", "E8"];
  const forms = { compact: "Compact", split: "Split real", complex: "Complex" };
  const humanize = value => String(value).replaceAll("-", " ");
  const meta = obj => obj.properties.lie_group;
  const el = (tag, text, className) => { const n = document.createElement(tag); if (text != null) n.textContent = text; if (className) n.className = className; return n; };
  const link = (id, label) => { const n = el("a", label); n.href = `/${id.split("/").map(encodeURIComponent).join("/")}/`; return n; };
  const typeTex = series => series.length === 1 ? `${series}_r` : `${series[0]}_${series.slice(1)}`;
  const compactness = obj => obj.properties.compact === true ? "yes" : obj.properties.compact === false ? "no" : typeof obj.properties.compact === "string" ? "parameter" : "unknown";
  const propertyText = (obj, key, yes, no) => obj.properties[key] === true ? yes : obj.properties[key] === false ? no : typeof obj.properties[key] === "string" ? `${humanize(key)}: ${obj.properties[key]}` : `${humanize(key)}: not recorded`;
  const field = obj => obj.category_ids.includes("complex-lie-groups") ? "complex" : "real";
  const dimensionTex = value => String(value).replaceAll("*", "\\cdot ");

  function math(tex, block = false) {
    const n = el("span", tex, block ? "lg-math-display" : "lg-math");
    if (window.katex) window.katex.render(tex, n, { throwOnError: false, trust: false, strict: "ignore", displayMode: block });
    return n;
  }
  function prose(value, tag = "p", className = "") {
    const text = String(value), n = el(tag, null, className);
    const pattern = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|\$([^$\n]+?)\$/g;
    let cursor = 0;
    for (const m of text.matchAll(pattern)) { n.append(document.createTextNode(text.slice(cursor, m.index)), math(m[1] || m[2] || m[3] || m[4], Boolean(m[1] || m[2]))); cursor = m.index + m[0].length; }
    n.append(document.createTextNode(text.slice(cursor))); return n;
  }
  const dimension = (value, scalar) => math(`\\dim_{\\mathbb ${scalar === "complex" ? "C" : "R"}}=${dimensionTex(value)}`);
  const presentationOrder = (a, b) => Number(b.status === "family") - Number(a.status === "family") || (meta(a).display_order ?? Infinity) - (meta(b).display_order ?? Infinity) || a.name.localeCompare(b.name, undefined, { numeric: true });

  async function start() {
    const response = await fetch(root.dataset.catalogUrl);
    if (!response.ok) throw new Error(`Data request failed (${response.status})`);
    const data = await response.json();
    const allObjects = new Map(data.objects.map(obj => [obj.id, obj]));
    const categories = new Map((data.categories || []).map(category => [category.id, category]));
    const objects = data.objects.filter(obj => obj.properties?.lie_group);
    if (!objects.length) throw new Error("No Lie-group table records are available yet");
    const byId = new Map(objects.map(obj => [obj.id, obj]));
    const cells = objects.flatMap(obj => (meta(obj).classification_cells || []).map(cell => ({ obj, cell, key: `${cell.series}:${cell.form}` })));
    const allEntries = objects.map(obj => ({ obj, cell: null, key: obj.id }));
    const entries = new Map([...allEntries, ...cells].map(entry => [entry.key, entry]));
    const search = new Map(objects.map(obj => [obj.id, `${obj.name} ${obj.id} ${obj.notation} ${obj.family} ${JSON.stringify(obj.parameters)} ${JSON.stringify(meta(obj))}`.toLowerCase()]));
    const families = [...new Set(objects.map(obj => obj.family))].sort();
    for (const name of families) { const option = el("option", humanize(name)); option.value = name; $("family").append(option); }
    for (const name of seriesOrder.filter(s => cells.some(entry => entry.cell.series === s))) { const option = el("option", `Type ${name}`); option.value = name; $("series").append(option); }
    const state = { layout: "classification", section: "all", field: "all", compact: "all", family: "all", query: "", series: "A", page: 1, selected: null };
    const dialog = $("detail");
    let visible = [], timer, restoring = false;
    const isMobile = () => window.matchMedia("(max-width: 650px)").matches;
    const pageSize = () => isMobile() ? 12 : 36;
    const currentEntries = () => visible.filter(entry => state.layout === "all" || !isMobile() || entry.cell.series === state.series);
    function writeUrl() {
      if (restoring) return;
      const url = new URL(location.href);
      for (const [key, value] of Object.entries({ layout: state.layout === "all" ? "all" : null, section: state.section === "all" ? null : state.section, field: state.field === "all" ? null : state.field, compact: state.compact === "all" ? null : state.compact, family: state.family === "all" ? null : state.family, q: state.query || null, series: state.series === "A" ? null : state.series, page: state.page > 1 ? state.page : null, group: state.selected ? entries.get(state.selected).obj.id : null, cell: state.selected && entries.get(state.selected).cell ? state.selected : null })) {
        if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
      }
      history.replaceState(null, "", url);
    }
    function tile(entry) {
      const { obj, cell, key } = entry, lg = meta(obj);
      const button = el("button", null, "lg-tile lg-region"); button.type = "button";
      Object.assign(button.dataset, { groupId: obj.id, entryKey: key, region: lg.section });
      if (cell) { button.dataset.series = cell.series; button.dataset.form = cell.form; }
      button.setAttribute("aria-haspopup", "dialog"); button.setAttribute("aria-controls", "lg-detail"); button.setAttribute("aria-expanded", String(state.selected === key));
      button.setAttribute("aria-label", `${obj.name}. ${cell ? `Type ${cell.series}, ${forms[cell.form]}. ${cell.parameter_summary}` : lg.parameter_summary}. Open details.`);
      const top = el("span", null, "lg-tile-top");
      top.append(el("span", cell ? forms[cell.form] : obj.status === "family" ? "Family" : "Specified group"), el("span", cell ? "Selected global form" : field(obj) === "complex" ? "Complex Lie group" : "Real Lie group"));
      const symbol = el("span", null, "lg-tile-symbol"); symbol.append(math(cell?.notation || obj.notation));
      const dims = el("span", null, "lg-tile-dimension");
      if (cell) dims.append(dimension(cell.dimension_tex, cell.dimension_field));
      else for (const scalar of ["real", "complex"]) if (obj.dimensions[scalar] != null) dims.append(dimension(obj.dimensions[scalar], scalar));
      const domain = prose(cell?.parameter_summary || lg.parameter_summary, "span", "lg-tile-domain");
      button.append(top, symbol);
      if (!cell) button.append(el("span", obj.name, "lg-tile-name"));
      button.append(dims, domain);
      if (!cell) button.append(el("span", compactness(obj) === "yes" ? "Compact" : compactness(obj) === "no" ? "Noncompact" : compactness(obj) === "parameter" ? "Compactness depends on parameters" : "Compactness not recorded", "lg-tile-property"));
      button.addEventListener("click", () => openDetails(key)); return button;
    }
    function renderMatrix(matches) {
      const board = $("board"), header = el("div", null, "lg-matrix-header");
      header.append(el("span", "Lie type"));
      for (const form of Object.keys(forms)) { const label = el("div"); label.append(el("strong", forms[form]), el("span", form === "complex" ? "Complex dimension" : "Real dimension")); header.append(label); }
      board.append(header);
      for (const series of seriesOrder) {
        const rowEntries = matches.filter(entry => entry.cell.series === series); if (!rowEntries.length) continue;
        const row = el("section", null, "lg-matrix-row"); row.dataset.series = series; row.dataset.active = String(series === state.series); row.setAttribute("aria-label", `Type ${series}`);
        const label = el("h2", null, "lg-series-label"); label.append(math(typeTex(series))); row.append(label);
        for (const form of Object.keys(forms)) {
          const entry = rowEntries.find(item => item.cell.form === form);
          if (entry) { row.append(tile(entry)); visible.push(entry); } else row.append(el("div", "No match", "lg-missing-cell"));
        }
        board.append(row);
      }
    }
    function renderAll(matches) {
      const sorted = [...matches].sort((a, b) => Object.keys(sections).indexOf(meta(a.obj).section) - Object.keys(sections).indexOf(meta(b.obj).section) || presentationOrder(a.obj, b.obj));
      const pages = Math.max(1, Math.ceil(sorted.length / pageSize())); state.page = Math.min(state.page, pages);
      const shown = sorted.slice((state.page - 1) * pageSize(), state.page * pageSize());
      for (const [section, title] of Object.entries(sections)) {
        const members = shown.filter(entry => meta(entry.obj).section === section); if (!members.length) continue;
        const region = el("section", null, "lg-family-section lg-region"); region.dataset.region = section;
        const heading = el("div", null, "lg-section-heading"); heading.append(el("h2", title), el("span", `${matches.filter(entry => meta(entry.obj).section === section).length} matching entries`));
        const grid = el("div", null, "lg-family-grid"); for (const entry of members) { grid.append(tile(entry)); visible.push(entry); }
        region.append(heading, grid); $("board").append(region);
      }
      $("pagination").hidden = pages <= 1;
      $("page-label").textContent = `Page ${state.page} of ${pages}`;
      $("page-previous").disabled = state.page <= 1; $("page-next").disabled = state.page >= pages;
    }
    function render() {
      clearTimeout(timer); visible = [];
      const typeQuery = state.query.match(/\btype\s+(A|B|C|D|G2|F4|E6|E7|E8)\b/i) || state.query.match(/\b(A|B|C|D)_r\b/i);
      const requestedSeries = typeQuery?.[1].toUpperCase();
      const tokens = (typeQuery ? state.query.replace(typeQuery[0], "") : state.query).toLowerCase().trim().split(/\s+/).filter(Boolean);
      const records = state.layout === "all" ? allEntries : cells;
      const matches = records.filter(entry => {
        const obj = entry.obj;
        return (!requestedSeries || (entry.cell ? entry.cell.series === requestedSeries : (meta(obj).classification_cells || []).some(cell => cell.series === requestedSeries))) && (state.section === "all" || meta(obj).section === state.section) && (state.field === "all" || field(obj) === state.field) && (state.compact === "all" || compactness(obj) === state.compact) && (state.family === "all" || obj.family === state.family) && tokens.every(token => search.get(obj.id).includes(token) || JSON.stringify(entry.cell || {}).toLowerCase().includes(token));
      });
      if (matches.length && state.layout === "classification" && !matches.some(entry => entry.cell.series === state.series)) state.series = matches[0].cell.series;
      root.dataset.layout = state.layout;
      $("classification").setAttribute("aria-pressed", String(state.layout === "classification")); $("all").setAttribute("aria-pressed", String(state.layout === "all"));
      for (const key of ["section", "field", "compact", "family", "series"]) $(key).value = state[key];
      $("view-description").textContent = state.layout === "all" ? "The complete catalogue, grouped by family." : "Compare a compact, split-real, and complex choice for each type.";
      const activeFilters = ["section", "field", "compact", "family"].filter(key => state[key] !== "all").length;
      $("filter-count").textContent = activeFilters ? `(${activeFilters})` : "";
      $("reset").hidden = !state.query && !activeFilters;
      $("scope").hidden = state.layout === "all";
      $("pagination").hidden = true; $("board").replaceChildren();
      if (matches.length) { if (state.layout === "all") renderAll(matches); else renderMatrix(matches); }
      else {
        const empty = el("section", null, "lg-empty"); empty.append(el("h2", "No matching entries in this view"), el("p", "Try a shorter name or clear a filter."));
        if (state.layout === "classification") { const button = el("button", "Search all groups", "lg-text-button"); button.type = "button"; button.addEventListener("click", () => { state.layout = "all"; state.page = 1; render(); }); empty.append(button); }
        $("board").append(empty);
      }
      $("results").textContent = state.layout === "classification" ? `${matches.length} selections · ${new Set(matches.map(entry => entry.cell.series)).size} Lie-algebra types` : `${matches.length ? (state.page - 1) * pageSize() + 1 : 0}–${Math.min(state.page * pageSize(), matches.length)} of ${matches.length} catalogue entries.`;
      $("series-position").textContent = `${seriesOrder.indexOf(state.series) + 1} / ${seriesOrder.length}`;
      for (const option of $("series").options) option.disabled = !matches.some(entry => entry.cell?.series === option.value);
      writeUrl();
    }
    function section(title, content) { const n = el("section"); n.append(el("h3", title), content); return n; }
    function relationList(relations, context = "direct") {
      const connections = el("div", null, "lg-connections"); connections.dataset.context = context;
      for (const relation of relations) {
        const row = el("article", null, "lg-detail-relation"); row.dataset.kind = relation.kind; row.dataset.relationId = relation.id; row.dataset.category = relation.category_id || "";
        const source = allObjects.get(relation.source), target = allObjects.get(relation.target);
        const endpoints = el("p", null, "lg-relation-endpoints"); endpoints.append(link(source.knowl, source.name), document.createTextNode(" → "), link(target.knowl, target.name));
        const category = relation.category_id ? (categories.get(relation.category_id)?.name || humanize(relation.category_id)) : "No morphism category asserted";
        row.append(el("strong", humanize(relation.kind), "lg-relation-kind"), el("p", category, "lg-relation-category"), endpoints, prose(relation.statement));
        if (relation.conditions.length) row.append(prose(`Conditions: ${relation.conditions.join(" ")}`)); row.append(link(relation.knowl, "Read this relationship")); connections.append(row);
      }
      return connections;
    }
    function openDetails(key, updateUrl = true) {
      const entry = entries.get(key); if (!entry) return;
      state.selected = key;
      const { obj, cell } = entry, lg = meta(obj), body = $("detail-body"); body.replaceChildren(); body.className = "lg-region"; body.dataset.region = lg.section;
      body.append(el("p", cell ? `Type ${cell.series} · ${forms[cell.form]}` : sections[lg.section], "lg-detail-region"));
      const symbol = el("div", null, "lg-detail-symbol"); symbol.append(math(cell?.notation || obj.notation)); body.append(symbol);
      const title = el("h2", obj.name); title.id = "lg-detail-title"; body.append(title);
      if (cell) {
        const slice = el("div", null, "lg-slice"); slice.append(prose(cell.parameter_summary), dimension(cell.dimension_tex, cell.dimension_field), prose(cell.specialization));
        body.append(section("This table selection", slice), section("Selected global form", prose(cell.global_form)));
      }
      const badges = el("div", null, "lg-detail-badges"); badges.append(el("span", obj.status === "family" ? "Full parameterized family" : "Specified group"), el("span", field(obj) === "complex" ? "Complex Lie group" : "Real Lie group")); body.append(badges, prose(lg.construction_summary));
      if (cell) { const full = el("div", null, "lg-full-family-symbol"); full.append(math(obj.notation)); body.append(section("Owning catalogue entry", full)); }
      body.append(section("Global group", prose(lg.global_form_summary)), section("Full parameter range", prose(lg.parameter_summary)));
      const dims = el("div", null, "lg-detail-dimensions"); for (const scalar of ["real", "complex"]) if (obj.dimensions[scalar] != null) { const row = el("div"); row.append(el("span", `${humanize(scalar)} dimension`), dimension(obj.dimensions[scalar], scalar)); dims.append(row); }
      body.append(section("Dimensions of the catalogue entry", dims));
      const properties = el("ul"); properties.append(prose(propertyText(obj, "compact", "Compact", "Noncompact"), "li"), prose(propertyText(obj, "connected", "Connected", "Disconnected"), "li"));
      if (obj.properties.simply_connected != null) properties.append(prose(propertyText(obj, "simply_connected", "Topologically simply connected", "Not topologically simply connected"), "li"));
      body.append(section(cell ? "Properties of the owning entry" : "Recorded properties", properties));
      if (obj.constraints.length) { const list = el("ul"); for (const condition of obj.constraints) list.append(prose(condition, "li")); body.append(section("Conditions and conventions", list)); }
      const links = el("nav", null, "lg-detail-links"); links.setAttribute("aria-label", "Explore this group");
      const definition = link(obj.knowl, "Read the definition"); definition.className = "lg-primary-link";
      const explore = el("a", "Explore homomorphisms"); explore.href = `/catalog/explorer/?${new URLSearchParams({ source: obj.id, target: obj.id, operation: "aut", category: field(obj) === "complex" ? "complex-lie-groups" : "real-lie-groups" })}`;
      links.append(definition, explore); body.append(links);
      const relations = data.relationships.filter(relation => relation.source === obj.id || relation.target === obj.id);
      if (relations.length) body.append(section("Recorded maps and coincidences", relationList(relations)));
      if (obj.status === "family") {
        const examples = new Set(objects.filter(candidate => candidate.status !== "family" && candidate.family === obj.family && field(candidate) === field(obj)).map(candidate => candidate.id));
        const related = data.relationships.filter(relation => ["isomorphism", "covering"].includes(relation.kind) && (examples.has(relation.source) || examples.has(relation.target)) && !relations.includes(relation)).sort((a, b) => Number(b.kind === "isomorphism") - Number(a.kind === "isomorphism") || a.id.localeCompare(b.id, undefined, { numeric: true }));
        if (related.length) {
          const context = el("div");
          context.append(el("p", "Fixed examples from the complete family; their parameter values and maps are separate from this table selection."), relationList(related.slice(0, 6), "family-examples"));
          if (related.length > 6) context.append(el("p", `Showing 6 of ${related.length} recorded example maps.`));
          const browse = el("a", "Browse the full family"); browse.href = `/catalog/lie-groups/table/?${new URLSearchParams({ layout: "all", family: obj.family, field: field(obj) })}`; context.append(browse);
          body.append(section("Low-rank examples from this family", context));
        }
      }
      const current = currentEntries(), index = current.findIndex(item => item.key === key);
      $("detail-position").textContent = index >= 0 ? `${index + 1} of ${current.length} visible tiles` : "Selected catalogue entry";
      $("previous").disabled = index <= 0; $("next").disabled = index < 0 || index >= current.length - 1;
      root.querySelectorAll(".lg-tile").forEach(button => button.setAttribute("aria-expanded", String(button.dataset.entryKey === key)));
      if (!dialog.open) dialog.showModal(); dialog.scrollTop = 0;
      if (updateUrl) writeUrl();
    }
    function moveSelection(direction) { const current = currentEntries(), index = current.findIndex(entry => entry.key === state.selected); if (index >= 0 && current[index + direction]) openDetails(current[index + direction].key); }
    function readUrl() {
      restoring = true;
      const query = new URLSearchParams(location.search);
      state.layout = query.get("layout") === "all" ? "all" : "classification";
      for (const key of ["section", "field", "compact", "family"]) state[key] = [...$(key).options].some(option => option.value === query.get(key)) ? query.get(key) : "all";
      if (["section", "field", "compact", "family"].some(key => state[key] !== "all")) state.layout = "all";
      state.query = query.get("q") || ""; state.series = seriesOrder.includes(query.get("series")) ? query.get("series") : "A";
      state.page = /^\d+$/.test(query.get("page") || "") ? Math.max(1, Number(query.get("page"))) : 1;
      state.selected = entries.get(query.get("cell"))?.obj.id === query.get("group") ? query.get("cell") : byId.has(query.get("group")) ? query.get("group") : null;
      if (entries.get(state.selected)?.cell) state.series = entries.get(state.selected).cell.series;
      $("search").value = state.query; render();
      if (state.selected) openDetails(state.selected, false); else if (dialog.open) dialog.close();
      restoring = false;
    }
    for (const layout of ["classification", "all"]) $(layout).addEventListener("click", () => { state.layout = layout; state.page = 1; if (layout === "classification") for (const key of ["section", "field", "compact", "family"]) state[key] = "all"; render(); });
    $("search").addEventListener("input", event => { state.query = event.target.value; state.page = 1; clearTimeout(timer); timer = setTimeout(render, 100); });
    for (const key of ["section", "field", "compact", "family"]) $(key).addEventListener("change", event => { state[key] = event.target.value; state.layout = "all"; state.page = 1; render(); });
    $("series").addEventListener("change", event => { state.series = event.target.value; render(); });
    $("reset").addEventListener("click", () => { state.query = ""; for (const key of ["section", "field", "compact", "family"]) state[key] = "all"; state.page = 1; $("search").value = ""; render(); });
    for (const direction of ["previous", "next"]) $(`page-${direction}`).addEventListener("click", () => { state.page += direction === "next" ? 1 : -1; render(); $("board").scrollIntoView({ block: "start" }); $("board").querySelector(".lg-tile")?.focus({ preventScroll: true }); });
    $("board").addEventListener("keydown", event => {
      const current = event.target.closest(".lg-tile"); if (!current || !["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Home", "End"].includes(event.key)) return;
      const buttons = [...$("board").querySelectorAll(".lg-tile")].filter(button => button.getClientRects().length), index = buttons.indexOf(current);
      let target;
      if (event.key === "Home") target = buttons[0]; else if (event.key === "End") target = buttons.at(-1);
      else if (event.key === "ArrowLeft") target = buttons[index - 1]; else if (event.key === "ArrowRight") target = buttons[index + 1];
      else { const box = current.getBoundingClientRect(), direction = event.key === "ArrowDown" ? 1 : -1;
        const candidates = buttons.filter(button => button !== current).map(button => { const rect = button.getBoundingClientRect(); return { button, dx: Math.abs(rect.left + rect.width / 2 - box.left - box.width / 2), dy: (rect.top + rect.height / 2 - box.top - box.height / 2) * direction }; }).filter(candidate => candidate.dy > 8).sort((a, b) => a.dy - b.dy || a.dx - b.dx);
        if (candidates.length) target = candidates.filter(candidate => candidate.dy < candidates[0].dy + 8).sort((a, b) => a.dx - b.dx)[0].button;
      }
      event.preventDefault(); target?.focus();
    });
    $("close").addEventListener("click", () => dialog.close()); $("previous").addEventListener("click", () => moveSelection(-1)); $("next").addEventListener("click", () => moveSelection(1));
    dialog.addEventListener("keydown", event => { if (event.key === "ArrowLeft" || event.key === "ArrowRight") { event.preventDefault(); moveSelection(event.key === "ArrowRight" ? 1 : -1); } });
    dialog.addEventListener("click", event => { if (event.target === dialog) { const box = dialog.getBoundingClientRect(); if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close(); } });
    dialog.addEventListener("close", () => { const selected = state.selected; state.selected = null; root.querySelectorAll(".lg-tile").forEach(button => { button.setAttribute("aria-expanded", "false"); if (button.dataset.entryKey === selected && button.getClientRects().length) button.focus(); }); writeUrl(); });
    window.addEventListener("popstate", readUrl);
    window.matchMedia("(max-width: 650px)").addEventListener("change", () => { state.page = 1; render(); });
    readUrl(); $("loaded").hidden = false;
    $("status").textContent = `${cells.length} table selections · ${objects.length} catalogue entries`;
    root.dataset.lieGroupsReady = "true";
  }
  start().catch(error => { $("status").textContent = `The table could not load: ${error.message}. Definitions remain available in the Lie-group catalogue.`; $("status").setAttribute("role", "alert"); console.error(error); });
}());
