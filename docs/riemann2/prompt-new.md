You are one of about forty authors who together translate a very large Lean 4 proof into a human-readable mathematical proof written as "knowls" (small linked textbook-style pages) for the Knowlpedia. No one will compile anything; the Lean is read as text only.

FIRST read, completely:
1. /home/codex/code/knowlpedia-root/documents/riemann2/GUIDE.md  (the project rules, formats, placeholder conventions — binding)
2. /home/codex/code/knowlpedia-root/documents/grh-lean/grh/GUIDE.md  (reading guide, glossary and notation of the Lean proof)
3. Look at three or four existing knowls to absorb the house style, e.g. knowlpedia-content/content/algebra-groups/group.knowl.md, knowlpedia-content/content/algebra-fields-galois/place-of-global-field.knowl.md, knowlpedia-content/content/algebra-fields-galois/galois-group.knowl.md.

YOUR AREA: `{AREA}`
YOUR LEAN FILES (relative to /home/codex/code/knowlpedia-root/documents/grh-lean/grh/src/): {FILES}
(`documents/grh-lean/grh/CONTENTS.md` lists every file with its title; `INDEX.md` lists main results. If your assignment says "first half/second half in import order", list the folder's files, order them by their imports, and take that half; the other half belongs to a sibling author.)

These files are part of the argument itself (folder `New`). Read every assigned file completely, including the proofs and the long comment at the head of each file, which usually explains the mathematics.

PRODUCE, writing to disk as you go (file by file, in import order, so that nothing is lost if you run out of budget):

(1) Proof knowls in `/home/codex/code/knowlpedia-root/knowlpedia-content/content/proofs/grh/{AREA}/<slug>.knowl.md`, one per definition/construction and per result that matters: each file's main results, everything that other files use, and the key intermediate lemmas that carry real mathematical content. Give each a faithful, complete statement and a human-readable `## Proof`. Aim for `proof_status = "full"` on the main results wherever you can genuinely follow the Lean proof; otherwise `"outline"`, saying exactly which steps are only asserted and which Lean declaration proves them. Do not pad and do not guess.

(2) The area page `/home/codex/code/knowlpedia-root/knowlpedia-content/content/proofs/grh/{AREA}.knowl.md`: a readable chapter for your area.

(3) The concept sidecar `/home/codex/code/knowlpedia-root/documents/riemann2/concepts/{AREA}.tsv`: every standard concept / known theorem you used (including Mathlib-level ones such as "Dirichlet character", "von Mangoldt function", "Haar measure"), with the precise definition as used. This list drives the creation of the missing definition knowls, so be thorough and include missing prerequisites of prerequisites.

(4) The coverage report `/home/codex/code/knowlpedia-root/documents/riemann2/reports/{AREA}.md`.

Objects defined in other areas: link with `[[?lean:Fully.Qualified.Name|text]]`. You may open other Lean files to read the definition of something you depend on (grep for `def NAME`/`structure NAME`), but write knowls only for declarations in your own files.

When done (or when you must stop), make sure the area page and the report reflect the true state, then reply with a short summary: counts of knowls by kind and by proof_status, files not fully covered, and your most important doubts.
