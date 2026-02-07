---
title: "Long exact sequence for derived functors"
description: "A short exact sequence induces a long exact sequence on left/right derived functors via connecting morphisms."
---

Derived functors (see {{< knowl id="derived-functor" text="derived functors" >}}) turn short exact sequences into long exact sequences in homology/cohomology. Conceptually, this is a systematic abstraction of the {{< knowl id="snake-lemma" text="snake lemma" >}} and its boundary map; see also {{< knowl id="connecting-homomorphism-lemma" text="connecting homomorphisms" >}}.

## Theorem (left derived functors)
Let $\mathcal A,\mathcal B$ be {{< knowl id="abelian-category" section="algebra-category-theory" text="abelian categories" >}} and let
\[
F:\mathcal A \to \mathcal B
\]
be an additive functor that is right exact. Assume $\mathcal A$ has enough projectives, so the left derived functors $L_nF$ exist.

Then for every {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}}
\[
0 \to A' \xrightarrow{u} A \xrightarrow{v} A'' \to 0
\]
in $\mathcal A$, there are natural connecting morphisms
\[
\delta_n: L_nF(A'') \to L_{n-1}F(A')
\]
such that the following sequence is exact:
\[
\cdots \to L_2F(A) \to L_2F(A'') \xrightarrow{\delta_2} L_1F(A') \to L_1F(A) \to L_1F(A'') \xrightarrow{\delta_1} L_0F(A') \to L_0F(A) \to L_0F(A'') \to 0.
\]
Moreover, $L_0F \cong F$.

## Theorem (right derived functors)
Let $G:\mathcal A\to\mathcal B$ be additive and left exact, and assume $\mathcal A$ has enough injectives so that the right derived functors $R^nG$ exist.

Then every short exact sequence $0\to A'\to A\to A''\to 0$ yields a natural long exact sequence
\[
0 \to G(A') \to G(A) \to G(A'') \xrightarrow{\delta^0} R^1G(A') \to R^1G(A) \to R^1G(A'') \xrightarrow{\delta^1} R^2G(A') \to \cdots.
\]

## Important special cases
- Taking $F(-)=(-)\otimes_R N$ (right exact; see {{< knowl id="tensor-right-exact" text="tensor is right exact" >}}) gives the {{< knowl id="long-exact-sequence-tor" text="long exact sequence in Tor" >}}.
- Taking $G(-)=\mathrm{Hom}_R(-,N)$ (left exact; see {{< knowl id="hom-left-exact" text="Hom is left exact" >}}) gives the {{< knowl id="long-exact-sequence-ext" text="long exact sequence in Ext" >}}.

## Examples

### Example 1: Computing $\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)$ from the long exact sequence
Start with the short exact sequence of $\mathbb Z$-modules
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0.
\]
Apply the right exact functor $(-)\otimes_{\mathbb Z} A$. The left derived functors are $\mathrm{Tor}^{\mathbb Z}_i(-,A)$, and the long exact sequence includes the segment
\[
\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z,A)\to \mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)\to
\mathbb Z\otimes A \xrightarrow{\times n} \mathbb Z\otimes A \to (\mathbb Z/n)\otimes A \to 0.
\]
Since $\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z,A)=0$ and $\mathbb Z\otimes A\cong A$, this simplifies to
\[
0 \to \mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)\to A \xrightarrow{\times n} A \to A/nA \to 0,
\]
so
\[
\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,A)\cong \ker(A \xrightarrow{\times n} A)=A[n].
\]

### Example 2: Computing $\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)$ from the long exact sequence
Apply the left exact functor $\mathrm{Hom}_{\mathbb Z}(-,A)$ to the same short exact sequence:
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0.
\]
The induced long exact sequence in right derived functors yields the segment
\[
0 \to \mathrm{Hom}(\mathbb Z/n,A)\to \mathrm{Hom}(\mathbb Z,A)\xrightarrow{\times n}\mathrm{Hom}(\mathbb Z,A)\to \mathrm{Ext}^1(\mathbb Z/n,A)\to 0.
\]
Using $\mathrm{Hom}(\mathbb Z,A)\cong A$, we get
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong \mathrm{coker}(A \xrightarrow{\times n} A)\cong A/nA.
\]
