---
title: "Automorphism"
description: "An isomorphism from an object to itself; an invertible endomorphism."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and \(A\) an {{< knowl id="object" text="object" >}} of \(\mathcal C\).

An **automorphism** of \(A\) is an {{< knowl id="isomorphism-category" text="isomorphism" >}}
\[
f:A\longrightarrow A.
\]
Equivalently, it is an {{< knowl id="endomorphism-category" text="endomorphism" >}} \(f:A\to A\) for which there exists \(g:A\to A\) such that
\[
g\circ f = \mathrm{id}_A,\qquad f\circ g = \mathrm{id}_A,
\]
where \(\mathrm{id}_A\) is the {{< knowl id="identity-morphism" text="identity morphism" >}}.

The set of automorphisms of \(A\) is denoted \(\mathrm{Aut}_{\mathcal C}(A)\).

## Group structure
With {{< knowl id="composition-category" text="composition" >}} as the operation, \(\mathrm{Aut}_{\mathcal C}(A)\) is a group:
- identity element: \(\mathrm{id}_A\),
- inverse: \(f^{-1}\) (the inverse isomorphism).

## Examples
1. **\(\mathbf{Set}\):** Automorphisms of a set \(X\) are exactly the {{< knowl id="bijective-function" section="shared-foundations" text="bijections" >}} \(X\to X\).  
   Thus \(\mathrm{Aut}_{\mathbf{Set}}(X)\) is the permutation group of \(X\).

2. **\(\mathbf{Grp}\):** Automorphisms of a group \(G\) are group isomorphisms \(G\to G\).  
   Example: \(\mathrm{Aut}_{\mathbf{Grp}}(\mathbb Z)\cong\{\pm 1\}\), since any automorphism is determined by where it sends \(1\).

3. **\(R\mathbf{-Mod}\):** Automorphisms of an \(R\)-module \(M\) are the invertible \(R\)-linear maps \(M\to M\).  
   For \(M=R^n\), \(\mathrm{Aut}_R(R^n)\) identifies with the group \(\mathrm{GL}_n(R)\) of invertible \(n\times n\) matrices over \(R\).
