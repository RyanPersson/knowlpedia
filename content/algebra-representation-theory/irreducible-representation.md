---
title: "Irreducible representation"
description: "A nonzero representation with no proper, nontrivial invariant subspaces."
---

Let \((V,\rho)\) be a finite-dimensional {{< knowl id="group-representation" text="group representation" >}} of a group \(G\) over a field \(k\). The representation \(V\neq 0\) is **irreducible** if its only {{< knowl id="subrepresentation" text="subrepresentations" >}} are \(0\) and \(V\) itself.

Equivalently, \(V\) is a **simple** \(k[G]\)-module (compare {{< knowl id="simple-module" section="algebra-modules" text="simple module" >}}).

Irreducible representations are the building blocks of {{< knowl id="completely-reducible-representation" text="completely reducible" >}} ones, and their characters are the {{< knowl id="irreducible-character" text="irreducible characters" >}}.

### Structural consequence (Schur)
A key fact is {{< knowl id="schurs-lemma" text="Schur's lemma" >}}: for irreducible \(V\), \(G\)-equivariant endomorphisms of \(V\) are very restricted (over an algebraically closed field, they are just scalars).

## Examples
1. **Cyclic groups over \(\mathbb{C}\): all irreducibles are 1-dimensional.**  
   For \(C_n=\langle g\mid g^n=1\rangle\) and \(k=\mathbb{C}\), every irreducible representation is
   \[
   \rho_j(g)=\zeta_n^j\in \mathbb{C}^\times,\quad j\in\{0,1,\dots,n-1\},
   \]
   hence \(\dim=1\). (These are precisely the complex characters of \(C_n\).)

2. **Irreducibles of \(S_3\) over \(\mathbb{C}\).**  
   Over \(\mathbb{C}\), the group \(S_3\) has exactly three irreducible representations up to isomorphism:
   - the trivial 1-dimensional representation,
   - the sign 1-dimensional representation \(\mathrm{sgn}\),
   - a 2-dimensional “standard” representation, realized as the action of \(S_3\) on
     \[
     W_{\mathrm{std}}=\{(x_1,x_2,x_3)\in \mathbb{C}^3:\ x_1+x_2+x_3=0\},
     \]
     where \(S_3\) permutes coordinates of \(\mathbb{C}^3\).

3. **Dependence on the field: a representation irreducible over \(\mathbb{R}\) but reducible over \(\mathbb{C}\).**  
   Let \(G=C_3=\langle g\rangle\). Consider \(V=\mathbb{R}^2\) with
   \[
   \rho(g)=\begin{pmatrix}
   \cos(2\pi/3)&-\sin(2\pi/3)\\
   \sin(2\pi/3)&\cos(2\pi/3)
   \end{pmatrix}.
   \]
   This rotation has no real eigenvectors, hence no \(1\)-dimensional \(G\)-invariant subspace; therefore \(V\) is irreducible over \(\mathbb{R}\).
   After extending scalars to \(\mathbb{C}\), \(\rho(g)\) becomes diagonalizable with eigenvalues \(e^{\pm 2\pi i/3}\), so \(V\otimes_{\mathbb{R}}\mathbb{C}\) splits as a direct sum of two \(1\)-dimensional \(\mathbb{C}\)-representations.

See also: {{< knowl id="character-orthogonality" text="character orthogonality" >}}, {{< knowl id="number-irreducibles-conjugacy-classes" text="number of irreducibles and conjugacy classes" >}}.
