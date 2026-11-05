"""Search-engine and AI-agent metadata for published Knowlpedia pages.

Everything here reads existing knowl data. It adds ``<head>`` metadata and
separate root or per-page files; it never changes rendered knowl content.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Callable, Iterable
from xml.sax.saxutils import escape as xml_escape

from knowl_patterns import FENCED_CODE_RE, INLINE_CODE_RE, MARKDOWN_LINK_RE, MATH_RE, WIKILINK_RE


SITE_URL = "https://knowlpedia.com"
SITE_NAME = "Knowlpedia"
DESCRIPTION_LIMIT = 155

ROBOTS_TXT = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

# Natural search qualifiers where the index label reads badly in parentheses.
# Every other subject uses its index label.
SUBJECT_QUALIFIERS = {
    "algebra-fields-galois": "Galois theory",
    "algebra-groups": "abstract algebra",
    "algebra-hyperstructures": "hyperstructures",
    "algebra-modules": "abstract algebra",
    "algebra-rings": "abstract algebra",
    "analysis": "analysis",
    "catalog": "catalogue of mathematical objects",
    "langlands": "Langlands program",
    "langlands-letter": "Langlands's letter",
    "lie-groups": "Lie groups",
    "nonassociative-algebra": "nonassociative algebra",
    "shale-paper": "Shale's paper",
    "shared-foundations": "mathematical foundations",
    "stat-mech-quantum": "quantum statistical mechanics",
}
# Long-form documents stand on their own; a subject would add nothing.
UNQUALIFIED_SUBJECTS = frozenset({"knowlification", "posts"})

# Kinds shown after the title. Structural kinds (index, page, ...) have no label.
LABELLED_KINDS = frozenset(
    {"calculation", "construction", "corollary", "definition", "example", "identity", "lemma", "notation", "proposition", "theorem"}
)
DEFINED_TERM_KINDS = frozenset({"definition", "notation"})
# The generic "knowl" kind holds definitions and statements alike, so a title
# that names a result or reads as a sentence must not be called a definition.
STATEMENT_TITLE_RE = re.compile(
    r"\b(theorem|lemma|proposition|corollary|conjecture|inequality|formula|law|principle|criterion|identity|"
    r"classification|convention|is|are|has|have|implies|exists?|admits?|uses|equals)\b|satz\b",
    re.IGNORECASE,
)
SLUG_ALIAS_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)+")

_GREEK = (
    "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi chi psi omega "
    "Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega"
).split()
_GREEK_LETTERS = "αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΥΦΨΩ"
TEX_SYMBOLS = {
    **{name: letter for name, letter in zip(_GREEK, _GREEK_LETTERS)},
    "varepsilon": "ε", "varphi": "φ", "vartheta": "θ",
    "times": "×", "otimes": "⊗", "oplus": "⊕", "cdot": "·", "circ": "∘", "pm": "±",
    "to": "→", "rightarrow": "→", "longrightarrow": "→", "leftarrow": "←", "mapsto": "↦",
    "hookrightarrow": "↪", "twoheadrightarrow": "↠", "Rightarrow": "⇒", "iff": "⇔",
    "in": "∈", "notin": "∉", "subset": "⊂", "subseteq": "⊆", "supset": "⊃", "supseteq": "⊇",
    "cup": "∪", "cap": "∩", "emptyset": "∅", "varnothing": "∅", "setminus": "∖",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠",
    "cong": "≅", "simeq": "≃", "sim": "∼", "approx": "≈", "equiv": "≡",
    "infty": "∞", "partial": "∂", "nabla": "∇", "forall": "∀", "exists": "∃", "neg": "¬",
    "sum": "∑", "prod": "∏", "int": "∫", "ell": "ℓ", "dots": "…", "ldots": "…", "cdots": "⋯",
}
BLACKBOARD = {"C": "ℂ", "F": "𝔽", "H": "ℍ", "N": "ℕ", "P": "ℙ", "Q": "ℚ", "R": "ℝ", "Z": "ℤ"}
SUPERSCRIPTS = str.maketrans("0123456789+-n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ")
SUBSCRIPTS = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")
_TEX_ARG = r"(?:\{([^{}]*)\}|\s*([A-Za-z0-9]))"


def absolute_url(path: str) -> str:
    return SITE_URL + path


def tex_to_text(tex: str) -> str:
    """Convert common LaTeX to readable Unicode; unknown commands lose their backslash."""

    def arg(match: re.Match[str], index: int = 1) -> str:
        return match.group(index) if match.group(index) is not None else match.group(index + 1)

    text = re.sub(r"\\mathbb" + _TEX_ARG, lambda m: BLACKBOARD.get(arg(m), arg(m)), tex)
    text = re.sub(r"\\(?:overline|bar)" + _TEX_ARG, lambda m: arg(m) + "\u0305", text)
    text = re.sub(r"\\(?:hat|widehat)" + _TEX_ARG, lambda m: arg(m) + "\u0302", text)
    text = re.sub(r"\\(?:tilde|widetilde)" + _TEX_ARG, lambda m: arg(m) + "\u0303", text)
    text = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", text)
    text = re.sub(r"\\(?:,|;|:|!| |quad|qquad)", " ", text).replace("~", " ")
    text = re.sub(r"\\(?:left|right|big|Big|bigg|Bigg)\b", "", text)
    text = re.sub(r"\\([A-Za-z]+)", lambda m: TEX_SYMBOLS.get(m.group(1), "\x01" + m.group(1)), text)
    # A remaining command is a wrapper such as \mathrm, whose argument survives
    # brace removal, or an unknown name; wrappers contribute no text of their own.
    text = re.sub(r"\x01(?:mathrm|mathfrak|mathcal|mathbf|mathsf|mathit|mathscr|operatorname|text|textbf|textit|rm|bf|it)\b", "", text)
    text = text.replace("\x01", "")

    def script(match: re.Match[str]) -> str:
        table = SUPERSCRIPTS if match.group(1) == "^" else SUBSCRIPTS
        value = match.group(2) if match.group(2) is not None else match.group(3)
        converted = value.translate(table)
        return converted if converted != value and all(c not in converted for c in value if c.isalnum()) else match.group(1) + value

    text = re.sub(r"([\^_])(?:\{([^{}]*)\}|([A-Za-z0-9+\-]))", script, text)
    text = text.replace("\\{", "\x02").replace("\\}", "\x03")
    text = re.sub(r"\\([%$&#_])", r"\1", text)
    text = text.replace("{", "").replace("}", "").replace("\x02", "{").replace("\x03", "}")
    return re.sub(r"\s+", " ", text).strip()


def plain_text(text: str) -> str:
    """Reduce source markup (wikilinks, Markdown, math) to one line of plain text."""
    math_tokens: list[str] = []

    def protect_math(match: re.Match[str]) -> str:
        tex = next(group for group in match.groups()[1:] if group is not None)
        math_tokens.append(tex_to_text(tex))
        return f"\x00{len(math_tokens) - 1}\x00"

    result = INLINE_CODE_RE.sub(lambda m: m.group(1), text)
    result = MATH_RE.sub(protect_math, result)
    result = MARKDOWN_LINK_RE.sub(lambda m: m.group(1), result)
    result = WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1).split("#", 1)[0].rsplit("/", 1)[-1].replace("-", " "), result)
    result = re.sub(r"\*\*([^*]+)\*\*", r"\1", result)
    result = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"\1", result)
    result = re.sub(r"\x00(\d+)\x00", lambda m: math_tokens[int(m.group(1))], result)
    return re.sub(r"\s+", " ", result).strip()


def truncate(text: str, limit: int = DESCRIPTION_LIMIT) -> str:
    if len(text) <= limit:
        return text
    head = text[: limit - 1]
    if " " in head:
        head = head.rsplit(" ", 1)[0]
    return head.rstrip(" ,;:") + "…"


def is_statement(knowl: Any) -> bool:
    return knowl.kind.lower() == "knowl" and bool(STATEMENT_TITLE_RE.search(plain_text(knowl.title)))


def kind_label(knowl: Any) -> str | None:
    """The kind to name in a page title, or None when it would add nothing."""
    kind = knowl.kind.lower()
    if knowl.learning_path:
        return "learning path"
    if kind == "knowl":
        return None if is_statement(knowl) else "definition"
    if kind not in LABELLED_KINDS or kind in plain_text(knowl.title).lower():
        return None
    return kind


def subject_qualifier(subject_id: str, subject_label: str) -> str | None:
    if subject_id in UNQUALIFIED_SUBJECTS:
        return None
    if subject_id in SUBJECT_QUALIFIERS:
        return SUBJECT_QUALIFIERS[subject_id]
    return subject_label[:1].lower() + subject_label[1:]


def short_title(knowl: Any, subject_id: str, subject_label: str) -> str:
    """The page title without the site suffix, used for Open Graph."""
    title = plain_text(knowl.title)
    qualifier = None if knowl.learning_path else subject_qualifier(subject_id, subject_label)
    label = kind_label(knowl)
    if qualifier and qualifier.casefold() == title.casefold():
        qualifier = None
    return title + (f" ({qualifier})" if qualifier else "") + (f": {label}" if label else "")


def full_title(short: str) -> str:
    return f"{short} | {SITE_NAME}"


def display_aliases(knowl: Any) -> list[str]:
    """Reader-facing alternate names, without URL slugs and title restatements."""

    def normalized(value: str) -> str:
        words = re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()
        return words[:-1] if words.endswith("s") else words

    seen = {normalized(plain_text(knowl.title))}
    result = []
    for alias in knowl.aliases:
        text = plain_text(alias)
        key = normalized(text)
        if not key or key in seen or "/" in text or "_" in text or SLUG_ALIAS_RE.fullmatch(text):
            continue
        seen.add(key)
        result.append(text)
    return result


def json_ld(data: dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'  <script type="application/ld+json">{payload}</script>\n'


def head_tags(path: str, og_title: str, description: str, schema: dict[str, Any], markdown: bool = False) -> str:
    url = html.escape(absolute_url(path), quote=True)
    title = html.escape(og_title, quote=True)
    summary = html.escape(description, quote=True)
    alternate = f'  <link rel="alternate" type="text/markdown" href="{url}index.md">\n' if markdown else ""
    return (
        f'  <meta name="description" content="{summary}">\n'
        f'  <link rel="canonical" href="{url}">\n'
        f"{alternate}"
        '  <meta property="og:type" content="article">\n'
        f'  <meta property="og:site_name" content="{SITE_NAME}">\n'
        f'  <meta property="og:title" content="{title}">\n'
        f'  <meta property="og:description" content="{summary}">\n'
        f'  <meta property="og:url" content="{url}">\n'
        '  <meta name="twitter:card" content="summary">\n'
        f"{json_ld(schema)}"
    )


def _graph(*items: dict[str, Any]) -> dict[str, Any]:
    return {"@context": "https://schema.org", "@graph": list(items)}


def _breadcrumbs(*crumbs: tuple[str, str | None]) -> dict[str, Any]:
    items = []
    for position, (name, url) in enumerate(crumbs, start=1):
        item: dict[str, Any] = {"@type": "ListItem", "position": position, "name": name}
        if url:
            item["item"] = url
        items.append(item)
    return {"@type": "BreadcrumbList", "itemListElement": items}


def page_description(knowl: Any) -> str:
    """The summary under the H1, or the first paragraph when it only restates the title."""
    title = plain_text(knowl.title)
    summary = plain_text(knowl.summary)
    if summary and summary.casefold() != title.casefold():
        return truncate(summary)
    for paragraph in re.split(r"\n\s*\n", FENCED_CODE_RE.sub("", knowl.core_markdown)):
        if paragraph.strip() and not paragraph.lstrip().startswith(("#", "|", "- ", "* ", "$$", "\\[")):
            text = plain_text(paragraph)
            if text.casefold() != title.casefold():
                return truncate(text)
    return truncate(summary or title)


def knowl_head(knowl: Any, path: str, subject_id: str, subject_label: str) -> tuple[str, str]:
    """Return the full ``<title>`` text and the extra head tags for a public page."""
    name = plain_text(knowl.title)
    description = page_description(knowl)
    url = absolute_url(path)
    subject_url = absolute_url(f"/index/#subject-{subject_id}")
    if knowl.kind.lower() in DEFINED_TERM_KINDS or (knowl.kind.lower() == "knowl" and not is_statement(knowl)):
        entity: dict[str, Any] = {"@type": "DefinedTerm", "name": name, "description": description, "url": url}
        aliases = display_aliases(knowl)
        if aliases:
            entity["alternateName"] = aliases
        entity["inDefinedTermSet"] = {"@type": "DefinedTermSet", "name": subject_label, "url": subject_url}
    else:
        entity = {"@type": "Article", "headline": name, "description": description, "url": url}
    schema = _graph(
        entity,
        _breadcrumbs((SITE_NAME, absolute_url("/")), (subject_label, subject_url), (name, None)),
    )
    short = short_title(knowl, subject_id, subject_label)
    return full_title(short), head_tags(path, short, description, schema, markdown=True)


def site_page_head(path: str, og_title: str, description: str) -> str:
    """Head tags for a generated page that has no knowl behind it."""
    schema = _graph(
        {"@type": "WebPage", "name": og_title, "description": description, "url": absolute_url(path)},
        _breadcrumbs((SITE_NAME, absolute_url("/")), (og_title, None)),
    )
    return head_tags(path, og_title, description, schema)


def homepage_head(description: str) -> str:
    schema = _graph({"@type": "WebSite", "name": SITE_NAME, "url": absolute_url("/"), "description": description})
    return head_tags("/", SITE_NAME, description, schema)


def rewrite_links(text: str, resolve: Callable[[str], str | None]) -> str:
    """Point source links at canonical HTML pages, leaving math and code untouched."""
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"\x00{len(protected) - 1}\x00"

    def wikilink(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = match.group(2).strip() if match.group(2) else target.split("#", 1)[0].rsplit("/", 1)[-1].replace("-", " ")
        url = resolve(target)
        return f"[{label}]({url})" if url else label

    def markdown_link(match: re.Match[str]) -> str:
        href = match.group(2).strip()
        return f"[{match.group(1)}]({absolute_url(href)})" if href.startswith("/") else match.group(0)

    result = FENCED_CODE_RE.sub(protect, text)
    result = INLINE_CODE_RE.sub(protect, result)
    result = MATH_RE.sub(protect, result)
    result = MARKDOWN_LINK_RE.sub(markdown_link, result)
    result = WIKILINK_RE.sub(wikilink, result)
    # Protected spans can nest (math inside a fenced block), so restore outermost last.
    pattern = re.compile(r"\x00(\d+)\x00")
    while pattern.search(result):
        result = pattern.sub(lambda m: protected[int(m.group(1))], result)
    return result


def markdown_document(knowl: Any, path: str, core: str, resolve: Callable[[str], str | None]) -> str:
    """The published source of a page: title, summary, body and examples."""
    parts = [
        f"Canonical: {absolute_url(path)}",
        f"# {rewrite_links(knowl.title, resolve)}",
        rewrite_links(knowl.summary, resolve),
    ]
    if core.strip():
        parts.append(rewrite_links(core.strip(), resolve))
    for section in knowl.sections:
        body = section.get("markdown", "").strip()
        if body:
            parts.append(f"## {rewrite_links(section['title'], resolve)}\n\n{rewrite_links(body, resolve)}")
    return "\n\n".join(parts) + "\n"


def git_lastmods(content_roots: Iterable[Path]) -> dict[str, str]:
    """Map content-relative paths to last commit dates, newest source winning.

    A shallow clone reports its one fetched commit for every file. Dates are
    omitted in that case, since a wrong ``<lastmod>`` is worse than none.
    """
    dates: dict[str, str] = {}
    for root in content_roots:
        try:
            shallow = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "--is-shallow-repository"],
                capture_output=True, text=True, check=True,
            ).stdout.strip()
            if shallow != "false":
                print(f"NOTE: sitemap omits lastmod for {root}: shallow git history", flush=True)
                continue
            log = subprocess.run(
                ["git", "-C", str(root), "log", "--format=%x00%cs", "--name-only", "--relative", "--", "."],
                capture_output=True, text=True, check=True,
            ).stdout
        except (OSError, subprocess.CalledProcessError):
            print(f"NOTE: sitemap omits lastmod for {root}: no git history", flush=True)
            continue
        date = ""
        for line in log.splitlines():
            if line.startswith("\x00"):
                date = line[1:]
            elif line and line not in dates:
                dates[line] = date
    return dates


def sitemap_xml(entries: Iterable[tuple[str, str | None]]) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, lastmod in entries:
        date = f"<lastmod>{lastmod}</lastmod>" if lastmod else ""
        lines.append(f"  <url><loc>{xml_escape(absolute_url(path))}</loc>{date}</url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def llms_txt(
    knowl_count: int,
    example_path: str,
    long_form: Iterable[tuple[str, str, str]],
    subjects: Iterable[tuple[str, str, int]],
    collections: Iterable[tuple[str, str, int]],
) -> str:
    """Follow the llms.txt convention: title, summary, then sections of links."""
    lines = [
        f"# {SITE_NAME}",
        "",
        f'> A linked library of {knowl_count:,} mathematical definitions, theorems, and reading guides ("knowls"). '
        "Each page gives a compact definition first, links to its prerequisites, and adds examples, proofs, and "
        "references where useful. Free to read, cite, crawl, and use for any purpose, including AI training.",
        "",
        f"Each page has a plain Markdown + LaTeX version at the same path with `index.md` (for example {absolute_url(example_path)}index.md).",
        "",
        "## Start here",
        f"- [Complete index]({absolute_url('/index/')}): every knowl, grouped by subject",
        f"- [Dependency graph]({absolute_url('/graph/')}): prerequisites and dependents",
    ]
    documents = [f"- [{title}]({absolute_url(path)}): {summary}" for title, path, summary in long_form]
    if documents:
        lines += ["", "## Learning paths and long-form documents", *documents]

    def directory(heading: str, rows: Iterable[tuple[str, str, int]]) -> list[str]:
        entries = [
            f"- [{label}]({absolute_url(f'/index/#subject-{subject_id}')}): {count:,} knowl{'s' if count != 1 else ''}"
            for subject_id, label, count in rows
        ]
        return ["", f"## {heading}", *entries] if entries else []

    lines += directory("Subjects", subjects)
    lines += directory("Sources and collections", collections)
    return "\n".join(lines) + "\n"
