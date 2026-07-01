+++
id = "algebra-category-theory/composition-category"
title = "Composition of morphisms"
kind = "knowl"
summary = "The rule that composes morphisms in a category, generalizing function composition."
aliases = ["composition-category", "Composition of morphisms"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/composition-category.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]]. If
\[
f : X \to Y \quad\text{and}\quad g : Y \to Z
\]
are [[algebra-category-theory/morphism|morphisms]] in \(\mathcal C\), their **composition** is a morphism
\[
g\circ f : X \to Z.
\]

Composition is required to satisfy:

- **Associativity:** for \(f:W\to X\), \(g:X\to Y\), \(h:Y\to Z\),
  \[
  h\circ(g\circ f) = (h\circ g)\circ f.
  \]
- **Unit laws:** using the [[algebra-category-theory/identity-morphism|identity morphisms]] \(1_X\),
  \[
  f\circ 1_X = f,\qquad 1_Y\circ f = f
  \]
  whenever \(f:X\to Y\).

This abstracts [[shared-foundations/composition|composition of functions]] in set theory.

## Examples
1. In \(\mathbf{Set}\), if \(f:X\to Y\) and \(g:Y\to Z\) are [[shared-foundations/function|functions]], then \(g\circ f\) is the usual function composition.
2. In \(\mathbf{Grp}\), composition is composition of group homomorphisms.
3. In \(\mathbf{Top}\), composition is composition of continuous maps.
