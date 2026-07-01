+++
id = "fiber-bundles/lemma-local-curvature-transformation-law-fg-g-1fg"
title = "Lemma: local curvature transforms by conjugation"
kind = "knowl"
summary = "Under a gauge transformation, the local curvature 2-form is conjugated by the gauge function"
aliases = ["lemma-local-curvature-transformation-law-fg-g-1fg", "Lemma: local curvature transforms by conjugation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lemma-local-curvature-transformation-law-fg-g-1fg.md"
+++

Let $U\subseteq M$ be open, let $G$ be a Lie group with Lie algebra $\mathfrak g$, and let
\[
A\in\Omega^1(U;\mathfrak g)
\]
be a [[fiber-bundles/local-connection-1-form|local connection 1-form]]. Its local curvature is
\[
F:=dA + A\wedge A\in\Omega^2(U;\mathfrak g),
\]
as in [[fiber-bundles/local-curvature-formula-f-da-aa|the local curvature formula]].

## Lemma (curvature transformation law)
Given a smooth map $g:U\to G$, define the gauge-transformed local connection 1-form by
\[
A^g := g^{-1}Ag + g^{-1}dg,
\]
which is the [[fiber-bundles/lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg|standard local gauge transformation]]. Let
\[
F^g:=dA^g + A^g\wedge A^g
\]
be its curvature. Then
\[
F^g = g^{-1}Fg.
\]
Equivalently, $F$ transforms by the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]] of $G$ on $\mathfrak g$.

### Proof (calculation)
Expand $F^g$ using $A^g=g^{-1}Ag+g^{-1}dg$ and the Leibniz rule:
- the mixed terms involving $d(g^{-1}dg)$ cancel using the Maurer--Cartan identity for $g^{-1}dg$,
- the remaining terms regroup into $g^{-1}(dA + A\wedge A)g$.

This is the usual statement that curvature is tensorial under gauge transformations.

A direct consequence is that on overlaps $U_i\cap U_j$ with transition function $g_{ij}$, the local curvature forms satisfy
\[
F_j = g_{ij}^{-1}F_i g_{ij},
\]
so invariant polynomials applied to $F_i$ glue to globally defined [[fiber-bundles/chernweil-form|Chern--Weil forms]].

## Examples
1. **Abelian groups (electromagnetism).**
   If $G$ is abelian (for example $U(1)$), then $g^{-1}Fg=F$, so the curvature 2-form is gauge invariant. In particular, the transformation reduces to $A^g=A+g^{-1}dg$ while $F^g=dA^g=dA=F$.

2. **Pure gauge connections have zero curvature.**
   On a trivial bundle, if $A=g^{-1}dg$ is [[fiber-bundles/pure-gauge-connection-ag-1dg-on-a-trivial-bundle|pure gauge]], then $F=dA+A\wedge A=0$. The lemma then gives $F^h=h^{-1}0\,h=0$ for any further gauge transformation $h$.

3. **Associated vector bundles (matrix conjugation).**
   If $G$ acts on a vector space via a representation (see [[lie-groups/representation-of-a-lie-group|representation]]), the induced curvature on the associated vector bundle is a matrix-valued 2-form, and this lemma becomes the familiar rule “curvature matrices conjugate under change of frame.”
