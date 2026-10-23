// Typesets diagram labels for diagrams.py: one JSON request per line in, one
// JSON reply per line out. Each reply gives the label's TeX box (in 1/1000 em,
// baseline at y = 0) and its glyphs as SVG, so Python can lay out a diagram
// around exact label sizes without running TeX.
const readline = require("readline");

const mathjax = require(process.env.MATHJAX_MODULE);

const ready = mathjax.init({
  loader: { load: ["input/tex", "output/svg"] },
  // Without noundefined, an unknown macro is an error instead of red text.
  tex: { packages: { "[-]": ["noundefined"] } },
  svg: { fontCache: "local" },
  startup: { typeset: false },
});

function typeset(MathJax, request) {
  const adaptor = MathJax.startup.adaptor;
  const container = MathJax.tex2svg(request.tex, { display: Boolean(request.display) });
  const markup = adaptor.outerHTML(container);
  const error = markup.match(/data-mjx-error="([^"]*)"/);
  if (error) return { error: error[1] };

  const svg = adaptor.firstChild(container);
  const [x, y, width, height] = adaptor.getAttribute(svg, "viewBox").split(/\s+/).map(Number);
  const glyphs = {};
  let body = "";
  for (const child of adaptor.childNodes(svg)) {
    if (adaptor.kind(child) === "defs") {
      for (const path of adaptor.childNodes(child)) {
        glyphs[adaptor.getAttribute(path, "id").replace(/^MJX-\d+-/, "")] = adaptor.getAttribute(path, "d");
      }
    } else {
      body += adaptor.outerHTML(child);
    }
  }
  body = body
    .replace(/xlink:href="#MJX-\d+-/g, 'href="#@')
    .replace(/ data-(?:mml-node|c|variant)="[^"]*"/g, "");
  return { x, width, height: -y, depth: height + y, glyphs, body };
}

const message = (error) => String(error && error.message ? error.message : error);
const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
let queue = Promise.resolve();
rl.on("line", (line) => {
  queue = queue
    .then(() => ready)
    .then(
      (MathJax) => {
        try {
          return typeset(MathJax, JSON.parse(line));
        } catch (error) {
          return { error: message(error) };
        }
      },
      (error) => ({ error: `MathJax failed to start: ${message(error)}` }),
    )
    .then((reply) => process.stdout.write(JSON.stringify(reply) + "\n"));
});
