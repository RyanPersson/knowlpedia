---
title: "Equivalence of categories"
description: "A functor that is invertible up to natural isomorphism."
---

Let \(\mathcal C,\mathcal D\) be {{< knowl id="category" text="categories" >}}.

A {{< knowl id="functor" text="functor" >}} \(F:\mathcal C\to\mathcal D\) is an **equivalence of categories** if there exists a functor \(G:\mathcal D\to\mathcal C\) and {{< knowl id="natural-isomorphism" text="natural isomorphisms" >}}
\[
\eta:\mathrm{Id}_{\mathcal C}\Rightarrow G\circ F,
\qquad
\varepsilon:F\circ G\Rightarrow \mathrm{Id}_{\mathcal D}.
\]
In this case \(G\) is called a **quasi-inverse** (or weak inverse) of \(F\), and we say \(\mathcal C\) and \(\mathcal D\) are **equivalent**.

Equivalently, \(F\) is an equivalence iff:
1. (**Fully faithful**) for all objects \(X,Y\in\mathcal C\), the induced map on hom-sets
   \[
   \mathrm{Hom}_{\mathcal C}(X,Y)\longrightarrow \mathrm{Hom}_{\mathcal D}(F(X),F(Y))
   \]
   is a bijection, and
2. (**Essentially surjective**) every object \(D\in\mathcal D\) is {{< knowl id="isomorphism-category" text="isomorphic" >}} to some \(F(C)\).

(These conditions make precise that \(F\) preserves and reflects all morphism data, and hits every object up to isomorphism.)

## Examples
1. **Finite sets vs. standard finite sets (FinSet)**.  
   Let \(\mathbf{FinSet}\) be the category of finite sets. Let \(\mathbf{FinStd}\) be the full subcategory whose objects are the standard sets
   \([n]=\{1,2,\dots,n\}\) (including \([0]=\varnothing\)).  
   The inclusion \(\mathbf{FinStd}\hookrightarrow \mathbf{FinSet}\) is an equivalence: every finite set is bijective to exactly one \([n]\) up to isomorphism, and morphisms are just set functions.

2. **Finite-dimensional vector spaces vs. matrices**.  
   Let \(\mathbf{FinVect}_k\) be finite-dimensional \(k\)-vector spaces. Let \(\mathbf{Mat}_k\) be the category with:
   - objects natural numbers \(n\),
   - morphisms \(n\to m\) given by \(m\times n\) matrices over \(k\),
   - composition given by matrix multiplication.  
   The functor \(F:\mathbf{Mat}_k\to \mathbf{FinVect}_k\) sending \(n\mapsto k^n\) and a matrix to the corresponding linear map is an equivalence (choosing a basis identifies any finite-dimensional space with some \(k^n\)).

3. **A category is equivalent to its skeleton**.  
   A **skeleton** of \(\mathcal C\) is a full {{< knowl id="full-subcategory" text="full subcategory" >}} containing exactly one object from each isomorphism class of objects in \(\mathcal C\).  
   The inclusion of a skeleton \(\mathrm{Sk}(\mathcal C)\hookrightarrow \mathcal C\) is an equivalence: it is fully faithful (being full) and essentially surjective by construction.
