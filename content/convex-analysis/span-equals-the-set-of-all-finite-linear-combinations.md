---
title: "Span equals finite linear combinations"
description: "The span of a set consists exactly of its finite linear combinations"
---

**Theorem.**
Let $X$ be a vector space and let $A\subset X$. Then the {{< knowl id="subspace-generated-by-a-set-span" text="span" >}} of $A$ is the set
$$
\left\{\sum_{i=1}^m \alpha_i x_i \ \middle|\ m\in\mathbb{N},\ \alpha_i\in K,\ x_i\in A\right\},
$$
i.e., all finite {{< knowl id="linear-combination" text="linear combinations" >}} of elements of $A$.

**Proof sketch.** Let $Y$ be the set of all such finite linear combinations. One checks that $Y$ is a linear subspace and contains $A$, hence $\operatorname{span}(A)\subset Y$ by minimality. Conversely, $\operatorname{span}(A)$ is a subspace containing $A$, so it is closed under forming finite linear combinations of elements of $A$, giving $Y\subset \operatorname{span}(A)$.
