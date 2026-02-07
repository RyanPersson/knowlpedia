---
title: "Regular representation"
description: "The canonical representation of a group on the vector space with basis the group, via left multiplication."
---

Let \(G\) be a finite group and \(k\) a field.

## Definition (left regular representation)
The **left regular representation** of \(G\) over \(k\) is the {{< knowl id="group-representation" text="representation" >}}
\[
\lambda: G \longrightarrow \mathrm{GL}\big(k[G]\big)
\]
on the {{< knowl id="group-algebra" text="group algebra" >}} \(k[G]\), where \(k[G]\) is the \(k\)-vector space with basis \(\{e_g : g\in G\}\) and the action is
\[
\lambda(h)(e_g) \;=\; e_{hg}\qquad (g,h\in G).
\]
Equivalently, \(G\) acts by left multiplication on \(k[G]\).

(There is also a right regular representation \(e_g\mapsto e_{gh^{-1}}\), which is generally different but closely related.)

## Character of the regular representation (over \(\mathbb C\))
Over \(\mathbb C\), the {{< knowl id="character" text="character" >}} \(\chi_{\mathrm{reg}}\) of the regular representation satisfies
\[
\chi_{\mathrm{reg}}(1)=|G|,\qquad \chi_{\mathrm{reg}}(g)=0\ \text{ for }g\ne 1.
\]
Reason: \(\lambda(g)\) permutes the basis \(\{e_h\}\); it has fixed points iff \(g=1\), and the trace of a permutation matrix equals the number of fixed basis vectors.

## Decomposition over \(\mathbb C\)
If \(\{V_i\}\) runs over the {{< knowl id="irreducible-representation" text="irreducible representations" >}} of \(G\) over \(\mathbb C\), with \(\dim V_i = d_i\), then the regular representation decomposes as
\[
\mathbb C[G] \;\cong\; \bigoplus_i d_i\, V_i.
\]
In particular,
\[
|G|=\dim \mathbb C[G] = \sum_i d_i^2,
\]
which is the content of {{< knowl id="sum-squares-degrees" text="the sum of squares formula" >}}. The index \(i\) ranges over exactly as many irreducibles as there are {{< knowl id="conjugacy-class" section="algebra-groups" text="conjugacy classes" >}} (see {{< knowl id="number-irreducibles-conjugacy-classes" text="number of irreducibles equals number of conjugacy classes" >}}).

## Examples
1. **Cyclic group \(C_n\) over \(\mathbb C\).**  
   All irreducibles of \(C_n\) are 1-dimensional characters \(\chi_j(g)=\zeta_n^{j}\) (for \(j=0,\dots,n-1\)). Hence
   \[
   \mathbb C[C_n]\;\cong\;\bigoplus_{j=0}^{n-1}\chi_j,
   \]
   i.e. the regular representation splits into \(n\) distinct 1-dimensional representations.

2. **\(S_3\) over \(\mathbb C\).**  
   The irreducible degrees are \(1,1,2\) (trivial, sign, standard). Therefore
   \[
   \mathbb C[S_3] \;\cong\; \mathbf{1}\;\oplus\;\mathrm{sgn}\;\oplus\;2\cdot V_{\mathrm{std}}.
   \]
   The multiplicity of each irreducible equals its dimension.

3. **Dihedral group \(D_4\) of order \(8\) over \(\mathbb C\).**  
   \(D_4\) has four 1-dimensional irreducibles and one 2-dimensional irreducible \(V\). Thus
   \[
   \mathbb C[D_4] \;\cong\; \chi_1\oplus\chi_2\oplus\chi_3\oplus\chi_4 \;\oplus\; 2\cdot V,
   \]
   and \(8 = 1^2+1^2+1^2+1^2+2^2\).
