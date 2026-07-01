+++
id = "algebra-category-theory/identity-morphism"
title = "Identity morphism"
kind = "knowl"
summary = "A morphism 1_X : X → X acting as a two-sided unit for composition."
aliases = ["identity-morphism", "Identity morphism"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/identity-morphism.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] and let \(X\) be an [[algebra-category-theory/object|object]] of \(\mathcal C\).
An **identity morphism** on \(X\) is a morphism \(1_X : X \to X\) such that:

- For every morphism \(f : X \to Y\), one has \(f \circ 1_X = f\).
- For every morphism \(g : Y \to X\), one has \(1_X \circ g = g\).

(Here \(\circ\) is [[algebra-category-theory/composition-category|composition]].)

**Uniqueness:** If \(e : X \to X\) also satisfies these unit laws, then \(e = 1_X\).

This generalizes the [[shared-foundations/identity-function|identity function]] on a set.

## Examples
1. In \(\mathbf{Set}\), \(1_X\) is the identity function \(x\mapsto x\) on the set \(X\).
2. In \(\mathbf{Grp}\), \(1_G : G\to G\) is the identity group homomorphism.
3. In \(\mathbf{Top}\), \(1_X : X\to X\) is the identity continuous map on a space \(X\).
