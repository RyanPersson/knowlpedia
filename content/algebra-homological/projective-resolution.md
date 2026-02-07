---
title: "Projective resolution"
description: "An exact chain complex of projective modules ending in a given module M, used to compute Tor and Ext."
---

Let \(R\) be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} and \(M\) an {{< knowl id="module" section="algebra-modules" text="R-module" >}}.

A **projective resolution** of \(M\) is an augmented {{< knowl id="chain-complex" text="chain complex" >}}
\[
\cdots \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{\varepsilon} M \to 0
\]
such that:
1. Each \(P_i\) is a {{< knowl id="projective-module" section="algebra-modules" text="projective R-module" >}}.
2. The sequence is exact (equivalently, the augmented complex is an {{< knowl id="exact-complex" text="exact complex" >}}).

Equivalently, if \(P_\bullet\) denotes the chain complex \(\cdots\to P_1\to P_0\to 0\) (forgetting the augmentation), then
\[
H_0(P_\bullet)\cong M,\qquad H_i(P_\bullet)=0 \text{ for all } i>0,
\]
where \(H_i\) is the {{< knowl id="homology-module" text="homology" >}} of the underlying chain complex.

A projective resolution is **free** if each \(P_i\) is {{< knowl id="free-module" section="algebra-modules" text="free" >}}.

Existence in module categories is guaranteed by {{< knowl id="projective-resolutions-exist" text="projective resolutions exist" >}}.

## What resolutions are for
- For any \(R\)-module \(N\), the homology of \(P_\bullet\otimes_R N\) computes {{< knowl id="tor" text="Tor" >}}:
  \[
  H_i(P_\bullet\otimes_R N)\cong \mathrm{Tor}_i^R(M,N).
  \]
  (Tensor is {{< knowl id="tensor-right-exact" text="right exact" >}}, so one needs derived functors.)
- Applying \(\operatorname{Hom}_R(P_\bullet,N)\) produces a {{< knowl id="cochain-complex" text="cochain complex" >}} whose cohomology computes {{< knowl id="ext" text="Ext" >}}:
  \[
  H^i(\operatorname{Hom}_R(P_\bullet,N))\cong \mathrm{Ext}_R^i(M,N).
  \]

## Examples

### Example 1: A projective resolution of \(\mathbb Z/n\mathbb Z\)
Over \(R=\mathbb Z\), the sequence
\[
0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0
\]
is exact, and \(\mathbb Z\) is free (hence projective). Thus it is a projective resolution of \(\mathbb Z/n\mathbb Z\) of length \(1\).

### Example 2: Computing \(\mathrm{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\)
Tensor the resolution in Example 1 with \(\mathbb Z/m\mathbb Z\):
\[
0\to \mathbb Z/m \xrightarrow{\times n} \mathbb Z/m \to 0.
\]
Then
\[
\mathrm{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)
\cong H_1
\cong \ker(\times n:\mathbb Z/m\to\mathbb Z/m)
\cong \mathbb Z/\gcd(m,n)\mathbb Z.
\]
(See {{< knowl id="tor" text="Tor" >}}.)

### Example 3: A resolution of \(k\) as a \(k[x]\)-module
Let \(R=k[x]\) and \(M=R/(x)\cong k\). Then
\[
0\to R \xrightarrow{\times x} R \to k \to 0
\]
is a free (hence projective) resolution of \(k\) of length \(1\). For instance,
\[
\mathrm{Tor}_1^{k[x]}(k,k)
\cong H_1\bigl((0\to R\xrightarrow{x}R\to 0)\otimes_{k[x]}k\bigr)
\cong H_1(0\to k\xrightarrow{0}k\to 0)\cong k.
\]
(See {{< knowl id="tor" text="Tor" >}}.)
