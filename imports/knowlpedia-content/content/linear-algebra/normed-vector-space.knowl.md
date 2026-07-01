+++
id = "linear-algebra/normed-vector-space"
title = "Normed vector space"
kind = "knowl"
summary = "A vector space together with a norm, giving a notion of distance and convergence."
aliases = ["normed-vector-space", "Normed vector space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/normed-vector-space.md"
+++

A **normed vector space** is a [[linear-algebra/vector-space|vector space]] $V$ equipped with a [[linear-algebra/norm|norm]] $\|\cdot\|$ on $V$.

The norm induces a [[topology/metric-space|metric space]] structure via $d(u,v)=\|u-v\|$, so notions from [[topology/topological-space|topology]] (like continuity and convergence) apply. If a normed vector space is complete with respect to this metric, it is a [[linear-algebra/banach-space|Banach space]]. Norms on linear maps are captured by the [[linear-algebra/operator-norm|operator norm]].

**Examples:**
- $(\mathbb{R}^n,\|\cdot\|_2)$ is a normed vector space.
- The space $C([0,1])$ of continuous real-valued functions on $[0,1]$ with the sup norm is a normed vector space.
- Any finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$ with any norm is a normed vector space.
