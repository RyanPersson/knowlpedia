---
title: "Bundle isomorphism"
description: "An invertible bundle morphism whose total-space map and base map are diffeomorphisms."
---

Let \(\pi:E\to M\) and \(\pi':E'\to M'\) be smooth fiber bundles. A **bundle isomorphism** is a {{< knowl id="bundle-morphism" text="bundle morphism" >}} \((\Phi,f)\) where:

- \(f:M\to M'\) is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}},
- \(\Phi:E\to E'\) is a diffeomorphism,
- and the projections commute: \(\pi'\circ \Phi=f\circ \pi\).

Equivalently, \(\Phi\) is a diffeomorphism that is fiber-preserving over \(f\), and its inverse \(\Phi^{-1}\) is fiber-preserving over \(f^{-1}\). If \(M=M'\) and \(f=\mathrm{id}_M\), one often calls \(\Phi\) a bundle automorphism.

In local trivializations, a bundle isomorphism is locally a diffeomorphism of products that preserves the base coordinate: over \(U\subset M\), it is represented as \((x,u)\mapsto (f(x),\psi(x,u))\) with each \(\psi(x,\cdot)\) a diffeomorphism of the typical fiber.

## Examples
1. **Trivialization as an isomorphism:** a global trivialization \(E\cong M\times F\) is a bundle isomorphism from \(E\) to the product bundle.
2. **Tangent bundles:** if \(f:M\to N\) is a diffeomorphism, then \(df:TM\to TN\) is a bundle isomorphism covering \(f\).
3. **Gauge transformations on products:** for \(M\times F\to M\), any map \((x,u)\mapsto(x,h(x)(u))\) with \(h:M\to \mathrm{Diff}(F)\) defines a bundle automorphism.
