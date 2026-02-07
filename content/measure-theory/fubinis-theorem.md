---
title: "Fubini's theorem"
description: "Interchange of iterated integrals for absolutely integrable functions on a product measure space."
---

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

This theorem applies to {{< knowl id="l1-function" text="integrable functions" >}} on a {{< knowl id="product-measure" text="product measure" >}} space and justifies computing a {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}} by iterated integration. Compare {{< knowl id="tonellis-theorem" text="Tonelli's theorem" >}}, which gives the same conclusion for nonnegative functions without assuming $\int|f|<\infty$.
