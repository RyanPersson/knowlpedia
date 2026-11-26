"""Publish the self-contained declaration index supplied by the GRH content package."""
from collections import defaultdict
from html import escape
import json
from pathlib import Path
import re
import shutil
from zipfile import ZipFile

ALLOWED = re.compile(
    r"(?:records|source)/[0-9]+\.json\.gz|(?:modules|project|libraries)\.json\.gz|"
    r"manifest\.json|dependencies\.tsv\.gz|LICENSE|NOTICE|ATTRIBUTION\.md"
)
SOURCE = re.compile(r"github\.com/lsernau/grh-lean/blob/[0-9a-f]{40}/grh/src/([\w/]+)\.lean(?:#L(\d+))?")


def publish(content_root, out_dir, registry, html_document, profile):
    bundle = content_root / "grh-lean/declarations.zip"
    if not bundle.is_file() or "grh-lean" not in registry:
        return
    dest = out_dir / "grh-lean/declarations"
    data = dest / "data"
    with ZipFile(bundle) as archive:
        manifest = json.loads(archive.read("manifest.json"))
        if manifest["version"] != 1:
            raise ValueError("Unsupported GRH declaration index version")
        for info in archive.infolist():
            if not ALLOWED.fullmatch(info.filename):
                raise ValueError(f"Unexpected GRH declaration index entry {info.filename!r}")
            path = data / info.filename
            path.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, path.open("wb") as output:
                shutil.copyfileobj(source, output)
    guides = defaultdict(lambda: defaultdict(list))
    for knowl in registry.values():
        if knowl.id == "grh-lean" or knowl.kind == "index":
            continue
        for section in knowl.sections:
            markdown = section.get("markdown", "")
            if "lsernau/grh-lean/blob/" not in markdown:
                continue
            for mod, line in set(SOURCE.findall(markdown)):
                guides[mod.replace("/", ".")][line or "module"].append([knowl.id, knowl.title])
    (data / "guides.json").write_text(json.dumps(guides, ensure_ascii=False), encoding="utf-8")
    runtime = Path(__file__).resolve().parents[1] / "static-runtime"
    shutil.copyfile(runtime/"lean-declarations.js", out_dir/"assets/lean-declarations.js")
    shutil.copyfile(runtime/"lean-declarations.css", out_dir/"assets/lean-declarations.css")
    package_links = " ".join(
        f'<li><a href="{escape(url, quote=True)}/tree/{escape(ref, quote=True)}">{escape(name)}</a> '
        f'<code>{escape(ref[:10])}</code></li>'
        for name, (url, ref, _) in manifest["packages"].items()
    )
    preview = manifest.get("sourcePreview", False)
    description = (f'Browse {manifest["projectCount"]:,} named source declarations and their original proof comments. '
                   'The kernel-level dependency rebuild is in progress.' if preview else
                   f'The proof terms reach {manifest["closure"]:,} declarations.')
    library_option = '' if preview else '<option value="libraries">Mathlib and Lean dependencies</option>'
    graph_note = ('Source references in this preview are name matches. Every module links to its exact source and imports.'
                  if preview else 'The expression graph records constants in declaration types and proof or definition bodies. '
                  'Kernel blocks also include their constructors, recursors and reduction rules. Source-only helpers are labeled separately.')
    download = ('Download the named source inventory with file and line (compressed TSV)' if preview else
                'Download all proof declarations with their direct dependencies (compressed TSV)')
    body = f'''<main id="main-content" class="page-shell lean-reader"><article class="knowl-page">
<header class="page-header"><p><a href="/grh-lean/">Guided proof</a> ·
<a href="/grh-lean/dependencies/">Mathematical dependency index</a></p>
<h1>Lean declaration index</h1><p class="page-summary">Follow any of the five theorems through its definitions and lemmas.
{description} All {manifest["sourceModules"]} modules of the readable edition are available here.</p></header>
<label for="lean-query">Find a declaration or module</label>
<input id="lean-query" type="search" placeholder="e.g. star_inequality" autocomplete="off" spellcheck="false">
<div class="lean-controls"><label for="lean-scope">Search in</label>
<select id="lean-scope"><option value="project">Readable edition</option>{library_option}
<option value="modules">Source modules</option></select></div>
<p id="lean-status" aria-live="polite">Loading the declaration index…</p>
<div id="lean-results"></div><section id="lean-focus" aria-label="Selected declaration or module"></section>
<details class="lean-provenance"><summary>Packages, logical axioms and downloads</summary>
<p>Toolchain {escape(manifest["toolchain"])}. {graph_note}</p>
<p>The axioms are <code>propext</code>, <code>Classical.choice</code> and <code>Quot.sound</code>.</p><ul>{package_links}</ul>
<p><a href="data/dependencies.tsv.gz" download>{download}</a>.</p>
<p>Readable-edition source and comments are reproduced under Apache 2.0.
<a href="data/LICENSE">License</a> · <a href="data/NOTICE">Notice</a> · <a href="data/ATTRIBUTION.md">Attribution</a></p></details>
<noscript><p>Enable JavaScript for recursive unfolding. The declaration list above is available as a download.</p></noscript>
</article></main>'''
    page = html_document("Lean declaration index", body, profile=profile, page_script="lean-declarations.js")
    page = page.replace("</head>", '<link rel="stylesheet" href="/assets/lean-declarations.css">\n</head>', 1)
    (dest/"index.html").write_text(page, encoding="utf-8")
