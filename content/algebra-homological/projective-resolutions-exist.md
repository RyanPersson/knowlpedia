---
title: "Existence of projective resolutions"
description: "Every module admits a projective (in fact free) resolution."
---

Let \(R\) be a ring and \(M\) a left \(R\)-{{< knowl id="module" section="algebra-modules" text="module" >}}.

## Statement
A **{{< knowl id="projective-resolution" text="projective resolution" >}}** of \(M\) is an exact augmented {{< knowl id="chain-complex" text="chain complex" >}}
\[
\cdots \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{\varepsilon} M \to 0
\]
such that each \(P_i\) is a {{< knowl id="projective-module" section="algebra-modules" text="projective module" >}} and the complex
\[
\cdots \to P_2 \to P_1 \to P_0 \to 0
\]
is {{< knowl id="exact-complex" text="exact" >}} in all positive degrees and has \(H_0 \cong M\) via the augmentation.

**Theorem (existence).** Every \(R\)-module \(M\) admits a projective resolution. In fact, one can choose each \(P_i\) to be a {{< knowl id="free-module" section="algebra-modules" text="free module" >}} (a *free resolution*).

Equivalently, the category of \(R\)-modules has **enough projectives**: every module is a quotient of a projective module.

## Construction (standard free resolution)
Choose a surjection \(F_0 \twoheadrightarrow M\) with \(F_0\) free (e.g. take \(F_0 = R^{(M)}\), the free module on the underlying set of \(M\)). Let
\[
K_1 := \ker(F_0 \twoheadrightarrow M).
\]
Then choose a surjection \(F_1 \twoheadrightarrow K_1\) with \(F_1\) free, set \(K_2 := \ker(F_1 \twoheadrightarrow K_1)\), and iterate. Splicing these short exact sequences produces an exact complex
\[
\cdots \to F_2 \to F_1 \to F_0 \to M \to 0
\]
with all \(F_i\) free, hence projective.

Cross-links: {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequences" >}}, {{< knowl id="chain-complex" text="chain complexes" >}}, {{< knowl id="projective-resolution" text="projective resolutions" >}}.

## Examples

### Example 1: A length-1 resolution of \(\mathbb Z/n\mathbb Z\) over \(\mathbb Z\)
As a \(\mathbb Z\)-module,
\[
0 \longrightarrow \mathbb Z \xrightarrow{\;\cdot n\;} \mathbb Z \longrightarrow \mathbb Z/n\mathbb Z \longrightarrow 0
\]
is exact, and the two copies of \(\mathbb Z\) are free (hence projective). Thus it is a projective resolution of \(\mathbb Z/n\mathbb Z\).

### Example 2: The principal-ideal case \(R/(f)\)
For any ring \(R\) and element \(f\in R\), the sequence
\[
0 \longrightarrow R \xrightarrow{\;\cdot f\;} R \longrightarrow R/(f) \longrightarrow 0
\]
is exact if and only if multiplication by \(f\) is injective (e.g. if \(f\) is not a zero-divisor). When exact, it gives a projective (free) resolution of \(R/(f)\) of length \(1\).

### Example 3: \(k\) as a \(k[x]\)-module
Let \(R=k[x]\) and \(k \cong R/(x)\) with \(x\) acting by \(0\). Then
\[
0 \longrightarrow R \xrightarrow{\;\cdot x\;} R \longrightarrow k \longrightarrow 0
\]
is a free resolution of \(k\) as an \(R\)-module.
