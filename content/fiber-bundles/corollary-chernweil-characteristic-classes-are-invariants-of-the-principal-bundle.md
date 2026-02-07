---
title: "Chern–Weil classes are independent of the connection"
description: "Characteristic classes obtained from invariant polynomials in curvature do not depend on the chosen principal connection."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle, and let \(p\) be an \(\mathrm{Ad}\)-invariant polynomial on the Lie algebra (for example, a symmetric \(k\)-linear form on \(\mathfrak g\) invariant under the adjoint action). Given a {{< knowl id="principal-connection" text="principal connection" >}} \(\omega\) with {{< knowl id="curvature" text="curvature" >}} \(\Omega\), the Chern–Weil construction produces a differential form on \(M\) by applying \(p\) to \(\Omega\) and using the fact that the resulting form is basic.

## Corollary (independence of connection)
For each invariant polynomial \(p\) of degree \(k\), there is a canonically defined de Rham cohomology class
\[
\mathrm{cw}_p(P)\in H^{2k}_{\mathrm{dR}}(M)
\]
with the following property:

- For any principal connection \(\omega\) on \(P\), the Chern–Weil form \(\mathrm{CW}_p(\omega)\in \Omega^{2k}(M)\) satisfies \(d\,\mathrm{CW}_p(\omega)=0\) (closedness, using {{< knowl id="exterior-derivative" text="the exterior derivative" >}}), and its class \([\mathrm{CW}_p(\omega)]\) depends only on \(P\), not on \(\omega\).

Equivalently, if \(\omega_0,\omega_1\) are two connections on \(P\), then
\[
\mathrm{CW}_p(\omega_1)-\mathrm{CW}_p(\omega_0)
\]
is an exact {{< knowl id="differential-k-form" text="differential form" >}} on \(M\). Thus Chern–Weil characteristic classes are invariants of the underlying principal bundle.

## Examples
1. **First Chern class of a line bundle.** For a principal \(U(1)\)-bundle (complex line bundle), choosing \(p\) to be the identity on \(\mathfrak u(1)\) gives a closed 2-form representing the first Chern class in real cohomology; changing the connection changes the representative by an exact form.
2. **Pontryagin classes.** For a principal \(SO(n)\)-bundle, invariant polynomials built from traces of powers of curvature produce the Pontryagin classes. For \(TM\), this shows Pontryagin classes are independent of the chosen Riemannian metric and its Levi–Civita connection.
3. **Second Chern class for \(SU(2)\).** For a principal \(SU(2)\)-bundle over a 4-manifold, the invariant polynomial \(p(X,Y)=\mathrm{tr}(XY)\) yields a 4-form representing the second Chern class (instanton number), independent of the chosen connection.
