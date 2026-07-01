+++
id = "convex-analysis/convexity-preserved-under-affine-composition"
title = "Convexity Preserved Under Affine Composition"
kind = "knowl"
summary = "Precomposition of a convex function with an affine map preserves convexity"
aliases = ["convexity-preserved-under-affine-composition", "Convexity Preserved Under Affine Composition"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convexity-preserved-under-affine-composition.md"
+++

**Affine Composition Rule**: Let $B:X\to Y$ be an [[convex-analysis/affine-mapping|affine mapping]] between [[linear-algebra/vector-space|vector spaces]], and let $f:Y\to\overline{\mathbb{R}}$ be a [[convex-analysis/convex-function-via-epigraph|convex function]]. Then $f\circ B$ is convex on $X$.

This is the basic "change of variables" principle in convex analysis: restricting a convex function to an affine subspace or composing with an affine parameterization preserves convexity.

**Proof sketch (idea):** Use the defining identity for affine maps,
$B(\lambda x+(1-\lambda)y)=\lambda B(x)+(1-\lambda)B(y)$,
and then apply Jensen's inequality for $f$.
