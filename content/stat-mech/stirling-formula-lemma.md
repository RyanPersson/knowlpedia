---
title: "Stirling's Formula"
description: "Asymptotic approximation for n! and log n!, used for entropy and large-N counting in statistical mechanics."
---

Stirling’s formula is a basic asymptotic tool for combinatorial and phase-space counting, and it is frequently used when connecting microscopic counting to {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="Boltzmann entropy" >}} and to information-theoretic quantities like {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}.

## Statement
As $n\to\infty$,
$$
n! \sim \sqrt{2\pi n}\,\Big(\frac{n}{e}\Big)^n.
$$
Equivalently,
$$
\log(n!) = n\log n - n + \tfrac12\log(2\pi n) + o(1).
$$

A common quantitative refinement is: for every integer $n\ge 1$ there exists $\theta_n\in(0,1)$ such that
$$
n! = \sqrt{2\pi n}\,\Big(\frac{n}{e}\Big)^n \exp\!\Big(\frac{\theta_n}{12n}\Big).
$$
In particular,
$$
\log(n!) = n\log n - n + \tfrac12\log(2\pi n) + O\!\Big(\frac{1}{n}\Big).
$$

## Key hypotheses and conclusions
**Hypotheses**
- $n\in\mathbb{N}$ and $n\to\infty$.

**Conclusions**
- Accurate leading-order and next-order asymptotics for $n!$ and $\log(n!)$.
- Enables asymptotics for multinomial coefficients; e.g. leading terms produce entropy-like functionals.

