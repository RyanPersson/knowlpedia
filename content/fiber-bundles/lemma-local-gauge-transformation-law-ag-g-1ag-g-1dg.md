---
title: "Local gauge transformation law for a connection"
description: "Under a change of local section, the local connection form transforms as A^g = g^{-1}Ag + g^{-1}dg."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with a {{< knowl id="principal-connection" text="principal connection" >}} $\omega$. Fix an open set $U\subset M$ and a local section $s:U\to P$. The associated local connection form is
\[
A:=s^*\omega\in\Omega^1(U;\mathfrak g).
\]

Let $g:U\to G$ be a {{< knowl id="smooth-map" text="smooth map" >}} and define a new local section by $s':=s\cdot g$ (right action of $G$ on $P$).

**Lemma (Local gauge transformation law).** The local connection form $A':=(s')^*\omega$ satisfies
\[
A'=\mathrm{Ad}(g^{-1})A + g^{-1}dg.
\]
In a matrix realization of $G$, this is $A' = g^{-1}Ag + g^{-1}dg$. The $1$-form $g^{-1}dg$ is the pullback of the left Maurer–Cartan form and satisfies the {{< knowl id="lemma-maurercartan-equation-for-the-left-maurercartan-form" text="Maurer–Cartan equation" >}}.

## Examples
1. **Abelian case (U(1)).** Since Ad is trivial, the formula becomes $A'=A+g^{-1}dg$, matching the usual shift of a $U(1)$ potential by an exact form locally.
2. **Constant change of section.** If $g$ is constant, then $dg=0$ and $A'=\mathrm{Ad}(g^{-1})A$ is just pointwise conjugation.
3. **Producing a pure gauge potential.** Starting from the trivial potential $A=0$ on a trivial bundle, the transformation gives $A'=g^{-1}dg$, a pure gauge connection.
