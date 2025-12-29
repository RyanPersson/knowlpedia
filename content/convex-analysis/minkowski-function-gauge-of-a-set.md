---
title: "Minkowski Function (Gauge)"
description: "A set-generated sublinear functional pΩ(x)=inf{t≥0 : x∈tΩ}."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$ be nonempty.

The **Minkowski function** (or **Minkowski gauge**) of $\Omega$ is the function $p_\Omega:X\to[0,\infty]$ defined by
$$
p_\Omega(x):=\inf\{t\ge 0 \mid x\in t\Omega\}, \qquad x\in X,
$$
with the convention $\inf(\emptyset)=\infty$.

When $\Omega$ is {{< knowl id="balanced-and-absorbing-sets" text="absorbing" >}} and {{< knowl id="convex-set" text="convex" >}}, the gauge is real-valued and {{< knowl id="subadditive-positively-homogeneous-and-sublinear-functions" text="sublinear" >}}; its strict and non-strict sublevel sets recover {{< knowl id="algebraic-interior-core-and-linear-closure" text="core(Ω) and lin(Ω)" >}} via {{< knowl id="properties-of-the-minkowski-functional-of-a-convex-set" text="the main Minkowski gauge theorem" >}}.

**Examples:**
- If $\Omega$ is the closed unit ball of a {{< knowl id="norm-normed-vector-space" text="norm" >}}, then $p_\Omega(x)=\|x\|$.
- If $\Omega$ is a cone (e.g., $\mathbb{R}^n_+$), then $p_\Omega$ can take the value $\infty$ outside the cone unless $\Omega$ is absorbing.
