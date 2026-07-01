+++
id = "lie-groups/classification-simple-lie-algebras"
title = "Classification of complex simple Lie algebras"
kind = "knowl"
summary = "Complex simple Lie algebras are classified by connected Dynkin diagrams of types A–G."
aliases = ["classification-simple-lie-algebras", "Classification of complex simple Lie algebras"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/classification-simple-lie-algebras.md"
+++

**Theorem (classification).** Every finite-dimensional complex [[lie-groups/simple-lie-algebra|simple Lie algebra]] is isomorphic to exactly one of the Lie algebras in the following families:
- Type $A_n$ ($n\ge 1$): $\mathfrak{sl}_{n+1}(\mathbb{C})$,
- Type $B_n$ ($n\ge 2$): $\mathfrak{so}_{2n+1}(\mathbb{C})$,
- Type $C_n$ ($n\ge 3$): $\mathfrak{sp}_{2n}(\mathbb{C})$,
- Type $D_n$ ($n\ge 4$): $\mathfrak{so}_{2n}(\mathbb{C})$,
- Exceptional types: $E_6,E_7,E_8,F_4,G_2$.

Equivalently, complex simple Lie algebras are classified by connected [[lie-groups/dynkin-diagram|Dynkin diagrams]], or by indecomposable [[lie-groups/cartan-matrix|Cartan matrices]] satisfying the Cartan axioms.

**Semisimple corollary.** Every complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] is a [[lie-groups/semisimple-direct-sum-simple|direct sum of simple ideals]], so its isomorphism type is determined by a (finite) multiset of Dynkin diagram types.

**Context.** The classification proceeds by choosing a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] $\mathfrak{h}$, analyzing the associated [[lie-groups/root-system|root system]] in $\mathfrak{h}^*$, and encoding the relative geometry of [[lie-groups/simple-root|simple roots]] in the Dynkin diagram. The root-system combinatorics precisely controls the Lie bracket via the [[lie-groups/root-space-decomposition|root space decomposition]].
