"""Source-markup patterns shared by the HTML renderer and the SEO outputs."""

from __future__ import annotations

import re


WIKILINK_RE = re.compile(
    r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*(?:#[^\]|]+)?)(?:\|((?:[^\]]|\](?=\]\])|\](?!\]))*?))?\]\](?!\])"
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
FENCED_CODE_RE = re.compile(
    r"(?ms)^[ \t]*(`{3,})[^\n]*\n.*?^[ \t]*\1`*[ \t]*(?:\n|$)|"
    r"^[ \t]*(~{3,})[^\n]*\n.*?^[ \t]*\2~*[ \t]*(?:\n|$)"
)
MATH_RE = re.compile(
    r"(?s)(\$\$(.+?)\$\$|\\\[(.+?)\\\]|\\\((.+?)\\\)|(?<!\\)\$(?!\$)(.+?)(?<!\\)\$)"
)
