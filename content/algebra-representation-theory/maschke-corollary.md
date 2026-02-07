---
title: "Maschke corollary (regular representation decomposition)"
description: "When char(k) does not divide |G|, the group algebra is semisimple and the regular representation splits into irreducibles with multiplicity equal to dimension."
---

Let $G$ be a finite group and let $k$ be a field with $\operatorname{char}(k)\nmid |G|$ (e.g. $k=\mathbb C$). By {{< knowl id="maschkes-theorem" text="Maschke's theorem" >}}, every finite-dimensional {{< knowl id="group-representation" text="representation" >}} of $G$ over $k$ is {{< knowl id="completely-reducible-representation" text="completely reducible" >}}; equivalently every $k[G]$-module is {{< knowl id="semisimple-module" section="algebra-modules" text="semisimple" >}}.

Assume moreover that $k$ is algebraically closed, and let $\{V_1,\dots,V_r\}$ be a complete set of pairwise non-isomorphic finite-dimensional {{< knowl id="irreducible-representation" text="irreducible representations" >}} of $G$, with $d_i=\dim_k(V_i)$.

## Corollary (regular representation decomposition)
As a left $kG$-module (i.e. as a $G$-representation), the {{< knowl id="regular-representation" text="regular representation" >}} decomposes as
\[
k[G]\;\cong\;\bigoplus_{i=1}^r d_i\,V_i.
\]
In particular, each irreducible $V_i$ occurs inside $k[G]$ with multiplicity exactly $\dim(V_i)$.

A closely related (often packaged together) semisimple-algebra statement is that the {{< knowl id="group-algebra" text="group algebra" >}} admits a Wedderburn decomposition
\[
k[G]\;\cong\;\bigoplus_{i=1}^r \operatorname{End}_k(V_i)\;\cong\;\bigoplus_{i=1}^r \mathrm{Mat}_{d_i}(k),
\]
where the second isomorphism uses $\dim(V_i)=d_i$ and algebraic closedness of $k$.

Taking dimensions in the module decomposition gives the formula {{< knowl id="sum-squares-degrees" text="sum of squares of degrees" >}}:
\[
|G|=\dim_k(k[G])=\sum_i d_i^2.
\]

## Examples

1. **$S_3$ (order $6$).**  
   Over $\mathbb C$, the irreducibles are $\mathbf{1}$ (trivial), $\mathrm{sgn}$ (sign), and the $2$-dimensional standard $V$.
   The corollary gives
   \[
   \mathbb C[S_3]\;\cong\; 1\cdot \mathbf{1}\;\oplus\;1\cdot \mathrm{sgn}\;\oplus\;2\cdot V.
   \]
   Dimension check: $1+1+2\cdot 2=6$.

2. **$C_n$ (order $n$).**  
   All irreducibles are $1$-dimensional characters $\chi_0,\dots,\chi_{n-1}$, hence
   \[
   \mathbb C[C_n]\;\cong\;\chi_0\oplus\chi_1\oplus\cdots\oplus\chi_{n-1}.
   \]

3. **$D_8$ (order $8$).**  
   $D_8$ has four $1$-dimensional irreducibles $\chi_1,\dots,\chi_4$ and one $2$-dimensional irreducible $V$, so
   \[
   \mathbb C[D_8]\;\cong\;\chi_1\oplus\chi_2\oplus\chi_3\oplus\chi_4\oplus 2\cdot V,
   \]
   and $4\cdot 1 + 2\cdot 2 = 8$.
