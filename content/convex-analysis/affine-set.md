---
title: "Affine Set"
description: "A set containing the entire line through any two of its points."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}}. A subset $\Omega\subset X$ is **affine** if for all $a,b\in\Omega$ we have
$$
L[a,b]\subset \Omega,
$$
where $L[a,b]$ is the {{< knowl id="line-connecting-two-points" text="line connecting a and b" >}}.

Equivalently, $\Omega$ is affine if it is a translate of a {{< knowl id="linear-subspace" text="linear subspace" >}} (see {{< knowl id="affine-sets-are-translates-of-subspaces" text="the translate characterization" >}}).

**Examples:**
- Any linear subspace is affine.
- In $\mathbb{R}^n$, a set of the form $x_0+L$ with $L$ a subspace is affine (an "affine subspace").
- A {{< knowl id="convex-set" text="convex set" >}} need not be affine; affine sets are "flat," while convex sets may be curved.
