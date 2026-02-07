---
title: "Ext¹ classifies extensions"
description: "Ext¹_R(C,A) is naturally identified with equivalence classes of short exact sequences 0→A→E→C→0."
---

Let \(R\) be a ring and \(A,C\) left \(R\)-modules.

## Statement
An **extension of \(C\) by \(A\)** is a {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}}
\[
0 \longrightarrow A \xrightarrow{i} E \xrightarrow{p} C \longrightarrow 0.
\]

Two extensions
\[
0\to A \xrightarrow{i} E \xrightarrow{p} C \to 0,
\qquad
0\to A \xrightarrow{i'} E' \xrightarrow{p'} C \to 0
\]
are **equivalent** if there exists an \(R\)-module isomorphism \(\phi:E\to E'\) such that \(\phi\circ i=i'\) and \(p' \circ \phi = p\) (i.e. a commutative diagram with identity on \(A\) and \(C\)).

Let \(\mathrm{Ext}(C,A)\) denote the set of equivalence classes of extensions of \(C\) by \(A\).

**Theorem (classification by Ext\(^1\)).** There is a natural bijection
\[
\mathrm{Ext}^1_R(C,A)\ \cong\ \mathrm{Ext}(C,A),
\]
where \(\mathrm{Ext}^1_R(C,A)\) is the degree-1 {{< knowl id="ext" text="Ext" >}} group (the first right derived functor of {{< knowl id="hom-module" section="algebra-modules" text="Hom" >}}; see {{< knowl id="derived-functor" text="derived functor" >}}).

Moreover:
- The zero element of \(\mathrm{Ext}^1_R(C,A)\) corresponds to the **split** extension \(E\cong A\oplus C\).
- The abelian group structure on \(\mathrm{Ext}^1_R(C,A)\) corresponds to the **Baer sum** of extensions (constructed via pullback/pushout in the category of modules).

Cross-links: {{< knowl id="projective-resolution" text="projective resolutions" >}}, {{< knowl id="injective-resolution" text="injective resolutions" >}}, {{< knowl id="hom-left-exact" text="Hom is left exact" >}}.

## Examples

### Example 1: \(\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z, A)\cong A/nA\)
Use the projective resolution from {{< knowl id="projective-resolutions-exist" text="existence of projective resolutions" >}}:
\[
0\to \mathbb Z \xrightarrow{\cdot n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0.
\]
Apply \(\mathrm{Hom}_{\mathbb Z}(-,A)\) to get
\[
0 \to \mathrm{Hom}(\mathbb Z/n\mathbb Z,A) \to A \xrightarrow{\cdot n} A \to \mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,A) \to 0,
\]
so
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,A)\ \cong\ \mathrm{coker}(A \xrightarrow{\cdot n} A)\ =\ A/nA.
\]

**Interpretation.** Elements of \(A/nA\) classify (up to the above equivalence) short exact sequences
\[
0\to A \to E \to \mathbb Z/n\mathbb Z \to 0.
\]
The class \(0\in A/nA\) corresponds to the split extension \(E\cong A\oplus \mathbb Z/n\mathbb Z\).

### Example 2: \(\mathrm{Ext}^1_{k[x]}(k,k)\cong k\) and the module \(k[x]/(x^2)\)
Let \(R=k[x]\) and \(k\cong R/(x)\). Using the free resolution
\[
0\to R \xrightarrow{\cdot x} R \to k \to 0,
\]
applying \(\mathrm{Hom}_R(-,k)\) yields a map \(k \xrightarrow{0} k\) (since \(x\) acts as \(0\) on \(k\)), hence
\[
\mathrm{Ext}^1_{k[x]}(k,k)\cong k.
\]

A concrete non-split extension representing a nonzero class is
\[
0 \longrightarrow (x)/(x^2) \longrightarrow k[x]/(x^2) \longrightarrow k[x]/(x) \longrightarrow 0,
\]
where \((x)/(x^2)\cong k\) and \(k[x]/(x)\cong k\) as \(k[x]\)-modules. The split class corresponds to \(k\oplus k\) (with \(x\) acting by \(0\) on each summand).

### Example 3: Over a field, every extension splits
If \(R=k\) is a field, all \(k\)-modules are projective (and injective), so
\[
\mathrm{Ext}^1_k(V,W)=0
\]
for all vector spaces \(V,W\). Equivalently, every short exact sequence \(0\to W\to E\to V\to 0\) of vector spaces splits (choose a linear section \(V\to E\)).
