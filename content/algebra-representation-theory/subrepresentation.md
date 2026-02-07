---
title: "Subrepresentation"
description: "An invariant subspace of a representation, closed under the group action."
---

Let \((V,\rho)\) be a {{< knowl id="group-representation" text="group representation" >}} of a group \(G\) over a field \(k\). A **subrepresentation** of \(V\) is a \(k\)-subspace \(W\subseteq V\) such that
\[
\rho(g)(W)\subseteq W\quad\text{for all } g\in G.
\]
Equivalently, \(W\) is a **\(G\)-invariant subspace** of \(V\). In that case, restricting \(\rho\) gives a representation \((W,\rho|_W)\).

In the {{< knowl id="group-algebra" text="group algebra" >}} viewpoint, subrepresentations are exactly \(k[G]\)-submodules.

### Basic properties
- The inclusion \(i:W\hookrightarrow V\) is a homomorphism of representations (a \(G\)-equivariant {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}}).
- If \(W\) is a subrepresentation, one can form the quotient vector space \(V/W\), which carries an induced \(G\)-action by \(\overline{v}\mapsto \overline{\rho(g)v}\) (well-defined precisely because \(W\) is \(G\)-stable).

Subrepresentations are the objects whose absence (except \(0\) and \(V\)) defines {{< knowl id="irreducible-representation" text="irreducibility" >}}.

## Examples
1. **Permutation representation of \(S_3\) on \(k^3\).**  
   Let \(V=k^3\) with \(S_3\) acting by permuting coordinates:
   \[
   \rho(\sigma)(e_i)=e_{\sigma(i)}.
   \]
   Then the line
   \[
   W_{\mathrm{triv}}=\mathrm{span}\{(1,1,1)\}
   \]
   is \(S_3\)-invariant, hence a subrepresentation (it is isomorphic to the trivial representation).
   Also the subspace
   \[
   W_{\mathrm{std}}=\{(x_1,x_2,x_3)\in k^3:\ x_1+x_2+x_3=0\}
   \]
   is invariant. When \(\mathrm{char}(k)\nmid 3\), one has a direct sum decomposition
   \[
   k^3 = W_{\mathrm{triv}} \oplus W_{\mathrm{std}},
   \]
   exhibiting complete reducibility in this case (see {{< knowl id="completely-reducible-representation" text="completely reducible representation" >}}).

2. **A canonical 1-dimensional subrepresentation inside the regular representation.**  
   In the {{< knowl id="regular-representation" text="regular representation" >}} of \(G\) on \(k[G]\), the vector
   \[
   \Omega=\sum_{g\in G} g \in k[G]
   \]
   spans a \(G\)-stable line: for any \(h\in G\),
   \[
   h\cdot \Omega = \sum_{g\in G} hg = \sum_{g\in G} g = \Omega.
   \]
   Thus \(k\Omega\) is a subrepresentation isomorphic to the trivial representation.

3. **An invariant line without an invariant complement (modular phenomenon).**  
   Let \(G=C_p=\langle g\rangle\) and \(k=\mathbb{F}_p\). Define a 2-dimensional representation on \(V=k^2\) by
   \[
   \rho(g)=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
   \]
   Then \(W=\mathrm{span}\{e_1\}\) is \(G\)-stable since \(\rho(g)e_1=e_1\). This is a subrepresentation, but (as discussed in {{< knowl id="completely-reducible-representation" text="complete reducibility" >}}) it has no \(G\)-stable complement in \(V\).

See also: {{< knowl id="irreducible-representation" text="irreducible representation" >}}, {{< knowl id="restricted-representation" text="restriction to a subgroup" >}} (different notion).
