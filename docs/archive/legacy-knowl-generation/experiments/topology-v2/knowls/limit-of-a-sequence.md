---
title: "Limit of a sequence"
description: "A point that a sequence in a metric space converges to"
---

A **limit of a sequence** $(x_n)$ in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a point $x\in X$ such that $(x_n)$ is a {{< knowl id="convergent-sequence" text="convergent sequence" >}} to $x$ (that is, $d(x_n,x)\to 0$).

In metric spaces, limits are unique: this is a consequence of the {{< knowl id="uniqueness-of-limits-hausdorff" section="topology-separation" text="uniqueness of limits in Hausdorff spaces" >}}. A sequence may still have {{< knowl id="limit-point-accumulation-point-cluster-point" section="topology-core" text="cluster points" >}} even when it has no limit.

**Examples:**
- In $\mathbb{R}$, the limit of $x_n=1/n$ is $0$.
- The sequence $x_n=(-1)^n$ has no limit in $\mathbb{R}$, but it has cluster points $1$ and $-1$.
