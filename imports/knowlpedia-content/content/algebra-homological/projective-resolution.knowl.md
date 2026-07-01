+++
id = "algebra-homological/projective-resolution"
title = "Projective resolution"
kind = "knowl"
summary = "An exact chain complex of projective modules ending in a given module M, used to compute Tor and Ext."
aliases = ["projective-resolution", "Projective resolution"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/projective-resolution.md"
+++

Let \(R\) be a [[algebra-rings/ring|ring]] and \(M\) an [[algebra-modules/module|R-module]].

A **projective resolution** of \(M\) is an augmented [[algebra-homological/chain-complex|chain complex]]
\[
\cdots \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{\varepsilon} M \to 0
\]
such that:
1. Each \(P_i\) is a [[algebra-modules/projective-module|projective R-module]].
2. The sequence is exact (equivalently, the augmented complex is an [[algebra-homological/exact-complex|exact complex]]).

Equivalently, if \(P_\bullet\) denotes the chain complex \(\cdots\to P_1\to P_0\to 0\) (forgetting the augmentation), then
\[
H_0(P_\bullet)\cong M,\qquad H_i(P_\bullet)=0 \text{ for all } i>0,
\]
where \(H_i\) is the [[algebra-homological/homology-module|homology]] of the underlying chain complex.

A projective resolution is **free** if each \(P_i\) is [[algebra-modules/free-module|free]].

Existence in module categories is guaranteed by [[algebra-homological/projective-resolutions-exist|projective resolutions exist]].

## What resolutions are for
- For any \(R\)-module \(N\), the homology of \(P_\bullet\otimes_R N\) computes [[algebra-homological/tor|Tor]]:
  \[
  H_i(P_\bullet\otimes_R N)\cong \mathrm{Tor}_i^R(M,N).
  \]
  (Tensor is [[algebra-homological/tensor-right-exact|right exact]], so one needs derived functors.)
- Applying \(\operatorname{Hom}_R(P_\bullet,N)\) produces a [[algebra-homological/cochain-complex|cochain complex]] whose cohomology computes [[algebra-homological/ext|Ext]]:
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
(See [[algebra-homological/tor|Tor]].)

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
(See [[algebra-homological/tor|Tor]].)
