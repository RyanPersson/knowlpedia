+++
id = "real-analysis/dinis-theorem"
title = "Dini's theorem"
kind = "knowl"
summary = "On a compact space, monotone pointwise convergence of continuous functions to a continuous limit is uniform."
aliases = ["dinis-theorem", "Dini's theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/dinis-theorem.md"
+++

**Dini's theorem:** Let $K$ be a compact [[topology/topological-space|topological space]] and let $f_n:K\to\mathbb{R}$ be [[topology/continuous-map|continuous]] for every $n$. Assume $(f_n)$ is monotone in $n$ (either $f_n(x)\le f_{n+1}(x)$ for all $x\in K$, or $f_n(x)\ge f_{n+1}(x)$ for all $x\in K$) and that $f_n\to f$ [[real-analysis/pointwise-convergence|pointwise]] on $K$, where $f$ is continuous. Then $f_n\to f$ [[real-analysis/uniform-convergence|uniformly]] on $K$.

This is a compactness-based upgrade from [[real-analysis/pointwise-convergence|pointwise convergence]] to [[real-analysis/uniform-convergence|uniform convergence]] under the additional hypothesis of monotonicity, as in a [[real-analysis/monotone-sequence-of-functions|monotone sequence of functions]].
