"""Faithful page images with semantic links for development-only documents.

The source PDF is never copied. Only individually named, hash-checked page
images from a private manifest become document assets. The linked transcript
remains the document body; its original extraction is checked page by page.
"""
from __future__ import annotations

import hashlib
import html
import json
import math
from pathlib import Path
import re
import shutil
import xml.etree.ElementTree as ET


LINK_RE = re.compile(r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*(?:#[^\]|]+)?)\|((?:[^\]]|\](?!\]))*?)\]\]")
SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def inside_file(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError("Facsimile paths must be relative to the private package")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError("Facsimile file is missing or escapes the private package")
    return path


def check_svg(path: Path) -> None:
    root = ET.fromstring(path.read_bytes())
    if root.tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError("Facsimile SVG must have an SVG root")
    for node in root.iter():
        tag = node.tag.rsplit("}", 1)[-1].lower()
        if tag in {"script", "style", "foreignobject", "iframe", "object", "embed"}:
            raise ValueError("Facsimile SVG contains active content")
        for key, value in node.attrib.items():
            key = key.rsplit("}", 1)[-1].lower()
            if key.startswith("on"):
                raise ValueError("Facsimile SVG contains an event handler")
            if key == "href" and not value.startswith(("#", "data:image/png;base64,", "data:image/jpeg;base64,")):
                raise ValueError("Facsimile SVG contains an external reference")
            for reference in re.findall(r"url\(([^)]*)\)", value, flags=re.I):
                if not reference.strip().strip("\"'").startswith("#"):
                    raise ValueError("Facsimile SVG contains an external CSS reference")


def load_manifest(package: Path, relative: str, transcript: str) -> dict:
    path = inside_file(package, relative)
    data = json.loads(path.read_text())
    if data.get("version") != 1 or not isinstance(data.get("pages"), list) or not data["pages"]:
        raise ValueError("Invalid facsimile manifest")
    parts = transcript.split("\f")
    if len(parts) != len(data["pages"]):
        raise ValueError("Facsimile page count does not match transcript")
    for number, (page, text) in enumerate(zip(data["pages"], parts), 1):
        if page.get("page") != number:
            raise ValueError("Facsimile pages must be consecutively numbered from one")
        width, height = page.get("width"), page.get("height")
        if any(not isinstance(x, (int, float)) or not math.isfinite(x) or x <= 0 for x in (width, height)):
            raise ValueError("Invalid facsimile page dimensions")
        plain = LINK_RE.sub(lambda m: m[2], text).strip()
        if hashlib.sha256(plain.encode()).hexdigest() != page.get("text_sha256"):
            raise ValueError(f"Facsimile transcript fidelity failed on page {number}")
        image = inside_file(package, page.get("image"))
        if image.suffix.lower() not in {".svg", ".png", ".webp", ".jpg", ".jpeg"}:
            raise ValueError("Facsimiles may copy page images only")
        if hashlib.sha256(image.read_bytes()).hexdigest() != page.get("image_sha256"):
            raise ValueError(f"Facsimile image hash failed on page {number}")
        if image.suffix.lower() == ".svg":
            check_svg(image)
        page["image_path"] = image
        page["transcript"] = text
        for link in page.get("links", []):
            if not isinstance(link.get("target"), str) or not isinstance(link.get("label"), str):
                raise ValueError("Invalid facsimile link")
            if not link.get("rects"):
                raise ValueError("A facsimile overlay needs at least one rectangle")
            for rect in link["rects"]:
                if len(rect) != 4 or any(not isinstance(x, (int, float)) or not math.isfinite(x) for x in rect):
                    raise ValueError("Invalid facsimile link rectangle")
                x0, y0, x1, y1 = rect
                if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
                    raise ValueError("Facsimile link rectangle lies outside its page")
        for concept in page.get("concepts", []):
            if not all(isinstance(concept.get(key), str) for key in ("target", "label")):
                raise ValueError("Invalid facsimile page concept")
        for reference in page.get("references", []):
            if not isinstance(reference.get("label"), str):
                raise ValueError("Invalid facsimile reference label")
            if "page" in reference:
                if type(reference["page"]) is not int or not 1 <= reference["page"] <= len(parts):
                    raise ValueError("Invalid facsimile reference destination")
                y = reference.get("y", 0)
                if not isinstance(y, (int, float)) or not math.isfinite(y) or not 0 <= y <= data["pages"][reference["page"]-1]["height"]:
                    raise ValueError("Invalid facsimile reference position")
            elif not isinstance(reference.get("url"), str) or not reference["url"].startswith("https://"):
                raise ValueError("Facsimile references require a page or HTTPS URL")
            rect = reference.get("rect", [])
            if len(rect) != 4 or any(not isinstance(x, (int, float)) or not math.isfinite(x) for x in rect):
                raise ValueError("Invalid facsimile reference rectangle")
            x0, y0, x1, y1 = rect
            if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height):
                raise ValueError("Facsimile reference lies outside its page")
    count = len(parts)
    for bookmark in data.get("bookmarks", []):
        if not isinstance(bookmark.get("label"), str) or type(bookmark.get("page")) is not int or not 1 <= bookmark["page"] <= count:
            raise ValueError("Invalid facsimile bookmark")
    for key, note in data.get("notes", {}).items():
        if not SLUG_RE.fullmatch(key) or not all(isinstance(note.get(field), str) for field in ("title", "body")):
            raise ValueError("Invalid facsimile note")
        if type(note.get("page")) is not int or not 1 <= note["page"] <= count:
            raise ValueError("Invalid facsimile note page")
    source_url = data.get("source_url", "")
    if source_url and not source_url.startswith("https://"):
        raise ValueError("Facsimile source links must use HTTPS")
    data["manifest_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return data


def targets(data: dict) -> list[str]:
    result = []
    for page in data["pages"]:
        result.extend(item["target"] for key in ("links", "concepts") for item in page.get(key, []))
    for note in data.get("notes", {}).values():
        result.extend(match[1] for match in LINK_RE.finditer(note["body"]))
    return list(dict.fromkeys(result))


def base_url(knowl) -> str:
    return "/" + knowl.id.lower() + "/"


def page_url(knowl, number: int) -> str:
    return base_url(knowl) + f"pages/{number:03d}/"


def anchor(knowl, target: str, label: str, render_ref, registry, *, css="document-term", extra="") -> str:
    note_prefix = knowl.id + "#note-"
    if target.startswith(note_prefix):
        key = target[len(note_prefix):]
        note = knowl.facsimile["notes"].get(key)
        if note is None:
            return render_ref(target, registry, label)
        href = page_url(knowl, note["page"])
        fragment = base_url(knowl) + f"notes/{key}.html"
        return (f'<a class="knowl {css}" href="{html.escape(href, quote=True)}" '
                f'data-knowl="{html.escape(fragment, quote=True)}" aria-expanded="false"{extra}>{html.escape(label)}</a>')
    rendered = render_ref(target, registry, label)
    return rendered.replace('class="knowl"', f'class="knowl {css}"', 1).replace(" aria-expanded=", extra + " aria-expanded=", 1)


def transcript_html(knowl, text, render_ref, registry) -> str:
    result, start = [], 0
    for match in LINK_RE.finditer(text):
        result.append(html.escape(text[start:match.start()]))
        result.append(anchor(knowl, match[1], match[2], render_ref, registry))
        start = match.end()
    result.append(html.escape(text[start:]))
    return "".join(result)


def render_page_body(knowl, page: dict, render_ref, registry) -> str:
    number, width, height = page["page"], page["width"], page["height"]
    image_url = base_url(knowl) + f'assets/page-{number:03d}{page["image_path"].suffix.lower()}'
    overlays = []
    for occurrence, link in enumerate(page.get("links", [])):
        for segment, (x0, y0, x1, y1) in enumerate(link["rects"]):
            style = (f"left:{100*x0/width:.6f}%;top:{100*y0/height:.6f}%;"
                     f"width:{100*(x1-x0)/width:.6f}%;height:{100*(y1-y0)/height:.6f}%;")
            extra = (f' style="{style}" title="{html.escape(link["label"], quote=True)}" '
                     f'data-occurrence="{occurrence}"')
            if segment:
                extra += ' tabindex="-1" aria-hidden="true"'
            overlays.append(anchor(knowl, link["target"], link["label"], render_ref, registry,
                                   css="document-term document-term-overlay", extra=extra))
    reference_links = []
    for reference in page.get("references", []):
        label = reference["label"]
        if "page" in reference:
            target_page = reference["page"]
            y = reference.get("y", 0)
            href = page_url(knowl, target_page) + f"#at-{y:g}"
            attrs = f' data-document-page="{target_page}" data-document-y="{y:g}"'
            title = f"{label} · page {target_page}"
        else:
            href, attrs, title = reference["url"], "", label
        safe_href = html.escape(href, quote=True)
        x0, y0, x1, y1 = reference["rect"]
        style = (f"left:{100*x0/width:.6f}%;top:{100*y0/height:.6f}%;"
                 f"width:{100*(x1-x0)/width:.6f}%;height:{100*(y1-y0)/height:.6f}%;")
        overlays.append(f'<a class="document-reference document-term-overlay" href="{safe_href}"{attrs} '
                        f'style="{style}" title="{html.escape(title, quote=True)}">{html.escape(label)}</a>')
        reference_links.append(f'<li><a href="{safe_href}"{attrs}>{html.escape(title)}</a></li>')
    concepts = list(page.get("concepts", []))
    concepts.extend({"target": link["target"], "label": link.get("concept_label", link["label"])} for link in page.get("links", []))
    seen, concept_links = set(), []
    for item in concepts:
        key = item["target"]
        if key in seen:
            continue
        seen.add(key)
        concept_links.append("<li>" + anchor(knowl, key, item["label"], render_ref, registry) + "</li>")
    return (
        f'<section class="document-page-content" data-page-number="{number}" aria-label="Page {number}">'
        '<div class="document-image-view"><div class="document-viewport" tabindex="0" aria-label="Page image; zoom and scroll to read">'
        f'<div class="document-sheet" style="aspect-ratio:{width}/{height}">'
        f'<img src="{image_url}" width="{width:g}" height="{height:g}" alt="Original page {number}. Use Text transcript for selectable text." decoding="async" draggable="false">'
        '<div class="document-page-overlay">' + "".join(overlays) + '</div></div></div></div>'
        '<div class="document-transcript-view" hidden><p class="document-transcript-note">'
        'The transcript preserves the PDF text extraction. Use Original page for equation and figure layout.</p>'
        '<pre class="document-transcript">' + transcript_html(knowl, page["transcript"], render_ref, registry) + '</pre></div>'
        f'<details class="document-concepts"><summary>Concepts on this page ({len(concept_links)})</summary>'
        '<ul>' + "".join(concept_links) + '</ul></details>'
        + ('<details class="document-references"><summary>Source references on this page</summary><ul>'
           + "".join(reference_links) + '</ul></details>' if reference_links else '') + '</section>'
    )


def reader_body(knowl, number: int, render_ref, registry) -> str:
    data = knowl.facsimile
    count = len(data["pages"])
    previous, following = max(1, number-1), min(count, number+1)
    bookmarks = ['<option value="">Contents…</option>']
    bookmarks.extend(f'<option value="{item["page"]}">{html.escape(item["label"])}</option>' for item in data.get("bookmarks", []))
    source = data.get("source_url")
    source_link = f'<a class="page-link" href="{html.escape(source, quote=True)}">Original PDF</a>' if source else ""
    if 'notation-guide' in data.get('notes', {}):
        source_link += ' · ' + anchor(knowl, knowl.id + '#note-notation-guide', 'Notation guide', render_ref, registry)
    return (
        '<main class="page-shell document-shell" id="main-content">'
        '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/library/">Library</a><span aria-hidden="true">/</span><span>Reading copy</span></nav>'
        f'<article class="knowl-page document-facsimile" data-knowl-id="{knowl.id}" data-knowl-visibility="private" '
        f'data-reader-base="{base_url(knowl)}" data-page-count="{count}" data-page-number="{number}">'
        f'<header class="page-header"><p class="kind">Private reading copy · {count} pages</p><h1>{html.escape(knowl.title)}</h1>'
        '<p class="page-summary">Expand highlighted mathematical terms without leaving the paper.</p>' + source_link + '</header>'
        '<nav class="document-toolbar" aria-label="Paper navigation">'
        f'<a class="document-page-link" data-document-page="{previous}" href="{page_url(knowl, previous)}" aria-label="Previous page">←</a>'
        f'<label class="document-page-label">Page <input class="document-page-number" type="number" min="1" max="{count}" value="{number}" inputmode="numeric"></label>'
        f'<span>of {count}</span>'
        f'<a class="document-page-link" data-document-page="{following}" href="{page_url(knowl, following)}" aria-label="Next page">→</a>'
        '<select class="document-bookmarks" aria-label="Paper contents">' + "".join(bookmarks) + '</select>'
        '<div class="document-view-controls"><button type="button" data-document-view="image" aria-pressed="true">Original page</button>'
        '<button type="button" data-document-view="text" aria-pressed="false">Text transcript</button></div>'
        '<div class="document-zoom-controls"><button type="button" data-document-zoom="-1" aria-label="Zoom out">−</button>'
        '<button type="button" data-document-zoom="reset" class="document-zoom-label">Fit width</button>'
        '<button type="button" data-document-zoom="1" aria-label="Zoom in">+</button></div></nav>'
        '<p class="document-load-status" role="status" aria-live="polite"></p>'
        '<div class="document-page-slot">' + render_page_body(knowl, data["pages"][number-1], render_ref, registry) + '</div>'
        '<aside class="document-concept-drawer" aria-label="Expanded mathematical concepts">'
        '<div class="document-drawer-header"><strong>Expanded concept</strong><button type="button" class="document-clear-concepts" aria-label="Close expanded concept">Close ×</button></div>'
        '<div class="document-knowl-slot" aria-live="polite"></div></aside>'
        '</article></main>'
    )


def write_assets_and_pages(knowl, out: Path, registry, render_ref, render_markdown, html_document, profile) -> None:
    if not profile.include_development_content or knowl.visibility != "private":
        raise ValueError("Facsimile output is restricted to private development documents")
    destination = out / knowl.id.lower()
    assets = destination / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for page in knowl.facsimile["pages"]:
        number = page["page"]
        source = page["image_path"]
        shutil.copyfile(source, assets / f"page-{number:03d}{source.suffix.lower()}")
        fragment = destination / f"pages/{number:03d}/body.html"
        fragment.parent.mkdir(parents=True, exist_ok=True)
        fragment.write_text(render_page_body(knowl, page, render_ref, registry))
        body = reader_body(knowl, number, render_ref, registry)
        (fragment.parent / "index.html").write_text(html_document(
            f"{knowl.title} · Page {number}", body, preload_mode="visible", profile=profile, page_script="facsimile.js",
        ))
    for key, note in knowl.facsimile.get("notes", {}).items():
        target = destination / f"notes/{key}.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            f'<div class="knowl-content" data-knowl-id="{knowl.id}#note-{key}" data-knowl-title="{html.escape(note["title"], quote=True)}" data-knowl-kind="Paper notation" data-knowl-visibility="private">'
            '<div class="knowl-body">' + render_markdown(note["body"], registry) + '</div>'
            '<div class="knowl-controls">'
            f'<a class="knowl-page-link" href="{page_url(knowl, note["page"])}">Read the source definition · p. {note["page"]}</a>'
            '<button type="button" class="knowl-close" aria-label="Collapse paper notation">×</button></div></div>'
        )
