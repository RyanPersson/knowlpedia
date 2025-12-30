---
title: "Fundamental Theorem of Symmetric Polynomials"
description: "Every symmetric polynomial is a polynomial in the elementary symmetric polynomials."
---

**Theorem.**  
Let \(R\) be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and consider \(R[x_1,\dots,x_n]\) (a {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}}). A polynomial \(f\in R[x_1,\dots,x_n]\) is **symmetric** if it is invariant under every permutation of the variables.  

Then every symmetric polynomial \(f\) can be written uniquely as
\[
f = F(e_1,\dots,e_n)
\]
for some \(F\in R[t_1,\dots,t_n]\), where \(e_k\) is the \(k\)-th elementary symmetric polynomial:
\[
e_1=\sum_i x_i,\quad e_2=\sum_{i<j}x_ix_j,\ \dots,\ e_n=x_1\cdots x_n.
\]

**Examples.**
1. For \(n=2\), \(x_1^2+x_2^2 = (x_1+x_2)^2 - 2x_1x_2 = e_1^2-2e_2\).
2. For \(n=3\), \(x_1^2+x_2^2+x_3^2 = e_1^2 - 2e_2\).
3. For \(n=2\), \(x_1^3+x_2^3 = (x_1+x_2)^3 - 3(x_1+x_2)(x_1x_2)= e_1^3-3e_1e_2\).

**Related.** {{< knowl id="field" section="algebra-rings" text="fields" >}}, {{< knowl id="fundamental-theorem-galois-theory" text="fundamental theorem of Galois theory" >}}.
