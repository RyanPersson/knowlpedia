---
title: "Riemann integrable function"
description: "A bounded function on [a,b] for which upper and lower sums can be made arbitrarily close."
---

A bounded function $f:[a,b]\to\mathbb{R}$ is **Riemann integrable** on $[a,b]$ if
$$\forall \varepsilon>0,\ \exists\ \text{a partition }P\ \text{of }[a,b]\ \text{such that}\ U(f,P)-L(f,P)<\varepsilon.$$

Equivalently, $f$ is Riemann integrable iff its **upper integral** $\inf_P U(f,P)$ equals its **lower integral** $\sup_P L(f,P)$ (where the infimum/supremum are taken over all partitions $P$).

Riemann integrability is designed so that the area under the graph is well-defined and agrees with limits of Riemann sums.

**Examples:**
- Every continuous function on $[a,b]$ is Riemann integrable.
- The function $\mathbf{1}_{\mathbb{Q}}$ on $[0,1]$ is not Riemann integrable (upper sums are always $1$, lower sums always $0$).
- Any monotone function on $[a,b]$ is Riemann integrable.
