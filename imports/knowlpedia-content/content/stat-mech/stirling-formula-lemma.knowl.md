+++
id = "stat-mech/stirling-formula-lemma"
title = "Stirling's Formula"
kind = "knowl"
summary = "Asymptotic approximation for n! and log n!, used for entropy and large-N counting in statistical mechanics."
aliases = ["stirling-formula-lemma", "Stirling's Formula"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/stirling-formula-lemma.md"
+++

Stirling’s formula is a basic asymptotic tool for combinatorial and phase-space counting, and it is frequently used when connecting microscopic counting to [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann entropy]] and to information-theoretic quantities like [[probability/shannon-entropy|Shannon entropy]].

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
