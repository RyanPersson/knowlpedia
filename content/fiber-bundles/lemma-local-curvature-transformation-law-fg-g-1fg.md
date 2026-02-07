---
title: "Lemma: local curvature transforms by conjugation"
description: "Under a gauge transformation, the local curvature 2-form is conjugated by the gauge function"
---

Let $U\subseteq M$ be open, let $G$ be a Lie group with Lie algebra $\mathfrak g$, and let
\[
A\in\Omega^1(U;\mathfrak g)
\]
be a {{< knowl id="local-connection-1-form" text="local connection 1-form" >}}. Its local curvature is
\[
F:=dA + A\wedge A\in\Omega^2(U;\mathfrak g),
\]
as in {{< knowl id="local-curvature-formula-f-da-aa" text="the local curvature formula" >}}.

## Lemma (curvature transformation law)
Given a smooth map $g:U\to G$, define the gauge-transformed local connection 1-form by
\[
A^g := g^{-1}Ag + g^{-1}dg,
\]
which is the {{< knowl id="lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg" text="standard local gauge transformation" >}}. Let
\[
F^g:=dA^g + A^g\wedge A^g
\]
be its curvature. Then
\[
F^g = g^{-1}Fg.
\]
Equivalently, $F$ transforms by the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" section="lie-groups">}} of $G$ on $\mathfrak g$.

### Proof (calculation)
Expand $F^g$ using $A^g=g^{-1}Ag+g^{-1}dg$ and the Leibniz rule:
- the mixed terms involving $d(g^{-1}dg)$ cancel using the Maurer--Cartan identity for $g^{-1}dg$,
- the remaining terms regroup into $g^{-1}(dA + A\wedge A)g$.

This is the usual statement that curvature is tensorial under gauge transformations.

A direct consequence is that on overlaps $U_i\cap U_j$ with transition function $g_{ij}$, the local curvature forms satisfy
\[
F_j = g_{ij}^{-1}F_i g_{ij},
\]
so invariant polynomials applied to $F_i$ glue to globally defined {{< knowl id="chernweil-form" text="Chern--Weil forms" >}}.

## Examples
1. **Abelian groups (electromagnetism).**  
   If $G$ is abelian (for example $U(1)$), then $g^{-1}Fg=F$, so the curvature 2-form is gauge invariant. In particular, the transformation reduces to $A^g=A+g^{-1}dg$ while $F^g=dA^g=dA=F$.

2. **Pure gauge connections have zero curvature.**  
   On a trivial bundle, if $A=g^{-1}dg$ is {{< knowl id="pure-gauge-connection-ag-1dg-on-a-trivial-bundle" text="pure gauge" >}}, then $F=dA+A\wedge A=0$. The lemma then gives $F^h=h^{-1}0\,h=0$ for any further gauge transformation $h$.

3. **Associated vector bundles (matrix conjugation).**  
   If $G$ acts on a vector space via a representation (see {{< knowl id="representation-of-a-lie-group" text="representation" section="lie-groups">}}), the induced curvature on the associated vector bundle is a matrix-valued 2-form, and this lemma becomes the familiar rule “curvature matrices conjugate under change of frame.”
