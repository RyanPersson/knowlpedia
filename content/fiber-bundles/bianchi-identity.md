---
title: "Bianchi identity"
description: "The covariant exterior derivative of the curvature form of a connection vanishes."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle, and let \(\omega \in \Omega^1(P;\mathfrak{g})\) be a connection \(1\)-form. The **curvature** is the \(\mathfrak{g}\)-valued \(2\)-form
$$
\Omega \;=\; d\omega \;+\; \frac{1}{2}[\omega \wedge \omega],
$$
where \([\omega\wedge\omega]\) denotes the wedge product combined with the Lie bracket on \(\mathfrak{g}\).

Define the **covariant exterior derivative** \(D_\omega\) acting on \(\mathfrak{g}\)-valued forms \(\eta \in \Omega^k(P;\mathfrak{g})\) by
$$
D_\omega \eta \;=\; d\eta \;+\; [\omega \wedge \eta].
$$

### Identity (second/Bianchi identity)
The curvature satisfies
$$
D_\omega \Omega = 0.
$$

### Interpretation and consequences
- \(D_\omega \Omega=0\) is the bundle/form version of the "second Bianchi identity." In tensor notation for a covariant derivative \(\nabla\) on the base, it corresponds to the cyclic identity
  $$
  (\nabla_X R)(Y,Z) + (\nabla_Y R)(Z,X) + (\nabla_Z R)(X,Y) = 0,
  $$
  where \(R\) is the curvature tensor.
- In Chern–Weil theory, the Bianchi identity implies that characteristic forms built from \(\Omega\) are closed. Combined with the {{< knowl id="basic-forms-theorem" text="basic forms theorem" >}}, this explains how these forms descend from \(P\) to well-defined de Rham cohomology classes on \(M\).
