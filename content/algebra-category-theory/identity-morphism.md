---
title: "Identity morphism"
description: "A morphism 1_X : X → X acting as a two-sided unit for composition."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}} and let \(X\) be an {{< knowl id="object" text="object" >}} of \(\mathcal C\).
An **identity morphism** on \(X\) is a morphism \(1_X : X \to X\) such that:

- For every morphism \(f : X \to Y\), one has \(f \circ 1_X = f\).
- For every morphism \(g : Y \to X\), one has \(1_X \circ g = g\).

(Here \(\circ\) is {{< knowl id="composition-category" text="composition" >}}.)

**Uniqueness:** If \(e : X \to X\) also satisfies these unit laws, then \(e = 1_X\).

This generalizes the {{< knowl id="identity-function" section="shared-foundations" text="identity function" >}} on a set.

## Examples
1. In \(\mathbf{Set}\), \(1_X\) is the identity function \(x\mapsto x\) on the set \(X\).
2. In \(\mathbf{Grp}\), \(1_G : G\to G\) is the identity group homomorphism.
3. In \(\mathbf{Top}\), \(1_X : X\to X\) is the identity continuous map on a space \(X\).
