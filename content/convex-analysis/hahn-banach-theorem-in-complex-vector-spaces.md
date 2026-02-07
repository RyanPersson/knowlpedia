---
title: "Hahn–Banach Theorem (Complex Vector Spaces)"
description: "Complex linear functionals dominated by a seminorm extend to the whole space."
---

Let $X$ be a complex {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}}, let $Y\subset X$ be a {{< knowl id="linear-subspace" text="linear subspace" >}}, and let $p:X\to\mathbb{R}$ be a {{< knowl id="seminorm" text="seminorm" >}}.

**Theorem**: If $f:Y\to\mathbb{C}$ is complex-linear and satisfies
$$
|f(y)|\le p(y)\quad\text{for all }y\in Y,
$$

then there exists a complex-linear functional $F:X\to\mathbb{C}$ such that
- $F|_Y=f$, and
- $|F(x)|\le p(x)$ for all $x\in X$.

**Context:**
A standard route is to extend the real part via {{< knowl id="hahn-banach-extension-dominated-by-a-seminorm-real-case" text="the real seminorm Hahn–Banach theorem" >}} after viewing $X$ as a real vector space, and then reconstruct the complex functional.
