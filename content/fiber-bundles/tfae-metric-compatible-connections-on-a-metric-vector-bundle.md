---
title: "TFAE: Metric-compatible connections on a metric vector bundle"
description: "Equivalent conditions for a connection to preserve a fiber metric, including skew connection forms and isometric parallel transport."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $(E,\langle\cdot,\cdot\rangle)\to M$ be a real vector bundle of rank $r$ equipped with a smoothly varying inner product on fibers. Let $\nabla$ be a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} on $E$.

## Theorem (TFAE)

The following are equivalent:

1. **Metric preservation (Leibniz rule for the inner product).**  
   For all smooth vector fields $X$ on $M$ and smooth sections $s,t$ of $E$,
   \[
   X\langle s,t\rangle \;=\; \langle \nabla_X s, t\rangle \;+\; \langle s,\nabla_X t\rangle.
   \]

2. **Vanishing covariant derivative of the metric.**  
   The covariant derivative $\nabla\langle\cdot,\cdot\rangle$ (viewed as a tensor) is identically zero; equivalently, the connection induced by $\nabla$ on $E^*\otimes E^*$ annihilates the section representing the metric.

3. **Skew connection $1$-forms in orthonormal frames.**  
   On any open set $U$ with a local orthonormal frame $(e_1,\dots,e_r)$, the connection is described by matrix-valued $1$-forms $\omega=(\omega^i{}_j)$ via
   \[
   \nabla e_j = \sum_i \omega^i{}_j\, e_i,
   \]
   and metric compatibility holds if and only if $\omega$ takes values in $\mathfrak{so}(r)$, i.e. $\omega^i{}_j+\omega^j{}_i=0$.

4. **Isometric parallel transport.**  
   For every smooth curve $\gamma:[0,1]\to M$, the parallel transport map on fibers is an isometry:
   \[
   \langle \mathrm{PT}_\gamma(v), \mathrm{PT}_\gamma(w)\rangle \;=\; \langle v,w\rangle
   \quad\text{for all }v,w\in E_{\gamma(0)},
   \]
   where $\mathrm{PT}_\gamma$ denotes {{< knowl id="parallel-transport" text="parallel transport" >}} determined by $\nabla$.

5. **Orthonormal frame bundle reduction and holonomy containment.**  
   The bundle of orthonormal frames $O(E)\to M$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $\mathrm{O}(r)$, and $\nabla$ is metric-compatible if and only if it corresponds to a principal $\mathrm{O}(r)$-connection on $O(E)$. Equivalently, the {{< knowl id="holonomy-group" text="holonomy group" >}} of $\nabla$ is contained in $\mathrm{O}(r)$.

## Examples

1. **Levi-Civita connection on the tangent bundle.**  
   On a Riemannian manifold, the Levi-Civita connection on the {{< knowl id="tangent-bundle" text="tangent bundle" >}} is metric-compatible by definition; its parallel transport preserves the Riemannian inner product on tangent spaces.

2. **Trivial bundle with constant metric and trivial connection.**  
   If $E=M\times\mathbb{R}^r$ carries the standard dot product fiberwise and $\nabla$ is the componentwise derivative in the trivialization, then the connection forms are zero (hence skew), and parallel transport is the identity, so $\nabla$ is metric-compatible.

3. **Matrix-valued connection with values in so(r).**  
   On a trivial rank-$r$ bundle, define $\nabla=d+A$ where $A$ is an $\mathfrak{so}(r)$-valued $1$-form. Then the connection preserves the standard metric and has holonomy contained in $\mathrm{O}(r)$; nonzero curvature can occur even though metric compatibility holds.
