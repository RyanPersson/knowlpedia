---
title: "Conditionally convergent series"
description: "A convergent series that fails to converge absolutely."
---

A series $\sum_{n=1}^\infty a_n$ (with $a_n\in\mathbb{R}$ or $\mathbb{C}$) is **conditionally convergent** if:
- $\sum_{n=1}^\infty a_n$ converges, and
- $\sum_{n=1}^\infty |a_n|$ diverges.

Conditional convergence is a specifically infinite-dimensional phenomenon: it is responsible for rearrangement pathology (e.g., Riemann rearrangement theorem in $\mathbb{R}$).

**Examples:**
- The alternating harmonic series $\sum_{n=1}^\infty (-1)^{n+1}\frac{1}{n}$ is conditionally convergent.
- $\sum_{n=1}^\infty \frac{(-1)^n}{\sqrt{n}}$ is conditionally convergent (by alternating series test, while $\sum 1/\sqrt{n}$ diverges).
- $\sum_{n=1}^\infty \frac{(-1)^n}{n^2}$ is not conditionally convergent because it is absolutely convergent.
