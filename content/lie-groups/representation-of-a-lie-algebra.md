---
title: "Representation of a Lie Algebra"
description: "A Lie algebra homomorphism from a Lie algebra to endomorphisms of a vector space."
---

Let \(\mathfrak{g}\) be a {{< knowl id="lie-algebra" text="Lie algebra" >}} and let \(V\) be a {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}.
A **representation of \(\mathfrak{g}\)** is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}
$$
\rho:\mathfrak{g}\to \mathfrak{gl}(V),
$$
where \(\mathfrak{gl}(V)\) is the Lie algebra of all {{< knowl id="linear-operator" section="linear-algebra" text="linear operators" >}} on \(V\) with bracket \([A,B]=AB-BA\).

Explicitly, \(\rho\) must satisfy
$$
\rho([X,Y]) = [\rho(X),\rho(Y)] \quad \text{for all } X,Y\in\mathfrak{g}.
$$

## Equivalent “module” viewpoint
Giving \(\rho\) is the same as giving an action \(\mathfrak{g}\times V\to V\), \((X,v)\mapsto X\cdot v\), such that
$$
[X,Y]\cdot v = X\cdot (Y\cdot v) - Y\cdot (X\cdot v).
$$

## Examples
- The **trivial representation**: \(\rho(X)=0\) for all \(X\).
- The {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} \(\operatorname{ad}:\mathfrak{g}\to\mathfrak{gl}(\mathfrak{g})\).
- Any {{< knowl id="representation-of-a-lie-group" text="Lie group representation" >}} \(\rho:G\to \operatorname{GL}(V)\) differentiates to one of \(\mathfrak{g}=T_eG\).

The kernel of a representation is always an {{< knowl id="ideal-of-lie-algebra" text="ideal" >}} of \(\mathfrak{g}\).
