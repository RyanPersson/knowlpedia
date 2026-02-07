---
title: "Monomorphism"
description: "A morphism that is left-cancellative under composition."
---

Let \(\mathcal C\) be a {{< knowl id="category" text="category" >}}. A morphism \(f : X \to Y\) is a **monomorphism** (or **mono**) if for every object \(Z\) and all morphisms \(g_1,g_2 : Z \to X\),
\[
f\circ g_1 = f\circ g_2 \quad \Longrightarrow \quad g_1 = g_2,
\]
where \(\circ\) denotes {{< knowl id="composition-category" text="composition" >}}.

Equivalently: \(f\) is mono iff it is **left-cancellative** with respect to composition.

Notes:
- Every {{< knowl id="isomorphism-category" text="isomorphism" >}} is a monomorphism.
- The “dual” notion is {{< knowl id="epimorphism-category" text="epimorphism" >}} (right-cancellative).

## Examples
1. In \(\mathbf{Set}\), monomorphisms are exactly {{< knowl id="injective-function" section="shared-foundations" text="injective functions" >}}.
2. In \(\mathbf{Grp}\), monomorphisms are exactly injective group homomorphisms.
3. In \(R\text{-}\mathbf{Mod}\) (and in \(\mathbf{Ab}\)), monomorphisms are exactly injective module homomorphisms.
