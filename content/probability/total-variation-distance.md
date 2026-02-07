---
title: "Total variation distance"
description: "A distance between two probability distributions defined by the largest possible difference they assign to the same event."
---

A **total variation distance** is the quantity
$$
d_{\mathrm{TV}}(P,Q)\;=\;\sup_{A\in\mathcal F}\,\bigl|P(A)-Q(A)\bigr|
$$

for two {{< knowl id="probability-measure" text="probability measures" >}} $P,Q$ on the same $(\Omega,\mathcal F)$, where the supremum ranges over all {{< knowl id="measurable-set" section="measure-theory" text="measurable sets" >}} $A$ (events). It measures the worst-case discrepancy in {{< knowl id="event-probability" text="event probabilities" >}} between $P$ and $Q$.

If $P$ and $Q$ are both absolutely continuous with respect to a common measure $\mu$ and have densities $p=\frac{dP}{d\mu}$ and $q=\frac{dQ}{d\mu}$ (via the Radon–Nikodym derivative from {{< knowl id="radon-nikodym-theorem" text="Radon–Nikodym theorem" >}}), then
$$
d_{\mathrm{TV}}(P,Q)=\frac12\int_\Omega |p-q|\,d\mu.
$$
Total variation is a strong notion of closeness of {{< knowl id="distribution-law" text="laws" >}}, and it can be controlled by {{< knowl id="relative-entropy-kl-divergence" text="KL divergence" >}} through {{< knowl id="pinsker-inequality" text="Pinsker's inequality" >}}.

**Examples:**
- If $P=\mathrm{Bernoulli}(p)$ and $Q=\mathrm{Bernoulli}(q)$ on $\{0,1\}$, then $d_{\mathrm{TV}}(P,Q)=|p-q|$.
- If $P$ and $Q$ have probability mass functions $(p_i)$ and $(q_i)$ on a finite set, then $d_{\mathrm{TV}}(P,Q)=\frac12\sum_i |p_i-q_i|$.
