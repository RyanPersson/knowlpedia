const readline = require("readline");

const katex = require(process.env.KATEX_MODULE);

const rl = readline.createInterface({
  input: process.stdin,
  crlfDelay: Infinity,
});

rl.on("line", (line) => {
  try {
    const request = JSON.parse(line);
    const html = katex.renderToString(request.tex, {
      displayMode: Boolean(request.display),
      output: "htmlAndMathml",
      throwOnError: false,
      strict: "ignore",
      trust: false,
    });
    process.stdout.write(JSON.stringify({ html }) + "\n");
  } catch (error) {
    process.stdout.write(JSON.stringify({ error: String(error && error.message ? error.message : error) }) + "\n");
  }
});
