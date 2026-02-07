---
title: "Vector bundle"
description: "A smooth fiber bundle whose fibers are vector spaces and whose local trivializations are fiberwise linear."
---

A **smooth real vector bundle** of rank \(k\) over a smooth manifold \(M\) is a {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}} \(\pi:E\to M\) together with the structure of a \(k\)-dimensional real vector space on each fiber \(E_x=\pi^{-1}(x)\), such that:

- the typical fiber is \(\mathbb{R}^k\), and
- there exists an open cover \(\{U_i\}\) of \(M\) with {{< knowl id="local-trivialization" text="local trivializations" >}} \(\Phi_i:\pi^{-1}(U_i)\to U_i\times\mathbb{R}^k\) whose restrictions \(\Phi_i|_{E_x}:E_x\to \mathbb{R}^k\) are linear isomorphisms for each \(x\in U_i\).

Equivalently, the {{< knowl id="transition-function" text="transition functions" >}} of such a bundle take values in \(\mathrm{GL}(k,\mathbb{R})\subset \mathrm{Diff}(\mathbb{R}^k)\). The {{< knowl id="tangent-bundle" text="tangent bundle" >}} and {{< knowl id="cotangent-bundle" text="cotangent bundle" >}} are the fundamental examples; many constructions in differential geometry (e.g. a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}}) are formulated for vector bundles.

## Examples
1. **Trivial rank-\(k\) bundle:** \(M\times \mathbb{R}^k\to M\) is a vector bundle with the obvious fiberwise linear structure.
2. **Tangent and cotangent bundles:** for an \(n\)-manifold \(M\), \(TM\to M\) and \(T^*M\to M\) are rank-\(n\) vector bundles.
3. **Möbius line bundle:** a nontrivial rank-1 real vector bundle over \(S^1\) with transition function \(-1\) on the overlap of two arcs.
