+++
id = "algebra-category-theory/monomorphism-category"
title = "Monomorphism"
kind = "knowl"
summary = "A morphism that is left-cancellative under composition."
aliases = ["monomorphism-category", "Monomorphism"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/monomorphism-category.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]]. A morphism \(f : X \to Y\) is a **monomorphism** (or **mono**) if for every object \(Z\) and all morphisms \(g_1,g_2 : Z \to X\),
\[
f\circ g_1 = f\circ g_2 \quad \Longrightarrow \quad g_1 = g_2,
\]
where \(\circ\) denotes [[algebra-category-theory/composition-category|composition]].

Equivalently: \(f\) is mono iff it is **left-cancellative** with respect to composition.

Notes:
- Every [[algebra-category-theory/isomorphism-category|isomorphism]] is a monomorphism.
- The “dual” notion is [[algebra-category-theory/epimorphism-category|epimorphism]] (right-cancellative).

## Examples
1. In \(\mathbf{Set}\), monomorphisms are exactly [[shared-foundations/injective-function|injective functions]].
2. In \(\mathbf{Grp}\), monomorphisms are exactly injective group homomorphisms.
3. In \(R\text{-}\mathbf{Mod}\) (and in \(\mathbf{Ab}\)), monomorphisms are exactly injective module homomorphisms.
