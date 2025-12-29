---
title: "Algebra of limits in normed spaces"
description: "Limits commute with addition and scalar multiplication"
---

**Proposition.**
Let $(X,\|\cdot\|)$ be a normed space.

1. If $x_n\to x$ and $y_n\to y$, then $x_n+y_n\to x+y$.
2. If $x_n\to x$ and $\alpha_n\to \alpha$ (in $\mathbb{R}$ or $\mathbb{C}$), then $\alpha_n x_n\to \alpha x$.

**Context.** These are the basic "limit laws" for sequences in normed linear settings.

**Proof sketch.**
1. By the triangle inequality,
$$
\|(x_n+y_n)-(x+y)\|\le \|x_n-x\|+\|y_n-y\|\to 0.
$$
2. Write
$$
\|\alpha_n x_n-\alpha x\|\le \|\alpha_n(x_n-x)\|+\|(\alpha_n-\alpha)x\|
=|\alpha_n|\,\|x_n-x\|+|\alpha_n-\alpha|\,\|x\|.
$$
Use that $(\alpha_n)$ is bounded and both factors tend to $0$.
