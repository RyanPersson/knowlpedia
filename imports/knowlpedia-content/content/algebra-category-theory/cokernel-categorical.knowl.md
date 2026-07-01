+++
id = "algebra-category-theory/cokernel-categorical"
title = "Cokernel (categorical)"
kind = "knowl"
summary = "In a pointed category, the cokernel of f:A→B is the coequalizer of f and the zero morphism A→B."
aliases = ["cokernel-categorical", "Cokernel (categorical)"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/cokernel-categorical.md"
+++

Cokernels are dual to [[algebra-category-theory/kernel-categorical|kernels]], capturing “quotienting out by the image of \(f\)” in contexts where that makes sense.

Throughout, assume \(\mathcal C\) is a [[algebra-category-theory/category|category]] with a zero object (e.g. any [[algebra-category-theory/additive-category|additive category]]), hence zero morphisms \(0_{A,B}:A\to B\).

## Definition (Cokernel)
Given a morphism \(f:A\to B\) in \(\mathcal C\), a **cokernel** of \(f\) is a morphism
\[
q:B\to Q
\]
such that:
1. \(q\circ f = 0_{A,Q}\), and
2. (Universal property) for every morphism \(s:B\to T\) with \(s\circ f=0_{A,T}\), there exists a unique morphism \(v:Q\to T\) with
   \[
   v\circ q = s.
   \]

Equivalently, \(q:B\to Q\) is a [[algebra-category-theory/coequalizer|coequalizer]] of the parallel pair \(f,0_{A,B}:A\rightrightarrows B\).

A cokernel, if it exists, is unique up to unique [[algebra-category-theory/isomorphism-category|isomorphism]]. Cokernels are [[algebra-category-theory/epimorphism-category|epimorphisms]] (because coequalizers are epic).

## Examples
1. **\(\mathbf{Ab}\).** For \(f:A\to B\) a homomorphism, \(\operatorname{coker}(f)\cong B/\operatorname{im}(f)\), and the cokernel map is the quotient \(B\twoheadrightarrow B/\operatorname{im}(f)\).

2. **\(R\)\(-\)\(\mathbf{Mod}\).** For \(f:M\to N\) an \(R\)-linear map, \(\operatorname{coker}(f)\cong N/\operatorname{im}(f)\).

3. **\(\mathbf{Grp}\).** For a group homomorphism \(f:G\to H\), the cokernel is the quotient
   \[
   H \twoheadrightarrow H/\langle\!\langle f(G)\rangle\!\rangle
   \]
   where \(\langle\!\langle f(G)\rangle\!\rangle\) is the normal closure of the subgroup \(f(G)\) in \(H\). (This is the coequalizer of \(f\) and the trivial map \(G\to H\).)
