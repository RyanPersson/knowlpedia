---
title: "Normed vector space"
description: "A vector space together with a norm, giving a notion of distance and convergence."
---

A **normed vector space** is a {{< knowl id="vector-space" text="vector space" >}} $V$ equipped with a {{< knowl id="norm" text="norm" >}} $\|\cdot\|$ on $V$.

The norm induces a {{< knowl id="metric-space" section="topology" text="metric space" >}} structure via $d(u,v)=\|u-v\|$, so notions from {{< knowl id="topological-space" section="topology" text="topology" >}} (like continuity and convergence) apply. If a normed vector space is complete with respect to this metric, it is a {{< knowl id="banach-space" text="Banach space" >}}. Norms on linear maps are captured by the {{< knowl id="operator-norm" text="operator norm" >}}.

**Examples:**
- $(\mathbb{R}^n,\|\cdot\|_2)$ is a normed vector space.
- The space $C([0,1])$ of continuous real-valued functions on $[0,1]$ with the sup norm is a normed vector space.
- Any finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$ with any norm is a normed vector space.
