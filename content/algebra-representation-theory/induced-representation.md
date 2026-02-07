---
title: "Induced representation"
description: "A construction Ind_H^G that extends a representation of a subgroup H to a representation of the whole group G."
---

## Definition (finite groups)

Let \(G\) be a finite group, \(H\le G\) a subgroup, and \(\sigma:H\to \mathrm{GL}(W)\) a finite-dimensional complex {{< knowl id="group-representation" text="representation" >}} of \(H\).

The **induced representation** \(\mathrm{Ind}_H^G \sigma\) is the representation of \(G\) on the vector space
\[
\mathrm{Ind}_H^G W
=\Bigl\{\, f:G\to W \ \Bigm|\  f(hg)=\sigma(h)\,f(g)\ \text{for all }h\in H,\ g\in G \Bigr\},
\]
with \(G\)-action given by right translation:
\[
(g_0\cdot f)(g)=f(gg_0)\qquad (g_0,g\in G).
\]
This space is finite-dimensional, and one has the dimension formula
\[
\dim(\mathrm{Ind}_H^G W)=[G:H]\cdot \dim(W),
\]
where \([G:H]\) is the index of \(H\) in \(G\).

## Equivalent module-theoretic description

Using the {{< knowl id="group-algebra" text="group algebra" >}}, induction can be realized as
\[
\mathrm{Ind}_H^G W \;\cong\; \mathbb{C}[G]\otimes_{\mathbb{C}[H]} W,
\]
where \(\mathbb{C}[G]\) is viewed as a \((\mathbb{C}[G],\mathbb{C}[H])\)-{{< knowl id="bimodule" section="algebra-modules" text="bimodule" >}} and \(\otimes\) is the {{< knowl id="tensor-product" section="algebra-modules" text="tensor product" >}} over \(\mathbb{C}[H]\).

## Relationship with restriction (Frobenius reciprocity)

Let \(\mathrm{Res}_H^G V\) denote the {{< knowl id="restricted-representation" text="restricted representation" >}} of a \(G\)-representation \(V\) to \(H\). Then induction is left adjoint to restriction: there is a natural vector space isomorphism
\[
\mathrm{Hom}_G(\mathrm{Ind}_H^G W,\; V)\;\cong\;\mathrm{Hom}_H(W,\; \mathrm{Res}_H^G V),
\]
where \(\mathrm{Hom}\) denotes {{< knowl id="module-homomorphism" section="algebra-modules" text="module homomorphisms" >}} in the appropriate categories.

## Examples

### Example 1: Inducing the trivial representation gives a permutation representation
Let \(\sigma\) be the trivial \(1\)-dimensional representation of \(H\). Then \(\mathrm{Ind}_H^G \sigma\) is naturally isomorphic to the permutation representation of \(G\) on the set of left {{< knowl id="coset" section="algebra-groups" text="cosets" >}} \(G/H\).

Special case: if \(H=\{e\}\), then \(G/H\cong G\) and \(\mathrm{Ind}_{\{e\}}^G \mathbf{1}\) is the {{< knowl id="regular-representation" text="regular representation" >}}.

### Example 2: \(S_3\) induced from an \(S_2\) subgroup
Let \(G=S_3\) and \(H\cong S_2\) be the stabilizer of \(3\) (so \([G:H]=3\)). Induce the trivial representation of \(H\):
\[
\mathrm{Ind}_{S_2}^{S_3} \mathbf{1}.
\]
This is the \(3\)-dimensional permutation representation of \(S_3\) on \(\{1,2,3\}\). It decomposes as
\[
\mathrm{Ind}_{S_2}^{S_3}\mathbf{1}\ \cong\ \mathbf{1}\ \oplus\ \rho_{\mathrm{std}},
\]
i.e. a \(1\)-dimensional invariant subspace (spanned by \((1,1,1)\)) plus the \(2\)-dimensional standard representation (compare {{< knowl id="completely-reducible-representation" text="complete reducibility" >}}).

### Example 3: Cyclic example \(C_4\) induced from \(C_2\)
Let \(G=C_4=\langle t\rangle\) and \(H=\langle t^2\rangle\cong C_2\). Induce the trivial character of \(H\). The induced representation has dimension \([C_4:C_2]\cdot 1 = 2\).

Over \(\mathbb{C}\), \(C_4\) has four \(1\)-dimensional characters, and precisely two of them restrict trivially to \(H\): the trivial character and the character sending \(t\mapsto -1\). Accordingly,
\[
\mathrm{Ind}_{C_2}^{C_4}\mathbf{1}\ \cong\ \mathbf{1}\ \oplus\ \chi,
\]
where \(\chi(t)=-1\). This illustrates how induction in abelian groups often decomposes as a direct sum of characters extending the given subgroup character.
