---
title: "Saddle-point method"
description: "Asymptotic evaluation of contour integrals and coefficient formulas using stationary points of the phase."
---

The saddle-point method (also called steepest descent in many contexts) is a complex-analytic technique for approximating integrals like
$$
I(n)=\int_{\Gamma} e^{n\phi(z)}\,\psi(z)\,dz
$$

for large $n$, where $\Gamma$ is a contour in the complex plane. It is closely related to {{< knowl id="laplaces-method" >}}, but uses complex contours chosen to pass through a *saddle point* (a stationary point of the phase).

## Saddle point and quadratic approximation
A point $z_0$ is a (simple) saddle point for $\phi$ if
$$
\phi'(z_0)=0
\quad\text{and}\quad
\phi''(z_0)\neq 0.
$$

Under standard analyticity and contour-deformation conditions, the leading contribution to $I(n)$ comes from a neighborhood of $z_0$. Expanding,
$$
\phi(z)=\phi(z_0)+\tfrac12\phi''(z_0)(z-z_0)^2+\cdots,
$$

and choosing $\Gamma$ along a direction of steepest descent, one typically gets a Gaussian-type leading term:
$$
I(n)\approx e^{n\phi(z_0)}\,\psi(z_0)\,\sqrt{\frac{2\pi}{n\,\phi''(z_0)}},
$$
with the square root interpreted using an appropriate branch and orientation of the contour.

## Coefficient asymptotics via Cauchy's integral formula
A very common application is estimating coefficients of an analytic generating function
$$
F(z)=\sum_{n\ge 0} a_n z^n.
$$
Cauchy's coefficient formula gives
$$
a_n=\frac{1}{2\pi i}\oint \frac{F(z)}{z^{n+1}}\,dz,
$$

so the integrand can be written as $\exp(n\phi(z))$ with
$$
\phi(z)=\frac{1}{n}\log F(z) - \log z
\quad\text{(up to harmless constants)}.
$$

The saddle-point condition for the dominant radius $r$ (often real and positive in applications with nonnegative coefficients) becomes
$$
\frac{d}{dz}\Bigl(\log F(z) - n\log z\Bigr)\Big|_{z=r}=0
\quad\Longleftrightarrow\quad
\frac{r F'(r)}{F(r)} = n.
$$

### A standard “real saddle” coefficient template
Define
$$
a(r)=\frac{rF'(r)}{F(r)},\qquad b(r)=r\,a'(r),
$$

and let $r=r_n$ solve $a(r)=n$. Under common regularity conditions (analyticity in a neighborhood of $r_n$, suitable decay away from the saddle, and a nondegenerate saddle), one gets the asymptotic form
$$
a_n \sim \frac{F(r_n)}{r_n^{\,n}\sqrt{2\pi\,b(r_n)}}.
$$
This is a workhorse for asymptotics in analytic combinatorics and partition-type problems.

## Relation to Laplace's method
If one can reduce a problem to an integral with a large parameter and a single dominant stationary point, the saddle-point method is the complex analogue of {{< knowl id="laplaces-method" >}}. Both rely on:
- identifying the dominant point (maximum/saddle),
- making a local quadratic approximation,
- evaluating a Gaussian integral.

## Practical notes
- Choosing the correct contour (often a steepest descent path) is part of the method; it ensures the contribution away from the saddle is negligible.
- Multiple saddle points can contribute; the leading asymptotic can be a sum of saddle contributions.
- Degenerate saddles (where $\phi''(z_0)=0$) require higher-order expansions and lead to different scaling.
