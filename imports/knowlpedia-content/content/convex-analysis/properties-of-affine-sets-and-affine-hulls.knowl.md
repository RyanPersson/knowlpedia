+++
id = "convex-analysis/properties-of-affine-sets-and-affine-hulls"
title = "Properties of Affine Sets and Affine Hulls"
kind = "knowl"
summary = "Characterizations and closure properties of affine sets; representation of aff(Ω)."
aliases = ["properties-of-affine-sets-and-affine-hulls", "Properties of Affine Sets and Affine Hulls"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/properties-of-affine-sets-and-affine-hulls.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$.

**Proposition** (key properties):
1. $\Omega$ is [[convex-analysis/affine-set|affine]] iff it contains all [[convex-analysis/affine-hull-affine-combination|affine combinations]] of its elements.
2. If $\Omega,\Omega_1,\Omega_2$ are affine, then $\Omega_1+\Omega_2$ and $\lambda\Omega$ (for any scalar $\lambda$) are affine.
3. If $B:X\to Y$ is an [[convex-analysis/affine-mapping|affine mapping]] and $\Omega\subset X$ is affine, then $B(\Omega)\subset Y$ is affine; if $\Theta\subset Y$ is affine, then $B^{-1}(\Theta)$ is affine.
4. The affine hull $\operatorname{aff}(\Omega)$ is the smallest affine set containing $\Omega$ and admits the representation
   $$
   \operatorname{aff}(\Omega)=\left\{\sum_{i=1}^m \lambda_i\omega_i \ \middle|\ \sum_{i=1}^m\lambda_i=1,\ \omega_i\in\Omega,\ m\in\mathbb{N}\right\}.
   $$

5. A set $\Omega$ is a [[convex-analysis/linear-subspace|linear subspace]] iff it is affine and contains $0$.

**Context:**
These results parallel the corresponding facts for [[convex-analysis/convex-set|convex sets]] and [[convex-analysis/convex-hull|convex hulls]], with affine combinations replacing convex combinations.
