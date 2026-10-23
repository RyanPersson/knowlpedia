"""Draw tikz-cd and simple TikZ diagrams as inline SVG without running TeX.

Cell and label contents are typeset by MathJax in a Node worker
(``mathjax_svg_worker.cjs``), which reports each box's exact width, height and
depth. This module parses the diagram source, lays it out with tikz-cd's
default spacing, routes the arrows, and writes one self-contained SVG whose
strokes and glyphs use ``currentColor``.

Geometry is in 1/1000 em of a 10pt font, the unit of MathJax's glyph outlines,
with y increasing upwards as in TikZ. Only the final SVG output flips y.

Unsupported syntax raises :class:`DiagramError` naming the construct, so an
author sees what to change instead of a silently wrong picture.
"""

from __future__ import annotations

import atexit
import hashlib
import html
import json
import math
import os
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

RENDERER_VERSION = 1

EM = 1000.0
PT = EM / 10
EX = 430.554
CM = 28.45274 * PT
UNITS = {
    "em": EM,
    "ex": EX,
    "pt": PT,
    "bp": PT * 72.27 / 72,
    "mm": CM / 10,
    "cm": CM,
    "in": PT * 72.27,
}

AXIS = 250.0  # math axis height of cmsy10
LINE = 0.4 * PT  # TeX rule thickness and TikZ's default line width
OUTER_SEP = LINE / 2
EQUAL_GAP = 2 * (366.87 - AXIS - LINE)  # gap between the bars of "="
ROUNDED = 4 * PT
LOOSENESS = 0.3915  # TikZ's control-point distance for curved "to" paths
BASELINE_SKIP = 12 * PT

CD_ROW_SEP = {"huge": 3.6 * EM, "large": 2.7 * EM, "normal": 1.8 * EM, "scriptsize": 1.35 * EM, "small": 0.9 * EM, "tiny": 0.45 * EM}
CD_COLUMN_SEP = {"huge": 4.8 * EM, "large": 3.6 * EM, "normal": 2.4 * EM, "scriptsize": 1.8 * EM, "small": 1.2 * EM, "tiny": 0.6 * EM}
CD_CELL_XSEP = EX
CD_CELL_YSEP = 0.85 * EX
CD_LABEL_SEP = 0.5 * EX
CD_SHIFT = 0.56 * EX
CD_CROSSING_CLEARANCE = 1.5 * EX
CD_DASH = (7 * LINE, 4 * LINE)
TIKZ_NODE_SEP = 0.3333 * EM
TIKZ_DASH = (3 * PT, 3 * PT)

# KaTeX sets math at 1.21em of the surrounding text; diagrams match it.
DISPLAY_SCALE = 1.21

POSITIONS = {
    "at start": 0.0,
    "very near start": 0.125,
    "near start": 0.25,
    "midway": 0.5,
    "near end": 0.75,
    "very near end": 0.875,
    "at end": 1.0,
}

DIRECTIONS = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}


class DiagramError(ValueError):
    """The diagram source uses syntax this renderer does not support."""


# --- Geometry helpers -------------------------------------------------------

Point = tuple[float, float]


def add(p: Point, q: Point) -> Point:
    return (p[0] + q[0], p[1] + q[1])


def sub(p: Point, q: Point) -> Point:
    return (p[0] - q[0], p[1] - q[1])


def mul(p: Point, k: float) -> Point:
    return (p[0] * k, p[1] * k)


def length(p: Point) -> float:
    return math.hypot(p[0], p[1])


def unit(p: Point) -> Point:
    size = length(p)
    return (p[0] / size, p[1] / size) if size else (0.0, 0.0)


def left_normal(p: Point) -> Point:
    return (-p[1], p[0])


def rotate(p: Point, degrees: float) -> Point:
    angle = math.radians(degrees)
    return (p[0] * math.cos(angle) - p[1] * math.sin(angle), p[0] * math.sin(angle) + p[1] * math.cos(angle))


def lerp(p: Point, q: Point, t: float) -> Point:
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


def bezier(points: list[Point], t: float) -> Point:
    p0, p1, p2, p3 = points
    s = 1 - t
    return (
        s**3 * p0[0] + 3 * s * s * t * p1[0] + 3 * s * t * t * p2[0] + t**3 * p3[0],
        s**3 * p0[1] + 3 * s * s * t * p1[1] + 3 * s * t * t * p2[1] + t**3 * p3[1],
    )


def bezier_tangent(points: list[Point], t: float) -> Point:
    p0, p1, p2, p3 = points
    s = 1 - t
    tangent = (
        3 * s * s * (p1[0] - p0[0]) + 6 * s * t * (p2[0] - p1[0]) + 3 * t * t * (p3[0] - p2[0]),
        3 * s * s * (p1[1] - p0[1]) + 6 * s * t * (p2[1] - p1[1]) + 3 * t * t * (p3[1] - p2[1]),
    )
    return tangent if length(tangent) > 1e-9 else sub(p3, p0)


def parse_length(text: str, default_unit: float | None = None) -> float:
    match = re.fullmatch(r"\s*([+-]?(?:\d+\.?\d*|\.\d+))\s*([a-z]{2})?\s*", text)
    if not match:
        raise DiagramError(f"Cannot read the length {text.strip()!r}")
    value = float(match.group(1))
    name = match.group(2)
    if name is None:
        if default_unit is None:
            raise DiagramError(f"The length {text.strip()!r} needs a unit")
        return value * default_unit
    if name not in UNITS:
        raise DiagramError(f"Unknown unit {name!r} in {text.strip()!r}")
    return value * UNITS[name]


# --- Source scanning --------------------------------------------------------


def strip_comments(source: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", source)


def read_group(text: str, start: int, opening: str, closing: str) -> tuple[str, int]:
    """Return the contents of the balanced group opening at ``start`` and the index after it."""
    if start >= len(text) or text[start] != opening:
        raise DiagramError(f"Expected {opening!r} in {text[start:start + 40]!r}")
    depth = 0
    brace = 0  # braces protect delimiters inside a [...] or (...) group
    i = start
    while i < len(text):
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if opening != "{" and char in "{}":
            brace += 1 if char == "{" else -1
        elif brace == 0 and char == opening:
            depth += 1
        elif brace == 0 and char == closing:
            depth -= 1
            if depth == 0:
                return text[start + 1 : i], i + 1
        i += 1
    raise DiagramError(f"Unbalanced {opening}{closing} in {text[start:start + 60]!r}")


def split_top(text: str, separator: str = ",") -> list[str]:
    """Split ``text`` on ``separator`` outside braces, brackets, parentheses and quotes."""
    parts: list[str] = []
    depth = 0
    quoted = False
    current: list[str] = []
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\\" and i + 1 < len(text):
            current.append(text[i : i + 2])
            i += 2
            continue
        if char == '"' and depth == 0:
            quoted = not quoted
        elif char in "{[(":
            depth += 1
        elif char in "}])":
            depth -= 1
        elif char == separator and depth == 0 and not quoted:
            parts.append("".join(current))
            current = []
            i += 1
            continue
        current.append(char)
        i += 1
    parts.append("".join(current))
    return [part.strip() for part in parts if part.strip()]


def unbrace(text: str) -> str:
    text = text.strip()
    if text.startswith("{") and text.endswith("}"):
        inner, end = read_group(text, 0, "{", "}")
        if end == len(text):
            return inner
    return text


def split_key(option: str) -> tuple[str, str | None]:
    key, equals, value = option.partition("=")
    return re.sub(r"\s+", " ", key.strip()), (value.strip() if equals else None)


# --- Typesetting ------------------------------------------------------------


@dataclass
class TexBox:
    """A typeset box: width, height above and depth below its baseline, and its SVG."""

    width: float
    height: float
    depth: float
    body: str = ""
    glyphs: dict[str, str] = field(default_factory=dict)
    x: float = 0.0


class MathJaxTypesetter:
    """Client for the MathJax worker; one long-lived Node process per build."""

    def __init__(self, node: Path, module: Path) -> None:
        worker = Path(__file__).with_name("mathjax_svg_worker.cjs")
        env = dict(os.environ)
        env["MATHJAX_MODULE"] = str(module)
        self._process = subprocess.Popen(
            [str(node), str(worker)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            env=env,
        )
        self._cache: dict[tuple[str, bool], TexBox] = {}
        atexit.register(self.close)

    def close(self) -> None:
        if self._process.poll() is None:
            self._process.terminate()

    def box(self, tex: str, display: bool = False) -> TexBox:
        key = (tex, display)
        if key not in self._cache:
            self._cache[key] = self._typeset(tex, display)
        return self._cache[key]

    def _typeset(self, tex: str, display: bool) -> TexBox:
        if self._process.poll() is not None or not self._process.stdin or not self._process.stdout:
            raise DiagramError("The MathJax worker is not running")
        self._process.stdin.write(json.dumps({"tex": tex, "display": display}) + "\n")
        self._process.stdin.flush()
        line = self._process.stdout.readline()
        if not line:
            raise DiagramError("The MathJax worker stopped")
        reply = json.loads(line)
        if "error" in reply:
            raise DiagramError(f"{reply['error']} in {tex!r}")
        return TexBox(reply["width"], reply["height"], reply["depth"], reply["body"], reply["glyphs"], reply["x"])


def stack_lines(lines: list[TexBox], gaps: list[float]) -> TexBox:
    """Stack text lines centred, as TikZ does for ``align=center`` nodes."""
    if len(lines) == 1:
        return lines[0]
    width = max(line.width for line in lines)
    body: list[str] = []
    glyphs: dict[str, str] = {}
    drop = 0.0
    for index, line in enumerate(lines):
        if index:
            drop += BASELINE_SKIP + gaps[index]
        body.append(f'<g transform="translate({fmt((width - line.width) / 2 - line.x)},{fmt(drop)})">{line.body}</g>')
        glyphs.update(line.glyphs)
    return TexBox(width, lines[0].height, drop + lines[-1].depth, "".join(body), glyphs)


def text_to_tex(text: str) -> str:
    """Turn TikZ node text (text mode with ``$...$`` math) into a MathJax expression."""
    pieces = re.split(r"(?<!\\)\$", text)
    if len(pieces) % 2 == 0:
        raise DiagramError(f"Unbalanced $ in node text {text!r}")
    tex: list[str] = []
    for index, piece in enumerate(pieces):
        if index % 2:
            tex.append("{" + piece + "}")
        elif piece.strip():
            tex.append(r"\text{" + piece + "}")
    return "".join(tex) or r"\phantom{}"


# --- Shapes -----------------------------------------------------------------


@dataclass
class Shape:
    """A placed node: a tikz-cd cell, a TikZ rectangle node, or a bare coordinate.

    ``x`` is the horizontal centre and ``base`` the text baseline. tikz-cd cells
    are "asymmetrical rectangles": their centre, east and west anchors sit on
    the math axis, so arrows between cells are level with the operators.
    """

    kind: str
    x: float
    base: float
    box: TexBox | None = None
    xsep: float = 0.0
    ysep: float = 0.0

    @property
    def half_width(self) -> float:
        return (self.box.width / 2 if self.box else 0.0) + self.xsep + OUTER_SEP * (self.kind != "point")

    @property
    def top(self) -> float:
        if self.kind == "point":
            return self.base
        return self.base + (self.box.height if self.box else 0.0) + self.ysep + OUTER_SEP

    @property
    def bottom(self) -> float:
        if self.kind == "point":
            return self.base
        return self.base - (self.box.depth if self.box else 0.0) - self.ysep - OUTER_SEP

    def center(self) -> Point:
        if self.kind == "cell":
            return (self.x, self.base + AXIS)
        if self.kind == "rect":
            return (self.x, (self.top + self.bottom) / 2)
        return (self.x, self.base)

    def anchor(self, name: str) -> Point:
        name = name.strip()
        middle = self.center()[1]
        horizontal = {"west": self.x - self.half_width, "east": self.x + self.half_width}
        points = {
            "center": self.center(),
            "real center": (self.x, (self.top + self.bottom) / 2),
            "base": (self.x, self.base),
            "mid": (self.x, self.base + 0.5 * EX),
            "north": (self.x, self.top),
            "south": (self.x, self.bottom),
            "east": (horizontal["east"], middle),
            "west": (horizontal["west"], middle),
            "north east": (horizontal["east"], self.top),
            "north west": (horizontal["west"], self.top),
            "south east": (horizontal["east"], self.bottom),
            "south west": (horizontal["west"], self.bottom),
            "base east": (horizontal["east"], self.base),
            "base west": (horizontal["west"], self.base),
            "mid east": (horizontal["east"], self.base + 0.5 * EX),
            "mid west": (horizontal["west"], self.base + 0.5 * EX),
        }
        if name in points:
            return points[name]
        if re.fullmatch(r"-?\d+(\.\d+)?", name):
            return self.border(add(self.center(), rotate((1.0, 0.0), float(name))))
        raise DiagramError(f"Unknown anchor {name!r}")

    def border(self, toward: Point) -> Point:
        """The point where the ray from the centre toward ``toward`` leaves the shape."""
        center = self.center()
        if self.kind == "point":
            return center
        dx, dy = sub(toward, center)
        if abs(dx) < 1e-9 and abs(dy) < 1e-9:
            return center
        half_height = self.top - center[1] if dy > 0 else center[1] - self.bottom
        scale = min(
            self.half_width / abs(dx) if abs(dx) > 1e-9 else math.inf,
            half_height / abs(dy) if abs(dy) > 1e-9 else math.inf,
        )
        return (center[0] + dx * scale, center[1] + dy * scale)


def rect_node(box: TexBox, center: Point, inner: float = TIKZ_NODE_SEP) -> Shape:
    base = center[1] - (box.height - box.depth) / 2
    return Shape("rect", center[0], base, box, inner, inner)


def anchored_node(box: TexBox, anchor: str, point: Point, inner: float) -> Shape:
    """Place a rectangle node so that its ``anchor`` lies on ``point``."""
    probe = rect_node(box, (0.0, 0.0), inner)
    offset = probe.anchor(anchor)
    return rect_node(box, sub(point, offset), inner)


# --- Paths ------------------------------------------------------------------


@dataclass
class Segment:
    kind: str  # "line" or "curve"
    points: list[Point]

    @property
    def start(self) -> Point:
        return self.points[0]

    @property
    def end(self) -> Point:
        return self.points[-1]

    def at(self, t: float) -> Point:
        return lerp(self.start, self.end, t) if self.kind == "line" else bezier(self.points, t)

    def tangent(self, t: float) -> Point:
        return sub(self.end, self.start) if self.kind == "line" else bezier_tangent(self.points, t)


@dataclass
class Operation:
    """One path operation (``--``, ``|-``, ``to``...) and the labels placed on it."""

    segments: list[Segment]
    labels: list["Label"] = field(default_factory=list)

    def at(self, pos: float) -> tuple[Point, Point]:
        count = len(self.segments)
        index = min(int(pos * count), count - 1)
        t = pos * count - index
        segment = self.segments[index]
        return segment.at(t), segment.tangent(t)


@dataclass
class Label:
    text: str | None
    pos: float = 0.5
    swap: bool = False
    anchor: str | None = None  # explicit anchor; None means "auto"
    auto: bool = True
    description: bool = False
    shift: Point = (0.0, 0.0)
    style: str = "script"  # tikz-cd labels are \scriptstyle; TikZ node text is text mode
    inner: float = CD_LABEL_SEP
    name: str | None = None
    coordinate: bool = False


@dataclass
class Stroke:
    """A drawn path with its line style and end tips."""

    operations: list[Operation]
    width: float = LINE
    dash: tuple[float, float] | None = None
    double: float | None = None  # gap between the two lines of a double line
    start_tip: tuple[str, dict] | None = None
    end_tip: tuple[str, dict] | None = None
    draw: bool = True
    rounded: float = 0.0
    closed: bool = False
    crossing: bool = False
    shorten_start: float = 0.0
    shorten_end: float = 0.0


# --- Arrow tips -------------------------------------------------------------
#
# Each tip is drawn in its own frame: origin at the tip's reference point, +x
# pointing forward (out of the line at that end), +y to the left. A tip returns
# its outline, how far its visible front lies ahead of the origin (``front``),
# and where the line should stop relative to the origin (``line_end``).


@dataclass
class TipShape:
    paths: list[list[tuple]]  # each path is a list of ("M"|"L"|"C"|"Z", points...)
    front: float
    line_end: float
    fill: bool = False
    width: float = LINE


def cm_to_tip(line: float, reversed_: bool = False) -> TipShape:
    a = 6.2 * line - line
    b = 2.096774 * 6.2 * line - line
    path = [
        ("M", (-a, b / 2)),
        ("C", (-0.81731 * a, 0.2 * b), (-0.41019 * a, 0.0583333 * b), (0.0, 0.0)),
        ("C", (-0.41019 * a, -0.0583333 * b), (-0.81731 * a, -0.2 * b), (-a, -b / 2)),
    ]
    if reversed_:
        path = [(command, *[(-x - a, y) for x, y in points]) for command, *points in path]
        return TipShape([path], line / 2, -a - line / 2, width=line)
    return TipShape([path], line / 2, -line / 2, width=line)


def double_to_tip(line: float) -> TipShape:
    first = cm_to_tip(line)
    a = 6.2 * line - line
    offset = -a + 1.6 * line
    second = [(command, *[(x + offset, y) for x, y in points]) for command, *points in first.paths[0]]
    return TipShape(first.paths + [second], line / 2, offset - line / 2, width=line)


def hook_tip(line: float, side: float) -> TipShape:
    rx = 3.6 * line - line / 2
    ry = (10.8 * line - line) / 4
    k = 0.5523
    path = [
        ("M", (0.0, side * 2 * ry)),
        ("C", (k * rx, side * 2 * ry), (rx, side * (ry + k * ry)), (rx, side * ry)),
        ("C", (rx, side * (ry - k * ry)), (k * rx, 0.0), (0.0, 0.0)),
    ]
    return TipShape([path], rx + line / 2, 0.0, width=line)


def bar_tip(line: float) -> TipShape:
    half = (8.2 * line) / 2 - line / 2
    return TipShape([[("M", (0.0, half)), ("L", (0.0, -half))]], line / 2, 0.0, width=line)


def implies_tip(line: float, gap: float) -> TipShape:
    half = gap / 2 + 2.5 * line
    a = 1.15 * half
    path = [
        ("M", (-a, half)),
        ("C", (-0.7 * a, 0.45 * half), (-0.35 * a, 0.12 * half), (0.0, 0.0)),
        ("C", (-0.35 * a, -0.12 * half), (-0.7 * a, -0.45 * half), (-a, -half)),
    ]
    return TipShape([path], line / 2, -0.55 * a, width=line)


def stealth_tip(line: float, options: dict) -> TipShape:
    size = parse_length(options["length"]) if "length" in options else 3 * PT + 4.5 * line
    width = parse_length(options["width"]) if "width" in options else 0.75 * size
    inset = parse_length(options["inset"]) if "inset" in options else 0.325 * size
    path = [("M", (0.0, 0.0)), ("L", (-size, width / 2)), ("L", (-size + inset, 0.0)), ("L", (-size, -width / 2)), ("Z",)]
    return TipShape([path], 0.0, -size + inset, fill=True, width=line)


def latex_tip(line: float, options: dict) -> TipShape:
    return stealth_tip(line, {"inset": "0pt", **options})


def make_tip(spec: tuple[str, dict], stroke: Stroke) -> TipShape:
    name, options = spec
    line = stroke.width
    if name == "to":
        return cm_to_tip(line)
    if name == "to reversed":
        return cm_to_tip(line, reversed_=True)
    if name == "double to":
        return double_to_tip(line)
    if name == "hook":
        return hook_tip(line, -1.0)
    if name == "hook'":
        return hook_tip(line, 1.0)
    if name == "bar":
        return bar_tip(line)
    if name == "implies":
        return implies_tip(line, stroke.double or EQUAL_GAP)
    if name == "stealth":
        return stealth_tip(line, options)
    if name == "latex":
        return latex_tip(line, options)
    raise DiagramError(f"Unknown arrow tip {name!r}")


def place_tip(tip: TipShape, end: Point, direction: Point) -> list[list[tuple]]:
    """Transform a tip so its front touches ``end``, pointing along ``direction``."""
    forward = unit(direction)
    left = left_normal(forward)
    origin = sub(end, mul(forward, tip.front))

    def transform(point: Point) -> Point:
        return add(origin, add(mul(forward, point[0]), mul(left, point[1])))

    return [[(command, *[transform(p) for p in points]) for command, *points in path] for path in tip.paths]


# --- tikz-cd ----------------------------------------------------------------


@dataclass
class CdArrow:
    row: int
    column: int
    options: list[str]


def parse_tikzcd(source: str) -> tuple[list[str], list[list[str]], list[CdArrow], dict[int, float]]:
    """Split a tikz-cd body into environment options, cell contents, arrows and extra row space."""
    text = strip_comments(source).strip()
    environment_options: list[str] = []
    begin = re.match(r"\\begin\{tikzcd\}\s*", text)
    if begin:
        text = text[begin.end() :]
        if text.startswith("["):
            options, end = read_group(text, 0, "[", "]")
            environment_options = split_top(options)
            text = text[end:]
        end_match = re.search(r"\\end\{tikzcd\}\s*$", text)
        if not end_match:
            raise DiagramError(r"\begin{tikzcd} has no matching \end{tikzcd}")
        text = text[: end_match.start()]
    elif "\\end{tikzcd}" in text:
        raise DiagramError(r"\end{tikzcd} without \begin{tikzcd}")
    if any(split_key(option)[0] == "ampersand replacement" for option in environment_options):
        text = text.replace("\\&", "&")

    rows: list[list[str]] = [[]]
    arrows: list[CdArrow] = []
    extra: dict[int, float] = {}
    cell: list[str] = []
    depth = 0
    i = 0

    def finish_cell() -> None:
        rows[-1].append("".join(cell).strip())
        cell.clear()

    while i < len(text):
        char = text[i]
        if char == "\\":
            if text.startswith("\\\\", i) and depth == 0:
                finish_cell()
                i += 2
                while i < len(text) and text[i].isspace():
                    i += 1
                if i < len(text) and text[i] == "[":
                    amount, i = read_group(text, i, "[", "]")
                    extra[len(rows) - 1] = parse_length(amount)
                rows.append([])
                continue
            shortcut = re.match(r"\\(arrow|ar|[udlr]ar|(?:u|d)(?:l|r)ar)(?![A-Za-z])", text[i:])
            if shortcut and depth == 0:
                command = shortcut.group(1)
                i += shortcut.end()
                while i < len(text) and text[i].isspace():
                    i += 1
                options: list[str] = []
                if i < len(text) and text[i] == "[":
                    body, i = read_group(text, i, "[", "]")
                    options = split_top(body)
                if i < len(text) and text[i] == "{":
                    raise DiagramError(r"Use the \arrow[r, \"f\"] syntax instead of \arrow{r}{f}")
                if command not in {"arrow", "ar"}:
                    options.insert(0, command[:-2])
                if not options and command in {"arrow", "ar"}:
                    raise DiagramError(r"\arrow needs a direction, as in \arrow[r]")
                arrows.append(CdArrow(len(rows) - 1, len(rows[-1]), options))
                continue
            control = re.match(r"\\([A-Za-z]+|.)", text[i:])
            cell.append(control.group(0))
            i += control.end()
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "&" and depth == 0:
            finish_cell()
            i += 1
            continue
        cell.append(char)
        i += 1
    finish_cell()
    if len(rows) > 1 and rows[-1] == [""]:
        rows.pop()
    return environment_options, rows, arrows, extra


def cd_separations(options: list[str]) -> tuple[float, float]:
    row_sep, column_sep = CD_ROW_SEP["normal"], CD_COLUMN_SEP["normal"]

    def amount(value: str | None, named: dict[str, float]) -> float:
        if value is None:
            raise DiagramError("row sep and column sep need a value")
        value = unbrace(value)
        return named[value] if value in named else parse_length(value)

    for option in options:
        key, value = split_key(option)
        if key == "row sep":
            row_sep = amount(value, CD_ROW_SEP)
        elif key == "column sep":
            column_sep = amount(value, CD_COLUMN_SEP)
        elif key == "sep":
            row_sep = amount(value, CD_ROW_SEP)
            column_sep = amount(value, CD_COLUMN_SEP)
        elif key == "ampersand replacement":
            continue
        else:
            raise DiagramError(f"Unsupported tikz-cd environment option {option!r}")
    return row_sep, column_sep


LABEL_KEYS = ("very near start", "very near end", "near start", "near end", "at start", "at end", "midway", "description", "swap", "coordinate", "marking")


def parse_cd_label(option: str) -> Label:
    """Parse a tikz-cd quoted label such as ``"f"'``, ``"g" near start`` or ``""{coordinate, name=Z}``."""
    closing = 1
    depth = 0
    while closing < len(option):
        char = option[closing]
        if char == "\\":
            closing += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == '"' and depth == 0:
            break
        closing += 1
    else:
        raise DiagramError(f"Unclosed label quote in {option!r}")
    label = Label(unbrace(option[1:closing]))
    rest = option[closing + 1 :].strip()
    if rest.startswith("'"):
        label.swap = True
        rest = rest[1:].strip()
    if rest.startswith("{"):
        words = split_top(unbrace(rest))
    else:
        words = []
        while rest:
            for key in LABEL_KEYS:
                if rest.startswith(key):
                    words.append(key)
                    rest = rest[len(key) :].strip()
                    break
            else:
                match = re.match(r"(pos|name|anchor|inner sep)\s*=\s*(\S+)", rest)
                if not match:
                    raise DiagramError(f"Unsupported label option {rest!r}")
                words.append(match.group(0))
                rest = rest[match.end() :].strip()
    for word in words:
        apply_label_option(label, word)
    return label


def apply_label_option(label: Label, option: str) -> None:
    key, value = split_key(option)
    if key in POSITIONS:
        label.pos = POSITIONS[key]
    elif key == "pos" and value is not None:
        label.pos = float(value)
    elif key in {"swap", "'"}:
        label.swap = True
    elif key == "description":
        label.description = True
        label.auto = False
        label.anchor = "center"
    elif key == "marking":
        label.auto = False
        label.anchor = "center"
        label.style = "text"
    elif key == "coordinate":
        label.coordinate = True
    elif key == "name" and value is not None:
        label.name = value
    elif key == "anchor" and value is not None:
        label.auto = False
        label.anchor = value
    elif key == "inner sep" and value is not None:
        label.inner = parse_length(value)
    else:
        raise DiagramError(f"Unsupported label option {option!r}")


@dataclass
class CdArrowSpec:
    target: tuple[int, int]
    stroke: Stroke
    labels: list[Label]
    bend: float = 0.0
    shift: float = 0.0
    start_anchor: str | None = None
    end_anchor: str | None = None
    to_path: str | None = None
    phantom: bool = False


def cd_arrow_spec(arrow: CdArrow) -> CdArrowSpec:
    stroke = Stroke([], end_tip=("to", {}))
    labels: list[Label] = []
    spec = CdArrowSpec((arrow.row, arrow.column), stroke, labels)
    label_defaults: list[str] = []
    direction = None
    for option in arrow.options:
        if option.startswith('"'):
            labels.append(parse_cd_label(option))
            continue
        key, value = split_key(option)
        if re.fullmatch(r"[udlr]+", key) and value is None:
            direction = key
        elif key in {"dashed", "dashrightarrow"}:
            stroke.dash = CD_DASH
            if key == "dashrightarrow":
                stroke.end_tip = ("to", {})
        elif key == "dotted":
            stroke.dash = (LINE, 2 * PT)
        elif key in {"two heads", "twoheadrightarrow"}:
            stroke.end_tip = ("double to", {})
        elif key in {"hook", "hookrightarrow"}:
            stroke.start_tip = ("hook", {})
        elif key == "hook'":
            stroke.start_tip = ("hook'", {})
        elif key in {"tail", "rightarrowtail"}:
            stroke.start_tip = ("to reversed", {})
        elif key in {"maps to", "mapsto"}:
            stroke.start_tip = ("bar", {})
        elif key in {"rightarrow", "to head"}:
            stroke.end_tip = ("to", {})
        elif key == "leftarrow":
            stroke.start_tip, stroke.end_tip = ("to", {}), None
        elif key == "leftrightarrow":
            stroke.start_tip, stroke.end_tip = ("to", {}), ("to", {})
        elif key in {"no head", "dash", "-"}:
            stroke.end_tip = None
            if key == "dash":
                stroke.start_tip = None
        elif key in {"equal", "equals"}:
            stroke.double = EQUAL_GAP
            stroke.start_tip = stroke.end_tip = None
        elif key in {"Rightarrow", "Leftarrow", "Leftrightarrow", "Mapsto"}:
            stroke.double = EQUAL_GAP
            stroke.end_tip = ("implies", {}) if key != "Leftarrow" else None
            stroke.start_tip = ("implies", {}) if key in {"Leftarrow", "Leftrightarrow"} else None
            if key == "Mapsto":
                stroke.start_tip = ("bar", {})
        elif key == "phantom":
            spec.phantom = True
            stroke.draw = False
        elif key == "crossing over":
            stroke.crossing = True
        elif key in {"bend left", "bend right"}:
            angle = float(value) if value is not None else 30.0
            spec.bend = angle if key == "bend left" else -angle
        elif key in {"shift left", "shift right"}:
            amount = CD_SHIFT if value is None else parse_length(unbrace(value), CD_SHIFT)
            spec.shift = amount if key == "shift left" else -amount
        elif key == "start anchor" and value is not None:
            spec.start_anchor = unbrace(value) or None
        elif key == "end anchor" and value is not None:
            spec.end_anchor = unbrace(value) or None
        elif key == "to path" and value is not None:
            spec.to_path = unbrace(value)
        elif key == "rounded corners":
            stroke.rounded = ROUNDED if value is None else parse_length(value)
        elif key in {"shorten", "shorten <", "shorten >"} and value is not None:
            apply_shorten(stroke, key, value)
        elif key in {"thick", "very thick", "thin", "semithick", "ultra thick"} or key == "line width":
            stroke.width = line_width(key, value)
        elif key in POSITIONS or key in {"swap", "'", "description"} or key == "pos":
            label_defaults.append(option)
        else:
            raise DiagramError(f"Unsupported tikz-cd arrow option {option!r}")
    if direction is None and spec.to_path is None:
        raise DiagramError(f"Arrow without a direction: [{', '.join(arrow.options)}]")
    if direction:
        dx = sum(DIRECTIONS[c][0] for c in direction)
        dy = sum(DIRECTIONS[c][1] for c in direction)
        spec.target = (arrow.row + dy, arrow.column + dx)
    for label in labels:
        for option in label_defaults:
            if split_key(option)[0] in POSITIONS or split_key(option)[0] == "pos":
                if label.pos == 0.5:
                    apply_label_option(label, option)
            else:
                apply_label_option(label, option)
        if spec.phantom:
            label.auto = False
            label.anchor = "center"
            label.style = "text"
    return spec


def apply_shorten(stroke: Stroke, key: str, value: str) -> None:
    """``shorten <=2pt`` reaches here as key ``shorten <`` and value ``2pt``."""
    amount = parse_length(value)
    if key in {"shorten", "shorten <"}:
        stroke.shorten_start = amount
    if key in {"shorten", "shorten >"}:
        stroke.shorten_end = amount


def line_width(key: str, value: str | None) -> float:
    widths = {"thin": 0.4 * PT, "semithick": 0.6 * PT, "thick": 0.8 * PT, "very thick": 1.2 * PT, "ultra thick": 1.6 * PT}
    if key in widths:
        return widths[key]
    if value is None:
        raise DiagramError("line width needs a value")
    return parse_length(value)


def render_tikzcd(source: str, typesetter: MathJaxTypesetter) -> "Drawing":
    environment_options, rows, arrows, extra = parse_tikzcd(source)
    row_sep, column_sep = cd_separations(environment_options)
    columns = max(len(row) for row in rows)
    boxes = [[typesetter.box(cell) if cell else None for cell in row] + [None] * (columns - len(row)) for row in rows]

    heights = [max([box.height + CD_CELL_YSEP + OUTER_SEP for box in row if box] or [0.0]) for row in boxes]
    depths = [max([box.depth + CD_CELL_YSEP + OUTER_SEP for box in row if box] or [0.0]) for row in boxes]
    half_widths = [
        max([boxes[r][c].width / 2 + CD_CELL_XSEP + OUTER_SEP for r in range(len(rows)) if boxes[r][c]] or [0.0])
        for c in range(columns)
    ]
    baselines = [0.0]
    for r in range(1, len(rows)):
        baselines.append(baselines[-1] - depths[r - 1] - row_sep - extra.get(r - 1, 0.0) - heights[r])
    centers = [0.0]
    for c in range(1, columns):
        centers.append(centers[-1] + half_widths[c - 1] + column_sep + half_widths[c])

    def cell(row: int, column: int) -> Shape:
        if not (0 <= row < len(rows) and 0 <= column < columns):
            raise DiagramError(f"An arrow points outside the diagram, to row {row + 1}, column {column + 1}")
        box = boxes[row][column]
        if box is None:
            return Shape("point", centers[column], baselines[row] + AXIS)
        return Shape("cell", centers[column], baselines[row], box, CD_CELL_XSEP, CD_CELL_YSEP)

    drawing = Drawing()
    for r, row in enumerate(boxes):
        for c, box in enumerate(row):
            if box:
                drawing.add_shape_text(cell(r, c))

    specs = [cd_arrow_spec(arrow) for arrow in arrows]
    named: dict[str, Shape] = {}
    routed: dict[int, Stroke] = {}
    # Arrows drawn with a custom "to path" may refer to coordinates named on
    # other arrows' labels, so they are routed after all the others.
    for index in sorted(range(len(arrows)), key=lambda i: specs[i].to_path is not None):
        arrow, spec = arrows[index], specs[index]
        start = cell(arrow.row, arrow.column)
        target = cell(*spec.target)
        if spec.to_path is not None:
            operations = parse_path(
                "(\\tikztostart) " + spec.to_path,
                PathContext(named, {"\\tikztostart": start, "\\tikztotarget": target}, CM),
                spec.labels,
            )
        else:
            operations = [Operation([route_between(start, target, spec)], list(spec.labels))]
        spec.stroke.operations = operations
        routed[index] = spec.stroke
        for operation in operations:
            for label in operation.labels:
                if label.name:
                    point, _ = operation.at(label.pos)
                    named[label.name] = Shape("point", point[0], point[1])
    for index in range(len(arrows)):
        drawing.add_stroke(routed[index], typesetter)
    return drawing


def route_between(start: Shape, target: Shape, spec: CdArrowSpec) -> Segment:
    a, b = start.center(), target.center()
    if spec.bend:
        direction = sub(b, a)
        out = add(a, rotate(direction, spec.bend))
        inward = add(b, rotate(mul(direction, -1), -spec.bend))
        p0 = start.anchor(spec.start_anchor) if spec.start_anchor else start.border(out)
        p3 = target.anchor(spec.end_anchor) if spec.end_anchor else target.border(inward)
        distance = LOOSENESS * length(sub(p3, p0))
        c1 = add(p0, mul(unit(rotate(direction, spec.bend)), distance))
        c2 = add(p3, mul(unit(rotate(mul(direction, -1), -spec.bend)), distance))
        segment = Segment("curve", [p0, c1, c2, p3])
    else:
        p0 = start.anchor(spec.start_anchor) if spec.start_anchor else start.border(b)
        p1 = target.anchor(spec.end_anchor) if spec.end_anchor else target.border(a)
        segment = Segment("line", [p0, p1])
    if spec.shift:
        offset = mul(unit(left_normal(sub(segment.end, segment.start))), spec.shift)
        segment = Segment(segment.kind, [add(point, offset) for point in segment.points])
    return segment


# --- TikZ paths -------------------------------------------------------------


@dataclass
class PathContext:
    named: dict[str, Shape]
    special: dict[str, Shape] = field(default_factory=dict)
    default_unit: float = CM


@dataclass
class Ref:
    """A path coordinate: a point, possibly a node whose border clips the path."""

    point: Point
    shape: Shape | None = None


def evaluate_coordinate(text: str, context: PathContext) -> Ref:
    text = text.strip()
    if text.startswith("["):
        options, end = read_group(text, 0, "[", "]")
        ref = evaluate_coordinate(text[end:], context)
        dx = dy = 0.0
        for option in split_top(options):
            key, value = split_key(option)
            if key == "xshift" and value is not None:
                dx += parse_length(value, PT)
            elif key == "yshift" and value is not None:
                dy += parse_length(value, PT)
            else:
                raise DiagramError(f"Unsupported coordinate option {option!r}")
        return Ref(add(ref.point, (dx, dy)))
    if text.startswith("$") and text.endswith("$"):
        return Ref(evaluate_calc(text[1:-1], context))
    polar = re.fullmatch(r"([+-]?[\d.]+)\s*:\s*(.+)", text)
    if polar:
        return Ref(rotate((parse_length(polar.group(2), context.default_unit), 0.0), float(polar.group(1))))
    if "," in text and not re.match(r"\\?[A-Za-z]", text.strip()):
        x, y = split_top(text)
        return Ref((parse_length(x, context.default_unit), parse_length(y, context.default_unit)))
    name, dot, anchor = text.partition(".")
    shape = context.special.get(name) or context.named.get(name)
    if shape is None:
        raise DiagramError(f"Unknown coordinate ({text})")
    if dot:
        return Ref(shape.anchor(anchor))
    return Ref(shape.center(), shape)


def evaluate_calc(expression: str, context: PathContext) -> Point:
    expression = expression.strip()
    partway = re.fullmatch(r"(\(.*?\))\s*!\s*([+-]?[\d.]+)\s*!\s*(\(.*\))", expression)
    if partway:
        p = evaluate_coordinate(partway.group(1)[1:-1], context).point
        q = evaluate_coordinate(partway.group(3)[1:-1], context).point
        return lerp(p, q, float(partway.group(2)))
    total = (0.0, 0.0)
    i = 0
    sign = 1.0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
        elif char in "+-":
            sign = 1.0 if char == "+" else -1.0
            i += 1
        elif char == "(":
            inner, i = read_group(expression, i, "(", ")")
            total = add(total, mul(evaluate_coordinate(inner, context).point, sign))
            sign = 1.0
        else:
            raise DiagramError(f"Unsupported calc expression ${expression}$")
    return total


def parse_tikz_node_options(options: list[str], label: Label) -> None:
    placements = {
        "above": "south",
        "below": "north",
        "left": "east",
        "right": "west",
        "above left": "south east",
        "above right": "south west",
        "below left": "north east",
        "below right": "north west",
    }
    for option in options:
        key, value = split_key(option)
        if key in placements:
            label.auto = False
            label.anchor = placements[key]
            if value is not None:
                distance = parse_length(value, CM)
                vector = {"south": (0, 1), "north": (0, -1), "east": (-1, 0), "west": (1, 0)}
                for part in placements[key].split():
                    label.shift = add(label.shift, mul(vector[part], distance))
        elif key == "align":
            continue
        elif key == "auto":
            label.auto = True
            label.anchor = None
        else:
            apply_label_option(label, option)


def parse_path(
    text: str,
    context: PathContext,
    inserted_labels: list[Label] | None = None,
    to_defaults: list[str] | None = None,
) -> list[Operation]:
    """Parse a TikZ path such as ``(A) -- node[above] {$f$} (B) to[bend left] (C)``."""
    operations: list[Operation] = []
    current: Ref | None = None
    pending: tuple[str, list[str]] | None = None
    pending_labels: list[Label] = []
    i = 0

    def skip() -> None:
        nonlocal i
        while i < len(text) and text[i].isspace():
            i += 1

    def attach(label: Label) -> None:
        # A node written after an operator and before its target belongs to
        # that operation; one written after a coordinate belongs to the
        # operation that ended there, or sits on the coordinate itself.
        if pending is not None:
            pending_labels.append(label)
        elif operations:
            operations[-1].labels.append(label)
        elif current is not None:
            operations.append(Operation([Segment("line", [current.point, current.point])], [label]))
        else:
            raise DiagramError("A node on a path has no position")

    while True:
        skip()
        if i >= len(text):
            break
        rest = text[i:]
        if rest.startswith("("):
            inner, i = read_group(text, i, "(", ")")
            ref = evaluate_coordinate(inner, context)
            if pending is None:
                current = ref
                continue
            if current is None:
                raise DiagramError("A path operation has no starting point")
            operation = build_operation(pending[0], pending[1], current, ref)
            operation.labels.extend(pending_labels)
            operations.append(operation)
            pending_labels = []
            pending = None
            current = ref
            continue
        match = re.match(r"(--|\|-|-\||rectangle\b|to\b)", rest)
        if match:
            operator = match.group(1)
            i += match.end()
            skip()
            options = list(to_defaults or []) if operator == "to" else []
            if operator == "to" and i < len(text) and text[i] == "[":
                body, i = read_group(text, i, "[", "]")
                options += split_top(body)
            pending = (operator, options)
            continue
        match = re.match(r"(?:\[([^\]]*)\]\s*)?\\tikztonodes\b", rest)
        if match:
            i += match.end()
            for label in inserted_labels or []:
                if match.group(1):
                    for option in split_top(match.group(1)):
                        apply_label_option(label, option)
                attach(label)
            continue
        match = re.match(r"node\b", rest)
        if match:
            i += match.end()
            skip()
            label = Label(None, style="tikz", inner=TIKZ_NODE_SEP, auto=False, anchor="center")
            if i < len(text) and text[i] == "[":
                body, i = read_group(text, i, "[", "]")
                parse_tikz_node_options(split_top(body), label)
                skip()
            if i < len(text) and text[i] == "(":
                _, i = read_group(text, i, "(", ")")
                skip()
            label.text, i = read_group(text, i, "{", "}")
            attach(label)
            continue
        if rest.startswith("cycle"):
            raise DiagramError("cycle paths are not supported")
        raise DiagramError(f"Cannot read the path at {rest[:40]!r}")

    if pending is not None:
        raise DiagramError(f"The path ends after {pending[0]!r}")
    return operations


def build_operation(operator: str, options: list[str], start: Ref, end: Ref) -> Operation:
    if operator == "--":
        p0 = start.shape.border(end.point) if start.shape else start.point
        p1 = end.shape.border(start.point) if end.shape else end.point
        return Operation([Segment("line", [p0, p1])])
    if operator in {"|-", "-|"}:
        corner = (start.point[0], end.point[1]) if operator == "|-" else (end.point[0], start.point[1])
        p0 = start.shape.border(corner) if start.shape else start.point
        p1 = end.shape.border(corner) if end.shape else end.point
        return Operation([Segment("line", [p0, corner]), Segment("line", [corner, p1])])
    if operator == "rectangle":
        (x0, y0), (x1, y1) = start.point, end.point
        corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
        return Operation([Segment("line", [corners[k], corners[k + 1]]) for k in range(4)])
    bend = 0.0
    for option in options:
        key, value = split_key(option)
        if key in {"bend left", "bend right"}:
            angle = float(value) if value is not None else 30.0
            bend = angle if key == "bend left" else -angle
        else:
            raise DiagramError(f"Unsupported to option {option!r}")
    if not bend:
        return build_operation("--", [], start, end)
    direction = sub(end.point, start.point)
    p0 = start.shape.border(add(start.point, rotate(direction, bend))) if start.shape else start.point
    p3 = end.shape.border(add(end.point, rotate(mul(direction, -1), -bend))) if end.shape else end.point
    distance = LOOSENESS * length(sub(p3, p0))
    c1 = add(p0, mul(unit(rotate(direction, bend)), distance))
    c2 = add(p3, mul(unit(rotate(mul(direction, -1), -bend)), distance))
    return Operation([Segment("curve", [p0, c1, c2, p3])])


# --- Drawing and SVG output -------------------------------------------------


def fmt(value: float) -> str:
    text = f"{value:.1f}".rstrip("0").rstrip(".")
    return "0" if text in {"-0", ""} else text


def segments_of(stroke: Stroke) -> list[Segment]:
    return [Segment(s.kind, list(s.points)) for operation in stroke.operations for s in operation.segments]


def shorten(segments: list[Segment], amount: float, at_end: bool) -> None:
    if amount <= 0 or not segments:
        return
    segment = segments[-1] if at_end else segments[0]
    points = segment.points
    if at_end:
        direction = unit(segment.tangent(1.0))
        points[-1] = sub(points[-1], mul(direction, amount))
        if segment.kind == "curve":
            points[-2] = sub(points[-2], mul(direction, amount))
    else:
        direction = unit(segment.tangent(0.0))
        points[0] = add(points[0], mul(direction, amount))
        if segment.kind == "curve":
            points[1] = add(points[1], mul(direction, amount))


def path_commands(segments: list[Segment], radius: float, closed: bool) -> list[tuple]:
    if radius and segments and all(s.kind == "line" for s in segments) and len(segments) > 1:
        vertices = [segments[0].start] + [s.end for s in segments]
        return rounded_commands(vertices, radius, closed)
    commands: list[tuple] = [("M", segments[0].start)]
    for segment in segments:
        if segment.kind == "line":
            commands.append(("L", segment.end))
        else:
            commands.append(("C", *segment.points[1:]))
    if closed:
        commands.append(("Z",))
    return commands


def rounded_commands(vertices: list[Point], radius: float, closed: bool) -> list[tuple]:
    """Round each corner of a polyline as TikZ's ``rounded corners`` does."""
    k = 0.5523

    def corner(previous: Point, vertex: Point, following: Point) -> tuple[Point, Point]:
        r = min(radius, length(sub(vertex, previous)) / 2, length(sub(following, vertex)) / 2)
        return add(vertex, mul(unit(sub(previous, vertex)), r)), add(vertex, mul(unit(sub(following, vertex)), r))

    if closed:
        points = vertices[:-1]
        commands: list[tuple] = []
        for index, vertex in enumerate(points):
            a, b = corner(points[index - 1], vertex, points[(index + 1) % len(points)])
            commands.append(("M" if index == 0 else "L", a))
            commands.append(("C", lerp(a, vertex, k), lerp(b, vertex, k), b))
        commands.append(("Z",))
        return commands
    commands = [("M", vertices[0])]
    for index in range(1, len(vertices) - 1):
        a, b = corner(vertices[index - 1], vertices[index], vertices[index + 1])
        commands.append(("L", a))
        commands.append(("C", lerp(a, vertices[index], k), lerp(b, vertices[index], k), b))
    commands.append(("L", vertices[-1]))
    return commands


def auto_anchor(direction: Point, swap: bool) -> str:
    """TikZ's ``auto`` placement: put the label left of the path (right if swapped)."""
    dx, dy = unit(direction)
    if not swap:
        if dx > 0.05:
            return "south east" if dy > 0.05 else "south west" if dy < -0.05 else "south"
        if dx < -0.05:
            return "north east" if dy > 0.05 else "north west" if dy < -0.05 else "north"
        return "east" if dy > 0 else "west"
    if dx > 0.05:
        return "north west" if dy > 0.05 else "north east" if dy < -0.05 else "north"
    if dx < -0.05:
        return "south west" if dy > 0.05 else "south east" if dy < -0.05 else "south"
    return "west" if dy > 0 else "east"


def split_lines(text: str) -> tuple[list[str], list[float]]:
    lines: list[str] = []
    gaps: list[float] = [0.0]
    current: list[str] = []
    depth = 0
    i = 0
    while i < len(text):
        if text.startswith("\\\\", i) and depth == 0:
            lines.append("".join(current))
            current = []
            i += 2
            gap = 0.0
            if i < len(text) and text[i] == "[":
                amount, i = read_group(text, i, "[", "]")
                gap = parse_length(amount)
            gaps.append(gap)
            continue
        char = text[i]
        if char == "\\":
            current.append(text[i : i + 2])
            i += 2
            continue
        depth += {"{": 1, "}": -1}.get(char, 0)
        current.append(char)
        i += 1
    lines.append("".join(current))
    return lines, gaps


class Drawing:
    """Collects text, strokes and tips in TikZ coordinates and writes one SVG."""

    def __init__(self) -> None:
        self.items: list[str] = []
        self.glyphs: dict[str, str] = {}
        self.bounds = [math.inf, math.inf, -math.inf, -math.inf]
        self._typesetter: MathJaxTypesetter | None = None

    def include(self, point: Point, pad: float = 0.0) -> None:
        self.bounds[0] = min(self.bounds[0], point[0] - pad)
        self.bounds[1] = min(self.bounds[1], point[1] - pad)
        self.bounds[2] = max(self.bounds[2], point[0] + pad)
        self.bounds[3] = max(self.bounds[3], point[1] + pad)

    def add_text(self, box: TexBox, left: float, baseline: float) -> None:
        self.glyphs.update(box.glyphs)
        self.items.append(f'<g transform="translate({fmt(left - box.x)},{fmt(-baseline)})">{box.body}</g>')
        self.include((left, baseline - box.depth))
        self.include((left + box.width, baseline + box.height))

    def add_shape_text(self, shape: Shape) -> None:
        assert shape.box is not None
        self.add_text(shape.box, shape.x - shape.box.width / 2, shape.base)
        self.include((shape.x - shape.half_width, shape.bottom))
        self.include((shape.x + shape.half_width, shape.top))

    def add_path(
        self,
        commands: list[tuple],
        width: float,
        *,
        dash: tuple[float, float] | None = None,
        fill: bool = False,
        knockout: bool = False,
        round_ends: bool = False,
    ) -> None:
        parts: list[str] = []
        for command, *points in commands:
            parts.append(command + " ".join(f"{fmt(x)} {fmt(-y)}" for x, y in points))
            for point in points:
                self.include(point, width / 2)
        color = "var(--diagram-knockout,#fff)" if knockout else "currentColor"
        attributes = [f'd="{" ".join(parts)}"']
        if knockout:
            attributes.append(f'style="stroke:{color}"')
            attributes.append('fill="none"')
        else:
            attributes.append('stroke="currentColor"')
            attributes.append('fill="currentColor"' if fill else 'fill="none"')
        attributes.append(f'stroke-width="{fmt(width)}"')
        if dash:
            attributes.append(f'stroke-dasharray="{fmt(dash[0])} {fmt(dash[1])}"')
        if round_ends:
            attributes.append('stroke-linecap="round" stroke-linejoin="round"')
        self.items.append(f"<path {' '.join(attributes)}/>")

    def add_box(self, shape: Shape) -> None:
        """Paint a label's background, as tikz-cd's ``description`` style does."""
        left = shape.x - shape.half_width + OUTER_SEP
        right = shape.x + shape.half_width - OUTER_SEP
        top, bottom = shape.top - OUTER_SEP, shape.bottom + OUTER_SEP
        self.items.append(
            f'<rect x="{fmt(left)}" y="{fmt(-top)}" width="{fmt(right - left)}" height="{fmt(top - bottom)}" '
            'style="fill:var(--diagram-knockout,#fff)"/>'
        )

    def add_stroke(self, stroke: Stroke, typesetter: MathJaxTypesetter) -> None:
        segments = segments_of(stroke)
        if stroke.draw and segments:
            shorten(segments, stroke.shorten_start, at_end=False)
            shorten(segments, stroke.shorten_end, at_end=True)
            tips: list[list[list[tuple]]] = []
            for spec, at_end in ((stroke.start_tip, False), (stroke.end_tip, True)):
                if not spec:
                    continue
                tip = make_tip(spec, stroke)
                segment = segments[-1] if at_end else segments[0]
                end = segment.end if at_end else segment.start
                forward = segment.tangent(1.0) if at_end else mul(segment.tangent(0.0), -1)
                tips.append((place_tip(tip, end, forward), tip))
                shorten(segments, tip.front - tip.line_end, at_end)
            commands = path_commands(segments, stroke.rounded, stroke.closed)
            if stroke.crossing:
                self.add_path(commands, CD_CROSSING_CLEARANCE, knockout=True)
            if stroke.double:
                self.add_path(commands, 2 * stroke.width + stroke.double, dash=stroke.dash)
                self.add_path(commands, stroke.double, knockout=True)
            else:
                self.add_path(commands, stroke.width, dash=stroke.dash)
            for paths, tip in tips:
                for path in paths:
                    self.add_path(path, tip.width, fill=tip.fill, round_ends=not tip.fill)
        for operation in stroke.operations:
            for label in operation.labels:
                point, tangent = operation.at(label.pos)
                self.add_label(label, point, tangent, typesetter)

    def add_label(self, label: Label, point: Point, tangent: Point, typesetter: MathJaxTypesetter) -> None:
        if label.coordinate or label.text is None or not label.text.strip():
            return
        if label.style == "script":
            box = typesetter.box("{\\scriptstyle " + label.text + "}")
        elif label.style == "tikz":
            lines, gaps = split_lines(label.text)
            box = stack_lines([typesetter.box(text_to_tex(line)) for line in lines], gaps)
        else:
            box = typesetter.box(label.text)
        anchor = auto_anchor(tangent, label.swap) if label.auto else (label.anchor or "center")
        shape = anchored_node(box, anchor, add(point, label.shift), label.inner)
        if label.description:
            self.add_box(shape)
        self.add_shape_text(shape)

    def to_svg(self, prefix: str, description: str) -> str:
        if not self.items:
            raise DiagramError("The diagram is empty")
        x0, y0, x1, y1 = self.bounds
        x0, y0, x1, y1 = x0 - LINE, y0 - LINE, x1 + LINE, y1 + LINE
        width, height = x1 - x0, y1 - y0
        defs = "".join(f'<path id="{prefix}{key}" d="{d}"/>' for key, d in sorted(self.glyphs.items()))
        body = "".join(self.items).replace('href="#@', f'href="#{prefix}')
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x0)} {fmt(-y1)} {fmt(width)} {fmt(height)}" '
            f'width="{width / EM * DISPLAY_SCALE:.3f}em" height="{height / EM * DISPLAY_SCALE:.3f}em" '
            'role="img" focusable="false">'
            f"<title>Commutative diagram</title><desc>{html.escape(description)}</desc>"
            f"<defs>{defs}</defs>{body}</svg>"
        )


# --- General TikZ pictures ---------------------------------------------------


TIP_NAMES = {">": "to", "<": "to", "to": "to", "To": "to", "Stealth": "stealth", "Latex": "latex", "|": "bar", "Bar": "bar"}


def tikz_tip(text: str) -> tuple[str, dict] | None:
    text = unbrace(text.strip())
    if not text:
        return None
    match = re.fullmatch(r"([A-Za-z]+|>|<|\|)\s*(?:\[(.*)\])?", text)
    if not match or match.group(1) not in TIP_NAMES:
        raise DiagramError(f"Unsupported arrow tip {text!r}")
    options = dict(split_key(option) for option in split_top(match.group(2) or ""))
    return TIP_NAMES[match.group(1)], options


def apply_draw_option(stroke: Stroke, option: str, to_defaults: list[str]) -> None:
    key, value = split_key(option)
    arrow = re.fullmatch(r"(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}|[^-{}=]*)-(\{.*\}|[^-{}=]*)", option.strip())
    if arrow and key not in {"rounded corners"}:
        stroke.start_tip = tikz_tip(arrow.group(1))
        stroke.end_tip = tikz_tip(arrow.group(2))
    elif key == "dashed":
        stroke.dash = TIKZ_DASH
    elif key == "dotted":
        stroke.dash = (LINE, 2 * PT)
    elif key in {"thick", "very thick", "thin", "semithick", "ultra thick", "line width"}:
        stroke.width = line_width(key, value)
    elif key == "rounded corners":
        stroke.rounded = ROUNDED if value is None else parse_length(value)
    elif key in {"bend left", "bend right"}:
        to_defaults.append(option)
    elif key == "double distance" and value is not None:
        stroke.double = parse_length(value)
    elif key == "double":
        stroke.double = stroke.double or 0.6 * PT
    elif key in {"shorten", "shorten <", "shorten >"} and value is not None:
        apply_shorten(stroke, key, value)
    elif key == "draw":
        stroke.draw = True
    else:
        raise DiagramError(f"Unsupported TikZ draw option {option!r}")


def render_tikz(source: str, typesetter: MathJaxTypesetter) -> Drawing:
    text = strip_comments(source).strip()
    begin = re.match(r"\\begin\{tikzpicture\}\s*", text)
    if begin:
        text = text[begin.end() :]
        if text.startswith("["):
            options, _ = read_group(text, 0, "[", "]")
            raise DiagramError(f"Unsupported tikzpicture options [{options}]")
        text = re.sub(r"\\end\{tikzpicture\}\s*$", "", text)
    named: dict[str, Shape] = {}
    context = PathContext(named, {}, CM)
    drawing = Drawing()
    for statement in split_top(text, ";"):
        command = re.match(r"\\(node|coordinate|draw|path)\b\s*", statement)
        if not command:
            raise DiagramError(f"Unsupported TikZ command {statement[:40]!r}")
        rest = statement[command.end() :]
        options: list[str] = []
        if rest.startswith("["):
            body, end = read_group(rest, 0, "[", "]")
            options = split_top(body)
            rest = rest[end:].strip()
        if command.group(1) in {"node", "coordinate"}:
            name = None
            if rest.startswith("("):
                name, end = read_group(rest, 0, "(", ")")
                rest = rest[end:].strip()
            at = re.match(r"at\s*", rest)
            if not at:
                raise DiagramError(f"\\{command.group(1)} needs an 'at (x,y)' position")
            coordinate, end = read_group(rest, at.end(), "(", ")")
            point = evaluate_coordinate(coordinate, context).point
            rest = rest[end:].strip()
            if command.group(1) == "coordinate":
                if name:
                    named[name] = Shape("point", point[0], point[1])
                continue
            content, _ = read_group(rest, 0, "{", "}")
            label = Label(content, style="tikz", inner=TIKZ_NODE_SEP, auto=False, anchor="center")
            parse_tikz_node_options(options, label)
            lines, gaps = split_lines(content)
            box = stack_lines([typesetter.box(text_to_tex(line)) for line in lines], gaps)
            shape = anchored_node(box, label.anchor or "center", add(point, label.shift), label.inner)
            drawing.add_shape_text(shape)
            if name:
                named[name] = shape
            continue
        stroke = Stroke([], draw=command.group(1) == "draw")
        to_defaults: list[str] = []
        for option in options:
            apply_draw_option(stroke, option, to_defaults)
        stroke.operations = parse_path(rest, context, to_defaults=to_defaults)
        stroke.closed = bool(re.search(r"\brectangle\b", rest)) and len(stroke.operations) == 1
        drawing.add_stroke(stroke, typesetter)
    return drawing


def render(source: str, kind: str, typesetter: MathJaxTypesetter) -> str:
    """Render a ``tikz-cd`` or ``tikz`` diagram source to an SVG element."""
    if kind == "tikz-cd" or "\\begin{tikzcd}" in source:
        drawing = render_tikzcd(source, typesetter)
    elif kind == "tikz":
        drawing = render_tikz(source, typesetter)
    else:
        raise DiagramError(f"Unknown diagram kind {kind!r}")
    digest = hashlib.sha256(f"{RENDERER_VERSION}\0{kind}\0{source}".encode("utf-8")).hexdigest()[:10]
    return drawing.to_svg(f"kd{digest}-", source.strip())
