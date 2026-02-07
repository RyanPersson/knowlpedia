---
title: "Bundle atlas"
description: "A collection of compatible local trivializations covering the base of a fiber bundle."
---

Let \(\pi:E\to M\) be a {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}} with typical fiber \(F\). A **bundle atlas** is a collection of {{< knowl id="local-trivialization" text="local trivializations" >}} \(\{(U_i,\Phi_i)\}_{i\in I}\) such that:

1. \(\{U_i\}_{i\in I}\) is an open cover of \(M\), and
2. for every overlap \(U_{ij}:=U_i\cap U_j\), the change of trivialization
   \[
   \Phi_i\circ \Phi_j^{-1}:U_{ij}\times F\longrightarrow U_{ij}\times F
   \]
   is a diffeomorphism over \(\mathrm{id}_{U_{ij}}\), hence is of the form \((x,f)\mapsto (x, t_{ij}(x)(f))\) for a smooth family of diffeomorphisms of \(F\).

The associated maps \(t_{ij}\) are the {{< knowl id="transition-function" text="transition functions" >}} of the atlas and satisfy the standard cocycle identities on triple overlaps.

## Examples
1. **From a manifold atlas:** the usual coordinate charts on \(M\) induce a bundle atlas for \(TM\to M\) by identifying \(TM|_{U_i}\cong U_i\times\mathbb{R}^n\).
2. **Möbius line bundle:** two local trivializations over overlapping arcs of \(S^1\) form a bundle atlas; the overlap map is given by a sign change in the fiber.
3. **Principal bundles:** local sections of a principal \(G\)-bundle yield local trivializations and hence a bundle atlas whose transitions take values in \(G\).
