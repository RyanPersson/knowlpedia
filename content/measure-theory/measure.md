---
title: "Measure"
description: "A countably additive function on a sigma-algebra assigning sizes to sets."
---

A **measure** on a measurable space $(X,\Sigma)$ is a function $\mu:\Sigma\to[0,\infty]$ such that $\mu(\varnothing)=0$ and for every pairwise disjoint sequence $(A_n)_{n\ge 1}$ in $\Sigma$,
\[
\mu\!\left(\bigcup_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty \mu(A_n).
\]

A measure assigns “sizes” to {{< knowl id="measurable-set" text="measurable sets" >}} and turns $(X,\Sigma)$ into a {{< knowl id="measure-space" text="measure space" >}}. Sets of measure zero are {{< knowl id="null-set" text="null sets" >}}, and they control notions like {{< knowl id="almost-everywhere" text="almost everywhere" >}}.

**Examples:**
- The counting measure on $(X,\mathcal P(X))$ is given by $\mu(A)=|A|$ (possibly $+\infty$) for any subset $A\subseteq X$.
- {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}} on $\mathbb R^n$ is the standard measure extending ordinary length/area/volume.
- For a point $x_0\in X$, the Dirac measure $\delta_{x_0}$ is defined by $\delta_{x_0}(A)=1$ if $x_0\in A$ and $0$ otherwise.
