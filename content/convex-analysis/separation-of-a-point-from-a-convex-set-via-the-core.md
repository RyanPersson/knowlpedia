---
title: "Separating a Point from a Convex Set via the Core"
description: "If x0 is outside core(Ω) and core(Ω)≠∅, then Ω and {x0} are separable by a hyperplane."
---

Let $X$ be a real {{< knowl id="vector-space" text="vector space" >}}, let $x_0\in X$, and let $\Omega\subset X$ be {{< knowl id="convex-set" text="convex" >}}. Assume that {{< knowl id="algebraic-interior-core-and-linear-closure" text="core(Ω)" >}} is nonempty and $x_0\notin \operatorname{core}(\Omega)$.

**Theorem**: The sets $\Omega$ and $\{x_0\}$ can be {{< knowl id="separation-by-a-hyperplane" text="separated by a hyperplane" >}}. Equivalently, there exists a nonzero linear functional $f:X\to\mathbb{R}$ such that
$$
f(x)\le f(x_0)\quad\text{for all }x\in\Omega.
$$

**Context:**
This is a geometric form of {{< knowl id="hahn-banach-theorem-in-real-vector-spaces" text="Hahn–Banach" >}}. The proof uses the {{< knowl id="minkowski-function-gauge-of-a-set" text="Minkowski gauge" >}} of $\Omega$ (after translation) to build a sublinear domination bound and then applies Hahn–Banach.
