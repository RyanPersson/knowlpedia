---
title: "Monotone convergence theorem"
description: "For an increasing sequence of nonnegative measurable functions, the integral of the limit equals the limit of the integrals."
---

**Monotone Convergence Theorem (Beppo Levi):** Let $(X,\Sigma,\mu)$ be a {{< knowl id="measure-space" text="measure space" >}} and let $(f_n)_{n\ge 1}$ be a {{< knowl id="sequence" section="shared-foundations" text="sequence" >}} of nonnegative {{< knowl id="measurable-function" text="measurable functions" >}} $f_n:X\to[0,\infty]$ such that $f_n(x)\le f_{n+1}(x)$ for all $x\in X$ and all $n$. Define $f(x)=\lim_{n\to\infty} f_n(x)$ (possibly $+\infty$). Then
\[
\int_X f\,d\mu \;=\; \lim_{n\to\infty}\int_X f_n\,d\mu,
\]
where the integrals are the (possibly infinite) {{< knowl id="lebesgue-integral-nonnegative" text="Lebesgue integrals of nonnegative functions" >}}.

If the monotone increase and the pointwise limit hold only {{< knowl id="almost-everywhere" text="almost everywhere" >}}, the conclusion is unchanged because modifying functions on a {{< knowl id="null-set" text="null set" >}} does not affect their integral (see {{< knowl id="ae-equality" text="a.e. equality" >}}). Along with {{< knowl id="fatous-lemma" text="Fatou's lemma" >}} and the {{< knowl id="dominated-convergence-theorem" text="dominated convergence theorem" >}}, it is one of the main tools for exchanging limits and {{< knowl id="lebesgue-integral" text="Lebesgue integration" >}}.
