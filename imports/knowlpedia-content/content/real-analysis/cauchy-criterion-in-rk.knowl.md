+++
id = "real-analysis/cauchy-criterion-in-rk"
title = "Cauchy Criterion in Rk"
kind = "knowl"
summary = "In Euclidean space, a sequence converges exactly when it is Cauchy."
aliases = ["cauchy-criterion-in-rk", "Cauchy Criterion in Rk"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/cauchy-criterion-in-rk.md"
+++

**Cauchy criterion in $\mathbb{R}^k$:** Let $(x_n)$ be a sequence in $\mathbb{R}^k$, with distance measured by the [[linear-algebra/euclidean-norm|Euclidean norm]] (equivalently, the Euclidean metric). Then $(x_n)$ converges in $\mathbb{R}^k$ if and only if it is a [[topology/cauchy-sequence|Cauchy sequence]], meaning: for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$,
$\|x_n-x_m\|<\varepsilon$.

This is the completeness of Euclidean space, i.e. that $\mathbb{R}^k$ is a [[topology/complete-metric-space|complete metric space]]. In one dimension it is one of the standard consequences of the [[real-analysis/completeness-axiom|completeness axiom]].
