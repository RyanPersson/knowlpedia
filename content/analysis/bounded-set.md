---
title: "Bounded set"
description: "A set that stays within finite bounds, in an ordered set or in a metric space."
---

A subset $S$ is called **bounded** in two common contexts:

- In an ordered set $(X,\le)$, a subset $S\subseteq X$ is **bounded** if it is bounded above and bounded below, i.e. if there exist $\ell,u\in X$ such that
  $$\forall s\in S,\ \ell\le s\le u.$$

- In a metric space $(X,d)$, a subset $S\subseteq X$ is **bounded** if there exist $x_0\in X$ and $M\in[0,\infty)$ such that
  $$\forall x\in S,\ d(x,x_0)\le M.$$

In $\mathbb{R}$ with its usual metric $d(x,y)=|x-y|$, these two notions agree. In general metric spaces there is no order, so the metric definition is the relevant one.

**Examples:**
- In $\mathbb{R}$, $S=[-2,5]$ is bounded: $-2\le s\le 5$ for all $s\in S$.
- In $(\mathbb{R}^2,\|\cdot\|_2)$, the unit circle $S=\{x\in\mathbb{R}^2:\|x\|_2=1\}$ is bounded (take $x_0=0$, $M=1$).
- In $\mathbb{R}$, the set $\mathbb{N}$ is not bounded (neither above, nor in the metric sense).
