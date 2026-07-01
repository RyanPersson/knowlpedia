+++
id = "algebra-category-theory/category"
title = "Category"
kind = "knowl"
summary = "A structure of objects and morphisms with associative composition and identity morphisms."
aliases = ["category"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/category.md"
+++

A **category** \(\mathcal C\) consists of:

1. A collection \(\mathrm{Ob}(\mathcal C)\) of **[[algebra-category-theory/object|objects]]**.
2. For each pair \(X,Y \in \mathrm{Ob}(\mathcal C)\), a collection \(\mathrm{Hom}_{\mathcal C}(X,Y)\) of **[[algebra-category-theory/morphism|morphisms]]** \(X \to Y\).
3. For each triple \(X,Y,Z\), a **[[algebra-category-theory/composition-category|composition]]** operation
   \[
   \circ : \mathrm{Hom}_{\mathcal C}(Y,Z)\times \mathrm{Hom}_{\mathcal C}(X,Y)\to \mathrm{Hom}_{\mathcal C}(X,Z),
   \quad (g,f)\mapsto g\circ f.
   \]
4. For each object \(X\), an **[[algebra-category-theory/identity-morphism|identity morphism]]** \(1_X \in \mathrm{Hom}_{\mathcal C}(X,X)\).

These data satisfy the **category axioms** (associativity and identity/unit laws); see [[algebra-category-theory/category-axioms|category axioms]].

This abstracts the behavior of [[shared-foundations/function|functions]] and their [[shared-foundations/composition|composition]].

## Examples
1. **\(\mathbf{Set}\)**: objects are [[shared-foundations/set|sets]], morphisms are [[shared-foundations/function|functions]], composition is ordinary function composition, and \(1_X\) is the [[shared-foundations/identity-function|identity function]] on \(X\).
2. **\(\mathbf{Grp}\)**: objects are groups, morphisms are group homomorphisms, with composition given by composing homomorphisms.
3. **\(\mathbf{Top}\)**: objects are topological spaces, morphisms are continuous maps, with composition the usual composition of continuous maps.
