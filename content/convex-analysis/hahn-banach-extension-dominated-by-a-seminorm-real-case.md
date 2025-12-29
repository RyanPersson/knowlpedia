---
title: "Hahn–Banach Extension Dominated by a Seminorm (Real Case)"
description: "A real linear functional bounded by a seminorm extends with the same bound."
---

Let $X$ be a real {{< knowl id="vector-space" text="vector space" >}}, let $Y\subset X$ be a {{< knowl id="linear-subspace" text="subspace" >}}, and let $p:X\to\mathbb{R}$ be a {{< knowl id="seminorm" text="seminorm" >}}.

**Theorem**: If $f:Y\to\mathbb{R}$ is linear and satisfies
$$
|f(y)|\le p(y)\quad\text{for all }y\in Y,
$$
then there exists a linear functional $F:X\to\mathbb{R}$ such that
- $F|_Y=f$, and
- $|F(x)|\le p(x)$ for all $x\in X$.

**Context:**
This is obtained from {{< knowl id="hahn-banach-theorem-in-real-vector-spaces" text="the sublinear Hahn–Banach theorem" >}} by applying it to both $f$ and $-f$ (or, equivalently, to the sublinear function $x\mapsto p(x)$ with symmetric domination).
