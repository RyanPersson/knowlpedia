---
title: "Category axioms"
description: "The associativity and identity laws governing composition in a category."
---

A {{< knowl id="category" text="category" >}} \(\mathcal C\) consists of:

- a collection of {{< knowl id="object" text="objects" >}} \(\mathrm{Ob}(\mathcal C)\),
- for each pair \(A,B\in\mathrm{Ob}(\mathcal C)\), a set of {{< knowl id="morphism" text="morphisms" >}} \(\mathrm{Hom}_{\mathcal C}(A,B)\),
- a partially defined {{< knowl id="composition-category" text="composition" >}} operation
  \[
  \circ:\mathrm{Hom}_{\mathcal C}(B,C)\times \mathrm{Hom}_{\mathcal C}(A,B)\to \mathrm{Hom}_{\mathcal C}(A,C),
  \quad (g,f)\mapsto g\circ f,
  \]
- and for each object \(A\), an {{< knowl id="identity-morphism" text="identity morphism" >}} \(\mathrm{id}_A\in \mathrm{Hom}_{\mathcal C}(A,A)\).

The **category axioms** are the following two laws.

## Axioms

1. **Associativity.** For any composable morphisms
   \[
   A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} D
   \]
   one has
   \[
   (h\circ g)\circ f \;=\; h\circ (g\circ f)\in \mathrm{Hom}_{\mathcal C}(A,D).
   \]

2. **Identity laws.** For any morphism \(f:A\to B\),
   \[
   \mathrm{id}_B\circ f = f
   \quad\text{and}\quad
   f\circ \mathrm{id}_A = f.
   \]

These axioms ensure that one can unambiguously write composites like \(h\circ g\circ f\) without parentheses.

## Examples

1. **\(\mathbf{Set}\).** Objects are {{< knowl id="set" section="shared-foundations" text="sets" >}} and morphisms are {{< knowl id="function" section="shared-foundations" text="functions" >}}. Composition is ordinary function composition and identities are {{< knowl id="identity-function" section="shared-foundations" text="identity functions" >}}.

2. **\(\mathbf{Grp}\).** Objects are groups and morphisms are group homomorphisms; composition and identities are the usual ones.

3. **\(R\text{-}\mathbf{Mod}\).** Objects are left \(R\)-modules and morphisms are \(R\)-linear maps; composition and identities are the usual ones.
