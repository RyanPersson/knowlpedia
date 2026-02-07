---
title: "Splitting of the Atiyah sequence"
description: "A right inverse TM to TP/G that is equivalent to choosing a principal connection."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with Atiyah sequence
\[
0 \to \mathrm{ad}(P) \to TP/G \xrightarrow{a} TM \to 0
\]
as in {{< knowl id="atiyah-sequence-tpgtm0" text="the Atiyah sequence" >}}.

A **splitting** of the Atiyah sequence is a vector bundle map
\[
\sigma:TM\to TP/G
\]
such that \(a\circ \sigma=\mathrm{id}_{TM}\). Equivalently, \(\sigma\) is a right inverse of the anchor map.

Splittings are in natural bijection with {{< knowl id="principal-connection" text="principal connections" >}} on \(P\):
- Given a principal connection with horizontal distribution \(H\subset TP\), define \(\sigma(v_x)\) to be the class in \(TP/G\) of the horizontal lift \(v^H_p\in H_p\) at any \(p\in P_x\) (well-defined because horizontality is \(G\)-invariant).
- Given a splitting \(\sigma\), define \(H_p\subset T_pP\) by declaring \(X\in T_pP\) to be horizontal iff its class \([X]\in (TP/G)_x\) equals \(\sigma(d\pi_p X)\). This yields a \(G\)-invariant complement to the vertical space.

The curvature of the induced connection can be recovered from \(\sigma\) as the obstruction to \(\sigma\) preserving brackets in the Atiyah algebroid: the \(\mathrm{ad}(P)\)-valued 2-form
\[
\Omega_\sigma(v,w) \coloneqq [\![\sigma(v),\sigma(w)]\!] - \sigma([v,w])
\]
vanishes exactly when the connection is flat.

## Examples
1. **Trivial bundle and a gauge potential.** For \(P=M\times G\), identify \(TP/G\cong TM\oplus (M\times \mathfrak{g})\). A choice of \(\mathfrak{g}\)-valued 1-form \(A\) gives a splitting \(\sigma(v)=(v,-A(v))\), whose associated principal connection has local connection form \(A\).

2. **Flatness as a bracket condition.** In the trivial-bundle identification above, the splitting coming from \(A\) preserves the Lie algebroid bracket precisely when \(F=dA+\tfrac12[A\wedge A]=0\), i.e. when the connection is flat.

3. **Circle bundles.** For a principal \(U(1)\)-bundle, any choice of connection 1-form determines a splitting. Since \(\mathfrak{u}(1)\) is abelian, the curvature is an ordinary 2-form measuring the failure of horizontal lifts to commute.
