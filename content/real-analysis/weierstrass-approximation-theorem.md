---
title: "Weierstrass approximation theorem"
description: "Every continuous function on a closed interval can be uniformly approximated by polynomials."
---

**Weierstrass approximation theorem:** Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="continuous-map" section="topology" text="continuous" >}}. For every $\varepsilon>0$ there exists a {{< knowl id="polynomial" text="polynomial" >}} $p$ such that
\[
\sup_{x\in[a,b]} |f(x)-p(x)| < \varepsilon.
\]
Equivalently, polynomials are dense in the {{< knowl id="space-of-continuous-functions" text="space of continuous functions" >}} on $[a,b]$ with respect to the {{< knowl id="supremum-norm" text="supremum norm" >}} (so $p_n\to f$ {{< knowl id="uniform-convergence" text="uniformly" >}} for some polynomial sequence $p_n$).

A far-reaching generalization is the {{< knowl id="stone-weierstrass-theorem" text="Stone–Weierstrass theorem" >}}, which replaces polynomials by more general subalgebras of continuous functions on compact spaces.
