---
title: "Operations Preserving Convexity"
description: "Nonnegative scaling, finite sums, and finite maxima preserve convexity"
---

**Operations Preserving Convexity**: Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $f,f_i:X\to\overline{\mathbb{R}}$ be {{< knowl id="convex-function-via-epigraph" text="convex functions" >}} for $i=1,\dots,m$. Then:

1. (**Nonnegative scaling**) For any $\lambda\ge 0$, the function $\lambda f$ is convex.
2. (**Finite sums**) The function $\sum_{i=1}^m f_i$ is convex.
3. (**Finite maxima**) The function $\max_{1\le i\le m} f_i$ is convex.

These closure properties are foundational for building new convex functions from old ones and are frequently combined with {{< knowl id="convexity-preserved-under-monotone-convex-composition" text="composition rules" >}} and {{< knowl id="supremum-of-convex-functions-is-convex" text="supremum constructions" >}}.

**Proof sketch (idea):** Use the Jensen inequality characterization from {{< knowl id="equivalent-characterizations-of-convex-functions" text="equivalent characterizations of convex functions" >}} and check it termwise for each operation.
