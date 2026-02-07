---
title: "Corollary of the M-test"
description: "If the sum of supremum norms is finite, then the corresponding series of functions converges uniformly."
---

**Corollary of the M-test:** Let $E$ be a set and let $f_n:E\to\mathbb{R}$ (or $\mathbb{C}$) be bounded functions. If the numerical series
\[
\sum_{n=1}^\infty \|f_n\|_\infty
\]
converges, where $\|f_n\|_\infty=\sup_{x\in E}|f_n(x)|$, then the series $\sum_{n=1}^\infty f_n$ converges {{< knowl id="uniform-convergence" text="uniformly" >}} on $E$ (and absolutely at each point of $E$).

This is the {{< knowl id="weierstrass-m-test" text="Weierstrass M-test" >}} applied with $M_n=\|f_n\|_\infty$, and it is a convenient criterion in settings involving the {{< knowl id="supremum-norm" text="supremum norm" >}}.
