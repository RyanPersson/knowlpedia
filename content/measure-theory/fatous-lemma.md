---
title: "Fatou's lemma"
description: "For nonnegative measurable functions, the integral of the liminf is bounded by the liminf of the integrals."
---

**Fatou's lemma:** Let $(X,\Sigma,\mu)$ be a {{< knowl id="measure-space" text="measure space" >}} and let $(f_n)_{n\ge 1}$ be a sequence of nonnegative {{< knowl id="measurable-function" text="measurable functions" >}} $f_n:X\to[0,\infty]$. Then
\[
\int_X \Bigl(\liminf_{n\to\infty} f_n\Bigr)\,d\mu \;\le\; \liminf_{n\to\infty}\int_X f_n\,d\mu,
\]
where $\liminf_{n\to\infty} f_n$ is taken pointwise (and may take the value $+\infty$).

Fatou's lemma expresses a fundamental lower-semicontinuity property of the {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}} and is closely related to the {{< knowl id="monotone-convergence-theorem" text="monotone convergence theorem" >}}. It is a standard ingredient in the {{< knowl id="dominated-convergence-theorem" text="dominated convergence theorem" >}} and many other limit arguments in measure theory.
