---
title: "Lebesgue integrable function"
description: "A measurable function whose absolute value has finite Lebesgue integral."
---

A **Lebesgue integrable function** on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ is a {{< knowl id="measurable-function" text="measurable function" >}} $f:X\to \mathbb R$ (or extended real-valued) such that
\[
\int_X |f|\,d\mu<\infty,
\]
where $|f|$ denotes the {{< knowl id="absolute-value" section="real-analysis" text="absolute value" >}} applied pointwise.

Lebesgue integrability ensures that the {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}} of $f$ is a finite real number and depends only on the {{< knowl id="ae-equality" text="a.e. equality" >}} class of $f$. The collection of such functions (modulo a.e. equality) is the space of {{< knowl id="l1-function" text="L1 functions" >}}.

**Examples:**
- On $\mathbb R$ with {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}, the function $f(x)=\frac{1}{1+x^2}$ is Lebesgue integrable.
- If $E$ is a {{< knowl id="measurable-set" text="measurable set" >}} with $\mu(E)<\infty$, then the {{< knowl id="indicator-function" text="indicator function" >}} $\mathbf{1}_E$ is Lebesgue integrable.
