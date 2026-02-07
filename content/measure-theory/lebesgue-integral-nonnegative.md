---
title: "Lebesgue integral of a nonnegative function"
description: "Definition of the Lebesgue integral for nonnegative measurable functions."
---

A **Lebesgue integral of a nonnegative measurable function** on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ is defined as follows. For a nonnegative {{< knowl id="simple-function" text="simple function" >}} of the form
\[
s=\sum_{k=1}^n a_k\,\mathbf{1}_{E_k}
\quad (a_k\ge 0,\; E_k\in\Sigma),
\]
where $\mathbf{1}_{E_k}$ is the {{< knowl id="indicator-function" text="indicator function" >}} of $E_k$, define
\[
\int_X s\,d\mu := \sum_{k=1}^n a_k\,\mu(E_k).
\]
For a nonnegative {{< knowl id="measurable-function" text="measurable function" >}} $f:X\to[0,\infty]$, define
\[
\int_X f\,d\mu := \sup\left\{\int_X s\,d\mu : s \text{ is simple and } 0\le s\le f\right\}.
\]

This is the starting point for the {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}} of general real-valued functions, obtained by decomposing a function into its positive and negative parts.

**Examples:**
- If $E$ is a {{< knowl id="measurable-set" text="measurable set" >}}, then $\int_X \mathbf{1}_E\,d\mu=\mu(E)$.
- On $\mathbb R$ with {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}, if $f(x)=x$ for $x$ in the {{< knowl id="interval" section="real-analysis" text="interval" >}} $[0,1]$ and $f(x)=0$ otherwise, then $\int_{\mathbb R} f\,dx=\tfrac12$.
