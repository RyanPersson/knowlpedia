---
title: "Bounded derivative implies uniform continuity"
description: "A differentiable function with bounded derivative is Lipschitz, hence uniformly continuous."
---

**Bounded derivative implies uniform continuity:** Let $I\subseteq\mathbb R$ be an {{< knowl id="interval" text="interval" >}} and let $f:I\to\mathbb R$ be {{< knowl id="differentiability-1d" text="differentiable" >}} on $I$. If there is a constant $M$ such that $|f'(t)|\le M$ for all $t\in I$, then for all $x,y\in I$,
$$
|f(x)-f(y)|\le M|x-y|.
$$

Consequently, $f$ is Lipschitz and in particular uniformly continuous on $I$.

This estimate is a direct application of the {{< knowl id="mean-value-theorem" text="mean value theorem" >}}. It is the one-dimensional special case of the {{< knowl id="mean-value-inequality" text="mean value inequality" >}} for differentiable maps.
