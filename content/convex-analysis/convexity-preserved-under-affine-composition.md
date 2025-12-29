---
title: "Convexity Preserved Under Affine Composition"
description: "Precomposition of a convex function with an affine map preserves convexity"
---

**Affine Composition Rule**: Let $B:X\to Y$ be an {{< knowl id="affine-mapping" text="affine mapping" >}} between {{< knowl id="vector-space" text="vector spaces" >}}, and let $f:Y\to\overline{\mathbb{R}}$ be a {{< knowl id="convex-function-via-epigraph" text="convex function" >}}. Then $f\circ B$ is convex on $X$.

This is the basic "change of variables" principle in convex analysis: restricting a convex function to an affine subspace or composing with an affine parameterization preserves convexity.

**Proof sketch (idea):** Use the defining identity for affine maps,
$B(\lambda x+(1-\lambda)y)=\lambda B(x)+(1-\lambda)B(y)$,
and then apply Jensen's inequality for $f$.
