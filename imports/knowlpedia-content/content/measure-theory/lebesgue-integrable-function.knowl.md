+++
id = "measure-theory/lebesgue-integrable-function"
title = "Lebesgue integrable function"
kind = "knowl"
summary = "A measurable function whose absolute value has finite Lebesgue integral."
aliases = ["lebesgue-integrable-function", "Lebesgue integrable function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/lebesgue-integrable-function.md"
+++

A **Lebesgue integrable function** on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is a [[measure-theory/measurable-function|measurable function]] $f:X\to \mathbb R$ (or extended real-valued) such that
\[
\int_X |f|\,d\mu<\infty,
\]
where $|f|$ denotes the [[real-analysis/absolute-value|absolute value]] applied pointwise.

Lebesgue integrability ensures that the [[measure-theory/lebesgue-integral|Lebesgue integral]] of $f$ is a finite real number and depends only on the [[measure-theory/ae-equality|a.e. equality]] class of $f$. The collection of such functions (modulo a.e. equality) is the space of [[measure-theory/l1-function|L1 functions]].

**Examples:**
- On $\mathbb R$ with [[measure-theory/lebesgue-measure|Lebesgue measure]], the function $f(x)=\frac{1}{1+x^2}$ is Lebesgue integrable.
- If $E$ is a [[measure-theory/measurable-set|measurable set]] with $\mu(E)<\infty$, then the [[measure-theory/indicator-function|indicator function]] $\mathbf{1}_E$ is Lebesgue integrable.
