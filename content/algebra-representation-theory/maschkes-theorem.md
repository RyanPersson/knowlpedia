---
title: "Maschke's theorem"
description: "If char(k) does not divide |G|, then every finite-dimensional k-representation of a finite group is completely reducible."
---

Let \(G\) be a finite group and \(k\) a field. Consider finite-dimensional {{< knowl id="group-representation" text="representations" >}} of \(G\) over \(k\), equivalently finite-dimensional \(kG\)-modules.

## Theorem (Maschke)
Assume that \(|G|\) is invertible in \(k\) (equivalently \(\mathrm{char}(k)\nmid |G|\)). Then every finite-dimensional \(k\)-representation \(V\) of \(G\) is **semisimple**: for every \(G\)-{{< knowl id="subrepresentation" text="subrepresentation" >}} \(W\subseteq V\), there exists a \(G\)-stable subspace \(U\subseteq V\) such that
\[
V \;=\; W \oplus U
\]
as \(G\)-representations (equivalently as \(kG\)-modules). In particular, every representation is {{< knowl id="completely-reducible-representation" text="completely reducible" >}}.

In module language: every finite-dimensional \(kG\)-module is a {{< knowl id="semisimple-module" section="algebra-modules" text="semisimple module" >}}.

## Standard averaging proof (key construction)
Let \(W\subseteq V\) be \(G\)-stable. Choose any \(k\)-linear projection \(p:V\to W\) (not necessarily \(G\)-equivariant). Define the averaged map
\[
p_G(v) \;=\; \frac{1}{|G|}\sum_{g\in G} g\cdot p(g^{-1}\cdot v).
\]
Then:
- \(p_G\) is \(G\)-equivariant, i.e. a {{< knowl id="module-homomorphism" section="algebra-modules" text="module homomorphism" >}} \(V\to W\),
- \(p_G|_W = \mathrm{id}_W\), so \(p_G\) is a \(G\)-equivariant projection,
- therefore \(\ker(p_G)\) is \(G\)-stable and gives the complement \(U=\ker(p_G)\).

This averaging step is exactly where the condition \(\frac{1}{|G|}\in k\) is used.

## Remarks and consequences
- Over \(k=\mathbb C\), Maschke always applies to finite groups, yielding {{< knowl id="complete-reducibility-complex" text="complete reducibility over \u211a" >}}.
- The theorem is equivalent to semisimplicity of the {{< knowl id="group-algebra" text="group algebra" >}} \(k[G]\) (as a ring), and it underlies character theory (e.g. {{< knowl id="character-orthogonality" text="orthogonality of irreducible characters" >}}).

## Examples
1. **A “good characteristic” decomposition for \(S_3\) over \(\mathbb C\).**  
   Let \(S_3\) act on \(\mathbb C^3\) by permuting coordinates (a permutation representation). The 1-dimensional subspace
   \[
   W = \{(a,a,a):a\in\mathbb C\}
   \]
   is \(S_3\)-stable (the trivial subrepresentation). Maschke guarantees an invariant complement, and indeed one is
   \[
   U=\{(x_1,x_2,x_3)\in\mathbb C^3 : x_1+x_2+x_3=0\},
   \]
   giving \(\mathbb C^3 \cong W \oplus U\), where \(U\) is the 2-dimensional standard irreducible.

2. **A “good characteristic” example where not all irreducibles are 1D.**  
   Take \(G=C_3=\langle g\rangle\) over \(k=\mathbb F_2\). Since \(\mathrm{char}(\mathbb F_2)=2\nmid 3\), Maschke applies: every \(\mathbb F_2[C_3]\)-module is semisimple.  
   In particular, \(\mathbb F_2[C_3]\) (the regular representation) decomposes as a direct sum of irreducibles, but over \(\mathbb F_2\) there is a 2-dimensional irreducible factor (because \(x^2+x+1\) is irreducible over \(\mathbb F_2\)). So semisimple does **not** mean “splits into 1-dimensional pieces”; it means “splits into irreducibles over the given field.”

3. **Failure in “bad characteristic”: \(C_p\) over \(\mathbb F_p\).**  
   Let \(G=C_p=\langle g\rangle\) and \(k=\mathbb F_p\), so \(\mathrm{char}(k)=p\mid |G|\). Consider the 2-dimensional representation \(V=k^2\) where \(g\) acts by the unipotent matrix
   \[
   \rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
   \]
   The line \(W=\langle e_1\rangle\) is \(G\)-stable, but there is **no** \(G\)-stable complement line: the only eigenvectors of \(\rho(g)\) lie in \(\langle e_1\rangle\), so no other 1-dimensional subspace is preserved. Hence \(V\) is not a direct sum of subrepresentations, and Maschke’s conclusion fails.
