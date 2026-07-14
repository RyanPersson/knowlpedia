---
title: "Auxiliary refinement by metric balls"
description: "Local ball containment produces an open-ball refinement of a cover"
---

**Auxiliary refinement (ball refinement):** Let $(X,d)$ be a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} and let $\mathcal U$ be an {{< knowl id="open-cover" text="open cover" >}} of a set $A\subseteq X$. Suppose that for each $x\in A$ we choose a set $U_x\in\mathcal U$ and a radius $r_x>0$ such that $B(x,r_x)\subseteq U_x$, where $B(x,r_x)$ is the {{< knowl id="open-ball" section="topology-metric" text="open ball" >}}. Then the family
\[
\mathcal V=\{B(x,r_x/2): x\in A\}
\]
is an open cover of $A$ and is a {{< knowl id="refinement-of-an-open-cover" text="refinement" >}} of $\mathcal U$.

This lemma packages the “shrink each neighborhood to a ball” step used in proofs such as the {{< knowl id="lebesgue-number-lemma" text="Lebesgue number lemma" >}}.
