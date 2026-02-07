---
title: "Principal connection"
description: "A G-invariant choice of horizontal subspaces complementing the vertical tangent spaces in a principal bundle."
---

Let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure {{< knowl id="lie-group" text="Lie group" >}} \(G\). For each \(p\in P\), define the **vertical subspace**
\[
V_p \coloneqq \ker(d\pi_p)\subset T_pP.
\]

A **principal connection** on \(P\) is a smooth assignment of a subspace \(H_p\subset T_pP\) (the **horizontal subspace**) for every \(p\in P\) such that:

1. (**Horizontal–vertical splitting**) \(T_pP = H_p \oplus V_p\) for all \(p\in P\).
2. (**Right-invariance**) For every \(g\in G\), the differential of the right action \(R_g:P\to P\) satisfies
   \[
   (R_g)_*(H_p)=H_{p\cdot g}.
   \]

Equivalently, a principal connection is a \(G\)-equivariant splitting of the short exact sequence of vector bundles over \(P\),
\[
0 \longrightarrow VP \longrightarrow TP \xrightarrow{d\pi} \pi^*TM \longrightarrow 0.
\]
A principal connection can also be encoded by a {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}} \(\omega\) on \(P\); its kernel at each point is the horizontal subspace.

A principal connection determines horizontal lifts of curves and hence a notion of {{< knowl id="parallel-transport" text="parallel transport" >}} in \(P\).

## Examples
1. **Trivial bundle with a chosen gauge potential.** On \(P=U\times G\to U\), any \(\mathfrak{g}\)-valued 1-form \(A\in \Omega^1(U;\mathfrak{g})\) defines a principal connection by declaring a tangent vector \((v,\xi)\in T_xU\oplus T_gG\cong T_{(x,g)}(U\times G)\) to be horizontal exactly when \(\omega(v,\xi)=0\) for the standard connection form \(\omega=\mathrm{Ad}(g^{-1})A + g^{-1}dg\). This makes the horizontal distribution explicit in a product trivialization.

2. **Connections on frame bundles.** If \(M\) has a linear connection on its {{< knowl id="tangent-bundle" text="tangent bundle" >}}, then the frame bundle \(\mathrm{Fr}(TM)\to M\) carries an induced principal connection whose horizontals correspond to parallel frames along curves.

3. **Hopf fibration.** The Hopf map \(S^3\to S^2\) is a principal \(U(1)\)-bundle. The standard contact 1-form on \(S^3\) defines a horizontal distribution (the orthogonal complement to the \(U(1)\)-orbits) that is invariant under the right \(U(1)\)-action, hence gives a principal connection.
