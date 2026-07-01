+++
id = "algebra-category-theory/opposite-category"
title = "Opposite Category"
kind = "knowl"
summary = "The category obtained by reversing the direction of every morphism."
aliases = ["opposite-category", "Opposite Category"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/opposite-category.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]].

The **opposite category** \(\mathcal C^{\mathrm{op}}\) is the category defined by:
- \(\mathrm{Ob}(\mathcal C^{\mathrm{op}})=\mathrm{Ob}(\mathcal C)\);
- for objects \(A,B\),
  \[
  \mathrm{Hom}_{\mathcal C^{\mathrm{op}}}(A,B) := \mathrm{Hom}_{\mathcal C}(B,A).
  \]
So a [[algebra-category-theory/morphism|morphism]] \(f:A\to B\) in \(\mathcal C^{\mathrm{op}}\) is “the same arrow” as a morphism \(f:B\to A\) in \(\mathcal C\).

## Composition and identities
- The [[algebra-category-theory/identity-morphism|identity morphism]] on an object \(A\) is the same arrow \(\mathrm{id}_A\) as in \(\mathcal C\).
- [[algebra-category-theory/composition-category|Composition]] is reversed: if
  \[
  f:A\to B,\quad g:B\to C \quad \text{in } \mathcal C^{\mathrm{op}},
  \]
  then in \(\mathcal C\) these correspond to \(f:B\to A\) and \(g:C\to B\), and the composite in \(\mathcal C^{\mathrm{op}}\) is defined by
  \[
  g\circ_{\mathcal C^{\mathrm{op}}} f := f\circ_{\mathcal C} g.
  \]

## Basic facts
- Taking opposites is involutive: \((\mathcal C^{\mathrm{op}})^{\mathrm{op}}=\mathcal C\).
- Many constructions come in dual pairs via \(\mathcal C \leftrightarrow \mathcal C^{\mathrm{op}}\).
  For instance, a morphism is a [[algebra-category-theory/monomorphism-category|monomorphism]] in \(\mathcal C\) iff it is an [[algebra-category-theory/epimorphism-category|epimorphism]] in \(\mathcal C^{\mathrm{op}}\).

## Examples
1. **Posets as categories:** A [[shared-foundations/partial-order|partially ordered set]] \((P,\le)\) can be viewed as a category with a unique morphism \(p\to q\) iff \(p\le q\).
   Its opposite category corresponds to the reversed order \(\ge\).

2. **Contravariance:** A [[algebra-category-theory/contravariant-functor|contravariant functor]] \(F:\mathcal C\to \mathcal D\) can be packaged as an ordinary [[algebra-category-theory/functor|functor]] \(F:\mathcal C^{\mathrm{op}}\to \mathcal D\).

3. **One-object categories from groups:** A group \(G\) defines a category with one object \(*\) and \(\mathrm{End}(*)=G\).
   The opposite category corresponds to reversing multiplication (the “opposite group”); inversion \(g\mapsto g^{-1}\) gives an isomorphism \(G\cong G^{\mathrm{op}}\).
