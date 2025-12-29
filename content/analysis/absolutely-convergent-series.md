---
title: "Absolutely convergent series"
description: "A series ∑ a_n such that ∑ |a_n| converges."
---

A {{< knowl id="series" text="series" >}} $\sum_{n=1}^\infty a_n$ with $a_n\in\mathbb{R}$ or $\mathbb{C}$ is **absolutely convergent** if the series of absolute values {{< knowl id="convergent-series" text="converges" >}}:
$$\sum_{n=1}^\infty |a_n| \ \text{converges}.$$

Absolute convergence is stronger than ordinary convergence and has powerful consequences: in $\mathbb{R}$ or $\mathbb{C}$ it implies convergence of $\sum a_n$ and stability under {{< knowl id="rearrangement-of-a-series" text="rearrangement" >}}.

**Examples:**
- $\sum_{n=1}^\infty \frac{1}{n^2}$ is absolutely convergent since $\sum |1/n^2|$ converges.
- $\sum_{n=1}^\infty (-1)^n\frac{1}{n^2}$ is absolutely convergent.
- The series $\sum_{n=1}^\infty (-1)^{n+1}\frac{1}{n}$ is not absolutely convergent (its absolute value series is harmonic and diverges).
