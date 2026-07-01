+++
id = "convex-analysis/convergent-sequences-are-cauchy"
title = "Convergent sequences are Cauchy"
kind = "knowl"
summary = "Convergence implies the Cauchy property in any metric space"
aliases = ["convergent-sequences-are-cauchy", "Convergent sequences are Cauchy"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convergent-sequences-are-cauchy.md"
+++

**Proposition.**
If $(x_n)$ is a convergent sequence in a metric space, then it is a [[topology/cauchy-sequence|Cauchy sequence]].

**Proof sketch.** If $x_n\to a$, then for $\varepsilon>0$ choose $N$ such that $d(x_n,a)<\varepsilon/2$ for all $n\ge N$. For $m,n\ge N$,
$$
d(x_m,x_n)\le d(x_m,a)+d(a,x_n)<\varepsilon/2+\varepsilon/2=\varepsilon
$$
by the triangle inequality.
