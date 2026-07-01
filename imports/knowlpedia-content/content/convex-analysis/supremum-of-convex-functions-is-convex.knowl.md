+++
id = "convex-analysis/supremum-of-convex-functions-is-convex"
title = "Supremum of Convex Functions"
kind = "knowl"
summary = "The pointwise supremum of any family of convex functions is convex"
aliases = ["supremum-of-convex-functions-is-convex", "Supremum of Convex Functions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/supremum-of-convex-functions-is-convex.md"
+++

**Supremum of Convex Functions**: Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\{f_i:X\to\overline{\mathbb{R}}\}_{i\in I}$ be a family of [[convex-analysis/convex-function-via-epigraph|convex functions]] indexed by a nonempty set $I$. Define
$$
f(x):=\sup_{i\in I} f_i(x).
$$

Then $f$ is convex on $X$.

This extends the "finite maximum" case in [[convex-analysis/basic-operations-preserving-convexity|operations preserving convexity]] and is used heavily to construct convex envelopes and support functions.

**Proof sketch (idea):** For each $i$, Jensen gives
$f_i(\lambda x+(1-\lambda)y)\le \lambda f_i(x)+(1-\lambda)f_i(y)\le \lambda f(x)+(1-\lambda)f(y)$.
Taking $\sup_i$ on the left yields Jensen for $f$.
