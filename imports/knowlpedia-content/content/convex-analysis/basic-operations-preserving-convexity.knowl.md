+++
id = "convex-analysis/basic-operations-preserving-convexity"
title = "Operations Preserving Convexity"
kind = "knowl"
summary = "Nonnegative scaling, finite sums, and finite maxima preserve convexity"
aliases = ["basic-operations-preserving-convexity", "Operations Preserving Convexity"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/basic-operations-preserving-convexity.md"
+++

**Operations Preserving Convexity**: Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $f,f_i:X\to\overline{\mathbb{R}}$ be [[convex-analysis/convex-function-via-epigraph|convex functions]] for $i=1,\dots,m$. Then:

1. (**Nonnegative scaling**) For any $\lambda\ge 0$, the function $\lambda f$ is convex.
2. (**Finite sums**) The function $\sum_{i=1}^m f_i$ is convex.
3. (**Finite maxima**) The function $\max_{1\le i\le m} f_i$ is convex.

These closure properties are foundational for building new convex functions from old ones and are frequently combined with [[convex-analysis/convexity-preserved-under-monotone-convex-composition|composition rules]] and [[convex-analysis/supremum-of-convex-functions-is-convex|supremum constructions]].

**Proof sketch (idea):** Use the Jensen inequality characterization from [[convex-analysis/equivalent-characterizations-of-convex-functions|equivalent characterizations of convex functions]] and check it termwise for each operation.
