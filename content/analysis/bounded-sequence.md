---
title: "Bounded sequence"
description: "A sequence whose values stay within some fixed finite distance of a point."
---

Let $(X,d)$ be a metric space and let $(x_n)$ be a sequence in $X$. The sequence is **bounded** if its range $\{x_n:n\in\mathbb{N}\}$ is a bounded subset of $X$, i.e. if there exist $x_0\in X$ and $M\in[0,\infty)$ such that
$$\forall n\in\mathbb{N},\ d(x_n,x_0)\le M.$$

Boundedness is a minimal compactness-type hypothesis: in $\mathbb{R}^k$, bounded sequences have convergent subsequences (Bolzano–Weierstrass).

**Examples:**
- In $\mathbb{R}$, $x_n=\sin n$ is bounded (since $|\sin n|\le 1$).
- In $\mathbb{R}$, $x_n=n$ is not bounded.
- In a normed space, any convergent sequence is bounded.
