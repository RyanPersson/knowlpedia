---
title: "Ideal of a Lie algebra"
description: "A subalgebra closed under bracketing with any element of the ambient algebra."
---

An **ideal** of a {{< knowl id="lie-algebra" text="Lie algebra" >}} \(\mathfrak{g}\) is a {{< knowl id="lie-subalgebra" text="subalgebra" >}} \(\mathfrak{h} \subseteq \mathfrak{g}\) such that
$$
[X, Y] \in \mathfrak{h} \quad \text{for all } X \in \mathfrak{g}, Y \in \mathfrak{h}.
$$

Equivalently, \([\mathfrak{g}, \mathfrak{h}] \subseteq \mathfrak{h}\).

## Properties
- Every ideal is a subalgebra (but not conversely).
- The quotient \(\mathfrak{g}/\mathfrak{h}\) inherits a Lie algebra structure when \(\mathfrak{h}\) is an ideal.
- The kernel of any Lie algebra {{< knowl id="lie-algebra-homomorphism" text="homomorphism" >}} is an ideal.

## Examples
- The center \(Z(\mathfrak{g}) = \{X : [X, Y] = 0 \text{ for all } Y\}\).
- The derived algebra \([\mathfrak{g}, \mathfrak{g}]\).
- \(\{0\}\) and \(\mathfrak{g}\) itself (trivial ideals).

## Simple and semisimple
- A Lie algebra is **simple** if it has no proper nonzero ideals and \(\dim \mathfrak{g} > 1\).
- A Lie algebra is **semisimple** if it has no nonzero abelian ideals.
