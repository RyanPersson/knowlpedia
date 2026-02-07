---
title: "Bounded sets and sequences"
description: "A set is bounded if it lies in some ball; a sequence is bounded if its range is bounded"
---

Let $(X,d)$ be a metric space and let $A\subset X$.

The set $A$ is **bounded** if there exist $a\in X$ and $r>0$ such that
$$
A\subset B(a;r),
$$

i.e., $A$ is contained in some {{< knowl id="open-and-closed-balls-in-a-metric-space" text="ball" >}}.

A sequence $(x_n)$ in $X$ is **bounded** if the set $\{x_n\mid n\in\mathbb{N}\}$ is bounded.

**Examples:**
- In $\mathbb{R}$, any interval $[a,b]$ is bounded; $\mathbb{R}$ itself is not bounded.
- In a normed space with metric $d(x,y)=\|x-y\|$, boundedness means $\|x_n\|\le M$ for some $M$ and all $n$.
- In the discrete metric, every subset is bounded (take radius $r=2$ around any point).
