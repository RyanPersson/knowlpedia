+++
id = "topology/convergence-in-product-metric-spaces"
title = "Convergence in product metric spaces"
kind = "knowl"
summary = "A sequence in X×Y converges iff each coordinate sequence converges"
aliases = ["convergence-in-product-metric-spaces", "Convergence in product metric spaces"]
domains = ["topology"]
legacy_source_path = "topology/convergence-in-product-metric-spaces.md"
+++

Let $(X,d_X)$ and $(Y,d_Y)$ be [[topology/metric-space|metric spaces]]. On the [[shared-foundations/cartesian-product|product]] $X\times Y$, define the metric
$
d_\infty\bigl((x,y),(x',y')\bigr)=\max\{d_X(x,x'),\,d_Y(y,y')\}.
$
(Any equivalent product metric, such as $d_1=d_X+d_Y$, yields the same notion of [[topology/convergent-sequence|convergence]].)

**Proposition (coordinatewise convergence)**: A sequence $((x_n,y_n))$ in $X\times Y$ converges to $(x,y)$ (with respect to $d_\infty$) if and only if
$
x_n\to x \text{ in } X \quad\text{and}\quad y_n\to y \text{ in } Y.
$
Likewise, $((x_n,y_n))$ is [[topology/cauchy-sequence|Cauchy]] in $X\times Y$ iff $(x_n)$ is Cauchy in $X$ and $(y_n)$ is Cauchy in $Y$.

This proposition justifies treating product convergence as "simultaneous convergence of components."
