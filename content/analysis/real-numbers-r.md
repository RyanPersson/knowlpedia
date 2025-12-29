---
title: "Real numbers (as a complete ordered field)"
description: "A field with a compatible total order and the least upper bound property."
---

The **real numbers** $\mathbb{R}$ are characterized (up to a unique order-preserving field isomorphism) by the following structure:

- $(\mathbb{R},+,\cdot)$ is a **field**: $(\mathbb{R},+)$ is an abelian group with identity $0$, $(\mathbb{R}\setminus\{0\},\cdot)$ is an abelian group with identity $1$, and multiplication distributes over addition.

- $\le$ is a **total order** on $\mathbb{R}$ compatible with the field operations, meaning:
  - if $a\le b$ then $a+c\le b+c$ for all $c\in\mathbb{R}$,
  - if $0\le a$ and $0\le b$ then $0\le ab$.

- (**Completeness / least upper bound property**) Every nonempty subset $S\subseteq\mathbb{R}$ that is bounded above has a supremum in $\mathbb{R}$.

Completeness is what distinguishes $\mathbb{R}$ from $\mathbb{Q}$ and underlies many limit and convergence theorems in analysis.

**Examples:**
- The set $S=(0,1)$ is nonempty and bounded above, and $\sup S=1\in\mathbb{R}$.
- The set $S=\{x\in\mathbb{R}: x^2<2\}$ is bounded above and has $\sup S=\sqrt{2}\in\mathbb{R}$.
- In contrast, viewed as a subset of $\mathbb{Q}$, $\{q\in\mathbb{Q}: q^2<2\}$ has no supremum in $\mathbb{Q}$ (illustrating incompleteness of $\mathbb{Q}$).
