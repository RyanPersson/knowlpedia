---
title: "Dual vector bundle"
description: "The vector bundle whose fiber over each point is the dual space of the original fiber."
---

Let $\pi:E\to M$ be a smooth vector bundle (real or complex) over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. The **dual vector bundle** of $E$ is the vector bundle
\[
\pi^*:E^*\to M
\]
defined fiberwise by
\[
E_x^* := \mathrm{Hom}_{\mathbb F}(E_x,\mathbb F),
\]
with smooth structure characterized by the property that any local trivialization $E|_U\cong U\times \mathbb F^r$ induces a local trivialization
\[
E^*|_U \cong U\times (\mathbb F^r)^*
\]
via fiberwise duality.

Equivalently, if $(e_1,\dots,e_r)$ is a local frame on $U$, then there is a uniquely determined dual local frame $(e^1,\dots,e^r)$ of $E^*|_U$ such that $e^i(e_j)=\delta^i_j$ pointwise; changes of frame are governed by inverse transpose (real case) or inverse conjugate transpose (Hermitian case).

A {{< knowl id="vector-bundle-morphism" text="vector bundle morphism" >}} $\Phi:E\to F$ over $\mathrm{id}_M$ induces a dual morphism $\Phi^*:F^*\to E^*$ over $\mathrm{id}_M$ by precomposition on each fiber.

## Examples
1. **Cotangent bundle.** The {{< knowl id="cotangent-bundle" text="cotangent bundle" >}} $T^*M$ is the dual vector bundle of the {{< knowl id="tangent-bundle" text="tangent bundle" >}} $TM$.

2. **Dual of a trivial bundle.** $(M\times \mathbb F^r)^*\cong M\times (\mathbb F^r)^*$ canonically.

3. **Dual line bundle.** If $L\to M$ is a real or complex line bundle, then $L^*$ is again a line bundle; fiberwise, it consists of linear functionals on $L_x$. The tensor product $L\otimes L^*$ has a canonical nowhere-zero section given by evaluation, so it is canonically trivial.
