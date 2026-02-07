---
title: "Irreducibles and Conjugacy Classes"
description: "Over ℂ, the number of irreducible representations equals the number of conjugacy classes of the group."
---

Let \(G\) be a finite group. A **class function** on \(G\) is a function \(f:G\to \mathbb{C}\) constant on each {{< knowl id="conjugacy-class" section="algebra-groups" text="conjugacy class" >}}. The space of class functions is denoted
\[
\mathrm{Cl}(G)=\{f:G\to \mathbb{C} \mid f(xgx^{-1})=f(g)\ \forall x,g\in G\}.
\]
(See {{< knowl id="class-function" section="algebra-groups" text="class function" >}}.)

Every complex {{< knowl id="group-representation" text="representation" >}} \(V\) has a {{< knowl id="character" text="character" >}} \(\chi_V\in \mathrm{Cl}(G)\), and irreducible representations have {{< knowl id="irreducible-character" text="irreducible characters" >}}.

## Theorem
Let \(G\) be a finite group. Over \(\mathbb{C}\), the number of isomorphism classes of {{< knowl id="irreducible-representation" text="irreducible representations" >}} of \(G\) equals the number of conjugacy classes of \(G\).

### Equivalent formulation (via class functions)
The irreducible characters \(\{\chi_1,\dots,\chi_r\}\) form an orthonormal basis of \(\mathrm{Cl}(G)\) with respect to the standard inner product
\[
\langle f,h\rangle=\frac{1}{|G|}\sum_{g\in G} f(g)\overline{h(g)}.
\]
In particular,
\[
r=\dim_\mathbb{C}\mathrm{Cl}(G).
\]
But \(\dim_\mathbb{C}\mathrm{Cl}(G)\) is the number of conjugacy classes (a class function is determined by its values on conjugacy classes), so \(r\) equals the number of conjugacy classes.

This perspective is tightly linked to {{< knowl id="character-orthonormality" text="character orthonormality" >}} (and {{< knowl id="character-orthogonality" text="character orthogonality" >}}).

## Examples

### Example 1: Abelian groups
If \(G\) is abelian, every conjugacy class is a singleton, so the number of conjugacy classes is \(|G|\). The theorem implies \(G\) has \(|G|\) irreducible complex representations. Indeed, all irreducibles are 1-dimensional characters, and there are exactly \(|G|\) of them (e.g. for \(C_n\), the characters \(g\mapsto \zeta^k\), \(k=0,\dots,n-1\)).

### Example 2: \(S_3\)
The symmetric group \(S_3\) has 3 conjugacy classes:
\[
\{e\},\quad \{\text{transpositions}\},\quad \{\text{3-cycles}\}.
\]
Hence it has exactly 3 irreducible complex representations: the trivial representation, the sign representation, and the 2-dimensional standard representation.

### Example 3: Dihedral group \(D_8\) (order 8)
Let \(D_8=\langle r,s \mid r^4=1,\ s^2=1,\ srs=r^{-1}\rangle\). Its conjugacy classes are
\[
\{1\},\ \{r^2\},\ \{r,r^3\},\ \{s,r^2s\},\ \{rs,r^3s\},
\]
so there are 5 conjugacy classes. Therefore \(D_8\) has exactly 5 irreducible complex representations (in fact: four 1-dimensional and one 2-dimensional).
