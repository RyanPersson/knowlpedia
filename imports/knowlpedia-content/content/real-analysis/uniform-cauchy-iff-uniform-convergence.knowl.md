+++
id = "real-analysis/uniform-cauchy-iff-uniform-convergence"
title = "Uniform Cauchy criterion"
kind = "knowl"
summary = "For functions into a complete metric space, uniform convergence is equivalent to being uniformly Cauchy."
aliases = ["uniform-cauchy-iff-uniform-convergence", "Uniform Cauchy criterion"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-cauchy-iff-uniform-convergence.md"
+++

**Uniform Cauchy criterion:** Let $E$ be a set and let $(Y,\rho)$ be a [[topology/complete-metric-space|complete metric space]]. A sequence of functions $f_n:E\to Y$ converges [[real-analysis/uniform-convergence|uniformly]] on $E$ if and only if it is [[real-analysis/uniform-cauchy|uniformly Cauchy]], meaning: for every $\varepsilon>0$ there exists $N$ such that for all $m,n\ge N$ and all $x\in E$,
\[
\rho\bigl(f_n(x),f_m(x)\bigr)<\varepsilon.
\]

Equivalently, uniform convergence is exactly convergence in the [[real-analysis/uniform-metric|uniform metric]] (and, for bounded real-valued functions, in the [[real-analysis/supremum-norm|supremum norm]]).
