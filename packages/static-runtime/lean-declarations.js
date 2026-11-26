/* Reader for the pinned, static declaration index. All source text stays text. */
(() => {
  "use strict";
  const input = document.getElementById("lean-query");
  if (!input) return;
  const scope = document.getElementById("lean-scope");
  const status = document.getElementById("lean-status");
  const results = document.getElementById("lean-results");
  const focus = document.getElementById("lean-focus");
  const cache = new Map();
  let meta, modules, guides, project, libraries;
  let lookup, moduleIds, displayed, generation = 0, shown = 35;

  function node(tag, text, className) {
    const result = document.createElement(tag);
    if (text !== undefined) result.textContent = text;
    if (className) result.className = className;
    return result;
  }
  function link(label, href) {
    const result = node("a", label);
    result.href = href;
    return result;
  }
  function hash(kind, value) {
    return "#" + kind + "=" + encodeURIComponent(value);
  }
  function data(file) {
    if (!cache.has(file)) {
      const promise = fetch("data/" + file).then(async response => {
        if (!response.ok) throw new Error("Could not load " + file);
        if (file.endsWith(".gz")) {
          const bytes = response.body.pipeThrough(new DecompressionStream("gzip"));
          return new Response(bytes).json();
        }
        return response.json();
      }).catch(error => { cache.delete(file); throw error; });
      cache.set(file, promise);
    }
    return cache.get(file);
  }
  async function loadLibraries() {
    if (libraries) return;
    const values = await data("libraries.json.gz");
    if (libraries) return;
    libraries = values;
    values.forEach((v, i) => lookup.set(v, meta.projectCount + i));
  }
  function nameOf(id) {
    return id < meta.projectCount ? project[id] : libraries[id - meta.projectCount];
  }
  async function record(id) {
    const shard = await data("records/" + Math.floor(id / meta.chunk) + ".json.gz");
    return shard[id % meta.chunk];
  }
  function disclosure(label, onOpen) {
    const element = node("details");
    element.append(node("summary", label));
    let busy = false, ready = false;
    element.addEventListener("toggle", async () => {
      if (!element.open || busy || ready) return;
      busy = true;
      const box = node("div", "Loading…", "lean-disclosure");
      element.append(box);
      try { await onOpen(box); ready = true; }
      catch (error) { box.textContent = error.message + ". Close and reopen to retry."; }
      finally { busy = false; if (!ready) element.addEventListener("toggle", () => box.remove(), {once:true}); }
    });
    return element;
  }
  function sourceURL(mod, line) {
    const [module, repo] = modules[mod];
    const [url, ref, prefix] = meta.packages[repo];
    return url + "/blob/" + ref + "/" + prefix + module.replaceAll(".", "/") + ".lean" +
           (line === undefined ? "" : "#L" + (line + 1));
  }
  function knowlLinks(box, records) {
    if (!records || !records.length) return;
    const line = node("p", "Read in Knowlpedia · ");
    records.forEach(([id,title], i) => {
      if (i) line.append(" · ");
      const a = link(title, "/" + id + "/");
      a.className = "knowl";
      a.dataset.knowl = "/fragments/" + id + "/core.html";
      a.setAttribute("aria-expanded", "false");
      line.append(a);
    });
    box.append(line);
  }
  function annotatedCode(raw, first, last, occurrences, trail) {
    const owner = node("div");
    const code = node("pre", undefined, "lean-code");
    const slot = node("div");
    let cursor = first, active;
    for (const [left, right, id] of occurrences) {
      if (left < cursor || right > last) continue;
      code.append(raw.slice(cursor, left));
      const term = node("button", raw.slice(left, right), "lean-term");
      term.type = "button";
      term.setAttribute("aria-expanded", "false");
      term.addEventListener("click", async () => {
        const previous = active;
        if (previous) previous.setAttribute("aria-expanded", "false");
        slot.replaceChildren();
        if (previous === term) { active = undefined; return; }
        active = term;
        term.setAttribute("aria-expanded", "true");
        const panel = node("div", "Loading…", "lean-inline");
        slot.append(panel);
        try {
          if (id >= meta.projectCount) await loadLibraries();
          if (trail.has(id)) panel.replaceChildren(link(nameOf(id), hash("decl",nameOf(id))));
          else await fillDeclaration(panel,id,trail);
        } catch (error) { panel.textContent = error.message; }
      });
      code.append(term);
      cursor = right;
    }
    code.append(raw.slice(cursor,last));
    owner.append(code,slot);
    return owner;
  }
  function sourceDisplay(box, source, span, kind, trail) {
    if (!span.length) return;
    const [first, col, last, endCol] = span;
    const selected = source.lines.slice(first,last+1);
    // Lean LSP columns count UTF-16 code units, as does JavaScript's slice.
    if (selected.length === 1) selected[0] = selected[0].slice(col,endCol);
    else {
      selected[selected.length-1] = selected[selected.length-1].slice(0,endCol);
      selected[0] = selected[0].slice(col);
    }
    const occurrences = [];
    let offset = 0;
    selected.forEach((line, i) => {
      const trim = i === 0 ? col : 0;
      for (const [l,r,target] of source.uses[first+i] || []) {
        if (l >= trim && r <= trim+line.length) occurrences.push([offset+l-trim,offset+r-trim,target]);
      }
      offset += line.length+1;
    });
    const raw = selected.join("\n");
    let code = raw.trim();
    const doc = /^(?:@\[[^\n]*\]\s*)?\/--\s*([\s\S]*?)\s*-\//.exec(code);
    if (doc) {
      box.append(node("p", doc[1].replace(/\s*\n(?!\n|[-*] )/g," ").replaceAll("`","").trim(), "lean-doc"));
      code = code.slice(doc[0].length).trim();
    }
    const theorem = kind === "theorem" || /^(?:private\s+|protected\s+)?(?:lemma|theorem)\s/m.test(code);
    const proof = theorem ? /\s+:=\s*|\s+where\s*\n/.exec(code) : null;
    const statement = proof ? code.slice(0,proof.index).trim() : code;
    const start = raw.lastIndexOf(code);
    if (statement) box.append(annotatedCode(raw,start,start+statement.length,occurrences,trail));
    if (proof) {
      const comments = code.slice(proof.index).split("\n");
      const groups = [];
      let previous = false, indent = -1;
      for (const line of comments) {
        const match = /^(\s*)--\s?(.*)$/.exec(line);
        if (match) {
          if (!previous || indent !== match[1].length) groups.push(match[2]);
          else groups[groups.length-1] += " " + match[2];
          indent = match[1].length;
        }
        previous = !!match;
      }
      if (groups.length) box.append(disclosure("Proof in the authors’ comments", panel => {
        const list = node("ol");
        groups.forEach(p => list.append(node("li",p.replaceAll("`",""))));
        panel.replaceChildren(list);
      }));
      box.append(disclosure("Formal proof", panel => panel.replaceChildren(
        annotatedCode(raw,start+proof.index,start+code.length,occurrences,trail))));
    }
  }
  function dependencyList(ids, trail) {
    const list = node("div", undefined, "lean-children");
    for (const id of ids) {
      const name = nameOf(id);
      if (trail.has(id)) {
        const p = node("p","Already open above · ");
        p.append(link(name,hash("decl", name)));
        list.append(p);
      } else {
        list.append(disclosure(name, box => fillDeclaration(box,id,trail)));
      }
    }
    return list;
  }
  async function fillDeclaration(box,id,parents) {
    const [mi,kind,mask,span,deps,block] = await record(id);
    const [mod,repo] = modules[mi];
    const name = nameOf(id);
    const panel = node("div");
    const trail = new Set(parents);
    trail.add(id);
    const heading = node("p",meta.kinds[kind] + " · ", "lean-meta");
    heading.append(link(mod,hash("module", mod)), " · ",link("Permalink",hash("decl",name)),
      " · ",link("Pinned source",sourceURL(mi,span.length ? (span[4] ?? span[0]) : undefined)));
    panel.append(heading);
    if (repo === "grh") {
      const code = await data("source/"+mi+".json.gz");
      const lookupGuides = guides[mod] || {};
      knowlLinks(panel, lookupGuides[String((span[4] ?? span[0]) + 1)]);
      sourceDisplay(panel,code,span,meta.kinds[kind],trail);
      if (!span.length) panel.append(node("p","Lean generated this declaration during elaboration. The module source and its formal dependencies are available here."));
    }
    if (mask || meta.sourcePreview) {
      for (const [title,children] of [[meta.sourcePreview ? "Named source references" : "Direct dependencies",deps],["Kernel block members",block]]) {
        if (children.length) panel.append(disclosure(title+" ("+children.length+")",async target => {
          if (children.some(x=>x>=meta.projectCount)) await loadLibraries();
          target.replaceChildren(dependencyList(children,trail));
        }));
      }
      if (!meta.sourcePreview && !deps.length && !block.length) panel.append(node("p","This declaration has no further dependencies."));
      if (!meta.sourcePreview) panel.append(disclosure("Public theorems using this declaration",target=>{
        const ul = node("ul");
        meta.roots.forEach((root,j) => {
          if (mask & (1<<j)) { const li = node("li"); li.append(link(nameOf(root),hash("decl",nameOf(root)))); ul.append(li); }
        });
        target.replaceChildren(ul);
      }));
    } else {
      panel.append(node("p","Additional source declaration outside the dependency closure of the five public theorems."));
    }
    box.replaceChildren(panel);
  }
  async function showModule(box, mi) {
    const [mod,repo,imports,members] = modules[mi];
    box.append(link("Pinned source",sourceURL(mi)));
    knowlLinks(box,(guides[mod]||{}).module);
    box.append(disclosure("Direct imports ("+imports.length+")", target=>{
      const list=node("ul");
      imports.forEach(n=>{
        const li=node("li");
        if (moduleIds.has(n)) li.append(link(n,hash("module",n))); else li.textContent=n;
        list.append(li);
      });
      target.replaceChildren(list);
    }));
    box.append(disclosure("Declarations ("+members.length+")",async target=>{
      if (repo!=="grh") await loadLibraries();
      target.replaceChildren(dependencyList(members,new Set()));
    }));
    if (repo==="grh") box.append(disclosure("Complete module source",async target=>{
      const code=await data("source/"+mi+".json.gz");
      target.replaceChildren(node("pre",code.lines.join("\n"),"lean-code"));
    }));
  }
  async function render() {
    const version=++generation;
    const params=new URLSearchParams(location.hash.slice(1));
    let selected=params.get("decl"), mod=params.get("module");
    const at=params.get("source");
    if (at) {
      const marker=at.lastIndexOf(":");
      const module=at.slice(0,marker), line=Number(at.slice(marker+1));
      if (moduleIds.has(module) && Number.isInteger(line) && line>0) {
        const members=modules[moduleIds.get(module)][3];
        const positions=await Promise.all(members.map(async id=>[id,(await record(id))[3]]));
        const match=positions.find(([,range])=>range[4]===line-1) ||
          positions.find(([,range])=>range.length>=6 && range[0]<=line-1 && range[2]>=line-1);
        if (match) selected=nameOf(match[0]); else mod=module;
      }
    }
    if (scope.value==="libraries" || (selected && !lookup.has(selected))) await loadLibraries();
    if (version!==generation) return;
    const term=input.value.trim().toLowerCase();
    const isModule=scope.value==="modules";
    const pool=isModule ? modules.filter(m=>m[1]==="grh").map(m=>m[0]) :
      scope.value==="libraries" ? libraries : project;
    const defaults=!term && scope.value==="project";
    const matches=defaults ? meta.rootNames : pool.filter(n=>n.toLowerCase().includes(term));
    const list=node("ul",undefined,"lean-matches");
    matches.slice(0,shown).forEach(n=>{
      const item=node("li");
      item.append(link(n,hash(isModule ? "module" : "decl",n)));
      list.append(item);
    });
    results.replaceChildren(list);
    if (shown<matches.length) {
      const more=node("button","Show more");
      more.type="button"; more.onclick=()=>{shown+=50; update();};
      results.append(more);
    }
    status.textContent=defaults ? "Five public theorems" : matches.length.toLocaleString()+" matches";
    const selection=selected ?? mod;
    const selectionKey=selected ? 'decl:'+selected : mod ? 'module:'+mod : null;
    if (selectionKey===displayed) return;
    displayed=selectionKey;
    focus.replaceChildren();
    if (selection===null) return;
    const title=node("h2",selection);
    const panel=node("div","Loading…");
    focus.append(title,panel);
    if (selected && lookup.has(selected)) await fillDeclaration(panel,lookup.get(selected),new Set());
    else if (mod && moduleIds.has(mod)) { panel.replaceChildren(); await showModule(panel,moduleIds.get(mod)); }
    else panel.textContent="No declaration or module has this name in this edition.";
    if (version===generation && document.activeElement!==input) focus.scrollIntoView({block:"nearest"});
  }
  function update() { render().catch(error => {status.textContent=error.message;}); }
  async function init() {
    [meta,modules,guides,project]=await Promise.all([data("manifest.json"),data("modules.json.gz"),data("guides.json"),data("project.json.gz")]);
    lookup=new Map(project.map((n,i)=>[n,i]));
    moduleIds=new Map(modules.map((m,i)=>[m[0],i]));
    let timer;
    input.addEventListener("input",()=>{clearTimeout(timer);shown=35;timer=setTimeout(update,100);});
    scope.addEventListener("change",()=>{shown=35;update();});
    window.addEventListener("hashchange",update);
    update();
  }
  init().catch(e=>{status.textContent="The declaration index could not be loaded. "+e.message;});
})();
