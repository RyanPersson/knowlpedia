---
title: "Outer measure"
description: "A monotone, countably subadditive set function defined on all subsets."
---

An **outer measure** on a set $X$ is a function $\mu^*:\mathcal P(X)\to[0,\infty]$ such that $\mu^*(\varnothing)=0$, $\mu^*(A)\le \mu^*(B)$ whenever $A\subseteq B$, and for every sequence $(A_n)_{n\ge 1}$,
\[
\mu^*\!\left(\bigcup_{n=1}^\infty A_n\right)\le \sum_{n=1}^\infty \mu^*(A_n).
\]

Outer measures live on the full {{< knowl id="power-set" section="shared-foundations" text="power set" >}} and are used to define {{< knowl id="caratheodory-measurable-set" text="Carathéodory measurable sets" >}}. The {{< knowl id="caratheodory-construction" text="Carathéodory construction" >}} turns an outer measure into a genuine {{< knowl id="measure" text="measure" >}} on a sigma-algebra.

**Examples:**
- If $(X,\Sigma,\mu)$ is a {{< knowl id="measure-space" text="measure space" >}}, then $\mu^*(A)=\inf\{\mu(B): B\in\Sigma,\ A\subseteq B\}$ defines an outer measure on $X$.
- Lebesgue outer measure on $\mathbb R^n$ is an outer measure built from coverings by rectangles and is the starting point for {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}.
