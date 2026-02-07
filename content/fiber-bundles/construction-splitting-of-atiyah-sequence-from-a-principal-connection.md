---
title: "Construction: Splitting of the Atiyah sequence from a principal connection"
description: "How a principal connection produces a canonical splitting of the Atiyah sequence of a principal bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$, where $G$ is a {{< knowl id="lie-group" text="Lie group" >}} with {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak g$.

Write $TP$ for the {{< knowl id="tangent-bundle" text="tangent bundle" >}} of $P$. The right action of $G$ on $P$ induces a right action on $TP$, and the quotient bundle
\[
\mathrm{At}(P)\;:=\;TP/G \;\longrightarrow\; M
\]
is the **Atiyah algebroid** of $P$. The differential $d\pi:TP\to TM$ is $G$-equivariant, hence descends to a vector-bundle map (the **anchor**)
\[
a:\mathrm{At}(P)\longrightarrow TM.
\]
The vertical subbundle $\ker(d\pi)\subset TP$ identifies (via fundamental vector fields) with $P\times\mathfrak g$, and after dividing by $G$ one obtains the **adjoint bundle**
\[
\operatorname{ad}(P):=P\times_{\mathrm{Ad}}\mathfrak g,
\]
together with an injective bundle map $\operatorname{ad}(P)\hookrightarrow \mathrm{At}(P)$. This yields the **Atiyah short exact sequence**
\[
0\longrightarrow \operatorname{ad}(P)\longrightarrow \mathrm{At}(P)\xrightarrow{\,a\,} TM\longrightarrow 0.
\]

## Construction (splitting from a connection)

Let $\omega$ be a {{< knowl id="principal-connection" text="principal connection" >}} on $P$, and let $H:=\ker(\omega)\subset TP$ be its horizontal distribution. Define a bundle map
\[
s_\omega:TM\longrightarrow \mathrm{At}(P)
\]
as follows. For $x\in M$ and $v_x\in T_xM$, choose any $p\in P_x:=\pi^{-1}(x)$. There is a unique horizontal vector $\widetilde v_p\in H_p$ with $d\pi(\widetilde v_p)=v_x$. Set
\[
s_\omega(v_x)\;:=\;[\widetilde v_p]\in (TP/G)_x.
\]

**Well-definedness.** If $p' = p\cdot g$, then horizontality is preserved by right translation and $\widetilde v_{p'} = (R_g)_*\widetilde v_p$, so $[\widetilde v_{p'}]=[\widetilde v_p]$ in $TP/G$. Hence $s_\omega$ is independent of the chosen point in the fiber.

**Splitting property.** By construction, $a\circ s_\omega=\mathrm{id}_{TM}$, so $s_\omega$ is a (right) splitting of the Atiyah sequence.

This construction is inverse to the correspondence in {{< knowl id="equivalence-principal-connections-splittings-of-the-atiyah-sequence" text="principal connections ↔ splittings of the Atiyah sequence" >}}.

## Examples

1. **Trivial bundle.** If $P=M\times G$, then $\mathrm{At}(P)\cong TM\oplus(M\times\mathfrak g)$. A connection is determined by a $\mathfrak g$-valued $1$-form $A$ on $M$, and the splitting is
   \[
   s_\omega(v_x)=(v_x,\,-A_x(v_x)).
   \]

2. **Frame bundle.** If $E\to M$ is a rank-$n$ vector bundle and $P=\mathrm{Fr}(E)$ is its {{< knowl id="construction-frame-bundle-fr-of-a-vector-bundle-e" text="frame bundle" >}}, then a {{< knowl id="connection-on-a-vector-bundle" text="vector bundle connection" >}} on $E$ induces a principal connection on $P$, hence a splitting $TM\to T\mathrm{Fr}(E)/\mathrm{GL}(n)$ as above.

3. **Hopf fibration.** For the Hopf bundle $S^3\to S^2$ (a principal $U(1)$-bundle), the standard connection takes horizontals to be orthogonal complements of the fiber circles. The resulting $s_\omega$ identifies each tangent vector on $S^2$ with the corresponding $U(1)$-equivalence class of its horizontal lift in $TS^3$.
