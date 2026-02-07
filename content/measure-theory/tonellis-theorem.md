---
title: "Tonelli's theorem"
description: "Interchange of integrals for nonnegative measurable functions on a product measure space."
---

**Tonelli's theorem:** Let $(X,\Sigma,\mu)$ and $(Y,\mathcal T,\nu)$ be $\sigma$-finite measure spaces, and let $f:X\times Y\to[0,\infty]$ be $(\Sigma\otimes\mathcal T)$-measurable. Then the functions
\[
x\mapsto \int_Y f(x,y)\,d\nu(y)
\quad\text{and}\quad
y\mapsto \int_X f(x,y)\,d\mu(x)
\]
are measurable and
\[
\int_{X\times Y} f\,d(\mu\times\nu)
=
\int_X\Big(\int_Y f(x,y)\,d\nu(y)\Big)\,d\mu(x)
=
\int_Y\Big(\int_X f(x,y)\,d\mu(x)\Big)\,d\nu(y),
\]
where all three integrals are allowed to be $+\infty$.

Here $\mu\times\nu$ is the {{< knowl id="product-measure" text="product measure" >}} on the {{< knowl id="cartesian-product" section="shared-foundations" text="Cartesian product" >}}, and the integrals are {{< knowl id="lebesgue-integral" text="Lebesgue integrals" >}} of a nonnegative {{< knowl id="measurable-function" text="measurable function" >}}. Tonelli’s theorem is the nonnegative-function counterpart of {{< knowl id="fubinis-theorem" text="Fubini's theorem" >}}, which applies under an absolute integrability hypothesis.
