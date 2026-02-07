---
title: "Exact sequence (categorical)"
description: "In an abelian category, a sequence is exact at an object when the image equals the kernel (equivalently, kernels and cokernels fit together appropriately)."
---

Exactness is a condition on a composable string of morphisms measuring “no loss, no redundancy” at each stage.

Because “image” behaves best in an {{< knowl id="abelian-category" text="abelian category" >}}, the standard categorical definition of exact sequences is given in that setting.

## Definition (Exact at an object)
Let \(\mathcal A\) be an {{< knowl id="abelian-category" text="abelian category" >}} and consider a composable pair
\[
A \xrightarrow{f} B \xrightarrow{g} C.
\]
The sequence is **exact at \(B\)** if:
1. \(g\circ f = 0\), and
2. the **image** of \(f\) equals the **kernel** of \(g\) as subobjects of \(B\):
   \[
   \operatorname{im}(f) \;=\; \ker(g).
   \]

In an abelian category one can define the image via kernels and cokernels:
\[
\operatorname{im}(f) := \ker(\operatorname{coker}(f)),
\]
using {{< knowl id="kernel-categorical" text="kernels" >}} and {{< knowl id="cokernel-categorical" text="cokernels" >}}.

A longer sequence
\[
\cdots \to A_{i-1}\xrightarrow{d_{i-1}} A_i \xrightarrow{d_i} A_{i+1}\to \cdots
\]
is **exact** if it is exact at every object \(A_i\), i.e. \(\operatorname{im}(d_{i-1})=\ker(d_i)\) for all \(i\).

## Short exact sequences
A sequence
\[
0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0
\]
is **short exact** if it is exact at \(A\), \(B\), and \(C\). In an abelian category this is equivalent to:
- \(f\) is a {{< knowl id="monomorphism-category" text="monomorphism" >}},
- \(g\) is a {{< knowl id="epimorphism-category" text="epimorphism" >}},
- \(\operatorname{im}(f)=\ker(g)\).

(Here \(0\) denotes a zero object; compare {{< knowl id="additive-category" text="additive category" >}}.)

## Examples
1. **In \(\mathbf{Ab}\): multiplication by \(2\).**
   \[
   0 \to 2\mathbb Z \xrightarrow{\ \iota\ } \mathbb Z \xrightarrow{\ \pi\ } \mathbb Z/2\mathbb Z \to 0,
   \]
   where \(\iota\) is inclusion and \(\pi\) is reduction mod \(2\). Exactness at \(\mathbb Z\) says \(\operatorname{im}(\iota)=2\mathbb Z=\ker(\pi)\).

2. **In \(\mathbf{Ab}\): \(\mathbb Z\subset \mathbb Q\).**
   \[
   0 \to \mathbb Z \to \mathbb Q \to \mathbb Q/\mathbb Z \to 0
   \]
   is short exact: the quotient \(\mathbb Q/\mathbb Z\) measures how \(\mathbb Q\) differs from \(\mathbb Z\).

3. **In \(R\)\(-\)\(\mathbf{Mod}\): principal ideal quotient.** For a ring \(R\) and an element \(x\in R\),
   \[
   R \xrightarrow{\ \cdot x\ } R \to R/(x) \to 0
   \]
   is exact (and is short exact on the left if \(\cdot x\) is injective). Here \((x)\) is the image of the multiplication map, so exactness at the middle \(R\) says \(\operatorname{im}(\cdot x)=\ker(R\twoheadrightarrow R/(x))\).
