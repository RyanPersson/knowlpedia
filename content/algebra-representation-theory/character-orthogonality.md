---
title: "Character orthogonality"
description: "Irreducible complex characters are orthonormal under the standard inner product on class functions."
---

Let \(G\) be a finite group. A (complex) {{< knowl id="character" text="character" >}} \(\chi:G\to\mathbb C\) is a {{< knowl id="class-function" section="algebra-groups" text="class function" >}}: it is constant on each {{< knowl id="conjugacy-class" section="algebra-groups" text="conjugacy class" >}}.

## Inner product on class functions
On the space \(\mathrm{Cl}(G)\) of complex class functions, define
\[
\langle f, g\rangle \;=\; \frac{1}{|G|}\sum_{x\in G} f(x)\,\overline{g(x)}.
\]
This is a Hermitian inner product (compare {{< knowl id="inner-product" section="linear-algebra" text="inner product" >}} and {{< knowl id="orthogonality" section="linear-algebra" text="orthogonality" >}}).

## Theorem (orthogonality of irreducible characters)
Let \(\chi_1,\dots,\chi_r\) be the distinct {{< knowl id="irreducible-character" text="irreducible characters" >}} of \(G\) over \(\mathbb C\). Then:

1. **Row orthogonality (orthonormality):**
   \[
   \langle \chi_i, \chi_j\rangle = \delta_{ij}.
   \]
   In particular, for any character \(\chi\),
   \[
   \langle \chi,\chi\rangle \in \mathbb Z_{\ge 0},
   \]
   and \(\chi\) is irreducible iff \(\langle \chi,\chi\rangle=1\) (see also {{< knowl id="character-orthonormality" text="character orthonormality" >}}).

2. **Completeness:** The set \(\{\chi_1,\dots,\chi_r\}\) is an orthonormal basis of \(\mathrm{Cl}(G)\). Hence \(r=\dim_\mathbb C \mathrm{Cl}(G)\), which equals the number of conjugacy classes (cf. {{< knowl id="number-irreducibles-conjugacy-classes" text="number of irreducibles equals number of conjugacy classes" >}}).

3. **Column orthogonality (one common form):** for \(g,h\in G\),
   \[
   \sum_{i=1}^r \chi_i(g)\,\overline{\chi_i(h)} =
   \begin{cases}
   0, & \text{if } g \text{ and } h \text{ are not conjugate},\\[4pt]
   |C_G(g)|, & \text{if } g \text{ and } h \text{ are conjugate},
   \end{cases}
   \]
   where \(C_G(g)\) is the {{< knowl id="centralizer" section="algebra-groups" text="centralizer" >}} of \(g\). In particular,
   \[
   \sum_{i=1}^r |\chi_i(g)|^2 = |C_G(g)|.
   \]

These identities are proved using complete reducibility (via {{< knowl id="maschkes-theorem" text="Maschke's theorem" >}}), the decomposition of tensor products, and {{< knowl id="schurs-lemma" text="Schur's lemma" >}}.

## Examples
1. **Cyclic group \(C_n\): discrete Fourier orthogonality.**  
   Let \(C_n=\langle t\rangle\). Its irreducible characters are \(\chi_j(t^m)=\zeta_n^{jm}\) for \(j=0,\dots,n-1\). Then
   \[
   \langle \chi_j,\chi_\ell\rangle
   = \frac{1}{n}\sum_{m=0}^{n-1} \zeta_n^{jm}\overline{\zeta_n^{\ell m}}
   = \frac{1}{n}\sum_{m=0}^{n-1} \zeta_n^{(j-\ell)m}
   = \delta_{j\ell}.
   \]

2. **\(S_3\): checking row orthogonality from the character table.**  
   \(S_3\) has three conjugacy classes: \(()\), transpositions, and 3-cycles. Let \(\chi_{\mathrm{triv}},\chi_{\mathrm{sgn}},\chi_{\mathrm{std}}\) be the irreducible characters (degrees \(1,1,2\)). Using the class sizes \(1,3,2\) and values
   \[
   \chi_{\mathrm{triv}}=(1,1,1),\quad
   \chi_{\mathrm{sgn}}=(1,-1,1),\quad
   \chi_{\mathrm{std}}=(2,0,-1),
   \]
   one computes for example
   \[
   \langle \chi_{\mathrm{std}},\chi_{\mathrm{sgn}}\rangle
   =\frac{1}{6}\Big(1\cdot 2\cdot 1 + 3\cdot 0\cdot(-1) + 2\cdot (-1)\cdot 1\Big)=0,
   \]
   and
   \[
   \langle \chi_{\mathrm{std}},\chi_{\mathrm{std}}\rangle
   =\frac{1}{6}\Big(1\cdot |2|^2 + 3\cdot |0|^2 + 2\cdot |-1|^2\Big)=1,
   \]
   confirming orthogonality and irreducibility.

3. **Column orthogonality in \(S_3\): centralizer sizes.**  
   In \(S_3\), a transposition \(\tau\) has centralizer size \(|C_{S_3}(\tau)|=2\). Column orthogonality predicts
   \[
   |\chi_{\mathrm{triv}}(\tau)|^2 + |\chi_{\mathrm{sgn}}(\tau)|^2 + |\chi_{\mathrm{std}}(\tau)|^2
   = |1|^2 + |-1|^2 + |0|^2 = 2,
   \]
   matching \(|C_{S_3}(\tau)|\).
