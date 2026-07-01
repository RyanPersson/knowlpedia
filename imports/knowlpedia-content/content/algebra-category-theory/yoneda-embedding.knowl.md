+++
id = "algebra-category-theory/yoneda-embedding"
title = "Yoneda embedding"
kind = "knowl"
summary = "The fully faithful functor sending an object to its Hom functor (a representable presheaf)."
aliases = ["yoneda-embedding", "Yoneda embedding"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/yoneda-embedding.md"
+++

Let \(\mathcal{C}\) be a locally small [[algebra-category-theory/category|category]]. The **Yoneda embedding** is the [[algebra-category-theory/functor|functor]]
\[
y:\mathcal{C}\longrightarrow \mathbf{Set}^{\mathcal{C}^{op}}
\]
defined as follows:

- On objects \(A\in \mathcal{C}\), set
  \[
  y(A) \;=\; \mathrm{Hom}_{\mathcal{C}}(-,A):\mathcal{C}^{op}\to \mathbf{Set}.
  \]
  This is a [[algebra-category-theory/representable-functor|representable functor]] (a representable presheaf).

- On a morphism \(f:A\to B\), define a [[algebra-category-theory/natural-transformation|natural transformation]]
  \[
  y(f):\mathrm{Hom}_{\mathcal{C}}(-,A)\Rightarrow \mathrm{Hom}_{\mathcal{C}}(-,B)
  \]
  by postcomposition:
  \[
  y(f)_X:\mathrm{Hom}_{\mathcal{C}}(X,A)\to \mathrm{Hom}_{\mathcal{C}}(X,B),\quad (h:X\to A)\mapsto f\circ h.
  \]

Here \(\mathcal{C}^{op}\) is the [[algebra-category-theory/opposite-category|opposite category]] and \(\mathbf{Set}^{\mathcal{C}^{op}}\) is the functor category of presheaves on \(\mathcal{C}\).

## Fundamental property (fully faithful)
By the [[algebra-category-theory/yoneda-lemma|Yoneda lemma]], the functor \(y\) is **fully faithful**: for all objects \(A,B\in\mathcal{C}\),
\[
\mathrm{Hom}_{\mathcal{C}}(A,B)\;\cong\;\mathrm{Nat}\big(\mathrm{Hom}_{\mathcal{C}}(-,A),\,\mathrm{Hom}_{\mathcal{C}}(-,B)\big).
\]
Equivalently, \(\mathcal{C}\) identifies with a [[algebra-category-theory/full-subcategory|full subcategory]] of \(\mathbf{Set}^{\mathcal{C}^{op}}\) whose objects are precisely the representables.

## Examples
### Example (Set)
For a set \(A\), \(y(A)\) is the presheaf
\[
X \longmapsto \mathrm{Hom}_{\mathbf{Set}}(X,A),
\]
the set of functions \(X\to A\). A map \(A\to B\) induces a natural transformation by postcomposition.

### Example (Posets)
Let \((P,\le)\) be a [[shared-foundations/partial-order|partial order]] regarded as a category (one morphism \(x\to y\) iff \(x\le y\)).
Then for \(a\in P\), the presheaf \(y(a)\) sends \(x\) to a singleton set if \(x\le a\), and to the empty set otherwise. Thus \(y(a)\) encodes the principal down-set \(\{x\mid x\le a\}\).

### Example (Grp)
For a group \(G\), \(y(G)\) is the presheaf
\[
H \longmapsto \mathrm{Hom}_{\mathbf{Grp}}(H,G),
\]
the set of group homomorphisms into \(G\). A group homomorphism \(G\to G'\) induces a natural transformation by postcomposition.
