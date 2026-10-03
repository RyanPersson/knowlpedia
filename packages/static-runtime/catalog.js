/* Sparse catalogue queries. No absent map, inverse, or composition is inferred. */
(function () {
  "use strict";
  const root = document.querySelector("[data-catalog-explorer]");
  if (!root) return;
  const $ = (id) => document.getElementById(`catalog-${id}`);
  const el = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text != null) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  const humanize = (s) => String(s).replace(/[-_]/g, " ");
  const display = (value) => typeof value === "object" ? JSON.stringify(value) : String(value);
  const badge = (text) => el("span", text, "catalog-badge");
  const knowlLink = (id, label = "Read definition") => {
    const link = el("a", label);
    link.href = `/${id.split("/").map(encodeURIComponent).join("/")}/`;
    return link;
  };
  const constructionKinds = new Set(["construction", "scalar-restriction", "complexification", "lie-algebra", "derivation-algebra", "automorphism-group"]);
  const isConstruction = (record) => !record.category_id || constructionKinds.has(record.kind);
  const inputs = (record) => [record.source, ...(record.parameters?.other_input_id ? [record.parameters.other_input_id] : [])];

  function math(tex, block = false) {
    const node = el("span", tex, block ? "catalog-display-math" : "catalog-inline-math");
    if (window.katex) window.katex.render(tex, node, { throwOnError: false, trust: false, strict: "ignore", displayMode: block });
    return node;
  }

  // Render only math delimiters, never execute HTML or author-supplied URLs.
  function prose(text, tag = "p", className = "") {
    const node = el(tag, null, className);
    const pattern = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|\$([^$\n]+?)\$/g;
    let cursor = 0;
    for (const match of String(text).matchAll(pattern)) {
      node.append(document.createTextNode(String(text).slice(cursor, match.index)));
      node.append(math(match[1] || match[2] || match[3] || match[4], Boolean(match[1] || match[2])));
      cursor = match.index + match[0].length;
    }
    node.append(document.createTextNode(String(text).slice(cursor)));
    return node;
  }

  function conditions(items, label = "Conditions") {
    const wrapper = el("div");
    if (!items?.length) return wrapper;
    wrapper.append(el("strong", label));
    const list = el("ul", null, "catalog-constraints");
    for (const item of items) list.append(prose(item, "li"));
    wrapper.append(list);
    return wrapper;
  }

  function evidence(record) {
    const detail = el("details");
    detail.append(el("summary", "Evidence"));
    const proof = badge(humanize(record.evidence.status));
    proof.dataset.evidence = record.evidence.status;
    detail.append(proof);
    detail.append(prose(record.evidence.method));
    for (const ref of record.evidence.references || []) {
      const p = el("p");
      const link = el("a", ref.title);
      if (/^https?:\/\//i.test(ref.url)) link.href = ref.url;
      p.append(link, document.createTextNode(` — ${ref.locator}`));
      detail.append(p);
    }
    const lean = record.evidence.lean;
    if (lean) detail.append(el("p", `Lean: ${lean.module} · ${lean.declaration} · ${lean.revision}`, "catalog-muted"));
    return detail;
  }

  async function start() {
    const response = await fetch(root.dataset.catalogUrl);
    if (!response.ok) throw new Error(`Catalogue request failed (${response.status})`);
    const data = await response.json();
    if (data.schema_version !== 1 || !data.objects?.length) throw new Error("This catalogue has no supported object records.");
    const collections = Object.fromEntries(["objects", "categories", "views", "relationships", "morphism_spaces"].map(name => [name, new Map(data[name].map(record => [record.id, record]))]));
    const { objects, categories, views, relationships, morphism_spaces: spaces } = collections;
    const indexes = data.indexes;
    const sortedObjects = [...objects.values()].sort((a, b) => a.name.localeCompare(b.name, undefined, { numeric: true }));
    const searchText = new Map(sortedObjects.map(obj => [obj.id, `${obj.name} ${obj.notation} ${obj.id} ${obj.kind} ${obj.family} ${JSON.stringify(obj.parameters)}`.toLowerCase()]));
    const state = { source: null, target: null, category: null, operation: "hom", sourceView: null, targetView: null };
    let relationLimit = 6;
    let pickerEndpoint = "source", pickerLimit = 40;
    let homTarget = null, homTargetView = null;
    const objectViews = (id, category = null) => (indexes.views_by_object[id] || []).map(viewId => views.get(viewId)).filter(view => !category || view.category_id === category);
    const matchesCategory = (record) => !state.category || !record.category_id || record.category_id === state.category;
    const pairKey = () => `${state.source}\0${state.target}\0${state.category || ""}`;
    let previousPair;

    function renderPicker() {
      const search = $("picker-search").value.trim().toLowerCase();
      const tokens = search.split(/\s+/).filter(Boolean);
      const matches = sortedObjects.filter(obj => tokens.every(token => searchText.get(obj.id).includes(token)));
      const wrapper = $("picker-results");
      wrapper.replaceChildren();
      $("picker-count").textContent = `${matches.length} object${matches.length === 1 ? "" : "s"}${matches.length > pickerLimit ? ` · showing ${pickerLimit}` : ""}`;
      if (!matches.length) wrapper.append(el("p", "No matches. Try a shorter name or a different notation.", "catalog-empty"));
      for (const obj of matches.slice(0, pickerLimit)) {
        const button = el("button", null, "catalog-picker-option");
        button.type = "button";
        button.dataset.objectId = obj.id;
        button.setAttribute("aria-label", `${obj.name}${obj.status === "family" ? ", symbolic family" : ""}`);
        button.setAttribute("aria-pressed", String(obj.id === state[pickerEndpoint]));
        const title = el("span", obj.name, "catalog-picker-name");
        const meta = el("span", `${humanize(obj.kind)}${obj.status === "family" ? " · family" : ""}`, "catalog-muted");
        button.append(title, meta);
        button.addEventListener("click", () => {
          state[pickerEndpoint] = obj.id;
          $("picker").close();
          render();
        });
        wrapper.append(button);
      }
      $("picker-more").hidden = matches.length <= pickerLimit;
    }

    function openPicker(endpoint) {
      pickerEndpoint = endpoint;
      pickerLimit = 40;
      $("picker-title").textContent = state.operation !== "hom" ? "Choose an object" : `Choose the ${endpoint}`;
      $("picker-search").value = "";
      renderPicker();
      $("picker").showModal();
      $("picker-search").focus();
    }

    function readUrl() {
      const query = new URLSearchParams(location.search);
      state.source = objects.has(query.get("source")) ? query.get("source") : objects.has("scalar-c") ? "scalar-c" : sortedObjects[0].id;
      state.target = objects.has(query.get("target")) ? query.get("target") : state.source;
      state.operation = ["hom", "end", "aut"].includes(query.get("operation")) ? query.get("operation") : "aut";
      state.category = query.get("category");
      state.sourceView = query.get("source_view");
      state.targetView = query.get("target_view");
      homTarget = null; homTargetView = null;
      render(false);
    }

    function writeUrl() {
      const url = new URL(location.href);
      for (const [key, value] of Object.entries({ source: state.source, target: state.target, category: state.category, operation: state.operation, source_view: state.sourceView, target_view: state.targetView })) {
        if (value) url.searchParams.set(key, value);
        else url.searchParams.delete(key);
      }
      if (url.href !== location.href) history.pushState(null, "", url);
    }

    function reconcile() {
      if (state.operation !== "hom") state.target = state.source;
      const sourceCategories = new Set(objectViews(state.source).map(v => v.category_id));
      const targetCategories = new Set(objectViews(state.target).map(v => v.category_id));
      const common = [...sourceCategories].filter(id => targetCategories.has(id)).map(id => categories.get(id)).sort((a, b) => a.name.localeCompare(b.name));
      if (!common.some(cat => cat.id === state.category)) {
        // Prefer a category containing an example for this operation and pair.
        const example = objectViews(state.source).flatMap(view => (indexes.morphisms_by_source[view.id] || []).map(id => spaces.get(id))).find(space => space.operation === state.operation && views.get(space.target_view).object_id === state.target && common.some(cat => cat.id === views.get(space.source_view).category_id));
        state.category = example ? views.get(example.source_view).category_id : common.find(cat => cat.id !== "sets")?.id || common[0]?.id || null;
        if (example) { state.sourceView = example.source_view; state.targetView = example.target_view; }
      }
      const sourceChoices = state.category ? objectViews(state.source, state.category) : [];
      const targetChoices = state.category ? objectViews(state.target, state.category) : [];
      if (!sourceChoices.some(v => v.id === state.sourceView)) state.sourceView = sourceChoices[0]?.id || null;
      if (!targetChoices.some(v => v.id === state.targetView)) state.targetView = targetChoices[0]?.id || null;
      if (state.operation !== "hom") state.targetView = state.sourceView;
      return { common, sourceChoices, targetChoices };
    }

    function renderView(endpoint, choices) {
      const selected = state[`${endpoint}View`];
      const select = $(`${endpoint}-view`);
      select.replaceChildren();
      for (const view of choices) {
        const option = el("option", view.description || (view.id === `${view.object_id}@${view.category_id}` ? "Canonical structure in this category" : view.id));
        option.value = view.id;
        select.append(option);
      }
      if (!choices.length) select.append(el("option", "No common category"));
      select.value = selected || "";
      select.hidden = choices.length <= 1;
      select.disabled = !choices.length || (endpoint === "target" && state.operation !== "hom");
      const meaningful = choices.length > 1 || choices.some(view => view.constraints?.length || (view.parameters && Object.keys(view.parameters).length) || view.description);
      $(`${endpoint}-view-field`).hidden = !meaningful || (endpoint === "target" && state.operation !== "hom");
      select.previousElementSibling.hidden = select.hidden;
      const info = $(`${endpoint}-view-info`);
      info.replaceChildren();
      if (!selected) return;
      const view = views.get(selected);
      if (view.description && choices.length <= 1) info.append(prose(view.description));
      if (view.parameters && Object.keys(view.parameters).length) info.append(prose(` Parameters: ${Object.entries(view.parameters).map(([key, value]) => `${key} = ${display(value)}`).join("; ")}.`, "span"));
      if (view.constraints?.length) info.append(conditions(view.constraints, "Structure constraints"));
    }

    function renderCategory(common) {
      const select = $("category");
      select.replaceChildren();
      const withResults = new Set(objectViews(state.source).flatMap(view => (indexes.morphisms_by_source[view.id] || []).map(id => spaces.get(id)))
        .filter(space => space.operation === state.operation && views.get(space.target_view).object_id === state.target)
        .map(space => views.get(space.source_view).category_id));
      for (const [label, hasResult] of [["With results", true], ["Other categories", false]]) {
        const choices = common.filter(category => withResults.has(category.id) === hasResult);
        if (!choices.length) continue;
        const group = el("optgroup"); group.label = label;
        for (const category of choices) {
          const option = el("option", category.name); option.value = category.id; group.append(option);
        }
        select.append(group);
      }
      if (!common.length) select.append(el("option", "No common category recorded"));
      select.value = state.category || "";
      select.disabled = !common.length;
      select.title = state.category ? categories.get(state.category).name : "No common category recorded";
      const wrapper = $("category-info");
      wrapper.replaceChildren();
      if (!state.category) {
        wrapper.append(el("p", "These objects have no common category recorded. Choose another object to compare their maps.", "catalog-empty"));
        return;
      }
      const category = categories.get(state.category);
      const details = el("details");
      details.append(el("summary", "What these maps preserve"));
      details.append(conditions(category.object_axioms, "Objects"), conditions(category.morphism_axioms, "Morphisms"));
      details.append(prose(`Units: ${category.unit_policy}. Regularity: ${category.regularity}.`));
      details.append(knowlLink(category.knowl, "Read category definition"));
      wrapper.append(details);
    }

    function renderObject(endpoint) {
      const obj = objects.get(state[endpoint]);
      const wrapper = $(`${endpoint}-card`);
      // Keep the opener and disclosure stable so updates preserve keyboard focus.
      if (!wrapper.firstChild) {
        const heading = el("div", null, "catalog-section-heading");
        const change = el("button", "Change", "catalog-button");
        change.type = "button";
        change.id = `catalog-${endpoint}-change`;
        change.setAttribute("aria-haspopup", "dialog");
        change.addEventListener("click", () => openPicker(endpoint));
        heading.append(el("div", null, "catalog-object-selected"), change);
        wrapper.append(heading, el("details", null, "catalog-object-details"));
      }
      const label = state.operation === "hom" ? (endpoint === "source" ? "From" : "To") : "Object";
      $(`${endpoint}-change`).setAttribute("aria-label", `Change ${state.operation === "hom" ? endpoint : "object"}: ${obj.name}`);
      const selected = wrapper.querySelector(".catalog-object-selected");
      selected.replaceChildren();
      const notation = el("div", null, "catalog-object-notation");
      notation.append(math(obj.notation));
      const name = el("div");
      const title = el("h2"); title.append(knowlLink(obj.knowl, obj.name));
      name.append(el("span", label, "catalog-object-label"), title);
      if (obj.status === "family") name.append(badge("Symbolic family"));
      selected.append(notation, name);
      const details = wrapper.querySelector("details");
      if (wrapper.dataset.objectId !== obj.id) details.open = false;
      wrapper.dataset.objectId = obj.id;
      details.replaceChildren(el("summary", "Object details"));
      if (obj.description) details.append(prose(obj.description));
      const facts = el("dl", null, "catalog-facts");
      const addFact = (key, value) => facts.append(el("dt", key), prose(value, "dd"));
      addFact("Type", humanize(obj.kind));
      addFact("Family", humanize(obj.family));
      for (const [key, value] of Object.entries(obj.parameters)) addFact(humanize(key), display(value));
      for (const [key, value] of Object.entries(obj.dimensions)) addFact(`${humanize(key)} dimension`, display(value));
      details.append(facts, conditions(obj.constraints, "Object constraints"));
      const categoryIds = [...new Set(objectViews(obj.id).map(v => v.category_id))];
      const catDetails = el("details");
      catDetails.append(el("summary", `${categoryIds.length} categories`));
      const list = el("ul", null, "catalog-constraints");
      for (const id of categoryIds) {
        const item = el("li");
        item.append(knowlLink(categories.get(id).knowl, categories.get(id).name));
        list.append(item);
      }
      catDetails.append(list);
      details.append(catDetails);
      if (Object.keys(obj.properties).length) {
        const properties = el("details");
        properties.append(el("summary", "Properties"));
        for (const [key, value] of Object.entries(obj.properties)) properties.append(prose(`${humanize(key)}: ${display(value)}`));
        details.append(properties);
      }
      details.append(el("p", obj.id, "catalog-object-id"));
    }

    function renderSuggestions() {
      const wrapper = $("suggestions");
      wrapper.replaceChildren();
      // Offer recorded results, without pretending that uncatalogued maps do not exist.
      const alternatives = objectViews(state.source).flatMap(view => (indexes.morphisms_by_source[view.id] || []).map(id => spaces.get(id)))
        .filter(space => space.operation === state.operation && views.get(space.target_view).object_id === state.target && (space.source_view !== state.sourceView || space.target_view !== state.targetView));
      const unique = [...new Map(alternatives.map(space => [`${space.source_view}\0${space.target_view}`, space])).values()];
      if (!unique.length) return;
      const details = el("details");
      details.open = !(indexes.morphism_lookup[state.sourceView]?.[state.targetView]?.[state.operation]?.length);
      details.append(el("summary", `Explore ${unique.length} other structure${unique.length === 1 ? "" : "s"} with results`));
      const list = el("div", null, "catalog-suggestions");
      for (const record of unique) {
        const view = views.get(record.source_view), target = views.get(record.target_view);
        const button = el("button", categories.get(view.category_id).name + (view.description ? ` · ${view.description}` : "") + (target.id !== view.id && target.description ? ` → ${target.description}` : ""), "catalog-button");
        button.type = "button";
        button.addEventListener("click", () => {
          state.category = view.category_id; state.sourceView = view.id; state.targetView = record.target_view;
          render(); $("category").focus();
        });
        list.append(button);
      }
      details.append(list); wrapper.append(details);
    }

    function renderSpaces() {
      const records = (indexes.morphism_lookup[state.sourceView]?.[state.targetView]?.[state.operation] || []).map(id => spaces.get(id));
      const result = $("morphisms");
      result.replaceChildren();
      const coverage = $("coverage");
      const complete = records.some(record => record.coverage === "complete");
      const partial = records.some(record => record.coverage === "partial");
      coverage.dataset.coverage = complete ? "complete" : partial ? "partial" : "unknown";
      coverage.textContent = !state.category ? "" : !records.length ? "Not catalogued" : complete ? "Complete description" : partial ? "Partial description" : "Coverage unspecified";
      coverage.hidden = !state.category;
      $("morphisms-title").textContent = { aut: "Automorphisms", end: "Endomorphisms", hom: "Maps between objects" }[state.operation];
      const queryLabel = $("query-label");
      queryLabel.replaceChildren();
      if (state.category) {
        queryLabel.append(math(`\\operatorname{${state.operation[0].toUpperCase()}${state.operation.slice(1)}}(${objects.get(state.source).notation}${state.operation === "hom" ? `, ${objects.get(state.target).notation}` : ""})`));
        queryLabel.append(document.createTextNode(` · ${categories.get(state.category).name}`));
      }
      renderSuggestions();
      if (!records.length) {
        result.append(el("p", state.category ? "No description yet. The maps may still exist; try another category or open the object definition." : "Choose objects with structures in the same category to see their maps.", "catalog-empty"));
        return;
      }
      for (const record of records) {
        const article = el("article", null, "catalog-record");
        article.dataset.recordId = record.id;
        const badges = el("div", null, "catalog-badges");
        const completeness = badge(record.coverage === "complete" ? "Complete under stated conditions" : record.coverage === "partial" ? "Partial description" : "Completeness not specified");
        completeness.dataset.coverage = record.coverage || "unknown";
        const proof = badge(humanize(record.evidence.status));
        proof.dataset.evidence = record.evidence.status;
        // A single result already carries its coverage in the section heading.
        if (records.length > 1) badges.append(completeness);
        if (record.evidence.status === "conjectural") badges.append(proof);
        if (badges.childElementCount) article.append(badges);
        article.append(prose(record.description), conditions(record.conditions));
        if (record.result_object_ids?.length) {
          const results = el("p", "See also: ");
          record.result_object_ids.forEach((id, index) => {
            if (index) results.append(document.createTextNode(", "));
            const obj = objects.get(id);
            results.append(knowlLink(obj.knowl, obj.name));
          });
          article.append(results);
        }
        article.append(knowlLink(record.knowl, "Explanation"), evidence(record));
        result.append(article);
      }
    }

    function svgNode(tag, attributes, text) {
      const node = document.createElementNS("http://www.w3.org/2000/svg", tag);
      for (const [key, value] of Object.entries(attributes)) node.setAttribute(key, value);
      if (text != null) node.textContent = text;
      return node;
    }

    function renderDiagram(records) {
      const wrapper = $("diagram");
      wrapper.replaceChildren();
      if (!records.length) {
        $("diagram-details").hidden = true;
        return;
      }
      $("diagram-details").hidden = false;
      const displayed = records.slice(0, 8);
      const same = state.source === state.target;
      const height = Math.max(160, 100 + displayed.length * 36);
      const svg = svgNode("svg", { viewBox: `0 0 760 ${height}`, class: "catalog-diagram", role: "img", "aria-labelledby": "catalog-diagram-title catalog-diagram-description" });
      svg.append(svgNode("title", { id: "catalog-diagram-title" }, "Recorded relationships between the selected objects"));
      svg.append(svgNode("desc", { id: "catalog-diagram-description" }, displayed.map(record => `${inputs(record).map(id => objects.get(id).name).join(" and ")} to ${objects.get(record.target).name}: ${record.kind}${isConstruction(record) ? " (construction or structural relationship)" : " (map)"}. ${record.conditions.join("; ")}`).join(" ")));
      const defs = svgNode("defs", {});
      for (const [name, className] of [["map", ""], ["construction", "catalog-construction-marker"]]) {
        const marker = svgNode("marker", { id: `catalog-arrow-${name}`, viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 5, markerHeight: 5, orient: "auto", class: className });
        marker.append(svgNode("path", { d: "M 0 0 L 10 5 L 0 10 z" }));
        defs.append(marker);
      }
      svg.append(defs);
      const middle = height / 2;
      const title = (name) => name.length > 27 ? `${name.slice(0, 25)}…` : name;
      const addNode = (x, id) => {
        svg.append(svgNode("rect", { x, y: middle - 25, width: 205, height: 50, rx: 9, class: "catalog-node" }));
        const label = svgNode("text", { x: x + 102.5, y: middle + 5, "text-anchor": "middle" }, title(objects.get(id).name));
        label.append(svgNode("title", {}, objects.get(id).name));
        svg.append(label);
      };
      addNode(same ? 35 : 15, state.source);
      if (!same) addNode(540, state.target);
      displayed.forEach((record, index) => {
        const isConstructed = isConstruction(record);
        const input = inputs(record).find(id => id === state.source || id === state.target) || record.source;
        const reverse = input !== state.source;
        const offset = (index - (displayed.length - 1) / 2) * 36;
        const path = same ? `M 240 ${middle - 10} C ${470 + index * 20} ${25 + index * 15}, ${470 + index * 20} ${height - 25 - index * 15}, 240 ${middle + 10}` : `M ${reverse ? 540 : 220} ${middle} Q 380 ${middle + offset * 2}, ${reverse ? 220 : 540} ${middle}`;
        svg.append(svgNode("path", { d: path, class: `catalog-edge${isConstructed ? " construction" : ""}${record.evidence.status === "conjectural" ? " conjectural" : ""}`, "marker-end": `url(#catalog-arrow-${isConstructed ? "construction" : "map"})`, "data-relationship-id": record.id }));
        const other = record.parameters?.other_input_id ? inputs(record).find(id => id !== input) || input : null;
        const label = `${humanize(record.kind)}${other ? ` (with ${title(objects.get(other).name)})` : ""}${record.conditions.length ? " *" : ""}`;
        svg.append(svgNode("text", { x: same ? 485 : 380, y: middle + offset - 6, "text-anchor": "middle", class: "catalog-edge-label" }, label));
      });
      wrapper.append(svg);
      if (records.length > 8) wrapper.append(el("p", `Showing 8 of ${records.length} recorded pair relationships.`, "catalog-muted"));
      if (records.some(record => record.conditions.length)) wrapper.append(el("p", "* Subject to the conditions recorded below.", "catalog-muted"));
    }

    function renderRelations() {
      const relIds = new Set([state.source, state.target].flatMap(id => [...(indexes.relationships_from[id] || []), ...(indexes.relationships_to[id] || []), ...(indexes.construction_inputs?.[id] || [])]));
      const all = [...relIds].map(id => relationships.get(id)).filter(matchesCategory);
      const pair = all.filter(record => (inputs(record).includes(state.source) && record.target === state.target) || (inputs(record).includes(state.target) && record.target === state.source));
      renderDiagram(pair);
      const ordered = [...pair, ...all.filter(record => !pair.includes(record))];
      const shown = ordered.slice(0, relationLimit);
      $("relations-status").textContent = `${all.length} relationship${all.length === 1 ? "" : "s"}`;
      const wrapper = $("relations");
      wrapper.replaceChildren();
      for (const record of shown) {
        const article = el("details", null, "catalog-record catalog-relation");
        article.dataset.relationshipId = record.id;
        const summary = el("summary");
        const heading = el("span", null, "catalog-relation-title");
        const source = objects.get(record.source), target = objects.get(record.target);
        const arrow = el("span", isConstruction(record) ? "⇢" : "→", "catalog-relation-arrow");
        arrow.dataset.construction = String(isConstruction(record));
        heading.append(el("span", source.name));
        if (record.parameters?.other_input_id) {
          const other = objects.get(record.parameters.other_input_id);
          heading.append(document.createTextNode(" + "), el("span", other.name));
        }
        heading.append(arrow, el("span", target.name));
        const badges = el("div", null, "catalog-badges");
        badges.append(badge(humanize(record.kind)), badge(isConstruction(record) ? "Structural" : categories.get(record.category_id).name));
        const proof = badge(humanize(record.evidence.status));
        proof.dataset.evidence = record.evidence.status;
        if (record.evidence.status === "conjectural") badges.append(proof);
        summary.append(heading, badges);
        article.append(summary, prose(record.statement), conditions(record.conditions));
        const footer = el("div", null, "catalog-record-footer");
        const explore = el("a", "Explore this pair");
        const params = new URLSearchParams({ source: record.source, target: record.target, operation: "hom" });
        if (record.category_id) params.set("category", record.category_id);
        explore.href = `/catalog/explorer/?${params}`;
        footer.append(knowlLink(record.knowl, "Explanation"), explore, knowlLink(source.knowl, "Source definition"), knowlLink(target.knowl, "Target definition"));
        if (record.parameters?.other_input_id) footer.append(knowlLink(objects.get(record.parameters.other_input_id).knowl, "Other input definition"));
        article.append(footer, evidence(record));
        wrapper.append(article);
      }
      if (!all.length) wrapper.append(el("p", "No related objects catalogued yet.", "catalog-empty"));
      if (all.length > shown.length) {
        const more = el("button", `Show ${Math.min(6, all.length - shown.length)} more (${all.length - shown.length} remaining)`, "catalog-show-more");
        more.type = "button";
        more.addEventListener("click", () => {
          const expanded = [...wrapper.querySelectorAll("details[data-relationship-id][open]")].map(node => node.dataset.relationshipId);
          relationLimit += 6; renderRelations();
          for (const node of wrapper.querySelectorAll("details[data-relationship-id]")) if (expanded.includes(node.dataset.relationshipId)) node.open = true;
          wrapper.querySelectorAll(".catalog-relation > summary")[shown.length]?.focus();
        });
        wrapper.append(more);
      }
    }

    function render(updateUrl = true) {
      const { common, sourceChoices, targetChoices } = reconcile();
      if (previousPair !== pairKey()) { relationLimit = 6; $("diagram-details").open = false; }
      previousPair = pairKey();
      $("operation").value = state.operation;
      $("target-card").hidden = state.operation !== "hom";
      $("object-cards").classList.toggle("catalog-single-object", state.operation !== "hom");
      renderCategory(common);
      renderView("source", sourceChoices); renderView("target", targetChoices);
      $("view-controls").hidden = $("source-view-field").hidden && $("target-view-field").hidden;
      renderObject("source"); renderObject("target");
      renderSpaces(); renderRelations();
      if (updateUrl) writeUrl();
    }

    for (const endpoint of ["source", "target"]) {
      $(`${endpoint}-view`).addEventListener("change", event => { state[`${endpoint}View`] = event.target.value; render(); });
    }
    $("picker-search").addEventListener("input", () => { pickerLimit = 40; renderPicker(); });
    $("picker-search").addEventListener("keydown", event => {
      if (event.key === "ArrowDown") { event.preventDefault(); $("picker-results").querySelector("button")?.focus(); }
      if (event.key === "Enter") { event.preventDefault(); $("picker-results").querySelector("button")?.click(); }
    });
    $("picker-results").addEventListener("keydown", event => {
      const options = [...$("picker-results").querySelectorAll("button")];
      const index = options.indexOf(document.activeElement);
      if (event.key === "ArrowDown") { event.preventDefault(); options[Math.min(index + 1, options.length - 1)]?.focus(); }
      if (event.key === "ArrowUp") { event.preventDefault(); (index > 0 ? options[index - 1] : $("picker-search")).focus(); }
      if (event.key === "Home") { event.preventDefault(); options[0]?.focus(); }
      if (event.key === "End") { event.preventDefault(); options.at(-1)?.focus(); }
    });
    $("picker-more").addEventListener("click", () => {
      const previous = pickerLimit; pickerLimit += 40; renderPicker();
      $("picker-results").querySelectorAll("button")[previous]?.focus();
    });
    $("picker").addEventListener("keydown", event => {
      if (event.key === "Escape") { event.preventDefault(); event.stopPropagation(); $("picker").close(); }
    });
    $("picker-close").addEventListener("click", () => $("picker").close());
    $("picker").addEventListener("close", () => $(`${pickerEndpoint}-change`).focus());
    $("operation").addEventListener("change", event => {
      if (state.operation === "hom") { homTarget = state.target; homTargetView = state.targetView; }
      state.operation = event.target.value;
      if (state.operation === "hom" && objects.has(homTarget)) { state.target = homTarget; state.targetView = homTargetView; }
      render();
    });
    $("category").addEventListener("change", event => { state.category = event.target.value; render(); });
    window.addEventListener("popstate", readUrl);
    readUrl();
    $("controls").hidden = false;
    $("status").textContent = "";
    $("status").hidden = true;
    $("finite-link").hidden = !sortedObjects.some(obj => obj.properties.finite_group);
    $("lie-link").hidden = !sortedObjects.some(obj => obj.properties.lie_group);
    $("counts").textContent = `${objects.size} objects · ${categories.size} categories · ${spaces.size} map descriptions`;
    root.dataset.catalogReady = "true";
  }

  start().catch(error => {
    $("status").textContent = `The explorer could not load: ${error.message}. The catalogue definitions remain available through the links above.`;
    $("status").setAttribute("role", "alert");
    console.error(error);
  });
}());
