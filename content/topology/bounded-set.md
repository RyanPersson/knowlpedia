---
title: "Bounded set"
description: "A subset of a metric space that lies inside some ball of finite radius."
---

A **bounded set** in a metric space $(X,d)$ is a subset $A\subseteq X$ for which there exist $x_0\in X$ and $R>0$ such that $A\subseteq B_d(x_0,R)$, where $B_d(x_0,R)$ is the {{< knowl id="open-ball" text="open ball" >}} of radius $R$ around $x_0$.

Equivalently, $A$ is bounded if and only if its {{< knowl id="diameter" text="diameter" >}} is finite. Boundedness is a basic size condition that appears in notions such as {{< knowl id="totally-bounded-set" text="total boundedness" >}}.

**Examples:**
- Any (open or closed) ball of finite radius is bounded.
- In $(\mathbb{R},|\cdot|)$, the interval $(0,1)$ is bounded, while $(0,\infty)$ is not.
