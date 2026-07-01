+++
id = "measure-theory/l1-function"
title = "L^1 function"
kind = "knowl"
summary = "A measurable function with finite integral of absolute value, modulo a.e. equality."
aliases = ["l1-function", "L^1 function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/l1-function.md"
+++

An **$L^1$ function** on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is an equivalence class of [[measure-theory/measurable-function|measurable functions]] $f:X\to\mathbb R$ such that
\[
\int_X |f|\,d\mu<\infty,
\]
where two functions are identified if they satisfy [[measure-theory/ae-equality|a.e. equality]].

Choosing any representative $f$ of the class, the quantity $\|f\|_1:=\int_X |f|\,d\mu$ is its [[measure-theory/lp-norm|Lp norm]] with $p=1$, and the set of all such classes is the [[measure-theory/lp-space|Lp space]] with $p=1$. An $L^1$ function is equivalently a [[measure-theory/lebesgue-integrable-function|Lebesgue integrable function]] once a representative is fixed.

**Examples:**
- On $\mathbb R$ with [[measure-theory/lebesgue-measure|Lebesgue measure]], the function $f(x)=\frac{1}{1+x^2}$ represents an $L^1$ function.
- On the [[real-analysis/interval|interval]] $[0,1]$ with Lebesgue measure, the function $f(x)=x^{-1/2}$ represents an $L^1$ function.
