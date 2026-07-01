+++
id = "probability/gibbs-inequality-kl"
title = "Gibbs' inequality (nonnegativity of KL divergence)"
kind = "knowl"
summary = "The Kullback–Leibler divergence is always nonnegative, and it is zero only when the two distributions are identical."
aliases = ["gibbs-inequality-kl", "Gibbs' inequality (nonnegativity of KL divergence)"]
domains = ["probability"]
legacy_source_path = "probability/gibbs-inequality-kl.md"
+++

**Gibbs' inequality:** Let $P$ and $Q$ be [[probability/probability-measure|probability measures]] on a [[shared-foundations/set|set]] $\Omega$ equipped with a [[measure-theory/sigma-algebra|sigma-algebra]] $\mathcal F$, and let $D(P\|Q)$ denote their [[probability/relative-entropy-kl-divergence|Kullback–Leibler divergence]] (allowing the value $+\infty$). Then
$$
D(P\|Q)\ge 0,
$$

with equality if and only if $P=Q$ (as measures on $(\Omega,\mathcal F)$).

Equivalently, in the case $P\ll Q$, writing $f=\frac{dP}{dQ}$ for the Radon–Nikodym derivative (see [[probability/radon-nikodym-theorem|Radon–Nikodym theorem]]), one has
$$
D(P\|Q)=\int_\Omega f\log f\,dQ \ge 0,
$$

and equality holds if and only if $f=1$ $Q$-almost everywhere.

This is the basic reason relative entropy is a divergence: it is minimized uniquely at the matching law, even though it is not a metric. It is also a key input for inequalities relating KL to [[probability/total-variation-distance|total variation distance]], such as [[probability/pinsker-inequality|Pinsker's inequality]].
