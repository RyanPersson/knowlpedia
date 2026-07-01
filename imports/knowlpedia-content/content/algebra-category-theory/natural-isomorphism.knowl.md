+++
id = "algebra-category-theory/natural-isomorphism"
title = "Natural isomorphism"
kind = "knowl"
summary = "A natural transformation whose components are isomorphisms."
aliases = ["natural-isomorphism", "Natural isomorphism"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/natural-isomorphism.md"
+++

Let \(F,G:\mathcal C\to\mathcal D\) be [[algebra-category-theory/functor|functors]].

A **natural isomorphism** \(\eta:F\Rightarrow G\) is a [[algebra-category-theory/natural-transformation|natural transformation]] such that for every [[algebra-category-theory/object|object]] \(X\in\mathcal C\), the component
\[
\eta_X:F(X)\to G(X)
\]
is an [[algebra-category-theory/isomorphism-category|isomorphism]] in \(\mathcal D\).

Equivalently, \(\eta\) is a natural isomorphism iff there exists a natural transformation \(\eta^{-1}:G\Rightarrow F\) such that \(\eta^{-1}_X=(\eta_X)^{-1}\) for all \(X\) (and hence \(\eta^{-1}\circ \eta=\mathrm{id}_F\), \(\eta\circ \eta^{-1}=\mathrm{id}_G\)).

## Examples
1. **Double dual on finite-dimensional vector spaces**.
   In \(\mathbf{FinVect}_k\), the canonical maps \(V\to V^{\ast\ast}\) assemble to a natural transformation
   \(\mathrm{Id}\Rightarrow (-)^{\ast\ast}\), and each component is an isomorphism. Hence
   \[
   \mathrm{Id}\;\cong\;(-)^{\ast\ast}
   \]
   naturally on \(\mathbf{FinVect}_k\).

2. **Swap of factors for products**.
   In any category with [[algebra-category-theory/categorical-product|binary products]], there is a natural isomorphism
   \[
   \sigma_{A,B}:A\times B \xrightarrow{\cong} B\times A
   \]
   characterized by \(\pi_1\circ \sigma_{A,B}=\pi_2\) and \(\pi_2\circ \sigma_{A,B}=\pi_1\).
   In \(\mathbf{Set}\) it is the function \((a,b)\mapsto(b,a)\); in \(\mathbf{Grp}\) it is the group homomorphism \((g,h)\mapsto(h,g)\).

3. **Swap of summands for coproducts**.
   Dually, in any category with [[algebra-category-theory/coproduct|binary coproducts]], there is a natural isomorphism
   \[
   A\sqcup B \xrightarrow{\cong} B\sqcup A
   \]
   induced by the universal property of the coproduct.
   In \(\mathbf{Set}\) this is the obvious bijection between disjoint unions; in \(\mathbf{Ab}\) it is the canonical isomorphism \(A\oplus B\cong B\oplus A\).
