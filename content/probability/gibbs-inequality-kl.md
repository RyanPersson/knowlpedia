---
title: "Gibbs' inequality (nonnegativity of KL divergence)"
description: "The Kullback–Leibler divergence is always nonnegative, and it is zero only when the two distributions are identical."
---

**Gibbs' inequality:** Let $P$ and $Q$ be {{< knowl id="probability-measure" text="probability measures" >}} on a {{< knowl id="set" section="shared-foundations" text="set" >}} $\Omega$ equipped with a {{< knowl id="sigma-algebra" section="measure-theory" text="sigma-algebra" >}} $\mathcal F$, and let $D(P\|Q)$ denote their {{< knowl id="relative-entropy-kl-divergence" text="Kullback–Leibler divergence" >}} (allowing the value $+\infty$). Then
$$
D(P\|Q)\ge 0,
$$

with equality if and only if $P=Q$ (as measures on $(\Omega,\mathcal F)$).

Equivalently, in the case $P\ll Q$, writing $f=\frac{dP}{dQ}$ for the Radon–Nikodym derivative (see {{< knowl id="radon-nikodym-theorem" text="Radon–Nikodym theorem" >}}), one has
$$
D(P\|Q)=\int_\Omega f\log f\,dQ \ge 0,
$$

and equality holds if and only if $f=1$ $Q$-almost everywhere.

This is the basic reason relative entropy is a divergence: it is minimized uniquely at the matching law, even though it is not a metric. It is also a key input for inequalities relating KL to {{< knowl id="total-variation-distance" text="total variation distance" >}}, such as {{< knowl id="pinsker-inequality" text="Pinsker's inequality" >}}.
