---
title: "Irreducible character"
description: "The character of an irreducible complex representation; these form an orthonormal basis of class functions."
---


Let \(G\) be a finite group. An **irreducible character** of \(G\) is the {{< knowl id="character" text="character" >}} \(\chi_\rho\) of an {{< knowl id="irreducible-representation" text="irreducible (complex) representation" >}} \(\rho:G\to \mathrm{GL}(V)\).

Equivalently, irreducible characters are the characters of the {{< knowl id="simple-module" section="algebra-modules" text="simple" >}} \(\mathbb{C}[G]\)-modules (via the {{< knowl id="group-algebra" text="group algebra" >}} correspondence).

## Orthogonality and completeness (key facts)

Define the standard inner product on complex class functions \(f,g:G\to\mathbb{C}\) by
\[
\langle f,g\rangle=\frac{1}{|G|}\sum_{x\in G} f(x)\,\overline{g(x)}.
\]
Then:

- (**Orthonormality**) Distinct irreducible characters are orthonormal:
  \[
  \langle \chi_i,\chi_j\rangle=\delta_{ij}
  \]
  (see {{< knowl id="character-orthonormality" text="character orthonormality" >}} / {{< knowl id="character-orthogonality" text="character orthogonality" >}}).

- (**Basis of class functions**) The irreducible characters form an orthonormal basis of the vector space of {{< knowl id="class-function" section="algebra-groups" text="class functions" >}} on \(G\). In particular, the number of irreducible characters equals the number of {{< knowl id="conjugacy-class" section="algebra-groups" text="conjugacy classes" >}} (see {{< knowl id="number-irreducibles-conjugacy-classes" text="number of irreducibles = number of conjugacy classes" >}}).

- (**Degree sum-of-squares**) If \(\chi_1,\dots,\chi_r\) are the irreducible characters and \(n_i=\chi_i(e)=\dim(V_i)\), then
  \[
  \sum_{i=1}^r n_i^2 = |G|
  \]
  (see {{< knowl id="sum-squares-degrees" text="sum of squares of degrees" >}}).

## Examples

### Example 1: Cyclic group \(C_n\)
Let \(G=C_n=\langle t\rangle\). Over \(\mathbb{C}\), every irreducible representation is \(1\)-dimensional, hence every irreducible character is a homomorphism \(C_n\to \mathbb{C}^\times\). Fix a primitive \(n\)th root of unity \(\zeta_n\). For \(k=0,1,\dots,n-1\),
\[
\chi_k(t^m)=\zeta_n^{km}
\]
is an irreducible character, and these \(n\) characters are all distinct and exhaust the irreducibles.

### Example 2: \(S_3\) (three irreducible characters)
The group \(S_3\) has three conjugacy classes: \(e\), transpositions \((12)\), and \(3\)-cycles \((123)\). Hence it has three irreducible characters. A standard character table is:

| conjugacy class | size | representative | \(\chi_{\mathrm{triv}}\) | \(\chi_{\mathrm{sgn}}\) | \(\chi_{\mathrm{std}}\) |
|---|---:|---|---:|---:|---:|
| \(e\) | 1 | \(e\) | 1 | 1 | 2 |
| transpositions | 3 | \((12)\) | 1 | \(-1\) | 0 |
| 3-cycles | 2 | \((123)\) | 1 | 1 | \(-1\) |

Here \(\chi_{\mathrm{std}}\) is the \(2\)-dimensional standard character (so \(\chi_{\mathrm{std}}(e)=2\)). The degree-sum formula \(1^2+1^2+2^2=6\) matches \(|S_3|=6\).

### Example 3: Dihedral group \(D_8\) (degrees)
Let \(D_8\) be the dihedral group of order \(8\). It has \(5\) conjugacy classes, hence \(5\) irreducible characters. Their degrees must satisfy \(\sum n_i^2=8\), so the only possibility is
\[
1,1,1,1,2,
\]
i.e. four \(1\)-dimensional irreducible characters and one \(2\)-dimensional irreducible character.
