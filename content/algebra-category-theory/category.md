---
title: "Category"
description: "A structure of objects and morphisms with associative composition and identity morphisms."
---

A **category** \(\mathcal C\) consists of:

1. A collection \(\mathrm{Ob}(\mathcal C)\) of **{{< knowl id="object" text="objects" >}}**.
2. For each pair \(X,Y \in \mathrm{Ob}(\mathcal C)\), a collection \(\mathrm{Hom}_{\mathcal C}(X,Y)\) of **{{< knowl id="morphism" text="morphisms" >}}** \(X \to Y\).
3. For each triple \(X,Y,Z\), a **{{< knowl id="composition-category" text="composition" >}}** operation
   \[
   \circ : \mathrm{Hom}_{\mathcal C}(Y,Z)\times \mathrm{Hom}_{\mathcal C}(X,Y)\to \mathrm{Hom}_{\mathcal C}(X,Z),
   \quad (g,f)\mapsto g\circ f.
   \]
4. For each object \(X\), an **{{< knowl id="identity-morphism" text="identity morphism" >}}** \(1_X \in \mathrm{Hom}_{\mathcal C}(X,X)\).

These data satisfy the **category axioms** (associativity and identity/unit laws); see {{< knowl id="category-axioms" text="category axioms" >}}.

This abstracts the behavior of {{< knowl id="function" section="shared-foundations" text="functions" >}} and their {{< knowl id="composition" section="shared-foundations" text="composition" >}}.

## Examples
1. **\(\mathbf{Set}\)**: objects are {{< knowl id="set" section="shared-foundations" text="sets" >}}, morphisms are {{< knowl id="function" section="shared-foundations" text="functions" >}}, composition is ordinary function composition, and \(1_X\) is the {{< knowl id="identity-function" section="shared-foundations" text="identity function" >}} on \(X\).
2. **\(\mathbf{Grp}\)**: objects are groups, morphisms are group homomorphisms, with composition given by composing homomorphisms.
3. **\(\mathbf{Top}\)**: objects are topological spaces, morphisms are continuous maps, with composition the usual composition of continuous maps.
