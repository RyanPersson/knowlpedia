---
title: "Refinement lemma for upper and lower sums"
description: "Refining a partition decreases upper sums and increases lower sums."
---

**Refinement lemma:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be bounded. If $P'$ is a {{< knowl id="refinement-of-a-partition" text="refinement" >}} of a {{< knowl id="partition-of-an-interval" text="partition" >}} $P$, then
$$
U(f,P')\le U(f,P)
\quad\text{and}\quad
L(f,P')\ge L(f,P),
$$

where $U(f,P)$ and $L(f,P)$ denote the {{< knowl id="upper-sum" text="upper sum" >}} and {{< knowl id="lower-sum" text="lower sum" >}} of $f$ with respect to $P$.

This monotonicity under refinement underlies the definition of the {{< knowl id="riemann-integral" text="Riemann integral" >}} as the common value of the infimum of upper sums and the supremum of lower sums.
