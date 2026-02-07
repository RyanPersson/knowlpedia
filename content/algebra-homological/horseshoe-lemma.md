---
title: "Horseshoe lemma"
description: "Given a short exact sequence of modules, compatible projective (or injective) resolutions can be spliced to produce a resolution of the middle module."
---

Let \(R\) be a ring and
\[
0 \longrightarrow A \xrightarrow{i} B \xrightarrow{p} C \longrightarrow 0
\]
a short exact sequence of \(R\)-modules (see {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}}).

## Statement (projective version)
Suppose we are given projective resolutions
\[
\cdots \to P_1^A \to P_0^A \to A \to 0,
\qquad
\cdots \to P_1^C \to P_0^C \to C \to 0
\]
with each \(P_n^A, P_n^C\) {{< knowl id="projective-module" section="algebra-modules" text="projective" >}}. Then there exists a projective resolution of \(B\),
\[
\cdots \to P_1^B \to P_0^B \to B \to 0,
\]
and chain maps fitting into a short exact sequence of chain complexes
\[
0 \to P_\bullet^A \to P_\bullet^B \to P_\bullet^C \to 0
\]
such that \(P_n^B \cong P_n^A \oplus P_n^C\) for all \(n\), and the augmentation maps recover \(0\to A\to B\to C\to 0\) in degree \(0\).

Equivalently: you can “splice” the two resolutions into one, degreewise as a direct sum, with differentials chosen so that exactness holds.

## Statement (injective version)
Dually, given injective resolutions of \(A\) and \(C\), one constructs an injective resolution of \(B\) with \(I^n_B \cong I^n_A \oplus I^n_C\) and a short exact sequence of cochain complexes
\[
0 \to I^\bullet_A \to I^\bullet_B \to I^\bullet_C \to 0.
\]
(See {{< knowl id="injective-resolution" text="injective resolution" >}} and {{< knowl id="injective-module" section="algebra-modules" text="injective modules" >}}.)

## Why it matters
The horseshoe lemma underlies functorial constructions of the long exact sequences in {{< knowl id="tor" text="Tor" >}} and {{< knowl id="ext" text="Ext" >}} (see {{< knowl id="long-exact-sequence-tor" text="long exact sequence for Tor" >}} and {{< knowl id="long-exact-sequence-ext" text="long exact sequence for Ext" >}}), and is a standard way to build resolutions needed to compute derived functors (see {{< knowl id="derived-functor" text="derived functor" >}}).

## Examples

### Example 1 (building a resolution of \(\mathbb Z/6\) from \(\mathbb Z/2\) and \(\mathbb Z/3\))
In \(\mathbf{Ab}\) (i.e. \(R=\mathbb Z\)), there is a short exact sequence
\[
0 \to \mathbb Z/2 \to \mathbb Z/6 \to \mathbb Z/3 \to 0.
\]
Use the standard projective resolutions
\[
0\to \mathbb Z \xrightarrow{\cdot 2} \mathbb Z \to \mathbb Z/2 \to 0,\qquad
0\to \mathbb Z \xrightarrow{\cdot 3} \mathbb Z \to \mathbb Z/3 \to 0.
\]
Horseshoe produces a resolution of \(\mathbb Z/6\) with
\[
P_1^B \cong \mathbb Z\oplus \mathbb Z,\quad P_0^B \cong \mathbb Z\oplus \mathbb Z,
\]
and an exact sequence of complexes \(0\to P_\bullet^{\mathbb Z/2}\to P_\bullet^{\mathbb Z/6}\to P_\bullet^{\mathbb Z/3}\to 0\).
This is not minimal, but it is explicit and sufficient to compute {{< knowl id="tor" text="Tor" >}} and {{< knowl id="ext" text="Ext" >}} groups.

### Example 2 (computing \(\operatorname{Tor}_1\) from a short exact sequence)
Let \(0\to A\to B\to C\to 0\) be short exact and fix an \(R\)-module \(N\).
Take a projective resolution \(P_\bullet^B\) of \(B\). By horseshoe, you can choose compatible resolutions so that \(0\to P_\bullet^A\to P_\bullet^B\to P_\bullet^C\to 0\) is exact.
Tensoring degreewise with \(N\) gives a short exact sequence of chain complexes (tensor is right exact; see {{< knowl id="tensor-right-exact" text="tensor is right exact" >}}), and the resulting long exact homology sequence identifies the connecting map as the boundary in
{{< knowl id="long-exact-sequence-tor" text="the long exact sequence of Tor" >}}.

### Example 3 (injective horseshoe and \(\operatorname{Ext}\))
If you want \(\operatorname{Ext}^n_R(-,I)\) computations, an injective horseshoe lets you choose compatible injective resolutions to compute
\[
\operatorname{Ext}^n_R(C,M)\to \operatorname{Ext}^n_R(B,M)\to \operatorname{Ext}^n_R(A,M)
\]
via a short exact sequence of cochain complexes and the induced long exact cohomology sequence (see {{< knowl id="long-exact-sequence-ext" text="long exact sequence for Ext" >}}).
