+++
id = "real-analysis/space-of-continuous-functions"
title = "Space of continuous functions"
kind = "knowl"
summary = "The set of all real-valued continuous functions on a given topological space."
aliases = ["space-of-continuous-functions", "Space of continuous functions"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/space-of-continuous-functions.md"
+++

The **space of continuous functions** on a [[topology/topological-space|topological space]] $X$ is
\[
C(X)=\{f:X\to\mathbb{R} \mid f \text{ is continuous}\},
\]
where continuity is in the sense of a [[topology/continuous-map|continuous map]]. It is naturally a vector space under pointwise addition and scalar multiplication.

On domains where continuous functions are bounded (for example, on a compact interval), $C(X)$ can be equipped with the [[real-analysis/supremum-norm|supremum norm]] and the associated [[real-analysis/uniform-metric|uniform metric]], linking function-space topology to [[real-analysis/uniform-convergence|uniform convergence]]. Theorems such as [[real-analysis/arzela-ascoli-theorem|Arzelà–Ascoli]] and [[real-analysis/stone-weierstrass-theorem|Stone–Weierstrass]] are statements about subsets of $C(X)$.

**Examples:**
- On $[0,1]$, every [[real-analysis/polynomial|polynomial]] function belongs to $C([0,1])$.
- On $[-1,1]$, the function $f(x)=|x|$ belongs to $C([-1,1])$.
