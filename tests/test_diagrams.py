from __future__ import annotations

import re
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "packages" / "compiler"))

import diagrams  # noqa: E402


class FakeTypesetter:
    """Boxes of predictable size: 0.5em per character, height 0.7em, no depth."""

    def __init__(self) -> None:
        self.requests: list[str] = []

    def box(self, tex: str, display: bool = False) -> diagrams.TexBox:
        self.requests.append(tex)
        return diagrams.TexBox(500.0 * len(tex), 700.0, 0.0, f'<g data-tex="{len(self.requests)}"/>', {})


def real_typesetter() -> diagrams.MathJaxTypesetter | None:
    node = shutil.which("node")
    module = ROOT / "node_modules" / "mathjax"
    if not node or not (module / "package.json").is_file():
        return None
    return diagrams.MathJaxTypesetter(Path(node), module)


SNAKE = r"""\begin{tikzcd}
0 \arrow[r] & \ker f' \arrow[r] \arrow[d] & \ker f \arrow[r] \arrow[d] & \ker f'' \arrow[d]
  \arrow[dddll, "\delta" description, rounded corners,
    to path={ -- ([xshift=2ex]\tikztostart.east)
      |- ($(\tikztostart)!0.5!(\tikztotarget)$) [near end]\tikztonodes
      -| ([xshift=-2ex]\tikztotarget.west)
      -- (\tikztotarget)}] & \\
0 \arrow[r] & A' \arrow[r, "i"] \arrow[d, "f'" near start] & A \arrow[r, "p"] \arrow[d, "f" near start] & A'' \arrow[r] \arrow[d, "f''" near start] & 0 \\[1.2em]
0 \arrow[r] & B' \arrow[r, "j"] \arrow[d] & B \arrow[r, "q"] \arrow[d] & B'' \arrow[r] \arrow[d] & 0 \\
& \operatorname{coker} f' \arrow[r] & \operatorname{coker} f \arrow[r] & \operatorname{coker} f'' \arrow[r] & 0
\end{tikzcd}"""


class ParseTests(unittest.TestCase):
    def test_cells_arrows_and_extra_row_space(self) -> None:
        options, rows, arrows, extra = diagrams.parse_tikzcd(
            "\\begin{tikzcd}[column sep=large]\nA \\arrow[r, \"{f,g}\"'] & B \\\\[1em]\n& C\n\\end{tikzcd}"
        )
        self.assertEqual(options, ["column sep=large"])
        self.assertEqual(rows, [["A", "B"], ["", "C"]])
        self.assertEqual([(a.row, a.column, a.options) for a in arrows], [(0, 0, ["r", '"{f,g}"\''])])
        self.assertAlmostEqual(extra[0], diagrams.EM)

    def test_braces_protect_ampersands_and_nested_option_brackets(self) -> None:
        _, rows, arrows, _ = diagrams.parse_tikzcd(r"\text{a & b} \arrow[r, to path={-- ([xshift=2ex]\tikztotarget)}] & B")
        self.assertEqual(rows, [[r"\text{a & b}", "B"]])
        self.assertEqual(arrows[0].options, ["r", r"to path={-- ([xshift=2ex]\tikztotarget)}"])

    def test_label_forms(self) -> None:
        label = diagrams.parse_cd_label('"f\'"\' near start')
        self.assertEqual((label.text, label.swap, label.pos), ("f'", True, 0.25))
        label = diagrams.parse_cd_label('"{[T]_{\\mathcal B}}" description')
        self.assertEqual(label.text, r"[T]_{\mathcal B}")
        self.assertTrue(label.description)
        label = diagrams.parse_cd_label('""{coordinate, name=Z}')
        self.assertTrue(label.coordinate)
        self.assertEqual(label.name, "Z")

    def test_unsupported_syntax_names_the_construct(self) -> None:
        typesetter = FakeTypesetter()
        with self.assertRaisesRegex(diagrams.DiagramError, "squiggly"):
            diagrams.render(r"A \arrow[r, squiggly] & B", "tikz-cd", typesetter)
        with self.assertRaisesRegex(diagrams.DiagramError, r"\\arrow\[r"):
            diagrams.render(r"A \arrow{r}{f} & B", "tikz-cd", typesetter)
        with self.assertRaisesRegex(diagrams.DiagramError, "outside the diagram"):
            diagrams.render(r"A \arrow[rr] & B", "tikz-cd", typesetter)
        with self.assertRaisesRegex(diagrams.DiagramError, "shade"):
            diagrams.render(r"\node (A) at (0,0) {$A$}; \shade (A) -- (1,1);", "tikz", typesetter)


class GeometryTests(unittest.TestCase):
    def cells(self) -> tuple[diagrams.Shape, diagrams.Shape]:
        box = diagrams.TexBox(700.0, 683.0, 0.0)
        a = diagrams.Shape("cell", 0.0, 0.0, box, diagrams.CD_CELL_XSEP, diagrams.CD_CELL_YSEP)
        b = diagrams.Shape("cell", 4000.0, 0.0, box, diagrams.CD_CELL_XSEP, diagrams.CD_CELL_YSEP)
        return a, b

    def test_arrows_run_between_cell_borders_on_the_math_axis(self) -> None:
        a, b = self.cells()
        spec = diagrams.cd_arrow_spec(diagrams.CdArrow(0, 0, ["r"]))
        segment = diagrams.route_between(a, b, spec)
        self.assertAlmostEqual(segment.start[0], a.x + a.half_width)
        self.assertAlmostEqual(segment.end[0], b.x - b.half_width)
        self.assertAlmostEqual(segment.start[1], diagrams.AXIS)
        self.assertAlmostEqual(segment.end[1], diagrams.AXIS)

    def test_shift_left_moves_to_the_left_of_the_direction(self) -> None:
        a, b = self.cells()
        spec = diagrams.cd_arrow_spec(diagrams.CdArrow(0, 0, ["r", "shift left"]))
        segment = diagrams.route_between(a, b, spec)
        self.assertAlmostEqual(segment.start[1], diagrams.AXIS + diagrams.CD_SHIFT)

    def test_bend_left_curves_to_the_left(self) -> None:
        a, b = self.cells()
        spec = diagrams.cd_arrow_spec(diagrams.CdArrow(0, 0, ["r", "bend left=40"]))
        segment = diagrams.route_between(a, b, spec)
        self.assertEqual(segment.kind, "curve")
        self.assertGreater(segment.at(0.5)[1], diagrams.AXIS + 500)

    def test_auto_labels_sit_left_of_the_arrow_and_swap_to_the_right(self) -> None:
        self.assertEqual(diagrams.auto_anchor((1, 0), False), "south")  # label above a right arrow
        self.assertEqual(diagrams.auto_anchor((0, -1), False), "west")  # label right of a down arrow
        self.assertEqual(diagrams.auto_anchor((0, -1), True), "east")
        self.assertEqual(diagrams.auto_anchor((1, -1), False), "south west")
        self.assertEqual(diagrams.auto_anchor((-1, 0), True), "south")

    def test_rows_and_columns_follow_tikz_cd_separations(self) -> None:
        typesetter = FakeTypesetter()
        drawing = diagrams.render_tikzcd(r"A \arrow[r] \arrow[d] & B \\ C", typesetter)
        # Two cells of one character: column centres 0.5em + 2*1ex apart plus 2.4em of column sep.
        translations = [tuple(map(float, m)) for m in re.findall(r"translate\(([-\d.]+),([-\d.]+)\)", "".join(drawing.items))]
        a, b, c = translations[:3]
        expected_gap = 500 + 2 * (diagrams.CD_CELL_XSEP + diagrams.OUTER_SEP) + diagrams.CD_COLUMN_SEP["normal"]
        self.assertAlmostEqual(b[0] - a[0], expected_gap, delta=0.2)
        expected_drop = 700 + 2 * (diagrams.CD_CELL_YSEP + diagrams.OUTER_SEP) + diagrams.CD_ROW_SEP["normal"]
        self.assertAlmostEqual(c[1] - a[1], expected_drop, delta=0.2)


class OutputTests(unittest.TestCase):
    def test_svg_uses_current_color_and_no_raster_images(self) -> None:
        svg = diagrams.render(r'A \arrow[r, "f", two heads] \arrow[d, hook, dashed] & B \\ C', "tikz-cd", FakeTypesetter())
        self.assertTrue(svg.startswith("<svg "))
        self.assertIn('stroke="currentColor"', svg)
        self.assertIn('stroke-dasharray="280 160"', svg)
        self.assertNotIn("<img", svg)
        self.assertRegex(svg, r'viewBox="[-\d.]+ [-\d.]+ [\d.]+ [\d.]+"')

    def test_description_labels_and_double_lines_paint_the_background(self) -> None:
        svg = diagrams.render(r'A \arrow[r, "x" description] \arrow[d, equal] & B \\ C', "tikz-cd", FakeTypesetter())
        self.assertIn('<rect ', svg)
        self.assertEqual(svg.count("var(--diagram-knockout,#fff)"), 2)

    def test_snake_lemma_connecting_arrow(self) -> None:
        typesetter = FakeTypesetter()
        svg = diagrams.render(SNAKE, "tikz-cd", typesetter)
        self.assertIn("{\\scriptstyle \\delta}", typesetter.requests)
        self.assertIn("<rect ", svg)  # the δ label is a description label

    def test_tikz_subset(self) -> None:
        source = r"""
\node (A) at (0,0) {$A$};
\node (B) at (3,0) {$B$};
\node[align=center] at (1.5,-1) {left\\square};
\draw[-{Stealth[length=3mm]}, thick] (A) -- node[above] {$f$} (B);
\draw[-{Stealth[length=3mm]}, bend left=20] (B) to node[below] {$g$} (A);
\draw[dashed, rounded corners] (-0.5,0.5) rectangle (3.5,-1.5);
"""
        typesetter = FakeTypesetter()
        svg = diagrams.render(source, "tikz", typesetter)
        self.assertIn(r"\text{left}", typesetter.requests)
        self.assertIn('fill="currentColor"', svg)  # Stealth tips are filled
        self.assertIn(" C", svg)


class MathJaxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.typesetter = real_typesetter()
        if cls.typesetter is None:
            raise unittest.SkipTest("node or the mathjax package is not installed")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.typesetter.close()

    def test_labels_have_exact_boxes_and_shared_glyphs(self) -> None:
        box = self.typesetter.box("M_i")
        self.assertGreater(box.width, 1000)
        self.assertAlmostEqual(box.height, 683, delta=1)
        self.assertGreater(box.depth, 100)
        svg = diagrams.render(r'M \arrow[r, "f"] & M', "tikz-cd", self.typesetter)
        ids = re.findall(r'<path id="([^"]+)"', svg)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(i.startswith("kd") for i in ids))
        self.assertEqual(len(re.findall(r'href="#[^"]+TEX-I-1D440"', svg)), 2)

    def test_tex_errors_are_reported(self) -> None:
        with self.assertRaisesRegex(diagrams.DiagramError, r"Undefined control sequence \\nosuchmacro"):
            diagrams.render(r"\nosuchmacro \arrow[r] & B", "tikz-cd", self.typesetter)


if __name__ == "__main__":
    unittest.main()
