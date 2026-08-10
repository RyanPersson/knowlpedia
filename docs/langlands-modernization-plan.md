# Langlands corpus modernization plan

This document is the bounded planning and review manifest for modernizing the
Langlands corpus. It treats the knowls derived from Robert Langlands' 1967
letter as a historically valuable reading collection while building the
separate, reusable vocabulary needed for the modern Langlands program.

The campaign follows `docs/july-26-retrospective.md` and the editorial model in
`knowlpedia-content/EDITORIAL.md`: concise self-contained cores, progressive
documentation, explicit convention boundaries, primary or standard literature
in final reference sections, semantic deduplication, and rendered validation.

## Branch and baseline

- `knowlpedia`: `modernize-langlands-corpus`, based on `develop` at `98fce51`.
- `knowlpedia-content`: `modernize-langlands-corpus`, based on `develop` at
  `ae80174`.
- Production content is under `knowlpedia-content/content`.
- Existing IDs must remain valid. The content model does not yet provide a
  general redirect mechanism.

## Why this collection is flagged

The source is foundational but historical. Its vocabulary predates the modern
formulation of local Langlands packets and their refinements, Arthur
parameters, stabilized trace formulas, the function-field construction by
multiple-leg shtukas and excursion operators, categorical geometric
Langlands, and the Fargues--Scholze geometrization of local Langlands.

The current Letter collection contains 33 dedicated knowls. A July 30 legacy
audit repaired seven of them, but that was not a collection-wide specialist
review or a historical-to-modern migration. The separate geometric Langlands
collection contains 32 knowls and must be reused rather than duplicated.

## Review statuses

- **FLAGGED**: in the campaign but not yet source-mapped individually.
- **VERIFY**: retain the existing concept and ID; check the statement and
  conventions against modern literature.
- **REFINE**: preserve the ID and core subject while improving precision,
  links, scope, or progressive documentation.
- **SPLIT**: preserve the source-derived ID, but move independently reusable
  concepts into canonical atomic knowls and turn the old page into a coherent
  bridge.
- **NEW**: create a missing canonical knowl after semantic deduplication.
- **LINK**: existing coverage is adequate; integrate it into the modern map.
- **TECHNICAL REVIEW**: automated and editorial checks are complete, but the
  record remains a good candidate for review by a subject-matter expert.
- **COMPLETE**: source mapping, editing, links, validation, and review evidence
  are recorded.

## Editorial and mathematical boundaries

1. Historical formulations belong in a `History` or `Relation to the letter`
   section, not in place of the modern canonical definition.
2. Definitions, theorems, conjectures, conditional results, and expected
   compatibilities must be labeled distinctly.
3. Local and global statements must not be blended. Number-field and
   function-field results must state their base fields.
4. Basic and refined local Langlands statements must be separated. Packet
   internal parametrizations require choices such as Whittaker data and, for
   inner forms, an appropriate rigidifying framework.
5. Arithmetic versus geometric Frobenius, normalized versus unnormalized
   induction, and (C)-algebraic versus (L)-algebraic conventions must be
   explicit wherever they affect formulas.
6. Fargues--Scholze parameter maps must not be advertised as an unconditional
   full refined local Langlands correspondence for all groups.
7. Existing geometric-Langlands knowls should be audited against the current
   theorem formulations rather than recreated under competing IDs.

## Existing Langlands Letter review manifest

The action column records the initial editorial classification. All 33 rows
were subsequently source-compared, rewritten in place, interlinked, and
validated. The completion record below distinguishes finished editorial work
from the smaller set of pages for which specialist review would still be
valuable.

| Existing ID suffix | Action | Principal concern |
|---|---|---|
| `adeles-restricted-product` | VERIFY | Restricted-product topology and measure conventions. |
| `automorphic-form-hecke-eigen` | SPLIT | Separate automorphic forms, automorphic representations, and spherical eigenvectors. |
| `borel-mostow-semisimple-normalizer` | VERIFY | Exact hypotheses and attribution. |
| `characters-separate-semisimple-classes` | VERIFY | Group, field, and representation-ring hypotheses. |
| `chevalley-basis` | VERIFY | Integral signs and pinning conventions. |
| `chevalley-lattice-integral-model` | REFINE | Separate lattice, group scheme, and integral model. |
| `contragredient-representation` | REFINE | Smooth dual versus Hilbert-space contragredient. |
| `coroots-and-pairing` | VERIFY | Root-datum conventions. |
| `dual-lattice` | VERIFY | Lattice dual versus character/cocharacter duality. |
| `eisenstein-series` | REFINE | Induced data, convergence, continuation, and spectral role. |
| `embeddings-qbar-to-q_p` | VERIFY | Places above (p) and dependence on choices. |
| `euler-product-and-local-factor` | SPLIT | Canonical local factors require Weil--Deligne and ramification data. |
| `frobenius-unramified` | REFINE | Arithmetic/geometric Frobenius convention. |
| `galois-descent-forms` | VERIFY | Forms, inner forms, and pure/rigid inner twists. |
| `galois-extension-and-group` | VERIFY | Mostly stable prerequisite. |
| `global-local-fields-completions` | REFINE | Separate number and function fields and their places. |
| `group-algebra-of-lattice` | VERIFY | Coefficient ring and invariant-subring hypotheses. |
| `ideles-artin-reciprocity-hecke-character` | SPLIT | Three reusable concepts and reciprocity normalization are bundled. |
| `l-group-satake-parameter` | SPLIT | Separate the \(L\)-group, unramified parameter, and Satake class. |
| `langlands-dual-group` | REFINE | Based root datum and coefficient-field forms. |
| `langlands-functoriality-l-homomorphism` | REFINE | Parameter-level formulation and known/conjectural transfer boundaries. |
| `maximal-compact-hyperspecial` | SPLIT | Real maximal compact and nonarchimedean hyperspecial notions differ. |
| `maximal-torus-weight-lattice` | REFINE | Character and cocharacter lattices should be explicit. |
| `nonabelian-h1-galois-cohomology` | VERIFY | Pointed-set and twisting conventions. |
| `p-adic-field` | VERIFY | Stable prerequisite. |
| `pinned-automorphisms` | VERIFY | Pinning and Galois action. |
| `root-vs-weight-lattice-isogeny` | VERIFY | Isogeny and simply connected/adjoint forms. |
| `roots-weights-weyl` | REFINE | Based root data and highest-weight hypotheses. |
| `semisimple-element-and-class` | VERIFY | Rational versus geometric conjugacy. |
| `simply-connected-semisimple-group` | VERIFY | Algebraic-group, not topological, simply connectedness. |
| `spherical-hecke-algebra-satake` | REFINE | Normalized Satake isomorphism and dual-group interpretation. |
| `split-reductive-group` | VERIFY | Split maximal torus and base-field hypotheses. |
| `unramified-extension-local` | VERIFY | Frobenius and residue-field conventions. |

## Accepted new coverage: ordinary local Langlands

| Status | Canonical ID | Kind | Purpose |
|---|---|---|---|
| NEW | `langlands/l-group` | definition | Canonical atomic \(L\)-group separated from the Letter's bundled page. |
| NEW | `langlands/satake-parameter` | definition | Normalized unramified conjugacy class separated from the \(L\)-group. |
| NEW | `langlands/weil-group` | definition | Local and global Weil groups, with scope separated. |
| NEW | `langlands/weil-deligne-group` | definition | Group-scheme and pair presentations, with convention warning. |
| NEW | `langlands/weil-deligne-representation` | definition | Frobenius-semisimple pairs ((r,N)). |
| NEW | `harmonic-analysis/smooth-representation-totally-disconnected-group` | definition | Smooth complex representations of locally profinite groups. |
| NEW | `harmonic-analysis/admissible-representation-p-adic-group` | definition | Finite-dimensional compact-open fixed spaces. |
| NEW | `harmonic-analysis/supercuspidal-representation` | definition | Irreducible admissible representations absent from proper parabolic induction. |
| NEW | `harmonic-analysis/unramified-representation-p-adic-group` | definition | Hyperspecial-fixed irreducibles and spherical vectors. |
| NEW | `harmonic-analysis/normalized-parabolic-induction-p-adic-group` | definition | Half-modulus normalization in the nonarchimedean setting. |
| NEW | `harmonic-analysis/whittaker-model` | definition | Generic representations and uniqueness setting. |
| NEW | `langlands/local-l-parameter` | definition | Admissible \(L\)-homomorphism into the \(L\)-group. |
| NEW | `langlands/local-langlands-correspondence` | conjecture | Basic finite-to-one correspondence and theorem-status boundaries. |
| NEW | `langlands/l-packet` | definition | Fiber of the basic local parameterization. |
| NEW | `langlands/component-group-of-l-parameter` | definition | Centralizer component groups and central quotients. |
| NEW | `langlands/whittaker-datum` | definition | Choice normalizing quasi-split packet parametrization. |
| NEW | `langlands/refined-local-langlands-correspondence` | conjecture | Internal packet parametrization and inner forms. |
| NEW | `langlands/local-langlands-correspondence-for-gln` | theorem | Established correspondence for \(\mathrm{GL}_n\). |
| NEW | `langlands/local-langlands-compatibilities` | theorem/conjecture | Central characters, twists, duals, and local factors. |

## Accepted new coverage: global automorphic and Galois dictionary

| Status | Canonical ID | Kind | Purpose |
|---|---|---|---|
| NEW | `langlands/automorphic-form` | definition | Canonical automorphic-form page split from the Letter's bundled eigenform page. |
| NEW | `langlands/automorphic-representation` | definition | Irreducible constituent of an automorphic representation space. |
| NEW | `langlands/restricted-tensor-product-automorphic-representation` | theorem | Factorization into local components. |
| NEW | `langlands/cuspidal-automorphic-representation` | definition | Cuspidal part of the automorphic spectrum. |
| NEW | `langlands/discrete-automorphic-spectrum` | definition | Hilbert direct-sum spectrum of the automorphic quotient. |
| NEW | `langlands/residual-automorphic-spectrum` | definition | Noncuspidal discrete spectrum from Eisenstein residues. |
| NEW | `langlands/global-langlands-parameter` | definition/conjecture | Global parameter concept with number/function-field boundaries. |
| NEW | `langlands/global-langlands-reciprocity` | conjecture | Automorphic and Galois/motivic parameterization. |
| NEW | `langlands/algebraic-automorphic-representation` | definition | Algebraicity at archimedean places. |
| NEW | `langlands/c-algebraic-automorphic-representation` | definition | Buzzard--Gee \(C\)-normalization. |
| NEW | `langlands/l-algebraic-automorphic-representation` | definition | Buzzard--Gee \(L\)-normalization. |
| NEW | `langlands/cohomological-automorphic-representation` | definition | Relative Lie algebra cohomology and its relation to C-algebraicity. |
| NEW | `langlands/regular-algebraic-cuspidal-automorphic-representation` | definition | The regular algebraic cuspidal general-linear-group setting for Galois constructions. |
| NEW | `langlands/compatible-system-of-galois-representations` | definition | Compatible Frobenius polynomials across \(\ell\). |
| NEW | `langlands/local-global-compatibility` | definition/theorem | Agreement of global Galois and local Langlands parameters. |
| NEW | `langlands/automorphic-galois-correspondence` | conjecture | Modern bridge with proved-case boundaries. |

## Accepted new coverage: trace formula, endoscopy, and Arthur packets

| Status | Canonical ID | Kind | Purpose |
|---|---|---|---|
| NEW | `langlands/arthur-selberg-trace-formula` | theorem/framework | Geometric and spectral expansions. |
| NEW | `langlands/strongly-regular-semisimple-element` | definition | Common regular locus for orbital integrals and endoscopic matching. |
| NEW | `langlands/orbital-integral` | definition | Conjugacy-orbit distribution. |
| NEW | `langlands/stable-conjugacy` | definition | Conjugacy after algebraic closure with Galois descent. |
| NEW | `langlands/stable-orbital-integral` | definition | Sum over rational classes in a stable class. |
| NEW | `langlands/kappa-orbital-integral` | definition | Character-weighted Fourier component inside a stable conjugacy class. |
| NEW | `langlands/endoscopic-datum` | definition | Dual-group datum controlling endoscopic transfer. |
| NEW | `langlands/transfer-factor` | definition | Normalized comparison factor for orbital integrals. |
| NEW | `langlands/endoscopic-transfer` | conjecture/theorem | Matching test functions and stable distributions. |
| NEW | `langlands/fundamental-lemma` | theorem | Unit-element identity enabling stabilization. |
| NEW | `langlands/stable-trace-formula` | theorem/framework | Stable decomposition of the invariant trace formula. |
| NEW | `langlands/arthur-parameter` | definition | \(L\)-parameter enlarged by an \(\mathrm{SL}_2\) factor. |
| NEW | `langlands/a-packet` | definition | Packet associated with an Arthur parameter. |
| NEW | `langlands/arthur-multiplicity-formula` | theorem/conjecture | Multiplicities in the discrete automorphic spectrum. |

## Accepted new coverage: function fields and local geometrization

| Status | Canonical ID | Kind | Purpose |
|---|---|---|---|
| NEW | `langlands/shtuka` | definition | Frobenius-modified bundle on a curve. |
| NEW | `langlands/g-shtuka` | definition | Multiple-leg shtuka for a reductive group. |
| NEW | `langlands/partial-frobenius-on-shtukas` | construction | Frobenius operations on selected legs. |
| NEW | `langlands/coalescence-of-shtuka-legs` | construction | Fusion maps used by excursion operators. |
| NEW | `langlands/excursion-operator` | construction | Commuting operators indexed by dual-group invariant data. |
| NEW | `langlands/excursion-algebra` | definition | Commutative algebra generated by excursion operators. |
| NEW | `langlands/lafforgue-global-parameterization` | theorem | Function-field automorphic-to-Galois decomposition. |
| NEW | `langlands/fargues-fontaine-curve` | definition | Curve underlying geometrized local Langlands. |
| NEW | `langlands/kottwitz-set-b-g` | definition | \(\sigma\)-conjugacy classes classifying \(G\)-bundles. |
| NEW | `langlands/g-bundle-on-fargues-fontaine-curve` | definition/theorem | \(G\)-bundles and their \(B(G)\)-classification. |
| NEW | `langlands/local-shtuka` | definition | Local modification space in mixed characteristic. |
| NEW | `langlands/stack-of-l-parameters` | definition | Spectral moduli stack for local Langlands. |
| NEW | `langlands/spectral-bernstein-center` | definition | Functions/perfect complexes on the parameter stack. |
| NEW | `langlands/spectral-action` | theorem/framework | Perfect complexes on the parameter stack acting on sheaves over the Fargues--Fontaine bundle stack. |
| NEW | `langlands/fargues-scholze-parameter-map` | theorem | Semisimplified parameter attached to a smooth irreducible representation. |

## Controlling literature

The principal source map is deliberately layered.

1. Jayce Getz and Heekyoung Hahn, *An Introduction to Automorphic
   Representations*, Springer, 2024.
2. Tasho Kaletha, “Representations of reductive groups over local fields,”
   2022, arXiv:2201.07741.
3. Kevin Buzzard and Toby Gee, “The conjectural connections between
   automorphic representations and Galois representations,” 2014,
   arXiv:1009.0785.
4. James Arthur, “The Principle of Functoriality,” 2002, and *An Introduction
   to the Trace Formula*, 2005.
5. Ngô Bảo Châu, “Survey on the Fundamental Lemma,” 2010, and “Le lemme
   fondamental pour les algèbres de Lie,” 2010.
6. James Arthur, *The Endoscopic Classification of Representations:
   Orthogonal and Symplectic Groups*, 2013.
7. Vincent Lafforgue, “Shtukas for reductive groups and Langlands
   correspondence for function fields,” 2018, backed by the full construction.
8. Naoki Imai, “On the geometrization of the local Langlands
   correspondence,” 2024, backed by Laurent Fargues and Peter Scholze,
   “Geometrization of the local Langlands correspondence,” 2021.
9. Ivan Mirković--Kari Vilonen, Dima Arinkin--Dennis Gaitsgory, and the 2024
   Dennis Gaitsgory--Sam Raskin geometric Langlands series for auditing the
   existing geometric collection.

## Completion record

The campaign was completed on 2026-08-10 in the content commit `b3e5313`.
`NEW` in the coverage tables records the change type, not unfinished work.

- All 33 Letter knowls were rewritten in place, preserving their IDs and
  `legacy_source_path` values.
- Sixty-four atomic knowls were added: six in `harmonic-analysis` and 58 in
  `langlands`. The modern and geometric guided indexes account for two more
  new files.
- The 32 pre-existing geometric-Langlands knowls were reused. Their current
  categorical theorem page and theorem-status boundaries were reviewed, and
  the collection received its own guided index rather than duplicate pages.
- The corpus interlinker proposed 397 links across the campaign files. A
  semantic review accepted 344 and rejected 53 category errors or misleading
  matches; a second pass left only those intentionally rejected candidates.
- The harmonic-analysis and top-level Langlands indexes now expose the new
  graph, while the Letter index explicitly identifies its historical scope.
- Four pre-existing nested knowl links, exposed by the production renderer in
  unrelated formal-group and hyperstructure pages, were flattened without
  changing their mathematical content.

## Dependency-closure follow-up

A second campaign pass audited the 97 substantive modernized pages by
mathematical concept rather than exact wording.  The reproducible ledger is in
[`langlands-dependency-audit.md`](langlands-dependency-audit.md).

- The deduplicated ledger contains 164 semantic entries: 88 concept families
  already covered by the corpus, 57 reusable missing prerequisites, and 19
  notation or convention items best defined in their consuming pages.
- All 57 reusable prerequisites were authored with concise canonical cores,
  progressive documentation, and literature sections. A repeat pass exposed
  Fontaine period rings and the Artin conductor; the read-only literal
  backstop then exposed a category mismatch between Euclidean test-function
  and distribution pages and their local-group analogues. All four became
  explicit reusable dependencies before declaring closure.
- Existing matches were accepted only after checking scope.  For example, the
  Euclidean Schwartz-distribution page was not treated as interchangeable
  with invariant distributions on a p-adic group, and smooth vector-bundle
  pages were not substituted for algebraic locally free sheaves.
- Ambiguous notation was resolved in place. In particular, the local
  parameter page now introduces \(W_F\) as the Weil group of the stated local
  field before defining \(L_F\).
- The content index
  `langlands/modern-langlands-dependency-index` exposes the full prerequisite
  collection as a navigable reading path.
- The repository's literal interlinking script is used only as a read-only
  final backstop for exact aliases and typos; the dependency decisions and
  page edits in this pass are model-reviewed.

## Remaining specialist-review candidates

These are follow-up opportunities, not known errors or blockers:

- `langlands-letter/knowls/borel-mostow-semisimple-normalizer` — verify the
  exact disconnected-group hypotheses against the version intended in the
  letter.
- `langlands-letter/knowls/characters-separate-semisimple-classes` — review
  the transition from connected invariant theory to twisted Frobenius cosets.
- `langlands/transfer-factor` and `langlands/arthur-multiplicity-formula` —
  review normalization and scope language against a specialist's preferred
  endoscopic conventions.
- `langlands/drinfeld-lemma` — review the precise coefficient-category and
  finiteness hypotheses across the finite-étale, lisse ell-adic, stack, and
  diamond variants.
- `langlands/fontaine-period-rings`, the four p-adic Hodge representation
  pages, `langlands/artin-conductor`, and the local factor pages — review sign,
  Frobenius, conductor, and additive-character normalization conventions as a
  connected cluster.
- `langlands/local-shimura-variety`, `langlands/rapoport-zink-space`, and
  `algebraic-geometry-foundations/v-stack` — review how far the concise pages
  should distinguish classical representable spaces from general diamonds
  and v-stacks.
- `langlands/spectral-action` and
  `langlands/fargues-scholze-parameter-map` — review the interface between the
  constructed spectral action, the semisimple parameter map, and the stronger
  categorical conjecture.
- `langlands/geometric-langlands-correspondence` — continue tracking the
  precise packaging and publication status of the Gaitsgory--Raskin theorem
  series.

## Validation and review evidence

- [x] Every accepted ID was authored; none were silently deferred.
- [x] Every Letter knowl has an action and completed editorial review.
- [x] The general and geometric Langlands indexes expose the new graph.
- [x] The 72 compiler/runtime tests pass.
- [x] The section audit passes for 3,390 primary knowls and 8,418 extracted
  sections; the external-link-format audit passes for all 3,390 files.
- [x] A strict development compilation resolves all IDs and links across
  4,576 knowls composed from 4,616 files. Its only diagnostics are 12
  pre-existing ambiguous alias warnings.
- [x] The production build compiles all 3,390 primary knowls, and the complete
  rendered-HTML scan reports no errors.
- [x] The generated before/after review contains 158 comparisons and was
  inspected in rendered form.
- [x] Representative local, global, endoscopic, function-field, and geometric
  pages were checked in rendered form.
- [x] Remaining SME-review candidates are explicitly identified above rather
  than silently marked complete.
