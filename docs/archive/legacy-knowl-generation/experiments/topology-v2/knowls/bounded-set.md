---
title: "Bounded set"
description: "A subset contained in some ball of finite radius in a metric space"
---

A **bounded set** in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a subset $A\subseteq X$ for which there exist a point $x_0\in X$ and a number $R>0$ such that $A\subseteq B_d(x_0,R)$ (equivalently, $d(x,x_0)\le R$ for all $x\in A$).

Boundedness is a metric notion (not purely topological): even {{< knowl id="equivalent-metrics" text="equivalent metrics" >}} can disagree about which subsets are bounded.

**Examples:**
- In $(\mathbb{R},|x-y|)$, the interval $[0,1]$ is bounded, while $\mathbb{Z}$ is not.
- In any metric space, every {{< knowl id="closed-ball" text="closed ball" >}} and {{< knowl id="open-ball" text="open ball" >}} of finite radius is bounded.
- In the discrete metric on a set $X$, every subset of $X$ is bounded.
