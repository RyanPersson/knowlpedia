---
title: "Properties of Affine Sets and Affine Hulls"
description: "Characterizations and closure properties of affine sets; representation of aff(Ω)."
---

Let $X$ be a {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$.

**Proposition** (key properties):
1. $\Omega$ is {{< knowl id="affine-set" text="affine" >}} iff it contains all {{< knowl id="affine-hull-affine-combination" text="affine combinations" >}} of its elements.
2. If $\Omega,\Omega_1,\Omega_2$ are affine, then $\Omega_1+\Omega_2$ and $\lambda\Omega$ (for any scalar $\lambda$) are affine.
3. If $B:X\to Y$ is an {{< knowl id="affine-mapping" text="affine mapping" >}} and $\Omega\subset X$ is affine, then $B(\Omega)\subset Y$ is affine; if $\Theta\subset Y$ is affine, then $B^{-1}(\Theta)$ is affine.
4. The affine hull $\operatorname{aff}(\Omega)$ is the smallest affine set containing $\Omega$ and admits the representation
   $$
   \operatorname{aff}(\Omega)=\left\{\sum_{i=1}^m \lambda_i\omega_i \ \middle|\ \sum_{i=1}^m\lambda_i=1,\ \omega_i\in\Omega,\ m\in\mathbb{N}\right\}.
   $$
5. A set $\Omega$ is a {{< knowl id="linear-subspace" text="linear subspace" >}} iff it is affine and contains $0$.

**Context:**
These results parallel the corresponding facts for {{< knowl id="convex-set" text="convex sets" >}} and {{< knowl id="convex-hull" text="convex hulls" >}}, with affine combinations replacing convex combinations.
