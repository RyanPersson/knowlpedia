---
title: "Hom is left exact"
description: "Hom preserves kernels: Hom_R(M,-) is left exact (covariant) and Hom_R(-,N) is left exact (contravariant); Ext measures the failure of exactness beyond that."
---

Let $R$ be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} and write {{< knowl id="hom-module" section="algebra-modules" text="$\mathrm{Hom}_R(-,-)$" >}} for the Hom functor.

## Statement (covariant in the second variable)
Fix a left $R$-module $M$. If
\[
0 \to A' \xrightarrow{u} A \xrightarrow{v} A''
\]
is an exact sequence of left $R$-modules, then
\[
0 \to \mathrm{Hom}_R(M,A') \xrightarrow{u_*} \mathrm{Hom}_R(M,A) \xrightarrow{v_*} \mathrm{Hom}_R(M,A'')
\]
is exact.

Equivalently: $\mathrm{Hom}_R(M,-)$ preserves kernels (and monomorphisms), but it need not preserve cokernels (and epimorphisms).

## Statement (contravariant in the first variable)
Fix a left $R$-module $N$. If
\[
A' \xrightarrow{u} A \xrightarrow{v} A'' \to 0
\]
is exact, then applying $\mathrm{Hom}_R(-,N)$ yields an exact sequence
\[
0 \to \mathrm{Hom}_R(A'',N) \xrightarrow{v^*} \mathrm{Hom}_R(A,N) \xrightarrow{u^*} \mathrm{Hom}_R(A',N).
\]

## Failure of right exactness and Ext
The failure of $\mathrm{Hom}$ to be exact is measured by {{< knowl id="ext" text="Ext" >}}: $\mathrm{Ext}^1_R(-,N)$ (and higher $\mathrm{Ext}^n$) are the {{< knowl id="derived-functor" text="right derived functors" >}} of $\mathrm{Hom}_R(-,N)$, and every {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}} gives a {{< knowl id="long-exact-sequence-ext" text="long exact sequence in Ext" >}} (a special case of {{< knowl id="long-exact-sequence-derived" text="the long exact sequence for derived functors" >}}).

If $M$ is {{< knowl id="projective-module" section="algebra-modules" text="projective" >}}, then $\mathrm{Hom}_R(M,-)$ is exact. If $N$ is {{< knowl id="injective-module" section="algebra-modules" text="injective" >}}, then $\mathrm{Hom}_R(-,N)$ is exact.

## Examples

### Example 1: Hom need not be right exact (over $\mathbb Z$)
Start from the short exact sequence
\[
0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n \to 0.
\]
Apply $\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$. Since $\mathrm{Hom}(\mathbb Z/n,\mathbb Z)=0$ and $\mathrm{Hom}(\mathbb Z,\mathbb Z)\cong \mathbb Z$, we get
\[
0 \to 0 \to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\to 0.
\]
The map $\mathbb Z\xrightarrow{\times n}\mathbb Z$ is not surjective for $|n|>1$, so $\mathrm{Hom}(-,\mathbb Z)$ fails to preserve the cokernel; the cokernel is
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong \mathbb Z/n.
\]

### Example 2: If $M$ is free, then Hom is exact
If $M\cong R^{\oplus r}$ is free, then
\[
\mathrm{Hom}_R(M,A)\cong A^{\oplus r}.
\]
Thus $\mathrm{Hom}_R(M,-)$ is a finite product of the identity functor, hence exact (it preserves both kernels and cokernels).

### Example 3: Vector spaces over a field
If $k$ is a field and $V$ is a $k$-vector space, then $V$ is free (hence projective). Therefore $\mathrm{Hom}_k(V,-)$ is exact, and equivalently
\[
\mathrm{Ext}^n_k(V,W)=0 \quad (n>0)
\]
for all $k$-vector spaces $W$.
