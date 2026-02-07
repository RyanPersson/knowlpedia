---
title: "Completely reducible representation"
description: "A representation that splits as a direct sum of irreducible subrepresentations."
---

Let \((V,\rho)\) be a finite-dimensional {{< knowl id="group-representation" text="group representation" >}} of \(G\) over a field \(k\). The representation \(V\) is **completely reducible** if there exist irreducible subrepresentations \(V_1,\dots,V_r\) such that
\[
V \cong V_1 \oplus \cdots \oplus V_r
\]
as \(G\)-representations (i.e. as \(k[G]\)-modules). Here \(\oplus\) is the {{< knowl id="direct-sum-modules" section="algebra-modules" text="direct sum" >}} in the module/representation sense.

Equivalently, \(V\) is completely reducible iff **every** {{< knowl id="subrepresentation" text="subrepresentation" >}} \(W\subseteq V\) has a \(G\)-stable complement: there exists a subrepresentation \(U\subseteq V\) such that
\[
V = W \oplus U.
\]
In module language, this is exactly: \(V\) is a {{< knowl id="semisimple-module" section="algebra-modules" text="semisimple module" >}} over the {{< knowl id="group-algebra" text="group algebra" >}} \(k[G]\).

### Maschke’s criterion
If \(G\) is finite and \(\mathrm{char}(k)\nmid |G|\), then **every** finite-dimensional \(k\)-representation of \(G\) is completely reducible: this is {{< knowl id="maschkes-theorem" text="Maschke’s theorem" >}}.
In particular, over \(k=\mathbb{C}\), all finite-group representations are completely reducible (see {{< knowl id="complete-reducibility-complex" text="complete reducibility over \u211d/\u2102" >}}).

## Examples
1. **A completely reducible permutation representation of \(S_3\) over \(\mathbb{C}\).**  
   Let \(V=\mathbb{C}^3\) with \(S_3\) permuting coordinates. Then the subspaces
   \[
   W_{\mathrm{triv}}=\mathrm{span}\{(1,1,1)\},\qquad
   W_{\mathrm{std}}=\{(x_1,x_2,x_3):x_1+x_2+x_3=0\}
   \]
   are \(S_3\)-stable and
   \[
   \mathbb{C}^3 = W_{\mathrm{triv}} \oplus W_{\mathrm{std}}.
   \]
   Here \(W_{\mathrm{triv}}\) is trivial and \(W_{\mathrm{std}}\) is {{< knowl id="irreducible-representation" text="irreducible" >}}.

2. **Regular representations over \(\mathbb{C}\) split into irreducibles with multiplicities.**  
   For a finite group \(G\), the {{< knowl id="regular-representation" text="regular representation" >}} \(\mathbb{C}[G]\) is completely reducible and decomposes as
   \[
   \mathbb{C}[G]\ \cong\ \bigoplus_{i} (\dim V_i)\, V_i,
   \]
   where \(\{V_i\}\) runs over the irreducible \(\mathbb{C}\)-representations of \(G\). Taking dimensions yields
   \[
   |G|=\sum_i (\dim V_i)^2,
   \]
   i.e. {{< knowl id="sum-squares-degrees" text="the sum of squares of degrees" >}} identity.

3. **A non-example in characteristic \(p\mid |G|\): no invariant complement.**  
   Let \(G=C_p=\langle g\rangle\) and \(k=\mathbb{F}_p\). On \(V=k^2\), define
   \[
   \rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
   \]
   The line \(W=\mathrm{span}\{e_1\}\) is \(G\)-stable, so it is a subrepresentation. If \(V\) were completely reducible, there would be a \(G\)-stable complementary line \(U\) with \(V=W\oplus U\). But \(\rho(g)\) has only one eigenline in characteristic \(p\), namely \(W\), so no such \(U\) exists. Hence \(V\) is **not** completely reducible.

See also: {{< knowl id="maschke-corollary" text="Maschke corollary" >}}, {{< knowl id="character-direct-sum" text="character of a direct sum" >}}.
