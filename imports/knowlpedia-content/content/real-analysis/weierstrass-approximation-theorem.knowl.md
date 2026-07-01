+++
id = "real-analysis/weierstrass-approximation-theorem"
title = "Weierstrass approximation theorem"
kind = "knowl"
summary = "Every continuous function on a closed interval can be uniformly approximated by polynomials."
aliases = ["weierstrass-approximation-theorem", "Weierstrass approximation theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/weierstrass-approximation-theorem.md"
+++

**Weierstrass approximation theorem:** Let $f:[a,b]\to\mathbb{R}$ be [[topology/continuous-map|continuous]]. For every $\varepsilon>0$ there exists a [[real-analysis/polynomial|polynomial]] $p$ such that
\[
\sup_{x\in[a,b]} |f(x)-p(x)| < \varepsilon.
\]
Equivalently, polynomials are dense in the [[real-analysis/space-of-continuous-functions|space of continuous functions]] on $[a,b]$ with respect to the [[real-analysis/supremum-norm|supremum norm]] (so $p_n\to f$ [[real-analysis/uniform-convergence|uniformly]] for some polynomial sequence $p_n$).

A far-reaching generalization is the [[real-analysis/stone-weierstrass-theorem|Stone–Weierstrass theorem]], which replaces polynomials by more general subalgebras of continuous functions on compact spaces.
