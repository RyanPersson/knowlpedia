import os

output_dir = "/Users/ryanpersson/anki/code/blog/tmp/v1-topology"

# All topology slugs combined for the manifest
all_topology_slugs = [
    # topology-core
    "topological-space", "topology", "topology-axioms", "open-set", "closed-set",
    "interior", "closure", "neighborhood", "limit-point-accumulation-point-cluster-point",
    "derived-set", "dense-set", "dense-subset", "subspace-topology", "continuous-map",
    "continuity-via-open-sets", "homeomorphism", "basis-of-a-topology", "topology-generated-by-basis",
    "subbasis-of-a-topology", "product-topology", "quotient-topology", "cover",
    # topology-metric
    "metric", "metric-space", "metric-induced-topology", "open-ball", "closed-ball",
    "sphere-metric-sphere", "diameter", "bounded-set", "separated-sets", "convergent-sequence",
    "limit-of-a-sequence", "cauchy-sequence", "every-cauchy-sequence-is-bounded",
    "convergent-sequence-is-cauchy", "complete-metric-space", "equivalent-metrics", "isometry",
    "uniformly-continuous-map", "lipschitz-continuity", "holder-continuity",
    "cantor-intersection-theorem", "nested-interval-theorem", "bolzano-weierstrass-theorem",
    # topology-compactness
    "open-cover", "refinement-of-an-open-cover", "finite-subcover-lemma", "compact-set",
    "compactness-implies-boundedness", "compactness-implies-closedness",
    "closed-subset-of-compact-set-is-compact", "continuous-image-of-compact-set-is-compact",
    "continuous-attains-max-min-compact", "finite-intersection-property-theorem",
    "sequentially-compact-set", "sequential-compactness-equals-compactness",
    "total-boundedness-epsilon-nets", "totally-bounded-set", "totally-bounded-cauchy-subsequence",
    "compactness-implies-total-boundedness", "compactness-implies-completeness",
    "compact-iff-complete-totally-bounded", "heine-borel-theorem", "lebesgue-number-lemma",
    "lebesgue-number-lemma-auxiliary-refinement", "compactness-of-graphs-lemma",
    "continuous-bijection-from-compact-homeomorphism-criterion",
    "continuous-image-compact-closed-bounded", "compact-subset-of-hausdorff-is-closed",
    "compactness-criteria-rk",
    # topology-connectedness
    "connected-set", "connected-component", "path", "path-connected-set",
    "continuous-image-of-connected-set-is-connected", "connected-subsets-of-r-are-intervals",
    "connectedness-criteria-r", "image-compact-connected-is-interval", "curve",
    "intermediate-value-property-topological",
    # topology-separation
    "t0-space", "t1-space", "hausdorff-space", "sequential-characterization-of-closed-sets",
    "sequential-characterization-of-closure", "uniqueness-of-limits-hausdorff",
    # topology-baire
    "baire-space", "baire-category-theorem", "nowhere-dense-set", "meager-set",
    "residual-set", "complete-metric-space-is-baire", "intersection-of-dense-open-is-dense",
    "category-argument-template"
]

# Prerequisites (no section param in v1 - just list them)
prereq_slugs = [
    # shared-foundations
    "axiom-of-choice", "bijective-function", "binary-operation", "cardinality", "cartesian-product",
    "codomain", "complement", "composition", "countable-set", "domain", "empty-set",
    "equivalence-class", "equivalence-relation", "function", "identity-function", "image",
    "injective-function", "intersection", "inverse-function", "lower-bound", "mathematical-induction",
    "morphism", "ordered-pair", "partial-order", "partition", "preimage", "proper-subset",
    "quotient-set", "relation", "set", "set-difference", "subset", "surjective-function",
    "total-order", "union", "upper-bound", "well-ordered-set", "well-ordering-principle",
    "well-ordering-theorem", "zfc-axioms", "zorns-lemma",
    # linear-algebra
    "banach-space", "basis-existence-theorem", "bilinear-form", "cayley-hamilton-theorem",
    "characteristic-polynomial", "compact-operator", "determinant", "eigenspace", "eigenvalue",
    "eigenvector", "euclidean-norm", "euclidean-space", "hilbert-space", "inner-product",
    "inner-product-space", "linear-map", "linear-operator", "minimal-polynomial", "norm",
    "operator-norm", "orthogonality", "rank-nullity-theorem", "trace", "vector-space"
]

# Batches by section
batches = {
    "topology-core": [
        "topological-space", "topology", "topology-axioms", "open-set", "closed-set",
        "interior", "closure", "neighborhood", "limit-point-accumulation-point-cluster-point",
        "derived-set", "dense-set", "dense-subset", "subspace-topology", "continuous-map",
        "continuity-via-open-sets", "homeomorphism", "basis-of-a-topology", "topology-generated-by-basis",
        "subbasis-of-a-topology", "product-topology", "quotient-topology", "cover"
    ],
    "topology-metric": [
        "metric", "metric-space", "metric-induced-topology", "open-ball", "closed-ball",
        "sphere-metric-sphere", "diameter", "bounded-set", "separated-sets", "convergent-sequence",
        "limit-of-a-sequence", "cauchy-sequence", "every-cauchy-sequence-is-bounded",
        "convergent-sequence-is-cauchy", "complete-metric-space", "equivalent-metrics", "isometry",
        "uniformly-continuous-map", "lipschitz-continuity", "holder-continuity",
        "cantor-intersection-theorem", "nested-interval-theorem", "bolzano-weierstrass-theorem"
    ],
    "topology-compactness": [
        "open-cover", "refinement-of-an-open-cover", "finite-subcover-lemma", "compact-set",
        "compactness-implies-boundedness", "compactness-implies-closedness",
        "closed-subset-of-compact-set-is-compact", "continuous-image-of-compact-set-is-compact",
        "continuous-attains-max-min-compact", "finite-intersection-property-theorem",
        "sequentially-compact-set", "sequential-compactness-equals-compactness",
        "total-boundedness-epsilon-nets", "totally-bounded-set", "totally-bounded-cauchy-subsequence",
        "compactness-implies-total-boundedness", "compactness-implies-completeness",
        "compact-iff-complete-totally-bounded", "heine-borel-theorem", "lebesgue-number-lemma",
        "lebesgue-number-lemma-auxiliary-refinement", "compactness-of-graphs-lemma",
        "continuous-bijection-from-compact-homeomorphism-criterion",
        "continuous-image-compact-closed-bounded", "compact-subset-of-hausdorff-is-closed",
        "compactness-criteria-rk"
    ],
    "topology-connectedness": [
        "connected-set", "connected-component", "path", "path-connected-set",
        "continuous-image-of-connected-set-is-connected", "connected-subsets-of-r-are-intervals",
        "connectedness-criteria-r", "image-compact-connected-is-interval", "curve",
        "intermediate-value-property-topological"
    ],
    "topology-separation": [
        "t0-space", "t1-space", "hausdorff-space", "sequential-characterization-of-closed-sets",
        "sequential-characterization-of-closure", "uniqueness-of-limits-hausdorff"
    ],
    "topology-baire": [
        "baire-space", "baire-category-theorem", "nowhere-dense-set", "meager-set",
        "residual-set", "complete-metric-space-is-baire", "intersection-of-dense-open-is-dense",
        "category-argument-template"
    ]
}

# v1 prompt template (based on step-3-create-and-link.md)
prompt_template = '''# Step 3: Create and Link Knowls

## Your Task

Create knowl markdown files **with cross-links already included**. You will receive:
1. The **full slug manifest** — all knowl slugs that will exist
2. Your **assigned batch** — the specific knowls you must create

Create each knowl in your batch with complete content and all relevant cross-links to other knowls in the manifest.

## Slug Manifest

The complete list of all knowl slugs (you can link to any of these):
```
{manifest}
```

## Output Format

For each item in your batch, produce a complete knowl with links:

**`[slug].md`**
```markdown
---
title: "[Display Name]"
description: "[One-line plain-text description]"
---

[Content with {{{{< knowl >}}}} links already included]
```

## Linking Syntax

Use the Hugo knowl shortcode:
```
{{{{< knowl id="[slug]" text="[display text]" >}}}}
```

**CRITICAL:** The shortcode uses **double curly braces**: `{{{{<` not `{{<`. Single braces will not render correctly.

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

[1-3 sentences of context with {{{{< knowl >}}}} links to prerequisite concepts]

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

[1-3 sentences of context with {{{{< knowl >}}}} links to key concepts]

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

[1-2 sentences connecting this to its {{{{< knowl >}}}} linked parent theorem]
```

## Critical Formatting Rules

**YAML Front Matter:**
- `description` must be **plain text only** — no LaTeX, no math symbols
- Bad: `description: "The map $f: X \\to Y$ satisfying..."`
- Good: `description: "A continuous map satisfying the universal property"`

**Shortcode Braces:**
- Use **exactly two** curly braces: `{{{{<` and `>}}}}`
- Triple braces `{{{{{{<` will cause Hugo errors
- Single braces `{{<` will not render

**No "Related" Sections:**
- Do NOT include a "Related" or "Related knowls" section at the end
- All cross-links must be woven naturally into the prose

## Your Batch

Generate knowls for these slugs:
{batch_slugs}

## Verification

Before submitting, verify:
- [ ] No shortcodes appear inside `$...$` or `$$...$$` math blocks
- [ ] No LaTeX or math symbols in YAML `description` field
- [ ] Shortcodes use exactly double braces `{{{{<` and `>}}}}`
- [ ] No term is linked more than once per knowl
- [ ] Every slug in your shortcodes appears in the manifest
- [ ] The term being defined is NOT linked to itself
- [ ] No "Related" section at the end
'''

# Build manifest
all_slugs = prereq_slugs + all_topology_slugs
manifest = "\n".join(f"{s}.md" for s in all_slugs)

# Create batch files
batch_num = 1
for section_name, slugs in batches.items():
    batch_slugs = "\n".join(f"- {s}" for s in slugs)
    
    content = prompt_template.format(
        manifest=manifest,
        batch_slugs=batch_slugs
    )
    
    filename = f"batch{batch_num}.md"
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write(content)
    
    print(f"Created {filename} for {section_name} ({len(slugs)} slugs)")
    batch_num += 1

# Create oracle config file
with open(os.path.join(output_dir, "oracle-config.txt"), 'w') as f:
    for i in range(1, 7):
        f.write(f"{output_dir}/batch{i}.md\n")

print(f"\nCreated oracle-config.txt")
print(f"Total: 6 batch files ready")
