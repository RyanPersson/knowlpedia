+++
id = "measure-theory/lebesgue-integral-nonnegative"
title = "Lebesgue integral of a nonnegative function"
kind = "knowl"
summary = "Definition of the Lebesgue integral for nonnegative measurable functions."
aliases = ["lebesgue-integral-nonnegative", "Lebesgue integral of a nonnegative function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/lebesgue-integral-nonnegative.md"
+++

A **Lebesgue integral of a nonnegative measurable function** on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is defined as follows. For a nonnegative [[measure-theory/simple-function|simple function]] of the form
\[
s=\sum_{k=1}^n a_k\,\mathbf{1}_{E_k}
\quad (a_k\ge 0,\; E_k\in\Sigma),
\]
where $\mathbf{1}_{E_k}$ is the [[measure-theory/indicator-function|indicator function]] of $E_k$, define
\[
\int_X s\,d\mu := \sum_{k=1}^n a_k\,\mu(E_k).
\]
For a nonnegative [[measure-theory/measurable-function|measurable function]] $f:X\to[0,\infty]$, define
\[
\int_X f\,d\mu := \sup\left\{\int_X s\,d\mu : s \text{ is simple and } 0\le s\le f\right\}.
\]

This is the starting point for the [[measure-theory/lebesgue-integral|Lebesgue integral]] of general real-valued functions, obtained by decomposing a function into its positive and negative parts.

**Examples:**
- If $E$ is a [[measure-theory/measurable-set|measurable set]], then $\int_X \mathbf{1}_E\,d\mu=\mu(E)$.
- On $\mathbb R$ with [[measure-theory/lebesgue-measure|Lebesgue measure]], if $f(x)=x$ for $x$ in the [[real-analysis/interval|interval]] $[0,1]$ and $f(x)=0$ otherwise, then $\int_{\mathbb R} f\,dx=\tfrac12$.
