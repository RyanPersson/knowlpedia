+++
id = "measure-theory/lebesgue-integral"
title = "Lebesgue integral"
kind = "knowl"
summary = "Integral of a measurable function defined from its positive and negative parts."
aliases = ["lebesgue-integral", "Lebesgue integral"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/lebesgue-integral.md"
+++

A **Lebesgue integral** on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ assigns a value to a [[measure-theory/measurable-function|measurable function]] $f:X\to[-\infty,\infty]$ by reducing to the nonnegative case. Define the positive and negative parts
\[
f^+ := \max(f,0), \qquad f^- := \max(-f,0),
\]
so that $f=f^+-f^-$ and $f^+,f^-$ are nonnegative measurable functions. If at least one of $\int_X f^+\,d\mu$ or $\int_X f^-\,d\mu$ is finite, define
\[
\int_X f\,d\mu := \int_X f^+\,d\mu - \int_X f^-\,d\mu,
\]
where the integrals on the right are understood via [[measure-theory/lebesgue-integral-nonnegative|the nonnegative Lebesgue integral]]. If both $\int_X f^+\,d\mu$ and $\int_X f^-\,d\mu$ are $+\infty$, the Lebesgue integral of $f$ is left undefined.

When $f$ is [[measure-theory/lebesgue-integrable-function|Lebesgue integrable]], the integral is a finite real number. Moreover, if $f$ and $g$ satisfy [[measure-theory/ae-equality|a.e. equality]], then (whenever defined) their Lebesgue integrals agree.

**Examples:**
- On $\mathbb R$ with [[measure-theory/lebesgue-measure|Lebesgue measure]], the function $f(x)=x$ for $x\in[-1,1]$ and $f(x)=0$ otherwise satisfies $\int_{\mathbb R} f\,dx=0$.
- If $E$ is a [[measure-theory/measurable-set|measurable set]] with $\mu(E)<\infty$ and $c\in\mathbb R$, then $\int_X c\,\mathbf{1}_E\,d\mu=c\,\mu(E)$.
