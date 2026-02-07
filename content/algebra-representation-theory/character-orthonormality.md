---
title: "Orthonormality of irreducible characters"
description: "With respect to the standard inner product on class functions, irreducible characters are orthonormal (and over ℂ they form an orthonormal basis)."
---

Let \(G\) be a finite group, and let \(\mathrm{Cl}(G;\mathbb C)\) denote the \(\mathbb C\)-vector space of complex-valued {{< knowl id="class-function" section="algebra-groups" text="class functions" >}} on \(G\).

## The standard inner product on class functions
Define an {{< knowl id="inner-product" section="linear-algebra" text="inner product" >}} on \(\mathrm{Cl}(G;\mathbb C)\) by
\[
\langle f,g\rangle \;:=\; \frac{1}{|G|}\sum_{x\in G} f(x)\,\overline{g(x)}.
\]
Equivalently, if the sum is taken over {{< knowl id="conjugacy-class" section="algebra-groups" text="conjugacy classes" >}} \(C\subseteq G\),
\[
\langle f,g\rangle \;=\; \sum_{C} \frac{|C|}{|G|}\, f(C)\,\overline{g(C)},
\]
since \(f,g\) are constant on each class.

For a (finite-dimensional complex) {{< knowl id="group-representation" text="representation" >}} \(V\) with {{< knowl id="character" text="character" >}} \(\chi_V(g)=\mathrm{tr}(V(g))\) (using {{< knowl id="trace" section="linear-algebra" text="trace" >}}), the inner product \(\langle \chi_V,\chi_W\rangle\) measures overlap between \(V\) and \(W\).

## Orthonormality statement
Let \(\chi,\psi\) be {{< knowl id="irreducible-character" text="irreducible characters" >}} of \(G\) (over \(\mathbb C\)). Then
\[
\langle \chi,\psi\rangle \;=\; \delta_{\chi,\psi}
\]
(i.e. \(1\) if \(\chi=\psi\) and \(0\) otherwise).

This is often presented as the “character orthogonality relations”; see {{< knowl id="character-orthogonality" text="character orthogonality" >}}.

## Consequences
1. **Multiplicity formula.**  
   If \(V\) is a complex representation with character \(\chi_V\) and \(\chi_i\) is irreducible, then the multiplicity \(m_i\) of the corresponding irreducible representation in \(V\) is
   \[
   m_i \;=\; \langle \chi_V,\chi_i\rangle \in \mathbb Z_{\ge 0}.
   \]
   This uses {{< knowl id="maschkes-theorem" text="Maschke's theorem" >}} / {{< knowl id="completely-reducible-representation" text="complete reducibility" >}} over \(\mathbb C\).

2. **Orthonormal basis of class functions (over \(\mathbb C\)).**  
   The irreducible characters form an orthonormal basis of \(\mathrm{Cl}(G;\mathbb C)\). In particular, every class function \(f\) has a unique expansion
   \[
   f \;=\; \sum_i \langle f,\chi_i\rangle\, \chi_i.
   \]
   The spanning/basis part is tied to {{< knowl id="number-irreducibles-conjugacy-classes" text="the number of irreducibles equals the number of conjugacy classes" >}}.

3. **Character tables as unitary matrices (after normalization).**  
   Writing the character table with rows \(\chi_i\) and columns indexed by conjugacy classes, orthonormality implies the rows are orthonormal with respect to the weights \(|C|/|G|\). (There is also a “column orthogonality” relation, equivalent to the same set of facts.)

## Examples

### Example 1: Cyclic group \(C_n\)
Let \(G=C_n=\langle a\rangle\) with \(|G|=n\), and fix \(\zeta=e^{2\pi i/n}\). The irreducible characters are 1-dimensional:
\[
\chi_k(a^m)=\zeta^{km}\qquad (k=0,1,\dots,n-1).
\]
Then
\[
\langle \chi_k,\chi_\ell\rangle
=\frac1n\sum_{m=0}^{n-1}\zeta^{km}\overline{\zeta^{\ell m}}
=\frac1n\sum_{m=0}^{n-1}\zeta^{(k-\ell)m}
=\begin{cases}
1,&k=\ell,\\
0,&k\ne \ell,
\end{cases}
\]
since the sum is a geometric series.

### Example 2: \(S_3\)
The group \(S_3\) has three conjugacy classes: \(1\), transpositions, and 3-cycles, with sizes \(1,3,2\). Its irreducible characters are:

| class | size | representative | \(\chi_{\mathrm{triv}}\) | \(\chi_{\mathrm{sgn}}\) | \(\chi_{\mathrm{std}}\) |
|---:|---:|:---:|---:|---:|---:|
| \(C_1\) | 1 | \(e\) | 1 | 1 | 2 |
| \(C_2\) | 3 | \((12)\) | 1 | \(-1\) | 0 |
| \(C_3\) | 2 | \((123)\) | 1 | 1 | \(-1\) |

Check orthonormality using
\(\langle \chi,\psi\rangle=\sum_C \frac{|C|}{6}\chi(C)\overline{\psi(C)}\):

- \(\langle \chi_{\mathrm{triv}},\chi_{\mathrm{sgn}}\rangle
=\frac16(1\cdot 1\cdot 1 + 3\cdot 1\cdot (-1) + 2\cdot 1\cdot 1)=0.\)

- \(\langle \chi_{\mathrm{std}},\chi_{\mathrm{std}}\rangle
=\frac16(1\cdot 2^2 + 3\cdot 0^2 + 2\cdot (-1)^2)=\frac16(4+0+2)=1.\)

- \(\langle \chi_{\mathrm{std}},\chi_{\mathrm{triv}}\rangle
=\frac16(1\cdot 2\cdot 1 + 3\cdot 0\cdot 1 + 2\cdot (-1)\cdot 1)=0.\)

Thus the three irreducible characters are orthonormal.

### Example 3: Dihedral group \(D_4\) of order \(8\)
Let \(D_4=\langle r,s \mid r^4=s^2=1,\; srs=r^{-1}\rangle\). Its conjugacy classes can be taken as
\(\{1\}, \{r^2\}, \{r,r^3\}, \{s,r^2s\}, \{rs,r^3s\}\)
with sizes \(1,1,2,2,2\).

The unique 2-dimensional irreducible character \(\chi_{2}\) has values
\[
\chi_{2}(1)=2,\quad \chi_{2}(r^2)=-2,\quad
\chi_{2}(r)=\chi_{2}(r^3)=0,\quad \chi_{2}(s)=\chi_{2}(rs)=0
\]
(and hence \(0\) on both reflection classes).

Then
\[
\langle \chi_{2},\chi_{2}\rangle
=\frac18\Big(1\cdot 2^2 + 1\cdot (-2)^2 + 2\cdot 0^2 + 2\cdot 0^2 + 2\cdot 0^2\Big)
=\frac18(4+4)=1.
\]
Also, against the trivial character \(\mathbf{1}\),
\[
\langle \chi_{2},\mathbf{1}\rangle
=\frac18\Big(1\cdot 2\cdot 1 + 1\cdot (-2)\cdot 1 + 0\Big)=0,
\]
so \(\chi_2\) is orthogonal to the 1-dimensional characters, as orthonormality predicts.
