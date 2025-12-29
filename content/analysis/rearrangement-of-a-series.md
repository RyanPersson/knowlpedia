---
title: "Rearrangement of a series"
description: "A permutation of the terms of a series, defined via a bijection of ℕ."
---

Let $\sum_{n=1}^\infty a_n$ be a series in $\mathbb{R}$ or $\mathbb{C}$. A **rearrangement** of the series is any series of the form
$$\sum_{n=1}^\infty a_{\sigma(n)},$$
where $\sigma:\mathbb{N}\to\mathbb{N}$ is a bijection (a permutation of the indices).

Rearrangements preserve sums for absolutely convergent series, but in $\mathbb{R}$ conditionally convergent series can have rearrangements with different sums or even divergence.

**Examples:**
- If $\sigma(n)=n$ for all $n$, the rearrangement is the original series.
- For $a_n=(-1)^{n+1}\frac{1}{n}$ (alternating harmonic), reordering terms can change the sum.
- Grouping terms is not the same as rearrangement unless it corresponds to a permutation of indices without changing term values.
