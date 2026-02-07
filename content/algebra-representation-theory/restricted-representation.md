---
title: "Restricted representation"
description: "Given a representation of a group and a subgroup, the restriction is the same action viewed only on the subgroup."
---

Let \(G\) be a group, \(H\le G\) a subgroup, and let \((V,\rho)\) be a (finite-dimensional) {{< knowl id="group-representation" text="representation" >}} of \(G\) over a field \(k\), i.e. a homomorphism
\[
\rho: G \longrightarrow \mathrm{GL}(V).
\]

## Definition (restriction)
The **restricted representation** of \((V,\rho)\) from \(G\) to \(H\) is the representation
\[
\mathrm{Res}^G_H(V,\rho)\;:=\;(V,\rho|_H),
\]
where \(\rho|_H: H\to \mathrm{GL}(V)\) is the composite \(H \hookrightarrow G \xrightarrow{\rho} \mathrm{GL}(V)\).

Equivalently, if \(V\) is a \(kG\)-module (via the {{< knowl id="group-algebra" text="group algebra" >}} \(k[G]\)), then \(\mathrm{Res}^G_H V\) is the same vector space \(V\) regarded as a \(kH\)-module by restricting scalars along the inclusion \(k[H]\hookrightarrow k[G]\).

- Any \(G\)-{{< knowl id="subrepresentation" text="subrepresentation" >}} is in particular an \(H\)-subrepresentation after restriction.
- If \(k=\mathbb C\) and \(\chi_V\) is the {{< knowl id="character" text="character" >}} of \(V\), then the character of \(\mathrm{Res}^G_H V\) is simply the pointwise restriction:
\[
\chi_{\mathrm{Res}^G_H V}(h)=\chi_V(h)\quad (h\in H).
\]

Restriction is a functor \(\mathrm{Res}^G_H:\mathrm{Rep}_k(G)\to \mathrm{Rep}_k(H)\), and it pairs naturally with {{< knowl id="induced-representation" text="induction" >}} (see Frobenius reciprocity).

## Examples
1. **Restricting the sign representation \(S_3\to A_3\).**  
   Let \(G=S_3\), \(H=A_3\cong C_3\). The 1-dimensional sign representation \(\mathrm{sgn}:S_3\to\{\pm 1\}\subset \mathbb C^\times\) becomes trivial on \(A_3\) (every element of \(A_3\) is even). Hence
   \[
   \mathrm{Res}^{S_3}_{A_3}(\mathrm{sgn}) \cong \mathbf{1}_{A_3}.
   \]

2. **Restricting the standard 2D representation \(S_3\to A_3\).**  
   Let \(V\) be the 2-dimensional irreducible (standard) representation of \(S_3\) over \(\mathbb C\). Restricting to \(A_3=\langle (123)\rangle\), the element \((123)\) acts as a rotation of order 3 on \(V\). Over \(\mathbb C\), this restriction splits as a direct sum of the two nontrivial 1-dimensional characters of \(C_3\):
   \[
   \mathrm{Res}^{S_3}_{A_3}(V)\;\cong\;\chi_\omega \oplus \chi_{\omega^2},
   \]
   where \(\omega=e^{2\pi i/3}\).

3. **Restricting the regular representation to a subgroup.**  
   Let \(G=S_3\) and let \(H=\langle (12)\rangle\cong C_2\). Consider the {{< knowl id="regular-representation" text="left regular representation" >}} \(k[G]\) with basis \(\{e_g:g\in G\}\) and action \(h\cdot e_g=e_{hg}\). Under restriction to \(H\), the set \(G\) decomposes into 3 left cosets of \(H\), each of size 2. Each coset is an \(H\)-orbit isomorphic (as an \(H\)-set) to \(H\) acting on itself by left translation, so as \(kH\)-modules:
   \[
   \mathrm{Res}^{S_3}_{H}\big(k[G]\big)\;\cong\;k[H]\oplus k[H]\oplus k[H].
   \]
