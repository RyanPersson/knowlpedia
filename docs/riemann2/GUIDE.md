# riemann2 project guide (read fully before writing anything)

## What the user asked for (their words)

> What I'm wanting is to create another (likely very large) batch of knowls to add to the knowlpedia, containing knowl definitions of any dependency concepts that aren't yet knowlified. They should match the existing format of knowls in the knowlpedia (minimal axiomatic definitions, with recursively unfoldable dependency knowls)
>
> I guess first step would be to go through the grh-lean proof and make a list of mathematical definitions that are used, then cross check that against the existing corpus of knowls to see what we already have and whats missing, then create the missing knowls, creating any subject folders that need to be added. Then audit those knowls for unlinked or missing dependency concepts. Once that's done, I want you to translate the lean proof into a complete, correct, human readable latex proof in the knowlpedia format, with all definitions/concepts clickable as in individual knowls.
>
> Goal is to translate the non-human readable lean proof into a complete, correct, human readable latex proof in knowlpedia format such that readers can use the knowl mechanism as intended to fully unroll definitions to either the raw underlying axiomatic definitions, or concepts they are familiar with, whichever comes first.
>
> (ignore the module learning path when you're getting an idea of the format that knowls use, that's not a widely used format)
>
> Maintain mathematical rigor and correctness in all knowls as well as the proof. (You can make a new section paralell to subjects and learning paths, call it proofs, we'll eventually add many others.) the complete proof should go in that proofs section, but the individual knowl definitions it imports should go in their respective subjects. You'll likely need to add missing subjects as well, the knowlpedia is far from complete.
>
> Note that knowls are *NOT* lean code. More like definitions in a textbook. Also don't try and compile the lean, we're just using it as a source, it's far too large of a proof to try and compile on this machine.

## Ground rules

- Work only inside `/home/codex/code/knowlpedia-root`. Do not open, list or search any other project under `~/code`. Do not borrow style or conventions from anywhere outside this folder. If you brief a subagent, pass these rules on and quote the user's own words above rather than a paraphrase.
- Never run `lake`, `lean`, or any build of the Lean code. Read it as text only.
- Do not run git commands that change state (no commit, checkout, stash, reset). The orchestrator commits.
- Do not edit existing knowls outside your assignment. Do not edit files other agents own.
- Knowls are textbook mathematics, not Lean. No Lean syntax in the body of a knowl. Lean names appear only in front matter and in the final `## References` section.
- Rigor first. Never invent a step, a hypothesis, a constant, or a citation. If you cannot follow a Lean proof well enough to write a correct human proof, write what you can verify and mark the status honestly (see `proof_status`). An honest "outline" is far better than a plausible-sounding wrong "full" proof.
- The Lean source is the authority for what is proved here. Where a Lean definition or theorem differs from the textbook one (weaker form, different normalization, extra hypotheses), say so precisely.

## Paths

| What | Where |
|---|---|
| Lean source (readable edition) | `documents/grh-lean/grh/src/` (docs: `documents/grh-lean/grh/{GUIDE,INDEX,CONTENTS,REFERENCES}.md`) |
| Knowl corpus | `knowlpedia-content/content/<subject>/<slug>.knowl.md` |
| Index of existing knowls (id, title, kind, aliases, summary) | `documents/riemann2/corpus-index.tsv` (grep this; ~4900 rows) |
| Editorial rules | `knowlpedia-content/EDITORIAL.md` |
| Proof knowls for this project | `knowlpedia-content/content/proofs/grh/...` |
| Concept sidecars | `documents/riemann2/concepts/<area>.tsv` |
| Coverage reports | `documents/riemann2/reports/<area>.md` |

Read `documents/grh-lean/grh/GUIDE.md` (reading order, glossary, letters, sizes, conventions) before reading Lean files. Use its letters and words as the common notation of the human proof, so that the chapters written by different authors agree: \(q_0, q_1, q_2\), \(d\), \(K=\mathbb{Q}(\sqrt{-d})\), \(E=K(\zeta)\), \(X_j, Y_j, V_j, W_j\), \(m, r, k, t, a, b, x, x_1, M, N\), etc.

## Knowl file format

Every knowl is one file `<slug>.knowl.md`: TOML front matter between `+++` lines, then Markdown with LaTeX.

```markdown
+++
id = "algebra-fields-galois/place-of-global-field"
title = "Place of a global field"
kind = "definition"
summary = "An equivalence class of nontrivial absolute values on a global field."
aliases = ["place", "places", "place of a number field"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/global-local-fields-completions"]
+++

Let \(F\) be a [[algebra-fields-galois/global-local-fields-completions|global field]]. A
**place of \(F\)** is an equivalence class of nontrivial absolute values on \(F\), where two
absolute values are equivalent when they induce the same topology on \(F\).

## Archimedean and nonarchimedean places

...

## References

1. Jürgen Neukirch, *Algebraic Number Theory*, Springer, 1999, Chapter II, §§4--5.
```

Rules:

- `id` = path under `content/` without `.knowl.md`. Lowercase, hyphens, ASCII.
- `kind`: `definition`, `theorem`, `lemma`, `proposition`, `construction`, `notation`, `example`; container kinds `page`, `section`, `index`.
- TOML strings: a backslash must be doubled inside `"..."`. Prefer titles and summaries without LaTeX; if you need a backslash use a TOML literal string `'...'`.
- Math delimiters: inline `\( ... \)`, display `\[ ... \]`. Never `$...$`. KaTeX-compatible LaTeX only (no `\newcommand`, no `\label`/`\ref`, no exotic packages; `\begin{aligned}`, `\begin{cases}`, `\begin{pmatrix}` are fine; `\operatorname{...}` for named operators).
- Knowl link: `[[subject/slug|display text]]`. The display text must not contain `|` or `]]` (inside math write `\lvert`, `\mid`, `\Vert`).
- **Core** = everything before the first `## ` heading. It is what opens inline when a reader clicks a link, so it must be the *smallest sufficient statement*: name the definiendum (bold) immediately, give all data and all axioms/hypotheses, link every genuine prerequisite concept on first use, and stand alone. No history, no motivation, no examples in the core. Keep defining axioms in the core — do not replace an axiomatic definition by a slick characterisation that presumes other machinery.
- "Minimal axiomatic definitions, with recursively unfoldable dependency knowls": a definition is stated in terms of the *immediately* lower-level concepts, each linked, so a reader can keep unfolding until they reach either raw axioms or something they know. Do not inline the definition of a prerequisite; link it.
- One knowl owns one concept (definition, theorem, construction). Do not bundle several independently reusable concepts into one page.
- Optional sections after the core, with `## ` headings: `## Examples`, `## Equivalent characterizations`, `## Properties`, `## Remarks`, `## Proof`, and last `## References`. Bibliographic sources go only in `## References`, with exact locators you are confident of. Never fabricate a locator; give a chapter-level locator or omit rather than guess.
- `prerequisites`: IDs of the concepts needed to read the core (normally exactly the knowl links in the core that are genuine dependencies). Must be acyclic. In drafts that still contain placeholder links, leave `prerequisites = []`; a later pass fills it.
- Link a technical term at its first useful occurrence in a block; do not saturate.

## Placeholder links (used while the missing knowls do not exist yet)

When you need to link a concept:

1. `grep -i` the corpus index for it (title and aliases). Open the candidate knowl file and check it really defines the concept you mean. If so, link it by its real ID: `[[algebra-groups/group|group]]`.
2. Otherwise, if it is a **standard mathematical concept or known theorem** (anything a textbook or the literature defines: Dirichlet character, adele ring, hermitian space, Selmer group, Breuil–Kisin module, …) write a concept placeholder:
   `[[?c:Dirichlet character|Dirichlet characters]]`
   The part after `?c:` is the canonical singular English name of the concept. Use the same canonical name every time. Record the concept in your sidecar TSV (below).
3. If it is a **definition or result of this proof** (a declaration of the Lean development that is not a standard textbook concept) written by you in this assignment, link its real `proofs/grh/...` ID. If it belongs to another author's area, write a Lean placeholder with the fully qualified Lean name:
   `[[?lean:New.Data.enough_forms|Theorem B]]`
   (the resolver matches on the Lean name recorded in the target's front matter).

Placeholders are resolved mechanically later, so spell them consistently and never leave an unlinked technical term that a reader might not know.

## Concept sidecar (`documents/riemann2/concepts/<area>.tsv`)

One line per standard concept or known theorem that your text uses (whether it already exists in the corpus or not), tab-separated, no header:

```
canonical name <TAB> kind (definition/theorem/construction/notation) <TAB> existing corpus id or NEW <TAB> suggested subject (e.g. analytic-number-theory, algebraic-number-theory, automorphic-forms, galois-representations, p-adic-hodge-theory, or an existing subject id) <TAB> precise definition/statement in one to three sentences, with the conventions the Lean source uses <TAB> its direct prerequisite concepts (canonical names, `; `-separated) <TAB> Lean/Mathlib names
```

Include the prerequisites' prerequisites as their own lines when they are missing from the corpus too (e.g. if you use "Hecke character" and the corpus lacks "idele class group", add both). The goal is that every concept can be unrolled down to things the corpus already has.

## Proof knowls (`knowlpedia-content/content/proofs/grh/<area>/<slug>.knowl.md`)

The human-readable proof is a tree of knowls. Each **definition, construction, lemma, proposition, or theorem of the proof** that matters is its own knowl; proofs cite other items by link, so a reader can unroll the argument.

```markdown
+++
id = "proofs/grh/<area>/<slug>"
title = "Plain-language title"
kind = "theorem"
summary = "One sentence."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.enough_forms"]
lean_files = ["src/New/Reduction/ShortAndEnough.lean"]
proof_status = "full"
+++

**Theorem (enough forms).** Let ... (complete statement, all hypotheses, all objects linked).

## Proof

...

## References

1. Lean: `New.Data.enough_forms` in `src/New/Reduction/ShortAndEnough.lean`.
2. (literature source, if the Lean file head cites one for this statement)
```

- `lean`: fully qualified names of the Lean declarations this knowl translates (several if it merges a definition with its basic lemmas). Fully qualified means including namespaces, e.g. `New.Data.enough_forms`, `New.TwistedLattice.covolume_add_index_nonneg`.
- `proof_status` (for lemma/proposition/theorem kinds):
  - `"full"`: the proof section is a complete human-readable proof at the level of a careful research paper; every step is justified by an explicit computation, a linked item of this proof, or a linked standard theorem; and you checked it against the Lean proof.
  - `"outline"`: the proof section gives the true structure and the key steps, but some steps are only asserted with a pointer to the Lean declaration that proves them. Say which.
  - `"cited"`: a known result from the literature; no proof reproduced; the source is in References. State exactly the form used here.
  - `"statement"`: statement translated; proof not examined.
- A definition's core must give the actual mathematical definition (data + axioms), not "the object defined in Lean as ...".
- Translate Lean statements faithfully: every hypothesis and every quantifier. Explain typeclass/instance assumptions as explicit hypotheses ("Let \(E\) be a CM field containing a primitive 5040-th root of unity …"). Junk values and totalised functions in Lean (division by zero = 0, `Classical.choose`) should be expressed as ordinary mathematical conventions, noted when they matter.
- Routine helper lemmas (simp lemmas, coercion lemmas, small algebraic identities) are folded into the proofs that use them; they do not get knowls.
- Each area also gets a page `knowlpedia-content/content/proofs/grh/<area>.knowl.md` (`id = "proofs/grh/<area>"`, `kind = "page"`, `section_mode = "continuous"`, `domains = ["proofs"]`): a readable chapter that states what the area proves, fixes notation, and walks through the items in logical order, linking each, with the connecting narrative of the argument. It imports from other areas only by links.

## Coverage report (`documents/riemann2/reports/<area>.md`)

List every Lean file you were assigned with: lines, how deeply you read it (full / statements + skim / head only), the knowls created from it, and any doubts, gaps, or places where the Lean statement surprised you. Be candid; the orchestrator uses this to tell the user what is and is not done.

## Addenda (from the first finished areas)

- Never write a literal `[[` or `]]` in mathematics: it collides with the knowl link syntax. Write formal power series rings as `R[\![X]\!]` and Laurent series as `R(\!(X)\!)`.
- Do not write "setting" knowls that restate notation owned by another area; link that area's declarations with `?lean:` placeholders.
- Do not spawn subagents. One author per area, working alone and economically.
- Keep helper scripts in a private subfolder of the scratchpad named after your area; the scratchpad is shared.
