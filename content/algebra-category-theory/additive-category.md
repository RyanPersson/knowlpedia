---
title: "Additive category"
description: "A preadditive category with a zero object and finite biproducts (so finite products and coproducts agree)."
---

An **additive category** is a {{< knowl id="category" text="category" >}} in which morphisms can be added and finite direct sums exist.

A category \(\mathcal A\) is **preadditive** if:
1. For all objects \(A,B\), the set \(\operatorname{Hom}_{\mathcal A}(A,B)\) is an abelian group (written additively).
2. {{< knowl id="composition-category" text="Composition" >}} is bilinear: for morphisms \(f,f':A\to B\) and \(g,g':B\to C\),
   \[
   g\circ (f+f') = g\circ f + g\circ f', \qquad (g+g')\circ f = g\circ f + g'\circ f.
   \]

A preadditive category \(\mathcal A\) is **additive** if, in addition:
3. \(\mathcal A\) has a **zero object** \(0\) (both initial and terminal), hence a distinguished **zero morphism**
   \(0_{A,B}:A\to B\) for all \(A,B\).
4. \(\mathcal A\) has **binary biproducts**: for all objects \(A,B\) there exists an object \(A\oplus B\) with morphisms
   \[
   i_A:A\to A\oplus B,\quad i_B:B\to A\oplus B,\quad
   p_A:A\oplus B\to A,\quad p_B:A\oplus B\to B
   \]
   such that \((A\oplus B, p_A,p_B)\) is a {{< knowl id="categorical-product" text="product" >}} of \(A,B\), and \((A\oplus B, i_A,i_B)\) is a {{< knowl id="coproduct" text="coproduct" >}} of \(A,B\), and the following identities hold:
   \[
   p_A i_A = \mathrm{id}_A,\quad p_B i_B=\mathrm{id}_B,\quad p_A i_B = 0,\quad p_B i_A=0,\quad
   i_A p_A + i_B p_B = \mathrm{id}_{A\oplus B}.
   \]

Equivalently: an additive category is a preadditive category with all finite biproducts (including the empty biproduct, i.e. a zero object). In an additive category, finite products and coproducts agree (up to canonical isomorphism).

## Examples
1. **\(\mathbf{Ab}\).** The category of abelian groups is additive: hom-sets are abelian groups under pointwise addition of homomorphisms, and \(A\oplus B\) is the usual direct sum/product.

2. **\(R\)\(-\)\(\mathbf{Mod}\).** For a ring \(R\), the category of (left) \(R\)-modules is additive, with biproduct given by the direct sum \(M\oplus N\).

3. **Chain complexes.** For any additive category \(\mathcal A\) (e.g. \(\mathbf{Ab}\) or \(R\)\(-\)\(\mathbf{Mod}\)), the category \(\mathbf{Ch}(\mathcal A)\) of chain complexes in \(\mathcal A\) is additive, with biproduct defined degreewise.
