+++
id = "lie-groups/irreducible-representation-lie-algebra"
title = "Irreducible representation of a Lie algebra"
kind = "knowl"
summary = "A representation with no nontrivial invariant subspaces."
aliases = ["irreducible-representation-lie-algebra", "Irreducible representation of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/irreducible-representation-lie-algebra.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]] and let $\rho:\mathfrak g\to \mathfrak{gl}(V)$ be a [[lie-groups/representation-of-a-lie-algebra|representation]] on a finite-dimensional vector space $V$.

**Definition (Irreducible).**
The representation $(\rho,V)$ is **irreducible** if the only $\mathfrak g$-invariant subspaces of $V$ are $\{0\}$ and $V$. Equivalently, $V$ is a simple $\mathfrak g$-module.

A subspace $W\subseteq V$ is $\mathfrak g$-invariant precisely when $\rho(x)W\subseteq W$ for all $x\in\mathfrak g$; such a $W$ is a [[lie-groups/subrepresentation-lie-algebra|subrepresentation]].

**Context.**
Irreducibles are the building blocks for representation theory. For semisimple $\mathfrak g$, every finite-dimensional representation is completely reducible (see [[lie-groups/weyls-theorem-complete-reducibility|Weyl's theorem]] and [[lie-groups/completely-reducible-representation-lie|complete reducibility]]), and irreducibles are classified by the [[lie-groups/highest-weight-theorem|highest-weight theorem]].
