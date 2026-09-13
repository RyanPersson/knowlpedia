"""Development-only Markdown documents with MathJax and inline notation notes."""
from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
import hashlib
import html
import json
from pathlib import Path
import re
import shutil

from private_facsimile import check_svg, inside_file, LINK_RE, SLUG_RE

ACTIVE = ContextVar('private_markdown_document', default=None)
ANCHOR_RE = re.compile(r'^<!-- anchor: ([a-zA-Z0-9_.-]+) -->$', re.M)
FIGURE_RE = re.compile(r'^!\[([^\]\n]*)\]\((figures/[a-z0-9-]+\.(?:svg|png|webp|jpg))\)$')


@contextmanager
def rendering(knowl):
    token = ACTIVE.set(knowl)
    try:
        yield
    finally:
        ACTIVE.reset(token)


def load_manifest(package: Path, relative: str, markdown: str) -> dict:
    path = inside_file(package, relative)
    data = json.loads(path.read_text())
    if data.get('version') != 1 or type(data.get('pages')) is not int or data['pages'] < 1:
        raise ValueError('Invalid private Markdown manifest')
    source = data.get('source_url', '')
    if source and not source.startswith('https://'):
        raise ValueError('Private Markdown source URL must use HTTPS')
    anchors = ANCHOR_RE.findall(markdown)
    if len(anchors) != len(set(anchors)):
        raise ValueError('Duplicate private Markdown anchor')
    data['anchors'] = anchors
    if data.get('markdown_body_sha256'):
        plain=LINK_RE.sub(lambda m:m[2],markdown).strip()
        if hashlib.sha256(plain.encode()).hexdigest()!=data['markdown_body_sha256']:
            raise ValueError('Private Markdown source fidelity check failed')
    for key, note in data.get('notes', {}).items():
        if not SLUG_RE.fullmatch(key) or not all(isinstance(note.get(k), str) for k in ('title', 'body')):
            raise ValueError('Invalid private Markdown notation note')
        if type(note.get('page')) is not int or not 1 <= note['page'] <= data['pages']:
            raise ValueError('Invalid private Markdown note page')
    if data.get('guide_note') and data['guide_note'] not in data.get('notes',{}):
        raise ValueError('Private Markdown guide note is missing')
    for name, figure in data.get('figures', {}).items():
        if not FIGURE_RE.fullmatch(f'![]({name})'):
            raise ValueError('Invalid private figure name')
        source = inside_file(package, figure.get('path'))
        if source.suffix.lower() != Path(name).suffix:
            raise ValueError('Private figure extension mismatch')
        if hashlib.sha256(source.read_bytes()).hexdigest() != figure.get('sha256'):
            raise ValueError('Private figure hash mismatch')
        if source.suffix.lower() == '.svg':
            check_svg(source)
        figure['source_path'] = source
    for _, name in re.findall(r'^!\[([^\]\n]*)\]\(([^)]+)\)$', markdown, re.M):
        if name not in data.get('figures', {}):
            raise ValueError('Private Markdown image is absent from its manifest')
    data['manifest_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    return data


def targets(data: dict) -> list[str]:
    return list(dict.fromkeys(m[1] for note in data.get('notes', {}).values() for m in LINK_RE.finditer(note['body'])))


def render_math(tex: str, display: bool) -> str:
    tag = 'div' if display else 'span'
    kind = 'display' if display else 'inline'
    left, right = (r'\[', r'\]') if display else (r'\(', r'\)')
    return f'<{tag} class="math-{kind} math-mathjax" data-document-math="true">{html.escape(left + tex + right)}</{tag}>'


def render_marker(line: str) -> str | None:
    knowl = ACTIVE.get()
    if knowl is None:
        return None
    anchor = ANCHOR_RE.fullmatch(line)
    if anchor:
        return f'<span class="document-anchor" id="{anchor[1]}"></span>'
    figure = FIGURE_RE.fullmatch(line)
    if figure:
        if figure[2] not in knowl.reading['figures']:
            raise ValueError('Unregistered private figure')
        return (f'<figure class="document-figure"><img src="/{knowl.id}/{figure[2]}" '
                f'alt="{html.escape(figure[1], quote=True)}" loading="lazy" decoding="async"></figure>')
    return None


def note_fragment_url(knowl, anchor: str | None) -> str | None:
    if knowl.reading and anchor and anchor.startswith('note-') and anchor[5:] in knowl.reading.get('notes', {}):
        return f'/{knowl.id}/notes/{anchor[5:]}.html'
    return None


def reader_body(knowl, registry, render_markdown) -> str:
    with rendering(knowl):
        content = render_markdown(knowl.core_markdown, registry)
        guide=knowl.reading.get('guide_note')
        guide_link=render_markdown(f'[[{knowl.id}#note-{guide}|{knowl.reading["notes"][guide]["title"]}]]',registry) if guide else ''
    source = knowl.reading.get('source_url')
    source_link = f'<a href="{html.escape(source, quote=True)}">Original PDF</a>' if source else ''
    return (
        '<main class="page-shell document-markdown-shell" id="main-content">'
        '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/library/">Library</a><span aria-hidden="true">/</span><span>Reading copy</span></nav>'
        f'<article class="knowl-page document-markdown" data-knowl-id="{knowl.id}" data-knowl-visibility="private" data-reading-manifest-sha256="{knowl.reading["manifest_sha256"]}">'
        f'<header class="page-header"><p class="kind">Private reading copy</p><h1>{html.escape(knowl.title)}</h1>'
        f'<p class="page-summary">{html.escape(knowl.summary)}</p>{source_link}{guide_link}</header>'
        '<section class="core-section" id="section.core">' + content + '</section></article></main>'
    )


def write_assets(knowl, out, registry, render_markdown, html_document, profile):
    if not profile.include_development_content or knowl.visibility != 'private':
        raise ValueError('Private Markdown assets require a private development document')
    destination = out / knowl.id
    for name, figure in knowl.reading.get('figures', {}).items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(figure['source_path'], target)
    for key, note in knowl.reading.get('notes', {}).items():
        target = destination / f'notes/{key}.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        # Public definitions and short private notes use pre-rendered math;
        # the full flowing document is typeset by its local MathJax runtime.
        target.write_text(
            f'<div class="knowl-content" data-knowl-id="{knowl.id}#note-{key}" data-knowl-title="{html.escape(note["title"], quote=True)}" data-knowl-kind="Paper notation" data-knowl-visibility="private">'
            '<div class="knowl-body">' + render_markdown(note['body'], registry) + '</div>'
            '<div class="knowl-controls">'
            f'<a class="knowl-page-link" href="/{knowl.id}/#page-{note["page"]}">Read the source definition · p. {note["page"]}</a>'
            '<button type="button" class="knowl-close" aria-label="Collapse paper notation">×</button></div></div>'
        )
    # Keep previously shared page URLs usable after conversion to a flowing
    # document. They jump to the corresponding source anchor in the text.
    for number in range(1, knowl.reading['pages'] + 1):
        path = destination / f'pages/{number:03}/index.html'
        path.parent.mkdir(parents=True, exist_ok=True)
        url = f'/{knowl.id}/#page-{number}'
        path.write_text(html_document(knowl.title, f'<main class="page-shell"><p><a href="{url}">Continue reading</a></p></main>', profile=profile, redirect_url=url))
