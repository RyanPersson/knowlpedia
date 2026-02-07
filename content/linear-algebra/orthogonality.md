---
title: "Orthogonality"
description: "Condition that two vectors have inner product equal to zero."
---

**Orthogonality** is the relation in an {{< knowl id="inner-product-space" text="inner product space" >}} $(V,\langle\cdot,\cdot\rangle)$ defined by
\[
u\perp v \quad\Longleftrightarrow\quad \langle u,v\rangle=0.
\]

Orthogonality provides a geometric notion of “perpendicularity” that is compatible with the {{< knowl id="norm" text="norm" >}} coming from the {{< knowl id="inner-product" text="inner product" >}}. Fundamental inequalities such as the {{< knowl id="cauchy-schwarz-inequality" text="Cauchy–Schwarz inequality" >}} control how orthogonality interacts with lengths.

**Examples:**
- In $\mathbb{R}^2$ with the standard inner product, $(1,1)$ is orthogonal to $(1,-1)$.
- In $\mathbb{R}^n$, distinct standard basis vectors $e_i$ and $e_j$ are orthogonal when $i\ne j$.
- For periodic functions on $[0,2\pi]$ with $\langle f,g\rangle=\int_0^{2\pi} f(t)g(t)\,dt$, the functions $\sin t$ and $\cos t$ are orthogonal.
