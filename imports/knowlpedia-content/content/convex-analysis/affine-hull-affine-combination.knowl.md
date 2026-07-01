+++
id = "convex-analysis/affine-hull-affine-combination"
title = "Affine Hull and Affine Combination"
kind = "knowl"
summary = "The smallest affine set containing Ω, and linear combinations with coefficients summing to 1."
aliases = ["affine-hull-affine-combination", "Affine Hull and Affine Combination"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/affine-hull-affine-combination.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$.

The **affine hull** of $\Omega$ is the intersection of all [[convex-analysis/affine-set|affine sets]] containing $\Omega$:
$$
\operatorname{aff}(\Omega):=\bigcap\{C\subset X\mid C\text{ is affine and }\Omega\subset C\}.
$$

A vector $x\in X$ is an **affine combination** of $\omega_1,\dots,\omega_m\in X$ if
$$
x=\sum_{i=1}^m \lambda_i\omega_i
\quad\text{with}\quad
\sum_{i=1}^m \lambda_i=1.
$$

Affine combinations are the natural building blocks of affine sets, just as [[convex-analysis/convex-combination|convex combinations]] are for convex sets.

**Examples:**
- If $m=2$ and $\lambda_1=\lambda$, $\lambda_2=1-\lambda$, then $x=\lambda\omega_1+(1-\lambda)\omega_2$ parameterizes the line through $\omega_1,\omega_2$ as $\lambda$ varies over $\mathbb{R}$.
- In $\mathbb{R}^n$, $\operatorname{aff}(\Omega)$ is the smallest affine subspace containing $\Omega$.
