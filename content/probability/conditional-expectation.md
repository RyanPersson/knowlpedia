---
title: "Conditional expectation"
description: "Expectation of a random variable given partial information represented by a sigma-algebra"
---

A **conditional expectation** of a {{< knowl id="random-variable" text="random variable" >}} $X$ given a sub-{{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}} $\mathcal G \subseteq \mathcal F$ on a {{< knowl id="probability-space" text="probability space" >}} $(\Omega,\mathcal F,\mathbb P)$ is any $\mathcal G$-{{< knowl id="measurable-function" section="measure-theory" text="measurable function" >}} $Y$ such that $X$ is integrable (i.e. $\mathbb E[|X|]<\infty$) and
$$
\mathbb E\!\left[Y\,\mathbf 1_G\right] \;=\; \mathbb E\!\left[X\,\mathbf 1_G\right]\quad\text{for every }G\in\mathcal G.
$$

Any two versions of $Y$ that satisfy this are equal almost surely, and one writes $Y=\mathbb E[X\mid \mathcal G]$.

Conditional expectation refines {{< knowl id="expectation" text="expectation" >}} by restricting to information contained in $\mathcal G$; the special case $X=\mathbf 1_A$ yields {{< knowl id="conditional-probability" text="conditional probability" >}} of an event $A$ given $\mathcal G$.

**Examples:**
- If $\mathcal G=\{\varnothing,\Omega\}$ is the trivial $\sigma$-algebra, then $\mathbb E[X\mid\mathcal G]=\mathbb E[X]$ (a constant random variable).
- If $X$ is $\mathcal G$-measurable (in particular if $\mathcal G=\mathcal F$), then $\mathbb E[X\mid\mathcal G]=X$ almost surely.
- If $B\in\mathcal F$ with $\mathbb P(B)\in(0,1)$ and $\mathcal G=\sigma(B)=\{\varnothing,B,B^c,\Omega\}$, then
  $$
  \mathbb E[X\mid \mathcal G]
  \;=\;
  \frac{\mathbb E[X\,\mathbf 1_B]}{\mathbb P(B)}\,\mathbf 1_B
  \;+\;
  \frac{\mathbb E[X\,\mathbf 1_{B^c}]}{\mathbb P(B^c)}\,\mathbf 1_{B^c}.
  $$
