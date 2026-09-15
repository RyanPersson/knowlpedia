# Ergodic theory and Koopman knowl collection

The `ergodic` branches now contain 119 new concept, construction, example, and
theorem knowls, plus eight reading-path indexes and the `ergodic-theory` subject
entry point. Thirteen existing subject indexes link the additions. Existing
definitions are reused through a prerequisite closure of 408 knowls.

The machine-readable inventory is [ergodic-knowl-coverage.json](ergodic-knowl-coverage.json).
It records every new ID and source hash, groups the reading paths, maps the
accessible conversations to entries, distinguishes supplementary theory, and
lists the reused prerequisite closure.

## Source coverage and limits

The requested sources are the conversations “Explain Noncommutative Ergodic
Theory” (`6aa8b0f9-2bec-83e8-bc01-223fdd770bf1`) and “Koopman representations”
(`6aa8d414-1adc-83e8-a6d4-33e9fe7f4a0a`). The finite, Gaussian, and number-field
exchanges were available in full. The initial noncommutative explanation and
the Koopman explanation were each truncated at 20,000 characters, and the
original image was unavailable. Coverage of those missing portions has not
been established. The unitary-conjugation example and multiple-recurrence
statement were completed independently from their visible beginnings.

The broader theorem layer adds disintegration and ergodic decomposition,
unique ergodicity, Krylov–Bogolyubov existence, Følner averages, Kingman,
Oseledets, dynamical entropy, the generator theorem, Shannon–McMillan–Breiman,
and DMD/EDMD. These additions support the request for major theorems and
applications without attributing unseen material to either conversation.

## Reading paths

| Index under `ergodic-theory/` | Coverage |
| --- | --- |
| `foundations-index` | Standard and atomless probability spaces; transformations, actions, invariant events, observables, time and space averages, factors, conjugacy, flows |
| `ergodic-theorems-index` | Mean, maximal, and pointwise ergodic theorems; recurrence; disintegration and decomposition; uniform averages and invariant-measure existence |
| `koopman-spectrum-index` | Forward operators and inverse-pullback representations; fixed vectors; spectral measures; mixing; discrete spectrum; Halmos–von Neumann; generators; spectral gaps, property T, and Howe–Moore |
| `examples-index` | Finite permutations and the three-point algebra; compact rotations, doubling, cat maps, Bernoulli shifts; linear and measurably conjugated Gaussian dynamics |
| `arithmetic-index` | Archimedean algebra, Minkowski embedding, trace pairing, codifferent, number-field torus, characters, single translation and joint ring action, Gaussian integers |
| `noncommutative-index` | States, fixed algebras, GNS dynamics, tracial averages, crossed products, freeness, factoriality, irrational orbit quotients, rotation algebra, derivations, foliations, matrix conjugation |
| `entropy-cocycles-index` | Partitions, entropy, generators, typical orbit names, subadditive and linear cocycles, Lyapunov exponents, Kingman and Oseledets |
| `applications-index` | Multiple recurrence and arithmetic progressions, Hamiltonian transport, finite-data Koopman approximations |

## Mathematical and editorial decisions

- Use one reusable concept per ordinary knowl, with its essential hypotheses
  and prerequisite links in the core. Space averages, the Minkowski embedding,
  and ergodic operator-algebra actions have separate canonical entries.
- Keep the inner product linear in the first argument. Use `U_T f = f ∘ T`
  for forward time averages and `κ(g)f = f ∘ T_(g⁻¹)` for a left group
  representation. Noninvertible pullback is an isometry, generally not unitary.
- Form the number-field torus from `K∞ / O_K`, with all Archimedean places.
  The codifferent indexes its characters. A single translation uses trace
  integrality; the joint additive `O_K` action has the integral-relation test.
- Require essential freeness in the crossed-product factor criterion. Use
  the regular group-coordinate construction, since multiplication and the
  Koopman operator on the original `L²` need not generate that crossed product.
- Distinguish finite tracial `L²` convergence from noncommutative pointwise
  convergence. Distinguish fixed continuous functions from measurable
  ergodicity, and Koopman equivalence from measurable conjugacy.
- Reuse `analysis/unique-ergodicity`, tightening its setting to compact metric
  spaces and linking the new uniform-averaging theorem.
- Preserve the repository's math delimiters and existing review history.
  No formal full-review counts have been added.

## Mathematical evidence

Elementary examples and Fourier criteria include direct calculations. Main
external sources have locators in each knowl's final References section:

- [Peterson's ergodic theory notes](https://math.vanderbilt.edu/peters10/teaching/Spring2011/ErgodicTheoryNotes.pdf):
  §1.6.1, §2.2 and Lemma 2.2.5, §2.5, and §2.6.
- [Jamneshan and Kreidler, ISEM 28](https://ajamnesh.github.io/pdf/ISem28_notes.pdf):
  §§5.1 and 6.1, Theorems 6.2.6–6.2.8, and the multiple-recurrence and
  correspondence results in Lectures 1 and 4.
- [Popa's group-action notes](https://www.math.ucla.edu/~popa/Books/OElectures.pdf):
  Theorem 4.1.1 and §4.3 for the regular crossed product, freeness, and MASAs.
- [Conrad, The Different Ideal](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf)
  and [Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
  trace-dual bases and the Archimedean lattice.
- [Connes, C*-algebras and differential geometry](https://arxiv.org/abs/hep-th/0101093):
  pp. 4–5 for the torus action, canonical derivations, and rapid-decay algebra.
- [Dajani's ergodic theory notes](https://www.staff.science.uu.nl/~kraai101/LectureNotesMM-2.pdf):
  Theorem 5.3.1, Exercise 5.3.2(c), and Theorem 5.4.2 for entropy generators
  and Shannon–McMillan–Breiman.
- [Filip's multiplicative ergodic theorem notes](https://math.uchicago.edu/~sfilip/public_files/MET_lectures.pdf):
  Theorem 2.2.6 and Variant 2.2.10 for the two-sided splitting.

These source checks support authorship; build success does not certify the
mathematics or complete the formal full-review queue.

## Validation and preview

Final validation results are recorded in `ergodic-knowl-coverage.json`:

- Exact development build: 5,330 knowls, passed.
- Exact production build: 4,142 knowls, passed; its complete rendering scan
  also passed, with rendered diagrams required.
- Prerequisite graph: 4,152 nodes and 13,847 edges, with no cycles, invalid
  sources, or missing targets.
- All 142 changed source files pass section-order preservation and external
  link placement; all inventory hashes match their files.
- All 128 new pages and core fragments load in the browser. Nine representative
  pages have rendered math; nested expansion, inline sections, and search pass.
  Three sampled mobile pages have no page overflow, and no JavaScript errors
  were observed.
- No new-entry rendering errors were found. The full development scan reports
  726 findings across 141 generated files, all belonging to the unchanged
  imported conjectures catalog or its entries in the combined index. That
  separate source working tree is clean.

The corpus-wide section audit also reports one unchanged failure in
`fiber-bundles/construction-splitting-of-atiyah-sequence-from-a-principal-connection`;
that failure is outside this collection.

The scope audit retains one assessed candidate: the C*-algebraic and von
Neumann formulations of a noncommutative probability space. These are variants
of the same probability-space concept. No exact-label mismatch was found in
the new entries.

The existing persistent service `devserver-knowlpedia-astra-benchmark.service`
serves this checkout's `public-imported` directory on port 8015. The entry point
is [Ergodic Theory](http://100.69.17.72:8015/ergodic-theory/).
The production build is a local validation artifact; no deployment is needed
to view the development preview.
