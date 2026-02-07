---
title: "Subadditive, Positively Homogeneous, and Sublinear Functions"
description: "Key algebraic properties for gauges and Hahn–Banach domination."
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $p:X\to\mathbb{R}$.

- $p$ is **subadditive** if
  $$
  p(x+y)\le p(x)+p(y)\quad\text{for all }x,y\in X.
  $$

- $p$ is **positively homogeneous** if
  $$
  p(\lambda x)=\lambda p(x)\quad\text{for all }x\in X,\ \lambda>0.
  $$

- $p$ is **sublinear** if it is both subadditive and positively homogeneous.

Sublinear functions appear as domination bounds in {{< knowl id="hahn-banach-theorem-in-real-vector-spaces" text="the real Hahn–Banach theorem" >}}. A primary source of sublinear functions is the {{< knowl id="minkowski-function-gauge-of-a-set" text="Minkowski gauge" >}} of an {{< knowl id="balanced-and-absorbing-sets" text="absorbing" >}} {{< knowl id="convex-set" text="convex set" >}}.
