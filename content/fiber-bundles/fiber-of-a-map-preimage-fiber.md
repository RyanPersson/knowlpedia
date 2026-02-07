---
title: "Fiber of a map"
description: "The preimage of a point under a map, viewed as a subset of the domain."
---

Let \(f : X \to Y\) be a map and let \(y \in Y\).

The **fiber of \(f\) over \(y\)** (also called the **preimage fiber**) is the subset
\[
f^{-1}(y)=\{x\in X \mid f(x)=y\}\subseteq X.
\]
When \(f : M \to N\) is a {{< knowl id="smooth-map" text="smooth map" >}} between {{< knowl id="smooth-manifold" text="smooth manifolds" >}}, the fiber \(f^{-1}(y)\) is a distinguished subset of \(M\) whose geometry depends strongly on whether \(y\) is a {{< knowl id="regular-value" text="regular value" >}}. In particular, if \(y\) is a regular value then \(f^{-1}(y)\) is a smooth submanifold of \(M\); if \(f\) is a {{< knowl id="smooth-submersion" text="smooth submersion" >}} then every \(y\in N\) is regular and all fibers are smooth submanifolds of the same dimension.

## Examples
1. **Projection fibers.** For the projection \(\pi_M : M\times F \to M\), the fiber over \(m\in M\) is
   \[
   \pi_M^{-1}(m)=\{m\}\times F.
   \]

2. **Level sets of a function.** For \(f:\mathbb{R}^2\to \mathbb{R}\) given by \(f(x,y)=x^2+y^2\), the fibers are the level sets:
   - if \(r>0\), then \(f^{-1}(r)=\{(x,y):x^2+y^2=r\}\), a circle of radius \(\sqrt r\);
   - if \(r=0\), then \(f^{-1}(0)=\{(0,0)\}\), a single point.

3. **A fiber with multiple components.** Let \(h:S^1\to \mathbb{R}\) be the height function \(h(\cos t,\sin t)=\sin t\). Then the fiber over \(0\) is
   \[
   h^{-1}(0)=\{(1,0),(-1,0)\},
   \]
   which has two connected components.
