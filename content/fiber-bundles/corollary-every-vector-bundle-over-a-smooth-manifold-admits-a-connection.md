---
title: "Every vector bundle admits a connection"
description: "Any smooth vector bundle over a smooth manifold admits at least one covariant derivative."
---

Let \(M\) be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let \(E\to M\) be a smooth vector bundle.

## Corollary (existence of vector bundle connections)
There exists at least one {{< knowl id="connection-on-a-vector-bundle" text="connection on the vector bundle" >}} \(E\to M\), i.e. a covariant derivative \(\nabla:\Gamma(E)\to \Omega^1(M;E)\) satisfying the Leibniz rule.

One proof strategy is to pass to the frame bundle \(\mathrm{Fr}(E)\to M\), use the existence of connections on principal bundles (see {{< knowl id="corollary-every-principal-g-bundle-over-a-smooth-manifold-admits-a-connection" text="existence of principal connections" >}}), and then induce a connection on \(E\) from a principal connection on \(\mathrm{Fr}(E)\).

## Examples
1. **Trivial bundle.** On \(E=M\times \mathbb R^k\), the operator \(d\) (componentwise differentiation in a trivialization) is a connection.
2. **Tangent bundle.** On a Riemannian manifold, the Levi–Civita connection gives a connection on \(TM\) and hence on all tensor bundles built from \(TM\) and \(T^*M\).
3. **Complex line bundles.** A Hermitian metric on a complex line bundle admits a compatible unitary connection; for holomorphic line bundles this includes the Chern connection.
