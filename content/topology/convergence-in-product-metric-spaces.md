---
title: "Convergence in product metric spaces"
description: "A sequence in X×Y converges iff each coordinate sequence converges"
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}. On the {{< knowl id="cartesian-product" section="shared-foundations" text="product" >}} $X\times Y$, define the metric
$
d_\infty\bigl((x,y),(x',y')\bigr)=\max\{d_X(x,x'),\,d_Y(y,y')\}.
$
(Any equivalent product metric, such as $d_1=d_X+d_Y$, yields the same notion of {{< knowl id="convergent-sequence" text="convergence" >}}.)

**Proposition (coordinatewise convergence)**: A sequence $((x_n,y_n))$ in $X\times Y$ converges to $(x,y)$ (with respect to $d_\infty$) if and only if
$
x_n\to x \text{ in } X \quad\text{and}\quad y_n\to y \text{ in } Y.
$
Likewise, $((x_n,y_n))$ is {{< knowl id="cauchy-sequence" text="Cauchy" >}} in $X\times Y$ iff $(x_n)$ is Cauchy in $X$ and $(y_n)$ is Cauchy in $Y$.

This proposition justifies treating product convergence as "simultaneous convergence of components."
