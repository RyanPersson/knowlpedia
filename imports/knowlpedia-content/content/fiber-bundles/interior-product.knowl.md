+++
id = "fiber-bundles/interior-product"
title = "Interior product"
kind = "knowl"
summary = "The contraction of a differential form with a vector field, lowering degree by one."
aliases = ["interior-product", "Interior product"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/interior-product.md"
+++

Let $M$ be a smooth manifold, let $X$ be a [[fiber-bundles/vector-field|vector field]] on $M$, and let $\omega\in\Omega^k(M)$ be a [[fiber-bundles/differential-k-form|differential $k$-form]] with $k\ge 1$. The **interior product** (or **contraction**) of $\omega$ with $X$ is the $(k-1)$-form $\iota_X\omega$ defined by
\[
(\iota_X\omega)_p(v_1,\dots,v_{k-1}) = \omega_p\bigl(X_p,v_1,\dots,v_{k-1}\bigr) \qquad (p\in M).
\]
By convention, $\iota_X\omega=0$ if $k=0$.

The operator $\iota_X$ is $\mathbb{R}$-linear in $X$ and is a graded derivation of degree $-1$ on the exterior algebra:
\[
\iota_X(\alpha\wedge\beta)=(\iota_X\alpha)\wedge\beta+(-1)^{\deg\alpha}\alpha\wedge(\iota_X\beta).
\]
It is linked to the [[fiber-bundles/lie-derivative|Lie derivative]] by Cartan’s identity
\[
\mathcal{L}_X=\mathrm{d}\circ\iota_X+\iota_X\circ\mathrm{d},
\]
where $\mathrm{d}$ is the exterior derivative.

## Examples
1. **A basic contraction in $\mathbb{R}^2$.** With $\omega=\mathrm{d}x\wedge \mathrm{d}y$ and $X=\partial_x$, one has $\iota_X\omega=\mathrm{d}y$.
2. **Volume form in $\mathbb{R}^3$.** For $\omega=\mathrm{d}x\wedge\mathrm{d}y\wedge\mathrm{d}z$ and $X=\partial_z$, one gets $\iota_X\omega=\mathrm{d}x\wedge\mathrm{d}y$.
3. **Symplectic geometry viewpoint.** On a symplectic manifold $(M,\omega)$, the assignment $X\mapsto \iota_X\omega$ identifies vector fields with 1-forms when $\omega$ is nondegenerate; Hamiltonian vector fields are characterized by $\iota_X\omega=\mathrm{d}H$ for some function $H$.
