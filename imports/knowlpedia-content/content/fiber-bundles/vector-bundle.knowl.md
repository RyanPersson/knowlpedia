+++
id = "fiber-bundles/vector-bundle"
title = "Vector bundle"
kind = "knowl"
summary = "A smooth fiber bundle whose fibers are vector spaces and whose local trivializations are fiberwise linear."
aliases = ["vector-bundle", "Vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/vector-bundle.md"
+++

A **smooth real vector bundle** of rank \(k\) over a smooth manifold \(M\) is a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] \(\pi:E\to M\) together with the structure of a \(k\)-dimensional real vector space on each fiber \(E_x=\pi^{-1}(x)\), such that:

- the typical fiber is \(\mathbb{R}^k\), and
- there exists an open cover \(\{U_i\}\) of \(M\) with [[fiber-bundles/local-trivialization|local trivializations]] \(\Phi_i:\pi^{-1}(U_i)\to U_i\times\mathbb{R}^k\) whose restrictions \(\Phi_i|_{E_x}:E_x\to \mathbb{R}^k\) are linear isomorphisms for each \(x\in U_i\).

Equivalently, the [[fiber-bundles/transition-function|transition functions]] of such a bundle take values in \(\mathrm{GL}(k,\mathbb{R})\subset \mathrm{Diff}(\mathbb{R}^k)\). The [[fiber-bundles/tangent-bundle|tangent bundle]] and [[fiber-bundles/cotangent-bundle|cotangent bundle]] are the fundamental examples; many constructions in differential geometry (e.g. a [[fiber-bundles/connection-on-a-vector-bundle|connection on a vector bundle]]) are formulated for vector bundles.

## Examples
1. **Trivial rank-\(k\) bundle:** \(M\times \mathbb{R}^k\to M\) is a vector bundle with the obvious fiberwise linear structure.
2. **Tangent and cotangent bundles:** for an \(n\)-manifold \(M\), \(TM\to M\) and \(T^*M\to M\) are rank-\(n\) vector bundles.
3. **Möbius line bundle:** a nontrivial rank-1 real vector bundle over \(S^1\) with transition function \(-1\) on the overlap of two arcs.
