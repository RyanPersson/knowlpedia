+++
id = "lie-groups/highest-weight"
title = "Highest weight"
kind = "knowl"
summary = "A dominant maximal weight that labels irreducible representations of semisimple Lie algebras."
aliases = ["highest-weight", "Highest weight"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/highest-weight.md"
+++

Let $\mathfrak g$ be a complex semisimple [[lie-groups/lie-algebra|Lie algebra]], fix a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] $\mathfrak h\subset \mathfrak g$, and choose a set of positive roots, hence a decomposition into root spaces (see [[lie-groups/root-space-decomposition|root space decomposition]]).

**Definition (Highest-weight vector and highest weight).**
Let $V$ be a finite-dimensional $\mathfrak g$-module. A nonzero vector $v\in V$ is a **highest-weight vector** if

1. $v$ is a weight vector: there exists $\lambda\in \mathfrak h^*$ such that $h\cdot v=\lambda(h)v$ for all $h\in \mathfrak h$ (compare [[lie-groups/weight-of-a-representation|weights]]), and
2. $v$ is killed by the positive root spaces: $\mathfrak n^+\cdot v=0$, where $\mathfrak n^+$ is the sum of [[lie-groups/positive-root|positive]] root spaces.

The corresponding weight $\lambda$ is called a **highest weight** of $V$.

In the finite-dimensional semisimple setting, the weights of $V$ are partially ordered by the positive root cone; a highest weight is maximal in this order, and (for irreducible $V$) it is unique.

**Context.**
The highest weight encodes the representation: irreducible finite-dimensional modules are classified by dominant integral highest weights via the [[lie-groups/highest-weight-theorem|highest-weight theorem]]. The action of the [[lie-groups/weyl-group|Weyl group]] permutes weights, but the highest weight is singled out by the choice of positive roots.
