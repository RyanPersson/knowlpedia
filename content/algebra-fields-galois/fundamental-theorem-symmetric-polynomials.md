---
title: "Fundamental theorem of symmetric polynomials"
description: "A symmetric polynomial can be expressed uniquely in terms of the elementary symmetric polynomials."
---

Let \(R\) be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and consider the polynomial ring \(R[x_1,\dots,x_n]\).

A polynomial \(f(x_1,\dots,x_n)\in R[x_1,\dots,x_n]\) is **symmetric** if
\[
f(x_{\sigma(1)},\dots,x_{\sigma(n)}) = f(x_1,\dots,x_n)
\quad\text{for every permutation }\sigma\text{ of }\{1,\dots,n\}.
\]
Define the **elementary symmetric polynomials**
\[
e_k(x_1,\dots,x_n)=\sum_{1\le i_1<\cdots<i_k\le n} x_{i_1}\cdots x_{i_k}
\qquad (k=1,\dots,n).
\]

**Theorem (Fundamental theorem of symmetric polynomials).** For every symmetric polynomial
\(f\in R[x_1,\dots,x_n]\), there exists a unique polynomial \(F\in R[t_1,\dots,t_n]\) such that
\[
f(x_1,\dots,x_n)=F\big(e_1(x_1,\dots,x_n),\dots,e_n(x_1,\dots,x_n)\big).
\]
Equivalently, the subring of symmetric polynomials is a polynomial ring:
\[
R[x_1,\dots,x_n]^{\text{sym}} \cong R[e_1,\dots,e_n].
\]

This theorem is a key bridge to {{< knowl id="galois-group" text="Galois groups" >}}: if \(f\in K[x]\) splits over a {{< knowl id="splitting-field" text="splitting field" >}} as \(\prod_{i=1}^n (x-\alpha_i)\), then the coefficients of \(f\) are (up to signs) exactly the elementary symmetric polynomials in the roots \(\alpha_i\).

### Examples
1. For \(n=2\), with \(e_1=x_1+x_2\) and \(e_2=x_1x_2\),
   \[
   x_1^2+x_2^2 = (x_1+x_2)^2 - 2x_1x_2 = e_1^2 - 2e_2.
   \]

2. For \(n=2\),
   \[
   x_1^3+x_2^3 = (x_1+x_2)^3 - 3(x_1+x_2)(x_1x_2) = e_1^3 - 3e_1e_2.
   \]

3. For \(n=3\), with \(e_1=x_1+x_2+x_3\) and \(e_2=x_1x_2+x_1x_3+x_2x_3\),
   \[
   x_1^2+x_2^2+x_3^2 = e_1^2 - 2e_2.
   \]
   (Note that \(e_3=x_1x_2x_3\) is not needed in this particular expression, but it appears in many others.)
