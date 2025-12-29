---
title: "Function (map)"
description: "An assignment that sends each input to a unique output."
---

A **function** (or **map**) from a {{< knowl id="set" text="set" >}} $X$ to a set $Y$ is a rule that assigns to each $x\in X$ exactly one element of $Y$, denoted $f(x)$. Formally, it is a subset $f\subseteq X\times Y$ (a {{< knowl id="cartesian-product" text="Cartesian product" >}}) such that:
- for every $x\in X$ there exists $y\in Y$ with $(x,y)\in f$, and
- if $(x,y_1)\in f$ and $(x,y_2)\in f$, then $y_1=y_2$.

One writes $f:X\to Y$ and calls $X$ the {{< knowl id="domain" text="domain" >}} and $Y$ the {{< knowl id="codomain" text="codomain" >}}. Functions are the primary objects of study in analysis: limits, {{< knowl id="continuity-at-a-point" text="continuity" >}}, {{< knowl id="differentiability-one-variable" text="differentiability" >}}, and integrability are properties of functions.

**Examples:**
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$.
- The projection $\pi_1:A\times B\to A$ given by $\pi_1(a,b)=a$.
- If $X=\varnothing$, there is exactly one function $f:\varnothing\to Y$ for any set $Y$ (the empty relation).
