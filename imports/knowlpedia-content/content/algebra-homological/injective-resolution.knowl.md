+++
id = "algebra-homological/injective-resolution"
title = "Injective resolution"
kind = "knowl"
summary = "An exact cochain complex starting at M and continuing with injective modules, used to compute Ext and right derived functors."
aliases = ["injective-resolution", "Injective resolution"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/injective-resolution.md"
+++

Let \(R\) be a [[algebra-rings/ring|ring]] and \(M\) an [[algebra-modules/module|R-module]].

An **injective resolution** of \(M\) is an augmented [[algebra-homological/cochain-complex|cochain complex]]
\[
0 \to M \xrightarrow{\eta} I^0 \xrightarrow{d^0} I^1 \xrightarrow{d^1} I^2 \xrightarrow{d^2} \cdots
\]
such that:
1. Each \(I^j\) is an [[algebra-modules/injective-module|injective R-module]].
2. The sequence is exact (i.e. an [[algebra-homological/exact-complex|exact complex]]).

Existence in module categories is guaranteed by [[algebra-homological/injective-resolutions-exist|injective resolutions exist]].

## What resolutions are for
If \(F\) is a [[algebra-homological/hom-left-exact|left exact]] functor, its right derived functors are computed by applying \(F\) to an injective resolution and taking [[algebra-homological/cohomology-module|cohomology]]; see [[algebra-homological/derived-functor|derived functor]].

In particular, for any \(R\)-module \(N\),
\[
\mathrm{Ext}_R^n(N,M)
\cong H^n\bigl(\operatorname{Hom}_R(N, I^\bullet)\bigr),
\]
where \(\operatorname{Hom}_R(N,I^\bullet)\) is a cochain complex (see [[algebra-homological/ext|Ext]]).

## Examples

### Example 1: Over a field, injective resolutions are trivial
If \(R=k\) is a field, every \(k\)-vector space is injective. Thus an injective resolution of a \(k\)-vector space \(V\) can be taken as
\[
0\to V \xrightarrow{=} V \to 0 \to 0 \to \cdots,
\]
and therefore $\mathrm{Ext}_k^n(W,V)=0$ for all $n>0$ (see [[algebra-homological/ext|Ext]]).

### Example 2: An injective resolution of \(\mathbb Z\)
In the category of abelian groups (\(R=\mathbb Z\)), both \(\mathbb Q\) and \(\mathbb Q/\mathbb Z\) are injective (they are divisible groups). The sequence
\[
0\to \mathbb Z \to \mathbb Q \to \mathbb Q/\mathbb Z \to 0
\]
is exact, hence yields an injective resolution of \(\mathbb Z\) of length \(1\).

Using it, one computes
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z)
\cong H^1\bigl(\operatorname{Hom}(\mathbb Z/n,\, [0\to \mathbb Q\to \mathbb Q/\mathbb Z\to 0])\bigr).
\]
Since \(\operatorname{Hom}(\mathbb Z/n,\mathbb Q)=0\) and \(\operatorname{Hom}(\mathbb Z/n,\mathbb Q/\mathbb Z)\cong (\mathbb Q/\mathbb Z)[n]\cong \mathbb Z/n\mathbb Z\), this gives
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong \mathbb Z/n\mathbb Z.
\]
(See [[algebra-homological/ext|Ext]].)

### Example 3: An injective resolution of \(\mathbb Z/n\mathbb Z\) and \(\mathrm{Ext}^1\) between cyclic groups
Embed \(\mathbb Z/n\mathbb Z\) into \(\mathbb Q/\mathbb Z\) as the \(n\)-torsion subgroup \((\mathbb Q/\mathbb Z)[n]\). Multiplication by \(n\) on \(\mathbb Q/\mathbb Z\) has kernel \((\mathbb Q/\mathbb Z)[n]\), so
\[
0\to \mathbb Z/n\mathbb Z \to \mathbb Q/\mathbb Z \xrightarrow{\times n} \mathbb Q/\mathbb Z \to 0
\]
is exact, with injective terms, hence an injective resolution of \(\mathbb Z/n\mathbb Z\).

Applying \(\operatorname{Hom}(\mathbb Z/m,-)\) yields
\[
0\to \operatorname{Hom}(\mathbb Z/m,\mathbb Q/\mathbb Z)\xrightarrow{\times n}
\operatorname{Hom}(\mathbb Z/m,\mathbb Q/\mathbb Z)\to 0,
\]
and \(\operatorname{Hom}(\mathbb Z/m,\mathbb Q/\mathbb Z)\cong (\mathbb Q/\mathbb Z)[m]\cong \mathbb Z/m\mathbb Z\). Therefore
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/m,\mathbb Z/n)
\cong \operatorname{coker}(\times n:\mathbb Z/m\to\mathbb Z/m)
\cong \mathbb Z/\gcd(m,n)\mathbb Z.
\]
(See [[algebra-homological/ext|Ext]].)
