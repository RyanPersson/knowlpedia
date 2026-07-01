+++
id = "linear-algebra/banach-space"
title = "Banach space"
kind = "knowl"
summary = "A complete normed vector space."
aliases = ["banach-space", "Banach space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/banach-space.md"
+++

A **Banach space** is a [[linear-algebra/normed-vector-space|normed vector space]] $(X,\|\cdot\|)$ such that every [[topology/cauchy-sequence|Cauchy sequence]] in $X$ converges (in the norm) to a point of $X$.

Equivalently, the metric $d(x,y)=\|x-y\|$ makes $X$ a [[topology/complete-metric-space|complete metric space]]. Completeness is a property of the metric induced by the [[linear-algebra/norm|norm]], and it is essential for many limit processes in analysis.

**Examples:**
- $\mathbb{R}^n$ with the [[linear-algebra/euclidean-norm|Euclidean norm]] (indeed, $\mathbb{R}^n$ is Banach for any norm).
- The space $C([0,1])$ of continuous real-valued functions on $[0,1]$ with the sup norm $\|f\|_\infty=\sup_{x\in[0,1]}|f(x)|$.
