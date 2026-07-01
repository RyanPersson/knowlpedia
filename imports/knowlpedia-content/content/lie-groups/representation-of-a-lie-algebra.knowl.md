+++
id = "lie-groups/representation-of-a-lie-algebra"
title = "Representation of a Lie Algebra"
kind = "knowl"
summary = "A Lie algebra homomorphism from a Lie algebra to endomorphisms of a vector space."
aliases = ["representation-of-a-lie-algebra", "Representation of a Lie Algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/representation-of-a-lie-algebra.md"
+++

Let \(\mathfrak{g}\) be a [[lie-groups/lie-algebra|Lie algebra]] and let \(V\) be a [[linear-algebra/vector-space|vector space]].
A **representation of \(\mathfrak{g}\)** is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]
$$
\rho:\mathfrak{g}\to \mathfrak{gl}(V),
$$
where \(\mathfrak{gl}(V)\) is the Lie algebra of all [[linear-algebra/linear-operator|linear operators]] on \(V\) with bracket \([A,B]=AB-BA\).

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
- The [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] \(\operatorname{ad}:\mathfrak{g}\to\mathfrak{gl}(\mathfrak{g})\).
- Any [[lie-groups/representation-of-a-lie-group|Lie group representation]] \(\rho:G\to \operatorname{GL}(V)\) differentiates to one of \(\mathfrak{g}=T_eG\).

The kernel of a representation is always an [[lie-groups/ideal-of-lie-algebra|ideal]] of \(\mathfrak{g}\).
