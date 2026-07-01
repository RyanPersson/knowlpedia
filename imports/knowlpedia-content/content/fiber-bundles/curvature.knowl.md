+++
id = "fiber-bundles/curvature"
title = "Curvature"
kind = "knowl"
summary = "A measure of the failure of parallel transport to be path-independent, or equivalently, the non-integrability of horizontal distributions."
aliases = ["curvature"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/curvature.md"
+++

In differential geometry, **curvature** measures the failure of parallel transport to be path-independent, or equivalently, the extent to which a [[fiber-bundles/horizontal-distribution|horizontal distribution]] fails to be integrable.

The notion takes different but related forms depending on context:

1. **Principal bundles.** For a [[fiber-bundles/principal-connection|principal connection]] on a [[fiber-bundles/principal-g-bundle|principal G-bundle]], the curvature is the [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature 2-form]] $\Omega \in \Omega^2(P;\mathfrak{g})$, defined by
   $$\Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega].$$

   In a local trivialization with gauge potential $A$, this pulls back to the [[fiber-bundles/local-curvature-2-form|local curvature]] $F = dA + \tfrac{1}{2}[A \wedge A]$.

2. **Vector bundles.** For a [[fiber-bundles/connection-on-a-vector-bundle|connection]] $\nabla$ on a [[fiber-bundles/vector-bundle|vector bundle]], the curvature is the [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature endomorphism]] $R^\nabla$, an $\mathrm{End}(E)$-valued 2-form satisfying
   $$R^\nabla(X,Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X,Y]}s.$$

3. **Frame bundles.** The [[fiber-bundles/curvature-2-form-in-a-frame|curvature in a frame]] relates the principal bundle and vector bundle viewpoints: a connection on a vector bundle induces a principal connection on its frame bundle, and their curvatures correspond.

A connection is [[fiber-bundles/flat-principal-connection|flat]] when its curvature vanishes. Flatness is equivalent to the horizontal distribution being integrable (Frobenius) and to parallel transport depending only on the homotopy class of paths.

The curvature appears fundamentally in the [[fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection|Chern–Weil theorem]], where invariant polynomials applied to the curvature yield [[fiber-bundles/characteristic-class|characteristic classes]].
