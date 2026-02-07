---
title: "Flat vector bundle connection"
description: "A vector bundle connection with zero curvature, admitting local parallel frames and homotopy-invariant transport."
---

Let $E\to M$ be a vector bundle with connection $\nabla$.

**Definition.** The connection $\nabla$ is flat if its {{< knowl id="curvature-of-a-vector-bundle-connection" text="curvature" >}} vanishes identically:
\[
R^\nabla = 0.
\]
Equivalently, in any local frame the curvature 2-form matrix is zero.

Flatness has two standard geometric consequences:
- On sufficiently small contractible open sets, there exist local frames of $\nabla$-parallel sections (frames $(e_i)$ with $\nabla e_i=0$), so locally the connection looks like the trivial connection in a suitable gauge.
- The associated {{< knowl id="parallel-transport" text="parallel transport" >}} along curves depends only on the homotopy class of the curve with fixed endpoints; loops therefore determine a representation of the fundamental group into the structure group, and the image is captured by the {{< knowl id="holonomy-group" text="holonomy group" >}}.

Viewed on the frame bundle, flatness corresponds to integrability of the induced horizontal distribution (compare {{< knowl id="integrable-horizontal-distribution" text="integrable horizontal distributions" >}}).

## Examples
1. **Trivial bundle with the trivial connection.** On $M\times\mathbb R^r$, the connection $\nabla=d$ has $R^\nabla=0$, so it is flat.
2. **Local systems from representations.** Given a representation $\rho:\pi_1(M)\to \mathrm{GL}(r,\mathbb R)$, one can form the associated flat vector bundle (a “local system”) whose parallel transport along loops realizes $\rho$.
3. **Flat but with nontrivial holonomy on the circle.** On $S^1$, let $E=S^1\times\mathbb R^r$ and define $\nabla = d + A\,d\theta$ with a constant matrix $A$. The curvature is zero (since $d\theta$ is closed and $A$ is constant), but parallel transport around the circle gives holonomy $\exp(2\pi A)$, which can be nontrivial.
