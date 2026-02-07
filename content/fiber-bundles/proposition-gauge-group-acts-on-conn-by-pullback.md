---
title: "Gauge group action on connections by pullback"
description: "Gauge transformations act on principal connections by pulling back the connection one-form."
---

Let \(G\) be a {{< knowl id="lie-group" text="Lie group" >}} and let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. Write \(\mathrm{Conn}(P)\) for the set of {{< knowl id="principal-connection" text="principal connections" >}} on \(P\), and let \(\mathrm{Gauge}(P)\) denote the gauge group, i.e. the group of \(G\)-equivariant diffeomorphisms \(\Phi:P\to P\) covering the identity on \(M\) (so \(\pi\circ\Phi=\pi\) and \(\Phi(p\cdot g)=\Phi(p)\cdot g\)).

## Proposition (pullback action on \(\mathrm{Conn}(P)\))
For every \(\Phi\in \mathrm{Gauge}(P)\) and every principal connection \(\omega\in \mathrm{Conn}(P)\), the pullback
\[
\Phi\cdot \omega \;:=\; \Phi^*\omega
\]
is again a principal connection on \(P\). Moreover, this defines a left group action of \(\mathrm{Gauge}(P)\) on \(\mathrm{Conn}(P)\), i.e.
\[
(\Phi_1\Phi_2)\cdot \omega \;=\; \Phi_2\cdot(\Phi_1\cdot \omega), 
\qquad \mathrm{id}\cdot \omega=\omega.
\]

Equivalently, if \(\omega\) is viewed as a \(G\)-equivariant horizontal distribution \(H=\ker\omega\subset TP\), then \(\Phi\) sends horizontals to horizontals:
\[
H^{\Phi^*\omega}_p \;=\; (d\Phi_p)^{-1}\bigl(H_{\Phi(p)}^{\omega}\bigr),
\]
so the gauge group acts on the set of horizontal distributions defining connections.

## Examples
1. **Trivial bundle \(P=M\times G\).** A gauge transformation is given by a smooth map \(g:M\to G\) via \(\Phi_g(x,h)=(x,g(x)h)\). Writing a connection in a global trivialization as a \(\mathfrak g\)-valued 1-form \(A\in\Omega^1(M;\mathfrak g)\), the action becomes
   \[
   A \longmapsto A^g := \mathrm{Ad}_{g^{-1}}A + g^{-1}dg.
   \]
2. **Abelian structure group.** If \(G\) is abelian (e.g. \(U(1)\)), then \(\mathrm{Ad}_{g^{-1}}\) is trivial and the transformation law reduces to
   \[
   A \longmapsto A + g^{-1}dg,
   \]
   i.e. gauge transformations act by translation by an exact 1-form (in a trivialization).
3. **Frame bundle viewpoint.** If \(P\) is a frame bundle of a vector bundle, a gauge transformation is a change of frame covering \(\mathrm{id}_M\). Pulling back the connection corresponds to the usual transformation rule for connection matrices under a change of frame.
