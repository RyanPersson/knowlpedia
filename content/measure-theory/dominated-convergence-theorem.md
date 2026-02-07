---
title: "Dominated convergence theorem"
description: "If measurable functions converge almost everywhere and are dominated by an integrable function, then integrals and L1 norms converge."
---

**Dominated Convergence Theorem:** Let $(X,\Sigma,\mu)$ be a {{< knowl id="measure-space" text="measure space" >}} and let $(f_n)_{n\ge 1}$ be a sequence of {{< knowl id="measurable-function" text="measurable functions" >}} $f_n:X\to\mathbb{R}$ (or $\mathbb{C}$) such that $f_n\to f$ {{< knowl id="almost-everywhere" text="almost everywhere" >}}. Suppose there exists a nonnegative {{< knowl id="l1-function" text="L1 function" >}} $g$ such that $|f_n|\le g$ almost everywhere for all $n$. Then $f$ is {{< knowl id="lebesgue-integrable-function" text="Lebesgue integrable" >}} and
\[
\lim_{n\to\infty}\int_X f_n\,d\mu \;=\; \int_X f\,d\mu,
\qquad\text{and}\qquad
\lim_{n\to\infty}\int_X |f_n-f|\,d\mu \;=\; 0.
\]
In particular, $f_n\to f$ in $L^1(\mu)$ (see {{< knowl id="convergence-in-lp" text="convergence in Lp" >}} with $p=1$).

Together with {{< knowl id="monotone-convergence-theorem" text="monotone convergence" >}} and {{< knowl id="fatous-lemma" text="Fatou's lemma" >}}, this theorem is a core tool for interchanging limits with the {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}}. It is especially useful when pointwise convergence is available but uniform bounds are only in the integrable sense.
