---
title: "Natural isomorphism"
description: "A natural transformation whose components are isomorphisms."
---

Let \(F,G:\mathcal C\to\mathcal D\) be {{< knowl id="functor" text="functors" >}}.

A **natural isomorphism** \(\eta:F\Rightarrow G\) is a {{< knowl id="natural-transformation" text="natural transformation" >}} such that for every {{< knowl id="object" text="object" >}} \(X\in\mathcal C\), the component
\[
\eta_X:F(X)\to G(X)
\]
is an {{< knowl id="isomorphism-category" text="isomorphism" >}} in \(\mathcal D\).

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
   In any category with {{< knowl id="categorical-product" text="binary products" >}}, there is a natural isomorphism
   \[
   \sigma_{A,B}:A\times B \xrightarrow{\cong} B\times A
   \]
   characterized by \(\pi_1\circ \sigma_{A,B}=\pi_2\) and \(\pi_2\circ \sigma_{A,B}=\pi_1\).  
   In \(\mathbf{Set}\) it is the function \((a,b)\mapsto(b,a)\); in \(\mathbf{Grp}\) it is the group homomorphism \((g,h)\mapsto(h,g)\).

3. **Swap of summands for coproducts**.  
   Dually, in any category with {{< knowl id="coproduct" text="binary coproducts" >}}, there is a natural isomorphism
   \[
   A\sqcup B \xrightarrow{\cong} B\sqcup A
   \]
   induced by the universal property of the coproduct.  
   In \(\mathbf{Set}\) this is the obvious bijection between disjoint unions; in \(\mathbf{Ab}\) it is the canonical isomorphism \(A\oplus B\cong B\oplus A\).
