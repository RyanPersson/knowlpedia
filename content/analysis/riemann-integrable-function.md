---
title: "Riemann integrable function"
description: "A bounded function on [a,b] for which upper and lower sums can be made arbitrarily close."
---

A {{< knowl id="bounded-set" text="bounded" >}} function $f:[a,b]\to\mathbb{R}$ is **Riemann integrable** on $[a,b]$ if
$$\forall \varepsilon>0,\ \exists\ \text{a }{{< knowl id="partition-of-an-interval" text="partition" >}}\ P\ \text{of }[a,b]\ \text{such that}\ U(f,P)-L(f,P)<\varepsilon.$$

Equivalently, $f$ is Riemann integrable iff its **upper integral** $\inf_P U(f,P)$ (using {{< knowl id="upper-sum-riemann" text="upper sums" >}}) equals its **lower integral** $\sup_P L(f,P)$ (using {{< knowl id="lower-sum-riemann" text="lower sums" >}}), where the infimum/supremum are taken over all partitions $P$.

Riemann integrability is designed so that the area under the graph is well-defined and agrees with limits of {{< knowl id="riemann-sum" text="Riemann sums" >}}.

**Examples:**
- Every continuous function on $[a,b]$ is Riemann integrable.
- The function $\mathbf{1}_{\mathbb{Q}}$ on $[0,1]$ is not Riemann integrable (upper sums are always $1$, lower sums always $0$).
- Any monotone function on $[a,b]$ is Riemann integrable.
