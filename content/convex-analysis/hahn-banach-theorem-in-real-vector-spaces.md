---
title: "Hahn–Banach Theorem (Real Vector Spaces)"
description: "A linear functional dominated by a sublinear function extends to the whole space."
---

**Hahn–Banach (real version)**: Let $X$ be a real {{< knowl id="vector-space" text="vector space" >}}, let $Y\subset X$ be a {{< knowl id="linear-subspace" text="linear subspace" >}}, and let $p:X\to\mathbb{R}$ be {{< knowl id="subadditive-positively-homogeneous-and-sublinear-functions" text="sublinear" >}}.

If $f:Y\to\mathbb{R}$ is a {{< knowl id="linear-operator-linear-transformation" text="linear" >}} functional satisfying
$$
f(y)\le p(y)\quad\text{for all }y\in Y,
$$
then there exists a linear functional $F:X\to\mathbb{R}$ such that
- $F(y)=f(y)$ for all $y\in Y$, and
- $F(x)\le p(x)$ for all $x\in X$.

**Context:**
This extension theorem is the analytic backbone of convex separation results (e.g., {{< knowl id="separation-of-a-point-from-a-convex-set-via-the-core" text="geometric Hahn–Banach separation" >}}). In the notes, the proof uses Zorn's lemma to extend $f$ maximally and then shows the domain must be all of $X$.
