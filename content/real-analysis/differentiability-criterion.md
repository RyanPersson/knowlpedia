---
title: "Differentiability criterion"
description: "Characterization of differentiability via a best linear approximation."
---

**Differentiability criterion:** Let $U\subseteq\mathbb R^k$ be an {{< knowl id="open-set" section="topology" text="open set" >}}, let $f:U\to\mathbb R^m$, and fix $a\in U$. The following are equivalent:

1. $f$ is {{< knowl id="differentiable-map" text="differentiable at" >}} $a$ (in the {{< knowl id="frechet-derivative" text="Fréchet" >}} sense).
2. There exists a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} $A:\mathbb R^k\to\mathbb R^m$ such that
   $$
   \lim_{h\to 0}\frac{\|f(a+h)-f(a)-Ah\|}{\|h\|}=0.
   $$

In this case, $A$ is unique and is denoted $Df(a)$.

This formulation says that differentiability is exactly the existence of a first-order linear approximation with an error term that is $o(\|h\|)$. In the one-dimensional case $k=m=1$, it is equivalent to the existence of the usual {{< knowl id="derivative" text="derivative" >}} at $a$.
