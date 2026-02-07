---
title: "Existence of injective resolutions"
description: "Every module embeds into an injective module, hence admits an injective resolution."
---

Let \(R\) be a ring and \(M\) a left \(R\)-{{< knowl id="module" section="algebra-modules" text="module" >}}.

## Statement
An **{{< knowl id="injective-resolution" text="injective resolution" >}}** of \(M\) is an exact augmented {{< knowl id="cochain-complex" text="cochain complex" >}}
\[
0 \to M \xrightarrow{\iota} I^0 \xrightarrow{d^0} I^1 \xrightarrow{d^1} I^2 \xrightarrow{d^2} \cdots
\]
such that each \(I^n\) is an {{< knowl id="injective-module" section="algebra-modules" text="injective module" >}}.

**Theorem (existence).** Every \(R\)-module \(M\) admits an injective resolution.

Equivalently, the category of \(R\)-modules has **enough injectives**: every module embeds into an injective module.

A standard route to this theorem uses either injective envelopes or explicit “large” injective modules constructed via character modules; {{< knowl id="baers-criterion" section="algebra-modules" text="Baer’s criterion" >}} is a key tool in many proofs and examples.

## Construction (iterating embeddings)
1. Choose a monomorphism \(M \hookrightarrow I^0\) with \(I^0\) injective.
2. Let \(C^0 := \operatorname{coker}(M \hookrightarrow I^0)\).
3. Choose a monomorphism \(C^0 \hookrightarrow I^1\) with \(I^1\) injective, and iterate.

Splicing the resulting short exact sequences yields an exact cochain complex
\[
0 \to M \to I^0 \to I^1 \to I^2 \to \cdots
\]
as required.

Cross-links: {{< knowl id="injective-resolution" text="injective resolutions" >}}, {{< knowl id="hom-left-exact" text="left exactness of Hom" >}}, {{< knowl id="derived-functor" text="derived functors" >}}.

## Examples

### Example 1: An injective resolution of \(\mathbb Z\) as a \(\mathbb Z\)-module
Injective \(\mathbb Z\)-modules are the divisible abelian groups. The inclusion \(\mathbb Z \hookrightarrow \mathbb Q\) has cokernel \(\mathbb Q/\mathbb Z\), and both \(\mathbb Q\) and \(\mathbb Q/\mathbb Z\) are divisible, hence injective. Thus
\[
0 \longrightarrow \mathbb Z \longrightarrow \mathbb Q \longrightarrow \mathbb Q/\mathbb Z \longrightarrow 0
\]
is an injective resolution of \(\mathbb Z\) of length \(1\).

### Example 2: An injective resolution of \(\mathbb Z/n\mathbb Z\)
The subgroup of \(\mathbb Q/\mathbb Z\) consisting of elements of order dividing \(n\) is isomorphic to \(\mathbb Z/n\mathbb Z\), giving an injection \(\mathbb Z/n\mathbb Z \hookrightarrow \mathbb Q/\mathbb Z\). Moreover, multiplication by \(n\) on \(\mathbb Q/\mathbb Z\) is surjective with kernel \(\mathbb Z/n\mathbb Z\). Hence
\[
0 \longrightarrow \mathbb Z/n\mathbb Z \longrightarrow \mathbb Q/\mathbb Z \xrightarrow{\;\cdot n\;} \mathbb Q/\mathbb Z \longrightarrow 0
\]
is an injective resolution of \(\mathbb Z/n\mathbb Z\) of length \(1\).

### Example 3: Over a field, resolutions are trivial
If \(R=k\) is a field, every \(k\)-vector space is injective (and projective). So for any \(k\)-module \(V\),
\[
0 \to V \xrightarrow{\mathrm{id}} V \to 0 \to \cdots
\]
is an injective resolution.
