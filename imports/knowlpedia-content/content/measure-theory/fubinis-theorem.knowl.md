+++
id = "measure-theory/fubinis-theorem"
title = "Fubini's theorem"
kind = "knowl"
summary = "Interchange of iterated integrals for absolutely integrable functions on a product measure space."
aliases = ["fubinis-theorem", "Fubini's theorem"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/fubinis-theorem.md"
+++

**Fubini's theorem:** Let $(X,\Sigma,\mu)$ and $(Y,\mathcal T,\nu)$ be $\sigma$-finite measure spaces, and let $f:X\times Y\to\mathbb R$ be $(\Sigma\otimes\mathcal T)$-measurable. If
\[
\int_{X\times Y} |f|\,d(\mu\times\nu)<\infty,
\]
then for $\mu$-almost every $x\in X$ the section $y\mapsto f(x,y)$ is $\nu$-integrable, and for $\nu$-almost every $y\in Y$ the section $x\mapsto f(x,y)$ is $\mu$-integrable. Moreover, the iterated integrals exist as finite numbers and satisfy
\[
\int_{X\times Y} f\,d(\mu\times\nu)
=
\int_X\Big(\int_Y f(x,y)\,d\nu(y)\Big)\,d\mu(x)
=
\int_Y\Big(\int_X f(x,y)\,d\mu(x)\Big)\,d\nu(y).
\]

This theorem applies to [[measure-theory/l1-function|integrable functions]] on a [[measure-theory/product-measure|product measure]] space and justifies computing a [[measure-theory/lebesgue-integral|Lebesgue integral]] by iterated integration. Compare [[measure-theory/tonellis-theorem|Tonelli's theorem]], which gives the same conclusion for nonnegative functions without assuming $\int|f|<\infty$.
