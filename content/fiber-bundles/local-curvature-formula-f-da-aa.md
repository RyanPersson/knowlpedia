---
title: "Local curvature formula"
description: "Local expression for the curvature of a principal connection in a chosen gauge."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group a {{< knowl id="lie-group" text="Lie group" >}} $G$ and {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak g$. Let $\omega$ be a {{< knowl id="principal-connection" text="principal connection" >}} on $P$ with {{< knowl id="curvature" text="curvature" >}} $\Omega\in\Omega^2(P;\mathfrak g)$. For an open set $U\subset M$ and a local section $s:U\to P$, define the local connection form and local curvature form by
\[
A := s^*\omega \in \Omega^1(U;\mathfrak g),
\qquad
F := s^*\Omega \in \Omega^2(U;\mathfrak g).
\]

**Theorem (Local curvature formula).** With the notation above,
\[
F \;=\; dA \;+\; \tfrac12[A\wedge A],
\]
where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} on $U$. The bracket-wedge uses the {{< knowl id="lie-bracket" text="Lie bracket" >}} on $\mathfrak g$: for $\alpha\in\Omega^p(U;\mathfrak g)$ and $\beta\in\Omega^q(U;\mathfrak g)$,
\[
[\alpha\wedge\beta](v_1,\dots,v_{p+q})
=\frac{1}{p!\,q!}\sum_{\sigma\in S_{p+q}}\mathrm{sgn}(\sigma)\,
\big[\alpha(v_{\sigma_1},\dots,v_{\sigma_p}),\beta(v_{\sigma_{p+1}},\dots,v_{\sigma_{p+q}})\big].
\]

Equivalently, this is the pullback along $s$ of the global structure equation $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ on $P$.

## Examples
1. **Abelian structure group.** If $G=U(1)$ (or any abelian Lie group), then the Lie bracket on $\mathfrak g$ is zero, hence $[A\wedge A]=0$ and the formula reduces to $F=dA$.
2. **Pure gauge has zero curvature.** On a trivial bundle over $U$, take $A=g^{-1}dg$ for a smooth map $g:U\to G$. Then $F=dA+\tfrac12[A\wedge A]=0$ by the {{< knowl id="lemma-maurercartan-equation-for-the-left-maurercartan-form" text="Maurer–Cartan equation" >}}.
3. **Non-abelian commutator term.** On $U\subset\mathbb R^2$ with coordinates $(x,y)$, choose constant elements $X,Y\in\mathfrak g$ and set $A=X\,dx+Y\,dy$. Then $dA=0$ but $[A\wedge A]=2[X,Y]\,dx\wedge dy$, so $F=[X,Y]\,dx\wedge dy$.
