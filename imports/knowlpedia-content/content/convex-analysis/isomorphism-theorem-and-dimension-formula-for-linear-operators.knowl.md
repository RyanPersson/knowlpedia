+++
id = "convex-analysis/isomorphism-theorem-and-dimension-formula-for-linear-operators"
title = "Isomorphism theorem for linear operators"
kind = "knowl"
summary = "The image of a linear map is isomorphic to the quotient by its kernel"
aliases = ["isomorphism-theorem-and-dimension-formula-for-linear-operators", "Isomorphism theorem for linear operators"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/isomorphism-theorem-and-dimension-formula-for-linear-operators.md"
+++

**Theorem (First isomorphism theorem; dimension formula).**
Let $T:X\to Y$ be a linear operator. Then
$$
\operatorname{im}T \cong X/\ker T.
$$
In particular, if dimensions are finite,
$$
\dim(\operatorname{im}T)=\operatorname{codim}(\ker T)=\dim(X/\ker T).
$$

**Context.** This theorem explains that a linear map is completely determined (up to isomorphism) by its [[convex-analysis/image-and-kernel-linear-isomorphism|kernel and image]]. The quotient here is the [[convex-analysis/quotient-vector-space-codimension|quotient vector space]] formed by collapsing $\ker T$ to $0$.

**Proof sketch.** Define $\widetilde{T}:X/\ker T\to \operatorname{im}T$ by $\widetilde{T}(x+\ker T)=T(x)$. This is well-defined because $x-x'\in\ker T$ implies $T(x)=T(x')$. It is linear, surjective by definition of $\operatorname{im}T$, and injective because $\widetilde{T}(x+\ker T)=0$ forces $x\in\ker T$.
