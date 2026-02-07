---
title: "Hölder inequality (finite sums)"
description: "∑|x_i y_i| is bounded by the product of ℓ^p and ℓ^q norms for conjugate exponents"
---

**Proposition (Hölder inequality for finite sums).**
Let $x_i,y_i\in\mathbb{R}$ for $i=1,\dots,m$. If $p>1$ and $q>1$ satisfy $1/p+1/q=1$, then
$$
\sum_{i=1}^m |x_i y_i|
\le
\left(\sum_{i=1}^m |x_i|^p\right)^{1/p}
\left(\sum_{i=1}^m |y_i|^q\right)^{1/q}.
$$

**Context.** This is the fundamental inequality behind duality of $\ell^p$ spaces and many estimates in analysis. It can be proved using the {{< knowl id="weighted-arithmeticgeometric-mean-inequality" text="weighted AM–GM inequality" >}} (or Young's inequality).

**Proof sketch.** Normalize so that $\sum |x_i|^p=1$ and $\sum |y_i|^q=1$ (otherwise scale). Apply weighted AM–GM with $\theta=1/p$ to $a=|x_i|^p$ and $b=|y_i|^q$ to get
$$
|x_i y_i|\le \frac{|x_i|^p}{p}+\frac{|y_i|^q}{q}.
$$

Sum over $i$ and undo the normalization.
