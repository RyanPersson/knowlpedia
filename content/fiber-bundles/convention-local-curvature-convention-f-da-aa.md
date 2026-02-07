---
title: "Convention: local curvature is F = dA + A wedge A"
description: "The sign and bracket convention relating a local connection 1 form to its local curvature 2 form."
---

A principal connection can be described locally by a Lie algebra–valued 1-form, and its curvature is then expressed by a standard structure equation. Different sign conventions appear in the literature; this knowl fixes the convention used here.

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} and let $\omega\in\Omega^1(P;\mathfrak{g})$ be a {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}}. Let $\Omega\in\Omega^2(P;\mathfrak{g})$ be its curvature (see {{< knowl id="curvature-2-form-of-a-principal-connection" text="curvature 2-form of a principal connection" >}}).

Fix a local section $s:U\to P$ over an open set $U\subseteq M$. Define:
- the **local connection 1-form** on $U$ by
  \[
  A := s^*\omega \in \Omega^1(U;\mathfrak{g}),
  \]
  as in {{< knowl id="local-connection-1-form" text="local connection 1-form" >}};
- the **local curvature 2-form** on $U$ by
  \[
  F := s^*\Omega \in \Omega^2(U;\mathfrak{g}),
  \]
  as in {{< knowl id="local-curvature-2-form" text="local curvature 2-form" >}}.

## Convention
We use the local curvature formula
\[
F = dA + A\wedge A.
\]
This is the convention recorded in {{< knowl id="local-curvature-formula-f-da-aa" text="the local curvature formula F = dA + A wedge A" >}}.

Here $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}, and $A\wedge A$ is the $\mathfrak{g}$-valued 2-form defined by
\[
(A\wedge A)(X,Y) := [A(X),A(Y)],
\]
using the {{< knowl id="lie-bracket" text="Lie bracket" >}} on $\mathfrak{g}$. (This is a standard way to combine the {{< knowl id="wedge-product-of-differential-forms" text="wedge product" >}} on forms with the bracket on the Lie algebra.)

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
   for a smooth map $g:U\to G$ (compare {{< knowl id="pure-gauge-connection-ag-1dg-on-a-trivial-bundle" text="pure gauge connection" >}}). With the convention above, one obtains
   \[
   F = dA + A\wedge A = 0,
   \]
   which is the local manifestation of flatness.

3. **Non-abelian contribution from A wedge A**
   For a non-abelian $G$ (for example $SU(2)$), even if the components of $A$ have constant coefficients in a coordinate chart, the term $A\wedge A$ can be nonzero because it depends on the Lie bracket. This is the origin of genuinely non-linear curvature effects in gauge theory.
