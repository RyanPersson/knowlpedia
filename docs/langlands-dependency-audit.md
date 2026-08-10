# Langlands dependency and interlinking audit

This ledger records the model-reviewed dependency closure of the Langlands
modernization campaign.  It is intentionally a semantic inventory, not the
output of a title-matching script.  The review unit is a mathematical concept:
different spellings and notations are merged only after checking that they
have the same meaning in context.

## Scope and method

- Baseline content commit: `b3e5313` (`Modernize Langlands corpus`).
- Reviewed scope: 97 substantive knowls: 64 new atomic knowls and 33 rewritten
  Langlands Letter knowls.  The two guided indexes and unrelated renderer
  repairs in the same commit are outside the dependency tally.
- A concept enters the ledger when a reader needs it to understand a canonical
  core or an important progressive section and the page does not define enough
  of it locally.
- `EXISTING` means that semantic coverage was found in the corpus, even when
  the filename or title differs from the wording in the reviewed page.
- `NEW` means that no adequate semantic equivalent was found and a reusable
  prerequisite knowl was accepted.
- `LOCAL` means notation, a convention, or narrow auxiliary machinery that is
  clearer when defined in the consuming page than when split into an atomic
  knowl.
- Links are added at the first useful occurrence in each section rather than
  mechanically linking every repeated word.
- The repository's literal title/alias interlinker does not make semantic
  decisions in this audit.  It is reserved for a read-only final backstop
  after the model-reviewed page edits, where it can expose misspellings or
  overlooked exact aliases without applying changes automatically.

The stable row labels make the tally reproducible without delegating any
mathematical decision to automation.

## Existing semantic coverage to reuse

| Row | Concept encountered | Existing canonical coverage |
|---|---|---|
| E01 | global field, number field, function field | `langlands-letter/knowls/global-local-fields-completions` |
| E02 | place, archimedean place, nonarchimedean place, completion | `langlands-letter/knowls/global-local-fields-completions` |
| E03 | local field | `langlands-letter/knowls/global-local-fields-completions` |
| E04 | p-adic field | `langlands-letter/knowls/p-adic-field` |
| E05 | finite field and residue field | `algebra-fields-galois/finite-field` plus local-field coverage in E01 |
| E06 | discrete valuation ring and uniformizer | `algebra-commutative/dvr` |
| E07 | valuation ring | `algebra-fields-galois/valuation-ring` |
| E08 | algebraic closure and separability terminology | `algebra-fields-galois/algebraic-closure` and `separable-extension` |
| E09 | absolute Galois group | `langlands-letter/knowls/galois-extension-and-group` |
| E10 | Frobenius element and arithmetic/geometric convention | `langlands-letter/knowls/frobenius-unramified` |
| E11 | Frobenius endomorphism, including absolute Frobenius after this pass | `algebra-fields-galois/frobenius-endomorphism` |
| E12 | unramified extension of a local field | `langlands-letter/knowls/unramified-extension-local` |
| E13 | tame ramification | `langlands/tame-ramification` |
| E14 | wild ramification | `langlands/wild-ramification` |
| E15 | adeles and restricted product | `langlands-letter/knowls/adeles-restricted-product` |
| E16 | ideles, Hecke characters, and global Artin reciprocity | `langlands-letter/knowls/ideles-artin-reciprocity-hecke-character` |
| E17 | locally compact group | `topology/locally-compact-group` |
| E18 | Haar measure and quotient measure | `harmonic-analysis/haar-measure` and `haar-integral` |
| E19 | modular function | `harmonic-analysis/modular-function` |
| E20 | convolution and Hecke algebra for a locally compact group | `harmonic-analysis/convolution-on-locally-compact-group` and `hecke-algebra-locally-compact-group-pair` |
| E21 | Schwartz--Bruhat function or space | `harmonic-analysis/schwartz-bruhat-space-local-field` and `schwartz-bruhat-space-adeles` |
| E22 | Euclidean Schwartz distribution and tempered distribution (comparison pages) | `functional-analysis/distribution` and `tempered-distribution` |
| E23 | Plancherel measure | `harmonic-analysis/plancherel-measure-nonabelian` |
| E24 | algebraic group and group scheme | `algebraic-geometry-foundations/algebraic-group` and `group-scheme` |
| E25 | connected reductive group | `algebraic-geometry-foundations/reductive-algebraic-group` |
| E26 | split reductive group | `langlands-letter/knowls/split-reductive-group` |
| E27 | maximal torus, character lattice, and cocharacter lattice | `langlands-letter/knowls/maximal-torus-weight-lattice` |
| E28 | roots, weights, Weyl group, and based root data | `langlands-letter/knowls/roots-weights-weyl` |
| E29 | coroot and root--coroot pairing | `langlands-letter/knowls/coroots-and-pairing` |
| E30 | root versus weight lattice and isogeny type | `langlands-letter/knowls/root-vs-weight-lattice-isogeny` |
| E31 | simply connected semisimple algebraic group | `langlands-letter/knowls/simply-connected-semisimple-group` |
| E32 | Borel subgroup | `algebraic-geometry-foundations/borel-subgroup` |
| E33 | parabolic subgroup | `algebraic-geometry-foundations/parabolic-subgroup` |
| E34 | algebraic principal bundle and G-torsor | `algebraic-geometry-foundations/principal-g-bundle-on-scheme` and `g-torsor-on-a-site` |
| E35 | moduli stack of G-bundles on a curve | `algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve` |
| E36 | form and inner form by Galois descent | `langlands-letter/knowls/galois-descent-forms` |
| E37 | nonabelian first Galois cohomology | `langlands-letter/knowls/nonabelian-h1-galois-cohomology` |
| E38 | semisimple element, Jordan decomposition, geometric/rational class | `langlands-letter/knowls/semisimple-element-and-class` |
| E39 | centralizer | `algebra-groups/centralizer` |
| E40 | normalizer | `algebra-groups/normalizer` |
| E41 | stabilizer and orbit | `algebra-groups/stabilizer` and `fiber-bundles/orbit-map` |
| E42 | hyperspecial maximal compact subgroup | `langlands-letter/knowls/maximal-compact-hyperspecial` |
| E43 | Chevalley basis and pinning | `langlands-letter/knowls/chevalley-basis` and `pinned-automorphisms` |
| E44 | Langlands dual group | `langlands-letter/knowls/langlands-dual-group` |
| E45 | L-group and L-homomorphism | `langlands/l-group` and `langlands-letter/knowls/langlands-functoriality-l-homomorphism` |
| E46 | Weil group | `langlands/weil-group` |
| E47 | Weil--Deligne group and representation | `langlands/weil-deligne-group` and `weil-deligne-representation` |
| E48 | Satake parameter and spherical Hecke algebra | `langlands/satake-parameter` and `langlands-letter/knowls/spherical-hecke-algebra-satake` |
| E49 | smooth representation of a totally disconnected group | `harmonic-analysis/smooth-representation-totally-disconnected-group` |
| E50 | admissible p-adic representation | `harmonic-analysis/admissible-representation-p-adic-group` |
| E51 | supercuspidal representation | `harmonic-analysis/supercuspidal-representation` |
| E52 | unramified representation and spherical vector | `harmonic-analysis/unramified-representation-p-adic-group` |
| E53 | normalized p-adic parabolic induction | `harmonic-analysis/normalized-parabolic-induction-p-adic-group` |
| E54 | Whittaker model and generic representation | `harmonic-analysis/whittaker-model` |
| E55 | square-integrability modulo the center | `lie-groups/square-integrable-modulo-center-representation` |
| E56 | contragredient and smooth dual | `langlands-letter/knowls/contragredient-representation` |
| E57 | restricted tensor product of representations | `langlands/restricted-tensor-product-automorphic-representation` |
| E58 | K-finite vector, (g,K)-module, and Harish--Chandra module | `lie-groups/k-finite-vector`, `g-k-module`, and `harish-chandra-module` |
| E59 | infinitesimal character | `lie-groups/infinitesimal-character` |
| E60 | local L-parameter, L-packet, and component group | `langlands/local-l-parameter`, `l-packet`, and `component-group-of-l-parameter` |
| E61 | Whittaker datum and refined local Langlands | `langlands/whittaker-datum` and `refined-local-langlands-correspondence` |
| E62 | automorphic form and automorphic representation | `langlands/automorphic-form` and `automorphic-representation` |
| E63 | cuspidal automorphic representation | `langlands/cuspidal-automorphic-representation` |
| E64 | discrete and residual automorphic spectrum | `langlands/discrete-automorphic-spectrum` and `residual-automorphic-spectrum` |
| E65 | Eisenstein series | `langlands-letter/knowls/eisenstein-series` |
| E66 | algebraic, C-algebraic, and L-algebraic automorphic representation | `langlands/algebraic-automorphic-representation`, `c-algebraic-automorphic-representation`, and `l-algebraic-automorphic-representation` |
| E67 | cohomological and regular algebraic cuspidal representation | `langlands/cohomological-automorphic-representation` and `regular-algebraic-cuspidal-automorphic-representation` |
| E68 | compatible system of Galois representations | `langlands/compatible-system-of-galois-representations` |
| E69 | local--global compatibility | `langlands/local-global-compatibility` |
| E70 | Euler product and unramified local factor | `langlands-letter/knowls/euler-product-and-local-factor` |
| E71 | Langlands functoriality | `langlands-letter/knowls/langlands-functoriality-l-homomorphism` |
| E72 | trace formula and stable trace formula | `langlands/arthur-selberg-trace-formula` and `stable-trace-formula` |
| E73 | strongly regular semisimple element and orbital integral | `langlands/strongly-regular-semisimple-element` and `orbital-integral` |
| E74 | stable conjugacy, stable orbital integral, and kappa orbital integral | `langlands/stable-conjugacy`, `stable-orbital-integral`, and `kappa-orbital-integral` |
| E75 | endoscopic datum, transfer factor, and endoscopic transfer | `langlands/endoscopic-datum`, `transfer-factor`, and `endoscopic-transfer` |
| E76 | fundamental lemma | `langlands/fundamental-lemma` |
| E77 | Arthur parameter, packet, and multiplicity formula | `langlands/arthur-parameter`, `a-packet`, and `arthur-multiplicity-formula` |
| E78 | algebraic stack, quotient stack, and derived algebraic stack | `algebraic-geometry-foundations/algebraic-stack` and `derived-algebraic-stack` |
| E79 | perverse sheaf and intersection complex | `langlands/perverse-sheaf` and `intersection-cohomology-complex` |
| E80 | geometric Satake equivalence | `langlands/geometric-satake-equivalence` |
| E81 | shtuka, G-shtuka, partial Frobenius, and coalescence | `langlands/shtuka`, `g-shtuka`, `partial-frobenius-on-shtukas`, and `coalescence-of-shtuka-legs` |
| E82 | excursion operator and excursion algebra | `langlands/excursion-operator` and `excursion-algebra` |
| E83 | Fargues--Fontaine curve and G-bundles on it | `langlands/fargues-fontaine-curve` and `g-bundle-on-fargues-fontaine-curve` |
| E84 | Kottwitz set, sigma-conjugacy class, and G-isocrystal | `langlands/kottwitz-set-b-g` |
| E85 | local shtuka and modification of a G-bundle | `langlands/local-shtuka` |
| E86 | stack of L-parameters, spectral center, and spectral action | `langlands/stack-of-l-parameters`, `spectral-bernstein-center`, and `spectral-action` |
| E87 | symmetric monoidal category | `algebra-category-theory/symmetric-monoidal-category` |
| E88 | group algebra and Laurent polynomial ring | `algebra-representation-theory/group-algebra` and `algebra-rings/laurent-polynomial-ring` |

## Accepted missing prerequisites

| Row | Concept or tightly coupled concept family | New canonical ID |
|---|---|---|
| N01 | decomposition group | `algebra-fields-galois/decomposition-group` |
| N02 | inertia subgroup | `algebra-fields-galois/inertia-subgroup` |
| N03 | local class field theory | `langlands/local-class-field-theory` |
| N04 | Chebotarev density theorem | `algebra-fields-galois/chebotarev-density-theorem` |
| N05 | Hodge--Tate representation and weights | `langlands/hodge-tate-representation` |
| N06 | de Rham Galois representation | `langlands/de-rham-galois-representation` |
| N07 | crystalline Galois representation | `langlands/crystalline-galois-representation` |
| N08 | semistable and potentially semistable Galois representation | `langlands/semistable-galois-representation` |
| N09 | quasi-split reductive group | `algebraic-geometry-foundations/quasi-split-reductive-group` |
| N10 | unramified reductive group | `algebraic-geometry-foundations/unramified-reductive-group` |
| N11 | Levi subgroup | `algebraic-geometry-foundations/levi-subgroup` |
| N12 | unipotent radical | `algebraic-geometry-foundations/unipotent-radical` |
| N13 | rigid inner twist | `langlands/rigid-inner-twist` |
| N14 | twisted conjugacy | `langlands/twisted-conjugacy` |
| N15 | locally profinite group and compact-open subgroup basis | `topology/locally-profinite-group` |
| N16 | Jacquet module | `harmonic-analysis/jacquet-module` |
| N17 | parabolic modulus character | `harmonic-analysis/parabolic-modulus-character` |
| N18 | tempered representation of a p-adic group | `harmonic-analysis/tempered-representation-p-adic-group` |
| N19 | Langlands classification for p-adic groups | `harmonic-analysis/langlands-classification-p-adic-group` |
| N20 | Bernstein decomposition | `harmonic-analysis/bernstein-decomposition` |
| N21 | Bernstein center | `harmonic-analysis/bernstein-center` |
| N22 | central character of a group representation | `algebra-representation-theory/central-character` |
| N23 | Harish--Chandra distribution character for p-adic groups | `harmonic-analysis/harish-chandra-character-p-adic-group` |
| N24 | local epsilon factor | `langlands/local-epsilon-factor` |
| N25 | local gamma factor | `langlands/local-gamma-factor` |
| N26 | automorphic constant term | `langlands/automorphic-constant-term` |
| N27 | continuous automorphic spectrum | `langlands/continuous-automorphic-spectrum` |
| N28 | relative Lie algebra cohomology | `lie-groups/relative-lie-algebra-cohomology` |
| N29 | isobaric automorphic representation | `langlands/isobaric-automorphic-representation` |
| N30 | strong multiplicity one | `langlands/strong-multiplicity-one-theorem` |
| N31 | Arthur truncation | `langlands/arthur-truncation` |
| N32 | global and local root number | `langlands/root-number` |
| N33 | stable distribution | `langlands/stable-distribution` |
| N34 | weighted orbital integral | `langlands/weighted-orbital-integral` |
| N35 | Tate--Nakayama duality | `langlands/tate-nakayama-duality` |
| N36 | Hitchin fibration | `langlands/hitchin-fibration` |
| N37 | affine Springer fiber | `langlands/affine-springer-fiber` |
| N38 | Harder--Narasimhan filtration and truncation | `algebraic-geometry-foundations/harder-narasimhan-filtration` |
| N39 | Drinfeld's lemma | `langlands/drinfeld-lemma` |
| N40 | lisse ell-adic sheaf | `algebraic-geometry-foundations/lisse-ell-adic-sheaf` |
| N41 | compactly supported etale cohomology | `algebraic-geometry-foundations/compactly-supported-etale-cohomology` |
| N42 | adic space | `algebraic-geometry-foundations/adic-space` |
| N43 | perfectoid field | `algebraic-geometry-foundations/perfectoid-field` |
| N44 | perfectoid space | `algebraic-geometry-foundations/perfectoid-space` |
| N45 | tilting and untilting | `algebraic-geometry-foundations/tilt-and-untilt` |
| N46 | isocrystal | `algebraic-geometry-foundations/isocrystal` |
| N47 | v-stack | `algebraic-geometry-foundations/v-stack` |
| N48 | perfect complex | `algebraic-geometry-foundations/perfect-complex` |
| N49 | Tannakian category and fiber functor | `algebra-category-theory/tannakian-category` |
| N50 | local Shimura variety | `langlands/local-shimura-variety` |
| N51 | Rapoport--Zink space | `langlands/rapoport-zink-space` |
| N52 | representation ring | `algebra-representation-theory/representation-ring` |
| N53 | Tamagawa measure | `langlands/tamagawa-measure` |
| N54 | Fontaine period rings | `langlands/fontaine-period-rings` |
| N55 | Artin conductor | `langlands/artin-conductor` |
| N56 | test-function space on a local group | `harmonic-analysis/test-function-space-local-group` |
| N57 | distribution on a local group | `harmonic-analysis/distribution-local-group` |

The scheme-theoretic absolute Frobenius was initially a `NEW` candidate.  The
semantic audit found that it is the natural geometric extension of E11, so the
existing Frobenius-endomorphism page is expanded instead of adding a duplicate.
The repeat closure pass over the new prerequisite pages exposed N54 and N55;
both recur across several p-adic Hodge and local-factor pages and therefore
belong in reusable knowls rather than in one consuming page. The final
read-only literal backstop then exposed a semantic scope error: several local
and adelic harmonic-analysis pages still pointed to the Euclidean
test-function and Schwartz-distribution pages. Model review rejected those
matches and added N56 and N57 to distinguish the archimedean and
nonarchimedean local-group categories explicitly.

## Concepts intentionally defined locally

| Row | Local item | Editorial decision |
|---|---|---|
| I01 | \(L_F\), the local Langlands group used in a page | Define immediately after introducing \(W_F\); conventions vary. |
| I02 | \(\operatorname{Irr}(G(F))\), \(\Phi(G)\), and similar set notation | Define at first use; these are notation, not concepts. |
| I03 | a chosen Frobenius lift | State arithmetic/geometric convention locally and link E10. |
| I04 | normalized versus unnormalized induction | State the convention locally and link E53 and N17. |
| I05 | Frobenius semisimplification | Define the operation in local--global compatibility; link E47 and E38. |
| I06 | relevance of an L-parameter to an inner form | Retain as a section of `local-l-parameter`; it depends on E33, N11, and N13. |
| I07 | elliptic/discrete parameter in a specific L-group | Define in the parameter page and link N18/E55 for the representation-side analogy. |
| I08 | z-pair in endoscopy | Explain in the endoscopic-transfer page; it is auxiliary transfer data rather than a general prerequisite. |
| I09 | Langlands--Shelstad a-data and chi-data | Explain their normalization role in the transfer-factor page; flag normalization for specialist review. |
| I10 | admissibility conditions on an L-homomorphism | State in the L-parameter page; the exact list depends on the chosen presentation of \(L_F\). |
| I11 | the invariant functions \(f\) used by excursion operators | Define in the construction; link E44 and E82 rather than atomizing the notation. |
| I12 | paws/legs and partitions of a finite index set | Define in the shtuka page; ordinary finite-set notation needs no knowl. |
| I13 | Hecke-finite vectors in shtuka cohomology | Define in the theorem page; link E48 and E82. |
| I14 | Newton point and Kottwitz invariant of a class in \(B(G)\) | Keep in E84, where the pair classifies the intended objects. |
| I15 | semistable locus in \(\operatorname{Bun}_G\) | Define in context using N38 and E83. |
| I16 | spectral support of a sheaf | Explain in the spectral-action page using N48 and E86; no competing general definition yet. |
| I17 | a choice of pinning or Whittaker normalization | State the choice locally and link E43/E61. |
| I18 | measure and additive-character normalizations of local factors | State on N24/N25 and in consuming pages; there is no choice-free formula. |
| I19 | source-specific notation from the 1967 letter | Preserve only in the historical section and translate it into the modern linked vocabulary. |

## Tally

The deduplicated audit contains **164 semantic entries**: **88** concepts or
concept families covered by existing knowls, **57** accepted missing
prerequisites, and **19** items to define locally.  This is a concept tally,
not a count of raw word occurrences.  Repeated occurrences are handled during
the page-by-page link pass.

## Closure and review evidence

- All 97 campaign knowls and all 57 reusable prerequisites received
  page-by-page semantic passes. The local parameter page now defines and links
  \(W_F\) before using \(L_F\).
- A read-only literal backstop was run only after those model-reviewed edits.
  It left 57 suggestions in the 97 campaign files and 33 in the 57
  prerequisites plus their index. Every remaining suggestion was inspected
  and rejected as either a repeated label already linked earlier in its
  section, a multiline-link parser false positive, or a category collision.
  Representative rejected collisions include p-adic versus real
  admissibility, algebraic versus topological simple connectedness, p-adic
  versus complex monodromy, and algebraic versus smooth vector bundles.
- The backstop did expose one genuine scope gap: local-group test functions
  and distributions had been linked to their Euclidean analogues. N56 and N57
  now separate those categories, and the affected orbital-integral,
  endoscopic, trace-formula, stable-distribution, and p-adic character pages
  point to the new canonical knowls.
- Strict development compilation resolves all IDs and links across 4,576
  knowls composed from 4,616 files. Its only diagnostics are 12 pre-existing
  ambiguous-alias warnings.
- All 72 compiler/runtime tests pass. The section audit passes for 3,390
  primary knowls and 8,418 extracted sections, and the external-link-format
  audit passes for all 3,390 primary knowls.
- The production build compiles all 3,390 primary knowls, and the full
  rendered-HTML scan reports no errors.
- The dependency index, local \(L\)-parameter page, and local-group
  test-function page were inspected in rendered form through the persistent
  port-8012 preview.
