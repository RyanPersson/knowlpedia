---
title: "Character of a representation"
description: "The class function χ(g)=tr(ρ(g)) attached to a finite-dimensional representation ρ of a finite group."
---


Let \(G\) be a finite group and let \(\rho:G\to \mathrm{GL}(V)\) be a finite-dimensional complex {{< knowl id="group-representation" text="representation" >}}. The **character** of \(\rho\) is the function
\[
\chi_\rho:G\to \mathbb{C},\qquad \chi_\rho(g)=\mathrm{tr}(\rho(g)),
\]
where \(\mathrm{tr}\) is the {{< knowl id="trace" section="linear-algebra" text="trace" >}} of a linear operator on \(V\).

## Basic properties

1. **Class function.** For all \(g,h\in G\),
\[
\chi_\rho(hgh^{-1})=\chi_\rho(g).
\]
Equivalently, \(\chi_\rho\) is constant on {{< knowl id="conjugacy-class" section="algebra-groups" text="conjugacy classes" >}}, i.e. it is a {{< knowl id="class-function" section="algebra-groups" text="class function" >}}.

2. **Isomorphism invariance.** If \(\rho\simeq \rho'\) (isomorphic representations), then \(\chi_\rho=\chi_{\rho'}\).

3. **Additivity and multiplicativity.**
   - For a {{< knowl id="character-direct-sum" text="direct sum" >}} \(\rho\oplus \sigma\),
     \[
     \chi_{\rho\oplus \sigma}=\chi_\rho+\chi_\sigma.
     \]
   - For a {{< knowl id="character-tensor-product" text="tensor product" >}} \(\rho\otimes \sigma\),
     \[
     \chi_{\rho\otimes \sigma}(g)=\chi_\rho(g)\,\chi_\sigma(g).
     \]

4. **Dimension.** \(\chi_\rho(e)=\dim_\mathbb{C}V\).

Characters are central tools because many structural questions about representations reduce to identities among class functions and the {{< knowl id="character-orthogonality" text="orthogonality relations" >}}.

## Examples

### Example 1: Trivial representation
If \(\rho\) is the trivial representation on \(V\) (every \(g\) acts as \(\mathrm{id}_V\)), then
\[
\chi_\rho(g)=\mathrm{tr}(\mathrm{id}_V)=\dim V
\]
for all \(g\in G\).

### Example 2: Regular representation
Let \(\mathbb{C}[G]\) be the {{< knowl id="group-algebra" text="group algebra" >}} and let \(G\) act by left multiplication (the {{< knowl id="regular-representation" text="regular representation" >}}). Its character satisfies
\[
\chi_{\mathrm{reg}}(e)=|G|,\qquad 
\chi_{\mathrm{reg}}(g)=0\ \text{for }g\neq e.
\]
(For \(g\neq e\), left multiplication by \(g\) permutes the basis \(\{\delta_h\}\) without fixed points, so the corresponding permutation matrix has trace \(0\).)

### Example 3: The standard \(2\)-dimensional representation of \(S_3\)
Let \(S_3\) act on \(\mathbb{C}^3\) by permuting coordinates, and restrict to the \(2\)-dimensional subspace
\[
W=\{(x_1,x_2,x_3)\in \mathbb{C}^3 : x_1+x_2+x_3=0\},
\]
which is \(S_3\)-stable. The resulting representation \(\rho_{\mathrm{std}}\) has character values (constant on conjugacy classes):
- \(\chi_{\mathrm{std}}(e)=2\),
- \(\chi_{\mathrm{std}}(\text{a transposition})=0\),
- \(\chi_{\mathrm{std}}(\text{a 3-cycle})=-1\).
This is the character of the unique \(2\)-dimensional irreducible representation of \(S_3\).
