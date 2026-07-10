# Step 3: Create and Link Knowls

## Your Task

Create knowl markdown files **with cross-links already included**. You will receive:
1. The **full slug manifest** — all knowl slugs that will exist
2. Your **assigned batch** — the specific knowls you must create

Create each knowl in your batch with complete content and all relevant cross-links to other knowls in the manifest.

## Slug Manifest

The complete list of all knowl slugs (you can link to any of these):
```
axiom-of-choice.md
bijective-function.md
binary-operation.md
cardinality.md
cartesian-product.md
codomain.md
complement.md
composition.md
countable-set.md
domain.md
empty-set.md
equivalence-class.md
equivalence-relation.md
function.md
identity-function.md
image.md
injective-function.md
intersection.md
inverse-function.md
lower-bound.md
mathematical-induction.md
morphism.md
ordered-pair.md
partial-order.md
partition.md
preimage.md
proper-subset.md
quotient-set.md
relation.md
set.md
set-difference.md
subset.md
surjective-function.md
total-order.md
union.md
upper-bound.md
well-ordered-set.md
well-ordering-principle.md
well-ordering-theorem.md
zfc-axioms.md
zorns-lemma.md
banach-space.md
basis-existence-theorem.md
bilinear-form.md
cayley-hamilton-theorem.md
characteristic-polynomial.md
compact-operator.md
determinant.md
eigenspace.md
eigenvalue.md
eigenvector.md
euclidean-norm.md
euclidean-space.md
hilbert-space.md
inner-product.md
inner-product-space.md
linear-map.md
linear-operator.md
minimal-polynomial.md
norm.md
operator-norm.md
orthogonality.md
rank-nullity-theorem.md
trace.md
vector-space.md
topological-space.md
topology.md
topology-axioms.md
open-set.md
closed-set.md
interior.md
closure.md
neighborhood.md
limit-point-accumulation-point-cluster-point.md
derived-set.md
dense-set.md
dense-subset.md
subspace-topology.md
continuous-map.md
continuity-via-open-sets.md
homeomorphism.md
basis-of-a-topology.md
topology-generated-by-basis.md
subbasis-of-a-topology.md
product-topology.md
quotient-topology.md
cover.md
metric.md
metric-space.md
metric-induced-topology.md
open-ball.md
closed-ball.md
sphere-metric-sphere.md
diameter.md
bounded-set.md
separated-sets.md
convergent-sequence.md
limit-of-a-sequence.md
cauchy-sequence.md
every-cauchy-sequence-is-bounded.md
convergent-sequence-is-cauchy.md
complete-metric-space.md
equivalent-metrics.md
isometry.md
uniformly-continuous-map.md
lipschitz-continuity.md
holder-continuity.md
cantor-intersection-theorem.md
nested-interval-theorem.md
bolzano-weierstrass-theorem.md
open-cover.md
refinement-of-an-open-cover.md
finite-subcover-lemma.md
compact-set.md
compactness-implies-boundedness.md
compactness-implies-closedness.md
closed-subset-of-compact-set-is-compact.md
continuous-image-of-compact-set-is-compact.md
continuous-attains-max-min-compact.md
finite-intersection-property-theorem.md
sequentially-compact-set.md
sequential-compactness-equals-compactness.md
total-boundedness-epsilon-nets.md
totally-bounded-set.md
totally-bounded-cauchy-subsequence.md
compactness-implies-total-boundedness.md
compactness-implies-completeness.md
compact-iff-complete-totally-bounded.md
heine-borel-theorem.md
lebesgue-number-lemma.md
lebesgue-number-lemma-auxiliary-refinement.md
compactness-of-graphs-lemma.md
continuous-bijection-from-compact-homeomorphism-criterion.md
continuous-image-compact-closed-bounded.md
compact-subset-of-hausdorff-is-closed.md
compactness-criteria-rk.md
connected-set.md
connected-component.md
path.md
path-connected-set.md
continuous-image-of-connected-set-is-connected.md
connected-subsets-of-r-are-intervals.md
connectedness-criteria-r.md
image-compact-connected-is-interval.md
curve.md
intermediate-value-property-topological.md
t0-space.md
t1-space.md
hausdorff-space.md
sequential-characterization-of-closed-sets.md
sequential-characterization-of-closure.md
uniqueness-of-limits-hausdorff.md
baire-space.md
baire-category-theorem.md
nowhere-dense-set.md
meager-set.md
residual-set.md
complete-metric-space-is-baire.md
intersection-of-dense-open-is-dense.md
category-argument-template.md
```

## Output Format

For each item in your batch, produce a complete knowl with links:

**`[slug].md`**
```markdown
---
title: "[Display Name]"
description: "[One-line plain-text description]"
---

[Content with {{< knowl >}} links already included]
```

## Linking Syntax

Use the Hugo knowl shortcode:
```
{{< knowl id="[slug]" text="[display text]" >}}
```

**CRITICAL:** The shortcode uses **double curly braces**: `{{<` not `{<`. Single braces will not render correctly.

Where:
- `[slug]` is the filename without `.md` (e.g., `group`, `lagranges-theorem`)
- `[display text]` is the text shown to the reader

### Linking Rules

**Link a term when:**
- It appears in prose/context sections
- It appears in example descriptions
- It is a key concept in the statement that benefits from expansion

**Do NOT link:**
- Terms inside LaTeX math environments (`$...$` or `$$...$$`)
- The term being defined in its own definition
- Every occurrence—link only the **first meaningful occurrence**

## Content Structure by Type

### For Definitions

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

A **[name]** is [formal definition using LaTeX notation].

[1-3 sentences of context with {{< knowl >}} links to prerequisite concepts]

**Examples:**
- [Concrete example with values/specifics]
- [Another example, possibly from a different context]
- [Optional: counterexample or edge case]
```

### For Theorems, Lemmas, Propositions

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

**[Name]**: [Precise statement of the result using LaTeX notation]

[1-3 sentences of context with {{< knowl >}} links to key concepts]

**Proof sketch** *(optional, include for major theorems)*:
[2-4 sentences outlining the key idea of the proof]
```

### For Corollaries

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

**[Name]**: [Statement of the corollary]

[1-2 sentences connecting this to its {{< knowl >}} linked parent theorem]
```

## Critical Formatting Rules

**YAML Front Matter:**
- `description` must be **plain text only** — no LaTeX, no math symbols
- Bad: `description: "The map $f: X \to Y$ satisfying..."`
- Good: `description: "A continuous map satisfying the universal property"`

**Shortcode Braces:**
- Use **exactly two** curly braces: `{{<` and `>}}`
- Triple braces `{{{<` will cause Hugo errors
- Single braces `{<` will not render

**No "Related" Sections:**
- Do NOT include a "Related" or "Related knowls" section at the end
- All cross-links must be woven naturally into the prose

## Your Batch

Generate knowls for these slugs:
- t0-space
- t1-space
- hausdorff-space
- sequential-characterization-of-closed-sets
- sequential-characterization-of-closure
- uniqueness-of-limits-hausdorff

## Verification

Before submitting, verify:
- [ ] No shortcodes appear inside `$...$` or `$$...$$` math blocks
- [ ] No LaTeX or math symbols in YAML `description` field
- [ ] Shortcodes use exactly double braces `{{<` and `>}}`
- [ ] No term is linked more than once per knowl
- [ ] Every slug in your shortcodes appears in the manifest
- [ ] The term being defined is NOT linked to itself
- [ ] No "Related" section at the end
