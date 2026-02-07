---
title: "Probability measure"
description: "A measure on a sigma-algebra with total mass 1."
---

A **probability measure** is a function $\mathbb{P}:\mathcal{F}\to[0,1]$ defined on a {{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}} $\mathcal{F}$ of subsets of a {{< knowl id="set" section="shared-foundations" text="set" >}} $\Omega$ such that $\mathbb{P}(\varnothing)=0$, $\mathbb{P}\!\left(\bigcup_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty \mathbb{P}(A_n)$ for every pairwise disjoint sequence $(A_n)_{n\ge1}\subseteq\mathcal{F}$, and $\mathbb{P}(\Omega)=1$.

A probability measure is a special case of a {{< knowl id="measure" section="measure-theory" text="measure" >}} and is the key ingredient in a {{< knowl id="probability-space" text="probability space" >}}; it assigns {{< knowl id="event-probability" text="probabilities to events" >}} (measurable sets).

**Examples:**
- If $\Omega=\{1,2,\dots,n\}$ and $\mathcal{F}=2^\Omega$, the uniform probability measure is $\mathbb{P}(A)=|A|/n$.
- If $\Omega=[0,1]$, $\mathcal{F}$ is the Borel $\sigma$-algebra, and $\lambda$ is {{< knowl id="lebesgue-measure" section="measure-theory" text="Lebesgue measure" >}}, then $\mathbb{P}(A)=\lambda(A)$ defines the uniform probability measure on $[0,1]$.
