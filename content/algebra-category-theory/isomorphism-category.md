---
title: "Isomorphism"
description: "A morphism that has a two-sided inverse in a category."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}}. A morphism \(f : X \to Y\) is an **isomorphism** if there exists a morphism \(g : Y \to X\) such that
\[
g\circ f = 1_X
\quad\text{and}\quad
f\circ g = 1_Y,
\]
where \(1_X\) and \(1_Y\) are the {{< knowl id="identity-morphism" text="identity morphisms" >}} and \(\circ\) is {{< knowl id="composition-category" text="composition" >}}.

The morphism \(g\) is unique if it exists, and is denoted \(f^{-1}\). In this case, \(X\) and \(Y\) are said to be **isomorphic** (in \(\mathcal C\)).

Related notions:
- An isomorphism \(X\to X\) is an {{< knowl id="automorphism-category" text="automorphism" >}}.
- Every isomorphism is both a {{< knowl id="monomorphism-category" text="monomorphism" >}} and an {{< knowl id="epimorphism-category" text="epimorphism" >}}.

## Examples
1. In \(\mathbf{Set}\), the isomorphisms are exactly the {{< knowl id="bijective-function" section="shared-foundations" text="bijective functions" >}}.
2. In \(\mathbf{Grp}\), the isomorphisms are exactly group isomorphisms (bijective homomorphisms).
3. In \(R\text{-}\mathbf{Mod}\), the isomorphisms are exactly \(R\)-linear maps with \(R\)-linear inverses (invertible module homomorphisms).
