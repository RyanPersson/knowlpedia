---
title: "Composition of morphisms"
description: "The rule that composes morphisms in a category, generalizing function composition."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}}. If
\[
f : X \to Y \quad\text{and}\quad g : Y \to Z
\]
are {{< knowl id="morphism" text="morphisms" >}} in \(\mathcal C\), their **composition** is a morphism
\[
g\circ f : X \to Z.
\]

Composition is required to satisfy:

- **Associativity:** for \(f:W\to X\), \(g:X\to Y\), \(h:Y\to Z\),
  \[
  h\circ(g\circ f) = (h\circ g)\circ f.
  \]
- **Unit laws:** using the {{< knowl id="identity-morphism" text="identity morphisms" >}} \(1_X\),
  \[
  f\circ 1_X = f,\qquad 1_Y\circ f = f
  \]
  whenever \(f:X\to Y\).

This abstracts {{< knowl id="composition" section="shared-foundations" text="composition of functions" >}} in set theory.

## Examples
1. In \(\mathbf{Set}\), if \(f:X\to Y\) and \(g:Y\to Z\) are {{< knowl id="function" section="shared-foundations" text="functions" >}}, then \(g\circ f\) is the usual function composition.
2. In \(\mathbf{Grp}\), composition is composition of group homomorphisms.
3. In \(\mathbf{Top}\), composition is composition of continuous maps.
