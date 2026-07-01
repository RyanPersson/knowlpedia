+++
id = "fiber-bundles/convention-local-curvature-convention-f-da-aa"
title = "Convention: local curvature is F = dA + A wedge A"
kind = "knowl"
summary = "The sign and bracket convention relating a local connection 1 form to its local curvature 2 form."
aliases = ["convention-local-curvature-convention-f-da-aa", "Convention: local curvature is F = dA + A wedge A"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/convention-local-curvature-convention-f-da-aa.md"
+++

A principal connection can be described locally by a Lie algebra–valued 1-form, and its curvature is then expressed by a standard structure equation. Different sign conventions appear in the literature; this knowl fixes the convention used here.

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] and let $\omega\in\Omega^1(P;\mathfrak{g})$ be a [[fiber-bundles/connection-1-form-on-a-principal-bundle|connection 1-form]]. Let $\Omega\in\Omega^2(P;\mathfrak{g})$ be its curvature (see [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature 2-form of a principal connection]]).

Fix a local section $s:U\to P$ over an open set $U\subseteq M$. Define:
- the **local connection 1-form** on $U$ by
  \[
  A := s^*\omega \in \Omega^1(U;\mathfrak{g}),
  \]
  as in [[fiber-bundles/local-connection-1-form|local connection 1-form]];
- the **local curvature 2-form** on $U$ by
  \[
  F := s^*\Omega \in \Omega^2(U;\mathfrak{g}),
  \]
  as in [[fiber-bundles/local-curvature-2-form|local curvature 2-form]].

## Convention
We use the local curvature formula
\[
F = dA + A\wedge A.
\]
This is the convention recorded in [[fiber-bundles/local-curvature-formula-f-da-aa|the local curvature formula F = dA + A wedge A]].

Here $d$ is the [[fiber-bundles/exterior-derivative|exterior derivative]], and $A\wedge A$ is the $\mathfrak{g}$-valued 2-form defined by
\[
(A\wedge A)(X,Y) := [A(X),A(Y)],
\]
using the [[fiber-bundles/lie-bracket|Lie bracket]] on $\mathfrak{g}$. (This is a standard way to combine the [[fiber-bundles/wedge-product-of-differential-forms|wedge product]] on forms with the bracket on the Lie algebra.)

With this convention, the global structure equation on $P$ can be written in the parallel form
\[
\Omega = d\omega + \omega\wedge\omega,
\]
where $\omega\wedge\omega$ uses the same bracketed wedge construction.

## Examples
1. **Abelian structure group**
   If $G$ is abelian (for instance $U(1)$), then $[\,\cdot,\cdot\,]=0$ on $\mathfrak{g}$, so $A\wedge A=0$ and the formula reduces to
   \[
   F=dA.
   \]

2. **Pure gauge gives zero curvature**
   On a trivial bundle over $U$, a pure gauge local connection can be written as
   \[
   A = g^{-1}dg
   \]
   for a smooth map $g:U\to G$ (compare [[fiber-bundles/pure-gauge-connection-ag-1dg-on-a-trivial-bundle|pure gauge connection]]). With the convention above, one obtains
   \[
   F = dA + A\wedge A = 0,
   \]
   which is the local manifestation of flatness.

3. **Non-abelian contribution from A wedge A**
   For a non-abelian $G$ (for example $SU(2)$), even if the components of $A$ have constant coefficients in a coordinate chart, the term $A\wedge A$ can be nonzero because it depends on the Lie bracket. This is the origin of genuinely non-linear curvature effects in gauge theory.
