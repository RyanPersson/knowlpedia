You are one of about forty authors who together translate a very large Lean 4 proof into a human-readable mathematical proof written as "knowls" (small linked textbook-style pages) for the Knowlpedia. No one will compile anything; the Lean is read as text only.

FIRST read, completely:
1. /home/codex/code/knowlpedia-root/documents/riemann2/GUIDE.md  (the project rules, formats, placeholder conventions — binding)
2. /home/codex/code/knowlpedia-root/documents/grh-lean/grh/GUIDE.md  (reading guide, glossary and notation of the Lean proof)
3. Look at three or four existing knowls to absorb the house style, e.g. knowlpedia-content/content/algebra-groups/group.knowl.md, knowlpedia-content/content/algebra-fields-galois/place-of-global-field.knowl.md, knowlpedia-content/content/algebra-fields-galois/galois-group.knowl.md.

YOUR AREA: `{AREA}`
YOUR LEAN FILES (relative to /home/codex/code/knowlpedia-root/documents/grh-lean/grh/src/): {FILES}
(`documents/grh-lean/grh/CONTENTS.md` lists every file with its title; `INDEX.md` lists the main results and the literature sources the authors give; `REFERENCES.md` the citations.)

These files are background (folder `Lib`): results classed as known in the literature that Mathlib lacks, proved in Lean, often in a weaker form that suffices for this proof and with the development's own definitions. In the human proof they play the role of the cited background theory, stated in exactly the form that is used.

For every assigned file: read the head comment, every `def`/`structure`/`class`/`abbrev` that later statements depend on, and the statements of the main results (those named in the file head, in INDEX.md, or used from other folders) carefully; read or skim the proofs enough to describe the strategy truthfully.

PRODUCE, writing to disk as you go (file by file, so that nothing is lost if you run out of budget):

(1) Proof knowls in `/home/codex/code/knowlpedia-root/knowlpedia-content/content/proofs/grh/{AREA}/<slug>.knowl.md`:
   - one per definition/construction of the development that other statements rely on, with the real mathematical definition (data and axioms) as the Lean gives it; if it coincides with a standard textbook concept, say so and link that concept as a `?c:` placeholder; if it deviates (weaker, differently normalised, a special case), say exactly how;
   - one per main result, stating exactly the form proved here with all hypotheses, and how it compares with the standard theorem (linked as a `?c:` placeholder and recorded in your sidecar with kind `theorem`). `## Proof`: the strategy in a few paragraphs, true to the Lean proof (`proof_status = "outline"`), or `proof_status = "cited"` with the literature source the file head gives in `## References` when you only state it. Use `"full"` only for proofs you actually wrote out completely and checked against the Lean.

(2) The area page `/home/codex/code/knowlpedia-root/knowlpedia-content/content/proofs/grh/{AREA}.knowl.md`: a readable chapter saying what background theory this area supplies, in what form, and how the pieces depend on each other.

(3) The concept sidecar `/home/codex/code/knowlpedia-root/documents/riemann2/concepts/{AREA}.tsv`: every standard concept / known theorem involved (including Mathlib-level ones), with the precise definition or statement. This list drives the creation of the missing definition knowls in the subject folders, so be thorough: include the standard concepts your definitions are built from and the missing prerequisites of prerequisites, down to things the corpus already has.

(4) The coverage report `/home/codex/code/knowlpedia-root/documents/riemann2/reports/{AREA}.md`.

Objects defined in other areas: link with `[[?lean:Fully.Qualified.Name|text]]`. You may open other Lean files to read a definition you depend on, but write knowls only for declarations in your own files.

When done (or when you must stop), make sure the area page and the report reflect the true state, then reply with a short summary: counts of knowls by kind and by proof_status, files not fully covered, and your most important doubts.
