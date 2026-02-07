---
title: "Determinant nonvanishing implies local invertibility lemma"
description: "Invertibility is stable under small perturbations, with a quantitative bound on the inverse"
---

Let $A:\mathbb{R}^n\to\mathbb{R}^n$ be a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}}. Saying $\det A\neq 0$ is equivalent to saying $A$ is invertible.

**Stability of invertibility (Neumann series lemma)**: If $A$ is invertible and $B$ is another linear map such that
$
\|A^{-1}(B-A)\|<1,
$
then $B$ is invertible and
$
B^{-1}=\sum_{k=0}^\infty \bigl(-A^{-1}(B-A)\bigr)^k\,A^{-1}.
$
Moreover,
$
\|B^{-1}\|\le \frac{\|A^{-1}\|}{1-\|A^{-1}(B-A)\|}.
$
In particular, if $\|B-A\|\le \frac{1}{2\|A^{-1}\|}$ then $B$ is invertible and $\|B^{-1}\|\le 2\|A^{-1}\|$.

This lemma is a key linear-algebraic ingredient in the {{< knowl id="inverse-function-theorem-rk" text="inverse function theorem" >}}: once $Df(a)$ is invertible, $Df(x)$ remains invertible for all $x$ sufficiently close to $a$ (because $Df$ is {{< knowl id="continuity-on-a-set" text="continuous" >}}).
