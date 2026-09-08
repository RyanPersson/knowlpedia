#!/usr/bin/env python3
"""Generate a side-by-side review site for substantive knowl edits."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import dataclass, field
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
    old_knowl: compiler.Knowl | None
    current_knowl: compiler.Knowl | None
    filename: str
    change_kind: str = "modified"
    review_notes: list[dict] = field(default_factory=list)
    notes_ref: str = "Working tree"


def load_review_notes(tree: Path) -> dict[str, list[dict]]:
    """Load recorded reviews, never triage records or inferred explanations."""
    by_id: dict[str, list[dict]] = {}
    for path in sorted((tree / "reviews" / "dependency-structure").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for index, record in enumerate(data.get("reviews", [])):
            if not record.get("id") or not any(record.get(key) for key in ("evidence", "changes", "reason")):
                continue
            by_id.setdefault(record["id"], []).append({
                "ledger": path.relative_to(tree).as_posix(),
                "record_index": index,
                "record": record,
            })
    return by_id


def attach_review_notes(items: list[ReviewItem], tree: Path, source_ref: str) -> None:
    notes = load_review_notes(tree)
    for item in items:
        ids = {knowl.id for knowl in (item.current_knowl, item.old_knowl) if knowl}
        item.review_notes = [note for kid in sorted(ids) for note in notes.get(kid, [])]
        item.notes_ref = source_ref


def note_matches_item(note: dict, item: ReviewItem) -> bool:
    text = item.current_text if item.current_knowl else item.old_text
    return note["record"].get("source_sha256") == hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_review_notes(items: list[ReviewItem], output: Path) -> None:
    """Export the original records and their provenance alongside the comparison."""
    directory = output / "notes"
    directory.mkdir(parents=True, exist_ok=True)
    for stale in directory.glob("*.json"):
        stale.unlink()
    for item in items:
        payload = {
            "path": item.path,
            "ledger_revision": item.notes_ref,
            "matching_source": "baseline" if item.current_knowl is None else "proposed",
            "records": [{**note, "matches_displayed_source": note_matches_item(note, item)}
                        for note in item.review_notes],
        }
        (directory / Path(item.filename).with_suffix(".json")).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
        )


def render_review_notes(item: ReviewItem, registry: dict[str, compiler.Knowl]) -> str:
    def record_html(note: dict) -> str:
        record = note["record"]
        labels = {"corrected": "Correction recorded", "reviewed_unchanged": "Reviewed unchanged",
                  "blocked": "Unresolved finding"}
        label = labels.get(record.get("outcome"), "Review note")
        if record.get("scope") == "targeted":
            label += " · targeted check"
        paragraphs = []
        seen = set()
        for key in ("changes", "reason", "evidence"):
            values = record.get(key, [])
            for value in values if isinstance(values, list) else [values]:
                if isinstance(value, str) and value.strip() and value not in seen:
                    paragraphs.append(f'<p class="review-reason-text">{html.escape(value)}</p>')
                    seen.add(value)
        sources = record.get("sources", [])
        if sources:
            paragraphs.append('<p><strong>Recorded sources:</strong></p><ul>')
            for source in sources:
                text = source if isinstance(source, str) else json.dumps(source, ensure_ascii=False)
                escaped = html.escape(text)
                link = (f'<a href="{escaped}" target="_blank" rel="noopener noreferrer">{escaped}</a>'
                        if text.startswith(("https://", "http://")) else escaped)
                paragraphs.append(f"<li>{link}</li>")
            paragraphs.append("</ul>")
        return (f'<article class="review-note"><p class="review-note-label">{label}</p>'
                + "".join(paragraphs)
                + f'<p class="review-note-source">{html.escape(note["ledger"])} · record {note["record_index"] + 1}</p></article>')

    matching = [note for note in item.review_notes if note_matches_item(note, item)]
    other = [note for note in item.review_notes if not note_matches_item(note, item)]
    priority = {"blocked": 0, "corrected": 1, "reviewed_unchanged": 2}
    matching.sort(key=lambda note: priority.get(note["record"].get("outcome"), 3))
    parts = ['<section class="review-reasons" aria-labelledby="review-reasons-heading">',
             '<h2 id="review-reasons-heading">Why this changed</h2>',
             '<p class="review-note-context">Saved review notes explain the change and the checks made. '
             'They describe the knowl as a whole, rather than each individual diff line.</p>']
    if matching:
        version = "baseline" if item.current_knowl is None else "proposed"
        parts.append(f'<p class="review-note-status">Notes matching the displayed {version} source</p>')
        parts.extend(record_html(note) for note in matching)
    else:
        parts.append('<p class="review-note-status">No saved note matches this exact source revision.</p>')
    if other:
        # When these are the only explanations available, expose them immediately.
        opened = "" if matching else " open"
        parts.append(f'<details class="review-note-history"{opened}><summary>Notes for other source versions ({len(other)})</summary>'
                     '<p>These notes may explain earlier edits, including decisions that were subsequently revised. '
                     'They are not verification of the displayed source.</p>')
        parts.extend(record_html(note) for note in other)
        parts.append('</details>')
    if not item.review_notes:
        parts.append('<p>No justification was recorded in the dependency review ledgers for this knowl.</p>')

    old = set(item.old_knowl.prerequisites if item.old_knowl else [])
    new = set(item.current_knowl.prerequisites if item.current_knowl else [])
    if old != new:
        parts.append('<details class="review-prerequisite-changes"><summary>Prerequisite changes</summary>'
                     '<p>Prerequisites are concepts needed to understand the opening definition or theorem. '
                     'Removing one from this list does not remove its ordinary links from the text.</p>')
        for label, targets in (("Added", new - old), ("Removed", old - new)):
            if not targets:
                continue
            parts.append(f'<p><strong>{label}</strong></p><ul>')
            for target in sorted(targets):
                knowl = registry.get(target)
                title = knowl.title if knowl else target
                parts.append(f'<li><a href="{html.escape(compiler.target_href(target))}" target="_blank" '
                             f'rel="noopener noreferrer">{html.escape(title)}</a></li>')
            parts.append('</ul>')
        parts.append('</details>')
    if item.review_notes:
        notes_file = Path(item.filename).with_suffix(".json").name
        parts.append(f'<p class="review-note-source">Saved with content revision {html.escape(item.notes_ref)} · '
                     f'<a href="../notes/{html.escape(notes_file)}" download>Download original review records</a></p>')
    parts.append('</section>')
    return "\n".join(parts)


@dataclass(frozen=True)
class DiffPlanItem:
    rank: int
    path: str
    changed_characters: int
    chunk: int


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


def changed_character_count(old_text: str, current_text: str) -> int:
    """Count inserted and removed characters after delimiter normalization."""

    old_text = canonicalize_delimiters(old_text)
    current_text = canonicalize_delimiters(current_text)
    return sum(
        (old_end - old_start) + (current_end - current_start)
        for operation, old_start, old_end, current_start, current_end
        in difflib.SequenceMatcher(None, old_text, current_text).get_opcodes()
        if operation != "equal"
    )


def build_diff_plan(
    comparisons: list[tuple[str, str, str]],
    chunk_count: int,
) -> list[DiffPlanItem]:
    """Rank comparisons by size and greedily balance them across chunks."""

    if chunk_count < 1:
        raise ValueError("chunk_count must be at least 1")
    ranked = sorted(
        (
            (changed_character_count(old_text, current_text), path)
            for path, old_text, current_text in comparisons
        ),
        key=lambda entry: (-entry[0], entry[1]),
    )
    chunk_loads = [0] * min(chunk_count, max(1, len(ranked)))
    plan = []
    for rank, (changed_characters, path) in enumerate(ranked, start=1):
        chunk_index = min(
            range(len(chunk_loads)),
            key=lambda index: (chunk_loads[index], index),
        )
        plan.append(
            DiffPlanItem(
                rank=rank,
                path=path,
                changed_characters=changed_characters,
                chunk=chunk_index + 1,
            )
        )
        chunk_loads[chunk_index] += changed_characters
    return plan


def write_diff_plan(
    plan: list[DiffPlanItem],
    destination: Path | None,
    baseline: str = "HEAD",
    proposed: str = "WORKTREE",
) -> None:
    records = [
        {
            **item.__dict__,
            "baseline": baseline,
            "proposed": proposed,
            "review_direction": "baseline_to_proposed",
        }
        for item in plan
    ]
    lines = [json.dumps(record, sort_keys=True) for record in records]
    output = "\n".join(lines) + ("\n" if lines else "")
    if destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)


def write_patch_chunks(
    content_repo: Path,
    plan: list[DiffPlanItem],
    destination: Path,
    baseline: str | None,
    proposed: str | None,
) -> list[Path]:
    """Write each balanced chunk as a standard unified Git patch."""

    destination.mkdir(parents=True, exist_ok=True)
    chunk_numbers = sorted({item.chunk for item in plan})
    width = max(2, len(str(max(chunk_numbers, default=1))))
    written = []
    for chunk in chunk_numbers:
        patch_parts = []
        for item in plan:
            if item.chunk != chunk:
                continue
            diff_args = [
                "diff",
                "--no-ext-diff",
                "--no-renames",
                "--unified=3",
                baseline or "HEAD",
            ]
            if proposed:
                diff_args.append(proposed)
            diff_args.extend(["--", item.path])
            patch_parts.append(git(*diff_args, cwd=content_repo).stdout)
        patch_path = destination / f"chunk-{chunk:0{width}d}.patch"
        patch_path.write_bytes(b"".join(patch_parts))
        written.append(patch_path)
    return written


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
    moved = ""
    seen: set[str] = set()
    while knowl.redirect_to and knowl.redirect_to in registry and knowl.id not in seen:
        seen.add(knowl.id)
        knowl = registry[knowl.redirect_to]
    if seen:
        moved = (f'<p class="review-consolidation">Consolidated into '
                 f'<a href="{compiler.escape_attr(compiler.target_href(knowl.id))}">'
                 f'{html.escape(knowl.title)}</a>. Canonical content follows.</p>')
    parts = [
        moved,
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
    .comparison-added { display: block; background: var(--surface); }
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
    .review-reasons { padding: 1.25rem clamp(1rem, 3vw, 3rem); background: var(--surface); border-bottom: 1px solid var(--line); }
    .review-reasons h2 { margin: 0 0 .5rem; font-size: 1.2rem; }
    .review-reasons p { max-width: 85ch; margin: .6rem 0; }
    .review-note-context, .review-note-source { color: var(--muted); font-size: .85rem; overflow-wrap: anywhere; }
    .review-note-status, .review-note-label { font-weight: 700; font-size: .9rem; }
    .review-note { padding: .35rem 0 .35rem 1rem; margin: .9rem 0; border-left: 3px solid var(--accent); }
    .review-reason-text { white-space: pre-line; overflow-wrap: anywhere; }
    .review-note-history, .review-prerequisite-changes { margin: 1rem 0; }
    .review-reasons summary { cursor: pointer; font-weight: 600; }
    .review-reasons li { overflow-wrap: anywhere; }
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
    .review-sort-row {
      display: flex; align-items: center; gap: .55rem; margin: 0 1rem .65rem;
      color: var(--muted); font-size: .85rem;
    }
    .review-sort-row select {
      min-width: 0; flex: 1; padding: .35rem .45rem;
      border: 1px solid var(--line-strong); border-radius: .35rem;
      background: var(--surface); color: var(--ink);
    }
    .review-toggle-row {
      display: flex; align-items: center; gap: .55rem; margin: 0 1rem .65rem;
      color: var(--muted); font-size: .85rem;
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
    .review-diff-size { display: block; margin-top: .2rem; color: var(--muted); font-size: .75rem; }
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
    display_knowl = item.current_knowl or item.old_knowl
    assert display_knowl is not None
    title = display_knowl.title
    knowl_href = "/" + display_knowl.id.strip("/") + "/"
    diff_open = " open" if item.change_kind == "modified" else ""
    if item.change_kind == "added":
        rendered = f"""<main class="comparison comparison-added">
    <section class="version version-current" aria-label="New knowl">
      <h2 class="version-label">{html.escape(right_label)} · new knowl</h2>
      {render_complete_knowl(item.current_knowl, registry)}
    </section>
  </main>"""
    elif item.change_kind == "deleted":
        assert item.old_knowl is not None
        rendered = f"""<main class="comparison comparison-added">
    <section class="version version-head" aria-label="Removed knowl">
      <h2 class="version-label">{html.escape(left_label)} · removed knowl</h2>
      {render_complete_knowl(item.old_knowl, registry)}
    </section>
  </main>"""
    else:
        assert item.current_knowl is not None
        assert item.old_knowl is not None
        rendered = f"""<main class="comparison">
    <section class="version version-head" aria-label="Baseline version">
      <h2 class="version-label">{html.escape(left_label)}</h2>
      {render_complete_knowl(item.old_knowl, registry)}
    </section>
    <section class="version version-current" aria-label="Proposed version">
      <h2 class="version-label">{html.escape(right_label)}</h2>
      {render_complete_knowl(item.current_knowl, registry)}
    </section>
  </main>"""
    current_link = (
        f'<a href="{html.escape(knowl_href)}" target="_top">Open current knowl ↗</a>'
        if item.current_knowl is not None
        else '<span>Removed from proposed content</span>'
    )
    return (
        common_head(f"{title} — content review")
        + item_styles()
        + f"""<body>
  <header class="review-toolbar">
    <p class="review-path"><strong>{item.index + 1} of {total}</strong> · {html.escape(item.path)}</p>
    {current_link}
  </header>
  {render_review_notes(item, registry)}
  <details class="source-diff"{diff_open}>
    <summary>Delimiter-normalized source diff</summary>
    <div class="diff-wrap">{source_diff(item.old_text, item.current_text, left_label, right_label)}</div>
  </details>
  {rendered}
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
    ranked_items = [
        (changed_character_count(item.old_text, item.current_text), original_index, item)
        for original_index, item in enumerate(items)
    ]
    ranked_items.sort(key=lambda entry: (-entry[0], entry[1]))
    for diff_length, original_index, item in ranked_items:
        display_knowl = item.current_knowl or item.old_knowl
        assert display_knowl is not None
        size_label = (
            f"new knowl · {len(item.current_text):,} source characters"
            if item.change_kind == "added"
            else (
                f"removed knowl · {len(item.old_text):,} source characters"
                if item.change_kind == "deleted"
                else f"{diff_length:,} changed characters"
            )
        )
        entries.append(
            f"""<li data-original-index="{original_index}" data-diff-length="{diff_length}"
    data-change-kind="{html.escape(item.change_kind)}">
  <a class="review-link" href="items/{html.escape(item.filename)}"
     data-target="items/{html.escape(item.filename)}"
     data-search="{html.escape((display_knowl.title + ' ' + item.path).lower())}">
    <span class="review-title">{html.escape(display_knowl.title)}</span>
    <span class="review-file">{html.escape(item.path.removeprefix('content/'))}</span>
    <span class="review-diff-size">{size_label}</span>
  </a>
</li>"""
        )
    default_items = [entry for entry in ranked_items if entry[2].change_kind != "added"]
    if not default_items:
        default_items = ranked_items
    first = f"items/{default_items[0][2].filename}" if default_items else ""
    added_count = sum(item.change_kind == "added" for item in items)
    added_checked = " checked" if items and added_count == len(items) else ""
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
      <label class="review-sort-row" for="review-sort">
        <span>Sort</span>
        <select id="review-sort">
          <option value="original">Original order</option>
          <option value="largest" selected>Largest diff first</option>
          <option value="smallest">Smallest diff first</option>
        </select>
      </label>
      <label class="review-toggle-row" for="review-include-added">
        <input id="review-include-added" type="checkbox"{added_checked}>
        <span>Include newly created knowls ({added_count})</span>
      </label>
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
    const sort = document.getElementById("review-sort");
    const count = document.getElementById("review-count");
    const includeAdded = document.getElementById("review-include-added");
    const list = document.getElementById("review-list");
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
    function updateVisibility() {{
      const query = search.value.trim().toLowerCase();
      let visible = 0;
      links.forEach(link => {{
        const entry = link.closest("li");
        const kindAllowed = includeAdded.checked || entry.dataset.changeKind !== "added";
        const show = kindAllowed && (!query || link.dataset.search.includes(query));
        entry.hidden = !show;
        if (show) visible += 1;
      }});
      count.textContent = visible + " visible";
      const active = links.find(link => link.classList.contains("active"));
      if (active && active.closest("li").hidden) {{
        const replacement = links.find(link => !link.closest("li").hidden);
        if (replacement) select(replacement);
      }}
    }}
    search.addEventListener("input", updateVisibility);
    includeAdded.addEventListener("change", updateVisibility);
    sort.addEventListener("change", () => {{
      const direction = sort.value === "largest" ? -1 : 1;
      const entries = links.map(link => link.closest("li"));
      entries.sort((left, right) => {{
        if (sort.value === "original") {{
          return Number(left.dataset.originalIndex) - Number(right.dataset.originalIndex);
        }}
        const difference = Number(left.dataset.diffLength) - Number(right.dataset.diffLength);
        return difference * direction
          || Number(left.dataset.originalIndex) - Number(right.dataset.originalIndex);
      }});
      entries.forEach(entry => list.appendChild(entry));
    }});
    const requested = decodeURIComponent(location.hash.slice(1));
    const initial = links.find(link => link.dataset.target === requested) || links[0];
    if (initial) select(initial, false);
    updateVisibility();
  </script>
</body>
</html>
"""
    )


def build(content_repo: Path, output: Path) -> int:
    substantive = [
        (path, old, current)
        for path, old, current in comparison_sources(content_repo, None, None, None)
        if normalize_delimiters(old) != normalize_delimiters(current)
    ]

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

    attach_review_notes(items, content_repo, "Working tree")
    write_review_notes(items, output)
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
    paths = ["content"]
    if path_exists_at_ref(content_repo, ref, "reviews/dependency-structure"):
        paths.append("reviews/dependency-structure")
    archive = git("archive", ref, *paths, cwd=content_repo).stdout
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


def added_knowl_paths(content_repo: Path, left_ref: str, right_ref: str) -> list[str]:
    """Return knowl paths added between two refs."""

    changed = git(
        "diff",
        "--diff-filter=A",
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


def deleted_knowl_paths(content_repo: Path, left_ref: str, right_ref: str) -> list[str]:
    """Return knowl paths deleted between two refs."""

    changed = git(
        "diff",
        "--diff-filter=D",
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


def comparison_sources(
    content_repo: Path,
    left_ref: str | None,
    right_ref: str | None,
    paths_file: Path | None,
) -> list[tuple[str, str, str]]:
    if left_ref and right_ref:
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
        return [
            (
                path,
                git("show", f"{left_ref}:{path}", cwd=content_repo).stdout.decode(),
                git("show", f"{right_ref}:{path}", cwd=content_repo).stdout.decode(),
            )
            for path in paths
        ]

    changed = git("diff", "--name-only", "-z", "--", "content", cwd=content_repo).stdout
    paths = [path for path in changed.decode().split("\0") if path.endswith(".knowl.md")]
    return [
        (
            path,
            git("show", f"HEAD:{path}", cwd=content_repo).stdout.decode(),
            (content_repo / path).read_text(encoding="utf-8"),
        )
        for path in paths
    ]


def build_ref_comparison(
    content_repo: Path,
    output: Path,
    left_ref: str,
    right_ref: str,
    paths_file: Path | None,
    left_label: str,
    right_label: str,
    heading: str,
    include_added: bool = False,
    include_deleted: bool = False,
) -> int:
    comparisons = comparison_sources(
        content_repo,
        left_ref,
        right_ref,
        paths_file,
    )
    added_paths: set[str] = set()
    deleted_paths: set[str] = set()
    if include_added:
        added_paths = set(added_knowl_paths(content_repo, left_ref, right_ref))
        comparisons.extend(
            (
                path,
                "",
                git("show", f"{right_ref}:{path}", cwd=content_repo).stdout.decode(),
            )
            for path in sorted(added_paths)
        )
    if include_deleted:
        deleted_paths = set(deleted_knowl_paths(content_repo, left_ref, right_ref))
        comparisons.extend(
            (
                path,
                git("show", f"{left_ref}:{path}", cwd=content_repo).stdout.decode(),
                "",
            )
            for path in sorted(deleted_paths)
        )
    with tempfile.TemporaryDirectory(prefix="knowl-review-ref-") as temp:
        right_tree = Path(temp)
        extract_ref(content_repo, right_ref, right_tree)
        right_knowls = compiler.discover_knowls(right_tree / "content")
        registry = {knowl.id: knowl for knowl in right_knowls}

        items: list[ReviewItem] = []
        for index, (path, left, right) in enumerate(comparisons):
            left_knowl = None if path in added_paths else parse_text(left, f"{left_ref}:{path}")
            right_knowl = None if path in deleted_paths else parse_text(right, f"{right_ref}:{path}")
            display_knowl = right_knowl or left_knowl
            assert display_knowl is not None
            safe_id = re.sub(r"[^a-z0-9-]+", "-", display_knowl.id.lower()).strip("-")
            items.append(
                ReviewItem(
                    index=index,
                    path=path,
                    old_text=left,
                    current_text=right,
                    old_knowl=left_knowl,
                    current_knowl=right_knowl,
                    filename=f"{index + 1:04d}-{safe_id}.html",
                    change_kind=(
                        "added" if path in added_paths
                        else "deleted" if path in deleted_paths
                        else "modified"
                    ),
                )
            )

        resolved_ref = git("rev-parse", right_ref, cwd=content_repo).stdout.decode().strip()
        attach_review_notes(items, right_tree, resolved_ref)

    write_review_notes(items, output)
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
    parser.add_argument(
        "--include-added",
        action="store_true",
        help="Include added knowls behind a toggle; their source diffs start collapsed",
    )
    parser.add_argument(
        "--include-deleted",
        action="store_true",
        help="Include removed knowls behind a toggle; their source diffs start collapsed",
    )
    parser.add_argument(
        "--diff-plan",
        nargs="?",
        type=Path,
        const="-",
        help="Write a largest-first JSONL diff plan to PATH, or stdout when PATH is omitted",
    )
    parser.add_argument(
        "--chunks",
        type=int,
        default=1,
        help="Greedily balance a --diff-plan across this many chunks (default: 1)",
    )
    parser.add_argument(
        "--patch-dir",
        type=Path,
        help="With --diff-plan, also write each balanced chunk as a standard Git patch",
    )
    args = parser.parse_args()
    if bool(args.left_ref) != bool(args.right_ref):
        parser.error("--left-ref and --right-ref must be used together")
    if args.paths_from and not args.left_ref:
        parser.error("--paths-from requires --left-ref and --right-ref")
    if args.chunks < 1:
        parser.error("--chunks must be at least 1")
    if args.chunks != 1 and args.diff_plan is None:
        parser.error("--chunks requires --diff-plan")
    if args.patch_dir and args.diff_plan is None:
        parser.error("--patch-dir requires --diff-plan")
    if args.diff_plan is not None:
        content_repo = args.content_repo.resolve()
        comparisons = comparison_sources(
            content_repo,
            args.left_ref,
            args.right_ref,
            args.paths_from.resolve() if args.paths_from else None,
        )
        plan = build_diff_plan(comparisons, args.chunks)
        destination = None if str(args.diff_plan) == "-" else args.diff_plan.resolve()
        write_diff_plan(
            plan,
            destination,
            baseline=args.left_ref or "HEAD",
            proposed=args.right_ref or "WORKTREE",
        )
        patch_paths = []
        if args.patch_dir:
            patch_paths = write_patch_chunks(
                content_repo,
                plan,
                args.patch_dir.resolve(),
                args.left_ref,
                args.right_ref,
            )
        if destination:
            chunk_totals: dict[int, int] = {}
            for item in plan:
                chunk_totals[item.chunk] = chunk_totals.get(item.chunk, 0) + item.changed_characters
            totals = ", ".join(
                f"chunk {chunk}: {total:,} chars"
                for chunk, total in sorted(chunk_totals.items())
            )
            print(f"Wrote {len(plan)} diffs to {destination} ({totals})")
            if patch_paths:
                print(
                    f"Wrote {len(patch_paths)} standard Git patches to "
                    f"{args.patch_dir.resolve()}"
                )
        return 0 if plan else 1
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
            args.include_added,
            args.include_deleted,
        )
    else:
        count = build(args.content_repo.resolve(), args.output.resolve())
    if not count:
        print("No substantive knowl edits found.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
