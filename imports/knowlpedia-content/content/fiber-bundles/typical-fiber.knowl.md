+++
id = "fiber-bundles/typical-fiber"
title = "Typical fiber"
kind = "knowl"
summary = "A chosen model manifold F that locally represents every fiber of a smooth fiber bundle."
aliases = ["typical-fiber", "Typical fiber"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/typical-fiber.md"
+++

Let \(\pi:E\to M\) be a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]]. A **typical fiber** (or **model fiber**) is a smooth manifold \(F\) for which there exists an open cover \(\{U_i\}\) of \(M\) and [[fiber-bundles/local-trivialization|local trivializations]] \(\Phi_i:\pi^{-1}(U_i)\to U_i\times F\).

In particular, for every \(x\in M\) the fiber \(E_x=\pi^{-1}(x)\) is [[fiber-bundles/diffeomorphism|diffeomorphic]] to \(F\), via restriction of \(\Phi_i\) to \(\{x\}\times F\). The typical fiber is not part of the bare fibered-manifold structure; it is extra data specifying *which* manifold is used as the local model. If both \(F\) and \(F'\) can serve as typical fibers for the same bundle, then \(F\) and \(F'\) must be diffeomorphic.

## Examples
1. **Tangent and cotangent bundles:** for an \(n\)-manifold \(M\), the typical fiber of \(TM\to M\) (and of \(T^*M\to M\)) is \(\mathbb{R}^n\).
2. **Principal bundles:** the typical fiber of a principal \(G\)-bundle \(P\to M\) is the [[fiber-bundles/lie-group|Lie group]] \(G\) itself.
3. **Sphere bundles:** the unit sphere bundle \(S(E)\to M\) of a rank-\(k\) vector bundle has typical fiber \(S^{k-1}\).
