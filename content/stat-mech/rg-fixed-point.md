---
title: "RG fixed point"
description: "A fixed point of a renormalization-group transformation and its linear stability data, which determine scaling and critical exponents."
---

## Definition (RG fixed point)
Let $R_b$ be a renormalization-group (RG) map implementing coarse-graining by a scale factor $b>1$ on a space of Hamiltonians or coupling parameters $g$ (e.g., $g=(K,h,\ldots)$). An **RG fixed point** is a point $g^\star$ such that
$$
R_b(g^\star)=g^\star \quad \text{for a given } b>1 \text{ (equivalently, for all } b \text{ in a consistent RG scheme).}
$$
A fixed point represents a scale-invariant effective description.

## Linearization and relevant/irrelevant directions
Linearize $R_b$ at $g^\star$:
$$
g' - g^\star = DR_b(g^\star)\,(g-g^\star) + \cdots
$$

Choose eigen-directions $u_i$ of the Jacobian with eigenvalues $\lambda_i(b)$:
$$
DR_b(g^\star)u_i=\lambda_i(b)\,u_i,\qquad \lambda_i(b)=b^{y_i}.
$$

The numbers $y_i$ are **scaling dimensions** (RG eigenvalues):
- **relevant** if $y_i>0$ (perturbations grow under coarse-graining),
- **irrelevant** if $y_i<0$ (perturbations die out),
- **marginal** if $y_i=0$ (need higher-order analysis).

A fixed point is **(infrared) stable** if it has no relevant directions except those forced by tuning parameters (e.g., temperature-like and field-like).

## Fixed points and critical behavior
Near a continuous phase transition, long-distance behavior is governed by a stable fixed point. If $y_t$ is the temperature-like relevant exponent, then the correlation-length exponent is
$$
\nu = \frac{1}{y_t},
$$
and other critical exponents follow from RG eigenvalues and scaling relations.

## Prerequisites / cross-links
- {{< knowl id="renormalization-group-transformation" text="renormalization-group (RG) transformation" >}}
- {{< knowl id="critical-exponent" text="critical exponents" >}}
- {{< knowl id="scaling-relation-exponents" text="scaling relations among exponents" >}}
- {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}
- {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions in Gibbs measures" >}}
