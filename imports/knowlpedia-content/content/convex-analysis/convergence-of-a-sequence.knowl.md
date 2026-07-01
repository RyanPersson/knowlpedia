+++
id = "convex-analysis/convergence-of-a-sequence"
title = "Convergence of a sequence in a metric space"
kind = "knowl"
summary = "A sequence converges if points eventually lie arbitrarily close to the limit"
aliases = ["convergence-of-a-sequence", "Convergence of a sequence in a metric space"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convergence-of-a-sequence.md"
+++

Let $(X,d)$ be a [[convex-analysis/metric-metric-space|metric space]]. A sequence $(x_n)$ in $X$ **converges** to a point $a\in X$ if
$$
(\forall \varepsilon>0)(\exists N\in\mathbb{N})(\forall n\ge N):\ d(x_n,a)<\varepsilon.
$$

We write $\lim_{n\to\infty}x_n=a$ or $x_n\to a$.

Convergence in metric spaces is the foundation for defining [[convex-analysis/closure-characterized-by-convergent-sequences|closure via sequences]] and for studying [[topology/cauchy-sequence|Cauchy sequences]].

**Examples:**
- In $\mathbb{R}$, $x_n=1/n$ converges to $0$.
- In any metric space, a constant sequence $x_n=x$ converges to $x$.
- In the discrete metric, $x_n\to a$ iff $x_n=a$ for all sufficiently large $n$.
