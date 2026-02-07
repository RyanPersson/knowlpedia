---
title: "Sum of squares of degrees"
description: "For a finite group, the sum of the squares of the dimensions of its irreducible complex representations equals the group order."
---

Let $G$ be a finite group and let $k$ be an algebraically closed field with $\operatorname{char}(k)\nmid |G|$ (in particular, $k=\mathbb C$).  Let
\[
\{V_1,\dots,V_r\}
\]
be a complete set of pairwise non-isomorphic finite-dimensional {{< knowl id="irreducible-representation" text="irreducible representations" >}} of $G$ over $k$, and write $d_i=\dim_k(V_i)$.

## Theorem (sum of squares of degrees)
\[
\sum_{i=1}^r d_i^2 \;=\; |G|.
\]

Equivalently, the underlying $kG$-module of the {{< knowl id="regular-representation" text="regular representation" >}} decomposes as
\[
k[G]\;\cong\;\bigoplus_{i=1}^r d_i\,V_i,
\]
and taking dimensions gives $\dim_k(k[G])=|G|=\sum_i d_i\dim(V_i)=\sum_i d_i^2$.

This decomposition is a standard consequence of {{< knowl id="maschke-corollary" text="Maschke-type semisimplicity statements" >}} (so $k[G]$ is semisimple) together with multiplicity computations using {{< knowl id="schurs-lemma" text="Schur's lemma" >}}.

## Examples

1. **Cyclic group $C_n$.**  
   Over $\mathbb C$, every irreducible representation of $C_n$ is $1$-dimensional (a character). There are $n$ such characters, so
   \[
   \sum_i d_i^2 \;=\; \underbrace{1^2+\cdots+1^2}_{n\text{ times}} \;=\; n \;=\; |C_n|.
   \]

2. **Symmetric group $S_3$ (order $6$).**  
   $S_3$ has irreducible degrees $1,1,2$ (trivial, sign, and the $2$-dimensional standard representation), hence
   \[
   1^2+1^2+2^2 \;=\; 6 \;=\; |S_3|.
   \]

3. **Dihedral group $D_8$ (symmetries of a square, order $8$).**  
   $D_8$ has four $1$-dimensional irreducibles and one $2$-dimensional irreducible, so
   \[
   4\cdot 1^2 + 1\cdot 2^2 \;=\; 8 \;=\; |D_8|.
   \]
