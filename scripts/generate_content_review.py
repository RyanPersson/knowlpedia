#!/usr/bin/env python3
"""Generate a side-by-side review site for substantive knowl edits."""

from __future__ import annotations

import argparse
import difflib
import html
import io
import re
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from packages.compiler import knowl_compile as compiler  # noqa: E402


INLINE_TOKEN = "\x01INLINE_MATH_DELIMITER\x01"
DISPLAY_TOKEN = "\x01DISPLAY_MATH_DELIMITER\x01"


@dataclass
class ReviewItem:
    index: int
    path: str
    old_text: str
    current_text: str
    old_knowl: compiler.Knowl
    current_knowl: compiler.Knowl
    filename: str


def git(*args: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=check,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def normalize_delimiters(text: str) -> str:
    """Make supported delimiter spellings equivalent without changing other text."""

    text = text.replace(r"\[", DISPLAY_TOKEN).replace(r"\]", DISPLAY_TOKEN)
    text = re.sub(r"(?<!\\)\$\$", DISPLAY_TOKEN, text)
    text = text.replace(r"\(", INLINE_TOKEN).replace(r"\)", INLINE_TOKEN)
    return re.sub(r"(?<!\\)\$", INLINE_TOKEN, text)


def canonicalize_delimiters(text: str) -> str:
    """Use dollar delimiters in the source diff so delimiter churn disappears."""

    return (
        text.replace(r"\[", "$$")
        .replace(r"\]", "$$")
        .replace(r"\(", "$")
        .replace(r"\)", "$")
    )


def parse_text(text: str, label: str) -> compiler.Knowl:
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".knowl.md",
        prefix="knowl-review-",
    ) as source:
        source.write(text)
        source.flush()
        return compiler.parse_single_file(Path(source.name))


def render_complete_knowl(knowl: compiler.Knowl, registry: dict[str, compiler.Knowl]) -> str:
    parts = [
        '<article class="review-knowl">',
        '<header class="review-knowl-header">',
        f'<p class="kind">{html.escape(compiler.display_kind(knowl.kind))}</p>',
        f"<h1>{compiler.render_inline(knowl.title, registry)}</h1>",
        f'<p class="page-summary">{compiler.render_inline(knowl.summary, registry)}</p>',
        "</header>",
        '<section class="review-core">',
        compiler.render_markdown(
            compiler.without_redundant_leading_h1(knowl.core_markdown),
            registry,
        ),
        compiler.render_structured_core(knowl, registry),
        "</section>",
    ]
    for section in knowl.sections:
        parts.extend(
            [
                '<section class="review-section">',
                f"<h2>{compiler.render_section_title(section['title'], registry)}</h2>",
                compiler.render_section(section, registry),
                "</section>",
            ]
        )
    parts.extend([compiler.render_relations(knowl, registry), "</article>"])
    return "\n".join(part for part in parts if part)


def source_diff(
    old_text: str,
    current_text: str,
    left_label: str = "HEAD",
    right_label: str = "Working tree",
) -> str:
    differ = difflib.HtmlDiff(tabsize=2, wrapcolumn=96)
    return differ.make_table(
        canonicalize_delimiters(old_text).splitlines(),
        canonicalize_delimiters(current_text).splitlines(),
        fromdesc=left_label,
        todesc=right_label,
        context=True,
        numlines=3,
    )


def common_head(title: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <script>
    (function () {{
      try {{
        var theme = localStorage.getItem("knowl-theme");
        if (theme !== "dark" && theme !== "light") {{
          theme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
        }}
        document.documentElement.dataset.theme = theme;
        var palette = localStorage.getItem("knowl-palette");
        var palettes = ["current", "original", "washi", "sumi", "aizome"];
        if (palettes.indexOf(palette) === -1) palette = "current";
        document.documentElement.dataset.palette = palette;
      }} catch (error) {{}}
    }}());
  </script>
  <link rel="stylesheet" href="/assets/katex.min.css">
  <link rel="stylesheet" href="/assets/knowl.css">
"""


def item_styles() -> str:
    return """
  <style>
    :root { color-scheme: light dark; }
    body { margin: 0; background: var(--canvas); color: var(--ink); }
    .review-toolbar {
      position: sticky; top: 0; z-index: 10; display: flex; align-items: center;
      justify-content: space-between; gap: 1rem; padding: .7rem 1rem;
      border-bottom: 1px solid var(--line);
      background: color-mix(in srgb, var(--surface) 94%, transparent);
      color: var(--ink);
      backdrop-filter: blur(10px);
    }
    .review-toolbar p { margin: 0; min-width: 0; }
    .review-path { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .review-toolbar a { white-space: nowrap; }
    .comparison {
      display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
      gap: 1px; background: var(--line);
    }
    .version { min-width: 0; background: var(--surface); color: var(--ink); }
    .version-label {
      position: sticky; top: 49px; z-index: 5; margin: 0; padding: .55rem 1.25rem;
      border-bottom: 1px solid var(--line);
      background: var(--surface); color: var(--ink);
      font-size: .8rem; letter-spacing: .08em;
      text-transform: uppercase;
    }
    .version-current .version-label { color: var(--accent-strong); }
    .review-knowl { max-width: 52rem; margin: 0 auto; padding: 1.5rem 1.5rem 4rem; }
    .review-knowl-header { margin-bottom: 1.5rem; }
    .review-knowl-header h1 { margin: .15rem 0 .5rem; overflow-wrap: anywhere; }
    .review-section { margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--line); }
    .review-section h2 { font-size: 1.25rem; }
    .source-diff {
      margin: 0; padding: 1.25rem; border-top: 1px solid var(--line);
      background: var(--canvas); color: var(--ink);
    }
    .source-diff summary { cursor: pointer; font-weight: 700; }
    .diff-wrap { margin-top: 1rem; overflow: auto; background: var(--surface); }
    table.diff { width: 100%; border-collapse: collapse; font: 12px/1.45 ui-monospace, monospace; }
    table.diff td, table.diff th { padding: .1rem .35rem; vertical-align: top; white-space: pre-wrap; overflow-wrap: anywhere; }
    .diff_header { background: var(--surface-strong); color: var(--ink); }
    .diff_next { display: none; }
    .diff_add { background: var(--accent-soft); color: var(--ink); }
    .diff_chg { background: var(--warning-soft); color: var(--ink); }
    .diff_sub { background: var(--surface-strong); color: var(--ink); }
    @media (max-width: 850px) {
      .comparison { grid-template-columns: 1fr; }
      .version-label { position: static; }
      .review-toolbar { align-items: flex-start; }
    }
  </style>
</head>
"""


def index_styles() -> str:
    return """
  <style>
    html, body { height: 100%; }
    body { margin: 0; overflow: hidden; background: var(--canvas); color: var(--ink); }
    .review-app { display: grid; grid-template-columns: minmax(18rem, 25rem) 1fr; height: 100vh; }
    .review-sidebar {
      display: flex; min-height: 0; flex-direction: column;
      border-right: 1px solid var(--line);
      background: var(--surface);
    }
    .review-heading { padding: 1rem; border-bottom: 1px solid var(--line); }
    .review-heading h1 { margin: .15rem 0 .4rem; font-size: 1.35rem; }
    .review-heading p { margin: 0; color: var(--muted); }
    .review-search {
      box-sizing: border-box; width: calc(100% - 2rem); margin: 1rem;
      padding: .7rem .8rem; border: 1px solid var(--line-strong);
      border-radius: .45rem; background: var(--surface); color: var(--ink);
    }
    .review-count { margin: 0 1rem .65rem; font-size: .85rem; color: var(--muted); }
    .review-list { min-height: 0; margin: 0; padding: 0; overflow: auto; list-style: none; }
    .review-link {
      display: block; padding: .72rem 1rem; border-top: 1px solid var(--line);
      color: inherit; text-decoration: none;
    }
    .review-link:hover, .review-link.active { background: var(--accent-soft); }
    .review-link.active { box-shadow: inset 3px 0 var(--accent); }
    .review-title { display: block; font-weight: 700; }
    .review-file { display: block; margin-top: .2rem; color: var(--muted); font-size: .75rem; overflow-wrap: anywhere; }
    .review-main { min-width: 0; min-height: 0; }
    .review-frame { width: 100%; height: 100%; border: 0; background: var(--surface); }
    @media (max-width: 760px) {
      body { overflow: auto; }
      .review-app { grid-template-columns: 1fr; grid-template-rows: auto 75vh; height: auto; min-height: 100vh; }
      .review-sidebar { max-height: 45vh; border-right: 0; border-bottom: 1px solid var(--line); }
    }
  </style>
</head>
"""


def render_item_page(
    item: ReviewItem,
    registry: dict[str, compiler.Knowl],
    total: int,
    left_label: str = "HEAD · original",
    right_label: str = "Working tree · edited",
) -> str:
    title = item.current_knowl.title
    knowl_href = "/" + item.current_knowl.id.strip("/") + "/"
    return (
        common_head(f"{title} — content review")
        + item_styles()
        + f"""<body>
  <header class="review-toolbar">
    <p class="review-path"><strong>{item.index + 1} of {total}</strong> · {html.escape(item.path)}</p>
    <a href="{html.escape(knowl_href)}" target="_top">Open current knowl ↗</a>
  </header>
  <main class="comparison">
    <section class="version version-head" aria-label="HEAD version">
      <h2 class="version-label">{html.escape(left_label)}</h2>
      {render_complete_knowl(item.old_knowl, registry)}
    </section>
    <section class="version version-current" aria-label="Working tree version">
      <h2 class="version-label">{html.escape(right_label)}</h2>
      {render_complete_knowl(item.current_knowl, registry)}
    </section>
  </main>
  <details class="source-diff">
    <summary>Delimiter-normalized source diff</summary>
    <div class="diff-wrap">{source_diff(item.old_text, item.current_text, left_label, right_label)}</div>
  </details>
</body>
</html>
"""
    )


def render_index(
    items: list[ReviewItem],
    head: str,
    heading: str = "Non-delimiter edits",
    description: str | None = None,
) -> str:
    entries = []
    for item in items:
        entries.append(
            f"""<li>
  <a class="review-link" href="items/{html.escape(item.filename)}"
     data-target="items/{html.escape(item.filename)}"
     data-search="{html.escape((item.current_knowl.title + ' ' + item.path).lower())}">
    <span class="review-title">{html.escape(item.current_knowl.title)}</span>
    <span class="review-file">{html.escape(item.path.removeprefix('content/'))}</span>
  </a>
</li>"""
        )
    first = f"items/{items[0].filename}" if items else ""
    return (
        common_head("Knowlpedia substantive edit review")
        + index_styles()
        + f"""<body>
  <main class="review-app">
    <aside class="review-sidebar">
      <header class="review-heading">
        <p class="kind">Content review</p>
        <h1>{html.escape(heading)}</h1>
        <p>{html.escape(description or f"{len(items)} knowls · HEAD {head}")}</p>
      </header>
      <input class="review-search" id="review-search" type="search"
             placeholder="Filter by title or path…" autocomplete="off">
      <p class="review-count" id="review-count">{len(items)} visible</p>
      <ol class="review-list" id="review-list">
        {''.join(entries)}
      </ol>
    </aside>
    <section class="review-main" aria-label="Side-by-side comparison">
      <iframe class="review-frame" id="review-frame" name="review-frame"
              src="{html.escape(first)}" title="Kn​​owl comparison"></iframe>
    </section>
  </main>
  <script>
    const search = document.getElementById("review-search");
    const count = document.getElementById("review-count");
    const frame = document.getElementById("review-frame");
    const links = Array.from(document.querySelectorAll(".review-link"));
    function select(link, updateHash = true) {{
      links.forEach(item => item.classList.toggle("active", item === link));
      frame.src = link.dataset.target;
      if (updateHash) history.replaceState(null, "", "#" + encodeURIComponent(link.dataset.target));
    }}
    links.forEach(link => link.addEventListener("click", event => {{
      event.preventDefault();
      select(link);
    }}));
    search.addEventListener("input", () => {{
      const query = search.value.trim().toLowerCase();
      let visible = 0;
      links.forEach(link => {{
        const show = !query || link.dataset.search.includes(query);
        link.closest("li").hidden = !show;
        if (show) visible += 1;
      }});
      count.textContent = visible + " visible";
    }});
    const requested = decodeURIComponent(location.hash.slice(1));
    const initial = links.find(link => link.dataset.target === requested) || links[0];
    if (initial) select(initial, false);
  </script>
</body>
</html>
"""
    )


def build(content_repo: Path, output: Path) -> int:
    changed = git("diff", "--name-only", "-z", "--", "content", cwd=content_repo).stdout
    paths = [path for path in changed.decode().split("\0") if path.endswith(".knowl.md")]
    substantive: list[tuple[str, str, str]] = []
    for path in paths:
        old = git("show", f"HEAD:{path}", cwd=content_repo).stdout.decode()
        current = (content_repo / path).read_text(encoding="utf-8")
        if normalize_delimiters(old) != normalize_delimiters(current):
            substantive.append((path, old, current))

    current_knowls = compiler.discover_knowls(content_repo / "content")
    registry = {knowl.id: knowl for knowl in current_knowls}
    items: list[ReviewItem] = []
    for index, (path, old, current) in enumerate(substantive):
        old_knowl = parse_text(old, f"HEAD:{path}")
        current_knowl = compiler.parse_single_file(content_repo / path)
        safe_id = re.sub(r"[^a-z0-9-]+", "-", current_knowl.id.lower()).strip("-")
        items.append(
            ReviewItem(
                index=index,
                path=path,
                old_text=old,
                current_text=current,
                old_knowl=old_knowl,
                current_knowl=current_knowl,
                filename=f"{index + 1:04d}-{safe_id}.html",
            )
        )

    item_dir = output / "items"
    item_dir.mkdir(parents=True, exist_ok=True)
    for stale in item_dir.glob("*.html"):
        stale.unlink()
    for item in items:
        (item_dir / item.filename).write_text(
            render_item_page(item, registry, len(items)),
            encoding="utf-8",
        )

    head = git("rev-parse", "--short", "HEAD", cwd=content_repo).stdout.decode().strip()
    (output / "index.html").write_text(render_index(items, head), encoding="utf-8")
    print(f"Generated {len(items)} comparisons at {output / 'index.html'}")
    return len(items)


def extract_ref(content_repo: Path, ref: str, destination: Path) -> None:
    archive = git("archive", ref, "content", cwd=content_repo).stdout
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(destination)


def modified_knowl_paths(content_repo: Path, left_ref: str, right_ref: str) -> list[str]:
    """Return knowl paths modified in place between two refs.

    Added and deleted files cannot form a two-version comparison, so this
    deliberately excludes them.
    """

    changed = git(
        "diff",
        "--diff-filter=M",
        "--name-only",
        "-z",
        left_ref,
        right_ref,
        "--",
        "content",
        cwd=content_repo,
    ).stdout
    return [
        path
        for path in changed.decode().split("\0")
        if path.endswith(".knowl.md")
    ]


def path_exists_at_ref(content_repo: Path, ref: str, path: str) -> bool:
    return git("cat-file", "-e", f"{ref}:{path}", cwd=content_repo, check=False).returncode == 0


def build_ref_comparison(
    content_repo: Path,
    output: Path,
    left_ref: str,
    right_ref: str,
    paths_file: Path | None,
    left_label: str,
    right_label: str,
    heading: str,
) -> int:
    if paths_file:
        requested_paths = [
            line.strip()
            for line in paths_file.read_text(encoding="utf-8").splitlines()
            if line.strip().endswith(".knowl.md")
        ]
        paths = [
            path
            for path in requested_paths
            if path_exists_at_ref(content_repo, left_ref, path)
            and path_exists_at_ref(content_repo, right_ref, path)
        ]
    else:
        paths = modified_knowl_paths(content_repo, left_ref, right_ref)
    with tempfile.TemporaryDirectory(prefix="knowl-review-ref-") as temp:
        right_tree = Path(temp)
        extract_ref(content_repo, right_ref, right_tree)
        right_knowls = compiler.discover_knowls(right_tree / "content")
        registry = {knowl.id: knowl for knowl in right_knowls}

        items: list[ReviewItem] = []
        for index, path in enumerate(paths):
            left = git("show", f"{left_ref}:{path}", cwd=content_repo).stdout.decode()
            right = git("show", f"{right_ref}:{path}", cwd=content_repo).stdout.decode()
            left_knowl = parse_text(left, f"{left_ref}:{path}")
            right_knowl = parse_text(right, f"{right_ref}:{path}")
            safe_id = re.sub(r"[^a-z0-9-]+", "-", right_knowl.id.lower()).strip("-")
            items.append(
                ReviewItem(
                    index=index,
                    path=path,
                    old_text=left,
                    current_text=right,
                    old_knowl=left_knowl,
                    current_knowl=right_knowl,
                    filename=f"{index + 1:04d}-{safe_id}.html",
                )
            )

    item_dir = output / "items"
    item_dir.mkdir(parents=True, exist_ok=True)
    for stale in item_dir.glob("*.html"):
        stale.unlink()
    for item in items:
        (item_dir / item.filename).write_text(
            render_item_page(
                item,
                registry,
                len(items),
                left_label=left_label,
                right_label=right_label,
            ),
            encoding="utf-8",
        )

    description = f"{len(items)} knowls · {left_label} vs {right_label}"
    (output / "index.html").write_text(
        render_index(items, f"{left_ref}..{right_ref}", heading, description),
        encoding="utf-8",
    )
    print(f"Generated {len(items)} comparisons at {output / 'index.html'}")
    return len(items)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-repo",
        type=Path,
        default=ROOT.parent / "knowlpedia-content",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "public-imported" / "review" / "non-delimiter-edits",
    )
    parser.add_argument("--left-ref")
    parser.add_argument("--right-ref")
    parser.add_argument(
        "--paths-from",
        type=Path,
        help="Optional newline-delimited subset of knowl paths for a ref comparison",
    )
    parser.add_argument("--left-label")
    parser.add_argument("--right-label")
    parser.add_argument("--heading", default="Content comparison")
    args = parser.parse_args()
    if bool(args.left_ref) != bool(args.right_ref):
        parser.error("--left-ref and --right-ref must be used together")
    if args.paths_from and not args.left_ref:
        parser.error("--paths-from requires --left-ref and --right-ref")
    if args.left_ref:
        count = build_ref_comparison(
            args.content_repo.resolve(),
            args.output.resolve(),
            args.left_ref,
            args.right_ref,
            args.paths_from.resolve() if args.paths_from else None,
            args.left_label or args.left_ref,
            args.right_label or args.right_ref,
            args.heading,
        )
    else:
        count = build(args.content_repo.resolve(), args.output.resolve())
    if not count:
        print("No substantive knowl edits found.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
