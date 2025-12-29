---
title: "Isomorphism theorem for linear operators"
description: "The image of a linear map is isomorphic to the quotient by its kernel"
---

**Theorem (First isomorphism theorem; dimension formula).**
Let $T:X\to Y$ be a linear operator. Then
$$
\operatorname{im}T \cong X/\ker T.
$$
In particular, if dimensions are finite,
$$
\dim(\operatorname{im}T)=\operatorname{codim}(\ker T)=\dim(X/\ker T).
$$

**Context.** This theorem explains that a linear map is completely determined (up to isomorphism) by its {{< knowl id="image-and-kernel-linear-isomorphism" text="kernel and image" >}}. The quotient here is the {{< knowl id="quotient-vector-space-codimension" text="quotient vector space" >}} formed by collapsing $\ker T$ to $0$.

**Proof sketch.** Define $\widetilde{T}:X/\ker T\to \operatorname{im}T$ by $\widetilde{T}(x+\ker T)=T(x)$. This is well-defined because $x-x'\in\ker T$ implies $T(x)=T(x')$. It is linear, surjective by definition of $\operatorname{im}T$, and injective because $\widetilde{T}(x+\ker T)=0$ forces $x\in\ker T$.
