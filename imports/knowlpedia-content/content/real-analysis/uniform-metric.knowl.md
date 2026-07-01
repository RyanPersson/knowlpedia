+++
id = "real-analysis/uniform-metric"
title = "Uniform metric"
kind = "knowl"
summary = "A metric on bounded functions defined by the supremum of pointwise distances."
aliases = ["uniform-metric", "Uniform metric"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-metric.md"
+++

The **uniform metric** on a set of bounded real-valued functions on $X$ is defined by
\[
d_\infty(f,g)=\sup_{x\in X} |f(x)-g(x)|.
\]
Equivalently, $d_\infty(f,g)=\|f-g\|_\infty$ where $\|\cdot\|_\infty$ is the [[real-analysis/supremum-norm|supremum norm]].

This is a [[topology/metric|metric]] on the space of bounded functions, and convergence with respect to $d_\infty$ is exactly [[real-analysis/uniform-convergence|uniform convergence]]. Many compactness and approximation results for functions are phrased in terms of this metric on [[real-analysis/space-of-continuous-functions|continuous functions]].

**Examples:**
- On $[0,1]$, with $f(x)=x$ and $g(x)=0$, one has $d_\infty(f,g)=1$.
- On $[0,1]$, for $f_n(x)=x/n$, $d_\infty(f_n,0)=1/n\to 0$, so $f_n\to 0$ uniformly.
