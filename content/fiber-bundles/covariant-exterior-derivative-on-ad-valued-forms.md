---
title: "Covariant exterior derivative on ad(P)-valued forms"
description: "The exterior derivative on differential forms with values in the adjoint bundle, defined using a principal connection."
---

Let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with Lie algebra \(\mathfrak{g}\). The **adjoint bundle** is the vector bundle
\[
\mathrm{ad}(P)\coloneqq P\times_{\mathrm{Ad}} \mathfrak{g}\;\to\;M,
\]
associated to the adjoint action of \(G\) on {{< knowl id="lie-algebra" text="the Lie algebra" section="lie-groups">}} \(\mathfrak{g}\).

A principal connection on \(P\) induces a connection \(\nabla\) on \(\mathrm{ad}(P)\) (equivalently, it induces the operator on tensorial forms described by {{< knowl id="exterior-covariant-derivative" text="the exterior covariant derivative" >}}). The **covariant exterior derivative**
\[
d_\nabla:\Omega^k(M;\mathrm{ad}(P))\to \Omega^{k+1}(M;\mathrm{ad}(P))
\]
is the unique graded derivation extending \(\nabla\) and satisfying the usual Koszul formula: for \(\alpha\in \Omega^k(M;\mathrm{ad}(P))\) and vector fields \(X_0,\dots,X_k\),
\[
\begin{aligned}
(d_\nabla \alpha)(X_0,\dots,X_k)
&= \sum_{i=0}^k (-1)^i\,\nabla_{X_i}\bigl(\alpha(X_0,\dots,\widehat{X_i},\dots,X_k)\bigr) \\
&\quad + \sum_{0\le i<j\le k} (-1)^{i+j}\,\alpha([X_i,X_j],X_0,\dots,\widehat{X_i},\dots,\widehat{X_j},\dots,X_k),
\end{aligned}
\]
where the bracket is the {{< knowl id="lie-bracket" text="Lie bracket" >}} of vector fields on \(M\).

Locally, if \(A\in \Omega^1(U;\mathfrak{g})\) is a local connection form and we identify \(\mathrm{ad}(P)|_U\cong U\times \mathfrak{g}\), then for \(\alpha\in \Omega^k(U;\mathfrak{g})\),
\[
d_\nabla \alpha = d\alpha + [A\wedge \alpha],
\]
with \(d\) the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.

## Examples
1. **Sections of \(\mathrm{ad}(P)\) (degree 0).** For \(\phi\in \Omega^0(M;\mathrm{ad}(P))\), locally \(\phi:U\to\mathfrak{g}\), one has
   \[
   d_\nabla \phi = d\phi + [A,\phi],
   \]
   which is the usual covariant derivative in the adjoint representation.

2. **Bianchi identity on the base.** Let \(F\in \Omega^2(U;\mathfrak{g})\) be the local curvature 2-form. Then
   \[
   d_\nabla F = 0
   \]
   is the Bianchi identity written as a covariant closure condition.

3. **Abelian structure group.** If \(G\) is abelian, then \([A\wedge \alpha]=0\) for all \(\alpha\), so \(d_\nabla\) reduces to the ordinary exterior derivative on \(\mathfrak{g}\)-valued forms.
