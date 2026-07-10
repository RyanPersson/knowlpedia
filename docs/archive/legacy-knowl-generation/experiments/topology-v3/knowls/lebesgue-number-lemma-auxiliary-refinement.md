---
title: "Auxiliary refinement for the Lebesgue number lemma"
description: "Refining an open cover by balls whose radii vary with the point"
---

**Auxiliary refinement lemma:** Let $(X,d)$ be a {{{< knowl id="metric-space" section="topology-metric" text="metric space" >}}}, let $K\subseteq X$, and let $\mathcal U$ be an {{{< knowl id="open-cover" text="open cover" >}}} of $K$. For each $x\in K$, choose a set $U_x\in\mathcal U$ with $x\in U_x$ and choose $r_x>0$ such that
\[
B(x,r_x)\cap K \subseteq U_x,
\]
where $B(x,r_x)$ is an {{{< knowl id="open-ball" section="topology-metric" text="open ball" >}}}. Then the family $\mathcal V=\{\,B(x,r_x)\cap K : x\in K\,\}$ is an open cover of $K$ that is a {{{< knowl id="refinement-of-an-open-cover" text="refinement" >}}} of $\mathcal U$.

In proofs of the {{{< knowl id="lebesgue-number-lemma" text="Lebesgue number lemma" >}}}, one combines this refinement with {{{< knowl id="compact-set" text="compactness" >}}} to extract a finite amount of local radius data and then takes a uniform minimum radius.
