---
title: "Ext"
description: "The right derived functors of Hom; measures extension classes and failure of exactness of Hom."
---

Let $R$ be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} and let $M,N$ be (left) {{< knowl id="module" section="algebra-modules" text="$R$-modules" >}}.

## Definition (via a projective resolution)
Choose a {{< knowl id="projective-resolution" text="projective resolution" >}} $P_\bullet \to M$, i.e.
\[
\cdots \to P_2 \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \to M \to 0
\]
with each $P_i$ projective. Apply the functor {{< knowl id="hom-module" section="algebra-modules" text="$\mathrm{Hom}_R(-,N)$" >}} to obtain a {{< knowl id="cochain-complex" text="cochain complex" >}}
\[
0 \to \mathrm{Hom}_R(P_0,N) \xrightarrow{d_1^*} \mathrm{Hom}_R(P_1,N) \xrightarrow{d_2^*} \mathrm{Hom}_R(P_2,N) \to \cdots.
\]
Define
\[
\mathrm{Ext}^n_R(M,N) \;:=\; H^n\!\big(\mathrm{Hom}_R(P_\bullet,N)\big),
\]
where $H^n(-)$ denotes {{< knowl id="cohomology-module" text="cohomology" >}}.

This construction is independent of the chosen resolution (up to canonical isomorphism), and is functorial: $\mathrm{Ext}^n_R(-,N)$ is contravariant in the first variable and $\mathrm{Ext}^n_R(M,-)$ is covariant in the second.

## Equivalent definition (via an injective resolution)
If $R\text{-Mod}$ has enough injectives, choose an {{< knowl id="injective-resolution" text="injective resolution" >}} $N \to I^\bullet$ and set
\[
\mathrm{Ext}^n_R(M,N) \;:=\; H^n\!\big(\mathrm{Hom}_R(M,I^\bullet)\big).
\]

In either approach, $\mathrm{Ext}^0_R(M,N)\cong \mathrm{Hom}_R(M,N)$.

## Conceptual meaning
- $\mathrm{Ext}^1_R(M,N)$ classifies extensions
  \[
  0 \to N \to E \to M \to 0
  \]
  up to the usual equivalence relation; see {{< knowl id="ext1-classifies-extensions" text="Ext^1 classifies extensions" >}}.
- Higher $\mathrm{Ext}^n$ can be viewed as higher obstructions and are the values of the {{< knowl id="derived-functor" text="right derived functors" >}} of {{< knowl id="hom-left-exact" text="$\mathrm{Hom}$ is left exact" >}}.
- A {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}} in either variable yields a {{< knowl id="long-exact-sequence-ext" text="long exact sequence in Ext" >}}, which is a special case of {{< knowl id="long-exact-sequence-derived" text="the long exact sequence for derived functors" >}}.

## Examples

### Example 1: Vector spaces over a field
Let $k$ be a field and $V,W$ be $k$-vector spaces. Every $k$-module is free (hence projective and injective), so any projective resolution can be taken to be length $0$. Therefore,
\[
\mathrm{Ext}^n_k(V,W)=0 \quad (n>0), \qquad \mathrm{Ext}^0_k(V,W)=\mathrm{Hom}_k(V,W).
\]

### Example 2: $\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n, A)\cong A/nA$
Take the standard projective resolution of $\mathbb Z/n$ as a $\mathbb Z$-module:
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0.
\]
Apply $\mathrm{Hom}_{\mathbb Z}(-,A)$:
\[
0 \to \mathrm{Hom}(\mathbb Z/n,A) \to \mathrm{Hom}(\mathbb Z,A)\xrightarrow{\times n} \mathrm{Hom}(\mathbb Z,A)\to \mathrm{Ext}^1(\mathbb Z/n,A)\to 0.
\]
Using $\mathrm{Hom}(\mathbb Z,A)\cong A$, the last map shows
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\;\cong\; \mathrm{coker}(A \xrightarrow{\times n} A)\;\cong\; A/nA.
\]
In particular, $\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong \mathbb Z/n$.

### Example 3: $\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong \mathbb Z/\gcd(n,m)$
From Example 2 with $A=\mathbb Z/m$,
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong (\mathbb Z/m)/n(\mathbb Z/m)\cong \mathbb Z/\gcd(n,m).
\]

(For these cyclic $\mathbb Z$-modules, $\mathrm{Ext}^i_{\mathbb Z}(\mathbb Z/n,-)=0$ for $i\ge 2$ because $\mathbb Z/n$ has projective dimension $1$.)
