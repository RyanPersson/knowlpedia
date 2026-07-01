+++
id = "convex-analysis/completeness-of-rk"
title = "Completeness of R^k"
kind = "knowl"
summary = "Every Cauchy sequence in Euclidean space converges"
aliases = ["completeness-of-rk", "Completeness of R^k"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/completeness-of-rk.md"
+++

**Theorem (Completeness of $\mathbb{R}^k$).**
For every integer $k\ge 1$, the Euclidean space $\mathbb{R}^k$ equipped with its usual distance is a [[convex-analysis/complete-metric-space-complete-subset|complete metric space]].

**Context.** This is the finite-dimensional completeness statement used throughout analysis, optimization, and convex geometry.

**Proof sketch.** Let $(x_n)$ be a [[topology/cauchy-sequence|Cauchy sequence]] in $\mathbb{R}^k$, with $x_n=(x_n^{(1)},\dots,x_n^{(k)})$. The Cauchy property implies each coordinate sequence $(x_n^{(j)})$ is Cauchy in $\mathbb{R}$. Since $\mathbb{R}$ is complete, each coordinate converges to some $a^{(j)}\in\mathbb{R}$. Let $a=(a^{(1)},\dots,a^{(k)})$. One checks that $x_n\to a$ by estimating the distance between $x_n$ and $a$ in terms of coordinate differences, hence $(x_n)$ [[convex-analysis/convergence-of-a-sequence|converges]] in $\mathbb{R}^k$.

**Example.** The sequence $x_n=(1/n,1/n^2,\dots,1/n^k)$ is Cauchy and converges to $0\in\mathbb{R}^k$.
