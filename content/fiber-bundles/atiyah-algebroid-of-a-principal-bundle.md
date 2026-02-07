---
title: "Atiyah algebroid of a principal bundle"
description: "The quotient TP/G with its natural Lie algebroid structure induced by G-invariant vector fields on the total space."
---

Let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. The right action of \(G\) on \(P\) lifts to an action on the {{< knowl id="tangent-bundle" text="tangent bundle" >}} \(TP\) by differentials \((R_g)_*:TP\to TP\). Form the quotient vector bundle
\[
A(P)\coloneqq TP/G \;\longrightarrow\; M,
\]
whose fiber over \(x\in M\) is \((T_pP)/G\) for any \(p\in P_x\).

The map \(d\pi:TP\to TM\) is \(G\)-equivariant and descends to a bundle map (the **anchor**)
\[
a:A(P)\to TM.
\]

A section of \(A(P)\) can be identified with a \(G\)-invariant vector field on \(P\): explicitly, \( \Gamma(A(P)) \cong \mathfrak{X}(P)^G \). Using this, define a bracket on \(\Gamma(A(P))\) by
\[
[\![\sigma,\tau]\!]\;\coloneqq\;\text{the class of }[X,Y],
\]
where \(X,Y\) are \(G\)-invariant vector fields representing \(\sigma,\tau\) and \([X,Y]\) is their {{< knowl id="lie-bracket" text="Lie bracket" >}}. This is well-defined and makes \(A(P)\) into a Lie algebroid over \(M\), called the **Atiyah algebroid** of \(P\).

## Examples
1. **Bundle over a point.** If \(M=\{\ast\}\) and \(P=G\), then \(TP/G\) identifies with the Lie algebra \(\mathfrak{g}\) (via left translation), and the induced bracket is the usual Lie bracket on \(\mathfrak{g}\).

2. **Trivial bundle.** For \(P=M\times G\), there is a vector bundle isomorphism
   \[
   TP/G \cong TM \oplus (M\times \mathfrak{g}),
   \]
   and the bracket on sections \((X,\phi)\), \((Y,\psi)\) is
   \[
   [\![(X,\phi),(Y,\psi)]\!] = \bigl([X,Y],\, X(\psi)-Y(\phi)+[\phi,\psi]\bigr).
   \]

3. **Principal \(U(1)\)-bundle.** Since \(\mathfrak{u}(1)\cong i\mathbb{R}\) is abelian, the adjoint part is central. Thus \(TP/U(1)\) is (as a Lie algebroid) a central extension of \(TM\) by a trivial line bundle, with curvature of a connection measuring the extension class.
