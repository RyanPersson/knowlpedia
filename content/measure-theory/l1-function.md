---
title: "L^1 function"
description: "A measurable function with finite integral of absolute value, modulo a.e. equality."
---

An **$L^1$ function** on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ is an equivalence class of {{< knowl id="measurable-function" text="measurable functions" >}} $f:X\to\mathbb R$ such that
\[
\int_X |f|\,d\mu<\infty,
\]
where two functions are identified if they satisfy {{< knowl id="ae-equality" text="a.e. equality" >}}.

Choosing any representative $f$ of the class, the quantity $\|f\|_1:=\int_X |f|\,d\mu$ is its {{< knowl id="lp-norm" text="Lp norm" >}} with $p=1$, and the set of all such classes is the {{< knowl id="lp-space" text="Lp space" >}} with $p=1$. An $L^1$ function is equivalently a {{< knowl id="lebesgue-integrable-function" text="Lebesgue integrable function" >}} once a representative is fixed.

**Examples:**
- On $\mathbb R$ with {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}, the function $f(x)=\frac{1}{1+x^2}$ represents an $L^1$ function.
- On the {{< knowl id="interval" section="real-analysis" text="interval" >}} $[0,1]$ with Lebesgue measure, the function $f(x)=x^{-1/2}$ represents an $L^1$ function.
