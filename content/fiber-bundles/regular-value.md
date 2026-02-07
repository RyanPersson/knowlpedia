---
title: "Regular value"
description: "A point in the target such that the differential is surjective along its fiber."
---

Let \(M\) and \(N\) be {{< knowl id="smooth-manifold" text="smooth manifolds" >}}, and let \(f:M\to N\) be a {{< knowl id="smooth-map" text="smooth map" >}}.

A point \(y\in N\) is called a **regular value** of \(f\) if for every \(x\in f^{-1}(y)\), the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential" >}}
\[
d f_x : T_x M \longrightarrow T_y N
\]
is surjective (with {{< knowl id="tangent-space-at-a-point" text="tangent spaces" >}} understood in the usual sense).

Equivalently: \(y\) is regular if \(f\) is a {{< knowl id="smooth-submersion" text="submersion" >}} at every point of the {{< knowl id="fiber-of-a-map-preimage-fiber" text="fiber" >}} \(f^{-1}(y)\). Points of \(N\) that are not regular values are called **critical values**.

## Regular value theorem
If \(y\in N\) is a regular value of \(f:M^m\to N^n\), then the fiber \(f^{-1}(y)\) is an embedded smooth submanifold of \(M\) of codimension \(n\) (and hence of dimension \(m-n\)). Moreover, for each \(x\in f^{-1}(y)\),
\[
T_x\bigl(f^{-1}(y)\bigr)=\ker(d f_x)\subseteq T_x M.
\]
This identifies the tangent space to the level set with the kernel of the differential at points on that level set.

## Examples
1. **Distance-squared on the plane.** For \(f:\mathbb{R}^2\to \mathbb{R}\), \(f(x,y)=x^2+y^2\), every \(r>0\) is a regular value: along \(f^{-1}(r)\) the gradient \((2x,2y)\) is never zero, so the differential is surjective. The value \(0\) is not regular, since the differential vanishes at \((0,0)\in f^{-1}(0)\).

2. **Height on the sphere.** Let \(f:S^2\to \mathbb{R}\) be the height function \(f(x,y,z)=z\). Then every \(c\in(-1,1)\) is a regular value and \(f^{-1}(c)\) is a circle (a “latitude”). The values \(c=\pm 1\) are not regular, because the fiber consists of a single pole where the differential cannot be surjective.

3. **A map that is everywhere regular.** If \(f:M\to N\) is a {{< knowl id="smooth-submersion" text="smooth submersion" >}}, then every \(y\in N\) is a regular value. For instance, for the projection \(\pi_M:M\times F\to M\), all fibers \(\pi_M^{-1}(m)=\{m\}\times F\) are smooth submanifolds.
