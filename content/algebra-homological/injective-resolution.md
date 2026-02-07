---
title: "Injective resolution"
description: "An exact cochain complex starting at M and continuing with injective modules, used to compute Ext and right derived functors."
---

Let \(R\) be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} and \(M\) an {{< knowl id="module" section="algebra-modules" text="R-module" >}}.

An **injective resolution** of \(M\) is an augmented {{< knowl id="cochain-complex" text="cochain complex" >}}
\[
0 \to M \xrightarrow{\eta} I^0 \xrightarrow{d^0} I^1 \xrightarrow{d^1} I^2 \xrightarrow{d^2} \cdots
\]
such that:
1. Each \(I^j\) is an {{< knowl id="injective-module" section="algebra-modules" text="injective R-module" >}}.
2. The sequence is exact (i.e. an {{< knowl id="exact-complex" text="exact complex" >}}).

Existence in module categories is guaranteed by {{< knowl id="injective-resolutions-exist" text="injective resolutions exist" >}}.

## What resolutions are for
If \(F\) is a {{< knowl id="hom-left-exact" text="left exact" >}} functor, its right derived functors are computed by applying \(F\) to an injective resolution and taking {{< knowl id="cohomology-module" text="cohomology" >}}; see {{< knowl id="derived-functor" text="derived functor" >}}.

In particular, for any \(R\)-module \(N\),
\[
\mathrm{Ext}_R^n(N,M)
\cong H^n\bigl(\operatorname{Hom}_R(N, I^\bullet)\bigr),
\]
where \(\operatorname{Hom}_R(N,I^\bullet)\) is a cochain complex (see {{< knowl id="ext" text="Ext" >}}).

## Examples

### Example 1: Over a field, injective resolutions are trivial
If \(R=k\) is a field, every \(k\)-vector space is injective. Thus an injective resolution of a \(k\)-vector space \(V\) can be taken as
\[
0\to V \xrightarrow{=} V \to 0 \to 0 \to \cdots,
\]
and therefore $\mathrm{Ext}_k^n(W,V)=0$ for all $n>0$ (see {{< knowl id="ext" text="Ext" >}}).

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
(See {{< knowl id="ext" text="Ext" >}}.)

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
(See {{< knowl id="ext" text="Ext" >}}.)
