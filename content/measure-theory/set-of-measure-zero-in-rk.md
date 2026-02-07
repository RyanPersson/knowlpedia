---
title: "Set of measure zero in ℝ^k"
description: "A set that can be covered by countably many rectangles (or balls) with arbitrarily small total volume."
---

A set $N\subseteq\mathbb{R}^k$ has **(Lebesgue) measure zero** (or is a **null set**) if for every $\varepsilon>0$ there exists a countable collection of $k$-dimensional rectangles (boxes) $\{R_n\}_{n=1}^\infty$ such that
$$N \subseteq \bigcup_{n=1}^\infty R_n
\quad\text{and}\quad
\sum_{n=1}^\infty \operatorname{vol}(R_n) < \varepsilon,$$

where for a rectangle $R=\prod_{j=1}^k [a_j,b_j]$ its volume is
$$\operatorname{vol}(R)=\prod_{j=1}^k (b_j-a_j).$$
(One may equivalently use open balls in place of rectangles; the definition is unchanged up to standard comparison arguments.)

Measure zero is a notion of "smallness" relevant to integration and differentiability. In Rudin-style analysis it is used in the Lebesgue criterion for Riemann integrability: a bounded function is Riemann integrable iff its discontinuity set has measure zero.

**Examples:**
- Any finite or countable subset of $\mathbb{R}^k$ has measure zero.
- Any $k$-dimensional hyperplane in $\mathbb{R}^{k+1}$ (e.g., $\mathbb{R}^k\times\{0\}$) has measure zero in $\mathbb{R}^{k+1}$.
- The Cantor set has measure zero in $\mathbb{R}$ (a standard construction result).
