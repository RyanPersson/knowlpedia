---
title: "Separation of a Point and a Subspace"
description: "If a point has positive distance to a subspace, a bounded functional separates them."
---

Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed space" >}}, let $Y\subset X$ be a {{< knowl id="linear-subspace" text="subspace" >}}, and let $x_0\in X$ satisfy
$$
d(x_0,Y):=\inf_{y\in Y}\|x_0-y\|=d>0.
$$

**Theorem (separating a point and a subspace)**: There exists a {{< knowl id="bounded-linear-functional-norm-of-a-functional" text="bounded linear functional" >}} $f:X\to\mathbb{K}$ such that
1. $f(y)=0$ for all $y\in Y$,
2. $\|f\|=1/d$, and
3. $f(x_0)=1$.

**Context:**
This is a geometric consequence of {{< knowl id="hahn-banach-theorem-in-normed-spaces" text="Hahn–Banach in normed spaces" >}}. It produces a continuous {{< knowl id="hyperplane" text="hyperplane" >}} through $Y$ that separates $x_0$ from $Y$.

**Proof sketch (idea):**
Define a linear functional on $Y\oplus \operatorname{span}\{x_0\}$ (see {{< knowl id="direct-sum-of-subspaces" text="direct sum" >}}) by mapping $y+\lambda x_0\mapsto \lambda$ and bound its norm using the distance assumption; then extend it by Hahn–Banach.
