---
title: "Curvature"
description: "A measure of the failure of parallel transport to be path-independent, or equivalently, the non-integrability of horizontal distributions."
---

In differential geometry, **curvature** measures the failure of parallel transport to be path-independent, or equivalently, the extent to which a {{< knowl id="horizontal-distribution" text="horizontal distribution" >}} fails to be integrable.

The notion takes different but related forms depending on context:

1. **Principal bundles.** For a {{< knowl id="principal-connection" text="principal connection" >}} on a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}, the curvature is the {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form" >}} $\Omega \in \Omega^2(P;\mathfrak{g})$, defined by
   $$\Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega].$$

   In a local trivialization with gauge potential $A$, this pulls back to the {{< knowl id="local-curvature-2-form" text="local curvature" >}} $F = dA + \tfrac{1}{2}[A \wedge A]$.

2. **Vector bundles.** For a {{< knowl id="connection-on-a-vector-bundle" text="connection" >}} $\nabla$ on a {{< knowl id="vector-bundle" text="vector bundle" >}}, the curvature is the {{< knowl id="curvature-of-a-vector-bundle-connection" text="curvature endomorphism" >}} $R^\nabla$, an $\mathrm{End}(E)$-valued 2-form satisfying
   $$R^\nabla(X,Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X,Y]}s.$$

3. **Frame bundles.** The {{< knowl id="curvature-2-form-in-a-frame" text="curvature in a frame" >}} relates the principal bundle and vector bundle viewpoints: a connection on a vector bundle induces a principal connection on its frame bundle, and their curvatures correspond.

A connection is {{< knowl id="flat-principal-connection" text="flat" >}} when its curvature vanishes. Flatness is equivalent to the horizontal distribution being integrable (Frobenius) and to parallel transport depending only on the homotopy class of paths.

The curvature appears fundamentally in the {{< knowl id="chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection" text="Chern–Weil theorem" >}}, where invariant polynomials applied to the curvature yield {{< knowl id="characteristic-class" text="characteristic classes" >}}.
