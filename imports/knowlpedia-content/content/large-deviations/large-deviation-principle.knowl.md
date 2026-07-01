+++
id = "large-deviations/large-deviation-principle"
title = "Large deviation principle"
kind = "knowl"
summary = "Asymptotic exponential bounds for probabilities of rare events at a given speed."
aliases = ["large-deviation-principle", "Large deviation principle"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/large-deviation-principle.md"
+++

A **large deviation principle (LDP)** for a sequence of probability measures $(\mu_n)_{n\ge 1}$ on a topological space $E$ (with its Borel $\sigma$-algebra) consists of a **speed** $(a_n)_{n\ge 1}$ with $a_n\to\infty$ and a [[large-deviations/rate-function|rate function]] $I:E\to[0,\infty]$ such that:
- for every closed set $F\subseteq E$,
  $$
  \limsup_{n\to\infty}\frac{1}{a_n}\log \mu_n(F)\le -\inf_{x\in F} I(x),
  $$

- for every open set $G\subseteq E$,
  $$
  \liminf_{n\to\infty}\frac{1}{a_n}\log \mu_n(G)\ge -\inf_{x\in G} I(x).
  $$

In many applications, $\mu_n$ is the [[probability/distribution-law|law]] of a sequence of [[probability/random-variable|random variables]] defined on a [[probability/probability-space|probability space]]. Additional structure such as a [[large-deviations/good-rate-function|good rate function]] or [[large-deviations/exponential-tightness|exponential tightness]] often ensures useful compactness properties and helps upgrade “local” bounds to a full LDP.

**Examples:**
- If $(X_i)_{i\ge1}$ is an [[probability/iid-sequence|i.i.d. sequence]] with suitable exponential moments, the empirical mean $\bar X_n=\frac1n\sum_{i=1}^n X_i$ satisfies an LDP at speed $a_n=n$; this is the content of [[large-deviations/cramers-theorem|Cramér's theorem]].
- The empirical measure of i.i.d. samples on a finite alphabet satisfies an LDP at speed $n$ with a relative-entropy-type rate; this is [[large-deviations/sanovs-theorem|Sanov's theorem]].
