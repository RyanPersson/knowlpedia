---
title: "Endomorphism"
description: "A morphism whose domain and codomain are the same object."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and let \(A\) be an {{< knowl id="object" text="object" >}} of \(\mathcal C\).

An **endomorphism** of \(A\) is a {{< knowl id="morphism" text="morphism" >}}
\[
f:A\longrightarrow A.
\]
The set of endomorphisms of \(A\) is denoted
\[
\mathrm{End}_{\mathcal C}(A)\;:=\;\mathrm{Hom}_{\mathcal C}(A,A).
\]

## Algebraic structure
With {{< knowl id="composition-category" text="composition" >}} as multiplication,
\[
(f,g)\mapsto f\circ g,
\]
the set \(\mathrm{End}_{\mathcal C}(A)\) is a monoid with identity element the {{< knowl id="identity-morphism" text="identity morphism" >}} \(\mathrm{id}_A\).

An endomorphism is an {{< knowl id="automorphism-category" text="automorphism" >}} precisely when it is invertible (i.e., an {{< knowl id="isomorphism-category" text="isomorphism" >}} \(A\to A\)).

## Examples
1. **\(\mathbf{Set}\):** Endomorphisms of a set \(X\) are just {{< knowl id="function" section="shared-foundations" text="functions" >}} \(X\to X\).

2. **\(\mathbf{Grp}\) / \(\mathbf{Ab}\):** Endomorphisms of a group (or abelian group) \(G\) are group homomorphisms \(G\to G\).  
   For example, \(n\mapsto kn\) defines an endomorphism of \(\mathbb Z\) for each integer \(k\).

3. **\(R\mathbf{-Mod}\):** Endomorphisms of an \(R\)-module \(M\) are \(R\)-linear maps \(M\to M\).  
   For a free module \(R^n\), \(\mathrm{End}_R(R^n)\) can be identified with the ring of \(n\times n\) matrices over \(R\) (via the action on the standard basis).
