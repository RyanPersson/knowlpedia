---
title: "Tor"
description: "The left derived functors of tensor product; measures failure of tensor to be left exact (flatness)."
---

Let $R$ be a {{< knowl id="ring" section="algebra-rings" text="ring" >}}.

To form a tensor product over $R$ in full generality, one typically takes a right $R$-module $M$ and a left $R$-module $N$, producing an abelian group
\[
M \otimes_R N,
\]
see {{< knowl id="tensor-product" section="algebra-modules" text="tensor product" >}}. (If $R$ is commutative, one may treat both as left $R$-modules.)

## Definition (via a projective resolution)
Choose a {{< knowl id="projective-resolution" text="projective resolution" >}} $P_\bullet \to M$ by projective right $R$-modules:
\[
\cdots \to P_2 \to P_1 \to P_0 \to M \to 0.
\]
Tensor with $N$ to obtain a {{< knowl id="chain-complex" text="chain complex" >}} $P_\bullet \otimes_R N$, and define
\[
\mathrm{Tor}^R_n(M,N)\;:=\; H_n(P_\bullet \otimes_R N),
\]
where $H_n(-)$ denotes {{< knowl id="homology-module" text="homology" >}}.

This is well-defined up to canonical isomorphism and is functorial in both variables.

## Basic properties
- $\mathrm{Tor}^R_0(M,N)\cong M\otimes_R N$.
- Because {{< knowl id="tensor-right-exact" text="tensor is right exact" >}}, the derived functors $\mathrm{Tor}^R_n$ measure precisely the *failure* of tensor to be left exact. In particular, a module $N$ is {{< knowl id="flat-module" section="algebra-modules" text="flat" >}} iff $\mathrm{Tor}^R_1(-,N)=0$ (equivalently, iff tensoring with $N$ preserves injections).
- Any {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}} gives rise to a {{< knowl id="long-exact-sequence-tor" text="long exact sequence in Tor" >}}, a special case of {{< knowl id="long-exact-sequence-derived" text="the long exact sequence for derived functors" >}}.

## Examples

### Example 1: Vector spaces over a field
If $k$ is a field and $V,W$ are $k$-vector spaces, every $k$-module is free (hence projective), so
\[
\mathrm{Tor}^k_n(V,W)=0 \quad (n>0), \qquad \mathrm{Tor}^k_0(V,W)=V\otimes_k W.
\]

### Example 2: $\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n, A)\cong A[n]$
Use the standard projective resolution of $\mathbb Z/n$:
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0.
\]
Tensor with $A$ to get
\[
0 \to A \xrightarrow{\times n} A \to (\mathbb Z/n)\otimes_{\mathbb Z} A \to 0.
\]
The homology at the left term is
\[
\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n, A)\;\cong\;\ker(A \xrightarrow{\times n} A)\;=\;\{a\in A : na=0\}=:A[n].
\]
Also $(\mathbb Z/n)\otimes_{\mathbb Z}A\cong A/nA$, so $\mathrm{Tor}^{\mathbb Z}_0(\mathbb Z/n,A)\cong A/nA$.

### Example 3: $\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,\mathbb Z/m)\cong \mathbb Z/\gcd(n,m)$
From Example 2 with $A=\mathbb Z/m$, the $n$-torsion subgroup has order $\gcd(n,m)$ and is cyclic, hence
\[
\mathrm{Tor}^{\mathbb Z}_1(\mathbb Z/n,\mathbb Z/m)\cong \mathbb Z/\gcd(n,m).
\]

(As in the Ext computations over $\mathbb Z$, these cyclic modules have projective dimension $1$, so $\mathrm{Tor}^{\mathbb Z}_i(\mathbb Z/n,-)=0$ for $i\ge 2$.)
